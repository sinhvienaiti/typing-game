// Source: new for the kit: the focus strip's "Load" host mode (Last Line's ALIVE_PLAN AL-05; the owner's Q1 and Q2 of 01/11)
/**
 * Load is a host mode, not a seventh style in the players' list: a game turns
 * it on with FocusStripOptions.load (only Last Line does; every other game
 * stays as it was), and the strip then follows the juice study's E1–E3
 * (docs/games/TYPING_BREAK_STUDY.md §2.2–2.4, measured frame by frame) in the
 * game's own look (glyph rings, crystal shards, glass; never gold):
 * - a right key: the letter at 2.6× with a white star (f0), a disc in the
 *   gun's colour with a white core of 30 % (f1), a thick white ring (f2), a
 *   dark glyph ring with ticks and 2–4 dark crystal shards (f3–4), a thin
 *   white arc open toward the next letter (f5), a dark arc turning 40° a
 *   frame (f6–8), clean at f9 (150 ms); a clean streak's tier adds rays and
 *   moves the hue toward glass;
 * - a finished word: every letter white for a frame and the rim 0.36 em out
 *   (f0), the letters squeezed (f1–3), then the word as one line with a
 *   ribbon flying into the host's target (the bay's magazine cell) over
 *   f3–12, the cell flashing white when it lands; the plate dims 70 % and
 *   folds toward the target (f3–9); the meaning gets its own beat after f12;
 * - a wrong key: the due letter twitches in pixel steps (never a scale), a
 *   crimson underline (f0–5), a cracked copy of the key typed drops 12 px and
 *   breaks at f9; never a red flash of the plate;
 * - a stray key: its ghost in red where the word stands, 1.4 → 1, dropping;
 * - backspace: the letter taken back shrinks to the caret and fades (4 f),
 *   the caret slides back (3 f); a release folds the strip down (8 f);
 * - a flawless word: a FLAWLESS stamp (f0–8) and a white thread in the ribbon;
 * - hidden letters: the host's glass tiles (when it has the art) shimmer,
 *   crack and melt on a reveal, shatter when typed.
 * The player's Stamp (the default) plays as Load's key; other styles keep
 * their own key and get the rest. Pure numbers and the key's recipe here;
 * the strip (strip.ts) and the canvas (draw.ts) play them.
 */
import { PK } from "./pool";
import { FRAME_MS, TONE, restPose, type GlyphPose, type SpawnCtx, type StyleRecipe, type WordCtx } from "./styles";
import type { TypingFxStyle } from "./settings";

/** A box in the strip's root (px). */
export type LoadRect = { x: number; y: number; w: number; h: number };

/** What a game gives to turn the Load mode on. */
export type LoadHost = {
  /** Where a finished word lands (root px), the bay's magazine cell; false: it rises and fades (a full bay takes nothing). */
  target(out: LoadRect): boolean;
  /** The word reached its target (f12): the host's own impact on top of the kit's white flash. */
  onLand?(): void;
  /** The player style that plays Load's key (default "stamp", the owner's pick and every game's default). */
  style?: TypingFxStyle;
  /** The host draws hidden letters as glass tiles (its CSS on `.tfx-g.is-masked`, `--tfx-shine` 0 … 1); false: "_". */
  glass?: boolean;
  /** Extra classes on the FLAWLESS stamp and the meaning's line (a game's painted plates). */
  flawlessClass?: string;
  learnClass?: string;
  /** The stamp's text (English: the games are English). */
  flawless?: string;
};

const F = FRAME_MS;
/**
 * The 60 Hz frame of `age` ms. A held clock's sums of 1000 / 60 sit a hair under each frame's start (two frames
 * add to 33.333…330, not 33.333…336); a hundredth of a frame of slack keeps every step on its own frame.
 */
export const loadFrame = (age: number): number => Math.floor(age / F + 0.01);
const frameOf = loadFrame;
const clamp01 = (v: number): number => (v < 0 ? 0 : v > 1 ? 1 : v);

/**
 * Load's numbers: frames at 60 Hz, sizes as shares of the strip's font size
 * (its letters' cap height is about 0.7 of it: E1's "1.9× the letter" disc is
 * 0.68 here as a radius).
 */
