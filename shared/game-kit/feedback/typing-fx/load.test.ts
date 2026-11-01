// @vitest-environment happy-dom
// Source: new for the kit: the focus strip's Load host mode (Last Line's ALIVE_PLAN AL-05)
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import {
  flawAt, flightAt, glassShine, landFlash, learnAt, LEARN_HOLD, LOAD, LOAD_KEY, loadBackPose, loadTier, loadWrongBeat, loadWrongPose, lockScale, plateAfterWord, releaseFold, strayAt, sweepAt, wordSqueeze, type LoadHost,
} from "./load";
import { ParticlePool, PK } from "./pool";
import { FRAME_MS, newPose, type SpawnCtx } from "./styles";
import { FocusStrip } from "./strip";

const F = FRAME_MS;
/** The middle of 60 Hz frame `f` (ms). */
const at = (f: number): number => f * F + 1;

const ctx = (pool: ParticlePool, extra: Partial<SpawnCtx> = {}): SpawnCtx => {
  let seed = 7;
  return { pool, owner: 1, prio: 1, x: 300, y: 120, h: 56, glyph: 0, now: 1000, mult: 1, size: 1, still: false, random: () => ((seed = (seed * 16807) % 2147483647) / 2147483647), light: () => {}, key: 0, tier: 0, ...extra };
};

