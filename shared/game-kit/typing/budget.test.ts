// Source: new for the kit (dragon-hold 00 §5; TD 6.5's stream cap)
import { describe, expect, it } from "vitest";
import { BudgetLedger, letterBudget, POOL, streamCap } from "./budget";
import { TD_TYPING } from "./config";

describe("letter budget (00 §5)", () => {
  it("N_max = min(16; A − 3), K_enemy = max(6; ⌈0.6 N⌉) with 2 urgent, others ≤ 4", () => {
    // 00 §5's example: vocabulary level 1, A ≈ 16 → N 13, K ≥ 8, others ≤ 4.
    expect(letterBudget(16, TD_TYPING.budget)).toEqual({ total: 13, enemy: 8, urgent: 2, other: 4 });
    expect(letterBudget(26, TD_TYPING.budget)).toEqual({ total: 16, enemy: 10, urgent: 2, other: 4 });
    // Few letters: enemies keep their 6, others get what is left.
    expect(letterBudget(11, TD_TYPING.budget)).toEqual({ total: 8, enemy: 6, urgent: 2, other: 2 });
    expect(letterBudget(2, TD_TYPING.budget)).toEqual({ total: 0, enemy: 0, urgent: 0, other: 0 });
  });

  it("TD's stream cap: clamp(A − 6; 4; 12)", () => {
    expect(streamCap(20, TD_TYPING.stream)).toBe(12);
    expect(streamCap(14, TD_TYPING.stream)).toBe(8);
    expect(streamCap(6, TD_TYPING.stream)).toBe(4);
  });

  it("a ledger keeps the urgent slots for urgent enemies, caps every source and the others' pool, and counts jams", () => {
    const ledger = new BudgetLedger(letterBudget(16, TD_TYPING.budget), [
      { id: "enemy", pool: POOL.enemy, cap: 99 },
      { id: "urgent", pool: POOL.urgent, cap: 99 },
      { id: "skill", pool: POOL.other, cap: 2 },
      { id: "assist", pool: POOL.other, cap: 2 },
      { id: "strike", pool: POOL.other, cap: 2 },
    ]);
    const [enemy, urgent, skill, assist, strike] = ["enemy", "urgent", "skill", "assist", "strike"].map((id) => ledger.source(id)) as [number, number, number, number, number];
    expect(() => ledger.source("nope")).toThrow();
    expect(ledger.add(skill) && ledger.add(skill)).toBe(true);
    expect(ledger.add(skill)).toBe(false); // its own cap
    expect(ledger.add(assist) && ledger.add(assist)).toBe(true);
    expect(ledger.add(strike)).toBe(false); // the others' pool (4) is full
    let enemies = 0;
    while (ledger.add(enemy)) enemies += 1;
    expect(enemies).toBe(13 - 4 - 2); // the 2 urgent slots stay free
    expect(ledger.add(urgent) && ledger.add(urgent)).toBe(true);
    expect(ledger.total).toBe(13);
    expect(ledger.add(urgent)).toBe(false);
    expect([...ledger.jams]).toEqual([1, 1, 1, 0, 1]);
    // An urgent word gone: its slot is for urgent enemies again.
    ledger.remove(urgent);
    expect(ledger.canAdd(enemy)).toBe(false);
    expect(ledger.canAdd(urgent)).toBe(true);
    // A skill word gone: another source may take its place in the others' pool.
    ledger.remove(skill);
    expect(ledger.add(strike)).toBe(true);
    expect(ledger.canAdd(enemy)).toBe(false);
    ledger.clear();
    expect(ledger.total).toBe(0);
  });
});
