import type { EnglishActivityDataset } from "./activity-dataset.mjs";
export declare function englishActivityItemsFromRecords(
  activity:string,
  records:unknown[],
  options?:{allowUnpublished?:boolean},
):EnglishActivityDataset["items"];
export declare function buildGameEnglishActivityDataset(
  gameId:EnglishActivityDataset["gameId"],
  activity:string,
  records:unknown[],
  requestId:string,
  options?:{allowUnpublished?:boolean;createdAt?:string},
):EnglishActivityDataset;
