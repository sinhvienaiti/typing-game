// @vitest-environment happy-dom
// Kit pass of 31/10 on the quick panels: slider fill layer, Mute column, list plates, row icons, icon Close, focus glow, title font.
import { afterEach, describe, expect, it } from "vitest";
import { KEYBOARD_CHOICES_CSS, KeyboardSoundChoices } from "./keyboard-choices";
import { QUICK_FILL_FROM_TRACK_FILTER, QUICK_SETTINGS_CSS, QUICK_SETTINGS_VARS } from "./css";
import * as quick from "./index";
import { QuickSettings, type QuickSettingsOptions } from "./quick-settings";
import { defaultSettingsRows, defaultSoundRows } from "./rows";
import { QUICK_ICON_NAMES, QUICK_ROW_ICON_NAMES, type QuickRow, type QuickValue } from "./types";

const ART = "https://art.example.test/";
const cleanups: (() => void)[] = [];
afterEach(() => {
  for (const cleanup of cleanups.splice(0).reverse()) cleanup();
});

function make(extra: Partial<QuickSettingsOptions> = {}, start: Record<string, QuickValue> = {}) {
  const host = document.createElement("div");
  document.body.append(host);
  const values: Record<string, QuickValue> = { master: 80, muted: false, music: 0, effects: 50, keyboardVolume: 100, voice: 25, ui: 65, keyboard: "creamy", ...start };
  const qs = new QuickSettings({ host, getValues: () => values, onChange: (id, value) => { values[id] = value; }, countdownMs: 0, ...extra });
  cleanups.push(() => { qs.destroy(); host.remove(); });
  const dialog = (panel: "settings" | "sound") => qs.root.querySelector<HTMLElement>(`.kit-qs__dialog[data-panel="${panel}"]`)!;
  const row = (id: string) => qs.root.querySelector<HTMLElement>(`[data-row="${id}"]`)!;
  return { qs, values, dialog, row, root: qs.root };
}

function slide(range: HTMLInputElement, value: number): void {
  range.value = String(value);
  range.dispatchEvent(new Event("input", { bubbles: true }));
}

/** A style sheet in the document for computed-style checks; removed after the test. */
function sheet(css: string): void {
  const style = document.createElement("style");
  style.textContent = css;
  document.head.append(style);
  cleanups.push(() => style.remove());
}

