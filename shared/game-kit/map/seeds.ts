import { hash32 } from "./hash";

export const RANK_SCALE = 1_000_000;

/** Each layer uses layerSeed(spec.seed, layer, generator.layers[layer]). */
export function layerSeed(mapSeed: number, layer: string, version: number): number {
  if (typeof layer !== "string" || layer.length === 0) {
    throw new RangeError("Layer names must be nonempty strings");
  }
  if (!Number.isSafeInteger(version) || version < 1) {
    throw new RangeError("Layer versions must be positive safe integers");
  }
  return hash32(mapSeed, layer, version);
}

/** Scatter independently in each cell using cellSeed(layerSeed, cx, cz). */
export function cellSeed(seed: number, cx: number, cz: number): number {
  for (const coordinate of [cx, cz]) {
    if (!Number.isInteger(coordinate) || coordinate < -2147483648 || coordinate > 2147483647) {
      throw new RangeError("Cell coordinates must be signed 32-bit integers");
    }
  }
  return hash32(seed, cx, cz);
}

/** The millionth-scale rank of candidate k, independent of density. */
export function rankOf(seed: number, k: number): number {
  if (!Number.isInteger(k) || k < 0 || k > 2147483647) {
    throw new RangeError("Candidate indices must be integers in [0, 2147483647]");
  }
  return hash32(seed, "rank", k) % RANK_SCALE;
}

/** Increasing density adds candidates without moving previously kept objects. */
export function rankKept(rank: number, densityPermille: number): boolean {
  if (!Number.isInteger(rank) || rank < 0 || rank >= RANK_SCALE) {
    throw new RangeError("Ranks must be integers in [0, 999999]");
  }
  if (!Number.isInteger(densityPermille) || densityPermille < 0 || densityPermille > 1000) {
    throw new RangeError("Density must be an integer in [0, 1000] permille");
  }
  return rank < densityPermille * 1000;
}
