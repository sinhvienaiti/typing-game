import type {
  ReviewPlan,
  ReviewPlanItem,
  ReviewGame,
} from "./review-session.mjs";

export type AdaptiveConcreteGame = Exclude<
  ReviewGame,
  "mixed-review" | "adaptive-mix"
>;

export type AdaptiveReviewChoice = {
  game: AdaptiveConcreteGame;
  score: number;
  reason: string;
};

export type AdaptiveReviewAssignment = AdaptiveReviewChoice & {
  entityType: string;
  entityId: string;
};

export type AdaptiveReviewSegment = {
  id: string;
  game: AdaptiveConcreteGame;
  items: ReviewPlanItem[];
  selectedCount: number;
  reasons: string[];
};

export type AdaptiveReviewSession = {
  version: 1;
  strategy: "adaptive";
  createdAt: string;
  sourcePlanCreatedAt: string;
  totalItems: number;
  segments: AdaptiveReviewSegment[];
  assignments: AdaptiveReviewAssignment[];
};

export const ADAPTIVE_THRESHOLDS: Readonly<{
  slowResponseMs: number;
  staleDays: number;
}>;

export function chooseAdaptiveReviewActivity(
  item: ReviewPlanItem,
): AdaptiveReviewChoice;

export function buildAdaptiveReviewSession(
  plan: ReviewPlan,
  createdAt?: string,
): AdaptiveReviewSession;