describe("slider fill layer (QuickSkin.sliderFill / sliderEmpty, --kit-qs-v)", () => {
  it("wraps every native range with an empty-groove and a fill layer that screen readers skip", () => {
    const h = make();
    const master = h.row("master");
    const slider = master.querySelector<HTMLElement>(".kit-qs__slider")!;
    const range = slider.querySelector<HTMLInputElement>("input.kit-qs__range")!;
    expect([...slider.children].map((child) => child.className)).toEqual(["kit-qs__groove", "kit-qs__fill", "kit-qs__range"]);
    expect(slider.querySelector(".kit-qs__groove")!.getAttribute("aria-hidden")).toBe("true");
    expect(slider.querySelector(".kit-qs__fill")!.getAttribute("aria-hidden")).toBe("true");
    // The range keeps its type, bounds and label.
    expect(range.type).toBe("range");
    expect([range.min, range.max, range.step]).toEqual(["0", "100", "1"]);
    expect(master.querySelector<HTMLLabelElement>("label.kit-qs__label")!.htmlFor).toBe(range.id);
    expect(range.closest(".kit-qs__control")!.classList.contains("kit-qs__control--slider")).toBe(true);
  });

  it("sets --kit-qs-v (0..1) on the wrapper from the value, on input and on refresh, within the row's own bounds", () => {
    const rows: QuickRow[] = [{ kind: "slider", id: "speed", label: "Speed", min: 50, max: 150, step: 10 }];
    const h = make({ soundRows: [...defaultSoundRows(), ...rows] }, { speed: 75 });
    const v = (id: string) => h.row(id).querySelector<HTMLElement>(".kit-qs__slider")!.style.getPropertyValue("--kit-qs-v");
    expect(v("master")).toBe("0.8000");
    expect(v("music")).toBe("0.0000");
    expect(v("keyboardVolume")).toBe("1.0000");
    expect(v("speed")).toBe("0.3000"); // 75 snaps to 80: (80 - 50) / 100
    h.qs.open("sound");
    slide(h.row("effects").querySelector<HTMLInputElement>(".kit-qs__range")!, 25);
    expect(v("effects")).toBe("0.2500");
    h.values.voice = 100;
    h.qs.refresh();
    expect(v("voice")).toBe("1.0000");
  });

  it("is off without sliderFill and sliderEmpty, so a game that sets neither looks as before", () => {
    const h = make({ skin: { sliderTrack: `${ART}track.png`, sliderThumb: `${ART}thumb.png` } });
    expect(h.root.classList.contains("kit-qs--skin-slider")).toBe(true);
    expect(h.root.classList.contains("kit-qs--slider-fill")).toBe(false);
    expect(h.root.style.getPropertyValue("--kit-qs-skin-fill")).toBe("");
    sheet(QUICK_SETTINGS_CSS);
    expect(getComputedStyle(h.row("master").querySelector(".kit-qs__fill")!).display).toBe("none");
    expect(getComputedStyle(h.row("master").querySelector(".kit-qs__groove")!).display).toBe("none");
  });

  it("sliderEmpty alone: the empty groove is that art, the fill is the track art (lit by the default filter)", () => {
    const h = make({ skin: { sliderTrack: `${ART}track.png`, sliderEmpty: `${ART}empty.png` } });
    const { classList, style } = h.root;
    expect(classList.contains("kit-qs--slider-fill")).toBe(true);
    expect(classList.contains("kit-qs--empty-art")).toBe(true);
    expect(classList.contains("kit-qs--fill-art")).toBe(false);
    expect(style.getPropertyValue("--kit-qs-skin-empty")).toBe(`url("${ART}empty.png")`);
    expect(style.getPropertyValue("--kit-qs-skin-fill")).toBe(`url("${ART}track.png")`);
    sheet(QUICK_SETTINGS_CSS);
    expect(getComputedStyle(h.row("music").querySelector(".kit-qs__fill")!).display).toBe("block");
    expect(QUICK_SETTINGS_CSS).toContain(`:where(.kit-qs--slider-fill:not(.kit-qs--fill-art)){--kit-qs-fill-filter:${QUICK_FILL_FROM_TRACK_FILTER}}`);
  });

  it("sliderFill alone: the fill is that art, the empty groove the track art; without any track art it is none", () => {
    const h = make({ skin: { sliderTrack: `${ART}track.png`, sliderFill: `${ART}fill.png` } });
    expect(h.root.classList.contains("kit-qs--fill-art")).toBe(true);
    expect(h.root.style.getPropertyValue("--kit-qs-skin-fill")).toBe(`url("${ART}fill.png")`);
    expect(h.root.style.getPropertyValue("--kit-qs-skin-empty")).toBe(`url("${ART}track.png")`);
    const bare = make({ skin: { sliderFill: `${ART}fill.png` } });
    // A fill layer needs the custom range look, track art or not.
    expect(bare.root.classList.contains("kit-qs--skin-slider")).toBe(true);
    expect(bare.root.style.getPropertyValue("--kit-qs-skin-empty")).toBe("none");
  });

  it("draws both layers in three slices and clips the fill at the knob's centre; the range's own track is cleared over them", () => {
    expect(QUICK_SETTINGS_CSS).toContain(".kit-qs--slider-fill .kit-qs__groove{border-image:var(--kit-qs-skin-empty,none) var(--kit-qs-groove-slice) fill / 0 var(--kit-qs-groove-cap) / 0 stretch;filter:var(--kit-qs-empty-filter)}");
    expect(QUICK_SETTINGS_CSS).toContain("border-image:var(--kit-qs-skin-fill,none) var(--kit-qs-fill-slice,var(--kit-qs-groove-slice)) fill / 0 var(--kit-qs-fill-cap,var(--kit-qs-groove-cap)) / 0 stretch");
    expect(QUICK_SETTINGS_CSS).toContain("clip-path:inset(calc(-1 * var(--kit-qs-groove-h)) calc(100% - var(--kit-qs-knob) / 2 - var(--kit-qs-v, 0) * (100% - var(--kit-qs-knob))) calc(-1 * var(--kit-qs-groove-h)) calc(-1 * var(--kit-qs-groove-h)))");
    // Outranks a game's own `.game.kit-qs--skin-slider .kit-qs__range::-webkit-slider-runnable-track` art (0,3,1).
    expect(QUICK_SETTINGS_CSS).toContain(".kit-qs.kit-qs--slider-fill .kit-qs__slider .kit-qs__range::-webkit-slider-runnable-track{border:0;border-image:none;background:transparent}");
    expect(QUICK_SETTINGS_CSS).toContain(".kit-qs.kit-qs--slider-fill .kit-qs__slider .kit-qs__range::-moz-range-track{border:0;border-image:none;background:transparent}");
    // The knob and groove sizes the clip reads are the ones the kit draws.
    expect(QUICK_SETTINGS_CSS).toContain("width:var(--kit-qs-knob);height:var(--kit-qs-knob);margin-top:calc((var(--kit-qs-groove-h) - var(--kit-qs-knob)) / 2)");
    expect(QUICK_SETTINGS_VARS["--kit-qs-knob"]).toBe("calc(22px * var(--kit-qs-s))");
    expect(QUICK_SETTINGS_VARS["--kit-qs-groove-h"]).toBe("calc(10px * var(--kit-qs-s))");
  });
});

