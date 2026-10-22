// Source: games/space-typing@feat/td-1a6 tests/td-router.test.ts (kit copy, on a typing session instead of TD's world)
import { describe, expect, it } from "vitest";
import { compileTyping, TD_TYPING, typingConfig } from "./config";
import { compileDeck, firstLetterOf, wordIndex, type Deck } from "./decks";
import { KEY } from "./router";
import { gradeWord, type Grade } from "./scorer";
import { addWord, createSession, dropWord, lockNext, shieldLeft, shieldLock, typeBackspace, typeLetter, unlock, wordTiming, type TypingSession, type WordTiming } from "./session";

/** The key router (docs/td/TYPING_DEFENSE_DESIGN.md 6.15) and the session around it. */
const rules = compileTyping(TD_TYPING);
const letter = (ch: string): number => ch.charCodeAt(0) - 97;
const smallDeck = (words: readonly string[]): Deck => compileDeck(words.map((text, index) => ({ id: "w" + index, text, level: 1 })));
const deck = smallDeck(["cat", "dog", "fish", "frog", "bird", "duck", "flame", "fresh"]);

type Hit = { slot: number; grade: Grade; timing: WordTiming };

/** A session with `words` live (tier 2 when the letter is taken), as a game would put them on its targets. */
function withWords(...words: string[]): { t: TypingSession; slot: (text: string) => number; hits: Hit[] } {
  const t = createSession(rules, deck);
  for (const text of words) {
    const word = wordIndex(deck, text);
    addWord(t, word, rules.kind.call!, t.letters.owner[firstLetterOf(deck, word)]! >= 0 ? 2 : 1, 0);
  }
  const slot = (text: string) => t.words.live().find((s) => t.words.word[s] === wordIndex(deck, text))!;
  return { t, slot, hits: [] };
}

/** Sends `text` one key a tick from `from` (or all on one tick with `step` 0); a typed word is graded, then dropped. */
function type(s: { t: TypingSession; hits: Hit[] }, text: string, from = 0, step = 1): number[] {
  let tick = from;
  return [...text].map((ch) => {
    const { result, slot } = typeLetter(s.t, letter(ch), tick);
    if (result === KEY.done) {
      const timing = wordTiming(s.t, slot, tick);
      s.hits.push({ slot, timing, grade: gradeWord(s.t.rules, timing, 35, 1000) });
      dropWord(s.t, slot, tick);
    }
    tick += step;
    return result;
  });
}

