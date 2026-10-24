import type { EnglishActivityDataset } from "./activity-dataset.mjs";
import type { EnglishRuntimeDataset } from "./runtime-loader.mjs";
export type EnglishRuntimeLoaderLike={
  loadDataset(dataset:EnglishRuntimeDataset,options?:{prefix?:string}):Promise<unknown[]>;
};
export declare function loadPublishedEnglishActivityRecords(
  loader:EnglishRuntimeLoaderLike,
  activity:string,
  options?:{limit?:number},
):Promise<unknown[]>;
export declare function countPublishedEnglishActivityRecords(
  loader:EnglishRuntimeLoaderLike,
  activity:string,
):Promise<number>;
export declare function publishedEnglishActivityAvailability(
  loader:EnglishRuntimeLoaderLike,
  gameCapabilityId:string,
):Promise<Record<string,number>>;
export declare function buildPublishedGameEnglishActivityDataset(
  loader:EnglishRuntimeLoaderLike,
  gameId:EnglishActivityDataset["gameId"],
  gameCapabilityId:string,
  activity:string,
  requestId:string,
  options?:{limit?:number;createdAt?:string},
):Promise<EnglishActivityDataset>;