describe("Mute out of the groove column (.kit-qs__aside)", () => {
  it("puts the toggle in a column after the number, and gives every slider row of that panel the same column", () => {
    const h = make();
    for (const id of ["master", "music", "effects", "keyboardVolume", "voice", "ui"]) {
      const control = h.row(id).querySelector<HTMLElement>(".kit-qs__control")!;
      expect([...control.children].map((child) => child.className), id).toEqual(["kit-qs__slider", "kit-qs__num", "kit-qs__aside"]);
    }
    const mute = h.row("master").querySelector<HTMLButtonElement>(".kit-qs__aside > .kit-qs__btn")!;
    expect(mute.dataset.toggle).toBe("muted");
    expect(mute.textContent).toBe("Mute");
    expect(h.row("music").querySelector(".kit-qs__aside")!.childElementCount).toBe(0);
    // The hooks games use for the muted row still find the button and the number in the Master row.
    expect(h.row("master").querySelector('.kit-qs__btn[data-toggle="muted"]')).toBe(mute);
    expect(h.row("master").querySelector(".kit-qs__num")!.textContent).toBe("80");
  });

  it("keeps the toggle's pressed state and focus order (range, then Mute)", () => {
    const h = make();
    h.qs.open("sound");
    const mute = h.row("master").querySelector<HTMLButtonElement>('[data-toggle="muted"]')!;
    expect(mute.getAttribute("aria-pressed")).toBe("false");
    mute.click();
    expect(h.values.muted).toBe(true);
    expect(mute.getAttribute("aria-pressed")).toBe("true");
    const focusable = [...h.dialog("sound").querySelectorAll<HTMLElement>("input, button")].map((el) => el.dataset.toggle ?? el.className);
    expect(focusable.indexOf("muted")).toBe(focusable.indexOf("kit-qs__range") + 1);
  });

  it("a panel with no slider toggle has no aside column; a toggle slider in Settings gives Settings one", () => {
    const h = make();
    expect(h.dialog("settings").querySelector(".kit-qs__aside")).toBeNull();
    const own = make({ settingsRows: [
      { kind: "slider", id: "camera", label: "Camera speed", toggle: { id: "invert", label: "Invert" } },
      { kind: "slider", id: "zoom", label: "Zoom" },
    ] });
    expect(own.dialog("settings").querySelectorAll(".kit-qs__aside")).toHaveLength(2);
  });

  it("fixes the number and the toggle column, so each groove has one length", () => {
    expect(QUICK_SETTINGS_CSS).toContain(".kit-qs__control--slider{flex-wrap:nowrap}");
    expect(QUICK_SETTINGS_CSS).toContain(".kit-qs__slider{position:relative;display:flex;align-items:center;flex:1 1 0;min-width:4em}");
    expect(QUICK_SETTINGS_CSS).toContain(".kit-qs__num{flex:0 0 2.4em;");
    expect(QUICK_SETTINGS_CSS).toContain(".kit-qs__aside{flex:0 0 var(--kit-qs-aside-w);display:flex;min-width:0}");
    expect(QUICK_SETTINGS_CSS).toContain(".kit-qs__aside>.kit-qs__btn{width:100%}");
  });
});

