import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");

async function readJson(relative) {
  return JSON.parse(await fs.readFile(path.join(root,relative),"utf8"));
}

function requireCondition(condition,message) {
  if (!condition) throw new Error(message);
}

function countBy(records,keyFn) {
  const counts={};
  for (const record of records) {
    const key=keyFn(record);
    if (key===undefined||key===null||key==="") continue;
    counts[key]=(counts[key]??0)+1;
  }
  return counts;
}

async function loadSentenceRuntime() {
  const manifest=await readJson("shared/sentences/manifest.json");
  const groups={examples:[],exercises:[],dialogues:[],mistakes:[]};
  const allRecords=[];

  for (const shard of manifest.shards??[]) {
    const relative="shared/sentences/"+String(shard.path);
    const doc=await readJson(relative);
    requireCondition(Array.isArray(doc.records),relative+" must contain records[]");
    requireCondition(
      doc.records.length===shard.count,
      relative+": manifest count "+String(shard.count)+" does not match records[] length "+String(doc.records.length),
    );
    const group=String(shard.path).split("/")[0];
    requireCondition(Array.isArray(groups[group]),relative+": unsupported sentence runtime group "+group);
    groups[group].push(...doc.records);
    allRecords.push(...doc.records);
  }

  requireCondition(
    allRecords.length===manifest.count,
    "shared/sentences/manifest.json count "+String(manifest.count)+" does not match loaded runtime count "+String(allRecords.length),
  );

  for (const record of allRecords) {
    requireCondition(
      record?.quality?.state==="published",
      "shared/sentences runtime contains non-published record "+String(record?.id??"<unknown>"),
    );
  }

  return {manifest,groups};
}

const [typingIndex,sentenceRuntime]=await Promise.all([
  readJson("shared/typing-texts/index.json"),
  loadSentenceRuntime(),
]);

requireCondition(Array.isArray(typingIndex.levels),"shared/typing-texts/index.json must contain levels[]");
const indexedTypingPassages=typingIndex.levels.reduce((sum,level)=>sum+Number(level?.passageCount??0),0);
requireCondition(
  indexedTypingPassages===typingIndex.totalPassages,
  "shared/typing-texts/index.json totalPassages does not match summed level passageCount",
);
requireCondition(
  typingIndex.levels.length===typingIndex.availableLevels,
  "shared/typing-texts/index.json availableLevels does not match levels[] length",
);

const exercises=sentenceRuntime.groups.exercises;
const exerciseByType=countBy(exercises,record=>record?.type);
const counts={
  "typing-texts":typingIndex.totalPassages,
  "translation-pairs":exerciseByType.translation??0,
  "cloze-exercises":exerciseByType.cloze??0,
  "dialogue-examples":sentenceRuntime.groups.dialogues.length,
  "common-mistakes":sentenceRuntime.groups.mistakes.length,
  "writing-exercises":exerciseByType.transformation??0,
};

const report={
  schemaVersion:1,
  contentVersion:sentenceRuntime.manifest.contentVersion,
  counts,
  definitions:{
    "typing-texts":{
      source:"shared/typing-texts/index.json",
      metric:"totalPassages",
    },
    "translation-pairs":{
      source:"shared/sentences/exercises/*.json",
      filter:{type:"translation"},
    },
    "cloze-exercises":{
      source:"shared/sentences/exercises/*.json",
      filter:{type:"cloze"},
    },
    "dialogue-examples":{
      source:"shared/sentences/dialogues/*.json",
      metric:"published runtime records",
    },
    "common-mistakes":{
      source:"shared/sentences/mistakes/*.json",
      metric:"published runtime records",
    },
    "writing-exercises":{
      source:"shared/sentences/exercises/*.json",
      filter:{type:"transformation"},
      canonicalE11Target:"sentence-transformations",
      note:"Runtime alias for the locked E11 sentence-transformations target; no separate writing-exercises corpus exists.",
    },
  },
};

const reportPath=path.join(root,"content","english","reports","e11-runtime-counts.json");
await fs.mkdir(path.dirname(reportPath),{recursive:true});
await fs.writeFile(reportPath,JSON.stringify(report,null,2)+"\n","utf8");
console.log(JSON.stringify(report,null,2));
