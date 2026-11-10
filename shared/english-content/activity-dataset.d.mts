export type EnglishActivityEntityType="vocabulary"|"grammar"|"sentence";
export type EnglishActivityItem={
  contentId:string;
  entityType:EnglishActivityEntityType;
  entityId:string;
  promptText:string;
  answerText:string;
  meaningVi?:string;
  ipa?:string;
  audioText?:string;
};
export type EnglishActivityDataset={
  version:1;
  type:"typing-game:english-content:v1:activity-dataset";
  requestId:string;
  createdAt:string;
  gameId:"monkeytype"|"recall-typing"|"vocab-shooter"|"karaoke-typing"|"space-typing";
  activity:string;
  items:EnglishActivityItem[];
};
export declare const ENGLISH_ACTIVITY_DATASET_MESSAGE:"typing-game:english-content:v1:activity-dataset";
export declare function defaultEnglishActivityEntityType(activity:string):EnglishActivityEntityType;
export declare function parseEnglishActivityItem(value:unknown,activity:string):EnglishActivityItem;
export declare function buildEnglishActivityDataset(
  gameId:EnglishActivityDataset["gameId"],
  activity:string,
  items:unknown[],
  requestId:string,
  createdAt?:string,
):EnglishActivityDataset;
export declare function parseEnglishActivityDataset(value:unknown):EnglishActivityDataset|null;
