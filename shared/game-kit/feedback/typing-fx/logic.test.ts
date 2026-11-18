// Source: new for the kit: settings, intensity curves, effect priority and the particle pool of typing-fx
import { describe, expect, it } from "vitest";
import { comboFactor, comboParticles, comboSize, INTENSITY, isMilestone, levelFor, PRIORITY, wordPriority } from "./intensity";
import { ParticlePool, PK } from "./pool";
import { DEFAULT_TYPING_FX, sanitizeTypingFx, stripCapPx, TYPING_FX_INTENSITIES, TYPING_FX_SIZES, TYPING_FX_STYLES } from "./settings";

describe("typing-fx settings", () => {
  it("keeps good values and drops each bad field to its default on its own", () => {
    expect(sanitizeTypingFx({ style: "rune", intensity: "ultra", size: "huge", soundProfile: "thock", volume: 0.25 })).toEqual({ style: "rune", intensity: "ultra", size: "huge", soundProfile: "thock", volume: 0.25 });
    expect(sanitizeTypingFx({ size: "giant" }).size).toBe("large");
    // An old save without the size field gets the default.
    expect(sanitizeTypingFx({ style: "smash", intensity: "low", soundProfile: "off", volume: 0.5 }).size).toBe("large");
    expect(sanitizeTypingFx({ style: "laser", intensity: "max", soundProfile: "../x", volume: 7 })).toEqual({ ...DEFAULT_TYPING_FX, volume: 1 });
    expect(sanitizeTypingFx(null)).toEqual(DEFAULT_TYPING_FX);
    expect(sanitizeTypingFx("stamp")).toEqual(DEFAULT_TYPING_FX);
    expect(sanitizeTypingFx({ volume: Number.NaN }).volume).toBe(DEFAULT_TYPING_FX.volume);
    expect(sanitizeTypingFx({ volume: -1 }).volume).toBe(0);
  });

  it("Stamp, Normal and Large by default (owner 29/10)", () => {
    expect(DEFAULT_TYPING_FX.style).toBe("stamp");
    expect(DEFAULT_TYPING_FX.size).toBe("large");
    expect(TYPING_FX_SIZES).toEqual(["medium", "large", "huge"]);
  });

  it("the word's cap height: Large about 40 / 56 px, Huge about 52 / 72 px at 720 / 1080, growing with the view", () => {
    expect(stripCapPx("large", 720)).toBe(40);
    expect(stripCapPx("large", 1080)).toBe(56);
    expect(stripCapPx("huge", 720)).toBe(52);
    expect(stripCapPx("huge", 1080)).toBe(72);
    expect(stripCapPx("large", 900)).toBe(48);
    expect(stripCapPx("large", 1440)).toBeCloseTo(74.67, 2);
    expect(stripCapPx("large", 540)).toBe(30);
    expect(stripCapPx("medium", 1080)).toBeLessThan(stripCapPx("large", 1080));
    for (const h of [480, 720, 900, 1080, 1440, 2160]) {
      expect(stripCapPx("medium", h)).toBeLessThan(stripCapPx("large", h));
      expect(stripCapPx("large", h)).toBeLessThan(stripCapPx("huge", h));
    }
  });

  it("offers six styles and the five intensities, Normal by default", () => {
    expect(TYPING_FX_STYLES.length).toBeGreaterThanOrEqual(6);
    expect(TYPING_FX_INTENSITIES).toEqual(["off", "low", "normal", "high", "ultra"]);
    expect(DEFAULT_TYPING_FX.intensity).toBe("normal");
  });
});

describe("typing-fx intensity", () => {
  it("grows from Off to Ultra and never spawns a particle below Normal", () => {
    expect(INTENSITY.off.fx).toBe(false);
    expect(INTENSITY.low.particles).toBe(0);
    expect(INTENSITY.low.cap).toBe(0);
    expect(INTENSITY.low.fly).toBe(false);
    const order = TYPING_FX_INTENSITIES.map((id) => INTENSITY[id]);
    for (let i = 1; i < order.length; i += 1) {
      expect(order[i]!.particles).toBeGreaterThanOrEqual(order[i - 1]!.particles);
      expect(order[i]!.cap).toBeGreaterThanOrEqual(order[i - 1]!.cap);
      expect(order[i]!.motion).toBeGreaterThanOrEqual(order[i - 1]!.motion);
    }
  });

  it("reduced motion keeps the cues but stops everything that moves", () => {
    for (const id of TYPING_FX_INTENSITIES) {
      const level = levelFor(id, true);
      expect(level.motion).toBe(0);
      expect(level.fly).toBe(false);
      expect(level.shock).toBe(false);
      expect(level.fx).toBe(INTENSITY[id].fx);
      expect(level.cap).toBeLessThanOrEqual(80);
    }
    expect(levelFor("normal", false)).toBe(INTENSITY.normal);
  });

  it("escalates combos on a capped, monotone curve", () => {
    expect(comboFactor(0)).toBe(0);
    expect(comboFactor(20)).toBe(1);
    expect(comboFactor(500)).toBe(1);
    expect(comboFactor(-4)).toBe(0);
    expect(comboFactor(Number.NaN)).toBe(0);
    let last = -1;
    for (let c = 0; c <= 40; c += 1) {
      const f = comboFactor(c);
      expect(f).toBeGreaterThanOrEqual(last);
      last = f;
    }
    expect(comboParticles(1000)).toBeCloseTo(1.6, 10);
    expect(comboSize(1000)).toBeCloseTo(1.2, 10);
  });

  it("a milestone upgrades the word effect instead of stacking a second one", () => {
    expect([1, 9, 10, 11, 25, 49, 50, 100, 150].map(isMilestone)).toEqual([false, false, true, false, true, false, true, true, true]);
    expect(wordPriority(false, 3)).toBe(PRIORITY.word);
    expect(wordPriority(true, 3)).toBe(PRIORITY.perfect);
    expect(wordPriority(false, 25)).toBe(PRIORITY.milestone);
    expect(wordPriority(true, 50)).toBe(PRIORITY.milestone);
    expect(PRIORITY.key).toBeLessThan(PRIORITY.word);
  });
});

