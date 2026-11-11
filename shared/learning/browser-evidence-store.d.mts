import type { LearningEvidenceEventInput, LearningEvidenceStore } from "./evidence-v2.mjs";

export declare const LEARNING_EVIDENCE_DB_NAME: string;
export declare const LEARNING_EVIDENCE_STORE_NAME: string;
export declare const LEARNING_EVIDENCE_KEY: string;

export declare class BrowserLearningEvidenceStore {
  constructor(options?: {
    indexedDB?: IDBFactory;
    databaseName?: string;
    storeName?: string;
  });
  load(): Promise<LearningEvidenceStore>;
  apply(event: LearningEvidenceEventInput): Promise<LearningEvidenceStore>;
  applyMany(events: LearningEvidenceEventInput[]): Promise<LearningEvidenceStore>;
  reset(): Promise<LearningEvidenceStore>;
}
