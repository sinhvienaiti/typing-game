import { describe, expect, it } from "vitest";
import { RngStream } from "../platform/rng";
import { hash32 } from "./hash";
import {
  cellCenterX, cellCenterZ, makeMask, rasterDisc, rasterPolygon, rasterPolyline, rasterRect,
  RASTER_LIMIT_CM, RASTER_MAX_HALF_WIDTH_CM, type RasterGrid, type RasterPoint,
} from "./raster";

const G0: RasterGrid = { originX: 0, originZ: 0, cellCm: 2, w: 5, h: 5 };
type Shape =
  | { kind: "disc"; at: RasterPoint; r: number }
  | { kind: "rect"; a: RasterPoint; b: RasterPoint }
  | { kind: "line"; points: readonly RasterPoint[]; hw: number }
  | { kind: "polygon"; points: readonly RasterPoint[] };

function paint(grid: RasterGrid, mask: Uint8Array, shape: Shape): void {
  switch (shape.kind) {
    case "disc": rasterDisc(grid, mask, ...shape.at, shape.r); break;
    case "rect": rasterRect(grid, mask, ...shape.a, ...shape.b); break;
    case "line": rasterPolyline(grid, mask, shape.points, shape.hw); break;
    case "polygon": rasterPolygon(grid, mask, shape.points); break;
  }
}

type BigPoint = readonly [bigint, bigint];
const bigPoint = ([x, z]: RasterPoint): BigPoint => [BigInt(x), BigInt(z)];
const square = (x: bigint): bigint => x * x;
const between = (v: bigint, a: bigint, b: bigint): boolean => a <= b ? a <= v && v <= b : b <= v && v <= a;

// Brute force visits every cell and uses exact arithmetic, without bounding boxes.
function oracle(shape: Shape): (x: number, z: number) => boolean {
  if (shape.kind === "disc") {
    const [ax, az] = bigPoint(shape.at);
    return (x, z) => square(BigInt(x) - ax) + square(BigInt(z) - az) <= square(BigInt(shape.r));
  }
  if (shape.kind === "rect") {
    const [ax, az] = bigPoint(shape.a);
    const [bx, bz] = bigPoint(shape.b);
    return (x, z) => ax <= BigInt(x) && BigInt(x) <= bx && az <= BigInt(z) && BigInt(z) <= bz;
  }
  const points = shape.points.map(bigPoint);
  if (shape.kind === "line") {
    const hw2 = square(BigInt(shape.hw));
    return (x, z) => {
      const px = BigInt(x);
      const pz = BigInt(z);
      for (let k = 0; k < Math.max(1, points.length - 1); k += 1) {
        const [ax, az] = points[k]!;
        const [bx, bz] = points[Math.min(k + 1, points.length - 1)]!;
        const dx = bx - ax;
        const dz = bz - az;
        const ux = px - ax;
        const uz = pz - az;
        const len2 = square(dx) + square(dz);
        const dot = ux * dx + uz * dz;
        const uu = square(ux) + square(uz);
        if (len2 === 0n || dot <= 0n) {
          if (uu <= hw2) return true;
        } else if (dot >= len2) {
          if (square(px - bx) + square(pz - bz) <= hw2) return true;
        } else if (uu * len2 - square(dot) <= hw2 * len2) {
          return true;
        }
      }
      return false;
    };
  }
  return (x, z) => {
    const px = BigInt(x);
    const pz = BigInt(z);
    let inside = false;
    for (let k = 0; k < points.length; k += 1) {
      const [ax, az] = points[k]!;
      const [bx, bz] = points[(k + 1) % points.length]!;
      const cross = (bx - ax) * (pz - az) - (bz - az) * (px - ax);
      if (cross === 0n && between(px, ax, bx) && between(pz, az, bz)) return true;
      if ((az > pz) !== (bz > pz) && (bz > az ? cross > 0n : cross < 0n)) inside = !inside;
    }
    return inside;
  };
}

