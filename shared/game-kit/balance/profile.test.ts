// Source: new for the kit: skill profile against docs/games/BALANCE.md §2
import { describe, expect, it } from "vitest";
import { SKILL_FULL, blendSkill, newSkillProfile, parseSkill, serializeSkill, skillDefaults, skillStorageKey, updateSkill, type SkillProfile, type SkillSample } from "./profile";

const stage = (overrides: Partial<SkillSample> = {}): SkillSample => ({
  outcome: "won",
  words: 60,
  wpm: 40,
  keys: 400,
  correctKeys: 380,
  backspaces: 20,
  cleanWords: 48,
  sloppyWords: 3,
  abandons: 2,
  cv: 0.3,
  byFamiliarity: { known: { words: 40, wpm: 44, recognize: 0.5 }, new: { words: 10, wpm: 30, recognize: 1.4 } },
  crowded: { words: 12, wpm: 30 },
  tactics: 0.6,
  telegraph: { handled: 6, total: 8 },
  safety: 0.6,
  idle: 0.05,
  nearMisses: 1,
  ...overrides,
});

const run = (profile: SkillProfile, samples: readonly SkillSample[]): SkillProfile => samples.reduce((current, sample) => updateSkill(current, sample).profile, profile);

describe("skill profile", () => {
  it("starts from the mode's and audience's defaults with no confidence", () => {
    const adult = blendSkill(newSkillProfile("adult", "balanced"));
    expect([adult.e, adult.a, adult.cv]).toEqual([35, 0.95, 0.25]);
    expect(adult.recognize).toEqual({ new: 1.2, learning: 0.7, known: 0.45 });
    expect(adult.speedBy.new).toBeCloseTo(24.5, 10);
    expect(adult.confidence.e).toBe(0);
    expect(skillDefaults("adult", "challenge").e).toBe(45);
    expect(skillDefaults("adult", "learn").e).toBe(25);
    const child = blendSkill(newSkillProfile("child", "relax"));
    expect([child.e, child.a, child.cv]).toEqual([15, 0.88, 0.4]);
    expect(skillStorageKey("dragon-hold")).toBe("dragon-hold.skill");
  });

  it("takes the first stage as is, then moves 0.25 toward each new stage", () => {
    const one = updateSkill(newSkillProfile(), stage());
    expect(one.accepted).toBe(true);
    const m = one.profile.measures;
    expect(m.e).toEqual({ value: 40, n: 60 });
    expect(m.a).toEqual({ value: 0.95, n: 400 });
    expect(m.backspace.value).toBeCloseTo(0.05, 10);
    expect(m.abandon.value).toBeCloseTo(2 / 62, 10);
    expect(m.recognize.known).toEqual({ value: 0.5, n: 40 });
    expect(m.recognize.learning).toEqual({ value: 0.7, n: 0 });
    expect(m.crowdDrop.value).toBeCloseTo(0.25, 10);
    expect(m.telegraph).toEqual({ value: 0.75, n: 8 });
    const two = updateSkill(one.profile, stage({ wpm: 20 })).profile;
    expect(two.measures.e).toEqual({ value: 35, n: 120 });
    const three = updateSkill(two, stage({ wpm: 60 })).profile;
    expect(three.measures.e.value).toBeCloseTo(41.25, 10);
  });

  it("blends defaults into measurements by confidence", () => {
    const half = updateSkill(newSkillProfile(), stage({ words: 30, wpm: 55 })).profile;
    const view = blendSkill(half);
    expect(view.confidence.e).toBeCloseTo(30 / SKILL_FULL.e, 10);
    expect(view.e).toBeCloseTo(35 + 0.5 * (55 - 35), 10);
    const full = run(newSkillProfile(), [stage({ wpm: 55 }), stage({ wpm: 55 })]);
    expect(blendSkill(full).e).toBe(55);
    expect(blendSkill(full).confidence.e).toBe(1);
    expect(blendSkill(full).confidence.recognize.learning).toBe(0);
  });

  it("leaves quit, AFK, short and wildly-off runs out of the skill, but counts them in the trend", () => {
    const base = run(newSkillProfile(), [stage(), stage()]);
    const quit = updateSkill(base, stage({ outcome: "quit", wpm: 10 }));
    expect([quit.accepted, quit.reason]).toEqual([false, "quit"]);
    expect(quit.profile.measures).toBe(base.measures);
    expect(quit.profile.trend.quits).toBe(1);
    const afk = updateSkill(base, stage({ afk: true }));
    expect([afk.accepted, afk.reason, afk.profile]).toEqual([false, "afk", base]);
    const short = updateSkill(base, stage({ outcome: "lost", words: 5 }));
    expect([short.reason, short.profile.measures === base.measures, short.profile.trend.streak]).toEqual(["short", true, -1]);
    expect(updateSkill(base, stage({ wpm: 12 })).reason).toBe("outlier");
    expect(updateSkill(base, stage({ wpm: 120 })).reason).toBe("outlier");
    expect(updateSkill(base, stage({ wpm: 30 })).accepted).toBe(true);
    // Before E is established nothing is an outlier.
    expect(updateSkill(newSkillProfile(), stage({ wpm: 120 })).accepted).toBe(true);
  });

  it("tracks streaks, easy wins and quits for the suggestion", () => {
    let profile = newSkillProfile();
    profile = run(profile, [stage({ safety: 0.95, idle: 0.25 }), stage({ safety: 0.92, idle: 0.3 })]);
    expect([profile.trend.streak, profile.trend.easyWins]).toEqual([2, 2]);
    profile = run(profile, [stage({ outcome: "lost", safety: 0 }), stage({ outcome: "lost", safety: 0 })]);
    expect([profile.trend.streak, profile.trend.easyWins, profile.trend.stages]).toEqual([-2, 0, 4]);
    profile = run(profile, [stage({ outcome: "quit" })]);
    expect([profile.trend.streak, profile.trend.quits]).toEqual([-2, 1]);
    profile = run(profile, [stage()]);
    expect([profile.trend.streak, profile.trend.quits]).toEqual([1, 0]);
    expect(profile.trend.safety.n).toBe(5);
  });

  it("measures in-session fatigue against the session's first stage", () => {
    let profile = run(newSkillProfile(), [stage({ wpm: 40, session: { first: true } })]);
    expect(profile.sessionWpm).toBe(40);
    profile = run(profile, [stage({ wpm: 36, session: { first: false } })]);
    expect(profile.measures.fatigue.value).toBeCloseTo(0.1, 10);
    profile = run(profile, [stage({ wpm: 40, session: { first: false } })]);
    expect(profile.measures.fatigue.value).toBeCloseTo(0.05, 10);
    profile = run(profile, [stage({ wpm: 30, session: { first: true } })]);
    expect([profile.sessionWpm, profile.measures.fatigue.value, profile.measures.fatigue.n]).toEqual([30, 0, 0]);
  });

  it("serialises and parses back the same profile; the settings' audience and mode win", () => {
    const profile = run(newSkillProfile(), [stage({ vocab: { mastery: 0.7, level: 3 }, ime: true, weakKeys: ["ă", "q"] }), stage({ wpm: 44 })]);
    const text = serializeSkill(profile);
    expect(parseSkill(text)).toEqual(profile);
    const relaxed = parseSkill(text, "adult", "relax");
    expect([relaxed.mode, relaxed.measures]).toEqual(["relax", profile.measures]);
    expect([profile.vocabLevel, profile.measures.vocab.value, profile.input.ime, profile.input.weakKeys]).toEqual([3, 0.7, true, ["ă", "q"]]);
  });

  it("falls back safely: garbage, unknown versions, and broken fields", () => {
    const fresh = newSkillProfile("child", "relax");
    for (const text of [null, undefined, "", "{", "[]", "42", JSON.stringify({ version: 2, measures: {} }), JSON.stringify({ measures: {} })]) {
      expect(parseSkill(text, "child", "relax")).toEqual(fresh);
    }
    const good = run(newSkillProfile(), [stage(), stage()]);
    const raw = JSON.parse(serializeSkill(good));
    raw.measures.e = { value: 9999, n: 60 };
    raw.measures.a = { value: 0.9, n: -1 };
    raw.measures.recognize.new = "slow";
    raw.trend.streak = 1.5;
    raw.input.weakKeys = ["x", 7, "toolongkey"];
    const parsed = parseSkill(JSON.stringify(raw));
    expect(parsed.measures.e).toEqual({ value: 35, n: 0 });
    expect(parsed.measures.a).toEqual({ value: 0.95, n: 0 });
    expect(parsed.measures.recognize.new).toEqual({ value: 1.2, n: 0 });
    expect(parsed.measures.cv).toEqual(good.measures.cv);
    expect(parsed.trend.streak).toBe(0);
    expect(parsed.input.weakKeys).toEqual(["x"]);
  });
});
