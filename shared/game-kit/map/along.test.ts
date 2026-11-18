import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import { describe, expect, it } from "vitest";
import { RngStream } from "../platform/rng";
import {
  ALONG_Q, ALONG_LIMIT_CM, ALONG_MAX_SIDE_CM, ALONG_MAX_ARC_Q,
  TAN_SCALE, TAN_HALF_DEG, floorDiv, roundDiv, isqrt, isqrtRound,
  yawDegOf, polylineArc, placeAlong, alongHash,
} from "./along";
import type { AlongItem, AlongParams, AlongPoint } from "./along";
import { hash32 } from "./hash";

const P0: AlongParams = {
  everyCm: 250, startCm: 0, sideCm: 100, alternate: false, jitterCm: 0, seed: 0, skip: [],
};
const row = (v: AlongItem): number[] => [v.k, v.s, v.seg, v.x, v.z, v.yawDeg, v.offsetCm];
const rows = (items: readonly AlongItem[]): number[][] => items.map(row);
const circularError = (a: number, b: number): number => Math.min(Math.abs(a - b), 360 - Math.abs(a - b));
const floatYaw = (dx: number, dz: number): number => (Math.atan2(dz, dx) * 180 / Math.PI + 360) % 360;

// Independent reference: Newton roots and signed BigInt floor division.
function sqrtBig(n: bigint): bigint {
  if (n < 2n) return n;
  let x = n;
  let y = (x + n / x) / 2n;
  while (y < x) {
    x = y;
    y = (x + n / x) / 2n;
  }
  return x;
}

function floorBig(a: bigint, b: bigint): bigint {
  const q = a / b;
  return a % b < 0n ? q - 1n : q;
}

const roundBig = (a: bigint, b: bigint): bigint => floorBig(2n * a + b, 2n * b);
const absBig = (n: bigint): bigint => n < 0n ? -n : n;
const tanBig = TAN_HALF_DEG.map(BigInt);

function yawBig(dx: bigint, dz: bigint): bigint {
  const ax = absBig(dx);
  const az = absBig(dz);
  const n = ax >= az ? az : ax;
  const d = ax >= az ? ax : az;
  let c = 0n;
  for (const boundary of tanBig) {
    if (n * 1048576n < boundary * d) break;
    c += 1n;
  }
  const a = ax >= az ? c : 90n - c;
  if (dz >= 0n) return dx >= 0n ? a : 180n - a;
  return dx < 0n ? 180n + a : (360n - a) % 360n;
}

function placeBig(points: readonly AlongPoint[], params: AlongParams): AlongItem[] {
  const p = points.map(([x, z]) => [BigInt(x), BigInt(z)] as const);
  const starts = [0n];
  const lengths: bigint[] = [];
  for (let i = 1; i < p.length; i += 1) {
    const dx = p[i]![0] - p[i - 1]![0];
    const dz = p[i]![1] - p[i - 1]![1];
    const n = (dx * dx + dz * dz) * 1048576n;
    const r = sqrtBig(n);
    const length = n - r * r > r ? r + 1n : r;
    lengths.push(length);
    starts.push(starts[i - 1]! + length);
  }
  const total = starts[starts.length - 1]!;
  if (total === 0n) return [];
  const every = BigInt(params.everyCm) * 1024n;
  const start = BigInt(params.startCm) * 1024n;
  const jitter = BigInt(params.jitterCm);
  const skip = params.skip.map(([a, b]) => [BigInt(a) * 1024n, BigInt(b) * 1024n] as const);
  const result: AlongItem[] = [];
  for (let k = 0n; start + k * every <= total; k += 1n) {
    let s = start + k * every;
    if (jitter > 0n) s += (BigInt(hash32(params.seed, "along", Number(k))) % (2n * jitter + 1n) - jitter) * 1024n;
    if (s < 0n || s > total || skip.some(([a, b]) => a <= s && s <= b)) continue;
    // Scan backwards, independently of the production forward cursor.
    let i = lengths.length - 1;
    while (lengths[i] === 0n || starts[i]! > s) i -= 1;
    const length = lengths[i]!;
    const t = s - starts[i]!;
    const dx = p[i + 1]![0] - p[i]![0];
    const dz = p[i + 1]![1] - p[i]![1];
    const bx = p[i]![0] + roundBig(dx * t, length);
    const bz = p[i]![1] + roundBig(dz * t, length);
    let offset = BigInt(params.sideCm);
    if (params.alternate && k % 2n === 1n) offset = -offset;
    result.push({
      k: Number(k), s: Number(s), seg: i,
      x: Number(bx + roundBig(-dz * offset * 1024n, length)),
      z: Number(bz + roundBig(dx * offset * 1024n, length)),
      yawDeg: Number(yawBig(dx, dz)), offsetCm: Number(offset),
    });
  }
  return result;
}

