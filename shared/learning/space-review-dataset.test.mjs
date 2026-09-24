import test from "node:test";
import assert from "node:assert/strict";

import {
  applyLearningEvent,
  createEmptyLearningProfile,
} from "./core.mjs";
import { buildReviewPlan } from "./review-session.mjs";
import {
  SPACE_REVIEW_DATASET_TYPE,
  buildSpaceReviewDataset,
} from "./space-review-dataset.mjs";

const NOW = "2026-09-24T15:50:00.000Z";

function profile() {
  let result = createEmptyLearningProfile("2026-09-20T00:00:00.000Z");
  for (const [entityId, minute] of [["airport", "10"], ["passport", "20"]]) {
    result = applyLearningEvent(result, {
      version: 1,
      entityType: "vocabulary",
      entityId,
      gameId: "space-typing",
      activityType: "typing",
      result: "wrong",
      occurredAt: `2026-09-24T14:${minute}:00.000Z`,
      hintUsed: false,
      replayUsed: false,
      expectedAnswer: entityId,
      errorType: "spelling",
    });
  }
  return result;
}

test("Space review dataset preserves selected vocabulary metadata", () => {
  const plan = buildReviewPlan(
    profile(),
    {
      reviewSet: "30d",
      content: ["vocabulary"],
      amount: "all",
      goal: "mixed",
      game: "space-typing",
    },
    NOW,
  );

  const dataset = buildSpaceReviewDataset(
    plan,
    "space-review-1",
    NOW,
  );

  assert.equal(dataset.type, SPACE_REVIEW_DATASET_TYPE);
  assert.equal(dataset.goal, "mixed");
  assert.deepEqual(
    dataset.items.map((item) => item.entityId),
    plan.items.map((item) => item.entityId),
  );
  assert.equal(typeof dataset.items[0]?.mastery, "number");
  assert.equal(typeof dataset.items[0]?.reviewPriority, "number");
});

test("Space review dataset rejects incompatible game plans", () => {
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

  assert.throws(
    () => buildSpaceReviewDataset(plan, "space-review-2", NOW),
    /must target space-typing/,
  );
});
