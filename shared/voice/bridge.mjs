import { VOICE_NAMESPACE, isVoiceMessage, parseVoiceMessage } from "./protocol.mjs";

/** The real Portal owns the capture. A factory is installed only after the offline engine gate passes. */
export class ParentVoiceBridge {
  constructor({ createHost = null, unavailableReason = "offline-engine-not-validated" } = {}) {
    this.createHost = createHost; this.unavailableReason = unavailableReason; this.binding = null; this.host = null;
  }
  reset() {
    const host = this.host; this.binding = null; this.host = null;
    // Host.stop invalidates synchronously; route rendering never waits for permission/worker cleanup.
    if (host) void host.stop().catch(() => {});
  }
  post(binding, op, fields) {
    if (this.binding !== binding) return;
    const message = parseVoiceMessage({ type: `${VOICE_NAMESPACE}:${op}`, version: 1, gameId: binding.gameId, gameInstanceId: binding.instanceId, ...fields });
    binding.source.postMessage(message, binding.origin);
  }
  handleMessage(event, frame, game) {
    if (!isVoiceMessage(event.data)) return false;
    if (!frame?.contentWindow || !game || game.id !== "space-typing" || event.source !== frame.contentWindow || event.origin !== new URL(game.appUrl).origin) return true;
    let message;
    try { message = parseVoiceMessage(event.data); } catch { return true; }
    if (message.gameId !== game.id) return true;
    const op = message.type.slice(VOICE_NAMESPACE.length + 1);
    if (op === "hello") {
      if (!message.versions.includes(1)) return true;
      const b = this.binding;
      if (!b || b.source !== event.source || b.instanceId !== message.gameInstanceId || b.origin !== event.origin) {
        this.reset();
        this.binding = { source: event.source, origin: event.origin, gameId: game.id, instanceId: message.gameInstanceId, mode: "typing", inputEpoch: 0 };
      }
      this.post(this.binding, "capabilities", { offlineEngineAvailable: typeof this.createHost === "function", reason: this.createHost ? "validated-local-engine" : this.unavailableReason });
      return true;
    }
    const b = this.binding;
    if (!b || b.source !== event.source || b.origin !== event.origin || b.instanceId !== message.gameInstanceId) return true;
    if (op === "configure") {
      if (message.inputEpoch < b.inputEpoch) return true;
      const host = this.host; this.host = null; if (host) void host.stop().catch(() => {});
      b.mode = message.mode; b.inputEpoch = message.inputEpoch;
      return true;
    }
    if (op === "start") {
      if (b.mode === "typing" || message.inputEpoch !== b.inputEpoch) return true;
      if (!this.createHost) { this.post(b, "error", { code: this.unavailableReason, message: "An offline engine must pass validation before Voice can start." }); return true; }
      // A second start is idempotent; configure/stop is required to start a fresh session.
      if (this.host) return true;
      let host;
      host = this.createHost((event) => {
        if (!host || this.host !== host || this.binding !== b) return;
        const { type, ...fields } = event;
        if (type === "ready") b.inputEpoch = fields.inputEpoch;
        this.post(b, type, fields);
      });
      this.host = host; void host.start(b.inputEpoch).catch(() => { if (this.host === host) this.post(b, "error", { code: "host-start-failed", message: "Local capture could not start." }); });
      return true;
    }
    const host = this.host, session = host?.session;
    if (!host || !session || message.sessionId !== session.sessionId) return true;
    const invoke = (promise) => { void promise.catch(() => { if (this.host === host) this.post(b, "error", { code: "host-operation-failed", message: "Local capture could not apply the request." }); }); };
    if (op === "suspend" && message.inputEpoch >= session.inputEpoch) { b.inputEpoch = message.inputEpoch; invoke(host.suspend(message.inputEpoch)); }
    else if (op === "resume" && message.inputEpoch >= session.inputEpoch) { b.inputEpoch = message.inputEpoch; invoke(host.resume(message.inputEpoch)); }
    else if (message.inputEpoch !== session.inputEpoch) return true;
    else if (op === "stop") {
      this.host = null;
      void host.stop().then(() => { if (this.host === null) this.post(b, "stopped", { sessionId: session.sessionId, inputEpoch: session.inputEpoch }); }).catch(() => {});
    }
    else if (op === "targets") invoke(host.applyTargets(message));
    else if (op === "audio-output-intent") invoke(host.audioOutputIntent(message.generation));
    else if (op === "audio-output-ended") invoke(host.audioOutputEnded(message.generation));
    // Child resolution is diagnostic; it never authorizes the parent to mutate a game.
    return true;
  }
}
