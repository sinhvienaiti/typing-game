// Source: new for the kit: PaceDirector against docs/games/BALANCE.md §4.2
import { describe, expect, it } from "vitest";
import { RngStream } from "../platform/rng";
import { BANDS } from "./bands";
import { PACE_TABLE, PaceDirector, paceTension, type PaceDecision, type PaceTable } from "./director";
import { FlowMeter, type FlowWindow } from "./flow";

const win = (overrides: Partial<FlowWindow> = {}): FlowWindow => ({ ticks: 1200, p: 250, i: 0, o: 0, hp: 800, hpMin: 800, hpLoss: 0, nearDefeat: false, kills: 0, q: null, ...overrides });
const LOW = win({ p: 50 });
const HIGH = win({ o: 200 });
const IN = win();

/** Feeds windows at 300-tick steps; returns the decisions' levers (null for none). */
function drive(director: PaceDirector, windows: readonly FlowWindow[], start = 0): (string | null)[] {
  return windows.map((window, index) => director.evaluate(window, start + (index + 1) * 300)?.lever ?? null);
}

const table = (overrides: Partial<PaceTable>): PaceTable => ({ ...PACE_TABLE, ...overrides });

describe("pace tension", () => {
  it("is 0 in the band (with slack), > 0 too hot, < 0 too calm; hot wins", () => {
    const band = BANDS.balanced;
    expect(paceTension(IN, band)).toBe(0);
    expect(paceTension(win({ p: 140 }), band)).toBe(0);
    expect(paceTension(LOW, band)).toBe(-100);
    expect(paceTension(win({ i: 300 }), band)).toBe(-200);
    expect(paceTension(HIGH, band)).toBe(120);
    expect(paceTension(win({ p: 500 }), band)).toBe(150);
    expect(paceTension(win({ p: 50, o: 200 }), band)).toBe(120);
  });

  it("reads HP only while it is still falling", () => {
    expect(paceTension(win({ hp: 300, hpLoss: 10 }), BANDS.balanced)).toBe(50);
    expect(paceTension(win({ hp: 300, hpLoss: 0 }), BANDS.balanced)).toBe(0);
    // Challenge's S floor is 15 %, but near defeat (< 30 %) is hot in every mode.
    expect(paceTension(win({ p: 400, hp: 200, hpLoss: 30 }), BANDS.challenge)).toBe(100);
    expect(paceTension(win({ hp: 600, hpLoss: 30 }), BANDS.relax)).toBe(100);
  });
});

