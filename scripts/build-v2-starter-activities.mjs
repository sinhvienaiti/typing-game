import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createSchemaValidator, readJson } from "./english-content-core.mjs";
import { englishContentReviewSourceDigest } from "./english-review-core.mjs";

/**
 * Non-destructive validator for curated Mục 3 & Mục 4 v2 starter exercises.
 * Content in content/english/sentences/v2-*.json and reviews/decisions.d/v2-*.json
 * is hand-curated and must never be overwritten by a build script.
 */
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

const DATASETS = [
  {
    batchId: "e11.v2-starter-building",
    exercisePath: "content/english/sentences/v2-starter-building-exercises.json",
    decisionPath: "content/english/reviews/decisions.d/v2-starter-building.json",
    expectedCount: 2500,
    expectedType: "sentence-building",
  },
  {
    batchId: "e11.v2-starter-contextual",
    exercisePath: "content/english/sentences/v2-starter-contextual-exercises.json",
    decisionPath: "content/english/reviews/decisions.d/v2-starter-contextual.json",
    expectedCount: 1200,
    expectedType: "contextual-usage",
  },
  {
    batchId: "e11.v2-e16-contrast",
    exercisePath: "content/english/sentences/v2-e16-contrast-exercises.json",
    decisionPath: "content/english/reviews/decisions.d/v2-e16-contrast.json",
    expectedCount: 800,
    expectedType: "contextual-usage",
  },
  {
    batchId: "e11.v2-starter-listening",
    exercisePath: "content/english/sentences/v2-starter-listening-exercises.json",
    decisionPath: "content/english/reviews/decisions.d/v2-starter-listening.json",
    expectedCount: 1000,
    expectedType: "listening-typing",
  },
];

async function loadSchemas() {
  const schemaDir = path.join(ROOT, "shared", "schemas", "english-content");
  const schemaNames = (await fs.readdir(schemaDir))
    .filter((name) => name.endsWith(".schema.json"))
    .sort((a, b) => a.localeCompare(b, "en"));
  const schemas = await Promise.all(schemaNames.map((name) => readJson(path.join(schemaDir, name))));
  const byName = new Map(schemaNames.map((name, index) => [name, schemas[index]]));
  return { byName, validator: createSchemaValidator(schemas) };
}

function validateRecordContent(spec, record, errors) {
  if (record.type !== spec.expectedType) {
    errors.push(`${spec.exercisePath} ${record.id}: expected type "${spec.expectedType}", got "${record.type}"`);
  }
  const prompt = typeof record.prompt === "string" ? record.prompt.trim() : "";
  if (!prompt) {
    errors.push(`${spec.exercisePath} ${record.id}: prompt must be non-empty`);
    return;
  }
  if (prompt.startsWith("Dịch sang tiếng Anh:")) {
    errors.push(`${spec.exercisePath} ${record.id}: placeholder Vietnamese translation prefix found`);
  }
  if (!Array.isArray(record.acceptedAnswers) || record.acceptedAnswers.length === 0) {
    errors.push(`${spec.exercisePath} ${record.id}: acceptedAnswers must contain at least one answer`);
  } else if (record.acceptedAnswers.some((answer) => typeof answer !== "string" || answer.trim() === "")) {
    errors.push(`${spec.exercisePath} ${record.id}: acceptedAnswers contains blank entry`);
  }

  if (spec.expectedType === "contextual-usage" && !prompt.includes("___")) {
    errors.push(`${spec.exercisePath} ${record.id}: contextual-usage prompt missing "___" blank`);
  }
  if (spec.expectedType === "sentence-building") {
    const colonIndex = prompt.indexOf(":");
    const tail = colonIndex >= 0 ? prompt.slice(colonIndex + 1).trim() : prompt;
    if (tail.split(/\s+/).filter(Boolean).length < 2) {
      errors.push(`${spec.exercisePath} ${record.id}: sentence-building prompt has too few tokens`);
    }
  }
}