const handCases: readonly [string, Shape, readonly number[]][] = [
  ["disc radius 2", { kind: "disc", at: [5, 5], r: 2 }, [7, 11, 12, 13, 17]],
  ["disc zero off-center", { kind: "disc", at: [4, 4], r: 0 }, []],
  ["disc zero on-center", { kind: "disc", at: [5, 5], r: 0 }, [12]],
  ["closed rect", { kind: "rect", a: [3, 3], b: [7, 5] }, [6, 7, 8, 11, 12, 13]],
  ["rect zero width off-center", { kind: "rect", a: [4, 0], b: [4, 10] }, []],
  ["rect zero width on-center", { kind: "rect", a: [5, 0], b: [5, 10] }, [2, 7, 12, 17, 22]],
  ["line width zero", { kind: "line", points: [[1, 1], [9, 1]], hw: 0 }, [0, 1, 2, 3, 4]],
  ["diagonal width 1", { kind: "line", points: [[1, 1], [9, 9]], hw: 1 }, [0, 6, 12, 18, 24]],
  ["diagonal width 2", { kind: "line", points: [[1, 1], [9, 9]], hw: 2 }, [0, 1, 5, 6, 7, 11, 12, 13, 17, 18, 19, 23, 24]],
  ["single point", { kind: "line", points: [[5, 5]], hw: 2 }, [7, 11, 12, 13, 17]],
  ["triangle", { kind: "polygon", points: [[0, 0], [10, 0], [0, 10]] }, [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 15, 16, 20]],
  ["polygon boundary", { kind: "polygon", points: [[1, 1], [5, 1], [5, 5], [1, 5]] }, [0, 1, 2, 5, 6, 7, 10, 11, 12]],
  ["self-intersecting bow tie", { kind: "polygon", points: [[0, 0], [10, 10], [10, 0], [0, 10]] }, [0, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 24]],
];

function seededCase(k: number, rng: RngStream): { grid: RasterGrid; shape: Shape } {
  const cellCm = k === 14 ? 2 : [2, 50, 200][rng.int(0, 2)]!;
  const w = rng.int(1, 64);
  const h = rng.int(1, 64);
  const grid = {
    originX: rng.int(-16384, 16384 - w * cellCm),
    originZ: rng.int(-16384, 16384 - h * cellCm), cellCm, w, h,
  };
  const clamp = (v: number): number => Math.max(-16384, Math.min(16384, v));
  const coord = (origin: number, count: number): number => {
    const base = Math.round(origin / (cellCm / 2)) * (cellCm / 2);
    const offset = rng.int(0, 3) === 0 ? (rng.int(0, 1) ? 1 : -1) * rng.int(1, 3) : 0;
    return clamp(base + rng.int(-count, 3 * count) * (cellCm / 2) + offset);
  };
  const point = (): RasterPoint => [coord(grid.originX, w), coord(grid.originZ, h)];
  const center: RasterPoint = [cellCenterX(grid, Math.floor(w / 2)), cellCenterZ(grid, Math.floor(h / 2))];
  // A far corner is at least 8 km from this small grid on one axis.
  const outside: RasterPoint = [grid.originX >= 0 ? -16384 : 16384, grid.originZ >= 0 ? -16384 : 16384];
  const corners: readonly RasterPoint[] = [
    [grid.originX, grid.originZ], [grid.originX + w * cellCm, grid.originZ],
    [grid.originX + w * cellCm, grid.originZ + h * cellCm], [grid.originX, grid.originZ + h * cellCm],
  ];
  if (k % 4 === 0) {
    return { grid, shape: { kind: "disc", at: k === 8 ? outside : k === 12 ? center : point(), r: k === 4 || k === 8 ? 0 : k === 12 ? 32768 : rng.int(0, 32768) } };
  }
  if (k % 4 === 1) {
    const a = point();
    const b = point();
    return { grid, shape: { kind: "rect",
      a: k === 5 ? outside : k === 9 ? corners[0]! : [Math.min(a[0], b[0]), Math.min(a[1], b[1])],
      b: k === 5 ? outside : k === 9 ? corners[2]! : [k === 1 ? Math.min(a[0], b[0]) : Math.max(a[0], b[0]), Math.max(a[1], b[1])],
    } };
  }
  if (k % 4 === 2) {
    const points = Array.from({ length: rng.int(1, 7) }, point);
    if (k === 6) points.splice(1, 0, points[0]!);
    return { grid, shape: { kind: "line", points: k === 2 ? [center] : k === 10 ? [outside, outside] : k === 14 ? [center] : points, hw: k === 10 ? 0 : k === 14 ? 2000 : rng.int(0, 2000) } };
  }
  return { grid, shape: { kind: "polygon", points: k === 3 ? [corners[0]!, corners[2]!, corners[1]!, corners[3]!] : k === 7 ? [outside, outside, outside] : k === 11 ? corners : Array.from({ length: rng.int(3, 8) }, point) } };
}

