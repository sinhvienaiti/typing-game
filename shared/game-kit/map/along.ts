import { hash32 } from "./hash";

export type AlongPoint = readonly [number, number]; // [x, z], integer cm
export const ALONG_Q = 1024; // Arc-length units per cm.
export const ALONG_LIMIT_CM = 16384;
export const ALONG_MAX_SIDE_CM = 2000;
export const ALONG_MAX_ARC_Q = 2147483647;
export const TAN_SCALE = 1048576;
export const TAN_HALF_DEG: readonly number[] = [
  9151, 27458, 45782, 64134, 82525, 100966, 119470, 138048, 156711, 175471,
  194342, 213335, 232464, 251741, 271180, 290796, 310602, 330615, 350849, 371320,
  392047, 413045, 434334, 455934, 477864, 500145, 522801, 545854, 569330, 593256,
  617658, 642568, 668017, 694037, 720666, 747942, 775905, 804601, 834075, 864379,
  895569, 927702, 960843, 995061, 1030433,
];

export interface AlongArc {
  readonly lengths: readonly number[]; // Segment lengths in arc-length units.
  readonly starts: readonly number[]; // One cumulative start per point.
  readonly total: number; // Last cumulative start.
}

export interface AlongParams {
  readonly everyCm: number;
  readonly startCm: number;
  readonly sideCm: number; // Positive is right of travel.
  readonly alternate: boolean;
  readonly jitterCm: number;
  readonly seed: number;
  readonly skip: readonly (readonly [number, number])[];
}

export interface AlongItem {
  readonly k: number;
  readonly s: number;
  readonly seg: number;
  readonly x: number;
  readonly z: number;
  readonly yawDeg: number;
  readonly offsetCm: number;
}

function integer(value: number, min: number, max: number): void {
  if (!Number.isSafeInteger(value) || value < min || value > max) {
    throw new RangeError("Expected a safe integer in the allowed range");
  }
}

/** Exact floor division, including negative numerators and signed zero. */
export function floorDiv(a: number, b: number): number {
  integer(a, -2251799813685248, 2251799813685248);
  integer(b, 1, 2251799813685248);
  let r = a % b;
  if (r < 0) r += b;
  return (a - r) / b + 0;
}

/** Nearest integer; ties go toward positive infinity. */
export function roundDiv(a: number, b: number): number {
  integer(a, -562949953421312, 562949953421312);
  integer(b, 1, 562949953421312);
  return floorDiv(2 * a + b, 2 * b);
}

/** Binary search with exact integer products throughout. */
export function isqrt(n: number): number {
  integer(n, 0, 4503599627370496);
  let lo = 0;
  let hi = 67108864;
  while (lo < hi) {
    const mid = lo + floorDiv(hi - lo + 1, 2);
    if (mid * mid <= n) lo = mid;
    else hi = mid - 1;
  }
  return lo;
}

export function isqrtRound(n: number): number {
  const r = isqrt(n);
  return n - r * r > r ? r + 1 : r;
}

function octant(n: number, d: number): number {
  let c = 0;
  while (c < 45 && n * TAN_SCALE >= TAN_HALF_DEG[c]! * d) c += 1;
  return c;
}

/** Degrees from +x toward +z, using integer half-degree boundaries. */
export function yawDegOf(dx: number, dz: number): number {
  integer(dx, -32768, 32768);
  integer(dz, -32768, 32768);
  if (dx === 0 && dz === 0) throw new RangeError("Direction must be nonzero");
  const ax = Math.abs(dx);
  const az = Math.abs(dz);
  const a = az <= ax ? octant(az, ax) : 90 - octant(ax, az);
  const t = dz >= 0 ? (dx >= 0 ? a : 180 - a) : (dx < 0 ? 180 + a : 360 - a);
  return t === 360 ? 0 : t + 0;
}

