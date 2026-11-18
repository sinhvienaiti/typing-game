// Source: new for the kit: Typing Feel data step (docs/games/TYPING_FEEL_SERVICE.md §4.3, §4.6, §5.1–5.3): catalogue-3 fields, timedJson, settleKeyboardChoice, typingFeelKeysBase
import { afterEach, describe, expect, it, vi } from "vitest";
import * as quickIndex from "../../ui/quick-settings/index";
import {
  KEYBOARD_CATALOG_TIMEOUT_MS, loadKeyboardCatalog, pendingKeyboardChoices, settleKeyboardChoice, timedJson, typingFeelKeysBase,
  type KeyboardCatalog, type KeyboardSoundChoice,
} from "./audio";
import * as fxIndex from "./index";

const ORIGIN = "https://feel.typing-game.local";
const BASE = ORIGIN + "/v1/keys/";
const OFF: KeyboardSoundChoice = { value: "off", label: "Off" };
const RELAY: KeyboardSoundChoice = { value: "relay", label: "Relay" };

/** A catalogue-3 export shaped like §4.3: sets sorted by family then set, `order` from 0, a provisional set, extra fields. */
const CATALOGUE_3 = {
  schema: "typing-feel/catalogue-3",
  contract: 1,
  revision: "r1",
  publishedAt: "2026-11-02T09:00:00Z",
  default: "bright-clack",
  effects: { style: "stamp", intensity: "normal", size: "large", volume: 1 },
  families: [{ id: "crisp", name: "Crisp", order: 4 }, { id: "bright-clack", name: "Bright Clack", order: 6 }],
  profiles: [
    {
      id: "crisp-silk", name: "Crisp Silk", family: "Crisp", familyId: "crisp", order: 0, score: 6.1, ownerPick: false,
      status: "published", keys: 72, spaces: 8,
      manifest: "sets/crisp-silk/0a1b2c3d4e5f/keys-manifest.json", preview: "sets/crisp-silk/0a1b2c3d4e5f/preview.ogg",
    },
    {
      id: "raindrop-tile", name: "Raindrop Tile", family: "Crisp", familyId: "crisp", order: 1, score: null, ownerPick: true,
      status: "provisional", keys: 17, spaces: 8,
      manifest: "sets/raindrop-tile/3f2a9c1e7b44/keys-manifest.json", preview: "sets/raindrop-tile/3f2a9c1e7b44/preview.ogg",
    },
    {
      id: "bright-clack", name: "Bright Clack", family: "Bright Clack", familyId: "bright-clack", order: 2, score: null, ownerPick: true,
      status: "published", keys: 80, spaces: 8,
      manifest: "sets/bright-clack/9e8d7c6b5a49/keys-manifest.json", preview: "sets/bright-clack/9e8d7c6b5a49/preview.ogg",
    },
  ],
};
/** The same sets as today's catalogue-2 writes them (no revision, default or effects). */
const CATALOGUE_2 = {
  schema: "typing-keys-firefly/catalogue-2",
  status: "owner-approved-source",
  profiles: [
    { id: "deep", name: "Deep Velvet", family: "Deep", score: 6.3729, manifest: "deep/keys-manifest.json", preview: "deep/preview.ogg", order: 0 },
    { id: "bright-clack", name: "Bright Clack", family: "Bright Clack", score: 6.1, manifest: "bright-clack/keys-manifest.json", preview: "bright-clack/preview.ogg", order: 1 },
  ],
};
const json = (data: unknown) => async (): Promise<unknown> => data;
const set = (id: string, fp: string, family: string): KeyboardSoundChoice => ({
  value: id, label: id, family, manifest: `${BASE}sets/${id}/${fp}/keys-manifest.json`, preview: `${BASE}sets/${id}/${fp}/preview.ogg`,
});

afterEach(() => {
  vi.unstubAllGlobals();
  vi.useRealTimers();
});

