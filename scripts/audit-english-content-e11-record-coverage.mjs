import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson } from "./english-content-core.mjs";
import {
  overlayEnglishReviewDecisions,
  readEnglishReviewLedger,
} from "./english-review-core.mjs";
import { readE11TypingTextReviewShards } from "./english-typing-text-shards.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

const [targetDoc, batchManifest, reviewLedger, readiness] = await Promise.all([
  readJson(path.join(root, "content", "english", "targets", "long-term.json")),
  readJson(path.join(root, "content", "english", "batches", "manifest.json")),
  readEnglishReviewLedger(root),
  readJson(path.join(root, "content", "english", "reports", "e11-readiness.json")),
]);

const batchSetsByPath = new Map();
for (const batch of batchManifest.batches ?? []) {
  for (const set of batch.recordSets ?? []) {
    batchSetsByPath.set(set.path, {
      batchId: batch.id,
      recordSetId: set.id,
      requiredChecks: set.requiredChecks ?? [],
    });
  }
}
const reviewedTypingTextPath = "content/english/sentences/e06-reviewed-typing-text-sentences.json";
const reviewedTypingTextContext = batchSetsByPath.get(reviewedTypingTextPath);
const e11TypingTextReviewShards = await readE11TypingTextReviewShards(root);
if (e11TypingTextReviewShards.length > 0 && reviewedTypingTextContext === undefined) {
  throw new TypeError(`${reviewedTypingTextPath}: missing manifest record-set context`);
}
for (const shard of e11TypingTextReviewShards) {
  batchSetsByPath.set(shard.relativePath, reviewedTypingTextContext);
}

const PUBLISHABLE_SENTENCE_TARGETS = new Set([
  "common-mistakes",
  "example-sentences",
  "translation-pairs",
  "cloze-exercises",
  "sentence-transformations",
  "dialogue-examples",
]);

function requireCondition(condition, message) {
  if (!condition) throw new Error(message);
}

function recordId(record, label) {
  const value = record?.id ?? record?.lexemeId;
  requireCondition(
    typeof value === "string" && value.trim() !== "",
    `${label}: record is missing a stable id/lexemeId`,
  );
  return value;
}

function selectCollection(doc, source) {
  const values = doc?.[source.collection];
  requireCondition(
    Array.isArray(values),
    `${source.path} does not contain ${source.collection}[]`,
  );
  if (source.filterField === undefined) return values;
  const wanted = new Set(source.filterValues ?? []);
  return values.filter((item) => wanted.has(String(item?.[source.filterField])));
}

function publishable(records, label) {
  const result = [];
  for (const record of records) {
    if (record?.quality?.state !== "published") continue;
    const checks = Object.values(record?.quality?.checks ?? {});
    const unfinished = checks.find(
      (check) => check?.status === "pending" || check?.status === "fail",
    );
    requireCondition(
      !unfinished,
      `${label}: published record ${String(record?.id ?? record?.lexemeId ?? "<unknown>")} has unfinished quality checks`,
    );
    result.push(record);
  }
  return result;
}

function selectTargetRecords(doc, source, targetId) {
  if (!PUBLISHABLE_SENTENCE_TARGETS.has(targetId) || source.collection !== "records") {
    return selectCollection(doc, source);
  }

  requireCondition(Array.isArray(doc?.records), `${source.path} does not contain records[]`);
  const context = batchSetsByPath.get(source.path);
  const reviewed =
    context === undefined
      ? doc.records
      : overlayEnglishReviewDecisions(doc.records, reviewLedger, context);
  const eligible = publishable(reviewed, `${targetId} @ ${source.path}`);

  if (source.filterField === undefined) return eligible;
  const wanted = new Set(source.filterValues ?? []);
  return eligible.filter((item) => wanted.has(String(item?.[source.filterField])));
}

function sourceKey(source) {
  return [
    source.path,
    source.collection,
    source.filterField ?? "",
    [...(source.filterValues ?? [])]
      .sort((a, b) => String(a).localeCompare(String(b), "en"))
      .join("\u0000"),
  ].join("\u0001");
}

