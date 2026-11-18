import { OfflineDecoder, type OfflineRecognizer } from "./decoder";
import workletUrl from "./capture.worklet.ts?worker&url";
import { loadVoiceModel } from "./model-cache";
import { resumeVoiceAudio } from "./audio-activation.mjs";
import { primeRecognizer, WARMUP_SAMPLES } from "./decoder-warmup.mjs";
import { CAPTURE_MAX_PENDING } from "./capture-policy";
import {
  matchFinalWords,
  type FinalWord,
} from "../../../shared/voice/final-matcher.mjs";
import type { VoiceSnapshot } from "../../../shared/voice/protocol.mjs";

type Callbacks = {
  sessionId: string;
  onDetection(value: Record<string, unknown>): void;
  onFeedback(value: Record<string, unknown>): void;
  onClock(sample: number): void;
  onError(text: string): void;
  onStatus(stage: "model" | "audio", text: string): void;
};
type Pcm = { generation: number; sample: number; data: Float32Array };

/** Grammar size cap (a stage vocabulary is a few hundred forms). */
const GRAMMAR_LIMIT = 4000;
/** Overloads recovered by a fresh recognizer before the session gives up. */
const OVERLOAD_LIMIT = 3;
const OVERLOAD_WINDOW_MS = 20000;
const OVERLOAD_MESSAGE =
  "Offline speech processing overloaded. Close heavy game tabs, then reconnect.";

/** Vosk owns its WASM Worker; the Portal only transports bounded capture blocks. */
export class BrowserVoiceRuntime {
  readonly engineId = "vosk-browser-0.0.8-memoryfs-v1-asr";
  readonly modelId = "vosk-small-en-us-0.15-space-endpoint-v1";
  readonly sampleRate = 16000;
  private clock = 0;
  private generation = 0;
  private enabled = false;
  private closed = false;
  private failed = false;
  private resumeTask: Promise<void> | null = null;
  private recognizer: OfflineRecognizer | null = null;
  private recognizerPreparation: AbortController | null = null;
  private baseSample: number | null = null;
  private pending: Pcm[] = [];
  private snapshots: VoiceSnapshot[] = [];
  private context: VoiceSnapshot | null = null;
  private sequence = 0;
  private modelRelease: (() => void) | null = null;
  private trackEnded: (() => void) | null = null;
  private vocabulary = new Set<string>();
  /**
   * Spoken forms the recognizer listens for: the stage vocabulary checked by
   * the game plus every supported on-screen target. Recognizing only these
   * keeps Vosk well under real time (measured: p95 98 ms per 100 ms block
   * against 214 ms, worst 209 ms against 951 ms with the open vocabulary).
   */
  private grammar = new Set<string>();
  private grammarRestart: Promise<void> | null = null;
  /** Grammar grew while a rebuild ran, or while the player was mid-word. */
  private grammarDirty = false;
  /** The latest partial result had words (an utterance is in progress). */
  private speaking = false;
  /** The host wants audio decoded (between its resume and suspend). */
  private wanted = false;
  private overloads: number[] = [];
  private constructor(
    private model: OfflineDecoder,
    private audio: AudioContext,
    private capture: AudioWorkletNode,
    private source: MediaStreamAudioSourceNode,
    private mute: GainNode,
    private callbacks: Callbacks,
  ) {}

