import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  PLANNED_LEVELS,
  buildArtifacts,
  normalizeEnglish,
  readLevels,
  stableJson,
  validateLevels,
} from "./vocabulary-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

function getNumberArg(name, fallback) {
  const index = process.argv.indexOf(name);
  if (index === -1) return fallback;
  const value = Number(process.argv[index + 1]);
  if (!Number.isInteger(value) || value < 0) {
    throw new Error(`${name} requires a non-negative integer`);
  }
  return value;
}

function getPathArg(name, fallback) {
  const index = process.argv.indexOf(name);
  if (index === -1) return fallback;
  const value = process.argv[index + 1];
  if (value === undefined || value.startsWith("--")) {
    throw new Error(`${name} requires a value`);
  }
  return path.resolve(value);
}

const inputFile = getPathArg(
  "--input",
  path.join(root, ".cache", "vocabulary-candidates.json"),
);
const targetEntries = getNumberArg("--target", 18000);
const minimumEntries = getNumberArg("--minimum", 15000);
const preserveThrough = getNumberArg("--preserve-through", 3);
const vocabularyDir = path.join(root, "shared", "vocabulary");
const levelsDir = path.join(vocabularyDir, "levels");

if (preserveThrough >= PLANNED_LEVELS) {
  throw new Error(`--preserve-through must be below ${PLANNED_LEVELS}`);
}
if (targetEntries < minimumEntries) {
  throw new Error("--target must be greater than or equal to --minimum");
}

function normalizeText(value) {
  return String(value ?? "").normalize("NFKC").trim().replace(/\s+/g, " ");
}

function hasTrustedProvenance(option) {
  const source = String(option?.source ?? "").toLowerCase();
  return source.includes("cmudict") &&
    (source.includes("wordnet") || source.includes("wiktionary"));
}

function sourceScore(option) {
  const source = String(option?.source ?? "").toLowerCase();
  let score = 0;
  if (source.includes("wiktionary")) score += 3;
  if (source.includes("wordnet")) score += 3;
  if (source.includes("cmudict")) score += 2;
  if (source.includes("llm")) score -= 1;
  return score;
}

function chooseOption(candidate) {
  const trusted = (candidate.options ?? []).filter((option) => {
    const ipa = normalizeText(option.ipa);
    return hasTrustedProvenance(option) &&
      ipa.startsWith("/") &&
      ipa.endsWith("/") &&
      Array.isArray(option.vi) &&
      option.vi.some((value) => normalizeText(value) !== "");
  });

  const sameCefr = candidate.cefr === null
    ? []
    : trusted.filter((option) => option.cefr === candidate.cefr);
  const pool = sameCefr.length > 0 ? sameCefr : trusted;

  return [...pool].sort((a, b) =>
    sourceScore(b) - sourceScore(a) ||
    (Number(b.frequency) || 0) - (Number(a.frequency) || 0) ||
    String(a.pos ?? "").localeCompare(String(b.pos ?? ""))
  )[0] ?? null;
}

function usefulnessCompare(a, b) {
  return b.frequency - a.frequency ||
    Number(b.cefr !== null) - Number(a.cefr !== null) ||
    a.complexity - b.complexity ||
    a.en.localeCompare(b.en);
}

function difficultyCompare(a, b) {
  return a.estimatedLevel - b.estimatedLevel ||
    b.frequency - a.frequency ||
    a.complexity - b.complexity ||
    a.en.localeCompare(b.en);
}

function labelForLevel(level) {
  const id = String(level).padStart(3, "0");
  if (level <= 12) return `A1 Foundation ${id}`;
  if (level <= 28) return `A2 Foundation ${id}`;
  if (level <= 46) return `B1 Intermediate ${id}`;
  if (level <= 65) return `B2 Upper Intermediate ${id}`;
  if (level <= 82) return `C1 Advanced ${id}`;
  if (level <= 94) return `C2 Advanced ${id}`;
  return `Advanced ${id}`;
}

const artifact = JSON.parse(await fs.readFile(inputFile, "utf8"));
if (artifact.version !== 2 || !Array.isArray(artifact.candidates)) {
  throw new Error("Candidate artifact must be version 2. Run: pnpm vocab:candidates");
}

const currentDocuments = await readLevels(vocabularyDir);
const preservedDocuments = currentDocuments.filter(
  ({ data }) => data.level <= preserveThrough,
);
const preservedValidation = validateLevels(preservedDocuments);
if (preservedValidation.errors.length > 0) {
  throw new Error(
    `Preserved vocabulary is invalid:\n${preservedValidation.errors.join("\n")}`,
  );
}

const preservedEnglish = new Set();
for (const { data } of preservedDocuments) {
  for (const entry of data.entries) {
    preservedEnglish.add(normalizeEnglish(entry.en));
  }
}

const eligible = [];
let skippedReview = 0;
let skippedUntrusted = 0;
let skippedPreserved = 0;

