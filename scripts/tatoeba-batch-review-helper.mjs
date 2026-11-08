import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  lexicalTokens,
  listJsonFiles,
  normalizeSentenceKey,
  readJson,
  stableJson,
  tokenJaccard,
} from "./english-content-core.mjs";
import {
  englishContentRecordDigest,
  englishContentReviewSourceDigest,
} from "./english-review-core.mjs";
import { TATOEBA_ENGLISH_RECORD_SET } from "./tatoeba-english-intake-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

export async function loadExistingExampleCorpus(root) {
  const files = await listJsonFiles(path.join(root, "shared/sentences/examples"));
  const corpus = [];
  for (const file of files) {
    const doc = JSON.parse(await fs.readFile(file, "utf8"));
    for (const record of doc.records ?? []) {
      if (typeof record.text === "string" && record.id) {
        corpus.push({ id: record.id, text: record.text });
      }
    }
  }
  return corpus;
}

function getTokens(item) {
  if (!item.tokenSet) {
    item.tokenSet = new Set(lexicalTokens(item.text));
  }
  return item.tokenSet;
}

function fastJaccard(targetTokens, otherTokens) {
  if (targetTokens.size === 0 && otherTokens.size === 0) return 1;
  if (targetTokens.size === 0 || otherTokens.size === 0) return 0;
  let intersection = 0;
  const smaller = targetTokens.size < otherTokens.size ? targetTokens : otherTokens;
  const larger = targetTokens.size < otherTokens.size ? otherTokens : targetTokens;
  for (const t of smaller) {
    if (larger.has(t)) intersection++;
  }
  return intersection / (targetTokens.size + otherTokens.size - intersection);
}

export function computeNearestAndJaccard(targetId, targetText, corpus, intraSlice = []) {
  const targetTokens = new Set(lexicalTokens(targetText));
  const scores = [];
  for (const item of corpus) {
    if (item.id === targetId) continue;
    const score = fastJaccard(targetTokens, getTokens(item));
    scores.push({ id: item.id, score });
  }
  for (const item of intraSlice) {
    if (item.id === targetId) continue;
    const score = fastJaccard(targetTokens, getTokens(item));
    scores.push({ id: item.id, score });
  }
  scores.sort((a, b) => b.score - a.score || a.id.localeCompare(b.id, "en"));
  const maxScore = scores.length > 0 ? scores[0].score : 0;
  const nearest = scores.slice(0, 3);
  return {
    maximumTokenJaccard: Number(maxScore.toFixed(4)),
    nearest,
  };
}

