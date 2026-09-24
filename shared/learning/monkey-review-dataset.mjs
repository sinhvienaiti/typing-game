export const MONKEY_REVIEW_DATASET_TYPE =
  "typing-game:learning:v1:review-dataset";

const GOALS = new Set([
  "remember-words",
  "spelling",
  "listening",
  "grammar",
  "sentence-building",
  "mixed",
]);

function isPlainObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

function optionalString(value) {
  return typeof value === "string" && value.trim() !== ""
    ? value.normalize("NFC").trim()
    : undefined;
}

function sentenceAcceptedAnswers(record) {
  const values = [];

  if (Array.isArray(record.recentAnswers)) {
    for (const sample of record.recentAnswers) {
      if (!isPlainObject(sample) || sample.result !== "correct") continue;
      const answer = optionalString(sample.answer);
      if (answer !== undefined) values.push(answer);
    }
  }

  if (Array.isArray(record.recentMistakes)) {
    for (const sample of record.recentMistakes) {
      if (!isPlainObject(sample)) continue;
      const expected = optionalString(sample.expectedAnswer);
      if (expected !== undefined) values.push(expected);
    }
  }

  const result = [];
  const seen = new Set();
  for (const value of values.reverse()) {
    const key = value.toLocaleLowerCase("en-US").replace(/\s+/g, " ");
    if (seen.has(key)) continue;
    seen.add(key);
    result.push(value);
    if (result.length >= 12) break;
  }
  return result;
}

function latestReviewContext(record) {
  if (!Array.isArray(record.recentMistakes)) return undefined;

  for (let index = record.recentMistakes.length - 1; index >= 0; index--) {
    const sample = record.recentMistakes[index];
    if (!isPlainObject(sample)) continue;

    const activityType = optionalString(sample.activityType);
    const expectedAnswer = optionalString(sample.expectedAnswer);
    const userAnswer = optionalString(sample.userAnswer);
    const errorType = optionalString(sample.errorType);
    if (
      activityType === undefined &&
      expectedAnswer === undefined &&
      userAnswer === undefined &&
      errorType === undefined
    ) {
      continue;
    }

    return {
      ...(activityType === undefined ? {} : { activityType }),
      ...(expectedAnswer === undefined ? {} : { expectedAnswer }),
      ...(userAnswer === undefined ? {} : { userAnswer }),
      ...(errorType === undefined ? {} : { errorType }),
    };
  }

  return undefined;
}

function collectionFor(profile, entityType) {
  if (entityType === "vocabulary") return profile.vocabulary;
  if (entityType === "grammar") return profile.grammar;
  return profile.sentences;
}

export function buildMonkeyReviewDataset(
  plan,
  profile,
  requestId,
  createdAt = new Date().toISOString(),
) {
  if (!isPlainObject(plan) || plan.version !== 1) {
    throw new TypeError("Monkey review plan is invalid");
  }
  if (!isPlainObject(plan.options) || plan.options.game !== "monkeytype") {
    throw new TypeError("Monkey review plan must target monkeytype");
  }
  const goal = optionalString(plan.options.goal);
  if (goal === undefined || !GOALS.has(goal)) {
    throw new TypeError("Monkey review goal is invalid");
  }
  if (
    typeof requestId !== "string" ||
    !/^[A-Za-z0-9._:-]{1,100}$/.test(requestId)
  ) {
    throw new TypeError("Monkey review requestId is invalid");
  }
  if (!Array.isArray(plan.items) || plan.items.length === 0) {
    throw new TypeError("Monkey review plan has no items");
  }

  const items = plan.items.map((item) => {
    if (
      !isPlainObject(item) ||
      !["vocabulary", "grammar", "sentence"].includes(item.entityType) ||
      typeof item.entityId !== "string" ||
      item.entityId.trim() === ""
    ) {
      throw new TypeError("Monkey review item is invalid");
    }

    const entityType = item.entityType;
    const entityId = item.entityId.normalize("NFC").trim();
    const record = collectionFor(profile, entityType)?.[entityId] ?? {};
    const reviewContext = latestReviewContext(record);
    const acceptedAnswers =
      entityType === "sentence" ? sentenceAcceptedAnswers(record) : [];

    return {
      entityType,
      entityId,
      ...(typeof item.mastery === "number" ? { mastery: item.mastery } : {}),
      ...(typeof item.reviewPriority === "number"
        ? { reviewPriority: item.reviewPriority }
        : {}),
      ...(acceptedAnswers.length === 0 ? {} : { acceptedAnswers }),
      ...(reviewContext === undefined ? {} : { reviewContext }),
    };
  });

  return {
    version: 1,
    type: MONKEY_REVIEW_DATASET_TYPE,
    requestId,
    createdAt: new Date(createdAt).toISOString(),
    goal,
    items,
  };
}