function manifestSources(targetId) {
  const sources = [];
  for (const batch of batchManifest.batches ?? []) {
    for (const set of batch.recordSets ?? []) {
      const setId = String(set?.id ?? "");
      const relative = String(set?.path ?? "");
      if (!relative) continue;

      if (batch?.phase === "E04" && batch?.category === "phrases") {
        if (targetId === "collocations" && (setId === "collocations" || setId === "scale-collocations")) {
          sources.push({ path: relative, collection: "records" });
        } else if (targetId === "verb-patterns" && (setId === "verb-patterns" || setId === "scale-verb-patterns")) {
          sources.push({ path: relative, collection: "records" });
        } else if (targetId === "phrasal-verbs" && (setId === "phrases" || setId === "scale-phrases")) {
          sources.push({
            path: relative,
            collection: "records",
            filterField: "type",
            filterValues: ["phrasal-verb"],
          });
        } else if (targetId === "idioms-chunks" && (setId === "phrases" || setId === "scale-phrases")) {
          sources.push({
            path: relative,
            collection: "records",
            filterField: "type",
            filterValues: ["idiom", "chunk"],
          });
        }
        continue;
      }

      if (
        targetId === "example-sentences" &&
        batch?.phase === "E03" &&
        batch?.category === "dictionary" &&
        setId === "reviewed-examples"
      ) {
        sources.push({ path: relative, collection: "records" });
        continue;
      }

      if (batch?.phase === "E05" && batch?.category === "grammar") {
        const isExerciseSet = setId === "exercises" || setId === "pilot-exercises";
        if (targetId === "example-sentences" && setId === "examples") {
          sources.push({ path: relative, collection: "records" });
        } else if (targetId === "translation-pairs" && isExerciseSet) {
          sources.push({
            path: relative,
            collection: "records",
            filterField: "type",
            filterValues: ["translation"],
          });
        } else if (targetId === "cloze-exercises" && isExerciseSet) {
          sources.push({
            path: relative,
            collection: "records",
            filterField: "type",
            filterValues: ["cloze"],
          });
        } else if (targetId === "common-mistakes" && setId === "common-mistakes") {
          sources.push({ path: relative, collection: "records" });
        }
      }
    }
  }
  return sources;
}

function sourcesForTarget(target) {
  const merged = [...(target.sources ?? []), ...manifestSources(target.id)];
  if (target.id === "example-sentences") {
    merged.push(...e11TypingTextReviewShards.map((shard) => ({
      path: shard.relativePath,
      collection: "records",
    })));
  }
  const seen = new Set();
  return merged.filter((source) => {
    const key = sourceKey(source);
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });
}

async function loadExpectedTargetIds(target) {
  const identities = new Map();
  for (const source of sourcesForTarget(target)) {
    const doc = await readJson(path.join(root, source.path));
    const records = selectTargetRecords(doc, source, target.id);
    for (const record of records) {
      const id = recordId(record, `${target.id} @ ${source.path}`);
      identities.set(`${id}\u0000${source.path}`, id);
    }
  }
  return [...identities.values()];
}

async function loadRuntimeGroups(baseDir, allowedGroups) {
  const manifest = await readJson(path.join(root, baseDir, "manifest.json"));
  const groups = Object.fromEntries(allowedGroups.map((group) => [group, []]));
  let loaded = 0;

  for (const shard of manifest.shards ?? []) {
    const relative = path.join(baseDir, String(shard.path));
    const doc = await readJson(path.join(root, relative));
    requireCondition(Array.isArray(doc.records), `${relative} must contain records[]`);
    requireCondition(
      doc.records.length === shard.count,
      `${relative}: manifest count ${String(shard.count)} does not match records[] length ${String(doc.records.length)}`,
    );
    const group = String(shard.path).split("/")[0];
    requireCondition(Array.isArray(groups[group]), `${relative}: unsupported runtime group ${group}`);
    for (const record of doc.records) {
      requireCondition(
        record?.quality?.state === "published",
        `${relative}: runtime contains non-published record ${String(record?.id ?? record?.lexemeId ?? "<unknown>")}`,
      );
    }
    groups[group].push(...doc.records);
    loaded += doc.records.length;
  }

  requireCondition(
    loaded === manifest.count,
    `${baseDir}/manifest.json count ${String(manifest.count)} does not match loaded runtime count ${String(loaded)}`,
  );
  return groups;
}

