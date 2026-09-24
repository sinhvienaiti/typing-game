import type { LearningEntityType, LearningProfile } from "./core.mjs";

export type ReviewSet =
  | "due"
  | "today"
  | "7d"
  | "30d"
  | "weakest"
  | "at-risk"
  | "custom";
export type ReviewGoal =
  | "remember-words"
  | "spelling"
  | "listening"
  | "grammar"
  | "sentence-building"
  | "mixed";
export type ReviewGame =
  | "monkeytype"
  | "recall-typing"
  | "vocab-shooter"
  | "space-typing"
  | "karaoke-typing"
  | "mixed-review";
export type ReviewAmount = 10 | 20 | 30 | 50 | "all";

export type ReviewPlanInput = {
  reviewSet: ReviewSet;
  content: LearningEntityType[];
  amount: ReviewAmount;
  sourceGame?: string;
  goal: ReviewGoal;
  game: ReviewGame;
  custom?: {
    masteryMin?: number;
    masteryMax?: number;
    mistakeMin?: number;
    lastWrongFrom?: string;
    lastWrongTo?: string;
  };
};

export type ReviewPlanItem = {
  entityType: LearningEntityType;
  entityId: string;
  mastery: number;
  reviewPriority: number;
  attempts: number;
  correct: number;
  wrong: number;
  hints: number;
  replays: number;
  avgResponseMs: number | null;
  correctStreak: number;
  lastSeenAt: string | null;
  lastCorrectAt: string | null;
  lastWrongAt: string | null;
  nextReviewAt: string | null;
  sourceGames: string[];
  compatibleGames: string[];
};

export type ReviewPlan = {
  version: 1;
  createdAt: string;
  durationMinutes: number;
  options: ReviewPlanInput;
  items: ReviewPlanItem[];
  totalCandidates: number;
  compatibleCount: number;
  excludedCount: number;
  selectedCount: number;
};

export const REVIEW_SETS: Set<string>;
export const REVIEW_CONTENT: Set<string>;
export const REVIEW_GOALS: Set<string>;
export const REVIEW_GAMES: Set<string>;
export const REVIEW_CAPABILITIES: Readonly<Record<string, {
  entities: string[];
  goals: string[];
}>>;

export function parseReviewPlanInput(input: unknown): ReviewPlanInput;
export function isAtRiskReviewItem(
  item: {
    mastery: number;
    lastCorrectAt: string | null;
    lastWrongAt: string | null;
  },
  now?: string,
): boolean;
export function compatibleGamesForItem(
  item: { entityType: string },
  goal?: string,
): string[];
export function buildReviewPlan(
  profileInput: LearningProfile | unknown,
  input: unknown,
  now?: string,
): ReviewPlan;
export function buildQuickReviewPlan(
  profileInput: LearningProfile | unknown,
  now?: string,
): ReviewPlan;
