// @vitest-environment happy-dom
import { afterEach, describe, expect, it, vi } from "vitest";
import { loadKeyboardCatalog, type KeyboardSoundChoice } from "../../feedback/typing-fx/audio";
import { KeyboardSoundChoices, KEYBOARD_CHOICES_CSS } from "./keyboard-choices";
import { QuickSettings } from "./quick-settings";

const OFF = { value: "off", label: "Off" };
const families = ["Deep", "Warm", "Rounded", "Solid", "Crisp", "Clear", "Bright Clack"];
const profiles = Array.from({ length: 84 }, (_, i) => ({
  id: `pack-${i}`, name: `Pack ${i}`, family: families[Math.floor(i / 12)]!, score: 9 - i / 100,
  order: i, manifest: `pack-${i}/keys-manifest.json`, preview: `pack-${i}/preview.ogg`,
}));
const cleanups: (() => void)[] = [];
afterEach(() => { for (const clean of cleanups.splice(0)) clean(); document.body.replaceChildren(); vi.restoreAllMocks(); });
async function options(): Promise<readonly KeyboardSoundChoice[]> {
  return (await loadKeyboardCatalog("/v2", { extra: [{ value: "relay", label: "Relay" }], fetchJson: async () => ({ profiles: [...profiles].reverse() }) })).options;
}
function picker(choices: readonly KeyboardSoundChoice[]) {
  const onSelect = vi.fn(); const onPreview = vi.fn(); const onStop = vi.fn();
  const control = new KeyboardSoundChoices({ document, options: choices, label: "Keyboard sound", onSelect, onPreview, onStop });
  document.body.append(control.element);
  cleanups.push(() => control.destroy());
  const option = (value: string) => control.element.querySelector<HTMLButtonElement>(`[role=option][data-value="${value}"]`)!;
  return { control, onSelect, onPreview, onStop, option };
}
function key(button: HTMLElement, key: string): void {
  button.dispatchEvent(new KeyboardEvent("keydown", { key, bubbles: true, cancelable: true }));
}
function geometry(element: HTMLElement, top: () => number, height: number): void {
  vi.spyOn(element, "getBoundingClientRect").mockImplementation(() => ({ top: top(), bottom: top() + height, left: 0, right: 200, height, width: 200, x: 0, y: top(), toJSON: () => ({}) }));
}

describe("219 family catalogue", () => {
  it("loads 84 packs, keeps order and metadata, and puts game choices after Off", async () => {
    const result = await options();
    expect(result).toHaveLength(86);
    expect(result.slice(0, 2)).toEqual([OFF, { value: "relay", label: "Relay" }]);
    expect(result.slice(2).map((p) => p.value)).toEqual(profiles.map((p) => p.id));
    expect(result[2]).toMatchObject({ family: "Deep", score: 9, manifest: "/v2/pack-0/keys-manifest.json" });
    expect(result.at(-1)).toMatchObject({ family: "Bright Clack", score: 8.17 });
  });
  it("supports a legacy catalogue and ignores invalid optional metadata", async () => {
    const legacy = { ...profiles[0]!, family: undefined, score: undefined };
    const odd = { ...profiles[1]!, family: "  ", score: "9" };
    const result = await loadKeyboardCatalog("/keys", { fetchJson: async () => ({ profiles: [legacy, odd, { ...profiles[2]!, family: " Warm ", score: Infinity }] }) });
    expect(result.options[1]).not.toHaveProperty("family");
    expect(result.options[1]).not.toHaveProperty("score");
    expect(result.options[2]).not.toHaveProperty("family");
    expect(result.options[2]).not.toHaveProperty("score");
    expect(result.options[3]?.family).toBe("Warm");
    expect(result.options[3]).not.toHaveProperty("score");
    expect(picker(result.options).control.element.querySelectorAll('[role="group"]')).toHaveLength(1);
  });
});

