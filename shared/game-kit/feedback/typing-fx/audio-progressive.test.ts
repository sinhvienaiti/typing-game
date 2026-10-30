import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { RngStream } from "../../platform/rng";
import { KEYBOARD_DECODE_BATCH_SIZE, KEYBOARD_FIRST_BATCH_SPACES, KeyboardSoundPreview, TypingSounds, VariantPicker, keyboardFiles, type TypingSoundProfile } from "./audio";

const deferred = <T>() => {
  let resolve!: (value: T) => void;
  const promise = new Promise<T>((done) => { resolve = done; });
  return { promise, resolve };
};
const flush = async () => { for (let i = 0; i < 30; i++) await Promise.resolve(); };
class Gain {
  gain = { value: 1, cancelScheduledValues: vi.fn(), setValueAtTime: vi.fn(), linearRampToValueAtTime: vi.fn() };
  connect = vi.fn(); disconnect = vi.fn();
}
class Source {
  buffer: AudioBuffer | null;
  onended: (() => void) | null = null;
  connect = vi.fn(); disconnect = vi.fn(); start = vi.fn(); stop = vi.fn();
  constructor(_ctx?: unknown, options?: { buffer: AudioBuffer }) { this.buffer = options?.buffer ?? null; }
}
class Context {
  state = "running"; currentTime = 0; destination = {};
  sources: Source[] = [];
  decodeAudioData = vi.fn(async (bytes: ArrayBuffer) => ({ duration: 0.1, id: new Uint8Array(bytes)[0] }) as unknown as AudioBuffer);
  resume = vi.fn(async () => {});
  createGain(): Gain { return new Gain(); }
  createBufferSource(): Source { const s = new Source(); this.sources.push(s); return s; }
}
const names = (n = 100) => Array.from({ length: n }, (_, i) => `key-${String(i + 1).padStart(2, "0")}.ogg`);
const profile = (id = "deep", n = 100): TypingSoundProfile => ({ id, name: id, source: "audio-lab", licence: "project-owned", pitch: 0, level: 0, files: { key: names(n) } });
const bytes = vi.fn(async (url: string) => new Uint8Array([Number(/key-(\d+)/.exec(url)?.[1] ?? 0)]).buffer);
const cleanups: (() => void)[] = [];
function player() {
  const ctx = new Context();
  const rng = new RngStream(219);
  const sounds = new TypingSounds({ context: ctx as unknown as AudioContext, random: () => rng.float() });
  cleanups.push(() => sounds.dispose());
  return { ctx, sounds };
}
beforeEach(() => {
  vi.useFakeTimers(); bytes.mockClear();
  vi.stubGlobal("GainNode", Gain); vi.stubGlobal("AudioBufferSourceNode", Source);
});
afterEach(() => { for (const c of cleanups.splice(0)) c(); vi.unstubAllGlobals(); vi.useRealTimers(); });

describe("219 large variant sets", () => {
  it.each([70, 80, 100])("uses every one of %i samples once per round without repeats in the last eight", (n) => {
    const rng = new RngStream(219); const pick = new VariantPicker(n, () => rng.float());
    const values = Array.from({ length: n * 100 }, () => pick.next());
    for (let i = 0; i < values.length; i++) expect(values.slice(Math.max(0, i - 8), i)).not.toContain(values[i]);
    for (let start = 0; start < values.length; start += n) expect(new Set(values.slice(start, start + n)).size).toBe(n);
  });
  it("keeps recent history while newly decoded variants join", () => {
    const pick = new VariantPicker(10, () => 0);
    const first = Array.from({ length: 8 }, () => pick.next());
    pick.grow(100);
    const values = [...first, ...Array.from({ length: 400 }, () => pick.next())];
    for (let i = 1; i < values.length; i++) expect(values.slice(Math.max(0, i - 8), i)).not.toContain(values[i]);
    expect(new Set(values).size).toBe(100);
  });
  it("remembers the last eight plays even when the early loading pool was very small", () => {
    const pick = new VariantPicker(2, () => 0);
    const early = Array.from({ length: 20 }, () => pick.next());
    pick.grow(100);
    const values = [...early.slice(-8), ...Array.from({ length: 100 }, () => pick.next())];
    for (let i = 8; i < values.length; i++) expect(values.slice(i - 8, i)).not.toContain(values[i]);
  });
  it("parses and numerically sorts key-100 and space-100, preserving legacy names", () => {
    const parsed = keyboardFiles({ files: ["key-100.ogg", "key-99.ogg", "key-01.ogg", "key-100.ogg", "space-100.wav", "../key-101.ogg"] }, "/keys");
    expect(parsed).toEqual({ key: ["/keys/key-01.ogg", "/keys/key-99.ogg", "/keys/key-100.ogg"], space: ["/keys/space-100.wav"] });
  });
});

