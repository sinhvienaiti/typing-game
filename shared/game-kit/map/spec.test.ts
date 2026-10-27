import { readFileSync } from "node:fs";
import { describe, expect, it } from "vitest";
import { sha256Hex } from "./sha256";
import { canonicalJson, specHash, validateSpec, SPEC_ERROR_CODES } from "./spec";
import type { SpecContext, SpecError, SpecErrorCode } from "./spec";

const readJson = (path: string) => JSON.parse(readFileSync(new URL(`../../../tools/map-factory/${path}`, import.meta.url), "utf8"));
const w1 = readJson("maps/typing-defense/w1-silverfall/map.spec.json");
const L2 = readJson("maps/dragon-hold/L2-cau/map.spec.json");
const fixtures = ["typing-defense.w1-silverfall", "dragon-hold.L2-cau"].map((name) => readJson(`test/fixtures/gameplay/${name}.json`));
const context: SpecContext = {
  gameplays: fixtures.map(({ game, map, adapter, commit, hash }) => ({ game, map, adapter, commit, hash })),
  kits: ["meadow", "pine-river"].map((name) => {
    const { kit, game, protos } = readJson(`registry/kits/${name}.json`);
    return { kit, game, protos: Object.keys(protos) };
  }),
};
const utf8 = new TextEncoder();
const badCases = [
  ["fractional-number", "not-integer", "/layers/water/streams/0/wobbleCm"],
  ["density-over-1000", "permille-range", "/layers/vegetation/groves/densityPermille"],
  ["unknown-proto", "proto-unknown", "/layers/vegetation/groves/mix/pine-giant"],
  ["gameplay-hash-mismatch", "gameplay-hash-mismatch", "/gameplay/hash"],
  ["bad-pin-id", "pin-id-format", "/pins/0/keep"],
  ["missing-budget", "budget-missing", "/budget"],
  ["odd-cell", "cell-not-even", "/extent/cellCm"],
] as const;