describe("key router", () => {
  it("a tier-1 first letter locks its word; right letters move it on, a wrong one is an error that does not", () => {
    const s = withWords("cat", "dog");
    expect(type(s, "cx")).toEqual([KEY.lock, KEY.wrong]);
    expect(s.t.router.lock).toBe(s.slot("cat"));
    expect([s.t.words.typed[s.slot("cat")], s.t.words.errors[s.slot("cat")]]).toEqual([1, 1]);
    expect(type(s, "at", 2)).toEqual([KEY.advance, KEY.done]);
    expect(s.hits).toMatchObject([{ grade: "ok", timing: { errors: 1, len: 3 } }]);
    expect(s.t.router.lock).toBe(-1);
  });

  it("soft switch: one letter in, no error yet, a key that starts another word moves the lock; one shared error, none on the old word", () => {
    const s = withWords("cat", "dog");
    expect(type(s, "cd")).toEqual([KEY.lock, KEY.switch]);
    expect(s.t.router.lock).toBe(s.slot("dog"));
    expect([s.t.words.typed[s.slot("cat")], s.t.words.errors[s.slot("cat")], s.t.words.touched[s.slot("cat")]]).toEqual([0, 0, 0]);
    expect(s.t.words.typed[s.slot("dog")]).toBe(1);
    expect(s.t.stats.errors).toBe(1);
    // Two letters in, the same key is an error on the locked word.
    const late = withWords("cat", "dog");
    expect(type(late, "cad")).toEqual([KEY.lock, KEY.advance, KEY.wrong]);
    expect(late.t.words.errors[late.slot("cat")]).toBe(1);
  });

  it("the soft switch's reach is a rule: 0 letters (came locked only) or 2", () => {
    const strict = createSession(compileTyping(typingConfig(TD_TYPING, { router: { softSwitchMaxTyped: 0 } })), deck);
    addWord(strict, wordIndex(deck, "cat"), 0, 1, 0);
    addWord(strict, wordIndex(deck, "dog"), 0, 1, 0);
    expect([typeLetter(strict, letter("c"), 0).result, typeLetter(strict, letter("d"), 1).result]).toEqual([KEY.lock, KEY.wrong]);
    const loose = createSession(compileTyping(typingConfig(TD_TYPING, { router: { softSwitchMaxTyped: 2 } })), deck);
    addWord(loose, wordIndex(deck, "cat"), 0, 1, 0);
    addWord(loose, wordIndex(deck, "dog"), 0, 1, 0);
    expect(["c", "a", "d"].map((ch, k) => typeLetter(loose, letter(ch), k).result)).toEqual([KEY.lock, KEY.advance, KEY.switch]);
  });

  it("a tier-2 pair opens on its letter; the second key picks the word, a miss is an error on the older one", () => {
    const s = withWords("fish", "frog");
    expect(s.t.words.tier[s.slot("frog")]).toBe(2);
    expect(type(s, "fr")).toEqual([KEY.group, KEY.advance]);
    expect([s.t.router.lock, s.t.words.typed[s.slot("frog")]]).toEqual([s.slot("frog"), 2]);
    // The pair's first key is the word's first key.
    expect(s.t.words.firstTick[s.slot("frog")]).toBe(0);
    const miss = withWords("fish", "frog");
    expect(type(miss, "fx")).toEqual([KEY.group, KEY.wrong]);
    expect([miss.t.router.lock, miss.t.words.typed[miss.slot("fish")], miss.t.words.errors[miss.slot("fish")]]).toEqual([miss.slot("fish"), 1, 1]);
  });

  it("when a pair's first word ends, the other one is told by its first letter alone (tier 1)", () => {
    const s = withWords("fish", "frog");
    const frog = s.slot("frog");
    type(s, "fish");
    expect(s.t.words.tier[frog]).toBe(1);
    expect(type(s, "f", 10)).toEqual([KEY.lock]);
    expect(s.t.router.lock).toBe(frog);
  });

  it("errors stop at 255: a flood of wrong keys in one tick never wraps a word back to clean", () => {
    const s = withWords("cat");
    type(s, "c" + "x".repeat(300) + "at", 1, 0);
    expect(s.hits).toMatchObject([{ grade: "sloppy", timing: { errors: 255 } }]);
  });

  it("Backspace takes a letter back (errors stay) and at 0 lets go", () => {
    const s = withWords("bird");
    type(s, "bix");
    typeBackspace(s.t);
    expect([s.t.words.typed[s.slot("bird")], s.t.words.errors[s.slot("bird")], s.t.router.lock]).toEqual([1, 1, s.slot("bird")]);
    typeBackspace(s.t);
    expect(s.t.router.lock).toBe(-1);
    expect(s.t.words.touched[s.slot("bird")]).toBe(1);
    // Nothing locked: Backspace does nothing.
    expect(typeBackspace(s.t)).toBe(false);
    // An open pair just closes.
    const pair = withWords("fish", "frog");
    type(pair, "f");
    expect(typeBackspace(pair.t)).toBe(true);
    expect(pair.t.router.group).toBe(-1);
  });

  it("a word that comes locked with no letter in (a target's next word): another word's first letter switches, Backspace lets go", () => {
    const s = withWords("cat", "dog");
    lockNext(s.t, s.slot("cat"));
    expect(type(s, "d")).toEqual([KEY.switch]);
    expect([s.t.router.lock, s.t.words.typed[s.slot("dog")], s.t.words.errors[s.slot("cat")]]).toEqual([s.slot("dog"), 1, 0]);
    const back = withWords("cat");
    lockNext(back.t, back.slot("cat"));
    typeBackspace(back.t);
    expect([back.t.router.lock, back.t.words.typed[back.slot("cat")]]).toEqual([-1, 0]);
    // Its first key goes on: the word's first key is that key.
    const on = withWords("cat");
    lockNext(on.t, on.slot("cat"));
    expect(type(on, "ca", 30)).toEqual([KEY.advance, KEY.advance]);
    expect(on.t.words.firstTick[on.slot("cat")]).toBe(30);
    // A wrong key that starts nothing is still an error on the locked word; after it, no switch.
    const typo = withWords("cat", "dog");
    lockNext(typo.t, typo.slot("cat"));
    expect(type(typo, "xd")).toEqual([KEY.wrong, KEY.wrong]);
  });

  it("unlock (Esc) lets go of the word and drops what was typed, errors uncounted; a key that starts nothing is a stray", () => {
    const s = withWords("duck");
    type(s, "dux");
    expect(unlock(s.t)).toBe(true);
    expect([s.t.router.lock, s.t.words.typed[s.slot("duck")], s.t.words.errors[s.slot("duck")]]).toEqual([-1, 0, 0]);
    type(s, "duck", 50, 0);
    expect(s.hits).toMatchObject([{ timing: { errors: 0 } }]);
    const again = withWords("duck");
    expect(type(again, "z")).toEqual([KEY.stray]);
    expect(again.t.stats.strays).toBe(1);
  });

  it("several keys in one tick route in order", () => {
    const s = withWords("flame");
    expect(type(s, "flame", 50, 0)).toEqual([KEY.lock, KEY.advance, KEY.advance, KEY.advance, KEY.done]);
    expect(s.t.stats.done).toBe(1);
  });
});

