// @vitest-environment happy-dom
// Source: new for the kit: the Sound panel's keyboard row against Typing Feel (docs/games/TYPING_FEEL_SERVICE.md §4.6, §5.1–5.3):
// game fetchers and load/fail hooks through QuickSettings, a rebuild that is not the player's, readable selected states, timedBytes.
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import {
  KEYBOARD_DECODE_BATCH_SIZE, KEYBOARD_SAMPLE_TIMEOUT_MS, KeyboardSoundPreview, settleKeyboardChoice, timedBytes, timedJson, TypingSounds,
  type KeyboardSoundChoice,
} from "../../feedback/typing-fx/audio";
import * as fxIndex from "../../feedback/typing-fx/index";
import { QUICK_SETTINGS_COLORS, QUICK_SETTINGS_CSS } from "./css";
import * as quickIndex from "./index";
import { KEYBOARD_CHOICES_CSS, KeyboardSoundChoices } from "./keyboard-choices";
import { QuickSettings, type QuickSettingsOptions } from "./quick-settings";
import type { QuickValue } from "./types";

const OFF: KeyboardSoundChoice = { value: "off", label: "Off" };
const RELAY: KeyboardSoundChoice = { value: "relay", label: "Relay" };
const set = (id: string): KeyboardSoundChoice => ({ value: id, label: id.toUpperCase(), family: "Feel", manifest: `/v1/keys/sets/${id}/f/keys-manifest.json`, preview: `/v1/keys/sets/${id}/f/preview.ogg` });
const DEEP = set("deep");
const WARM = set("warm");
const CLEAR = set("clear");
const FIRST = [OFF, RELAY, DEEP, WARM];
const SECOND = [OFF, RELAY, DEEP, WARM, CLEAR];
const FILES = { files: ["key-01.ogg", "key-02.ogg", "space-01.ogg"] };

class Param {
  value = 1;
  cancelScheduledValues = vi.fn();
  setValueAtTime(value: number): void { this.value = value; }
  linearRampToValueAtTime = vi.fn();
}
class Gain {
  gain = new Param();
  connect(): void {}
  disconnect = vi.fn();
}
class Source {
  buffer: unknown;
  onended: (() => void) | null = null;
  start = vi.fn();
  stop = vi.fn();
  connect(): void {}
  disconnect = vi.fn();
}
class Context {
  get currentTime(): number { return Date.now() / 1000; }
  state = "running";
  destination = {};
  sources: Source[] = [];
  decodeAudioData = vi.fn(async () => ({ duration: 1 }) as AudioBuffer);
  resume = vi.fn(async () => { this.state = "running"; });
  createGain(): Gain { return new Gain(); }
  createBufferSource(): Source { const source = new Source(); this.sources.push(source); return source; }
}

const flush = async (): Promise<void> => { for (let i = 0; i < 40; i++) await Promise.resolve(); };
type Point = readonly [number, number];
/** A mouse pointer event at `at` (client px); over, move and down bubble as in a browser, enter and leave do not. */
const pointer = (element: Element, type: string, at: Point = [0, 0]): boolean =>
  element.dispatchEvent(new PointerEvent(type, { pointerType: "mouse", clientX: at[0], clientY: at[1], bubbles: !/enter|leave/.test(type) }));
/** The player moves the mouse onto `element`: pointerover, pointerenter, then pointermove, all at `at`. */
const moveOnto = (element: Element, at: Point): void => { for (const type of ["pointerover", "pointerenter", "pointermove"]) pointer(element, type, at); };
/** The browser catching up after the layout moved under a still pointer: pointerover and pointerenter at `at`, no pointermove. */
const caughtUp = (element: Element, at: Point): void => { for (const type of ["pointerover", "pointerenter"]) pointer(element, type, at); };
const cleanups: (() => void)[] = [];

beforeEach(() => {
  vi.useFakeTimers();
  vi.setSystemTime(0);
  vi.stubGlobal("GainNode", Gain);
  vi.stubGlobal("AudioBufferSourceNode", Source);
});
afterEach(() => {
  for (const cleanup of cleanups.splice(0)) cleanup();
  document.body.replaceChildren();
  vi.unstubAllGlobals();
  vi.useRealTimers();
});

/**
 * A Sound panel as a game builds it: the gameplay player on a fake context, the game's fetchers, and the save.
 * `online`: the global fetch answers too (bytes), so a test does not depend on which fetch the panel used.
 */
