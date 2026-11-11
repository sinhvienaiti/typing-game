export type EnglishGradingMode =
  | "exact-normalized"
  | "closed-choice"
  | "guided-self-check";

export type EnglishNormalizationOptions = {
  caseSensitive?: boolean;
  punctuationOptional?: boolean;
  contractionsEquivalent?: boolean;
};

export type EnglishGradingEvaluation = {
  outcome: "correct" | "incorrect" | "needs-review";
  mode: EnglishGradingMode;
  normalizedInput: string;
  matchedAnswer?: string;
  reasonCode?: string;
  note?: string;
  acceptedAnswers: string[];
  autoGradable: boolean;
};

export declare const GRADING_MODES: readonly EnglishGradingMode[];
export declare function normalizeEnglishForGrading(
  value: string,
  options?: EnglishNormalizationOptions,
): string;
export declare function evaluateEnglishAnswer(
  item: {
    answerText?: string;
    acceptedAnswers?: string[];
    lessSuitableAlternatives?: Array<string | { text: string; noteVi?: string }>;
    gradingMode?: EnglishGradingMode;
    normalization?: EnglishNormalizationOptions;
  },
  userAnswer: string,
): EnglishGradingEvaluation;
