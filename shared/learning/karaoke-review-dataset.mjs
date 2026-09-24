export const KARAOKE_REVIEW_DATASET_TYPE =
  "typing-game:learning:v1:review-dataset";

const GOALS = new Set([
  "remember-words",
  "listening",
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

function latestExpectedText(record, fallback) {
  if (Array.isArray(record?.recentMistakes)) {
    for (let index = record.recentMistakes.length - 1; index >= 0; index--) {
      const sample = record.recentMistakes[index];
      if (!isPlainObject(sample)) continue;
      const expected = optionalString(sample.expectedAnswer);
      if (expected !== undefined) return expected;
    }
  }

  if (Array.isArray(record?.recentAnswers)) {
    for (let index = record.recentAnswers.length - 1; index >= 0; index--) {
      const sample = record.recentAnswers[index];
      if (!isPlainObject(sample)) continue;
      const answer = optionalString(sample.answer);
      if (answer !== undefined) return answer;
    }
  }

  return fallback;
}

function collectionFor(profile, entityType) {
  return entityType === "vocabulary"
    ? profile.vocabulary
    : profile.sentences;
}

export function buildKaraokeReviewDataset(
  plan,
  profile,
  requestId,
  createdAt = new Date().toISOString(),
) {
  if (!isPlainObject(plan) || plan.version !== 1) {
    throw new TypeError("Karaoke review plan is invalid");
  }
  if (!isPlainObject(plan.options) || plan.options.game !== "karaoke-typing") {
    throw new TypeError("Karaoke review plan must target karaoke-typing");
  }
  if (
    typeof plan.options.goal !== "string" ||
    !GOALS.has(plan.options.goal)
  ) {
    throw new TypeError("Karaoke review goal is invalid");
  }
  if (
    typeof requestId !== "string" ||
    !/^[A-Za-z0-9._:-]{1,100}$/.test(requestId)
  ) {
    throw new TypeError("Karaoke review requestId is invalid");
  }
  if (!Array.isArray(plan.items) || plan.items.length === 0) {
    throw new TypeError("Karaoke review plan has no items");
  }
  if (!isPlainObject(profile)) {
    throw new TypeError("Karaoke learning profile is invalid");
  }

  const items = plan.items.map((item) => {
    if (
      !isPlainObject(item) ||
      (item.entityType !== "vocabulary" &&
        item.entityType !== "sentence") ||
      typeof item.entityId !== "string" ||
      item.entityId.trim() === ""
    ) {
      throw new TypeError(
        "Karaoke review plan must contain vocabulary or sentence items only",
      );
    }

    const entityType = item.entityType;
    const entityId = item.entityId.normalize("NFC").trim();
    const record = collectionFor(profile, entityType)?.[entityId] ?? {};
    const text = latestExpectedText(record, entityId);

    return {
      entityType,
      entityId,
      text,
      ...(typeof item.mastery === "number" ? { mastery: item.mastery } : {}),
      ...(typeof item.reviewPriority === "number"
        ? { reviewPriority: item.reviewPriority }
        : {}),
    };
  });

  return {
    version: 1,
    type: KARAOKE_REVIEW_DATASET_TYPE,
    requestId,
    createdAt: new Date(createdAt).toISOString(),
    goal: plan.options.goal,
    items,
  };
}
