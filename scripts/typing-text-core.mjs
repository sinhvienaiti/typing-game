import fs from "node:fs/promises";
import path from "node:path";

export const PLANNED_LEVELS = 100;
export const MIN_PASSAGES_PER_LEVEL = 15;
export const MIN_WORDS_PER_PASSAGE = 250;
export const MAX_WORDS_PER_PASSAGE = 300;
export const MIN_TARGET_WORDS = 20;
export const MAX_TARGET_WORDS = 30;

const PASSAGE_FIELDS = [
  "id",
  "topic",
  "style",
  "setting",
  "tone",
  "targetWords",
  "wordCount",
  "text",
];

export function expectedCefr(level) {
  if (level <= 12) return "A1";
  if (level <= 28) return "A2";
  if (level <= 46) return "B1";
  if (level <= 65) return "B2";
  if (level <= 82) return "C1";
  if (level <= 94) return "C2";
  return "Advanced";
}

export function stableJson(value) {
  return JSON.stringify(value, null, 2) + "\n";
}

export function countWords(text) {
  return text.match(/[A-Za-z]+(?:'[A-Za-z]+)?/g)?.length ?? 0;
}

export function normalizeText(text) {
  return text.toLocaleLowerCase("en-US").replace(/\s+/g, " ").trim();
}

function allowedKeys(value, fields) {
  const keys = Object.keys(value).sort();
  const expected = [...fields].sort();
  return keys.length === expected.length && keys.every((key, index) => key === expected[index]);
}

function hasValidTypingCharacters(text) {
  return /^[A-Za-z ,.' ]+$/.test(text);
}

function validateCapitalization(text) {
  let sentenceStart = true;

  for (const character of text) {
    if (/[A-Za-z]/.test(character)) {
      if (sentenceStart) {
        if (character !== character.toUpperCase()) return false;
        sentenceStart = false;
      } else if (character !== character.toLowerCase()) {
        return false;
      }
      continue;
    }

    if (character === ".") sentenceStart = true;
  }

  return true;
}

function targetAppears(text, target) {
  const normalizedTarget = normalizeText(target);
  if (normalizedTarget === "") return false;
  const escaped = normalizedTarget
    .replace(/[.*+?^$()|[\]\\{}]/g, "\\$&")
    .replace(/ +/g, "\\s+");
  const regex = new RegExp(`(^|[^a-z])${escaped}(?=$|[^a-z])`, "i");
  return regex.test(normalizeText(text));
}

function passageSentences(text) {
  return text
    .split(".")
    .map((sentence) => sentence.trim())
    .filter(Boolean);
}

function tokenNgrams(text, size) {
  const tokens = normalizeText(text).match(/[a-z]+(?:'[a-z]+)?/g) ?? [];
  const grams = [];
  for (let index = 0; index + size <= tokens.length; index++) {
    grams.push(tokens.slice(index, index + size).join(" "));
  }
  return grams;
}

export async function readTypingLevels(typingTextDir) {
  const levelsDir = path.join(typingTextDir, "levels");
  let names;
  try {
    names = await fs.readdir(levelsDir);
  } catch (error) {
    if (error?.code === "ENOENT") return [];
    throw error;
  }

  const jsonFiles = names.filter((name) => name.endsWith(".json")).sort();
  const documents = [];

  for (const filename of jsonFiles) {
    const filePath = path.join(levelsDir, filename);
    let data;
    try {
      data = JSON.parse(await fs.readFile(filePath, "utf8"));
    } catch (error) {
      throw new Error(`${filename}: invalid JSON: ${error.message}`);
    }
    documents.push({ filename, filePath, data });
  }

  return documents;
}

async function vocabularyForLevel(vocabularyDir, level) {
  const filename = `${String(level).padStart(3, "0")}.json`;
  const filePath = path.join(vocabularyDir, "levels", filename);
  const data = JSON.parse(await fs.readFile(filePath, "utf8"));
  if (!Array.isArray(data.entries)) {
    throw new Error(`Vocabulary level ${filename} has no entries array`);
  }
  return data.entries;
}

export async function validateTypingLevels(documents, vocabularyDir) {
  const errors = [];
  const warnings = [];
  const passageIds = new Set();
  const exactPassages = new Map();
  const exactSentences = new Map();
  const longPhrases = new Map();
  const similarityPassages = [];
  const fiveGramOwners = new Map();
  const levelReports = [];
  let totalPassages = 0;
  let totalWords = 0;

  const seenLevels = new Set();

  for (const { filename, data } of documents) {
    const filenameMatch = /^(\d{3})\.json$/.exec(filename);
    if (filenameMatch === null) {
      errors.push(`${filename}: level filename must use NNN.json`);
      continue;
    }

    if (data === null || typeof data !== "object" || Array.isArray(data)) {
      errors.push(`${filename}: root must be an object`);
      continue;
    }

    if (!allowedKeys(data, ["version", "level", "cefr", "passages"])) {
      errors.push(`${filename}: root fields must be version, level, cefr, passages`);
    }

    const level = Number(data.level);
    if (!Number.isInteger(level) || level < 1 || level > PLANNED_LEVELS) {
      errors.push(`${filename}: level must be an integer from 1 to ${PLANNED_LEVELS}`);
      continue;
    }

    if (seenLevels.has(level)) errors.push(`${filename}: duplicate level ${level}`);
    seenLevels.add(level);

    if (Number(filenameMatch[1]) !== level) {
      errors.push(`${filename}: filename does not match level ${level}`);
    }
    if (data.version !== 1) errors.push(`${filename}: version must be 1`);

    const cefr = expectedCefr(level);
    if (data.cefr !== cefr) {
      errors.push(`${filename}: cefr must be ${cefr} for level ${level}`);
    }

    if (!Array.isArray(data.passages)) {
      errors.push(`${filename}: passages must be an array`);
      continue;
    }
    if (data.passages.length < MIN_PASSAGES_PER_LEVEL) {
      errors.push(`${filename}: requires at least ${MIN_PASSAGES_PER_LEVEL} passages`);
    }

    let vocabulary;
    try {
      vocabulary = await vocabularyForLevel(vocabularyDir, level);
    } catch (error) {
      errors.push(`${filename}: cannot load vocabulary level: ${error.message}`);
      continue;
    }

    const vocabularyMap = new Map(
      vocabulary.map((entry) => [normalizeText(entry.en), entry]),
    );
    const targeted = new Set();
    let levelWords = 0;

    for (let passageIndex = 0; passageIndex < data.passages.length; passageIndex++) {
      const passage = data.passages[passageIndex];
      const label = `${filename} passage ${passageIndex + 1}`;

      if (passage === null || typeof passage !== "object" || Array.isArray(passage)) {
        errors.push(`${label}: must be an object`);
        continue;
      }
      if (!allowedKeys(passage, PASSAGE_FIELDS)) {
        errors.push(`${label}: passage fields do not match the contract`);
      }

      const expectedId = `L${String(level).padStart(3, "0")}-P${String(passageIndex + 1).padStart(3, "0")}`;
      if (passage.id !== expectedId) {
        errors.push(`${label}: id must be ${expectedId}`);
      }
      if (typeof passage.id === "string") {
        if (passageIds.has(passage.id)) errors.push(`${label}: duplicate passage id ${passage.id}`);
        passageIds.add(passage.id);
      }

      for (const field of ["topic", "style", "setting", "tone"]) {
        if (typeof passage[field] !== "string" || passage[field].trim() === "") {
          errors.push(`${label}: ${field} must be a non-empty string`);
        }
      }

      if (typeof passage.text !== "string" || passage.text.trim() === "") {
        errors.push(`${label}: text must be a non-empty string`);
        continue;
      }

      const text = passage.text;
      const actualWordCount = countWords(text);
      levelWords += actualWordCount;
      totalWords += actualWordCount;
      totalPassages++;

      if (actualWordCount < MIN_WORDS_PER_PASSAGE || actualWordCount > MAX_WORDS_PER_PASSAGE) {
        errors.push(`${label}: word count ${actualWordCount} must be ${MIN_WORDS_PER_PASSAGE}-${MAX_WORDS_PER_PASSAGE}`);
      }
      if (passage.wordCount !== actualWordCount) {
        errors.push(`${label}: wordCount ${passage.wordCount} does not match actual ${actualWordCount}`);
      }

      if (!hasValidTypingCharacters(text)) {
        errors.push(`${label}: text contains forbidden typing characters`);
      }
      if (/\s{2,}/.test(text)) errors.push(`${label}: repeated whitespace is not allowed`);
      if (/\s[,.]/.test(text)) errors.push(`${label}: spaces before comma or period are not allowed`);
      if (/[,.](?! |$)/.test(text)) errors.push(`${label}: comma or period must be followed by one space or end of text`);
      if (!text.endsWith(".")) errors.push(`${label}: text must end with a period`);
      if (!validateCapitalization(text)) {
        errors.push(`${label}: only the first alphabetic character after a period may be uppercase`);
      }

      if (!Array.isArray(passage.targetWords)) {
        errors.push(`${label}: targetWords must be an array`);
      } else {
        if (passage.targetWords.length < MIN_TARGET_WORDS || passage.targetWords.length > MAX_TARGET_WORDS) {
          errors.push(`${label}: targetWords must contain ${MIN_TARGET_WORDS}-${MAX_TARGET_WORDS} entries`);
        }

        const uniqueTargets = new Set();
        for (const target of passage.targetWords) {
          if (typeof target !== "string" || target.trim() === "") {
            errors.push(`${label}: every target word must be a non-empty string`);
            continue;
          }

          const normalized = normalizeText(target);
          if (uniqueTargets.has(normalized)) {
            errors.push(`${label}: duplicate target word "${target}"`);
            continue;
          }
          uniqueTargets.add(normalized);

          if (!vocabularyMap.has(normalized)) {
            errors.push(`${label}: target word "${target}" is not in vocabulary level ${level}`);
            continue;
          }

          targeted.add(normalized);
          if (!targetAppears(text, target)) {
            errors.push(`${label}: target word "${target}" does not appear in the passage text`);
          }
        }
      }

      const normalizedPassage = normalizeText(text);
      const previousPassage = exactPassages.get(normalizedPassage);
      if (previousPassage !== undefined) {
        errors.push(`${label}: exact duplicate of ${previousPassage}`);
      } else {
        exactPassages.set(normalizedPassage, label);
      }

      for (const sentence of passageSentences(text)) {
        if (countWords(sentence) < 8) continue;
        const normalizedSentence = normalizeText(sentence);
        const previousSentence = exactSentences.get(normalizedSentence);
        if (previousSentence !== undefined) {
          errors.push(`${label}: repeated substantial sentence also used in ${previousSentence}`);
        } else {
          exactSentences.set(normalizedSentence, label);
        }
      }

      const passageGrams = new Set(tokenNgrams(text, 8));
      for (const gram of passageGrams) {
        const previous = longPhrases.get(gram);
        if (previous !== undefined && previous !== label) {
          warnings.push(`${label}: repeated 8-word phrase also appears in ${previous}: "${gram}"`);
        } else {
          longPhrases.set(gram, label);
        }
      }

      const fiveGrams = new Set(tokenNgrams(text, 5));
      const overlapCounts = new Map();
      for (const gram of fiveGrams) {
        for (const ownerIndex of fiveGramOwners.get(gram) ?? []) {
          overlapCounts.set(
            ownerIndex,
            (overlapCounts.get(ownerIndex) ?? 0) + 1,
          );
        }
      }

      for (const [ownerIndex, intersection] of overlapCounts) {
        const previous = similarityPassages[ownerIndex];
        if (previous === undefined) continue;
        const union = fiveGrams.size + previous.grams.size - intersection;
        const similarity = union === 0 ? 0 : intersection / union;
        const threshold = previous.level === level ? 0.25 : 0.35;
        if (similarity >= threshold) {
          warnings.push(
            `${label}: ${(similarity * 100).toFixed(1)}% 5-gram similarity with ${previous.label}`,
          );
        }
      }

      const ownerIndex = similarityPassages.length;
      similarityPassages.push({ label, level, grams: fiveGrams });
      for (const gram of fiveGrams) {
        const owners = fiveGramOwners.get(gram) ?? [];
        owners.push(ownerIndex);
        fiveGramOwners.set(gram, owners);
      }
    }

    const coverage = vocabulary.length === 0 ? 0 : targeted.size / vocabulary.length;
    levelReports.push({
      level,
      cefr,
      passageCount: data.passages.length,
      wordCount: levelWords,
      vocabularyCount: vocabulary.length,
      targetedCount: targeted.size,
      coverage,
    });
  }

  if (documents.length > 0) {
    const sortedLevels = [...seenLevels].sort((a, b) => a - b);
    const maxLevel = sortedLevels.at(-1) ?? 0;
    for (let level = 1; level <= maxLevel; level++) {
      if (!seenLevels.has(level)) {
        errors.push(`Missing typing-text level ${String(level).padStart(3, "0")}.json`);
      }
    }
  }

  return { errors, warnings, levelReports, totalPassages, totalWords };
}

export function buildIndex(documents) {
  const levels = documents
    .map(({ filename, data }) => ({
      level: data.level,
      cefr: data.cefr,
      file: `levels/${filename}`,
      passageCount: Array.isArray(data.passages) ? data.passages.length : 0,
      wordCount: Array.isArray(data.passages)
        ? data.passages.reduce(
            (sum, passage) => sum + (Number.isInteger(passage.wordCount) ? passage.wordCount : 0),
            0,
          )
        : 0,
    }))
    .sort((a, b) => a.level - b.level);

  return {
    version: 1,
    plannedLevels: PLANNED_LEVELS,
    availableLevels: levels.length,
    totalPassages: levels.reduce((sum, level) => sum + level.passageCount, 0),
    totalWords: levels.reduce((sum, level) => sum + level.wordCount, 0),
    levels,
  };
}
