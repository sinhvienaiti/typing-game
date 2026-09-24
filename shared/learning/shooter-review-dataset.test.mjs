import test from "node:test";
import assert from "node:assert/strict";

import {
  applyLearningEvent,
  createEmptyLearningProfile,
} from "./core.mjs";
import { buildReviewPlan } from "./review-session.mjs";
import {
  SHOOTER_REVIEW_DATASET_TYPE,
  buildShooterReviewDataset,
} from "./shooter-review-dataset.mjs";

const NOW = "2026-09-24T15:20:00.000Z";

function profile() {
  let result = createEmptyLearningProfile("2026-09-20T00:00:00.000Z");
  for (const [entityId, minute] of [["airport", "10"], ["passport", "20"]]) {
    result = applyLearningEvent(result, {
      version: 1,
      entityType: "vocabulary",
      entityId,
      gameId: "vocab-shooter",
      activityType: "typing",
      result: "wrong",
      occurredAt: `2026-09-24T14:${minute}:00.000Z`,
      responseMs: 1200,
      hintUsed: false,
      replayUsed: false,
      expectedAnswer: entityId,
      errorType: "spelling",
    });
  }
  return result;
}

test("Shooter review dataset preserves the parent-selected vocabulary set", () => {
  const plan = buildReviewPlan(
    profile(),
    {
      reviewSet: "30d",
      content: ["vocabulary"],
      amount: "all",
      goal: "spelling",
      game: "vocab-shooter",
    },
    NOW,
  );

  const dataset = buildShooterReviewDataset(
    plan,
    "shooter-review-1",
    NOW,
  );

  assert.equal(dataset.type, SHOOTER_REVIEW_DATASET_TYPE);
  assert.equal(dataset.goal, "spelling");
  assert.deepEqual(
    dataset.items.map((item) => item.entityId),
    plan.items.map((item) => item.entityId),
  );
  assert.equal(typeof dataset.items[0]?.mastery, "number");
  assert.equal(typeof dataset.items[0]?.reviewPriority, "number");
});

test("Shooter review dataset rejects incompatible game plans", () => {
  const plan = buildReviewPlan(
    profile(),
    {
      reviewSet: "30d",
      content: ["vocabulary"],
      amount: "all",
      goal: "spelling",
      game: "recall-typing",
    },
    NOW,
  );

  assert.throws(
    () => buildShooterReviewDataset(plan, "shooter-review-2", NOW),
    /must target vocab-shooter/,
  );
});