function panel(options: readonly KeyboardSoundChoice[], extra: Partial<QuickSettingsOptions> = {}, online = false) {
  const ctx = new Context();
  const sounds = new TypingSounds({ context: ctx as unknown as AudioContext });
  const fetchJson = vi.fn(async (_url: string): Promise<unknown> => FILES);
  const fetchBytes = vi.fn(async (_url: string) => new ArrayBuffer(2));
  // Anything that reaches the global fetch bypassed the game's fetchers.
  const globalFetch = vi.fn(async (url: string): Promise<Response> => {
    if (!online) throw new Error("global fetch: " + url);
    return { ok: true, status: 200, arrayBuffer: async () => new ArrayBuffer(2) } as unknown as Response;
  });
  vi.stubGlobal("fetch", globalFetch);
  const values: Record<string, QuickValue> = { master: 80, keyboardVolume: 50, muted: false, keyboard: "deep" };
  const onChange = vi.fn((id: string, value: QuickValue) => { values[id] = value; });
  const onKeyboardLoad = vi.fn();
  const onKeyboardFail = vi.fn();
  const qs = new QuickSettings({
    keyboardSounds: sounds, keyboardProfiles: options, getValues: () => values, onChange, countdownMs: 0,
    keyboardFetch: { fetchJson, fetchBytes }, onKeyboardLoad, onKeyboardFail, ...extra,
  });
  cleanups.push(() => { qs.destroy(); sounds.dispose(); });
  const list = () => qs.root.querySelector<HTMLElement>(".kit-keyboards")!;
  const option = (value: string) => qs.root.querySelector<HTMLButtonElement>(`.kit-keyboards [role="option"][data-value="${value}"]`)!;
  /** Every sample or preview URL asked for, through either fetch. */
  const fetched = (): string[] => [...fetchBytes.mock.calls, ...globalFetch.mock.calls].map(([url]) => url);
  return { ctx, sounds, qs, values, onChange, onKeyboardLoad, onKeyboardFail, fetchJson, fetchBytes, globalFetch, fetched, list, option };
}

describe("QuickSettings keyboardFetch: the game's fetchers reach the panel's keyboard preview", () => {
  it("a set picked in the panel loads its manifest through fetchJson and its samples through fetchBytes; hover previews use fetchBytes too", async () => {
    const p = panel(FIRST);
    p.qs.open("sound");
    pointer(p.option("warm"), "pointerenter");
    await vi.advanceTimersByTimeAsync(150);
    await flush();
    expect(p.fetchBytes).toHaveBeenCalledWith(WARM.preview);
    p.option("warm").click();
    await vi.runAllTimersAsync();
    expect(p.values.keyboard).toBe("warm");
    expect(p.fetchJson).toHaveBeenCalledWith(WARM.manifest);
    expect(p.fetchBytes).toHaveBeenCalledWith("/v1/keys/sets/warm/f/key-01.ogg");
    expect(p.fetchBytes).toHaveBeenCalledWith("/v1/keys/sets/warm/f/space-01.ogg");
    expect(p.globalFetch).not.toHaveBeenCalled();
    expect(p.sounds.profile?.id).toBe("warm");
    expect(p.onKeyboardLoad).toHaveBeenCalledWith(expect.objectContaining({ id: "warm", keys: 2, spaces: 1 }));
    expect(p.onKeyboardFail).not.toHaveBeenCalled();
  });

  it("without keyboardFetch the kit's own fetch is used, as before", async () => {
    const p = panel(FIRST, { keyboardFetch: undefined });
    p.qs.open("sound");
    p.option("warm").click();
    await vi.runAllTimersAsync();
    expect(p.globalFetch).toHaveBeenCalledWith(WARM.manifest, { cache: "no-cache" });
    expect(p.fetchJson).not.toHaveBeenCalled();
    // The kit's fetch failed (offline here): nothing loaded, and the game hears of it.
    expect(p.onKeyboardFail).toHaveBeenCalledWith(expect.objectContaining({ value: "warm" }));
  });
});

