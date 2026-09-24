const GAME_ORDER = Object.freeze([
  "recall-typing",
  "vocab-shooter",
  "space-typing",
  "karaoke-typing",
  "monkeytype",
]);

function isPlainObject(value) {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

function cloneItem(item) {
  return {
    ...item,
    compatibleGames: Array.isArray(item.compatibleGames)
      ? [...item.compatibleGames]
      : [],
  };
}

export function mixedReviewItemKey(entityType, entityId) {
  const type = String(entityType).trim();
  const id = String(entityId).normalize("NFC").trim();
  return type + ":" + id;
}

export function buildMixedReviewSession(
  plan,
  createdAt = new Date().toISOString(),
) {
  if (!isPlainObject(plan) || plan.version !== 1) {
    throw new TypeError("Mixed Review plan is invalid");
  }
  if (!isPlainObject(plan.options) || plan.options.game !== "mixed-review") {
    throw new TypeError("Mixed Review plan must target mixed-review");
  }
  if (!Array.isArray(plan.items) || plan.items.length === 0) {
    throw new TypeError("Mixed Review plan has no items");
  }

  const buckets = new Map(GAME_ORDER.map((game) => [game, []]));

  for (const item of plan.items) {
    if (
      !isPlainObject(item) ||
      typeof item.entityType !== "string" ||
      typeof item.entityId !== "string" ||
      !Array.isArray(item.compatibleGames)
    ) {
      throw new TypeError("Mixed Review item is invalid");
    }

    const candidates = GAME_ORDER.filter((game) =>
      item.compatibleGames.includes(game),
    );
    if (candidates.length === 0) {
      throw new TypeError(
        "Mixed Review item has no concrete compatible game: " +
          item.entityType +
          ":" +
          item.entityId,
      );
    }

    let selected = candidates[0];
    for (const candidate of candidates.slice(1)) {
      if (buckets.get(candidate).length < buckets.get(selected).length) {
        selected = candidate;
      }
    }
    buckets.get(selected).push(cloneItem(item));
  }

  const segments = GAME_ORDER.flatMap((game) => {
    const items = buckets.get(game);
    if (items.length === 0) return [];
    return [{
      id: "segment-" + String(
        GAME_ORDER.slice(0, GAME_ORDER.indexOf(game) + 1)
          .filter((candidate) => (buckets.get(candidate)?.length ?? 0) > 0)
          .length,
      ),
      game,
      items,
      selectedCount: items.length,
    }];
  });

  return {
    version: 1,
    createdAt: new Date(createdAt).toISOString(),
    sourcePlanCreatedAt: plan.createdAt,
    totalItems: plan.items.length,
    segments,
  };
}

export function reviewPlanForMixedSegment(plan, segment) {
  if (
    !isPlainObject(plan) ||
    plan.version !== 1 ||
    !isPlainObject(segment) ||
    typeof segment.game !== "string" ||
    !Array.isArray(segment.items)
  ) {
    throw new TypeError("Mixed Review segment is invalid");
  }

  return {
    ...plan,
    options: {
      ...plan.options,
      game: segment.game,
    },
    items: segment.items.map(cloneItem),
    compatibleCount: segment.items.length,
    excludedCount: 0,
    selectedCount: segment.items.length,
  };
}

export function createMixedReviewProgress(session) {
  if (!isPlainObject(session) || session.version !== 1) {
    throw new TypeError("Mixed Review session is invalid");
  }

  return {
    version: 1,
    activeSegmentIndex: 0,
    completedBySegment: {},
    completedAt: null,
  };
}

function normalizeEventEntityId(event) {
  const value = String(event.entityId).normalize("NFC").trim();
  return event.entityType === "vocabulary"
    ? value.toLocaleLowerCase("en-US").replace(/\s+/g, " ")
    : value;
}

export function recordMixedReviewEvent(
  session,
  progressInput,
  event,
  occurredAt,
) {
  if (
    !isPlainObject(session) ||
    session.version !== 1 ||
    !Array.isArray(session.segments)
  ) {
    throw new TypeError("Mixed Review session is invalid");
  }
  if (
    !isPlainObject(progressInput) ||
    progressInput.version !== 1 ||
    !Number.isInteger(progressInput.activeSegmentIndex) ||
    !isPlainObject(progressInput.completedBySegment)
  ) {
    throw new TypeError("Mixed Review progress is invalid");
  }
  if (
    !isPlainObject(event) ||
    typeof event.gameId !== "string" ||
    typeof event.entityType !== "string" ||
    typeof event.entityId !== "string"
  ) {
    throw new TypeError("Mixed Review learning event is invalid");
  }

  const completionAt =
    typeof occurredAt === "string"
      ? occurredAt
      : typeof event.occurredAt === "string"
        ? event.occurredAt
        : new Date().toISOString();

  const progress = structuredClone(progressInput);
  if (progress.completedAt !== null) {
    return {
      progress,
      matched: false,
      segmentCompleted: false,
      sessionCompleted: true,
    };
  }

  const segment = session.segments[progress.activeSegmentIndex];
  if (segment === undefined || event.gameId !== segment.game) {
    return {
      progress,
      matched: false,
      segmentCompleted: false,
      sessionCompleted: segment === undefined,
    };
  }

  const eventKey = mixedReviewItemKey(
    event.entityType,
    normalizeEventEntityId(event),
  );
  const expectedKeys = new Set(
    segment.items.map((item) =>
      mixedReviewItemKey(
        item.entityType,
        item.entityType === "vocabulary"
          ? String(item.entityId)
              .normalize("NFC")
              .trim()
              .toLocaleLowerCase("en-US")
              .replace(/\s+/g, " ")
          : item.entityId,
      ),
    ),
  );

  if (!expectedKeys.has(eventKey)) {
    return {
      progress,
      matched: false,
      segmentCompleted: false,
      sessionCompleted: false,
    };
  }

  const completed = new Set(progress.completedBySegment[segment.id] ?? []);
  completed.add(eventKey);
  progress.completedBySegment[segment.id] = [...completed];

  const segmentCompleted = [...expectedKeys].every((key) =>
    completed.has(key),
  );
  if (segmentCompleted) {
    progress.activeSegmentIndex += 1;
    if (progress.activeSegmentIndex >= session.segments.length) {
      progress.completedAt = new Date(completionAt).toISOString();
    }
  }

  return {
    progress,
    matched: true,
    segmentCompleted,
    sessionCompleted: progress.completedAt !== null,
  };
}
