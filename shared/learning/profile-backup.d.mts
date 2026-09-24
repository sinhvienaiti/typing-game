import type {
  LearningEntityType,
  LearningProfile,
} from "./core.mjs";

export type LearningProfileBackup = {
  format: "typing-game-learning-profile";
  version: 1;
  exportedAt: string;
  profile: LearningProfile;
};

export type LearningProfileCounts = {
  vocabulary: number;
  grammar: number;
  sentence: number;
  total: number;
};

export const LEARNING_BACKUP_FORMAT: "typing-game-learning-profile";
export const LEARNING_BACKUP_VERSION: 1;

export function validateLearningProfile(
  profileInput: unknown,
): LearningProfile;

export function createLearningProfileBackup(
  profileInput: unknown,
  exportedAt?: string,
): LearningProfileBackup;

export function parseLearningProfileBackup(
  input: unknown,
): LearningProfile;

export function resetLearningProfileSelection(
  profileInput: unknown,
  entityTypes: LearningEntityType[],
  updatedAt?: string,
): LearningProfile;

export function resetAllLearningProfile(
  updatedAt?: string,
): LearningProfile;

export function learningProfileCounts(
  profileInput: unknown,
): LearningProfileCounts;