export const LOAD = {
  key: { ms: 150, copy: 2.6, lift: 0.28, tilt: -3, star: 1.2, starIn: 0.09, disc: 0.68, core: 0.3, ring: 0.72, ringStroke: 0.2, dark: 0.76, darkStroke: 0.17, ticks: 12, arc: 0.83, gap: 1.15, turn: (40 * Math.PI) / 180, shards: 2, shardsMax: 4 },
  /** The clean streak's tiers (Last Line's 3, 6, 10, 20 clean words) and the star's rays at each. */
  tiers: [3, 6, 10, 20],
  rays: [4, 6, 8, 8, 10],
  /** The dark of the glyph ring and the arcs (rgba(20,12,12,.85), the study's E1). */
  dark: "rgba(20,12,12,0.85)",
  word: { flash: 1, flashPerfect: 2, rim: 0.36, squeeze: [0.86, 0.66, 0.5], flyAt: 3, flyFrames: 9, dim: 0.3, foldAt: 3, foldFrames: 6, gap: 150, ribs: 8, rib: 0.07, ribWidth: 0.2, thread: 0.36, land: 8 },
  learn: { at: 12, rise: 0.14, in: 8, hold: 650, out: 8 },
  flaw: { scale: [1.35, 1.12, 1], hold: 8, out: 4 },
  wrong: { twitch: [0.053, -0.053, 0.035, 0], bar: 6, drop: 0.21, crack: 9, shards: [2, 3] },
  stray: { from: 1.4, drop: 0.35, frames: 15 },
  back: { frames: 4, to: 0.6, slide: 3 },
  release: { frames: 8 },
  lock: { scale: [0.9, 0.96, 1.02, 1.04, 1.03, 1.01, 1], sweepFrom: 2, sweepTo: 12, breathe: 1500 },
  mask: { shimmer: 2400, phase: 0.7, reveal: 6, hint: 0.62 },
} as const;

/** The clean streak's tier: 0 under 3 clean words, then 1 … 4. */
export function loadTier(streak: number): number {
  let tier = 0;
  for (const from of LOAD.tiers) if (streak >= from) tier += 1;
  return tier;
}

/** The plate's scale `age` ms after a word locks (0.9 → 1.04 → 1 in steps, f0–6). */
export function lockScale(age: number): number {
  if (age < 0) return 1;
  return LOAD.lock.scale[frameOf(age)] ?? 1;
}

/** The light along the plate's top edge `age` ms after a lock: 0 … 1 across it from f2 to f12; −1 outside. */
export function sweepAt(age: number): number {
  const t = (age - LOAD.lock.sweepFrom * F) / ((LOAD.lock.sweepTo - LOAD.lock.sweepFrom) * F);
  return t < 0 || t > 1 ? -1 : t;
}

/** The plate's rim breathing while a word is typed, 0 … 1 over 1.5 s. */
export const breathe = (t: number): number => 0.5 - 0.5 * Math.cos((2 * Math.PI * t) / LOAD.lock.breathe);

/** A finished word's letters, squeezed toward the middle (f1–3), then gone into the flying line: scaleX, or 0 once it flies. */
export function wordSqueeze(age: number): number {
  const f = frameOf(age);
  if (f <= 0) return 1;
  return f <= LOAD.word.squeeze.length ? LOAD.word.squeeze[f - 1]! : 0;
}

/** The plate after a finished word: its alpha (dimmed 70 % from f1, so the muzzle owns the release) and its fold toward the target (scaleX, f3–9, ease-in). */
export function plateAfterWord(age: number): { alpha: number; fold: number } {
  const f = age / F + 0.01;
  const alpha = f < 1 ? 1 : LOAD.word.dim;
  const k = clamp01((f - LOAD.word.foldAt) / LOAD.word.foldFrames);
  return { alpha: k >= 1 ? 0 : alpha, fold: 1 - k * k };
}

/** A release (a word let go): the strip folds down in 8 frames, ease-in; 1 → 0. */
export function releaseFold(age: number): number {
  const k = clamp01(age / (LOAD.release.frames * F));
  return 1 - k * k;
}

/** The flight's progress `age` ms after the word completed: 0 … 1 from f3 to f12 (slow start, fast arrival); < 0 before it starts. */
export function flightAt(age: number): number {
  const t = (age - LOAD.word.flyAt * F) / (LOAD.word.flyFrames * F) + 0.001;
  if (t < 0) return -1;
  const x = clamp01(t);
  return x >= 1 ? 1 : x * (0.35 + 0.65 * x);
}

