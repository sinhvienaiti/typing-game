// Source: games/space-typing/tests/audio-mix.test.ts (plus the per-game bus table)
import { describe, expect, it } from "vitest";
import { AUDIO_GROUP_GAIN, BusMix, DEFAULT_BUSES, PRONUNCIATION_DUCK, mixedSfxGain, setPronunciationBoost } from "./index";

describe("audio mix", () => {
  it("keeps warnings above normal combat in the base hierarchy", () => {
    expect(AUDIO_GROUP_GAIN.warnings).toBeGreaterThan(AUDIO_GROUP_GAIN.combat);
    expect(AUDIO_GROUP_GAIN.typing).toBeGreaterThan(AUDIO_GROUP_GAIN.combat);
  });

  it("ducks SFX while pronunciation is active without muting warnings", () => {
    const normal = mixedSfxGain(1, "combat", 1, false);
    const ducked = mixedSfxGain(1, "combat", 1, true);
    const warning = mixedSfxGain(1, "warnings", 1, true);
    expect(ducked).toBeLessThan(normal);
    expect(warning).toBeGreaterThan(ducked);
    expect(warning).toBeGreaterThan(0);
  });

  it("keeps Credit pickups audible while a word is spoken, still under warnings", () => {
    const combat = mixedSfxGain(1, "combat", 1, true);
    const rewards = mixedSfxGain(1, "rewards", 1, true);
    const warning = mixedSfxGain(1, "warnings", 1, true);
    expect(rewards).toBeGreaterThan(combat);
    expect(rewards).toBeLessThan(warning);
  });

  it("clamps master and event gains", () => {
    expect(mixedSfxGain(5, "typing", 5)).toBe(AUDIO_GROUP_GAIN.typing);
    expect(mixedSfxGain(-1, "typing", 1)).toBe(0);
  });

  it("Voice boost ducks effects deeper while a word is spoken, never when silent", () => {
    try {
      setPronunciationBoost(1);
      expect(mixedSfxGain(1, "warnings", 1, true)).toBeCloseTo(AUDIO_GROUP_GAIN.warnings * PRONUNCIATION_DUCK.warnings);
      setPronunciationBoost(3);
      expect(mixedSfxGain(1, "warnings", 1, true)).toBeCloseTo(AUDIO_GROUP_GAIN.warnings / 3);
      expect(mixedSfxGain(1, "combat", 1, false)).toBeCloseTo(AUDIO_GROUP_GAIN.combat);
      setPronunciationBoost(9);
      expect(mixedSfxGain(1, "warnings", 1, true)).toBeCloseTo(AUDIO_GROUP_GAIN.warnings / 3);
    } finally {
      setPronunciationBoost(1);
    }
  });

  it("takes a game's own bus table", () => {
    const mix = new BusMix({ fire: { gain: 0.9, duck: 0.5 }, horde: { gain: 0.6, duck: 0.3 }, alarm: { gain: 1, duck: 0.8 } });
    expect(mix.busNames).toEqual(["fire", "horde", "alarm"]);
    expect(mix.mixedGain(1, "fire", 1)).toBeCloseTo(0.9);
    expect(mix.mixedGain(1, "horde", 1, true)).toBeCloseTo(0.18);
    mix.setPronunciationBoost(2);
    expect(mix.busGain("alarm", true)).toBeCloseTo(0.5);
    expect(Object.keys(DEFAULT_BUSES)).toEqual(["typing", "combat", "warnings", "ui", "rewards"]);
  });
});
