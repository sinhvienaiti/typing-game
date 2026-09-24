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
import type { ReviewPlan } from "../../../shared/learning/review-session.mjs";

const MIXED_KEY = "typingGameMixedReviewV1";

type StoredMixedReview = {
  version: 1;
  sourcePlanCreatedAt: string;
  session: MixedReviewSession | AdaptiveReviewSession;
  progress: MixedReviewProgress;
  launchedSegmentId: string | null;
};

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
    const value = JSON.parse(raw) as StoredMixedReview;
    if (
      value.version !== 1 ||
      typeof value.sourcePlanCreatedAt !== "string" ||
      value.session?.version !== 1 ||
      value.progress?.version !== 1
    ) {
      return null;
    }
    return enrich(value);
  } catch {
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
