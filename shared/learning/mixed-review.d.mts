import type { LearningEvent } from "./core.mjs";
import type {
  ReviewGame,
  ReviewPlan,
  ReviewPlanItem,
} from "./review-session.mjs";

export type ConcreteReviewGame = Exclude<
  ReviewGame,
  "mixed-review" | "adaptive-mix"
>;

export type MixedReviewSegment = {
  id: string;
  game: ConcreteReviewGame;
  items: ReviewPlanItem[];
  selectedCount: number;
};

export type MixedReviewSession = {
  version: 1;
  createdAt: string;
  sourcePlanCreatedAt: string;
  totalItems: number;
  segments: MixedReviewSegment[];
};

export type MixedReviewProgress = {
  version: 1;
  activeSegmentIndex: number;
  completedBySegment: Record<string, string[]>;
  completedAt: string | null;
};

export function mixedReviewItemKey(
  entityType: string,
  entityId: string,
): string;

export function buildMixedReviewSession(
  plan: ReviewPlan,
  createdAt?: string,
): MixedReviewSession;

export function reviewPlanForMixedSegment(
  plan: ReviewPlan,
  segment: MixedReviewSegment,
): ReviewPlan;

export function createMixedReviewProgress(
  session: MixedReviewSession,
): MixedReviewProgress;

export function recordMixedReviewEvent(
  session: MixedReviewSession,
  progress: MixedReviewProgress,
  event: LearningEvent,
  occurredAt?: string,
): {
  progress: MixedReviewProgress;
  matched: boolean;
  segmentCompleted: boolean;
  sessionCompleted: boolean;
};
