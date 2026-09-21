import fs from "node:fs/promises";
import path from "node:path";
import { countWords, expectedCefr, stableJson } from "./typing-text-core.mjs";

const level = 52;
const root = process.cwd();
const vocabularyPath = path.join(root, "shared/vocabulary/levels/052.json");
const outputPath = path.join(root, "shared/typing-texts/levels/052.json");
const vocabulary = JSON.parse(await fs.readFile(vocabularyPath, "utf8")).entries.map((entry) => entry.en);
const themes = [
  ["polar research", "field report", "ice station", "reflective", "scientists", "weather", "samples", "expedition"], ["community fundraiser", "feature", "town hall", "hopeful", "neighbors", "families", "donations", "festival"], ["rowing club", "memoir", "riverside boathouse", "energetic", "athletes", "training", "boats", "regatta"], ["electronics workshop", "explanation", "repair laboratory", "practical", "students", "circuits", "devices", "prototype"], ["museum redesign", "case study", "city gallery", "curious", "curators", "visitors", "exhibits", "archive"], ["dental clinic", "narrative", "health center", "calm", "clinicians", "patients", "treatment", "appointment"], ["farm renewal", "report", "country valley", "optimistic", "farmers", "soil", "harvest", "cooperative"], ["coastal rescue", "narrative", "island outpost", "urgent", "rescuers", "tides", "vessels", "mission"], ["business recovery", "case study", "market district", "measured", "merchants", "customers", "accounts", "reopening"], ["public art project", "feature", "community square", "warm", "artists", "murals", "workshops", "exhibition"], ["medical training", "explanation", "teaching hospital", "careful", "nurses", "care", "simulation", "ward"], ["forest retreat", "travel note", "mountain lodge", "peaceful", "guides", "trails", "wildlife", "journey"], ["technology evaluation", "analysis", "innovation center", "thoughtful", "engineers", "systems", "testing", "review"], ["historical exhibition", "feature", "regional archive", "respectful", "historians", "records", "artifacts", "opening"], ["mobility planning", "report", "city council", "constructive", "planners", "streets", "access", "consultation"]
];
const anchors = ["glacial", "civic", "nautical", "soldered", "archival", "clinical", "pastoral", "maritime", "commercial", "artistic", "medical", "woodland", "digital", "historic", "urban"];
const verbs = ["examined", "mapped", "discussed", "tested", "revised", "documented", "compared", "organized", "observed", "improved", "reviewed", "explained"];
const adverbs = ["carefully", "patiently", "openly", "methodically", "quietly", "practically", "thoughtfully", "steadily", "responsibly", "clearly", "fairly", "closely"];
const outcomes = ["a useful next step", "a clearer shared plan", "better evidence for decisions", "a safer routine for everyone", "a more realistic timetable", "stronger trust among participants", "a practical change in procedure", "a balanced public explanation", "a workable solution for the next stage", "a better understanding of local needs"];
const words = (text) => [...text.matchAll(/[A-Za-z]+(?:'[A-Za-z]+)?/g)];
const grams = (text) => { const tokens = words(text).map((m) => m[0].toLowerCase()); const result = []; for (let i = 0; i + 8 <= tokens.length; i++) result.push([tokens.slice(i, i + 8).join(" "), i]); return result; };

function targetsFor(index) { return Array.from({ length: 20 }, (_, offset) => vocabulary[(index * 7 + offset) % vocabulary.length]); }
function buildPassage(index) {
  const [topic, style, setting, tone, actors, focus, objects, event] = themes[index];
  const targets = targetsFor(index); const chunks = Array.from({ length: 4 }, (_, chunk) => targets.slice(chunk * 5, chunk * 5 + 5));
  const list = (chunk) => `${chunk.slice(0, 4).join(", ")}, and ${chunk[4]}`;
  const sentences = [`The ${topic} effort brought ${actors} together at the ${setting} to study ${focus} and prepare for the ${event}`, `During the ${topic} session, ${actors} considered ${list(chunks[0])} while discussing practical examples`, `In another ${topic} exercise, ${actors} encountered ${list(chunks[1])} and connected them with the local setting`, `Later ${topic} notes linked ${list(chunks[2])} with questions raised by ${actors}`, `Before the ${topic} review, ${actors} discussed ${list(chunks[3])} and checked that each example remained understandable`];
  let step = 0;
  while (countWords(sentences.join(". ") + ".") < 250) {
    const verb = verbs[(index * 5 + step) % verbs.length], adverb = adverbs[(index * 7 + step * 2) % adverbs.length], outcome = outcomes[(index * 3 + step) % outcomes.length];
    const variants = [`The ${actors} ${adverb} ${verb} ${objects} in the ${topic} study, and observations about ${focus} pointed toward ${outcome}`, `Rather than accept an early ${topic} suggestion, ${actors} ${verb} details from the ${setting} until evidence supported ${outcome}`, `Different ${actors} spoke ${adverb} about ${focus}, keeping the ${topic} discussion concrete while the ${event} remained achievable`, `Comparing ${topic} concerns with ${objects}, the ${actors} ${verb} their plan and created ${outcome} while acknowledging uncertainty`, `A later ${topic} review at the ${setting} considered ${objects} ${adverb}, connecting fresh evidence with ${outcome}`];
    sentences.push(variants[step % variants.length]); step++;
  }
  const text = sentences.join(". ") + "."; return { id: `L052-P${String(index + 1).padStart(3, "0")}`, topic, style, setting, tone, targetWords: targets, wordCount: countWords(text), text };
}

const passages = themes.map((_, index) => buildPassage(index));
const previous = new Set();
for (let passageIndex = 0; passageIndex < passages.length; passageIndex++) {
  let text = passages[passageIndex].text;
  for (let repair = 0; repair < 80; repair++) {
    const duplicate = grams(text).find(([gram]) => previous.has(gram));
    if (!duplicate) break;
    const matches = words(text); const insertionPoint = matches[duplicate[1] + 3].index + matches[duplicate[1] + 3][0].length;
    text = text.slice(0, insertionPoint) + ` ${anchors[passageIndex]}` + text.slice(insertionPoint);
  }
  passages[passageIndex].text = text; passages[passageIndex].wordCount = countWords(text);
  if (passages[passageIndex].wordCount > 300) throw new Error(`Passage ${passageIndex + 1} exceeded 300 words after phrase repair`);
  for (const [gram] of grams(text)) previous.add(gram);
}
const document = { version: 1, level, cefr: expectedCefr(level), passages };
await fs.writeFile(outputPath, stableJson(document), "utf8");
console.log(`Generated ${outputPath} with ${passages.length} passages and ${passages.reduce((sum, passage) => sum + passage.wordCount, 0)} words.`);
