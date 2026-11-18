// Ticket 259 · Claude's acceptance simulation of chunk RING on the real colour map (check 6; the critic's defect 2).
// Text in the notes folder, not game code; Codex does not run it.
//
// Orthographic views of the guard from +z (front) and −z (back), 2000 px per unit blade, the top-most surface per
// pixel, the colour map's nearest texel (linear), then the ticket's §2 RING rules with hard edges: the region (inside
// rCut, under both crest planes plus the margin, not a bead) and the colour classes (white jade, pale gold). Per view it
// prints the share of pixels changed (J + G > 0.05) in two radius bands round the hole's centre:
//   gold  0.084–0.092: the painted gold line on the disc's outer wall (and what covers it): must stay as the reference;
//   flange 0.092–0.102: the flange to the silver rim, kept by design: must stay ≤ 3 %.
//
// Run from the game's root; ImageMagick (`magick`) decodes the GLB's JPEG colour map into a temporary folder:
//   cd /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation
//   node node_modules/tsx/dist/cli.mjs ../../docs/codex-queue/259/ring-sim.ts [<root>]
// With <root> (e.g. ../.wt-immortality-cultivation-codex) it measures with that tree's exported jadeRingOf (its port);
// without, with jade-ring-reference.ts. Exit code 1 when a limit fails.
//
// Reference (04/11/2026, HEAD bc94110, rCut at the flange's inner edge), changed share gold band / flange band:
//   full front 37.7 % / 1.8 %   full back 33.9 % / 1.4 %   lod front 40.9 % / 0.0 %   lod back 36.1 % / 0.0 %
// The earlier rCut in the flange's middle gave flange 18.8 / 14.4 / 19.4 / 14.0 % (the critic's defect 2).
import { execFileSync } from "node:child_process";
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { pathToFileURL } from "node:url";
import * as THREE from "../../../games/immortality-cultivation/node_modules/three/build/three.module.js";
import { jadeRingOf as referenceRing, readGlbScene, type JadeRing } from "./jade-ring-reference";

const MAIN = resolve(__dirname, "../../../games/immortality-cultivation");
const GLB = join(MAIN, "art-src/lab/models/weapons/");
const PPU = 2000;
const GOLD_REF: Record<string, number> = { "full front": 37.7, "full back": 33.9, "lod front": 40.9, "lod back": 36.1 };
const FLANGE_MAX = 3;

const ss = (a: number, b: number, x: number): number => {
  const t = Math.min(1, Math.max(0, (x - a) / (b - a)));
  return t * t * (3 - 2 * t);
};
const lin = (c: number): number => {
  const v = c / 255;
  return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4;
};

/** The GLB's base colour map as raw 8-bit RGB rows from the top (glTF UV: v down), decoded by ImageMagick. */
function colourMap(path: string, dir: string): { rgb: Buffer; w: number; h: number } {
  const buf = readFileSync(path);
  const jsonLen = buf.readUInt32LE(12);
  const json = JSON.parse(buf.subarray(20, 20 + jsonLen).toString("utf8"));
  const bin = 20 + jsonLen + 8;
  const tex = json.materials[0].pbrMetallicRoughness.baseColorTexture.index;
  const image = json.images[json.textures[tex].source];
  const view = json.bufferViews[image.bufferView];
  const src = join(dir, "colour.img");
  writeFileSync(src, buf.subarray(bin + (view.byteOffset ?? 0), bin + (view.byteOffset ?? 0) + view.byteLength));
  const [w, h] = execFileSync("magick", ["identify", "-format", "%w %h", src]).toString().trim().split(" ").map(Number) as [number, number];
  const raw = join(dir, "colour.rgb");
  execFileSync("magick", [src, "-depth", "8", `rgb:${raw}`]);
  return { rgb: readFileSync(raw), w, h };
}

interface Bands {
  gold: number;
  flange: number;
  region: { jade: number; gold: number; kept: number };
}

