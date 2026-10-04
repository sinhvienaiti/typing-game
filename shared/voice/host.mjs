import { parseSnapshot, parseDetection, parseFeedback } from "./protocol.mjs";

/** Injected local capture/decoder only. There is deliberately no browser SpeechRecognition fallback. */
export class VoiceHost {
  constructor({ requestMicrophone, createRuntime, createSessionId, cancelMicrophone = () => {}, onEvent = () => {}, waitTail = (ms) => new Promise((r) => setTimeout(r, ms)), echoTailMs = 300 }) {
    if (![requestMicrophone, createRuntime, createSessionId, cancelMicrophone, onEvent, waitTail].every((f) => typeof f === "function") || !Number.isFinite(echoTailMs) || echoTailMs < 0) throw new TypeError("invalid local host dependencies");
    Object.assign(this, { requestMicrophone, createRuntime, createSessionId, cancelMicrophone, onEvent, waitTail, echoTailMs });
    this.state = "IDLE"; this.generation = 0; this.session = null; this.runtime = null; this.stream = null;
    this.applyQueue = Promise.resolve(); this.pendingTargets = 0; this.outputGeneration = 0; this.outputClosedGeneration = 0; this.outputActive = false; this.resuming = false;
  }
  current(generation) { return generation === this.generation; }
  emit(event) { this.onEvent(event); }
  runtimeError(message, generation) {
    if (!this.current(generation) || !this.session) return false;
    const runtime = this.runtime, stream = this.stream;
    // Invalidate callbacks before teardown; even a hung decoder cannot hold the mic.
    ++this.generation;
    this.session = null; this.runtime = null; this.stream = null; this.state = "ERROR";
    this.cancelMicrophone();
    void this.dispose(runtime, stream).catch(() => {});
    this.emit({ type: "error", code: "microphone-runtime-failed", message: String(message).slice(0, 300) });
    return true;
  }
  stopTracks(stream) { for (const track of stream?.getTracks() ?? []) track.stop(); }
  async dispose(runtime, stream) {
    // Release the device before waiting for decoder teardown; a stuck worker must not keep the mic live.
    this.stopTracks(stream); await runtime?.close();
  }
  async stop() {
    const generation = ++this.generation;
    const runtime = this.runtime, stream = this.stream, session = this.session;
    // Invalidate synchronously, before teardown can yield to late permission/results.
    this.session = null; this.runtime = null; this.stream = null; this.state = "STOPPING";
    this.cancelMicrophone();
    try { await this.dispose(runtime, stream); }
    finally {
      if (this.current(generation)) { this.state = "IDLE"; if (session) this.emit({ type: "stopped", ...session }); }
    }
  }
  async start(inputEpoch) {
    if (!Number.isSafeInteger(inputEpoch) || inputEpoch < 0) throw new TypeError("invalid input epoch");
    const generation = ++this.generation;
    const previousRuntime = this.runtime, previousStream = this.stream;
    this.session = null; this.runtime = null; this.stream = null; this.state = "STOPPING";
    this.cancelMicrophone();
    await this.dispose(previousRuntime, previousStream);
    if (!this.current(generation)) return false;
    const sessionId = this.createSessionId();
    this.session = { sessionId, inputEpoch, audioEpoch: 0 };
    this.outputGeneration = 0; this.outputClosedGeneration = 0; this.outputActive = false; this.applyQueue = Promise.resolve(); this.resuming = false;
    this.state = "REQUESTING_PERMISSION";
    this.emit({ type: "preparing", inputEpoch, stage: "permission", message: "Waiting for microphone permission…" });
    let stream = null, runtime = null;
    try {
      stream = await this.requestMicrophone();
      if (!this.current(generation)) { this.stopTracks(stream); return false; }
      this.stream = stream; this.state = "PREPARING";
      runtime = await this.createRuntime(stream, { sessionId, onError: (message) => this.runtimeError(message, generation), onStatus: (stage, message) => { if (this.current(generation) && this.state === "PREPARING") this.emit({ type: "preparing", inputEpoch, stage, message }); }, onDetection: (d) => this.receiveDetection(d, generation), onFeedback: (f) => this.receiveFeedback(f, generation), onClock: (sample) => { if (this.current(generation) && this.session && this.runtime && Number.isSafeInteger(sample) && sample >= 0) this.emit({ type: "clock", ...this.session, sample }); } });
      if (!this.current(generation)) { await this.dispose(runtime, stream); return false; }
      // Capture owns a monotonic sample clock even when inference is suspended.
      parseSnapshot({ ...this.session, snapshotId: "ready", registryRevision: 0, publishedAtSample: runtime.nowSample(), sampleRate: runtime.sampleRate, targets: [] });
      if (!runtime.engineId || !runtime.modelId) throw new TypeError("missing verified engine/model identity");
      this.runtime = runtime;
      await runtime.suspend();
      if (!this.current(generation)) return false;
      this.state = "READY"; this.emitReady(); return true;
    } catch (error) {
      if (this.current(generation)) {
        this.runtime = null; this.stream = null; this.session = null; this.state = "ERROR";
        await this.dispose(runtime, stream);
        if (this.current(generation)) this.emit({ type: "error", code: "local-runtime-failed", message: String(error).slice(0, 300) });
      }
      return false;
    }
  }
  emitReady() {
    this.emit({ type: "ready", ...this.session, engineId: this.runtime.engineId, modelId: this.runtime.modelId, sampleRate: this.runtime.sampleRate, fromSample: this.runtime.nowSample() });
  }
  checkVocabulary(value) {
    const s = this.session;
    if (!s || !this.runtime || !["READY", "LISTENING", "SUSPENDED"].includes(this.state) || value.sessionId !== s.sessionId || value.inputEpoch !== s.inputEpoch || value.audioEpoch !== s.audioEpoch) return false;
    const unsupported = this.runtime.unsupportedForms?.(value.forms) ?? value.forms;
    this.emit({ type: "vocabulary-checked", ...s, requestId: value.requestId, unsupported }); return true;
  }
  receiveDetection(value, generation) {
    if (!this.current(generation) || this.state !== "LISTENING" || !this.session) return false;
    const detection = parseDetection(value), s = this.session;
    if (detection.sessionId !== s.sessionId || detection.inputEpoch !== s.inputEpoch || detection.audioEpoch !== s.audioEpoch || detection.engineId !== this.runtime.engineId || detection.modelId !== this.runtime.modelId || detection.audioEndSample > this.runtime.nowSample()) return false;
    this.emit({ type: "detection", ...detection }); return true;
  }
  receiveFeedback(value, generation) {
    if (!this.current(generation) || this.state !== "LISTENING" || !this.session) return false;
    let feedback; try { feedback = parseFeedback(value); } catch { return false; }
    const s = this.session;
    if (feedback.sessionId !== s.sessionId || feedback.inputEpoch !== s.inputEpoch || feedback.audioEpoch !== s.audioEpoch || feedback.engineId !== this.runtime.engineId || feedback.modelId !== this.runtime.modelId || feedback.audioEndSample > this.runtime.nowSample()) return false;
    this.emit({ type: "feedback", ...feedback }); return true;
  }
  applyTargets(value) {
    const snapshot = parseSnapshot(value), generation = this.generation;
    if (this.pendingTargets >= 4) return Promise.reject(new Error("target-update-backpressure"));
    this.pendingTargets++;
    const apply = async () => {
      const s = this.session;
      if (!this.current(generation) || !s || !["READY", "LISTENING"].includes(this.state) || snapshot.sessionId !== s.sessionId || snapshot.inputEpoch !== s.inputEpoch || snapshot.audioEpoch !== s.audioEpoch || snapshot.sampleRate !== this.runtime.sampleRate || snapshot.publishedAtSample > this.runtime.nowSample()) return false;
      const runtime = this.runtime;
      const { ready, unsupported } = await runtime.applyTargets(snapshot);
      if (!this.current(generation) || !["READY", "LISTENING"].includes(this.state) || this.session.inputEpoch !== snapshot.inputEpoch || this.session.audioEpoch !== snapshot.audioEpoch) return false;
      const ids = new Set(snapshot.targets.map((t) => t.unitId)), classified = [...ready, ...unsupported];
      if (classified.length !== ids.size || new Set(classified).size !== classified.length || classified.some((id) => !ids.has(id))) throw new TypeError("incomplete/duplicate target capability ACK");
      const appliedAtSample = runtime.nowSample();
      this.emit({ type: "targets-applied", ...s, snapshotId: snapshot.snapshotId, ready, unsupported, appliedAtSample });
      if (this.state === "READY") {
        await runtime.resume();
        if (!this.current(generation) || this.state !== "READY" || this.session.inputEpoch !== s.inputEpoch || this.session.audioEpoch !== s.audioEpoch) return false;
        this.state = "LISTENING";
        this.emit({ type: this.resuming ? "listening-resumed" : "listening", ...s, fromSample: runtime.nowSample() });
        this.resuming = false;
      }
      return true;
    };
    const task = this.applyQueue.then(apply).finally(() => { this.pendingTargets--; });
    // A failed compile does not poison the queue, nor silently make targets ready.
    this.applyQueue = task.catch(() => {}); return task;
  }
  async suspend(inputEpoch) {
    if (!this.session || !Number.isSafeInteger(inputEpoch) || inputEpoch < this.session.inputEpoch) return false;
    const generation = this.generation, runtime = this.runtime;
    this.session = { ...this.session, inputEpoch }; this.state = "SUSPENDED";
    await runtime?.suspend(); return this.current(generation);
  }
  async resume(inputEpoch) {
    if (!this.session || this.outputActive || this.state !== "SUSPENDED" || !Number.isSafeInteger(inputEpoch) || inputEpoch < this.session.inputEpoch) return false;
    const generation = this.generation, runtime = this.runtime;
    const inputSession = { ...this.session, inputEpoch };
    this.session = inputSession;
    await runtime.flush();
    if (!this.current(generation) || this.session !== inputSession || this.state !== "SUSPENDED") return false;
    this.session = { ...inputSession, audioEpoch: inputSession.audioEpoch + 1 };
    this.state = "READY"; this.resuming = true; this.emitReady(); return true;
  }
  async audioOutputIntent(generation) {
    if (!this.session || !Number.isSafeInteger(generation) || generation <= this.outputGeneration || !["READY", "LISTENING", "SUSPENDED"].includes(this.state)) return false;
    this.outputGeneration = generation;
    this.outputClosedGeneration = 0; this.outputActive = true;
    const hostGeneration = this.generation;
    await this.suspend(this.session.inputEpoch);
    if (!this.current(hostGeneration) || generation !== this.outputGeneration || !this.session) return false;
    this.outputClosedGeneration = generation;
    this.emit({ type: "gate-closed", ...this.session, generation, fromSample: this.runtime.nowSample() }); return true;
  }
  async audioOutputEnded(generation) {
    if (!this.session || !this.outputActive || !Number.isSafeInteger(generation) || generation < 1 || generation !== this.outputGeneration || generation !== this.outputClosedGeneration || this.state !== "SUSPENDED") return false;
    const hostGeneration = this.generation, session = this.session;
    await this.waitTail(this.echoTailMs);
    if (!this.current(hostGeneration) || !this.outputActive || generation !== this.outputGeneration || this.session !== session || this.state !== "SUSPENDED") return false;
    this.outputActive = false; this.outputClosedGeneration = 0; return this.resume(session.inputEpoch);
  }
}
