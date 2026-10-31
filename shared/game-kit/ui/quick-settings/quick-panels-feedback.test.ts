// @vitest-environment happy-dom
// Judges' kit items of 31/10 (night) after the art wiring: the muted Master row, Listen feedback (size, hover, press,
// lit while its sample sounds), the keyboard list's thin scrollbar. (Tab and Shift+Tab in the panel: focus.ts.)
import { afterEach, describe, expect, it, vi } from "vitest";
import { KeyboardSoundPreview, TypingSounds, type KeyboardSoundChoice } from "../../feedback/typing-fx/audio";
import { KEYBOARD_CHOICES_CSS, KeyboardSoundChoices } from "./keyboard-choices";
import { QUICK_SETTINGS_CSS, QUICK_SETTINGS_VARS } from "./css";
import { QuickSettings, type QuickSettingsOptions } from "./quick-settings";
import { defaultSoundRows } from "./rows";
import type { QuickChoiceOption, QuickValue } from "./types";

const ART = "https://art.example.test/";
const ICONS = { "hud-sound": `${ART}sound.png`, "hud-sound-muted": `${ART}muted.png`, "vol-master": `${ART}master.png` };
const SETS: QuickChoiceOption[] = [
  { value: "off", label: "Off" },
  { value: "deep", label: "Deep", preview: `${ART}deep.ogg` },
  { value: "warm", label: "Warm", preview: `${ART}warm.ogg` },
];

const cleanups: (() => void)[] = [];
afterEach(() => {
  for (const cleanup of cleanups.splice(0).reverse()) cleanup();
  document.body.replaceChildren();
  vi.unstubAllGlobals();
  vi.useRealTimers();
  vi.restoreAllMocks();
});

function make(extra: Partial<QuickSettingsOptions> = {}, start: Record<string, QuickValue> = {}) {
  const host = document.createElement("div");
  document.body.append(host);
  const values: Record<string, QuickValue> = { master: 80, muted: false, music: 40, effects: 50, keyboardVolume: 70, voice: 25, ui: 65, keyboard: "deep", ...start };
  const qs = new QuickSettings({ host, keyboardProfiles: SETS, getValues: () => values, onChange: (id, value) => { values[id] = value; }, countdownMs: 0, icons: ICONS, ...extra });
  cleanups.push(() => { qs.destroy(); host.remove(); });
  const dialog = (panel: "settings" | "sound") => qs.root.querySelector<HTMLElement>(`.kit-qs__dialog[data-panel="${panel}"]`)!;
  const master = () => dialog("sound").querySelector<HTMLElement>('.kit-qs__row[data-row="master"]')!;
  const mute = () => master().querySelector<HTMLButtonElement>('[data-toggle="muted"]')!;
  const icon = () => master().querySelector<HTMLImageElement>(".kit-qs__icon-cell img")?.getAttribute("src") ?? null;
  return { qs, values, dialog, master, mute, icon };
}

function slide(range: HTMLInputElement, value: number): void {
  range.value = String(value);
  range.dispatchEvent(new Event("input", { bubbles: true }));
}

