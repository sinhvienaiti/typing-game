// Source: games/space-typing@survival-s0 tests/feedback-motion.test.ts (kit copy, plus the profiles and the held blows)
import { describe, expect, it } from "vitest";
import { compileTyping, TD_TYPING, typingConfig } from "../typing/config";
import { compileDeck, wordIndex } from "../typing/decks";
import { KEY } from "../typing/router";
import { addWord, createSession, dropWord, typeLetter } from "../typing/session";
import { BlowQueue, HitStop } from "./hitstop";
import { DRAGON, SHIP, TD } from "./profiles";
import { Reactions, squashAt } from "./reaction";
import { STOP_GAP_MS, SWEEP, TIERS } from "./tiers";
import { Trauma } from "./trauma";

/**
 * The shared feedback (docs/survival/BUILD_S0.md §6; dragon-hold 05 §5): the
 * tier table, the shake (trauma², × the player's setting, off at 0 and under
 * reduced motion), hit stops (tiers, 150 ms apart, one per sweep) and a foe's
 * reaction, each read from the game's profile.
 */
const seeded = (seed: number) => () => ((seed = (Math.imul(seed, 48271) + 7) >>> 0) / 4294967296);

describe("tiers", () => {
  it("grow from T0 to T5 and stop the world only from T2", () => {
    expect(TIERS).toHaveLength(6);
    for (let t = 1; t < 6; t += 1) expect(TIERS[t]!.trauma).toBeGreaterThan(TIERS[t - 1]!.trauma);
    expect(TIERS.map((tier) => tier.stopMs)).toEqual([0, 0, 12, 35, 45, 70]);
    expect(TIERS[2]!.bass && !TIERS[1]!.bass).toBe(true);
  });

  it("knock foes back by the S0 review's recoil (T1 0.18, T2 0.30)", () => {
    expect(TIERS.map((tier) => tier.recoil)).toEqual([0, 0.18, 0.3, 0.32, 0.45, 0.6]);
    for (let t = 1; t < 6; t += 1) expect(TIERS[t]!.recoil).toBeGreaterThan(TIERS[t - 1]!.recoil);
  });
});

describe("trauma", () => {
  const peak = (trauma: Trauma, seconds: number): number => {
    let max = 0;
    for (let t = 0; t < seconds * 60; t += 1) {
      trauma.update(1 / 60, 1080);
      // Per axis; the diagonal is checked below (the noise pair stays in the unit circle).
      max = Math.max(max, Math.abs(trauma.offsetX), Math.abs(trauma.offsetY));
    }
    return max;
  };

  it("shakes trauma² (at most 14 px at 1080p) and calms down at 1.8 a second", () => {
    const full = new Trauma(SHIP, seeded(11));
    full.add(1);
    expect(peak(full, 0.1)).toBeLessThanOrEqual(14);
    expect(full.trauma).toBeCloseTo(1 - 1.8 * 0.1, 1);
    const half = new Trauma(SHIP, seeded(12));
    half.add(0.5);
    const a = peak(half, 0.05);
    const strong = new Trauma(SHIP, seeded(12));
    strong.add(1);
    expect(a).toBeLessThan(peak(strong, 0.05));
    peak(full, 1);
    expect(full.trauma).toBe(0);
  });

  it("never passes maxPx at 1080p, even held at full trauma, for any seed (both axes at their peak at once)", () => {
    const held = (trauma: Trauma, height: number): number => {
      let max = 0;
      for (let k = 0; k < 60 * 20; k += 1) {
        trauma.add(1);
        trauma.update(1 / 60, height);
        max = Math.max(max, Math.hypot(trauma.offsetX, trauma.offsetY));
      }
      return max;
    };
    for (let seed = 1; seed <= 40; seed += 1) {
      const max = held(new Trauma(SHIP, seeded(seed)), 1080);
      expect(max, "seed " + seed).toBeLessThanOrEqual(14 + 1e-9);
      // The cap is reached, not just respected.
      expect(max, "seed " + seed).toBeGreaterThan(12);
    }
    // Fixed phases, the default Math.random phases, other heights and profiles.
    for (const phase of [0, 0.123, 0.5, 0.999]) expect(held(new Trauma(SHIP, () => phase), 1080)).toBeLessThanOrEqual(14 + 1e-9);
    for (let k = 0; k < 10; k += 1) expect(held(new Trauma(), 1080)).toBeLessThanOrEqual(14 + 1e-9);
    expect(held(new Trauma(SHIP, seeded(3)), 720)).toBeLessThanOrEqual((14 * 720) / 1080 + 1e-9);
    expect(held(new Trauma(DRAGON, seeded(3)), 1080)).toBeLessThanOrEqual(12 + 1e-9);
    expect(held(new Trauma(TD, seeded(3)), 1080)).toBeLessThanOrEqual(8 + 1e-9);
  });

  it("scales with the player's screen-shake setting: none at 0, none with reduced motion", () => {
    const off = new Trauma();
    off.scale = 0;
    off.add(1);
    off.kick(1, 0, 6);
    expect(peak(off, 0.3)).toBe(0);
    const reduced = new Trauma();
    reduced.reduced = true;
    reduced.add(1);
    reduced.kick(0, 1, 6);
    expect(peak(reduced, 0.3)).toBe(0);
    const halfScale = new Trauma();
    halfScale.scale = 0.5;
    const fullScale = new Trauma();
    for (const t of [halfScale, fullScale]) t.kick(1, 0, 6);
    halfScale.update(0.001, 1080);
    fullScale.update(0.001, 1080);
    expect(halfScale.offsetX).toBeCloseTo(fullScale.offsetX * 0.5, 1);
  });

  it("kicks against the shot by 2–6 px and springs back within ~120 ms", () => {
    const t = new Trauma();
    t.kick(-1, 0, 20);
    t.update(0.001, 1080);
    expect(t.offsetX).toBeLessThanOrEqual(-5.5);
    expect(t.offsetX).toBeGreaterThanOrEqual(-6.01);
    for (let k = 0; k < 8; k += 1) t.update(1 / 60, 1080);
    expect(Math.abs(t.offsetX)).toBeLessThan(0.3);
  });

  it("dragon shakes at most 12 px; a seeded noise shakes the same way twice", () => {
    const a = new Trauma(DRAGON, seeded(5));
    const b = new Trauma(DRAGON, seeded(5));
    a.add(1);
    b.add(1);
    const ship = new Trauma(SHIP, seeded(5));
    ship.add(1);
    let max = 0;
    for (let k = 0; k < 30; k += 1) {
      a.update(1 / 60, 1080);
      b.update(1 / 60, 1080);
      ship.update(1 / 60, 1080);
      expect(a.offsetX).toBe(b.offsetX);
      expect(Math.abs(a.offsetX)).toBeCloseTo((Math.abs(ship.offsetX) * 12) / 14, 6);
      max = Math.max(max, Math.hypot(a.offsetX, a.offsetY));
    }
    expect(max).toBeLessThanOrEqual(12 + 1e-9);
  });
});

