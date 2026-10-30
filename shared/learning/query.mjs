import {
  calculateMastery,
  calculateReviewPriority,
  normalizeVocabularyKey,
  viewLearningProfile,
} from "./core.mjs";

export const REVIEW_SORTS = new Set([
  "smart-priority",
  "lowest-mastery",
  "most-mistakes",
  "recent-mistake",
  "oldest-review",
  "slowest-response",
  "most-attempts",
  "a-z",
  "z-a",
]);

const ENTITY_TYPES = new Set(["vocabulary", "grammar", "sentence"]);
export const LOOKUP_MAX_IDS = 200;
const PROTOTYPE_IDS = new Set(
  Object.getOwnPropertyNames(Object.prototype)
    .flatMap((id) => [id, normalizeVocabularyKey(id)]),
);
const PAGE_SIZES = new Set([10, 25, 50, 100]);
const STATUS_VALUES = new Set([
  "needs-review",
  "learning",
  "improving",
  "mastered",
]);

function plainObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

const SAMPLE_RESULTS = new Set(["correct", "wrong"]);

// LearningSample in core.d.mts: three strings, a known result and a boolean.
export function isLearningSample(sample) {
  return (
    plainObject(sample) &&
    typeof sample.occurredAt === "string" &&
    typeof sample.gameId === "string" &&
    typeof sample.activityType === "string" &&
    SAMPLE_RESULTS.has(sample.result) &&
    typeof sample.hintUsed === "boolean"
  );
}

// Rebuild each sample from the five contract fields; drop a whole sample
// with a wrong type instead of coercing it.
function contractSamples(samples) {
  if (!Array.isArray(samples)) return [];
  const result = [];
  for (const sample of samples) {
    if (!plainObject(sample)) continue;
    const projected = {
      occurredAt: sample.occurredAt,
      gameId: sample.gameId,
      activityType: sample.activityType,
      result: sample.result,
      hintUsed: sample.hintUsed,
    };
    if (isLearningSample(projected)) result.push(projected);
  }
  return result;
}

function optionalString(value, field, max = 200) {
  if (value === undefined || value === null || value === "") return undefined;
  if (typeof value !== "string") throw new TypeError(`${field} must be a string`);
  const result = value.trim();
  if (result.length > max) throw new TypeError(`${field} is too long`);
  return result === "" ? undefined : result;
}

function optionalNumber(value, field, min, max) {
  if (value === undefined || value === null) return undefined;
  if (!Number.isFinite(value) || value < min || value > max) {
    throw new TypeError(`${field} must be between ${min} and ${max}`);
  }
  return value;
}

function parseDate(value, field) {
  const text = optionalString(value, field, 64);
  if (text === undefined) return undefined;
  const timestamp = Date.parse(text);
  if (!Number.isFinite(timestamp)) {
    throw new TypeError(`${field} must be a date-time`);
  }
  return new Date(timestamp).toISOString();
}

export function parseLearningLookup(input) {
  if (
    !plainObject(input) ||
    (Object.getPrototypeOf(input) !== Object.prototype &&
      Object.getPrototypeOf(input) !== null)
  ) {
    throw new TypeError("learning lookup must be a plain object");
  }
  if (!ENTITY_TYPES.has(input.entityType)) {
    throw new TypeError("entityType is not supported");
  }
  if (
    !Array.isArray(input.entityIds) ||
    input.entityIds.length < 1 ||
    input.entityIds.length > LOOKUP_MAX_IDS
  ) {
    throw new TypeError(`entityIds must contain 1 to ${LOOKUP_MAX_IDS} ids`);
  }

  const ids = new Set();
  for (const value of input.entityIds) {
    if (typeof value !== "string") {
      throw new TypeError("entityIds must contain strings");
    }
    const trimmed = value.trim();
    if (trimmed.length > 200) throw new TypeError("entityId is too long");
    const id = input.entityType === "vocabulary"
      ? normalizeVocabularyKey(trimmed)
      : trimmed;
    if (id !== "") ids.add(id);
  }
  if (ids.size === 0) throw new TypeError("entityIds must contain a non-empty id");
  return { entityType: input.entityType, entityIds: [...ids] };
}