describe("219 family picker", () => {
  it("renders seven named ARIA groups, with non-selectable headers and all 86 options", async () => {
    const p = picker(await options());
    const groups = [...p.control.element.querySelectorAll('[role="group"]')];
    expect(groups).toHaveLength(7);
    expect(groups.map((g) => document.getElementById(g.getAttribute("aria-labelledby")!)?.textContent)).toEqual(families);
    expect(groups.map((g) => g.querySelectorAll('[role="option"]').length)).toEqual(Array(7).fill(12));
    expect(p.control.element.querySelectorAll('[role="option"]')).toHaveLength(86);
    const headers = [...p.control.element.querySelectorAll<HTMLElement>('.kit-keyboards__list .kit-keyboards__family')];
    for (const header of headers) {
      expect(header.tagName).toBe("DIV");
      expect(header.tabIndex).toBe(-1);
      expect(header.getAttribute("role")).not.toBe("option");
      header.click(); key(header, "Enter");
    }
    expect(p.onSelect).not.toHaveBeenCalled();
    expect(p.onPreview).not.toHaveBeenCalled();
    expect(p.control.element.querySelectorAll('.kit-keyboards__listens > .kit-keyboards__family')).toHaveLength(7);
    expect(KEYBOARD_CHOICES_CSS).toContain("max-height:306px;overflow:auto");
  });
  it("arrows cross headers and disabled options; Home/End span the entire catalogue", async () => {
    const choices = [...await options()];
    choices[14] = { ...choices[14]!, disabled: true }; // First Warm pack.
    const p = picker(choices);
    p.control.sync("pack-11"); p.option("pack-11").focus();
    key(p.option("pack-11"), "ArrowDown");
    expect(document.activeElement).toBe(p.option("pack-13"));
    key(p.option("pack-13"), "ArrowUp");
    expect(document.activeElement).toBe(p.option("pack-11"));
    key(p.option("pack-11"), "Home"); expect(document.activeElement).toBe(p.option("off"));
    key(p.option("off"), "End"); expect(document.activeElement).toBe(p.option("pack-83"));
    expect(p.onSelect).not.toHaveBeenCalled();
    expect(p.option("pack-11").getAttribute("aria-selected")).toBe("true");
  });
  it("PageDown/PageUp jump to the first enabled pack of the next/previous family", async () => {
    const choices = [...await options()]; choices[14] = { ...choices[14]!, disabled: true };
    const p = picker(choices);
    p.option("off").focus(); key(p.option("off"), "PageDown"); expect(document.activeElement).toBe(p.option("pack-0"));
    key(p.option("pack-0"), "PageDown"); expect(document.activeElement).toBe(p.option("pack-13"));
    key(p.option("pack-13"), "PageDown"); expect(document.activeElement).toBe(p.option("pack-24"));
    key(p.option("pack-24"), "PageUp"); expect(document.activeElement).toBe(p.option("pack-13"));
    key(p.option("pack-13"), "PageUp"); expect(document.activeElement).toBe(p.option("pack-0"));
    key(p.option("pack-0"), "PageUp"); expect(document.activeElement).toBe(p.option("pack-0"));
    p.option("pack-83").focus(); key(p.option("pack-83"), "PageDown"); expect(document.activeElement).toBe(p.option("pack-83"));
    expect(p.onSelect).not.toHaveBeenCalled();
  });
  it("keeps legacy lists flat and retains Home/End and arrow navigation", () => {
    const p = picker([OFF, { value: "one", label: "One" }, { value: "two", label: "Two" }]);
    expect(p.control.element.querySelectorAll('[role="group"]')).toHaveLength(0);
    p.option("one").focus(); key(p.option("one"), "PageDown"); expect(document.activeElement).toBe(p.option("one"));
    key(p.option("one"), "End"); expect(document.activeElement).toBe(p.option("two"));
    key(p.option("two"), "ArrowUp"); expect(document.activeElement).toBe(p.option("one"));
  });
  it("does not reorder packs when a family recurs later in order", () => {
    const choices = [OFF, ...["Deep", "Warm", "Deep"].map((family, i) => ({ value: `${i}`, label: `${i}`, family }))];
    const p = picker(choices);
    expect([...p.control.element.querySelectorAll('[role="option"]')].map((b) => b.getAttribute("data-value"))).toEqual(["off", "0", "1", "2"]);
    expect(p.control.element.querySelectorAll('[role="group"]')).toHaveLength(3);
    p.option("1").focus(); key(p.option("1"), "PageDown"); expect(document.activeElement).toBe(p.option("2"));
  });
  it("opening Sound scrolls to the selected pack, only inside the list, on each reopen", async () => {
    const qs = new QuickSettings({ keyboardProfiles: await options(), getValues: () => ({ keyboard: "pack-80" }), onChange: () => {}, countdownMs: 0 });
    cleanups.push(() => qs.destroy());
    const root = qs.root.querySelector<HTMLElement>('.kit-keyboards')!;
    const selected = root.querySelector<HTMLElement>('[data-value="pack-80"]')!;
    const outer = root.closest<HTMLElement>('.kit-qs__body')!;
    geometry(root, () => 100, 306); geometry(selected, () => 2600 - root.scrollTop, 34);
    Object.defineProperty(root, "clientHeight", { configurable: true, value: 306 });
    const outerScroll = outer.scrollTop;
    qs.open("sound"); await Promise.resolve();
    expect(root.scrollTop).toBe(2228);
    expect(outer.scrollTop).toBe(outerScroll);
    qs.close(); root.scrollTop = 0; qs.open("sound"); await Promise.resolve();
    expect(root.scrollTop).toBe(2228);
    expect(outer.scrollTop).toBe(outerScroll);
  });
  it("scrolls upward only as far as needed and avoids scrolling after destruction", async () => {
    const p = picker(await options()); const root = p.control.element;
    geometry(root, () => 100, 306); geometry(p.option("pack-0"), () => 580 - root.scrollTop, 34);
    Object.defineProperty(root, "clientHeight", { configurable: true, value: 306 });
    root.scrollTop = 500; p.control.sync("pack-0"); await Promise.resolve(); expect(root.scrollTop).toBe(480);
    root.scrollTop = 500; p.control.sync("pack-0"); p.control.destroy(); await Promise.resolve(); expect(root.scrollTop).toBe(500);
  });
});
