// @vitest-environment happy-dom
// Judges' fixes of 31/10 (evening) on the quick panels: knob over the groove art, title context, list edges and
// snapping, Listen buttons out of the Tab order, list hover, button and label fonts.
import { afterEach, describe, expect, it, vi } from "vitest";
import { KEYBOARD_CHOICES_CSS, KeyboardSoundChoices } from "./keyboard-choices";
import { QUICK_SETTINGS_CSS, QUICK_SETTINGS_VARS } from "./css";
import { QuickSettings, type QuickSettingsOptions } from "./quick-settings";
import { defaultSettingsRows } from "./rows";
import type { QuickChoiceOption, QuickContext, QuickValue } from "./types";

const ART = "https://art.example.test/";
const cleanups: (() => void)[] = [];
afterEach(() => {
  for (const cleanup of cleanups.splice(0).reverse()) cleanup();
  vi.restoreAllMocks();
});

const SETS: QuickChoiceOption[] = [
  { value: "off", label: "Off" },
  ...["creamy", "thock", "marbly", "clack", "dome"].map((value) => ({ value, label: value[0]!.toUpperCase() + value.slice(1), preview: `${ART}${value}.ogg` })),
];

function make(extra: Partial<QuickSettingsOptions> = {}, start: Record<string, QuickValue> = {}) {
  const host = document.createElement("div");
  document.body.append(host);
  const values: Record<string, QuickValue> = { master: 80, muted: false, music: 40, effects: 50, keyboardVolume: 70, voice: 25, ui: 65, keyboard: "marbly", ...start };
  const qs = new QuickSettings({ host, keyboardProfiles: SETS, getValues: () => values, onChange: (id, value) => { values[id] = value; }, countdownMs: 0, ...extra });
  cleanups.push(() => { qs.destroy(); host.remove(); });
  const dialog = (panel: "settings" | "sound") => qs.root.querySelector<HTMLElement>(`.kit-qs__dialog[data-panel="${panel}"]`)!;
  const action = (id: string) => dialog("settings").querySelector<HTMLButtonElement>(`[data-action="${id}"]`)!;
  return { qs, values, dialog, action, root: qs.root };
}

function sheet(css: string): void {
  const style = document.createElement("style");
  style.textContent = css;
  document.head.append(style);
  cleanups.push(() => style.remove());
}

/** What Tab would visit in `scope`, in order: enabled, not hidden, tabIndex ≥ 0. */
function tabOrder(scope: HTMLElement): HTMLElement[] {
  return [...scope.querySelectorAll<HTMLElement>("button, input, [tabindex]")].filter(
    (el) => el.tabIndex >= 0 && !(el as HTMLButtonElement).disabled && el.closest("[hidden]") === null,
  );
}

function rect(top: number, height: number): DOMRect {
  return { top, bottom: top + height, left: 0, right: 200, height, width: 200, x: 0, y: top, toJSON: () => ({}) } as DOMRect;
}

