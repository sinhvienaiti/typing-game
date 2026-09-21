import path from "node:path";
import { fileURLToPath } from "node:url";
import { readTypingLevels, validateTypingLevels } from "./typing-text-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const typingTextDir = path.join(root, "shared", "typing-texts");
const vocabularyDir = path.join(root, "shared", "vocabulary");
const documents = await readTypingLevels(typingTextDir);
const result = await validateTypingLevels(documents, vocabularyDir);
const errors = result.errors.filter((message) => message.startsWith("052.json"));
const warnings = result.warnings.filter((message) => message.startsWith("052.json"));
const report = result.levelReports.find((item) => item.level === 52);

if (errors.length > 0) {
  console.error(errors.join("\n"));
  process.exit(1);
}
if (warnings.length > 0) {
  console.error(warnings.map((message) => `WARN: ${message}`).join("\n"));
  process.exit(1);
}
if (!report || report.passageCount < 15) {
  console.error("052.json did not produce a complete level report");
  process.exit(1);
}
console.log(`Level 052 PASS: ${report.passageCount} passages, ${report.wordCount} words, ${(report.coverage * 100).toFixed(1)} percent vocabulary coverage, 0 duplicate/similarity warnings.`);
