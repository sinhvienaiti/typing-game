// Source: games/space-typing@feat/td-1a6 tests/td-scorer.test.ts (kit copy; the mode and E-floor parts that need TD's world stay in TD)
import { describe, expect, it } from "vitest";
import { compileTyping, TD_TYPING, typingConfig } from "./config";
import { compileDeck } from "./decks";
import { KEY } from "./router";
import { allowedErrors, expectedTicks, gradeWord, lifeSeconds, lifeTicks, rawWpm, scoreWord, typeSeconds } from "./scorer";
import { addWord, createSession, typeLetter, wordTiming } from "./session";
import { lengthBand, type SpeedBand } from "./tempo";

/** Scoring a word (docs/td/TYPING_DEFENSE_DESIGN.md 6.4, 6.6; dragon-hold 01 §3.7). */
const rules = compileTyping(TD_TYPING);
const E = 35;
/** TD 1A.6's modes: k_L of the life, and challenge's floor. */
const K = { relax: 1.25, balanced: 1, challenge: 0.9, learn: 1.25 } as const;
const HARD_MIN = 2.7;

describe("word life, the clock a word is scored against", () => {
  it("L_w = clamp(1.2 + 12·(len + 1)/(E·d); 3; 6) × k_L: TK 6.4's examples", () => {
    expect(lifeSeconds(rules, 5, 20, 1, K.balanced)).toBeCloseTo(4.8, 10);
    expect(lifeSeconds(rules, 5, 35, 1, K.balanced)).toBeCloseTo(3.257, 3);
    expect(lifeSeconds(rules, 5, 60, 1, K.balanced)).toBe(3);
    expect(lifeSeconds(rules, 8, 12, 1, K.relax)).toBe(7.5);
    expect(lifeSeconds(rules, 8, 12, 1, K.learn)).toBe(7.5);
    expect(lifeSeconds(rules, 3, 140, 1, K.challenge, HARD_MIN)).toBeCloseTo(2.7, 10);
    expect(lifeTicks(rules, 5, 35, 1, K.balanced)).toBe(195);
  });
});

describe("word length follows E (TK 6.3)", () => {
  const LENGTH_BY_E: readonly SpeedBand[] = [
    { minE: 0, len: [3, 5] },
    { minE: 25, len: [3, 6] },
    { minE: 45, len: [4, 7] },
    { minE: 65, len: [4, 8] },
  ];
  it("takes the last band whose minE ≤ E", () => {
    expect(lengthBand(LENGTH_BY_E, 20)).toEqual([3, 5]);
    expect(lengthBand(LENGTH_BY_E, 35)).toEqual([3, 6]);
    expect(lengthBand(LENGTH_BY_E, 70)).toEqual([4, 8]);
    expect(lengthBand(LENGTH_BY_E, 12)).toEqual([3, 5]);
  });
});

describe("scoring by errors, with slack for long words (TK 6.6)", () => {
  const A = (len: number, errors: number) => scoreWord(rules, len, errors, lifeTicks(rules, len, E, 1), 60, E, 1);
  it("matches TK 6.6's table of A_w and grade for lengths 3, 5, 8, 12", () => {
    const table: [number, number, number, string][] = [
      [3, 0, 1, "clean"], [3, 1, 0.6, "ok"], [3, 2, 0.2, "sloppy"], [3, 3, 0, "sloppy"],
      [5, 0, 1, "clean"], [5, 1, 0.7, "ok"], [5, 2, 0.4, "sloppy"], [5, 3, 0.1, "sloppy"],
      [8, 0, 1, "clean"], [8, 1, 0.8125, "good"], [8, 2, 0.625, "sloppy"], [8, 3, 0.4375, "sloppy"],
      [12, 0, 1, "clean"], [12, 1, 0.85, "good"], [12, 2, 0.7, "good"], [12, 3, 0.55, "sloppy"],
    ];
    for (const [len, errors, accuracy, grade] of table) {
      const score = A(len, errors);
      expect(score.accuracy, len + "/" + errors).toBeCloseTo(accuracy, 10);
      // No error: Flash or Perfect by speed (the next test); otherwise the table's grade.
      if (grade === "clean") expect(["flash", "perfect"]).toContain(score.grade);
      else expect(score.grade, len + "/" + errors).toBe(grade);
    }
  });

  it("measures speed from the moment the word appeared: Flash at S_w ≥ 0.7, Perfect slower, 0 at the end of life", () => {
    const life = lifeTicks(rules, 5, E, 1);
    const fast = Math.floor((0.35 + 0.8 * typeSeconds(rules, 5, E, 1)) * 60);
    expect(scoreWord(rules, 5, 0, life, fast, E, 1).speed).toBe(1);
    expect(scoreWord(rules, 5, 0, life, fast, E, 1).grade).toBe("flash");
    const at = (speed: number) => Math.round(life - speed * (life - fast));
    expect(scoreWord(rules, 5, 0, life, at(0.75), E, 1).grade).toBe("flash");
    expect(scoreWord(rules, 5, 0, life, at(0.6), E, 1).grade).toBe("perfect");
    expect(scoreWord(rules, 5, 0, life, life, E, 1).speed).toBe(0);
    const score = scoreWord(rules, 5, 1, life, at(0.5), E, 1);
    expect(score.speedEff).toBeCloseTo(score.speed * (0.4 + 0.6 * 0.7), 10);
    expect(score.quality).toBeCloseTo(0.6 * 0.7 + 0.4 * score.speedEff, 10);
  });

  it("keeps the raw typing speed (first key to last) apart from scoring", () => {
    expect(rawWpm(6, 1000, 2000)).toBeCloseTo(60, 10);
    expect(rawWpm(6, 1000, 1000)).toBe(0);
  });

  it("scores keys sent in one tick like keys a tick apart (only the tick of the last counts)", () => {
    const deck = compileDeck([{ id: "w0", text: "apple", level: 1 }]);
    const scores = [true, false].map((sameTick) => {
      const t = createSession(rules, deck);
      const s = addWord(t, 0, rules.kind.call!, 1, 0);
      let last = -1;
      [..."apple"].forEach((ch, k) => {
        last = sameTick ? 64 : 60 + k;
        typeLetter(t, ch.charCodeAt(0) - 97, last);
      });
      expect(t.stats.done).toBe(1);
      const timing = wordTiming(t, s, last);
      return scoreWord(rules, timing.len, timing.errors, lifeTicks(rules, 5, E, 1), timing.total, E, 1);
    });
    expect(scores[0]).toEqual(scores[1]);
  });
});

