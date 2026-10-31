// @vitest-environment happy-dom
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { pendingKeyboardChoices, settleKeyboardChoice, type KeyboardSoundChoice } from "../../feedback/typing-fx/audio";
import { QUICK_SETTINGS_STYLE_ID } from "./css";
import { QuickSettings, type QuickSettingsOptions } from "./quick-settings";
import type { QuickValue } from "./types";

const ART = "https://art.example.test/";
const ICONS = { "hud-settings": `${ART}gear.png`, "hud-sound": `${ART}sound.png`, "hud-sound-muted": `${ART}muted.png`, "vol-master": `${ART}master.png` };

type Harness = ReturnType<typeof setup>;
let current: Harness | null = null;

function setup(extra: Partial<QuickSettingsOptions> = {}) {
  const host = document.createElement("div");
  host.style.position = "relative";
  const input = document.createElement("input");
  document.body.append(host, input);
  input.focus();
  const values: Record<string, QuickValue> = {
    master: 80, muted: false, music: 60, effects: 70, keyboard: "creamy", keyboardVolume: 50, voice: 90, ui: 40,
    fxStyle: "stamp", fxIntensity: "normal", fxSize: "large", quality: "high", reducedMotion: false,
  };
  const gameKeys: string[] = [];
  const onGameKey = (event: KeyboardEvent) => gameKeys.push(`${event.type}:${event.key}`);
  window.addEventListener("keydown", onGameKey);
  document.addEventListener("keypress", onGameKey);
  window.addEventListener("keyup", onGameKey);
  const spies = {
    onChange: vi.fn((id: string, value: QuickValue) => {
      values[id] = value;
    }),
    onPreview: vi.fn(),
    onPause: vi.fn(),
    onResume: vi.fn(),
    onQuit: vi.fn(),
  };
  const qs = new QuickSettings({ host, getValues: () => values, ...spies, ...extra });
  const harness = {
    qs, host, input, values, gameKeys, ...spies,
    dialog: (panel: "settings" | "sound") => qs.root.querySelector<HTMLElement>(`.kit-qs__dialog[data-panel="${panel}"]`)!,
    corner: (panel: "settings" | "sound") => qs.root.querySelector<HTMLButtonElement>(`.kit-qs__corner[data-panel="${panel}"]`)!,
    row: (id: string) => qs.root.querySelector<HTMLElement>(`[data-row="${id}"]`)!,
    teardown() {
      qs.destroy();
      window.removeEventListener("keydown", onGameKey);
      document.removeEventListener("keypress", onGameKey);
      window.removeEventListener("keyup", onGameKey);
      host.remove();
      input.remove();
    },
  };
  current = harness;
  return harness;
}

function press(target: EventTarget, key: string, type = "keydown"): KeyboardEvent {
  const event = new KeyboardEvent(type, { key, bubbles: true, cancelable: true });
  target.dispatchEvent(event);
  return event;
}

function slide(range: HTMLInputElement, value: number): void {
  range.value = String(value);
  range.dispatchEvent(new Event("input", { bubbles: true }));
}

function choose(row: HTMLElement, value: string): void {
  const option = row.querySelector<HTMLButtonElement>(`button[role="option"][data-value="${value}"]`);
  if (option) { option.click(); return; }
  const radio = row.querySelector<HTMLInputElement>(`input[value="${value}"]`)!;
  radio.checked = true;
  radio.dispatchEvent(new Event("change", { bubbles: true }));
}

beforeEach(() => vi.useFakeTimers());
afterEach(() => {
  current?.teardown();
  current = null;
  vi.useRealTimers();
});

