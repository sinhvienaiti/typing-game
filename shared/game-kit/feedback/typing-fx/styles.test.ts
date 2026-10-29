// Source: new for the kit: the six letter-effect styles (timing budgets, rest, reduced motion, particle budgets)
import { describe, expect, it } from "vitest";
import { comboParticles, INTENSITY, levelFor } from "./intensity";
import { ParticlePool } from "./pool";
import { TYPING_FX_STYLES } from "./settings";
import { FRAME_MS, flyEase, newPose, popEnvelope, spawnWrongBeat, squeeze, STYLES, wrongPose, WRONG_MS, type GlyphPose, type SpawnCtx } from "./styles";
import { PK } from "./pool";

const ctx = (pool: ParticlePool, mult = 1, still = false): SpawnCtx => {
  let seed = 11;
  return { pool, owner: 1, prio: 1, x: 300, y: 120, h: 52, glyph: 0, now: 0, mult, size: 1, still, random: () => ((seed = (seed * 16807) % 2147483647) / 2147483647), light: () => {}, key: 0 };
};

const isRest = (p: GlyphPose): boolean => p.scale === 1 && p.rot === 0 && p.dx === 0 && p.dy === 0 && p.alpha === 1 && p.hot === 0 && !p.aOn && !p.bOn;

/** Spawns every phase of a style's key; how many particles it made. */
function keyParticles(style: (typeof TYPING_FX_STYLES)[number], mult: number, still = false): number {
  const pool = new ParticlePool(400);
  const c = ctx(pool, mult, still);
  STYLES[style].phases.forEach((_, phase) => STYLES[style].spawnKey(phase, c));
  return pool.count;
}