describe("PaceDirector", () => {
  it("steps harder after 3 low windows and easier after 2 high windows", () => {
    const up = new PaceDirector({ band: BANDS.balanced });
    up.beginWave(1);
    expect(drive(up, [LOW, LOW, LOW])).toEqual([null, null, "spawn"]);
    expect(up.log).toEqual([{ type: "pace", id: 1, tick: 900, wave: 1, dir: 1, lever: "spawn", amount: -70, cost: 0, tension: -100, level: 1, spawnScale: 930 }]);
    const down = new PaceDirector({ band: BANDS.balanced });
    down.beginWave(1);
    expect(drive(down, [HIGH, HIGH])).toEqual([null, "spawn"]);
    expect(down.log[0]).toMatchObject({ dir: -1, amount: 70, spawnScale: 1070, level: -1 });
  });

  it("has hysteresis: in-band windows reset the streak, reversing needs one more window", () => {
    const director = new PaceDirector({ band: BANDS.balanced });
    director.beginWave(1);
    expect(drive(director, [LOW, LOW, IN, LOW, LOW, win({ p: 140 }), LOW, LOW])).toEqual([null, null, null, null, null, null, null, null]);
    expect(drive(director, [LOW], 2400)).toEqual(["spawn"]);
    expect(drive(director, [HIGH, HIGH, HIGH], 2700)).toEqual([null, null, "spawn"]);
    expect(director.log.map((event) => event.spawnScale)).toEqual([930, 1000]);
    // After a down step, the next harder step needs 4 low windows.
    director.beginWave(2);
    expect(drive(director, [LOW, LOW, LOW, LOW], 3600)).toEqual([null, null, null, "elite"]);
  });

  it("takes at most 2 steps a wave and rotates through the table's levers", () => {
    const director = new PaceDirector({ band: BANDS.balanced });
    director.beginWave(1);
    expect(drive(director, Array(9).fill(LOW))).toEqual([null, null, "spawn", null, null, "elite", null, null, null]);
    director.beginWave(2);
    expect(drive(director, Array(6).fill(LOW), 2700)).toEqual([null, null, "peak", null, null, "lull"]);
    expect(director.log.map((event) => [event.wave, event.amount])).toEqual([[1, -70], [1, 1], [2, -180], [2, -180]]);
    expect(director.summary()).toMatchObject({ steps: 4, waves: 2, stepsPerWave: 2, maxWaveSteps: 2, spawnMin: 930, spawnMax: 1000, composition: 30 });
  });

  it("keeps the spawn interval within ±15 % over the stage", () => {
    const director = new PaceDirector({ band: BANDS.balanced, table: table({ up: ["spawn"], down: ["spawn"] }), rules: { perWave: 10 } });
    director.beginWave(1);
    expect(drive(director, Array(9).fill(LOW))).toEqual([null, null, "spawn", null, null, "spawn", null, null, null]);
    expect(director.log.map((event) => event.spawnScale)).toEqual([930, 860]);
    expect(drive(director, Array(18).fill(HIGH), 2700).filter(Boolean)).toEqual(["spawn", "spawn", "spawn", "spawn"]);
    expect(director.log.map((event) => event.spawnScale)).toEqual([930, 860, 930, 1000, 1070, 1140]);
    expect(director.summary()).toMatchObject({ spawnMin: 860, spawnMax: 1140 });
  });

  it("keeps composition/W within ±10 %, against what the game reports", () => {
    const director = new PaceDirector({ band: BANDS.balanced, table: table({ up: ["elite"], eliteCost: 40 }), rules: { perWave: 10 } });
    director.beginWave(1);
    expect(drive(director, Array(9).fill(LOW)).filter(Boolean)).toEqual(["elite", "elite"]);
    expect(director.budget(1)).toBe(20);
    director.report(1, 10);
    expect([director.summary().composition, director.budget(1), director.log[0]!.cost]).toEqual([50, 50, 10]);
    // The low streak was still standing, so the freed budget is used at once.
    expect(drive(director, Array(3).fill(LOW), 2700)).toEqual(["elite", null, null]);
    expect(drive(director, Array(3).fill(LOW), 3600)).toEqual([null, null, null]);
    expect(director.summary().composition).toBe(90);
    director.report(99, 0);
    director.report(1, 10);
    expect(director.summary().composition).toBe(90);
  });

  it("drops one support item near defeat, once a wave", () => {
    const director = new PaceDirector({ band: BANDS.balanced, rules: { perWave: 3 } });
    const dying = win({ hp: 200, hpLoss: 50, nearDefeat: true });
    director.beginWave(1);
    expect(drive(director, [dying, dying, dying, dying])).toEqual([null, "support", null, "spawn"]);
    director.beginWave(2);
    expect(drive(director, [dying, dying], 1200)).toEqual([null, "support"]);
    expect(director.summary().supports).toBe(2);
    // Support is never a harder step, and never far from defeat.
    const calmer = new PaceDirector({ band: BANDS.balanced, table: table({ down: ["support"] }) });
    calmer.beginWave(1);
    expect(drive(calmer, [HIGH, HIGH, HIGH])).toEqual([null, null, null]);
  });

  it("does nothing when off (oath, crown, ranked, duel) or on a short window", () => {
    for (const off of ["oath", "crown", "ranked", "duel", "setting"] as const) {
      const director = new PaceDirector({ band: BANDS.balanced, off });
      director.beginWave(1);
      expect(director.enabled).toBe(false);
      expect(drive(director, Array(6).fill(LOW))).toEqual(Array(6).fill(null));
      expect(director.log).toEqual([]);
      expect(director.last).toMatchObject({ tension: -100, judged: false });
    }
    const director = new PaceDirector({ band: BANDS.balanced });
    director.beginWave(1);
    expect(drive(director, Array(4).fill(win({ p: 50, ticks: 300 })))).toEqual(Array(4).fill(null));
  });

  it("is deterministic: the same snapshots give the same decisions", () => {
    const play = (seed: number) => {
      const rng = new RngStream(seed);
      const meter = new FlowMeter();
      const director = new PaceDirector({ band: BANDS.balanced });
      const decisions: PaceDecision[] = [];
      let hp = 1;
      for (let wave = 1; wave <= 5; wave += 1) {
        director.beginWave(wave);
        meter.resetWindow();
        for (let tick = 0; tick < 3600; tick += 1) {
          const heat = wave / 5;
          if (rng.chance(0.002 * heat)) hp = Math.max(0.05, hp - 0.05);
          meter.feed({ danger: rng.chance(heat * 0.6), hp, live: rng.int(0, 7), capped: rng.chance(heat * 0.1), backlog: rng.int(0, 5), busy: rng.chance(0.5), kills: rng.chance(0.01) ? [rng.float()] : undefined });
          const decision = director.step(meter);
          if (decision !== null) decisions.push(decision);
        }
      }
      return { decisions, log: director.log, state: director.state(), meter: meter.state() };
    };
    const first = play(42);
    expect(play(42)).toEqual(first);
    expect(first.decisions.length).toBeGreaterThan(0);
    expect(first.decisions).toEqual(first.log.map(({ type: _type, ...decision }) => decision));
    expect(play(43)).not.toEqual(first);
  });

  it("judges once per 300 fed ticks", () => {
    const meter = new FlowMeter();
    const director = new PaceDirector({ band: BANDS.balanced });
    let judged = 0;
    for (let tick = 0; tick < 3000; tick += 1) {
      meter.feed({ danger: false, hp: 1, live: 0, capped: false, backlog: 0, busy: false });
      const before = director.last;
      director.step(meter);
      if (director.last !== before) judged += 1;
    }
    expect(judged).toBe(10);
    expect(director.last?.tick).toBe(3000);
  });
});
