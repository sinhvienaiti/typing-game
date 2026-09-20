import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { normalizeEnglish } from "./vocabulary-core.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

function getArg(name, fallback) {
  const index = process.argv.indexOf(name);
  if (index === -1) return fallback;
  const value = process.argv[index + 1];
  if (value === undefined || value.startsWith("--")) {
    throw new Error(`${name} requires a value`);
  }
  return path.resolve(value);
}

const sourceRoot = path.join(root, ".cache", "vocabulary-sources");
const dictionaryDir = getArg(
  "--dictionary-dir",
  path.join(sourceRoot, "thichhoc-dict", "dict-en-vi", "data", "entries"),
);
const cefrFile = getArg(
  "--cefr",
  path.join(sourceRoot, "olp-en-cefrj", "cefrj-vocabulary-profile-1.5.csv"),
);
const advancedCefrFile = getArg(
  "--cefr-advanced",
  path.join(sourceRoot, "olp-en-cefrj", "octanove-vocabulary-profile-c1c2-1.0.csv"),
);
const outputFile = getArg(
  "--output",
  path.join(root, ".cache", "vocabulary-candidates.json"),
);

const POS_TO_CEFR = {
  n: "noun",
  v: "verb",
  adj: "adjective",
  adv: "adverb",
  prep: "preposition",
  conj: "conjunction",
  pron: "pronoun",
  det: "determiner",
  intj: "interjection",
};

const CEFR_RANK = { A1: 1, A2: 2, B1: 3, B2: 4, C1: 5, C2: 6 };
const LEVEL_RANGE = {
  A1: [1, 12],
  A2: [13, 28],
  B1: [29, 46],
  B2: [47, 65],
  C1: [66, 82],
  C2: [83, 94],
};

function parseCsv(text) {
  const rows = [];
  let row = [];
  let field = "";
  let quoted = false;

  for (let index = 0; index < text.length; index++) {
    const char = text[index];
    if (quoted) {
      if (char === '"') {
        if (text[index + 1] === '"') {
          field += '"';
          index++;
        } else {
          quoted = false;
        }
      } else {
        field += char;
      }
      continue;
    }

    if (char === '"') quoted = true;
    else if (char === ",") {
      row.push(field);
      field = "";
    } else if (char === "\n") {
      row.push(field);
      rows.push(row);
      row = [];
      field = "";
    } else if (char !== "\r") {
      field += char;
    }
  }

  if (field.length > 0 || row.length > 0) {
    row.push(field);
    rows.push(row);
  }
  return rows;
}

function spellingDifficulty(value) {
  const letters = value.replace(/[^a-z]/g, "");
  const words = value.split(" ").length;
  let score = Math.max(0, letters.length - 5) * 0.45 + Math.max(0, words - 1) * 1.5;
  if (/(ough|augh|eigh|ght|tion|sion|ture|wr|kn|mb)/.test(value)) score += 2;
  return Number(Math.min(10, score).toFixed(2));
}

function pronunciationDifficulty(ipa) {
  const body = ipa.replace(/[\/ˈˌ .-]/g, "");
  let score = Math.max(0, body.length - 4) * 0.25;
  if (/[θðʒŋɹɝɚ]/.test(ipa)) score += 1;
  if ((ipa.match(/[ˈˌ]/g) ?? []).length > 1) score += 1;
  return Number(Math.min(10, score).toFixed(2));
}

function earliestCefr(values) {
  return values
    .filter((value) => CEFR_RANK[value] !== undefined)
    .sort((a, b) => CEFR_RANK[a] - CEFR_RANK[b])[0] ?? null;
}

async function loadCefr(files) {
  const map = new Map();
  for (const file of files) {
    let raw;
    try {
      raw = await fs.readFile(file, "utf8");
    } catch (error) {
      if (error?.code === "ENOENT" && file === advancedCefrFile) continue;
      throw error;
    }

    const rows = parseCsv(raw);
    const header = rows.shift() ?? [];
    const headwordIndex = header.findIndex((value) => value.toLowerCase() === "headword");
    const posIndex = header.findIndex((value) => value.toLowerCase() === "pos");
    const cefrIndex = header.findIndex((value) => value.toLowerCase() === "cefr");
    if (headwordIndex < 0 || posIndex < 0 || cefrIndex < 0) {
      throw new Error(`Unsupported CEFR CSV header in ${file}`);
    }

    for (const row of rows) {
      const headword = normalizeEnglish(row[headwordIndex] ?? "");
      const pos = (row[posIndex] ?? "").trim().toLowerCase();
      const cefr = (row[cefrIndex] ?? "").trim().toUpperCase();
      if (!headword || !pos || CEFR_RANK[cefr] === undefined) continue;
      const key = `${headword}\t${pos}`;
      const previous = map.get(key);
      if (previous === undefined || CEFR_RANK[cefr] < CEFR_RANK[previous]) {
        map.set(key, cefr);
      }
    }
  }
  return map;
}