describe("219 progressive decoding and memory", () => {
  it("bounds concurrent decoding, yields between batches and plays before loading completes", async () => {
    const { ctx, sounds } = player();
    const pending = deferred<AudioBuffer>();
    ctx.decodeAudioData.mockReturnValueOnce(pending.promise);
    let done = false;
    const result = sounds.load(profile(), bytes).then((r) => { done = true; return r; });
    await flush();
    expect(bytes).toHaveBeenCalledTimes(KEYBOARD_DECODE_BATCH_SIZE);
    expect(ctx.decodeAudioData).toHaveBeenCalledTimes(KEYBOARD_DECODE_BATCH_SIZE);
    expect(done).toBe(false);
    // Fifteen samples can sound even when one decode in the first batch is held.
    expect(sounds.play("key")).toBe(true);
    pending.resolve({ duration: 0.1 } as AudioBuffer); await flush();
    expect(done).toBe(false);
    expect(bytes).toHaveBeenCalledTimes(KEYBOARD_DECODE_BATCH_SIZE);
    const frameOpportunity = vi.fn(); setTimeout(frameOpportunity, 0);
    await vi.runAllTimersAsync();
    expect(frameOpportunity).toHaveBeenCalledOnce();
    expect(await result).toEqual({ loaded: 100, missing: [] });
    expect(bytes).toHaveBeenCalledTimes(100);
    expect(ctx.decodeAudioData).toHaveBeenCalledTimes(100);
  });
  it("a fully decoded 100-file profile plays all 100 evenly through the real player", async () => {
    const { sounds } = player();
    const sources: Source[] = [];
    vi.stubGlobal("AudioBufferSourceNode", class extends Source { constructor(ctx: unknown, options: { buffer: AudioBuffer }) { super(ctx, options); sources.push(this); } });
    const loading = sounds.load(profile(), bytes); await vi.runAllTimersAsync(); await loading;
    for (let i = 0; i < 1000; i++) sounds.play("key");
    const ids = sources.map((s) => (s.buffer as unknown as { id: number }).id);
    for (let start = 0; start < 1000; start += 100) expect(new Set(ids.slice(start, start + 100)).size).toBe(100);
    for (let i = 0; i < 1000; i++) expect(ids.slice(Math.max(0, i - 8), i)).not.toContain(ids[i]);
  });
  it("lists failures while still decoding the remainder of all batches", async () => {
    const { sounds } = player();
    const fetchBytes = vi.fn(async (url: string) => { if (url === "key-19.ogg") throw new Error("missing"); return bytes(url); });
    const loading = sounds.load(profile(), fetchBytes); await vi.runAllTimersAsync();
    expect(await loading).toEqual({ loaded: 99, missing: ["key-19.ogg"] });
    expect(fetchBytes).toHaveBeenCalledTimes(100); expect(sounds.play("key")).toBe(true);
  });
  it("switching releases the old pack and voice buffers, and switching back requires a reload", async () => {
    const { sounds } = player();
    const sources: Source[] = [];
    vi.stubGlobal("AudioBufferSourceNode", class extends Source { constructor(ctx: unknown, options: { buffer: AudioBuffer }) { super(ctx, options); sources.push(this); } });
    await sounds.load(profile("deep", 10), bytes); sounds.play("key");
    await sounds.load(profile("warm", 10), bytes);
    expect(sources[0]!.stop).toHaveBeenCalled(); expect(sources[0]!.disconnect).toHaveBeenCalled();
    expect(sources[0]!.buffer).toBeNull(); expect(sounds.profile?.id).toBe("warm");
    expect(sounds.use("deep")).toBe(false);
  });
  it("release cancels publication and future batches when an old decode finishes late", async () => {
    const { ctx, sounds } = player(); const pending = deferred<AudioBuffer>();
    ctx.decodeAudioData.mockReturnValueOnce(pending.promise);
    const loading = sounds.load(profile(), bytes); await flush();
    sounds.release("deep");
    pending.resolve({ duration: 1 } as AudioBuffer); await vi.runAllTimersAsync(); await loading;
    expect(bytes).toHaveBeenCalledTimes(KEYBOARD_DECODE_BATCH_SIZE);
    expect(sounds.use("deep")).toBe(false); expect(sounds.play("key")).toBe(false);
  });
  it("disposal prevents late decoding from restoring a pack", async () => {
    const { ctx, sounds } = player(); const pending = deferred<AudioBuffer>();
    ctx.decodeAudioData.mockReturnValueOnce(pending.promise);
    const loading = sounds.load(profile(), bytes); await flush(); sounds.dispose();
    pending.resolve({ duration: 1 } as AudioBuffer); await vi.runAllTimersAsync(); await loading;
    expect(sounds.use("deep")).toBe(false); expect(bytes).toHaveBeenCalledTimes(KEYBOARD_DECODE_BATCH_SIZE);
  });
});