describe("QuickSettings buttons and shortcuts", () => {
  it("puts two buttons in the host's corner and installs the styles once", () => {
    const h = setup();
    const second = new QuickSettings({ host: h.host, getValues: () => ({}), onChange: () => {} });
    expect(document.querySelectorAll(`#${QUICK_SETTINGS_STYLE_ID}`)).toHaveLength(1);
    second.destroy();
    expect(h.host.querySelectorAll(".kit-qs__bar > button")).toHaveLength(2);
    expect(h.corner("settings").title).toBe("Settings (F1)");
    expect(h.corner("sound").getAttribute("aria-keyshortcuts")).toBe("F2");
    expect(h.qs.root.style.zIndex).toBe("100");
    expect(h.dialog("settings").getAttribute("aria-hidden")).toBe("true");
  });

  it("opens with F1, F2 and a click, switches panels, and pauses once", () => {
    const h = setup();
    const f1 = press(h.input, "F1");
    expect(f1.defaultPrevented).toBe(true);
    expect(h.qs.panel).toBe("settings");
    expect(h.dialog("settings").hasAttribute("aria-hidden")).toBe(false);
    expect(h.corner("settings").getAttribute("aria-expanded")).toBe("true");
    press(document.activeElement ?? document.body, "F2");
    expect(h.qs.panel).toBe("sound");
    expect(h.dialog("settings").getAttribute("aria-hidden")).toBe("true");
    press(h.input, "F2");
    expect(h.qs.isOpen).toBe(false);
    expect(h.qs.blocking).toBe(true);
    h.corner("settings").click();
    expect(h.qs.panel).toBe("settings");
    press(document.activeElement ?? document.body, "Escape");
    expect(h.qs.isOpen).toBe(false);
    expect(h.onPause).toHaveBeenCalledTimes(1);
    expect(h.gameKeys).toEqual([]);
  });

  it("never opens a panel from letters and ignores a held F1", () => {
    const h = setup();
    for (const key of ["s", "S", "o", "1", "Enter", "Escape"]) press(h.input, key);
    expect(h.qs.isOpen).toBe(false);
    press(h.input, "F1");
    const held = new KeyboardEvent("keydown", { key: "F1", repeat: true, bubbles: true, cancelable: true });
    h.input.dispatchEvent(held);
    expect(h.qs.panel).toBe("settings");
    expect(held.defaultPrevented).toBe(true);
  });

  it("returns focus to the typing input after closing", () => {
    const h = setup();
    press(h.input, "F1");
    expect(h.dialog("settings").contains(document.activeElement)).toBe(true);
    h.qs.close();
    expect(document.activeElement).toBe(h.input);
  });
});

describe("QuickSettings typing freeze", () => {
  it("lets typing through when closed and swallows it while open and during the countdown", () => {
    const h = setup();
    const free = press(h.input, "a");
    expect(free.defaultPrevented).toBe(false);
    expect(h.gameKeys).toEqual(["keydown:a"]);

    press(h.input, "F1");
    for (const type of ["keydown", "keypress", "keyup"]) expect(press(h.input, "b", type).defaultPrevented).toBe(true);
    press(document.activeElement ?? document.body, "Escape");
    expect(h.qs.blocking).toBe(true);
    expect(press(h.input, "c").defaultPrevented).toBe(true);
    expect(press(h.input, "Escape", "keyup").defaultPrevented).toBe(true);
    expect(h.gameKeys).toEqual(["keydown:a"]);

    vi.advanceTimersByTime(1500);
    expect(h.qs.blocking).toBe(false);
    press(h.input, "d");
    expect(h.gameKeys).toEqual(["keydown:a", "keydown:d"]);
  });

  it("gives keys inside the panel to its controls and not to the game", () => {
    const h = setup();
    press(h.input, "F2");
    const range = h.row("music").querySelector<HTMLInputElement>("input[type=range]")!;
    const seen: string[] = [];
    range.addEventListener("keydown", (event) => seen.push(event.key));
    for (const key of ["ArrowRight", "a"]) expect(press(range, key).defaultPrevented).toBe(false);
    expect(seen).toEqual(["ArrowRight", "a"]);
    // Tab is the panel's own: focus goes round its controls (focus.ts), from the range to the next one.
    range.focus();
    expect(press(range, "Tab").defaultPrevented).toBe(true);
    expect(document.activeElement).not.toBe(range);
    expect(h.dialog("sound").contains(document.activeElement)).toBe(true);
    expect(h.gameKeys).toEqual([]);
  });
});

