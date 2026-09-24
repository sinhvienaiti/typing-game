import test from "node:test";
import assert from "node:assert/strict";

import {
  applyLearningEvent,
  createEmptyLearningProfile,
} from "./core.mjs";
import {
  buildQuickReviewPlan,
  buildReviewPlan,
  compatibleGamesForItem,
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
      result: "correct",
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

test("Quick Review uses a 15-minute mixed-review plan", () => {
  const plan = buildQuickReviewPlan(profile(), NOW);
  assert.equal(plan.durationMinutes, 15);
  assert.equal(plan.options.reviewSet, "due");
  assert.equal(plan.options.game, "mixed-review");
  assert.equal(plan.options.goal, "mixed");
});

test("compatibility helper keeps grammar on capable games only", () => {
  const games = compatibleGamesForItem(
    { entityType: "grammar" },
    "grammar",
  );
  assert.deepEqual(games, ["monkeytype"]);
});
