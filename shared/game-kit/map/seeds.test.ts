import { describe, expect, it } from "vitest";
import { cellSeed, hash32, layerSeed, rankKept, rankOf, RANK_SCALE } from "./index";

describe("map seeds and ranks", () => {
  it.each([
    [20261027, "vegetation", 1, 2739991112],
    [20261028, "fields", 1, 3301207131],
  ] as const)("matches layerSeed(%i, %s, %i): %i", (seed, layer, version, expected) => {
    expect(layerSeed(seed, layer, version)).toBe(expected);
  });

  it.each([[0, 0, 578876828], [-5, -4, 2270686687]])("matches cell (%i, %i): %i", (cx, cz, expected) => {
    expect(cellSeed(2739991112, cx!, cz!)).toBe(expected);
  });

  it.each([[0, 693049], [1, 191962], [2, 805752]])("matches candidate %i: %i", (k, expected) => {
    expect(rankOf(2270686687, k!)).toBe(expected);
  });

  it("keeps the golden populations and a monotonic density subset across 10000 candidates", () => {
    let sparse = 0;
    let dense = 0;
    for (let k = 0; k < 10000; k += 1) {
      const rank = rankOf(2739991112, k);
      const at350 = rankKept(rank, 350);
      const at550 = rankKept(rank, 550);
      if (at350) sparse += 1;
      if (at550) dense += 1;
      expect(!at350 || at550).toBe(true);
    }
    expect(sparse).toBe(3463);
    expect(dense).toBe(5519);
  });

  it("uses strict density thresholds and accepts range endpoints", () => {
    expect(RANK_SCALE).toBe(1000000);
    expect(rankKept(0, 0)).toBe(false);
    expect(rankKept(999999, 1000)).toBe(true);
    expect(rankKept(349999, 350)).toBe(true);
    expect(rankKept(350000, 350)).toBe(false);
    expect(cellSeed(-2147483648, -2147483648, 2147483647)).toBe(hash32(-2147483648, -2147483648, 2147483647));
    expect(rankOf(4294967295, 2147483647)).toBe(hash32(4294967295, "rank", 2147483647) % RANK_SCALE);
    expect(layerSeed(1, "x", 4294967295)).toBe(hash32(1, "x", 4294967295));
  });

  it.each([
    () => layerSeed(1, "", 1),
    () => layerSeed(1, true as never, 1),
    () => layerSeed(1, "x", 0),
    () => layerSeed(1, "x", 1.5),
    () => layerSeed(1, "x", Number.MAX_SAFE_INTEGER + 1),
    () => layerSeed(1, "x", 4294967296),
    () => layerSeed(NaN, "x", 1),
    () => cellSeed(1, 2147483648, 0),
    () => cellSeed(1, 0, 4294967295),
    () => cellSeed(1, -2147483649, 0),
    () => cellSeed(1, 0, 0.5),
    () => cellSeed(Infinity, 0, 0),
    () => rankOf(1, -1),
    () => rankOf(1, 2147483648),
    () => rankOf(1, NaN),
    () => rankOf(1, 0.5),
    () => rankOf(4294967296, 0),
    () => rankKept(0, 1001),
    () => rankKept(1000000, 5),
    () => rankKept(-1, 5),
    () => rankKept(0.5, 5),
    () => rankKept(0, -1),
    () => rankKept(0, 5.5),
    () => rankKept(NaN, 5),
    () => rankKept(0, Infinity),
  ])("rejects invalid seed/rank arguments (case %#)", (call) => {
    expect(call).toThrow(RangeError);
  });
});
