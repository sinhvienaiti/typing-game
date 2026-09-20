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
const CEFR_RANK = { A1: 1, A2: 2, B1: 3, B2: 4, C1: 5, C2: 6 };

function numberArg(name, fallback) {
  const i = process.argv.indexOf(name);
  if (i === -1) return fallback;
  const value = Number(process.argv[i + 1]);
  if (!Number.isInteger(value) || value < 0) throw new Error(`${name} requires an integer >= 0`);
  return value;
}

function pathArg(name, fallback) {
  const i = process.argv.indexOf(name);
  if (i === -1) return fallback;
  const value = process.argv[i + 1];
  if (!value || value.startsWith("--")) throw new Error(`${name} requires a value`);
  return path.resolve(value);
}

const sourceRoot = path.join(root, ".cache", "vocabulary-sources");
const inputFile = pathArg("--input", path.join(root, ".cache", "vocabulary-candidates.json"));
const rankingFile = pathArg("--wordfreq", path.join(sourceRoot, "wordfreq", "ranking.tsv"));
const target = numberArg("--target", 18000);
const minimum = numberArg("--minimum", 15000);
const preserveThrough = numberArg("--preserve-through", 3);
const vocabularyDir = path.join(root, "shared", "vocabulary");
const levelsDir = path.join(vocabularyDir, "levels");

if (preserveThrough >= PLANNED_LEVELS) throw new Error("Invalid preserve level");
if (target < minimum) throw new Error("--target must be >= --minimum");

const clean = (value) => String(value ?? "").normalize("NFKC").trim().replace(/\s+/g, " ");

function trusted(option) {
  const source = String(option?.source ?? "").toLowerCase();
  return source.includes("cmudict") && source.includes("wiktionary");
}

function buildEntry(candidate) {
  const options = (candidate.options ?? []).filter((option) => {
    const ipa = clean(option.ipa);
    return trusted(option) && ipa.startsWith("/") && ipa.endsWith("/") &&
      Array.isArray(option.vi) && option.vi.some((value) => clean(value));
  });
  if (!options.length) return null;

  const pronunciations = new Set(options.map((option) => clean(option.ipa)));
  if (pronunciations.size !== 1) return null;

  options.sort((a, b) =>
    Number(b.cefr === candidate.cefr) - Number(a.cefr === candidate.cefr) ||
    Number(String(b.source).toLowerCase().includes("wordnet")) -
      Number(String(a.source).toLowerCase().includes("wordnet")) ||
    String(a.pos ?? "").localeCompare(String(b.pos ?? ""))
  );

  const meanings = [];
  for (const option of options) {
    const meaning = clean(option.vi.find((value) => clean(value)));
    if (meaning && !meanings.includes(meaning)) meanings.push(meaning);
    if (meanings.length === 3) break;
  }
  if (!meanings.length) return null;

  return { en: normalizeEnglish(candidate.en), vi: meanings.join("; "), ipa: clean(options[0].ipa) };
}

function label(level) {
  const id = String(level).padStart(3, "0");
  if (level <= 12) return `A1 Foundation ${id}`;
  if (level <= 28) return `A2 Foundation ${id}`;
  if (level <= 46) return `B1 Intermediate ${id}`;
  if (level <= 65) return `B2 Upper Intermediate ${id}`;
  if (level <= 82) return `C1 Advanced ${id}`;
  if (level <= 94) return `C2 Advanced ${id}`;
  return `Advanced ${id}`;
}

function cefrPosition(cefr) {
  const rank = CEFR_RANK[cefr];
  return rank === undefined ? null : (rank - 0.5) / 6;
}

const artifact = JSON.parse(await fs.readFile(inputFile, "utf8"));
if (artifact.version !== 3 || !Array.isArray(artifact.candidates)) {
  throw new Error("Candidate artifact must be version 3. Run: pnpm vocab:candidates");
}

const current = await readLevels(vocabularyDir);
const preserved = current.filter(({ data }) => data.level <= preserveThrough);
const preservedCheck = validateLevels(preserved);
if (preservedCheck.errors.length) throw new Error(preservedCheck.errors.join("\n"));

const preservedEnglish = new Set(
  preserved.flatMap(({ data }) => data.entries.map((entry) => normalizeEnglish(entry.en))),
);
const candidates = new Map(artifact.candidates.map((item) => [normalizeEnglish(item.en), item]));
const ranking = (await fs.readFile(rankingFile, "utf8")).trim().split("\n").map((line) => {
  const [rank, zipf, en] = line.split("\t");
  return { rank: Number(rank), zipf: Number(zipf), en: normalizeEnglish(en) };
});

const eligible = [];
const skipped = { preserved: 0, missingDictionary: 0, reviewRequired: 0, invalidEntry: 0 };

