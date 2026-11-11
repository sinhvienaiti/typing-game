import type { EnglishGradingMode, EnglishNormalizationOptions } from "./grading.mjs";

export type EnglishActivityEntityType = "vocabulary" | "grammar" | "sentence";
export type EnglishLearningFocus =
  | "typing-fluency"
  | "recognition"
  | "recall"
  | "usage-discrimination"
  | "comprehension"
  | "production";

export type EnglishActivityItem = {
  contentId: string;
  entityType: EnglishActivityEntityType;
  entityId: string;
  promptText: string;
  answerText: string;
  meaningVi?: string;
  ipa?: string;
  audioText?: string;
  acceptedAnswers?: string[];
  gradingMode?: EnglishGradingMode;
  normalization?: EnglishNormalizationOptions;
  cefr?: "A1" | "A2" | "B1" | "B2" | "C1" | "C2";
  targetConfidence?: "verified" | "unverified-rotational";
  learningFocus?: EnglishLearningFocus;
  packId?: string;
  stage?: string;
};

export type EnglishActivityDataset = {
  version: 1;
  type: "typing-game:english-content:v1:activity-dataset";
  requestId: string;
  createdAt: string;
  gameId: "monkeytype" | "recall-typing" | "vocab-shooter" | "karaoke-typing" | "space-typing";
  activity: string;
  items: EnglishActivityItem[];
};

export declare const ENGLISH_ACTIVITY_DATASET_MESSAGE: "typing-game:english-content:v1:activity-dataset";
export declare function defaultEnglishActivityEntityType(activity: string): EnglishActivityEntityType;
export declare function parseEnglishActivityItem(value: unknown, activity: string): EnglishActivityItem;
export declare function buildEnglishActivityDataset(
  gameId: EnglishActivityDataset["gameId"],
  activity: string,
  items: unknown[],
  requestId: string,
  createdAt?: string,
): EnglishActivityDataset;
export declare function parseEnglishActivityDataset(value: unknown): EnglishActivityDataset | null;
