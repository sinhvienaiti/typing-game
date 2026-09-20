import path from "node:path";
import { fileURLToPath } from "node:url";
import {
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

if (result.levelReports.length === 0) {
  console.log("No production typing-text levels exist yet.");
  process.exit(0);
}

for (const item of result.levelReports) {
  console.log(
    [
      `Level ${String(item.level).padStart(3, "0")}`,
      item.cefr,
      `${item.passageCount} passages`,
      `${item.wordCount} words`,
      `${item.targetedCount}/${item.vocabularyCount} targets`,
      `${(item.coverage * 100).toFixed(1)}% coverage`,
    ].join(" | "),
  );
}

if (result.warnings.length > 0) {
  console.log(`Review warnings: ${result.warnings.length}`);
}
