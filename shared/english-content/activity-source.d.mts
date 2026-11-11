import type { EnglishActivityDataset } from "./activity-dataset.mjs";
import type { EnglishRuntimeDataset, EnglishRuntimeShard } from "./runtime-loader.mjs";

export type EnglishRuntimeLoaderLike = {
  loadDataset(dataset: EnglishRuntimeDataset, options?: { prefix?: string }): Promise<unknown[]>;
  loadShard?(dataset: EnglishRuntimeDataset, shard: EnglishRuntimeShard): Promise<unknown[]>;
  loadAvailability?(): Promise<any | null>;
  loadActivityIndex?(activity: string): Promise<any | null>;
};

export type EnglishActivitySelectionOptions = {
  limit?: number;
  cefr?: string;
  seed?: number;
  offset?: number;
  maxAnswerLength?: number;
};

export declare const ENGLISH_ACTIVITY_SOURCES: Readonly<
  Record<string, ReadonlyArray<{ dataset: EnglishRuntimeDataset; prefix: string; type?: string }>>
>;

export declare function loadPublishedEnglishActivityRecords(
  loader: EnglishRuntimeLoaderLike,
  activity: string,
  options?: EnglishActivitySelectionOptions,
): Promise<unknown[]>;

export declare function countPublishedEnglishActivityRecords(
  loader: EnglishRuntimeLoaderLike,
  activity: string,
  options?: Pick<EnglishActivitySelectionOptions, "cefr" | "maxAnswerLength">,
): Promise<number>;

export declare function publishedEnglishActivityAvailability(
  loader: EnglishRuntimeLoaderLike,
  gameCapabilityId: string,
): Promise<Record<string, number>>;

export declare function buildPublishedGameEnglishActivityDataset(
  loader: EnglishRuntimeLoaderLike,
  gameId: EnglishActivityDataset["gameId"],
  gameCapabilityId: string,
  activity: string,
  requestId: string,
  options?: EnglishActivitySelectionOptions & { createdAt?: string },
): Promise<EnglishActivityDataset>;
