import type {
  ReviewGoal,
  ReviewPlan,
} from "./review-session.mjs";

export type RecallReviewGoal = Extract<
  ReviewGoal,
  "remember-words" | "spelling" | "listening" | "mixed"
>;

export type RecallReviewDatasetItem = {
  entityType: "vocabulary";
  entityId: string;
  mastery?: number;
  reviewPriority?: number;
};

export type RecallReviewDataset = {
  version: 1;
  type: "typing-game:learning:v1:review-dataset";
  requestId: string;
  createdAt: string;
  goal: RecallReviewGoal;
  items: RecallReviewDatasetItem[];
};

export const RECALL_REVIEW_DATASET_TYPE:
  "typing-game:learning:v1:review-dataset";

export function buildRecallReviewDataset(
  plan: ReviewPlan,
  requestId: string,
  createdAt?: string,
): RecallReviewDataset;
