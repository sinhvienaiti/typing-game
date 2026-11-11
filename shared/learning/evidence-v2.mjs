export const LEARNING_EVIDENCE_VERSION = 2;
export const MAX_EVIDENCE_SAMPLES = 12;

export const EVIDENCE_DIMENSIONS = Object.freeze([
  "typing-fluency",
  "recognition",
  "recall",
  "usage-discrimination",
  "comprehension",
  "production",
]);

export const EVIDENCE_ENTITY_KINDS = Object.freeze([
  "lexeme",
  "sense",
  "phrase",
  "grammar",
  "sentence",
  "pack",
  "vocabulary",
]);

export const EVIDENCE_OUTCOMES = Object.freeze(["correct", "incorrect", "needs-review"]);

const DIMENSION_SET = new Set(EVIDENCE_DIMENSIONS);
const KIND_SET = new Set(EVIDENCE_ENTITY_KINDS);
const OUTCOME_SET = new Set(EVIDENCE_OUTCOMES);

function isPlainObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

function cleanRequired(value, field, max = 200) {
  if (typeof value !== "string" || value.trim() === "") {
    throw new TypeError(`${field} must be a non-empty string`);
  }
  const normalized = value.normalize("NFC").trim();
  if (normalized.length > max) throw new TypeError(`${field} is too long`);
  return normalized;
}

function cleanOptional(value, field, max = 2000) {
  if (value === undefined || value === null || value === "") return undefined;
  if (typeof value !== "string") throw new TypeError(`${field} must be a string`);
  const normalized = value.normalize("NFC").trim();
  if (normalized.length > max) throw new TypeError(`${field} is too long`);
  return normalized === "" ? undefined : normalized;
}

export function inferEvidenceEntityKind(entityId, explicitKind) {
  if (explicitKind !== undefined) {
    if (!KIND_SET.has(explicitKind)) throw new TypeError("Unsupported evidence entityKind: " + explicitKind);
    return explicitKind;
  }
  const id = String(entityId ?? "");
  if (id.startsWith("lex.")) return "lexeme";
  if (id.startsWith("sense.")) return "sense";
  if (/^(col|pv|pat|chunk|idiom)\./.test(id)) return "phrase";
  if (id.startsWith("gr.")) return "grammar";
  if (id.startsWith("pack.")) return "pack";
  if (/^(sent|ex|dlg|err)\./.test(id)) return "sentence";
  return "vocabulary";
}

export function defaultEvidenceDimensionForActivity(activity, explicitFocus) {
  if (explicitFocus && DIMENSION_SET.has(explicitFocus)) return explicitFocus;
  if (activity === "example-typing" || activity === "dialogue") return "typing-fluency";
  if (activity === "listening-typing" || activity === "grammar-topic") return "recognition";
  if (activity === "contextual-usage" || activity === "error-correction" || activity === "verb-pattern") {
    return "usage-discrimination";
  }
  if (activity === "translation" || activity === "transformation" || activity === "sentence-building") {
    return "production";
  }
  return "recall";
}

export function parseLearningEvidenceEvent(input) {
  if (!isPlainObject(input)) throw new TypeError("evidence event must be an object");
  if (input.version !== LEARNING_EVIDENCE_VERSION) {
    throw new TypeError(`evidence event version must be ${LEARNING_EVIDENCE_VERSION}`);
  }

  const contentId = cleanRequired(input.contentId, "contentId", 200);
  const rawEntityId = cleanRequired(input.entityId ?? contentId, "entityId", 200);
  const targetConfidence = input.targetConfidence === "unverified-rotational" ? "unverified-rotational" : "verified";

  let entityKind = inferEvidenceEntityKind(rawEntityId, input.entityKind);
  let entityId = rawEntityId;
  // Strictly guard rotational E11 gr.* targets from polluting grammar semantic evidence
  if (entityKind === "grammar" && targetConfidence === "unverified-rotational") {
    entityKind = "sentence";
    entityId = cleanOptional(input.fallbackSentenceId, "fallbackSentenceId", 200) ?? contentId;
  }

  const dimension = cleanRequired(
    defaultEvidenceDimensionForActivity(input.activityType, input.dimension),
    "dimension",
    40,
  );
  if (!DIMENSION_SET.has(dimension)) throw new TypeError("Unsupported evidence dimension: " + dimension);

  const outcome = cleanRequired(input.outcome, "outcome", 24);
  if (!OUTCOME_SET.has(outcome)) throw new TypeError("Unsupported evidence outcome: " + outcome);

  const occurredAtRaw = cleanRequired(input.occurredAt ?? new Date().toISOString(), "occurredAt", 64);
  const parsedTime = Date.parse(occurredAtRaw);
  if (!Number.isFinite(parsedTime)) throw new TypeError("occurredAt must be an ISO date-time");

  let responseMs;
  if (input.responseMs !== undefined && input.responseMs !== null) {
    if (!Number.isFinite(input.responseMs) || input.responseMs < 0) {
      throw new TypeError("responseMs must be non-negative");
    }
    responseMs = Math.round(input.responseMs);
  }

  const packId = cleanOptional(input.packId, "packId", 120);
  const stage = cleanOptional(input.stage, "stage", 40);
  const reasonCode = cleanOptional(input.reasonCode, "reasonCode", 64);
  const userAnswer = cleanOptional(input.userAnswer, "userAnswer");
  const expectedAnswer = cleanOptional(input.expectedAnswer, "expectedAnswer");

  return {
    version: LEARNING_EVIDENCE_VERSION,
    contentId,
    entityKind,
    entityId,
    dimension,
    outcome,
    activityType: cleanRequired(input.activityType, "activityType", 64),
    source: cleanRequired(input.source ?? "portal", "source", 64),
    occurredAt: new Date(parsedTime).toISOString(),
    hintUsed: Boolean(input.hintUsed),
    replayUsed: Boolean(input.replayUsed),
    targetConfidence,
    ...(responseMs === undefined ? {} : { responseMs }),
    ...(packId === undefined ? {} : { packId }),
    ...(stage === undefined ? {} : { stage }),
    ...(reasonCode === undefined ? {} : { reasonCode }),
    ...(userAnswer === undefined ? {} : { userAnswer }),
    ...(expectedAnswer === undefined ? {} : { expectedAnswer }),
  };
}