  static async create(
    stream: MediaStream,
    callbacks: Callbacks,
    signal?: AbortSignal,
  ): Promise<BrowserVoiceRuntime> {
    const cached = await loadVoiceModel(
      (text) => callbacks.onStatus("model", text),
      signal,
    );
    let model: OfflineDecoder | null = null,
      audio: AudioContext | null = null;
    try {
      signal?.throwIfAborted();
      callbacks.onStatus("model", "Starting offline speech recognizer…");
      model = new OfflineDecoder(cached.url);
      const loading = model;
      await new Promise<void>((resolve, reject) => {
        const timer = setTimeout(
          () => reject(new Error("Offline recognizer preparation timed out.")),
          60000,
        );
        signal?.addEventListener(
          "abort",
          () => {
            clearTimeout(timer);
            reject(signal.reason);
          },
          { once: true },
        );
        loading.worker.addEventListener(
          "error",
          () => {
            clearTimeout(timer);
            reject(new Error("Offline speech worker failed to start."));
          },
          { once: true },
        );
        loading.on("load", (message) => {
          clearTimeout(timer);
          "result" in message && message.result
            ? resolve()
            : reject(new Error("Unable to load offline model."));
        });
        loading.on("error", (message) => {
          clearTimeout(timer);
          reject(
            new Error(
              String(
                (message as { error?: string }).error ?? "Recognizer error",
              ),
            ),
          );
        });
      });
      signal?.throwIfAborted();
      callbacks.onStatus("audio", "Starting microphone audio capture…");
      audio = new AudioContext();
      await audio.audioWorklet.addModule(workletUrl);
      signal?.throwIfAborted();
      const capture = new AudioWorkletNode(audio, "typing-voice-capture", {
        numberOfInputs: 1,
        numberOfOutputs: 1,
        outputChannelCount: [1],
      });
      const source = audio.createMediaStreamSource(stream);
      const mute = audio.createGain();
      mute.gain.value = 0;
      source.connect(capture);
      capture.connect(mute);
      mute.connect(audio.destination);
      await resumeVoiceAudio(audio, signal);
      signal?.throwIfAborted();
      const runtime = new BrowserVoiceRuntime(
        model,
        audio,
        capture,
        source,
        mute,
        callbacks,
      );
      runtime.modelRelease = cached.release;
      runtime.vocabulary = cached.vocabulary;
      capture.port.onmessage = ({ data }) => runtime.captureMessage(data);
      model.on("error", () =>
        runtime.fail("Speech engine error. Reconnect the microphone."),
      );
      const worker = model.worker;
      worker.addEventListener("error", () =>
        runtime.fail("Speech worker stopped. Reconnect the microphone."),
      );
      runtime.trackEnded = () =>
        runtime.fail("Microphone disconnected. Reconnect to continue.");
      stream
        .getAudioTracks()
        .forEach((track) =>
          track.addEventListener("ended", runtime.trackEnded!),
        );
      runtime.tracks = stream.getAudioTracks();
      return runtime;
    } catch (error) {
      model?.terminate();
      await audio?.close();
      cached.release();
      throw error;
    }
  }
  private tracks: MediaStreamTrack[] = [];
  nowSample(): number {
    return this.clock;
  }
  private fail(text: string): void {
    if (this.closed || this.failed) return;
    this.failed = true;
    void this.suspend();
    this.callbacks.onError(text);
  }
  /**
   * Decoding fell behind: drop the backlog (that utterance) and continue with
   * a fresh recognizer. Only repeated overloads end the session.
   */
  private overloaded(): void {
    const now = performance.now();
    this.overloads = this.overloads.filter((at) => now - at < OVERLOAD_WINDOW_MS);
    this.overloads.push(now);
    if (this.overloads.length > OVERLOAD_LIMIT) {
      this.fail(OVERLOAD_MESSAGE);
      return;
    }
    void this.restartRecognizer().catch(() => this.fail(OVERLOAD_MESSAGE));
  }
  /** Halts decoding now (synchronously) and, if still wanted, prepares a new recognizer. */
  private async restartRecognizer(): Promise<void> {
    if (this.closed || this.failed) return;
    await this.halt();
    if (!this.wanted || this.closed || this.failed) return;
    await this.startDecoding();
  }
  /** Adds supported spoken forms to the grammar; a live recognizer is rebuilt to hear them. */
  addGrammarForms(forms: readonly string[]): void {
    let added = false;
    for (const form of forms) {
      if (this.grammar.size >= GRAMMAR_LIMIT) break;
      if (this.grammar.has(form) || this.unsupportedForms([form]).length > 0) continue;
      this.grammar.add(form);
      added = true;
    }
    if (added && this.enabled) this.scheduleGrammarRestart();
  }
  /**
   * One rebuild for every form added in this turn. Never cuts a word the
   * player is saying: mid-utterance it waits for that utterance's result.
   */
  private scheduleGrammarRestart(): void {
    if (this.grammarRestart || this.speaking) {
      this.grammarDirty = true;
      return;
    }
    this.grammarDirty = false;
    const restart = Promise.resolve()
      .then(() => this.restartRecognizer())
      .catch(() => this.fail("Speech recognizer could not reload its vocabulary."))
      .finally(() => {
        if (this.grammarRestart === restart) this.grammarRestart = null;
        if (this.grammarDirty && this.enabled) this.scheduleGrammarRestart();
      });
    this.grammarRestart = restart;
  }
  private captureMessage(message: {
    type: string;
    sample?: number;
    generation?: number;
    data?: Float32Array;
  }): void {
    if (this.closed) return;
    if (Number.isSafeInteger(message.sample))
      this.clock = Math.max(this.clock, message.sample!);
    this.callbacks.onClock(this.clock);
    if (message.type === "overflow") {
      if (message.generation === this.generation && this.enabled) this.overloaded();
      return;
    }
    if (
      message.type !== "pcm" ||
      !this.enabled ||
      message.generation !== this.generation ||
      !message.data ||
      !this.recognizer
    )
      return;
    if (this.pending.length >= CAPTURE_MAX_PENDING) {
      this.overloaded();
      return;
    }
    this.baseSample ??= this.clock - message.data.length - WARMUP_SAMPLES;
    this.pending.push(message as Pcm);
    this.recognizer.acceptWaveformFloat(message.data, this.sampleRate);
  }
  private acknowledge(generation: number): void {
    if (this.closed || generation !== this.generation) return;
    if (this.pending.shift())
      this.capture.port.postMessage({ type: "credit", generation });
  }
  private final(
    result: { text?: string; result?: FinalWord[] },
    generation: number,
  ): void {
    this.acknowledge(generation);
    if (
      !this.enabled ||
      generation !== this.generation ||
      !this.context ||
      this.baseSample === null
    )
      return;
    // Calibration is never user evidence, including a word crossing the gate.
    // "[unk]" is the grammar's catch-all for speech outside the target words.
    const words = (result.result ?? []).filter(word =>
      word.word !== "[unk]" && Number.isFinite(word.start) && word.start * this.sampleRate >= WARMUP_SAMPLES);
    const transcript = words.map(word => word.word).join(" ").trim().slice(0, 200);
    // Empty Vosk endpoints without timestamped lexical evidence are silence, not a failed attempt.
    if (!words.length || !transcript) return;
    const context = this.context;
    const matches = matchFinalWords(
      words,
      this.snapshots,
      this.baseSample,
      this.sampleRate,
    );
    let detectionId: string | undefined;
    for (const match of matches) {
      if (match.audioEndSample > this.clock) continue;
      detectionId = `${this.callbacks.sessionId}:${++this.sequence}`;
      this.callbacks.onDetection({
        ...context,
        ...match.target,
        streamEpoch: generation,
        evidence: "final-utterance",
        detectionId,
        snapshotId: match.snapshotId,
        form: match.form,
        audioStartSample: match.audioStartSample,
        audioEndSample: match.audioEndSample,
        engineId: this.engineId,
        modelId: this.modelId,
        emittedAtMs: performance.timeOrigin + performance.now(),
      });
    }
    const start =
      this.baseSample + Math.floor(words[0].start * this.sampleRate);
    const end =
      this.baseSample + Math.ceil(words.at(-1)!.end * this.sampleRate);
    if (
      !Number.isSafeInteger(start) ||
      start < 0 ||
      !Number.isSafeInteger(end) ||
      end <= start ||
      end > this.clock
    )
      return;
    this.callbacks.onFeedback({
      sessionId: context.sessionId,
      inputEpoch: context.inputEpoch,
      audioEpoch: context.audioEpoch,
      streamEpoch: generation,
      feedbackId: `${this.callbacks.sessionId}:feedback:${++this.sequence}`,
      result: "recognized",
      evidence: "final-utterance",
      transcript,
      ...(detectionId ? { detectionId } : {}),
      audioStartSample: start,
      audioEndSample: end,
      engineId: this.engineId,
      modelId: this.modelId,
      emittedAtMs: performance.timeOrigin + performance.now(),
    });
  }
  async applyTargets(
    snapshot: VoiceSnapshot,
  ): Promise<{ ready: string[]; unsupported: string[] }> {
    if (this.closed) throw new Error("Voice runtime closed");
    this.context = snapshot;
    const stamped = { ...snapshot, publishedAtSample: this.clock };
    this.snapshots.push(stamped);
    while (
      this.snapshots.length > 1 &&
      this.snapshots[1].publishedAtSample < this.clock - 10 * this.sampleRate
    )
      this.snapshots.shift();
    if (this.snapshots.length > 512)
      throw new Error("Voice target history overflow");
    const supports = (forms: string[]) =>
      this.unsupportedForms(forms).length === 0;
    this.addGrammarForms(snapshot.targets.filter((t) => supports(t.forms)).flatMap((t) => t.forms));
    return {
      ready: snapshot.targets
        .filter((t) => supports(t.forms))
        .map((t) => t.unitId),
      unsupported: snapshot.targets
        .filter((t) => !supports(t.forms))
        .map((t) => t.unitId),
    };
  }
  unsupportedForms(forms: string[]): string[] {
    return forms.filter(
      (form) =>
        !/^[a-z]+(?:[ '\-][a-z]+)*$/.test(form) ||
        form.split(" ").some((word) => !this.vocabulary.has(word)),
    );
  }
  async suspend(): Promise<void> {
    this.wanted = false;
    await this.halt();
  }
  /** Stops decoding without changing what the host asked for. */
  private async halt(): Promise<void> {
    this.enabled = false;
    this.speaking = false;
    this.resumeTask = null;
    this.generation++;
    this.recognizerPreparation?.abort();
    this.recognizerPreparation = null;
    this.capture.port.postMessage({
      type: "gate",
      enabled: false,
      generation: this.generation,
    });
    this.recognizer?.remove();
    this.recognizer = null;
    this.pending = [];
    this.baseSample = null;
  }
  async flush(): Promise<void> {
    await this.suspend();
    this.snapshots = [];
    this.context = null;
  }
  resume(): Promise<void> {
    this.wanted = true;
    return this.startDecoding();
  }
  private startDecoding(): Promise<void> {
    if (this.closed || this.failed || this.enabled) return Promise.resolve();
    if (this.resumeTask) return this.resumeTask;
    const task = this.prepareAndResume();
    this.resumeTask = task;
    void task.finally(() => {
      if (this.resumeTask === task) this.resumeTask = null;
    }).catch(() => {});
    return task;
  }
  private async prepareAndResume(): Promise<void> {
    const generation = ++this.generation;
    const grammarSize = this.grammar.size;
    this.grammarDirty = false;
    const recognizer = this.model.createRecognizer(
      this.sampleRate,
      grammarSize > 0 ? [...this.grammar] : undefined,
    );
    this.recognizer = recognizer;
    const preparation = new AbortController();
    this.recognizerPreparation = preparation;
    try {
      await primeRecognizer(recognizer, preparation.signal);
    } catch (error) {
      if (this.closed || generation !== this.generation) return;
      await this.suspend();
      throw error;
    } finally {
      if (this.recognizerPreparation === preparation) this.recognizerPreparation = null;
    }
    if (this.closed || generation !== this.generation) return;
    recognizer.on("error", (message) =>
      { if (generation === this.generation) this.fail(message.error ?? "Speech recognizer stopped"); },
    );
    recognizer.setWords(true);
    recognizer.on("partialresult", (message) => {
      if (generation === this.generation)
        this.speaking = Boolean((message.result as { partial?: string } | undefined)?.partial);
      this.acknowledge(generation);
    });
    recognizer.on("result", (message) => {
      this.final(
        ("result" in message ? message.result : {}) as {
          text?: string;
          result?: FinalWord[];
        },
        generation,
      );
      if (generation !== this.generation) return;
      this.speaking = false;
      // A grammar rebuild that waited for this utterance runs now.
      if (this.grammarDirty && this.enabled) this.scheduleGrammarRestart();
    });
    if (this.closed || generation !== this.generation) return;
    this.enabled = true;
    this.capture.port.postMessage({ type: "gate", enabled: true, generation });
    // Words that arrived while this recognizer was warming up need a rebuild.
    if (this.grammar.size !== grammarSize) this.scheduleGrammarRestart();
  }
  async close(): Promise<void> {
    if (this.closed) return;
    this.closed = true;
    await this.suspend();
    if (this.trackEnded)
      this.tracks.forEach((track) =>
        track.removeEventListener("ended", this.trackEnded!),
      );
    this.capture.port.close();
    this.source.disconnect();
    this.capture.disconnect();
    this.mute.disconnect();
    this.model.terminate();
    await this.audio.close();
    this.modelRelease?.();
    this.snapshots = [];
  }
}