describe("first decode batch mixes keys and spaces (TYPING_FEEL_SERVICE.md §4.6)", () => {
  const spaceNames = (n: number) => Array.from({ length: n }, (_, i) => `space-${String(i + 1).padStart(2, "0")}.ogg`);
  /** Spaces decode to ids 200+, keys to their number. */
  const mixedBytes = vi.fn(async (url: string) => {
    const space = /space-(\d+)/.exec(url);
    return new Uint8Array([space ? 200 + Number(space[1]) : Number(/key-(\d+)/.exec(url)?.[1] ?? 0)]).buffer;
  });
  const mixed = (keys: number, spaces: number): TypingSoundProfile => ({ id: "mixed", name: "mixed", source: "audio-lab", licence: "project-owned", pitch: 0, level: 0, files: { key: names(keys), space: spaceNames(spaces) } });

  it("a ticket-218 set (80 keys, 8 spaces): 12 keys and 4 spaces first, and a word sounds as a word before batch two", async () => {
    mixedBytes.mockClear();
    const { sounds } = player();
    const sources: Source[] = [];
    vi.stubGlobal("AudioBufferSourceNode", class extends Source { constructor(ctx: unknown, options: { buffer: AudioBuffer }) { super(ctx, options); sources.push(this); } });
    const loading = sounds.load(mixed(80, 8), mixedBytes);
    await flush();
    const first = mixedBytes.mock.calls.map(([url]) => url);
    expect(KEYBOARD_DECODE_BATCH_SIZE).toBe(16);
    expect(KEYBOARD_FIRST_BATCH_SPACES).toBe(4);
    expect(first).toEqual([...names(12), ...spaceNames(4)]);
    // Only the first batch is in: the space set already plays a finished word.
    expect(sounds.play("word")).toBe(true);
    expect((sources.at(-1)!.buffer as unknown as { id: number }).id).toBeGreaterThan(200);
    await vi.runAllTimersAsync();
    expect(await loading).toEqual({ loaded: 88, missing: [] });
    expect(mixedBytes.mock.calls.map(([url]) => url)).toEqual([...names(12), ...spaceNames(4), ...names(80).slice(12), ...spaceNames(8).slice(4)]);
  });

  it.each([
    // keys, spaces → first batch keys, first batch spaces (a short set gives its slots to the other; the batch stays 16)
    [80, 3, 13, 3],
    [80, 1, 15, 1],
    [80, 0, 16, 0],
    [10, 8, 10, 6],
    [5, 20, 5, 11],
    [0, 3, 0, 3],
    [10, 3, 10, 3],
    [11, 4, 11, 4],
  ])("%i keys and %i spaces: the first batch holds %i keys and %i spaces, the rest follow in order", async (keys, spaces, firstKeys, firstSpaces) => {
    mixedBytes.mockClear();
    const { sounds } = player();
    const loading = sounds.load(mixed(keys, spaces), mixedBytes);
    await flush();
    const first = mixedBytes.mock.calls.map(([url]) => url);
    expect(first).toEqual([...names(keys).slice(0, firstKeys), ...spaceNames(spaces).slice(0, firstSpaces)]);
    expect(first.length).toBe(Math.min(KEYBOARD_DECODE_BATCH_SIZE, keys + spaces));
    await vi.runAllTimersAsync();
    expect(await loading).toEqual({ loaded: keys + spaces, missing: [] });
    expect(mixedBytes.mock.calls.map(([url]) => url)).toEqual([
      ...names(keys).slice(0, firstKeys), ...spaceNames(spaces).slice(0, firstSpaces), ...names(keys).slice(firstKeys), ...spaceNames(spaces).slice(firstSpaces),
    ]);
  });
});

