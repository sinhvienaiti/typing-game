// @vitest-environment happy-dom
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { KeyboardSoundPreview, loadKeyboardCatalog, keyboardPreviewGain, TypingSounds, type KeyboardSoundChoice } from "../../feedback/typing-fx/audio";
import { defaultSoundRows } from "./rows";
import { readChoice } from "./logic";
import { KeyboardSoundChoices, KEYBOARD_CHOICES_CSS } from "./keyboard-choices";
import { QuickSettings } from "./quick-settings";
import type { QuickChoiceRow, QuickValue } from "./types";

const DEEP = { value: "deep", label: "Deep", manifest: "/keys/packs/deep/keys-manifest.json", preview: "/keys/deep/preview.ogg" };
const WARM = { value: "warm", label: "Warm", manifest: "/keys/warm/keys-manifest.json", preview: "/keys/warm/preview.ogg" };
const OFF = { value: "off", label: "Off" };
const OPTIONS = [OFF, DEEP, WARM];
const rootEntry = (id: string, order: number) => ({ id, name: id.toUpperCase(), manifest: `packs/${id}/keys-manifest.json`, preview: `${id}/preview.ogg`, order });
const deferred = <T>() => {
  let resolve!: (value: T) => void;
  const promise = new Promise<T>((done) => { resolve = done; });
  return { promise, resolve };
};
const flush = async () => { for (let i = 0; i < 25; i++) await Promise.resolve(); };

class Param {
  value = 1;
  ramps: [number, number][] = [];
  cancelScheduledValues = vi.fn();
  setValueAtTime(value: number, _time: number): void { this.value = value; }
  linearRampToValueAtTime(value: number, time: number): void { this.ramps.push([value, time]); }
}
class Gain {
  gain = new Param();
  target: unknown;
  connect(target: unknown): void { this.target = target; }
  disconnect = vi.fn();
}
class Source {
  buffer: unknown;
  gain: Gain | null = null;
  onended: (() => void) | null = null;
  start = vi.fn();
  stop = vi.fn();
  connect(target: Gain): void { this.gain = target; }
  disconnect = vi.fn();
}
class Context {
  get currentTime(): number { return Date.now() / 1000; }
  state = "running";
  destination = {};
  sources: Source[] = [];
  gains: Gain[] = [];
  decodeAudioData = vi.fn(async (_bytes: ArrayBuffer) => ({ duration: 1 }) as AudioBuffer);
  resume = vi.fn(async () => { this.state = "running"; });
  createGain(): Gain { const gain = new Gain(); this.gains.push(gain); return gain; }
  createBufferSource(): Source { const source = new Source(); this.sources.push(source); return source; }
}
const cleanups: (() => void)[] = [];
beforeEach(() => {
  vi.useFakeTimers();
  vi.setSystemTime(0);
  vi.stubGlobal("GainNode", Gain);
});
afterEach(() => {
  for (const cleanup of cleanups.splice(0)) cleanup();
  document.body.replaceChildren();
  vi.unstubAllGlobals();
  vi.useRealTimers();
});