describe("keyboard list plates (QuickSkin.listRow / listRowActive)", () => {
  const OPTIONS = [{ value: "off", label: "Off" }, { value: "creamy", label: "Creamy" }, { value: "thock", label: "Thock" }];

  it("is off without listRow and listRowActive, even with button art", () => {
    const h = make({ skin: { button: `${ART}button.png`, buttonActive: `${ART}active.png` } });
    expect(h.root.classList.contains("kit-qs--skin-list")).toBe(false);
    expect(h.root.style.getPropertyValue("--kit-qs-list-row")).toBe("");
  });

  it("sets the plates, cuts and edges from the skin, and insets the label by the wider side edge", () => {
    const h = make({ keyboardProfiles: OPTIONS, skin: {
      listRow: { url: `${ART}row.png`, slice: [64, 120, 64, 120], edge: [10, 16, 10, 16] },
      listRowActive: { url: `${ART}row-active.png`, slice: 80, edge: 12 },
    } });
    const style = h.root.style;
    expect(h.root.classList.contains("kit-qs--skin-list")).toBe(true);
    expect(h.root.classList.contains("kit-qs--list-tint")).toBe(false);
    expect(style.getPropertyValue("--kit-qs-list-row")).toBe(`url("${ART}row.png")`);
    expect(style.getPropertyValue("--kit-qs-list-slice")).toBe("64 120 64 120");
    expect(style.getPropertyValue("--kit-qs-list-edge")).toBe("10px 16px 10px 16px");
    expect(style.getPropertyValue("--kit-qs-list-text-x")).toBe("20px");
    expect(style.getPropertyValue("--kit-qs-list-row-active")).toBe(`url("${ART}row-active.png")`);
    expect(style.getPropertyValue("--kit-qs-list-active-slice")).toBe("80");
    expect(style.getPropertyValue("--kit-qs-list-active-edge")).toBe("12px");
  });

  it("a plate without a url is the button art; a missing active plate is button-active with the row's cut", () => {
    const h = make({ skin: { button: `${ART}button.png`, buttonActive: `${ART}active.png`, listRow: { slice: [170, 260], edge: [12, 18] } } });
    const style = h.root.style;
    expect(style.getPropertyValue("--kit-qs-list-row")).toBe(`url("${ART}button.png")`);
    expect(style.getPropertyValue("--kit-qs-list-row-active")).toBe(`url("${ART}active.png")`);
    expect(style.getPropertyValue("--kit-qs-list-active-slice")).toBe("170 260");
    expect(style.getPropertyValue("--kit-qs-list-active-edge")).toBe("12px 18px");
    expect(h.root.classList.contains("kit-qs--list-tint")).toBe(false);
  });

  it("no active art at all: the chosen row wears the row plate, lit (--kit-qs-list-active-filter)", () => {
    const h = make({ skin: { listRow: { url: `${ART}row.png`, slice: 40 } } });
    expect(h.root.classList.contains("kit-qs--list-tint")).toBe(true);
    expect(h.root.style.getPropertyValue("--kit-qs-list-row-active")).toBe(`url("${ART}row.png")`);
    expect(h.root.style.getPropertyValue("--kit-qs-list-edge")).toBe("12px");
    expect(KEYBOARD_CHOICES_CSS).toContain(".kit-qs.kit-qs--list-tint .kit-keyboards button.kit-keyboards__option[aria-selected=\"true\"]::before{filter:var(--kit-qs-list-active-filter)}");
  });

  it("only listRowActive: rows are the button art with the active plate's cut", () => {
    const h = make({ skin: { button: `${ART}button.png`, listRowActive: { url: `${ART}row-active.png`, slice: [30, 50], edge: 9 } } });
    expect(h.root.style.getPropertyValue("--kit-qs-list-row")).toBe(`url("${ART}button.png")`);
    expect(h.root.style.getPropertyValue("--kit-qs-list-slice")).toBe("30 50");
    expect(h.root.style.getPropertyValue("--kit-qs-list-edge")).toBe("9px");
  });

  it("bad cuts and edges fall back (slice 0, edge 12 px) instead of writing broken CSS", () => {
    const h = make({ skin: { listRow: { url: `${ART}row.png`, slice: [Number.NaN, 4], edge: [-1] } } });
    expect(h.root.style.getPropertyValue("--kit-qs-list-slice")).toBe("0");
    expect(h.root.style.getPropertyValue("--kit-qs-list-edge")).toBe("12px");
    const empty = make({ skin: { listRow: { url: `${ART}row.png`, slice: [] } } });
    expect(empty.root.style.getPropertyValue("--kit-qs-list-slice")).toBe("0");
  });

  it("with plates the list loses its web box and flat fills; a list outside a skinned panel (the Lab) keeps them", () => {
    sheet(KEYBOARD_CHOICES_CSS);
    const h = make({ keyboardProfiles: OPTIONS, skin: { listRow: { url: `${ART}row.png`, slice: 20 } } });
    const list = h.row("keyboard").querySelector<HTMLElement>(".kit-keyboards")!;
    const chosen = list.querySelector<HTMLButtonElement>('[role="option"][data-value="creamy"]')!;
    expect(chosen.getAttribute("aria-selected")).toBe("true");
    const box = getComputedStyle(list);
    expect(box.borderTopStyle === "none" || box.borderTopWidth === "0px").toBe(true);
    expect(box.borderTopLeftRadius).toBe("0px");
    expect(box.backgroundColor).toMatch(/transparent|rgba\(0, 0, 0, 0\)/);
    expect(getComputedStyle(chosen).backgroundColor).toMatch(/transparent|rgba\(0, 0, 0, 0\)/);

    const lab = new KeyboardSoundChoices({ document, options: OPTIONS, label: "Keyboard sound", onSelect: () => {}, onPreview: () => {}, onStop: () => {} });
    document.body.append(lab.element);
    cleanups.push(() => lab.destroy());
    lab.sync("creamy");
    expect(getComputedStyle(lab.element).borderTopLeftRadius).toBe("6px");
    expect(getComputedStyle(lab.element.querySelector('[data-value="creamy"]')!).backgroundColor).not.toMatch(/transparent|rgba\(0, 0, 0, 0\)/);
  });

  it("draws each plate on ::before, the chosen one on the active plate, and focus as a glow on the plate", () => {
    const option = ".kit-qs.kit-qs--skin-list .kit-keyboards button.kit-keyboards__option";
    expect(KEYBOARD_CHOICES_CSS).toContain(`${option}::before{content:"";position:absolute;inset:var(--kit-qs-list-inset,2px 0);z-index:-1;`);
    expect(KEYBOARD_CHOICES_CSS).toContain("border-image:var(--kit-qs-list-row,none) var(--kit-qs-list-slice,0) fill / var(--kit-qs-list-edge,12px) / 0 stretch");
    expect(KEYBOARD_CHOICES_CSS).toContain(`${option}[aria-selected="true"]::before{border-image:var(--kit-qs-list-row-active,none) var(--kit-qs-list-active-slice,0) fill / var(--kit-qs-list-active-edge,12px) / 0 stretch}`);
    expect(KEYBOARD_CHOICES_CSS).toContain(`${option}:focus-visible{outline:none}`);
    expect(KEYBOARD_CHOICES_CSS).toContain(`${option}[aria-selected]:focus-visible::before{filter:var(--kit-qs-glow-filter)}`);
    expect(KEYBOARD_CHOICES_CSS).toContain("color:var(--kit-qs-active-text,var(--kit-qs-text,#F3F4F6))");
    // The label keeps its ellipsis while the glow may pass the row's edge.
    expect(KEYBOARD_CHOICES_CSS).toContain("overflow:clip;overflow-clip-margin:8px;padding:0 var(--kit-qs-list-text-x,16px)");
  });
});

