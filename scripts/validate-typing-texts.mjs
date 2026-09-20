import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  buildIndex,
  readTypingLevels,
  validateTypingLevels,
} from "./typing-text-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const typingTextDir = path.join(root, "shared", "typing-texts");
const vocabularyDir = path.join(root, "shared", "vocabulary");

const documents = await readTypingLevels(typingTextDir);
const result = await validateTypingLevels(documents, vocabularyDir);

if (result.errors.length > 0) {
  console.error(result.errors.join("\n"));
  process.exit(1);
}

const currentIndex = JSON.parse(
  await fs.readFile(path.join(typingTextDir, "index.json"), "utf8"),
);
const expectedIndex = buildIndex(documents);
if (JSON.stringify(currentIndex) !== JSON.stringify(expectedIndex)) {
  console.error("shared/typing-texts/index.json is stale. Run: pnpm typing-texts:generate");
  process.exit(1);
}

for (const warning of result.warnings) {
  console.warn(`WARN: ${warning}`);
}

console.log(
  `Typing texts PASS: ${result.totalPassages} passages, ${documents.length} levels, ${result.totalWords} words, ${result.warnings.length} review warnings.`,
);