/** A point on the flight's curve at `u` (a quadratic from the row through `ctl` to the target). */
export function flightPoint(u: number, x0: number, y0: number, cx: number, cy: number, x1: number, y1: number, out: { x: number; y: number }): { x: number; y: number } {
  const v = 1 - u;
  out.x = v * v * x0 + 2 * v * u * cx + u * u * x1;
  out.y = v * v * y0 + 2 * v * u * cy + u * u * y1;
  return out;
}

/** The control point: the line leaves sideways along the row (off the lane's middle), then turns to the target. */
export function flightControl(x0: number, y0: number, x1: number, y1: number, out: { x: number; y: number }): { x: number; y: number } {
  out.x = x0 + (x1 - x0) * 0.85;
  out.y = y0 + (y1 - y0) * 0.1;
  return out;
}

/** The target's white flash `age` ms after the line lands: whole on its first frame, gone by f8; its scale 1.25 → 1. */
export function landFlash(age: number): { alpha: number; scale: number } {
  if (age < 0 || age >= LOAD.word.land * F) return { alpha: 0, scale: 1 };
  const f = frameOf(age);
  return { alpha: f === 0 ? 1 : Math.exp(-(age - F) / 40) * 0.9, scale: f === 0 ? 1.25 : f === 1 ? 1.1 : 1 };
}

/** The meaning's beat `age` ms after the word completed: alpha and rise (shares of the font size); it starts at f12. */
export function learnAt(age: number): { alpha: number; rise: number } {
  const t = age - LOAD.learn.at * F;
  const fadeIn = LOAD.learn.in * F;
  const out = LOAD.learn.out * F;
  if (t < 0) return { alpha: 0, rise: LOAD.learn.rise };
  if (t < fadeIn) return { alpha: t / fadeIn, rise: LOAD.learn.rise * (1 - t / fadeIn) };
  if (t < fadeIn + LOAD.learn.hold) return { alpha: 1, rise: 0 };
  return { alpha: Math.max(0, 1 - (t - fadeIn - LOAD.learn.hold) / out), rise: 0 };
}

/** How long the meaning stays fully readable (ms). */
export const LEARN_HOLD = LOAD.learn.hold;

/** The FLAWLESS stamp `age` ms after a flawless word: its scale in steps (f0–2), held to f8, gone by f12. */
export function flawAt(age: number): { alpha: number; scale: number } {
  if (age < 0) return { alpha: 0, scale: 1 };
  const f = frameOf(age);
  const scale = LOAD.flaw.scale[f] ?? 1;
  if (f < LOAD.flaw.hold) return { alpha: 1, scale };
  const alpha = 1 - (age - LOAD.flaw.hold * F) / (LOAD.flaw.out * F);
  return { alpha: alpha > 1e-6 ? alpha : 0, scale };
}

/** A stray key's ghost: scale 1.4 → 1, dropping 0.35 of the font size (20 px at 720p) over 15 frames, fading. */
export function strayAt(age: number, still: boolean): { alpha: number; scale: number; drop: number } {
  const T = LOAD.stray.frames * F;
  if (age < 0 || age >= T) return { alpha: 0, scale: 1, drop: 0 };
  const t = age / T;
  const f = frameOf(age);
  return { alpha: f < 2 ? 1 : 1 - (t - (2 * F) / T) / (1 - (2 * F) / T), scale: still ? 1 : f === 0 ? LOAD.stray.from : f === 1 ? 1.15 : 1, drop: still ? 0 : LOAD.stray.drop * t * t };
}

/** The shimmer of hidden letter `i`'s glass at `now` (0 … 1, 2.4 s a cycle, each letter 0.7 rad behind the one before). */
export const glassShine = (now: number, i: number): number => 0.5 + 0.5 * Math.sin((2 * Math.PI * now) / LOAD.mask.shimmer - i * LOAD.mask.phase);

/** Load's wrong-key twitch: +3, −3, +2, 0 px at 720p in steps (as em), never a scale. */
export function loadWrongPose(age: number, motion: number, out: GlyphPose): GlyphPose {
  restPose(out);
  if (age < 0 || age >= LOAD.wrong.twitch.length * F) return out;
  out.dx = (LOAD.wrong.twitch[frameOf(age)] ?? 0) * Math.min(1, motion);
  return out;
}

/** A letter taken back (backspace): its typed copy shrinks to the caret and fades in 4 frames. */
export function loadBackPose(age: number, motion: number, out: GlyphPose): GlyphPose {
  restPose(out);
  const T = LOAD.back.frames * F;
  if (age < 0 || age >= T) return out;
  const t = age / T;
  out.aOn = true;
  out.aScale = 1 - (1 - LOAD.back.to) * t * Math.min(1, motion);
  out.aDx = -0.18 * t * Math.min(1, motion);
  out.aAlpha = 1 - t;
  return out;
}

