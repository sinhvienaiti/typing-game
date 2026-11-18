// Source: new for the kit: each game's profile against its design (dragon-hold 05 §5)
import { describe, expect, it } from "vitest";
import { DRAGON, FEEDBACK_PROFILES, SHIP, TD, feedbackProfile } from "./profiles";
import { TIERS, tier } from "./tiers";

describe("feedback profiles", () => {
  it("ship is Sinh Tồn S0 unchanged", () => {
    expect(SHIP.tiers).toBe(TIERS);
    expect([SHIP.stopGapMs, SHIP.stopScale, SHIP.holdMaxMs]).toEqual([150, 0, 70]);
    expect(SHIP.trauma).toEqual({ maxPx: 14, decay: 1.8, kickRate: 38, kickPx: 6 });
    expect(SHIP.sweep).toEqual({ kills: 30, windowMs: 500, stopMs: 25, cooldownMs: 1500 });
    expect(SHIP.debris.restS).toBe(8);
  });

  it("dragon follows 05 §5: T0–T5 trauma and stops, world at 0.05, ≤ 12 px, blows held ≤ 70 ms, shards 6 s", () => {
    expect(DRAGON.tiers.map((row) => row.trauma)).toEqual([0, 0.03, 0.08, 0.16, 0.3, 0.55]);
    expect(DRAGON.tiers.map((row) => row.stopMs)).toEqual([0, 0, 12, 35, 45, 70]);
    expect(DRAGON.tiers.map((row) => row.number?.life ?? 0)[1]).toBe(0.45);
    expect([DRAGON.stopScale, DRAGON.trauma.maxPx, DRAGON.holdMaxMs, DRAGON.stopGapMs, DRAGON.debris.restS]).toEqual([0.05, 12, 70, 150, 6]);
    expect([DRAGON.numbers.mergeS, DRAGON.numbers.tickMergeS]).toEqual([0.15, 0.3]);
    expect([DRAGON.sweep.kills, DRAGON.sweep.windowMs, DRAGON.sweep.stopMs]).toEqual([30, 500, 25]);
  });

  it("td is calmer; every profile is found by its id", () => {
    expect(TD.tiers.map((row) => row.stopMs)).toEqual([0, 0, 0, 25, 35, 50]);
    expect(TD.trauma.maxPx).toBeLessThan(DRAGON.trauma.maxPx);
    for (const id of ["ship", "dragon", "td"] as const) expect(feedbackProfile(id).id).toBe(id);
    expect(Object.keys(FEEDBACK_PROFILES)).toEqual(["ship", "dragon", "td"]);
  });

  it("tier() clamps to T0–T5 and reads the table it is given", () => {
    expect(tier(-2)).toBe(TIERS[0]);
    expect(tier(9)).toBe(TIERS[5]);
    expect(tier(3, TD.tiers).stopMs).toBe(25);
  });
});
