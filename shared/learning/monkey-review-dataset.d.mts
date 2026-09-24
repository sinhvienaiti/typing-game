import type {
  LearningEntityType,
  LearningProfile,
} from "./core.mjs";
import type {
  ReviewGoal,
  ReviewPlan,
} from "./review-session.mjs";

export type MonkeyReviewContext = {
  activityType?: string;
  expectedAnswer?: string;
  userAnswer?: string;
  errorType?: string;
};

export type MonkeyReviewDatasetItem = {
  entityType: LearningEntityType;
  entityId: string;
  mastery?: number;
  reviewPriority?: number;
  acceptedAnswers?: string[];
  reviewContext?: MonkeyReviewContext;
};

export type MonkeyReviewDataset = {
  version: 1;
  type: "typing-game:learning:v1:review-dataset";
  requestId: string;
  createdAt: string;
  goal: ReviewGoal;
  items: MonkeyReviewDatasetItem[];
};

export const MONKEY_REVIEW_DATASET_TYPE:
  "typing-game:learning:v1:review-dataset";

export function buildMonkeyReviewDataset(
  plan: ReviewPlan,
  profile: LearningProfile,
  requestId: string,
  createdAt?: string,
): MonkeyReviewDataset;