describe("word timing (what a game grades by)", () => {
  it("counts ticks from birth to the first key, first key to last, birth to done", () => {
    const t = createSession(rules, deck);
    const s = addWord(t, wordIndex(deck, "flame"), 0, 1, 100);
    let done: WordTiming | null = null;
    [..."flame"].forEach((ch, k) => {
      const out = typeLetter(t, letter(ch), 130 + k * 10);
      if (out.result === KEY.done) done = wordTiming(t, out.slot, 130 + k * 10);
    });
    expect(done).toEqual({ len: 5, errors: 0, toFirstKey: 30, typing: 40, total: 70 });
    expect(t.words.used[s]).toBe(1); // the game drops it after grading
  });

  it("a soft switch away drops the old word's progress: its next first key starts its clock again", () => {
    const t = createSession(rules, deck);
    const cat = addWord(t, wordIndex(deck, "cat"), 0, 1, 0);
    addWord(t, wordIndex(deck, "dog"), 0, 1, 0);
    typeLetter(t, letter("c"), 10);
    typeLetter(t, letter("d"), 20);
    typeLetter(t, letter("x"), 25); // an error on dog: no switch back
    expect(t.router.lock).not.toBe(cat);
    unlock(t);
    typeLetter(t, letter("c"), 40);
    expect(t.words.firstTick[cat]).toBe(40);
  });
});

describe("lock protection (dragon-hold 01 §3.3)", () => {
  const dragon = compileTyping(typingConfig(TD_TYPING, { router: { protectS: 1.2 } }));
  const session = () => {
    const t = createSession(dragon, deck);
    const cat = addWord(t, wordIndex(deck, "cat"), 0, 1, 0);
    const dog = addWord(t, wordIndex(deck, "dog"), 0, 1, 0);
    return { t, cat, dog };
  };

  it("is off by default (TD) and needs a lock with a letter in", () => {
    const off = createSession(rules, deck);
    const cat = addWord(off, wordIndex(deck, "cat"), 0, 1, 0);
    typeLetter(off, letter("c"), 0);
    expect(shieldLock(off, cat, 1)).toBe(false);
    const { t, cat: c2, dog } = session();
    expect(shieldLock(t, c2, 0)).toBe(false); // not locked
    lockNext(t, c2);
    expect(shieldLock(t, c2, 0)).toBe(false); // locked, nothing typed
    typeLetter(t, letter("c"), 1);
    expect(shieldLock(t, dog, 2)).toBe(false); // another word
    expect(shieldLock(t, c2, 2)).toBe(true);
  });

  it("holds the target 1.2 s from the first lethal blow; typed in time, the word is done; after, the lock is lost unpunished", () => {
    const { t, cat } = session();
    typeLetter(t, letter("c"), 10);
    expect(shieldLock(t, cat, 100)).toBe(true);
    expect(shieldLeft(t, cat, 130)).toBe(72 - 30);
    expect(shieldLock(t, cat, 171)).toBe(true);
    expect(shieldLock(t, cat, 172)).toBe(false);
    // The game lets the target die: the lock goes, counted, and the next stray is forgiven.
    dropWord(t, cat, 172);
    expect([t.router.lock, t.stats.lost, t.stats.errors]).toEqual([-1, 1, 0]);
    expect(typeLetter(t, letter("a"), 173).result).toBe(KEY.forgiven);
    expect(typeLetter(t, letter("t"), 174).result).toBe(KEY.stray);
    expect([t.stats.forgiven, t.stats.strays]).toEqual([1, 1]);
  });

  it("the next key after a lost lock still counts: it may lock another word", () => {
    const { t, cat, dog } = session();
    typeLetter(t, letter("c"), 0);
    dropWord(t, cat, 100);
    expect(typeLetter(t, letter("d"), 101)).toEqual({ result: KEY.lock, slot: dog });
  });

  it("a new lock opens a new window; counting from the lock's first letter is a rule", () => {
    const { t, cat, dog } = session();
    typeLetter(t, letter("c"), 0);
    expect(shieldLock(t, cat, 10)).toBe(true);
    typeLetter(t, letter("d"), 20); // soft switch to dog
    typeLetter(t, letter("o"), 21);
    expect(shieldLock(t, dog, 200)).toBe(true);
    expect(shieldLeft(t, dog, 230)).toBe(42);
    const fromLock = createSession(compileTyping(typingConfig(TD_TYPING, { router: { protectS: 1.2, protectFrom: "lock" } })), deck);
    const c = addWord(fromLock, wordIndex(deck, "cat"), 0, 1, 0);
    typeLetter(fromLock, letter("c"), 50);
    expect(shieldLock(fromLock, c, 121)).toBe(true);
    expect(shieldLock(fromLock, c, 122)).toBe(false);
  });

  it("a word dropped with nothing typed, or typed out, is not a lost lock", () => {
    const { t, cat, dog } = session();
    lockNext(t, cat);
    dropWord(t, cat, 5);
    typeLetter(t, letter("d"), 6);
    typeLetter(t, letter("o"), 7);
    const done = typeLetter(t, letter("g"), 8);
    expect(done).toEqual({ result: KEY.done, slot: dog });
    dropWord(t, dog, 8);
    expect(t.stats.lost).toBe(0);
  });
});