describe("catalogue-3: revision, default and effects", () => {
  it("reads a §4.3 catalogue-3 export: the sets in order, plus revision, defaultId and effects", async () => {
    const catalog = await loadKeyboardCatalog(BASE, { extra: [RELAY], fallback: [], fetchJson: json(CATALOGUE_3) });
    expect(catalog.state).toBe("ready");
    expect(catalog.options.map((choice) => choice.value)).toEqual(["off", "relay", "crisp-silk", "raindrop-tile", "bright-clack"]);
    expect(catalog.options[3]).toEqual({
      value: "raindrop-tile", label: "Raindrop Tile", family: "Crisp",
      manifest: BASE + "sets/raindrop-tile/3f2a9c1e7b44/keys-manifest.json", preview: BASE + "sets/raindrop-tile/3f2a9c1e7b44/preview.ogg",
    });
    expect(catalog.revision).toBe("r1");
    expect(catalog.defaultId).toBe("bright-clack");
    expect(catalog.effects).toEqual({ style: "stamp", intensity: "normal", size: "large", volume: 1 });
  });

  it("catalogue-2 still parses, with none of the new fields", async () => {
    const catalog = await loadKeyboardCatalog("/assets/x/audio/keys/", { extra: [RELAY], fallback: [], fetchJson: json(CATALOGUE_2) });
    expect(catalog).toStrictEqual({
      state: "ready",
      options: [OFF, RELAY,
        { value: "deep", label: "Deep Velvet", family: "Deep", score: 6.3729, manifest: "/assets/x/audio/keys/deep/keys-manifest.json", preview: "/assets/x/audio/keys/deep/preview.ogg" },
        { value: "bright-clack", label: "Bright Clack", family: "Bright Clack", score: 6.1, manifest: "/assets/x/audio/keys/bright-clack/keys-manifest.json", preview: "/assets/x/audio/keys/bright-clack/preview.ogg" }],
    });
  });

  it("drops each invalid effect field on its own and never takes a sound id from effects", async () => {
    const read = async (effects: unknown): Promise<KeyboardCatalog["effects"]> => (await loadKeyboardCatalog(BASE, { fetchJson: json({ ...CATALOGUE_3, effects }) })).effects;
    expect(await read({ style: "sparkle", intensity: "normal", size: "giant", volume: 1.5, soundProfile: "deep", extra: true })).toEqual({ intensity: "normal" });
    expect(await read({ style: "rune", intensity: 7, size: "huge", volume: -0.1 })).toEqual({ style: "rune", size: "huge" });
    expect(await read({ volume: 0 })).toEqual({ volume: 0 });
    expect(await read({ volume: 0.35, style: null })).toEqual({ volume: 0.35 });
    for (const bad of [{ volume: Number.NaN }, { volume: "1" }, {}, [], "stamp", null, 3]) expect(await read(bad)).toBeUndefined();
  });

  it("defaultId only names a set this catalogue lists and the kit kept", async () => {
    const read = async (patch: Record<string, unknown>): Promise<string | undefined> =>
      (await loadKeyboardCatalog(BASE, { extra: [RELAY], fetchJson: json({ ...CATALOGUE_3, ...patch }) })).defaultId;
    expect(await read({ default: "raindrop-tile" })).toBe("raindrop-tile");
    // Unknown, Off, the game's own sound, not a string, or a row the kit dropped (no preview).
    expect(await read({ default: "no-such-set" })).toBeUndefined();
    expect(await read({ default: "off" })).toBeUndefined();
    expect(await read({ default: "relay" })).toBeUndefined();
    expect(await read({ default: 3 })).toBeUndefined();
    const broken = { ...CATALOGUE_3, profiles: CATALOGUE_3.profiles.map((row) => row.id === "bright-clack" ? { ...row, preview: undefined } : row) };
    expect((await loadKeyboardCatalog(BASE, { fetchJson: json(broken) })).defaultId).toBeUndefined();
  });

  it("revision is a trimmed printable string up to 128 characters", async () => {
    const read = async (revision: unknown): Promise<string | undefined> => (await loadKeyboardCatalog(BASE, { fetchJson: json({ ...CATALOGUE_3, revision }) })).revision;
    expect(await read("  rev-2026-11-02T09:00:00Z ")).toBe("rev-2026-11-02T09:00:00Z");
    expect(await read("x".repeat(128))).toBe("x".repeat(128));
    for (const bad of ["", "   ", "x".repeat(129), "r1\nr2", "r1\u0007", 7, null, { id: "r1" }]) expect(await read(bad)).toBeUndefined();
  });

  it("a missing or invalid catalogue carries no revision, default or effects", async () => {
    const missing = await loadKeyboardCatalog(BASE, { fallback: [], fetchJson: async () => { throw new Error("404"); } });
    expect(missing).toStrictEqual({ state: "missing", options: [OFF] });
    const invalid = await loadKeyboardCatalog(BASE, { fallback: [], fetchJson: json({ ...CATALOGUE_3, profiles: "none" }) });
    expect(invalid).toStrictEqual({ state: "invalid", options: [OFF] });
  });

  it("a catalogue with no usable set (an empty list, or every row dropped) is invalid, so saves are kept", async () => {
    const malformed = CATALOGUE_3.profiles.map(({ order: _order, ...row }) => row);
    for (const profiles of [[], malformed, [null, 3, "bright-clack"]]) {
      const catalog = await loadKeyboardCatalog(BASE, { extra: [RELAY], fallback: [], fetchJson: json({ ...CATALOGUE_3, profiles }) });
      expect(catalog).toStrictEqual({ state: "invalid", options: [OFF, RELAY] });
      expect(settleKeyboardChoice("raindrop-tile", catalog, RELAY, "bright-clack")).toMatchObject({ id: "raindrop-tile", repaired: false });
    }
    // One usable row is enough.
    const one = await loadKeyboardCatalog(BASE, { fallback: [], fetchJson: json({ ...CATALOGUE_3, profiles: [...malformed, CATALOGUE_3.profiles[1]] }) });
    expect(one.state).toBe("ready");
    expect(one.options.map((choice) => choice.value)).toEqual(["off", "raindrop-tile"]);
  });

  it("a null base (no Typing Feel origin) fetches nothing: missing, with the fallback", async () => {
    const fetchJson = vi.fn(json(CATALOGUE_3));
    const fetch = vi.fn();
    vi.stubGlobal("fetch", fetch);
    expect(await loadKeyboardCatalog(null, { extra: [RELAY], fallback: [], fetchJson })).toStrictEqual({ state: "missing", options: [OFF, RELAY] });
    expect(await loadKeyboardCatalog(typingFeelKeysBase(undefined), { extra: [RELAY], fallback: [] })).toStrictEqual({ state: "missing", options: [OFF, RELAY] });
    expect(fetchJson).not.toHaveBeenCalled();
    expect(fetch).not.toHaveBeenCalled();
  });
});

