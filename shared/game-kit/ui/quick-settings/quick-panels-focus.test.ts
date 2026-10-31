// @vitest-environment happy-dom
// Judges 31/10 (night): on the title, Tab left Settings when the last row was a choice whose checked chip is not its
// last one (a11y-dialog ends its trap at the last radio), and Shift+Tab from the dialog itself did nothing.
import { afterEach, describe, expect, it } from "vitest";
import { QUICK_SETTINGS_CSS } from "./css";
import { nextStop, tabStops } from "./focus";
import { QuickSettings, type QuickSettingsOptions } from "./quick-settings";
import { defaultSettingsRows } from "./rows";
import type { QuickChoiceOption, QuickContext, QuickRow, QuickValue } from "./types";

const cleanups: (() => void)[] = [];
afterEach(() => {
  for (const cleanup of cleanups.splice(0).reverse()) cleanup();
});

const SETS: QuickChoiceOption[] = [
  { value: "off", label: "Off" },
  ...["creamy", "thock", "marbly"].map((value) => ({ value, label: value, preview: `https://art.example.test/${value}.ogg` })),
];

function make(context: QuickContext, extra: Partial<QuickSettingsOptions> = {}, start: Record<string, QuickValue> = {}) {
  const style = document.createElement("style");
  style.textContent = QUICK_SETTINGS_CSS;
  document.head.append(style);
  const host = document.createElement("div");
  // Something focusable outside the layer, after it: where an escaped Tab would land.
  const after = document.createElement("button");
  after.textContent = "game";
  document.body.append(host, after);
  const values: Record<string, QuickValue> = { master: 80, muted: false, music: 40, effects: 50, keyboardVolume: 70, ui: 65, keyboard: "marbly", quality: "high", ...start };
  const qs = new QuickSettings({ host, keyboardProfiles: SETS, getValues: () => values, onChange: (id, value) => { values[id] = value; }, countdownMs: 0, context, ...extra });
  cleanups.push(() => { qs.destroy(); host.remove(); after.remove(); style.remove(); });
  const dialog = (panel: "settings" | "sound") => qs.root.querySelector<HTMLElement>(`.kit-qs__dialog[data-panel="${panel}"]`)!;
  return { qs, values, dialog };
}

/** The browser's own Tab order over the whole document: radio groups as one stop (the checked radio), hidden parts skipped. */
function nativeOrder(): HTMLElement[] {
  const all = [...document.querySelectorAll<HTMLElement>("button, input, [tabindex]")].filter(
    (el) => el.tabIndex >= 0 && !(el as HTMLButtonElement).disabled && el.closest('[hidden], [aria-hidden="true"]') === null,
  );
  return all.filter((el) => {
    const radio = el as HTMLInputElement;
    if (el.tagName !== "INPUT" || radio.type !== "radio") return true;
    const group = all.filter((other) => (other as HTMLInputElement).name === radio.name) as HTMLInputElement[];
    return el === (group.find((other) => other.checked) ?? group[0]);
  });
}

/** One Tab (Shift+Tab with `back`): the keydown goes out; unless a listener took it, focus moves as the browser would. */
function press(back = false): void {
  const target = document.activeElement ?? document.body;
  const event = new KeyboardEvent("keydown", { key: "Tab", shiftKey: back, bubbles: true, cancelable: true });
  target.dispatchEvent(event);
  if (event.defaultPrevented) return;
  const order = nativeOrder();
  const at = order.indexOf(target as HTMLElement);
  const next = order[back ? (at < 0 ? order.length - 1 : at - 1) : at + 1];
  if (next !== undefined) next.focus();
  else (target as HTMLElement).blur?.();
}