interface RouteCase { name: string; points: readonly AlongPoint[]; params: AlongParams }
interface Golden extends RouteCase {
  total: number;
  count: number;
  hash: number;
  edges: number[][];
}

function fixture(name: string, sha: string, gameplayHash: string): { points: AlongPoint[] }[] {
  const bytes = readFileSync(new URL(`../../../tools/map-factory/test/fixtures/gameplay/${name}`, import.meta.url));
  expect(createHash("sha256").update(bytes).digest("hex"), `${name}: chạy lại phiếu 028 (sha256 của file)`).toBe(sha);
  const parsed = JSON.parse(bytes.toString("utf8")) as {
    hash: string; routes?: { points: AlongPoint[] }[]; lanes?: { points: AlongPoint[] }[];
  };
  expect(parsed.hash, `${name}: chạy lại phiếu 028 (hash lớp chơi)`).toBe(gameplayHash);
  return (parsed.routes ?? parsed.lanes)!;
}

function goldens(): Golden[] {
  const td = fixture("typing-defense.w1-silverfall.json",
    "71160a56c917a195f44baff68ceee9d2aa31e31e39169697ca839d7f54fc1428",
    "7faeaa7c0d5bf39803019444b1ae8056c36d3914a916a74baaed834e76ef4b23")[0]!.points;
  const dh = fixture("dragon-hold.L2-cau.json",
    "ad67509d387ba403f4cb6b1860de98266c892758e233a8b78d71a522e2a9fb37",
    "c852b4d70147c8d2bf87f22999334f090646d0ae87bde6a9873b35de45d9659a")[0]!.points;
  expect(td).toHaveLength(476);
  expect(td.slice(0, 3)).toEqual([[-1000, -4600], [-983, -4582], [-966, -4564]]);
  expect(td.slice(-3)).toEqual([[29, 3959], [14, 3979], [0, 4000]]);
  expect(dh).toEqual([[850, -2900], [500, -2250], [220, -1540], [120, -1000], [40, -600]]);
  return [
    { name: "td-route0", points: td,
      params: { everyCm: 750, startCm: 300, sideCm: 280, alternate: true, jitterCm: 0, seed: 0, skip: [[0, 800], [5000, 5600]] },
      total: 12163917, count: 14, hash: 1811293709,
      edges: [[1, 1075200, 41, -113, -4160, 23, -280], [2, 1843200, 71, 287, -3370, 37, 280],
        [3, 2611200, 101, 422, -2801, 149, -280], [15, 11827200, 461, 417, 3942, 133, -280]] },
    { name: "dh-cau", points: dh,
      params: { everyCm: 120, startCm: 60, sideCm: -200, alternate: false, jitterCm: 30, seed: 20261028, skip: [[950, 1940]] },
      total: 2517567, count: 12, hash: 1575973982,
      edges: [[0, 74752, 0, 991, -2741, 118, -200], [1, 204800, 0, 931, -2629, 118, -200],
        [2, 276480, 0, 898, -2567, 118, -200], [19, 2373632, 3, 264, -699, 101, -200]] },
    { name: "synthetic", points: [[0, 0], [0, 0], [1000, 0], [1000, 1], [1000, 700], [300, 0], [300, 0],
      [-500, -800], [-500, -800], [-1700, -800], [-1700, 400], [-1000, -300], [16384, -16384]],
      params: { everyCm: 37, startCm: 0, sideCm: 45, alternate: true, jitterCm: 18, seed: 123456789,
        skip: [[100, 150], [140, 200], [555, 555], [30000, 2097151]] },
      total: 31636035, count: 808, hash: 440583006,
      edges: [[1, 30720, 1, 30, -45, 0, -45], [2, 89088, 1, 87, 45, 0, 45],
        [6, 220160, 1, 215, 45, 0, 45], [811, 30709760, 11, 15689, -15803, 317, -45]] },
  ];
}

