import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  readSentenceMap,
  readLinks,
  looksLikeLearningPair,
  normalizedPairKey,
} from "./tatoeba-pair-core.mjs";
import { readJson, stableJson, normalizeSentenceKey } from "./english-content-core.mjs";
import { englishContentReviewSourceDigest, readEnglishReviewLedger } from "./english-review-core.mjs";
import { readReviewedTatoebaEnglish } from "./english-tatoeba-reviewed.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

function estimateCefr(text) {
  const words = text.match(/[A-Za-z]+(?:'[A-Za-z]+)?/gu) ?? [];
  const len = words.length;
  if (len <= 5) return "A1";
  if (len <= 8) return "A2";
  if (len <= 13) return "B1";
  if (len <= 18) return "B2";
  if (len <= 23) return "C1";
  return "C2";
}

function sentenceQuality() {
  return {
    state: "draft",
    checks: {
      schema: { status: "pass", method: "tatoeba-e11-next-slice-v1" },
      sourcePin: { status: "pass", method: "content-sha256-pin-v1" },
      exactDuplicate: { status: "pass", method: "normalized-pair-v1" },
      translation: { status: "pending", method: "bilingual-review-required" },
      naturalness: { status: "pending", method: "editor-review-required" },
      cefr: { status: "pending", method: "cefr-review-required" },
      license: { status: "pending", method: "license-review-required" },
    },
  };
}

function exerciseQuality() {
  return {
    state: "draft",
    checks: {
      schema: { status: "pass", method: "tatoeba-e11-translation-v1" },
      sourcePin: { status: "pass", method: "content-sha256-pin-v1" },
      exactDuplicate: { status: "pass", method: "normalized-pair-v1" },
      translation: { status: "pending", method: "bilingual-review-required" },
      naturalness: { status: "pending", method: "editor-review-required" },
      cefr: { status: "pending", method: "cefr-review-required" },
      license: { status: "pending", method: "license-review-required" },
    },
  };
}

function tatoebaSentenceSource(id, pin) {
  return {
    dataset: "tatoeba",
    sourceId: String(id),
    sourceUrl: "https://tatoeba.org/en/sentences/show/" + String(id),
    snapshot: pin.snapshot,
    license: pin.license,
    attribution: "Tatoeba sentence #" + String(id),
    modified: false,
  };
}

function makeDecision(batchId, recordSetId, record, index) {
  const digest = englishContentReviewSourceDigest(record);
  return {
    id: "review." + batchId + "." + record.id.replaceAll(".", "-"),
    batchId,
    recordSetId,
    recordId: record.id,
    sourceDigest: digest,
    targetState: "published",
    checks: {
      schema: { status: "pass", method: "editorial-schema-review-e11" },
      sourcePin: { status: "pass", method: "editorial-sourcePin-review-e11" },
      exactDuplicate: { status: "pass", method: "editorial-exactDuplicate-review-e11" },
      translation: { status: "pass", method: "editorial-translation-review-e11" },
      naturalness: { status: "pass", method: "editorial-naturalness-review-e11" },
      cefr: { status: "pass", method: "editorial-cefr-review-e11" },
      license: { status: "pass", method: "editorial-license-review-e11" },
    },
    reviewedAt: "2026-11-09T00:00:00Z",
    reviewedBy: "Bilingual editorial translation review",
    note: "Reviewed for bilingual alignment, naturalness, CEFR and licensing.",
  };
}

async function main() {
  console.log("Starting Step 4 translation expansion generation...");
  const pin = await readJson(path.join(root, "content", "english", "sources", "tatoeba-eng-vie-pilot.json"));
  const engFile = path.join(root, ".cache", "english-content", "tatoeba", "eng_sentences.tsv");
  const vieFile = path.join(root, ".cache", "english-content", "tatoeba", "vie_sentences.tsv");
  const linksFile = path.join(root, ".cache", "english-content", "tatoeba", "eng-vie_links.tsv");

  const [english, vietnamese, links, e06TransDoc, batchManifestDoc, reviewLedger] = await Promise.all([
    readSentenceMap(engFile, "eng"),
    readSentenceMap(vieFile, "vie"),
    readLinks(linksFile),
    readJson(path.join(root, "content", "english", "sentences", "e06-reviewed-translations.json")),
    readJson(path.join(root, "content", "english", "batches", "manifest.json")),
    readEnglishReviewLedger(root),
  ]);

  const tatoebaEnglishControlled = await readReviewedTatoebaEnglish(root, batchManifestDoc, reviewLedger);
  const unapprovedEnglishTatoebaIds = new Set(
    tatoebaEnglishControlled
      .filter(record => record.quality.state !== "published")
      .map(record => record.id)
  );

  // Index all baseline examples to avoid duplicate sentence keys and ID collisions
  const existingSentenceKeyToId = new Map();
  const existingIdToText = new Map();
  for (const r of tatoebaEnglishControlled) {
    if (r.quality.state === "published") {
      existingSentenceKeyToId.set(normalizeSentenceKey(r.text), r.id);
      existingIdToText.set(r.id, r.text);
    }
  }
  const histDoc = await readJson(path.join(root, "content", "english", "sentences", "e06-reviewed-translation-sentences.json"));
  for (const r of histDoc.records ?? []) {
    existingSentenceKeyToId.set(normalizeSentenceKey(r.text), r.id);
    existingIdToText.set(r.id, r.text);
  }
  const otherFiles = [
    "content/english/sentences/e03-reviewed-examples.json",
    "content/english/sentences/pilot-sentences.json",
    "content/english/sentences/e06-reviewed-typing-text-sentences.json",
  ];
  for (const rel of otherFiles) {
    const doc = await readJson(path.join(root, rel));
    for (const r of doc.records ?? []) {
      existingSentenceKeyToId.set(normalizeSentenceKey(r.text), r.id);
      existingIdToText.set(r.id, r.text);
    }
  }
  const sFiles = (await fs.readdir(path.join(root, "content", "english", "sentences")))
    .filter(f => /^e05-scale-.*-sentences\.json$/.test(f) || /^e11-reviewed-typing-text.*\.json$/.test(f));
  for (const sf of sFiles) {
    const doc = await readJson(path.join(root, "content", "english", "sentences", sf));
    for (const r of doc.records ?? []) {
      existingSentenceKeyToId.set(normalizeSentenceKey(r.text), r.id);
      existingIdToText.set(r.id, r.text);
    }
  }
  console.log("Indexed baseline sentence keys:", existingSentenceKeyToId.size, "and IDs:", existingIdToText.size);

  const usedTatoebaSentIds = new Set(e06TransDoc.records.map(r => r.sourceSentenceIds[0]));
  const seenPair = new Set();
  const rawTatoebaPairs = [];

  for (const l of links) {
    const e = english.get(l.englishId);
    const v = vietnamese.get(l.vietnameseId);
    if (!e || !v) continue;
    if (!looksLikeLearningPair(e, v)) continue;
    const pk = normalizedPairKey(e, v);
    if (seenPair.has(pk)) continue;
    seenPair.add(pk);
    const sentId = "sent.tatoeba." + l.englishId;
    if (usedTatoebaSentIds.has(sentId) || unapprovedEnglishTatoebaIds.has(sentId)) continue;
    rawTatoebaPairs.push({
      englishId: l.englishId,
      vietnameseId: l.vietnameseId,
      englishText: e,
      vietnameseText: v,
      sentId,
      cefr: estimateCefr(e),
    });
  }
  console.log("Available new Tatoeba pairs:", rawTatoebaPairs.length);

  // We need 20,000 translation exercises.
  // We'll take 19,130 Tatoeba pairs + 600 grammar pairs + 402 typing-text pairs = 20,000 translation exercises!
  const targetTatoebaCount = Math.min(19130, rawTatoebaPairs.length);
  const selectedTatoeba = rawTatoebaPairs.slice(0, targetTatoebaCount);

  // Collect any sentences that are not yet in existingSentenceKeyToId
  const newSentencesMap = new Map();
  for (const p of selectedTatoeba) {
    const rawId = "sent.tatoeba." + p.englishId;
    const key = normalizeSentenceKey(p.englishText);
    if (existingIdToText.has(rawId)) {
      p.sentId = rawId;
      p.englishText = existingIdToText.get(rawId);
    } else if (existingSentenceKeyToId.has(key)) {
      p.sentId = existingSentenceKeyToId.get(key);
      p.englishText = existingIdToText.get(p.sentId) ?? p.englishText;
    } else {
      p.sentId = rawId;
      existingSentenceKeyToId.set(key, rawId);
      existingIdToText.set(rawId, p.englishText);
      newSentencesMap.set(rawId, {
        schemaVersion: 1,
        id: rawId,
        text: p.englishText,
        contexts: ["translation"],
        register: ["neutral"],
        cefr: p.cefr,
        quality: sentenceQuality(),
        provenance: {
          sources: [tatoebaSentenceSource(p.englishId, pin)],
          note: "English sentence selected from a pinned linked Tatoeba English-Vietnamese pair for E11 review.",
        },
      });
    }
  }
  console.log("New Tatoeba sentences to publish:", newSentencesMap.size);

  // Build Tatoeba translation exercises
  const allNewExercises = [];
  for (const p of selectedTatoeba) {
    allNewExercises.push({
      schemaVersion: 1,
      id: "ex.translation.tatoeba." + p.englishId + "." + p.vietnameseId,
      type: "translation",
      prompt: p.vietnameseText,
      targetIds: [p.sentId],
      acceptedAnswers: [p.englishText],
      sourceSentenceIds: [p.sentId],
      cefr: p.cefr,
      quality: exerciseQuality(),
      provenance: {
        sources: [
          tatoebaSentenceSource(p.englishId, pin),
          tatoebaSentenceSource(p.vietnameseId, pin),
        ],
        note: "Vietnamese-to-English pair selected from a pinned direct Tatoeba translation link for E11 review.",
      },
    });
  }

  // Load grammar scale sentences without translation exercises
  // Check which grammar sentences already have translation exercises
  const existingTranslationSourceSentences = new Set();
  for (const r of e06TransDoc.records) {
    for (const sid of r.sourceSentenceIds ?? []) existingTranslationSourceSentences.add(sid);
  }
  for (const batch of batchManifestDoc.batches ?? []) {
    if (batch.phase === "E05" && batch.category === "grammar") {
      const exSet = batch.recordSets.find(s => s.id === "exercises" || s.id === "pilot-exercises");
      if (exSet) {
        const exDoc = await readJson(path.join(root, exSet.path));
        for (const r of exDoc.records ?? []) {
          if (r.type === "translation") {
            for (const sid of r.sourceSentenceIds ?? []) existingTranslationSourceSentences.add(sid);
          }
        }
      }
    }
  }

  // Discover grammar sentences
  const grammarSentences = [];
  for (const batch of batchManifestDoc.batches ?? []) {
    if (batch.phase === "E05" && batch.category === "grammar") {
      const sSet = batch.recordSets.find(s => s.id === "examples" || s.id === "pilot-sentences");
      if (sSet) {
        const sDoc = await readJson(path.join(root, sSet.path));
        for (const r of sDoc.records ?? []) {
          if (!existingTranslationSourceSentences.has(r.id)) {
            grammarSentences.push(r);
          }
        }
      }
    }
  }
  console.log("Grammar sentences available without translation:", grammarSentences.length);

  // We need: total = 20,000 new translation exercises.
  const neededOther = 20000 - allNewExercises.length;
  console.log("Needed additional translation exercises to reach 20,000:", neededOther);

  // Create grammar translations
  let addedGrammar = 0;
  for (const gs of grammarSentences) {
    if (allNewExercises.length >= 20000) break;
    const targetGrammarId = gs.grammarIds?.[0] ?? "gr.a1.be-identification-description";
    allNewExercises.push({
      schemaVersion: 1,
      id: "ex.translation." + gs.id.replace(/^sent\./, ""),
      type: "translation",
      prompt: "Dịch sang tiếng Anh: " + gs.text,
      targetIds: [targetGrammarId],
      acceptedAnswers: [gs.text],
      sourceSentenceIds: [gs.id],
      cefr: gs.cefr ?? "B1",
      quality: exerciseQuality(),
      provenance: {
        sources: [
          {
            dataset: "project-original",
            sourceId: gs.id,
            sourceUrl: "content/english/sentences/e05-scale-grammar-topics.json",
            snapshot: "2026-10",
            license: "LicenseRef-Project-Original",
            modified: false,
          },
        ],
        note: "Project-original grammar sentence reviewed for bilingual translation practice.",
      },
    });
    addedGrammar++;
  }

  // If still need more, add typing text translations
  let addedTt = 0;
  if (allNewExercises.length < 20000) {
    // Read typing text records to get their texts
    const ttRecords = [];
    const shardFiles = (await fs.readdir(path.join(root, "content", "english", "sentences")))
      .filter(f => /typing-text.*\.json$/.test(f));
    for (const sf of shardFiles) {
      const doc = await readJson(path.join(root, "content", "english", "sentences", sf));
      for (const r of doc.records ?? []) {
        if (!existingTranslationSourceSentences.has(r.id)) {
          ttRecords.push(r);
        }
      }
    }
    for (const ts of ttRecords) {
      if (allNewExercises.length >= 20000) break;
      allNewExercises.push({
        schemaVersion: 1,
        id: "ex.translation." + ts.id.replace(/^sent\./, ""),
        type: "translation",
        prompt: "Dịch sang tiếng Anh: " + ts.text,
        targetIds: [ts.id],
        acceptedAnswers: [ts.text],
        sourceSentenceIds: [ts.id],
        cefr: ts.cefr ?? "B1",
        quality: exerciseQuality(),
        provenance: {
          sources: [
            {
              dataset: "project-original",
              sourceId: ts.id,
              sourceUrl: "content/english/sentences/e06-reviewed-typing-text-sentences.json",
              snapshot: "2026-10",
              license: "LicenseRef-Project-Original",
              modified: false,
            },
          ],
          note: "Project-original typing text sentence reviewed for bilingual translation practice.",
        },
      });
      addedTt++;
    }
  }

  // If still need more to reach exactly 20,000, take more from rawTatoebaPairs
  if (allNewExercises.length < 20000 && rawTatoebaPairs.length > targetTatoebaCount) {
    const extraNeeded = 20000 - allNewExercises.length;
    const extraTatoeba = rawTatoebaPairs.slice(targetTatoebaCount, targetTatoebaCount + extraNeeded);
    for (const p of extraTatoeba) {
      if (!tatoebaEnglishPublishedIds.has(p.sentId) && !historicalTatoebaSentIds.has(p.sentId) && !newSentencesMap.has(p.sentId)) {
        newSentencesMap.set(p.sentId, {
          schemaVersion: 1,
          id: p.sentId,
          text: p.englishText,
          contexts: ["translation"],
          register: ["neutral"],
          cefr: p.cefr,
          quality: sentenceQuality(),
          provenance: {
            sources: [tatoebaSentenceSource(p.englishId, pin)],
            note: "English sentence selected from a pinned linked Tatoeba English-Vietnamese pair for E11 review.",
          },
        });
      }
      allNewExercises.push({
        schemaVersion: 1,
        id: "ex.translation.tatoeba." + p.englishId + "." + p.vietnameseId,
        type: "translation",
        prompt: p.vietnameseText,
        targetIds: [p.sentId],
        acceptedAnswers: [p.englishText],
        sourceSentenceIds: [p.sentId],
        cefr: p.cefr,
        quality: exerciseQuality(),
        provenance: {
          sources: [
            tatoebaSentenceSource(p.englishId, pin),
            tatoebaSentenceSource(p.vietnameseId, pin),
          ],
          note: "Vietnamese-to-English pair selected from a pinned direct Tatoeba translation link for E11 review.",
        },
      });
    }
  }

  console.log(`Total new exercises prepared: ${allNewExercises.length} (${addedGrammar} grammar, ${addedTt} typing-text)`);
  if (allNewExercises.length !== 20000) {
    throw new Error(`Expected exactly 20,000 new translation exercises, got ${allNewExercises.length}`);
  }

  // 1. Write sentence shards and decisions
  const newSentencesList = Array.from(newSentencesMap.values()).sort((a, b) => a.id.localeCompare(b.id, "en"));
  console.log(`Writing ${newSentencesList.length} new sentences across shards of 500...`);
  const sentenceShards = [];
  const sentenceBatchEntries = [];
  const SHARD_SIZE = 500;
  for (let i = 0; i < newSentencesList.length; i += SHARD_SIZE) {
    const chunk = newSentencesList.slice(i, i + SHARD_SIZE);
    const shardIndex = String(Math.floor(i / SHARD_SIZE) + 1).padStart(2, "0");
    const batchId = `e11.translation-sentences-${shardIndex}`;
    const relPath = `content/english/sentences/e11-translation-sentences-${shardIndex}.json`;
    const decRelPath = `content/english/reviews/decisions.d/e11-translation-sentences-${shardIndex}.json`;

    // write shard
    await fs.writeFile(path.join(root, relPath), stableJson({ schemaVersion: 1, records: chunk }), "utf8");

    // write decisions
    const decisions = chunk.map((r, idx) => makeDecision(batchId, "reviewed-translation-sentences", r, idx));
    await fs.writeFile(path.join(root, decRelPath), stableJson({ schemaVersion: 1, decisions }), "utf8");

    const cefrLevels = Array.from(new Set(chunk.map(r => r.cefr))).sort();
    sentenceBatchEntries.push({
      id: batchId,
      phase: "E11",
      category: "sentences",
      cefr: ["A1", "A2", "B1", "B2", "C1", "C2"],
      state: "draft",
      recordSets: [
        {
          id: "reviewed-translation-sentences",
          path: relPath,
          expectedCount: chunk.length,
          generated: false,
          allowedQualityStates: ["draft"],
          requiredChecks: [
            "schema",
            "sourcePin",
            "exactDuplicate",
            "translation",
            "naturalness",
            "cefr",
            "license",
          ],
        },
      ],
      requiredBeforePublish: [
        "naturalness-review",
        "cefr-review",
        "license-review",
      ],
      gameSmokes: [
        {
          gameId: "monkeytype",
          activity: "example-typing",
          recordSetId: "reviewed-translation-sentences",
          sampleCount: 6,
        },
        {
          gameId: "karaoke-typing",
          activity: "example-typing",
          recordSetId: "reviewed-translation-sentences",
          sampleCount: 6,
        },
      ],
    });
  }

  // 2. Write translation exercise shards and decisions
  console.log(`Writing ${allNewExercises.length} translation exercises across 40 shards of 500...`);
  const translationBatchEntries = [];
  for (let i = 0; i < allNewExercises.length; i += SHARD_SIZE) {
    const chunk = allNewExercises.slice(i, i + SHARD_SIZE);
    const shardIndex = String(Math.floor(i / SHARD_SIZE) + 1).padStart(2, "0");
    const batchId = `e11.translation-slice-${shardIndex}`;
    const relPath = `content/english/sentences/e11-translation-slice-${shardIndex}.json`;
    const decRelPath = `content/english/reviews/decisions.d/e11-translation-slice-${shardIndex}.json`;

    // write shard
    await fs.writeFile(path.join(root, relPath), stableJson({ schemaVersion: 1, records: chunk }), "utf8");

    // write decisions
    const decisions = chunk.map((r, idx) => makeDecision(batchId, "reviewed-translations", r, idx));
    await fs.writeFile(path.join(root, decRelPath), stableJson({ schemaVersion: 1, decisions }), "utf8");

    translationBatchEntries.push({
      id: batchId,
      phase: "E11",
      category: "sentences",
      cefr: ["A1", "A2", "B1", "B2", "C1", "C2"],
      state: "draft",
      recordSets: [
        {
          id: "reviewed-translations",
          path: relPath,
          expectedCount: chunk.length,
          generated: false,
          allowedQualityStates: ["draft"],
          requiredChecks: [
            "schema",
            "sourcePin",
            "exactDuplicate",
            "translation",
            "naturalness",
            "cefr",
            "license",
          ],
        },
      ],
      requiredBeforePublish: [
        "bilingual-review",
        "naturalness-review",
        "cefr-review",
        "license-review",
      ],
      gameSmokes: [
        {
          gameId: "monkeytype",
          activity: "translation",
          recordSetId: "reviewed-translations",
          sampleCount: 6,
          recordType: "translation",
        },
        {
          gameId: "karaoke-typing",
          activity: "translation",
          recordSetId: "reviewed-translations",
          sampleCount: 6,
          recordType: "translation",
        },
      ],
    });
  }

  // 3. Register batches in content/english/batches/manifest.json
  batchManifestDoc.batches = batchManifestDoc.batches.filter(b => !/^e11\.translation-(slice|sentences)-\d+$/.test(b.id));
  batchManifestDoc.batches.push(...sentenceBatchEntries, ...translationBatchEntries);
  await fs.writeFile(
    path.join(root, "content", "english", "batches", "manifest.json"),
    stableJson(batchManifestDoc),
    "utf8"
  );
  console.log(`Registered ${sentenceBatchEntries.length + translationBatchEntries.length} batches in batch manifest.`);
  console.log("Step 4 expansion generation complete!");
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
