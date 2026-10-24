// Source: games/space-typing@survival-s0 tests/feedback-numbers.test.ts (kit copy, plus the profiles)
import { afterEach, describe, expect, it } from "vitest";
import { NUMBER_ATLAS, NumberField, NumberSprites, STYLE, digitCellWidth, popScale, type GlyphMetrics } from "./numbers";
import { DRAGON, SHIP } from "./profiles";

/**
 * Damage numbers (docs/survival/BUILD_S0.md §6): blows on one target within
 * 150 ms roll up, beam ticks over 0.3 s with "×N", the cap drops the
 * smallest first (never T3 and up), and no number covers a protected
 * rectangle (the learning frame, the gun slots, the health bar).
 */
const field = () => {
  const f = new NumberField();
  f.fontPx = 20;
  f.limit = 160;
  return f;
};
const live = (f: NumberField) => [...f.alive].map((alive, i) => (alive === 1 ? i : -1)).filter((i) => i >= 0);

describe("rolling up", () => {
  it("adds blows on one target within 150 ms into one number that pops again", () => {
    const f = field();
    const a = f.spawn(7, 400, 300, 7, STYLE.normal, 1, 1, 0.45, 0, -1, 1.0);
    f.update(0.05);
    const b = f.spawn(7, 410, 300, 7, STYLE.crit, 2, 1.3, 0.6, 0, -1, 1.1);
    expect(b).toBe(a);
    expect(f.value[a]).toBe(14);
    expect(f.style[a]).toBe(STYLE.crit);
    expect(f.pop[a]).toBe(1);
    expect(f.live).toBe(1);
    // After the window a new number starts; another target elsewhere is another number.
    expect(f.spawn(7, 400, 300, 7, STYLE.normal, 1, 1, 0.45, 0, -1, 1.2)).not.toBe(a);
    expect(f.spawn(8, 700, 300, 7, STYLE.normal, 1, 1, 0.45, 0, -1, 1.2)).not.toBe(a);
    expect(f.live).toBe(3);
  });

  it("rolls beam ticks up over 0.3 s and shows ×N", () => {
    const f = field();
    const i = f.spawn(3, 500, 200, 6, STYLE.tick, 1, 1, 0.45, 1, 0, 0);
    for (let k = 1; k <= 5; k += 1) f.spawn(3, 500, 200, 6, STYLE.tick, 1, 1, 0.45, 1, 0, k * 0.05);
    expect(f.text(i)).toBe("36×6");
    expect(f.spawn(3, 500, 200, 6, STYLE.tick, 1, 1, 0.45, 1, 0, 0.35)).not.toBe(i);
    // A tick and a round on the same target stay apart.
    expect(f.spawn(3, 500, 200, 7, STYLE.normal, 1, 1, 0.45, 1, 0, 0.36)).not.toBe(i);
  });

  it("flies along its blow, then fades out", () => {
    const f = field();
    const i = f.spawn(1, 300, 300, 9, STYLE.normal, 1, 1, 0.45, 1, 0, 0);
    const x = f.x[i]!;
    f.update(0.1);
    expect(f.x[i]).toBeGreaterThan(x);
    f.update(0.5);
    expect(f.alive[i]).toBe(0);
  });
});

describe("the cap", () => {
  it("drops the smallest number below T3 first, and never a T3 one", () => {
    const f = field();
    f.limit = 4;
    f.spawn(1, 100, 100, 5, STYLE.normal, 1, 1, 1, 0, -1, 0);
    f.spawn(2, 200, 100, 9, STYLE.normal, 1, 1, 1, 0, -1, 0);
    f.spawn(3, 300, 100, 30, STYLE.perfect, 3, 1.6, 1, 0, -1, 0);
    f.spawn(4, 400, 100, 2, STYLE.normal, 1, 1, 1, 0, -1, 0);
    expect(f.live).toBe(4);
    // A bigger one replaces the smallest (2); a smaller one is dropped.
    f.spawn(5, 500, 100, 12, STYLE.crit, 2, 1.3, 1, 0, -1, 0);
    expect(live(f).map((i) => f.value[i]).sort((a, b) => a! - b!)).toEqual([5, 9, 12, 30]);
    expect(f.spawn(6, 600, 100, 1, STYLE.normal, 1, 1, 1, 0, -1, 0)).toBe(-1);
    // T3 blows push out small ones but the T3 numbers themselves stay.
    for (let k = 0; k < 6; k += 1) f.spawn(10 + k, 100 + k * 50, 200, 3, STYLE.perfect, 3, 1.6, 1, 0, -1, 0);
    expect(live(f).every((i) => f.tier[i] === 3)).toBe(true);
    expect(f.live).toBeLessThanOrEqual(4);
  });
});