export function polylineArc(points: readonly AlongPoint[]): AlongArc {
  if (!Array.isArray(points) || points.length < 1 || points.length > 100000) {
    throw new RangeError("Expected 1 to 100000 points");
  }
  for (const point of points) {
    if (!Array.isArray(point) || point.length !== 2) throw new RangeError("Expected an x,z pair");
    integer(point[0], -ALONG_LIMIT_CM, ALONG_LIMIT_CM);
    integer(point[1], -ALONG_LIMIT_CM, ALONG_LIMIT_CM);
  }
  const lengths: number[] = [];
  const starts = [0];
  let total = 0;
  for (let i = 0; i < points.length - 1; i += 1) {
    const dx = points[i + 1]![0] - points[i]![0];
    const dz = points[i + 1]![1] - points[i]![1];
    const length = isqrtRound((dx * dx + dz * dz) * ALONG_Q * ALONG_Q);
    total += length;
    if (total > ALONG_MAX_ARC_Q) throw new RangeError("Total arc exceeds its allowed range");
    lengths.push(length);
    starts.push(total);
  }
  return { lengths, starts, total };
}

export function placeAlong(points: readonly AlongPoint[], params: AlongParams): AlongItem[] {
  const { lengths, starts, total } = polylineArc(points);
  if (typeof params !== "object" || params === null) throw new RangeError("Expected along parameters");
  integer(params.everyCm, 1, 100000);
  integer(params.startCm, 0, 100000);
  integer(params.sideCm, -ALONG_MAX_SIDE_CM, ALONG_MAX_SIDE_CM);
  if (typeof params.alternate !== "boolean") throw new RangeError("Expected boolean alternate");
  integer(params.jitterCm, 0, floorDiv(params.everyCm - 1, 2));
  integer(params.seed, 0, 4294967295);
  if (!Array.isArray(params.skip) || params.skip.length > 1000) throw new RangeError("Expected at most 1000 skip windows");
  for (const window of params.skip) {
    if (!Array.isArray(window) || window.length !== 2) throw new RangeError("Expected a skip pair");
    integer(window[0], 0, 2097151);
    integer(window[1], window[0], 2097151);
  }
  if (total === 0) return [];
  const E = params.everyCm * ALONG_Q;
  const S0 = params.startCm * ALONG_Q;
  const J = params.jitterCm;
  const segments: number[] = [];
  for (let i = 0; i < lengths.length; i += 1) if (lengths[i]! > 0) segments.push(i);
  let cursor = 0;
  const items: AlongItem[] = [];
  for (let k = 0; S0 + k * E <= total; k += 1) {
    let s = S0 + k * E;
    if (J > 0) s += ((hash32(params.seed, "along", k) % (2 * J + 1)) - J) * ALONG_Q;
    if (s < 0 || s > total) continue;
    if (params.skip.some(([from, to]) => from * ALONG_Q <= s && s <= to * ALONG_Q)) continue;
    // Jitter preserves order, so a forward cursor selects the latest positive segment.
    while (cursor + 1 < segments.length && starts[segments[cursor + 1]!]! <= s) cursor += 1;
    const i = segments[cursor]!;
    const L = lengths[i]!;
    const t = s - starts[i]!;
    const [ax, az] = points[i]!;
    const dx = points[i + 1]![0] - ax;
    const dz = points[i + 1]![1] - az;
    const bx = ax + roundDiv(dx * t, L);
    const bz = az + roundDiv(dz * t, L);
    const o = (params.alternate && k % 2 === 1 ? 0 - params.sideCm : params.sideCm) + 0;
    const x = bx + roundDiv(-dz * o * ALONG_Q, L) + 0;
    const z = bz + roundDiv(dx * o * ALONG_Q, L) + 0;
    items.push({ k, s, seg: i, x, z, yawDeg: yawDegOf(dx, dz), offsetCm: o });
  }
  return items;
}

export function alongHash(items: readonly AlongItem[]): number {
  if (!Array.isArray(items)) throw new RangeError("Expected an array of along items");
  const parts: number[] = [];
  for (const item of items) {
    if (typeof item !== "object" || item === null) throw new RangeError("Expected an along item");
    for (const value of [item.k, item.s, item.seg, item.x, item.z, item.yawDeg, item.offsetCm]) {
      integer(value, -2147483648, 4294967295);
      parts.push(value);
    }
  }
  return hash32(...parts);
}