function audio(extra: Partial<ConstructorParameters<typeof KeyboardSoundPreview>[0]> = {}) {
  const ctx = new Context();
  const sounds = new TypingSounds({ context: ctx as unknown as AudioContext });
  const levels = { master: 0.8, keyboard: 0.5, muted: false };
  const fetchBytes = vi.fn(async (_url: string) => new ArrayBuffer(2));
  const fetchJson = vi.fn(async (_url: string) => ({ files: [
    ...Array.from({ length: 10 }, (_, i) => `key-${String(i + 1).padStart(2, "0")}.ogg`),
    ...Array.from({ length: 3 }, (_, i) => `space-${String(i + 1).padStart(2, "0")}.ogg`),
  ] }));
  const onLoad = vi.fn();
  const player = new KeyboardSoundPreview({ sounds, levels: () => levels, fetchBytes, fetchJson, onLoad, ...extra });
  cleanups.push(() => player.destroy());
  return { ctx, sounds, levels, fetchBytes, fetchJson, onLoad, player };
}
function picker(h: ReturnType<typeof audio>, select = vi.fn()) {
  const choices = new KeyboardSoundChoices({ document, options: OPTIONS, label: "Keyboard sound", listenIcon: "/art/180/hud-sound.64.png", onSelect: (choice) => { select(choice); h.player.select(choice); }, onPreview: (choice, delay) => h.player.preview(choice, delay), onStop: () => h.player.stop() });
  document.body.append(choices.element);
  choices.sync("deep");
  cleanups.push(() => choices.destroy());
  return { choices, select, option: (id: string) => choices.element.querySelector<HTMLButtonElement>(`[role=option][data-value="${id}"]`)!, listen: (id: string) => choices.element.querySelector<HTMLButtonElement>(`[data-listen="${id}"]`)! };
}
const pointer = (button: HTMLElement, type: string, pointerType = "mouse") => button.dispatchEvent(new PointerEvent(type, { pointerType }));
const key = (button: HTMLElement, value: string) => button.dispatchEvent(new KeyboardEvent("keydown", { key: value, bubbles: true, cancelable: true }));

describe("190 catalogue", () => {
  it("puts Off first, sorts by order stably, and resolves explicit URLs", async () => {
    const fetchJson = vi.fn(async () => ({ profiles: [rootEntry("warm", 2), rootEntry("deep", 0), rootEntry("clear", 2)] }));
    const result = await loadKeyboardCatalog("/keys", { fetchJson });
    expect(fetchJson).toHaveBeenCalledWith("/keys/keys-manifest.json");
    expect(result.state).toBe("ready");
    expect(result.options.map((p) => p.value)).toEqual(["off", "deep", "warm", "clear"]);
    expect(result.options[1]).toMatchObject({ manifest: "/keys/packs/deep/keys-manifest.json", preview: "/keys/deep/preview.ogg" });
  });
  it("missing root file returns the legacy fallback, or a caller's empty fallback", async () => {
    const fetchJson = async () => { throw new Error("404"); };
    expect((await loadKeyboardCatalog("/keys", { fetchJson })).options.map((p) => p.value)).toEqual(["off", "creamy", "thock", "marbly", "clack", "dome"]);
    expect(await loadKeyboardCatalog("/keys", { fetchJson, fallback: [] })).toEqual({ state: "missing", options: [OFF] });
  });
  it("malformed root has an explicit invalid state", async () => {
    expect((await loadKeyboardCatalog("/keys", { fetchJson: async () => ({ files: [] }), fallback: [] })).state).toBe("invalid");
  });
  it("keeps the first duplicate id and one Off, ignores malformed entries", async () => {
    const result = await loadKeyboardCatalog("/keys", { fetchJson: async () => ({ profiles: [rootEntry("deep", 2), rootEntry("deep", 0), rootEntry("off", 0), { ...rootEntry("bad", 1), preview: "../outside.ogg" }, { ...rootEntry("empty", 1), name: "" }, rootEntry("warm", 3)] }) });
    expect(result.options.map((p) => p.value)).toEqual(["off", "deep", "warm"]);
    expect(result.options[1]?.label).toBe("DEEP");
  });
  it("lets games append and override their own choices such as Relay", async () => {
    const relay = { value: "relay", label: "Relay" };
    const result = await loadKeyboardCatalog("/keys", { fetchJson: async () => ({ profiles: [rootEntry("deep", 0), rootEntry("relay", 1)] }), extra: [relay, relay, OFF] });
    expect(result.options).toEqual([OFF, expect.objectContaining({ value: "deep" }), relay]);
  });
  it("removed stored id resolves to the first available pack, Off stays Off", () => {
    const row = defaultSoundRows({ keyboardProfiles: OPTIONS })[3] as QuickChoiceRow;
    expect(readChoice(row, "creamy")).toBe("deep");
    expect(readChoice({ ...row, default: "warm" }, "gone")).toBe("deep");
    expect(readChoice(row, "off")).toBe("off");
    expect(readChoice({ ...row, options: [OFF], default: "deep" }, "gone")).toBe("off");
  });
});

