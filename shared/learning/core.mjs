export const LEARNING_EVENT_VERSION = 1;
export const LEARNING_PROFILE_VERSION = 1;
export const MAX_RECENT_SAMPLES = 8;

const ENTITY_TYPES = new Set(["vocabulary", "grammar", "sentence"]);
const RESULTS = new Set(["correct", "wrong"]);

export function normalizeVocabularyKey(value) {
  return value.normalize("NFKC").trim().replace(/\s+/g, " ").toLowerCase();
}

function isPlainObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

function assertNonEmptyString(value, field, maxLength = 2000) {
  if (typeof value !== "string" || value.trim() === "") {
    throw new TypeError(`${field} must be a non-empty string`);
  }
  const normalized = value.trim();
  if (normalized.length > maxLength) throw new TypeError(`${field} is too long`);
  return normalized;
}

function parseOptionalBoolean(value, field) {
  if (value === undefined) return false;
  if (typeof value !== "boolean") throw new TypeError(`${field} must be a boolean`);
  return value;
}

function parseOptionalString(value, field, maxLength = 2000) {
  if (value === undefined || value === null) return undefined;
  if (typeof value !== "string") throw new TypeError(`${field} must be a string`);
  const normalized = value.normalize("NFC").trim();
  if (normalized.length > maxLength) throw new TypeError(`${field} is too long`);
  return normalized === "" ? undefined : normalized;
}

function parseOccurredAt(value) {
  const occurredAt = assertNonEmptyString(value, "occurredAt");
  const time = Date.parse(occurredAt);
  if (!Number.isFinite(time)) throw new TypeError("occurredAt must be an ISO date-time");
  return new Date(time).toISOString();
}

export function parseLearningEvent(input) {
  if (!isPlainObject(input)) throw new TypeError("learning event must be an object");
  if (input.version !== LEARNING_EVENT_VERSION) {
    throw new TypeError(`learning event version must be ${LEARNING_EVENT_VERSION}`);
  }

  const entityType = assertNonEmptyString(input.entityType, "entityType", 32);
  if (!ENTITY_TYPES.has(entityType)) throw new TypeError("entityType is not supported");

  let entityId = assertNonEmptyString(input.entityId, "entityId", 200);
  entityId = entityType === "vocabulary" ? normalizeVocabularyKey(entityId) : entityId;
  if (entityId === "") throw new TypeError("entityId must not normalize to an empty value");

  const result = assertNonEmptyString(input.result, "result", 16);
  if (!RESULTS.has(result)) throw new TypeError("result must be correct or wrong");

  let responseMs;
  if (input.responseMs !== undefined && input.responseMs !== null) {
    if (!Number.isFinite(input.responseMs) || input.responseMs < 0) {
      throw new TypeError("responseMs must be a finite non-negative number");
    }
    responseMs = Math.round(input.responseMs);
  }

  const userAnswer = parseOptionalString(input.userAnswer, "userAnswer");
  const expectedAnswer = parseOptionalString(input.expectedAnswer, "expectedAnswer");
  const errorType = parseOptionalString(input.errorType, "errorType", 64);

  return {
    version: LEARNING_EVENT_VERSION,
    entityType,
    entityId,
    gameId: assertNonEmptyString(input.gameId, "gameId", 64),
    activityType: assertNonEmptyString(input.activityType, "activityType", 64),
    result,
    occurredAt: parseOccurredAt(input.occurredAt),
    ...(responseMs === undefined ? {} : { responseMs }),
    hintUsed: parseOptionalBoolean(input.hintUsed, "hintUsed"),
    replayUsed: parseOptionalBoolean(input.replayUsed, "replayUsed"),
    ...(userAnswer === undefined ? {} : { userAnswer }),
    ...(expectedAnswer === undefined ? {} : { expectedAnswer }),
    ...(errorType === undefined ? {} : { errorType }),
  };
}

export function createEmptyLearningProfile(updatedAt = new Date(0).toISOString()) {
  return {
    version: LEARNING_PROFILE_VERSION,
    updatedAt: new Date(updatedAt).toISOString(),
    vocabulary: {},
    grammar: {},
    sentences: {},
  };
}

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value));
}

function daysBetween(olderIso, newerIso) {
  if (olderIso == null) return Number.POSITIVE_INFINITY;
  return Math.max(0, (Date.parse(newerIso) - Date.parse(olderIso)) / 86_400_000);
}

function responseStrength(avgResponseMs) {
  if (avgResponseMs == null) return 5;
  if (avgResponseMs <= 1500) return 10;
  if (avgResponseMs <= 3000) return 7;
  if (avgResponseMs <= 5000) return 4;
  if (avgResponseMs <= 8000) return 2;
  return 0;
}

