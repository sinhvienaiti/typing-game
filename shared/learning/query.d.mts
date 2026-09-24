import type { LearningEntityType } from "./core.mjs";

export type LearningStatus =
  | "needs-review"
  | "learning"
  | "improving"
  | "mastered";

export type LearningQuery = {
  entityType: LearningEntityType;
  page: number;
  pageSize: 10 | 25 | 50 | 100;
  search: string;
  sort: string;
  filters: {
    status?: LearningStatus;
    sourceGame?: string;
    masteryMin?: number;
    masteryMax?: number;
    dueOnly?: boolean;
    lastSeenFrom?: string;
    lastSeenTo?: string;
    lastWrongFrom?: string;
    lastWrongTo?: string;
    mistakeMin?: number;
    hintMin?: number;
    replayMin?: number;
    responseMsMin?: number;
    correctStreakMax?: number;
  };
};

export type LearningQueryItem = Record<string, unknown> & {
  entityType: LearningEntityType;
  entityId: string;
  mastery: number;
  reviewPriority: number;
  status: LearningStatus;
  attempts: number;
  correct: number;
  wrong: number;
  sourceGames: string[];
};

export type LearningQueryResult = {
  items: LearningQueryItem[];
  page: number;
  pageSize: number;
  totalItems: number;
  totalPages: number;
};

export const REVIEW_SORTS: Set<string>;
export function parseLearningQuery(input: unknown): LearningQuery;
export function queryLearningProfile(
  profileInput: unknown,
  queryInput: unknown,
  now?: string,
): LearningQueryResult;