// JSON fixtures intentionally stay mutable so every invalid mutation can be expressed.
type Mutation = { n: number; sample: typeof w1; mutate: (s: typeof w1) => void; expected: SpecError[] };
const mutations: Mutation[] = [
  { n: 1, sample: w1, mutate: (s) => { delete s.format; }, expected: [{ code: "required", path: "/format" }] },
  { n: 2, sample: w1, mutate: (s) => { s.format = "map-spec/1"; }, expected: [{ code: "const", path: "/format" }] },
  { n: 3, sample: w1, mutate: (s) => { s.unit = "m"; }, expected: [{ code: "const", path: "/unit" }] },
  { n: 4, sample: w1, mutate: (s) => { s.seed = -1; }, expected: [{ code: "range", path: "/seed" }] },
  { n: 5, sample: w1, mutate: (s) => { s.seed = 1.5; }, expected: [{ code: "not-integer", path: "/seed" }] },
  { n: 6, sample: w1, mutate: (s) => { s.seed = "1"; }, expected: [{ code: "type", path: "/seed" }] },
  { n: 7, sample: w1, mutate: (s) => { s.id = "w1 silverfall"; }, expected: [{ code: "pattern", path: "/id" }] },
  { n: 8, sample: w1, mutate: (s) => { s.title = 5; }, expected: [{ code: "type", path: "/title" }] },
  { n: 9, sample: w1, mutate: (s) => { s.locks = {}; }, expected: [{ code: "unknown-key", path: "/locks" }] },
  { n: 10, sample: w1, mutate: (s) => { s.generator.layers.foliage = 1; }, expected: [{ code: "unknown-key", path: "/generator/layers/foliage" }] },
  { n: 11, sample: w1, mutate: (s) => { s.generator.layers.paint = 0; }, expected: [{ code: "range", path: "/generator/layers/paint" }] },
  { n: 12, sample: w1, mutate: (s) => { delete s.generator.layers.paint; }, expected: [{ code: "layer-version-missing", path: "/layers/paint" }] },
  { n: 13, sample: w1, mutate: (s) => { s.generator.factory = "0.1"; }, expected: [{ code: "pattern", path: "/generator/factory" }] },
  { n: 14, sample: w1, mutate: (s) => { s.gameplay.commit = s.gameplay.commit.toUpperCase(); }, expected: [{ code: "pattern", path: "/gameplay/commit" }] },
  { n: 15, sample: w1, mutate: (s) => { s.gameplay.adapter = "dragon-hold@1"; }, expected: [{ code: "pattern", path: "/gameplay/adapter" }] },
  { n: 16, sample: w1, mutate: (s) => { s.gameplay.adapter = "typing-defense@2"; }, expected: [{ code: "gameplay-adapter-mismatch", path: "/gameplay/adapter" }] },
  { n: 17, sample: w1, mutate: (s) => { s.gameplay.commit = "84d0ac116b396df2b341ed4330461653a05fd8b2"; }, expected: [{ code: "gameplay-commit-mismatch", path: "/gameplay/commit" }] },
  { n: 18, sample: w1, mutate: (s) => { s.id = "w1-silverfall-b"; }, expected: [{ code: "gameplay-missing", path: "/gameplay" }] },
  { n: 19, sample: w1, mutate: (s) => { s.registry.kit = "meadow"; }, expected: [{ code: "pattern", path: "/registry/kit" }] },
  { n: 20, sample: w1, mutate: (s) => { s.registry.kit = "meadow@2"; }, expected: [{ code: "kit-unknown", path: "/registry/kit" }] },
  { n: 21, sample: w1, mutate: (s) => { s.registry.kit = "pine-river@1"; }, expected: [{ code: "kit-unknown", path: "/registry/kit" }] },
  { n: 22, sample: w1, mutate: (s) => { s.registry.scan = "27/10/2026"; }, expected: [{ code: "pattern", path: "/registry/scan" }] },
  { n: 23, sample: w1, mutate: (s) => { delete s.extent.cellCm; }, expected: [{ code: "required", path: "/extent/cellCm" }] },
  { n: 24, sample: w1, mutate: (s) => { s.extent.skirtCm = 0; }, expected: [{ code: "range", path: "/extent/skirtCm" }] },
  { n: 25, sample: w1, mutate: (s) => { s.extent.field = 4800; }, expected: [{ code: "unknown-key", path: "/extent/field" }] },
  { n: 26, sample: w1, mutate: (s) => { s.review.yawsDeg = [0, 360]; }, expected: [{ code: "range", path: "/review/yawsDeg/1" }] },
  { n: 27, sample: w1, mutate: (s) => { s.review.pitchesDeg = []; }, expected: [{ code: "range", path: "/review/pitchesDeg" }] },
  { n: 28, sample: w1, mutate: (s) => { s.layers.water.streams[0].wobbleCm = null; }, expected: [{ code: "type", path: "/layers/water/streams/0/wobbleCm" }] },
  { n: 29, sample: w1, mutate: (s) => { s.layers.height.stamps[0].heightCm = 100001; }, expected: [{ code: "range", path: "/layers/height/stamps/0/heightCm" }] },
  { n: 30, sample: w1, mutate: (s) => { s.layers.height.stamps[0].heightCm = -300; }, expected: [] },
  { n: 31, sample: w1, mutate: (s) => { s.layers.dressing.landmarks[3].yawDeg = 400; }, expected: [{ code: "range", path: "/layers/dressing/landmarks/3/yawDeg" }] },
  { n: 32, sample: w1, mutate: (s) => { s.layers.dressing.along[0].skipNearCm.gate = 100001; }, expected: [{ code: "range", path: "/layers/dressing/along/0/skipNearCm/gate" }] },
  { n: 33, sample: w1, mutate: (s) => { s.layers.dressing.along[0].skipNearCm.gateMs = 70000; }, expected: [{ code: "range", path: "/layers/dressing/along/0/skipNearCm/gateMs" }] },
  { n: 34, sample: w1, mutate: (s) => { s.layers.vegetation.edge.densityPermille = -1; }, expected: [{ code: "permille-range", path: "/layers/vegetation/edge/densityPermille" }] },
  { n: 35, sample: w1, mutate: (s) => { s.layers.vegetation.groves.radiusCm = [500, 1000.5]; }, expected: [{ code: "not-integer", path: "/layers/vegetation/groves/radiusCm/1" }] },
  { n: 36, sample: w1, mutate: (s) => { s.layers.paint.tintNoiseCm = 100001; }, expected: [{ code: "range", path: "/layers/paint/tintNoiseCm" }] },
  { n: 37, sample: w1, mutate: (s) => { s.layers.paint.decals["a/b~c"] = 1.5; }, expected: [{ code: "not-integer", path: "/layers/paint/decals/a~1b~0c" }] },
  { n: 38, sample: w1, mutate: (s) => { s.pins[1].scalePermille = 0; }, expected: [{ code: "range", path: "/pins/1/scalePermille" }] },
  { n: 39, sample: w1, mutate: (s) => { s.pins[1].scalePermille = 10001; }, expected: [{ code: "range", path: "/pins/1/scalePermille" }] },
  { n: 40, sample: w1, mutate: (s) => { s.layers.dressing.along[0].proto = "Lamp-Post"; }, expected: [{ code: "pattern", path: "/layers/dressing/along/0/proto" }] },
  { n: 41, sample: w1, mutate: (s) => { s.layers.dressing.along[0].proto = 5; }, expected: [{ code: "type", path: "/layers/dressing/along/0/proto" }] },
  { n: 42, sample: w1, mutate: (s) => { s.layers.dressing.along[0].proto = "lamp-pots"; }, expected: [{ code: "proto-unknown", path: "/layers/dressing/along/0/proto" }] },
  { n: 43, sample: w1, mutate: (s) => { s.layers.vegetation.decorTrees.mix["almond-tree"] = 0; }, expected: [{ code: "range", path: "/layers/vegetation/decorTrees/mix/almond-tree" }] },
  { n: 44, sample: w1, mutate: (s) => { s.layers.vegetation.gameplayTrees.mix["mountain-pine"] = 2.5; }, expected: [{ code: "not-integer", path: "/layers/vegetation/gameplayTrees/mix/mountain-pine" }] },
  { n: 45, sample: w1, mutate: (s) => { s.layers.vegetation.clutter.mix.Fern = 1; }, expected: [{ code: "pattern", path: "/layers/vegetation/clutter/mix/Fern" }] },
  { n: 46, sample: w1, mutate: (s) => { s.layers.vegetation.groves.mix = ["fern"]; }, expected: [{ code: "type", path: "/layers/vegetation/groves/mix" }] },
  { n: 47, sample: w1, mutate: (s) => { s.layers.height.stamps[0].id = "rainbow hill"; }, expected: [{ code: "pattern", path: "/layers/height/stamps/0/id" }] },
  { n: 48, sample: w1, mutate: (s) => { s.exclude[0].poly = s.exclude[0].poly.slice(0, 2); }, expected: [{ code: "range", path: "/exclude/0/poly" }] },
  { n: 49, sample: w1, mutate: (s) => { s.exclude[0].poly[0] = [1, 2, 3]; }, expected: [{ code: "type", path: "/exclude/0/poly/0" }] },
  { n: 50, sample: w1, mutate: (s) => { s.exclude[0].poly[0] = [16385, 3200]; }, expected: [{ code: "range", path: "/exclude/0/poly/0/0" }] },
  { n: 51, sample: w1, mutate: (s) => { s.pins[0].keep = "veg:groves:c-0_-4:2"; }, expected: [{ code: "pin-id-format", path: "/pins/0/keep" }] },
  { n: 52, sample: w1, mutate: (s) => { s.pins[0].keep = "veg:groves:c-5_-4:2147483648"; }, expected: [{ code: "pin-id-format", path: "/pins/0/keep" }] },
  { n: 53, sample: w1, mutate: (s) => { delete s.pins[1].at; }, expected: [{ code: "required", path: "/pins/1/at" }] },
  { n: 54, sample: w1, mutate: (s) => { s.pins[1].colour = "red"; }, expected: [{ code: "unknown-key", path: "/pins/1/colour" }] },
  { n: 55, sample: w1, mutate: (s) => { s.pins[0].note = "x"; }, expected: [{ code: "unknown-key", path: "/pins/0/note" }] },
  { n: 56, sample: w1, mutate: (s) => { delete s.budget.high.drawCalls; }, expected: [{ code: "required", path: "/budget/high/drawCalls" }] },
  { n: 57, sample: w1, mutate: (s) => { s.budget.ultra = { propTriangles: 1, drawCalls: 1, loadMs: 1 }; }, expected: [{ code: "unknown-key", path: "/budget/ultra" }] },
  { n: 58, sample: w1, mutate: (s) => { delete s.budget.high; }, expected: [{ code: "budget-missing", path: "/budget/high" }] },
  { n: 59, sample: w1, mutate: (s) => { s.layers.foliage = {}; }, expected: [{ code: "unknown-key", path: "/layers/foliage" }] },
  { n: 60, sample: w1, mutate: (s) => { s.layers.paint = []; }, expected: [{ code: "type", path: "/layers/paint" }] },
  { n: 61, sample: L2, mutate: (s) => { s.layers.dressing = {}; }, expected: [{ code: "layer-version-missing", path: "/layers/dressing" }] },
  { n: 62, sample: L2, mutate: (s) => { s.gameplay.adapter = "typing-defense@1"; }, expected: [{ code: "pattern", path: "/gameplay/adapter" }] },
  { n: 63, sample: L2, mutate: (s) => { delete s.gameplay; }, expected: [{ code: "required", path: "/gameplay" }] },
];