function randomCases(): RouteCase[] {
  const cases: RouteCase[] = [];
  for (let k = 1; k <= 100; k += 1) {
    const rng = new RngStream(hash32("along", k));
    const count = rng.int(1, 40);
    const short = k % 3 === 0;
    const points: AlongPoint[] = [];
    for (let i = 0; i < count; i += 1) {
      const previous = points[i - 1] ?? [0, 0];
      points.push(short ? [previous[0] + rng.int(-3, 3), previous[1] + rng.int(-3, 3)]
        : [rng.int(-16384, 16384), rng.int(-16384, 16384)]);
    }
    const everyCm = rng.int(1, short ? 5 : 3000);
    const startCm = rng.int(0, 50);
    const sideCm = rng.int(-2000, 2000);
    const alternate = rng.int(0, 1) === 1;
    const jitterCm = rng.int(0, Math.floor((everyCm - 1) / 2));
    const seed = rng.next();
    const skip: [number, number][] = [];
    const skipCount = rng.int(0, 3);
    const max = Math.floor(polylineArc(points).total / 1024) + 10;
    for (let i = 0; i < skipCount; i += 1) {
      const a = rng.int(0, max);
      const b = rng.int(0, max);
      skip.push([Math.min(a, b), Math.max(a, b)]);
    }
    cases.push({ name: `seed-${k}`, points, params: { everyCm, startCm, sideCm, alternate, jitterCm, seed, skip } });
  }
  return cases;
}

describe("along integer arithmetic", () => {
  it("matches all division examples and eliminates negative zero", () => {
    for (const [a, b, expected] of [[7, 2, 3], [-7, 2, -4], [-8, 2, -4], [-1, 1024, -1], [0, 5, 0], [-0, 5, 0]]) {
      expect(floorDiv(a!, b!)).toBe(expected);
    }
    for (const [a, b, expected] of [[5, 2, 3], [-5, 2, -2], [-7, 2, -3], [7, 3, 2], [-20480000, 512000, -40], [15360000, 512000, 30]]) {
      expect(roundDiv(a!, b!)).toBe(expected);
    }
  });

  it("matches every root example", () => {
    const inputs = [0, 1, 2, 3, 4, 15, 16, 99999999, 100000000, 4503599627370495, 4503599627370496];
    expect(inputs.map(isqrt)).toEqual([0, 1, 1, 1, 2, 3, 4, 9999, 10000, 67108863, 67108864]);
    expect([2, 3, 6, 7, 12, 13, 2097152, 262144000000].map(isqrtRound)).toEqual([1, 2, 2, 3, 3, 4, 1448, 512000]);
  });

  it("matches Newton BigInt on 10000 seeded inputs and square boundaries", () => {
    let count = 0;
    const check = (n: bigint): void => {
      if (n < 0n || n > 4503599627370496n) return;
      const r = sqrtBig(n);
      expect(isqrt(Number(n))).toBe(Number(r));
      expect(isqrtRound(Number(n))).toBe(Number(n - r * r > r ? r + 1n : r));
      count += 1;
    };
    for (let k = 0; k < 10000; k += 1) {
      const rng = new RngStream(hash32("isqrt", k));
      check(((BigInt(rng.next()) << 32n) + BigInt(rng.next())) % 4503599627370497n);
    }
    for (const [from, to] of [[1, 2000], [67106864, 67108864]] as const) {
      for (let m = from; m <= to; m += 1) {
        const square = BigInt(m) * BigInt(m);
        for (const delta of [-1n, 0n, 1n]) check(square + delta);
      }
    }
    console.info(`along roots: ${count} inputs; 10000 seeded`);
  });

  it("checks exact division limits against BigInt", () => {
    for (const a of [-2251799813685248, -2251799813685247, -1, 0, 1, 2251799813685247, 2251799813685248]) {
      for (const b of [1, 2, 3, 1024, 2251799813685247, 2251799813685248]) {
        expect(floorDiv(a, b)).toBe(Number(floorBig(BigInt(a), BigInt(b))));
      }
    }
    for (const a of [-562949953421312, -562949953421311, 0, 562949953421311, 562949953421312]) {
      for (const b of [1, 2, 3, 562949953421312]) expect(roundDiv(a, b)).toBe(Number(roundBig(BigInt(a), BigInt(b))));
    }
  });

  it.each([
    () => isqrt(-1), () => isqrt(1.5), () => isqrt(4503599627370497),
    () => floorDiv(1, 0), () => roundDiv(1, -2), () => floorDiv(2251799813685249, 1),
    () => floorDiv(1, 2251799813685249), () => roundDiv(562949953421313, 1),
    () => roundDiv(1, 562949953421313), () => floorDiv(NaN, 1), () => roundDiv(Infinity, 1),
  ])("rejects invalid arithmetic input %#", (call) => expect(call).toThrow(RangeError));
});