describe("QuickSettings onKeyboardLoad / onKeyboardFail: a set picked in the panel that cannot sound", () => {
  it("a manifest that fails: the load result is \"pending\" and onKeyboardFail names the pick, so the game can stand its own sound in", async () => {
    const p = panel(FIRST);
    p.fetchJson.mockImplementation(async (url: string) => { if (url === WARM.manifest) throw new Error("404"); return FILES; });
    p.qs.open("sound");
    p.option("warm").click();
    await vi.runAllTimersAsync();
    expect(p.values.keyboard).toBe("warm");
    expect(p.onKeyboardLoad).toHaveBeenLastCalledWith({ id: "warm", state: "pending", keys: 0, spaces: 0, missing: [] });
    expect(p.onKeyboardFail).toHaveBeenCalledOnce();
    expect(p.onKeyboardFail).toHaveBeenCalledWith(expect.objectContaining({ value: "warm", manifest: WARM.manifest }));
    expect(p.sounds.profile).toBeNull();
  });

  it("samples that all fail end the same way; a set with one good sample plays and reports no failure", async () => {
    const p = panel(FIRST);
    p.fetchBytes.mockImplementation(async (url: string) => { if (url.includes("/deep/") && !url.endsWith("key-02.ogg")) throw new Error("404"); if (url.includes("/warm/")) throw new Error("404"); return new ArrayBuffer(2); });
    p.qs.open("sound");
    p.option("warm").click();
    await vi.runAllTimersAsync();
    expect(p.onKeyboardFail).toHaveBeenCalledWith(expect.objectContaining({ value: "warm" }));
    p.onKeyboardFail.mockClear();
    p.option("deep").click();
    await vi.runAllTimersAsync();
    expect(p.onKeyboardLoad).toHaveBeenLastCalledWith(expect.objectContaining({ id: "deep", state: "partial", keys: 1 }));
    expect(p.onKeyboardFail).not.toHaveBeenCalled();
    expect(p.sounds.profile?.id).toBe("deep");
  });

  it("a pick the player has moved on from never reports", async () => {
    let fail!: () => void;
    const p = panel(FIRST);
    p.fetchJson.mockImplementation((url: string) => (url === WARM.manifest ? new Promise((_, reject) => { fail = () => reject(new Error("late 404")); }) : Promise.resolve(FILES)));
    p.qs.open("sound");
    p.option("warm").click();
    await flush();
    p.option("relay").click();
    fail();
    await vi.runAllTimersAsync();
    expect(p.onKeyboardFail).not.toHaveBeenCalled();
    expect(p.onKeyboardLoad).not.toHaveBeenCalled();
  });

  it("KeyboardSoundPreview.onFail also fires when the load itself fails (no audio context)", async () => {
    const sounds = new TypingSounds({ context: () => { throw new Error("no AudioContext"); } });
    const onFail = vi.fn();
    const onLoad = vi.fn();
    const preview = new KeyboardSoundPreview({ sounds, levels: () => ({ master: 1, keyboard: 1 }), fetchJson: async () => FILES, fetchBytes: async () => new ArrayBuffer(2), onLoad, onFail });
    cleanups.push(() => preview.destroy());
    preview.select(WARM, false);
    await flush();
    expect(onFail).toHaveBeenCalledWith(WARM);
    expect(onLoad).not.toHaveBeenCalled();
  });
});