describe("Load: the numbers (E1–E3)", () => {
  it("a key's letter is 2.6× on its own frame, at 1× from f1, at rest by f9 (150 ms)", () => {
    const out = newPose();
    const f0 = LOAD_KEY.keyPose(at(0), 1, out);
    expect(f0.aOn).toBe(true);
    expect(f0.aScale).toBeCloseTo(2.6);
    expect(f0.alpha).toBe(0);
    const f1 = LOAD_KEY.keyPose(at(1), 1, out);
    expect(f1.aOn).toBe(false);
    expect(f1.scale).toBe(1);
    expect(f1.hot).toBe(1);
    expect(LOAD_KEY.keyMs).toBe(150);
    const rest = LOAD_KEY.keyPose(150, 1, out);
    expect(rest.hot + Math.abs(rest.squash) + (rest.aOn ? 1 : 0)).toBe(0);
    // Reduced motion: light only, no copy, no squash.
    const still = LOAD_KEY.keyPose(at(0), 0, out);
    expect(still.aOn).toBe(false);
    expect(still.hot).toBe(1);
    expect(LOAD_KEY.keyPose(at(2), 0, out).squash).toBe(0);
  });

  it("a key spawns one stepped mark at f0 and 2–4 dark crystal shards at f3, more with the clean streak", () => {
    const pool = new ParticlePool(64);
    const c = ctx(pool);
    LOAD_KEY.spawnKey(0, c);
    expect(pool.count).toBe(1);
    expect(pool.kind[0]).toBe(PK.loadKey);
    expect(pool.life[0]).toBe(150);
    LOAD_KEY.spawnKey(1, c);
    expect(pool.count - 1).toBe(2);
    const hot = new ParticlePool(64);
    const t4 = ctx(hot, { tier: 4 });
    LOAD_KEY.spawnKey(0, t4);
    LOAD_KEY.spawnKey(1, t4);
    expect(hot.count - 1).toBe(4);
    // Tier 4 shifts the hue to glass.
    expect(hot.tone[0]).toBe(9);
    expect(LOAD_KEY.phases).toEqual([0, 3 * F]);
    // Low and Off spawn nothing.
    const off = new ParticlePool(64);
    LOAD_KEY.spawnKey(0, ctx(off, { mult: 0 }));
    LOAD_KEY.spawnKey(1, ctx(off, { mult: 0 }));
    expect(off.count).toBe(0);
  });

  it("the streak's tiers start at 3, 6, 10 and 20 clean words", () => {
    expect([0, 2, 3, 5, 6, 9, 10, 19, 20, 99].map(loadTier)).toEqual([0, 0, 1, 1, 2, 2, 3, 3, 4, 4]);
  });

  it("a wrong key twitches +3, −3, +2, 0 px at 720p in steps, never scales; a crimson line, a cracked copy, its shards at f9", () => {
    const out = newPose();
    const dx = [0, 1, 2, 3, 4].map((f) => loadWrongPose(at(f), 1, out).dx);
    expect(dx).toEqual([0.053, -0.053, 0.035, 0, 0]);
    expect(loadWrongPose(at(0), 1, out).scale).toBe(1);
    const pool = new ParticlePool(64);
    loadWrongBeat(ctx(pool, { key: "q".charCodeAt(0) }));
    const kinds = Array.from(pool.kind.subarray(0, pool.count));
    expect(kinds.filter((k) => k === PK.bar)).toHaveLength(1);
    expect(kinds.filter((k) => k === PK.crackGlyph)).toHaveLength(1);
    const shards = kinds.map((k, i) => (k === PK.crystal ? i : -1)).filter((i) => i >= 0);
    expect(shards.length).toBeGreaterThanOrEqual(2);
    expect(shards.length).toBeLessThanOrEqual(3);
    // The shards wait for the copy's end (f9).
    for (const i of shards) expect(pool.born[i]).toBeCloseTo(1000 + LOAD.wrong.crack * F);
    // The line lasts f0–5.
    expect(pool.life[kinds.indexOf(PK.bar)]).toBeCloseTo(6 * F);
  });

  it("a finished word squeezes f1–2, flies f3–12, the plate dims 70 % from f1 and folds f3–9", () => {
    expect(flightAt(at(2))).toBe(-1);
    expect(flightAt(3 * F)).toBeCloseTo(0, 2);
    expect(flightAt(12 * F)).toBe(1);
    expect(flightAt(at(7))).toBeGreaterThan(0.2);
    expect(flightAt(at(7))).toBeLessThan(0.6);
    expect([0, 1, 2, 3, 4].map((f) => wordSqueeze(at(f)))).toEqual([1, 0.86, 0.72, 0, 0]);
    // The line takes over at f3 at the squeezed word's width.
    expect(LOAD.word.line[0]).toBe(LOAD.word.squeeze.at(-1));
    expect(plateAfterWord(at(0))).toEqual({ alpha: 1, fold: 1 });
    expect(plateAfterWord(at(1)).alpha).toBeCloseTo(0.3);
    expect(plateAfterWord(at(6)).fold).toBeLessThan(1);
    expect(plateAfterWord(9 * F + 1).alpha).toBe(0);
  });

  it("the cell flashes white on its landing frame (≥ 95 % of the peak) and is gone by f8", () => {
    expect(landFlash(0).alpha).toBe(1);
    expect(landFlash(0).scale).toBe(1.25);
    expect(landFlash(at(3)).alpha).toBeLessThan(1);
    expect(landFlash(8 * F).alpha).toBe(0);
    expect(landFlash(-1).alpha).toBe(0);
  });

  it("the meaning gets its own beat: from f12, rising 8 px at 720p in 8 f, fully readable ≥ 600 ms, out in 8 f", () => {
    expect(learnAt(at(11)).alpha).toBe(0);
    expect(learnAt(12 * F).alpha).toBe(0);
    expect(learnAt(at(16)).alpha).toBeGreaterThan(0.4);
    expect(learnAt(at(16)).rise).toBeGreaterThan(0);
    expect(LEARN_HOLD).toBeGreaterThanOrEqual(600);
    const start = 20 * F;
    expect(learnAt(start + 1).alpha).toBe(1);
    expect(learnAt(start + 600).alpha).toBe(1);
    expect(learnAt(start + LEARN_HOLD + 8 * F + 1).alpha).toBe(0);
    // 0.14 of a 57 px font is 8 px.
    expect(LOAD.learn.rise * 57).toBeCloseTo(8, 0);
  });

  it("FLAWLESS steps in (1.35 → 1.12 → 1), holds to f8, is gone by f12 when the meaning comes", () => {
    expect([0, 1, 2, 5].map((f) => flawAt(at(f)).scale)).toEqual([1.35, 1.12, 1, 1]);
    expect(flawAt(at(7)).alpha).toBe(1);
    expect(flawAt(12 * F).alpha).toBe(0);
  });

  it("the plate locks 0.9 → 1.04 → 1 in f0–6, its top edge lights f2–12", () => {
    expect([0, 3, 6, 9].map((f) => lockScale(at(f)))).toEqual([0.9, 1.04, 1, 1]);
    expect(sweepAt(at(1))).toBe(-1);
    expect(sweepAt(2 * F)).toBe(0);
    expect(sweepAt(at(12))).toBe(-1);
  });

  it("a stray ghost is 1.4× on its frame, drops 20 px at 720p in 15 f; reduced motion keeps it still", () => {
    expect(strayAt(0, false).scale).toBe(1.4);
    expect(strayAt(at(14), false).drop * 57).toBeGreaterThan(15);
    expect(strayAt(15 * F, false).alpha).toBe(0);
    expect(strayAt(at(5), true)).toMatchObject({ scale: 1, drop: 0 });
  });

  it("backspace's letter shrinks to 0.6 and fades in 4 f; a release folds in 8 f", () => {
    const out = newPose();
    expect(loadBackPose(0, 1, out).aAlpha).toBe(1);
    expect(loadBackPose(at(3), 1, out).aScale).toBeLessThan(0.75);
    expect(loadBackPose(4 * F, 1, out).aOn).toBe(false);
    expect(releaseFold(0)).toBe(1);
    expect(releaseFold(8 * F)).toBe(0);
  });

  it("hidden letters shimmer on a 2.4 s cycle, each letter behind the one before", () => {
    expect(glassShine(0, 0)).toBeCloseTo(glassShine(2400, 0));
    expect(glassShine(0, 0)).not.toBeCloseTo(glassShine(0, 1));
  });
});