describe("hit stop", () => {
  it("grants a tier's stop, 150 ms apart and a tier's own spacing", () => {
    const stop = new HitStop();
    expect(stop.request(1, 0)).toBe(0);
    expect(stop.request(3, 1000)).toBe(35);
    expect(stop.request(4, 1000 + STOP_GAP_MS - 1)).toBe(0);
    expect(stop.request(4, 1000 + STOP_GAP_MS)).toBe(45);
    // T3 again only after its own 400 ms.
    expect(stop.request(3, 1000 + 300)).toBe(0);
    expect(stop.request(3, 1000 + 400)).toBe(35);
    expect(stop.request(2, 2000)).toBe(12);
  });

  it("gives one 25 ms stop for 30 kills inside 0.5 s, then rests", () => {
    const stop = new HitStop();
    expect(stop.kill(20, 0)).toBe(0);
    expect(stop.kill(9, 200)).toBe(0);
    expect(stop.kill(1, 400)).toBe(SWEEP.stopMs);
    expect(stop.kill(40, 700)).toBe(0);
    expect(stop.kill(40, 400 + SWEEP.cooldownMs)).toBe(SWEEP.stopMs);
    // Slow kills never make a sweep.
    const slow = new HitStop();
    for (let k = 0; k < 100; k += 1) expect(slow.kill(1, k * 40)).toBe(0);
  });

  it("dragon slows the world to 0.05 during a stop (ship holds it); outside a stop it runs at 1", () => {
    const dragon = new HitStop(DRAGON);
    expect(dragon.request(5, 1000)).toBe(70);
    expect(dragon.scale(999)).toBe(1);
    expect(dragon.scale(1000)).toBe(0.05);
    expect(dragon.scale(1069)).toBe(0.05);
    expect(dragon.scale(1070)).toBe(1);
    // A 1/60 s frame wholly inside the stop: 5 % of it; one that straddles its end: the rest at full speed.
    expect(dragon.worldDt(1 / 60, 1050)).toBeCloseTo((1 / 60) * 0.05, 9);
    expect(dragon.worldDt(0.02, 1080)).toBeCloseTo(0.01 * 0.05 + 0.01, 9);
    expect(dragon.worldDt(0.02, 2000)).toBeCloseTo(0.02, 9);
    const ship = new HitStop(SHIP);
    ship.request(3, 0);
    expect(ship.worldDt(0.01, 10)).toBe(0);
    ship.clear();
    expect(ship.scale(10)).toBe(1);
  });

  it("td stops only from T3, shorter", () => {
    const td = new HitStop(TD);
    expect(td.request(2, 0)).toBe(0);
    expect(td.request(3, 1000)).toBe(25);
    expect(td.request(5, 2000)).toBe(50);
  });
});