export function parseLearningQuery(input) {
  if (!plainObject(input)) throw new TypeError("learning query must be an object");

  const entityType = optionalString(input.entityType, "entityType", 32);
  if (entityType === undefined || !ENTITY_TYPES.has(entityType)) {
    throw new TypeError("entityType is not supported");
  }

  const page = input.page === undefined ? 1 : input.page;
  if (!Number.isInteger(page) || page < 1) {
    throw new TypeError("page must be a positive integer");
  }

  const pageSize = input.pageSize === undefined ? 25 : input.pageSize;
  if (!PAGE_SIZES.has(pageSize)) {
    throw new TypeError("pageSize must be one of 10, 25, 50, 100");
  }

  const sort = optionalString(input.sort, "sort", 40) ?? "smart-priority";
  if (!REVIEW_SORTS.has(sort)) throw new TypeError("sort is not supported");

  const rawFilters = input.filters === undefined ? {} : input.filters;
  if (!plainObject(rawFilters)) throw new TypeError("filters must be an object");

  const status = optionalString(rawFilters.status, "filters.status", 32);
  if (status !== undefined && !STATUS_VALUES.has(status)) {
    throw new TypeError("filters.status is not supported");
  }

  const sourceGame = optionalString(
    rawFilters.sourceGame,
    "filters.sourceGame",
    64,
  );
  const masteryMin = optionalNumber(
    rawFilters.masteryMin,
    "filters.masteryMin",
    0,
    100,
  );
  const masteryMax = optionalNumber(
    rawFilters.masteryMax,
    "filters.masteryMax",
    0,
    100,
  );
  const lastSeenFrom = parseDate(
    rawFilters.lastSeenFrom,
    "filters.lastSeenFrom",
  );
  const lastSeenTo = parseDate(
    rawFilters.lastSeenTo,
    "filters.lastSeenTo",
  );
  const lastWrongFrom = parseDate(
    rawFilters.lastWrongFrom,
    "filters.lastWrongFrom",
  );
  const lastWrongTo = parseDate(
    rawFilters.lastWrongTo,
    "filters.lastWrongTo",
  );
  const mistakeMin = optionalNumber(
    rawFilters.mistakeMin,
    "filters.mistakeMin",
    0,
    1_000_000,
  );
  const hintMin = optionalNumber(
    rawFilters.hintMin,
    "filters.hintMin",
    0,
    1_000_000,
  );
  const replayMin = optionalNumber(
    rawFilters.replayMin,
    "filters.replayMin",
    0,
    1_000_000,
  );
  const responseMsMin = optionalNumber(
    rawFilters.responseMsMin,
    "filters.responseMsMin",
    0,
    600_000,
  );
  const correctStreakMax = optionalNumber(
    rawFilters.correctStreakMax,
    "filters.correctStreakMax",
    0,
    1_000_000,
  );

  if (
    rawFilters.dueOnly !== undefined &&
    typeof rawFilters.dueOnly !== "boolean"
  ) {
    throw new TypeError("filters.dueOnly must be a boolean");
  }
  if (
    masteryMin !== undefined &&
    masteryMax !== undefined &&
    masteryMin > masteryMax
  ) {
    throw new TypeError(
      "filters.masteryMin must not exceed filters.masteryMax",
    );
  }
  if (
    lastSeenFrom !== undefined &&
    lastSeenTo !== undefined &&
    Date.parse(lastSeenFrom) > Date.parse(lastSeenTo)
  ) {
    throw new TypeError(
      "filters.lastSeenFrom must not be after filters.lastSeenTo",
    );
  }
  if (
    lastWrongFrom !== undefined &&
    lastWrongTo !== undefined &&
    Date.parse(lastWrongFrom) > Date.parse(lastWrongTo)
  ) {
    throw new TypeError(
      "filters.lastWrongFrom must not be after filters.lastWrongTo",
    );
  }

  return {
    entityType,
    page,
    pageSize,
    search:
      optionalString(input.search, "search", 200)?.toLocaleLowerCase() ?? "",
    sort,
    filters: {
      ...(status === undefined ? {} : { status }),
      ...(sourceGame === undefined ? {} : { sourceGame }),
      ...(masteryMin === undefined ? {} : { masteryMin }),
      ...(masteryMax === undefined ? {} : { masteryMax }),
      ...(rawFilters.dueOnly === undefined
        ? {}
        : { dueOnly: rawFilters.dueOnly }),
      ...(lastSeenFrom === undefined ? {} : { lastSeenFrom }),
      ...(lastSeenTo === undefined ? {} : { lastSeenTo }),
      ...(lastWrongFrom === undefined ? {} : { lastWrongFrom }),
      ...(lastWrongTo === undefined ? {} : { lastWrongTo }),
      ...(mistakeMin === undefined ? {} : { mistakeMin }),
      ...(hintMin === undefined ? {} : { hintMin }),
      ...(replayMin === undefined ? {} : { replayMin }),
      ...(responseMsMin === undefined ? {} : { responseMsMin }),
      ...(correctStreakMax === undefined ? {} : { correctStreakMax }),
    },
  };
}

