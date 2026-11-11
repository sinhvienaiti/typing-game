export type LearningEvidenceDimension =
  | "typing-fluency"
  | "recognition"
  | "recall"
  | "usage-discrimination"
  | "comprehension"
  | "production";

export type LearningEvidenceEntityKind =
  | "lexeme"
  | "sense"
  | "phrase"
  | "grammar"
  | "sentence"
  | "pack"
  | "vocabulary";

export type LearningEvidenceOutcome = "correct" | "incorrect" | "needs-review";

export type LearningEvidenceEventInput = {
  version: 2;
  contentId: string;
  entityId?: string;
  entityKind?: LearningEvidenceEntityKind;
  fallbackSentenceId?: string;
  targetConfidence?: "verified" | "unverified-rotational";
  dimension?: LearningEvidenceDimension;
  outcome: LearningEvidenceOutcome;
  activityType: string;
  source?: string;
  occurredAt?: string;
  responseMs?: number;
  hintUsed?: boolean;
  replayUsed?: boolean;
  packId?: string;
  stage?: string;
  reasonCode?: string;
  userAnswer?: string;
  expectedAnswer?: string;
};

export type LearningEvidenceStore = {
  version: 2;
  updatedAt: string;
  entities: Record<string, any>;
  packs: Record<string, any>;
};

export declare const LEARNING_EVIDENCE_VERSION: 2;
export declare const EVIDENCE_DIMENSIONS: readonly LearningEvidenceDimension[];
export declare const EVIDENCE_ENTITY_KINDS: readonly LearningEvidenceEntityKind[];
export declare const EVIDENCE_OUTCOMES: readonly LearningEvidenceOutcome[];
export declare function inferEvidenceEntityKind(
  entityId: string,
  explicitKind?: LearningEvidenceEntityKind,
): LearningEvidenceEntityKind;
export declare function defaultEvidenceDimensionForActivity(
  activity: string,
  explicitFocus?: string,
): LearningEvidenceDimension;
export declare function parseLearningEvidenceEvent(input: unknown): any;
export declare function createEmptyEvidenceStore(updatedAt?: string): LearningEvidenceStore;
export declare function computeSemanticMastery(entityRecord: any): number;
export declare function computeFluencyScore(entityRecord: any): number;
export declare function applyLearningEvidenceEvent(
  storeInput: LearningEvidenceStore | null | undefined,
  eventInput: LearningEvidenceEventInput,
): LearningEvidenceStore;
export declare function toCompatibleV1LearningEvent(eventInput: LearningEvidenceEventInput): any | null;