describe("QuickSettings.setChoiceOptions: a rebuild is not the player's doing", () => {
  it("keyboard focus stays on the same option, and that focus plays no preview", async () => {
    const p = panel(FIRST, {}, true);
    p.qs.open("sound");
    p.option("warm").focus();
    await vi.advanceTimersByTimeAsync(200);
    await flush();
    expect(p.ctx.sources).toHaveLength(1);
    expect(p.qs.setChoiceOptions("keyboard", SECOND)).toBe(true);
    expect(p.option("clear")).not.toBeNull();
    expect(document.activeElement).toBe(p.option("warm"));
    expect(p.option("warm").tabIndex).toBe(0);
    await vi.advanceTimersByTimeAsync(500);
    await flush();
    expect(p.ctx.sources).toHaveLength(1);
    expect(p.fetched()).toEqual([WARM.preview]);
    expect(p.onChange).not.toHaveBeenCalled();
    // The player's own moves still preview.
    p.option("warm").dispatchEvent(new KeyboardEvent("keydown", { key: "ArrowDown", bubbles: true, cancelable: true }));
    await vi.advanceTimersByTimeAsync(200);
    await flush();
    expect(document.activeElement).toBe(p.option("clear"));
    expect(p.fetched()).toEqual([WARM.preview, CLEAR.preview]);
    expect(p.ctx.sources).toHaveLength(2);
  });

  it("a focused option the new list lacks hands focus to the selected one, still without a preview", async () => {
    const p = panel(SECOND, {}, true);
    p.qs.open("sound");
    p.option("clear").focus();
    await vi.advanceTimersByTimeAsync(200);
    await flush();
    const before = p.ctx.sources.length;
    expect(before).toBe(1);
    p.qs.setChoiceOptions("keyboard", FIRST);
    expect(document.activeElement).toBe(p.option("deep"));
    expect(p.qs.root.contains(document.activeElement)).toBe(true);
    await vi.advanceTimersByTimeAsync(500);
    await flush();
    expect(p.ctx.sources).toHaveLength(before);
  });

  it("a Listen button that had focus keeps it", () => {
    const p = panel(FIRST);
    p.qs.open("sound");
    p.qs.root.querySelector<HTMLButtonElement>('[data-listen="warm"]')!.focus();
    p.qs.setChoiceOptions("keyboard", SECOND);
    expect((document.activeElement as HTMLElement).dataset.listen).toBe("warm");
  });

  it("the list keeps its scroll position and does not jump to the selected option", async () => {
    const p = panel(SECOND);
    p.qs.open("sound");
    await flush();
    p.list().scrollTop = 120;
    p.qs.setChoiceOptions("keyboard", [...SECOND, set("solid")]);
    const list = p.list();
    // The selected option sits far below the view: an auto-scroll would move the list.
    vi.spyOn(list, "getBoundingClientRect").mockReturnValue({ top: 100, bottom: 406, left: 0, right: 200, height: 306, width: 200, x: 0, y: 100, toJSON: () => ({}) });
    vi.spyOn(p.option("deep"), "getBoundingClientRect").mockReturnValue({ top: 2000, bottom: 2034, left: 0, right: 200, height: 34, width: 200, x: 0, y: 2000, toJSON: () => ({}) });
    Object.defineProperty(list, "clientHeight", { configurable: true, value: 306 });
    await flush();
    expect(list.scrollTop).toBe(120);
    expect(p.option("deep").getAttribute("aria-selected")).toBe("true");
    // Opening the panel again still brings the selection into view, in the middle of the list.
    p.qs.close();
    p.qs.open("sound");
    await flush();
    expect(list.scrollTop).toBe(120 + (2000 + 2034) / 2 - 100 - 306 / 2);
  });

  it("a resting pointer over an option previews nothing when the list under it is rebuilt; moving to another option does", async () => {
    const p = panel(FIRST, {}, true);
    p.qs.open("sound");
    const at: Point = [576, 348];
    moveOnto(p.option("warm"), at);
    await vi.advanceTimersByTimeAsync(200);
    await flush();
    expect(p.ctx.sources).toHaveLength(1);
    p.qs.setChoiceOptions("keyboard", SECOND);
    // The browser tells the new element under the still pointer that it is hovered.
    caughtUp(p.option("warm"), at);
    await vi.advanceTimersByTimeAsync(200);
    await flush();
    expect(p.ctx.sources).toHaveLength(1);
    pointer(p.option("warm"), "pointermove", [576, 360]);
    pointer(p.option("warm"), "pointerleave", [576, 383]);
    moveOnto(p.option("deep"), [576, 383]);
    await vi.advanceTimersByTimeAsync(200);
    await flush();
    expect(p.ctx.sources).toHaveLength(2);
    expect(p.fetched().at(-1)).toBe(DEEP.preview);
  });

  it("a different option that lands under the resting pointer (the list grew) previews nothing and stops nothing, until the pointer moves", async () => {
    const p = panel(FIRST, {}, true);
    p.qs.open("sound");
    const at: Point = [576, 348];
    moveOnto(p.option("warm"), at);
    await vi.advanceTimersByTimeAsync(200);
    await flush();
    expect(p.fetched()).toEqual([WARM.preview]);
    const playing = p.ctx.sources[0]!;
    // Its own 1 s end, scheduled when it started.
    expect(playing.stop).toHaveBeenCalledOnce();
    p.qs.setChoiceOptions("keyboard", SECOND);
    // Chrome, about 0.8 s later: the option now under the still pointer is another one (mouse, no pointermove).
    caughtUp(p.option("deep"), at);
    await vi.advanceTimersByTimeAsync(500);
    await flush();
    // The list shifts again (its scroll is put back): leave and enter at the same point, and a catch-up move there too.
    pointer(p.option("deep"), "pointerleave", at);
    caughtUp(p.option("clear"), at);
    pointer(p.option("clear"), "pointermove", at);
    await vi.advanceTimersByTimeAsync(500);
    await flush();
    expect(p.fetched()).toEqual([WARM.preview]);
    expect(p.ctx.sources).toHaveLength(1);
    expect(playing.stop).toHaveBeenCalledOnce();
    // The player moves: from then on every hover is theirs.
    pointer(p.option("clear"), "pointermove", [577, 352]);
    pointer(p.option("clear"), "pointerleave", [577, 320]);
    expect(playing.stop).toHaveBeenCalledTimes(2);
    moveOnto(p.option("deep"), [577, 320]);
    await vi.advanceTimersByTimeAsync(200);
    await flush();
    expect(p.fetched()).toEqual([WARM.preview, DEEP.preview]);
  });

  it("a pointer resting over the panel but off the list previews nothing when the grown list reaches it", async () => {
    const p = panel(FIRST, {}, true);
    p.qs.open("sound");
    const title = p.qs.root.querySelector('.kit-qs__dialog[data-panel="sound"] .kit-qs__title')!;
    const at: Point = [300, 420];
    moveOnto(title, at);
    p.qs.setChoiceOptions("keyboard", SECOND);
    caughtUp(p.option("clear"), at);
    await vi.advanceTimersByTimeAsync(500);
    await flush();
    expect(p.fetched()).toEqual([]);
    pointer(p.option("clear"), "pointermove", [300, 426]);
    pointer(p.option("clear"), "pointerleave", [300, 392]);
    moveOnto(p.option("warm"), [300, 392]);
    await vi.advanceTimersByTimeAsync(200);
    await flush();
    expect(p.fetched()).toEqual([WARM.preview]);
  });

  it("the player's own move into a rebuilt list previews at once: the panel knows where the pointer was", async () => {
    const p = panel(FIRST, {}, true);
    p.qs.open("sound");
    moveOnto(p.qs.root.querySelector('.kit-qs__dialog[data-panel="sound"] .kit-qs__title')!, [300, 60]);
    p.qs.setChoiceOptions("keyboard", SECOND);
    moveOnto(p.option("warm"), [300, 400]);
    await vi.advanceTimersByTimeAsync(200);
    await flush();
    expect(p.fetched()).toEqual([WARM.preview]);
  });

  it("with no mouse event seen yet, the first one the rebuilt list sees is where the pointer rests", async () => {
    const p = panel(FIRST, {}, true);
    p.qs.open("sound");
    p.qs.setChoiceOptions("keyboard", SECOND);
    caughtUp(p.option("clear"), [40, 500]);
    pointer(p.option("clear"), "pointermove", [40, 500]);
    await vi.advanceTimersByTimeAsync(500);
    await flush();
    expect(p.fetched()).toEqual([]);
    pointer(p.option("clear"), "pointermove", [42, 503]);
    pointer(p.option("clear"), "pointerleave", [42, 470]);
    moveOnto(p.option("warm"), [42, 470]);
    await vi.advanceTimersByTimeAsync(200);
    await flush();
    expect(p.fetched()).toEqual([WARM.preview]);
  });

  it("an open panel keeps its top through a rebuild that changes its height, until it closes or the layer resizes", () => {
    let resized = (): void => {};
    vi.stubGlobal("ResizeObserver", class { constructor(callback: () => void) { resized = callback; } observe(): void {} disconnect(): void {} });
    const p = panel(FIRST);
    const dialog = p.qs.root.querySelector<HTMLElement>('.kit-qs__dialog[data-panel="sound"]')!;
    const box = dialog.querySelector<HTMLElement>(".kit-qs__panel")!;
    const rect = (top: number, height: number): DOMRect => ({ top, bottom: top + height, left: 0, right: 560, width: 560, height, x: 0, y: top, toJSON: () => ({}) });
    const held = (): string[] => [box.style.alignSelf, box.style.marginTop, box.style.maxHeight];
    vi.spyOn(dialog, "getBoundingClientRect").mockReturnValue(rect(0, 600));
    // Closed: nothing to hold.
    const top = vi.spyOn(box, "getBoundingClientRect").mockReturnValue(rect(120, 360));
    p.qs.setChoiceOptions("keyboard", SECOND);
    expect(held()).toEqual(["", "", ""]);
    p.qs.open("sound");
    // The same height: the panel stays centred.
    p.qs.setChoiceOptions("keyboard", SECOND);
    expect(held()).toEqual(["", "", ""]);
    // Three rows centred at y = 120; the grown list would centre the panel at y = 41 in a 600 px frame.
    top.mockReturnValueOnce(rect(120, 360)).mockReturnValue(rect(41, 518));
    p.qs.setChoiceOptions("keyboard", [...SECOND, set("solid")]);
    expect(held()).toEqual(["flex-start", "120px", "calc(100% - 136px)"]);
    // A new layer size centres it again.
    resized();
    expect(held()).toEqual(["", "", ""]);
    top.mockReturnValueOnce(rect(120, 360)).mockReturnValue(rect(41, 518));
    p.qs.setChoiceOptions("keyboard", SECOND);
    expect(held()).toEqual(["flex-start", "120px", "calc(100% - 136px)"]);
    // Closing ends the hold: the next opening is centred.
    p.qs.close();
    expect(held()).toEqual(["", "", ""]);
  });

  it("a preview the player started plays on through a rebuild", async () => {
    const p = panel(FIRST, {}, true);
    p.qs.open("sound");
    pointer(p.option("warm"), "pointerenter");
    await vi.advanceTimersByTimeAsync(200);
    await flush();
    const playing = p.ctx.sources[0]!;
    // Its own end (1 s) is scheduled when it starts.
    expect(playing.stop).toHaveBeenCalledOnce();
    p.qs.setChoiceOptions("keyboard", SECOND);
    expect(playing.stop).toHaveBeenCalledOnce();
    // Closing the panel still stops it.
    p.qs.close();
    expect(playing.stop).toHaveBeenCalledTimes(2);
  });

  it("a radio row keeps focus on the same value", () => {
    const p = panel(FIRST, { getValues: () => ({ quality: "high", keyboard: "deep" }) });
    p.qs.open("settings");
    const radio = (value: string) => p.qs.root.querySelector<HTMLInputElement>(`[data-row="quality"] input[value="${value}"]`)!;
    radio("low").focus();
    p.qs.setChoiceOptions("quality", [{ value: "low", label: "Low" }, { value: "medium", label: "Medium" }, { value: "high", label: "High" }]);
    expect(document.activeElement).toBe(radio("low"));
    expect(radio("high").checked).toBe(true);
  });
});

