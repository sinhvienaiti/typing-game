import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import type { AudioManifestSource } from "./manifest";
import { DRAGON_SAMPLES } from "./dragon-voice";
import { SceneAudio } from "./scene-audio";
import { buffer, deferred, FakeContext, FakeFetch, flush, type FakeNode } from "./fake-audio.test-helper";
let f: FakeFetch;
const buses = { fx: { gain: 0.8, duck: 0.5 }, music: { gain: 0.9, duck: 0.3 } };
const context = () => FakeContext.all[0]!;
beforeEach(() => { f = new FakeFetch(); f.install(); vi.spyOn(Math, "random").mockReturnValue(0.5); });
afterEach(() => { vi.unstubAllGlobals(); vi.restoreAllMocks(); });
describe("scene file playback", () => {
  it("fetches a lazy id on first play without playing late; measures the selected variant at its rate", async () => {
    const gate = deferred<AudioBuffer>(); const hook = vi.fn(() => 0.2);
    const audio = new SceneAudio({ sounds: { hit: { bus: "fx", gain: 0.6 } }, buses, manifest: { version: 2, sounds: { hit: { files: ["a", "b"], durationMs: [100, 200] } } }, missing: { hit: hook }, dragonSamples: false });
    audio.unlock(); await audio.ready(); context().decodeAudioData.mockImplementation(() => gate.promise);
    expect(f.calls).toEqual([]); expect(audio.play("hit")).toBe(0.2); await flush(); expect(f.calls).toHaveLength(2);
    gate.resolve(buffer(2)); await flush(); expect(context().sources).toHaveLength(0); expect(hook).toHaveBeenCalledTimes(1);
    context().currentTime = 1;
    expect(audio.play("hit", 0.5, { rate: 2, variant: 1, pan: 0.7 })).toBe(1);
    const src = context().sources[0]!; expect(src.buffer?.duration).toBe(2); expect(src.playbackRate.value).toBe(2);
    expect(src.connections[0]!.gain.value).toBe(0.3); expect(src.connections[0]!.connections[0]!.pan.value).toBe(0.7);
    expect(audio.stats().plays.hit).toEqual({ file: 1, hook: 1, silent: 0 }); expect(audio.stats().durationMismatches).toHaveLength(2);
  });
  it("stays silent for a missing file without a hook and never replays the loading event", async () => {
    const pending = f.hold("/assets/audio/lazy");
    const audio = new SceneAudio({ sounds: { hit: {} }, manifest: { sounds: { hit: ["lazy"] } }, dragonSamples: false });
    audio.unlock(); await audio.ready(); expect(audio.play("hit")).toBe(0);
    pending.resolve(f.response()); await flush(); expect(context().sources).toHaveLength(0);
    expect(audio.stats().plays.hit).toEqual({ file: 0, hook: 0, silent: 1 });
    expect(audio.play("hit")).toBe(1); expect(context().sources).toHaveLength(1);
  });
  it("loads dragon recordings at unlock alongside legacy files, without waiting for their completion", async () => {
    const old = f.hold("/assets/audio/old");
    const audio = new SceneAudio({ sounds: { hit: "old" }, dragonSamples: { burst: DRAGON_SAMPLES.burst } });
    audio.unlock(); await flush();
    expect(f.calls).toContain("/assets/audio/dragon/fire-burst.mp3");
    old.resolve(f.response()); await audio.ready();
  });
  it("manifest files override table URLs while table bus/gain/gap remain authoritative", async () => {
    const hook = vi.fn();
    const audio = new SceneAudio({ sounds: { hit: { url: "old", bus: "fx", gain: 0.4, gap: 0.2 } }, buses, manifest: { sounds: { hit: ["new"] } }, preload: ["hit"], missing: { hit: hook }, dragonSamples: false });
    audio.unlock(); await audio.ready(); expect(f.calls).toEqual(["/assets/audio/new"]); expect(audio.url("hit")).toBe("/assets/audio/new");
    expect(audio.play("hit")).toBe(1); expect(audio.play("hit")).toBe(0); expect(hook).not.toHaveBeenCalled();
    expect(context().sources[0]!.connections[0]!.gain.value).toBe(0.4);
    expect(audio.stats().plays.hit).toEqual({ file: 1, hook: 0, silent: 1 });
  });
  it("missing hooks use the same gain/pan/bus nodes and gap as synth", async () => {
    let out: FakeNode | undefined; const hook = vi.fn((_c, node) => { out = node as FakeNode; return 0.25; });
    const audio = new SceneAudio({ sounds: { hit: { bus: "fx", gain: 0.4, gap: 0.2 } }, buses, missing: { hit: hook }, dragonSamples: false });
    audio.unlock(); await audio.ready(); expect(audio.play("hit", 0.5, { pan: -0.7 })).toBe(0.25);
    const hookOut = out!; expect(hookOut.gain.value).toBe(0.2); expect(hookOut.connections[0]!.pan.value).toBe(-0.7);
    context().currentTime = 0.1; audio.play("hit"); expect(hook).toHaveBeenCalledTimes(1);
    audio.synth("compare", (_c, node) => { out = node as unknown as FakeNode; }, 0.2, { pan: -0.7, gap: 0.2, bus: "fx" });
    expect(out!.gain.value).toBe(hookOut.gain.value); expect(out!.connections[0]!.pan.value).toBe(-0.7);
    expect(out!.connections[0]!.connections).toEqual(hookOut.connections[0]!.connections);
    audio.synth("compare", hook); expect(hook).toHaveBeenCalledTimes(1);
    audio.setEnabled(false); context().currentTime = 1; expect(audio.play("hit")).toBe(0); expect(hook).toHaveBeenCalledTimes(1);
  });
  it("counts silence, never runs hooks for loops or an unavailable explicit variant of ready files", async () => {
    const hook = vi.fn(); const audio = new SceneAudio({ sounds: { bed: {}, hit: {}, none: {} }, manifest: { version: 2, sounds: { bed: { files: ["bed"], loop: true }, hit: { files: ["hit"] } } }, missing: { bed: hook, hit: hook }, preload: ["bed", "hit"], dragonSamples: false });
    audio.unlock(); await audio.ready(); expect(audio.play("bed")).toBe(0); expect(audio.loopBuffer("bed")?.duration).toBe(1);
    expect(audio.play("hit", 1, { variant: 9 })).toBe(0); expect(audio.play("none")).toBe(0); expect(hook).not.toHaveBeenCalled();
    expect(audio.stats().plays.none?.silent).toBe(1);
  });
  it("keeps identical playback logs and node counts for absent, empty, and 404 manifests", async () => {
    async function run(manifest?: AudioManifestSource) {
      FakeContext.all = []; f.calls = []; f.json("/assets/audio/missing", {}, false);
      const log: unknown[] = []; let audio!: SceneAudio<"hook" | "file", "fx" | "music">;
      audio = new SceneAudio<"hook" | "file", "fx" | "music">({ sounds: { hook: { bus: "fx", gain: 0.7, gap: 0.1 }, file: "file" }, buses, defaultBus: "fx", manifest, missing: { hook: (c, out) => { const node = out as unknown as FakeNode; log.push(["hook", c.currentTime, "fx", node.gain.value, "hook"]); return 0.1; } }, dragonSamples: false });
      audio.unlock(); await audio.ready();
      for (const [id, time] of [["hook", 0], ["file", 0], ["hook", 0.05], ["file", 0.1], ["hook", 0.2]] as const) {
        context().currentTime = time; const n = context().sources.length; audio.play(id);
        if (context().sources.length > n) { const source = context().sources.at(-1)!; log.push([id, time, "fx", source.connections[0]!.gain.value, "file"]); }
      }
      return { log, nodes: context().nodes.map(n => n.kind), stats: audio.stats().plays };
    }
    const absent = await run();
    expect(absent.log).toEqual([["hook", 0, "fx", 0.7, "hook"], ["file", 0, "fx", 1, "file"], ["file", 0.1, "fx", 1, "file"], ["hook", 0.2, "fx", 0.7, "hook"]]);
    expect(absent.nodes).toHaveLength(16);
    expect(await run({ version: 2, sounds: {} })).toEqual(absent); expect(await run("missing")).toEqual(absent);
  });
});
describe("scene music", () => {
  it("routes both music APIs through a destination bus, independent of sfxVolume, with pronunciation duck", async () => {
    const audio = new SceneAudio({ sounds: {}, buses, musicBus: "music", manifest: { music: { calm: "calm" } }, dragonSamples: false, musicVolume: 0.4 });
    audio.unlock(); await audio.ready(); expect(f.calls).toEqual([]); await audio.playTrack("calm");
    const ctx = context(); const bus = ctx.gains[2]!; const gain = ctx.sources[0]!.connections[0]!;
    expect(gain.connections).toEqual([bus]); expect(bus.connections).toEqual([ctx.destination]); expect(gain.gain.value).toBe(0.4);
    audio.setVolumes(0, 0.4); expect(gain.gain.value).toBe(0.4); expect(bus.gain.value).toBe(0.9);
    audio.setPronunciationActive(true); expect(bus.gain.value).toBeCloseTo(0.27);
    const pending = f.hold("/assets/audio/next");
    const next = audio.playMusic("next");
    expect(ctx.sources[0]!.stop).toHaveBeenCalledWith(2);
    pending.resolve(f.response()); await next; expect(ctx.sources.at(-1)!.connections[0]!.connections).toEqual([bus]); expect(ctx.sources[0]!.stop).toHaveBeenCalledWith(2);
    await audio.playTrack(null); expect(ctx.sources.at(-1)!.stop).toHaveBeenCalled();
  });
  it("without musicBus keeps direct destination routing", async () => {
    const audio = new SceneAudio({ sounds: {}, buses, dragonSamples: false }); audio.unlock(); await audio.ready(); await audio.playMusic("m");
    expect(context().sources[0]!.connections[0]!.connections).toEqual([context().destination]);
  });
  it("cancels a pending track on stop or replacement, preserving the newest request", async () => {
    const pending = f.hold("/assets/audio/slow"); const audio = new SceneAudio({ sounds: {}, dragonSamples: false }); audio.unlock();
    const slow = audio.playMusic("slow"); await audio.playMusic(null); pending.resolve(f.response()); await slow; expect(context().sources).toHaveLength(0);
    const a = f.hold("/assets/audio/a"); const first = audio.playMusic("a"); await audio.playMusic("b"); a.resolve(f.response()); await first; expect(context().sources).toHaveLength(1);
  });
});