async function loadDictionary(cefrMap) {
  const names = (await fs.readdir(dictionaryDir))
    .filter((name) => name.endsWith(".jsonl"))
    .sort();
  const grouped = new Map();

  for (const name of names) {
    const raw = await fs.readFile(path.join(dictionaryDir, name), "utf8");
    const lines = raw.split("\n");
    for (let lineNumber = 0; lineNumber < lines.length; lineNumber++) {
      const line = lines[lineNumber].trim();
      if (!line) continue;

      let source;
      try {
        source = JSON.parse(line);
      } catch {
        throw new Error(`${name}:${lineNumber + 1}: invalid JSON`);
      }

      if (source.lang !== "en-vi") continue;
      const en = normalizeEnglish(String(source.headword ?? ""));
      const pos = String(source.pos ?? "").trim();
      const ipa = String(source.pron ?? "").trim();
      const senses = Array.isArray(source.senses_vi)
        ? [...new Set(source.senses_vi.map((value) => String(value).trim()).filter(Boolean))]
        : [];

      if (!en || !/^[a-z][a-z' -]*$/.test(en)) continue;
      if (!ipa.startsWith("/") || !ipa.endsWith("/") || senses.length === 0) continue;

      const cefrPos = POS_TO_CEFR[pos];
      const cefr = cefrPos === undefined ? null : cefrMap.get(`${en}\t${cefrPos}`) ?? null;
      const option = {
        pos,
        vi: senses.slice(0, 3),
        ipa,
        cefr,
        frequency: Number(source.freq) || 0,
        source: String(source.source ?? ""),
      };

      const existing = grouped.get(en) ?? [];
      existing.push(option);
      grouped.set(en, existing);
    }
  }
  return grouped;
}

function buildCandidates(grouped) {
  const candidates = [];
  for (const [en, options] of grouped) {
    options.sort((a, b) => b.frequency - a.frequency || a.pos.localeCompare(b.pos));
    const cefr = earliestCefr(options.map((option) => option.cefr));
    const frequency = Math.max(...options.map((option) => option.frequency));
    const spelling = spellingDifficulty(en);
    const pronunciation = Math.min(
      ...options.map((option) => pronunciationDifficulty(option.ipa)),
    );

    candidates.push({
      en,
      cefr,
      frequency,
      spellingDifficulty: spelling,
      pronunciationDifficulty: pronunciation,
      proposedLevel: null,
      reviewRequired: true,
      reviewChecks: [
        "usefulness",
        "Vietnamese meaning",
        "part of speech",
        "IPA/heteronym",
        "abstractness",
        "technical vs general balance",
      ],
      options,
    });
  }

  for (const cefr of Object.keys(LEVEL_RANGE)) {
    const group = candidates
      .filter((candidate) => candidate.cefr === cefr)
      .sort((a, b) => {
        const scoreA =
          a.spellingDifficulty + a.pronunciationDifficulty - a.frequency * 4;
        const scoreB =
          b.spellingDifficulty + b.pronunciationDifficulty - b.frequency * 4;
        return scoreA - scoreB || a.en.localeCompare(b.en);
      });
    const [minLevel, maxLevel] = LEVEL_RANGE[cefr];
    const span = maxLevel - minLevel + 1;

    for (let index = 0; index < group.length; index++) {
      const offset = Math.min(
        span - 1,
        Math.floor((index * span) / Math.max(1, group.length)),
      );
      group[index].proposedLevel = minLevel + offset;
    }
  }

  return candidates.sort((a, b) => {
    const levelA = a.proposedLevel ?? 101;
    const levelB = b.proposedLevel ?? 101;
    return levelA - levelB || b.frequency - a.frequency || a.en.localeCompare(b.en);
  });
}

const cefrMap = await loadCefr([cefrFile, advancedCefrFile]);
const grouped = await loadDictionary(cefrMap);
const candidates = buildCandidates(grouped);

await fs.mkdir(path.dirname(outputFile), { recursive: true });
await fs.writeFile(
  outputFile,
  JSON.stringify(
    {
      version: 1,
      generatedAt: new Date().toISOString(),
      note:
        "Review artifact only. Never copy candidates into level files without manual VI/IPA/POS/usefulness review.",
      sources: {
        dictionary: dictionaryDir,
        cefr: cefrFile,
        cefrAdvanced: advancedCefrFile,
      },
      total: candidates.length,
      candidates,
    },
    null,
    2,
  ) + "\n",
);

console.log(`Prepared ${candidates.length} review candidates: ${outputFile}`);