/** A hidden letter revealed by a wrong key: its glass cracks and melts in 6 frames while the letter comes in, pale (a hint). */
export function loadRevealPose(age: number, out: GlyphPose): GlyphPose {
  restPose(out);
  const T = LOAD.mask.reveal * F;
  if (age < 0 || age >= T) return out;
  out.alpha = LOAD.mask.hint * clamp01((age - 2 * F) / (T - 2 * F));
  out.hot = age < 2 * F ? 0.6 : 0;
  return out;
}

// ── The key (E1) ───────────────────────────────────────────────────────────

/** Every spawn goes through here: a multiplier of 0 (Low, Off) spawns nothing. */
function spawn(c: SpawnCtx, kind: number, tone: number, life: number, x = c.x, y = c.y, delay = 0): number {
  if (c.mult <= 0) return -1;
  const i = c.pool.spawn(kind as (typeof PK)[keyof typeof PK], c.owner, c.prio, x, y, c.now + delay, life);
  if (i >= 0) c.pool.tone[i] = tone;
  return i;
}

/** `n` crystal shards out from (x, y) at radius `r0`, `look` 0 dark, 1 glass, 2 crimson; `delay` ms. */
export function crystals(c: SpawnCtx, n: number, x: number, y: number, r0: number, look: number, tone: number, life: number, delay = 0, down = 0): void {
  for (let k = 0; k < n; k += 1) {
    const a = (k / n) * Math.PI * 2 + c.random() * 1.4;
    const dir = down > 0 ? Math.PI / 2 + (c.random() * 2 - 1) * 1.1 : a;
    const i = spawn(c, PK.crystal, tone, life * (0.85 + 0.3 * c.random()), x + Math.cos(dir) * r0, y + Math.sin(dir) * r0, delay);
    if (i < 0) return;
    c.pool.aux[i] = look;
    c.pool.size[i] = (0.11 + 0.07 * c.random()) * c.h * c.size;
    c.pool.rot[i] = dir;
    c.pool.spin[i] = c.still ? 0 : (c.random() * 2 - 1) * 14;
    if (c.still) continue;
    const speed = (7 + 6 * c.random()) * c.h;
    c.pool.vx[i] = Math.cos(dir) * speed;
    c.pool.vy[i] = Math.sin(dir) * speed;
    c.pool.drag[i] = 7;
    c.pool.grav[i] = down > 0 ? 18 * c.h : 4 * c.h;
  }
}

/** The key's tone by the streak's tier: the gun's colour, lighter from tier 2, glass at tier 4 (the hue shift of a clean streak). */
export const keyTone = (tier: number): number => (tier >= 4 ? TONE.glass : tier >= 2 ? TONE.light : TONE.accent);

export const LOAD_KEY: StyleRecipe = {
  id: "load",
  keyMs: LOAD.key.ms,
  clip: null,
  ghost: "hot",
  // f0: the stepped mark; f3: its crystal shards.
  phases: [0, 3 * F],
  keyPose(age, m, out) {
    restPose(out);
    if (age < 0 || age >= this.keyMs) return out;
    const f = frameOf(age);
    if (f === 0) {
      if (m <= 0) {
        out.hot = 1;
        return out;
      }
      // f0: the letter at 2.6×, high and a little tilted, white-hot and flat (the study: no shadow), the star's rays round it.
      out.alpha = 0;
      out.aOn = true;
      out.aScale = 1 + (LOAD.key.copy - 1) * m;
      out.aDy = -LOAD.key.lift * m;
      out.aRot = LOAD.key.tilt * m;
      return out;
    }
    // f1: down at 1× on the disc, white-hot; a landing squash, then the ink comes back as the rings pass.
    const HOT = [1, 1, 0.75, 0.5, 0.3, 0.15, 0.08, 0.04, 0.02];
    const SQUASH = [0, 0, 0.12, -0.05, 0.02, 0];
    out.hot = HOT[f] ?? 0;
    out.squash = (SQUASH[f] ?? 0) * m;
    out.dy = f === 2 ? 0.03 * m : 0;
    return out;
  },
  spawnKey(phase, c) {
    if (phase === 0) {
      const i = spawn(c, PK.loadKey, keyTone(c.tier), LOAD.key.ms);
      if (i >= 0) {
        c.pool.size[i] = c.h * c.size;
        c.pool.aux[i] = c.tier;
        // The arcs open toward the next letter (+x); a hair of turn so no two keys look stamped.
        c.pool.rot[i] = (c.random() - 0.5) * 0.3;
      }
      c.light(1, 0.45);
      c.light(-1, 0.25);
      return;
    }
    // f3: 2–4 dark crystal shards thrown off the dark ring (more with the streak).
    const n = Math.min(LOAD.key.shardsMax, LOAD.key.shards + Math.min(2, c.tier));
    crystals(c, c.mult > 0 ? n : 0, c.x, c.y, LOAD.key.dark * c.h, 0, keyTone(c.tier), 150);
  },
  spawnRelease(w: WordCtx) {
    // The study's f4–6: a thin white ring round the whole word as it squeezes.
    if (w.mult <= 0) return;
    const i = w.pool.spawn(PK.shock, w.owner, w.prio, w.cx, w.cy, w.now, 120);
    if (i < 0) return;
    w.pool.tone[i] = w.gold ? TONE.glass : TONE.hot;
    w.pool.size[i] = w.rowW / 2 + 0.25 * w.h;
    w.pool.size2[i] = 0.62 * w.h;
    w.pool.rot[i] = 0.035 * w.h;
    w.pool.aux[i] = w.still ? 0 : 0.12;
  },
  spawnWrong(c) {
    loadWrongBeat(c);
  },
};

