import test from "node:test";
import assert from "node:assert/strict";
import { createEnglishRuntimeLoader, parseRuntimeManifest } from "./runtime-loader.mjs";
import { indexBucketHex } from "./index-bucket.mjs";
import { datasetForEnglishContentId, createEnglishReviewItemResolver } from "./review-item.mjs";
import { supportsEnglishActivity, listEnglishActivities } from "./capabilities.mjs";

test("runtime manifest validates counts and optional shard integrity fields", () => {
  const m = parseRuntimeManifest(
    {
      schemaVersion: 1,
      contentVersion: "2026.10.0",
      dataset: "phrases",
      count: 2,
      shards: [{
        id: "p-0",
        path: "p/000.json",
        count: 2,
        bytes: 120,
        sha256: "a".repeat(64),
      }],
    },
    "phrases",
  );
  assert.equal(m.count, 2);
  assert.equal(m.shards[0].bytes, 120);
  assert.throws(() => parseRuntimeManifest({ schemaVersion: 1, contentVersion: "x", dataset: "phrases", count: 2, shards: [] }, "phrases"));
  assert.throws(() => parseRuntimeManifest({
    schemaVersion: 1,
    contentVersion: "2026.10.0",
    dataset: "phrases",
    count: 1,
    shards: [{ id: "p-0", path: "p/000.json", count: 1, sha256: "bad" }],
  }, "phrases"));
});

test("runtime loader caches bounded manifest and shard", async () => {
  const calls = [];
  const payloads = {
    "https://typing-game.local/english-content/phrases/manifest.json": {
      schemaVersion: 1,
      contentVersion: "2026.10.0",
      dataset: "phrases",
      count: 1,
      shards: [{ id: "phrases-000", path: "items/000.json", count: 1 }],
    },
    "https://typing-game.local/english-content/phrases/items/000.json": {
      schemaVersion: 1,
      records: [{ id: "pv.00000001", text: "get up" }],
    },
  };
  const fetcher = async (input) => {
    calls.push(input);
    return { ok: true, status: 200, json: async () => payloads[input] };
  };
  const loader = createEnglishRuntimeLoader({ fetcher });
  assert.equal((await loader.loadDataset("phrases")).length, 1);
  assert.equal((await loader.loadDataset("phrases")).length, 1);
  assert.equal(calls.length, 2);
});

test("runtime loader enforces bounded LRU shard eviction, version pinning, and indexed resolution", async () => {
  const shard1Id = "sent.1";
  const shard2Id = "sent.2";
  const b1 = indexBucketHex(shard1Id);
  const b2 = indexBucketHex(shard2Id);
  const colHex = indexBucketHex("col.1");

  const calls = [];
  const payloads = {
    "https://typing-game.local/english-content/sentences/manifest.json": {
      schemaVersion: 1,
      contentVersion: "2026.10.0",
      dataset: "sentences",
      count: 2,
      shards: [
        { id: "examples-000", path: "examples/000.json", count: 1 },
        { id: "examples-001", path: "examples/001.json", count: 1 },
      ],
    },
    "https://typing-game.local/english-content/sentences/examples/000.json": {
      schemaVersion: 1,
      records: [{ id: shard1Id, text: "First.", cefr: "A1" }],
    },
    "https://typing-game.local/english-content/sentences/examples/001.json": {
      schemaVersion: 1,
      records: [{ id: shard2Id, text: "Second.", cefr: "B1" }],
    },
    "https://typing-game.local/english-content/grammar/manifest.json": {
      schemaVersion: 1,
      contentVersion: "2026.99.0",
      dataset: "grammar",
      count: 0,
      shards: [],
    },
    [`https://typing-game.local/english-content/indexes/by-id/${b1}.json`]: {
      schemaVersion: 1,
      contentVersion: "2026.10.0",
      bucket: b1,
      entries: {
        [shard1Id]: ["sentences", "examples/000.json", 0],
        ...(b1 === b2 ? { [shard2Id]: ["sentences", "examples/001.json", 0] } : {}),
      },
    },
    ...(b1 !== b2
      ? {
          [`https://typing-game.local/english-content/indexes/by-id/${b2}.json`]: {
            schemaVersion: 1,
            contentVersion: "2026.10.0",
            bucket: b2,
            entries: { [shard2Id]: ["sentences", "examples/001.json", 0] },
          },
        }
      : {}),
    [`https://typing-game.local/english-content/indexes/evidence/${colHex}.json`]: {
      schemaVersion: 1,
      contentVersion: "2026.10.0",
      bucket: colHex,
      entries: { "col.1": { exampleIds: [shard1Id, shard2Id] } },
    },
  };

  const fetcher = async (input) => {
    calls.push(input);
    const data = payloads[input];
    if (data === undefined) return { ok: false, status: 404, json: async () => ({}) };
    return { ok: true, status: 200, json: async () => data };
  };

  // LRU maxCachedShards: 1 forces refetch when switching shards
  const loader = createEnglishRuntimeLoader({ fetcher, maxCachedShards: 1, maxConcurrency: 2 });
  const resolved = await loader.resolvePublishedByIds([shard2Id, "sent.missing"]);
  assert.equal(resolved.usedIndex, true);
  assert.equal(resolved.recordsById.get(shard2Id)?.text, "Second.");
  assert.deepEqual(resolved.missingIds, ["sent.missing"]);
  assert.equal(loader.getPinnedContentVersion(), "2026.10.0");

  // getEvidence respects CEFR filter
  const ev = await loader.getEvidence("col.1", { cefr: "B1", limit: 5 });
  assert.equal(ev.records.length, 1);
  assert.equal(ev.records[0].id, shard2Id);

  // Version drift across datasets fails explicitly
  await assert.rejects(() => loader.loadManifest("grammar"), /contentVersion drift/);
});