describe("typing-fx particle pool", () => {
  it("spawns, expires and keeps the live range dense", () => {
    const pool = new ParticlePool(8);
    for (let i = 0; i < 5; i += 1) expect(pool.spawn(PK.spark, 1, 1, i, 0, 0, 100 + i * 100)).toBe(i);
    expect(pool.count).toBe(5);
    expect(pool.expire(250)).toBe(3);
    // The survivors are the long-lived ones, packed at the front.
    const lives = Array.from(pool.life.subarray(0, pool.count)).sort((a, b) => a - b);
    expect(lives).toEqual([300, 400, 500]);
    pool.clear();
    expect(pool.count).toBe(0);
  });

  it("past the cap takes the lowest priority first, then the oldest, and refuses a weaker spawn", () => {
    const pool = new ParticlePool(4);
    pool.spawn(PK.spark, 1, 2, 0, 0, 0, 1000);
    pool.spawn(PK.spark, 2, 1, 0, 0, 10, 1000);
    pool.spawn(PK.spark, 3, 1, 0, 0, 5, 1000);
    pool.spawn(PK.spark, 4, 2, 0, 0, 1, 1000);
    const slot = pool.spawn(PK.ring, 9, 2, 0, 0, 20, 1000);
    expect(slot).toBeGreaterThanOrEqual(0);
    expect(pool.owner[slot]).toBe(9);
    // Owner 3 (priority 1, born 5) went: the oldest of the lowest priority.
    expect(Array.from(pool.owner.subarray(0, pool.count)).sort()).toEqual([1, 2, 4, 9]);
    expect(pool.stolen).toBe(1);
    pool.spawn(PK.ring, 10, 2, 0, 0, 30, 1000); // takes owner 2 (priority 1)
    expect(pool.spawn(PK.spark, 11, 1, 0, 0, 40, 1000)).toBe(-1);
    expect(pool.refused).toBe(1);
  });

  it("a word effect removes its last letter's particles by owner", () => {
    const pool = new ParticlePool(16);
    for (let i = 0; i < 4; i += 1) pool.spawn(PK.spark, 7, 1, 0, 0, 0, 500);
    for (let i = 0; i < 3; i += 1) pool.spawn(PK.spark, 8, 1, 0, 0, 0, 500);
    expect(pool.killOwner(8)).toBe(3);
    expect(pool.count).toBe(4);
    expect(Array.from(pool.owner.subarray(0, pool.count))).toEqual([7, 7, 7, 7]);
  });

  it("a cap of 0 refuses every spawn; lowering the cap trims at once", () => {
    const pool = new ParticlePool(10);
    for (let i = 0; i < 10; i += 1) pool.spawn(PK.spark, i, 1, 0, 0, 0, 500);
    pool.cap = 4;
    expect(pool.count).toBe(4);
    pool.cap = 0;
    expect(pool.count).toBe(0);
    expect(pool.spawn(PK.spark, 1, 4, 0, 0, 0, 100)).toBe(-1);
    pool.cap = 99;
    expect(pool.cap).toBe(10);
  });

  it("positions are closed-form: drag slows a particle to a stop, gravity pulls it down", () => {
    const pool = new ParticlePool(2);
    const i = pool.spawn(PK.ink, 1, 1, 10, 20, 1000, 1000);
    pool.vx[i] = 100;
    pool.drag[i] = 10;
    pool.grav[i] = 200;
    const out = new Float32Array(2);
    pool.position(i, 1000, out);
    expect([out[0], out[1]]).toEqual([10, 20]);
    pool.position(i, 2000, out);
    expect(out[0]!).toBeCloseTo(10 + (100 * (1 - Math.exp(-10))) / 10, 3);
    expect(out[1]!).toBeCloseTo(20 + 100, 3);
    expect(pool.age(i, 1500)).toBeCloseTo(0.5, 6);
  });

  it("15 keys a second for 60 s never grows the pool or loses the dense range", () => {
    const pool = new ParticlePool(160);
    let maxCount = 0;
    for (let k = 0; k < 15 * 60; k += 1) {
      const now = (k * 1000) / 15;
      pool.expire(now);
      for (let p = 0; p < 12; p += 1) pool.spawn(PK.spark, k, 1, 0, 0, now, 200 + p * 20);
      maxCount = Math.max(maxCount, pool.count);
    }
    expect(maxCount).toBeLessThanOrEqual(160);
    expect(pool.capacity).toBe(160);
  });
});
