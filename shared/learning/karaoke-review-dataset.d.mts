import type { LearningProfile } from "./core.mjs";
import type {
  ReviewGoal,
  ReviewPlan,
} from "./review-session.mjs";

export type KaraokeReviewGoal = Extract<
  ReviewGoal,
  "remember-words" | "listening" | "sentence-building" | "mixed"
>;

export type KaraokeReviewDatasetItem = {
  entityType: "vocabulary" | "sentence";
  entityId: string;
  text: string;
  mastery?: number;
  reviewPriority?: number;
};

export type KaraokeReviewDataset = {
  version: 1;
  type: "typing-game:learning:v1:review-dataset";
  requestId: string;
  createdAt: string;
  goal: KaraokeReviewGoal;
  items: KaraokeReviewDatasetItem[];
};

export const KARAOKE_REVIEW_DATASET_TYPE:
  "typing-game:learning:v1:review-dataset";

export function buildKaraokeReviewDataset(
  plan: ReviewPlan,
  profile: LearningProfile,
  requestId: string,
  createdAt?: string,
): KaraokeReviewDataset;
