// Source: new for the kit: before-stage levers against docs/games/BALANCE.md §4.1
import { describe, expect, it } from "vitest";
import { DRAGON_C_REF, capacity, effectiveE, familiarityMix, newWordShare, paceK, peakLanes, scaleTicks, skillAdvice, suggestDifficulty, telegraphScale, telegraphTicks } from "./pace";
import { blendSkill, newSkillProfile, skillDefaults } from "./profile";

const dragon = (len: number) => ({ len, d: 0.86, ref: DRAGON_C_REF });

describe("effective speed and pace k", () => {
  it("E_eff = E × (0.6 + 0.4a²) × (1 − 0.5CV), held in [0.7E, E]", () => {
    expect(effectiveE({ e: 35, a: 0.95, cv: 0.25 })).toBeCloseTo(29.430625, 10);
    expect(effectiveE({ e: 25, a: 0.95, cv: 0.25 })).toBeCloseTo(21.021875, 10);
    expect(effectiveE({ e: 60, a: 0.95, cv: 0.25 })).toBeCloseTo(50.4525, 10);
    expect(effectiveE({ e: 40, a: 1, cv: 0 })).toBe(40);
    expect(effectiveE({ e: 40, a: 0.5, cv: 0.8 })).toBeCloseTo(28, 10);
    expect(effectiveE({ e: 0, a: 1, cv: 0 })).toBe(0);
    // Fatigue lowers E itself, at most 15 %.
    expect(effectiveE({ e: 40, a: 1, cv: 0, fatigue: 0.1 })).toBeCloseTo(36, 10);
    expect(effectiveE({ e: 40, a: 1, cv: 0, fatigue: 0.4 })).toBeCloseTo(34, 10);
    // Straight from a profile: an unmeasured adult on Balanced is the standard bot.
    expect(effectiveE(blendSkill(newSkillProfile()))).toBeCloseTo(29.430625, 10);
    expect(effectiveE(blendSkill(newSkillProfile("child", "relax")))).toBeCloseTo(15 * (0.6 + 0.4 * 0.88 ** 2) * 0.8, 10);
  });

  it("C(E) gives Dragonhold's reference 22.7 words a minute at 35 WPM", () => {
    expect(DRAGON_C_REF).toBeCloseTo(22.7, 1);
    expect(capacity(25, 4.5, 0.86)).toBeCloseTo(17.0, 1);
    expect(capacity(60, 5.5, 0.86)).toBeCloseTo(30.6, 1);
    expect(capacity(0, 4.5, 0.86)).toBe(0);
    expect(familiarityMix({ known: 0.6, learning: 0.2, new: 0.2 })).toBeCloseTo(0.91, 10);
    expect(familiarityMix({})).toBe(1);
  });

  it("k goes both ways: 25 / 35 / 60 WPM at 95 % and CV 0.25", () => {
    expect(paceK(effectiveE({ e: 25, a: 0.95, cv: 0.25 }), dragon(4.5))).toBe(0.75);
    expect(paceK(effectiveE({ e: 35, a: 0.95, cv: 0.25 }), dragon(4.5))).toBe(0.864);
    expect(paceK(effectiveE({ e: 50, a: 0.95, cv: 0.25 }), dragon(5.5))).toBe(1.014);
    expect(paceK(effectiveE({ e: 60, a: 0.95, cv: 0.25 }), dragon(5.5))).toBe(1.176);
    expect(paceK(effectiveE({ e: 100, a: 0.95, cv: 0.25 }), dragon(6))).toBe(1.3);
    expect(paceK(35, dragon(4.5))).toBe(1);
    expect(paceK(35, { len: 4.5, d: 0.86, ref: 0 })).toBe(1);
    // Spawn gaps × 1/k.
    expect(scaleTicks(600, 0.75)).toBe(800);
    expect(scaleTicks(600, 1.176)).toBe(510);
    expect(scaleTicks(1, 1.3)).toBe(1);
  });
});

describe("other before-stage levers", () => {
  it("new-word share drops for a < 90 % or slow new-word recognition, never below the floor", () => {
    const view = blendSkill(newSkillProfile());
    expect(newWordShare(view, 0.3)).toBe(0.3);
    expect(newWordShare({ a: 0.88, recognize: view.recognize }, 0.3)).toBe(0.18);
    expect(newWordShare({ a: 0.88, recognize: { ...view.recognize, new: 1.8 } }, 0.3)).toBe(0.126);
    expect(newWordShare({ a: 0.88, recognize: { ...view.recognize, new: 1.8 } }, 0.3, 0.15)).toBe(0.15);
  });

  it("telegraph time × 0.85–1.5 by reflex, never under the game's minimum", () => {
    expect([0.2, 0.35, 0.55, 0.75, 0.85, 0.95, 1].map(telegraphScale)).toEqual([1.5, 1.5, 1.25, 1, 0.925, 0.85, 0.85]);
    expect(telegraphScale(skillDefaults("adult", "balanced").telegraph)).toBe(1);
    expect(telegraphTicks(120, 0.85, 90)).toBe(102);
    expect(telegraphTicks(100, 0.85, 90)).toBe(90);
  });

  it("one lane fewer at the peak when the crowd drop passes 35 %", () => {
    expect(peakLanes(3, 0.2)).toBe(3);
    expect(peakLanes(3, 0.4)).toBe(2);
    expect(peakLanes(1, 0.5)).toBe(1);
  });

  it("suggests up after two easy wins, down after two losses", () => {
    expect(suggestDifficulty({ easyWins: 2, streak: 2 })).toBe("up");
    expect(suggestDifficulty({ easyWins: 1, streak: 5 })).toBe("stay");
    expect(suggestDifficulty({ easyWins: 0, streak: -2 })).toBe("down");
    expect(suggestDifficulty({ easyWins: 0, streak: -1 })).toBe("stay");
  });

  it("picks one piece of advice", () => {
    const base = skillDefaults("adult", "balanced");
    expect(skillAdvice(base)).toBe("keep-going");
    expect(skillAdvice({ ...base, fatigue: 0.12 })).toBe("rest");
    expect(skillAdvice({ ...base, e: 55, a: 0.9 })).toBe("slow-down");
    expect(skillAdvice({ ...base, a: 0.85 })).toBe("accuracy");
    expect(skillAdvice({ ...base, cv: 0.4 })).toBe("steady");
    expect(skillAdvice({ ...base, recognize: { ...base.recognize, new: 1.7 } })).toBe("new-words");
    expect(skillAdvice({ ...base, crowdDrop: 0.4 })).toBe("crowd");
  });
});