function luminance(color: string): number {
  const hex = color.trim().toUpperCase();
  expect(hex, color).toMatch(/^#[0-9A-F]{6}$/);
  const [r, g, b] = [1, 3, 5]
    .map((start) => parseInt(hex.slice(start, start + 2), 16) / 255)
    .map((value) => (value <= 0.03928 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4)) as [number, number, number];
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}
const contrast = (a: string, b: string): number => {
  const [hi, lo] = [luminance(a), luminance(b)].sort((x, y) => y - x) as [number, number];
  return (hi + 0.05) / (lo + 0.05);
};
/** The element's own ground, or the nearest ancestor's when it is transparent. */
function ground(element: HTMLElement): string {
  for (let node: HTMLElement | null = element; node !== null; node = node.parentElement) {
    const color = getComputedStyle(node).backgroundColor;
    if (color && color !== "transparent" && !/rgba\([^)]*,\s*0\)/.test(color)) return color;
  }
  return "#FFFFFF";
}
/** A style sheet whose :hover is the class `is-hover`, so a test can hover an element. */
function hoverable(css: string): void {
  const style = document.createElement("style");
  style.textContent = css.replace(/:hover/g, ".is-hover");
  document.head.append(style);
  cleanups.push(() => style.remove());
}

describe("readable keyboard options: selected, hovered, disabled (≥ 4.5:1 against their row)", () => {
  it.each([false, true])("every option state, hover %s, the \"Saved sound · unavailable\" one included", (hover) => {
    hoverable(KEYBOARD_CHOICES_CSS);
    // The catalogue did not load: the saved set stays selected and is listed disabled.
    const settled = settleKeyboardChoice("hail-stone", { state: "missing", options: [OFF, RELAY] }, RELAY);
    const options = [...settled.options, DEEP, { ...WARM, disabled: true }];
    const picker = new KeyboardSoundChoices({ document, options, label: "Keyboard sound", onSelect: () => {}, onPreview: () => {}, onStop: () => {} });
    document.body.append(picker.element);
    cleanups.push(() => picker.destroy());
    const button = (value: string) => picker.element.querySelector<HTMLButtonElement>(`[role="option"][data-value="${value}"]`)!;
    const check = (value: string, selected: string): void => {
      picker.sync(selected);
      const target = button(value);
      target.classList.toggle("is-hover", hover);
      const style = getComputedStyle(target);
      const label = `${value} (selected ${selected}, hover ${hover}): ${style.color} on ${ground(target)}`;
      expect(contrast(style.color, ground(target)), label).toBeGreaterThanOrEqual(4.5);
      target.classList.remove("is-hover");
    };
    expect(button("hail-stone").disabled).toBe(true);
    expect(button("hail-stone").textContent).toBe("Saved sound unavailable");
    check("hail-stone", "hail-stone");
    check("deep", "deep");
    check("relay", "relay");
    check("deep", "hail-stone");
    check("warm", "deep");
    check("warm", "warm");
    // The selected, unavailable option is still marked as the current one.
    picker.sync("hail-stone");
    expect(getComputedStyle(button("hail-stone")).boxShadow).toContain(QUICK_SETTINGS_COLORS["--kit-qs-accent"]);
    // Measured on the fallbacks, which are QuickSettings' own colours.
    for (const name of ["--kit-qs-bg", "--kit-qs-control", "--kit-qs-muted", "--kit-qs-accent", "--kit-qs-accent-text"] as const) {
      expect(KEYBOARD_CHOICES_CSS).toContain(`var(${name},${QUICK_SETTINGS_COLORS[name]})`);
    }
  });

  it.each([false, true])("a quick-settings radio chip that is checked and disabled, hover %s", (hover) => {
    hoverable(QUICK_SETTINGS_CSS);
    const qs = new QuickSettings({
      getValues: () => ({ quality: "ultra" }), onChange: () => {}, countdownMs: 0,
      settingsRows: [{ kind: "choice", id: "quality", label: "Quality", options: [{ value: "high", label: "High" }, { value: "ultra", label: "Ultra", disabled: true, note: "unavailable" }] }],
    });
    cleanups.push(() => qs.destroy());
    for (const [name, value] of Object.entries(QUICK_SETTINGS_COLORS)) qs.root.style.setProperty(name, value);
    for (const value of ["ultra", "high"]) {
      const input = qs.root.querySelector<HTMLInputElement>(`input[value="${value}"]`)!;
      const chip = input.nextElementSibling as HTMLElement;
      input.parentElement!.classList.toggle("is-hover", hover);
      const style = getComputedStyle(chip);
      expect(contrast(style.color, ground(chip)), `${value}: ${style.color} on ${ground(chip)}`).toBeGreaterThanOrEqual(4.5);
    }
    expect(qs.root.querySelector<HTMLInputElement>('input[value="ultra"]')!.checked).toBe(true);
  });
});