describe("190 preview voice", () => {
  it("waits 150 ms, fetches lazily, and limits playback to exactly 1 second", async () => {
    const h = audio();
    h.player.preview(DEEP);
    expect(h.fetchBytes).not.toHaveBeenCalled();
    await vi.advanceTimersByTimeAsync(149);
    expect(h.ctx.sources).toHaveLength(0);
    await vi.advanceTimersByTimeAsync(1);
    expect(h.fetchBytes).toHaveBeenCalledWith(DEEP.preview);
    expect(h.ctx.sources[0]!.start).toHaveBeenCalledWith(0.15, 0, 1);
    expect(h.ctx.sources[0]!.stop).toHaveBeenCalledWith(1.15);
  });
  it("leaving before 150 ms cancels playback and fetch", async () => {
    const h = audio();
    h.player.preview(DEEP);
    await vi.advanceTimersByTimeAsync(149);
    h.player.stop();
    await vi.advanceTimersByTimeAsync(500);
    expect(h.fetchBytes).not.toHaveBeenCalled();
    expect(h.ctx.sources).toHaveLength(0);
  });
  it("leaving during fetch prevents late playback, but decoded buffer stays cached", async () => {
    const bytes = deferred<ArrayBuffer>();
    const h = audio({ fetchBytes: () => bytes.promise });
    h.player.preview(DEEP, 0);
    h.player.stop();
    bytes.resolve(new ArrayBuffer(1));
    await flush();
    expect(h.ctx.sources).toHaveLength(0);
    h.player.preview(DEEP, 0);
    await flush();
    expect(h.ctx.sources).toHaveLength(1);
    expect(h.ctx.decodeAudioData).toHaveBeenCalledTimes(1);
  });
  it("leaving during decode never plays the old option", async () => {
    const h = audio();
    const decoded = deferred<AudioBuffer>();
    h.ctx.decodeAudioData.mockImplementationOnce(() => decoded.promise);
    h.player.preview(DEEP, 0);
    await flush();
    h.player.stop();
    decoded.resolve({ duration: 1 } as AudioBuffer);
    await flush();
    expect(h.ctx.sources).toHaveLength(0);
  });
  it("switching fades the old voice for 30 ms; the next cannot overlap its tail", async () => {
    const h = audio();
    h.player.preview(DEEP, 0);
    await flush();
    const old = h.ctx.sources[0]!;
    await vi.advanceTimersByTimeAsync(100);
    h.player.preview(WARM, 0);
    await flush();
    expect(old.gain!.gain.ramps).toEqual([[0, 0.13]]);
    expect(old.stop).toHaveBeenLastCalledWith(0.13);
    expect(h.ctx.sources[1]!.start).toHaveBeenCalledWith(0.13, 0, 1);
  });
  it("rapid switches and out-of-order fetches play only the latest option", async () => {
    const deep = deferred<ArrayBuffer>();
    const h = audio({ fetchBytes: (url) => url === DEEP.preview ? deep.promise : Promise.resolve(new ArrayBuffer(1)) });
    h.player.preview(DEEP, 0);
    h.player.preview(WARM, 0);
    await flush();
    deep.resolve(new ArrayBuffer(1));
    await flush();
    expect(h.ctx.sources).toHaveLength(1);
  });
  it("cache avoids repeat fetch/decode, including concurrent requests for the same preview", async () => {
    const h = audio();
    h.player.preview(DEEP, 0);
    h.player.preview(DEEP, 0);
    await flush();
    h.player.preview(DEEP, 0);
    await flush();
    expect(h.fetchBytes).toHaveBeenCalledTimes(1);
    expect(h.ctx.decodeAudioData).toHaveBeenCalledTimes(1);
    expect(h.ctx.sources).toHaveLength(2);
  });
  it("uses Master × Keyboard without the effects bus; live sliders update the gain", async () => {
    const h = audio();
    h.player.preview(DEEP, 0);
    await flush();
    const gain = h.ctx.sources[0]!.gain!;
    expect(gain.gain.value).toBeCloseTo(0.4);
    expect(gain.target).toBe(h.ctx.destination);
    h.levels.master = 0.5;
    h.player.refreshVolume();
    expect(gain.gain.value).toBeCloseTo(0.25);
    expect(keyboardPreviewGain({ master: NaN, keyboard: 1 })).toBe(0);
    expect(keyboardPreviewGain({ master: 2, keyboard: 0.5 })).toBe(0.5);
  });
  it.each(["muted", "zero"])("Master %s prevents fetch/play and interrupts active audio", async (state) => {
    const h = audio();
    if (state === "muted") h.levels.muted = true;
    else h.levels.master = 0;
    h.player.preview(DEEP, 0);
    expect(h.fetchBytes).not.toHaveBeenCalled();
    h.levels.master = 0.8; h.levels.muted = false;
    h.player.preview(DEEP, 0);
    await flush();
    h.levels.muted = true;
    h.player.refreshVolume();
    expect(h.ctx.sources[0]!.stop).toHaveBeenLastCalledWith(0.03);
  });
  it("muting while a fetch is pending prevents its eventual playback", async () => {
    const bytes = deferred<ArrayBuffer>();
    const h = audio({ fetchBytes: () => bytes.promise });
    h.player.preview(DEEP, 0);
    h.levels.muted = true;
    h.player.refreshVolume();
    bytes.resolve(new ArrayBuffer(1));
    await flush();
    expect(h.ctx.sources).toHaveLength(0);
  });
  it("missing preview is silent and a later gesture retries", async () => {
    const h = audio();
    h.fetchBytes.mockRejectedValueOnce(new Error("404"));
    h.player.preview(DEEP, 0);
    await flush();
    h.player.preview(DEEP, 0);
    await flush();
    expect(h.ctx.sources).toHaveLength(1);
    expect(h.fetchBytes).toHaveBeenCalledTimes(2);
  });
  it("Off and disabled choices never fetch", async () => {
    const h = audio();
    h.player.preview(OFF, 0);
    h.player.preview({ ...DEEP, disabled: true }, 0);
    await flush();
    expect(h.fetchBytes).not.toHaveBeenCalled();
  });
  it("selection cancels dwell, loads all 13 files from the explicit manifest and previews once", async () => {
    const h = audio();
    h.player.preview(DEEP);
    h.player.select(DEEP);
    await flush();
    await vi.advanceTimersByTimeAsync(300);
    expect(h.fetchJson).toHaveBeenCalledWith(DEEP.manifest);
    expect(h.fetchBytes).toHaveBeenCalledTimes(14);
    expect(h.fetchBytes).toHaveBeenCalledWith("/keys/packs/deep/key-01.ogg");
    expect(h.fetchBytes).toHaveBeenCalledWith("/keys/packs/deep/space-03.ogg");
    expect(h.sounds.profile?.id).toBe("deep");
    expect(h.ctx.sources).toHaveLength(1);
    expect(h.onLoad).toHaveBeenCalledWith(expect.objectContaining({ keys: 10, spaces: 3, state: "ready" }));
  });
  it("a late selected-pack load never replaces a later selection or Off", async () => {
    const manifest = deferred<unknown>();
    const h = audio({ fetchJson: () => manifest.promise });
    h.player.select(DEEP);
    h.player.select(OFF);
    manifest.resolve({ files: ["key-01.ogg"] });
    await flush();
    expect(h.sounds.profile).toBeNull();
  });
  it("the legacy loadKeyboard API still activates a loaded profile", async () => {
    const h = audio();
    const result = await h.sounds.loadKeyboard("/legacy", "deep", "Deep", h.fetchJson, h.fetchBytes);
    expect(result.state).toBe("ready");
    expect(h.sounds.profile?.id).toBe("deep");
  });
  it("natural completion disconnects nodes and does not stop a newer voice", async () => {
    const h = audio();
    h.player.preview(DEEP, 0);
    await flush();
    const old = h.ctx.sources[0]!;
    h.player.preview(WARM, 0);
    await flush();
    old.onended!();
    expect(old.disconnect).toHaveBeenCalledOnce();
    expect(old.gain!.disconnect).toHaveBeenCalledOnce();
    h.player.stop();
    expect(h.ctx.sources[1]!.stop).toHaveBeenLastCalledWith(0.03);
  });
  it("a failed pack is retried after selecting another pack while it was loading", async () => {
    const pending = deferred<unknown>();
    const h = audio({ fetchJson: vi.fn().mockImplementationOnce(() => pending.promise).mockResolvedValue({ files: ["key-01.ogg"] }) });
    h.player.select(DEEP);
    h.player.select(OFF);
    pending.resolve({ files: [] });
    await flush();
    h.player.select(DEEP);
    await flush();
    expect(h.sounds.profile?.id).toBe("deep");
  });
  it("selection still preloads all files under mute, with no preview", async () => {
    const h = audio();
    h.levels.muted = true;
    h.player.select(DEEP);
    await flush();
    expect(h.fetchBytes).toHaveBeenCalledTimes(13);
    expect(h.sounds.profile?.id).toBe("deep");
    expect(h.ctx.sources).toHaveLength(0);
  });
});

