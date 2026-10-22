// Source: new for the kit: the sound rules that need no AudioContext (Sinh Tồn S0 checked its sounds by ear)
import { describe, expect, it } from "vitest";
import { AudioCues, CUE_BUS_GAIN, keyStepRatio, pentatonicRatio } from "./audio-cues";
import { DRAGON, PRONUNCIATION_EVENT, SHIP } from "./profiles";

describe("audio cues", () => {
  it("wood keys climb a semitone a letter, at most 12 (dragon-hold 05 §7.2)", () => {
    expect(keyStepRatio(0, 12)).toBe(1);
    expect(keyStepRatio(1, 12)).toBeCloseTo(2 ** (1 / 12), 12);
    expect(keyStepRatio(12, 12)).toBeCloseTo(2, 12);
    expect(keyStepRatio(20, 12)).toBeCloseTo(2, 12);
    expect(keyStepRatio(-3, 12)).toBe(1);
    expect(DRAGON.audio.keys).toBe("wood");
    expect(DRAGON.audio.keySteps).toBe(12);
  });

  it("kill chains climb the pentatonic scale: a perfect word's note is a fifth up (C6 → G6)", () => {
    expect([0, 1, 2, 3, 4, 5].map((step) => Math.round(1000 * pentatonicRatio(step)) / 1000)).toEqual([1, 1.122, 1.26, 1.498, 1.682, 2]);
    expect(1046.5 * pentatonicRatio(3)).toBeCloseTo(1568, 0);
    expect(pentatonicRatio(99)).toBe(pentatonicRatio(12));
  });

  it("plays nothing before resume(), never throws without audio, and listens to kit speech's event until disposed", () => {
    const events = new EventTarget();
    let added = 0;
    let removed = 0;
    const counting = Object.assign(events, {
      addEventListener: (...args: Parameters<EventTarget["addEventListener"]>) => {
        added += args[0] === PRONUNCIATION_EVENT ? 1 : 0;
        EventTarget.prototype.addEventListener.apply(events, args);
      },
      removeEventListener: (...args: Parameters<EventTarget["removeEventListener"]>) => {
        removed += args[0] === PRONUNCIATION_EVENT ? 1 : 0;
        EventTarget.prototype.removeEventListener.apply(events, args);
      },
    });
    const cues = new AudioCues({ profile: DRAGON, events: counting });
    expect(cues.ready).toBe(false);
    cues.key(true, 3, 2);
    cues.key(false, 3);
    cues.word(true);
    cues.hit(3, 0, 0);
    cues.flush(100);
    cues.kill(3, 0, false, 100);
    events.dispatchEvent(new Event(PRONUNCIATION_EVENT));
    cues.dispose();
    expect([added, removed]).toEqual([1, 1]);
    // No window in Node: a default AudioCues listens to nothing.
    expect(() => new AudioCues({ profile: SHIP }).dispose()).not.toThrow();
  });

  it("keeps the five buses", () => {
    expect(Object.keys(CUE_BUS_GAIN)).toEqual(["keys", "shots", "hits", "kills", "alerts"]);
  });
});