describe("hit stop never swallows keys (dragon-hold 05 §5)", () => {
  it("every key typed during a stop reaches the typing core at once; only the word's blow waits, at most 70 ms", () => {
    const deck = compileDeck(["fire", "gold", "moss"].map((text, index) => ({ id: "w" + index, text, level: 1 })));
    const t = createSession(compileTyping(typingConfig(TD_TYPING, { router: { protectS: 1.2 } })), deck);
    const fire = addWord(t, wordIndex(deck, "fire"), 0, 1, 0);
    const gold = addWord(t, wordIndex(deck, "gold"), 0, 1, 0);
    const stop = new HitStop(DRAGON);
    const blows = new BlowQueue<number>(DRAGON.holdMaxMs);
    const fired: { slot: number; at: number }[] = [];
    // A T5 blow at 1000 ms stops the world for 70 ms; the player keeps typing, a key every 8 ms.
    expect(stop.request(5, 1000)).toBe(70);
    let now = 1000;
    let tick = 60;
    const results: number[] = [];
    for (const ch of "firegold") {
      now += 8;
      // The world crawls: a sim tick only every so often, but the key goes in now, on the tick there is.
      tick += stop.scale(now) === 1 ? 1 : 0;
      const { result, slot } = typeLetter(t, ch.charCodeAt(0) - 97, tick);
      results.push(result);
      if (result === KEY.done) {
        dropWord(t, slot, tick);
        blows.push(slot, now);
      }
      for (const blow of blows.take(now, stop.stopped(now))) fired.push({ slot: blow, at: now });
    }
    expect(fired).toEqual([]);
    for (let frame = 0; frame < 4; frame += 1) {
      now += 8;
      for (const blow of blows.take(now, stop.stopped(now))) fired.push({ slot: blow, at: now });
    }
    expect(results).toEqual([KEY.lock, KEY.advance, KEY.advance, KEY.done, KEY.lock, KEY.advance, KEY.advance, KEY.done]);
    expect(t.stats.keys).toBe(8);
    expect([t.stats.strays, t.stats.errors, t.stats.done]).toEqual([0, 0, 2]);
    // "fire" was done at 1032 (in the stop): its blow fired when the world ran again (1072), 40 ms later.
    // "gold" was done at 1064 (in the stop): it fired at 1072 too, with the first.
    expect(fired.map((f) => f.slot)).toEqual([fire, gold]);
    for (const f of fired) expect(f.at).toBe(1072);
    expect(blows.size).toBe(0);
  });

  it("a blow held while the world stays stopped fires after holdMaxMs; outside a stop at once", () => {
    const blows = new BlowQueue<string>(70);
    blows.push("a", 0);
    expect(blows.take(10, false)).toEqual(["a"]);
    blows.push("b", 100);
    blows.push("c", 150);
    expect(blows.take(169, true)).toEqual([]);
    expect(blows.take(170, true)).toEqual(["b"]);
    expect(blows.take(219, true)).toEqual([]);
    expect(blows.take(220, true)).toEqual(["c"]);
    blows.push("d", 300);
    blows.clear();
    expect(blows.take(400, false)).toEqual([]);
  });
});

describe("reaction", () => {
  it("flashes white for the tier's frames, knocks back along the blow and returns, squashes 0.91 / 1.07 in 120 ms", () => {
    const r = new Reactions(8);
    const out = new Float32Array(5);
    r.hit(2, 77, 3, 0, 1, 10);
    expect(r.sample(2, 77, 10, out)[0]).toBe(1);
    expect(r.sample(2, 77, 10 + 3 / 60, out)[0]).toBe(1);
    expect(r.sample(2, 77, 10 + 0.12, out)[0]).toBe(0);
    const push = r.sample(2, 77, 10.03, out)[2]!;
    expect(push).toBeGreaterThan(0.25);
    expect(r.sample(2, 77, 10.2, out)[2]!).toBeLessThan(push * 0.15);
    expect(squashAt(0)).toBeCloseTo(0.91);
    expect(squashAt(0.04)).toBeCloseTo(1.07);
    expect(squashAt(0.12)).toBe(1);
    // A reused slot (a new owner) starts clean.
    expect(r.sample(2, 78, 10, out)[0]).toBe(0);
  });

  it("reads its tier table from the profile", () => {
    const flat = { ...SHIP, tiers: TIERS.map((row) => ({ ...row, recoil: 0 })) };
    const r = new Reactions(2, flat);
    const out = new Float32Array(5);
    r.hit(0, 1, 4, 1, 0, 0);
    expect(r.sample(0, 1, 0.03, out)[1]).toBe(0);
    expect(r.sample(0, 1, 0.03, out)[3]).toBeGreaterThan(1);
  });
});
