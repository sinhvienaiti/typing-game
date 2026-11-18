import { vi } from "vitest";

export function deferred<T>() {
  let resolve!: (value: T) => void;
  let reject!: (reason?: unknown) => void;
  const promise = new Promise<T>((yes, no) => { resolve = yes; reject = no; });
  return { promise, resolve, reject };
}
export const flush = async () => { for (let i = 0; i < 30; i++) await Promise.resolve(); };
export const buffer = (duration = 1) => ({ duration }) as AudioBuffer;
export class FakeNode {
  connections: FakeNode[] = [];
  gain = { value: 1, setTargetAtTime: vi.fn((value: number) => { this.gain.value = value; }) };
  pan = { value: 0 };
  playbackRate = { value: 1 };
  buffer: AudioBuffer | null = null;
  loop = false;
  start = vi.fn();
  stop = vi.fn();
  constructor(readonly kind: string) {}
  connect(next: FakeNode) { this.connections.push(next); return next; }
}
export class FakeContext {
  static all: FakeContext[] = [];
  currentTime = 0;
  state = "running";
  sampleRate = 8000;
  destination = new FakeNode("destination");
  nodes: FakeNode[] = [];
  constructor() { FakeContext.all.push(this); }
  private node(kind: string) { const n = new FakeNode(kind); this.nodes.push(n); return n; }
  createGain() { return this.node("gain"); }
  createStereoPanner() { return this.node("panner"); }
  createBufferSource() { return this.node("source"); }
  createWaveShaper() { return this.node("shaper"); }
  createDynamicsCompressor() {
    return Object.assign(this.node("compressor"), Object.fromEntries(
      ["threshold", "knee", "ratio", "attack", "release"].map(key => [key, { value: 0 }]),
    ));
  }
  createBuffer() { return { duration: 2, getChannelData: () => new Float32Array(8) }; }
  decodeAudioData = vi.fn(async (_data: ArrayBuffer) => buffer());
  resume = vi.fn();
  get sources() { return this.nodes.filter(n => n.kind === "source"); }
  get gains() { return this.nodes.filter(n => n.kind === "gain"); }
  get audio() { return this as unknown as AudioContext; }
}

/** Every URL can be held and resolved explicitly; no real requests escape the fake. */
export class FakeFetch {
  calls: string[] = [];
  replies = new Map<string, Promise<Response>>();
  fetch = vi.fn((url: string) => {
    this.calls.push(url);
    return this.replies.get(url) ?? Promise.resolve(this.response());
  });
  response(json: unknown = {}, ok = true): Response {
    return { ok, status: ok ? 200 : 404, json: async () => json, arrayBuffer: async () => new ArrayBuffer(4) } as Response;
  }
  hold(url: string) { const d = deferred<Response>(); this.replies.set(url, d.promise); return d; }
  json(url: string, json: unknown, ok = true) { this.replies.set(url, Promise.resolve(this.response(json, ok))); }
  install() {
    FakeContext.all = [];
    vi.stubGlobal("fetch", this.fetch);
    vi.stubGlobal("AudioContext", FakeContext);
  }
}