describe("along yaw", () => {
  it("stores exactly the prescribed 45 tangent boundaries", () => {
    expect(TAN_HALF_DEG).toEqual([
      9151, 27458, 45782, 64134, 82525, 100966, 119470, 138048, 156711, 175471,
      194342, 213335, 232464, 251741, 271180, 290796, 310602, 330615, 350849, 371320,
      392047, 413045, 434334, 455934, 477864, 500145, 522801, 545854, 569330, 593256,
      617658, 642568, 668017, 694037, 720666, 747942, 775905, 804601, 834075, 864379,
      895569, 927702, 960843, 995061, 1030433,
    ]);
    expect(TAN_HALF_DEG).toHaveLength(45);
    TAN_HALF_DEG.forEach((t, c) => expect(t).toBe(Math.round(Math.tan((c + 0.5) * Math.PI / 180) * 1048576)));
    expect(TAN_SCALE).toBe(1048576);
  });

  it.each([
    [1, 0, 0], [1, 1, 45], [0, 1, 90], [-1, 1, 135], [-1, 0, 180], [-1, -1, 225],
    [0, -1, 270], [1, -1, 315], [300, 400, 53], [-1, -10000, 270], [10000, -1, 0],
    [17, 18, 47], [100, 1, 1], [114, 1, 1], [115, 1, 0],
  ])("yaw(%i,%i) = %i", (dx, dz, y) => expect(yawDegOf(dx, dz)).toBe(y));

  it("compares all 381200 specified vectors with atan2", () => {
    let count = 0;
    let maxError = 0;
    let different = 0;
    const check = (dx: number, dz: number): void => {
      const a = floatYaw(dx, dz);
      const y = yawDegOf(dx, dz);
      const error = circularError(y, a);
      if (error > 0.501) throw new Error(`yaw ${dx},${dz}: error ${error}`);
      maxError = Math.max(maxError, error);
      if (y !== Math.round(a) % 360) different += 1;
      count += 1;
    };
    for (let dx = -300; dx <= 300; dx += 1) {
      for (let dz = -300; dz <= 300; dz += 1) if (dx !== 0 || dz !== 0) check(dx, dz);
    }
    for (let k = 1; k <= 20000; k += 1) check(hash32("yaw", k, 0) % 65537 - 32768, hash32("yaw", k, 1) % 65537 - 32768);
    expect(count).toBe(381200);
    console.info(`along yaw: ${count} vectors; max=${maxError.toFixed(9)}deg; different=${different}`);
  });

  it.each([[0, 0], [32769, 0], [0.5, 1], [0, -32769], [NaN, 1]])("rejects yaw(%s,%s)", (dx, dz) => {
    expect(() => yawDegOf(dx, dz)).toThrow(RangeError);
  });
});