function expectErrors(value: unknown, expected: readonly SpecError[], ctx?: SpecContext): void {
  const actual = validateSpec(value, ctx);
  expect(actual, JSON.stringify(actual)).toEqual(expected);
}

describe("canonicalJson", () => {
  it.each([
    [{ b: 1, B: 2, a: 3, _: 4 }, '{"B":2,"_":4,"a":3,"b":1}'],
    [{ b: 1, a: [true, null, "x"] }, '{"a":[true,null,"x"],"b":1}'],
    [-0, "0"],
    ["Thác Bạc", '"Thác Bạc"'],
    ['a"b\n', '"a\\"b\\n"'],
  ])("writes canonical JSON for %j", (value, expected) => {
    expect(canonicalJson(value)).toBe(expected);
  });

  it.each([1.5, NaN, Infinity, 9007199254740992, undefined, { a: undefined }, [1, , 2], () => 1, 1n].map((value) => ({ value })))("rejects unsupported value $#", ({ value }) => {
    expect(() => canonicalJson(value)).toThrow(TypeError);
  });

  it.each(fixtures)("matches ticket 028 hash for $game", (fixture) => {
    const { commit, hash, ...gameplay } = fixture;
    expect(sha256Hex(utf8.encode(canonicalJson(gameplay)))).toBe(hash);
  });
});

