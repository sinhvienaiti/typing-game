// Source: new for the kit: typing-fx key sounds on a fake AudioContext (round-robin, voice cap, hierarchy)
import { afterAll, beforeAll, describe, expect, it } from "vitest";
import { RngStream } from "../../platform/rng";
import { KEYBOARD_PROFILES, keyboardFiles, profileGaps, TYPING_SOUND_MAP, TYPING_SOUND_SET, TypingSounds, VariantPicker, VoicePool, type TypingSoundProfile } from "./audio";

/** Just enough Web Audio for the player: a clock, gains and sources that record what they did. */
class FakeParam {
  value: number;
  events: string[] = [];
  constructor(value: number) {
    this.value = value;
  }
  cancelScheduledValues(): void {}
  setValueAtTime(v: number, t: number): void {
    this.value = v;
    this.events.push(`set ${v.toFixed(3)}@${t.toFixed(3)}`);
  }
  linearRampToValueAtTime(v: number, t: number): void {
    this.events.push(`ramp ${v}@${t.toFixed(3)}`);
  }
}
class FakeNode {
  connected: unknown[] = [];
  connect(node: unknown): unknown {
    this.connected.push(node);
    return node;
  }
  disconnect(): void {}
}
class FakeGain extends FakeNode {
  gain: FakeParam;
  constructor(_ctx: unknown, options: { gain?: number } = {}) {
    super();
    this.gain = new FakeParam(options.gain ?? 1);
  }
}
const started: FakeSource[] = [];
class FakeSource extends FakeNode {
  buffer: { duration: number; id: number };
  playbackRate: number;
  startAt = -1;
  stopAt = -1;
  constructor(_ctx: unknown, options: { buffer: { duration: number; id: number }; playbackRate: number }) {
    super();
    this.buffer = options.buffer;
    this.playbackRate = options.playbackRate;
  }
  start(t: number): void {
    this.startAt = t;
    started.push(this);
  }
  stop(t: number): void {
    this.stopAt = t;
  }
}
class FakeContext {
  currentTime = 0;
  state = "running";
  destination = new FakeNode();
  decoded = 0;
  async decodeAudioData(bytes: ArrayBuffer): Promise<{ duration: number; id: number }> {
    const view = new Uint8Array(bytes);
    if (view[0] === 255) throw new Error("broken file");
    this.decoded += 1;
    return { duration: view[1]! / 100, id: view[0]! };
  }
  async resume(): Promise<void> {}
  async close(): Promise<void> {}
}

const saved: Record<string, unknown> = {};
beforeAll(() => {
  for (const name of ["GainNode", "AudioBufferSourceNode"]) saved[name] = (globalThis as Record<string, unknown>)[name];
  Object.assign(globalThis, { GainNode: FakeGain, AudioBufferSourceNode: FakeSource });
});
afterAll(() => Object.assign(globalThis, saved));

/** Files named "<id>:<centiseconds>[.ext]" decode to a buffer with that id and length; id 255 is broken. */
const bytes = async (url: string): Promise<ArrayBuffer> => {
  const name = url.split("/").pop()!.replace(/\.[a-z0-9]+$/, "");
  const [id, cs] = name.split(":").map(Number);
  return new Uint8Array([id!, cs!]).buffer;
};
const files = (from: number, n: number, cs: number): string[] => Array.from({ length: n }, (_, i) => `${from + i}:${cs}`);

const PROFILE: TypingSoundProfile = { id: "test", name: "Test", source: "audio-lab", licence: "project-owned", files: { key: files(1, 10, 8), space: files(40, 3, 40) } };

describe("typing sounds: variants", () => {
  it("plays every variant once a round and never the same one twice in a row", () => {
    const rng = new RngStream(7);
    const picker = new VariantPicker(8, () => rng.float());
    const picks = Array.from({ length: 8 * 50 }, () => picker.next());
    for (let round = 0; round < 50; round += 1) expect(new Set(picks.slice(round * 8, round * 8 + 8)).size).toBe(8);
    for (let i = 1; i < picks.length; i += 1) expect(picks[i]).not.toBe(picks[i - 1]);
  });

  it("a single variant always plays", () => {
    const picker = new VariantPicker(1);
    expect([picker.next(), picker.next()]).toEqual([0, 0]);
  });
});

describe("typing sounds: voices", () => {
  it("caps voices and cuts the one that started first", () => {
    const pool = new VoicePool(3);
    expect([pool.acquire(0, 1), pool.acquire(0.1, 1), pool.acquire(0.2, 1)]).toEqual([0, 1, 2]);
    expect(pool.active(0.25)).toBe(3);
    expect(pool.acquire(0.3, 1)).toBe(0);
    expect(pool.stole).toBe(true);
    expect(pool.stolen).toBe(1);
    expect(pool.acquire(5, 0.1)).toBe(0);
    expect(pool.stole).toBe(false);
    expect(pool.active(5.05)).toBe(1);
  });
});

