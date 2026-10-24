// Source: new for the kit: target bands against docs/games/BALANCE.md §3
import { describe, expect, it } from "vitest";
import { BANDS, BAND_METRICS, bandModeFor, rangeText, scoreBand } from "./bands";

describe("target bands", () => {
  it("hold §3's table in ‰ (N as a count)", () => {
    expect(BANDS.relax.win).toEqual({ min: 920 });
    expect(BANDS.balanced).toEqual({
      win: { min: 750, max: 900 },
      s: { min: 350, max: 650 },
      p: { min: 150, max: 350 },
      i: { max: 100 },
      o: { max: 80 },
      n: { min: 0.3, max: 1 },
      q: { min: 500, max: 700 },
    });
    expect(BANDS.challenge.p).toEqual({ min: 300, max: 500 });
    expect(BANDS.challenge.n).toEqual({ min: 1, max: 2 });
    for (const mode of ["relax", "balanced", "challenge"] as const) expect(Object.keys(BANDS[mode])).toEqual([...BAND_METRICS]);
  });

  it("children play the Relax band unless a parent picks another; Learn plays at Relax", () => {
    expect(bandModeFor("child", "challenge")).toBe("relax");
    expect(bandModeFor("child", "balanced", "balanced")).toBe("balanced");
    expect(bandModeFor("adult", "learn")).toBe("relax");
    expect(bandModeFor("adult", "challenge")).toBe("challenge");
  });

  it("scores a summary in, below or above each metric", () => {
    const score = scoreBand({ win: 800, s: 300, p: 400, i: 100, o: 0, n: 0.5, q: null }, BANDS.balanced);
    expect(score.rows.map((row) => [row.metric, row.verdict])).toEqual([
      ["win", "in"],
      ["s", "below"],
      ["p", "above"],
      ["i", "in"],
      ["o", "in"],
      ["n", "in"],
      ["q", "missing"],
    ]);
    expect(score.inBand).toBe(false);
    expect(scoreBand({ win: 800, s: 500, p: 200, i: 50, o: 10 }, BANDS.balanced, ["win", "s", "p", "i", "o"]).inBand).toBe(true);
    expect(scoreBand({ win: 990, s: 990 }, BANDS.relax, ["win", "s"]).inBand).toBe(true);
  });

  it("prints ranges for a report", () => {
    expect(rangeText("p", BANDS.balanced.p)).toBe("15–35 %");
    expect(rangeText("win", BANDS.relax.win)).toBe("≥ 92 %");
    expect(rangeText("o", BANDS.relax.o)).toBe("≤ 3 %");
    expect(rangeText("n", BANDS.balanced.n)).toBe("0.3–1");
  });
});