describe("QuickSettings countdown", () => {
  it("counts 3, 2, 1 before onResume", () => {
    const h = setup();
    h.qs.open("settings");
    h.qs.close();
    const count = h.qs.root.querySelector<HTMLElement>(".kit-qs__count")!;
    expect(count.hidden).toBe(false);
    expect(count.textContent).toBe("3");
    vi.advanceTimersByTime(500);
    expect(count.textContent).toBe("2");
    vi.advanceTimersByTime(500);
    expect(count.textContent).toBe("1");
    expect(h.onResume).not.toHaveBeenCalled();
    vi.advanceTimersByTime(500);
    expect(h.onResume).toHaveBeenCalledTimes(1);
    expect(count.hidden).toBe(true);
    expect(h.qs.blocking).toBe(false);
  });

  it("cancels the countdown when a panel opens again, staying paused", () => {
    const h = setup();
    h.qs.open("sound");
    h.qs.close();
    vi.advanceTimersByTime(600);
    press(h.input, "F1");
    vi.advanceTimersByTime(5000);
    expect(h.onResume).not.toHaveBeenCalled();
    expect(h.onPause).toHaveBeenCalledTimes(1);
    expect(h.qs.panel).toBe("settings");
    expect(h.qs.root.querySelector<HTMLElement>(".kit-qs__count")!.hidden).toBe(true);
  });

  it("resumes at once with countdownMs 0 and quits without a countdown", () => {
    let step = 0;
    const h = setup({ countdownMs: () => step });
    h.qs.open("settings");
    h.qs.close();
    expect(h.onResume).toHaveBeenCalledTimes(1);
    expect(h.qs.blocking).toBe(false);
    step = 500;
    h.qs.open("settings");
    h.qs.root.querySelector<HTMLButtonElement>('[data-action="quit"]')!.click();
    expect(h.onQuit).toHaveBeenCalledTimes(1);
    expect(h.qs.blocking).toBe(false);
    vi.advanceTimersByTime(2000);
    expect(h.onResume).toHaveBeenCalledTimes(1);
  });

  it("resumes through the Resume button", () => {
    const h = setup();
    h.qs.open("settings");
    h.qs.root.querySelector<HTMLButtonElement>('[data-action="resume"]')!.click();
    expect(h.qs.isOpen).toBe(false);
    vi.advanceTimersByTime(1500);
    expect(h.onResume).toHaveBeenCalledTimes(1);
  });
});