describe("protected rectangles", () => {
  it("moves a number above a protected rectangle, or drops it; none ever covers one", () => {
    const f = field();
    f.protected = [{ x: 400, y: 580, w: 480, h: 140 }, { x: 0, y: 0, w: 330, h: 60 }];
    // Spawned inside the learning frame: lifted above it.
    const i = f.spawn(1, 640, 600, 20, STYLE.crit, 2, 1.3, 0.6, 0, 1, 0);
    expect(i).toBeGreaterThanOrEqual(0);
    const box = f.box(i, { x: 0, y: 0, w: 0, h: 0 });
    expect(box.y + box.h).toBeLessThanOrEqual(580);
    // Under the health bar with no room above: dropped.
    expect(f.spawn(2, 100, 20, 20, STYLE.normal, 1, 1, 0.6, 0, -1, 0)).toBe(-1);
    // Drifting into one: gone.
    const j = f.spawn(3, 200, 100, 20, STYLE.normal, 1, 1, 2, 0, -1, 0);
    expect(j).toBeGreaterThanOrEqual(0);
    for (let t = 0; t < 40 && f.alive[j] === 1; t += 1) {
      f.update(1 / 60);
      expect(f.overlaps()).toBe(0);
    }
    expect(f.alive[j]).toBe(0);
    // A storm of numbers over the whole screen never covers a rectangle.
    let seed = 3;
    const random = () => ((seed = (Math.imul(seed, 48271) + 7) >>> 0) / 4294967296);
    for (let k = 0; k < 600; k += 1) {
      f.spawn(100 + (k % 80), random() * 1280, random() * 720, 1 + random() * 40, k % 7 === 0 ? STYLE.perfect : STYLE.normal, k % 7 === 0 ? 3 : 1, k % 7 === 0 ? 1.6 : 1, 0.6, random() - 0.5, random() - 0.5, k / 60);
      f.update(1 / 60);
      expect(f.overlaps()).toBe(0);
    }
    expect(f.live).toBeLessThanOrEqual(f.limit);
  });
});