for (const candidate of artifact.candidates) {
  const en = normalizeEnglish(candidate.en ?? "");
  if (!en) continue;

  if (preservedEnglish.has(en)) {
    skippedPreserved++;
    continue;
  }
  if (candidate.reviewRequired === true) {
    skippedReview++;
    continue;
  }

  const option = chooseOption(candidate);
  if (option === null) {
    skippedUntrusted++;
    continue;
  }

  const vi = normalizeText(option.vi.find((value) => normalizeText(value) !== ""));
  const ipa = normalizeText(option.ipa);
  const frequency = Number(candidate.frequency) || Number(option.frequency) || 0;
  const complexity =
    (Number(candidate.spellingDifficulty) || 0) +
    (Number(candidate.pronunciationDifficulty) || 0);

  eligible.push({
    en,
    vi,
    ipa,
    cefr: candidate.cefr ?? null,
    proposedLevel: Number.isInteger(candidate.proposedLevel)
      ? candidate.proposedLevel
      : null,
    frequency,
    complexity,
    estimatedLevel: null,
  });
}

const preservedCount = preservedValidation.totalEntries;
if (targetEntries < preservedCount) {
  throw new Error(
    `Target ${targetEntries} is below ${preservedCount} preserved entries`,
  );
}

const autoTarget = targetEntries - preservedCount;
eligible.sort(usefulnessCompare);
const selected = eligible.slice(0, autoTarget);
const finalTotal = preservedCount + selected.length;

if (finalTotal < minimumEntries) {
  throw new Error(
    `Only ${finalTotal} trusted entries are available; minimum is ${minimumEntries}. ` +
    "Do not fill the gap with untrusted/generated vocabulary.",
  );
}

const unknown = selected
  .filter((candidate) => candidate.proposedLevel === null)
  .sort((a, b) =>
    b.frequency - a.frequency ||
    a.complexity - b.complexity ||
    a.en.localeCompare(b.en)
  );

for (let index = 0; index < unknown.length; index++) {
  unknown[index].estimatedLevel = 1 + Math.min(
    PLANNED_LEVELS - 1,
    Math.floor((index * PLANNED_LEVELS) / Math.max(1, unknown.length)),
  );
}

for (const candidate of selected) {
  if (candidate.estimatedLevel === null) {
    candidate.estimatedLevel = candidate.proposedLevel;
  }
}
selected.sort(difficultyCompare);

const generatedLevels = PLANNED_LEVELS - preserveThrough;
const baseCount = Math.floor(selected.length / generatedLevels);
const remainder = selected.length % generatedLevels;
let cursor = 0;
const generatedDocuments = [];

for (let level = preserveThrough + 1; level <= PLANNED_LEVELS; level++) {
  const relative = level - preserveThrough - 1;
  const count = baseCount + (relative < remainder ? 1 : 0);
  const chunk = selected.slice(cursor, cursor + count);
  cursor += count;

  generatedDocuments.push({
    file: `${String(level).padStart(3, "0")}.json`,
    data: {
      version: 1,
      level,
      label: labelForLevel(level),
      entries: chunk.map((entry, index) => ({
        id: `L${String(level).padStart(3, "0")}-${String(index + 1).padStart(3, "0")}`,
        en: entry.en,
        vi: entry.vi,
        ipa: entry.ipa,
      })),
    },
  });
}

const allDocuments = [...preservedDocuments, ...generatedDocuments];
const validation = validateLevels(allDocuments);
if (validation.errors.length > 0) {
  throw new Error(
    `Generated vocabulary is invalid:\n${validation.errors.join("\n")}`,
  );
}

await fs.mkdir(levelsDir, { recursive: true });
const existingNames = await fs.readdir(levelsDir);
for (const name of existingNames) {
  if (!/^\d{3}\.json$/.test(name)) continue;
  const level = Number(name.slice(0, 3));
  if (level > preserveThrough) {
    await fs.rm(path.join(levelsDir, name));
  }
}

for (const document of generatedDocuments) {
  await fs.writeFile(
    path.join(levelsDir, document.file),
    stableJson(document.data),
  );
}

const artifacts = buildArtifacts(allDocuments);
await fs.writeFile(
  path.join(vocabularyDir, "index.json"),
  stableJson(artifacts.index),
);
await fs.writeFile(
  path.join(vocabularyDir, "lookup.json"),
  stableJson(artifacts.lookup),
);

const report = {
  version: 1,
  generatedAt: new Date().toISOString(),
  input: inputFile,
  requestedTarget: targetEntries,
  minimumEntries,
  preservedThroughLevel: preserveThrough,
  preservedEntries: preservedCount,
  trustedEligibleCandidates: eligible.length,
  selectedAutomaticEntries: selected.length,
  totalEntries: finalTotal,
  skipped: {
    preservedEnglish: skippedPreserved,
    reviewRequired: skippedReview,
    untrustedProvenance: skippedUntrusted,
  },
  levelCounts: allDocuments.map(({ data }) => ({
    level: data.level,
    count: data.entries.length,
  })),
};

const reportFile = path.join(
  root,
  ".cache",
  "vocabulary-build-report.json",
);
await fs.mkdir(path.dirname(reportFile), { recursive: true });
await fs.writeFile(reportFile, stableJson(report));

console.log(
  `Built ${finalTotal} trusted vocabulary entries across ${PLANNED_LEVELS} levels ` +
  `(${preservedCount} preserved, ${selected.length} automatic).`,
);
if (finalTotal < targetEntries) {
  console.warn(
    `Target ${targetEntries} was not reached; kept trusted total ${finalTotal}.`,
  );
}
console.log(`Build report: ${reportFile}`);
