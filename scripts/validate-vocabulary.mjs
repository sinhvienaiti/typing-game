import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { buildArtifacts, readLevels, stableJson, validateLevels } from "./vocabulary-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const vocabularyDir = path.join(root, "shared", "vocabulary");
const documents = await readLevels(vocabularyDir);
const result = validateLevels(documents);

if (result.errors.length > 0) {
  console.error(result.errors.join("\n"));
  process.exit(1);
}

const artifacts = buildArtifacts(documents);
for (const [name, expected] of [["index.json", artifacts.index], ["lookup.json", artifacts.lookup]]) {
  const current = await fs.readFile(path.join(vocabularyDir, name), "utf8");
  if (current !== stableJson(expected)) {
    console.error(`${name} is stale. Run: pnpm vocab:generate`);
    process.exit(1);
  }
}

const counts = documents.map(({ data }) => data.entries.length);
const min = Math.min(...counts);
const max = Math.max(...counts);
const average = result.totalEntries / Math.max(1, documents.length);
console.log(`Vocabulary PASS: ${result.totalEntries} entries, ${documents.length} levels, min ${min}, max ${max}, average ${average.toFixed(1)}.`);