describe("a crowd's numbers (S0 review: no towers)", () => {
  const extent = (f: NumberField) => {
    const boxes = live(f).map((i) => f.box(i, { x: 0, y: 0, w: 0, h: 0 }));
    return { top: Math.min(...boxes.map((b) => b.y)), bottom: Math.max(...boxes.map((b) => b.y + b.h)) };
  };
  const overlapping = (f: NumberField) => {
    const boxes = live(f).map((i) => f.box(i, { x: 0, y: 0, w: 0, h: 0 }));
    let count = 0;
    for (let i = 0; i < boxes.length; i += 1) {
      for (let j = i + 1; j < boxes.length; j += 1) {
        const p = boxes[i]!;
        const q = boxes[j]!;
        if (p.x < q.x + q.w && p.x + p.w > q.x && p.y < q.y + q.h && p.y + p.h > q.y) count += 1;
      }
    }
    return count;
  };

  it("takes beam ticks from many stretches landing on one spot into one number, not a column", () => {
    const f = field();
    for (let k = 0; k < 10; k += 1) f.spawn(-1 - k, 640 + (k % 3) * 4, 300 - (k % 2) * 6, 6, STYLE.tick, 1, 1, 0.45, 1, 0, k * 0.02);
    expect(f.live).toBeLessThanOrEqual(2);
    expect(live(f).reduce((sum, i) => sum + f.value[i]!, 0)).toBe(60);
    const { top, bottom } = extent(f);
    expect(bottom - top).toBeLessThanOrEqual(f.fontPx * 2.6);
  });

  it("rounds on different foes at one spot roll up while young; a number of another style goes beside, not on top", () => {
    const f = field();
    const a = f.spawn(1, 640, 300, 7, STYLE.normal, 1, 1, 0.45, 0, -1, 0);
    expect(f.spawn(2, 642, 302, 7, STYLE.normal, 1, 1, 0.45, 0, -1, 0.05)).toBe(a);
    expect(f.value[a]).toBe(14);
    expect(f.count[a]).toBe(2);
    const c = f.spawn(3, 640, 300, 16, STYLE.crit, 2, 1.3, 0.6, 1, 0, 0.06);
    expect(c).not.toBe(a);
    expect(overlapping(f)).toBe(0);
    // Beside: about level with it, not stacked above.
    expect(Math.abs(f.y[c]! - f.y[a]!)).toBeLessThan(f.fontPx);
    // A T3 number never swallows (nor is swallowed by) the others.
    const p = f.spawn(4, 640, 300, 30, STYLE.perfect, 3, 1.6, 0.8, 0, -1, 0.07);
    expect([a, c]).not.toContain(p);
    expect(f.value[p]).toBe(30);
  });

  it("an old number of the same style is not taken: the new one goes beside it", () => {
    const f = field();
    const a = f.spawn(1, 640, 300, 7, STYLE.normal, 1, 1, 2, 0, -1, 0);
    const b = f.spawn(2, 640, 300, 7, STYLE.normal, 1, 1, 2, 0, -1, 0.31);
    expect(b).not.toBe(a);
    expect(f.value[a]).toBe(7);
    expect(overlapping(f)).toBe(0);
  });

  it("a number that grows onto its neighbour takes it in: live numbers never overlap after a frame", () => {
    const f = field();
    const a = f.spawn(-1, 600, 300, 6, STYLE.tick, 1, 1, 0.9, 0, -1, 0);
    const width = f.box(a, { x: 0, y: 0, w: 0, h: 0 }).w;
    const b = f.spawn(-2, 600 + width + 6, 300, 6, STYLE.tick, 1, 1, 0.9, 0, -1, 0.4);
    expect(b).not.toBe(a);
    // a's label grows ("6" → "48×8"): its box now reaches b.
    for (let k = 1; k < 8; k += 1) f.spawn(-1, 600, 300, 6, STYLE.tick, 1, 1, 0.9, 0, -1, k * 0.03);
    f.update(1 / 60);
    expect(overlapping(f)).toBe(0);
    expect(live(f).reduce((sum, i) => sum + f.value[i]!, 0)).toBe(54);
  });

  it("settle() lifts the younger of two overlapping numbers it may not merge (another style) above the older", () => {
    const f = field();
    const a = f.spawn(1, 640, 300, 7, STYLE.normal, 1, 1, 2, 0, -1, 0);
    const c = f.spawn(2, 900, 300, 16, STYLE.crit, 2, 1.3, 2, 0, -1, 0.01);
    // Moved onto a by hand (a game dragging numbers with its view).
    f.x[c] = f.x[a]!;
    f.y[c] = f.y[a]!;
    expect(overlapping(f)).toBe(1);
    f.settle();
    expect(overlapping(f)).toBe(0);
    expect(f.y[c]!).toBeLessThan(f.y[a]!);
    expect([f.alive[a], f.alive[c]]).toEqual([1, 1]);
  });

  it("a fight's blows on a crowd: overlaps last at most a frame, no tall columns, none on the learning frame", () => {
    const f = field();
    f.protected = [{ x: 400, y: 580, w: 480, h: 140 }];
    let seed = 9;
    const random = () => ((seed = (Math.imul(seed, 48271) + 7) >>> 0) / 4294967296);
    const pairs = () => {
      const ids = live(f);
      const out = new Set<string>();
      for (const i of ids) {
        for (const j of ids) {
          if (j <= i) continue;
          const p = f.box(i, { x: 0, y: 0, w: 0, h: 0 });
          const q = f.box(j, { x: 0, y: 0, w: 0, h: 0 });
          if (p.x < q.x + q.w && p.x + p.w > q.x && p.y < q.y + q.h && p.y + p.h > q.y) out.add(i + ":" + j + ":" + f.born[i] + ":" + f.born[j]);
        }
      }
      return out;
    };
    let previous = new Set<string>();
    let lasting = 0;
    let column = 0;
    for (let frame = 0; frame < 600; frame += 1) {
      // 120 blows a second on 40 foes in a 300 × 100 px band; 40 % are beam ticks.
      for (let k = 0; k < 2; k += 1) {
        const foe = Math.floor(random() * 40);
        const tick = random() < 0.4;
        const style = tick ? STYLE.tick : random() < 0.15 ? STYLE.crit : STYLE.normal;
        f.spawn(tick ? -1 - (foe % 6) : foe, 490 + random() * 300, 340 + random() * 100, 2 + random() * 12, style, random() < 0.2 ? 2 : 1, 1, 0.6, random() - 0.5, -1, frame / 60);
      }
      f.update(1 / 60);
      expect(f.overlaps()).toBe(0);
      const now = pairs();
      for (const pair of now) if (previous.has(pair)) lasting += 1;
      previous = now;
      // The most numbers stacked on one vertical line (a tower).
      const boxes = live(f).map((i) => f.box(i, { x: 0, y: 0, w: 0, h: 0 }));
      for (const b of boxes) column = Math.max(column, boxes.filter((q) => q.x <= b.x + b.w / 2 && q.x + q.w >= b.x + b.w / 2).length);
    }
    // The pre-review code on this run: 7016 lasting overlaps, 12 numbers in one column (now 0 and 9).
    expect(lasting).toBeLessThanOrEqual(2);
    expect(column).toBeLessThanOrEqual(10);
  });

  it("counts a number's pop in its box, so a popping number near the learning frame never spills onto it", () => {
    const f = field();
    expect(popScale(3, 1)).toBeCloseTo(1.35);
    expect(popScale(3, 0)).toBe(1);
    expect(popScale(0, 1)).toBe(1);
    expect(popScale(9, 1)).toBeCloseTo(1.5);
    f.protected = [{ x: 400, y: 580, w: 480, h: 140 }];
    // Just above the frame at rest size, over it while popping (1.35×).
    const i = f.spawn(1, 640, 578, 30, STYLE.perfect, 3, 1.6, 0.8, 0, -1, 0);
    expect(i).toBeGreaterThanOrEqual(0);
    // Drawn size at its pop: the glyph height is the font size × pop.
    const px = f.fontPx * f.size[i]! * popScale(f.tier[i]!, f.pop[i]!);
    expect(f.y[i]! + px / 2).toBeLessThanOrEqual(580);
    expect(f.box(i, { x: 0, y: 0, w: 0, h: 0 }).h).toBeCloseTo(px * 1.42, 6);
    expect(f.overlaps()).toBe(0);
  });

  it("reads the pop from the field's profile", () => {
    const flat = { ...SHIP, tiers: SHIP.tiers.map((row) => ({ ...row, number: row.number && { ...row.number, pop: 1 } })) };
    expect(popScale(3, 1, flat.tiers)).toBe(1);
    const f = new NumberField(flat);
    const i = f.spawn(1, 640, 300, 30, STYLE.perfect, 3, 1.6, 0.8, 0, -1, 0);
    expect(f.box(i, { x: 0, y: 0, w: 0, h: 0 }).h).toBeCloseTo(f.fontPx * 1.6 * 1.42, 4);
  });
});