describe("row icons on every row", () => {
  it("every kit row that has an icon cell names an icon, and the new names stay out of the ticket-180 list games map", () => {
    const rows = [...defaultSoundRows(), ...defaultSettingsRows({ learning: { meaning: true, ipa: true } })];
    const iconRows = rows.filter((row) => row.kind === "slider" || row.kind === "choice" || row.kind === "toggle");
    expect(iconRows.filter((row) => !("icon" in row) || row.icon === undefined).map((row) => row.id)).toEqual([]);
    expect(rows.find((row) => row.id === "keyboardVolume")).toMatchObject({ icon: "vol-keyboard-volume" });
    expect(rows.find((row) => row.id === "keyboard")).toMatchObject({ icon: "vol-keyboard" });
    for (const name of QUICK_ROW_ICON_NAMES) expect(QUICK_ICON_NAMES as readonly string[]).not.toContain(name);
    expect(quick.QUICK_ROW_ICON_NAMES).toBe(QUICK_ROW_ICON_NAMES);
  });

  it("a game gives any row an icon by any name; a name without art leaves an empty cell that keeps its place", () => {
    const h = make({
      settingsRows: [
        { kind: "toggle", id: "pace", label: "Pace adapts to your typing", icon: "game-pace" },
        { kind: "choice", id: "mode", label: "Story mode", icon: "game-mode", options: [{ value: "a", label: "A" }] },
        { kind: "choice", id: "quality", label: "Quality", options: [{ value: "high", label: "High" }] },
      ],
      icons: { "game-pace": `${ART}pace.png`, "vol-keyboard-volume": `${ART}kv.png` },
    });
    expect(h.row("pace").querySelector(".kit-qs__icon-cell img")!.getAttribute("src")).toBe(`${ART}pace.png`);
    expect(h.row("keyboardVolume").querySelector(".kit-qs__icon-cell img")!.getAttribute("src")).toBe(`${ART}kv.png`);
    const mode = h.row("mode").querySelector<HTMLElement>(".kit-qs__icon-cell")!;
    expect(mode.dataset.icon).toBe("game-mode");
    expect(mode.childElementCount).toBe(0);
    // Every row keeps its icon cell first, so labels line up.
    for (const id of ["pace", "mode", "quality"]) expect(h.row(id).firstElementChild!.className).toBe("kit-qs__icon-cell");
    expect(h.row("quality").querySelector<HTMLElement>(".kit-qs__icon-cell")!.dataset.icon).toBeUndefined();
    h.qs.setIcons({ "game-mode": `${ART}mode.png` });
    expect(mode.querySelector("img")!.getAttribute("src")).toBe(`${ART}mode.png`);
  });

  it("sizes the icon cell itself and the first grid column by --kit-qs-icon-size", () => {
    expect(QUICK_SETTINGS_CSS).toContain(".kit-qs__row{display:grid;grid-template-columns:var(--kit-qs-icon-size) 9.5em minmax(0,1fr);");
    expect(QUICK_SETTINGS_CSS).toContain(".kit-qs__icon-cell{display:block;width:var(--kit-qs-icon-size);height:var(--kit-qs-icon-size)}");
    sheet(QUICK_SETTINGS_CSS);
    const h = make();
    const cell = h.row("music").querySelector<HTMLElement>(".kit-qs__icon-cell")!;
    expect(cell.childElementCount).toBe(0);
    expect(getComputedStyle(cell).display).toBe("block");
  });
});