describe("QuickSettings values", () => {
  it("lays out the sound rows in order and reads values when a panel opens", () => {
    const h = setup();
    const rows = [...h.dialog("sound").querySelectorAll<HTMLElement>("[data-row]")].map((row) => row.dataset.row);
    expect(rows).toEqual(["master", "music", "effects", "keyboard", "keyboardVolume", "voice", "ui"]);
    h.values.music = 15;
    h.qs.open("sound");
    expect(h.row("music").querySelector<HTMLInputElement>("input[type=range]")!.value).toBe("15");
    h.values.voice = 5;
    h.qs.refresh();
    expect(h.row("voice").querySelector(".kit-qs__num")!.textContent).toBe("5");
  });

  it("sends slider changes at once and previews at most every 150 ms", () => {
    const h = setup();
    h.qs.open("sound");
    const range = h.row("master").querySelector<HTMLInputElement>("input[type=range]")!;
    for (const value of [50, 40, 30]) slide(range, value);
    expect(h.onChange.mock.calls).toEqual([["master", 50], ["master", 40], ["master", 30]]);
    expect(h.onPreview.mock.calls).toEqual([["master"]]);
    vi.advanceTimersByTime(150);
    expect(h.onPreview.mock.calls).toEqual([["master"], ["master"]]);
    vi.advanceTimersByTime(300);
    expect(h.onPreview).toHaveBeenCalledTimes(2);
  });

  it("previews a keyboard profile when chosen and keeps pending packs unselectable", () => {
    const h = setup({
      keyboardProfiles: [
        { value: "off", label: "Off" },
        { value: "creamy", label: "Creamy" },
        { value: "thock", label: "Thock" },
        { value: "dome", label: "Soft Dome", disabled: true },
      ],
    });
    h.qs.open("sound");
    choose(h.row("keyboard"), "thock");
    expect(h.onChange).toHaveBeenLastCalledWith("keyboard", "thock");
    expect(h.onPreview).toHaveBeenLastCalledWith("keyboard");
    const pending = h.row("keyboard").querySelector<HTMLButtonElement>('button[data-value="dome"]')!;
    expect(pending.disabled).toBe(true);
    expect(pending.textContent).toBe("Soft Dome pending");
  });

  it("toggles switches and settings choices", () => {
    const h = setup();
    h.qs.open("settings");
    const motion = h.row("reducedMotion").querySelector<HTMLButtonElement>('[role="switch"]')!;
    expect(motion.getAttribute("aria-checked")).toBe("false");
    motion.click();
    expect(h.onChange).toHaveBeenLastCalledWith("reducedMotion", true);
    expect(motion.getAttribute("aria-checked")).toBe("true");
    expect(motion.textContent).toBe("On");
    expect(h.qs.root.classList.contains("kit-qs--still")).toBe(true);
    choose(h.row("fxStyle"), "rune");
    expect(h.onChange).toHaveBeenLastCalledWith("fxStyle", "rune");
    expect(h.onPreview).not.toHaveBeenCalled();
  });

  it("mounts the preview and game slots only while Settings is open", () => {
    const stop = vi.fn();
    const mountPreview = vi.fn((host: HTMLElement) => {
      host.append(document.createElement("canvas"));
      return stop;
    });
    const h = setup({ mountPreview, gameRows: [{ kind: "toggle", id: "hints", label: "Hints" }] });
    expect(mountPreview).not.toHaveBeenCalled();
    h.qs.open("settings");
    const slot = h.row("fxPreview").querySelector<HTMLElement>(".kit-qs__slot")!;
    expect(mountPreview).toHaveBeenCalledWith(slot);
    expect(h.row("hints")).not.toBeNull();
    h.qs.close();
    expect(stop).toHaveBeenCalledTimes(1);
    expect(slot.childElementCount).toBe(0);
  });
});

