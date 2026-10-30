import { afterEach, describe, expect, it, vi } from "vitest";
import { loadAudioManifest, parseAudioManifest } from "./manifest";
import { FakeFetch } from "./fake-audio.test-helper";
afterEach(() => vi.unstubAllGlobals());
describe("manifest", () => {
  it("normalizes v1", () => {
    const m = parseAudioManifest({ sounds: { hit: ["a.ogg", "b.ogg"] }, music: { calm: "music/calm.ogg" } });
    expect(m).toEqual({ sounds: { hit: { files: ["a.ogg", "b.ogg"], loop: false } }, music: { calm: { file: "music/calm.ogg" } }, errors: [] });
  });
  it("normalizes v2 and strips mix policy", () => {
    const m = parseAudioManifest({ version: 2, sounds: { hit: { files: ["a"], durationMs: [100], loop: true, gain: 4, bus: "bad", priority: 1 } }, music: { calm: { file: "m", bpm: 96, bars: 8 } } });
    expect(m.sounds.hit).toEqual({ files: ["a"], durationMs: [100], loop: true });
    expect(m.music.calm).toEqual({ file: "m", bpm: 96, bars: 8 });
    expect(m.errors).toEqual([]);
  });
  it("drops only invalid entries", () => {
    const m = parseAudioManifest({ version: 2, sounds: { good: { files: ["ok"] }, bad: { files: "x" }, blank: { files: [" "] }, mismatch: { files: ["a"], durationMs: [] }, number: { files: [1] }, empty: { files: [] }, duration: { files: ["a"], durationMs: [-1] } }, music: { good: { file: "m" }, bad: { file: "" } } });
    expect(Object.keys(m.sounds)).toEqual(["good"]);
    expect(Object.keys(m.music)).toEqual(["good"]);
    expect(m.errors).toHaveLength(7);
  });
  it("rejects future versions entirely", () => {
    const m = parseAudioManifest({ version: 3, sounds: { hit: ["a"] }, music: { calm: "m" } });
    expect(m.sounds).toEqual({}); expect(m.music).toEqual({}); expect(m.errors).toHaveLength(1);
  });
  it("reports malformed roots and collections", () => {
    expect(parseAudioManifest(null).errors).toHaveLength(1);
    expect(parseAudioManifest({ sounds: [], music: 4 }).errors).toHaveLength(2);
  });
  it("loads valid JSON", async () => {
    const f = new FakeFetch(); f.install(); f.json("/m", { sounds: { hit: ["a"] } });
    expect((await loadAudioManifest("/m")).sounds.hit?.files).toEqual(["a"]);
  });
  it.each(["404", "network", "json"])("returns empty with errors on %s", async kind => {
    const f = new FakeFetch(); f.install();
    if (kind === "404") f.json("/m", {}, false);
    else if (kind === "network") f.fetch.mockImplementationOnce(async () => { throw Error("offline"); });
    else f.fetch.mockImplementationOnce(async () => ({ ...f.response(), json: async () => { throw Error("bad JSON"); } }) as Response);
    const m = await loadAudioManifest("/m");
    expect(m.sounds).toEqual({}); expect(m.music).toEqual({}); expect(m.errors).toHaveLength(1);
  });
});