export function calculateMastery(record, now = record.lastSeenAt ?? new Date(0).toISOString()) {
  if (!record || record.attempts <= 0) return 0;

  const accuracy = (record.correct / record.attempts) * 55;
  const streak = Math.min(record.correctStreak, 5) * 4;
  const speed = responseStrength(record.avgResponseMs);
  const dependenceRatio = (record.hints + record.replays) / Math.max(1, record.attempts * 2);
  const independence = 10 * (1 - clamp(dependenceRatio, 0, 1));

  const daysSinceCorrect = daysBetween(record.lastCorrectAt, now);
  const recency = daysSinceCorrect <= 1 ? 5 : daysSinceCorrect <= 7 ? 3 : daysSinceCorrect <= 30 ? 1 : 0;

  return Math.round(clamp(accuracy + streak + speed + independence + recency, 0, 100));
}

function stalenessPressure(lastCorrectAt, now) {
  const days = daysBetween(lastCorrectAt, now);
  if (!Number.isFinite(days)) return 15;
  return clamp((days / 30) * 15, 0, 15);
}

function slowPressure(avgResponseMs) {
  if (avgResponseMs == null || avgResponseMs <= 2000) return 0;
  return clamp(((avgResponseMs - 2000) / 6000) * 5, 0, 5);
}

export function calculateReviewPriority(record, now = new Date().toISOString()) {
  if (!record || record.attempts <= 0) return 0;
  const mastery = calculateMastery(record, now);
  const weakness = (100 - mastery) * 0.55;
  const failure = Math.min(record.wrong, 5) * 4;
  const staleness = stalenessPressure(record.lastCorrectAt, now);
  const slowness = slowPressure(record.avgResponseMs);
  const dependence = clamp(((record.hints + record.replays) / Math.max(1, record.attempts)) * 5, 0, 5);
  return Math.round(clamp(weakness + failure + staleness + slowness + dependence, 0, 100));
}

export function calculateNextReviewAt(record, now = record.lastSeenAt ?? new Date(0).toISOString()) {
  const mastery = calculateMastery(record, now);
  const intervalDays = mastery < 40 ? 0 : mastery < 70 ? 1 : mastery < 90 ? 3 : 7;
  return new Date(Date.parse(now) + intervalDays * 86_400_000).toISOString();
}

function createBaseRecord(idField, entityId) {
  return {
    [idField]: entityId,
    attempts: 0,
    correct: 0,
    wrong: 0,
    hints: 0,
    replays: 0,
    avgResponseMs: null,
    responseSamples: 0,
    correctStreak: 0,
    lastSeenAt: null,
    lastCorrectAt: null,
    lastWrongAt: null,
    mastery: 0,
    reviewPriority: 0,
    nextReviewAt: null,
    sourceGames: [],
  };
}

function createRecord(entityType, entityId) {
  if (entityType === "vocabulary") {
    return { ...createBaseRecord("wordKey", entityId), recentMistakes: [] };
  }
  if (entityType === "grammar") {
    return { ...createBaseRecord("grammarId", entityId), errorTypes: {}, recentMistakes: [] };
  }
  return {
    ...createBaseRecord("sentenceId", entityId),
    errorTypes: {},
    recentMistakes: [],
    recentAnswers: [],
  };
}

function boundedAppend(items, value) {
  const next = [...items, value];
  return next.length > MAX_RECENT_SAMPLES ? next.slice(next.length - MAX_RECENT_SAMPLES) : next;
}

function boundedAppendChronological(items, value) {
  const next = [...items, value].sort(
    (left, right) => Date.parse(left.occurredAt) - Date.parse(right.occurredAt),
  );
  return next.length > MAX_RECENT_SAMPLES
    ? next.slice(next.length - MAX_RECENT_SAMPLES)
    : next;
}

function laterIso(current, candidate) {
  if (current == null) return candidate;
  return Date.parse(candidate) >= Date.parse(current) ? candidate : current;
}

function updateAverage(previousAverage, previousMeasuredAttempts, responseMs) {
  if (responseMs === undefined) return previousAverage;
  if (previousAverage == null || previousMeasuredAttempts <= 0) return responseMs;
  return Math.round((previousAverage * previousMeasuredAttempts + responseMs) / (previousMeasuredAttempts + 1));
}

export function viewLearningProfile(raw) {
  if (raw == null) return createEmptyLearningProfile();
  if (!isPlainObject(raw)) throw new TypeError("learning profile must be an object");
  if (raw.version !== LEARNING_PROFILE_VERSION) {
    throw new TypeError(`unsupported learning profile version: ${String(raw.version)}`);
  }

  return {
    version: LEARNING_PROFILE_VERSION,
    updatedAt:
      typeof raw.updatedAt === "string" &&
      Number.isFinite(Date.parse(raw.updatedAt))
        ? new Date(raw.updatedAt).toISOString()
        : new Date(0).toISOString(),
    vocabulary: isPlainObject(raw.vocabulary) ? raw.vocabulary : {},
    grammar: isPlainObject(raw.grammar) ? raw.grammar : {},
    sentences: isPlainObject(raw.sentences) ? raw.sentences : {},
  };
}