type FakeResponse = { ok: boolean; status: number; headers: Headers; text: () => Promise<string> };
const answer = (body: string, status = 200, type?: string): FakeResponse => ({
  ok: status >= 200 && status < 300, status, headers: new Headers(type === undefined ? {} : { "content-type": type }), text: async () => body,
});
const HTML = "<!doctype html><html><head><title>Last Line</title></head><body></body></html>";

describe("timedJson: a catalogue fetch with a deadline", () => {
  it("reads JSON with no-cache and an abort signal, and clears its timer", async () => {
    vi.useFakeTimers();
    const fetch = vi.fn(async (_url: string, _init?: RequestInit) => answer(JSON.stringify(CATALOGUE_3), 200, "application/json"));
    vi.stubGlobal("fetch", fetch);
    await expect(timedJson()(BASE + "keys-manifest.json")).resolves.toEqual(CATALOGUE_3);
    expect(fetch).toHaveBeenCalledWith(BASE + "keys-manifest.json", expect.objectContaining({ cache: "no-cache", signal: expect.any(AbortSignal) }));
    expect(vi.getTimerCount()).toBe(0);
  });

  it("gives up after 3000 ms, aborts the request and leaves no timer or unhandled rejection", async () => {
    vi.useFakeTimers();
    let signal: AbortSignal | undefined;
    vi.stubGlobal("fetch", vi.fn((_url: string, init?: RequestInit) => new Promise<never>((_, reject) => {
      signal = init?.signal ?? undefined;
      // The request's own rejection arrives after the deadline already won: it must stay handled.
      signal?.addEventListener("abort", () => reject(new DOMException("The operation was aborted.", "AbortError")));
    })));
    const unhandled = vi.fn();
    process.on("unhandledRejection", unhandled);
    try {
      const pending = timedJson()(BASE + "keys-manifest.json");
      const settled = vi.fn();
      pending.then(settled, settled);
      expect(KEYBOARD_CATALOG_TIMEOUT_MS).toBe(3000);
      await vi.advanceTimersByTimeAsync(2999);
      expect(settled).not.toHaveBeenCalled();
      expect(signal?.aborted).toBe(false);
      await vi.advanceTimersByTimeAsync(1);
      await expect(pending).rejects.toThrow(/no answer in 3000 ms/);
      expect(signal?.aborted).toBe(true);
      expect(vi.getTimerCount()).toBe(0);
      vi.useRealTimers();
      await new Promise((resolve) => setTimeout(resolve, 10));
      expect(unhandled).not.toHaveBeenCalled();
    } finally {
      process.off("unhandledRejection", unhandled);
    }
  });

  it("still rejects on time when fetch ignores the signal (a host that hangs for 10 s)", async () => {
    vi.useFakeTimers();
    vi.stubGlobal("fetch", vi.fn(() => new Promise((resolve) => setTimeout(() => resolve(answer("{}")), 10_000))));
    const pending = timedJson(500)(BASE + "keys-manifest.json");
    const result = pending.then(() => "resolved", (error: Error) => error.message);
    await vi.advanceTimersByTimeAsync(500);
    expect(await result).toMatch(/no answer in 500 ms/);
    await vi.advanceTimersByTimeAsync(10_000);
    expect(vi.getTimerCount()).toBe(0);
  });

  it("a non-positive, non-finite or above-setTimeout timeout takes the 3000 ms default", async () => {
    vi.useFakeTimers();
    vi.stubGlobal("fetch", vi.fn(() => new Promise<never>(() => {})));
    for (const ms of [0, -5, Number.NaN, Number.POSITIVE_INFINITY, 2_147_483_648, 3_000_000_000]) {
      const result = timedJson(ms)("/never.json").then(() => "resolved", (error: Error) => error.message);
      await vi.advanceTimersByTimeAsync(2999);
      await vi.advanceTimersByTimeAsync(1);
      expect(await result).toMatch(/no answer in 3000 ms/);
    }
  });

  it("the largest setTimeout delay is kept as given, not fired at once", async () => {
    vi.useFakeTimers();
    vi.stubGlobal("fetch", vi.fn(() => new Promise<never>(() => {})));
    const settled = vi.fn();
    timedJson(2_147_483_647)("/never.json").then(settled, settled);
    await vi.advanceTimersByTimeAsync(KEYBOARD_CATALOG_TIMEOUT_MS * 10);
    expect(settled).not.toHaveBeenCalled();
    vi.clearAllTimers();
  });

  it("cache is no-cache unless given, e.g. \"default\" for a set manifest whose versioned URL never changes", async () => {
    vi.useFakeTimers();
    const fetch = vi.fn(async (_url: string, _init?: RequestInit) => answer("{\"files\":[]}", 200, "application/json"));
    vi.stubGlobal("fetch", fetch);
    await timedJson(3000, {})("/a.json");
    await timedJson(3000, { cache: "default" })("/b.json");
    expect(fetch.mock.calls.map(([url, init]) => [url, init?.cache])).toEqual([["/a.json", "no-cache"], ["/b.json", "default"]]);
    expect(vi.getTimerCount()).toBe(0);
  });

  it.each([
    ["text/html; charset=utf-8", /HTML, not JSON/],
    [undefined, /not JSON/],
    ["application/json", /not JSON/],
  ])("HTML with status 200 (content-type %s) rejects instead of failing in JSON.parse", async (type, message) => {
    vi.useFakeTimers();
    vi.stubGlobal("fetch", vi.fn(async () => answer(HTML, 200, type)));
    await expect(timedJson()(BASE + "keys-manifest.json")).rejects.toThrow(message);
    expect(vi.getTimerCount()).toBe(0);
  });

  it("rejects on a non-OK status and on a network or CORS failure, clearing the timer", async () => {
    vi.useFakeTimers();
    vi.stubGlobal("fetch", vi.fn(async () => answer("Not found", 404, "text/plain")));
    await expect(timedJson()(BASE + "keys-manifest.json")).rejects.toThrow(/: 404$/);
    expect(vi.getTimerCount()).toBe(0);
    vi.stubGlobal("fetch", vi.fn(async () => { throw new TypeError("Failed to fetch"); }));
    await expect(timedJson()(BASE + "keys-manifest.json")).rejects.toThrow("Failed to fetch");
    expect(vi.getTimerCount()).toBe(0);
  });

  it("through loadKeyboardCatalog: HTML 200 or a hung host leaves the catalogue missing within 3 s", async () => {
    vi.useFakeTimers();
    vi.stubGlobal("fetch", vi.fn(async () => answer(HTML, 200, "text/html")));
    expect(await loadKeyboardCatalog(BASE, { extra: [RELAY], fallback: [], fetchJson: timedJson() })).toStrictEqual({ state: "missing", options: [OFF, RELAY] });
    vi.stubGlobal("fetch", vi.fn(() => new Promise<never>(() => {})));
    const hung = loadKeyboardCatalog(BASE, { extra: [RELAY], fallback: [], fetchJson: timedJson(3000) });
    await vi.advanceTimersByTimeAsync(3000);
    expect(await hung).toStrictEqual({ state: "missing", options: [OFF, RELAY] });
    expect(vi.getTimerCount()).toBe(0);
  });

  it("end to end: origin → keys base → timed catalogue-3 fetch", async () => {
    vi.useFakeTimers();
    const fetch = vi.fn(async (_url: string) => answer(JSON.stringify(CATALOGUE_3), 200, "application/json"));
    vi.stubGlobal("fetch", fetch);
    const catalog = await loadKeyboardCatalog(typingFeelKeysBase(ORIGIN + "/"), { extra: [RELAY], fallback: [], fetchJson: timedJson() });
    expect(fetch.mock.calls.map(([url]) => url)).toEqual([BASE + "keys-manifest.json"]);
    expect(catalog).toMatchObject({ state: "ready", revision: "r1", defaultId: "bright-clack" });
    expect(settleKeyboardChoice("retired-set", catalog, RELAY, "deep")).toMatchObject({ id: "bright-clack", repaired: true });
  });
});

