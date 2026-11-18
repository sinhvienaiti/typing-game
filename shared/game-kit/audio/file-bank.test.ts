import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { FileBank, LayeredBank } from "./file-bank";
import { buffer, deferred, FakeContext, FakeFetch, flush } from "./fake-audio.test-helper";
let f: FakeFetch; let ctx: FakeContext;
beforeEach(() => { f = new FakeFetch(); f.install(); ctx = new FakeContext(); });
afterEach(() => vi.unstubAllGlobals());
describe("file bank loading", () => {
  it("loads manifest, ordered priority ids, then legacy; leaves other ids and music lazy", async () => {
    const manifest = f.hold("/audio/manifest.json"); const key = f.hold("/audio/key"); const ui = f.hold("/audio/ui");
    const bank = new FileBank<string>({ audioBase: "/audio/", manifest: "manifest.json", preload: ["key", "ui"], legacy: { old: "old", key: "obsolete" } });
    const ready = bank.unlock(ctx.audio); expect(f.calls).toEqual(["/audio/manifest.json"]);
    manifest.resolve(f.response({ sounds: { key: ["key"], ui: ["ui"], lazy: ["lazy"] }, music: { calm: "music" } }));
    await flush(); expect(f.calls).toEqual(["/audio/manifest.json", "/audio/key"]);
    key.resolve(f.response()); await flush(); expect(f.calls.at(-1)).toBe("/audio/ui"); expect(f.calls).not.toContain("/audio/old");
    ui.resolve(f.response()); await ready; expect(f.calls.at(-1)).toBe("/audio/old");
    expect(f.calls).not.toContain("/audio/obsolete"); expect(f.calls).not.toContain("/audio/lazy"); expect(f.calls).not.toContain("/audio/music");
    expect(bank.select("lazy")).toBeNull(); await flush(); expect(f.calls.at(-1)).toBe("/audio/lazy");
    expect(bank.select("lazy")?.buffer.duration).toBe(1);
  });
  it("keeps first-play lazy requests behind all priority ids, even while the manifest is pending", async () => {
    const meta = f.hold("/assets/audio/manifest"); const key = f.hold("/assets/audio/key");
    const bank = new FileBank<string>({ manifest: "manifest", preload: ["key", "ui"] });
    const ready = bank.unlock(ctx.audio); bank.select("lazy");
    meta.resolve(f.response({ sounds: { key: ["key"], ui: ["ui"], lazy: ["lazy"] } }));
    await flush(); expect(f.calls).toEqual(["/assets/audio/manifest", "/assets/audio/key"]);
    key.resolve(f.response()); await ready; await flush();
    expect(f.calls).toEqual(["/assets/audio/manifest", "/assets/audio/key", "/assets/audio/ui", "/assets/audio/lazy"]);
  });
  it("never starts more fetch/decode jobs than its concurrency, and loads every variant", async () => {
    const gates = Array.from({ length: 7 }, () => deferred<AudioBuffer>()); let active = 0; let peak = 0; let started = 0;
    ctx.decodeAudioData.mockImplementation(async () => { const i = started++; active++; peak = Math.max(peak, active); const b = await gates[i]!.promise; active--; return b; });
    const bank = new FileBank({ manifest: { sounds: { hit: ["0", "1", "2", "3", "4", "5", "6"] } }, preload: ["hit"], decodeConcurrency: 2 });
    const ready = bank.unlock(ctx.audio); await flush(); expect(started).toBe(2);
    expect(bank.select("hit")).toBeNull();
    gates[0]!.resolve(buffer()); await flush(); expect(started).toBe(3); expect(bank.select("hit")?.variant).toBe(0);
    for (const gate of gates) { gate.resolve(buffer()); await flush(); }
    await ready; expect(peak).toBe(2); expect(started).toBe(7);
    expect(bank.select("hit", 6)?.variant).toBe(6);
  });
  it("defaults concurrency to four and shares cached file jobs", async () => {
    const gate = deferred<AudioBuffer>(); ctx.decodeAudioData.mockImplementation(() => gate.promise);
    const bank = new FileBank({ legacy: { a: "a", b: "b", c: "c", d: "d", e: "e", same: "a" } });
    const ready = bank.unlock(ctx.audio); await flush(); expect(ctx.decodeAudioData).toHaveBeenCalledTimes(4);
    gate.resolve(buffer()); await ready; expect(ctx.decodeAudioData).toHaveBeenCalledTimes(5);
  });
  it("measures durations, replaces hints, and reports only differences over 20ms", async () => {
    const bank = new FileBank({ manifest: { version: 2, sounds: { hit: { files: ["a", "b", "c"], durationMs: [900, 980, 1000] } } } });
    await bank.unlock(ctx.audio); expect(bank.duration("hit", 0)).toBe(0.9);
    await bank.ensure("hit"); expect(bank.duration("hit", 0)).toBe(1);
    expect(bank.stats().durationMismatches).toEqual([{ id: "hit", variant: 0, expectedMs: 900, actualMs: 1000 }]);
  });
  it("loops are retrieved as buffers; music loads only on request", async () => {
    const bank = new FileBank({ manifest: { version: 2, sounds: { bed: { files: ["bed"], loop: true } }, music: { calm: { file: "music", bpm: 96, bars: 8 } } } });
    await bank.unlock(ctx.audio); expect(f.calls).toEqual([]);
    expect(bank.loopBuffer("bed")).toBeNull(); await flush(); expect(bank.loopBuffer("bed")?.duration).toBe(1);
    expect(bank.select("bed")).toBeNull(); expect(await bank.track("calm")).toEqual({ url: "/assets/audio/music", buffer: buffer() });
    expect(await bank.track("unknown")).toBeNull();
  });
  it("failed variants keep original indices; errors are observable and do not throw", async () => {
    f.json("/assets/audio/bad", {}, false);
    const bank = new FileBank({ manifest: { sounds: { hit: ["bad", "good"] } }, preload: ["hit"] });
    await bank.unlock(ctx.audio); expect(bank.select("hit", 0)).toBeNull(); expect(bank.select("hit", 1)?.variant).toBe(1);
    expect(bank.stats().errors).toHaveLength(1);
  });
});
describe("layered selection", () => {
  it("selects existing game hooks only until a file is ready, excluding loops", async () => {
    const hook = vi.fn(); const bank = new FileBank({ manifest: { sounds: { hit: ["hit"] } } });
    const layered = new LayeredBank(bank, { hit: hook }); await bank.unlock(ctx.audio);
    expect(layered.select("hit")).toEqual({ kind: "hook", hook }); await flush();
    expect(layered.select("hit").kind).toBe("file"); expect(hook).not.toHaveBeenCalled();
  });
});