describe("typing sounds: player", () => {
  const make = (): { sounds: TypingSounds; ctx: FakeContext } => {
    const ctx = new FakeContext();
    const rng = new RngStream(3);
    const sounds = new TypingSounds({ context: ctx as unknown as AudioContext, random: () => rng.float() });
    return { sounds, ctx };
  };

  it("decodes everything before play and lists broken files", async () => {
    const { sounds, ctx } = make();
    const result = await sounds.load({ ...PROFILE, files: { ...PROFILE.files, space: ["255:10", "41:10"] } }, bytes);
    expect(result.missing).toEqual(["255:10"]);
    expect(result.loaded).toBe(10 + 1);
    expect(ctx.decoded).toBe(11);
  });

  it("nothing plays before resume, while muted, or with no profile", async () => {
    const quiet = new TypingSounds({ context: new FakeContext() as unknown as AudioContext });
    expect(quiet.play("key")).toBe(false);
    const { sounds } = make();
    await sounds.load(PROFILE, bytes);
    sounds.muted = true;
    expect(sounds.play("key")).toBe(false);
    sounds.muted = false;
    expect(sounds.use("off")).toBe(false);
    expect(sounds.play("key")).toBe(false);
    expect(sounds.use("test")).toBe(true);
    expect(sounds.play("key")).toBe(true);
  });

  it("15 keys a second hold at most 6 key voices; a word keeps its own voice", async () => {
    const { sounds, ctx } = make();
    await sounds.load({ ...PROFILE, files: { key: files(1, 10, 90), space: files(40, 3, 40) } }, bytes); // long 0.9 s keys force cuts
    started.length = 0;
    let maxActive = 0;
    for (let k = 0; k < 45; k += 1) {
      ctx.currentTime = k / 15;
      sounds.key(k % 6);
      if (k === 30) sounds.complete(true, 3);
      maxActive = Math.max(maxActive, sounds.activeVoices());
    }
    expect(maxActive).toBeLessThanOrEqual(6 + 2);
    expect(sounds.stolen).toBeGreaterThan(0);
    const word = started.find((s) => s.buffer.id >= 40)!;
    expect(word.stopAt).toBe(-1); // never cut by the keys after it
    expect(started.filter((s) => s.stopAt >= 0).length).toBeGreaterThan(0);
  });

  it("pitch and level vary a little, never the same file twice in a row", async () => {
    const { sounds, ctx } = make();
    await sounds.load(PROFILE, bytes);
    started.length = 0;
    for (let k = 0; k < 40; k += 1) {
      ctx.currentTime = k;
      sounds.key(0);
    }
    const rates = started.map((s) => s.playbackRate);
    for (const r of rates) expect(Math.abs(r - 1)).toBeLessThanOrEqual(0.03 + 1e-9);
    expect(new Set(rates.map((r) => r.toFixed(4))).size).toBeGreaterThan(30);
    for (let i = 1; i < started.length; i += 1) expect(started[i]!.buffer.id).not.toBe(started[i - 1]!.buffer.id);
  });

  it("letters play the key set; a word, the spacebar and milestones the space set, louder up the hierarchy", async () => {
    const { sounds, ctx } = make();
    await sounds.load(PROFILE, bytes);
    started.length = 0;
    const set = (): string => (started.at(-1)!.buffer.id >= 40 ? "space" : "key");
    const calls: [string, () => void][] = [
      ["key", () => sounds.key(2)],
      ["key", () => sounds.wrong()],
      ["key", () => sounds.stray()],
      ["space", () => sounds.space()],
      ["space", () => sounds.complete(false, 3)],
      ["space", () => sounds.complete(true, 3)],
      ["space", () => sounds.complete(true, 25)],
    ];
    for (const [want, call] of calls) {
      ctx.currentTime += 1;
      call();
      expect(set()).toBe(want);
    }
    const g = TYPING_SOUND_MAP;
    expect(g.stray.gain).toBeLessThan(g.wrong.gain);
    expect(g.wrong.gain).toBeLessThan(g.key.gain);
    expect(g.key.gain).toBeLessThan(g.word.gain);
    expect(g.word.gain).toBeLessThan(g.perfect.gain);
    expect(g.perfect.gain).toBeLessThan(g.combo.gain);
  });

  it("a profile without its space set still sounds a finished word (a key)", async () => {
    const { sounds, ctx } = make();
    await sounds.load({ ...PROFILE, id: "keys-only", files: { key: files(1, 10, 8) } }, bytes);
    started.length = 0;
    ctx.currentTime = 1;
    expect(sounds.play("word")).toBe(true);
    expect(started[0]!.buffer.id).toBeLessThan(40);
  });

  it("a synth profile only plays through a stand-in the Lab sets", async () => {
    const { sounds } = make();
    await sounds.load({ id: "synth", name: "Kit synth (test only)", source: "synth", licence: "project-owned", files: {} });
    sounds.use("synth");
    expect(sounds.play("key")).toBe(false);
    const heard: string[] = [];
    sounds.standIn = (event, step) => heard.push(event + step);
    sounds.key(2);
    sounds.complete(false, 10);
    expect(heard).toEqual(["key2", "combo0"]);
  });
});