for (let i = 0; i < ranking.length; i++) {
  const ranked = ranking[i];
  if (!/^[a-z]{2,}$/.test(ranked.en)) continue;
  if (preservedEnglish.has(ranked.en)) { skipped.preserved++; continue; }

  const candidate = candidates.get(ranked.en);
  if (!candidate) { skipped.missingDictionary++; continue; }
  if (candidate.reviewRequired) { skipped.reviewRequired++; continue; }

  const entry = buildEntry(candidate);
  if (!entry) { skipped.invalidEntry++; continue; }

  const freqPosition = i / Math.max(1, ranking.length - 1);
  const cefr = cefrPosition(candidate.cefr);
  const complexity = (Number(candidate.spellingDifficulty) || 0) +
    (Number(candidate.pronunciationDifficulty) || 0);
  const difficulty = (cefr === null ? freqPosition : cefr * 0.7 + freqPosition * 0.3) +
    Math.min(0.035, complexity * 0.00175);

  eligible.push({ ...entry, wordfreqRank: ranked.rank, zipf: ranked.zipf, difficulty });
}

const preservedCount = preservedCheck.totalEntries;
const selectedByFrequency = eligible
  .sort((a, b) => a.wordfreqRank - b.wordfreqRank || a.en.localeCompare(b.en))
  .slice(0, Math.max(0, target - preservedCount));
const total = preservedCount + selectedByFrequency.length;
if (total < minimum) {
  throw new Error(`Only ${total} trusted common-word entries are available; minimum is ${minimum}.`);
}

const selected = [...selectedByFrequency].sort((a, b) =>
  a.difficulty - b.difficulty || a.wordfreqRank - b.wordfreqRank || a.en.localeCompare(b.en)
);
const generatedLevelCount = PLANNED_LEVELS - preserveThrough;
const baseCount = Math.floor(selected.length / generatedLevelCount);
const remainder = selected.length % generatedLevelCount;
let cursor = 0;
const generated = [];

for (let level = preserveThrough + 1; level <= PLANNED_LEVELS; level++) {
  const relative = level - preserveThrough - 1;
  const count = baseCount + (relative < remainder ? 1 : 0);
  const chunk = selected.slice(cursor, cursor + count);
  cursor += count;
  generated.push({
    file: `${String(level).padStart(3, "0")}.json`,
    data: {
      version: 1,
      level,
      label: label(level),
      entries: chunk.map((entry, index) => ({
        id: `L${String(level).padStart(3, "0")}-${String(index + 1).padStart(3, "0")}`,
        en: entry.en,
        vi: entry.vi,
        ipa: entry.ipa,
      })),
    },
  });
}

const documents = [...preserved, ...generated];
const check = validateLevels(documents);
if (check.errors.length) throw new Error(check.errors.join("\n"));

await fs.mkdir(levelsDir, { recursive: true });
for (const name of await fs.readdir(levelsDir)) {
  if (/^\d{3}\.json$/.test(name) && Number(name.slice(0, 3)) > preserveThrough) {
    await fs.rm(path.join(levelsDir, name));
  }
}
for (const doc of generated) {
  await fs.writeFile(path.join(levelsDir, doc.file), stableJson(doc.data));
}

const artifacts = buildArtifacts(documents);
await fs.writeFile(path.join(vocabularyDir, "index.json"), stableJson(artifacts.index));
await fs.writeFile(path.join(vocabularyDir, "lookup.json"), stableJson(artifacts.lookup));

const report = {
  version: 3,
  requestedTarget: target,
  minimum,
  preservedEntries: preservedCount,
  rankingHeadwords: ranking.length,
  trustedCommonCandidates: eligible.length,
  selectedAutomaticEntries: selected.length,
  totalEntries: total,
  selectedRankRange: selected.length ? {
    first: Math.min(...selected.map((entry) => entry.wordfreqRank)),
    last: Math.max(...selected.map((entry) => entry.wordfreqRank)),
  } : null,
  skipped,
  levelCounts: documents.map(({ data }) => ({ level: data.level, count: data.entries.length })),
};
const reportFile = path.join(root, ".cache", "vocabulary-build-report.json");
await fs.mkdir(path.dirname(reportFile), { recursive: true });
await fs.writeFile(reportFile, stableJson(report));

console.log(`Built ${total} trusted common-word entries across ${PLANNED_LEVELS} levels (${preservedCount} preserved, ${selected.length} automatic).`);
console.log(`wordfreq ranking: ${ranking.length}; trusted matches: ${eligible.length}; selected max rank: ${report.selectedRankRange?.last ?? "n/a"}.`);
console.log(`Build report: ${reportFile}`);
