import fs from "node:fs/promises";

const levelPath = "shared/typing-texts/levels/052.json";
const indexPath = "shared/typing-texts/index.json";
const processPath = "docs/TYPING_TEXT_PROCESS.md";
const level = JSON.parse(await fs.readFile(levelPath, "utf8"));
const index = JSON.parse(await fs.readFile(indexPath, "utf8"));
const words = level.passages.reduce((sum, passage) => sum + passage.wordCount, 0);
let process = await fs.readFile(processPath, "utf8");
const checkpoint = "7950cb0f4313d3af7c77c80ac1fa9515dc4f7940";
const oldStatus = "- Levels 001-051 index: 51 levels, 765 passages, 199221 words.\n- Next active level: 052.";
const newStatus = `- Level 052: ${level.passages.length} passages, ${words} words, duplicate/similarity warnings 0, checkpoint \`${checkpoint}\`.\n- Levels 001-052 index: ${index.availableLevels} levels, ${index.totalPassages} passages, ${index.totalWords} words.\n- Next active level: 053.`;
if (!process.includes(oldStatus)) throw new Error("Expected Level 051 checkpoint status was not found in PROCESS.md");
process = process.replace(oldStatus, newStatus);
await fs.writeFile(processPath, process, "utf8");
console.log(newStatus);
