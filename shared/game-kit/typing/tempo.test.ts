// Source: new for the kit (TD 6.6 baseline, dragon-hold 00 §4.3–4.4)
import { describe, expect, it } from "vitest";
import { BASELINE, expectedSpeed, median, paceFactor, typingCapacity, updateBaseline } from "./tempo";

describe("tempo", () => {
  it("E = max(B, the floor)", () => {
    expect(expectedSpeed(12, 20)).toBe(20);
    expect(expectedSpeed(48, 20)).toBe(48);
  });

  it("moves B toward the median raw speed after ≥ 40 good words: 0.20 up, 0.08 down, held in 12–140", () => {
    const words = (wpm: number, n = 40) => Array.from({ length: n }, (_, k) => wpm + (k % 2 === 0 ? -1 : 1));
    expect(median([5, 1, 3])).toBe(3);
    expect(median([4, 1, 3, 2])).toBe(2.5);
    expect(updateBaseline(30, words(50, 39))).toBe(30);
    expect(updateBaseline(30, words(50))).toBeCloseTo(34, 10);
    expect(updateBaseline(30, words(20))).toBeCloseTo(29.2, 10);
    expect(updateBaseline(139, words(900))).toBe(BASELINE.max);
    expect(updateBaseline(12.5, [...words(5), 0, Number.NaN])).toBe(BASELINE.min);
  });

  it("C(E) ≈ 22.7 words a minute at the reference (E 35, ℓ̄ 4.5, d 0.86); k_E only slows: 25 WPM → 0.75", () => {
    expect(typingCapacity(35, 4.5, 0.86)).toBeCloseTo(22.7, 1);
    expect(typingCapacity(25, 4.5, 0.86)).toBeCloseTo(17.0, 1);
    expect(typingCapacity(60, 5.5, 0.86)).toBeCloseTo(30.6, 1);
    expect(paceFactor(typingCapacity(25, 4.5, 0.86))).toBeCloseTo(0.75, 2);
    expect(paceFactor(typingCapacity(18, 4.5, 0.86))).toBe(0.75);
    expect(paceFactor(typingCapacity(30, 4.5, 0.86))).toBeCloseTo(typingCapacity(30, 4.5, 0.86) / 22.7, 10);
    expect(paceFactor(typingCapacity(60, 5.5, 0.86))).toBe(1);
  });
});
