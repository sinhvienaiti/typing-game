import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  buildVocabularyCurriculum,
  loadCurriculumInputs,
  writeCurriculumArtifacts,
} from "./vocabulary-curriculum-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const { source, lookup } = await loadCurriculumInputs(root);
const artifacts = buildVocabularyCurriculum(source, lookup);
await writeCurriculumArtifacts(root, artifacts);

console.log(
  "Generated curriculum:",
  artifacts.index.totalGroups + " groups,",
  artifacts.index.totalTopics + " topics,",
  artifacts.index.uniqueVocabularyKeys + " unique vocabulary keys.",
);