describe("raster cell-center rules", () => {
  it.each(handCases)("hand case: %s", (_name, shape, indices) => {
    const mask = makeMask(G0);
    paint(G0, mask, shape);
    expect(Array.from(mask.keys()).filter((k) => mask[k] === 1)).toEqual(indices);
  });

  it("matches BigInt for 200 seeded shapes and preserves existing cells", () => {
    let cells = 0;
    for (let k = 1; k <= 200; k += 1) {
      const rng = new RngStream(hash32("raster", k));
      const { grid, shape } = seededCase(k, rng);
      const mask = makeMask(grid);
      for (let n = 0; n < 5; n += 1) mask[rng.int(0, mask.length - 1)] = 1;
      const expected = mask.slice();
      const contains = oracle(shape);
      for (let j = 0; j < grid.h; j += 1) {
        for (let i = 0; i < grid.w; i += 1) {
          const x = grid.originX + i * grid.cellCm + grid.cellCm / 2;
          const z = grid.originZ + j * grid.cellCm + grid.cellCm / 2;
          if (contains(x, z)) expected[j * grid.w + i] = 1;
        }
      }
      paint(grid, mask, shape);
      expect(mask, `raster seed ${k}: ${JSON.stringify({ grid, shape })}`).toEqual(expected);
      cells += mask.length;
    }
    console.info(`raster brute-force: 200 cases; ${cells} cells compared`);
  }, 60000);

  it("compares safely when cross squared exceeds the safe integer range", () => {
    const grid: RasterGrid = { originX: -16384, originZ: -16384, cellCm: 512, w: 64, h: 64 };
    for (const points of [
      [[-16384, -16384], [16384, 16384]],
      [[16384, -16384], [-16384, 16384]],
      [[-16384, 0], [16384, 1]],
    ] as const) {
      for (const hw of [0, 1, 2000]) {
        const shape: Shape = { kind: "line", points, hw };
        const contains = oracle(shape);
        const mask = makeMask(grid);
        paint(grid, mask, shape);
        expect(Array.from(mask)).toEqual(Array.from(mask, (_, k) => Number(contains(cellCenterX(grid, k % grid.w), cellCenterZ(grid, Math.floor(k / grid.w))))));
      }
    }
  });

  it("unions calls and leaves unrelated mask bytes untouched", () => {
    const mask = makeMask(G0);
    mask[24] = 7;
    rasterDisc(G0, mask, 5, 5, 0);
    rasterRect(G0, mask, 1, 1, 3, 1);
    rasterPolyline(G0, mask, [[3, 3]], 0);
    rasterPolygon(G0, mask, [[5, 5], [7, 5], [5, 7]]);
    expect(Array.from(mask.keys()).filter((k) => mask[k] !== 0)).toEqual([0, 1, 6, 12, 13, 17, 24]);
    expect(mask[24]).toBe(7);
  });

  it("exposes integer centers and documented limits", () => {
    expect(makeMask(G0)).toEqual(new Uint8Array(25));
    expect(cellCenterX(G0, 4)).toBe(9);
    expect(cellCenterZ({ ...G0, originZ: -10 }, 0)).toBe(-9);
    expect(RASTER_LIMIT_CM).toBe(16384);
    expect(RASTER_MAX_HALF_WIDTH_CM).toBe(2000);
  });

  const badGrids: readonly [string, RasterGrid][] = [
    ["odd cells", { ...G0, cellCm: 3 }], ["zero cells", { ...G0, cellCm: 0 }],
    ["zero width", { ...G0, w: 0 }], ["too tall", { ...G0, h: 4097 }],
    ["east overflow", { ...G0, originX: 16380 }], ["south overflow", { ...G0, originZ: 16380 }],
    ["west overflow", { ...G0, originX: -16385 }], ["north overflow", { ...G0, originZ: -16385 }],
    ["fractional dimension", { ...G0, w: 1.5 }], ["NaN", { ...G0, originX: NaN }],
    ["infinity", { ...G0, cellCm: Infinity }], ["unsafe integer", { ...G0, h: Number.MAX_SAFE_INTEGER + 1 }],
  ];
  it.each(badGrids)("rejects grid: %s", (_name, grid) => {
    expect(() => makeMask(grid)).toThrow(RangeError);
    expect(() => cellCenterX(grid, 0)).toThrow(RangeError);
    expect(() => cellCenterZ(grid, 0)).toThrow(RangeError);
    for (const [, shape] of handCases) expect(() => paint(grid, new Uint8Array(25), shape)).toThrow(RangeError);
  });

  const badShapes: readonly [string, Shape][] = [
    ["negative radius", { kind: "disc", at: [0, 0], r: -1 }],
    ["large radius", { kind: "disc", at: [0, 0], r: 32769 }],
    ["fractional radius", { kind: "disc", at: [0, 0], r: 1.5 }],
    ["reversed x", { kind: "rect", a: [2, 0], b: [1, 5] }],
    ["reversed z", { kind: "rect", a: [0, 2], b: [5, 1] }],
    ["empty line", { kind: "line", points: [], hw: 0 }],
    ["large half-width", { kind: "line", points: [[0, 0]], hw: 2001 }],
    ["negative half-width", { kind: "line", points: [[0, 0]], hw: -1 }],
    ["fractional half-width", { kind: "line", points: [[0, 0]], hw: 1.5 }],
    ["two-point polygon", { kind: "polygon", points: [[0, 0], [1, 1]] }],
  ];
  it.each(badShapes)("rejects shape: %s", (_name, shape) => {
    expect(() => paint(G0, makeMask(G0), shape)).toThrow(RangeError);
  });

  it.each([1.5, 16385, -16385, NaN, Infinity, Number.MAX_SAFE_INTEGER + 1])("rejects invalid coordinates %s before painting", (value) => {
    for (const at of [[value, 1], [1, value]] as const) {
      const shapes: Shape[] = [
        { kind: "disc", at, r: 1 }, { kind: "rect", a: at, b: [10, 10] },
        { kind: "rect", a: [0, 0], b: at },
        { kind: "line", points: [[1, 1], [5, 5], at], hw: 0 },
        { kind: "polygon", points: [[1, 1], [5, 1], [5, 5], at] },
      ];
      for (const shape of shapes) {
        const mask = makeMask(G0);
        expect(() => paint(G0, mask, shape)).toThrow(RangeError);
        expect(mask).toEqual(new Uint8Array(25));
      }
    }
  });

  it("rejects wrong mask lengths for every painter and invalid cell indices", () => {
    for (const [, shape] of handCases) expect(() => paint(G0, new Uint8Array(24), shape)).toThrow(RangeError);
    for (const index of [-1, 5, 1.5, NaN]) {
      expect(() => cellCenterX(G0, index)).toThrow(RangeError);
      expect(() => cellCenterZ(G0, index)).toThrow(RangeError);
    }
  });
});