function statusForMastery(mastery) {
  if (mastery < 40) return "needs-review";
  if (mastery < 70) return "learning";
  if (mastery < 90) return "improving";
  return "mastered";
}

function entityId(record, entityType) {
  if (entityType === "vocabulary") return record.wordKey;
  if (entityType === "grammar") return record.grammarId;
  return record.sentenceId;
}

function collectionFor(profile, entityType) {
  if (entityType === "vocabulary") return profile.vocabulary;
  if (entityType === "grammar") return profile.grammar;
  return profile.sentences;
}

function queryItem(record, entityType, now) {
  const mastery = calculateMastery(record, now);
  return {
    ...record,
    ...(record.recentSamples === undefined ? {} : {
      recentSamples: contractSamples(record.recentSamples),
    }),
    entityType,
    entityId: entityId(record, entityType),
    mastery,
    reviewPriority: calculateReviewPriority(record, now),
    status: statusForMastery(mastery),
  };
}

export function lookupLearningRecords(
  profileInput,
  lookupInput,
  now = new Date().toISOString(),
) {
  return lookupParsedLearningRecords(profileInput, parseLearningLookup(lookupInput), now);
}

// Accept only the result of parseLearningLookup; normalization may expand ids.
export function lookupParsedLearningRecords(
  profileInput,
  lookup,
  now = new Date().toISOString(),
) {
  const profile = viewLearningProfile(profileInput);
  const collection = collectionFor(profile, lookup.entityType);
  const items = [];
  for (const id of lookup.entityIds) {
    if (PROTOTYPE_IDS.has(id) || !Object.hasOwn(collection, id)) continue;
    const record = collection[id];
    items.push({
      recentSamples: [],
      ...queryItem(record, lookup.entityType, now),
    });
  }
  return { entityType: lookup.entityType, items };
}

function dateValue(value, fallback) {
  if (value == null) return fallback;
  const parsed = Date.parse(value);
  return Number.isFinite(parsed) ? parsed : fallback;
}

