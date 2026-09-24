import test from "node:test";
import assert from "node:assert/strict";

import {
  applyLearningEvent,
  createEmptyLearningProfile,
} from "./core.mjs";
import { buildReviewPlan } from "./review-session.mjs";
import {
  KARAOKE_REVIEW_DATASET_TYPE,
  buildKaraokeReviewDataset,
} from "./karaoke-review-dataset.mjs";

const NOW = "2026-09-24T16:00:00.000Z";

function profile() {
  let result = createEmptyLearningProfile("2026-09-20T00:00:00.000Z");
  result = applyLearningEvent(result, {
    version: 1,
    entityType: "sentence",
    entityId: "We fly tonight",
    gameId: "karaoke-typing",
    activityType: "karaoke-line",
    result: "wrong",
    occurredAt: "2026-09-24T15:00:00.000Z",
    responseMs: 2200,
    hintUsed: false,
    replayUsed: false,
    userAnswer: "We fly tonigt",
    expectedAnswer: "We fly tonight",
    errorType: "spelling",
  });
  result = applyLearningEvent(result, {
    version: 1,
    entityType: "vocabulary",
    entityId: "airport",
    gameId: "karaoke-typing",
    activityType: "typing",
    result: "wrong",
    occurredAt: "2026-09-24T15:05:00.000Z",
    hintUsed: false,
    replayUsed: false,
    expectedAnswer: "Airport",
    errorType: "spelling",
  });
  return result;
}

test("Karaoke review dataset keeps reliable sentence and word text", () => {
  const learningProfile = profile();
  const plan = buildReviewPlan(
    learningProfile,
    {
      reviewSet: "30d",
      content: ["vocabulary", "sentence"],
      amount: "all",
      goal: "mixed",
      game: "karaoke-typing",
    },
    NOW,
  );

  const dataset = buildKaraokeReviewDataset(
    plan,
    learningProfile,
    "karaoke-review-1",
    NOW,
  );

  assert.equal(dataset.type, KARAOKE_REVIEW_DATASET_TYPE);
  assert.equal(dataset.goal, "mixed");

  const sentence = dataset.items.find(
    (item) => item.entityType === "sentence",
  );
  assert.equal(sentence?.text, "We fly tonight");

  const vocabulary = dataset.items.find(
    (item) => item.entityType === "vocabulary",
  );
  assert.equal(vocabulary?.text, "Airport");
});

test("Karaoke review dataset rejects unsupported entity plans", () => {
  assert.throws(
    () =>
      buildKaraokeReviewDataset(
        {
          version: 1,
          options: {
            game: "karaoke-typing",
            goal: "mixed",
          },
          items: [
            {
              entityType: "grammar",
              entityId: "time.present",
            },
          ],
        },
        profile(),
        "karaoke-review-2",
        NOW,
      ),
    /vocabulary or sentence/,
  );
});