/**
 * Load's wrong key (E2): a crimson underline kicked down and back (f0–5); a
 * cracked copy of the key typed over the due letter, dropping 12 px at 720p,
 * breaking into 2–3 crimson shards at f9. Nothing crosses the row after the
 * due letter or the meaning; no plate flash, no shake.
 */
export function loadWrongBeat(c: SpawnCtx): void {
  const b = spawn(c, PK.bar, TONE.crimson, LOAD.wrong.bar * F, c.x, c.y + 0.56 * c.h);
  if (b >= 0) {
    c.pool.size[b] = 0.36 * c.h;
    c.pool.size2[b] = c.still ? 0 : 0.11 * c.h;
    c.pool.aux[b] = Math.max(3, 0.1 * c.h);
  }
  if (c.key <= 32) return;
  const g = spawn(c, PK.crackGlyph, TONE.crimson, LOAD.wrong.crack * F, c.x, c.y - 0.95 * c.h);
  if (g >= 0) {
    c.pool.size[g] = 0.56 * c.h;
    c.pool.aux[g] = c.key;
    c.pool.size2[g] = c.still ? 0 : LOAD.wrong.drop * c.h;
  }
  const n = LOAD.wrong.shards[0] + (c.random() < 0.5 ? 0 : 1);
  crystals(c, n, c.x, c.y - 0.95 * c.h + (c.still ? 0 : LOAD.wrong.drop * c.h), 0.12 * c.h, 2, TONE.crimson, 130, LOAD.wrong.crack * F, 1);
}

/** A hidden letter typed right: its glass bursts into glass shards and a small star (a reward for remembering it). */
export function glassBurst(c: SpawnCtx): void {
  crystals(c, 4, c.x, c.y, 0.3 * c.h, 1, TONE.glass, 170);
  const s = spawn(c, PK.star, TONE.glass, 150, c.x + 0.32 * c.h, c.y - 0.42 * c.h);
  if (s >= 0) c.pool.size[s] = 0.34 * c.h;
}

/** A hidden letter revealed by a wrong key: cracks over its glass (f0–2), then the glass melts into shards (f2–6). */
export function glassReveal(c: SpawnCtx): void {
  const k = spawn(c, PK.glassCrack, TONE.glass, LOAD.mask.reveal * F);
  if (k >= 0) {
    c.pool.size[k] = 0.5 * c.h;
    c.pool.rot[k] = c.random() * Math.PI * 2;
  }
  crystals(c, 3, c.x, c.y, 0.18 * c.h, 1, TONE.glass, 4 * F, 2 * F, 1);
}

/** The caret sliding back from `fromX` to `c.x` under the row in 3 frames (backspace). */
export function caretSlide(c: SpawnCtx, fromX: number): void {
  const i = spawn(c, PK.slide, TONE.hot, LOAD.back.slide * F, fromX, c.y + 0.56 * c.h);
  if (i < 0) return;
  c.pool.aux[i] = c.still ? fromX : c.x;
  c.pool.size[i] = 0.3 * c.h;
  c.pool.size2[i] = Math.max(2, 0.075 * c.h);
}
