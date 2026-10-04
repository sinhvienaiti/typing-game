import workerUrl from "virtual:offline-vosk-worker";

type DecoderMessage = {
  event: string;
  recognizerId?: string;
  result?: unknown;
  error?: string;
};
type Listener = (message: DecoderMessage) => void;

/** Small, explicit binding to the pinned upstream Worker protocol. */
export class OfflineDecoder {
  readonly worker: Worker;
  private listeners = new Map<string, Listener[]>();
  private recognizers = new Map<string, OfflineRecognizer>();
  private sequence = 0;
  constructor(modelUrl: string) {
    this.worker = new Worker(workerUrl);
    this.worker.onmessage = ({ data }: MessageEvent<DecoderMessage>) => {
      if (!data || typeof data !== "object") return;
      if (data.recognizerId)
        this.recognizers.get(data.recognizerId)?.receive(data);
      else
        this.listeners.get(data.event)?.forEach((listener) => listener(data));
    };
    this.worker.postMessage({ action: "set", key: "logLevel", value: -1 });
    this.worker.postMessage({ action: "load", modelUrl });
  }
  on(event: string, listener: Listener): void {
    const listeners = this.listeners.get(event) ?? [];
    listeners.push(listener);
    this.listeners.set(event, listeners);
  }
  createRecognizer(sampleRate: number): OfflineRecognizer {
    const id = `recognizer:${++this.sequence}`;
    const recognizer = new OfflineRecognizer(this.worker, id, sampleRate, () =>
      this.recognizers.delete(id),
    );
    this.recognizers.set(id, recognizer);
    return recognizer;
  }
  terminate(): void {
    this.listeners.clear();
    for (const recognizer of this.recognizers.values()) recognizer.remove();
    this.worker.terminate();
  }
}

export class OfflineRecognizer {
  private listeners = new Map<string, Listener[]>();
  private readyPromise: Promise<void>;
  private readyResolve!: () => void;
  private readyReject!: (error: Error) => void;
  private readyTimer: ReturnType<typeof setTimeout>;
  constructor(
    private worker: Worker,
    private id: string,
    sampleRate: number,
    private unregister: () => void,
  ) {
    this.readyPromise = new Promise((resolve, reject) => {
      this.readyResolve = resolve;
      this.readyReject = reject;
    });
    this.readyTimer = setTimeout(
      () => this.readyReject(new Error("Recognizer preparation timed out")),
      10000,
    );
    void this.readyPromise.catch(() => {});
    worker.postMessage({ action: "create", recognizerId: id, sampleRate });
  }
  setWords(value: boolean): void {
    this.worker.postMessage({
      action: "set",
      recognizerId: this.id,
      key: "words",
      value,
    });
  }
  on(event: string, listener: Listener): void {
    const list = this.listeners.get(event) ?? [];
    list.push(listener);
    this.listeners.set(event, list);
  }
  ready(): Promise<void> {
    return this.readyPromise;
  }
  receive(message: DecoderMessage): void {
    if (message.event === "recognizer-ready") {
      clearTimeout(this.readyTimer);
      this.readyResolve();
    }
    if (message.event === "error") {
      clearTimeout(this.readyTimer);
      this.readyReject(new Error(message.error ?? "Recognizer failed"));
    }
    this.listeners.get(message.event)?.forEach((listener) => listener(message));
  }
  acceptWaveformFloat(buffer: Float32Array, sampleRate: number): void {
    const data = buffer.map(
      (value) => Math.max(-1, Math.min(1, value)) * 32768,
    );
    this.worker.postMessage(
      { action: "audioChunk", recognizerId: this.id, sampleRate, data },
      [data.buffer],
    );
  }
  remove(): void {
    clearTimeout(this.readyTimer);
    this.readyReject(new Error("Recognizer removed"));
    this.unregister();
    this.listeners.clear();
    this.worker.postMessage({ action: "remove", recognizerId: this.id });
  }
}
