// Source: new for the kit: manifest parsing, URL resolution and the multi-manifest library (no WebGL)
import { describe, expect, it } from "vitest";
import { MODEL_CONTRACTS, MODEL_KINDS, isModelKind, missingClips, missingSockets, modelKey } from "./model-contracts";
import { ModelLibrary, SPACE_MODEL_MANIFEST_URL, parseModelManifest, pickModelTier, resolveModelUrl, type ManifestFetch } from "./model-loader";

const GAME = "/assets/dragon-hold/models/manifest.json";

const entry = (kind: string, id: string, tiers: Record<string, unknown>, extra: Record<string, unknown> = {}) => ({ kind, id, tiers, triangles: 1200, sockets: ["FX_CORE"], clips: ["Enemy_Idle"], size: [1, 2, 1], ...extra });

/** A fetch over a table of URL → JSON (or a status), counting calls. */
function fakeFetch(table: Record<string, unknown>): ManifestFetch & { calls: string[] } {
  const calls: string[] = [];
  const fetcher = async (url: string) => {
    calls.push(url);
    const body = table[url];
    if (body === undefined) return { ok: false, headers: { get: () => "text/html" }, json: async () => null };
    if (body instanceof Error) throw body;
    return { ok: true, headers: { get: (name: string) => (name === "content-type" ? "application/json; charset=utf-8" : null) }, json: async () => body };
  };
  return Object.assign(fetcher, { calls });
}

describe("model contracts", () => {
  it("know Space's kinds plus units and props, each with a contract of its own kind", () => {
    expect(MODEL_KINDS).toEqual(["ships", "enemies", "bosses", "skills", "items", "heroes", "guides", "units", "props"]);
    for (const kind of MODEL_KINDS) expect(MODEL_CONTRACTS[kind].kind).toBe(kind);
    expect(isModelKind("units") && isModelKind("props")).toBe(true);
    expect(isModelKind("traps")).toBe(false);
    expect(modelKey("units", "ve-binh-reu")).toBe("units/ve-binh-reu");
  });

  it("report missing sockets by name and missing clips by substring (a _V3 suffix passes)", () => {
    expect(missingSockets(MODEL_CONTRACTS.bosses, ["FX_CORE", "FX_HALO"])).toEqual(["FX_CAST_L", "FX_CAST_R"]);
    expect(missingClips(MODEL_CONTRACTS.bosses, ["__EXPORT__00_Boss_Idle_Hover_V3"])).toEqual([]);
    expect(missingClips(MODEL_CONTRACTS.guides, ["Guide_Wave"])).toEqual(["Guide_Idle"]);
    expect(missingSockets(MODEL_CONTRACTS.props, [])).toEqual([]);
    expect(MODEL_CONTRACTS.enemies.optionalSockets).toContain("FX_HEAD");
  });
});

describe("model URLs", () => {
  it("keep root-relative and absolute URLs, query and all; resolve the rest against the manifest's folder", () => {
    expect(resolveModelUrl("/assets/space-typing/models/guides/a.high.glb?v=1", GAME)).toBe("/assets/space-typing/models/guides/a.high.glb?v=1");
    expect(resolveModelUrl("https://cdn.example.org/m.glb", GAME)).toBe("https://cdn.example.org/m.glb");
    expect(resolveModelUrl("enemies/e09/e09.high.glb?v=ab", GAME)).toBe("/assets/dragon-hold/models/enemies/e09/e09.high.glb?v=ab");
    expect(resolveModelUrl("./units/u.glb", GAME)).toBe("/assets/dragon-hold/models/units/u.glb");
    expect(resolveModelUrl("../shared/p.glb#x", GAME)).toBe("/assets/dragon-hold/shared/p.glb#x");
    expect(resolveModelUrl("props/p.glb", "https://game.local/assets/dragon-hold/models/manifest.json")).toBe("https://game.local/assets/dragon-hold/models/props/p.glb");
  });

  it("pick the tier for the quality: none on low, medium first on medium, high first on high and ultra", () => {
    const both = { kind: "enemies" as const, id: "x", tiers: { high: { url: "h", bytes: 2 }, medium: { url: "m", bytes: 1 } }, triangles: 0, sockets: [], clips: [], size: [1, 1, 1] as [number, number, number] };
    expect(pickModelTier(both, "low")).toBeNull();
    expect(pickModelTier(both, "medium")).toBe("m");
    expect(pickModelTier(both, "high")).toBe("h");
    expect(pickModelTier(both, "ultra")).toBe("h");
    expect(pickModelTier({ ...both, tiers: { high: { url: "h", bytes: 2 } } }, "medium")).toBe("h");
    expect(pickModelTier({ ...both, tiers: { medium: { url: "m", bytes: 1 } } }, "ultra")).toBe("m");
  });
});