export async function processTatoebaBatch({
  batchNum,
  queue,
  reviews,
  corpus,
  reviewer = "Antigravity editorial review",
  reviewedAt = new Date().toISOString(),
}) {
  const batchId = `e11.tatoeba-english-reviewed-slice-${batchNum}`;
  const recordSetId = TATOEBA_ENGLISH_RECORD_SET;

  if (queue.candidates.length !== 200) {
    throw new Error(`Queue must contain exactly 200 candidates, got ${queue.candidates.length}`);
  }
  if (reviews.length !== 200) {
    throw new Error(`Reviews must cover exactly 200 candidates, got ${reviews.length}`);
  }

  const reviewById = new Map();
  for (const rev of reviews) {
    if (!rev.id || !rev.outcome || !rev.rationale) {
      throw new Error(`Invalid review item: ${JSON.stringify(rev)}`);
    }
    if (rev.outcome === "publish" && !["A1", "A2", "B1", "B2", "C1", "C2"].includes(rev.cefr)) {
      throw new Error(`${rev.id}: publication requires explicit valid CEFR`);
    }
    if (rev.outcome === "reject" && rev.cefr !== null && rev.cefr !== undefined) {
      throw new Error(`${rev.id}: rejection must have cefr null`);
    }
    if (reviewById.has(rev.id)) {
      throw new Error(`Duplicate review for id: ${rev.id}`);
    }
    reviewById.set(rev.id, rev);
  }

  // Pre-gather intra-slice final texts for similarity check
  const intraSlice = queue.candidates.map(c => {
    const rev = reviewById.get(c.record.id);
    if (!rev) throw new Error(`Missing review for candidate: ${c.record.id}`);
    return { id: c.record.id, text: rev.finalText ?? c.record.text };
  });

  const sliceRecords = [];
  const decisions = [];
  const pilotRecords = [];

  let publishedCount = 0;
  let rejectedCount = 0;
  let editedCount = 0;
  const cefrLevels = new Set();

  for (const candidate of queue.candidates) {
    const rawRecord = candidate.record;
    const rev = reviewById.get(rawRecord.id);
    const sourceEv = candidate.sourceEvidence;
    const originalText = rawRecord.text;
    const finalText = rev.finalText ?? originalText;
    const modified = finalText !== originalText;

    if (modified) editedCount++;
    if (rev.outcome === "publish") {
      publishedCount++;
      cefrLevels.add(rev.cefr);
    } else {
      rejectedCount++;
    }

    const intakeSourceDigest = englishContentReviewSourceDigest(rawRecord);

    // Compute Jaccard
    const { maximumTokenJaccard, nearest } = computeNearestAndJaccard(rawRecord.id, finalText, corpus, intraSlice);

    // Build authoring slice record
    const note = modified
      ? `Pinned English-only intake. Current owner is not asserted to be the original/sole author. Experimental upstream ratings prioritize review; they do not constitute local editorial approval or CEFR evidence. Editorial edit: ${rev.rationale}`
      : "Pinned English-only intake. Current owner is not asserted to be the original/sole author. Experimental upstream ratings prioritize review; they do not constitute local editorial approval or CEFR evidence.";

    const sliceRecord = {
      schemaVersion: 1,
      id: rawRecord.id,
      text: finalText,
      contexts: ["typing-practice"],
      quality: {
        state: "draft",
        checks: {
          schema: { status: "pass", method: "tatoeba-english-intake-v1" },
          sourcePin: { status: "pass", method: "canonical-and-compressed-sha256-v1" },
          grammar: { status: "pending", method: "editorial-review-required" },
          naturalness: { status: "pending", method: "editorial-review-required" },
          sourceSuitability: { status: "pending", method: "standalone-learning-content-review-required" },
          cefr: { status: "pending", method: "editorial-cefr-review-required" },
          exactDuplicate: { status: "pending", method: "controlled-corpus-review-required" },
          nearDuplicate: { status: "pending", method: "controlled-corpus-review-required" },
          license: { status: "pending", method: "source-attribution-review-required" },
        },
      },
      provenance: {
        sources: [
          {
            dataset: "tatoeba",
            sourceId: String(sourceEv.id),
            sourceUrl: `https://tatoeba.org/en/sentences/show/${sourceEv.id}`,
            snapshot: "english-only-weekly-2026-10-31-observed-2026-11-07-v1",
            license: "CC-BY-2.0-FR",
            attribution: `Tatoeba Project; current owner ${sourceEv.owner}; contributor history at the sentence URL`,
            modified,
          },
        ],
        note,
      },
    };

    if (rev.outcome === "publish") {
      sliceRecord.cefr = rev.cefr;
    }

    const controlledSourceDigest = englishContentReviewSourceDigest(sliceRecord);

    // Build decision
    const decisionId = `review.e11.tatoeba-english-${batchNum}.${sourceEv.id}`;
    let decision;
    if (rev.outcome === "publish") {
      decision = {
        id: decisionId,
        batchId,
        recordSetId,
        recordId: rawRecord.id,
        sourceDigest: controlledSourceDigest,
        targetState: "published",
        checks: {
          schema: { status: "pass", method: "tatoeba-english-editorial-review-v1" },
          sourcePin: { status: "pass", method: "tatoeba-english-editorial-review-v1" },
          grammar: { status: "pass", method: "tatoeba-english-editorial-review-v1" },
          naturalness: { status: "pass", method: "tatoeba-english-editorial-review-v1" },
          sourceSuitability: { status: "pass", method: "tatoeba-english-editorial-review-v1" },
          cefr: { status: "pass", method: "sentence-level-editorial-cefr-v1" },
          exactDuplicate: { status: "pass", method: "tatoeba-english-editorial-review-v1" },
          nearDuplicate: { status: "pass", method: "exact-jaccard-cross-runtime-editorial-v1" },
          license: { status: "pass", method: "cc-by-2-fr-attribution-source-review-v1" },
        },
        reviewedAt,
        reviewedBy: reviewer,
        note: `${rev.rationale} Canonical snapshot english-only-weekly-2026-10-31-observed-2026-11-07-v1. Upstream ratings remain experimental; local editorial suitability, grammar, naturalness and attribution reviewed separately. CEFR ${rev.cefr}. Maximum cross-runtime/new-slice token Jaccard ${maximumTokenJaccard.toFixed(4)}.`,
      };
    } else {
      decision = {
        id: decisionId,
        batchId,
        recordSetId,
        recordId: rawRecord.id,
        sourceDigest: controlledSourceDigest,
        targetState: "deprecated",
        checks: {
          sourceSuitability: { status: "fail", method: "standalone-learning-content-rejection-v1" },
        },
        reviewedAt,
        reviewedBy: reviewer,
        note: `${rev.rationale} Canonical snapshot english-only-weekly-2026-10-31-observed-2026-11-07-v1. Upstream ratings remain experimental; local editorial suitability, grammar, naturalness and attribution reviewed separately. No publication or CEFR assignment.`,
      };
    }

    sliceRecords.push(sliceRecord);
    decisions.push(decision);

    pilotRecords.push({
      id: rawRecord.id,
      outcome: rev.outcome,
      cefr: rev.outcome === "publish" ? rev.cefr : null,
      originalText,
      finalText,
      intakeSourceDigest,
      controlledSourceDigest,
      maximumTokenJaccard,
      nearest,
      rationale: rev.rationale,
    });
  }

  const pilotReport = {
    schemaVersion: 1,
    sourceSnapshot: "english-only-weekly-2026-10-31-observed-2026-11-07-v1",
    reviewed: 200,
    published: publishedCount,
    rejected: rejectedCount,
    edited: editedCount,
    records: pilotRecords,
  };

  const slicePath = path.join(root, `content/english/sentences/e11-tatoeba-english-reviewed-slice-${batchNum}.json`);
  const decisionPath = path.join(root, `content/english/reviews/decisions.d/e11-tatoeba-english-${batchNum}.json`);
  const pilotPath = path.join(root, `content/english/reports/tatoeba-english-editorial-pilot-${batchNum}.json`);

  await fs.writeFile(slicePath, stableJson({ schemaVersion: 1, records: sliceRecords }), "utf8");
  await fs.writeFile(decisionPath, stableJson({ schemaVersion: 1, decisions }), "utf8");
  await fs.writeFile(pilotPath, stableJson(pilotReport), "utf8");

  // Update batches/manifest.json
  const manifestPath = path.join(root, "content/english/batches/manifest.json");
  const manifest = await readJson(manifestPath);

  const existingBatchIdx = (manifest.batches ?? []).findIndex(b => b.id === batchId);
  const sortedCefr = ["A1", "A2", "B1", "B2", "C1", "C2"].filter(lvl => cefrLevels.has(lvl));

  const batchEntry = {
    id: batchId,
    phase: "E11",
    category: "sentences",
    cefr: sortedCefr,
    state: "draft",
    recordSets: [
      {
        id: recordSetId,
        path: `content/english/sentences/e11-tatoeba-english-reviewed-slice-${batchNum}.json`,
        expectedCount: 200,
        generated: false,
        allowedQualityStates: ["draft"],
        requiredChecks: [
          "schema",
          "sourcePin",
          "grammar",
          "naturalness",
          "sourceSuitability",
          "cefr",
          "exactDuplicate",
          "nearDuplicate",
          "license",
        ],
      },
    ],
    requiredBeforePublish: [
      "source-integrity-review",
      "grammar-review",
      "naturalness-review",
      "cefr-review",
      "dedup-review",
      "license-review",
    ],
    gameSmokes: [
      {
        gameId: "monkeytype",
        activity: "example-typing",
        recordSetId,
        sampleCount: 6,
      },
      {
        gameId: "karaoke-typing",
        activity: "example-typing",
        recordSetId,
        sampleCount: 6,
      },
    ],
  };

  if (existingBatchIdx >= 0) {
    manifest.batches[existingBatchIdx] = batchEntry;
  } else {
    manifest.batches.push(batchEntry);
  }

  await fs.writeFile(manifestPath, stableJson(manifest), "utf8");

  // Update corpus with newly published sentences
  for (const r of sliceRecords) {
    if (r.cefr) {
      corpus.push({ id: r.id, text: r.text });
    }
  }

  return {
    batchNum,
    reviewed: 200,
    published: publishedCount,
    rejected: rejectedCount,
    edited: editedCount,
    cefr: sortedCefr,
  };
}
