import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { selectTypingTextReviewSlice } from "./typing-text-review-core.mjs";

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
      options.limit = Number(argv[index + 1] ?? "");
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

const result = selectTypingTextReviewSlice({
  candidates: candidateDocument.records,
  controlled: controlledDocument.records,
  reviewedIds: decisionIds,
  limit: options.limit,
});
const selected = result.records;

const packet = {
  schemaVersion: 1,
  kind: "english-content-review-packet",
  recordSetId,
  state: result.state,
  sourceQueue: path.relative(root, options.candidatePath).replaceAll(path.sep, "/"),
  controlledSource: path.relative(root, options.controlledPath).replaceAll(path.sep, "/"),
  selection: result.selection,
  records: selected,
};

await fs.mkdir(path.dirname(options.outputPath), { recursive: true });
await fs.writeFile(options.outputPath, `${JSON.stringify(packet, null, 2)}\n`, "utf8");

console.log(
  "E11 typing-text next review slice:",
  JSON.stringify({
    output: path.relative(root, options.outputPath).replaceAll(path.sep, "/"),
    state: result.state,
    ...result.selection,
    selectedIds: selected.map(record => record.id),
  }),
);
