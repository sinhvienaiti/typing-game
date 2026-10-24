import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const defaultCandidatePath = path.join(
  root,
  "content",
  "english",
  "review-queues",
  "typing-text-e06-sentences.json",
);
const defaultControlledPath = path.join(
  root,
  "content",
  "english",
  "sentences",
  "e06-reviewed-typing-text-sentences.json",
);
const defaultOutputPath = path.join(
  root,
  "content",
  "english",
  "review-queues",
  "typing-text-e11-next-review.json",
);
const reviewRoot = path.join(root, "content", "english", "reviews");
const recordSetId = "reviewed-typing-text-sentences";

function parseArgs(argv) {
  const options = {
    limit: 24,
    candidatePath: defaultCandidatePath,
    controlledPath: defaultControlledPath,
    outputPath: defaultOutputPath,
  };
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (arg === "--limit") {
      options.limit = Number.parseInt(argv[index + 1] ?? "", 10);
      index += 1;
    } else if (arg === "--candidate-path") {
      options.candidatePath = path.resolve(root, argv[index + 1] ?? "");
      index += 1;
    } else if (arg === "--controlled-path") {
      options.controlledPath = path.resolve(root, argv[index + 1] ?? "");
      index += 1;
    } else if (arg === "--output") {
      options.outputPath = path.resolve(root, argv[index + 1] ?? "");
      index += 1;
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }
  if (!Number.isInteger(options.limit) || options.limit < 1 || options.limit > 200) {
    throw new Error("--limit must be an integer from 1 to 200");
  }
  return options;
}

async function readJson(filePath) {
  return JSON.parse(await fs.readFile(filePath, "utf8"));
}

function assertRecordList(document, label) {
  if (!document || !Array.isArray(document.records)) {
    throw new Error(`${label} must contain a records array`);
  }
}

function assertUniqueIds(records, label) {
  const seen = new Set();
  for (const record of records) {
    const id = String(record?.id ?? "");
    if (!id) throw new Error(`${label} contains a record without an id`);
    if (seen.has(id)) throw new Error(`${label} contains duplicate id ${id}`);
    seen.add(id);
  }
  return seen;
}

function collectDecisionRecordIds(document, output) {
  for (const decision of document?.decisions ?? []) {
    if (decision?.recordSetId !== recordSetId) continue;
    const recordId = String(decision?.recordId ?? "");
    if (recordId) output.add(recordId);
  }
}

async function reviewedDecisionIds() {
  const ids = new Set();
  const mainDecisionPath = path.join(reviewRoot, "decisions.json");
  try {
    collectDecisionRecordIds(await readJson(mainDecisionPath), ids);
  } catch (error) {
    if (error?.code !== "ENOENT") throw error;
  }

  const shardDir = path.join(reviewRoot, "decisions.d");
  let entries = [];
  try {
    entries = await fs.readdir(shardDir, { withFileTypes: true });
  } catch (error) {
    if (error?.code !== "ENOENT") throw error;
  }
  for (const entry of entries
    .filter(item => item.isFile() && item.name.endsWith(".json"))
    .sort((left, right) => left.name.localeCompare(right.name))) {
    collectDecisionRecordIds(await readJson(path.join(shardDir, entry.name)), ids);
  }
  return ids;
}

const options = parseArgs(process.argv.slice(2));
const [candidateDocument, controlledDocument, decisionIds] = await Promise.all([
  readJson(options.candidatePath),
  readJson(options.controlledPath),
  reviewedDecisionIds(),
]);
assertRecordList(candidateDocument, "Typing-text candidate queue");
assertRecordList(controlledDocument, "Controlled typing-text source");

const candidateIds = assertUniqueIds(candidateDocument.records, "Typing-text candidate queue");
const controlledIds = assertUniqueIds(controlledDocument.records, "Controlled typing-text source");
const excludedIds = new Set([...controlledIds, ...decisionIds]);
for (const id of excludedIds) {
  if (!candidateIds.has(id)) continue;
}

const remaining = candidateDocument.records.filter(record => !excludedIds.has(record.id));
if (remaining.length < options.limit) {
  throw new Error(
    `Only ${remaining.length} unreviewed typing-text candidates remain; requested ${options.limit}`,
  );
}
const selected = remaining.slice(0, options.limit);
for (const record of selected) {
  if (record?.quality?.state !== "candidate") {
    throw new Error(
      `Next review record ${record.id} must remain candidate; found ${record?.quality?.state ?? "missing"}`,
    );
  }
}

const packet = {
  schemaVersion: 1,
  kind: "english-content-review-packet",
  recordSetId,
  sourceQueue: path.relative(root, options.candidatePath).replaceAll(path.sep, "/"),
  controlledSource: path.relative(root, options.controlledPath).replaceAll(path.sep, "/"),
  selection: {
    strategy: "generator-order-after-controlled-and-ledger-exclusion-v1",
    requestedLimit: options.limit,
    candidateCount: candidateDocument.records.length,
    controlledCount: controlledIds.size,
    reviewedDecisionCount: decisionIds.size,
    excludedCount: excludedIds.size,
    remainingBeforeSelection: remaining.length,
  },
  records: selected,
};

await fs.mkdir(path.dirname(options.outputPath), { recursive: true });
await fs.writeFile(options.outputPath, `${JSON.stringify(packet, null, 2)}\n`, "utf8");

console.log(
  "E11 typing-text next review slice:",
  JSON.stringify({
    output: path.relative(root, options.outputPath).replaceAll(path.sep, "/"),
    candidateCount: candidateDocument.records.length,
    controlledCount: controlledIds.size,
    reviewedDecisionCount: decisionIds.size,
    remainingBeforeSelection: remaining.length,
    selectedCount: selected.length,
    selectedIds: selected.map(record => record.id),
  }),
);