/** One view (side +1 front, −1 back) of geometry `g` with ring `R` (see the header). */
function view(g: THREE.BufferGeometry, R: JadeRing, map: { rgb: Buffer; w: number; h: number }, side: number): Bands {
  const pos = g.getAttribute("position");
  const uv = g.getAttribute("uv");
  const index = g.getIndex()!;
  const x0 = R.x - 0.13;
  const y1 = R.y + 0.13;
  const N = Math.round(0.26 * PPU);
  const depth = new Float32Array(N * N).fill(-Infinity);
  const zs = new Float32Array(N * N);
  const us = new Float32Array(N * N);
  const vs = new Float32Array(N * N);
  for (let t = 0; t + 2 < index.count; t += 3) {
    const ids = [index.getX(t), index.getX(t + 1), index.getX(t + 2)];
    const P = ids.map((k) => [pos.getX(k), pos.getY(k), pos.getZ(k)] as const);
    if (P.every((p) => Math.hypot(p[0] - R.x, p[1] - R.y) > 0.14)) continue;
    const S = P.map((p) => [(p[0] - x0) * PPU, (y1 - p[1]) * PPU] as const);
    const [A, B, C] = S as [readonly [number, number], readonly [number, number], readonly [number, number]];
    const area = (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0]);
    if (Math.abs(area) < 1e-12) continue;
    const ya = Math.max(0, Math.floor(Math.min(A[1], B[1], C[1])));
    const yb = Math.min(N - 1, Math.ceil(Math.max(A[1], B[1], C[1])));
    const xa = Math.max(0, Math.floor(Math.min(A[0], B[0], C[0])));
    const xb = Math.min(N - 1, Math.ceil(Math.max(A[0], B[0], C[0])));
    for (let y = ya; y <= yb; y += 1) {
      for (let x = xa; x <= xb; x += 1) {
        const px = x + 0.5;
        const py = y + 0.5;
        const w0 = ((B[0] - px) * (C[1] - py) - (B[1] - py) * (C[0] - px)) / area;
        const w1 = ((C[0] - px) * (A[1] - py) - (C[1] - py) * (A[0] - px)) / area;
        const w2 = 1 - w0 - w1;
        if (w0 < 0 || w1 < 0 || w2 < 0) continue;
        const z = w0 * P[0]![2] + w1 * P[1]![2] + w2 * P[2]![2];
        const k = y * N + x;
        if (z * side <= depth[k]!) continue;
        depth[k] = z * side;
        zs[k] = z;
        us[k] = w0 * uv.getX(ids[0]!) + w1 * uv.getX(ids[1]!) + w2 * uv.getX(ids[2]!);
        vs[k] = w0 * uv.getY(ids[0]!) + w1 * uv.getY(ids[1]!) + w2 * uv.getY(ids[2]!);
      }
    }
  }
  const band = { gold: [0, 0], flange: [0, 0] };
  const region = { jade: 0, gold: 0, kept: 0 };
  for (let k = 0; k < N * N; k += 1) {
    if (!Number.isFinite(depth[k]!)) continue;
    const X = x0 + ((k % N) + 0.5) / PPU;
    const Y = y1 - (Math.floor(k / N) + 0.5) / PPU;
    const qx = X - R.x;
    const qy = Y - R.y;
    const d = Math.hypot(qx, qy);
    if (d < 0.084 || d >= 0.102) continue;
    const u = Math.min(map.w - 1, Math.max(0, Math.floor(us[k]! * map.w)));
    const v = Math.min(map.h - 1, Math.max(0, Math.floor(vs[k]! * map.h)));
    const o = (v * map.w + u) * 3;
    const r = lin(map.rgb[o]!);
    const gg = lin(map.rgb[o + 1]!);
    const b = lin(map.rgb[o + 2]!);
    // sword-material.ts JADE (the beads) and §2 RING, hard-edged.
    const bead = ss(0.07, 0.17, (gg - r) / Math.max(gg, 0.04)) * ss(-0.05, 0, gg - b);
    const capF = R.front.a + R.front.bx * qx + R.front.by * qy + R.margin;
    const capB = R.back.a + R.back.bx * qx + R.back.by * qy + R.margin;
    const inside = (d < R.rCut ? 1 : 0) * (zs[k]! < capF ? 1 : 0) * (-zs[k]! < capB ? 1 : 0) * (1 - bead);
    const lum = 0.2126 * r + 0.7152 * gg + 0.0722 * b;
    const mx = Math.max(r, gg, b);
    const sat = (mx - Math.min(r, gg, b)) / Math.max(mx, 1e-3);
    const gk = ss(0.38, 0.52, sat) * ss(0.05, 0.12, r - b);
    const jk = (1 - gk) * ss(0.2, 0.35, lum) * (1 - ss(0.18, 0.3, sat));
    const J = inside * jk;
    const G = inside * gk;
    const acc = d < 0.092 ? band.gold : band.flange;
    acc[0]! += 1;
    if (J + G > 0.05) acc[1]! += 1;
    if (inside >= 0.5) {
      if (J > 0.5) region.jade += 1;
      else if (G > 0.5) region.gold += 1;
      else region.kept += 1;
    }
  }
  const pct = (a: number[]): number => Math.round((1000 * a[1]!) / Math.max(1, a[0]!)) / 10;
  return { gold: pct(band.gold), flange: pct(band.flange), region };
}

