// Source: new for the kit: HumanTypist statistics over many seeds (docs/games/BALANCE.md §6)
import { describe, expect, it } from "vitest";
import { RngStream } from "../platform/rng";
import { detExp, detLn } from "./math";
import { HumanTypist, KeyPlayer, RECOGNIZE, STANDARD_BOTS, botParams, type BotId, type TypedWord, type TypistParams, type WordContext } from "./typist";

const SEEDS = 40;
const WORDS = 100;

function words(seed: number, length?: number): string[] {
  const rng = new RngStream(seed ^ 0x5eed);
  return Array.from({ length: WORDS }, () => Array.from({ length: length ?? rng.int(4, 7) }, () => "abcdefghijklmnopqrstuvwxyz"[rng.int(0, 25)]).join(""));
}

/** Every word each seed's typist plans. */
function plans(params: TypistParams, context: WordContext = { familiarity: "known" }, length?: number): TypedWord[] {
  const out: TypedWord[] = [];
  for (let seed = 1; seed <= SEEDS; seed += 1) {
    const typist = new HumanTypist(params, new RngStream(seed));
    for (const text of words(seed, length)) out.push(typist.word(text, context));
  }
  return out;
}

/** Gross WPM: keystrokes after the first over the time from the first key to the last. */
function grossWpm(typed: readonly TypedWord[], hz = 60): number {
  let strokes = 0;
  let ticks = 0;
  for (const word of typed) {
    if (word.events.length < 2) continue;
    strokes += word.events.length - 1;
    ticks += word.events[word.events.length - 1]!.at - word.events[0]!.at;
  }
  return (12 * strokes) / (ticks / hz);
}

const keyEvents = (typed: readonly TypedWord[]) => typed.flatMap((word) => word.events.filter((event) => event.kind === "key"));

