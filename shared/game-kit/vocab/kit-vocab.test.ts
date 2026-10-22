import { afterEach, describe, expect, it, vi } from "vitest";
import {
  WordPicker,
  clearVocabularyRuntimeCache,
  filterVocabularyEntries,
  isMatureEntry,
  isSensitiveEntry,
  loadVocabularyIndex,
  loadVocabularyKeys,
  loadVocabularyLevel,
  parseCustomVocabulary,
  textHasBlockedWord,
  vocabularyLevelUrl,
  vocabularyUrl,
  type VocabularyEntry,
  type VocabularyIndex,
} from "./index";

function entries(words: readonly string[]): VocabularyEntry[] {
  return words.map((en, index) => ({ id: "w" + String(index), en, vi: "", ipa: "" }));
}

const index: VocabularyIndex = {
  version: 1,
  plannedLevels: 100,
  availableLevels: 1,
  totalEntries: 4,
  levels: [{ level: 1, label: "L1", file: "levels/001.json", count: 4 }],
};

function stubFetch(routes: Record<string, unknown>) {
  const fetchMock = vi.fn(async (url: string) => {
    const body = routes[url];
    return { ok: body !== undefined, json: async () => body } as Response;
  });
  vi.stubGlobal("fetch", fetchMock);
  return fetchMock;
}

afterEach(() => {
  clearVocabularyRuntimeCache();
  vi.unstubAllGlobals();
});

describe("content filter (00-canon D15)", () => {
  it("drops sensitive words always and mature words only on request", () => {
    const list = entries(["dragon", "shit", "kill", "fire"]);
    expect(filterVocabularyEntries(list).map((entry) => entry.en)).toEqual(["dragon", "kill", "fire"]);
    expect(filterVocabularyEntries(list, { excludeMature: true }).map((entry) => entry.en)).toEqual(["dragon", "fire"]);
  });

  it("reads data flags as well as the block lists", () => {
    expect(isSensitiveEntry({ id: "a", en: "harmless", vi: "", ipa: "", sensitive: true })).toBe(true);
    expect(isMatureEntry({ id: "b", en: "harmless", vi: "", ipa: "", flags: ["mature"] })).toBe(true);
    expect(isSensitiveEntry({ id: "c", en: "dragon", vi: "", ipa: "" })).toBe(false);
  });

  it("checks every word of a phrase, whole words only", () => {
    expect(textHasBlockedWord("kill time", { excludeMature: true })).toBe(true);
    expect(textHasBlockedWord("kill time")).toBe(false);
    expect(textHasBlockedWord("Pass")).toBe(false);
    expect(textHasBlockedWord("class assignment")).toBe(false);
  });
});

describe("vocabulary base URL", () => {
  it("defaults to /vocabulary/ and accepts another base", () => {
    expect(vocabularyUrl("index.json")).toBe("/vocabulary/index.json");
    expect(vocabularyUrl("/levels/001.json", "/kit-words")).toBe("/kit-words/levels/001.json");
    expect(vocabularyLevelUrl(index.levels[0]!, "https://cdn.example/v/")).toBe("https://cdn.example/v/levels/001.json");
  });

  it("loads the index and levels from the given base and filters the level", async () => {
    const fetchMock = stubFetch({
      "/words/index.json": index,
      "/words/levels/001.json": { entries: entries(["dragon", "fuck", "gun", "river"]) },
    });
    const loaded = await loadVocabularyIndex({ baseUrl: "/words/" });
    expect(loaded.levels).toHaveLength(1);
    const all = await loadVocabularyLevel(1, loaded, { baseUrl: "/words/" });
    expect(all.map((entry) => entry.en)).toEqual(["dragon", "gun", "river"]);
    const child = await loadVocabularyLevel(1, loaded, { baseUrl: "/words/", excludeMature: true });
    expect(child.map((entry) => entry.en)).toEqual(["dragon", "river"]);
    expect(fetchMock).toHaveBeenCalledTimes(2);
  });

  it("drops blocked Smart Review keys instead of failing on them", async () => {
    stubFetch({
      "/vocabulary/lookup.json": { version: 1, totalEntries: 3, entries: { dragon: 1, shit: 1, river: 1 } },
      "/vocabulary/levels/001.json": { entries: entries(["dragon", "shit", "river"]) },
    });
    const loaded = await loadVocabularyKeys(["river", "shit", "dragon"], index);
    expect(loaded.entries.map((entry) => entry.en)).toEqual(["river", "dragon"]);
    expect(loaded).not.toHaveProperty("blocked");
  });

  it("drops custom rows with blocked words", () => {
    expect(parseCustomVocabulary("dragon | rồng\nshit | x\ngun | súng").map((entry) => entry.en)).toEqual(["dragon", "gun"]);
    expect(parseCustomVocabulary("gun | súng", { excludeMature: true })).toEqual([]);
  });
});

describe("WordPicker (from Space Campaign 3D)", () => {
  it("never gives two targets on screen the same first letter", () => {
    const picker = new WordPicker(entries(["apple", "angle", "banana", "bridge", "cherry", "comet", "delta", "dragon"]), 8, () => 0);
    const taken = new Set<string>();
    for (let step = 0; step < 4; step += 1) {
      const word = picker.pick("enemy", taken);
      expect(word).not.toBeNull();
      expect(taken.has(word!.text[0]!)).toBe(false);
      taken.add(word!.text[0]!);
    }
    expect(picker.pick("enemy", taken)).toBeNull();
  });

  it("keeps ordinary words within the stage's length and uses the whole band before repeating", () => {
    const picker = new WordPicker(entries(["sun", "moon", "star", "orbit", "planet", "satellite", "constellation", "comet"]), 6);
    const seen: string[] = [];
    for (let step = 0; step < 6; step += 1) seen.push(picker.pick("enemy", new Set())!.text);
    expect(seen.every((word) => word.length >= 3 && word.length <= 6)).toBe(true);
    expect(new Set(seen).size).toBe(6);
  });

  it("gives bosses phrases and the longest words", () => {
    const picker = new WordPicker(entries(["go", "cat", "dog", "rocket", "space station", "constellation", "sun", "map", "pen", "cup", "hat", "bag", "box", "car"]), 6, () => 0);
    expect(["spacestation", "constellation"]).toContain(picker.pick("boss", new Set())!.text);
  });

  it("never picks a blocked word", () => {
    const words = ["shit", "kill", "lamp", "moat", "nest", "oak", "pine", "quay"];
    const picker = new WordPicker(entries(words), 6, () => 0, { excludeMature: true });
    const picked = new Set<string>();
    for (let step = 0; step < 20; step += 1) picked.add(picker.pick("enemy", new Set())!.text);
    expect(picked.has("shit")).toBe(false);
    expect(picked.has("kill")).toBe(false);
  });
});
