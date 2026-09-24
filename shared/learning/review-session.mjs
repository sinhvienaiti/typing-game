import {
  calculateMastery,
  calculateReviewPriority,
  migrateLearningProfile,
} from "./core.mjs";

export const REVIEW_SETS = new Set([
  "due",
  "today",
  "7d",
  "30d",
  "weakest",
  "at-risk",
  "custom",
]);

export const REVIEW_CONTENT = new Set([
  "vocabulary",
  "grammar",
  "sentence",
]);

export const REVIEW_GOALS = new Set([
  "remember-words",
  "spelling",
  "listening",
  "grammar",
  "sentence-building",
  "mixed",
]);

export const REVIEW_GAMES = new Set([
  "monkeytype",
  "recall-typing",
  "vocab-shooter",
  "space-typing",
  "karaoke-typing",
  "mixed-review",
]);

const AMOUNTS = new Set([10, 20, 30, 50, "all"]);

export const REVIEW_CAPABILITIES = Object.freeze({
  monkeytype: {
    entities: ["vocabulary", "grammar", "sentence"],
    goals: [
      "remember-words",
      "spelling",
      "listening",
      "grammar",
      "sentence-building",
      "mixed",
    ],
  },
  "recall-typing": {
    entities: ["vocabulary"],
    goals: ["remember-words", "spelling", "listening", "mixed"],
  },
  "vocab-shooter": {
    entities: ["vocabulary"],
    goals: ["remember-words", "spelling", "mixed"],
  },
  "space-typing": {
    entities: ["vocabulary"],
    goals: ["remember-words", "spelling", "mixed"],
  },
  "karaoke-typing": {
    entities: ["vocabulary", "sentence"],
    goals: ["remember-words", "listening", "sentence-building", "mixed"],
  },
});

function plainObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

function nonEmptyString(value, field, max = 100) {
  if (typeof value !== "string" || value.trim() === "") {
    throw new TypeError(`${field} must be a non-empty string`);
  }
  const result = value.trim();
  if (result.length > max) throw new TypeError(`${field} is too long`);
  return result;
}

function parseAmount(value) {
  const amount = value ?? 20;
  if (!AMOUNTS.has(amount)) {
    throw new TypeError("amount must be 10, 20, 30, 50 or all");
  }
  return amount;
}

function parseContent(value) {
  if (!Array.isArray(value) || value.length === 0) {
    throw new TypeError("content must contain at least one entity type");
  }
  const unique = [...new Set(value)];
  for (const entityType of unique) {
    if (typeof entityType !== "string" || !REVIEW_CONTENT.has(entityType)) {
      throw new TypeError("content contains an unsupported entity type");
    }
  }
  return unique;
}

function optionalNumber(value, field, min, max) {
  if (value === undefined || value === null) return undefined;
  if (!Number.isFinite(value) || value < min || value > max) {
    throw new TypeError(`${field} must be between ${min} and ${max}`);
  }
  return value;
}

function optionalDate(value, field) {
  if (value === undefined || value === null || value === "") return undefined;
  const text = nonEmptyString(value, field, 64);
  const timestamp = Date.parse(text);
  if (!Number.isFinite(timestamp)) throw new TypeError(`${field} must be a date-time`);
  return new Date(timestamp).toISOString();
}

