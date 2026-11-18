import { describe, expect, it } from "vitest";
import { VariantPicker } from "./variants";
function seeded() { let seed = 198; return () => ((seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0) / 2 ** 32); }
describe("variants", () => {
  it("has no consecutive repeats and distributes 1000 plays across three variants", () => {
    const p = new VariantPicker({ random: seeded() }); const counts = [0, 0, 0]; let last = -1;
    for (let i = 0; i < 1000; i++) { const n = p.pick("hit", [0, 1, 2])!; expect(n).not.toBe(last); counts[n]!++; last = n; }
    for (const count of counts) expect(count / 1000).toBeGreaterThanOrEqual(0.2);
    for (const count of counts) expect(count / 1000).toBeLessThanOrEqual(0.47);
  });
  it("avoids the last two of four, independently per id", () => {
    const p = new VariantPicker({ random: seeded(), avoidLast: 2 }); const history: number[] = [];
    for (let i = 0; i < 1000; i++) { const n = p.pick("key", [0, 1, 2, 3])!; expect(history.slice(-2)).not.toContain(n); history.push(n); p.pick("other", [0]); }
  });
  it("caps history to count minus one, including one or zero variants", () => {
    const p = new VariantPicker({ avoidLast: 99, random: () => 0 });
    expect(p.pick("none", [])).toBeUndefined();
    expect(p.pick("one", [7])).toBe(7); expect(p.pick("one", [7])).toBe(7);
    expect([p.pick("two", [0, 1]), p.pick("two", [0, 1]), p.pick("two", [0, 1])]).toEqual([0, 1, 0]);
  });
  it("uses explicit zero-based variant and remembers it; unavailable means silence", () => {
    const p = new VariantPicker({ random: () => 0 });
    expect(p.pick("hit", [0, 2], 2)).toBe(2); expect(p.pick("hit", [0, 2], 1)).toBeUndefined();
    expect(p.pick("hit", [0, 2])).toBe(0); expect(p.pick("hit", [0, 2], 0)).toBe(0);
  });
});
