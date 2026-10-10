import { listEnglishActivities } from "./capabilities.mjs";
import { buildGameEnglishActivityDataset } from "./game-adapters.mjs";

const RECORD_SOURCES=Object.freeze({
  vocabulary:[{dataset:"dictionary",prefix:"lexemes-"}],
  collocation:[{dataset:"phrases",prefix:"collocations-"}],
  "verb-pattern":[{dataset:"phrases",prefix:"verb-patterns-"}],
  "phrasal-verb":[{dataset:"phrases",prefix:"phrases-",type:"phrasal-verb"}],
  chunk:[{dataset:"phrases",prefix:"phrases-",type:"chunk"}],
  idiom:[{dataset:"phrases",prefix:"phrases-",type:"idiom"}],
  "grammar-topic":[{dataset:"grammar",prefix:"topics-"}],
  "grammar-challenge":[{dataset:"grammar",prefix:"topics-"}],
  "example-typing":[{dataset:"sentences",prefix:"examples-"}],
  "listening-typing":[
    {dataset:"sentences",prefix:"exercises-",type:"listening-typing"},
    {dataset:"sentences",prefix:"examples-"},
  ],
  translation:[{dataset:"sentences",prefix:"exercises-",type:"translation"}],
  cloze:[{dataset:"sentences",prefix:"exercises-",type:"cloze"}],
  "error-correction":[
    {dataset:"sentences",prefix:"exercises-",type:"error-correction"},
    {dataset:"sentences",prefix:"mistakes-"},
  ],
  "sentence-building":[{dataset:"sentences",prefix:"exercises-",type:"sentence-building"}],
  transformation:[{dataset:"sentences",prefix:"exercises-",type:"transformation"}],
  "contextual-usage":[{dataset:"sentences",prefix:"exercises-",type:"contextual-usage"}],
  dialogue:[{dataset:"sentences",prefix:"dialogues-"}],
});

function sourceSpecs(activity){
  const specs=RECORD_SOURCES[activity];
  if(!Array.isArray(specs)) throw new TypeError("No published runtime source for activity: "+activity);
  return specs;
}
function published(record){
  return record!==null&&typeof record==="object"&&!Array.isArray(record)&&record.quality?.state==="published";
}
function matchesType(record,type){
  return type===undefined||record?.type===type;
}
function boundedLimit(value){
  const limit=Number(value??20);
  if(!Number.isInteger(limit)||limit<1||limit>100) throw new TypeError("English activity limit must be an integer from 1 to 100");
  return limit;
}

export async function loadPublishedEnglishActivityRecords(loader,activity,options={}){
  if(loader===null||typeof loader!=="object"||typeof loader.loadDataset!=="function") {
    throw new TypeError("English runtime loader is required");
  }
  const limit=boundedLimit(options.limit);
  const results=[];
  const seen=new Set();
  for(const spec of sourceSpecs(activity)){
    const records=await loader.loadDataset(spec.dataset,{prefix:spec.prefix});
    for(const record of records){
      if(!published(record)||!matchesType(record,spec.type)) continue;
      const id=typeof record.id==="string"?record.id:typeof record.lexemeId==="string"?record.lexemeId:"";
      const key=id||JSON.stringify(record);
      if(seen.has(key)) continue;
      seen.add(key);
      results.push(record);
      if(results.length>=limit) return results;
    }
  }
  return results;
}

export async function countPublishedEnglishActivityRecords(loader,activity){
  if(loader===null||typeof loader!=="object"||typeof loader.loadDataset!=="function") {
    throw new TypeError("English runtime loader is required");
  }
  const seen=new Set();
  for(const spec of sourceSpecs(activity)){
    const records=await loader.loadDataset(spec.dataset,{prefix:spec.prefix});
    for(const record of records){
      if(!published(record)||!matchesType(record,spec.type)) continue;
      const id=typeof record.id==="string"?record.id:typeof record.lexemeId==="string"?record.lexemeId:"";
      seen.add(id||JSON.stringify(record));
    }
  }
  return seen.size;
}

export async function publishedEnglishActivityAvailability(loader,gameCapabilityId){
  const activities=listEnglishActivities(gameCapabilityId);
  const pairs=await Promise.all(activities.map(async activity=>[
    activity,
    await countPublishedEnglishActivityRecords(loader,activity),
  ]));
  return Object.fromEntries(pairs);
}

export async function buildPublishedGameEnglishActivityDataset(
  loader,
  gameId,
  gameCapabilityId,
  activity,
  requestId,
  options={},
){
  if(!listEnglishActivities(gameCapabilityId).includes(activity)) {
    throw new TypeError("English activity is not supported by "+gameId);
  }
  const records=await loadPublishedEnglishActivityRecords(loader,activity,options);
  if(records.length===0) throw new Error("No published English content is available for "+activity);
  return buildGameEnglishActivityDataset(
    gameId,
    activity,
    records,
    requestId,
    {createdAt:options.createdAt},
  );
}