// ── The strip in Load mode (a stubbed 2D canvas: happy-dom has none) ─────────

const noop = (): void => {};
const gradient = { addColorStop: noop };
const fakeContext = new Proxy({}, { get: (_, key) => (key === "measureText" ? () => ({ actualBoundingBoxAscent: 70, width: 30 }) : key === "createRadialGradient" || key === "createLinearGradient" ? () => gradient : key === "canvas" ? undefined : noop), set: () => true });

describe("Load: the strip", () => {
  let root: HTMLDivElement;
  let time = 0;
  beforeEach(() => {
    vi.spyOn(HTMLCanvasElement.prototype, "getContext").mockImplementation((() => fakeContext) as unknown as typeof HTMLCanvasElement.prototype.getContext);
    root = document.createElement("div");
    document.body.append(root);
    time = 1000;
  });
  afterEach(() => {
    root.remove();
    vi.restoreAllMocks();
  });

  const make = (load?: LoadHost, style: "stamp" | "flare" = "stamp") =>
    new FocusStrip({ root, autoTick: false, reducedMotion: false, clock: () => time, settings: { style, intensity: "normal" }, load, random: () => 0.5 });

  const typeWord = (strip: FocusStrip, word: string, perfect = true): void => {
    strip.setWord(word, "cảm ơn", 0, time, 0);
    for (let i = 0; i < word.length; i += 1) {
      strip.key(i, time);
      time += 100;
      strip.update(time);
    }
    strip.complete(perfect, 3, time);
  };

  it("leaves every other game as it was: no Load class, its own styles, no Load elements", () => {
    const strip = make();
    expect(strip.el.className).not.toContain("tfx--host-load");
    expect(strip.el.className).toContain("tfx--stamp");
    expect(root.querySelector(".tfx-learn")).toBeNull();
    expect(root.querySelector(".tfx-line")).toBeNull();
    strip.dispose();
  });

  it("plays Load's key for the default Stamp, keeps another style's own key", () => {
    const target = vi.fn(() => false);
    const loadStrip = make({ target });
    expect(loadStrip.el.className).toContain("tfx--host-load");
    expect(loadStrip.el.className).toContain("tfx--load");
    loadStrip.dispose();
    const flare = make({ target }, "flare");
    expect(flare.el.className).toContain("tfx--flare");
    expect(flare.el.className).toContain("tfx--host-load");
    flare.dispose();
  });

  it("flies a finished word into the target and lands on f12 once; a flawless word stamps FLAWLESS, never gold", () => {
    const onLand = vi.fn();
    const strip = make({ target: (out) => ((out.x = 40), (out.y = 200), (out.w = 30), (out.h = 18), true), onLand });
    typeWord(strip, "thank");
    const done = time;
    const flaw = root.querySelector<HTMLElement>(".tfx-flaw")!;
    strip.update(done);
    expect(Number(flaw.style.opacity)).toBe(1);
    expect(flaw.textContent).toBe("FLAWLESS");
    expect(root.querySelector(".tfx-rim")!.classList.contains("is-gold")).toBe(false);
    expect(root.querySelector(".tfx-rim")!.classList.contains("is-crystal")).toBe(true);
    for (let f = 1; f <= 11; f += 1) strip.update(done + f * F);
    expect(onLand).not.toHaveBeenCalled();
    const line = root.querySelector<HTMLElement>(".tfx-line")!;
    expect(line.style.display).toBe("block");
    expect(root.querySelectorAll(".tfx-rib.is-thread").length).toBeGreaterThan(0);
    strip.update(done + 12 * F + 1);
    expect(onLand).toHaveBeenCalledTimes(1);
    strip.update(done + 13 * F);
    expect(onLand).toHaveBeenCalledTimes(1);
    expect(root.querySelector<HTMLElement>(".tfx-land")!.style.display).toBe("block");
    // The meaning's beat: the word and its meaning, full by f20, still there 600 ms later.
    const learn = root.querySelector<HTMLElement>(".tfx-learn")!;
    expect(learn.textContent).toBe("thankcảm ơn");
    strip.update(done + 21 * F);
    expect(Number(learn.style.opacity)).toBe(1);
    strip.update(done + 21 * F + 600);
    expect(Number(learn.style.opacity)).toBe(1);
    expect(strip.stats.flyers).toBe(1);
    strip.dispose();
  });

  it("a full bay (no target): the word rises and fades, nothing lands", () => {
    const onLand = vi.fn();
    const strip = make({ target: () => false, onLand });
    typeWord(strip, "fate");
    const done = time;
    for (let f = 0; f <= 20; f += 1) strip.update(done + f * F);
    expect(onLand).not.toHaveBeenCalled();
    strip.dispose();
  });

  it("a stray key shows its ghost; a wrong key never flashes the plate red", () => {
    const strip = make({ target: () => false });
    strip.stray(time, "z");
    strip.update(time);
    const ghost = root.querySelector<HTMLElement>(".tfx-stray")!;
    expect(ghost.textContent).toBe("z");
    expect(Number(ghost.style.opacity)).toBe(1);
    strip.setWord("fate", "số phận", 1, time, 0);
    strip.wrong(1, time, "q");
    strip.update(time);
    expect(root.querySelector<HTMLElement>(".tfx-warn")!.style.opacity).toBe("0");
    strip.dispose();
  });

  it("hidden letters: glass tiles when the host has the art, a wrong key reveals one as a pale hint", () => {
    const strip = make({ target: () => false, glass: true });
    strip.setWord("glass", "kính", 0, time, 0b00110);
    const g = root.querySelectorAll<HTMLElement>(".tfx-layer.is-on .tfx-g");
    expect(g[1]!.classList.contains("is-masked")).toBe(true);
    expect(g[1]!.textContent).not.toContain("_");
    strip.mask(0b00100, time);
    expect(g[1]!.classList.contains("is-masked")).toBe(false);
    expect(g[1]!.classList.contains("is-hint")).toBe(true);
    strip.key(0, time);
    strip.key(1, time);
    expect(g[1]!.classList.contains("is-hint")).toBe(false);
    strip.dispose();
    // Without the art: "_" as before.
    const plain = make({ target: () => false });
    plain.setWord("glass", "kính", 0, time, 0b00010);
    expect(root.querySelector(".tfx-layer.is-on .tfx-g:nth-child(2)")!.textContent).toContain("_");
    plain.dispose();
  });
});
