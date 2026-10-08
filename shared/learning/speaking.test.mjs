import test from "node:test";
import assert from "node:assert/strict";
import { applyLearningEvent, createEmptyLearningProfile } from "./core.mjs";
import {
  createLearningProfileBackup,
  parseLearningProfileBackup,
  resetLearningProfileSelection,
} from "./profile-backup.mjs";
const event = (activityType, extra = {}) => ({
  version: 1,
  entityType: "vocabulary",
  entityId: "planet",
  gameId: "space-typing",
  activityType,
  result: "correct",
  occurredAt: "2026-10-04T00:00:00Z",
  hintUsed: false,
  replayUsed: false,
  expectedAnswer: "planet",
  ...extra,
});
test("speaking and speaking recall preserve assists without contributing to spelling mastery", () => {
  let p = applyLearningEvent(createEmptyLearningProfile(), event("typing"));
  const before = structuredClone(p.vocabulary.planet);
  p = applyLearningEvent(p, event("speaking"));
  p = applyLearningEvent(
    p,
    event("speaking-recall", {
      hintUsed: true,
      replayUsed: true,
      responseMs: 500,
    }),
  );
  assert.deepEqual(p.vocabulary.planet, before);
  assert.deepEqual(p.speaking.planet.activities, {
    speaking: 1,
    "speaking-recall": 1,
  });
  assert.equal(p.speaking.planet.hints, 1);
  assert.equal(p.speaking.planet.replays, 1);
  assert.equal(p.speaking.planet.recentEvents[1].responseMs, 500);
  assert.equal(p.speaking.planet.mastery, undefined);
  assert.deepEqual(
    parseLearningProfileBackup(JSON.stringify(createLearningProfileBackup(p))),
    p,
  );
});
test("speaking-only profiles round-trip, bound history, and reset with vocabulary history", () => {
  let p = createEmptyLearningProfile();
  for (let i = 0; i < 20; i++) p = applyLearningEvent(p, event("speaking"));
  assert.deepEqual(p.vocabulary, {});
  assert.equal(p.speaking.planet.recentEvents.length, 8);
  assert.equal(
    parseLearningProfileBackup(createLearningProfileBackup(p)).speaking.planet
      .accepted,
    20,
  );
  assert.deepEqual(
    resetLearningProfileSelection(p, ["vocabulary"]).speaking,
    {},
  );
  const bad = structuredClone(p);
  bad.speaking.planet.accepted = 1;
  assert.throws(() => createLearningProfileBackup(bad));
});
