import { supportsEnglishActivity } from "./capabilities.mjs";

export const ENGLISH_ACTIVITY_DATASET_MESSAGE =
  "typing-game:english-content:v1:activity-dataset";

const GAME_CAPABILITY_IDS=Object.freeze({
  monkeytype:"monkeytype",
  "recall-typing":"recall",
  "vocab-shooter":"shooter",
  "karaoke-typing":"karaoke",
  "space-typing":"space",
});
const ENTITY_TYPES=new Set(["vocabulary","grammar","sentence"]);
const REQUEST_ID_PATTERN=/^[A-Za-z0-9._:-]{1,100}$/;

function plainObject(value){
  return value!==null&&typeof value==="object"&&!Array.isArray(value);
}
function cleanText(value,field,maxLength=2000){
  if(typeof value!=="string") throw new TypeError(field+" must be a string");
  const cleaned=value.normalize("NFC").trim().replace(/\s+/g," ");
  if(cleaned===""||cleaned.length>maxLength) throw new TypeError(field+" is invalid");
  return cleaned;
}
function optionalText(value,field,maxLength=2000){
  if(value===undefined||value===null||value==="") return undefined;
  return cleanText(value,field,maxLength);
}
function capabilityId(gameId){
  const id=GAME_CAPABILITY_IDS[gameId];
  if(id===undefined) throw new TypeError("English activity gameId is invalid");
  return id;
}
export function defaultEnglishActivityEntityType(activity){
  return activity==="vocabulary"
    ?"vocabulary"
    :activity==="grammar-topic"||activity==="grammar-challenge"
      ?"grammar"
      :"sentence";
}
export function parseEnglishActivityItem(value,activity){
  if(!plainObject(value)) throw new TypeError("English activity item must be an object");
  const contentId=cleanText(value.contentId,"contentId",200);
  const promptText=cleanText(value.promptText,"promptText");
  const answerText=cleanText(value.answerText,"answerText");
  const entityType=value.entityType??defaultEnglishActivityEntityType(activity);
  if(typeof entityType!=="string"||!ENTITY_TYPES.has(entityType)) {
    throw new TypeError("English activity entityType is invalid");
  }
  const defaultEntityId=entityType==="vocabulary"
    ?answerText.normalize("NFKC").toLocaleLowerCase("en-US")
    :contentId;
  const entityId=cleanText(value.entityId??defaultEntityId,"entityId",200);
  if(entityType==="grammar"&&!entityId.startsWith("gr.")) {
    throw new TypeError("Grammar activity entityId must use a gr.* id");
  }
  return {
    contentId,
    entityType,
    entityId,
    promptText,
    answerText,
    ...(optionalText(value.meaningVi,"meaningVi")===undefined?{}:{meaningVi:optionalText(value.meaningVi,"meaningVi")}),
    ...(optionalText(value.ipa,"ipa",300)===undefined?{}:{ipa:optionalText(value.ipa,"ipa",300)}),
    ...(optionalText(value.audioText,"audioText")===undefined?{}:{audioText:optionalText(value.audioText,"audioText")}),
  };
}
export function buildEnglishActivityDataset(
  gameId,
  activity,
  items,
  requestId,
  createdAt=new Date().toISOString(),
){
  if(typeof gameId!=="string") throw new TypeError("English activity gameId is invalid");
  const capability=capabilityId(gameId);
  if(typeof activity!=="string"||!supportsEnglishActivity(capability,activity)) {
    throw new TypeError("English activity is not supported by "+gameId);
  }
  if(typeof requestId!=="string"||!REQUEST_ID_PATTERN.test(requestId)) {
    throw new TypeError("English activity requestId is invalid");
  }
  if(!Array.isArray(items)||items.length===0||items.length>100) {
    throw new TypeError("English activity items must contain 1 to 100 records");
  }
  const parsed=items.map(item=>parseEnglishActivityItem(item,activity));
  const contentIds=new Set();
  for(const item of parsed){
    if(contentIds.has(item.contentId)) throw new TypeError("English activity contentId is duplicated");
    contentIds.add(item.contentId);
  }
  return {
    version:1,
    type:ENGLISH_ACTIVITY_DATASET_MESSAGE,
    requestId,
    createdAt:new Date(createdAt).toISOString(),
    gameId,
    activity,
    items:parsed,
  };
}
export function parseEnglishActivityDataset(value){
  if(!plainObject(value)||value.type!==ENGLISH_ACTIVITY_DATASET_MESSAGE) return null;
  if(value.version!==1) throw new TypeError("English activity dataset version is invalid");
  return buildEnglishActivityDataset(
    value.gameId,
    value.activity,
    value.items,
    value.requestId,
    value.createdAt,
  );
}