describe("settleKeyboardChoice: the saved set against the catalogue", () => {
  const CRISP = set("crisp-silk", "0a1b2c3d4e5f", "Crisp");
  const RAIN = set("raindrop-tile", "3f2a9c1e7b44", "Crisp");
  const BRIGHT = set("bright-clack", "9e8d7c6b5a49", "Bright Clack");
  const ready = (extra: Partial<KeyboardCatalog> = {}): KeyboardCatalog => ({ state: "ready", options: [OFF, RELAY, CRISP, RAIN, BRIGHT], ...extra });
  const UNAVAILABLE = (id: string): KeyboardSoundChoice => ({ value: id, label: "Saved sound", note: "unavailable", disabled: true });

  it.each(["missing", "invalid"] as const)("catalogue %s: keeps the saved id, listed as a disabled unavailable choice; not repaired", (state) => {
    const catalog: KeyboardCatalog = { state, options: [OFF, RELAY] };
    expect(settleKeyboardChoice("raindrop-tile", catalog, RELAY, "bright-clack")).toEqual({ id: "raindrop-tile", options: [OFF, RELAY, UNAVAILABLE("raindrop-tile")], repaired: false });
  });

  it("catalogue not ready and the saved id is the built-in sound, Off or already listed: no extra choice", () => {
    const catalog: KeyboardCatalog = { state: "missing", options: [OFF, RELAY, CRISP] };
    for (const id of ["relay", "off", "crisp-silk"]) {
      const settled = settleKeyboardChoice(id, catalog, RELAY, "bright-clack");
      expect(settled).toEqual({ id, options: catalog.options, repaired: false });
    }
  });

  it("catalogue not ready and the built-in was never listed: it is added after Off, and the saved built-in needs no extra choice", () => {
    const catalog: KeyboardCatalog = { state: "missing", options: [OFF] };
    expect(settleKeyboardChoice("relay", catalog, RELAY)).toEqual({ id: "relay", options: [OFF, RELAY], repaired: false });
    expect(settleKeyboardChoice("deep", catalog, RELAY).options).toEqual([OFF, RELAY, UNAVAILABLE("deep")]);
    expect(settleKeyboardChoice("deep", { state: "missing", options: [] }, RELAY).options).toEqual([RELAY, UNAVAILABLE("deep")]);
  });

  it("ready and the saved id is listed: kept as is, options untouched", () => {
    const catalog = ready({ defaultId: "bright-clack" });
    for (const id of ["raindrop-tile", "relay", "off"]) expect(settleKeyboardChoice(id, catalog, RELAY, "crisp-silk")).toEqual({ id, options: catalog.options, repaired: false });
    expect(settleKeyboardChoice("raindrop-tile", catalog, RELAY).options).toBe(catalog.options);
  });

  it("ready and the saved id is gone: defaultId, then the game's default, then the first set, then the built-in; repaired", () => {
    expect(settleKeyboardChoice("retired", ready({ defaultId: "raindrop-tile" }), RELAY, "bright-clack")).toMatchObject({ id: "raindrop-tile", repaired: true });
    expect(settleKeyboardChoice("retired", ready(), RELAY, "bright-clack")).toMatchObject({ id: "bright-clack", repaired: true });
    // A default the options do not list (or list disabled) is skipped.
    expect(settleKeyboardChoice("retired", ready({ defaultId: "gone" }), RELAY, "also-gone")).toMatchObject({ id: "crisp-silk", repaired: true });
    const disabledBright = ready({ options: [OFF, RELAY, { ...CRISP, disabled: true }, { ...BRIGHT, disabled: true }, RAIN], defaultId: "bright-clack" });
    expect(settleKeyboardChoice("retired", disabledBright, RELAY, "crisp-silk")).toMatchObject({ id: "raindrop-tile", repaired: true });
    // No set at all: the game's own sound.
    expect(settleKeyboardChoice("retired", { state: "ready", options: [OFF, RELAY] }, RELAY, "bright-clack")).toEqual({ id: "relay", options: [OFF, RELAY], repaired: true });
    expect(settleKeyboardChoice("retired", { state: "ready", options: [OFF] }, RELAY)).toEqual({ id: "relay", options: [OFF, RELAY], repaired: true });
  });

  it("no saved id (null or undefined): the catalogue's default, not saved; without a ready catalogue the built-in", () => {
    for (const none of [null, undefined]) {
      expect(settleKeyboardChoice(none, ready({ defaultId: "raindrop-tile" }), RELAY, "bright-clack")).toEqual({ id: "raindrop-tile", options: ready().options, repaired: false });
      expect(settleKeyboardChoice(none, ready(), RELAY, "bright-clack")).toMatchObject({ id: "bright-clack", repaired: false });
      expect(settleKeyboardChoice(none, ready(), RELAY)).toMatchObject({ id: "crisp-silk", repaired: false });
      for (const state of ["missing", "invalid"] as const) {
        // No "Saved sound · unavailable" row: nothing was saved.
        expect(settleKeyboardChoice(none, { state, options: [OFF, RELAY] }, RELAY, "bright-clack")).toEqual({ id: "relay", options: [OFF, RELAY], repaired: false });
        expect(settleKeyboardChoice(none, { state, options: [OFF] }, RELAY)).toEqual({ id: "relay", options: [OFF, RELAY], repaired: false });
      }
    }
  });

  it("a saved string that can never name a set (\"\", \"Bad Id\", \"../x\"): the default, repaired, never listed", () => {
    for (const bogus of ["", "Bad Id", "../x", "x".repeat(33)]) {
      expect(settleKeyboardChoice(bogus, ready({ defaultId: "raindrop-tile" }), RELAY, "bright-clack")).toEqual({ id: "raindrop-tile", options: ready().options, repaired: true });
      expect(settleKeyboardChoice(bogus, { state: "missing", options: [OFF, RELAY] }, RELAY, "bright-clack")).toEqual({ id: "relay", options: [OFF, RELAY], repaired: true });
    }
    // An option the catalogue lists is kept whatever its shape (a game's own sound).
    const odd: KeyboardSoundChoice = { value: "Original_Keys", label: "Original" };
    expect(settleKeyboardChoice("Original_Keys", { state: "missing", options: [OFF] }, odd)).toEqual({ id: "Original_Keys", options: [OFF, odd], repaired: false });
  });

  it("ready and the saved id is listed but disabled: repaired like a missing one", () => {
    const catalog = ready({ options: [OFF, RELAY, { ...RAIN, disabled: true }, BRIGHT], defaultId: "bright-clack" });
    expect(settleKeyboardChoice("raindrop-tile", catalog, RELAY)).toMatchObject({ id: "bright-clack", repaired: true });
  });

  it("Wordwoven's rule (quick.ts keyboardChoices) gives the same id, options and repaired flag", () => {
    const BAMBOO: KeyboardSoundChoice = { value: "bamboo", label: "Bamboo (original)" };
    // Wordwoven today: listed → keep; not ready → append the unavailable choice; ready → default, first set, Bamboo.
    const wordwoven = (saved: string, catalog: KeyboardCatalog): { id: string; options: readonly KeyboardSoundChoice[]; repaired: boolean } => {
      const options = catalog.options;
      if (options.some((choice) => choice.value === saved)) return { id: saved, options, repaired: false };
      if (catalog.state !== "ready") return { id: saved, options: [...options, UNAVAILABLE(saved)], repaired: false };
      return { id: (options.find((choice) => choice.value === "bright-clack") ?? options.find((choice) => choice.manifest !== undefined) ?? BAMBOO).value, options, repaired: true };
    };
    const catalogs: KeyboardCatalog[] = [
      { state: "ready", options: [OFF, BAMBOO, CRISP, RAIN, BRIGHT] },
      { state: "ready", options: [OFF, BAMBOO, CRISP, RAIN] },
      { state: "ready", options: [OFF, BAMBOO] },
      { state: "missing", options: [OFF, BAMBOO] },
      { state: "invalid", options: [OFF, BAMBOO] },
    ];
    for (const catalog of catalogs) {
      for (const saved of ["bright-clack", "raindrop-tile", "bamboo", "off", "retired"]) {
        expect(settleKeyboardChoice(saved, catalog, BAMBOO, "bright-clack"), `${catalog.state} ${catalog.options.length} ${saved}`).toEqual(wordwoven(saved, catalog));
      }
    }
  });
});