export function migrateLearningProfile(raw) {
  return structuredClone(viewLearningProfile(raw));
}

function applyParsedLearningEvent(next, event) {
  const collectionName = event.entityType === "vocabulary"
    ? "vocabulary"
    : event.entityType === "grammar"
      ? "grammar"
      : "sentences";
  const collection = next[collectionName];
  const existing = Object.hasOwn(collection, event.entityId)
    ? collection[event.entityId]
    : createRecord(event.entityType, event.entityId);
  const record = { ...existing };
  const previousLastSeenAt = record.lastSeenAt;
  const isNewestEvent =
    previousLastSeenAt == null ||
    Date.parse(event.occurredAt) >= Date.parse(previousLastSeenAt);

  const priorResponseCount = record.responseSamples ?? 0;
  record.attempts += 1;
  record.correct += event.result === "correct" ? 1 : 0;
  record.wrong += event.result === "wrong" ? 1 : 0;
  record.hints += event.hintUsed ? 1 : 0;
  record.replays += event.replayUsed ? 1 : 0;
  record.avgResponseMs = updateAverage(
    record.avgResponseMs,
    priorResponseCount,
    event.responseMs,
  );
  record.responseSamples =
    priorResponseCount + (event.responseMs === undefined ? 0 : 1);
  if (isNewestEvent) {
    record.correctStreak =
      event.result === "correct" ? record.correctStreak + 1 : 0;
  }
  record.lastSeenAt = laterIso(record.lastSeenAt, event.occurredAt);
  if (event.result === "correct") {
    record.lastCorrectAt = laterIso(record.lastCorrectAt, event.occurredAt);
  }
  if (event.result === "wrong") {
    record.lastWrongAt = laterIso(record.lastWrongAt, event.occurredAt);
  }
  if (!record.sourceGames.includes(event.gameId)) {
    record.sourceGames = [...record.sourceGames, event.gameId];
  }

  if (event.result === "wrong") {
    record.recentMistakes = boundedAppendChronological(
      record.recentMistakes ?? [],
      {
        occurredAt: event.occurredAt,
        ...(event.userAnswer === undefined
          ? {}
          : { userAnswer: event.userAnswer }),
        ...(event.expectedAnswer === undefined
          ? {}
          : { expectedAnswer: event.expectedAnswer }),
        ...(event.errorType === undefined
          ? {}
          : { errorType: event.errorType }),
        activityType: event.activityType,
        gameId: event.gameId,
      },
    );
    if (
      (event.entityType === "grammar" || event.entityType === "sentence") &&
      event.errorType !== undefined
    ) {
      record.errorTypes = { ...(record.errorTypes ?? {}) };
      record.errorTypes[event.errorType] =
        (record.errorTypes[event.errorType] ?? 0) + 1;
    }
  }

  if (event.entityType === "sentence" && event.userAnswer !== undefined) {
    record.recentAnswers = boundedAppendChronological(
      record.recentAnswers ?? [],
      {
        occurredAt: event.occurredAt,
        answer: event.userAnswer,
        result: event.result,
      },
    );
  }

  const metricTime = record.lastSeenAt ?? event.occurredAt;
  record.mastery = calculateMastery(record, metricTime);
  record.reviewPriority = calculateReviewPriority(record, metricTime);
  record.nextReviewAt = calculateNextReviewAt(record, metricTime);

  Object.defineProperty(collection, event.entityId, {
    value: record,
    enumerable: true,
    configurable: true,
    writable: true,
  });
  next.updatedAt = laterIso(next.updatedAt, event.occurredAt);
  return next;
}

export function applyLearningEvent(profileInput, eventInput) {
  const next = migrateLearningProfile(profileInput);
  return applyParsedLearningEvent(next, parseLearningEvent(eventInput));
}

export function applyLearningEvents(profileInput, eventInputs) {
  if (!Array.isArray(eventInputs)) {
    throw new TypeError("learning events must be an array");
  }

  const next = migrateLearningProfile(profileInput);
  const events = eventInputs
    .map((event) => parseLearningEvent(event))
    .map((event, index) => ({ event, index }))
    .sort(
      (left, right) =>
        Date.parse(left.event.occurredAt) - Date.parse(right.event.occurredAt) ||
        left.index - right.index,
    );

  for (const { event } of events) {
    applyParsedLearningEvent(next, event);
  }
  return next;
}
