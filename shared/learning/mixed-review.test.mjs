import test from "node:test";
import assert from "node:assert/strict";

import {
  buildMixedReviewSession,
  createMixedReviewProgress,
  recordMixedReviewEvent,
  reviewPlanForMixedSegment,
} from "./mixed-review.mjs";

const plan = {
  version: 1,
  createdAt: "2026-09-24T16:00:00.000Z",
  durationMinutes: 15,
  options: {
    reviewSet: "due",
    content: ["vocabulary", "grammar", "sentence"],
    amount: 20,
    sourceGame: "",
    goal: "mixed",
    game: "mixed-review",
    custom: {},
  },
  items: [
    {
      entityType: "vocabulary",
      entityId: "airport",
      compatibleGames: [
        "monkeytype",
        "recall-typing",
        "vocab-shooter",
        "space-typing",
        "karaoke-typing",
      ],
    },
    {
      entityType: "vocabulary",
      entityId: "passport",
      compatibleGames: [
        "monkeytype",
        "recall-typing",
        "vocab-shooter",
        "space-typing",
        "karaoke-typing",
      ],
    },
    {
      entityType: "grammar",
      entityId: "time.present",
      compatibleGames: ["monkeytype"],
    },
    {
      entityType: "sentence",
      entityId: "We fly tonight",
      compatibleGames: ["monkeytype", "karaoke-typing"],
    },
  ].map((item, index) => ({
    mastery: 20 + index,
    reviewPriority: 90 - index,
    attempts: 3,
    correct: 1,
    wrong: 2,
    hints: 0,
    replays: 0,
    avgResponseMs: null,
    correctStreak: 0,
    lastSeenAt: "2026-09-24T15:00:00.000Z",
    lastCorrectAt: null,
    lastWrongAt: "2026-09-24T15:00:00.000Z",
    nextReviewAt: "2026-09-24T15:00:00.000Z",
    sourceGames: ["monkeytype"],
    ...item,
  })),
  totalCandidates: 4,
  compatibleCount: 4,
  excludedCount: 0,
  selectedCount: 4,
};

test("Mixed Review balances items deterministically across compatible games", () => {
  const session = buildMixedReviewSession(
    plan,
    "2026-09-24T16:05:00.000Z",
  );

  assert.equal(session.totalItems, 4);
  assert.deepEqual(
    session.segments.map((segment) => [
      segment.game,
      segment.items.map((item) => item.entityId),
    ]),
    [
      ["recall-typing", ["airport"]],
      ["vocab-shooter", ["passport"]],
      ["karaoke-typing", ["We fly tonight"]],
      ["monkeytype", ["time.present"]],
    ],
  );
});

test("Mixed Review segment plan keeps parent metadata but targets one concrete game", () => {
  const session = buildMixedReviewSession(plan);
  const segmentPlan = reviewPlanForMixedSegment(plan, session.segments[0]);

  assert.equal(segmentPlan.options.game, "recall-typing");
  assert.equal(segmentPlan.selectedCount, 1);
  assert.equal(segmentPlan.items[0].entityId, "airport");
});

test("Mixed Review progress advances only on persisted events from the active game/item", () => {
  const session = buildMixedReviewSession(plan);
  let progress = createMixedReviewProgress(session);

  const ignored = recordMixedReviewEvent(session, progress, {
    version: 1,
    entityType: "vocabulary",
    entityId: "airport",
    gameId: "space-typing",
    activityType: "typing",
    result: "correct",
    occurredAt: "2026-09-24T16:10:00.000Z",
    hintUsed: false,
    replayUsed: false,
  });
  assert.equal(ignored.matched, false);
  assert.equal(ignored.progress.activeSegmentIndex, 0);

  const first = recordMixedReviewEvent(session, progress, {
    version: 1,
    entityType: "vocabulary",
    entityId: "AIRPORT",
    gameId: "recall-typing",
    activityType: "recall",
    result: "correct",
    occurredAt: "2026-09-24T16:11:00.000Z",
    hintUsed: false,
    replayUsed: false,
  });
  assert.equal(first.matched, true);
  assert.equal(first.segmentCompleted, true);
  assert.equal(first.progress.activeSegmentIndex, 1);
  progress = first.progress;

  for (let index = 1; index < session.segments.length; index++) {
    const segment = session.segments[index];
    const item = segment.items[0];
    const result = recordMixedReviewEvent(session, progress, {
      version: 1,
      entityType: item.entityType,
      entityId: item.entityId,
      gameId: segment.game,
      activityType: "typing",
      result: "correct",
      occurredAt: "2026-09-24T16:12:00.000Z",
      hintUsed: false,
      replayUsed: false,
    });
    progress = result.progress;
  }

  assert.equal(progress.activeSegmentIndex, session.segments.length);
  assert.equal(progress.completedAt, "2026-09-24T16:12:00.000Z");
});
