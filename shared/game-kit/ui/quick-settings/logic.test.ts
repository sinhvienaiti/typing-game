import { afterEach, describe, expect, it, vi } from "vitest";
import { QUICK_SETTINGS_COLORS, QUICK_SETTINGS_CSS, cssUrl } from "./css";
import { createKeyedThrottle, isQuickMuted, quickScale, readChoice, readRowValues, readSlider, routeQuickKey, startCountdown } from "./logic";
import { DEFAULT_KEYBOARD_PROFILES, defaultSettingsRows, defaultSoundRows } from "./rows";
import type { QuickChoiceRow, QuickRow, QuickSliderRow } from "./types";

function luminance(hex: string): number {
  const [r, g, b] = [1, 3, 5]
    .map((start) => parseInt(hex.slice(start, start + 2), 16) / 255)
    .map((value) => (value <= 0.03928 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4)) as [number, number, number];
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

function contrast(a: string, b: string): number {
  const [hi, lo] = [luminance(a), luminance(b)].sort((x, y) => y - x) as [number, number];
  return (hi + 0.05) / (lo + 0.05);
}

const closed = { panel: null, blocking: false } as const;
const open = { panel: "settings", blocking: true } as const;
const counting = { panel: null, blocking: true } as const;
const key = (k: string, extra: { type?: string; repeat?: boolean; inside?: boolean } = {}) => ({ type: "keydown", key: k, repeat: false, inside: false, ...extra });

describe("quick settings key routing", () => {
  it("opens with F1/F2 only on a fresh keydown, and always keeps them from the browser", () => {
    expect(routeQuickKey(closed, key("F1"))).toEqual({ swallow: true, command: { toggle: "settings" } });
    expect(routeQuickKey(closed, key("F2"))).toEqual({ swallow: true, command: { toggle: "sound" } });
    expect(routeQuickKey(open, key("F2"))).toEqual({ swallow: true, command: { toggle: "sound" } });
    expect(routeQuickKey(closed, key("F1", { repeat: true }))).toEqual({ swallow: true, command: null });
    expect(routeQuickKey(closed, key("F1", { type: "keyup" }))).toEqual({ swallow: true, command: null });
  });

  it("never opens a panel from a letter, digit or Enter", () => {
    for (const k of ["s", "S", "o", "1", "Enter", " ", "Tab", "Backspace"]) {
      expect(routeQuickKey(closed, key(k))).toEqual({ swallow: false, command: null });
    }
  });

  it("closes with Esc when open, swallows it during the countdown and leaves it to the game otherwise", () => {
    expect(routeQuickKey(open, key("Escape"))).toEqual({ swallow: true, command: "close" });
    expect(routeQuickKey(open, key("Escape", { type: "keyup" }))).toEqual({ swallow: true, command: null });
    expect(routeQuickKey(counting, key("Escape"))).toEqual({ swallow: true, command: null });
    expect(routeQuickKey(closed, key("Escape"))).toEqual({ swallow: false, command: null });
  });

  it("swallows keys outside the panel while blocking and lets keys inside reach the controls", () => {
    for (const state of [open, counting]) {
      for (const type of ["keydown", "keypress", "keyup"]) {
        expect(routeQuickKey(state, key("a", { type }))).toEqual({ swallow: true, command: null });
        expect(routeQuickKey(state, key("ArrowRight", { type, inside: true }))).toEqual({ swallow: false, command: null });
      }
    }
  });
});

describe("resume countdown", () => {
  afterEach(() => vi.useRealTimers());

  it("shows 3, 2, 1 one step apart, then finishes", () => {
    vi.useFakeTimers();
    const steps: number[] = [];
    const done = vi.fn();
    startCountdown(3, 500, (left) => steps.push(left), done);
    expect(steps).toEqual([3]);
    vi.advanceTimersByTime(499);
    expect(steps).toEqual([3]);
    vi.advanceTimersByTime(1);
    expect(steps).toEqual([3, 2]);
    vi.advanceTimersByTime(500);
    expect(steps).toEqual([3, 2, 1]);
    expect(done).not.toHaveBeenCalled();
    vi.advanceTimersByTime(500);
    expect(done).toHaveBeenCalledTimes(1);
  });

  it("never finishes after cancel, and finishes at once with no time", () => {
    vi.useFakeTimers();
    const done = vi.fn();
    const cancel = startCountdown(3, 500, () => {}, done);
    vi.advanceTimersByTime(700);
    cancel();
    vi.advanceTimersByTime(5000);
    expect(done).not.toHaveBeenCalled();
    startCountdown(3, 0, () => {}, done);
    expect(done).toHaveBeenCalledTimes(1);
  });
});

describe("preview throttle", () => {
  afterEach(() => vi.useRealTimers());

  it("runs the first call at once, one trailing call per window, and keys apart", () => {
    vi.useFakeTimers();
    const run = vi.fn();
    const throttle = createKeyedThrottle(run, 150);
    for (let i = 0; i < 10; i += 1) throttle.call("music");
    throttle.call("voice");
    expect(run.mock.calls).toEqual([["music"], ["voice"]]);
    vi.advanceTimersByTime(150);
    expect(run.mock.calls).toEqual([["music"], ["voice"], ["music"]]);
    vi.advanceTimersByTime(150);
    expect(run).toHaveBeenCalledTimes(3);
    throttle.call("music");
    expect(run).toHaveBeenCalledTimes(4);
    throttle.call("music");
    throttle.cancel();
    vi.advanceTimersByTime(1000);
    expect(run).toHaveBeenCalledTimes(4);
  });
});

describe("value checks", () => {
  const slider: QuickSliderRow = { kind: "slider", id: "music", label: "Music" };
  const choice: QuickChoiceRow = {
    kind: "choice",
    id: "keyboard",
    label: "Keyboard sound",
    default: "creamy",
    options: [
      { value: "off", label: "Off" },
      { value: "creamy", label: "Creamy" },
      { value: "thock", label: "Thock", disabled: true, note: "pending" },
    ],
  };

  it("clamps and snaps slider values, and falls back to the default", () => {
    expect(readSlider(slider, 42.4)).toBe(42);
    expect(readSlider(slider, 150)).toBe(100);
    expect(readSlider(slider, -3)).toBe(0);
    expect(readSlider(slider, "70")).toBe(0);
    expect(readSlider({ ...slider, default: 80 }, Number.NaN)).toBe(80);
    expect(readSlider({ ...slider, min: 0, max: 1, step: 0.05 }, 0.333)).toBe(0.35);
  });

  it("keeps a known choice (a disabled one too), else the default", () => {
    expect(readChoice(choice, "off")).toBe("off");
    expect(readChoice(choice, "thock")).toBe("thock");
    expect(readChoice(choice, "laser")).toBe("creamy");
    expect(readChoice({ ...choice, default: undefined }, 7)).toBe("off");
  });

  it("reads every row's value, the mute flag included", () => {
    const values = readRowValues(defaultSoundRows(), { master: 0, muted: "yes", music: 55, keyboard: "marbly" });
    expect(values).toMatchObject({ master: 0, muted: false, music: 55, effects: 0, keyboard: "marbly" });
  });

  it("shows the muted icon for mute or a zero master", () => {
    expect(isQuickMuted({ master: 80, muted: false })).toBe(false);
    expect(isQuickMuted({ master: 80, muted: true })).toBe(true);
    expect(isQuickMuted({ master: 0, muted: false })).toBe(true);
    expect(isQuickMuted({})).toBe(false);
  });

  it("sizes buttons 32 px at 720 and up to 48 px at 1080", () => {
    expect(32 * quickScale(720)).toBe(32);
    expect(32 * quickScale(1080)).toBe(48);
    expect(32 * quickScale(2160)).toBe(48);
    expect(32 * quickScale(500)).toBe(32);
    expect(quickScale(0)).toBe(1);
  });
});

describe("default rows", () => {
  const ids = (rows: readonly QuickRow[]) => rows.map((row) => row.id);

  it("lists the sound rows in the spec's order", () => {
    const rows = defaultSoundRows();
    expect(ids(rows)).toEqual(["master", "music", "effects", "keyboard", "keyboardVolume", "voice", "ui"]);
    expect(rows.map((row) => ("label" in row ? row.label : ""))).toEqual(["Master", "Music", "Effects", "Keyboard sound", "Keyboard volume", "Voice", "Interface"]);
    expect(rows[0]).toMatchObject({ kind: "slider", toggle: { id: "muted" } });
    expect(rows[3]).toMatchObject({ kind: "choice", preview: "keyboard" });
    expect(DEFAULT_KEYBOARD_PROFILES.map((option) => option.value)).toEqual(["off", "creamy", "thock", "marbly", "clack", "dome"]);
    expect(DEFAULT_KEYBOARD_PROFILES.map((option) => option.label)).toEqual(["Off", "Creamy Linear", "Deep Thock", "Marbly", "Clean Clack", "Soft Dome"]);
  });

  it("takes the game's keyboard list with pending packs", () => {
    const profiles = [{ value: "creamy", label: "Creamy" }, { value: "thock", label: "Thock", disabled: true, note: "pending" }];
    expect(defaultSoundRows({ keyboardProfiles: profiles })[3]).toMatchObject({ options: profiles });
  });

  it("lists the settings rows in the spec's order", () => {
    expect(ids(defaultSettingsRows())).toEqual(["typingHeading", "fxStyle", "fxIntensity", "fxSize", "graphicsHeading", "quality", "reducedMotion", "resume", "quit"]);
    const mount = () => {};
    const full = defaultSettingsRows({
      mountPreview: mount,
      learning: { meaning: true, ipa: true },
      gameRows: [{ kind: "toggle", id: "hints", label: "Hints" }],
      mountGameItems: mount,
    });
    expect(ids(full)).toEqual([
      "typingHeading", "fxStyle", "fxIntensity", "fxSize", "fxPreview",
      "graphicsHeading", "quality", "reducedMotion",
      "learningHeading", "learnMeaning", "learnIpa",
      "gameHeading", "hints", "gameItems",
      "resume", "quit",
    ]);
    expect(ids(defaultSettingsRows({ learning: { ipa: true } }))).toContain("learnIpa");
    expect(ids(defaultSettingsRows({ learning: { ipa: true } }))).not.toContain("learnMeaning");
    const style = full[1] as QuickChoiceRow;
    expect(style.options.map((option) => option.label)).toEqual(["Stamp", "Flare", "Smash", "Shatter", "Rune", "Minimal"]);
    expect(style.default).toBe("stamp");
    expect((full[2] as QuickChoiceRow).options.map((option) => option.label)).toEqual(["Off", "Low", "Normal", "High", "Ultra"]);
    expect((full[3] as QuickChoiceRow).options.map((option) => option.label)).toEqual(["Medium", "Large", "Huge"]);
    expect((full[6] as QuickChoiceRow).options.map((option) => option.label)).toEqual(["Low", "Medium", "High", "Ultra"]);
    expect(full.slice(-2).map((row) => row.label)).toEqual(["Resume", "Quit to title"]);
  });
});

describe("panel look", () => {
  it("keeps every panel text pair at WCAG AAA (≥ 7:1)", () => {
    const c = QUICK_SETTINGS_COLORS;
    const pairs: [string, string][] = [
      [c["--kit-qs-text"], c["--kit-qs-bg"]],
      [c["--kit-qs-muted"], c["--kit-qs-bg"]],
      [c["--kit-qs-text"], c["--kit-qs-control"]],
      [c["--kit-qs-muted"], c["--kit-qs-control"]],
      [c["--kit-qs-accent-text"], c["--kit-qs-accent"]],
    ];
    for (const [text, background] of pairs) expect(contrast(text, background), `${text} on ${background}`).toBeGreaterThanOrEqual(7);
    expect(contrast(c["--kit-qs-text"], c["--kit-qs-bg"])).toBeCloseTo(16.45, 1);
  });

  it("defines the colours as variables, hides closed panels and draws no ornaments", () => {
    for (const name of Object.keys(QUICK_SETTINGS_COLORS)) expect(QUICK_SETTINGS_CSS).toContain(`${name}:`);
    expect(QUICK_SETTINGS_CSS).toContain('.kit-qs__dialog[aria-hidden="true"]{display:none!important}');
    expect(QUICK_SETTINGS_CSS).toContain("prefers-reduced-motion");
    expect(QUICK_SETTINGS_CSS).not.toMatch(/<svg|content:\s*"[^"]/);
    expect(cssUrl('a"b\\c.png')).toBe('url("a\\"b\\\\c.png")');
  });
});