describe("typing-fx styles", () => {
  it("each style starts on the key's own frame and is back at rest by its end (≤ 400 ms)", () => {
    const out = newPose();
    for (const id of TYPING_FX_STYLES) {
      const style = STYLES[id];
      expect(style.keyMs).toBeLessThanOrEqual(400);
      expect(isRest(style.keyPose(0, 1, out)), id + " at 0 ms").toBe(false);
      expect(isRest(style.keyPose(style.keyMs, 1, out)), id + " at its end").toBe(true);
      expect(isRest(style.keyPose(-5, 1, out))).toBe(true);
    }
  });

  it("stamp slams from 3× to 1× in three frames and lands at 50 ms (T1)", () => {
    const out = newPose();
    const scales = [0, 1, 2].map((f) => STYLES.stamp.keyPose(f * FRAME_MS + 1, 1, out).aScale);
    expect(scales).toEqual([3, 2.35, 1.6]);
    expect(STYLES.stamp.keyPose(10, 1, out).alpha).toBe(0);
    const landed = STYLES.stamp.keyPose(51, 1, out);
    expect(landed.aOn).toBe(false);
    expect(landed.alpha).toBe(1);
    expect(landed.hot).toBeGreaterThan(0.9);
    expect(STYLES.stamp.phases).toEqual([50]);
  });

  it("smash punches at 2.1× for one frame under the white disc (T2), done by 150 ms", () => {
    const out = newPose();
    expect(STYLES.smash.keyPose(1, 1, out).scale).toBeCloseTo(2.1, 10);
    expect(STYLES.smash.keyPose(FRAME_MS + 1, 1, out).scale).toBe(1);
    expect(STYLES.smash.keyMs).toBe(150);
  });

  it("the six styles look different: their pose curves over the first 200 ms differ pairwise", () => {
    const out = newPose();
    const sig = (id: (typeof TYPING_FX_STYLES)[number]): string =>
      Array.from({ length: 13 }, (_, k) => {
        const p = STYLES[id].keyPose(k * FRAME_MS + 1, 1, out);
        return [p.scale, p.alpha, p.hot, p.aOn, p.bOn, p.dy].map((v) => (typeof v === "number" ? v.toFixed(2) : v)).join(",");
      }).join("|");
    const sigs = TYPING_FX_STYLES.map(sig);
    expect(new Set(sigs).size).toBe(TYPING_FX_STYLES.length);
  });

  it("reduced motion (motion 0) leaves no scale, tilt, offset or ghost: light and colour only", () => {
    const out = newPose();
    for (const id of TYPING_FX_STYLES) {
      for (let age = 0; age < 400; age += 5) {
        const p = STYLES[id].keyPose(age, 0, out);
        expect(p.scale, id).toBe(1);
        expect(p.rot === 0 && p.dx === 0 && p.dy === 0, id).toBe(true);
        expect(p.aOn || p.bOn).toBe(false);
      }
      expect(keyParticles(id, levelFor("normal", true).particles, true)).toBeLessThanOrEqual(keyParticles(id, 1));
    }
  });

  it("Low halves the motion and spawns nothing; Normal stays within 12 particles a key, Ultra at combo 20 within 24", () => {
    const out = newPose();
    const full = STYLES.flare.keyPose(1, 1, out).scale - 1;
    const half = STYLES.flare.keyPose(1, INTENSITY.low.motion, out).scale - 1;
    expect(half).toBeCloseTo(full / 2, 10);
    for (const id of TYPING_FX_STYLES) {
      expect(keyParticles(id, INTENSITY.low.particles)).toBe(0);
      expect(keyParticles(id, INTENSITY.normal.particles), id).toBeLessThanOrEqual(12);
      expect(keyParticles(id, INTENSITY.ultra.particles * comboParticles(20)), id).toBeLessThanOrEqual(24);
    }
    expect(keyParticles("minimal", 2)).toBe(0);
  });

  it("15 keys a second at Ultra and a full combo stay under Ultra's cap", () => {
    for (const id of TYPING_FX_STYLES) {
      const pool = new ParticlePool(400);
      pool.cap = INTENSITY.ultra.cap;
      const c = ctx(pool, INTENSITY.ultra.particles * comboParticles(20));
      let peak = 0;
      for (let k = 0; k < 150; k += 1) {
        c.now = (k * 1000) / 15;
        c.owner = k;
        pool.expire(c.now);
        STYLES[id].phases.forEach((_, phase) => STYLES[id].spawnKey(phase, c));
        peak = Math.max(peak, pool.count);
      }
      expect(peak, id).toBeLessThanOrEqual(INTENSITY.ultra.cap);
      expect(pool.stolen, id).toBe(0);
    }
  });

  it("a wrong key twitches sideways only, never scales (it must not cover the next letters)", () => {
    const out = newPose();
    let moved = false;
    for (let age = 0; age <= WRONG_MS; age += 4) {
      const p = wrongPose(age, 1, out);
      expect(p.scale).toBe(1);
      expect(Math.abs(p.dx)).toBeLessThanOrEqual(0.12);
      moved ||= p.dx !== 0;
    }
    expect(moved).toBe(true);
    expect(wrongPose(WRONG_MS, 1, out).dx).toBe(0);
    expect(wrongPose(10, 0, out).dx === 0).toBe(true);
    // Each style's wrong burst is small: within 0.7 glyph of the due letter.
    for (const id of TYPING_FX_STYLES) {
      const pool = new ParticlePool(50);
      STYLES[id].spawnWrong(ctx(pool));
      for (let i = 0; i < pool.count; i += 1) expect(Math.max(pool.size[i]!, pool.size2[i]!), id).toBeLessThanOrEqual(0.7 * 52 * 1.4);
    }
  });

  it("the shared wrong beat stays under the row: a kicked bar, and the typed letter only when the game says it", () => {
    const pool = new ParticlePool(50);
    const c = ctx(pool);
    spawnWrongBeat(c);
    expect(pool.count).toBe(1);
    expect(pool.kind[0]).toBe(PK.bar);
    c.key = "x".charCodeAt(0);
    spawnWrongBeat(c);
    expect(pool.count).toBe(3);
    const glyph = [...pool.kind.subarray(0, pool.count)].indexOf(PK.glyph);
    expect(pool.aux[glyph]).toBe(120);
    // Off the row (centre 120, letter 52 px): the bar under the baseline, the bounced letter above the cap line, going left.
    for (let i = 0; i < pool.count; i += 1) expect(Math.abs(pool.y[i]! - 120), String(pool.kind[i])).toBeGreaterThan(0.45 * 52);
    expect(pool.vx[glyph]!).toBeLessThan(0);
    expect(pool.vy[glyph]!).toBeLessThan(0);
    // Stamp's own red blot lies under the line too.
    const stamp = new ParticlePool(50);
    STYLES.stamp.spawnWrong(ctx(stamp));
    for (let i = 0; i < stamp.count; i += 1) expect(stamp.y[i]!).toBeGreaterThan(120 + 0.45 * 52);
  });

  it("each style has its own word release: something at Normal, nothing at Low/Off, bounded at Ultra", () => {
    const sx = new Float32Array([-90, -45, 0, 45, 90]);
    const word = (pool: ParticlePool, mult: number) => ({ pool, owner: 1, prio: 3, gold: false, cx: 400, cy: 120, rowW: 230, h: 52, len: 5, sx, now: 0, mult, still: false, random: () => 0.37 });
    for (const id of TYPING_FX_STYLES) {
      const normal = new ParticlePool(400);
      STYLES[id].spawnRelease(word(normal, 1));
      expect(normal.count, id).toBeGreaterThan(0);
      const off = new ParticlePool(400);
      STYLES[id].spawnRelease(word(off, 0));
      expect(off.count, id).toBe(0);
      const ultra = new ParticlePool(400);
      STYLES[id].spawnRelease(word(ultra, 2.2));
      expect(ultra.count, id).toBeLessThanOrEqual(32);
    }
  });

  it("the word envelopes: rim holds two frames then falls; the squeeze holds then flattens; letters arrive fast", () => {
    expect(popEnvelope(0, 50)).toBe(1);
    expect(popEnvelope(2 * FRAME_MS - 1, 50)).toBe(1);
    expect(popEnvelope(2 * FRAME_MS + 50, 50)).toBeCloseTo(Math.exp(-1), 6);
    expect(squeeze(30)).toBe(1);
    expect(squeeze(110)).toBeCloseTo(0.75, 6);
    expect(squeeze(160)).toBe(0);
    expect(flyEase(0)).toBe(0);
    expect(flyEase(1)).toBe(1);
    expect(flyEase(0.5)).toBeLessThan(0.5 + 0.1);
    let last = 0;
    for (let t = 0.05; t <= 1; t += 0.05) {
      expect(flyEase(t)).toBeGreaterThan(last);
      last = flyEase(t);
    }
  });
});