async function main() {
  const { byName, validator } = await loadSchemas();
  const exerciseSetSchema = byName.get("exercise-set.schema.json");
  const reviewLedgerSchema = byName.get("review-ledger.schema.json");
  const batchManifestSchema = byName.get("batch-manifest.schema.json");
  const manifest = await readJson(path.join(ROOT, "content/english/batches/manifest.json"));

  const errors = [];
  for (const problem of validator.validate(manifest, batchManifestSchema)) {
    errors.push(`content/english/batches/manifest.json ${problem}`);
  }

  const globalRecordIds = new Set();
  const globalDecisionIds = new Set();
  const summary = [];

  for (const spec of DATASETS) {
    const exerciseSet = await readJson(path.join(ROOT, spec.exercisePath));
    const ledger = await readJson(path.join(ROOT, spec.decisionPath));

    for (const problem of validator.validate(exerciseSet, exerciseSetSchema)) {
      errors.push(`${spec.exercisePath} ${problem}`);
    }
    for (const problem of validator.validate(ledger, reviewLedgerSchema)) {
      errors.push(`${spec.decisionPath} ${problem}`);
    }

    const batch = (manifest.batches ?? []).find((entry) => entry.id === spec.batchId);
    const recordSet = batch?.recordSets?.find((entry) => entry.id === "exercises");
    if (!batch || !recordSet) {
      errors.push(`manifest missing batch/recordSet for ${spec.batchId}`);
    } else {
      if (recordSet.path !== spec.exercisePath) {
        errors.push(`manifest ${spec.batchId}: path mismatch (${recordSet.path} !== ${spec.exercisePath})`);
      }
      if (recordSet.expectedCount !== spec.expectedCount) {
        errors.push(`manifest ${spec.batchId}: expectedCount mismatch (${recordSet.expectedCount} !== ${spec.expectedCount})`);
      }
    }

    const records = exerciseSet.records ?? [];
    const decisions = ledger.decisions ?? [];
    if (records.length !== spec.expectedCount) {
      errors.push(`${spec.exercisePath}: expected ${spec.expectedCount} records, got ${records.length}`);
    }
    if (decisions.length !== spec.expectedCount) {
      errors.push(`${spec.decisionPath}: expected ${spec.expectedCount} decisions, got ${decisions.length}`);
    }

    const decisionByRecordId = new Map();
    for (const decision of decisions) {
      if (globalDecisionIds.has(decision.id)) {
        errors.push(`${spec.decisionPath}: duplicate decision id ${decision.id}`);
      }
      globalDecisionIds.add(decision.id);
      if (decisionByRecordId.has(decision.recordId)) {
        errors.push(`${spec.decisionPath}: duplicate decision for recordId ${decision.recordId}`);
      }
      decisionByRecordId.set(decision.recordId, decision);
    }

    for (const record of records) {
      if (globalRecordIds.has(record.id)) {
        errors.push(`${spec.exercisePath}: duplicate record id ${record.id}`);
      }
      globalRecordIds.add(record.id);
      validateRecordContent(spec, record, errors);

      const decision = decisionByRecordId.get(record.id);
      if (!decision) {
        errors.push(`${spec.decisionPath}: missing decision for ${record.id}`);
        continue;
      }
      if (decision.batchId !== spec.batchId || decision.recordSetId !== "exercises") {
        errors.push(`${spec.decisionPath} ${decision.id}: batch/recordSet mismatch`);
      }
      if (decision.targetState !== "published") {
        errors.push(`${spec.decisionPath} ${decision.id}: expected targetState="published", got "${decision.targetState}"`);
      }
      const expectedDigest = englishContentReviewSourceDigest(record);
      if (decision.sourceDigest !== expectedDigest) {
        errors.push(`${spec.decisionPath} ${decision.id}: stale sourceDigest (expected ${expectedDigest}, got ${decision.sourceDigest})`);
      }
    }

    summary.push({
      batchId: spec.batchId,
      records: records.length,
      decisions: decisions.length,
      type: spec.expectedType,
    });
  }

  if (errors.length > 0) {
    console.error(`v2 starter activities validation FAILED (${errors.length} issue(s)):`);
    for (const err of errors.slice(0, 25)) console.error(` - ${err}`);
    process.exit(1);
  }

  console.log(JSON.stringify({ status: "validated-only", totalRecords: globalRecordIds.size, datasets: summary }, null, 2));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
