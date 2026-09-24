import type { LearningProfile } from "./core.mjs";

export const LEARNING_DB_NAME: string;
export const LEARNING_STORE_NAME: string;
export const LEARNING_PROFILE_KEY: string;

export class BrowserLearningProfileStore {
  constructor(options?: {
    indexedDB?: IDBFactory;
    databaseName?: string;
    storeName?: string;
  });
  load(): Promise<LearningProfile>;
  save(profile: unknown): Promise<LearningProfile>;
  apply(event: unknown): Promise<LearningProfile>;
  applyMany(events: unknown[]): Promise<LearningProfile>;
}