const DEEP = { value: "deep", label: "Deep", manifest: "/deep/keys-manifest.json", preview: "/deep/preview.ogg" };
const WARM = { value: "warm", label: "Warm", manifest: "/warm/keys-manifest.json", preview: "/warm/preview.ogg" };
function selection(fetchJson = vi.fn(async (_url: string) => ({ files: names() }) as unknown)) {
  const h = player(); const onLoad = vi.fn();
  const preview = new KeyboardSoundPreview({ sounds: h.sounds, levels: () => ({ master: 1, keyboard: 1 }), fetchBytes: bytes, fetchJson, onLoad });
  cleanups.push(() => preview.destroy());
  return { ...h, preview, fetchJson, onLoad };
}
describe("219 selected pack lifecycle", () => {
  it("selected packs can play early; cached 1-second previews survive releasing the old pack", async () => {
    const h = selection(); h.preview.select(DEEP); await flush();
    expect(h.sounds.profile?.id).toBe("deep"); expect(h.sounds.play("key")).toBe(true);
    expect(h.onLoad).not.toHaveBeenCalled();
    await vi.runAllTimersAsync();
    expect(h.onLoad).toHaveBeenLastCalledWith(expect.objectContaining({ keys: 100 }));
    h.preview.select(WARM); await vi.runAllTimersAsync();
    expect(h.sounds.use("deep")).toBe(false);
    const count = bytes.mock.calls.filter(([url]) => url === DEEP.preview).length;
    h.preview.preview(DEEP, 0); await flush();
    expect(bytes.mock.calls.filter(([url]) => url === DEEP.preview)).toHaveLength(count);
    expect(h.ctx.sources.at(-1)!.start).toHaveBeenCalledWith(expect.any(Number), 0, 1);
    h.preview.select(DEEP); await vi.runAllTimersAsync();
    expect(h.fetchJson).toHaveBeenCalledTimes(3);
    expect(bytes.mock.calls.filter(([url]) => url === "/deep/key-100.ogg")).toHaveLength(2);
  });
  it("reselecting the current pack shares its in-flight load and never duplicates decoding", async () => {
    const h = selection(); h.preview.select(DEEP); await flush(); h.preview.select(DEEP);
    await vi.runAllTimersAsync();
    expect(h.fetchJson).toHaveBeenCalledOnce();
    expect(bytes.mock.calls.filter(([url]) => url.startsWith("/deep/key-"))).toHaveLength(100);
    expect(h.onLoad).toHaveBeenCalledOnce();
  });
  it("switching during a manifest fetch cancels sample fetches for the old choice", async () => {
    const pending = deferred<unknown>();
    const h = selection(vi.fn(async (url: string) => url === DEEP.manifest ? pending.promise : { files: names(10) }));
    h.preview.select(DEEP); h.preview.select(WARM); await flush();
    pending.resolve({ files: names() }); await vi.runAllTimersAsync();
    expect(bytes.mock.calls.filter(([url]) => url.startsWith("/deep/key-"))).toHaveLength(0);
    expect(h.sounds.profile?.id).toBe("warm");
  });
  it("switching to Off cancels an in-flight decode, frees samples and retains preview cache", async () => {
    const h = selection(); const pending = deferred<AudioBuffer>();
    h.ctx.decodeAudioData.mockImplementationOnce(async () => ({ duration: 1 }) as AudioBuffer).mockReturnValueOnce(pending.promise);
    h.preview.select(DEEP); await flush();
    h.preview.select({ value: "off", label: "Off" });
    pending.resolve({ duration: 1 } as AudioBuffer); await vi.runAllTimersAsync();
    expect(h.sounds.profile).toBeNull(); expect(h.sounds.use("deep")).toBe(false);
    expect(bytes.mock.calls.filter(([url]) => url.startsWith("/deep/key-"))).toHaveLength(KEYBOARD_DECODE_BATCH_SIZE);
    expect(h.onLoad).not.toHaveBeenCalled();
  });
  it("Off also releases a completed pack", async () => {
    const h = selection(); h.preview.select(DEEP); await vi.runAllTimersAsync();
    h.preview.select({ value: "off", label: "Off" });
    expect(h.sounds.use("deep")).toBe(false);
  });
  it("the Lab can restore a saved pack progressively without starting a preview", async () => {
    const h = selection(); h.preview.select(DEEP, false); await flush();
    expect(h.ctx.sources).toHaveLength(0); expect(h.sounds.profile?.id).toBe("deep");
    expect(h.sounds.play("key")).toBe(true); await vi.runAllTimersAsync();
    expect(bytes.mock.calls.some(([url]) => url === DEEP.preview)).toBe(false);
  });
});