describe("QuickSettings icons", () => {
  it("swaps the Sound icon when muted or at zero", () => {
    const h = setup({ icons: ICONS });
    const sound = h.corner("sound");
    expect(h.corner("settings").querySelector("img")!.getAttribute("src")).toBe(ICONS["hud-settings"]);
    expect(sound.querySelector("img")!.getAttribute("src")).toBe(ICONS["hud-sound"]);
    expect(sound.getAttribute("aria-label")).toBe("Sound");
    h.qs.open("sound");
    const mute = h.row("master").querySelector<HTMLButtonElement>('[data-toggle="muted"]')!;
    mute.click();
    expect(h.onChange).toHaveBeenLastCalledWith("muted", true);
    expect(mute.getAttribute("aria-pressed")).toBe("true");
    expect(sound.querySelector("img")!.getAttribute("src")).toBe(ICONS["hud-sound-muted"]);
    expect(sound.getAttribute("aria-label")).toBe("Sound off");
    mute.click();
    expect(sound.querySelector("img")!.getAttribute("src")).toBe(ICONS["hud-sound"]);
    slide(h.row("master").querySelector<HTMLInputElement>("input[type=range]")!, 0);
    expect(sound.querySelector("img")!.getAttribute("src")).toBe(ICONS["hud-sound-muted"]);
    // The Master row's own speaker follows the corner (its mutedIcon), then comes back above 0.
    expect(h.row("master").querySelector(".kit-qs__icon-cell img")!.getAttribute("src")).toBe(ICONS["hud-sound-muted"]);
    slide(h.row("master").querySelector<HTMLInputElement>("input[type=range]")!, 40);
    expect(h.row("master").querySelector(".kit-qs__icon-cell img")!.getAttribute("src")).toBe(ICONS["vol-master"]);
    expect(h.row("music").querySelector(".kit-qs__icon-cell")!.childElementCount).toBe(0);
  });

  it("falls back to plain text without art and never draws an icon", () => {
    const h = setup();
    expect(h.corner("settings").textContent).toBe("Settings");
    expect(h.corner("sound").textContent).toBe("Sound");
    h.values.muted = true;
    h.qs.refresh();
    expect(h.corner("sound").textContent).toBe("Sound off");
    expect(h.qs.root.querySelectorAll("img, svg, canvas")).toHaveLength(0);
    h.qs.setIcons({ "hud-settings": ICONS["hud-settings"] });
    const img = h.corner("settings").querySelector("img")!;
    expect(img.getAttribute("src")).toBe(ICONS["hud-settings"]);
    img.dispatchEvent(new Event("error"));
    expect(h.corner("settings").textContent).toBe("Settings");
    expect(h.corner("settings").querySelector("img")).toBeNull();
  });

  it("applies skin images as CSS variables", () => {
    const h = setup({ skin: { panel: `${ART}frame.png`, sliderThumb: `${ART}thumb.png` } });
    expect(h.qs.root.classList.contains("kit-qs--skin-panel")).toBe(true);
    expect(h.qs.root.classList.contains("kit-qs--skin-slider")).toBe(true);
    expect(h.qs.root.classList.contains("kit-qs--skin-button")).toBe(false);
    expect(h.qs.root.style.getPropertyValue("--kit-qs-skin-panel")).toContain("frame.png");
  });
});

describe("QuickSettings destroy", () => {
  it("removes the layer, the dialogs and the key listeners without callbacks", () => {
    const h = setup({ mountPreview: () => () => {} });
    h.qs.open("settings");
    h.qs.destroy();
    expect(h.host.querySelector(".kit-qs")).toBeNull();
    expect(document.querySelector('[aria-modal="true"]')).toBeNull();
    expect(h.qs.isOpen).toBe(false);
    expect(h.qs.blocking).toBe(false);
    expect(press(h.input, "F1").defaultPrevented).toBe(false);
    press(h.input, "x");
    expect(h.gameKeys).toEqual(["keydown:F1", "keydown:x"]);
    h.qs.open("sound");
    expect(h.qs.isOpen).toBe(false);
    vi.advanceTimersByTime(2000);
    expect(h.onResume).not.toHaveBeenCalled();
  });
});