describe("timedBytes: a sample fetch with a deadline", () => {
  const bytesAnswer = (status = 200) => ({ ok: status >= 200 && status < 300, status, arrayBuffer: async () => new ArrayBuffer(3) }) as unknown as Response;

  it("reads bytes with an abort signal and the fetch's own cache mode, and clears its timer", async () => {
    const fetch = vi.fn(async (_url: string, _init?: RequestInit) => bytesAnswer());
    vi.stubGlobal("fetch", fetch);
    expect((await timedBytes()("/a.ogg")).byteLength).toBe(3);
    await timedBytes(1000, { cache: "force-cache" })("/b.ogg");
    expect(fetch.mock.calls[0]![1]).toEqual({ signal: expect.any(AbortSignal) });
    expect(fetch.mock.calls[1]![1]).toEqual({ cache: "force-cache", signal: expect.any(AbortSignal) });
    expect(vi.getTimerCount()).toBe(0);
  });

  it("gives up after 8000 ms by default, aborting the request, even one that ignores the signal", async () => {
    let signal: AbortSignal | undefined;
    vi.stubGlobal("fetch", vi.fn((_url: string, init?: RequestInit) => { signal = init?.signal ?? undefined; return new Promise<never>(() => {}); }));
    const settled = vi.fn();
    const pending = timedBytes()("/hang.ogg");
    pending.then(settled, settled);
    expect(KEYBOARD_SAMPLE_TIMEOUT_MS).toBe(8000);
    await vi.advanceTimersByTimeAsync(7999);
    expect(settled).not.toHaveBeenCalled();
    await vi.advanceTimersByTimeAsync(1);
    await expect(pending).rejects.toThrow("/hang.ogg: no answer in 8000 ms");
    expect(signal?.aborted).toBe(true);
    expect(vi.getTimerCount()).toBe(0);
  });

  it("a non-positive, non-finite or above-setTimeout timeout takes the 8000 ms default; a given one is kept", async () => {
    vi.stubGlobal("fetch", vi.fn(() => new Promise<never>(() => {})));
    for (const ms of [0, -1, Number.NaN, Number.POSITIVE_INFINITY, 2_147_483_648]) {
      const result = timedBytes(ms)("/x.ogg").then(() => "resolved", (error: Error) => error.message);
      await vi.advanceTimersByTimeAsync(8000);
      expect(await result).toMatch(/no answer in 8000 ms/);
    }
    const short = timedBytes(250)("/y.ogg").then(() => "resolved", (error: Error) => error.message);
    await vi.advanceTimersByTimeAsync(250);
    expect(await short).toMatch(/no answer in 250 ms/);
  });

  it("rejects on a non-OK status and on a network failure, clearing the timer", async () => {
    vi.stubGlobal("fetch", vi.fn(async () => bytesAnswer(404)));
    await expect(timedBytes()("/missing.ogg")).rejects.toThrow("/missing.ogg: 404");
    vi.stubGlobal("fetch", vi.fn(async () => { throw new TypeError("Failed to fetch"); }));
    await expect(timedBytes()("/cors.ogg")).rejects.toThrow("Failed to fetch");
    expect(vi.getTimerCount()).toBe(0);
  });

  it("through the panel: a hung sample counts as missing after its limit, so a pick that never sounds still reports", async () => {
    // The manifest answers; every sample hangs.
    vi.stubGlobal("fetch", vi.fn((url: string) => (url.endsWith(".json") ? Promise.resolve({ ok: true, status: 200, headers: new Headers(), text: async () => JSON.stringify(FILES) }) : new Promise<never>(() => {}))));
    const sounds = new TypingSounds({ context: new Context() as unknown as AudioContext });
    const onKeyboardFail = vi.fn();
    const qs = new QuickSettings({
      keyboardSounds: sounds, keyboardProfiles: FIRST, getValues: () => ({ master: 80, keyboardVolume: 50, keyboard: "deep" }), onChange: () => {}, countdownMs: 0,
      keyboardFetch: { fetchJson: quickIndex.timedJson(3000, { cache: "default" }), fetchBytes: timedBytes(500) }, onKeyboardFail,
    });
    cleanups.push(() => { qs.destroy(); sounds.dispose(); });
    qs.open("sound");
    qs.root.querySelector<HTMLButtonElement>('[role="option"][data-value="warm"]')!.click();
    await vi.advanceTimersByTimeAsync(499);
    expect(onKeyboardFail).not.toHaveBeenCalled();
    await vi.advanceTimersByTimeAsync(1);
    await flush();
    expect(onKeyboardFail).toHaveBeenCalledWith(expect.objectContaining({ value: "warm" }));
    expect(vi.getTimerCount()).toBe(0);
  });

  it("a full set picked on a hung sample host reports after one sample timeout, not one per batch, and asks for one batch only", async () => {
    const keys = Array.from({ length: 80 }, (_, i) => `key-${String(i + 1).padStart(2, "0")}.ogg`);
    const spaces = Array.from({ length: 8 }, (_, i) => `space-0${i + 1}.ogg`);
    const fetch = vi.fn((url: string) => (url.endsWith(".json") ? Promise.resolve({ ok: true, status: 200, headers: new Headers(), text: async () => JSON.stringify({ files: [...keys, ...spaces] }) }) : new Promise<never>(() => {})));
    vi.stubGlobal("fetch", fetch);
    const sounds = new TypingSounds({ context: new Context() as unknown as AudioContext });
    const onKeyboardFail = vi.fn();
    const qs = new QuickSettings({
      keyboardSounds: sounds, keyboardProfiles: FIRST, getValues: () => ({ master: 80, keyboardVolume: 50, keyboard: "deep" }), onChange: () => {}, countdownMs: 0,
      keyboardFetch: { fetchJson: timedJson(3000, { cache: "default" }), fetchBytes: timedBytes() }, onKeyboardFail,
    });
    cleanups.push(() => { qs.destroy(); sounds.dispose(); });
    qs.open("sound");
    qs.root.querySelector<HTMLButtonElement>('[role="option"][data-value="warm"]')!.click();
    await vi.advanceTimersByTimeAsync(KEYBOARD_SAMPLE_TIMEOUT_MS - 1);
    expect(onKeyboardFail).not.toHaveBeenCalled();
    await vi.advanceTimersByTimeAsync(1);
    await flush();
    expect(onKeyboardFail).toHaveBeenCalledWith(expect.objectContaining({ value: "warm" }));
    const samples = fetch.mock.calls.map(([url]) => url).filter((url) => /\/(key|space)-\d+\.ogg$/.test(url));
    expect(samples).toHaveLength(KEYBOARD_DECODE_BATCH_SIZE);
    expect(sounds.profile).toBeNull();
    expect(vi.getTimerCount()).toBe(0);
  });

  it("is exported beside timedJson by feedback/typing-fx and ui/quick-settings", () => {
    expect(fxIndex.timedBytes).toBe(timedBytes);
    expect(quickIndex.timedBytes).toBe(timedBytes);
    expect(fxIndex.KEYBOARD_SAMPLE_TIMEOUT_MS).toBe(8000);
    expect(quickIndex.KEYBOARD_SAMPLE_TIMEOUT_MS).toBe(8000);
  });
});
