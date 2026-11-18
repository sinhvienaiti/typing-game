// Ticket 259 · the reference for jadeRingOf() (Claude, 04/11/2026). Codex ports `jadeRingOf` into
// src/view/skills/blades.ts with the same rules and numbers; the GLB reader below is what
// scripts/visual/jade-ring-measure.ts does for check 5. Text in the notes folder, not game code.
//
// Run from the game's root (reads the GLBs of the main checkout, writes nothing):
//   cd /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation
//   node node_modules/tsx/dist/cli.mjs ../../docs/codex-queue/259/jade-ring-reference.ts
// Prints (04/11/2026, HEAD bc94110; rCut at the flange's inner edge since the critic's round, see the ticket's
// "Phản biện"), 5 decimals:
//   full: x 0.00230, y -0.02741, rIn 0.04401, rCut 0.09243, front {a 0.02450, bx -0.01751, by -0.03781},
//         back {a 0.02744, bx -0.00356, by 0.03750}, margin 0.00313, ~15 ms
//   lod:  x 0.00205, y -0.02767, rIn 0.04409, rCut 0.09201, front {a 0.02453, bx -0.01954, by -0.03616},
//         back {a 0.02738, bx -0.00116, by 0.03477}, margin 0.00309, ~14 ms
// The synthetic ring of the unit test (ticket §Việc 5) gives: x 0, y -0.0274, rIn 0.0440, rCut 0.0891,
//   front {a 0.0230, bx 0.0002, by 0.0445}, back {a 0.0230, bx -0.0000, by -0.0445}, margin 0.00275;
//   the same ring with no hole (a solid disc) and a plain blade give null (fail called once, with a step name).
import { readFileSync } from "node:fs";
import * as THREE from "../../../games/immortality-cultivation/node_modules/three/build/three.module.js";
import { auraAnchorsOf, bladeFromObject, guardBand } from "../../../games/immortality-cultivation/src/view/skills/blades";
import { edgeField } from "../../../games/immortality-cultivation/src/view/skills/sword-material";

export interface CrestPlane {
  readonly a: number;
  readonly bx: number;
  readonly by: number;
}

export interface JadeRing {
  readonly x: number;
  readonly y: number;
  readonly rIn: number;
  readonly rCut: number;
  readonly front: CrestPlane;
  readonly back: CrestPlane;
  readonly margin: number;
}

/** Index of the q-quantile in an ascending array of n values: floor(n × q), capped. */
const at = (n: number, q: number): number => Math.min(n - 1, Math.floor(n * q));

/**
 * `fail` (optional) is called once with the failing step's name before a null: "hole-seed", "hole-open", "band",
 * "flange", "crest-front", "crest-back", "bounds" (modelOf passes one that warns with the model's name).
 */