export function parseReviewPlanInput(input) {
  if (!plainObject(input)) throw new TypeError("review plan input must be an object");

  const reviewSet = nonEmptyString(input.reviewSet ?? "due", "reviewSet", 32);
  if (!REVIEW_SETS.has(reviewSet)) throw new TypeError("reviewSet is not supported");

  const goal = nonEmptyString(input.goal ?? "mixed", "goal", 40);
  if (!REVIEW_GOALS.has(goal)) throw new TypeError("goal is not supported");

  const game = nonEmptyString(input.game ?? "monkeytype", "game", 40);
  if (!REVIEW_GAMES.has(game)) throw new TypeError("game is not supported");

  const sourceGame =
    input.sourceGame === undefined || input.sourceGame === null || input.sourceGame === ""
      ? ""
      : nonEmptyString(input.sourceGame, "sourceGame", 64);

  const custom = plainObject(input.custom) ? input.custom : {};
  const masteryMin = optionalNumber(custom.masteryMin, "custom.masteryMin", 0, 100);
  const masteryMax = optionalNumber(custom.masteryMax, "custom.masteryMax", 0, 100);
  const mistakeMin = optionalNumber(custom.mistakeMin, "custom.mistakeMin", 0, 1_000_000);
  const lastWrongFrom = optionalDate(custom.lastWrongFrom, "custom.lastWrongFrom");
  const lastWrongTo = optionalDate(custom.lastWrongTo, "custom.lastWrongTo");

  if (
    masteryMin !== undefined &&
    masteryMax !== undefined &&
    masteryMin > masteryMax
  ) {
    throw new TypeError("custom.masteryMin must not exceed custom.masteryMax");
  }
  if (
    lastWrongFrom !== undefined &&
    lastWrongTo !== undefined &&
    Date.parse(lastWrongFrom) > Date.parse(lastWrongTo)
  ) {
    throw new TypeError("custom.lastWrongFrom must not be after custom.lastWrongTo");
  }

  return {
    reviewSet,
    content: parseContent(input.content ?? ["vocabulary"]),
    amount: parseAmount(input.amount),
    sourceGame,
    goal,
    game,
    custom: {
      ...(masteryMin === undefined ? {} : { masteryMin }),
      ...(masteryMax === undefined ? {} : { masteryMax }),
      ...(mistakeMin === undefined ? {} : { mistakeMin }),
      ...(lastWrongFrom === undefined ? {} : { lastWrongFrom }),
      ...(lastWrongTo === undefined ? {} : { lastWrongTo }),
    },
  };
}

function dayKey(value) {
  const date = new Date(value);
  if (!Number.isFinite(date.getTime())) return "";
  return [
    date.getFullYear(),
    String(date.getMonth() + 1).padStart(2, "0"),
    String(date.getDate()).padStart(2, "0"),
  ].join("-");
}

function entityId(record, entityType) {
  if (entityType === "vocabulary") return record.wordKey;
  if (entityType === "grammar") return record.grammarId;
  return record.sentenceId;
}

function allItems(profile, now) {
  const groups = [
    ["vocabulary", profile.vocabulary],
    ["grammar", profile.grammar],
    ["sentence", profile.sentences],
  ];

  return groups.flatMap(([entityType, collection]) =>
    Object.values(collection).map((record) => ({
      entityType,
      entityId: entityId(record, entityType),
      mastery: calculateMastery(record, now),
      reviewPriority: calculateReviewPriority(record, now),
      attempts: record.attempts,
      correct: record.correct,
      wrong: record.wrong,
      hints: record.hints,
      replays: record.replays,
      avgResponseMs: record.avgResponseMs,
      correctStreak: record.correctStreak,
      lastSeenAt: record.lastSeenAt,
      lastCorrectAt: record.lastCorrectAt,
      lastWrongAt: record.lastWrongAt,
      nextReviewAt: record.nextReviewAt,
      sourceGames: [...record.sourceGames],
    })),
  );
}

export function isAtRiskReviewItem(item, now = new Date().toISOString()) {
  const lastCorrect =
    item.lastCorrectAt == null ? 0 : Date.parse(item.lastCorrectAt);
  const lastWrong = item.lastWrongAt == null ? 0 : Date.parse(item.lastWrongAt);
  const ageDays =
    lastCorrect === 0
      ? Number.POSITIVE_INFINITY
      : (Date.parse(now) - lastCorrect) / 86_400_000;

  return (
    (item.mastery >= 70 && ageDays >= 7) ||
    (item.mastery >= 40 && lastWrong > lastCorrect)
  );
}