describe("typing sounds: the Audio Lab's keyboard layout", () => {
  const json = (data: unknown) => async (url: string): Promise<unknown> => {
    if (data === undefined) throw new Error(url + ": 404");
    return data;
  };

  it("reads the files a keys-manifest.json names, whatever its shape, in number order", () => {
    const manifest = {
      profile: "thock",
      files: [{ file: "space-02.ogg" }, { file: "key-10.ogg" }, { file: "key-02.ogg" }, { path: "key-01.ogg", lufs: -20 }, "space-01.ogg", "notes.txt"],
      extra: { nested: ["key-03.ogg", "key-02.ogg"] },
    };
    expect(keyboardFiles(manifest, "/keys/thock")).toEqual({
      key: ["/keys/thock/key-01.ogg", "/keys/thock/key-02.ogg", "/keys/thock/key-03.ogg", "/keys/thock/key-10.ogg"],
      space: ["/keys/thock/space-01.ogg", "/keys/thock/space-02.ogg"],
    });
    // Never a path out of the profile's folder.
    expect(keyboardFiles(["../x/key-01.ogg", "/abs/key-02.ogg", "https://x/key-03.ogg"], "/k/")).toEqual({ key: [], space: [] });
  });

  it("loads a staged profile from <base>/<id>/, ready with ten keys and three spaces", async () => {
    const ctx = new FakeContext();
    const sounds = new TypingSounds({ context: ctx as unknown as AudioContext });
    const names = [...Array.from({ length: 10 }, (_, i) => `key-${String(i + 1).padStart(2, "0")}.ogg`), "space-01.ogg", "space-02.ogg", "space-03.ogg"];
    const fetched: string[] = [];
    const fetchBytes = async (url: string): Promise<ArrayBuffer> => {
      fetched.push(url);
      return new Uint8Array([url.includes("space") ? 41 : 2, 8]).buffer;
    };
    const load = await sounds.loadKeyboard("/staging/keys", "creamy", "Creamy", json({ files: names }), fetchBytes);
    expect(load).toEqual({ id: "creamy", state: "ready", keys: 10, spaces: 3, missing: [] });
    expect(fetched[0]).toBe("/staging/keys/creamy/key-01.ogg");
    expect(sounds.use("creamy")).toBe(true);
    const partial = await sounds.loadKeyboard("/staging/keys", "dome", "Soft Dome", json({ files: names.slice(0, 7) }), fetchBytes);
    expect(partial.state).toBe("partial");
  });

  it("with nothing staged a profile is pending and silent: nothing stands in for it", async () => {
    const sounds = new TypingSounds({ context: new FakeContext() as unknown as AudioContext });
    expect(await sounds.loadKeyboard("/staging/keys", "marbly", "Marbly", json(undefined))).toEqual({ id: "marbly", state: "pending", keys: 0, spaces: 0, missing: [] });
    expect(await sounds.loadKeyboard("/staging/keys", "clack", "Clean Clack", json({ files: [] }))).toMatchObject({ state: "pending" });
    expect(sounds.use("marbly")).toBe(false);
  });

  it("the owner's five profiles, and the gap the Audio Lab still owes", () => {
    expect(KEYBOARD_PROFILES.map((p) => p.id)).toEqual(["creamy", "thock", "marbly", "clack", "dome"]);
    expect(KEYBOARD_PROFILES.map((p) => p.name)).toEqual(["Creamy Linear", "Deep Thock", "Marbly", "Clean Clack", "Soft Dome"]);
    expect(TYPING_SOUND_SET.key.want).toBe(10);
    expect(TYPING_SOUND_SET.space.want).toBe(3);
    expect(profileGaps({ ...PROFILE, files: { key: files(1, 10, 8), space: files(40, 1, 8) } })).toEqual([{ set: "space", have: 1, ...TYPING_SOUND_SET.space }]);
  });
});
