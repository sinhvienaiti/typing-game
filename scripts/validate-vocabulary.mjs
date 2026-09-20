import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { buildArtifacts, readLevels, validateLevels } from "./vocabulary-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const vocabularyDir = path.join(root, "shared", "vocabulary");
const schema = JSON.parse(
  await fs.readFile(path.join(vocabularyDir, "schema.json"), "utf8"),
);
const idPattern = schema?.properties?.entries?.items?.properties?.id?.pattern;
const requiredEntryFields = schema?.properties?.entries?.items?.required;
const schemaErrors = [];

if (typeof idPattern !== "string") {
  schemaErrors.push("schema.json: entry id pattern is missing");
} else {
  const idRegex = new RegExp(idPattern);
  if (!idRegex.test("L001-001") || idRegex.test("L01-001") || idRegex.test("L001-01")) {
    schemaErrors.push("schema.json: entry id pattern does not match the Lxxx-xxx contract");
  }
}

for (const field of ["id", "en", "vi", "ipa"]) {
  if (!Array.isArray(requiredEntryFields) || !requiredEntryFields.includes(field)) {
    schemaErrors.push(`schema.json: entry required fields must include ${field}`);
  }
}

if (schema?.properties?.entries?.items?.additionalProperties !== false) {
  schemaErrors.push("schema.json: entry additionalProperties must be false");
}

if (schemaErrors.length > 0) {
  console.error(schemaErrors.join("\n"));
  process.exit(1);
}

const documents = await readLevels(vocabularyDir);
const result = validateLevels(documents);

if (result.errors.length > 0) {
  console.error(result.errors.join("\n"));
  process.exit(1);
}

const artifacts = buildArtifacts(documents);
for (const [name, expected] of [["index.json", artifacts.index], ["lookup.json", artifacts.lookup]]) {
  const current = JSON.parse(
    await fs.readFile(path.join(vocabularyDir, name), "utf8"),
  );
  if (JSON.stringify(current) !== JSON.stringify(expected)) {
    console.error(`${name} is stale. Run: pnpm vocab:generate`);
    process.exit(1);
  }
}

const counts = documents.map(({ data }) => data.entries.length);
const min = Math.min(...counts);
const max = Math.max(...counts);
const average = result.totalEntries / Math.max(1, documents.length);
console.log(`Vocabulary PASS: ${result.totalEntries} entries, ${documents.length} levels, min ${min}, max ${max}, average ${average.toFixed(1)}.`);