describe("QuickSettings choice options after the catalogue (setChoiceOptions)", () => {
  const OFF: KeyboardSoundChoice = { value: "off", label: "Off" };
  const RELAY: KeyboardSoundChoice = { value: "relay", label: "Relay" };
  const pack = (id: string): KeyboardSoundChoice => ({ value: id, label: id.toUpperCase(), family: "Feel", manifest: `/v1/keys/sets/${id}/f/keys-manifest.json`, preview: `/v1/keys/sets/${id}/f/preview.ogg` });
  const CATALOG = { state: "ready" as const, options: [OFF, RELAY, pack("creamy"), pack("deep")] };
  const listed = (h: Harness) => [...h.row("keyboard").querySelectorAll<HTMLButtonElement>('button[role="option"]')];
  // Choosing a set previews and loads it: keep that off the network.
  const fetch = vi.fn(async (url: string) => { throw new Error(`offline: ${url}`); });
  beforeEach(() => vi.stubGlobal("fetch", fetch));
  afterEach(() => vi.unstubAllGlobals());

  it("placeholder options without the saved set make the kit overwrite it (the bug pendingKeyboardChoices avoids)", () => {
    const h = setup({ keyboardProfiles: [OFF, RELAY] });
    expect(h.onChange).toHaveBeenCalledWith("keyboard", "relay");
  });

  it("a panel built before the catalogue keeps the saved set as Loading…, then lists the sets in place", () => {
    const h = setup({ keyboardProfiles: pendingKeyboardChoices("creamy", RELAY) });
    expect(h.onChange).not.toHaveBeenCalled();
    expect(listed(h).map((b) => [b.textContent, b.disabled, b.getAttribute("aria-selected")])).toEqual([["Off", false, "false"], ["Relay", false, "false"], ["Loading…", true, "true"]]);
    const settled = settleKeyboardChoice(String(h.values.keyboard), CATALOG, RELAY);
    expect(h.qs.setChoiceOptions("keyboard", settled.options)).toBe(true);
    expect(h.onChange).not.toHaveBeenCalled();
    expect(h.values.keyboard).toBe("creamy");
    expect(listed(h).map((b) => b.dataset.value)).toEqual(["off", "relay", "creamy", "deep"]);
    expect(listed(h).find((b) => b.getAttribute("aria-selected") === "true")?.dataset.value).toBe("creamy");
    expect(h.row("keyboard").querySelectorAll(".kit-keyboards")).toHaveLength(1);
    // The new list is live: a choice saves at once, and icons reach its Listen buttons.
    choose(h.row("keyboard"), "deep");
    expect(h.onChange).toHaveBeenLastCalledWith("keyboard", "deep");
    h.qs.setIcons({ "hud-sound": `${ART}listen.png` });
    expect(h.row("keyboard").querySelector<HTMLImageElement>(".kit-keyboards__listen img")?.getAttribute("src")).toBe(`${ART}listen.png`);
  });

  it("while the Sound panel is open, focus stays on the option the player was on, in the new list", () => {
    const h = setup({ keyboardProfiles: pendingKeyboardChoices("creamy", RELAY), countdownMs: 0 });
    h.qs.open("sound");
    listed(h)[1]!.focus();
    expect(h.row("keyboard").contains(document.activeElement)).toBe(true);
    h.qs.setChoiceOptions("keyboard", settleKeyboardChoice("creamy", CATALOG, RELAY).options);
    expect(h.qs.isOpen).toBe(true);
    // Relay, not the selected set: a rebuild never moves keyboard focus.
    expect((document.activeElement as HTMLElement | null)?.dataset.value).toBe("relay");
    expect(listed(h).find((b) => b.getAttribute("aria-selected") === "true")?.dataset.value).toBe("creamy");
  });

  it("new options that lack the saved id repair it through onChange, as at construction", () => {
    const h = setup({ keyboardProfiles: pendingKeyboardChoices("creamy", RELAY) });
    h.qs.setChoiceOptions("keyboard", [OFF, RELAY, pack("deep")]);
    expect(h.onChange).toHaveBeenCalledWith("keyboard", "relay");
  });

  it("a radio choice row takes new options too; an unknown row or a destroyed panel: false", () => {
    const h = setup();
    expect(h.qs.setChoiceOptions("quality", [{ value: "low", label: "Low" }, { value: "high", label: "High" }])).toBe(true);
    const radios = [...h.row("quality").querySelectorAll<HTMLInputElement>('input[type="radio"]')];
    expect(radios.map((r) => [r.value, r.checked])).toEqual([["low", false], ["high", true]]);
    expect(h.qs.setChoiceOptions("nope", [])).toBe(false);
    h.qs.destroy();
    expect(h.qs.setChoiceOptions("quality", [{ value: "low", label: "Low" }])).toBe(false);
  });
});
