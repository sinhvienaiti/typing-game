import test from "node:test";
import assert from "node:assert/strict";

import {
  applyLearningEvent,
  createEmptyLearningProfile,
} from "./core.mjs";
import { buildReviewPlan } from "./review-session.mjs";
import {
  RECALL_REVIEW_DATASET_TYPE,
  buildRecallReviewDataset,
} from "./recall-review-dataset.mjs";

const NOW = "2026-09-24T15:00:00.000Z";

function profile() {
  let result = createEmptyLearningProfile("2026-09-20T00:00:00.000Z");
  for (const [entityId, prioritySeed] of [
    ["airport", 1],
    ["passport", 2],
  ]) {
    result = applyLearningEvent(result, {
      version: 1,
      entityType: "vocabulary",
      entityId,
      gameId: "recall-typing",
      activityType: "recall",
      result: "wrong",
      occurredAt: `2026-09-24T1${prioritySeed}:00:00.000Z`,
      responseMs: 900 + prioritySeed,
      hintUsed: false,
      replayUsed: false,
      expectedAnswer: entityId,
      errorType: "spelling",
    });
  }
  return result;
}

test("Recall review dataset preserves parent queue order and metadata", () => {
  const learningProfile = profile();
  const plan = buildReviewPlan(
    learningProfile,
    {
      reviewSet: "30d",
      content: ["vocabulary"],
      amount: "all",
      goal: "listening",
      game: "recall-typing",
    },
    NOW,
  );

  const dataset = buildRecallReviewDataset(
    plan,
    "recall-review-1",
    NOW,
  );

  assert.equal(dataset.type, RECALL_REVIEW_DATASET_TYPE);
  assert.equal(dataset.goal, "listening");
  assert.deepEqual(
    dataset.items.map((item) => item.entityId),
    plan.items.map((item) => item.entityId),
  );
  assert.equal(typeof dataset.items[0]?.mastery, "number");
  assert.equal(typeof dataset.items[0]?.reviewPriority, "number");
});

test("Recall review dataset rejects another game", () => {
  const learningProfile = profile();
  const plan = buildReviewPlan(
    learningProfile,
    {
      reviewSet: "30d",
      content: ["vocabulary"],
      amount: "all",
      goal: "spelling",
      game: "monkeytype",
    },
    NOW,
  );

  assert.throws(
    () => buildRecallReviewDataset(plan, "recall-review-2", NOW),
    /must target recall-typing/,
  );
});

test("Recall review dataset rejects non-vocabulary queue content", () => {
  assert.throws(
    () =>
      buildRecallReviewDataset(
        {
          version: 1,
          options: {
            game: "recall-typing",
            goal: "mixed",
          },
          items: [
            {
              entityType: "grammar",
              entityId: "time.present",
            },
          ],
        },
        "recall-review-3",
        NOW,
      ),
    /vocabulary items only/,
  );
});
