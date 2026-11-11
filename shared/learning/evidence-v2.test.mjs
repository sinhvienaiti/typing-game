import test from "node:test";
import assert from "node:assert/strict";
import {
  applyLearningEvidenceEvent,
  createEmptyEvidenceStore,
  toCompatibleV1LearningEvent,
} from "./evidence-v2.mjs";

test("typing-fluency copy-typing never inflates semantic sense mastery", () => {
  let store = createEmptyEvidenceStore("2026-11-10T00:00:00.000Z");
  store = applyLearningEvidenceEvent(store, {
    version: 2,
    contentId: "sent.tatoeba.100",
    entityId: "sense.make.01",
    entityKind: "sense",
    activityType: "example-typing",
    dimension: "typing-fluency",
    outcome: "correct",
    responseMs: 1200,
    occurredAt: "2026-11-10T00:01:00.000Z",
  });

  const record = store.entities["sense:sense.make.01"];
  assert.ok(record.typingFluencyScore >= 80);
  assert.equal(record.semanticMastery, 0);

  // Now add genuine semantic usage discrimination -> raises semanticMastery
  store = applyLearningEvidenceEvent(store, {
    version: 2,
    contentId: "ex.ctx.1",
    entityId: "sense.make.01",
    entityKind: "sense",
    activityType: "contextual-usage",
    dimension: "usage-discrimination",
    outcome: "correct",
    responseMs: 3100,
    occurredAt: "2026-11-10T00:02:00.000Z",
  });
  assert.ok(store.entities["sense:sense.make.01"].semanticMastery > 0);
});

test("needs-review open outcomes never record incorrect counts or emit wrong v1 events", () => {
  let store = createEmptyEvidenceStore();
  const ev = {
    version: 2,
    contentId: "ex.trans.1",
    entityId: "sent.1",
    activityType: "translation",
    dimension: "production",
    outcome: "needs-review",
    userAnswer: "Every morning I check my inbox.",
    expectedAnswer: "I check my email every morning.",
    occurredAt: "2026-11-10T00:03:00.000Z",
  };
  store = applyLearningEvidenceEvent(store, ev);
  const record = store.entities["sentence:sent.1"];
  assert.equal(record.dimensions.production.incorrect, 0);
  assert.equal(record.dimensions.production.needsReview, 1);
  assert.equal(toCompatibleV1LearningEvent(ev), null);
});

test("unverified rotational E11 targets cannot pollute grammar semantic mastery", () => {
  let store = createEmptyEvidenceStore();
  store = applyLearningEvidenceEvent(store, {
    version: 2,
    contentId: "ex.cloze.e11.01.020",
    entityId: "gr.a2.too-much-many-enough-noun",
    fallbackSentenceId: "sent.00000007",
    targetConfidence: "unverified-rotational",
    activityType: "cloze",
    dimension: "recall",
    outcome: "incorrect",
    occurredAt: "2026-11-10T00:04:00.000Z",
  });

  assert.equal(store.entities["grammar:gr.a2.too-much-many-enough-noun"], undefined);
  assert.equal(store.entities["sentence:sent.00000007"].dimensions.recall.incorrect, 1);
});

test("tracks Topic Pack progress safely across items", () => {
  let store = createEmptyEvidenceStore();
  store = applyLearningEvidenceEvent(store, {
    version: 2,
    contentId: "col.00000002",
    packId: "pack.travel-01",
    stage: "practice",
    activityType: "collocation",
    outcome: "correct",
    occurredAt: "2026-11-10T00:05:00.000Z",
  });
  assert.deepEqual(store.packs["pack.travel-01"].completedContentIds, ["col.00000002"]);
});