export function jadeRingOf(geometry: THREE.BufferGeometry, guard: readonly [number, number], guardHalf: number, fail?: (step: string) => void): JadeRing | null {
  const pos = geometry.getAttribute("position");
  const index = geometry.getIndex();
  const tri = index !== null ? index.count : pos.count;
  const vi = (k: number): number => (index !== null ? index.getX(k) : k);
  // 1. Height maps of the guard band seen along z: top = max z, bot = min z, 512 × 512 cells.
  const M = 512;
  const h = 1.25 * guardHalf;
  const cy0 = (guard[0] + guard[1]) / 2;
  const x0 = -h;
  const y0 = cy0 - h;
  const cell = (2 * h) / M;
  const top = new Float32Array(M * M).fill(-Infinity);
  const bot = new Float32Array(M * M).fill(Infinity);
  const yLo = guard[0] - 0.02;
  const yHi = guard[1] + 0.02;
  for (let t = 0; t + 2 < tri; t += 3) {
    const a = vi(t);
    const b = vi(t + 1);
    const c = vi(t + 2);
    const ya = pos.getY(a);
    const yb = pos.getY(b);
    const yc = pos.getY(c);
    if (Math.max(ya, yb, yc) < yLo || Math.min(ya, yb, yc) > yHi) continue;
    const ax = (pos.getX(a) - x0) / cell;
    const ay = (ya - y0) / cell;
    const bx = (pos.getX(b) - x0) / cell;
    const by = (yb - y0) / cell;
    const cx = (pos.getX(c) - x0) / cell;
    const cy = (yc - y0) / cell;
    const area = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax);
    if (Math.abs(area) < 1e-9) continue;
    const i0 = Math.max(0, Math.floor(Math.min(ax, bx, cx)));
    const i1 = Math.min(M - 1, Math.ceil(Math.max(ax, bx, cx)));
    const j0 = Math.max(0, Math.floor(Math.min(ay, by, cy)));
    const j1 = Math.min(M - 1, Math.ceil(Math.max(ay, by, cy)));
    const az = pos.getZ(a);
    const bz = pos.getZ(b);
    const cz = pos.getZ(c);
    for (let j = j0; j <= j1; j += 1) {
      for (let i = i0; i <= i1; i += 1) {
        const px = i + 0.5;
        const py = j + 0.5;
        const w0 = ((bx - px) * (cy - py) - (by - py) * (cx - px)) / area;
        const w1 = ((cx - px) * (ay - py) - (cy - py) * (ax - px)) / area;
        const w2 = 1 - w0 - w1;
        if (w0 < 0 || w1 < 0 || w2 < 0) continue;
        const z = w0 * az + w1 * bz + w2 * cz;
        const k = j * M + i;
        if (z > top[k]!) top[k] = z;
        if (z < bot[k]!) bot[k] = z;
      }
    }
  }
  // 2. The hole: the empty cell nearest (0, cy0) within 40 cells, flooded over empty cells (4 neighbours).
  const ci = Math.floor((0 - x0) / cell);
  const cj = Math.floor((cy0 - y0) / cell);
  let seed = -1;
  let best = Infinity;
  for (let j = cj - 40; j <= cj + 40; j += 1) {
    for (let i = ci - 40; i <= ci + 40; i += 1) {
      if (i < 0 || j < 0 || i >= M || j >= M || top[j * M + i] !== -Infinity) continue;
      const d = (i - ci) ** 2 + (j - cj) ** 2;
      if (d < best) {
        best = d;
        seed = j * M + i;
      }
    }
  }
  if (seed < 0) {
    fail?.("hole-seed");
    return null;
  }
  const seen = new Uint8Array(M * M);
  const stack = [seed];
  seen[seed] = 1;
  let n = 0;
  let sx = 0;
  let sy = 0;
  while (stack.length > 0) {
    const k = stack.pop()!;
    const i = k % M;
    const j = (k - i) / M;
    if (i === 0 || j === 0 || i === M - 1 || j === M - 1) {
      fail?.("hole-open");
      return null;
    }
    n += 1;
    sx += i + 0.5;
    sy += j + 0.5;
    for (const q of [k - 1, k + 1, k - M, k + M]) {
      if (seen[q] === 0 && top[q] === -Infinity) {
        seen[q] = 1;
        stack.push(q);
      }
    }
  }
  const hx = x0 + (sx / n) * cell;
  const hy = y0 + (sy / n) * cell;
  const rIn = Math.sqrt(n / Math.PI) * cell;
  const sample = (buf: Float32Array, X: number, Y: number): number => {
    const i = Math.floor((X - x0) / cell);
    const j = Math.floor((Y - y0) / cell);
    if (i < 0 || j < 0 || i >= M || j >= M) return NaN;
    const v = buf[j * M + i]!;
    return Number.isFinite(v) ? v : NaN;
  };
  // 3. Thickness (top − bot) round the hole: per radius (step one cell), 180 angles, its 25th percentile.
  const A = 180;
  const rs: number[] = [];
  const thick: number[] = [];
  const cover: number[] = [];
  for (let r = rIn + cell; r < h; r += cell) {
    const v: number[] = [];
    for (let k = 0; k < A; k += 1) {
      const th = ((k + 0.5) / A) * 2 * Math.PI;
      const X = hx + r * Math.cos(th);
      const Y = hy + r * Math.sin(th);
      const f = sample(top, X, Y);
      if (Number.isFinite(f)) v.push(f - sample(bot, X, Y));
    }
    v.sort((p, q) => p - q);
    rs.push(r);
    cover.push(v.length / A);
    thick.push(v.length > 0 ? v[at(v.length, 0.25)]! : NaN);
  }
  let start = 0;
  while (start < rs.length && cover[start]! < 0.95) start += 1;
  let end = rs.length;
  for (let i = start; i < rs.length; i += 1) {
    if (cover[i]! < 0.9) {
      end = i;
      break;
    }
  }
  if (start >= end) {
    fail?.("band");
    return null;
  }
  // 4. The flange: the deepest valley of the thickness between the disc and the silver rim (depth = the lower of
  //    the highest thickness on its inner side and on its outer side, minus its own); the disc's crest is the
  //    thickest radius inside it, the rim's the thickest outside it. rCut = the INNER end of the run under thr:
  //    the foot of the disc's outer wall, the flange's inner edge. Not the run's middle: the flange is painted a
  //    saturated bronze (linear saturation 0.44-0.59) that the colour classes cannot tell from the gold line, so the
  //    region must stop before it (ticket 259, "Phản biện", defect 2).
  let fl = -1;
  let depth = 0;
  for (let i = start; i < end; i += 1) {
    let left = 0;
    let right = 0;
    for (let k = start; k <= i; k += 1) left = Math.max(left, thick[k]!);
    for (let k = i; k < end; k += 1) right = Math.max(right, thick[k]!);
    const d = Math.min(left, right) - thick[i]!;
    if (d > depth) {
      depth = d;
      fl = i;
    }
  }
  if (fl < 0) {
    fail?.("flange");
    return null;
  }
  let crest = start;
  for (let i = start; i <= fl; i += 1) if (thick[i]! > thick[crest]!) crest = i;
  let rim = fl;
  for (let i = fl; i < end; i += 1) if (thick[i]! > thick[rim]!) rim = i;
  const tCrest = thick[crest]!;
  const tFl = thick[fl]!;
  if (!(tFl <= 0.4 * tCrest) || !(depth >= 0.2 * tCrest)) {
    fail?.("flange");
    return null;
  }
  const thr = tFl + 0.25 * (Math.min(tCrest, thick[rim]!) - tFl);
  let a0 = fl;
  while (a0 > crest && thick[a0 - 1]! < thr) a0 -= 1;
  const rCut = rs[a0]!;
  // 5. Crest planes, front (top) and back (−bot): per angle (120) the highest cell over the band
  //    rIn + 0.30 w … rIn + 0.55 w (step half a cell), then h(θ) = a + b cos θ + c sin θ fitted to the lower envelope.
  const w = rCut - rIn;
  const P = 120;
  const thetas: number[] = [];
  const hf: number[] = [];
  const hb: number[] = [];
  for (let k = 0; k < P; k += 1) {
    const th = ((k + 0.5) / P) * 2 * Math.PI;
    let f = -Infinity;
    let b = -Infinity;
    for (let r = rIn + 0.3 * w; r <= rIn + 0.55 * w; r += cell * 0.5) {
      const X = hx + r * Math.cos(th);
      const Y = hy + r * Math.sin(th);
      const vf = sample(top, X, Y);
      const vb = sample(bot, X, Y);
      if (Number.isFinite(vf)) f = Math.max(f, vf);
      if (Number.isFinite(vb)) b = Math.max(b, -vb);
    }
    thetas.push(th);
    hf.push(f);
    hb.push(b);
  }
  const rMid = rIn + 0.425 * w;
  const margin = 0.06 * tCrest;
  const fit = (hs: number[], step: string): CrestPlane | null => {
    const ok = hs.map((v) => Number.isFinite(v));
    let keep = ok.slice();
    let coef = [0, 0, 0];
    let res: number[] = [];
    for (let it = 0; it < 5; it += 1) {
      const N = [0, 0, 0, 0, 0, 0, 0, 0, 0];
      const R = [0, 0, 0];
      for (let i = 0; i < hs.length; i += 1) {
        if (!keep[i]) continue;
        const row = [1, Math.cos(thetas[i]!), Math.sin(thetas[i]!)];
        for (let p = 0; p < 3; p += 1) {
          R[p]! += row[p]! * hs[i]!;
          for (let q = 0; q < 3; q += 1) N[p * 3 + q]! += row[p]! * row[q]!;
        }
      }
      coef = solve3(N, R);
      res = hs.map((v, i) => (ok[i] ? v - (coef[0]! + coef[1]! * Math.cos(thetas[i]!) + coef[2]! * Math.sin(thetas[i]!)) : NaN));
      const sorted = res.filter((e) => Number.isFinite(e)).sort((p, q) => p - q);
      if (sorted.length < 24) {
        fail?.(step);
        return null;
      }
      const cut = sorted[at(sorted.length, 0.4)]!;
      keep = res.map((e, i) => ok[i]! && e <= cut);
    }
    // The angles the last fit was made on must sit on it: none more than half the margin above.
    let worst = 0;
    for (let i = 0; i < hs.length; i += 1) if (keep[i]) worst = Math.max(worst, res[i]!);
    if (!(worst <= 0.5 * margin) || !(coef[0]! > 0)) {
      fail?.(step);
      return null;
    }
    return { a: coef[0]!, bx: coef[1]! / rMid, by: coef[2]! / rMid };
  };
  const front = fit(hf, "crest-front");
  if (front === null) return null;
  const back = fit(hb, "crest-back");
  if (back === null) return null;
  if (!(rIn > 0.2 * guardHalf && rIn < 0.7 * guardHalf && Math.abs(hx) <= 0.1 * guardHalf && hy >= guard[0] && hy <= guard[1] && w >= 0.3 * rIn)) {
    fail?.("bounds");
    return null;
  }
  return { x: hx, y: hy, rIn, rCut, front, back, margin };
}