describe("HumanTypist", () => {
  it("types familiar words at E within 5 %", () => {
    for (const id of ["novice", "standard", "skilled", "fast"] as const) {
      const params = botParams(id);
      expect(Math.abs(grossWpm(plans(params)) / params.wpm - 1)).toBeLessThan(0.05);
    }
  });

  it("makes wrong keys at 1 − a", () => {
    for (const id of ["steady", "standard", "sloppy", "child"] as const) {
      const keys = keyEvents(plans(botParams(id)));
      const wrong = keys.filter((event) => event.kind === "key" && !event.correct).length / keys.length;
      expect(Math.abs(wrong - (1 - botParams(id).accuracy))).toBeLessThan(0.012);
    }
    const keys = keyEvents(plans(botParams("standard")));
    for (const event of keys) if (event.kind === "key" && !event.correct) expect(event.key).toMatch(/^[a-z]$/);
  });

  it("spreads per-word time with the target CV (log-normal)", () => {
    for (const cv of [0.15, 0.25, 0.4]) {
      const typed = plans(botParams("standard", { accuracy: 1, cv }), { familiarity: "known" }, 6);
      const times = typed.map((word) => word.events[word.events.length - 1]!.at - word.events[0]!.at);
      const mean = times.reduce((sum, value) => sum + value, 0) / times.length;
      const sd = Math.sqrt(times.reduce((sum, value) => sum + (value - mean) ** 2, 0) / (times.length - 1));
      expect(Math.abs(sd / mean / cv - 1)).toBeLessThan(0.12);
    }
  });

  it("recognises words in §6's ranges by familiarity", () => {
    for (const familiarity of ["known", "learning", "new"] as const) {
      const typed = plans(botParams("standard"), { familiarity });
      const [lo, hi] = RECOGNIZE[familiarity];
      const firsts = typed.map((word) => word.events[0]!.at);
      expect(Math.min(...firsts)).toBeGreaterThanOrEqual(Math.floor(lo * 60));
      expect(Math.max(...firsts)).toBeLessThanOrEqual(Math.ceil(hi * 60));
      expect(typed.every((word) => word.recognize === word.events[0]!.at)).toBe(true);
      const mean = firsts.reduce((sum, value) => sum + value, 0) / firsts.length / 60;
      expect(mean).toBeCloseTo((lo + hi) / 2, 1);
    }
  });

  it("follows a wrong key with Backspace or a dropped lock by its chances", () => {
    const typed = plans(botParams("sloppy"));
    let wrong = 0;
    let backspace = 0;
    let abandon = 0;
    for (const word of typed) {
      word.events.forEach((event, index) => {
        if (event.kind !== "key" || event.correct) return;
        wrong += 1;
        const next = word.events[index + 1];
        if (next?.kind === "backspace") backspace += 1;
        if (next?.kind === "abandon") abandon += 1;
      });
      expect(word.abandoned).toBe(word.events[word.events.length - 1]!.kind === "abandon");
    }
    const p = botParams("sloppy");
    expect(Math.abs(abandon / wrong - p.abandon)).toBeLessThan(0.015);
    expect(Math.abs(backspace / wrong - (1 - p.abandon) * p.backspace)).toBeLessThan(0.03);
    // A finished word ends on its last letter, typed right.
    for (const word of typed.filter((entry) => !entry.abandoned)) expect(word.events[word.events.length - 1]).toMatchObject({ kind: "key", correct: true });
  });

  it("slows down in a crowd and with fatigue", () => {
    const params = botParams("standard");
    const typist = new HumanTypist(params, new RngStream(1));
    expect(typist.speed()).toBe(35);
    expect(typist.speed({ live: 5 })).toBe(35);
    expect(typist.speed({ live: 6 })).toBeCloseTo(28, 10);
    expect(typist.speed({ minute: 20 })).toBeCloseTo(35 * 0.94, 10);
    expect(typist.speed({ minute: 1000 })).toBeCloseTo(35 * 0.7, 10);
    const crowded = grossWpm(plans(params, { familiarity: "known", live: 8 }));
    expect(Math.abs(crowded / 28 - 1)).toBeLessThan(0.05);
  });

  it("picks targets by its mix, looks away, answers telegraphs by its reflex", () => {
    const options = [
      { danger: 1, distance: 5, shown: 0 },
      { danger: 3, distance: 9, shown: 2 },
      { danger: 2, distance: 1, shown: 1 },
    ];
    const only = (target: TypistParams["target"]) => new HumanTypist(botParams("standard", { target }), new RngStream(3)).choose(options);
    expect(only({ danger: 1, nearest: 0, first: 0 })).toBe(1);
    expect(only({ danger: 0, nearest: 1, first: 0 })).toBe(2);
    expect(only({ danger: 0, nearest: 0, first: 1 })).toBe(0);
    expect(new HumanTypist(botParams("standard"), new RngStream(3)).choose([])).toBe(-1);
    const good = new HumanTypist(botParams("fast"), new RngStream(9));
    const picks = [0, 0, 0];
    for (let index = 0; index < 4000; index += 1) picks[good.choose(options)]! += 1;
    expect(picks[1]! / 4000).toBeCloseTo(0.7, 1);
    const looks = Array.from({ length: 500 }, () => good.lookAway());
    expect(Math.min(...looks)).toBeGreaterThanOrEqual(36);
    expect(Math.max(...looks)).toBeLessThanOrEqual(72);
    let handled = 0;
    for (let index = 0; index < 4000; index += 1) if (good.handlesTelegraph()) handled += 1;
    expect(handled / 4000).toBeCloseTo(0.9, 1);
  });

  it("is deterministic per seed; the no-type bot never types", () => {
    const a = new HumanTypist(botParams("sloppy"), new RngStream(77));
    const b = new HumanTypist(botParams("sloppy"), new RngStream(77));
    for (const text of ["dragon", "keep", "fire", "nguoi"]) expect(a.word(text, { familiarity: "new" })).toEqual(b.word(text, { familiarity: "new" }));
    const idle = new HumanTypist(botParams("no-type"), new RngStream(1)).word("dragon", { familiarity: "known" });
    expect([idle.events, idle.abandoned]).toEqual([[], true]);
  });

  it("plays a planned word out from a start tick", () => {
    const word = new HumanTypist(botParams("standard", { accuracy: 1 }), new RngStream(5)).word("fire", { familiarity: "known" });
    const player = new KeyPlayer(word, 100);
    expect(player.due(100 + word.recognize - 1)).toEqual([]);
    expect(player.due(100 + word.recognize).map((event) => event.kind === "key" && event.key)).toEqual(["f"]);
    expect(player.due(100 + word.ticks).map((event) => event.kind === "key" && event.key)).toEqual(["i", "r", "e"]);
    expect(player.done).toBe(true);
  });

  it("carries §6's standard bot set", () => {
    const rows = STANDARD_BOTS.map((bot) => [bot.label, bot.wpm, bot.accuracy, bot.cv, bot.tactics]);
    expect(rows).toEqual([
      ["Trẻ em", 15, 0.88, 0.4, "poor"],
      ["Mới", 25, 0.92, 0.35, "fair"],
      ["Chậm chắc", 25, 0.99, 0.2, "fair"],
      ["Chuẩn", 35, 0.95, 0.25, "fair"],
      ["Khá", 50, 0.96, 0.2, "good"],
      ["Ẩu", 50, 0.85, 0.35, "fair"],
      ["Nhanh", 70, 0.97, 0.15, "good"],
      ["Không gõ", 0, 1, 0, "good"],
      ["Chỉ gõ", 35, 0.95, 0.25, "none"],
    ]);
    const ids: BotId[] = STANDARD_BOTS.map((bot) => bot.id);
    expect(new Set(ids).size).toBe(9);
    expect(botParams("standard", { tactics: "poor" })).toMatchObject({ tactics: "poor", reflex: 0.5, target: { danger: 0.2 } });
    expect(() => botParams("nobody" as BotId)).toThrow();
  });

  it("draws log-normal factors with basic arithmetic only", () => {
    for (const x of [-20, -3.7, -0.5, 0, 0.3, 1, 7.25, 40]) expect(detExp(x) / Math.exp(x)).toBeCloseTo(1, 13);
    for (const x of [1e-6, 0.07, 0.5, 1, 1.0625, 2, 10, 12345]) expect(detLn(x) - Math.log(x)).toBeCloseTo(0, 13);
    expect([detExp(Number.NaN), detExp(800), detExp(-800), detLn(0), detLn(-1)]).toEqual([Number.NaN, Number.POSITIVE_INFINITY, 0, Number.NEGATIVE_INFINITY, Number.NaN]);
  });
});