describe("pendingKeyboardChoices: the keyboard row before the catalogue arrives", () => {
  const LOADING = (id: string): KeyboardSoundChoice => ({ value: id, label: "Loading…", note: "", disabled: true });

  it("Off, the built-in, and the saved set as a disabled Loading… choice", () => {
    expect(pendingKeyboardChoices("raindrop-tile", RELAY)).toEqual([OFF, RELAY, LOADING("raindrop-tile")]);
  });

  it("no Loading… choice for Off, the built-in, no saved id, or an id that cannot name a set", () => {
    for (const saved of ["off", "relay", null, undefined, "", "Bad Id"]) expect(pendingKeyboardChoices(saved, RELAY)).toEqual([OFF, RELAY]);
    expect(pendingKeyboardChoices("deep", OFF)).toEqual([OFF, LOADING("deep")]);
  });

  it("then settleKeyboardChoice gives the real list, still holding the saved set", async () => {
    const pending = pendingKeyboardChoices("raindrop-tile", RELAY);
    const catalog = await loadKeyboardCatalog(BASE, { extra: [RELAY], fallback: [], fetchJson: json(CATALOGUE_3) });
    const settled = settleKeyboardChoice("raindrop-tile", catalog, RELAY, "bright-clack");
    expect(pending.map((choice) => choice.value)).toContain(settled.id);
    expect(settled).toMatchObject({ id: "raindrop-tile", repaired: false });
  });
});