describe("profiles", () => {
  it("rolls up inside the profile's windows", () => {
    const slow = new NumberField({ ...SHIP, numbers: { ...SHIP.numbers, mergeS: 0.4, tickMergeS: 0.8 } });
    const a = slow.spawn(1, 300, 300, 5, STYLE.normal, 1, 1, 2, 0, -1, 0);
    expect(slow.spawn(1, 300, 300, 5, STYLE.normal, 1, 1, 2, 0, -1, 0.35)).toBe(a);
    const t = slow.spawn(2, 600, 300, 2, STYLE.tick, 1, 1, 2, 0, -1, 0);
    expect(slow.spawn(2, 600, 300, 2, STYLE.tick, 1, 1, 2, 0, -1, 0.7)).toBe(t);
    expect(slow.text(t)).toBe("4×2");
    const ship = new NumberField(SHIP);
    const b = ship.spawn(1, 300, 300, 5, STYLE.normal, 1, 1, 2, 0, -1, 0);
    expect(ship.spawn(1, 300, 300, 5, STYLE.normal, 1, 1, 2, 0, -1, 0.35)).not.toBe(b);
  });

  it("takes a crowd's numbers in only inside the profile's crowdMergeS", () => {
    expect(SHIP.numbers.crowdMergeS).toBe(0.3);
    const never = new NumberField({ ...SHIP, numbers: { ...SHIP.numbers, crowdMergeS: -1 } });
    const a = never.spawn(1, 640, 300, 7, STYLE.normal, 1, 1, 0.45, 0, -1, 0);
    const b = never.spawn(2, 640, 300, 7, STYLE.normal, 1, 1, 0.45, 0, -1, 0.05);
    expect(b).not.toBe(a);
    expect(Math.abs(never.y[b]! - never.y[a]!)).toBeLessThan(never.fontPx);
    const ship = new NumberField(SHIP);
    const c = ship.spawn(1, 640, 300, 7, STYLE.normal, 1, 1, 0.45, 0, -1, 0);
    expect(ship.spawn(2, 640, 300, 7, STYLE.normal, 1, 1, 0.45, 0, -1, 0.05)).toBe(c);
  });

  it("dragon draws no gold numbers (gold is money): every colour is pale, the label white-teal", () => {
    const gold = (hex: string) => {
      const [r, g, b] = [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16)) as [number, number, number];
      return r > 200 && g > 150 && b < 120;
    };
    expect(SHIP.numbers.colors.some(gold)).toBe(true);
    expect(DRAGON.numbers.colors.some(gold)).toBe(false);
    expect(DRAGON.numbers.label).toBe("HOÀN HẢO");
  });
});

