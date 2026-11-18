#!/usr/bin/env node
// What a fixed perspective game camera can show: the numbers a map concept is written from.
// No dependencies. Mirrors a three.js PerspectiveCamera (vertical FOV, lookAt with +y up).
//
//   node frame-budget.mjs --camera cam.json [--layout layout.json] [--size 1280x720] [--unit 2]
//                         [--json] [--mvg blocks.mvg] [--check pairs.json]
//
// cam.json, either form (metres and degrees, the engine's own world axes; yaw 0 looks toward -z):
//   { "pitch": 42, "fov": 42, "yaw": 0, "look": [3, 0, 3], "distance": 46 }      orbit rig: camera = look + offset
//   { "pitch": 36, "fov": 42, "yaw": 0, "position": [0, 19.8, 17.75] }            camera placed directly
//   optional: "groundY" (play surface height, default 0)
// layout.json (all optional):
//   { "points": [{ "name": "Gate", "at": [x, y, z] }],
//     "boxes":  [{ "name": "Warden", "centre": [x, z], "size": [w, d], "height": h, "base": 0, "rot": 0, "rgba": [255, 0, 212, 0.5] }],
//     "ground": [{ "name": "Ink spill", "pts": [[x, z], ...], "y": 0, "rgba": [128, 0, 200, 0.55] }],
//     "hud":    [{ "name": "Status bar", "box": [x0, y0, x1, y1], "always": true }] }   HUD boxes in px at --size
// pairs.json: [{ "what": "bridge end", "world": [x, y, z], "screen": [px, py] }]  the engine's own projection,
//   taken from the running game at --size; prints the script's error in px. Trust no table until this is ≤ 2 px.
// --mvg writes an ImageMagick draw file (blocks translucent, HUD flat grey, no text):
//   magick capture.png -modulate 100,55 -draw @blocks.mvg -strip base.png
import { readFileSync, writeFileSync } from "node:fs";
import { pathToFileURL } from "node:url";

const DEG = Math.PI / 180;
const args = process.argv.slice(2);
const opt = (name, fallback) => {
  const i = args.indexOf("--" + name);
  return i >= 0 && args[i + 1] && !args[i + 1].startsWith("--") ? args[i + 1] : fallback;
};
const has = (name) => args.includes("--" + name);
const readJson = (p) => JSON.parse(readFileSync(p, "utf8"));
const r1 = (v) => Math.round(v * 10) / 10;
const r0 = Math.round;

const sub = (a, b) => [a[0] - b[0], a[1] - b[1], a[2] - b[2]];
const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
const cross = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
const norm = (a) => { const l = Math.hypot(...a); return a.map((v) => v / l); };

export function makeCamera(c, W = 1280, H = 720) {
  const pitch = c.pitch * DEG, yaw = (c.yaw ?? 0) * DEG;
  const f = [-Math.sin(yaw) * Math.cos(pitch), -Math.sin(pitch), -Math.cos(yaw) * Math.cos(pitch)];
  const P = c.position ?? sub(c.look, f.map((v) => v * c.distance));
  const r = norm(cross(f, [0, 1, 0]));
  const u = cross(r, f);
  const t = Math.tan((c.fov * DEG) / 2);
  const aspect = W / H;
  const g0 = c.groundY ?? 0;
  const ray = (px, py) => { const nx = (px / W) * 2 - 1, ny = 1 - (py / H) * 2; return norm([0, 1, 2].map((i) => f[i] + r[i] * nx * t * aspect + u[i] * ny * t)); };
  const cam = {
    c, P, f, r, u, t, W, H, g0,
    project(x, y, z) {
      const v = sub([x, y, z], P), depth = dot(v, f);
      const nx = dot(v, r) / (depth * t * aspect), ny = dot(v, u) / (depth * t);
      return { px: ((nx + 1) / 2) * W, py: ((1 - ny) / 2) * H, depth, inFrame: depth > 0 && Math.abs(nx) <= 1 && Math.abs(ny) <= 1 };
    },
    /** Ground point (y = groundY) under a screen pixel, or null when that pixel looks at or above the horizon. */
    groundAt(px, py) {
      const d = ray(px, py);
      if (d[1] >= 0) return null;
      const k = (g0 - P[1]) / d[1];
      return { x: P[0] + d[0] * k, z: P[2] + d[2] * k };
    },
    /** Degrees below horizontal of the ray through a pixel (negative: it looks at sky). */
    depression(px, py) { return -Math.asin(ray(px, py)[1]) / DEG; },
    /** Height above ground at (x, z) where the frame's top edge cuts a vertical line, and the screen x there. */
    topLimit(x, z) {
      const g = sub(u, f.map((v) => v * t));
      const y = P[1] - (g[0] * (x - P[0]) + g[2] * (z - P[2])) / g[1];
      const p = cam.project(x, y, z);
      return { h: y - g0, px: p.px, depth: p.depth, sideways: p.depth > 0 && (p.px < 0 || p.px > W) };
    },
    /** For a foot inside the frame whose vertical line leaves through a side edge (tall things lean outward):
     *  the height at which it crosses that side edge. */
    sideLimit(x, z) {
      const a = r[0] * (x - P[0]) + r[2] * (z - P[2]);
      if (a === 0) return null;
      const need = Math.abs(a) / (t * aspect);
      const y = P[1] + (need - f[0] * (x - P[0]) - f[2] * (z - P[2])) / f[1];
      const p = cam.project(x, y, z);
      return { h: y - g0, px: p.px, py: p.py, edge: a < 0 ? "left" : "right" };
    },
    /** For a foot below the frame's bottom edge: the height at which a vertical line there enters the frame. */
    bottomEntry(x, z) {
      const g = [0, 1, 2].map((i) => u[i] + f[i] * t);
      const y = P[1] - (g[0] * (x - P[0]) + g[2] * (z - P[2])) / g[1];
      const p = cam.project(x, y, z);
      return { h: y - g0, px: p.px, depth: p.depth };
    },
  };
  return cam;
}