describe("grading from the keys alone (dragon-hold 01 §3.7, 00 §4.2)", () => {
  const dragon = compileTyping(typingConfig(TD_TYPING, { grade: { longLen: 0 } }));
  const grade = (len: number, errors: number, typing: number, d = 1000, allowed?: number) => gradeWord(dragon, { len, errors, typing }, E, d, allowed);

  it("Flash: no error and t_k ≤ 0.85 × t_exp, t_exp = 12·(len − 1)/(E·d); exact at the edge, in integers", () => {
    expect(expectedTicks(dragon, 5, E, 1000)).toBeCloseTo((12 * 4 * 60) / 35, 10);
    expect(grade(5, 0, 69)).toBe("flash");
    expect(grade(5, 0, 70)).toBe("perfect");
    // A new word (d 0.70) gives more time.
    expect(grade(5, 0, 99, 700)).toBe("flash");
    expect(grade(5, 0, 100, 700)).toBe("perfect");
    // One key: only an instant word is a Flash.
    expect(grade(1, 0, 0)).toBe("flash");
  });

  it("one error: Good from 6 letters, OK under; two: Sloppy (a boss chain allows 2)", () => {
    expect(grade(6, 1, 10)).toBe("good");
    expect(grade(5, 1, 10)).toBe("ok");
    expect(grade(5, 2, 10)).toBe("sloppy");
    expect(grade(12, 2, 10)).toBe("sloppy");
    expect(grade(5, 2, 10, 1000, 2)).toBe("ok");
    expect(grade(7, 2, 10, 1000, 2)).toBe("good");
    expect(grade(7, 3, 10, 1000, 2)).toBe("sloppy");
  });

  it("TD's slack for long words is a rule: 2 errors allowed from 12 letters", () => {
    expect(allowedErrors(rules.grade, 12)).toBe(2);
    expect(allowedErrors(rules.grade, 11)).toBe(1);
    expect(allowedErrors(dragon.grade, 12)).toBe(1);
    expect(gradeWord(rules, { len: 12, errors: 2, typing: 10 }, E, 1000)).toBe("good");
  });

  it("grades a session's word by its own keys, whatever came before the first key", () => {
    const deck = compileDeck([{ id: "w0", text: "apple", level: 1 }]);
    const t = createSession(dragon, deck);
    const s = addWord(t, 0, 0, 1, 0);
    // Read for 5 s, then typed in 0.9 s: still a Flash (reading time is not typing time).
    [..."apple"].forEach((ch, k) => typeLetter(t, ch.charCodeAt(0) - 97, 300 + k * 13));
    const timing = wordTiming(t, s, 352);
    expect(timing).toMatchObject({ toFirstKey: 300, typing: 52, total: 352 });
    expect(gradeWord(dragon, timing, E, 1000)).toBe("flash");
    expect(KEY.done).toBe(3);
  });
});