async function main(): Promise<void> {
  const root = process.argv[2] !== undefined ? resolve(process.argv[2]) : null;
  const bladesUrl = pathToFileURL(join(root ?? MAIN, "src/view/skills/blades.ts")).href;
  const materialUrl = pathToFileURL(join(root ?? MAIN, "src/view/skills/sword-material.ts")).href;
  const blades = await import(bladesUrl);
  const { edgeField } = await import(materialUrl);
  const measure: typeof referenceRing = root !== null ? blades.jadeRingOf : referenceRing;
  if (typeof measure !== "function") throw new Error(`no jadeRingOf exported by ${bladesUrl}`);
  const dir = mkdtempSync(join(tmpdir(), "ring-sim-"));
  let ok = true;
  try {
    const fullGeo = blades.bladeFromObject(readGlbScene(GLB + "clear-wind.glb"), {}, { keepUv: true });
    const lodGeo = blades.bladeFromObject(readGlbScene(GLB + "clear-wind-swarm.glb"), {}, { keepUv: true, map: fullGeo.userData.bladeMap });
    for (const [name, g, file] of [["full", fullGeo, "clear-wind.glb"], ["lod", lodGeo, "clear-wind-swarm.glb"]] as const) {
      const guard = blades.guardBand(g);
      const bladeFrom = Math.max(0.01, guard[1] + 0.01);
      const anchors = blades.auraAnchorsOf(g, guard, bladeFrom, edgeField(g, bladeFrom), true);
      const R = measure(g, guard, anchors.guardHalf, (step: string) => console.log(`${name}: jadeRingOf failed at ${step}`));
      if (R === null) {
        ok = false;
        continue;
      }
      const map = colourMap(GLB + file, dir);
      for (const side of [1, -1]) {
        const key = `${name} ${side > 0 ? "front" : "back"}`;
        const b = view(g, R, map, side);
        const pass = b.flange <= FLANGE_MAX && b.gold >= GOLD_REF[key]! - 1;
        ok &&= pass;
        console.log(JSON.stringify({ view: key, rCut: Number(R.rCut.toFixed(5)), goldBand: b.gold, goldRef: GOLD_REF[key], flangeBand: b.flange, flangeMax: FLANGE_MAX, inRegion084to102: b.region, pass }));
      }
    }
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
  console.log(ok ? "PASS" : "FAIL");
  if (!ok) process.exitCode = 1;
}

void main();
