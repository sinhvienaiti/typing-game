import test from "node:test";
import assert from "node:assert/strict";

import {
  applyLearningEvent,
  createEmptyLearningProfile,
} from "./core.mjs";
import { buildReviewPlan } from "./review-session.mjs";
import {
  MONKEY_REVIEW_DATASET_TYPE,
  buildMonkeyReviewDataset,
} from "./monkey-review-dataset.mjs";

const NOW = "2026-09-24T14:00:00.000Z";

function event(overrides = {}) {
  return {
    version: 1,
    entityType: "vocabulary",
    entityId: "airport",
    gameId: "monkeytype",
    activityType: "recall",
    result: "wrong",
    occurredAt: "2026-09-24T13:00:00.000Z",
    responseMs: 1500,
    hintUsed: false,
    replayUsed: false,
    ...overrides,
  };
}

function profile() {
  let result = createEmptyLearningProfile("2026-09-20T00:00:00.000Z");
  result = applyLearningEvent(result, event());
  result = applyLearningEvent(
    result,
    event({
      entityType: "grammar",
      entityId: "time.present",
      activityType: "cloze",
      expectedAnswer: "today",
      userAnswer: "tomorrow",
      errorType: "wrong-tense",
    }),
  );
  result = applyLearningEvent(
    result,
    event({
      entityType: "sentence",
      entityId: "present-perfect-lived-here",
      activityType: "sentence-builder",
      result: "correct",
      expectedAnswer: "Since 2020, I have lived here.",
      userAnswer: "Since 2020, I have lived here.",
      errorType: undefined,
    }),
  );
  result = applyLearningEvent(
    result,
    event({
      entityType: "sentence",
      entityId: "present-perfect-lived-here",
      activityType: "sentence-builder",
      expectedAnswer: "I have lived here since 2020.",
      userAnswer: "I lived here since 2020.",
      errorType: "wrong-tense",
      occurredAt: "2026-09-24T13:30:00.000Z",
    }),
  );
  return result;
}

test("Monkey review dataset keeps parent order and bounded reconstruction context", () => {
  const learningProfile = profile();
  const plan = buildReviewPlan(
    learningProfile,
    {
      reviewSet: "30d",
      content: ["vocabulary", "grammar", "sentence"],
      amount: "all",
      goal: "mixed",
      game: "monkeytype",
    },
    NOW,
  );

  const dataset = buildMonkeyReviewDataset(
    plan,
    learningProfile,
    "monkey-review-1",
    NOW,
  );

  assert.equal(dataset.type, MONKEY_REVIEW_DATASET_TYPE);
  assert.equal(dataset.goal, "mixed");
  assert.deepEqual(
    dataset.items.map((item) => [item.entityType, item.entityId]),
    plan.items.map((item) => [item.entityType, item.entityId]),
  );

  const grammar = dataset.items.find(
    (item) => item.entityType === "grammar",
  );
  assert.deepEqual(grammar?.reviewContext, {
    activityType: "cloze",
    expectedAnswer: "today",
    userAnswer: "tomorrow",
    errorType: "wrong-tense",
  });

  const sentence = dataset.items.find(
    (item) => item.entityType === "sentence",
  );
  assert.deepEqual(sentence?.acceptedAnswers, [
    "I have lived here since 2020.",
    "Since 2020, I have lived here.",
  ]);
  assert.equal(sentence?.reviewContext?.errorType, "wrong-tense");
});

test("Monkey review dataset rejects plans for another game", () => {
  const learningProfile = profile();
  const plan = buildReviewPlan(
    learningProfile,
    {
      reviewSet: "30d",
      content: ["vocabulary"],
      amount: "all",
      goal: "spelling",
      game: "space-typing",
    },
    NOW,
  );

  assert.throws(
    () =>
      buildMonkeyReviewDataset(
        plan,
        learningProfile,
        "monkey-review-2",
        NOW,
      ),
    /must target monkeytype/,
  );
});
