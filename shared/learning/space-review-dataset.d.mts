import type {
  ReviewGoal,
  ReviewPlan,
} from "./review-session.mjs";

export type SpaceReviewGoal = Extract<
  ReviewGoal,
  "remember-words" | "spelling" | "mixed"
>;

export type SpaceReviewDatasetItem = {
  entityType: "vocabulary";
  entityId: string;
  mastery?: number;
  reviewPriority?: number;
};

export type SpaceReviewDataset = {
  version: 1;
  type: "typing-game:learning:v1:review-dataset";
  requestId: string;
  createdAt: string;
  goal: SpaceReviewGoal;
  items: SpaceReviewDatasetItem[];
};

export const SPACE_REVIEW_DATASET_TYPE:
  "typing-game:learning:v1:review-dataset";

export function buildSpaceReviewDataset(
  plan: ReviewPlan,
  requestId: string,
  createdAt?: string,
): SpaceReviewDataset;
