import test from "node:test";
import assert from "node:assert/strict";

import {
  applyLearningEvent,
  applyLearningEvents,
  createEmptyLearningProfile,
} from "./core.mjs";
import {
  LEARNING_ATTEMPT_MESSAGE,
  LEARNING_QUERY_MESSAGE,
  isLearningMessage,
  parseLearningMessage,
} from "./message-contract.mjs";
import { parseLearningQuery, queryLearningProfile } from "./query.mjs";

function attempt(entityId, result, occurredAt, extra = {}) {
  return {
    version: 1,
    entityType: "vocabulary",
    entityId,
    gameId: extra.gameId ?? "monkeytype",
    activityType: "recall",
    result,
    occurredAt,
    responseMs: extra.responseMs ?? 2000,
    hintUsed: extra.hintUsed ?? false,
    replayUsed: false,
  };
}

test("learning message contract accepts only supported versioned messages", () => {
  const payload = {
    type: LEARNING_ATTEMPT_MESSAGE,
    requestId: "req-1",
    event: attempt("Cache", "correct", "2026-09-24T10:00:00.000Z"),
  };

  assert.equal(isLearningMessage(payload), true);
  assert.equal(parseLearningMessage(payload).event.entityId, "cache");
  assert.throws(
    () =>
      parseLearningMessage({
        ...payload,
        requestId: "bad id with spaces",
      }),
    /requestId/,
  );
  assert.throws(
    () =>
      parseLearningMessage({
        ...payload,
        type: "typing-game:learning:v1:unknown",
      }),
    /not supported/,
  );
});

test("learning query message validates the nested query", () => {
  const parsed = parseLearningMessage({
    type: LEARNING_QUERY_MESSAGE,
    requestId: "query-1",
    query: {
      entityType: "vocabulary",
      page: 2,
      pageSize: 50,
      filters: { dueOnly: true },
    },
  });
  assert.equal(parsed.query.page, 2);
  assert.equal(parsed.query.pageSize, 50);
  assert.equal(parsed.query.filters.dueOnly, true);
});

test("query parser enforces bounded pagination, filters and sort values", () => {
  assert.equal(
    parseLearningQuery({ entityType: "vocabulary" }).pageSize,
    25,
  );
  assert.throws(
    () => parseLearningQuery({ entityType: "vocabulary", pageSize: 500 }),
    /pageSize/,
  );
  assert.throws(
    () => parseLearningQuery({ entityType: "vocabulary", sort: "random" }),
    /sort/,
  );
  assert.throws(
    () =>
      parseLearningQuery({
        entityType: "vocabulary",
        filters: { dueOnly: "yes" },
      }),
    /dueOnly/,
  );
  assert.throws(
    () =>
      parseLearningQuery({
        entityType: "vocabulary",
        filters: { masteryMin: 80, masteryMax: 20 },
      }),
    /masteryMin/,
  );
  assert.throws(
    () =>
      parseLearningQuery({
        entityType: "vocabulary",
        filters: {
          lastWrongFrom: "2026-09-24T10:00:00.000Z",
          lastWrongTo: "2026-09-23T10:00:00.000Z",
        },
      }),
    /lastWrongFrom/,
  );
});

test("batched learning events preserve every event in order", () => {
  const events = [
    attempt("alpha", "correct", "2026-09-24T09:00:00.000Z"),
    attempt("alpha", "wrong", "2026-09-24T09:05:00.000Z"),
    attempt("alpha", "correct", "2026-09-24T09:10:00.000Z"),
  ];
  const profile = applyLearningEvents(createEmptyLearningProfile(), events);
  assert.equal(profile.vocabulary.alpha.attempts, 3);
  assert.equal(profile.vocabulary.alpha.correct, 2);
  assert.equal(profile.vocabulary.alpha.wrong, 1);
  assert.equal(profile.vocabulary.alpha.lastSeenAt, events[2].occurredAt);
});

test("profile query filters, sorts and paginates bounded results", () => {
  let profile = createEmptyLearningProfile();
  profile = applyLearningEvent(
    profile,
    attempt("alpha", "correct", "2026-09-24T09:00:00.000Z", {
      responseMs: 1000,
    }),
  );
  profile = applyLearningEvent(
    profile,
    attempt("beta", "wrong", "2026-09-24T09:10:00.000Z", {
      responseMs: 6000,
      hintUsed: true,
      gameId: "space-typing",
    }),
  );
  profile = applyLearningEvent(
    profile,
    attempt("gamma", "wrong", "2026-09-24T09:20:00.000Z", {
      responseMs: 5000,
      gameId: "space-typing",
    }),
  );

  const result = queryLearningProfile(
    profile,
    {
      entityType: "vocabulary",
      page: 1,
      pageSize: 10,
      sort: "smart-priority",
      filters: { sourceGame: "space-typing" },
    },
    "2026-09-24T10:00:00.000Z",
  );

  assert.equal(result.totalItems, 2);
  assert.deepEqual(
    result.items.map((item) => item.entityId),
    ["beta", "gamma"],
  );
  assert.ok(
    result.items[0].reviewPriority >= result.items[1].reviewPriority,
  );
});
