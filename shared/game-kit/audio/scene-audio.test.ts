import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { SceneAudio, audioUrl } from "./index";

type FakeNode = {
  kind: string;
  gain: { value: number; setTargetAtTime: (value: number) => void };
  connections: FakeNode[];
  connect(next: FakeNode): FakeNode;
  [key: string]: unknown;
};

let contexts: FakeContext[];

function node(kind: string): FakeNode {
  const created: FakeNode = {
    kind,
    connections: [],
    gain: { value: 1, setTargetAtTime: (value: number) => (created.gain.value = value) },
    connect(next: FakeNode) {
      created.connections.push(next);
      return next;
    },
  };
  return created;
}

class FakeContext {
  currentTime = 0;
  state = "running";
  sampleRate = 8000;
  destination = node("destination");
  gains: FakeNode[] = [];
  sources: FakeNode[] = [];
  constructor() {
    contexts.push(this);
  }
  createGain() {
    const gain = node("gain");
    this.gains.push(gain);
    return gain;
  }
  createStereoPanner() {
    return Object.assign(node("panner"), { pan: { value: 0 } });
  }
  createBufferSource() {
    const source = Object.assign(node("source"), { playbackRate: { value: 1 }, buffer: null, start: vi.fn() });
    this.sources.push(source);
    return source;
  }
  createWaveShaper() {
    return node("shaper");
  }
  createDynamicsCompressor() {
    const param = () => ({ value: 0 });
    return Object.assign(node("compressor"), { threshold: param(), knee: param(), ratio: param(), attack: param(), release: param() });
  }
  createBuffer() {
    return { getChannelData: () => new Float32Array(16), duration: 1 };
  }
  decodeAudioData = vi.fn(async () => ({ duration: 1 }));
  resume = vi.fn();
}

beforeEach(() => {
  contexts = [];
  vi.stubGlobal("AudioContext", FakeContext);
  vi.stubGlobal(
    "fetch",
    vi.fn(async () => ({ ok: true, arrayBuffer: async () => new ArrayBuffer(4) })),
  );
});

afterEach(() => {
  vi.unstubAllGlobals();
});

const flush = () => new Promise((resolve) => setTimeout(resolve, 0));

describe("SceneAudio with a game's sound table", () => {
  it("resolves table paths under the audio base and keeps absolute URLs", () => {
    expect(audioUrl("dragon/roar.mp3")).toBe("/assets/audio/dragon/roar.mp3");
    expect(audioUrl("/x.ogg", "/a/")).toBe("/x.ogg");
    expect(audioUrl("https://cdn/x.ogg")).toBe("https://cdn/x.ogg");
    const audio = new SceneAudio({
      sounds: { fire: "dragon-hold/fire.ogg", gong: { url: "/assets/ui/gong.ogg", bus: "warnings" } },
      audioBase: "/assets/audio/",
    });
    expect(audio.url("fire")).toBe("/assets/audio/dragon-hold/fire.ogg");
    expect(audio.url("gong")).toBe("/assets/ui/gong.ogg");
  });

  it("refuses a sound on an unknown bus", () => {
    expect(() => new SceneAudio({ sounds: { a: { url: "a.ogg", bus: "nope" as "ui" } } })).toThrow("unknown bus");
  });

  it("builds one gain per bus under the master and routes each sound to its bus", async () => {
    const audio = new SceneAudio({
      sounds: { breath: { url: "breath.ogg", bus: "fire" }, siren: { url: "siren.ogg", bus: "alarm", gain: 0.5 } },
      buses: { fire: { gain: 0.8, duck: 0.4 }, alarm: { gain: 1, duck: 0.9 } },
      dragonSamples: false,
      sfxVolume: 0.6,
    });
    audio.play("breath");
    expect(contexts).toHaveLength(0);
    audio.unlock();
    await flush();
    const context = contexts[0]!;
    const [master, fire, alarm] = context.gains;
    expect(master!.gain.value).toBe(0.6);
    expect(master!.connections).toEqual([context.destination]);
    expect(fire!.gain.value).toBeCloseTo(0.8);
    expect(alarm!.gain.value).toBeCloseTo(1);
    expect(fire!.connections[0]).toBe(master);

    audio.play("siren");
    const source = context.sources.at(-1)!;
    const volume = source.connections[0]!;
    expect(volume.gain.value).toBe(0.5);
    const panner = volume.connections[0]!;
    expect(panner.connections[0]).toBe(alarm);

    // The same sound inside its gap is skipped.
    audio.play("siren");
    expect(context.sources.at(-1)).toBe(source);

    audio.setPronunciationActive(true);
    expect(fire!.gain.value).toBeCloseTo(0.32);
    expect(alarm!.gain.value).toBeCloseTo(0.9);
  });

  it("stays silent when disabled and loads a file on its first playFile", async () => {
    const audio = new SceneAudio({ sounds: {}, dragonSamples: false });
    audio.unlock();
    await flush();
    const context = contexts[0]!;
    audio.playFile("extra/horn.ogg");
    await flush();
    expect(fetch).toHaveBeenCalledWith("/assets/audio/extra/horn.ogg");
    audio.setEnabled(false);
    audio.playFile("extra/horn.ogg");
    expect(context.sources).toHaveLength(0);
    audio.setEnabled(true);
    audio.playFile("extra/horn.ogg");
    expect(context.sources).toHaveLength(1);
  });
});