describe("Close as an icon (QuickSkin.close)", () => {
  it("draws Close as the skin's image with the accessible name Close, in both panels", () => {
    const h = make({ skin: { close: `${ART}close.png` } });
    expect(h.root.classList.contains("kit-qs--skin-close")).toBe(true);
    for (const panel of ["settings", "sound"] as const) {
      const close = h.dialog(panel).querySelector<HTMLButtonElement>(".kit-qs__head .kit-qs__close")!;
      expect(close.classList.contains("kit-qs__close--icon")).toBe(true);
      // Out of the games' `.kit-qs__btn` plate rules while it is an icon.
      expect(close.classList.contains("kit-qs__btn")).toBe(false);
      expect(close.getAttribute("aria-label")).toBe("Close");
      expect(close.title).toBe("Close (Esc)");
      const img = close.querySelector("img")!;
      expect(img.getAttribute("src")).toBe(`${ART}close.png`);
      expect(img.alt).toBe("");
    }
    h.qs.open("sound");
    h.dialog("sound").querySelector<HTMLButtonElement>(".kit-qs__close")!.click();
    expect(h.qs.isOpen).toBe(false);
  });

  it("falls back to the text button without the skin or when the image fails", () => {
    const plain = make();
    const text = plain.dialog("sound").querySelector<HTMLButtonElement>(".kit-qs__close")!;
    expect(text.className).toBe("kit-qs__btn kit-qs__close");
    expect(text.textContent).toBe("Close");
    expect(text.hasAttribute("aria-label")).toBe(false);

    const h = make({ skin: { close: `${ART}missing.png` } });
    const close = h.dialog("settings").querySelector<HTMLButtonElement>(".kit-qs__close")!;
    close.querySelector("img")!.dispatchEvent(new Event("error"));
    for (const panel of ["settings", "sound"] as const) {
      const button = h.dialog(panel).querySelector<HTMLButtonElement>(".kit-qs__close")!;
      expect(button.textContent).toBe("Close");
      expect(button.querySelector("img")).toBeNull();
      expect(button.classList.contains("kit-qs__btn")).toBe(true);
      expect(button.classList.contains("kit-qs__close--icon")).toBe(false);
      expect(button.hasAttribute("aria-label")).toBe(false);
    }
  });

  it("sizes the icon by --kit-qs-close-size (32 px at 720p) and lets a game move it onto the frame", () => {
    expect(QUICK_SETTINGS_VARS["--kit-qs-close-size"]).toBe("calc(32px * var(--kit-qs-s))");
    expect(QUICK_SETTINGS_CSS).toContain("width:var(--kit-qs-close-size);height:var(--kit-qs-close-size)");
    expect(QUICK_SETTINGS_CSS).toContain("transform:translate(var(--kit-qs-close-x,0px),var(--kit-qs-close-y,0px))");
  });
});

