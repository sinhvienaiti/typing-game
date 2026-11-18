// Source: new for the kit: typing-fx's driver on the kit's real typing session (feedback reflects, never decides)
import { describe, expect, it } from "vitest";
import { compileTyping, TD_TYPING } from "../../typing/config";
import { compileDeck, firstLetterOf, wordIndex, wordText } from "../../typing/decks";
import { KEY } from "../../typing/router";
import { addWord, createSession, dropWord, typeBackspace, typeLetter } from "../../typing/session";
import { kitKind, TypingFxDriver, type TypingFxProgress, type TypingFxSink } from "./driver";

/** A sink that writes down every call. */
function recorder(): TypingFxSink & { log: string[] } {
  const log: string[] = [];
  return {
    log,
    setWord: (text, _meaning, typed, _now, mask) => log.push(`word ${text} ${typed}` + (mask ? ` mask ${mask}` : "")),
    mask: (hidden) => log.push(`mask ${hidden}`),
    key: (index) => log.push(`key ${index}`),
    wrong: (index) => log.push(`wrong ${index}`),
    stray: () => log.push("stray"),
    back: (typed) => log.push(`back ${typed}`),
    complete: (perfect, combo) => log.push(`complete ${perfect} ${combo}`),
    clear: () => log.push("clear"),
  };
}

const rules = compileTyping(TD_TYPING);
const deck = compileDeck(["cat", "dog", "fish", "frog", "bird", "duck"].map((text, index) => ({ id: "w" + index, text, level: 1, vi: "nghĩa " + text })));
const letter = (ch: string): number => ch.charCodeAt(0) - 97;

/** A game's view: one reused snapshot, filled from the kit session after each key. */
function play(keys: string, words: string[]): string[] {
  const t = createSession(rules, deck);
  for (const text of words) {
    const word = wordIndex(deck, text);
    addWord(t, word, rules.kind.call!, t.letters.owner[firstLetterOf(deck, word)]! >= 0 ? 2 : 1, 0);
  }
  const sink = recorder();
  const driver = new TypingFxDriver([sink]);
  const p: TypingFxProgress = { kind: "stray", word: -1, text: "", meaning: "", typed: 0, combo: 0 };
  let combo = 0;
  let tick = 0;
  for (const ch of keys) {
    tick += 1;
    if (ch === "<") {
      const slot = t.router.lock;
      typeBackspace(t);
      p.kind = "back";
      p.word = slot;
      p.typed = slot >= 0 ? t.words.typed[slot]! : 0;
      driver.progress(p, tick);
      continue;
    }
    const before = t.router.lock;
    const { result, slot } = typeLetter(t, letter(ch), tick);
    const kind = kitKind(result);
    if (kind === null) continue;
    const s = kind === "stray" ? before : slot;
    p.kind = kind;
    p.word = s;
    p.text = s >= 0 ? wordText(deck, t.words.word[s]!) : "";
    p.typed = s >= 0 ? t.words.typed[s]! : 0;
    if (result === KEY.done) {
      combo = t.words.errors[s]! === 0 ? combo + 1 : 0;
      p.combo = combo;
      p.perfect = t.words.errors[s]! === 0;
      dropWord(t, s, tick);
    } else p.perfect = undefined;
    driver.progress(p, tick);
  }
  return sink.log;
}

