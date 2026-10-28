export const EDT_INF = 2147483647;

// Scratch storage grows on demand; no returned result aliases these buffers.
let vertical = new Int32Array(0);
let s = new Int32Array(0);
let t = new Int32Array(0);

/** Exact squared Euclidean distance, Meijster, Roerdink and Hesselink (2000). */
export function edtSquared(mask: Uint8Array, w: number, h: number): Int32Array {
  if (!Number.isSafeInteger(w) || !Number.isSafeInteger(h)
    || w < 1 || w > 4096 || h < 1 || h > 4096 || mask.length !== w * h) {
    throw new RangeError("Invalid EDT dimensions or mask length");
  }
  const out = new Int32Array(w * h);
  if (vertical.length < out.length) vertical = new Int32Array(out.length);
  if (s.length < w) {
    s = new Int32Array(w);
    t = new Int32Array(w);
  }
  const sentinel = w + h;
  let nonempty = false;

  // Phase 1: vertical distances, clamped so empty columns stay at sentinel.
  for (let i = 0; i < w; i += 1) {
    let distance = sentinel;
    for (let j = 0; j < h; j += 1) {
      const k = j * w + i;
      if (mask[k] !== 0) {
        distance = 0;
        nonempty = true;
      } else {
        distance = Math.min(sentinel, distance + 1);
      }
      vertical[k] = distance;
    }
    for (let j = h - 2; j >= 0; j -= 1) {
      const k = j * w + i;
      vertical[k] = Math.min(vertical[k]!, vertical[k + w]! + 1);
    }
  }
  if (!nonempty) {
    out.fill(EDT_INF);
    return out;
  }

  // Phase 2: s holds parabola sites, t their first winning integer abscissae.
  // sentinel^2 exceeds every real grid distance, so empty columns never win.
  for (let j = 0; j < h; j += 1) {
    const row = j * w;
    let q = 0;
    s[0] = 0;
    t[0] = 0;
    for (let u = 1; u < w; u += 1) {
      const gu = vertical[row + u]!;
      while (q >= 0) {
        const i = s[q]!;
        const x = t[q]!;
        const gi = vertical[row + i]!;
        if ((x - i) * (x - i) + gi * gi <= (x - u) * (x - u) + gu * gu) break;
        q -= 1;
      }
      if (q < 0) {
        q = 0;
        s[0] = u;
        t[0] = 0;
      } else {
        const i = s[q]!;
        const gi = vertical[row + i]!;
        const start = 1 + Math.floor((u * u - i * i + gu * gu - gi * gi) / (2 * (u - i)));
        if (start < w) {
          q += 1;
          s[q] = u;
          t[q] = start;
        }
      }
    }
    for (let x = w - 1; x >= 0; x -= 1) {
      const i = s[q]!;
      const g = vertical[row + i]!;
      out[row + x] = (x - i) * (x - i) + g * g;
      if (x === t[q]) q -= 1;
    }
  }
  return out;
}