function filterType(records, values) {
  const wanted = new Set(values);
  return records.filter((record) => wanted.has(String(record?.type)));
}

function toIdMultiset(records, label) {
  const counts = new Map();
  for (const record of records) {
    const id = typeof record === "string" ? record : recordId(record, label);
    counts.set(id, (counts.get(id) ?? 0) + 1);
  }
  return counts;
}

function compareMultisets(expected, actual) {
  const keys = new Set([...expected.keys(), ...actual.keys()]);
  const missing = [];
  const extra = [];
  for (const id of [...keys].sort((a, b) => a.localeCompare(b, "en"))) {
    const expectedCount = expected.get(id) ?? 0;
    const actualCount = actual.get(id) ?? 0;
    if (actualCount < expectedCount) {
      missing.push({ id, count: expectedCount - actualCount });
    } else if (actualCount > expectedCount) {
      extra.push({ id, count: actualCount - expectedCount });
    }
  }
  return { missing, extra };
}

const [grammar, phrases, sentences] = await Promise.all([
  loadRuntimeGroups("shared/grammar", ["topics"]),
  loadRuntimeGroups("shared/phrases", ["collocations", "verb-patterns", "items"]),
  loadRuntimeGroups("shared/sentences", ["examples", "exercises", "dialogues", "mistakes"]),
]);

const runtimeByTarget = {
  "grammar-topics": grammar.topics,
  "verb-patterns": phrases["verb-patterns"],
  collocations: phrases.collocations,
  "phrasal-verbs": filterType(phrases.items, ["phrasal-verb"]),
  "idioms-chunks": filterType(phrases.items, ["idiom", "chunk"]),
  "common-mistakes": sentences.mistakes,
  "example-sentences": sentences.examples,
  "translation-pairs": filterType(sentences.exercises, ["translation"]),
  "cloze-exercises": filterType(sentences.exercises, ["cloze"]),
  "sentence-transformations": filterType(sentences.exercises, ["transformation"]),
  "dialogue-examples": sentences.dialogues,
};

const readinessCounts = new Map(
  (readiness.targets ?? []).map((target) => [target.id, target.current]),
);
const results = [];
let failed = false;

for (const target of targetDoc.targets ?? []) {
  requireCondition(
    Object.hasOwn(runtimeByTarget, target.id),
    `No runtime mapping is defined for locked E11 target ${target.id}`,
  );

  const expectedIds = await loadExpectedTargetIds(target);
  const runtimeRecords = runtimeByTarget[target.id];
  const readinessCount = readinessCounts.get(target.id);

  requireCondition(
    typeof readinessCount === "number",
    `E11 readiness report is missing target ${target.id}`,
  );
  requireCondition(
    expectedIds.length === readinessCount,
    `E11 source-selection drift for ${target.id}: audit=${String(expectedIds.length)}, readiness=${String(readinessCount)}`,
  );

  const expected = toIdMultiset(expectedIds, `${target.id} expected`);
  const actual = toIdMultiset(runtimeRecords, `${target.id} runtime`);
  const { missing, extra } = compareMultisets(expected, actual);
  const state = missing.length === 0 && extra.length === 0 ? "matched" : "drift";
  if (state !== "matched") failed = true;

  results.push({
    target: target.id,
    state,
    sourceCount: expectedIds.length,
    runtimeCount: runtimeRecords.length,
    missingCount: missing.reduce((sum, item) => sum + item.count, 0),
    extraCount: extra.reduce((sum, item) => sum + item.count, 0),
    missingSample: missing.slice(0, 20),
    extraSample: extra.slice(0, 20),
  });
}

const report = {
  schemaVersion: 1,
  state: failed ? "drift" : "matched",
  targets: results,
};

console.log(JSON.stringify(report, null, 2));
if (failed) {
  console.error(
    "E11 record coverage drift detected: published runtime IDs do not exactly match the source records counted by E11 readiness.",
  );
  process.exitCode = 1;
}
