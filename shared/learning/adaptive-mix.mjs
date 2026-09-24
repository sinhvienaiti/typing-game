const GAME_ORDER = Object.freeze([
  "monkeytype",
  "recall-typing",
  "vocab-shooter",
  "space-typing",
  "karaoke-typing",
]);

const SLOW_RESPONSE_MS = 3500;
const STALE_DAYS = 7;

function isPlainObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

function hasGame(item, game) {
  return Array.isArray(item.compatibleGames) &&
    item.compatibleGames.includes(game);
}

function addScore(scores, reasons, game, points, reason) {
  if (!scores.has(game)) return;
  scores.set(game, scores.get(game) + points);
  reasons.get(game).push(reason);
}

function candidateMaps(item) {
  const candidates = GAME_ORDER.filter((game) => hasGame(item, game));
  return {
    candidates,
    scores: new Map(candidates.map((game) => [game, 0])),
    reasons: new Map(candidates.map((game) => [game, []])),
  };
}

function signals(item) {
  return isPlainObject(item.weaknessSignals)
    ? item.weaknessSignals
    : {
        spellingErrors: 0,
        listeningErrors: 0,
        contextErrors: 0,
        grammarErrors: 0,
        staleDays: null,
      };
}

export function chooseAdaptiveReviewActivity(item) {
  if (
    !isPlainObject(item) ||
    typeof item.entityType !== "string" ||
    typeof item.entityId !== "string"
  ) {
    throw new TypeError("Adaptive Review item is invalid");
  }

  const { candidates, scores, reasons } = candidateMaps(item);
  if (candidates.length === 0) {
    throw new TypeError(
      "Adaptive Review item has no concrete compatible game",
    );
  }

  const weakness = signals(item);

  if (item.entityType === "grammar") {
    addScore(
      scores,
      reasons,
      "monkeytype",
      20,
      "grammar items use Sentence Builder/Cloze-capable practice",
    );
  } else if (item.entityType === "sentence") {
    addScore(
      scores,
      reasons,
      "monkeytype",
      8,
      "sentence structure benefits from direct sentence practice",
    );
    addScore(
      scores,
      reasons,
      "karaoke-typing",
      6,
      "sentence context benefits from full-line practice",
    );
    if (
      Number(weakness.listeningErrors) > 0 ||
      Number(item.replays) > 0
    ) {
      addScore(
        scores,
        reasons,
        "karaoke-typing",
        8,
        "recent listening/replay weakness needs listen-and-type context",
      );
    }
    if (
      Number(weakness.grammarErrors) > 0 ||
      Number(weakness.contextErrors) > 0
    ) {
      addScore(
        scores,
        reasons,
        "monkeytype",
        6,
        "recent structure/context errors need controlled sentence practice",
      );
    }
  } else {
    addScore(
      scores,
      reasons,
      "recall-typing",
      1,
      "default vocabulary fallback is focused recall",
    );

    if (Number(weakness.spellingErrors) > 0) {
      addScore(
        scores,
        reasons,
        "monkeytype",
        10,
        "recent spelling errors need precise direct typing",
      );
    }

    if (
      Number(weakness.listeningErrors) > 0 ||
      Number(item.replays) > 0
    ) {
      addScore(
        scores,
        reasons,
        "recall-typing",
        10,
        "recent listening/replay weakness needs audio recall",
      );
    }

    if (
      typeof item.avgResponseMs === "number" &&
      item.avgResponseMs >= SLOW_RESPONSE_MS
    ) {
      addScore(
        scores,
        reasons,
        "vocab-shooter",
        8,
        "slow recognition benefits from fast visual recognition",
      );
    }

    if (
      typeof weakness.staleDays === "number" &&
      weakness.staleDays >= STALE_DAYS
    ) {
      addScore(
        scores,
        reasons,
        "space-typing",
        7,
        "stale vocabulary benefits from repeated game exposure",
      );
    }

    if (Number(item.hints) > 0) {
      addScore(
        scores,
        reasons,
        "recall-typing",
        4,
        "hint history indicates recall support is still useful",
      );
    }

    if (Number(item.mastery) < 50) {
      addScore(
        scores,
        reasons,
        "recall-typing",
        3,
        "low mastery benefits from focused recall",
      );
    }
  }

  let selected = candidates[0];
  for (const candidate of candidates.slice(1)) {
    const score = scores.get(candidate);
    const selectedScore = scores.get(selected);
    if (score > selectedScore) selected = candidate;
  }

  const selectedReasons = reasons.get(selected);
  return {
    game: selected,
    score: scores.get(selected),
    reason:
      selectedReasons.length > 0
        ? selectedReasons.join("; ")
        : "deterministic compatible fallback",
  };
}

export function buildAdaptiveReviewSession(
  plan,
  createdAt = new Date().toISOString(),
) {
  if (!isPlainObject(plan) || plan.version !== 1) {
    throw new TypeError("Adaptive Mix plan is invalid");
  }
  if (!isPlainObject(plan.options) || plan.options.game !== "adaptive-mix") {
    throw new TypeError("Adaptive Mix plan must target adaptive-mix");
  }
  if (!Array.isArray(plan.items) || plan.items.length === 0) {
    throw new TypeError("Adaptive Mix plan has no items");
  }

  const buckets = new Map(GAME_ORDER.map((game) => [game, []]));
  const assignments = [];

  for (const item of plan.items) {
    const choice = chooseAdaptiveReviewActivity(item);
    buckets.get(choice.game).push({ ...item });
    assignments.push({
      entityType: item.entityType,
      entityId: item.entityId,
      game: choice.game,
      score: choice.score,
      reason: choice.reason,
    });
  }

  let segmentIndex = 0;
  const segments = GAME_ORDER.flatMap((game) => {
    const items = buckets.get(game);
    if (items.length === 0) return [];
    segmentIndex += 1;
    const itemKeys = new Set(
      items.map((item) => item.entityType + ":" + item.entityId),
    );
    return [{
      id: "adaptive-" + String(segmentIndex),
      game,
      items,
      selectedCount: items.length,
      reasons: assignments
        .filter((assignment) =>
          itemKeys.has(
            assignment.entityType + ":" + assignment.entityId,
          ),
        )
        .map((assignment) => assignment.reason),
    }];
  });

  return {
    version: 1,
    strategy: "adaptive",
    createdAt: new Date(createdAt).toISOString(),
    sourcePlanCreatedAt: plan.createdAt,
    totalItems: plan.items.length,
    segments,
    assignments,
  };
}

export const ADAPTIVE_THRESHOLDS = Object.freeze({
  slowResponseMs: SLOW_RESPONSE_MS,
  staleDays: STALE_DAYS,
});
