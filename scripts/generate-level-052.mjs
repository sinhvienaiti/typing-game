import fs from "node:fs/promises";
import path from "node:path";
import { countWords, expectedCefr, stableJson } from "./typing-text-core.mjs";

const level = 52;
const root = process.cwd();
const vocabularyPath = path.join(root, "shared/vocabulary/levels/052.json");
const outputPath = path.join(root, "shared/typing-texts/levels/052.json");
const vocabulary = JSON.parse(await fs.readFile(vocabularyPath, "utf8")).entries.map((entry) => entry.en);

const themes = [
  ["polar research", "field report", "ice station", "reflective", "scientists", "weather", "samples", "expedition"],
  ["community fundraiser", "feature", "town hall", "hopeful", "neighbors", "families", "donations", "festival"],
  ["rowing club", "memoir", "riverside boathouse", "energetic", "athletes", "training", "boats", "regatta"],
  ["electronics workshop", "explanation", "repair laboratory", "practical", "students", "circuits", "devices", "prototype"],
  ["museum redesign", "case study", "city gallery", "curious", "curators", "visitors", "exhibits", "archive"],
  ["dental clinic", "narrative", "health center", "calm", "clinicians", "patients", "treatment", "appointment"],
  ["farm renewal", "report", "country valley", "optimistic", "farmers", "soil", "harvest", "cooperative"],
  ["coastal rescue", "narrative", "island outpost", "urgent", "rescuers", "tides", "vessels", "mission"],
  ["business recovery", "case study", "market district", "measured", "merchants", "customers", "accounts", "reopening"],
  ["public art project", "feature", "community square", "warm", "artists", "murals", "workshops", "exhibition"],
  ["medical training", "explanation", "teaching hospital", "careful", "nurses", "care", "simulation", "ward"],
  ["forest retreat", "travel note", "mountain lodge", "peaceful", "guides", "trails", "wildlife", "journey"],
  ["technology evaluation", "analysis", "innovation center", "thoughtful", "engineers", "systems", "testing", "review"],
  ["historical exhibition", "feature", "regional archive", "respectful", "historians", "records", "artifacts", "opening"],
  ["mobility planning", "report", "city council", "constructive", "planners", "streets", "access", "consultation"],
];

const verbs = ["examined", "mapped", "discussed", "tested", "revised", "documented", "compared", "organized", "observed", "improved", "reviewed", "explained"];
const adverbs = ["carefully", "patiently", "openly", "methodically", "quietly", "practically", "thoughtfully", "steadily", "responsibly", "clearly", "fairly", "closely"];
const outcomes = ["a useful next step", "a clearer shared plan", "better evidence for decisions", "a safer routine for everyone", "a more realistic timetable", "stronger trust among participants", "a practical change in procedure", "a balanced public explanation", "a workable solution for the next stage", "a better understanding of local needs"];

function targetsFor(index) {
  const targets = [];
  for (let offset = 0; offset < 20; offset++) targets.push(vocabulary[(index * 7 + offset) % vocabulary.length]);
  return targets;
}

function buildPassage(index) {
  const [topic, style, setting, tone, actors, focus, objects, event] = themes[index];
  const targets = targetsFor(index);
  const chunks = Array.from({ length: 4 }, (_, chunk) => targets.slice(chunk * 5, chunk * 5 + 5));
  const sentences = [
    `The ${topic} effort brought ${actors} together at the ${setting} to study ${focus} and prepare for the ${event}`,
    `During one focused session, the group considered ${chunks[0].slice(0, 4).join(", ")}, and ${chunks[0][4]} in examples suited to the ${topic} work`,
    `In a separate practical exercise, participants encountered ${chunks[1].slice(0, 4).join(", ")}, and ${chunks[1][4]} in examples suited to the ${topic} work`,
    `Later notes connected ${chunks[2].slice(0, 4).join(", ")}, and ${chunks[2][4]} in examples suited to the ${topic} work`,
    `Before the final review, everyone discussed ${chunks[3].slice(0, 4).join(", ")}, and ${chunks[3][4]} in examples suited to the ${topic} work`,
  ];

  let step = 0;
  while (countWords(sentences.join(". ") + ".") < 250) {
    const verb = verbs[(index * 5 + step) % verbs.length];
    const adverb = adverbs[(index * 7 + step * 2) % adverbs.length];
    const outcome = outcomes[(index * 3 + step) % outcomes.length];
    const variants = [
      `The ${actors} ${adverb} ${verb} how ${objects} affected ${focus}, then recorded observations that pointed toward ${outcome}`,
      `Instead of accepting the first suggestion, the team ${verb} details from the ${setting} and asked which evidence could support ${outcome}`,
      `People with different experience spoke ${adverb}, so discussion about ${focus} stayed concrete while the ${event} remained an achievable goal`,
      `By comparing everyday concerns with information about ${objects}, participants ${verb} the plan and created ${outcome} without hiding remaining uncertainty`,
      `A later review at the ${setting} considered ${objects} ${adverb} and connected fresh evidence with ${outcome}`,
    ];
    sentences.push(variants[step % variants.length]);
    step++;
  }

  const text = sentences.join(". ") + ".";
  const wordCount = countWords(text);
  if (wordCount > 300) throw new Error(`Passage ${index + 1} exceeded 300 words: ${wordCount}`);
  return {
    id: `L052-P${String(index + 1).padStart(3, "0")}`,
    topic,
    style,
    setting,
    tone,
    targetWords: targets,
    wordCount,
    text,
  };
}

const document = {
  version: 1,
  level,
  cefr: expectedCefr(level),
  passages: themes.map((_, index) => buildPassage(index)),
};

await fs.writeFile(outputPath, stableJson(document), "utf8");
console.log(`Generated ${outputPath} with ${document.passages.length} passages and ${document.passages.reduce((sum, passage) => sum + passage.wordCount, 0)} words.`);
