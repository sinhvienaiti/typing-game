import test from "node:test";
import assert from "node:assert/strict";

import {
  buildAdaptiveReviewSession,
  chooseAdaptiveReviewActivity,
} from "./adaptive-mix.mjs";

function item(overrides = {}) {
  return {
    entityType: "vocabulary",
    entityId: "airport",
    mastery: 55,
    reviewPriority: 80,
    attempts: 4,
    correct: 2,
    wrong: 2,
    hints: 0,
    replays: 0,
    avgResponseMs: 1800,
    correctStreak: 0,
    lastSeenAt: "2026-09-24T10:00:00.000Z",
    lastCorrectAt: "2026-09-24T09:00:00.000Z",
    lastWrongAt: "2026-09-24T10:00:00.000Z",
    nextReviewAt: "2026-09-24T10:00:00.000Z",
    sourceGames: ["monkeytype"],
    compatibleGames: [
      "monkeytype",
      "recall-typing",
      "vocab-shooter",
      "space-typing",
      "karaoke-typing",
    ],
    weaknessSignals: {
      spellingErrors: 0,
      listeningErrors: 0,
      contextErrors: 0,
      grammarErrors: 0,
      staleDays: 0,
    },
    ...overrides,
  };
}

test("Adaptive Mix maps explicit weakness types to transparent activities", () => {
  assert.equal(
    chooseAdaptiveReviewActivity(
      item({
        weaknessSignals: {
          spellingErrors: 2,
          listeningErrors: 0,
          contextErrors: 0,
          grammarErrors: 0,
          staleDays: 0,
        },
      }),
    ).game,
    "monkeytype",
  );

  assert.equal(
    chooseAdaptiveReviewActivity(
      item({
        weaknessSignals: {
          spellingErrors: 0,
          listeningErrors: 2,
          contextErrors: 0,
          grammarErrors: 0,
          staleDays: 0,
        },
      }),
    ).game,
    "recall-typing",
  );

  assert.equal(
    chooseAdaptiveReviewActivity(
      item({
        avgResponseMs: 5100,
      }),
    ).game,
    "vocab-shooter",
  );

  assert.equal(
    chooseAdaptiveReviewActivity(
      item({
        weaknessSignals: {
          spellingErrors: 0,
          listeningErrors: 0,
          contextErrors: 0,
          grammarErrors: 0,
          staleDays: 12,
        },
      }),
    ).game,
    "space-typing",
  );
});

test("Adaptive Mix keeps grammar and contextual listening on capable games", () => {
  const grammar = chooseAdaptiveReviewActivity(
    item({
      entityType: "grammar",
      entityId: "time.present",
      compatibleGames: ["monkeytype"],
      weaknessSignals: {
        spellingErrors: 0,
        listeningErrors: 0,
        contextErrors: 1,
        grammarErrors: 2,
        staleDays: 0,
      },
    }),
  );
  assert.equal(grammar.game, "monkeytype");
  assert.match(grammar.reason, /grammar/);

  const sentence = chooseAdaptiveReviewActivity(
    item({
      entityType: "sentence",
      entityId: "We fly tonight",
      compatibleGames: ["monkeytype", "karaoke-typing"],
      replays: 2,
      weaknessSignals: {
        spellingErrors: 0,
        listeningErrors: 1,
        contextErrors: 0,
        grammarErrors: 0,
        staleDays: 0,
      },
    }),
  );
  assert.equal(sentence.game, "karaoke-typing");
  assert.match(sentence.reason, /listening/);
});

test("Adaptive Mix session groups assignments into deterministic concrete segments", () => {
  const plan = {
    version: 1,
    createdAt: "2026-09-24T16:20:00.000Z",
    durationMinutes: 15,
    options: {
      reviewSet: "due",
      content: ["vocabulary", "grammar", "sentence"],
      amount: 20,
      sourceGame: "",
      goal: "mixed",
      game: "adaptive-mix",
      custom: {},
    },
    items: [
      item({
        entityId: "spell",
        weaknessSignals: {
          spellingErrors: 1,
          listeningErrors: 0,
          contextErrors: 0,
          grammarErrors: 0,
          staleDays: 0,
        },
      }),
      item({
        entityId: "slow",
        avgResponseMs: 5000,
      }),
      item({
        entityType: "grammar",
        entityId: "time.present",
        compatibleGames: ["monkeytype"],
      }),
    ],
    totalCandidates: 3,
    compatibleCount: 3,
    excludedCount: 0,
    selectedCount: 3,
  };

  const session = buildAdaptiveReviewSession(
    plan,
    "2026-09-24T16:21:00.000Z",
  );

  assert.deepEqual(
    session.assignments.map((assignment) => [
      assignment.entityId,
      assignment.game,
    ]),
    [
      ["spell", "monkeytype"],
      ["slow", "vocab-shooter"],
      ["time.present", "monkeytype"],
    ],
  );
  assert.deepEqual(
    session.segments.map((segment) => [
      segment.game,
      segment.items.map((entry) => entry.entityId),
    ]),
    [
      ["monkeytype", ["spell", "time.present"]],
      ["vocab-shooter", ["slow"]],
    ],
  );
});
