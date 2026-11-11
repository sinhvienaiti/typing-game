import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { CEFR_LEVELS, readJson } from "./english-content-core.mjs";
import { englishContentReviewSourceDigest } from "./english-review-core.mjs";

/**
 * Non-destructive validator for E11 cloze exercise slices and review digests.
 * content/english/sentences/e11-cloze-slice-*.json,
 * content/english/reviews/decisions.d/e11-cloze-slice-*.json, and
 * content/english/batches/manifest.json are hand-reviewed and must never
 * be overwritten by a script.
 */
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const SENTENCES_DIR = path.join(ROOT, "content", "english", "sentences");
const DECISIONS_DIR = path.join(ROOT, "content", "english", "reviews", "decisions.d");
const SHARD_COUNT = 100;
const SHARD_SIZE = 500;
const VALID_CEFR = new Set(CEFR_LEVELS);

/**
 * Validates structural and editorial invariants for a single E11 cloze record.
 */
function validateClozeRecord(record, shardNo, topicIds, seenIds, seenPrompts, errors, label) {
  if (record.schemaVersion !== 1 || record.type !== "cloze") {
    errors.push(`${label} ${record.id}: expected schemaVersion=1 and type="cloze"`);
  }
  const expectedPrefix = `ex.cloze.e11.${shardNo}.`;
  if (typeof record.id !== "string" || !record.id.startsWith(expectedPrefix)) {
    errors.push(`${label} ${record.id}: invalid ID prefix (expected ${expectedPrefix}*)`);
  }
  if (seenIds.has(record.id)) {
    errors.push(`${label} ${record.id}: duplicate cloze record ID`);
  }
  seenIds.add(record.id);

  const prompt = typeof record.prompt === "string" ? record.prompt : "";
  const blankMatches = prompt.match(/___/g) ?? [];
  if (!prompt.trim() || prompt.trim() !== prompt || blankMatches.length !== 1) {
    errors.push(`${label} ${record.id}: prompt must be trimmed and contain exactly one ___ blank`);
  }
  if (seenPrompts.has(prompt)) {
    errors.push(`${label} ${record.id}: duplicate E11 cloze prompt ${JSON.stringify(prompt)}`);
  }
  seenPrompts.add(prompt);

  if (!VALID_CEFR.has(record.cefr)) {
    errors.push(`${label} ${record.id}: invalid CEFR ${JSON.stringify(record.cefr)}`);
  }
  if (record.quality?.state !== "draft") {
    errors.push(`${label} ${record.id}: quality.state must remain "draft" (overlay publication only)`);
  }
  if (!Array.isArray(record.targetIds) || record.targetIds.length === 0) {
    errors.push(`${label} ${record.id}: targetIds must be a non-empty array`);
  } else if (record.targetIds.some((id) => !topicIds.has(id))) {
    errors.push(`${label} ${record.id}: unknown targetId in ${JSON.stringify(record.targetIds)}`);
  }

  if (!Array.isArray(record.acceptedAnswers) || record.acceptedAnswers.length === 0) {
    errors.push(`${label} ${record.id}: acceptedAnswers must be a non-empty array`);
  } else {
    const seenAnswers = new Set();
    for (const answer of record.acceptedAnswers) {
      if (typeof answer !== "string" || answer.trim() !== answer || !answer || answer.includes("___")) {
        errors.push(`${label} ${record.id}: malformed acceptedAnswer ${JSON.stringify(answer)}`);
        continue;
      }
      if (seenAnswers.has(answer)) {
        errors.push(`${label} ${record.id}: duplicate acceptedAnswer ${JSON.stringify(answer)}`);
      }
      seenAnswers.add(answer);
    }
  }

  if (!Array.isArray(record.sourceSentenceIds) || record.sourceSentenceIds.some((id) => !/^sent\./.test(String(id)))) {
    errors.push(`${label} ${record.id}: malformed sourceSentenceIds`);
  }
  if (!Array.isArray(record.provenance?.sources) || record.provenance.sources.length === 0) {
    errors.push(`${label} ${record.id}: missing provenance.sources`);
  }
}

async function main() {
  const [catalog, batchManifest, sentenceEntries] = await Promise.all([
    readJson(path.join(ROOT, "shared", "curriculum", "topic-catalog.json")),
    readJson(path.join(ROOT, "content", "english", "batches", "manifest.json")),
    fs.readdir(SENTENCES_DIR),
  ]);

  const topicIds = new Set((catalog.topics ?? []).map((topic) => topic.id));
  const batchById = new Map((batchManifest.batches ?? []).map((batch) => [batch.id, batch]));
  const sliceFiles = sentenceEntries
    .filter((file) => /^e11-cloze-slice-\d+\.json$/.test(file))
    .sort((a, b) => a.localeCompare(b, "en"));

  const errors = [];
  if (sliceFiles.length !== SHARD_COUNT) {
    errors.push(`Expected ${SHARD_COUNT} E11 cloze slice files, found ${sliceFiles.length}`);
  }

  const seenIds = new Set();
  const seenPrompts = new Set();
  let totalRecords = 0;

  for (const file of sliceFiles) {
    const shardMatch = /^e11-cloze-slice-(\d+)\.json$/.exec(file);
    const shardNo = shardMatch[1];
    const batchId = `e11.cloze-slice-${shardNo}`;
    const batch = batchById.get(batchId);
    const clozeSet = batch?.recordSets?.find((rs) => rs.id === "cloze");
    if (!batch || !clozeSet || clozeSet.expectedCount !== SHARD_SIZE) {
      errors.push(`${file}: missing or invalid manifest batch registration for ${batchId}`);
    }

    const [doc, dec] = await Promise.all([
      readJson(path.join(SENTENCES_DIR, file)),
      readJson(path.join(DECISIONS_DIR, file)),
    ]);

    const records = doc.records ?? [];
    if (records.length !== SHARD_SIZE) {
      errors.push(`${file}: expected ${SHARD_SIZE} records, found ${records.length}`);
    }

    const decisionById = new Map((dec.decisions ?? []).map((d) => [d.recordId, d]));
    for (const record of records) {
      totalRecords++;
      validateClozeRecord(record, shardNo, topicIds, seenIds, seenPrompts, errors, file);

      const decision = decisionById.get(record.id);
      if (!decision) {
        errors.push(`${file} ${record.id}: missing decision entry in decisions.d/${file}`);
        continue;
      }
      if (decision.batchId !== batchId || decision.recordSetId !== "cloze" || decision.targetState !== "published") {
        errors.push(`${file} ${record.id}: invalid decision metadata in decisions.d/${file}`);
      }
      const expectedDigest = englishContentReviewSourceDigest(record);
      if (decision.sourceDigest !== expectedDigest) {
        errors.push(`${file} ${record.id}: sourceDigest mismatch (${decision.sourceDigest} !== ${expectedDigest})`);
      }
    }
  }

  if (errors.length > 0) {
    for (const err of errors.slice(0, 50)) {
      console.error(`ERROR: ${err}`);
    }
    console.error(`Validation failed with ${errors.length} error(s) across ${sliceFiles.length} E11 cloze slices.`);
    process.exitCode = 1;
    return;
  }

  console.log(
    JSON.stringify({
      status: "ok",
      slices: sliceFiles.length,
      totalRecords,
    }),
  );
}

main().catch((err) => {
  console.error(err);
  process.exitCode = 1;
});