/** Presses Tab `n` times; every focus must stay inside `dialog`. Returns what was focused, in order. */
function walk(dialog: HTMLElement, n: number, back = false): HTMLElement[] {
  const seen: HTMLElement[] = [];
  for (let i = 0; i < n; i += 1) {
    press(back);
    const active = document.activeElement as HTMLElement;
    expect(dialog.contains(active), `press ${i + 1}${back ? " (Shift)" : ""} left the panel for ${active?.tagName} ${active?.textContent ?? ""}`).toBe(true);
    seen.push(active);
  }
  return seen;
}

const titleRows = (rows: readonly QuickRow[]): QuickRow[] => rows.filter((row) => row.kind !== "button");

describe("Tab stays inside an open panel", () => {
  // The kit's rows; a game with one choice row (Quality on High: Ultra is the last radio); a game whose last row is a
  // five-chip choice on its first chip and whose toggle comes before it.
  const rowSets: Record<string, QuickRow[]> = {
    kit: defaultSettingsRows({ learning: { meaning: true, ipa: true } }),
    quality: [
      { kind: "choice", id: "quality", label: "Quality", options: ["low", "medium", "high", "ultra"].map((value) => ({ value, label: value })), default: "high" },
      ...defaultSettingsRows().filter((row) => row.kind === "button"),
    ],
    story: [
      { kind: "heading", id: "game", label: "Game" },
      { kind: "toggle", id: "pace", label: "Pace", default: true },
      { kind: "choice", id: "mode", label: "Story mode", options: ["profile", "relax", "balanced", "challenge", "learn"].map((value) => ({ value, label: value })), default: "profile" },
      ...defaultSettingsRows().filter((row) => row.kind === "button"),
    ],
  };

  for (const [name, rows] of Object.entries(rowSets)) {
    it(`on the title (${name} rows): Tab and Shift+Tab go round every control and never leave`, () => {
      const h = make("title", { settingsRows: rows });
      h.qs.open("settings");
      const dialog = h.dialog("settings");
      const box = dialog.querySelector<HTMLElement>(".kit-qs__panel")!;
      const stops = tabStops(box);
      // Close, one stop per choice row (its checked chip) and per toggle; Resume and Quit to title are hidden.
      expect(stops[0]!.classList.contains("kit-qs__close")).toBe(true);
      expect(stops.length).toBe(1 + titleRows(rows).filter((row) => row.kind === "choice" || row.kind === "toggle").length);
      expect(stops.some((el) => el.dataset.action !== undefined)).toBe(false);
      const n = Math.max(10, stops.length * 2 + 2);
      const forward = walk(dialog, n);
      expect(forward.slice(0, stops.length)).toEqual(stops);
      expect(forward[stops.length]).toBe(stops[0]);
      const back = walk(dialog, n, true);
      // From where the forward walk stopped, backwards round.
      const from = stops.indexOf(forward.at(-1)!);
      expect(back.slice(0, stops.length)).toEqual(stops.map((_, i) => stops[(from - 1 - i + stops.length * 2) % stops.length]));
    });
  }

  it("Shift+Tab from the dialog itself (where it opens) goes to the last control, Tab to Close", () => {
    const h = make("title", { settingsRows: rowSets.quality });
    h.qs.open("settings");
    const dialog = h.dialog("settings");
    const stops = tabStops(dialog.querySelector<HTMLElement>(".kit-qs__panel")!);
    expect(document.activeElement).toBe(dialog);
    press(true);
    expect(document.activeElement).toBe(stops.at(-1));
    expect((document.activeElement as HTMLInputElement).value).toBe("high");
    dialog.focus();
    press();
    expect(document.activeElement).toBe(stops[0]);
  });

  it("in play the last stop is Quit to title, and Tab from it comes back to Close", () => {
    const h = make("play", { settingsRows: rowSets.story });
    h.qs.open("settings");
    const dialog = h.dialog("settings");
    const stops = tabStops(dialog.querySelector<HTMLElement>(".kit-qs__panel")!);
    expect(stops.at(-1)!.dataset.action).toBe("quit");
    stops.at(-1)!.focus();
    press();
    expect(document.activeElement).toBe(stops[0]);
    walk(dialog, 12);
    walk(dialog, 12, true);
  });

  it("a focus that escaped to the page comes back on the next Tab", () => {
    const h = make("title");
    h.qs.open("settings");
    (document.activeElement as HTMLElement).blur();
    expect(document.activeElement).toBe(document.body);
    press();
    expect(h.dialog("settings").contains(document.activeElement)).toBe(true);
    expect((document.activeElement as HTMLElement).classList.contains("kit-qs__close")).toBe(true);
  });

  it("Sound: the keyboard list's tabbable option and its Listen button are stops, and the last slider wraps to Close", () => {
    const h = make("title");
    h.qs.open("sound");
    const dialog = h.dialog("sound");
    const stops = tabStops(dialog.querySelector<HTMLElement>(".kit-qs__panel")!);
    const option = stops.find((el) => el.classList.contains("kit-keyboards__option"))!;
    expect(option.dataset.value).toBe("marbly");
    expect(stops[stops.indexOf(option) + 1]!.dataset.listen).toBe("marbly");
    expect(stops.filter((el) => el.classList.contains("kit-keyboards__option"))).toHaveLength(1);
    expect((stops.at(-1) as HTMLInputElement).type).toBe("range");
    walk(dialog, stops.length * 2 + 2);
    walk(dialog, stops.length * 2 + 2, true);
  });

  it("modifier Tabs are left to the browser, and nothing is handled with no panel open", () => {
    const h = make("play");
    const plain = new KeyboardEvent("keydown", { key: "Tab", bubbles: true, cancelable: true });
    document.body.dispatchEvent(plain);
    expect(plain.defaultPrevented).toBe(false);
    h.qs.open("settings");
    const ctrl = new KeyboardEvent("keydown", { key: "Tab", ctrlKey: true, bubbles: true, cancelable: true });
    document.activeElement!.dispatchEvent(ctrl);
    expect(ctrl.defaultPrevented).toBe(false);
  });
});