describe("focus as a glow on skinned art (--kit-qs-glow)", () => {
  it("defines the glow colour from the focus colour and one glow filter that hugs the art", () => {
    expect(QUICK_SETTINGS_VARS["--kit-qs-glow"]).toBe("var(--kit-qs-focus)");
    expect(QUICK_SETTINGS_VARS["--kit-qs-glow-filter"]).toContain("drop-shadow(0 0 1px var(--kit-qs-glow))");
    expect(QUICK_SETTINGS_CSS).toContain("--kit-qs-glow:var(--kit-qs-focus);");
  });

  it("swaps the flat outline for the glow on skinned buttons, chips, knobs, icon buttons and Close; plain ones keep the outline", () => {
    const glow = "{outline:none;filter:var(--kit-qs-glow-filter)}";
    expect(QUICK_SETTINGS_CSS).toContain(`.kit-qs.kit-qs--skin-button .kit-qs__panel .kit-qs__btn:focus-visible,.kit-qs.kit-qs--skin-button .kit-qs__bar .kit-qs__corner:focus-visible${glow}`);
    expect(QUICK_SETTINGS_CSS).toContain(`.kit-qs.kit-qs--skin-button .kit-qs__panel .kit-qs__opt input:focus-visible+.kit-qs__chip${glow}`);
    expect(QUICK_SETTINGS_CSS).toContain(`.kit-qs__corner.has-icon:focus-visible${glow}`);
    expect(QUICK_SETTINGS_CSS).toContain(`.kit-qs.kit-qs--skin-close .kit-qs__head .kit-qs__close--icon:focus-visible${glow}`);
    expect(QUICK_SETTINGS_CSS).toContain(".kit-qs--skin-slider .kit-qs__range:focus-visible::-webkit-slider-thumb{filter:var(--kit-qs-glow-filter)}");
    expect(QUICK_SETTINGS_CSS).toContain(".kit-qs__btn:focus-visible{outline:2px solid var(--kit-qs-focus);outline-offset:2px}");
  });
});

describe("buttonActive and the title font", () => {
  it("a pressed or switched-on button wears buttonActive; no field, no class", () => {
    const h = make({ skin: { button: `${ART}button.png`, buttonActive: `${ART}active.png` } });
    expect(h.root.classList.contains("kit-qs--skin-button-active")).toBe(true);
    expect(h.root.style.getPropertyValue("--kit-qs-skin-button-active")).toBe(`url("${ART}active.png")`);
    expect(make().root.classList.contains("kit-qs--skin-button-active")).toBe(false);
    expect(QUICK_SETTINGS_CSS).toContain('.kit-qs--skin-button-active .kit-qs__btn[aria-pressed="true"],.kit-qs--skin-button-active .kit-qs__btn[aria-checked="true"]{border-color:transparent;background:var(--kit-qs-skin-button-active) center/100% 100% no-repeat transparent;color:var(--kit-qs-active-text)}');
  });

  it("the title reads --kit-qs-title-font, else the panel's own font", () => {
    expect(QUICK_SETTINGS_CSS).toContain(".kit-qs__title{margin:0;font-family:var(--kit-qs-title-font,inherit);");
    expect(Object.keys(QUICK_SETTINGS_VARS)).not.toContain("--kit-qs-title-font");
    expect(QUICK_SETTINGS_CSS).not.toContain("--kit-qs-title-font:");
  });

  it("exports the new names from the public index", () => {
    expect(quick.QUICK_SETTINGS_VARS).toBe(QUICK_SETTINGS_VARS);
    expect(quick.QUICK_FILL_FROM_TRACK_FILTER).toBe(QUICK_FILL_FROM_TRACK_FILTER);
    for (const name of Object.keys(QUICK_SETTINGS_VARS)) expect(QUICK_SETTINGS_CSS).toContain(`${name}:`);
  });
});
