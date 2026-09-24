export const SPACE_REVIEW_DATASET_TYPE =
  "typing-game:learning:v1:review-dataset";

const GOALS = new Set([
  "remember-words",
  "spelling",
  "mixed",
]);

function isPlainObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

function optionalNumber(value) {
  return typeof value === "number" && Number.isFinite(value)
    ? value
    : undefined;
}

export function buildSpaceReviewDataset(
  plan,
  requestId,
  createdAt = new Date().toISOString(),
) {
  if (!isPlainObject(plan) || plan.version !== 1) {
    throw new TypeError("Space review plan is invalid");
  }
  if (!isPlainObject(plan.options) || plan.options.game !== "space-typing") {
    throw new TypeError("Space review plan must target space-typing");
  }
  if (
    typeof plan.options.goal !== "string" ||
    !GOALS.has(plan.options.goal)
  ) {
    throw new TypeError("Space review goal is invalid");
  }
  if (
    typeof requestId !== "string" ||
    !/^[A-Za-z0-9._:-]{1,100}$/.test(requestId)
  ) {
    throw new TypeError("Space review requestId is invalid");
  }
  if (!Array.isArray(plan.items) || plan.items.length === 0) {
    throw new TypeError("Space review plan has no items");
  }

  const items = plan.items.map((item) => {
    if (
      !isPlainObject(item) ||
      item.entityType !== "vocabulary" ||
      typeof item.entityId !== "string" ||
      item.entityId.trim() === ""
    ) {
      throw new TypeError(
        "Space review plan must contain vocabulary items only",
      );
    }

    const mastery = optionalNumber(item.mastery);
    const reviewPriority = optionalNumber(item.reviewPriority);
    return {
      entityType: "vocabulary",
      entityId: item.entityId.normalize("NFC").trim(),
      ...(mastery === undefined ? {} : { mastery }),
      ...(reviewPriority === undefined ? {} : { reviewPriority }),
    };
  });

  return {
    version: 1,
    type: SPACE_REVIEW_DATASET_TYPE,
    requestId,
    createdAt: new Date(createdAt).toISOString(),
    goal: plan.options.goal,
    items,
  };
}