export function createEmptyEvidenceStore(updatedAt = new Date(0).toISOString()) {
  return {
    version: LEARNING_EVIDENCE_VERSION,
    updatedAt: new Date(updatedAt).toISOString(),
    entities: {},
    packs: {},
  };
}

function clamp(v, lo, hi) {
  return Math.min(hi, Math.max(lo, v));
}

export function computeSemanticMastery(entityRecord) {
  if (!entityRecord || !isPlainObject(entityRecord.dimensions)) return 0;
  // Typing-fluency is intentionally excluded from semantic mastery!
  const semanticDims = ["recognition", "recall", "usage-discrimination", "comprehension", "production"];
  let gradableAttempts = 0;
  let gradableCorrect = 0;
  let distinctDimsMastered = 0;
  let unassistedCorrect = 0;

  for (const dim of semanticDims) {
    const stat = entityRecord.dimensions[dim];
    if (!stat) continue;
    const ga = (stat.correct ?? 0) + (stat.incorrect ?? 0);
    if (ga > 0) {
      gradableAttempts += ga;
      gradableCorrect += stat.correct ?? 0;
      unassistedCorrect += stat.unassistedCorrect ?? 0;
      if ((stat.correct ?? 0) / ga >= 0.7) distinctDimsMastered++;
    }
  }
  if (gradableAttempts === 0) return 0;
  const accuracy = (gradableCorrect / gradableAttempts) * 70;
  const independence = (unassistedCorrect / gradableAttempts) * 15;
  const breadth = clamp(distinctDimsMastered * 5, 0, 15);
  return Math.round(clamp(accuracy + independence + breadth, 0, 100));
}

export function computeFluencyScore(entityRecord) {
  const stat = entityRecord?.dimensions?.["typing-fluency"];
  if (!stat) return 0;
  const ga = (stat.correct ?? 0) + (stat.incorrect ?? 0);
  if (ga === 0) return 0;
  const acc = (stat.correct / ga) * 80;
  const speedBonus = stat.avgResponseMs != null && stat.avgResponseMs <= 2500 ? 20 : stat.avgResponseMs <= 4500 ? 10 : 5;
  return Math.round(clamp(acc + speedBonus, 0, 100));
}

function emptyDimensionStats() {
  return {
    attempts: 0,
    correct: 0,
    incorrect: 0,
    needsReview: 0,
    unassistedCorrect: 0,
    correctStreak: 0,
    avgResponseMs: null,
    responseSamples: 0,
    lastSeenAt: null,
  };
}

