import { describe, expect, it } from "vitest";
import { RngStream } from "../platform/rng";
import { edtSquared, EDT_INF } from "./edt";
import { hash32 } from "./hash";
import { makeMask, rasterDisc } from "./raster";

function bruteForce(mask: Uint8Array, w: number): Int32Array {
  const sites = Array.from(mask.keys()).filter((k) => mask[k] !== 0);
  return Int32Array.from(mask, (_, k) => {
    let best = EDT_INF;
    for (const site of sites) {
      const dx = k % w - site % w;
      const dz = Math.floor(k / w) - Math.floor(site / w);
      best = Math.min(best, dx * dx + dz * dz);
    }
    return best;
  });
}

describe("Meijster squared EDT", () => {
  it("hand case: rasterized disc", () => {
    const grid = { originX: 0, originZ: 0, cellCm: 2, w: 5, h: 5 };
    const mask = makeMask(grid);
    rasterDisc(grid, mask, 5, 5, 2);
    expect(Array.from(edtSquared(mask, 5, 5))).toEqual([
      5, 2, 1, 2, 5,
      2, 1, 0, 1, 2,
      1, 0, 0, 0, 1,
      2, 1, 0, 1, 2,
      5, 2, 1, 2, 5,
    ]);
  });

  it("hand case: origin site", () => {
    const mask = new Uint8Array(25);
    mask[0] = 1;
    expect(Array.from(edtSquared(mask, 5, 5))).toEqual([
      0, 1, 4, 9, 16, 1, 2, 5, 10, 17, 4, 5, 8, 13, 20,
      9, 10, 13, 18, 25, 16, 17, 20, 25, 32,
    ]);
  });

  it("hand case: empty mask", () => {
    expect(Array.from(edtSquared(new Uint8Array(6), 3, 2))).toEqual(Array(6).fill(EDT_INF));
  });

  it("matches brute force on 200 seeded grids", () => {
    let cells = 0;
    for (let k = 1; k <= 200; k += 1) {
      const rng = new RngStream(hash32("edt", k));
      const w = k === 1 ? 1 : k === 2 ? 64 : rng.int(1, 64);
      const h = k === 1 ? 64 : k === 2 ? 1 : rng.int(1, 64);
      const mask = new Uint8Array(w * h);
      const p = rng.int(1, 600);
      for (let i = 0; i < mask.length; i += 1) mask[i] = Number(rng.int(1, 1000) <= p);
      if (k === 3 || k === 5) mask.fill(0);
      if (k === 4) mask.fill(1);
      if (k === 5) mask[rng.int(0, mask.length - 1)] = 1;
      const before = mask.slice();
      expect(edtSquared(mask, w, h), `edt seed ${k}, ${w}x${h}`).toEqual(bruteForce(mask, w));
      expect(mask).toEqual(before);
      cells += mask.length;
    }
    console.info(`edt brute-force: 200 grids; ${cells} cells compared`);
  }, 60000);

  it("reuses scratch across growing/shrinking calls while returning independent arrays", () => {
    const mask = new Uint8Array(63);
    mask[31] = 255;
    const first = edtSquared(mask, 7, 9);
    const snapshot = first.slice();
    const second = edtSquared(mask, 7, 9);
    expect(first).not.toBe(second);
    second.fill(-1);
    edtSquared(new Uint8Array(4096), 4096, 1);
    edtSquared(Uint8Array.of(2), 1, 1);
    expect(first).toEqual(snapshot);
    expect(first).toEqual(bruteForce(mask, 7));
    expect(edtSquared(Uint8Array.of(2), 1, 1)).toEqual(Int32Array.of(0));
  });

  it("handles maximum dimensions and their exact farthest squared distance", () => {
    const w = 4096;
    const mask = new Uint8Array(w * w);
    mask[0] = 1;
    const result = edtSquared(mask, w, w);
    expect(result[result.length - 1]).toBe(33538050);
    expect(result[4095]).toBe(16769025);
    expect(result[4095 * w]).toBe(16769025);
  });

  it.each([
    [0, 1, 0], [1, 4097, 4097], [2, 2, 3], [1.5, 2, 3],
    [1, 0, 0], [4097, 1, 4097], [NaN, 1, 0], [1, Infinity, 0],
  ])("rejects invalid dimensions or mask: %s x %s, length %s", (w, h, length) => {
    expect(() => edtSquared(new Uint8Array(length!), w!, h!)).toThrow(RangeError);
  });
});
