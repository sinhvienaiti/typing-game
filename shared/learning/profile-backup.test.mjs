import test from "node:test";
import assert from "node:assert/strict";

import {
  applyLearningEvent,
  createEmptyLearningProfile,
} from "./core.mjs";
import {
  createLearningProfileBackup,
  learningProfileCounts,
  parseLearningProfileBackup,
  resetAllLearningProfile,
  resetLearningProfileSelection,
} from "./profile-backup.mjs";

const NOW = "2026-09-24T17:00:00.000Z";

function profile() {
  let result = createEmptyLearningProfile("2026-09-24T12:00:00.000Z");
  result = applyLearningEvent(result, {
    version: 1,
    entityType: "vocabulary",
    entityId: "airport",
    gameId: "recall-typing",
    activityType: "recall",
    result: "wrong",
    occurredAt: "2026-09-24T13:00:00.000Z",
    responseMs: 3200,
    hintUsed: true,
    replayUsed: false,
    expectedAnswer: "airport",
    errorType: "spelling",
  });
  result = applyLearningEvent(result, {
    version: 1,
    entityType: "grammar",
    entityId: "time.present",
    gameId: "monkeytype",
    activityType: "sentence-builder",
    result: "wrong",
    occurredAt: "2026-09-24T14:00:00.000Z",
    hintUsed: false,
    replayUsed: false,
    expectedAnswer: "goes",
    errorType: "wrong-form",
  });
  result = applyLearningEvent(result, {
    version: 1,
    entityType: "sentence",
    entityId: "We fly tonight",
    gameId: "karaoke-typing",
    activityType: "karaoke-line",
    result: "correct",
    occurredAt: "2026-09-24T15:00:00.000Z",
    responseMs: 1800,
    hintUsed: false,
    replayUsed: false,
    userAnswer: "We fly tonight",
    expectedAnswer: "We fly tonight",
  });
  return result;
}

test("learning profile backup round-trips through JSON", () => {
  const original = profile();
  const backup = createLearningProfileBackup(original, NOW);
  assert.equal(backup.format, "typing-game-learning-profile");
  assert.equal(backup.version, 1);
  assert.equal(backup.exportedAt, NOW);

  const restored = parseLearningProfileBackup(JSON.stringify(backup));
  assert.deepEqual(restored, original);
  assert.deepEqual(learningProfileCounts(restored), {
    vocabulary: 1,
    grammar: 1,
    sentence: 1,
    total: 3,
  });
});

test("import accepts a validated raw v1 profile for recovery compatibility", () => {
  const original = profile();
  assert.deepEqual(
    parseLearningProfileBackup(JSON.stringify(original)),
    original,
  );
});

test("import rejects malformed records before IndexedDB replacement", () => {
  const malformed = structuredClone(profile());
  malformed.vocabulary.airport.attempts = -1;

  assert.throws(
    () =>
      parseLearningProfileBackup({
        format: "typing-game-learning-profile",
        version: 1,
        exportedAt: NOW,
        profile: malformed,
      }),
    /attempts is invalid/,
  );
});

test("import rejects partial v1 profiles instead of silently filling collections", () => {
  const partial = structuredClone(profile());
  delete partial.sentences;

  assert.throws(
    () => parseLearningProfileBackup(partial),
    /sentences is required/,
  );
});

test("import rejects non-canonical vocabulary keys", () => {
  const malformed = structuredClone(profile());
  malformed.vocabulary.Airport = {
    ...malformed.vocabulary.airport,
    wordKey: "Airport",
  };
  delete malformed.vocabulary.airport;

  assert.throws(
    () => parseLearningProfileBackup(malformed),
    /non-canonical entity key/,
  );
});

test("selected reset clears only requested collections", () => {
  const original = profile();
  const next = resetLearningProfileSelection(
    original,
    ["vocabulary", "sentence"],
    NOW,
  );

  assert.deepEqual(next.vocabulary, {});
  assert.deepEqual(next.sentences, {});
  assert.equal(Object.keys(next.grammar).length, 1);
  assert.equal(next.updatedAt, NOW);
  assert.equal(Object.keys(original.vocabulary).length, 1);
});

test("reset all returns a fresh empty profile", () => {
  const next = resetAllLearningProfile(NOW);
  assert.deepEqual(learningProfileCounts(next), {
    vocabulary: 0,
    grammar: 0,
    sentence: 0,
    total: 0,
  });
  assert.equal(next.updatedAt, NOW);
});


test("import rejects internally inconsistent learning counters", () => {
  const malformed = structuredClone(profile());
  malformed.vocabulary.airport.correct = 1;

  assert.throws(
    () => parseLearningProfileBackup(malformed),
    /correct \+ wrong must equal attempts/,
  );
});

test("import rejects out-of-range derived scores", () => {
  const malformed = structuredClone(profile());
  malformed.vocabulary.airport.mastery = 101;

  assert.throws(
    () => parseLearningProfileBackup(malformed),
    /mastery is invalid/,
  );
});

test("import rejects fractional counters and impossible error totals", () => {
  const fractional = structuredClone(profile());
  fractional.vocabulary.airport.attempts = 1.5;
  assert.throws(
    () => parseLearningProfileBackup(fractional),
    /attempts is invalid/,
  );

  const impossibleErrors = structuredClone(profile());
  impossibleErrors.grammar["time.present"].errorTypes["wrong-form"] = 2;
  assert.throws(
    () => parseLearningProfileBackup(impossibleErrors),
    /errorTypes is invalid/,
  );
});