describe("the muted Master row (kit, was each game's own quick.ts)", () => {
  it("the default Master row names its pressed label and muted icon", () => {
    const master = defaultSoundRows()[0]!;
    expect(master.kind === "slider" && master.toggle).toEqual({ id: "muted", label: "Mute", pressedLabel: "Unmute" });
    expect(master.kind === "slider" && master.mutedIcon).toBe("hud-sound-muted");
  });

  it("Mute pressed: the button reads Unmute on the pressed plate, the row is muted and silent, its speaker is the muted one", () => {
    const h = make();
    h.qs.open("sound");
    expect(h.mute().textContent).toBe("Mute");
    expect(h.master().classList.contains("kit-qs__row--muted")).toBe(false);
    expect(h.icon()).toBe(ICONS["vol-master"]);
    h.mute().click();
    expect(h.values.muted).toBe(true);
    expect(h.mute().getAttribute("aria-pressed")).toBe("true");
    expect(h.mute().textContent).toBe("Unmute");
    expect(h.master().classList.contains("kit-qs__row--muted")).toBe(true);
    expect(h.master().classList.contains("kit-qs__row--silent")).toBe(true);
    expect(h.icon()).toBe(ICONS["hud-sound-muted"]);
    // Other slider rows never take the muted state.
    expect(h.dialog("sound").querySelectorAll(".kit-qs__row--muted")).toHaveLength(1);
    h.mute().click();
    expect(h.mute().textContent).toBe("Mute");
    expect(h.master().classList.contains("kit-qs__row--muted")).toBe(false);
    expect(h.icon()).toBe(ICONS["vol-master"]);
  });

  it("Master at 0 is silent (muted speaker) but not struck; a saved mute shows at once, and after refresh()", () => {
    const h = make({}, { muted: true });
    expect(h.mute().textContent).toBe("Unmute");
    expect(h.icon()).toBe(ICONS["hud-sound-muted"]);
    h.values.muted = false;
    h.qs.refresh();
    expect(h.mute().textContent).toBe("Mute");
    h.qs.open("sound");
    slide(h.master().querySelector<HTMLInputElement>(".kit-qs__range")!, 0);
    expect(h.master().classList.contains("kit-qs__row--silent")).toBe(true);
    expect(h.master().classList.contains("kit-qs__row--muted")).toBe(false);
    expect(h.icon()).toBe(ICONS["hud-sound-muted"]);
  });

  it("without muted art (or when it fails) the row keeps its own icon", () => {
    const h = make({ icons: { "vol-master": ICONS["vol-master"] } }, { muted: true });
    expect(h.icon()).toBe(ICONS["vol-master"]);
    h.qs.setIcons({ "hud-sound-muted": ICONS["hud-sound-muted"] });
    expect(h.icon()).toBe(ICONS["hud-sound-muted"]);
    h.master().querySelector("img")!.dispatchEvent(new Event("error"));
    expect(h.icon()).toBe(ICONS["vol-master"]);
  });

  it("CSS: the muted row dims its slider (both groove layers and the knob) and strikes its number", () => {
    expect(QUICK_SETTINGS_VARS["--kit-qs-muted-filter"]).toBe("grayscale(.7) brightness(.6)");
    expect(QUICK_SETTINGS_CSS).toContain(".kit-qs__row--muted .kit-qs__slider{filter:var(--kit-qs-muted-filter)}");
    expect(QUICK_SETTINGS_CSS).toMatch(/\.kit-qs__row--muted \.kit-qs__num\{opacity:\.55;text-decoration:line-through;/);
  });
});

describe("Listen buttons give feedback", () => {
  it("CSS: the icon scales with the panel, glows under the pointer, shrinks while pressed, is lit while playing", () => {
    expect(KEYBOARD_CHOICES_CSS).toContain(".kit-keyboards__listen img{display:block;width:calc(24px * var(--kit-qs-s,1));height:calc(24px * var(--kit-qs-s,1));");
    expect(KEYBOARD_CHOICES_CSS).toContain(".kit-qs.kit-qs--skin-list .kit-keyboards .kit-keyboards__listen:hover:not(:disabled){background:transparent;filter:brightness(1.2) var(--kit-qs-glow-filter)}");
    expect(KEYBOARD_CHOICES_CSS).toContain(".kit-keyboards__listen:active:not(:disabled) img{transform:scale(.84)}");
    expect(KEYBOARD_CHOICES_CSS).toMatch(/\.kit-keyboards__listen\.is-playing img\{filter:brightness\(1\.35\) drop-shadow\(/);
  });

  it("playing(value) lights only that set's Listen button; null clears it", () => {
    const picker = new KeyboardSoundChoices({ document, options: SETS, label: "Keyboard sound", onSelect: () => {}, onPreview: () => {}, onStop: () => {} });
    document.body.append(picker.element);
    const lit = () => [...picker.element.querySelectorAll<HTMLElement>(".kit-keyboards__listen.is-playing")].map((b) => b.dataset.listen);
    picker.playing("warm");
    expect(lit()).toEqual(["warm"]);
    picker.playing("deep");
    expect(lit()).toEqual(["deep"]);
    picker.playing(null);
    expect(lit()).toEqual([]);
  });

  it("the preview reports when its sample starts and ends, and a stop or a new preview ends it", async () => {
    vi.useFakeTimers();
    vi.setSystemTime(0);
    const ctx = fakeContext();
    vi.stubGlobal("GainNode", ctx.Gain);
    const onPlaying = vi.fn();
    const player = new KeyboardSoundPreview({ sounds: new TypingSounds({ context: ctx as unknown as AudioContext }), levels: () => ({ master: 1, keyboard: 1 }), fetchBytes: async () => new ArrayBuffer(2), onPlaying });
    cleanups.push(() => player.destroy());
    const deep = SETS[1] as KeyboardSoundChoice;
    const warm = SETS[2] as KeyboardSoundChoice;
    player.preview(deep, 0);
    await vi.advanceTimersByTimeAsync(0);
    expect(onPlaying).toHaveBeenLastCalledWith(deep);
    ctx.sources[0]!.onended?.();
    expect(onPlaying).toHaveBeenLastCalledWith(null);
    player.preview(warm, 0);
    await vi.advanceTimersByTimeAsync(0);
    expect(onPlaying).toHaveBeenLastCalledWith(warm);
    player.preview(deep, 0);
    expect(onPlaying).toHaveBeenLastCalledWith(null);
    await vi.advanceTimersByTimeAsync(0);
    expect(onPlaying).toHaveBeenLastCalledWith(deep);
    player.stop();
    expect(onPlaying).toHaveBeenLastCalledWith(null);
    const calls = onPlaying.mock.calls.length;
    player.stop();
    expect(onPlaying).toHaveBeenCalledTimes(calls);
  });

  it("QuickSettings lights the Listen button while its sample sounds", async () => {
    vi.useFakeTimers();
    vi.setSystemTime(0);
    const ctx = fakeContext();
    vi.stubGlobal("GainNode", ctx.Gain);
    vi.stubGlobal("fetch", vi.fn(async () => ({ ok: true, arrayBuffer: async () => new ArrayBuffer(2) })));
    const h = make({ keyboardSounds: new TypingSounds({ context: ctx as unknown as AudioContext }) });
    h.qs.open("sound");
    const listen = h.dialog("sound").querySelector<HTMLButtonElement>('[data-listen="warm"]')!;
    listen.click();
    await vi.advanceTimersByTimeAsync(0);
    expect(listen.classList.contains("is-playing")).toBe(true);
    expect(h.dialog("sound").querySelectorAll(".is-playing")).toHaveLength(1);
    ctx.sources.at(-1)!.onended?.();
    expect(listen.classList.contains("is-playing")).toBe(false);
    listen.click();
    await vi.advanceTimersByTimeAsync(0);
    expect(listen.classList.contains("is-playing")).toBe(true);
    h.qs.close();
    expect(listen.classList.contains("is-playing")).toBe(false);
  });
});

describe("the keyboard list's scrollbar", () => {
  it("is thin, in --kit-qs-scroll-thumb on a clear track (default the line colour)", () => {
    expect(KEYBOARD_CHOICES_CSS).toContain("scrollbar-width:thin;scrollbar-color:var(--kit-qs-scroll-thumb,var(--kit-qs-line,#4A505C)) transparent;");
    expect(QUICK_SETTINGS_VARS["--kit-qs-scroll-thumb"]).toBe("var(--kit-qs-line)");
  });
});

function fakeContext() {
  class Param {
    value = 1;
    cancelScheduledValues(): void {}
    setValueAtTime(value: number): void { this.value = value; }
    linearRampToValueAtTime(): void {}
  }
  class Gain { gain = new Param(); connect(): void {} disconnect(): void {} }
  class Source {
    buffer: unknown;
    onended: (() => void) | null = null;
    start(): void {}
    stop(): void {}
    connect(): void {}
    disconnect(): void {}
  }
  const ctx = {
    get currentTime(): number { return Date.now() / 1000; },
    state: "running",
    destination: {},
    sources: [] as Source[],
    decodeAudioData: async () => ({ duration: 1 }) as AudioBuffer,
    resume: async () => { ctx.state = "running"; },
    createGain: () => new Gain(),
    createBufferSource: () => { const source = new Source(); ctx.sources.push(source); return source; },
    Gain,
  };
  return ctx;
}