/** Solves the 3 × 3 system N·c = R (row-major N), partial pivoting. */
function solve3(N: number[], R: number[]): number[] {
  const m = [0, 1, 2].map((r) => [N[r * 3]!, N[r * 3 + 1]!, N[r * 3 + 2]!, R[r]!]);
  for (let c = 0; c < 3; c += 1) {
    let p = c;
    for (let r = c + 1; r < 3; r += 1) if (Math.abs(m[r]![c]!) > Math.abs(m[p]![c]!)) p = r;
    [m[c], m[p]] = [m[p]!, m[c]!];
    for (let r = 0; r < 3; r += 1) {
      if (r === c) continue;
      const f = m[r]![c]! / m[c]![c]!;
      for (let q = c; q < 4; q += 1) m[r]![q]! -= f * m[c]![q]!;
    }
  }
  return [m[0]![3]! / m[0]![0]!, m[1]![3]! / m[1]![1]!, m[2]![3]! / m[2]![2]!];
}

// ── GLB reader (no textures, no compression: these two files use none) ──────────────────────────────
const TYPES: Record<number, Float32ArrayConstructor | Uint32ArrayConstructor | Uint16ArrayConstructor | Uint8ArrayConstructor> = { 5126: Float32Array, 5125: Uint32Array, 5123: Uint16Array, 5121: Uint8Array };
const SIZES: Record<string, number> = { SCALAR: 1, VEC2: 2, VEC3: 3, VEC4: 4 };

