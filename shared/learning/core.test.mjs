import test from "node:test";
import assert from "node:assert/strict";
import {
  MAX_RECENT_SAMPLES,
  applyLearningEvent,
  applyLearningEvents,
  calculateMastery,
  calculateReviewPriority,
  createEmptyLearningProfile,
  normalizeVocabularyKey,
  parseLearningEvent,
} from "./core.mjs";

const baseTime = "2026-09-24T10:00:00.000Z";

function event(overrides = {}) {
  return {
    version: 1,
    entityType: "vocabulary",
    entityId: " Environment ",
    gameId: "monkeytype",
    activityType: "recall",
    result: "correct",
    occurredAt: baseTime,
    responseMs: 1800,
    hintUsed: false,
    replayUsed: false,
    ...overrides,
  };
}

test("vocabulary normalization matches the shared library contract", () => {
  assert.equal(normalizeVocabularyKey("  ＣＡＣＨＥ   Control "), "cache control");
});

test("event parser validates and canonicalizes learning events", () => {
  const parsed = parseLearningEvent(event());
  assert.equal(parsed.entityId, "environment");
  assert.equal(parsed.occurredAt, baseTime);
  assert.throws(() => parseLearningEvent({ ...event(), version: 2 }), /version/);
  assert.throws(() => parseLearningEvent({ ...event(), responseMs: -1 }), /responseMs/);
});

test("vocabulary aggregates are deterministic and keep source games unique", () => {
  let profile = createEmptyLearningProfile();
  profile = applyLearningEvent(profile, event());
  profile = applyLearningEvent(profile, event({
    result: "wrong",
    occurredAt: "2026-09-24T10:05:00.000Z",
    responseMs: 4200,
    hintUsed: true,
    userAnswer: "enviroment",
    expectedAnswer: "environment",
    errorType: "spelling",
  }));
  profile = applyLearningEvent(profile, event({
    occurredAt: "2026-09-24T10:10:00.000Z",
    gameId: "recall-typing",
    responseMs: 2000,
  }));

  const record = profile.vocabulary.environment;
  assert.equal(record.attempts, 3);
  assert.equal(record.correct, 2);
  assert.equal(record.wrong, 1);
  assert.equal(record.hints, 1);
  assert.deepEqual(record.sourceGames, ["monkeytype", "recall-typing"]);
  assert.equal(record.recentMistakes[0].userAnswer, "enviroment");
  assert.equal(record.avgResponseMs, 2667);
  assert.equal(record.correctStreak, 1);
  assert.equal(record.mastery, calculateMastery(record, record.lastSeenAt));
  assert.equal(record.reviewPriority, calculateReviewPriority(record, record.lastSeenAt));
});

test("recent mistakes are bounded", () => {
  let profile = createEmptyLearningProfile();
  for (let index = 0; index < MAX_RECENT_SAMPLES + 4; index += 1) {
    profile = applyLearningEvent(profile, event({
      result: "wrong",
      occurredAt: new Date(Date.parse(baseTime) + index * 60_000).toISOString(),
      userAnswer: `wrong-${index}`,
    }));
  }
  const mistakes = profile.vocabulary.environment.recentMistakes;
  assert.equal(mistakes.length, MAX_RECENT_SAMPLES);
  assert.equal(mistakes[0].userAnswer, "wrong-4");
});

test("grammar keeps error classifications separate from vocabulary spelling", () => {
  let profile = createEmptyLearningProfile();
  profile = applyLearningEvent(profile, event({
    entityType: "grammar",
    entityId: "present-perfect",
    result: "wrong",
    errorType: "wrong-tense",
    userAnswer: "I lived here since 2020.",
    expectedAnswer: "I have lived here since 2020.",
  }));
  const record = profile.grammar["present-perfect"];
  assert.equal(record.errorTypes["wrong-tense"], 1);
  assert.equal(profile.vocabulary.environment, undefined);
});

