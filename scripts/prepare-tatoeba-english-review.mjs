import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { listJsonFiles, stableJson } from "./english-content-core.mjs";
import { readEnglishReviewLedger } from "./english-review-core.mjs";
import { readTatoebaEnglishSnapshot, selectTatoebaEnglishReview, TATOEBA_ENGLISH_RECORD_SET } from "./tatoeba-english-intake-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const args = process.argv.slice(2);
let limit = 24;
let output = path.join(root, "content/english/review-queues/tatoeba-english-next-review.json");
for (let index = 0; index < args.length; index++) {
  if (args[index] === "--limit") limit = Number(args[++index] ?? "");
  else if (args[index] === "--output" && args[index + 1]) output = path.resolve(root, args[++index]);
  else throw new Error(`Unknown or incomplete argument: ${args[index]}`);
}
if (!Number.isInteger(limit) || limit < 1 || limit > 200) throw new Error("--limit must be an integer from 1 to 200");
const [{ pin, rows }, ledger] = await Promise.all([readTatoebaEnglishSnapshot(root), readEnglishReviewLedger(root)]);
const controlled = [];
// All canonical sentence sets, including drafts and existing unpublished review decisions,
// reserve their IDs/texts. Do not silently replace an older Tatoeba source snapshot.
for (const file of await listJsonFiles(path.join(root, "content/english/sentences"))) {
  const doc = JSON.parse(await fs.readFile(file, "utf8"));
  controlled.push(...(doc.records ?? []).filter(record => record.id?.startsWith("sent.") && typeof record.text === "string"));
}
const reviewedIds = new Set(ledger.decisions.filter(row => row.recordSetId === TATOEBA_ENGLISH_RECORD_SET).map(row => row.recordId));
const packet = selectTatoebaEnglishReview({ rows, pin, controlled, reviewedIds, limit });
await fs.mkdir(path.dirname(output), { recursive: true });
await fs.writeFile(output, stableJson(packet), "utf8");
console.log("Pinned Tatoeba English review queue:", JSON.stringify({ state: packet.state, ...packet.selection }));
