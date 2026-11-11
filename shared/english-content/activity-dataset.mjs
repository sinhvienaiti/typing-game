import { supportsEnglishActivity } from "./capabilities.mjs";

export const ENGLISH_ACTIVITY_DATASET_MESSAGE =
  "typing-game:english-content:v1:activity-dataset";

const GAME_CAPABILITY_IDS = Object.freeze({
  monkeytype: "monkeytype",
  "recall-typing": "recall",
  "vocab-shooter": "shooter",
  "karaoke-typing": "karaoke",
  "space-typing": "space",
});
const ENTITY_TYPES = new Set(["vocabulary", "grammar", "sentence"]);
const CEFR_LEVELS = new Set(["A1", "A2", "B1", "B2", "C1", "C2"]);
const GRADING_MODES = new Set(["exact-normalized", "closed-choice", "guided-self-check"]);
const LEARNING_FOCUSES = new Set([
  "typing-fluency",
  "recognition",
  "recall",
  "usage-discrimination",
  "comprehension",
  "production",
]);
const REQUEST_ID_PATTERN = /^[A-Za-z0-9._:-]{1,100}$/;

function plainObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}
function cleanText(value, field, maxLength = 2000) {
  if (typeof value !== "string") throw new TypeError(field + " must be a string");
  const cleaned = value.normalize("NFC").trim().replace(/\s+/g, " ");
  if (cleaned === "" || cleaned.length > maxLength) throw new TypeError(field + " is invalid");
  return cleaned;
}
function optionalText(value, field, maxLength = 2000) {
  if (value === undefined || value === null || value === "") return undefined;
  return cleanText(value, field, maxLength);
}
function capabilityId(gameId) {
  const id = GAME_CAPABILITY_IDS[gameId];
  if (id === undefined) throw new TypeError("English activity gameId is invalid");
  return id;
}

export function defaultEnglishActivityEntityType(activity) {
  return activity === "vocabulary"
    ? "vocabulary"
    : activity === "grammar-topic" || activity === "grammar-challenge"
      ? "grammar"
      : "sentence";
}

function parseAcceptedAnswers(value) {
  if (value === undefined) return undefined;
  if (!Array.isArray(value) || value.length === 0) {
    throw new TypeError("acceptedAnswers must be a non-empty array");
  }
  const seen = new Set();
  const out = [];
  for (const item of value) {
    const cleaned = cleanText(item, "acceptedAnswers[]");
    if (!seen.has(cleaned)) {
      seen.add(cleaned);
      out.push(cleaned);
    }
  }
  return out;
}

function parseNormalization(value) {
  if (value === undefined) return undefined;
  if (!plainObject(value)) throw new TypeError("normalization must be an object");
  const out = {};
  for (const flag of ["caseSensitive", "punctuationOptional", "contractionsEquivalent"]) {
    if (value[flag] !== undefined) {
      if (typeof value[flag] !== "boolean") throw new TypeError(`normalization.${flag} must be boolean`);
      out[flag] = value[flag];
    }
  }
  return Object.keys(out).length > 0 ? out : undefined;
}

export function parseEnglishActivityItem(value, activity) {
  if (!plainObject(value)) throw new TypeError("English activity item must be an object");
  const contentId = cleanText(value.contentId, "contentId", 200);
  const promptText = cleanText(value.promptText, "promptText");
  const answerText = cleanText(value.answerText, "answerText");
  const entityType = value.entityType ?? defaultEnglishActivityEntityType(activity);
  if (typeof entityType !== "string" || !ENTITY_TYPES.has(entityType)) {
    throw new TypeError("English activity entityType is invalid");
  }
  const defaultEntityId = entityType === "vocabulary"
    ? answerText.normalize("NFKC").toLocaleLowerCase("en-US")
    : contentId;
  const entityId = cleanText(value.entityId ?? defaultEntityId, "entityId", 200);
  if (entityType === "grammar" && !entityId.startsWith("gr.")) {
    throw new TypeError("Grammar activity entityId must use a gr.* id");
  }

  const meaningVi = optionalText(value.meaningVi, "meaningVi");
  const ipa = optionalText(value.ipa, "ipa", 300);
  const audioText = optionalText(value.audioText, "audioText");
  const acceptedAnswers = parseAcceptedAnswers(value.acceptedAnswers);
  const normalization = parseNormalization(value.normalization);

  if (value.gradingMode !== undefined && !GRADING_MODES.has(value.gradingMode)) {
    throw new TypeError("gradingMode is invalid");
  }
  if (value.cefr !== undefined && !CEFR_LEVELS.has(value.cefr)) {
    throw new TypeError("cefr is invalid");
  }
  if (value.learningFocus !== undefined && !LEARNING_FOCUSES.has(value.learningFocus)) {
    throw new TypeError("learningFocus is invalid");
  }
  if (
    value.targetConfidence !== undefined &&
    value.targetConfidence !== "verified" &&
    value.targetConfidence !== "unverified-rotational"
  ) {
    throw new TypeError("targetConfidence is invalid");
  }
  const packId = optionalText(value.packId, "packId", 120);
  const stage = optionalText(value.stage, "stage", 40);

  return {
    contentId,
    entityType,
    entityId,
    promptText,
    answerText,
    ...(meaningVi === undefined ? {} : { meaningVi }),
    ...(ipa === undefined ? {} : { ipa }),
    ...(audioText === undefined ? {} : { audioText }),
    ...(acceptedAnswers === undefined ? {} : { acceptedAnswers }),
    ...(value.gradingMode === undefined ? {} : { gradingMode: value.gradingMode }),
    ...(normalization === undefined ? {} : { normalization }),
    ...(value.cefr === undefined ? {} : { cefr: value.cefr }),
    ...(value.targetConfidence === undefined ? {} : { targetConfidence: value.targetConfidence }),
    ...(value.learningFocus === undefined ? {} : { learningFocus: value.learningFocus }),
    ...(packId === undefined ? {} : { packId }),
    ...(stage === undefined ? {} : { stage }),
  };
}

export function buildEnglishActivityDataset(
  gameId,
  activity,
  items,
  requestId,
  createdAt = new Date().toISOString(),
) {
  if (typeof gameId !== "string") throw new TypeError("English activity gameId is invalid");
  const capability = capabilityId(gameId);
  if (typeof activity !== "string" || !supportsEnglishActivity(capability, activity)) {
    throw new TypeError("English activity is not supported by " + gameId);
  }
  if (typeof requestId !== "string" || !REQUEST_ID_PATTERN.test(requestId)) {
    throw new TypeError("English activity requestId is invalid");
  }
  if (!Array.isArray(items) || items.length === 0 || items.length > 100) {
    throw new TypeError("English activity items must contain 1 to 100 records");
  }
  const parsed = items.map((item) => parseEnglishActivityItem(item, activity));
  const contentIds = new Set();
  for (const item of parsed) {
    if (contentIds.has(item.contentId)) throw new TypeError("English activity contentId is duplicated");
    contentIds.add(item.contentId);
  }
  return {
    version: 1,
    type: ENGLISH_ACTIVITY_DATASET_MESSAGE,
    requestId,
    createdAt: new Date(createdAt).toISOString(),
    gameId,
    activity,
    items: parsed,
  };
}

export function parseEnglishActivityDataset(value) {
  if (!plainObject(value) || value.type !== ENGLISH_ACTIVITY_DATASET_MESSAGE) return null;
  if (value.version !== 1) throw new TypeError("English activity dataset version is invalid");
  return buildEnglishActivityDataset(
    value.gameId,
    value.activity,
    value.items,
    value.requestId,
    value.createdAt,
  );
}