test("sentence answers are bounded and keep accepted-result history", () => {
  let profile = createEmptyLearningProfile();
  for (let index = 0; index < MAX_RECENT_SAMPLES + 2; index += 1) {
    profile = applyLearningEvent(profile, event({
      entityType: "sentence",
      entityId: "sentence-001",
      occurredAt: new Date(Date.parse(baseTime) + index * 60_000).toISOString(),
      userAnswer: `answer ${index}`,
      result: index % 2 === 0 ? "correct" : "wrong",
      ...(index % 2 === 0 ? {} : { errorType: "word-order" }),
    }));
  }
  const record = profile.sentences["sentence-001"];
  assert.equal(record.recentAnswers.length, MAX_RECENT_SAMPLES);
  assert.equal(record.recentAnswers[0].answer, "answer 2");
  assert.equal(record.errorTypes["word-order"], 5);
});

test("weak and stale records receive higher review priority", () => {
  const strong = {
    attempts: 10, correct: 10, wrong: 0, hints: 0, replays: 0,
    avgResponseMs: 1200, correctStreak: 5,
    lastCorrectAt: "2026-09-24T09:00:00.000Z", lastSeenAt: baseTime,
  };
  const weak = {
    attempts: 10, correct: 4, wrong: 6, hints: 3, replays: 2,
    avgResponseMs: 6500, correctStreak: 0,
    lastCorrectAt: "2026-08-01T09:00:00.000Z", lastSeenAt: baseTime,
  };
  assert.ok(calculateReviewPriority(weak, baseTime) > calculateReviewPriority(strong, baseTime));
  assert.ok(calculateMastery(strong, baseTime) > calculateMastery(weak, baseTime));
});


test("batched events are applied in event-time order without rolling current state backward", () => {
  const profile = applyLearningEvents(createEmptyLearningProfile(), [
    event({
      occurredAt: "2026-09-24T10:10:00.000Z",
      result: "correct",
    }),
    event({
      occurredAt: "2026-09-24T10:05:00.000Z",
      result: "wrong",
      userAnswer: "enviroment",
      errorType: "spelling",
    }),
    event({
      occurredAt: "2026-09-24T10:15:00.000Z",
      result: "correct",
    }),
  ]);

  const record = profile.vocabulary.environment;
  assert.equal(record.attempts, 3);
  assert.equal(record.correctStreak, 2);
  assert.equal(record.lastSeenAt, "2026-09-24T10:15:00.000Z");
  assert.equal(record.lastWrongAt, "2026-09-24T10:05:00.000Z");
  assert.equal(profile.updatedAt, "2026-09-24T10:15:00.000Z");

  const withLateEvent = applyLearningEvent(profile, event({
    occurredAt: "2026-09-24T10:01:00.000Z",
    result: "wrong",
    userAnswer: "late-old-error",
    errorType: "spelling",
  }));
  const lateRecord = withLateEvent.vocabulary.environment;

  assert.equal(lateRecord.attempts, 4);
  assert.equal(lateRecord.correctStreak, 2);
  assert.equal(lateRecord.lastSeenAt, "2026-09-24T10:15:00.000Z");
  assert.equal(lateRecord.lastWrongAt, "2026-09-24T10:05:00.000Z");
  assert.equal(withLateEvent.updatedAt, "2026-09-24T10:15:00.000Z");
  assert.deepEqual(
    lateRecord.recentMistakes.map((sample) => sample.userAnswer),
    ["late-old-error", "enviroment"],
  );
});

test("batched learning updates keep the input profile immutable", () => {
  const input = applyLearningEvent(createEmptyLearningProfile(), event());
  const snapshot = structuredClone(input);

  const output = applyLearningEvents(input, [
    event({
      occurredAt: "2026-09-24T10:01:00.000Z",
      gameId: "recall-typing",
    }),
    event({
      occurredAt: "2026-09-24T10:02:00.000Z",
      result: "wrong",
      userAnswer: "enviroment",
      errorType: "spelling",
    }),
  ]);

  assert.deepEqual(input, snapshot);
  assert.notEqual(output, input);
  assert.equal(output.vocabulary.environment.attempts, 3);
});