describe("the knob is drawn over the groove and fill art", () => {
  it("lifts the range above both art layers (z-index 1 over 0), at rest, with no hover or focus filter", () => {
    expect(QUICK_SETTINGS_CSS).toContain(".kit-qs--slider-fill .kit-qs__range{position:relative;z-index:1}");
    expect(QUICK_SETTINGS_CSS).toMatch(/\.kit-qs--slider-fill \.kit-qs__groove,\.kit-qs--slider-fill \.kit-qs__fill\{display:block;position:absolute;z-index:0;/);
    sheet(QUICK_SETTINGS_CSS);
    const h = make({ skin: { sliderTrack: `${ART}track.png`, sliderFill: `${ART}fill.png`, sliderThumb: `${ART}thumb.png` } });
    h.qs.open("sound");
    for (const value of [0, 50, 100]) {
      h.values.music = value;
      h.qs.refresh();
      const slider = h.dialog("sound").querySelector<HTMLElement>('[data-row="music"] .kit-qs__slider')!;
      const range = slider.querySelector<HTMLElement>(".kit-qs__range")!;
      const layers = [slider.querySelector<HTMLElement>(".kit-qs__groove")!, slider.querySelector<HTMLElement>(".kit-qs__fill")!];
      expect(getComputedStyle(range).position).toBe("relative");
      expect(Number(getComputedStyle(range).zIndex)).toBeGreaterThan(Math.max(...layers.map((layer) => Number(getComputedStyle(layer).zIndex))));
      // The range is the last child: at the same level it would paint over the layers anyway.
      expect(slider.lastElementChild).toBe(range);
      expect(slider.style.getPropertyValue("--kit-qs-v")).toBe((value / 100).toFixed(4));
    }
  });
});

describe("title context: Resume and Quit to title only in play", () => {
  it("shows both in play (the default) and hides them, with their row, on the title", () => {
    const h = make();
    expect(h.qs.context).toBe("play");
    expect(h.action("resume").hidden).toBe(false);
    expect(h.action("quit").hidden).toBe(false);
    h.qs.setContext("title");
    expect(h.qs.context).toBe("title");
    expect(h.root.dataset.context).toBe("title");
    expect(h.action("resume").hidden).toBe(true);
    expect(h.action("quit").hidden).toBe(true);
    expect(h.action("resume").closest<HTMLElement>(".kit-qs__actions")!.hidden).toBe(true);
    h.qs.open("settings");
    expect(tabOrder(h.dialog("settings")).some((el) => el.dataset.action !== undefined)).toBe(false);
    h.qs.setContext("play");
    expect(h.action("resume").hidden).toBe(false);
    expect(h.action("quit").hidden).toBe(false);
    expect(h.action("resume").closest<HTMLElement>(".kit-qs__actions")!.hidden).toBe(false);
  });

  it("reads a context function on each open and refresh", () => {
    let where: QuickContext = "title";
    const h = make({ context: () => where });
    expect(h.action("quit").hidden).toBe(true);
    where = "play";
    h.qs.open("settings");
    expect(h.action("quit").hidden).toBe(false);
    h.qs.close();
    where = "title";
    h.qs.refresh();
    expect(h.action("quit").hidden).toBe(true);
    expect(h.action("resume").hidden).toBe(true);
  });

  it("keeps a game's own button on the title, and its row", () => {
    const rows = [...defaultSettingsRows(), { kind: "button" as const, id: "credits", label: "Credits", action: () => {} }];
    const h = make({ settingsRows: rows, context: "title" });
    expect(h.action("credits").hidden).toBe(false);
    expect(h.action("credits").closest<HTMLElement>(".kit-qs__actions")!.hidden).toBe(false);
    expect(h.action("resume").hidden).toBe(true);
  });

  it("moves focus from a button that hides to Close", () => {
    const h = make();
    h.qs.open("settings");
    h.action("resume").focus();
    h.qs.setContext("title");
    expect(document.activeElement).toBe(h.dialog("settings").querySelector(".kit-qs__close"));
  });
});

describe("keyboard list edges: fades where rows go on, snapping, the selection in the middle", () => {
  it("fades an edge only while more rows lie beyond it", () => {
    expect(KEYBOARD_CHOICES_CSS).toContain("mask-image:linear-gradient(to bottom,transparent,#000 var(--kit-kb-fade-top),#000 calc(100% - var(--kit-kb-fade-bottom)),transparent)");
    expect(KEYBOARD_CHOICES_CSS).toContain("--kit-kb-fade:calc(10px * var(--kit-qs-s,1))");
    expect(KEYBOARD_CHOICES_CSS).toContain(".kit-keyboards[data-more-above]{--kit-kb-fade-top:var(--kit-kb-fade)}");
    expect(KEYBOARD_CHOICES_CSS).toContain(".kit-keyboards[data-more-below]{--kit-kb-fade-bottom:var(--kit-kb-fade)}");
    const list = new KeyboardSoundChoices({ document, options: SETS, label: "Keyboard sound", onSelect: () => {}, onPreview: () => {}, onStop: () => {} });
    document.body.append(list.element);
    cleanups.push(() => list.destroy());
    const el = list.element;
    Object.defineProperty(el, "clientHeight", { configurable: true, value: 100 });
    Object.defineProperty(el, "scrollHeight", { configurable: true, value: 204 });
    el.scrollTop = 0;
    el.dispatchEvent(new Event("scroll"));
    expect([el.hasAttribute("data-more-above"), el.hasAttribute("data-more-below")]).toEqual([false, true]);
    el.scrollTop = 50;
    el.dispatchEvent(new Event("scroll"));
    expect([el.hasAttribute("data-more-above"), el.hasAttribute("data-more-below")]).toEqual([true, true]);
    el.scrollTop = 104;
    el.dispatchEvent(new Event("scroll"));
    expect([el.hasAttribute("data-more-above"), el.hasAttribute("data-more-below")]).toEqual([true, false]);
  });

  it("snaps rows and family headings to the top, past the fade", () => {
    expect(KEYBOARD_CHOICES_CSS).toContain("scroll-snap-type:y proximity;scroll-padding-block:var(--kit-kb-fade)");
    expect(KEYBOARD_CHOICES_CSS).toContain(".kit-keyboards__list .kit-keyboards__option,.kit-keyboards__list .kit-keyboards__family{scroll-snap-align:start}");
  });

  it("arrowing down past the view stops on a row's snap position with the row in view; up brings a family heading along", () => {
    const options = [SETS[0]!, ...["a", "b", "c", "d", "e", "f", "g", "h"].map((value, i) => ({ value, label: value, family: i < 4 ? "Deep" : "Warm" }))];
    const list = new KeyboardSoundChoices({ document, options, label: "Keyboard sound", onSelect: () => {}, onPreview: () => {}, onStop: () => {} });
    document.body.append(list.element);
    cleanups.push(() => list.destroy());
    const el = list.element;
    // A 120 px view at y = 100; rows 34 px, headings 28 px, in list order from content y = 0.
    Object.defineProperty(el, "clientHeight", { configurable: true, value: 120 });
    vi.spyOn(el, "getBoundingClientRect").mockReturnValue(rect(100, 120));
    let y = 0;
    for (const item of el.querySelectorAll<HTMLElement>(".kit-keyboards__list .kit-keyboards__option, .kit-keyboards__list .kit-keyboards__family")) {
      const at = y;
      const height = item.classList.contains("kit-keyboards__family") ? 28 : 34;
      vi.spyOn(item, "getBoundingClientRect").mockImplementation(() => rect(100 + at - el.scrollTop, height));
      y += height;
    }
    const option = (value: string) => el.querySelector<HTMLButtonElement>(`[role="option"][data-value="${value}"]`)!;
    // Off 0, Deep 34, a 62, b 96, c 130, d 164, Warm 198, e 226 ...
    option("b").focus();
    option("b").dispatchEvent(new KeyboardEvent("keydown", { key: "ArrowDown", bubbles: true }));
    expect(document.activeElement).toBe(option("c"));
    // c ends at 164: the smallest snap at or past 164 - 120 = 44 is a's top, 62.
    expect(el.scrollTop).toBe(62);
    option("c").dispatchEvent(new KeyboardEvent("keydown", { key: "ArrowDown", bubbles: true }));
    option("d").dispatchEvent(new KeyboardEvent("keydown", { key: "ArrowDown", bubbles: true }));
    expect(document.activeElement).toBe(option("e"));
    // e ends at 260: the smallest snap at or past 140 is d's top, 164 (view 164..284 holds e at 226..260).
    expect(el.scrollTop).toBe(164);
    // d is in view: arrowing up to it does not scroll.
    option("e").dispatchEvent(new KeyboardEvent("keydown", { key: "ArrowUp", bubbles: true }));
    expect(document.activeElement).toBe(option("d"));
    expect(el.scrollTop).toBe(164);
    el.scrollTop = 120;
    option("d").dispatchEvent(new KeyboardEvent("keydown", { key: "ArrowUp", bubbles: true }));
    option("c").dispatchEvent(new KeyboardEvent("keydown", { key: "ArrowUp", bubbles: true }));
    option("b").dispatchEvent(new KeyboardEvent("keydown", { key: "ArrowUp", bubbles: true }));
    expect(document.activeElement).toBe(option("a"));
    // a is the first of Deep: the list shows the heading above it (34).
    expect(el.scrollTop).toBe(34);
  });
});

describe("Listen buttons stay out of the Tab order but the current row's", () => {
  it("Tab from the list reaches Keyboard volume within 2 presses", () => {
    const h = make();
    h.qs.open("sound");
    const order = tabOrder(h.dialog("sound"));
    const listens = order.filter((el) => el.classList.contains("kit-keyboards__listen"));
    expect(listens.map((el) => el.dataset.listen)).toEqual(["marbly"]);
    const option = order.findIndex((el) => el.getAttribute("role") === "option");
    const volume = order.findIndex((el) => el.id.endsWith("-keyboardVolume"));
    expect(order[option]!.dataset.value).toBe("marbly");
    expect(volume).toBeGreaterThan(option);
    expect(volume - option).toBeLessThanOrEqual(2);
    // Every Listen button is still in the document for the pointer and screen readers.
    expect(h.dialog("sound").querySelectorAll(".kit-keyboards__listen")).toHaveLength(5);
  });

  it("the tabbable Listen button follows the focused row, and Off (no preview) leaves none", () => {
    const h = make();
    h.qs.open("sound");
    const sound = h.dialog("sound");
    const option = (value: string) => sound.querySelector<HTMLButtonElement>(`[role="option"][data-value="${value}"]`)!;
    const tabbableListens = () => tabOrder(sound).filter((el) => el.classList.contains("kit-keyboards__listen")).map((el) => el.dataset.listen);
    option("dome").focus();
    expect(tabbableListens()).toEqual(["dome"]);
    option("off").focus();
    expect(tabbableListens()).toEqual([]);
    // A Listen button can still take focus by pointer or script.
    const listen = sound.querySelector<HTMLButtonElement>('[data-listen="thock"]')!;
    listen.focus();
    expect(document.activeElement).toBe(listen);
  });
});

describe("list hover and fonts", () => {
  it("hover lights a list plate through --kit-qs-list-hover-filter (brighter, with the glow)", () => {
    expect(QUICK_SETTINGS_VARS["--kit-qs-list-hover-filter"]).toBe("brightness(1.3) drop-shadow(0 0 calc(5px * var(--kit-qs-s)) var(--kit-qs-glow))");
    expect(QUICK_SETTINGS_CSS).toContain("--kit-qs-list-hover-filter:brightness(1.3) drop-shadow(0 0 calc(5px * var(--kit-qs-s)) var(--kit-qs-glow));");
    expect(KEYBOARD_CHOICES_CSS).toContain(".kit-qs.kit-qs--skin-list .kit-keyboards button.kit-keyboards__option:hover:not(:disabled)::before{filter:var(--kit-qs-list-hover-filter,");
  });

  it("buttons, chips, corner text and keyboard rows read --kit-qs-button-font; labels and headings --kit-qs-label-font; notes stay in the battle font", () => {
    expect(QUICK_SETTINGS_CSS).toContain(".kit-qs .kit-qs__btn,.kit-qs .kit-qs__chip,.kit-qs .kit-qs__corner,.kit-qs .kit-keyboards button.kit-keyboards__option{font-family:var(--kit-qs-button-font,inherit)}");
    expect(QUICK_SETTINGS_CSS).toContain(".kit-qs__label{font-family:var(--kit-qs-label-font,inherit);");
    expect(QUICK_SETTINGS_CSS).toMatch(/\.kit-qs__heading\{[^}]*font-family:var\(--kit-qs-label-font,inherit\)/);
    expect(QUICK_SETTINGS_CSS).toContain(".kit-qs .kit-keyboards .kit-keyboards__family{font-family:var(--kit-qs-label-font,inherit)}");
    expect(QUICK_SETTINGS_CSS).toContain('.kit-qs .kit-qs__note,.kit-qs .kit-keyboards__note{font-family:var(--kit-qs-note-font,var(--kit-font-battle,"Be Vietnam Pro","Segoe UI",system-ui,sans-serif))}');
    // Unset, every part keeps the panel's font (no new default face).
    expect(Object.keys(QUICK_SETTINGS_VARS)).not.toContain("--kit-qs-button-font");
    expect(Object.keys(QUICK_SETTINGS_VARS)).not.toContain("--kit-qs-label-font");
    sheet(QUICK_SETTINGS_CSS);
    const h = make();
    h.root.style.setProperty("--kit-qs-button-font", '"Display Face", serif');
    h.root.style.setProperty("--kit-qs-label-font", '"Label Face", serif');
    const family = (el: Element) => getComputedStyle(el).fontFamily;
    expect(family(h.action("resume"))).toContain("Display Face");
    expect(family(h.dialog("sound").querySelector(".kit-qs__label")!)).toContain("Label Face");
  });
});
