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
      if (message.generation === this.generation)
        this.fail("Offline speech processing overloaded. Close heavy game tabs, then reconnect.");
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
      this.fail("Offline speech processing overloaded. Close heavy game tabs, then reconnect.");
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
    const words = (result.result ?? []).filter(word =>
      Number.isFinite(word.start) && word.start * this.sampleRate >= WARMUP_SAMPLES);
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
    this.enabled = false;
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
    const recognizer = this.model.createRecognizer(this.sampleRate);
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
    recognizer.on("partialresult", () => this.acknowledge(generation));
    recognizer.on("result", (message) =>
      this.final(
        ("result" in message ? message.result : {}) as {
          text?: string;
          result?: FinalWord[];
        },
        generation,
      ),
    );
    if (this.closed || generation !== this.generation) return;
    this.enabled = true;
    this.capture.port.postMessage({ type: "gate", enabled: true, generation });
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
