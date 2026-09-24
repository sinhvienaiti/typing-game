import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  buildVocabularyCurriculum,
  CURRICULUM_ARTIFACTS,
  loadCurriculumInputs,
  stableJson,
} from "./vocabulary-curriculum-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const { vocabularyDir, source, lookup } = await loadCurriculumInputs(root);
const expected = buildVocabularyCurriculum(source, lookup);
const errors = [];

if (expected.index.totalGroups < 15) errors.push("expected at least 15 curriculum groups");
if (expected.index.totalTopics < 90) errors.push("expected at least 90 practical topics");
if (expected.coverage.topicExactMatchRate < 0.95) {
  errors.push("topic exact-match rate must stay >= 95%");
}

for (const topic of expected.coverage.topics) {
  if (topic.resolved < 4) errors.push(topic.id + ": fewer than 4 resolved vocabulary keys");
}

for (const id of ["noun", "verb", "adjective", "adverb"]) {
  const category = expected.partsOfSpeech.categories.find((item) => item.id === id);
  if (!category || category.entries.length < 20) {
    errors.push(id + ": core POS view must resolve at least 20 vocabulary keys");
  }
}

const topicIds = new Set(expected.index.topics.map((topic) => topic.id));
for (const module of expected.grammar.modules) {
  for (const topicId of module.topicIds) {
    if (!topicIds.has(topicId)) errors.push(module.id + ": unknown topic " + topicId);
  }
}
for (const id of expected.grammar.primaryTimeGroups) {
  if (!expected.grammar.modules.some((module) => module.id === id)) {
    errors.push("missing primary time group: " + id);
  }
}

for (const [key, topics] of Object.entries(expected.index.reverseTopics)) {
  const level = lookup.entries[key];
  if (!Number.isInteger(level) || level < 1 || level > 100) {
    errors.push("reverse topic key is not in vocabulary lookup: " + key);
  }
  if (!Array.isArray(topics) || topics.length === 0) {
    errors.push("reverse topic key has no topic: " + key);
  }
}

for (const [relativePath, key] of Object.entries(CURRICULUM_ARTIFACTS)) {
  const target = path.join(vocabularyDir, relativePath);
  let actual;
  try {
    actual = await fs.readFile(target, "utf8");
  } catch {
    errors.push("missing generated curriculum artifact: " + relativePath);
    continue;
  }
  if (actual !== stableJson(expected[key])) {
    errors.push(relativePath + ": stale generated artifact; run pnpm curriculum:generate");
  }
}

if (errors.length > 0) {
  console.error(errors.join("\n"));
  process.exitCode = 1;
} else {
  console.log(
    "Vocabulary curriculum valid:",
    expected.index.totalTopics + " topics,",
    expected.index.uniqueVocabularyKeys + " unique topic keys,",
    (expected.coverage.topicExactMatchRate * 100).toFixed(1) + "% exact-match.",
  );
}
