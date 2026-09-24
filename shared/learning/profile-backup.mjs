import {
  createEmptyLearningProfile,
  migrateLearningProfile,
} from "./core.mjs";

export const LEARNING_BACKUP_FORMAT = "typing-game-learning-profile";
export const LEARNING_BACKUP_VERSION = 1;

const ENTITY_TYPES = new Set(["vocabulary", "grammar", "sentence"]);
const REQUIRED_NUMBERS = [
  "attempts",
  "correct",
  "wrong",
  "hints",
  "replays",
  "responseSamples",
  "correctStreak",
  "mastery",
  "reviewPriority",
];

function plainObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

function validIsoOrNull(value) {
  return value === null ||
    (typeof value === "string" && Number.isFinite(Date.parse(value)));
}

function requireFiniteNonNegative(record, field) {
  const value = record[field];
  if (
    typeof value !== "number" ||
    !Number.isFinite(value) ||
    value < 0
  ) {
    throw new TypeError(`learning record ${field} is invalid`);
  }
}

function validateSamples(value, field) {
  if (!Array.isArray(value)) {
    throw new TypeError(`learning record ${field} is invalid`);
  }
  if (value.length > 8) {
    throw new TypeError(`learning record ${field} exceeds the history bound`);
  }
  for (const sample of value) {
    if (!plainObject(sample)) {
      throw new TypeError(`learning record ${field} contains an invalid sample`);
    }
  }
}

function validateRecord(entityType, key, record) {
  if (!plainObject(record)) {
    throw new TypeError(`learning record ${key} is invalid`);
  }

  for (const field of REQUIRED_NUMBERS) {
    requireFiniteNonNegative(record, field);
  }

  if (
    record.avgResponseMs !== null &&
    (typeof record.avgResponseMs !== "number" ||
      !Number.isFinite(record.avgResponseMs) ||
      record.avgResponseMs < 0)
  ) {
    throw new TypeError("learning record avgResponseMs is invalid");
  }

  for (const field of [
    "lastSeenAt",
    "lastCorrectAt",
    "lastWrongAt",
    "nextReviewAt",
  ]) {
    if (!validIsoOrNull(record[field])) {
      throw new TypeError(`learning record ${field} is invalid`);
    }
  }

  if (
    !Array.isArray(record.sourceGames) ||
    record.sourceGames.some(
      (game) => typeof game !== "string" || game.trim() === "",
    )
  ) {
    throw new TypeError("learning record sourceGames is invalid");
  }

  const idField =
    entityType === "vocabulary"
      ? "wordKey"
      : entityType === "grammar"
        ? "grammarId"
        : "sentenceId";
  if (
    typeof record[idField] !== "string" ||
    record[idField].normalize("NFC").trim() !== key
  ) {
    throw new TypeError(`learning record ${idField} does not match its key`);
  }

  validateSamples(record.recentMistakes ?? [], "recentMistakes");

  if (entityType === "sentence") {
    validateSamples(record.recentAnswers ?? [], "recentAnswers");
  }

  if (
    (entityType === "grammar" || entityType === "sentence") &&
    (!plainObject(record.errorTypes) ||
      Object.values(record.errorTypes).some(
        (count) =>
          typeof count !== "number" ||
          !Number.isFinite(count) ||
          count < 0,
      ))
  ) {
    throw new TypeError("learning record errorTypes is invalid");
  }
}

export function validateLearningProfile(profileInput) {
  const profile = migrateLearningProfile(profileInput);
  if (!Number.isFinite(Date.parse(profile.updatedAt))) {
    throw new TypeError("learning profile updatedAt is invalid");
  }

  for (const [entityType, collectionName] of [
    ["vocabulary", "vocabulary"],
    ["grammar", "grammar"],
    ["sentence", "sentences"],
  ]) {
    const collection = profile[collectionName];
    if (!plainObject(collection)) {
      throw new TypeError(`learning profile ${collectionName} is invalid`);
    }
    for (const [key, record] of Object.entries(collection)) {
      if (key.normalize("NFC").trim() !== key || key === "") {
        throw new TypeError("learning profile contains an invalid entity key");
      }
      validateRecord(entityType, key, record);
    }
  }

  return profile;
}

export function createLearningProfileBackup(
  profileInput,
  exportedAt = new Date().toISOString(),
) {
  const profile = validateLearningProfile(profileInput);
  return {
    format: LEARNING_BACKUP_FORMAT,
    version: LEARNING_BACKUP_VERSION,
    exportedAt: new Date(exportedAt).toISOString(),
    profile,
  };
}

export function parseLearningProfileBackup(input) {
  let value = input;
  if (typeof input === "string") {
    try {
      value = JSON.parse(input);
    } catch {
      throw new TypeError("Learning profile backup is not valid JSON");
    }
  }

  if (!plainObject(value)) {
    throw new TypeError("Learning profile backup must be an object");
  }

  if (value.format === LEARNING_BACKUP_FORMAT) {
    if (value.version !== LEARNING_BACKUP_VERSION) {
      throw new TypeError(
        `Unsupported learning backup version: ${String(value.version)}`,
      );
    }
    if (
      typeof value.exportedAt !== "string" ||
      !Number.isFinite(Date.parse(value.exportedAt))
    ) {
      throw new TypeError("Learning profile backup exportedAt is invalid");
    }
    return validateLearningProfile(value.profile);
  }

  if (value.version === 1) {
    return validateLearningProfile(value);
  }

  throw new TypeError("Unsupported learning profile backup format");
}

export function resetLearningProfileSelection(
  profileInput,
  entityTypes,
  updatedAt = new Date().toISOString(),
) {
  const profile = validateLearningProfile(profileInput);
  if (!Array.isArray(entityTypes) || entityTypes.length === 0) {
    throw new TypeError("Select at least one learning-history group to reset");
  }

  const selected = new Set(entityTypes);
  for (const entityType of selected) {
    if (!ENTITY_TYPES.has(entityType)) {
      throw new TypeError(`Unsupported learning-history group: ${String(entityType)}`);
    }
  }

  const next = structuredClone(profile);
  if (selected.has("vocabulary")) next.vocabulary = {};
  if (selected.has("grammar")) next.grammar = {};
  if (selected.has("sentence")) next.sentences = {};
  next.updatedAt = new Date(updatedAt).toISOString();
  return next;
}

export function resetAllLearningProfile(
  updatedAt = new Date().toISOString(),
) {
  return createEmptyLearningProfile(new Date(updatedAt).toISOString());
}

export function learningProfileCounts(profileInput) {
  const profile = validateLearningProfile(profileInput);
  return {
    vocabulary: Object.keys(profile.vocabulary).length,
    grammar: Object.keys(profile.grammar).length,
    sentence: Object.keys(profile.sentences).length,
    total:
      Object.keys(profile.vocabulary).length +
      Object.keys(profile.grammar).length +
      Object.keys(profile.sentences).length,
  };
}
