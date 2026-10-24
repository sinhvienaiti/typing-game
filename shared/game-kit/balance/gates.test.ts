// Source: new for the kit: gates B1–B9 against docs/games/BALANCE.md §7
import { describe, expect, it } from "vitest";
import type { BandMode } from "./bands";
import type { FlowSummary } from "./flow";
import { formatGates, gate, pct, runGates, summarizeRuns, type BotModeSummary, type GateInput } from "./gates";

const flow = (overrides: Partial<FlowSummary> = {}): FlowSummary => ({ outcome: "won", ticks: 20000, p: 250, i: 50, o: 20, s: 500, hpMin: 400, n: 0.5, kills: 80, q: 600, support: 300, ...overrides });

/** A cell that sits mid-band in Balanced (win 80 %, S 50 %, P 25 %, I 5 %, O 2 %). */
const cell = (bot: string, mode: BandMode, overrides: Partial<BotModeSummary> = {}): BotModeSummary => ({
  bot, mode, director: true, runs: 20, win: 800, s: 500, p: 250, i: 50, o: 20, n: 0.5, q: 600, support: 300,
  killSeconds: 3, stepsPerWave: 1.2, maxWaveSteps: 2, spawnMin: 930, spawnMax: 1070, learnOk: true, ...overrides,
});

/** A matrix that passes every gate but B9 (no human play-test yet). */
function matrix(): BotModeSummary[] {
  const rows: BotModeSummary[] = [
    cell("novice", "balanced"),
    cell("steady", "balanced", { s: 600 }),
    cell("standard", "balanced"),
    cell("skilled", "balanced"),
    cell("sloppy", "balanced", { s: 450, killSeconds: 3.4 }),
    cell("fast", "balanced"),
    cell("child", "relax", { win: 950, s: 800 }),
    cell("standard", "balanced", { director: false, stepsPerWave: null, spawnMin: null, spawnMax: null }),
  ];
  for (const mode of ["relax", "balanced", "challenge"] as const) rows.push(cell("no-type", mode, { win: 0, s: 0 }));
  for (const mode of ["balanced", "challenge"] as const) {
    rows.push(cell("standard@good", mode, { win: 820 }));
    rows.push(cell("standard@poor", mode, { win: 690 }));
  }
  return rows;
}

const status = (input: GateInput) => Object.fromEntries(runGates(input).map((row) => [row.id, row.status]));

