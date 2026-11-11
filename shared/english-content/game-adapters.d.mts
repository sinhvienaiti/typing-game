import type { EnglishActivityDataset, EnglishActivityItem } from "./activity-dataset.mjs";

export declare function hasVerifiedTargetAttribution(record: Record<string, any>): boolean;
export declare function englishActivityItemsFromRecords(
  activity: string,
  records: unknown[],
  options?: {
    allowUnpublished?: boolean;
    includeAcceptedAnswers?: boolean;
    includeGrading?: boolean;
    boundDialogueTurns?: boolean;
    maxItems?: number;
  },
): EnglishActivityItem[];
export declare function buildGameEnglishActivityDataset(
  gameId: EnglishActivityDataset["gameId"],
  activity: string,
  records: unknown[],
  requestId: string,
  options?: {
    createdAt?: string;
    allowUnpublished?: boolean;
    includeAcceptedAnswers?: boolean;
    includeGrading?: boolean;
    boundDialogueTurns?: boolean;
    maxItems?: number;
  },
): EnglishActivityDataset;