describe("tab stops and the next stop", () => {
  it("skips hidden, disabled and negative-tabindex controls and keeps one radio a group", () => {
    const box = document.createElement("div");
    box.innerHTML = `<button id="a">a</button><button id="b" hidden>b</button><button id="c" disabled>c</button><button id="d" tabindex="-1">d</button>
      <input type="radio" name="g" value="1" id="r1"><input type="radio" name="g" value="2" id="r2" checked><input type="radio" name="g" value="3" id="r3">
      <input type="radio" name="h" value="1" id="h1" disabled><input type="radio" name="h" value="2" id="h2"><div hidden><button id="e">e</button></div><input type="range" id="z">`;
    document.body.append(box);
    cleanups.push(() => box.remove());
    expect(tabStops(box).map((el) => el.id)).toEqual(["a", "r2", "h2", "z"]);
  });

  it("from a control that is not a stop, steps from where it sits; from outside, the first or the last", () => {
    const box = document.createElement("div");
    box.innerHTML = `<button id="a">a</button><input type="radio" name="g" id="r1"><input type="radio" name="g" id="r2" checked><input type="radio" name="g" id="r3"><button id="b">b</button>`;
    document.body.append(box);
    cleanups.push(() => box.remove());
    const stops = tabStops(box);
    const by = (id: string) => box.querySelector<HTMLElement>(`#${id}`)!;
    expect(nextStop(stops, by("r3"), box, false)?.id).toBe("b");
    expect(nextStop(stops, by("r1"), box, true)?.id).toBe("a");
    expect(nextStop(stops, document.body, box, false)?.id).toBe("a");
    expect(nextStop(stops, document.body, box, true)?.id).toBe("b");
    expect(nextStop(stops, by("b"), box, false)?.id).toBe("a");
    expect(nextStop([], by("b"), box, false)).toBeNull();
  });
});
