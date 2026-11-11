import test from "node:test";
import assert from "node:assert/strict";
import {
  buildPublishedGameEnglishActivityDataset,
  countPublishedEnglishActivityRecords,
  loadPublishedEnglishActivityRecords,
  publishedEnglishActivityAvailability,
} from "./activity-source.mjs";

const published = { state: "published" };

function fakeLoader(groups) {
  return {
    async loadDataset(dataset, { prefix } = {}) {
      return groups[dataset + ":" + String(prefix ?? "")] ?? [];
    },
  };
}

test("loads only published records for the requested exercise type", async () => {
  const loader = fakeLoader({
    "sentences:exercises-": [
      { id: "ex.cloze.1", type: "cloze", quality: published },
      { id: "ex.translation.1", type: "translation", quality: published },
      { id: "ex.translation.draft", type: "translation", quality: { state: "draft" } },
    ],
  });
  const records = await loadPublishedEnglishActivityRecords(loader, "translation", { limit: 10 });
  assert.deepEqual(records.map((record) => record.id), ["ex.translation.1"]);
  assert.equal(await countPublishedEnglishActivityRecords(loader, "translation"), 1);
});

test("builds a bounded Karaoke translation dataset from published runtime records", async () => {
  const loader = fakeLoader({
    "sentences:exercises-": [{
      id: "ex.translation.1",
      type: "translation",
      prompt: "Tôi đang đợi tàu.",
      acceptedAnswers: ["I am waiting for the train."],
      sourceSentenceIds: ["sent.1"],
      quality: published,
    }],
  });
  const dataset = await buildPublishedGameEnglishActivityDataset(
    loader,
    "karaoke-typing",
    "karaoke",
    "translation",
    "karaoke-runtime-1",
    { limit: 20, createdAt: "2026-10-03T00:00:00.000Z" },
  );
  assert.equal(dataset.items.length, 1);
  assert.equal(dataset.items[0].entityId, "sent.1");
});

test("builds Space grammar challenge from published topics", async () => {
  const loader = fakeLoader({
    "grammar:topics-": [{
      id: "gr.a1.present-simple-routines",
      title: "Present Simple",
      objective: "Describe repeated routines.",
      forms: { positive: ["I work at home."] },
      quality: published,
    }],
  });
  const dataset = await buildPublishedGameEnglishActivityDataset(
    loader,
    "space-typing",
    "space",
    "grammar-challenge",
    "space-runtime-1",
  );
  assert.equal(dataset.items[0].entityType, "grammar");
  assert.equal(dataset.items[0].entityId, "gr.a1.present-simple-routines");
});

test("uses indexes for O(1) availability, CEFR/length filtering, and bounds multi-turn dialogues safely", async () => {
  let datasetScanned = false;
  const indexedLoader = {
    async loadDataset() {
      datasetScanned = true;
      return [];
    },
    async loadAvailability() {
      return {
        schemaVersion: 1,
        contentVersion: "2026.10.0",
        activities: {
          cloze: { total: 50600, byCefr: { B1: 12000 }, within200: 50600, within240: 50600 },
          dialogue: { total: 10125, byCefr: { A2: 10000 }, within200: 10125, within240: 10125 },
        },
      };
    },
    async loadActivityIndex(activity) {
      if (activity === "cloze") {
        return {
          schemaVersion: 1,
          contentVersion: "2026.10.0",
          activity: "cloze",
          total: 50600,
          shards: [
            { dataset: "sentences", shardId: "exercises-000", path: "exercises/000.json", count: 2, matchedCount: 2, byCefr: { A1: 2 }, minLen: 5, maxLen: 10 },
            { dataset: "sentences", shardId: "exercises-001", path: "exercises/001.json", count: 2, matchedCount: 2, byCefr: { B1: 2 }, minLen: 6, maxLen: 12 },
          ],
        };
      }
      return null;
    },
    async loadShard(_ds, shard) {
      if (shard.id === "exercises-001") {
        return [
          { id: "ex.cloze.b1.1", type: "cloze", prompt: "He ___", acceptedAnswers: ["decided"], cefr: "B1", quality: published },
          { id: "ex.cloze.b1.2", type: "cloze", prompt: "She ___", acceptedAnswers: ["arrived"], cefr: "B1", quality: published },
        ];
      }
      throw new Error("Should not load non-matching shard " + shard.id);
    },
  };

  assert.equal(await countPublishedEnglishActivityRecords(indexedLoader, "cloze", { cefr: "B1" }), 12000);
  const avail = await publishedEnglishActivityAvailability(indexedLoader, "karaoke");
  assert.equal(avail.dialogue, 10125);
  assert.equal(datasetScanned, false);

  const b1 = await loadPublishedEnglishActivityRecords(indexedLoader, "cloze", { cefr: "B1", limit: 1, seed: 7 });
  assert.equal(b1.length, 1);
  assert.equal(b1[0].cefr, "B1");

  // Dialogue with 10 records x 15 turns = 150 turns -> bounded to <= 100 turns without throwing!
  const turns15 = Array.from({ length: 15 }, (_, idx) => ({
    speaker: idx % 2 === 0 ? "User" : "System",
    text: `Turn number ${idx + 1}.`,
  }));
  const manyDialogues = Array.from({ length: 10 }, (_, d) => ({
    id: `dlg.mw.test.${d}`,
    scenario: "hotel",
    turns: turns15,
    quality: published,
  }));
  const dLoader = fakeLoader({ "sentences:dialogues-": manyDialogues });
  const dialogueDataset = await buildPublishedGameEnglishActivityDataset(
    dLoader,
    "karaoke-typing",
    "karaoke",
    "dialogue",
    "karaoke-bound-turns",
    { limit: 20 },
  );
  assert.ok(dialogueDataset.items.length > 0 && dialogueDataset.items.length <= 100);
});

test("refuses unsupported game/activity combinations", async () => {
  const loader = fakeLoader({ "sentences:exercises-": [] });
  await assert.rejects(
    buildPublishedGameEnglishActivityDataset(
      loader,
      "vocab-shooter",
      "shooter",
      "translation",
      "bad-runtime",
    ),
    /not supported/,
  );
});