export function applyLearningEvidenceEvent(storeInput, eventInput) {
  const base = isPlainObject(storeInput) && storeInput.version === LEARNING_EVIDENCE_VERSION
    ? structuredClone(storeInput)
    : createEmptyEvidenceStore();
  const ev = parseLearningEvidenceEvent(eventInput);
  const key = `${ev.entityKind}:${ev.entityId}`;

  const entity = Object.hasOwn(base.entities, key)
    ? base.entities[key]
    : {
        entityKey: key,
        entityKind: ev.entityKind,
        entityId: ev.entityId,
        semanticMastery: 0,
        typingFluencyScore: 0,
        dimensions: {},
        recentSamples: [],
      };

  const dimStat = Object.hasOwn(entity.dimensions, ev.dimension)
    ? { ...entity.dimensions[ev.dimension] }
    : emptyDimensionStats();

  dimStat.attempts += 1;
  if (ev.outcome === "correct") {
    dimStat.correct += 1;
    dimStat.correctStreak += 1;
    if (!ev.hintUsed && !ev.replayUsed) dimStat.unassistedCorrect += 1;
  } else if (ev.outcome === "incorrect") {
    dimStat.incorrect += 1;
    dimStat.correctStreak = 0;
  } else {
    // needs-review: never penalizes incorrect or resets streak
    dimStat.needsReview += 1;
  }

  if (ev.responseMs !== undefined) {
    const prevCount = dimStat.responseSamples;
    dimStat.avgResponseMs = prevCount === 0 || dimStat.avgResponseMs == null
      ? ev.responseMs
      : Math.round((dimStat.avgResponseMs * prevCount + ev.responseMs) / (prevCount + 1));
    dimStat.responseSamples = prevCount + 1;
  }
  dimStat.lastSeenAt = dimStat.lastSeenAt == null || Date.parse(ev.occurredAt) >= Date.parse(dimStat.lastSeenAt)
    ? ev.occurredAt
    : dimStat.lastSeenAt;

  Object.defineProperty(entity.dimensions, ev.dimension, {
    value: dimStat,
    enumerable: true,
    configurable: true,
    writable: true,
  });

  entity.recentSamples = [
    ...entity.recentSamples,
    {
      occurredAt: ev.occurredAt,
      contentId: ev.contentId,
      dimension: ev.dimension,
      outcome: ev.outcome,
      activityType: ev.activityType,
      ...(ev.reasonCode === undefined ? {} : { reasonCode: ev.reasonCode }),
    },
  ].slice(-MAX_EVIDENCE_SAMPLES);

  entity.semanticMastery = computeSemanticMastery(entity);
  entity.typingFluencyScore = computeFluencyScore(entity);

  Object.defineProperty(base.entities, key, {
    value: entity,
    enumerable: true,
    configurable: true,
    writable: true,
  });

  if (ev.packId) {
    const packState = Object.hasOwn(base.packs, ev.packId)
      ? { ...base.packs[ev.packId] }
      : {
          packId: ev.packId,
          attempts: 0,
          correct: 0,
          incorrect: 0,
          needsReview: 0,
          completedContentIds: [],
          lastSeenAt: null,
        };
    packState.attempts += 1;
    if (ev.outcome === "correct") packState.correct += 1;
    else if (ev.outcome === "incorrect") packState.incorrect += 1;
    else packState.needsReview += 1;
    if (ev.outcome !== "incorrect" && !packState.completedContentIds.includes(ev.contentId)) {
      packState.completedContentIds = [...packState.completedContentIds, ev.contentId];
    }
    packState.lastSeenAt = ev.occurredAt;
    Object.defineProperty(base.packs, ev.packId, {
      value: packState,
      enumerable: true,
      configurable: true,
      writable: true,
    });
  }

  base.updatedAt = Date.parse(ev.occurredAt) >= Date.parse(base.updatedAt) ? ev.occurredAt : base.updatedAt;
  return base;
}

/**
 * Bridge an eligible graded v2 evidence event to a compatible v1 LearningEvent ONLY
 * when auto-graded and strictly safe (never emits "wrong" for "needs-review").
 */
export function toCompatibleV1LearningEvent(eventInput) {
  const ev = parseLearningEvidenceEvent(eventInput);
  if (ev.outcome === "needs-review") return null;

  const v1EntityType =
    ev.entityKind === "grammar"
      ? "grammar"
      : ev.entityKind === "vocabulary" || ev.entityKind === "lexeme"
        ? "vocabulary"
        : "sentence";

  if (ev.entityKind === "pack") return null;

  return {
    version: 1,
    entityType: v1EntityType,
    entityId: ev.entityId,
    gameId: ev.source,
    activityType: ev.activityType,
    result: ev.outcome === "correct" ? "correct" : "wrong",
    occurredAt: ev.occurredAt,
    ...(ev.responseMs === undefined ? {} : { responseMs: ev.responseMs }),
    hintUsed: ev.hintUsed,
    replayUsed: ev.replayUsed,
    ...(ev.userAnswer === undefined ? {} : { userAnswer: ev.userAnswer }),
    ...(ev.expectedAnswer === undefined ? {} : { expectedAnswer: ev.expectedAnswer }),
  };
}