describe("typingFeelKeysBase: the keys base from VITE_TYPING_FEEL_ORIGIN", () => {
  it.each([
    [ORIGIN, BASE],
    [ORIGIN + "/", BASE],
    [ORIGIN + "///", BASE],
    ["  " + ORIGIN + "  ", BASE],
    ["http://127.0.0.1:8090", "http://127.0.0.1:8090/v1/keys/"],
    ["https://cdn.example.com/feel/", "https://cdn.example.com/feel/v1/keys/"],
  ])("%j → %j", (origin, base) => {
    expect(typingFeelKeysBase(origin)).toBe(base);
  });

  it.each([
    undefined, "", "   ", "feel.typing-game.local", "/v1/keys/", "ftp://feel.typing-game.local", "file:///tmp/keys", "javascript:alert(1)",
    "https://", "https://user:secret@feel.typing-game.local", "https://feel.typing-game.local/?x=1", "https://feel.typing-game.local/#top",
    "https://feel.typing-game.local?", "https://feel typing-game.local",
  ])("%j → null", (origin) => {
    expect(typingFeelKeysBase(origin)).toBeNull();
  });
});

describe("Typing Feel data API: exported beside the other keyboard helpers", () => {
  it("feedback/typing-fx and ui/quick-settings export it", () => {
    for (const name of ["pendingKeyboardChoices", "settleKeyboardChoice", "timedJson", "typingFeelKeysBase"] as const) {
      expect(typeof fxIndex[name]).toBe("function");
      expect(quickIndex[name]).toBe(fxIndex[name]);
    }
    expect(fxIndex.KEYBOARD_CATALOG_TIMEOUT_MS).toBe(3000);
    expect(fxIndex.KEYBOARD_FIRST_BATCH_SPACES).toBe(4);
  });
});