describe("MapSpec v0", () => {
  it.each([
    [w1, 3189, "d304337326698ceb407b6352e2c2ba8bffcb0effe53358cc7347e3be877e6f16"],
    [L2, 1145, "e77ce877fbcf6acb4baa04818249b770276d3c9a71ba508913bc85af64f6db83"],
  ] as const)("matches byte length and golden spec hash for $0.id", (spec, length, hash) => {
    expect(utf8.encode(canonicalJson(spec)).length).toBe(length);
    expect(specHash(spec)).toBe(hash);
  });

  it.each([w1, L2])("accepts clean sample $id with and without context", (spec) => {
    expectErrors(spec, [], context);
    expectErrors(spec, []);
  });

  it.each(badCases)("reports only the intended error for %s", (name, code, path) => {
    const spec = readJson(`test/fixtures/bad-spec/${name}/map.spec.json`);
    const expected = [{ code, path }];
    expectErrors(spec, expected, context);
    expectErrors(spec, name === "unknown-proto" || name === "gameplay-hash-mismatch" ? [] : expected);
  });

  it.each(mutations)("matches mutation $n", ({ sample, mutate, expected }) => {
    const s = structuredClone(sample);
    mutate(s);
    expectErrors(s, expected, context);
  });

  it("sorts and deduplicates all six errors", () => {
    const s = structuredClone(w1);
    s.seed = 1.5; s.unit = "m"; delete s.budget; s.locks = 1;
    s.pins[0].keep = "veg"; s.layers.vegetation.groves.densityPermille = 1001;
    expectErrors(s, [
      { code: "budget-missing", path: "/budget" },
      { code: "permille-range", path: "/layers/vegetation/groves/densityPermille" },
      { code: "unknown-key", path: "/locks" },
      { code: "pin-id-format", path: "/pins/0/keep" },
      { code: "not-integer", path: "/seed" },
      { code: "const", path: "/unit" },
    ]);
  });

  it.each([[1], null, "x", undefined, 1, false].map((value) => ({ value })))("rejects non-object root $# without throwing", ({ value }) => {
    expectErrors(value, [{ code: "type", path: "" }]);
  });

  it("exports exactly the fixed 19 codes, all non-CLI codes exercised by cases 5–8", () => {
    expect(SPEC_ERROR_CODES).toEqual([
      "spec-json", "type", "required", "unknown-key", "not-integer", "range", "permille-range", "pattern", "const",
      "cell-not-even", "layer-version-missing", "pin-id-format", "budget-missing", "gameplay-missing",
      "gameplay-adapter-mismatch", "gameplay-commit-mismatch", "gameplay-hash-mismatch", "kit-unknown", "proto-unknown",
    ]);
    const seen = new Set<SpecErrorCode>();
    for (const [name] of badCases) for (const error of validateSpec(readJson(`test/fixtures/bad-spec/${name}/map.spec.json`), context)) seen.add(error.code);
    for (const { sample, mutate } of mutations) {
      const s = structuredClone(sample);
      mutate(s);
      for (const error of validateSpec(s, context)) seen.add(error.code);
    }
    seen.add(validateSpec(null)[0]!.code);
    expect([...seen].sort()).toEqual(SPEC_ERROR_CODES.filter((code) => code !== "spec-json").sort());
  });

  it("checks generic layer units without interpreting any layer meanings", () => {
    const s = structuredClone(L2);
    s.layers.height = {
      count: [9, 6], fromGameplay: "absent/99", fit: "bridge/999", freeInteger: -9007199254740991,
      offsetCm: { nested: [-100000, 100000], gateMs: 60000 }, scalePermille: [1, 10000], densityPermille: [0, 1000],
    };
    expectErrors(s, [], context);
  });

  it("does not cascade from missing, unknown, wrongly typed or fractional values", () => {
    const s = structuredClone(L2);
    s.generator = []; s.extent = []; s.review = { pitchesDeg: [0.5], yawsDeg: [] };
    s.layers = { foliage: { proto: "unknown" }, paint: { densityPermille: 1000.5, mix: { Fern: 0 } } };
    expectErrors(s, [
      { code: "type", path: "/extent" }, { code: "type", path: "/generator" },
      { code: "unknown-key", path: "/layers/foliage" },
      { code: "not-integer", path: "/layers/paint/densityPermille" },
      { code: "pattern", path: "/layers/paint/mix/Fern" }, { code: "range", path: "/layers/paint/mix/Fern" },
      { code: "not-integer", path: "/review/pitchesDeg/0" }, { code: "range", path: "/review/yawsDeg" },
    ], context);
  });

  it("does not mutate inputs and uses the first matching gameplay reference", () => {
    const s = structuredClone(w1);
    const before = canonicalJson(s);
    const ctx = { ...context, gameplays: [...context.gameplays!, { ...context.gameplays![0]!, hash: "0".repeat(64) }] };
    expectErrors(s, [], ctx);
    expect(canonicalJson(s)).toBe(before);
  });
});