describe("along placement", () => {
  const east: AlongPoint[] = [[0, 0], [1000, 0]];
  const handCases: [string, readonly AlongPoint[], Partial<AlongParams>, number[][]][] = [
    ["east", east, {}, [[0, 0, 0, 0, 100, 0, 100], [1, 256000, 0, 250, 100, 0, 100], [2, 512000, 0, 500, 100, 0, 100], [3, 768000, 0, 750, 100, 0, 100], [4, 1024000, 0, 1000, 100, 0, 100]]],
    ["alternate", east, { alternate: true }, [[0, 0, 0, 0, 100, 0, 100], [1, 256000, 0, 250, -100, 0, -100], [2, 512000, 0, 500, 100, 0, 100], [3, 768000, 0, 750, -100, 0, -100], [4, 1024000, 0, 1000, 100, 0, 100]]],
    ["zero side", east, { sideCm: 0, alternate: true }, [[0, 0, 0, 0, 0, 0, 0], [1, 256000, 0, 250, 0, 0, 0], [2, 512000, 0, 500, 0, 0, 0], [3, 768000, 0, 750, 0, 0, 0], [4, 1024000, 0, 1000, 0, 0, 0]]],
    ["north", [[0, 0], [0, -1000]], {}, [[0, 0, 0, 100, 0, 270, 100], [1, 256000, 0, 100, -250, 270, 100], [2, 512000, 0, 100, -500, 270, 100], [3, 768000, 0, 100, -750, 270, 100], [4, 1024000, 0, 100, -1000, 270, 100]]],
    ["diagonal", [[0, 0], [300, 400]], { everyCm: 100, sideCm: 50 }, [[0, 0, 0, -40, 30, 53, 50], [1, 102400, 0, 20, 110, 53, 50], [2, 204800, 0, 80, 190, 53, 50], [3, 307200, 0, 140, 270, 53, 50], [4, 409600, 0, 200, 350, 53, 50], [5, 512000, 0, 260, 430, 53, 50]]],
    ["corner", [[0, 0], [100, 0], [100, 100]], { everyCm: 50, sideCm: 10 }, [[0, 0, 0, 0, 10, 0, 10], [1, 51200, 0, 50, 10, 0, 10], [2, 102400, 1, 90, 0, 90, 10], [3, 153600, 1, 90, 50, 90, 10], [4, 204800, 1, 90, 100, 90, 10]]],
    ["closed skips", east, { skip: [[250, 250], [700, 1000]] }, [[0, 0, 0, 0, 100, 0, 100], [2, 512000, 0, 500, 100, 0, 100]]],
    ["start past end", east, { startCm: 1001 }, []],
    ["one point", [[5, 5]], {}, []], ["same points", [[5, 5], [5, 5]], {}, []],
  ];
  it.each(handCases)("matches hand calculation: %s", (_name, points, override, expected) => {
    const items = placeAlong(points, { ...P0, ...override });
    expect(rows(items)).toEqual(expected);
    for (const v of items) for (const n of row(v)) expect(Object.is(n, -0)).toBe(false);
  });

  it("keeps outgoing segments through duplicates and the final positive segment at the end", () => {
    const points: AlongPoint[] = [[0, 0], [0, 0], [100, 0], [100, 0], [100, 100], [100, 100]];
    expect(polylineArc(points)).toEqual({ lengths: [0, 102400, 0, 102400, 0], starts: [0, 0, 102400, 102400, 204800, 204800], total: 204800 });
    expect(placeAlong(points, { ...P0, everyCm: 100 }).map((v) => v.seg)).toEqual([1, 3, 3]);
    expect(polylineArc([[5, 5]])).toEqual({ lengths: [], starts: [0], total: 0 });
    expect(placeAlong([[-0, -0], [100, -0]], { ...P0, sideCm: -0, alternate: true }).every((v) => row(v).every((n) => !Object.is(n, -0)))).toBe(true);
  });

  it("matches golden totals, counts, hashes, endpoints and repeats exactly", () => {
    const cases = goldens();
    expect(polylineArc(cases[0]!.points).lengths.slice(0, 4)).toEqual([25353, 25353, 26107, 25353]);
    expect(polylineArc(cases[0]!.points).lengths).toHaveLength(475);
    expect(polylineArc(cases[1]!.points).lengths).toEqual([755959, 781534, 562362, 417712]);
    expect(polylineArc(cases[2]!.points).lengths).toEqual([0, 1024000, 1024, 715776, 1013708, 0, 1158524, 0, 1228800, 1228800, 1013708, 24251695]);
    expect(hash32(20261028, "along", 0)).toBe(2665129022);
    expect([0, 1, 2, 3].map((k) => hash32(20261028, "along", k) % 61 - 30)).toEqual([13, 20, -30, -27]);
    expect([0, 1, 2, 3].map((k) => hash32(123456789, "along", k) % 37 - 18)).toEqual([-2, -7, 13, 4]);
    for (const c of cases) {
      const items = placeAlong(c.points, c.params);
      const arc = polylineArc(c.points);
      const edges = rows([...items.slice(0, 3), items[items.length - 1]!]);
      expect(arc.total).toBe(c.total);
      expect(items).toHaveLength(c.count);
      expect(alongHash(items)).toBe(c.hash);
      expect(edges).toEqual(c.edges);
      expect(placeAlong(c.points, c.params)).toEqual(items);
      console.info(`along golden ${c.name}: total=${arc.total}; items=${items.length}; hash=${alongHash(items)}; edges=${JSON.stringify(edges)}`);
    }
    expect(alongHash([])).toBe(2872998923);
    const items = placeAlong(east, P0);
    expect(alongHash(items)).toBe(hash32(...rows(items).flat()));
  });

  it("matches BigInt and all geometric properties on 103 routes", () => {
    const cases = [...goldens(), ...randomCases()];
    let compared = 0;
    let allArc = 0;
    let allSide = 0;
    let allYaw = 0;
    for (let caseIndex = 0; caseIndex < cases.length; caseIndex += 1) {
      const c = cases[caseIndex]!;
      const { points, params } = c;
      const items = placeAlong(points, params);
      expect(items, c.name).toEqual(placeBig(points, params));
      compared += items.length;
      const arc = polylineArc(points);
      const bases = placeAlong(points, { ...params, sideCm: 0 });
      expect(bases.map((v) => v.k)).toEqual(items.map((v) => v.k));
      const realStarts = [0];
      for (let i = 1; i < points.length; i += 1) realStarts.push(realStarts[i - 1]! + Math.hypot(points[i]![0] - points[i - 1]![0], points[i]![1] - points[i - 1]![1]));
      const byK = new Map(items.map((v) => [v.k, v]));
      let eligible = 0;
      for (let k = 0; params.startCm * 1024 + k * params.everyCm * 1024 <= arc.total && arc.total > 0; k += 1) {
        const shift = params.jitterCm === 0 ? 0 : hash32(params.seed, "along", k) % (2 * params.jitterCm + 1) - params.jitterCm;
        const s = (params.startCm + k * params.everyCm + shift) * 1024;
        const wanted = s >= 0 && s <= arc.total && !params.skip.some(([a, b]) => a * 1024 <= s && s <= b * 1024);
        expect(byK.has(k), `${c.name} candidate ${k}`).toBe(wanted);
        if (wanted) {
          expect(byK.get(k)!.s).toBe(s);
          eligible += 1;
        }
      }
      expect(items.length).toBe(eligible);
      let maxArc = 0;
      let maxSide = 0;
      let maxYaw = 0;
      for (let j = 0; j < items.length; j += 1) {
        const v = items[j]!;
        const base = bases[j]!;
        const previous = items[j - 1];
        if (previous) {
          expect(v.s).toBeGreaterThan(previous.s);
          expect(v.k).toBeGreaterThan(previous.k);
          if (params.jitterCm === 0 && v.k === previous.k + 1) expect(v.s - previous.s).toBe(params.everyCm * 1024);
        }
        for (const n of row(v)) {
          expect(Number.isSafeInteger(n)).toBe(true);
          expect(Object.is(n, -0)).toBe(false);
        }
        const shift = v.s - (params.startCm + v.k * params.everyCm) * 1024;
        expect(shift % 1024 === 0).toBe(true);
        expect(Math.abs(shift)).toBeLessThanOrEqual(params.jitterCm * 1024);
        expect(v.offsetCm).toBe(params.alternate && v.k % 2 === 1 ? -params.sideCm : params.sideCm);
        const a = points[v.seg]!;
        const b = points[v.seg + 1]!;
        const arcError = Math.abs(realStarts[v.seg]! + Math.hypot(base.x - a[0], base.z - a[1]) - v.s / 1024);
        const sideError = Math.abs(Math.hypot(v.x - base.x, v.z - base.z) - Math.abs(v.offsetCm));
        const yawError = circularError(v.yawDeg, floatYaw(b[0] - a[0], b[1] - a[1]));
        expect(arcError, `${c.name} arc k=${v.k}`).toBeLessThanOrEqual(0.7072 + (v.seg + 1) * 0.5 / 1024);
        expect(sideError, `${c.name} side k=${v.k}`).toBeLessThanOrEqual(0.7072 + Math.abs(v.offsetCm) * 0.5 / arc.lengths[v.seg]!);
        expect(yawError).toBeLessThanOrEqual(0.501);
        if (caseIndex < 3) {
          expect(arcError).toBeLessThanOrEqual(1);
          expect(sideError).toBeLessThanOrEqual(1);
        }
        maxArc = Math.max(maxArc, arcError);
        maxSide = Math.max(maxSide, sideError);
        maxYaw = Math.max(maxYaw, yawError);
      }
      allArc = Math.max(allArc, maxArc);
      allSide = Math.max(allSide, maxSide);
      allYaw = Math.max(allYaw, maxYaw);
      if (caseIndex < 3) console.info(`along errors ${c.name}: arc=${maxArc.toFixed(9)}cm; side=${maxSide.toFixed(9)}cm; yaw=${maxYaw.toFixed(9)}deg`);
    }
    expect(cases).toHaveLength(103);
    console.info(`along BigInt/properties: routes=${cases.length}; items=${compared}; maxArc=${allArc.toFixed(9)}cm; maxSide=${allSide.toFixed(9)}cm; maxYaw=${allYaw.toFixed(9)}deg`);
  }, 30000);

  it.each([
    [], [[1.5, 0]], [[16385, 0]], [[1, 2, 3]],
    Array.from({ length: 65 }, (_, i) => [i % 2 === 0 ? -16384 : 16384, 0]),
    null, [null], [[NaN, 0]], [[0, Infinity]], Array.from({ length: 100001 }, () => [0, 0]),
  ].map((points) => [points]))("rejects invalid points %#", (points) => {
    expect(() => polylineArc(points as unknown as AlongPoint[])).toThrow(RangeError);
    expect(() => placeAlong(points as unknown as AlongPoint[], P0)).toThrow(RangeError);
  });

  it.each([
    { everyCm: 0 }, { everyCm: 100001 }, { startCm: -1 }, { startCm: 100001 },
    { sideCm: 2001 }, { sideCm: -2001 }, { alternate: 1 }, { everyCm: 10, jitterCm: 5 },
    { jitterCm: -1 }, { seed: -1 }, { seed: 4294967296 }, { seed: 1.5 },
    { skip: [[5, 4]] }, { skip: [[-1, 3]] }, { skip: [[0, 2097152]] }, { skip: [[1]] },
    { skip: null }, { skip: [null] }, { skip: Array.from({ length: 1001 }, () => [0, 0]) },
  ])("rejects invalid parameters %# even on a zero arc", (override) => {
    const params = { ...P0, ...override } as unknown as AlongParams;
    expect(() => placeAlong(east, params)).toThrow(RangeError);
    expect(() => placeAlong([[0, 0]], params)).toThrow(RangeError);
  });

  it("requires a parameter object and accepts inclusive coordinate/parameter bounds", () => {
    expect(() => placeAlong(east, null as unknown as AlongParams)).toThrow(RangeError);
    expect(() => placeAlong(east, undefined as unknown as AlongParams)).toThrow(RangeError);
    expect(polylineArc([[-16384, -16384], [16384, 16384]]).total).toBe(isqrtRound(2251799813685248));
    expect(placeAlong(east, { everyCm: 100000, startCm: 100000, sideCm: -2000, alternate: false, jitterCm: 49999, seed: 4294967295, skip: [[0, 2097151]] })).toEqual([]);
    expect([ALONG_Q, ALONG_LIMIT_CM, ALONG_MAX_SIDE_CM, ALONG_MAX_ARC_Q]).toEqual([1024, 16384, 2000, 2147483647]);
  });

  it("contains no Math.sqrt anywhere in the core source", () => {
    expect(readFileSync(new URL("./along.ts", import.meta.url), "utf8")).not.toContain("Math.sqrt");
  });

  it("rejects malformed hash input with RangeError", () => {
    for (const input of [null, {}, [null], [{}], [{ ...placeAlong(east, P0)[0]!, s: "0" }],
      [{ ...placeAlong(east, P0)[0]!, x: 4294967296 }]]) {
      expect(() => alongHash(input as unknown as AlongItem[])).toThrow(RangeError);
    }
  });
});
