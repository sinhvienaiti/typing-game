import type { LearningEvent } from "../../../shared/learning/core.mjs";
import {
  buildAdaptiveReviewSession,
  type AdaptiveReviewSession,
} from "../../../shared/learning/adaptive-mix.mjs";
import {
  buildMixedReviewSession,
  createMixedReviewProgress,
  recordMixedReviewEvent,
  reviewPlanForMixedSegment,
  type MixedReviewProgress,
  type MixedReviewSession,
} from "../../../shared/learning/mixed-review.mjs";
import {
  REVIEW_CAPABILITIES,
  type ReviewPlan,
} from "../../../shared/learning/review-session.mjs";

const MIXED_KEY = "typingGameMixedReviewV1";

type StoredMixedReview = {
  version: 1;
  sourcePlanCreatedAt: string;
  session: MixedReviewSession | AdaptiveReviewSession;
  progress: MixedReviewProgress;
  launchedSegmentId: string | null;
};


function plainObject(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}

function validStoredMixedReview(value: unknown): value is StoredMixedReview {
  if (!plainObject(value) || value["version"] !== 1) return false;
  if (typeof value["sourcePlanCreatedAt"] !== "string") return false;

  const session = value["session"];
  const progress = value["progress"];
  const launchedSegmentId = value["launchedSegmentId"];
  if (
    !plainObject(session) ||
    session["version"] !== 1 ||
    !Array.isArray(session["segments"]) ||
    !Number.isInteger(session["totalItems"]) ||
    (session["totalItems"] as number) < 0
  ) {
    return false;
  }

  for (const segment of session["segments"]) {
    if (
      !plainObject(segment) ||
      typeof segment["id"] !== "string" ||
      typeof segment["game"] !== "string" ||
      REVIEW_CAPABILITIES[segment["game"]] === undefined ||
      !Array.isArray(segment["items"]) ||
      !Number.isInteger(segment["selectedCount"]) ||
      segment["selectedCount"] !== segment["items"].length
    ) {
      return false;
    }
  }

  if (
    !plainObject(progress) ||
    progress["version"] !== 1 ||
    !Number.isInteger(progress["activeSegmentIndex"]) ||
    (progress["activeSegmentIndex"] as number) < 0 ||
    (progress["activeSegmentIndex"] as number) > session["segments"].length ||
    !plainObject(progress["completedBySegment"])
  ) {
    return false;
  }

  for (const completed of Object.values(progress["completedBySegment"])) {
    if (
      !Array.isArray(completed) ||
      completed.some((key) => typeof key !== "string")
    ) {
      return false;
    }
  }

  if (
    progress["completedAt"] !== null &&
    (typeof progress["completedAt"] !== "string" ||
      !Number.isFinite(Date.parse(progress["completedAt"])))
  ) {
    return false;
  }
  if (
    launchedSegmentId !== null &&
    typeof launchedSegmentId !== "string"
  ) {
    return false;
  }
  return true;
}

export type MixedReviewState = StoredMixedReview & {
  activeSegment:
    | MixedReviewSession["segments"][number]
    | null;
  completedSegments: number;
};

function enrich(value: StoredMixedReview): MixedReviewState {
  return {
    ...value,
    activeSegment:
      value.session.segments[value.progress.activeSegmentIndex] ?? null,
    completedSegments: Math.min(
      value.progress.activeSegmentIndex,
      value.session.segments.length,
    ),
  };
}

function save(value: StoredMixedReview): MixedReviewState {
  sessionStorage.setItem(MIXED_KEY, JSON.stringify(value));
  return enrich(value);
}

export function clearMixedReview(): void {
  sessionStorage.removeItem(MIXED_KEY);
}

export function readMixedReview(): MixedReviewState | null {
  const raw = sessionStorage.getItem(MIXED_KEY);
  if (raw === null) return null;

  try {
    const value: unknown = JSON.parse(raw);
    if (!validStoredMixedReview(value)) {
      throw new TypeError("stored Mixed Review state is invalid");
    }
    return enrich(value);
  } catch {
    sessionStorage.removeItem(MIXED_KEY);
    return null;
  }
}

export function ensureMixedReview(plan: ReviewPlan): MixedReviewState {
  if (
    plan.options.game !== "mixed-review" &&
    plan.options.game !== "adaptive-mix"
  ) {
    throw new TypeError(
      "Review orchestration state requires mixed-review or adaptive-mix",
    );
  }

  const current = readMixedReview();
  if (current?.sourcePlanCreatedAt === plan.createdAt) return current;

  const session =
    plan.options.game === "adaptive-mix"
      ? buildAdaptiveReviewSession(plan)
      : buildMixedReviewSession(plan);
  return save({
    version: 1,
    sourcePlanCreatedAt: plan.createdAt,
    session,
    progress: createMixedReviewProgress(session),
    launchedSegmentId: null,
  });
}

export function activeMixedReviewPlan(
  plan: ReviewPlan,
): ReviewPlan | null {
  const state = ensureMixedReview(plan);
  return state.activeSegment === null
    ? null
    : reviewPlanForMixedSegment(plan, state.activeSegment);
}

export function markMixedReviewSegmentStarted(
  plan: ReviewPlan,
): MixedReviewState {
  const current = ensureMixedReview(plan);
  if (current.activeSegment === null) return current;
  return save({
    version: 1,
    sourcePlanCreatedAt: current.sourcePlanCreatedAt,
    session: current.session,
    progress: current.progress,
    launchedSegmentId: current.activeSegment.id,
  });
}

export function cancelMixedReviewSegmentStart(): MixedReviewState | null {
  const current = readMixedReview();
  if (current === null) return null;
  return save({
    version: 1,
    sourcePlanCreatedAt: current.sourcePlanCreatedAt,
    session: current.session,
    progress: current.progress,
    launchedSegmentId: null,
  });
}

export function recordMixedLearningEvent(
  event: LearningEvent,
): {
  matched: boolean;
  segmentCompleted: boolean;
  sessionCompleted: boolean;
  state: MixedReviewState | null;
} {
  const current = readMixedReview();
  if (current === null || current.progress.completedAt !== null) {
    return {
      matched: false,
      segmentCompleted: false,
      sessionCompleted: current?.progress.completedAt !== null,
      state: current,
    };
  }

  if (
    current.activeSegment === null ||
    current.launchedSegmentId !== current.activeSegment.id
  ) {
    return {
      matched: false,
      segmentCompleted: false,
      sessionCompleted: false,
      state: current,
    };
  }

  const result = recordMixedReviewEvent(
    current.session,
    current.progress,
    event,
    event.occurredAt,
  );
  if (!result.matched) {
    return {
      matched: false,
      segmentCompleted: false,
      sessionCompleted: result.sessionCompleted,
      state: current,
    };
  }

  const state = save({
    version: 1,
    sourcePlanCreatedAt: current.sourcePlanCreatedAt,
    session: current.session,
    progress: result.progress,
    launchedSegmentId: result.segmentCompleted
      ? null
      : current.launchedSegmentId,
  });
  return {
    matched: true,
    segmentCompleted: result.segmentCompleted,
    sessionCompleted: result.sessionCompleted,
    state,
  };
}
