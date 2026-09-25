import test from "node:test";
import assert from "node:assert/strict";

import {
  applyLearningEvent,
  createEmptyLearningProfile,
} from "./core.mjs";
import {
  REVIEW_CAPABILITIES,
  buildQuickReviewPlan,
  buildReviewPlan,
  compatibleGamesForItem,
  parseReviewPlan,
  parseReviewPlanInput,
} from "./review-session.mjs";

const NOW = "2026-09-24T10:00:00.000Z";

function event(overrides = {}) {
  return {
    version: 1,
    entityType: "vocabulary",
    entityId: "alpha",
    gameId: "monkeytype",
    activityType: "recall",
    result: "wrong",
    occurredAt: "2026-09-24T09:00:00.000Z",
    responseMs: 4000,
    hintUsed: false,
    replayUsed: false,
    ...overrides,
  };
}

function profile() {
  let result = createEmptyLearningProfile();
  result = applyLearningEvent(result, event({ entityId: "alpha" }));
  result = applyLearningEvent(
    result,
    event({
      entityId: "beta",
      gameId: "space-typing",
      occurredAt: "2026-09-20T09:00:00.000Z",
      result: "wrong",
    }),
  );
  result = applyLearningEvent(
    result,
    event({
      entityType: "grammar",
      entityId: "present-perfect",
      activityType: "sentence-builder",
      occurredAt: "2026-09-24T08:00:00.000Z",
      errorType: "wrong-tense",
    }),
  );
  result = applyLearningEvent(
    result,
    event({
      entityType: "sentence",
      entityId: "sentence-001",
      activityType: "sentence-builder",
      occurredAt: "2026-09-23T08:00:00.000Z",
      errorType: "word-order",
    }),
  );
  return result;
}

test("review plan input rejects invalid content and amount", () => {
  assert.throws(
    () =>
      parseReviewPlanInput({
        content: [],
        amount: 20,
      }),
    /content/,
  );
  assert.throws(
    () =>
      parseReviewPlanInput({
        content: ["vocabulary"],
        amount: 999,
      }),
    /amount/,
  );
});

test("Due Now returns priority-sorted compatible items", () => {
  const plan = buildReviewPlan(
    profile(),
    {
      reviewSet: "due",
      content: ["vocabulary", "grammar", "sentence"],
      amount: "all",
      goal: "mixed",
      game: "monkeytype",
    },
    NOW,
  );

  assert.ok(plan.selectedCount >= 1);
  assert.equal(plan.excludedCount, 0);
  for (let index = 1; index < plan.items.length; index += 1) {
    assert.ok(
      plan.items[index - 1].reviewPriority >=
        plan.items[index].reviewPriority,
    );
  }
});

test("capability matching excludes unsupported grammar from Space Typing", () => {
  const plan = buildReviewPlan(
    profile(),
    {
      reviewSet: "30d",
      content: ["vocabulary", "grammar"],
      amount: "all",
      goal: "mixed",
      game: "space-typing",
    },
    NOW,
  );

  assert.ok(plan.compatibleCount >= 1);
  assert.ok(plan.excludedCount >= 1);
  assert.ok(plan.items.every((item) => item.entityType === "vocabulary"));
});

test("source filter and amount limit are deterministic", () => {
  const plan = buildReviewPlan(
    profile(),
    {
      reviewSet: "30d",
      content: ["vocabulary"],
      amount: 10,
      sourceGame: "space-typing",
      goal: "spelling",
      game: "space-typing",
    },
    NOW,
  );

  assert.equal(plan.selectedCount, 1);
  assert.equal(plan.items[0].entityId, "beta");
});

test("Quick Review uses a 15-minute Adaptive Mix plan", () => {
  const plan = buildQuickReviewPlan(profile(), NOW);
  assert.equal(plan.durationMinutes, 15);
  assert.equal(plan.options.reviewSet, "due");
  assert.equal(plan.options.game, "adaptive-mix");
  assert.equal(plan.options.goal, "mixed");
  assert.ok(
    plan.items.every(
      (item) =>
        typeof item.weaknessSignals.spellingErrors === "number" &&
        "staleDays" in item.weaknessSignals,
    ),
  );
});

test("compatibility helper keeps grammar on capable games only", () => {
  const games = compatibleGamesForItem(
    { entityType: "grammar" },
    "grammar",
  );
  assert.deepEqual(games, ["monkeytype"]);
});

test("Monkey goal compatibility narrows content before dataset launch", () => {
  const learningProfile = profile();

  const listening = buildReviewPlan(
    learningProfile,
    {
      reviewSet: "30d",
      content: ["vocabulary", "grammar", "sentence"],
      amount: "all",
      goal: "listening",
      game: "monkeytype",
    },
    NOW,
  );
  assert.ok(listening.items.length >= 1);
  assert.ok(
    listening.items.every((item) => item.entityType === "vocabulary"),
  );

  const grammar = buildReviewPlan(
    learningProfile,
    {
      reviewSet: "30d",
      content: ["vocabulary", "grammar", "sentence"],
      amount: "all",
      goal: "grammar",
      game: "monkeytype",
    },
    NOW,
  );
  assert.ok(grammar.items.length >= 1);
  assert.ok(grammar.items.every((item) => item.entityType === "grammar"));

  const sentences = buildReviewPlan(
    learningProfile,
    {
      reviewSet: "30d",
      content: ["vocabulary", "grammar", "sentence"],
      amount: "all",
      goal: "sentence-building",
      game: "monkeytype",
    },
    NOW,
  );
  assert.ok(sentences.items.length >= 1);
  assert.ok(
    sentences.items.every((item) => item.entityType === "sentence"),
  );
});


test("cross-game capability matrix exposes only concrete review executors", () => {
  assert.deepEqual(Object.keys(REVIEW_CAPABILITIES), [
    "monkeytype",
    "recall-typing",
    "vocab-shooter",
    "space-typing",
    "karaoke-typing",
  ]);

  const vocabularyGames = compatibleGamesForItem(
    { entityType: "vocabulary" },
    "mixed",
  );
  assert.ok(vocabularyGames.length >= 1);
  assert.equal(vocabularyGames.includes("mixed-review"), false);
  assert.equal(vocabularyGames.includes("adaptive-mix"), false);
});


test("persisted review plan validation rejects stale malformed session data", () => {
  const valid = buildQuickReviewPlan(profile(), NOW);
  assert.deepEqual(parseReviewPlan(structuredClone(valid)), valid);

  const missingOptions = structuredClone(valid);
  delete missingOptions.options;
  assert.throws(
    () => parseReviewPlan(missingOptions),
    /review plan input must be an object/,
  );

  const badItems = structuredClone(valid);
  badItems.items[0].compatibleGames = "monkeytype";
  assert.throws(
    () => parseReviewPlan(badItems),
    /compatibleGames is invalid/,
  );

  const noCompatibleGame = structuredClone(valid);
  noCompatibleGame.items[0].compatibleGames = [];
  assert.throws(
    () => parseReviewPlan(noCompatibleGame),
    /incompatible with the stored plan/,
  );

  const badCounts = structuredClone(valid);
  badCounts.selectedCount += 1;
  assert.throws(
    () => parseReviewPlan(badCounts),
    /counts are inconsistent/,
  );
});
