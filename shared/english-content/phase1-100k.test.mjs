import assert from "node:assert/strict";
import fs from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

import { createEnglishRuntimeLoader } from "./runtime-loader.mjs";
import { loadPublishedEnglishActivityRecords } from "./activity-source.mjs";
import { englishActivityItemsFromRecords } from "./game-adapters.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");

test("Phase 2 200k vocabulary runtime integrity", async () => {
  // 1. Verify shared/dictionary/manifest.json
  const manifestRaw = await fs.readFile(path.join(root, "shared", "dictionary", "manifest.json"), "utf8");
  const manifest = JSON.parse(manifestRaw);
  assert.equal(manifest.schemaVersion, 1);
  assert.equal(manifest.dataset, "dictionary");
  assert.equal(manifest.count, 200900);
  assert.equal(manifest.shards.length, 203);

  // 2. Verify shared/dictionary/lookup.json
  const lookupRaw = await fs.readFile(path.join(root, "shared", "dictionary", "lookup.json"), "utf8");
  const lookup = JSON.parse(lookupRaw);
  assert.equal(lookup.schemaVersion, 1);
  assert.equal(lookup.totalEntries, 200297);
  assert.equal(lookup.totalShards, 200);

  // Test spot checks in lookup across Phase 1 and Phase 2
  assert.equal(typeof lookup.entries["about"], "number");
  assert.equal(typeof lookup.entries["good"], "number");
  assert.equal(typeof lookup.entries["water"], "number");
  assert.equal(typeof lookup.entries["accessed"], "number");
  assert.equal(typeof lookup.entries["above all"], "number");

  // 3. Verify activity index for vocabulary
  const vocabIndexRaw = await fs.readFile(path.join(root, "shared", "indexes", "activities", "vocabulary.json"), "utf8");
  const vocabIndex = JSON.parse(vocabIndexRaw);
  assert.equal(vocabIndex.schemaVersion, 1);
  assert.equal(vocabIndex.total, 200300);
  assert.equal(vocabIndex.shards.length, 201);

  // 4. Verify attribution records in shared/attribution/english-content/
  const attrRaw = await fs.readFile(path.join(root, "shared", "attribution", "english-content", "sources", "000.json"), "utf8");
  const attr = JSON.parse(attrRaw);
  const thichhoc = attr.records.find((r) => r.id === "thichhoc-dict");
  const cmudict = attr.records.find((r) => r.id === "cmudict");
  assert.ok(thichhoc, "thichhoc-dict attribution is required");
  assert.equal(thichhoc.license, "CC-BY-SA-4.0");
  assert.ok(cmudict, "cmudict attribution is required");
  assert.equal(cmudict.license, "BSD-2-Clause");

  // 5. Verify legacy vocabulary levels (001 to 100) are intact
  const level001Raw = await fs.readFile(path.join(root, "shared", "vocabulary", "levels", "001.json"), "utf8");
  const level001 = JSON.parse(level001Raw);
  assert.equal(level001.version, 1);
  assert.equal(level001.level, 1);
  assert.equal(level001.entries[0].en, "good");

  // 6. Test runtime loading & game adaptation
  // Mock fetcher for local file system testing
  async function localFetcher(url) {
    const rel = url.replace("https://typing-game.local/english-content/", "");
    const fullPath = path.join(root, "shared", rel);
    const content = await fs.readFile(fullPath, "utf8");
    return {
      ok: true,
      status: 200,
      json: async () => JSON.parse(content),
    };
  }

  const loader = createEnglishRuntimeLoader({ fetcher: localFetcher });

  // Load vocabulary records via activity-source
  const records = await loadPublishedEnglishActivityRecords(loader, "vocabulary", {
    limit: 25,
    tier: "core",
  });
  assert.ok(records.length > 0, "must load published vocabulary records");

  // Adapt records to game activity items
  const items = englishActivityItemsFromRecords("vocabulary", records);
  assert.equal(items.length, records.length);
  for (const item of items) {
    assert.equal(item.entityType, "vocabulary");
    assert.ok(item.promptText.length > 0, "promptText (Vietnamese) must be non-empty");
    assert.ok(item.answerText.length > 0, "answerText (English) must be non-empty");
    assert.ok(item.meaningVi.length > 0, "meaningVi must be non-empty");
  }
});
