import type {
  ReviewGoal,
  ReviewPlan,
} from "./review-session.mjs";

export type ShooterReviewGoal = Extract<
  ReviewGoal,
  "remember-words" | "spelling" | "mixed"
>;

export type ShooterReviewDatasetItem = {
  entityType: "vocabulary";
  entityId: string;
  mastery?: number;
  reviewPriority?: number;
};

export type ShooterReviewDataset = {
  version: 1;
  type: "typing-game:learning:v1:review-dataset";
  requestId: string;
  createdAt: string;
  goal: ShooterReviewGoal;
  items: ShooterReviewDatasetItem[];
};

export const SHOOTER_REVIEW_DATASET_TYPE:
  "typing-game:learning:v1:review-dataset";

export function buildShooterReviewDataset(
  plan: ReviewPlan,
  requestId: string,
  createdAt?: string,
): ShooterReviewDataset;