function hull(points) {
  const p = [...points].sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  const z = (o, a, b) => (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
  const lo = [], hi = [];
  for (const q of p) { while (lo.length >= 2 && z(lo.at(-2), lo.at(-1), q) <= 0) lo.pop(); lo.push(q); }
  for (const q of p.reverse()) { while (hi.length >= 2 && z(hi.at(-2), hi.at(-1), q) <= 0) hi.pop(); hi.push(q); }
  return [...lo.slice(0, -1), ...hi.slice(0, -1)];
}

function boxOutline(cam, b) {
  const [cx, cz] = b.centre, [w, d] = b.size, base = (b.base ?? 0) + cam.g0, rot = (b.rot ?? 0) * DEG;
  const pts = [];
  for (const dx of [-w / 2, w / 2]) for (const dz of [-d / 2, d / 2]) for (const y of [base, base + b.height]) {
    const p = cam.project(cx + dx * Math.cos(rot) + dz * Math.sin(rot), y, cz - dx * Math.sin(rot) + dz * Math.cos(rot));
    if (p.depth > 0.1) pts.push([p.px, p.py]);
  }
  return hull(pts).map(([x, y]) => [r0(x), r0(y)]);
}

const clipBox = (pts, W, H) => {
  const xs = pts.map((q) => q[0]), ys = pts.map((q) => q[1]);
  const box = [Math.min(...xs), Math.min(...ys), Math.max(...xs), Math.max(...ys)];
  const clipped = [Math.max(0, box[0]), Math.max(0, box[1]), Math.min(W, box[2]), Math.min(H, box[3])];
  return { box, clipped, visible: clipped[0] < clipped[2] && clipped[1] < clipped[3] };
};

function main() {
  if (!opt("camera")) { console.error("usage: node frame-budget.mjs --camera cam.json [--layout layout.json] [--size 1280x720] [--unit 2] [--json] [--mvg out.mvg] [--check pairs.json]"); process.exit(2); }
  const [W, H] = opt("size", "1280x720").split("x").map(Number);
  const unit = Number(opt("unit", "2"));
  const cam = makeCamera(readJson(opt("camera")), W, H);
  const layout = opt("layout") ? readJson(opt("layout")) : {};
  const out = { size: [W, H], camera: { ...cam.c, at: cam.P.map(r1) } };

  const topCentre = cam.depression(W / 2, 0), topCorner = Math.min(cam.depression(0, 0), cam.depression(W, 0));
  out.sky = {
    topCentreDeg: r1(topCentre), topCornerDeg: r1(topCorner), visible: topCorner < 0,
    horizonPy: r0((1 - Math.tan(cam.c.pitch * DEG) / cam.t) / 2 * H),
    note: topCorner < 0 ? "the horizon is in frame: sky shows" : `no sky: the top edge looks ${r1(topCorner)}° or more below the horizon`,
  };

  const cols = [0.2, 0.5, 0.8].map((k) => r0(W * k));
  out.rows = [];
  for (let i = 0; i <= 8; i += 1) {
    const py = Math.min(r0((H * i) / 8), H - 1);
    const mid = cam.groundAt(W / 2, py);
    if (!mid) { out.rows.push({ py, ground: null }); continue; }
    const left = cam.groundAt(0, py), right = cam.groundAt(W, py);
    const a = cam.project(mid.x, cam.g0, mid.z), b = cam.project(mid.x + 1, cam.g0, mid.z), top = cam.project(mid.x, cam.g0 + unit, mid.z);
    const budget = cols.map((px) => { const g = cam.groundAt(px, py); return g ? r1(cam.topLimit(g.x, g.z).h) : null; });
    out.rows.push({ py, ground: [r1(mid.x), r1(mid.z)], visibleX: [r1(left.x), r1(right.x)], pxPerM: r1(b.px - a.px), unitPx: r0(a.py - top.py), heightBudget: Object.fromEntries(cols.map((c, j) => [c, budget[j]])) });
  }
  const near = out.rows.filter((q) => q.ground).at(-1);
  out.texel = { nearPxPerM: near.pxPerM, texelsPerMetreDpr1: r0(near.pxPerM), texelsPerMetreDpr2: r0(near.pxPerM * 2), note: "ground textures need at least this many texels per metre at the nearest row to stay sharp (more at the closest zoom); set anisotropy 8-16 for the far rows" };

  // The vertical budget at a ground spot: how tall a thing standing there can be before the top edge cuts it,
  // or, for a spot nearer than the bottom edge, how tall before it rises into the frame over the play.
  const vertical = (x, z) => {
    const foot = cam.project(x, cam.g0, z), lim = cam.topLimit(x, z);
    if (foot.depth > 0 && foot.py > H) {
      const b = cam.bottomEntry(x, z);
      const sideways = b.px < 0 || b.px > W;
      return { kind: "below", entersM: r1(b.h), px: r0(b.px), sideways, text: sideways ? "foot below the frame; never enters it" : `foot below the frame; rises into it above ${r1(b.h)} m (screen x ${r0(b.px)})` };
    }
    if (lim.depth <= 0) return { kind: "none", text: "no top limit in front of the camera" };
    if (lim.sideways) {
      const s = foot.inFrame ? cam.sideLimit(x, z) : null;
      if (!s) return { kind: "sideways", text: "outside the frame sideways at any height" };
      return { kind: "side", sideLimitM: r1(s.h), px: r0(s.px), py: r0(s.py), edge: s.edge, text: `≤ ${r1(s.h)} m before it leans out of the ${s.edge} edge (at screen y ${r0(s.py)}); check the side HUD cards` };
    }
    return { kind: "top", topLimitM: r1(lim.h), px: r0(lim.px), text: lim.h < 0 ? `shows only below ${r1(lim.h)} m (screen x ${r0(lim.px)})` : `≤ ${r1(lim.h)} m before the top edge cuts it (screen x ${r0(lim.px)})` };
  };
  out.points = (layout.points ?? []).map((q) => {
    const p = cam.project(...q.at);
    return { name: q.name, at: q.at, px: [r0(p.px), r0(p.py)], at1080: [r0(p.px * 1080 / H), r0(p.py * 1080 / H)], inFrame: p.inFrame, vertical: vertical(q.at[0], q.at[2]) };
  });
  out.boxes = (layout.boxes ?? []).map((b) => {
    const outline = boxOutline(cam, b), cb = clipBox(outline, W, H), v = vertical(b.centre[0], b.centre[1]);
    const top = b.height + (b.base ?? 0);
    const note = v.kind === "top" ? (top > v.topLimitM ? `cropped: top ${top} m over the ${v.topLimitM} m budget` : `whole (budget ${v.topLimitM} m)`) : v.kind === "side" ? (top > v.sideLimitM ? `cropped: leans out of the ${v.edge} edge above ${v.sideLimitM} m` : `whole (side budget ${v.sideLimitM} m); check it clears the side HUD cards`) : v.kind === "below" ? (top > v.entersM ? `rises into the frame from below (above ${v.entersM} m): check it hides no play or HUD-free zone` : "stays below the frame") : v.text;
    return { name: b.name, outline, ...cb, vertical: v, note, rgba: b.rgba };
  });
  out.ground = (layout.ground ?? []).map((g) => {
    const outline = g.pts.map(([x, z]) => { const p = cam.project(x, cam.g0 + (g.y ?? 0), z); return [r0(p.px), r0(p.py)]; });
    return { name: g.name, outline, ...clipBox(outline, W, H), rgba: g.rgba };
  });
  out.hud = (layout.hud ?? []).map((h) => {
    const [x0, y0, x1, y1] = h.box;
    const corners = [[x0, y0], [x1, y0], [x1, y1], [x0, y1]].map(([x, y]) => cam.groundAt(x, y)).map((g) => (g ? [r1(g.x), r1(g.z)] : null));
    return { name: h.name, box: h.box, always: h.always !== false, hidesGround: corners };
  });

  if (opt("check")) {
    const pairs = readJson(opt("check")).map((q) => { const p = cam.project(...q.world); const e = Math.hypot(p.px - q.screen[0], p.py - q.screen[1]); return { what: q.what, engine: q.screen, script: [r1(p.px), r1(p.py)], errPx: r1(e) }; });
    out.check = { maxErrPx: Math.max(...pairs.map((q) => q.errPx)), pairs };
  }

  if (opt("mvg")) {
    const fill = (c, fallback) => { const [R, G, B, A] = c ?? fallback; return `stroke rgba(${R},${G},${B},${Math.min(1, A + 0.3).toFixed(2)}) stroke-width 1.5 fill rgba(${R},${G},${B},${A.toFixed(2)})`; };
    const lines = [];
    for (const g of out.ground) lines.push(fill(g.rgba, [255, 255, 255, 0.5]), `polygon ${g.outline.map((q) => q.join(",")).join(" ")}`);
    for (const b of out.boxes) lines.push(fill(b.rgba, [255, 0, 212, 0.5]), `polygon ${b.outline.map((q) => q.join(",")).join(" ")}`);
    for (const h of out.hud) lines.push(`stroke none fill ${h.always ? "rgba(128,128,128,0.92)" : "rgba(205,205,205,0.55)"}`, `rectangle ${h.box[0]},${h.box[1]} ${h.box[2]},${h.box[3]}`);
    writeFileSync(opt("mvg"), lines.join("\n") + "\n");
  }

  if (has("json")) { console.log(JSON.stringify(out, null, 1)); return; }
  const c = out.camera;
  console.log(`Camera at (${c.at.join(", ")}), pitch ${c.pitch}°, vertical FOV ${c.fov}°, ${W}×${H}. Sky: ${out.sky.note} (top centre ${out.sky.topCentreDeg}°, horizon at y ${out.sky.horizonPy}).\n`);
  console.log(`| Screen y | Ground (x, z) at centre | Visible x | px per m | ${unit} m figure (px) | Height budget (m) at x ${cols.join(" / ")} |\n|---|---|---|---|---|---|`);
  for (const q of out.rows) if (q.ground) console.log(`| ${q.py} | (${q.ground.join(", ")}) | ${q.visibleX[0]} … ${q.visibleX[1]} | ${q.pxPerM} | ${q.unitPx} | ${cols.map((k) => q.heightBudget[k]).join(" / ")} |`);
  console.log(`\nGround texel need: ${out.texel.texelsPerMetreDpr1} texels/m at dpr 1, ${out.texel.texelsPerMetreDpr2} at dpr 2 (nearest row).`);
  if (out.points.length) {
    console.log(`\n| Point | World | ${W}×${H} | 1080p | In frame | Vertical budget at its ground spot |\n|---|---|---|---|---|---|`);
    for (const q of out.points) console.log(`| ${q.name} | (${q.at.join(", ")}) | (${q.px.join(", ")}) | (${q.at1080.join(", ")}) | ${q.inFrame ? "yes" : "no"} | ${q.vertical.text} |`);
  }
  if (out.boxes.length) {
    console.log(`\n| Block | Screen box (clipped) | Height check |\n|---|---|---|`);
    for (const b of out.boxes) console.log(`| ${b.name} | ${b.visible ? `x ${b.clipped[0]}–${b.clipped[2]}, y ${b.clipped[1]}–${b.clipped[3]}` : "not in frame"} | ${b.note} |`);
  }
  for (const g of out.ground) console.log(`Ground shape ${g.name}: ${g.visible ? `x ${g.clipped[0]}–${g.clipped[2]}, y ${g.clipped[1]}–${g.clipped[3]}` : "not in frame"}`);
  for (const h of out.hud) console.log(`HUD ${h.name} (${h.box.join(", ")}) hides ground ${h.hidesGround.map((q) => (q ? `(${q.join(", ")})` : "sky")).join(" ")}`);
  if (out.check) console.log(`\nEngine check: max error ${out.check.maxErrPx} px over ${out.check.pairs.length} points${out.check.maxErrPx > 2 ? " (FAIL: fix the camera model before using any number)" : ""}.`);
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) main();