describe("190 shared picker and Sound lifecycle", () => {
  it("mouse pointerenter/leave schedules and cancels; touch pointerenter stays silent", async () => {
    const h = audio(); const p = picker(h);
    pointer(p.option("deep"), "pointerenter", "touch");
    await vi.advanceTimersByTimeAsync(200);
    expect(h.fetchBytes).not.toHaveBeenCalled();
    pointer(p.option("deep"), "pointerenter");
    await vi.advanceTimersByTimeAsync(100);
    pointer(p.option("deep"), "pointerleave");
    await vi.advanceTimersByTimeAsync(100);
    expect(h.fetchBytes).not.toHaveBeenCalled();
    pointer(p.option("warm"), "pointerenter");
    await vi.advanceTimersByTimeAsync(150);
    expect(h.ctx.sources).toHaveLength(1);
  });
  it("keyboard focus previews; arrows/Home/End move focus without selecting", async () => {
    const h = audio(); const p = picker(h);
    p.option("deep").focus();
    await vi.advanceTimersByTimeAsync(150);
    expect(h.ctx.sources).toHaveLength(1);
    key(p.option("deep"), "ArrowDown");
    expect(document.activeElement).toBe(p.option("warm"));
    expect(h.ctx.sources[0]!.stop).toHaveBeenLastCalledWith(0.18);
    await vi.advanceTimersByTimeAsync(150);
    expect(h.ctx.sources).toHaveLength(2);
    key(p.option("warm"), "Home");
    expect(document.activeElement).toBe(p.option("off"));
    key(p.option("off"), "End");
    expect(document.activeElement).toBe(p.option("warm"));
    key(p.option("warm"), "ArrowUp");
    expect(document.activeElement).toBe(p.option("deep"));
    expect(p.select).not.toHaveBeenCalled();
    expect(p.option("deep").getAttribute("aria-selected")).toBe("true");
  });
  it.each(["Enter", " ", "click"])("%s selects once, cancelling the pending focus preview", async (action) => {
    const h = audio(); const p = picker(h);
    p.option("deep").focus();
    if (action === "click") p.option("deep").click();
    else key(p.option("deep"), action);
    await vi.advanceTimersByTimeAsync(200);
    expect(p.select).toHaveBeenCalledTimes(1);
    expect(h.ctx.sources).toHaveLength(1);
  });
  it("touch Listen uses ticket-180 art, previews once, and does not select", async () => {
    const h = audio(); const p = picker(h);
    const listen = p.listen("warm");
    expect(listen.querySelector("img")?.getAttribute("src")).toBe("/art/180/hud-sound.64.png");
    expect(listen.getAttribute("aria-label")).toBe("Listen to Warm");
    expect(listen.closest('[role="option"]')).toBeNull();
    pointer(listen, "pointerenter", "touch");
    pointer(listen, "pointerdown", "touch");
    listen.focus();
    listen.click();
    await flush();
    expect(h.ctx.sources).toHaveLength(1);
    expect(p.select).not.toHaveBeenCalled();
    pointer(p.option("deep"), "pointerdown", "touch");
    p.option("deep").focus();
    p.option("deep").click();
    await vi.advanceTimersByTimeAsync(200);
    expect(p.select).toHaveBeenCalledOnce();
    expect(h.ctx.sources).toHaveLength(2);
  });
  it("constrains the list to nine desktop rows with its own scroll; no drawn icons", () => {
    const h = audio(); const p = picker(h);
    expect(KEYBOARD_CHOICES_CSS).toContain("max-height:306px;overflow:auto");
    expect(KEYBOARD_CHOICES_CSS).toContain("flex:0 0 34px");
    expect(p.choices.element.querySelectorAll("svg,canvas")).toHaveLength(0);
  });
  it("persists the selected id synchronously, and stops audio on panel close/switch/destroy", async () => {
    const ctx = new Context();
    const sounds = new TypingSounds({ context: ctx as unknown as AudioContext });
    const saved: Record<string, QuickValue> = { master: 80, keyboardVolume: 50, keyboard: "creamy" };
    const onChange = vi.fn((id: string, value: QuickValue) => { saved[id] = value; });
    const qs = new QuickSettings({ keyboardSounds: sounds, keyboardProfiles: OPTIONS, getValues: () => saved, onChange, countdownMs: 0 });
    cleanups.push(() => qs.destroy());
    expect(saved.keyboard).toBe("deep");
    expect(onChange).toHaveBeenCalledWith("keyboard", "deep");
    const requests: string[] = [];
    vi.stubGlobal("fetch", vi.fn(async (url: string) => { requests.push(url); return { ok: true, json: async () => ({ files: ["key-01.ogg"] }), arrayBuffer: async () => new ArrayBuffer(1) }; }));
    qs.open("sound");
    const warm = qs.root.querySelector<HTMLButtonElement>('[data-value="warm"]')!;
    warm.click();
    expect(saved.keyboard).toBe("warm");
    await flush();
    expect(ctx.sources).toHaveLength(1);
    expect(ctx.sources[0]!.gain!.gain.value).toBeCloseTo(0.4);
    expect(requests).toContain(WARM.manifest);
    qs.close();
    expect(ctx.sources[0]!.stop).toHaveBeenLastCalledWith(0.03);
    qs.open("sound");
    pointer(warm, "pointerenter");
    qs.open("settings");
    await vi.advanceTimersByTimeAsync(200);
    expect(ctx.sources).toHaveLength(1);
    qs.open("sound");
    pointer(warm, "pointerenter");
    qs.destroy();
    await vi.advanceTimersByTimeAsync(200);
    expect(ctx.sources).toHaveLength(1);
  });
  it("closing during fetch prevents a late preview", async () => {
    const ctx = new Context();
    const sounds = new TypingSounds({ context: ctx as unknown as AudioContext });
    const bytes = deferred<ArrayBuffer>();
    vi.stubGlobal("fetch", vi.fn(async () => ({ ok: true, arrayBuffer: () => bytes.promise })));
    const qs = new QuickSettings({ keyboardSounds: sounds, keyboardProfiles: OPTIONS, getValues: () => ({ master: 100, keyboardVolume: 100, keyboard: "deep" }), onChange: () => {}, countdownMs: 0 });
    cleanups.push(() => qs.destroy());
    qs.open("sound");
    pointer(qs.root.querySelector<HTMLElement>('[data-value="warm"]')!, "pointerenter");
    await vi.advanceTimersByTimeAsync(150);
    qs.close();
    bytes.resolve(new ArrayBuffer(1));
    await flush();
    expect(ctx.sources).toHaveLength(0);
  });
});