describe("typing-fx driver", () => {
  it("maps the kit router's KEY codes", () => {
    expect(kitKind(KEY.stray)).toBe("stray");
    expect(kitKind(KEY.lock)).toBe("lock");
    expect(kitKind(KEY.advance)).toBe("advance");
    expect(kitKind(KEY.done)).toBe("done");
    expect(kitKind(KEY.wrong)).toBe("wrong");
    expect(kitKind(KEY.switch)).toBe("switch");
    expect(kitKind(KEY.group)).toBeNull();
    expect(kitKind(KEY.forgiven)).toBeNull();
    expect(kitKind(99)).toBeNull();
  });

  it("a clean word: the lock shows the word, each letter plays once, one complete", () => {
    expect(play("cat", ["cat", "dog"])).toEqual(["word cat 0", "key 0", "key 1", "key 2", "complete true 1"]);
  });

  it("a wrong key marks the due letter and the word is no longer perfect", () => {
    expect(play("cxat", ["cat"])).toEqual(["word cat 0", "key 0", "wrong 1", "key 1", "key 2", "complete false 0"]);
  });

  it("a stray key with nothing locked plays a stray, never a key", () => {
    expect(play("zcat", ["cat"])).toEqual(["stray", "word cat 0", "key 0", "key 1", "key 2", "complete true 1"]);
  });

  it("a soft switch shows the new word with its first letter as a key", () => {
    // "d" locks dog; "c" switches to cat (soft switch, no error yet).
    expect(play("dcat", ["cat", "dog"])).toEqual(["word dog 0", "key 0", "word cat 0", "key 0", "key 1", "key 2", "complete true 1"]);
  });

  it("a tier-2 pair resolving puts two letters in on one key: both play", () => {
    // fish and frog share f: "f" opens the pair (no feedback), "r" picks frog with 2 letters in.
    expect(play("frog", ["fish", "frog"])).toEqual(["word frog 0", "key 0", "key 1", "key 2", "key 3", "complete true 1"]);
  });

  it("backspace takes letters back, and to zero drops the word", () => {
    expect(play("ca<<", ["cat"])).toEqual(["word cat 0", "key 0", "key 1", "back 1", "back 0"]);
  });

  it("a word that leaves unfinished clears the strip; another word's release is ignored", () => {
    const sink = recorder();
    const driver = new TypingFxDriver([sink]);
    driver.progress({ kind: "lock", word: 4, text: "duck", meaning: "con vịt", typed: 1, combo: 0 }, 1);
    driver.progress({ kind: "release", word: 2, text: "", meaning: "", typed: 0, combo: 0 }, 2);
    driver.progress({ kind: "release", word: 4, text: "", meaning: "", typed: 0, combo: 0 }, 3);
    expect(sink.log).toEqual(["word duck 0", "key 0", "clear"]);
    expect(driver.word).toBe(-1);
  });

  it("a word shown with no key (it comes locked) plays no key until one comes", () => {
    const sink = recorder();
    const driver = new TypingFxDriver([sink]);
    driver.progress({ kind: "show", word: 3, text: "frog", meaning: "", typed: 0, combo: 0 }, 1);
    driver.progress({ kind: "advance", word: 3, text: "frog", meaning: "", typed: 1, combo: 0 }, 2);
    expect(sink.log).toEqual(["word frog 0", "key 0"]);
  });

  it("a game's hidden letters go with the word; a reveal is passed on once", () => {
    const sink = recorder();
    const driver = new TypingFxDriver([sink]);
    const p: TypingFxProgress = { kind: "lock", word: 7, text: "planet", meaning: "", typed: 1, combo: 0, mask: 0b10100 };
    driver.progress(p, 1);
    p.kind = "wrong";
    p.mask = 0b10000; // the wrong key revealed letter 2
    driver.progress(p, 2);
    driver.progress(p, 3); // unchanged: nothing more
    expect(sink.log).toEqual(["word planet 0 mask 20", "key 0", "mask 16", "wrong 1", "wrong 1"]);
  });

  it("every sink gets the same calls (strip and sounds stay in step)", () => {
    const a = recorder();
    const b = recorder();
    const driver = new TypingFxDriver([a, b]);
    driver.progress({ kind: "lock", word: 1, text: "ox", meaning: "", typed: 1, combo: 0 }, 1);
    driver.progress({ kind: "done", word: 1, text: "ox", meaning: "", typed: 2, combo: 10 }, 2);
    expect(a.log).toEqual(b.log);
    expect(a.log).toEqual(["word ox 0", "key 0", "key 1", "complete true 10"]);
  });
});