test("review item routes stable ids", async () => {
  assert.equal(datasetForEnglishContentId("col.00000001"), "phrases");
  assert.equal(datasetForEnglishContentId("gr.a1.x"), "grammar");
  assert.equal(datasetForEnglishContentId("unknown.x"), null);
  const resolver = createEnglishReviewItemResolver({ findById: async (dataset, id) => (dataset === "phrases" ? { id } : null) });
  assert.equal((await resolver("pv.00000001")).dataset, "phrases");
});

test("capability routing is explicit per game", () => {
  assert.equal(supportsEnglishActivity("monkeytype", "sentence-building"), true);
  assert.equal(supportsEnglishActivity("shooter", "sentence-building"), false);
  assert.ok(listEnglishActivities("space").includes("grammar-challenge"));
});

test("runtime loader serves optional topic packs and E14 lexical pilot", async () => {
  const pack = {
    schemaVersion: 1,
    id: "pack.travel-booking-a2",
    title: "Travel & Booking Essentials (A2)",
    items: [{ contentId: "col.00000006", stage: "input", activity: "collocation", learningFocus: "recognition" }],
  };
  const payloads = {
    "https://typing-game.local/english-content/indexes/packs/manifest.json": {
      schemaVersion: 1,
      contentVersion: "2026.10.0",
      count: 1,
      packs: [{ id: pack.id, title: pack.title, itemCount: 1 }],
    },
    "https://typing-game.local/english-content/indexes/packs/pack.travel-booking-a2.json": {
      schemaVersion: 1,
      contentVersion: "2026.10.0",
      pack,
    },
    "https://typing-game.local/english-content/indexes/lexical/e14-pilot.json": {
      schemaVersion: 1,
      contentVersion: "2026.10.0",
      lexemes: [{ lexemeId: "lex.e14.take", lemma: "take", senses: [{ senseId: "sense.e14.take.1" }] }],
    },
  };
  const loader = createEnglishRuntimeLoader({
    fetcher: async (input) => {
      const data = payloads[input];
      if (data === undefined) return { ok: false, status: 404, json: async () => ({}) };
      return { ok: true, status: 200, json: async () => data };
    },
  });

  const manifest = await loader.loadTopicPacksManifest();
  assert.equal(manifest.count, 1);
  assert.equal(manifest.packs[0].id, "pack.travel-booking-a2");

  const loadedPack = await loader.loadTopicPack("pack.travel-booking-a2");
  assert.equal(loadedPack.id, "pack.travel-booking-a2");
  assert.equal(loadedPack.items.length, 1);
  assert.equal(await loader.loadTopicPack("pack.missing"), null);
  assert.equal(await loader.loadTopicPack("  "), null);

  const pilot = await loader.loadLexicalPilot();
  assert.equal(pilot.lexemes.length, 1);
  assert.equal(pilot.lexemes[0].lemma, "take");

  // Cached index manifest obeys contentVersion drift pin
  await assert.rejects(
    async () => {
      const badLoader = createEnglishRuntimeLoader({
        pinnedContentVersion: "2026.99.0",
        fetcher: async (input) => ({
          ok: true,
          status: 200,
          json: async () => payloads[input],
        }),
      });
      await badLoader.loadLexicalPilot();
    },
    /contentVersion drift/,
  );
});