/**
 * The glyph atlas (dragon-hold review 2 minor 2): in 48 px cells the italic
 * digits with their 9 px outline overran into the next cell, so every glyph
 * 1–9 and × was drawn with 2–5 ink columns of the glyph before it, and the
 * label's accents (À, Ả) reached into the digit row, so a "3" carried bits of
 * "Ả" under it. Glyph metrics below are Chrome's for dragon-hold's fonts (Be
 * Vietnam Pro 800, the digits slanted: "italic 800 52px"; the label 800
 * 40 px), measured on the Dell (Windows Chrome 155, textAlign centre).
 */
describe("the glyph atlas", () => {
  const DIGIT: Record<string, GlyphMetrics> = {
    "0": { width: 36.8, actualBoundingBoxLeft: 13.4, actualBoundingBoxRight: 23.6 },
    "1": { width: 23.2, actualBoundingBoxLeft: 3.6, actualBoundingBoxRight: 17.4 },
    "2": { width: 34.8, actualBoundingBoxLeft: 15.4, actualBoundingBoxRight: 22.6 },
    "3": { width: 35.7, actualBoundingBoxLeft: 12.9, actualBoundingBoxRight: 22.1 },
    "4": { width: 37.6, actualBoundingBoxLeft: 15.8, actualBoundingBoxRight: 21.2 },
    "5": { width: 35.8, actualBoundingBoxLeft: 12.9, actualBoundingBoxRight: 23.1 },
    "6": { width: 36.7, actualBoundingBoxLeft: 13.4, actualBoundingBoxRight: 21.6 },
    "7": { width: 31.1, actualBoundingBoxLeft: 8.6, actualBoundingBoxRight: 24.4 },
    "8": { width: 35.3, actualBoundingBoxLeft: 13.7, actualBoundingBoxRight: 22.3 },
    "9": { width: 36.7, actualBoundingBoxLeft: 12.4, actualBoundingBoxRight: 22.6 },
    "×": { width: 33.5, actualBoundingBoxLeft: 8.8, actualBoundingBoxRight: 17.2 },
  };
  const LABEL = { width: 225.7, actualBoundingBoxLeft: 110.8, actualBoundingBoxRight: 112.7, actualBoundingBoxAscent: 30.4, actualBoundingBoxDescent: 11.6 };
  const A = NUMBER_ATLAS;
  /** A glyph's ink span across the atlas when painted centred at x (outline included). */
  const ink = (m: GlyphMetrics, x: number) => [x - m.actualBoundingBoxLeft! - A.digitOutline / 2, x + m.actualBoundingBoxRight! + A.digitOutline / 2] as const;

  it("gives every glyph a cell its ink fits in, with room at both edges (48 px cells did not)", () => {
    const cell = digitCellWidth((glyph) => DIGIT[glyph]!);
    expect(cell).toBeGreaterThanOrEqual(A.minCellW);
    expect(cell * A.glyphs.length).toBeLessThanOrEqual(A.width);
    let overranOld = 0;
    [...A.glyphs].forEach((glyph, index) => {
      const [left, right] = ink(DIGIT[glyph]!, index * cell + cell / 2);
      expect(left).toBeGreaterThanOrEqual(index * cell + A.edgePx);
      expect(right).toBeLessThanOrEqual((index + 1) * cell - A.edgePx);
      const [oldLeft, oldRight] = ink(DIGIT[glyph]!, index * 48 + 24);
      if (oldLeft < index * 48 || oldRight > (index + 1) * 48) overranOld += 1;
    });
    // The old layout: most glyphs reached into a neighbour's cell.
    expect(overranOld).toBeGreaterThanOrEqual(8);
  });

  it("widens the cells for a wider font, never past the atlas, and without a measured box still leaves room", () => {
    const wide = digitCellWidth(() => ({ width: 40, actualBoundingBoxLeft: 30, actualBoundingBoxRight: 34 }));
    expect(wide).toBe(2 * Math.ceil(34 + A.digitOutline / 2 + A.edgePx));
    expect(digitCellWidth(() => ({ width: 90, actualBoundingBoxLeft: 80, actualBoundingBoxRight: 80 }))).toBe(92);
    const blind = digitCellWidth(() => ({ width: 33.4 }));
    expect(blind / 2).toBeGreaterThanOrEqual(33.4 / 2 + A.digitOutline / 2 + A.edgePx);
  });

  type Paint = { text: string; x: number; y: number; font: string };
  const originalDocument = (globalThis as { document?: unknown }).document;
  afterEach(() => {
    (globalThis as { document?: unknown }).document = originalDocument;
  });
  /** A canvas whose 2D context measures with the metrics above and records what is painted. */
  const fakeCanvas = () => {
    const painted: Paint[] = [];
    const context = {
      font: "",
      textAlign: "start",
      textBaseline: "alphabetic",
      lineJoin: "miter",
      lineWidth: 1,
      strokeStyle: "",
      fillStyle: "",
      measureText(text: string) {
        return this.font.startsWith("italic") ? DIGIT[text]! : LABEL;
      },
      strokeText() {},
      fillText(text: string, x: number, y: number) {
        painted.push({ text, x, y, font: this.font });
      },
    };
    const canvas = { width: 0, height: 0, getContext: () => context };
    (globalThis as { document?: unknown }).document = { createElement: () => canvas };
    return { canvas, painted };
  };

  it("paints each digit in the middle of its own cell and the label in its own row, below the digits' reach", () => {
    const { canvas, painted } = fakeCanvas();
    const sprites = new NumberSprites(DRAGON);
    expect([canvas.width, canvas.height]).toEqual([A.width, A.height]);
    const cell = sprites.cellWidth;
    expect(cell).toBe(digitCellWidth((glyph) => DIGIT[glyph]!));
    const digits = painted.filter((p) => p.font === A.digitFont);
    expect(digits.map((p) => p.text).join("")).toBe(A.glyphs);
    digits.forEach((p, index) => expect([p.x, p.y]).toEqual([index * cell + cell / 2, A.digitMidY]));
    const label = painted.find((p) => p.text === "HOÀN HẢO")!;
    expect(label.font).toBe(A.labelFont);
    expect(label.y).toBe(A.labelTop + A.labelRowH / 2);
    // The accents' top (ascent + outline) stays inside the label row, and the row starts below the digit row.
    expect(label.y - LABEL.actualBoundingBoxAscent - A.labelOutline / 2).toBeGreaterThan(A.labelTop + A.edgePx);
    expect(label.y + LABEL.actualBoundingBoxDescent + A.labelOutline / 2).toBeLessThan(A.labelTop + A.labelRowH - A.edgePx);
    expect(A.labelTop).toBeGreaterThanOrEqual(2 * A.cellH);
    // The old atlas put the label's middle at 96: its accents reached row 57, inside the 64 digit rows.
    expect(96 - LABEL.actualBoundingBoxAscent - A.labelOutline / 2).toBeLessThan(A.cellH);
  });

  it("draws the glyphs at the scale and place they always had: only the quads grew round them", () => {
    fakeCanvas();
    const sprites = new NumberSprites(DRAGON);
    const cell = sprites.cellWidth;
    const field = new NumberField(DRAGON);
    field.fontPx = 20;
    const i = field.spawn(1, 640, 300, 120, STYLE.perfect, 3, 1.6, 1, 0, -1, 0);
    sprites.write(field, 1280, 720);
    const { rect, uv } = sprites as unknown as { rect: Float32Array; uv: Float32Array };
    const px = field.fontPx * field.size[i]! * popScale(field.tier[i]!, field.pop[i]!, DRAGON.tiers);
    const advance = A.advance * px;
    const top = field.y[i]! - px / 2;
    const text = field.text(i);
    expect(text).toBe("120");
    for (let c = 0; c < text.length; c += 1) {
      const o = c * 4;
      const g = A.glyphs.indexOf(text[c]!);
      // One whole cell of the digit row, nothing of its neighbours or the label row.
      expect(uv[o]! * A.width).toBeCloseTo(g * cell, 3);
      expect(uv[o + 2]! * A.width).toBeCloseTo((g + 1) * cell, 3);
      expect([uv[o + 1], uv[o + 3]! * A.height]).toEqual([0, A.cellH]);
      // Screen px per atlas px as before (1.4 advances per 48 columns, 1.25 font sizes per 64 rows); the glyph's middle on its advance.
      expect(rect[o + 2]! / cell).toBeCloseTo((advance * 1.4) / 48, 6);
      expect(rect[o + 3]! / A.cellH).toBeCloseTo((px * 1.25) / 64, 6);
      expect(rect[o]! + rect[o + 2]! / 2).toBeCloseTo(field.x[i]! - (text.length * advance) / 2 + (c + 0.5) * advance, 4);
      expect(rect[o + 1]).toBeCloseTo(top, 4);
    }
    // The label: its own row, its middle 0.4 label heights above the digits' top, 1.3 label heights per 64 rows.
    const o = text.length * 4;
    const lh = px * A.label;
    expect([uv[o + 1]! * A.height, uv[o + 3]! * A.height]).toEqual([A.labelTop, A.labelTop + A.labelRowH]);
    expect(rect[o + 3]! / A.labelRowH).toBeCloseTo((lh * 1.3) / 64, 6);
    expect(rect[o + 1]! + rect[o + 3]! / 2).toBeCloseTo(top - 0.4 * lh, 4);
  });
});
