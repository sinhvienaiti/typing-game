export type EnglishRuntimeDataset = "dictionary" | "grammar" | "sentences" | "phrases";
export type EnglishRuntimeShard = {
  id: string;
  path: string;
  count: number;
  bytes?: number;
  sha256?: string;
};
export type EnglishRuntimeManifest = {
  schemaVersion: 1;
  contentVersion: string;
  dataset: EnglishRuntimeDataset;
  count: number;
  shards: EnglishRuntimeShard[];
};
export type EnglishTopicPackItem = {
  contentId: string;
  stage: "pre-check" | "input" | "practice" | "contrast" | "post-check";
  activity: string;
  learningFocus: "typing-fluency" | "recognition" | "recall" | "usage-discrimination" | "comprehension" | "production";
  noteVi?: string;
};
export type EnglishTopicPack = {
  schemaVersion: 1;
  id: string;
  title: string;
  titleVi: string;
  description: string;
  cefr: string[];
  estimatedMinutes?: number;
  objectives: string[];
  items: EnglishTopicPackItem[];
};
export type EnglishTopicPackSummary = {
  id: string;
  title: string;
  titleVi: string;
  description: string;
  cefr: string[];
  estimatedMinutes: number;
  itemCount: number;
  path: string;
};
export declare function parseRuntimeManifest(
  value: unknown,
  expectedDataset: EnglishRuntimeDataset,
): EnglishRuntimeManifest;
export declare function createEnglishRuntimeLoader(options?: {
  fetcher?: (input: string, init?: RequestInit) => Promise<Pick<Response, "ok" | "status" | "json">>;
  baseUrl?: string;
  maxCachedShards?: number;
  maxCachedBuckets?: number;
  maxConcurrency?: number;
  pinnedContentVersion?: string;
}): {
  loadManifest(dataset: EnglishRuntimeDataset): Promise<EnglishRuntimeManifest>;
  loadShard(dataset: EnglishRuntimeDataset, shard: EnglishRuntimeShard): Promise<unknown[]>;
  loadDataset(dataset: EnglishRuntimeDataset, options?: { prefix?: string }): Promise<unknown[]>;
  findById(dataset: EnglishRuntimeDataset, id: string): Promise<any | null>;
  resolvePublishedByIds(ids: string[]): Promise<{
    recordsById: Map<string, any>;
    missingIds: string[];
    contentVersion: string | null;
    usedIndex: boolean;
  }>;
  getEvidence(
    targetId: string,
    filters?: { kinds?: string[]; cefr?: string; limit?: number },
  ): Promise<{ targetId: string; refs: Record<string, string[]>; records: any[] }>;
  loadIndexManifest(): Promise<any | null>;
  loadAvailability(): Promise<{
    schemaVersion: 1;
    contentVersion: string;
    activities: Record<string, { total: number; byCefr: Record<string, number>; within200: number; within240: number }>;
  } | null>;
  loadActivityIndex(activity: string): Promise<any | null>;
  loadTopicPacksManifest(): Promise<{
    schemaVersion: 1;
    contentVersion: string;
    count: number;
    packs: EnglishTopicPackSummary[];
  } | null>;
  loadTopicPack(packId: string): Promise<EnglishTopicPack | null>;
  loadLexicalPilot(): Promise<any | null>;
  getPinnedContentVersion(): string | null;
  clear(): void;
};