function compareItems(a, b, sort) {
  if (sort === "lowest-mastery") {
    return a.mastery - b.mastery || a.entityId.localeCompare(b.entityId);
  }
  if (sort === "most-mistakes") {
    return b.wrong - a.wrong || b.reviewPriority - a.reviewPriority;
  }
  if (sort === "recent-mistake") {
    return (
      dateValue(b.lastWrongAt, 0) - dateValue(a.lastWrongAt, 0) ||
      b.reviewPriority - a.reviewPriority
    );
  }
  if (sort === "oldest-review") {
    return (
      dateValue(a.lastCorrectAt, 0) - dateValue(b.lastCorrectAt, 0) ||
      b.reviewPriority - a.reviewPriority
    );
  }
  if (sort === "slowest-response") {
    return (
      (b.avgResponseMs ?? -1) - (a.avgResponseMs ?? -1) ||
      b.reviewPriority - a.reviewPriority
    );
  }
  if (sort === "most-attempts") {
    return b.attempts - a.attempts || b.reviewPriority - a.reviewPriority;
  }
  if (sort === "a-z") return a.entityId.localeCompare(b.entityId);
  if (sort === "z-a") return b.entityId.localeCompare(a.entityId);
  return (
    b.reviewPriority - a.reviewPriority ||
    a.entityId.localeCompare(b.entityId)
  );
}

export function queryLearningProfile(
  profileInput,
  queryInput,
  now = new Date().toISOString(),
) {
  const profile = viewLearningProfile(profileInput);
  const query = parseLearningQuery(queryInput);
  const nowMs = Date.parse(now);
  const source = Object.values(collectionFor(profile, query.entityType));

  const items = source
    .map((record) => queryItem(record, query.entityType, now))
    .filter((item) => {
      const filters = query.filters;
      if (
        query.search !== "" &&
        !item.entityId.toLocaleLowerCase().includes(query.search)
      ) {
        return false;
      }
      if (filters.status !== undefined && item.status !== filters.status) {
        return false;
      }
      if (
        filters.sourceGame !== undefined &&
        !item.sourceGames.includes(filters.sourceGame)
      ) {
        return false;
      }
      if (
        filters.masteryMin !== undefined &&
        item.mastery < filters.masteryMin
      ) {
        return false;
      }
      if (
        filters.masteryMax !== undefined &&
        item.mastery > filters.masteryMax
      ) {
        return false;
      }
      if (
        filters.dueOnly === true &&
        (item.nextReviewAt == null || Date.parse(item.nextReviewAt) > nowMs)
      ) {
        return false;
      }
      if (
        filters.lastSeenFrom !== undefined &&
        dateValue(item.lastSeenAt, -Infinity) <
          Date.parse(filters.lastSeenFrom)
      ) {
        return false;
      }
      if (
        filters.lastSeenTo !== undefined &&
        dateValue(item.lastSeenAt, Infinity) > Date.parse(filters.lastSeenTo)
      ) {
        return false;
      }
      if (
        filters.lastWrongFrom !== undefined &&
        dateValue(item.lastWrongAt, -Infinity) <
          Date.parse(filters.lastWrongFrom)
      ) {
        return false;
      }
      if (
        filters.lastWrongTo !== undefined &&
        dateValue(item.lastWrongAt, Infinity) > Date.parse(filters.lastWrongTo)
      ) {
        return false;
      }
      if (filters.mistakeMin !== undefined && item.wrong < filters.mistakeMin) {
        return false;
      }
      if (filters.hintMin !== undefined && item.hints < filters.hintMin) {
        return false;
      }
      if (filters.replayMin !== undefined && item.replays < filters.replayMin) {
        return false;
      }
      if (
        filters.responseMsMin !== undefined &&
        (item.avgResponseMs ?? 0) < filters.responseMsMin
      ) {
        return false;
      }
      if (
        filters.correctStreakMax !== undefined &&
        item.correctStreak > filters.correctStreakMax
      ) {
        return false;
      }
      return true;
    });

  items.sort((a, b) => compareItems(a, b, query.sort));

  const totalItems = items.length;
  const totalPages = Math.max(1, Math.ceil(totalItems / query.pageSize));
  const page = Math.min(query.page, totalPages);
  const start = (page - 1) * query.pageSize;

  return {
    items: items.slice(start, start + query.pageSize),
    page,
    pageSize: query.pageSize,
    totalItems,
    totalPages,
  };
}
