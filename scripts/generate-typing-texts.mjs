import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  buildIndex,
  readTypingLevels,
  stableJson,
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

const index = buildIndex(documents);
await fs.writeFile(path.join(typingTextDir, "index.json"), stableJson(index));
console.log(
  `Generated typing-text index for ${index.totalPassages} passages across ${index.availableLevels} levels.`,
);
