export type LearningEntityType = "vocabulary" | "grammar" | "sentence";
export type LearningResult = "correct" | "wrong";

export type LearningEvent = {
  version: 1;
  entityType: LearningEntityType;
  entityId: string;
  gameId: string;
  activityType: string;
  result: LearningResult;
  occurredAt: string;
  responseMs?: number;
  hintUsed: boolean;
  replayUsed: boolean;
  userAnswer?: string;
  expectedAnswer?: string;
  errorType?: string;
};

export type LearningRecord = {
  attempts: number;
  correct: number;
  wrong: number;
  hints: number;
  replays: number;
  avgResponseMs: number | null;
  responseSamples: number;
  correctStreak: number;
  lastSeenAt: string | null;
  lastCorrectAt: string | null;
  lastWrongAt: string | null;
  mastery: number;
  reviewPriority: number;
  nextReviewAt: string | null;
  sourceGames: string[];
  recentMistakes?: Array<Record<string, unknown>>;
  recentAnswers?: Array<Record<string, unknown>>;
  errorTypes?: Record<string, number>;
  wordKey?: string;
  grammarId?: string;
  sentenceId?: string;
};

export type LearningProfile = {
  version: 1;
  updatedAt: string;
  vocabulary: Record<string, LearningRecord>;
  grammar: Record<string, LearningRecord>;
  sentences: Record<string, LearningRecord>;
};

export const LEARNING_EVENT_VERSION: 1;
export const LEARNING_PROFILE_VERSION: 1;
export const MAX_RECENT_SAMPLES: number;

export function normalizeVocabularyKey(value: string): string;
export function parseLearningEvent(input: unknown): LearningEvent;
export function createEmptyLearningProfile(updatedAt?: string): LearningProfile;
export function viewLearningProfile(raw: unknown): LearningProfile;
export function migrateLearningProfile(raw: unknown): LearningProfile;
export function applyLearningEvent(
  profileInput: unknown,
  eventInput: unknown,
): LearningProfile;
export function applyLearningEvents(
  profileInput: unknown,
  eventInputs: unknown[],
): LearningProfile;
export function calculateMastery(
  record: LearningRecord,
  now?: string,
): number;
export function calculateReviewPriority(
  record: LearningRecord,
  now?: string,
): number;
export function calculateNextReviewAt(
  record: LearningRecord,
  now?: string,
): string;