describe("manifest parsing", () => {
  it("takes only version 1 with a models object", () => {
    expect(parseModelManifest(null, GAME)).toBeNull();
    expect(parseModelManifest({ version: 2, models: {} }, GAME)).toBeNull();
    expect(parseModelManifest({ version: 1, models: [] }, GAME)).toBeNull();
    expect(parseModelManifest({ version: 1, generatedAt: "t", models: {} }, GAME)).toEqual({ version: 1, generatedAt: "t", models: {}, dropped: 0 });
  });

  it("files entries under kind/id with resolved URLs and safe defaults; drops unknown kinds and entries with no tier", () => {
    const manifest = parseModelManifest(
      {
        version: 1,
        generatedAt: "2026-10-23T00:00:00Z",
        models: {
          "enemies/e09": entry("enemies", "e09", { high: { url: "enemies/e09/e09.high.glb?v=1", bytes: 900 }, medium: { url: "enemies/e09/e09.medium.glb?v=2" } }),
          "wrong-key": entry("units", "ve-binh-reu", { medium: { url: "/assets/dragon-hold/models/units/vbr.medium.glb", bytes: 10 } }, { size: "big", sockets: ["FX_CORE", 7], clips: null }),
          "traps/gai": entry("traps", "gai", { high: { url: "traps/gai.glb", bytes: 1 } }),
          "props/empty": entry("props", "empty", { high: { bytes: 1 } }),
          "bad": 5,
        },
      },
      GAME,
    )!;
    expect(manifest.dropped).toBe(3);
    expect(Object.keys(manifest.models)).toEqual(["enemies/e09", "units/ve-binh-reu"]);
    expect(manifest.models["enemies/e09"]!.tiers).toEqual({
      high: { url: "/assets/dragon-hold/models/enemies/e09/e09.high.glb?v=1", bytes: 900 },
      medium: { url: "/assets/dragon-hold/models/enemies/e09/e09.medium.glb?v=2", bytes: 0 },
    });
    expect(manifest.models["units/ve-binh-reu"]).toMatchObject({ size: [1, 1, 1], sockets: ["FX_CORE"], clips: [], triangles: 1200 });
  });
});

describe("model library", () => {
  const game = { version: 1, models: { "guides/bach-long": entry("guides", "bach-long", { high: { url: "guides/bach-long.high.glb", bytes: 1 } }) } };
  const space = {
    version: 1,
    models: {
      "guides/bach-long": entry("guides", "bach-long", { high: { url: "/assets/space-typing/models/guides/old.glb", bytes: 1 } }),
      "enemies/e01": entry("enemies", "e01", { medium: { url: "/assets/space-typing/models/enemies/e01.medium.glb", bytes: 1 } }),
    },
  };

  it("asks every manifest once, the first that lists a model wins, the others fill in", async () => {
    const fetcher = fakeFetch({ [GAME]: game, [SPACE_MODEL_MANIFEST_URL]: space });
    const library = new ModelLibrary({ manifests: [GAME, SPACE_MODEL_MANIFEST_URL], fetcher });
    expect(await library.url("guides", "bach-long", "high")).toBe("/assets/dragon-hold/models/guides/bach-long.high.glb");
    expect(await library.url("enemies", "e01", "high")).toBe("/assets/space-typing/models/enemies/e01.medium.glb");
    expect(await library.url("enemies", "e01", "low")).toBeNull();
    expect(await library.entry("props", "nothing")).toBeNull();
    expect(fetcher.calls.sort()).toEqual([GAME, SPACE_MODEL_MANIFEST_URL].sort());
  });

  it("a manifest that is missing, not JSON or throws is null, and is asked again only after the retry time", async () => {
    let now = 1000;
    const table: Record<string, unknown> = { [SPACE_MODEL_MANIFEST_URL]: space, "/broken.json": new Error("offline") };
    const fetcher = fakeFetch(table);
    const library = new ModelLibrary({ manifests: [GAME, "/broken.json", SPACE_MODEL_MANIFEST_URL], fetcher, retryMs: 30_000, now: () => now });
    expect(await library.manifest(GAME)).toBeNull();
    expect(await library.manifest("/broken.json")).toBeNull();
    expect(await library.url("enemies", "e01", "medium")).toBe("/assets/space-typing/models/enemies/e01.medium.glb");
    const asked = fetcher.calls.length;
    now += 29_999;
    await library.manifests();
    expect(fetcher.calls.length).toBe(asked);
    // The game's manifest arrives (a media pull): picked up after the retry time.
    table[GAME] = game;
    now += 1;
    expect(await library.url("guides", "bach-long", "high")).toBe("/assets/dragon-hold/models/guides/bach-long.high.glb");
    expect(fetcher.calls.length).toBe(asked + 2);
    library.reset();
    await library.manifests();
    expect(fetcher.calls.length).toBe(asked + 5);
  });

  it("needs at least one manifest URL", () => {
    expect(() => new ModelLibrary({ manifests: [] })).toThrow();
    expect(new ModelLibrary({ manifests: GAME }).urls).toEqual([GAME]);
  });
});