export function readGlbScene(path: string): THREE.Object3D {
  const buf = readFileSync(path);
  const jsonLen = buf.readUInt32LE(12);
  const json = JSON.parse(buf.subarray(20, 20 + jsonLen).toString("utf8"));
  const bin = 20 + jsonLen + 8;
  const accessor = (i: number): THREE.BufferAttribute => {
    const a = json.accessors[i];
    const view = json.bufferViews[a.bufferView];
    const T = TYPES[a.componentType]!;
    const size = SIZES[a.type]!;
    if (view.byteStride !== undefined && view.byteStride !== size * T.BYTES_PER_ELEMENT) throw new Error("interleaved accessor");
    const off = bin + (view.byteOffset ?? 0) + (a.byteOffset ?? 0);
    const bytes = buf.buffer.slice(buf.byteOffset + off, buf.byteOffset + off + a.count * size * T.BYTES_PER_ELEMENT);
    return new THREE.BufferAttribute(new T(bytes), size, a.normalized === true);
  };
  const root = new THREE.Group();
  for (const node of json.nodes) {
    if (node.mesh === undefined) continue;
    for (const prim of json.meshes[node.mesh].primitives) {
      const g = new THREE.BufferGeometry();
      g.setAttribute("position", accessor(prim.attributes.POSITION));
      if (prim.attributes.NORMAL !== undefined) g.setAttribute("normal", accessor(prim.attributes.NORMAL));
      if (prim.attributes.TEXCOORD_0 !== undefined) g.setAttribute("uv", accessor(prim.attributes.TEXCOORD_0));
      if (prim.indices !== undefined) g.setIndex(accessor(prim.indices));
      const mesh = new THREE.Mesh(g, new THREE.MeshStandardMaterial());
      if (node.matrix !== undefined) {
        mesh.matrix.fromArray(node.matrix);
        mesh.matrix.decompose(mesh.position, mesh.quaternion, mesh.scale);
      }
      if (node.translation !== undefined) mesh.position.fromArray(node.translation);
      if (node.rotation !== undefined) mesh.quaternion.fromArray(node.rotation);
      if (node.scale !== undefined) mesh.scale.fromArray(node.scale);
      root.add(mesh);
    }
  }
  return root;
}

// Runs only when this file is the script (ring-sim.ts imports jadeRingOf and readGlbScene from it).
if (process.argv[1]?.endsWith("jade-ring-reference.ts") === true) {
  const DIR = "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/lab/models/weapons/";
  const fullGeo = bladeFromObject(readGlbScene(DIR + "clear-wind.glb"), {}, { keepUv: true })!;
  const map = fullGeo.userData.bladeMap as THREE.Matrix4;
  const lodGeo = bladeFromObject(readGlbScene(DIR + "clear-wind-swarm.glb"), {}, { keepUv: true, map })!;
  for (const [name, g] of [["full", fullGeo], ["lod", lodGeo]] as const) {
    const guard = guardBand(g);
    const bladeFrom = Math.max(0.01, guard[1] + 0.01);
    const anchors = auraAnchorsOf(g, guard, bladeFrom, edgeField(g, bladeFrom), true);
    const t0 = performance.now();
    const ring = jadeRingOf(g, guard, anchors.guardHalf);
    const ms = performance.now() - t0;
    console.log(name, `${ms.toFixed(1)} ms`, "guard", guard.map((v) => v.toFixed(4)).join(" … "), "guardHalf", anchors.guardHalf.toFixed(4), JSON.stringify(ring, (_k, v) => (typeof v === "number" ? Number(v.toFixed(5)) : v)));
  }
}
