import fs from "node:fs/promises";
import path from "node:path";

export const PLANNED_LEVELS = 100;

export function normalizeEnglish(value) {
  return value.normalize("NFKC").trim().toLowerCase().replace(/\s+/g, " ");
}

export async function readLevels(vocabularyDir) {
  const levelsDir = path.join(vocabularyDir, "levels");
  const names = (await fs.readdir(levelsDir))
    .filter((name) => /^\d{3}\.json$/.test(name))
    .sort();

  const documents = [];
  for (const name of names) {
    const raw = await fs.readFile(path.join(levelsDir, name), "utf8");
    documents.push({ file: name, data: JSON.parse(raw) });
  }
  return documents;
}

export function validateLevels(documents) {
  const errors = [];
  const ids = new Map();
  const english = new Map();
  const seenLevels = new Set();
  let totalEntries = 0;

  for (const { file, data } of documents) {
    if (data === null || typeof data !== "object" || Array.isArray(data)) {
      errors.push(`${file}: root must be an object`);
      continue;
    }

    const expectedLevel = Number(file.slice(0, 3));
    if (data.version !== 1) errors.push(`${file}: version must be 1`);
    if (!Number.isInteger(data.level) || data.level < 1 || data.level > PLANNED_LEVELS) {
      errors.push(`${file}: level must be an integer from 1 to ${PLANNED_LEVELS}`);
    } else {
      if (data.level !== expectedLevel) {
        errors.push(`${file}: level ${data.level} does not match filename ${expectedLevel}`);
      }
      if (seenLevels.has(data.level)) {
        errors.push(`${file}: duplicate level ${data.level}`);
      }
      seenLevels.add(data.level);
    }
    if (typeof data.label !== "string" || data.label.trim() === "") {
      errors.push(`${file}: label is required`);
    }
    if (!Array.isArray(data.entries) || data.entries.length === 0) {
      errors.push(`${file}: entries must be a non-empty array`);
      continue;
    }

    for (let index = 0; index < data.entries.length; index++) {
      const entry = data.entries[index];
      const at = `${file}:entries[${index}]`;
      totalEntries++;

      if (entry === null || typeof entry !== "object" || Array.isArray(entry)) {
        errors.push(`${at}: entry must be an object`);
        continue;
      }

      const allowedFields = new Set(["id", "en", "vi", "ipa"]);
      for (const field of Object.keys(entry)) {
        if (!allowedFields.has(field)) {
          errors.push(`${at}: unsupported field ${field}`);
        }
      }

      for (const field of ["id", "en", "vi", "ipa"]) {
        if (typeof entry[field] !== "string" || entry[field].trim() === "") {
          errors.push(`${at}: ${field} is required`);
        }
      }

      if (typeof entry.id === "string") {
        if (!/^L\d{3}-\d{3,}$/.test(entry.id)) {
          errors.push(`${at}: id must match Lxxx-xxx`);
        } else {
          const expectedPrefix = `L${String(expectedLevel).padStart(3, "0")}-`;
          if (!entry.id.startsWith(expectedPrefix)) {
            errors.push(`${at}: id must start with ${expectedPrefix}`);
          }
        }
      }
      if (
        typeof entry.ipa === "string" &&
        (!entry.ipa.trim().startsWith("/") || !entry.ipa.trim().endsWith("/"))
      ) {
        errors.push(`${at}: ipa must be wrapped in /.../`);
      }

      if (typeof entry.id === "string") {
        const existing = ids.get(entry.id);
        if (existing !== undefined) errors.push(`${at}: duplicate id ${entry.id} (also ${existing})`);
        else ids.set(entry.id, at);
      }

      if (typeof entry.en === "string" && entry.en.trim() !== "") {
        const key = normalizeEnglish(entry.en);
        const existing = english.get(key);
        if (existing !== undefined) errors.push(`${at}: duplicate English "${entry.en}" (also ${existing})`);
        else english.set(key, at);
      }
    }
  }

  if (seenLevels.size > 0) {
    const highestLevel = Math.max(...seenLevels);
    for (let level = 1; level <= highestLevel; level++) {
      if (!seenLevels.has(level)) {
        errors.push(`missing level file for level ${level}`);
      }
    }
  }

  return { errors, totalEntries };
}

export function buildArtifacts(documents) {
  const levels = [...documents].sort((a, b) => a.data.level - b.data.level);
  const lookupEntries = {};
  let totalEntries = 0;
  let maxWordCount = 1;

  for (const { data } of levels) {
    for (const entry of data.entries) {
      const key = normalizeEnglish(entry.en);
      lookupEntries[key] = data.level;
      maxWordCount = Math.max(maxWordCount, key.split(" ").length);
      totalEntries++;
    }
  }

  return {
    index: {
      version: 1,
      plannedLevels: PLANNED_LEVELS,
      availableLevels: levels.length,
      totalEntries,
      levels: levels.map(({ file, data }) => ({
        level: data.level,
        label: data.label,
        file: `levels/${file}`,
        count: data.entries.length,
      })),
    },
    lookup: {
      version: 1,
      totalEntries,
      maxWordCount,
      entries: lookupEntries,
    },
  };
}

export function stableJson(value) {
  return JSON.stringify(value, null, 2) + "\n";
}