describe("balance gates", () => {
  it("fold a cell's runs: win rate, median S, mean P/I/O/N, median Q, director numbers", () => {
    const runs = [
      { flow: flow({ s: 600, p: 200 }), pace: { steps: 4, waves: 4, stepsPerWave: 1, maxWaveSteps: 2, spawnMin: 930, spawnMax: 1000, spawnScale: 1000, composition: 0, supports: 0 }, killSeconds: 2, learnOk: true },
      { flow: flow({ s: 400, p: 300, q: 700 }), pace: { steps: 8, waves: 4, stepsPerWave: 2, maxWaveSteps: 2, spawnMin: 860, spawnMax: 1070, spawnScale: 1000, composition: 30, supports: 1 }, killSeconds: 4, learnOk: true },
      { flow: flow({ outcome: "lost", s: 0, n: 2, q: null }), learnOk: false },
    ];
    const summary = summarizeRuns("standard", "balanced", runs);
    expect(summary).toMatchObject({ runs: 3, win: 667, s: 400, p: 250, n: 1, q: 650, killSeconds: 3, stepsPerWave: 1.5, maxWaveSteps: 2, spawnMin: 860, spawnMax: 1070, learnOk: false, director: true });
    expect(summarizeRuns("x", "relax", [])).toMatchObject({ runs: 0, win: 0, q: null, stepsPerWave: null, learnOk: null });
  });

  it("pass a healthy matrix; B9 waits for a human play-test", () => {
    expect(status({ summaries: matrix() })).toEqual({ B1: "pass", B2: "pass", B3: "pass", B4: "pass", B5: "pass", B6: "pass", B7: "pass", B8: "pass", B9: "skip" });
  });

  it("B1 fails a bot outside the Balanced band and says which metric", () => {
    const rows = matrix().map((row) => (row.bot === "fast" && row.mode === "balanced" ? { ...row, p: 80, i: 250 } : row));
    const b1 = gate("B1", { summaries: rows });
    expect(b1.status).toBe("fail");
    const fast = b1.checks.find((check) => check.label === "fast")!;
    expect([fast.pass, fast.threshold]).toEqual([false, "lệch: Áp lực P thấp, Nhàn I cao"]);
  });

  it("B2 catches an easy stage; B3 a hard one", () => {
    const easy = matrix().map((row) => (row.bot === "fast" && row.mode === "balanced" ? { ...row, s: 950, i: 260 } : row));
    expect(gate("B2", { summaries: easy }).status).toBe("fail");
    const hard = matrix().map((row) => (row.bot === "novice" ? { ...row, win: 650 } : row));
    expect(gate("B3", { summaries: hard }).checks.map((check) => check.pass)).toEqual([false, true]);
  });

  it("B4 compares steady with sloppy, and kill time (or Q) of standard with sloppy", () => {
    const rows = matrix();
    expect(gate("B4", { summaries: rows }).checks.map((check) => check.measured)).toEqual(["S 60 % vs 45 %", "hạ quái 3.00 s vs 3.40 s"]);
    const noTimes = rows.map((row) => ({ ...row, killSeconds: null, q: row.bot === "sloppy" ? 650 : row.q }));
    expect(gate("B4", { summaries: noTimes }).checks[1]).toMatchObject({ measured: "Q 60 % vs 65 %", pass: true });
    const sloppyWins = rows.map((row) => (row.bot === "sloppy" ? { ...row, s: 700 } : row));
    expect(gate("B4", { summaries: sloppyWins }).status).toBe("fail");
  });

  it("B5 lets the no-type bot win only where the game says so", () => {
    const rows = matrix().map((row) => (row.bot === "no-type" && row.mode === "relax" ? { ...row, win: 600 } : row));
    expect(gate("B5", { summaries: rows }).status).toBe("fail");
    expect(gate("B5", { summaries: rows, options: { noTypeExempt: ["relax"] } }).status).toBe("pass");
  });

  it("B6 needs good tactics ≥ 10 points over poor in Balanced and Challenge", () => {
    const rows = matrix().map((row) => (row.bot === "standard@poor" && row.mode === "challenge" ? { ...row, win: 750 } : row));
    expect(gate("B6", { summaries: rows }).checks.map((check) => check.pass)).toEqual([true, false]);
  });

  it("B7 checks steps a wave, the ±15 % spawn cap and the standard bot with the director off", () => {
    const busy = matrix().map((row) => (row.bot === "skilled" ? { ...row, stepsPerWave: 3.5 } : row));
    expect(gate("B7", { summaries: busy }).status).toBe("fail");
    const wide = matrix().map((row) => (row.bot === "skilled" ? { ...row, spawnMin: 800 } : row));
    expect(gate("B7", { summaries: wide }).status).toBe("fail");
    const offBand = matrix().map((row) => (!row.director ? { ...row, p: 60 } : row));
    expect(gate("B7", { summaries: offBand }).checks.at(-1)).toMatchObject({ label: "standard · tắt nhịp", pass: false });
  });

  it("B8 reads the game's learning gate; B9 compares a human play-test within 15 %", () => {
    const rows = matrix().map((row) => (row.bot === "sloppy" ? { ...row, learnOk: false } : row));
    expect(gate("B8", { summaries: rows }).status).toBe("fail");
    const human = { s: 500, p: 300, i: 40, o: 20, n: 1, q: 600 };
    const close = { s: 560, p: 330, i: 60, o: 40, n: 1.1, q: 650 };
    expect(gate("B9", { summaries: rows, options: { human: [{ label: "chủ dự án · ải 3", human, bot: close }] } }).status).toBe("pass");
    const far = { ...close, p: 400 };
    expect(gate("B9", { summaries: rows, options: { human: [{ label: "chủ dự án · ải 3", human, bot: far }] } }).checks[0]).toMatchObject({ pass: false, threshold: "lệch: Áp lực P" });
  });

  it("skip, never pass, when cells are missing", () => {
    const rows = matrix().filter((row) => row.bot !== "novice");
    const b1 = gate("B1", { summaries: rows });
    expect([b1.status, b1.missing]).toEqual(["skip", ["novice · Cân bằng"]]);
    expect(gate("B3", { summaries: rows }).status).toBe("skip");
    expect(status({ summaries: [] })).toEqual({ B1: "skip", B2: "skip", B3: "skip", B4: "skip", B5: "skip", B6: "skip", B7: "skip", B8: "skip", B9: "skip" });
  });

  it("print the same Markdown table in every game", () => {
    const text = formatGates(runGates({ summaries: matrix() }));
    const lines = text.split("\n");
    expect(lines[0]).toBe("| # | Cổng | Kết quả | Số đo |");
    expect(lines).toHaveLength(11);
    expect(lines[2]).toMatch(/^\| B1 \| Cùng vùng cuốn \| ĐẠT \| ✓ novice: Thắng 80 %/);
    expect(lines[10]).toBe("| B9 | Khớp người thật | THIẾU SỐ | thiếu: buổi chơi thử của người thật |");
    expect([pct(800), pct(25), pct(30), pct(null)]).toEqual(["80 %", "2.5 %", "3 %", "—"]);
  });
});