function matchesSet(item, reviewSet, now, custom) {
  const nowMs = Date.parse(now);

  if (reviewSet === "due") {
    return item.nextReviewAt != null && Date.parse(item.nextReviewAt) <= nowMs;
  }
  if (reviewSet === "today") {
    return item.lastWrongAt != null && dayKey(item.lastWrongAt) === dayKey(now);
  }
  if (reviewSet === "7d" || reviewSet === "30d") {
    if (item.lastWrongAt == null) return false;
    const days = reviewSet === "7d" ? 7 : 30;
    return nowMs - Date.parse(item.lastWrongAt) <= days * 86_400_000;
  }
  if (reviewSet === "at-risk") return isAtRiskReviewItem(item, now);
  if (reviewSet !== "custom") return true;

  if (custom.masteryMin !== undefined && item.mastery < custom.masteryMin) return false;
  if (custom.masteryMax !== undefined && item.mastery > custom.masteryMax) return false;
  if (custom.mistakeMin !== undefined && item.wrong < custom.mistakeMin) return false;
  if (
    custom.lastWrongFrom !== undefined &&
    (item.lastWrongAt == null || Date.parse(item.lastWrongAt) < Date.parse(custom.lastWrongFrom))
  ) {
    return false;
  }
  if (
    custom.lastWrongTo !== undefined &&
    (item.lastWrongAt == null || Date.parse(item.lastWrongAt) > Date.parse(custom.lastWrongTo))
  ) {
    return false;
  }
  return true;
}

function monkeySupportsGoalEntity(entityType, goal) {
  if (
    goal === "remember-words" ||
    goal === "spelling" ||
    goal === "listening"
  ) {
    return entityType === "vocabulary";
  }
  if (goal === "grammar") return entityType === "grammar";
  if (goal === "sentence-building") return entityType === "sentence";
  return goal === "mixed";
}

function supports(game, item, goal) {
  if (game === "mixed-review") {
    return Object.entries(REVIEW_CAPABILITIES).some(([candidate]) =>
      supports(candidate, item, goal),
    );
  }

  const capability = REVIEW_CAPABILITIES[game];
  if (
    capability === undefined ||
    !capability.entities.includes(item.entityType) ||
    !capability.goals.includes(goal)
  ) {
    return false;
  }

  return game !== "monkeytype" || monkeySupportsGoalEntity(item.entityType, goal);
}

export function compatibleGamesForItem(item, goal = "mixed") {
  return Object.keys(REVIEW_CAPABILITIES).filter((game) =>
    supports(game, item, goal),
  );
}

function comparePriority(a, b) {
  return b.reviewPriority - a.reviewPriority || a.entityId.localeCompare(b.entityId);
}

function compareWeakest(a, b) {
  return a.mastery - b.mastery || comparePriority(a, b);
}

export function buildReviewPlan(
  profileInput,
  input,
  now = new Date().toISOString(),
) {
  const profile = migrateLearningProfile(profileInput);
  const options = parseReviewPlanInput(input);
  const content = new Set(options.content);

  let candidates = allItems(profile, now)
    .filter((item) => content.has(item.entityType))
    .filter((item) =>
      options.sourceGame === "" || item.sourceGames.includes(options.sourceGame),
    )
    .filter((item) => matchesSet(item, options.reviewSet, now, options.custom));

  candidates.sort(options.reviewSet === "weakest" ? compareWeakest : comparePriority);

  const compatible = [];
  const incompatible = [];
  for (const item of candidates) {
    if (supports(options.game, item, options.goal)) compatible.push(item);
    else incompatible.push(item);
  }

  const requestedCount =
    options.amount === "all" ? compatible.length : options.amount;
  const items = compatible.slice(0, requestedCount).map((item) => ({
    ...item,
    compatibleGames: compatibleGamesForItem(item, options.goal),
  }));

  return {
    version: 1,
    createdAt: now,
    durationMinutes: 15,
    options,
    items,
    totalCandidates: candidates.length,
    compatibleCount: compatible.length,
    excludedCount: incompatible.length,
    selectedCount: items.length,
  };
}

export function buildQuickReviewPlan(
  profileInput,
  now = new Date().toISOString(),
) {
  return buildReviewPlan(
    profileInput,
    {
      reviewSet: "due",
      content: ["vocabulary", "grammar", "sentence"],
      amount: 20,
      sourceGame: "",
      goal: "mixed",
      game: "mixed-review",
    },
    now,
  );
}
