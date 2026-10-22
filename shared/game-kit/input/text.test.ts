// Source: games/space-typing/tests/logic.test.ts (Enemy fixtures replaced by TypingTarget)
import { describe, expect, it } from "vitest";
import {
  accuracyPercent,
  chooseTarget,
  clamp,
  multiplierForStreak,
  normalizeWord,
  splitDisplayByTypedLetters,
  stageWordsPerMinute,
  typingText,
  type TypingTarget,
} from "./index";

function target(id: number, word: string, x: number, y: number): TypingTarget {
  return { id, word, typed: 0, x, y };
}

describe("typed text helpers", () => {
  it("normalizes target words", () => {
    expect(normalizeWord("  Reactor ")).toBe("reactor");
  });

  it("keeps phrase display text while typing only English letters", () => {
    expect(typingText("ice cream")).toBe("icecream");
    expect(typingText("can't-stop")).toBe("cantstop");

    expect(splitDisplayByTypedLetters("ice cream", 3)).toEqual({ typed: "ice", remaining: " cream" });
    expect(splitDisplayByTypedLetters("ice cream", 4)).toEqual({ typed: "ice c", remaining: "ream" });
    expect(splitDisplayByTypedLetters("can't", 4)).toEqual({ typed: "can't", remaining: "" });
    expect(splitDisplayByTypedLetters("word", 0)).toEqual({ typed: "", remaining: "word" });
  });

  it("raises score multiplier at streak milestones", () => {
    expect(multiplierForStreak(24)).toBe(1);
    expect(multiplierForStreak(25)).toBe(2);
    expect(multiplierForStreak(50)).toBe(3);
    expect(multiplierForStreak(100)).toBe(4);
  });

  it("chooses the nearest matching first-letter target", () => {
    const targets = [target(1, "space travel", 300, 100), target(2, "shield", 500, 500), target(3, "code", 400, 600)];
    expect(chooseTarget(targets, "s", 400, 700)?.id).toBe(2);
    expect(chooseTarget(targets, "x", 400, 700)).toBeNull();
  });

  it("reacquires skill-advanced partial words by their next letter", () => {
    const partial = { ...target(7, "meteor", 420, 420), typed: 2 };
    const fresh = target(8, "travel", 400, 500);
    expect(chooseTarget([fresh, partial], "t", 400, 700)?.id).toBe(7);
  });

  it("uses stable tie-breaks for same-initial targets", () => {
    const targets = [target(9, "morning", 300, 500), target(3, "month", 500, 500), target(1, "me", 400, 400)];
    expect(chooseTarget(targets, "m", 400, 600)?.id).toBe(3);
  });

  it("keeps the caller's own target type", () => {
    const lanes = [{ ...target(4, "fire", 0, 0), lane: 2 }];
    expect(chooseTarget(lanes, "f", 0, 0)?.lane).toBe(2);
  });

  it("calculates WPM, accuracy and clamps", () => {
    expect(stageWordsPerMinute(300, 60)).toBe(60);
    expect(stageWordsPerMinute(150, 30)).toBe(60);
    expect(stageWordsPerMinute(50, 0)).toBe(600);
    expect(accuracyPercent(0, 0)).toBe(100);
    expect(accuracyPercent(9, 1)).toBe(90);
    expect(clamp(5, 0, 3)).toBe(3);
    expect(clamp(-1, 0, 3)).toBe(0);
  });
});
