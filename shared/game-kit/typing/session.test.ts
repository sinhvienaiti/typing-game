// Source: new for the kit: a stream of words over the real shared vocabulary (TD's td-calls checks this on its world)
import { existsSync, readFileSync } from "node:fs";
import { describe, expect, it } from "vitest";
import { createRng } from "../platform/rng";
import { availableLetters, bandWords, compileDeck, firstLetterOf, gloss, wordText, type DeckEntry } from "./decks";
import { withinOneEdit } from "./distance";
import { compileTyping, TD_TYPING, typingConfig } from "./config";
import { createBag } from "./picker";
import { KEY } from "./router";
import { addWord, createSession, dealWord, dropWord, typeLetter } from "./session";
import { letterBudget } from "./budget";

const LEVELS = new URL("../../vocabulary/levels/", import.meta.url);
const level = (n: number): { id: string; en: string; vi: string; ipa: string }[] =>
  JSON.parse(readFileSync(new URL(String(n).padStart(3, "0") + ".json", LEVELS), "utf8")).entries;
const hasVocabulary = existsSync(new URL("001.json", LEVELS));

describe("decks", () => {
  it("keeps a–z words within the bounds, first spelling only, with a hash that follows letters and levels", () => {
    const entries: DeckEntry[] = ["cat", "dog", "ox", "Dog", "dragonfly", "cat", "fern"].map((text, index) => ({ id: "e" + index, text, level: 1, vi: "nghĩa " + index }));
    const deck = compileDeck(entries);
    expect([...deck.ids]).toEqual(["e0", "e1", "e6"]);
    expect(compileDeck(entries, { min: 2, max: 9 }).count).toBe(5);
    expect(compileDeck(entries).hash).toBe(deck.hash);
    expect(compileDeck(entries.map((entry) => ({ ...entry, level: 2 }))).hash).not.toBe(deck.hash);
    expect(wordText(deck, 2)).toBe("fern");
    expect(gloss(compileDeck([{ id: "x", text: "never", level: 1, vi: "chưa bao giờ, không bao giờ (trạng từ); không hề" }]), 0)).toBe("chưa bao giờ");
  });
});

describe.skipIf(!hasVocabulary)("a stream on the shared vocabulary", () => {
  it("keeps every live first letter unique (tier 1), every pair told apart by its second letter, no two words one edit apart", () => {
    const rules = compileTyping(typingConfig(TD_TYPING, { router: { protectS: 1.2 } }));
    const entries = [1, 2, 3].flatMap((n) => level(n).map((entry) => ({ id: entry.id, text: entry.en.trim().toLowerCase(), level: n, vi: entry.vi, ipa: entry.ipa })));
    const deck = compileDeck(entries);
    const words = bandWords(deck, 3, 3, 6);
    const budget = letterBudget(availableLetters(deck, words, rules.letters.minWordsPerLetter), rules.budget);
    expect(budget.total).toBeGreaterThanOrEqual(10);
    const t = createSession(rules, deck, 32);
    const bag = createBag(words);
    const rng = createRng(11).words;
    const kind = rules.kind.call!;
    let dealt = 0;
    let jams = 0;
    for (let tick = 0; tick < 60 * 120; tick += 1) {
      // Every 0.25 s: a word for each free slot of the budget; one in five live words is typed out, one in seven dies.
      if (tick % 15 === 0) {
        while (t.words.count < budget.total) {
          if (dealWord(t, bag, kind, tick, 3, -1, rng) < 0) {
            jams += 1;
            break;
          }
          dealt += 1;
        }
      }
      if (tick % 20 === 7) {
        const live = t.words.live();
        const s = live[tick % live.length]!;
        if (tick % 140 === 7) dropWord(t, s, tick);
        else if (t.router.lock < 0) {
          // A tier-2 word types the same: its first key opens the pair, its second picks it.
          const text = wordText(deck, t.words.word[s]!);
          const results = [...text].map((ch) => typeLetter(t, ch.charCodeAt(0) - 97, tick).result);
          expect(results[results.length - 1]).toBe(KEY.done);
          dropWord(t, s, tick);
        }
      }
      // The live words change only on those ticks.
      if (tick % 15 !== 0 && tick % 20 !== 7) continue;
      const live = t.words.live();
      const owners = new Map<number, number[]>();
      for (const s of live) {
        const c = firstLetterOf(deck, t.words.word[s]!);
        owners.set(c, [...(owners.get(c) ?? []), s]);
      }
      for (const [c, slots] of owners) {
        expect(slots.length).toBeLessThanOrEqual(2);
        if (slots.length === 2) {
          const [a, b] = slots.map((s) => t.words.word[s]!) as [number, number];
          expect(deck.letters[deck.start[a]! + 1]).not.toBe(deck.letters[deck.start[b]! + 1]);
        }
        expect(slots).toContain(t.letters.owner[c]!);
      }
      for (let i = 0; i < live.length; i += 1) {
        for (let j = i + 1; j < live.length; j += 1) {
          const a = t.words.word[live[i]!]!;
          const b = t.words.word[live[j]!]!;
          expect(withinOneEdit(deck.letters, deck.start[a]!, deck.len[a]!, deck.start[b]!, deck.len[b]!, rules.letters.maxEditCheckLen), wordText(deck, a) + " / " + wordText(deck, b)).toBe(false);
        }
      }
    }
    expect(dealt).toBeGreaterThan(200);
    expect(jams).toBeLessThan(dealt / 4);
    expect(t.stats.lost).toBe(0);
  });
});

describe("session store", () => {
  it("puts a word live on any target the game names, and gives a full store −1", () => {
    const deck = compileDeck(["cat", "dog"].map((text, index) => ({ id: "w" + index, text, level: 1 })));
    const t = createSession(compileTyping(TD_TYPING), deck, 1);
    expect(addWord(t, 0, 0, 1, 0, 4242)).toBe(0);
    expect(t.words.owner[0]).toBe(4242);
    expect(addWord(t, 1, 0, 1, 0)).toBe(-1);
    expect(dealWord(t, createBag(Int32Array.of(1)), 0, 0, 1, -1, createRng(1).words)).toBe(-1);
  });
});
