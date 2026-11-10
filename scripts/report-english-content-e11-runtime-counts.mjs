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

async function loadPublishedRuntime(baseDir,allowedGroups) {
  const manifest=await readJson(baseDir+"/manifest.json");
  const groups=Object.fromEntries(allowedGroups.map(group=>[group,[]]));
  const allRecords=[];

  for (const shard of manifest.shards??[]) {
    const relative=baseDir+"/"+String(shard.path);
    const doc=await readJson(relative);
    requireCondition(Array.isArray(doc.records),relative+" must contain records[]");
    requireCondition(
      doc.records.length===shard.count,
      relative+": manifest count "+String(shard.count)+" does not match records[] length "+String(doc.records.length),
    );
    const group=String(shard.path).split("/")[0];
    requireCondition(Array.isArray(groups[group]),relative+": unsupported runtime group "+group);
    groups[group].push(...doc.records);
    allRecords.push(...doc.records);
  }

  requireCondition(
    allRecords.length===manifest.count,
    baseDir+"/manifest.json count "+String(manifest.count)+" does not match loaded runtime count "+String(allRecords.length),
  );

  for (const record of allRecords) {
    requireCondition(
      record?.quality?.state==="published",
      baseDir+" runtime contains non-published record "+String(record?.id??record?.lexemeId??"<unknown>"),
    );
  }

  return {manifest,groups};
}

const [typingIndex,grammarRuntime,phraseRuntime,sentenceRuntime,readiness]=await Promise.all([
  readJson("shared/typing-texts/index.json"),
  loadPublishedRuntime("shared/grammar",["topics"]),
  loadPublishedRuntime("shared/phrases",["collocations","verb-patterns","items"]),
  loadPublishedRuntime("shared/sentences",["examples","exercises","dialogues","mistakes"]),
  readJson("content/english/reports/e11-readiness.json"),
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

requireCondition(
  grammarRuntime.manifest.contentVersion===sentenceRuntime.manifest.contentVersion,
  "shared/grammar contentVersion does not match shared/sentences",
);
requireCondition(
  phraseRuntime.manifest.contentVersion===sentenceRuntime.manifest.contentVersion,
  "shared/phrases contentVersion does not match shared/sentences",
);

const exercises=sentenceRuntime.groups.exercises;
const exerciseByType=countBy(exercises,record=>record?.type);
const phraseItemsByType=countBy(phraseRuntime.groups.items,record=>record?.type);
const mappedPhraseItems=
  (phraseItemsByType["phrasal-verb"]??0)+
  (phraseItemsByType.idiom??0)+
  (phraseItemsByType.chunk??0);
requireCondition(
  mappedPhraseItems===phraseRuntime.groups.items.length,
  "shared/phrases/items contains published records outside E11 phrasal-verbs/idioms-chunks targets: "+JSON.stringify(phraseItemsByType),
);
const counts={
  "typing-texts":typingIndex.totalPassages,
  "translation-pairs":exerciseByType.translation??0,
  "cloze-exercises":exerciseByType.cloze??0,
  "dialogue-examples":sentenceRuntime.groups.dialogues.length,
  "common-mistakes":sentenceRuntime.groups.mistakes.length,
  "writing-exercises":exerciseByType.transformation??0,
};

const publishedTargetCounts={
  "grammar-topics":grammarRuntime.groups.topics.length,
  "verb-patterns":phraseRuntime.groups["verb-patterns"].length,
  collocations:phraseRuntime.groups.collocations.length,
  "phrasal-verbs":phraseItemsByType["phrasal-verb"]??0,
  "idioms-chunks":(phraseItemsByType.idiom??0)+(phraseItemsByType.chunk??0),
  "common-mistakes":counts["common-mistakes"],
  "example-sentences":sentenceRuntime.groups.examples.length,
  "translation-pairs":counts["translation-pairs"],
  "cloze-exercises":counts["cloze-exercises"],
  "sentence-transformations":counts["writing-exercises"],
  "dialogue-examples":counts["dialogue-examples"],
};

const readinessCounts=new Map((readiness.targets??[]).map(target=>[target.id,target.current]));
const targetCoverage=Object.entries(publishedTargetCounts).map(([e11Target,runtimeCount])=>{
  const readinessCount=readinessCounts.get(e11Target);
  requireCondition(
    typeof readinessCount==="number",
    "E11 readiness report is missing target "+e11Target,
  );
  requireCondition(
    runtimeCount===readinessCount,
    "E11 readiness/runtime drift for "+e11Target+": runtime="+String(runtimeCount)+", readiness="+String(readinessCount),
  );
  return {e11Target,runtimeCount,readinessCount};
});

const readinessMappings=[
  ["translation-pairs","translation-pairs"],
  ["cloze-exercises","cloze-exercises"],
  ["dialogue-examples","dialogue-examples"],
  ["common-mistakes","common-mistakes"],
  ["writing-exercises","sentence-transformations"],
];
const compared=readinessMappings.map(([runtimeMetric,e11Target])=>{
  const runtimeCount=counts[runtimeMetric];
  const readinessCount=readinessCounts.get(e11Target);
  requireCondition(
    typeof readinessCount==="number",
    "E11 readiness report is missing target "+e11Target+" required by runtime metric "+runtimeMetric,
  );
  requireCondition(
    runtimeCount===readinessCount,
    "E11 readiness/runtime drift for "+runtimeMetric+" -> "+e11Target+": runtime="+String(runtimeCount)+", readiness="+String(readinessCount),
  );
  return {runtimeMetric,e11Target,runtimeCount,readinessCount};
});

const report={
  schemaVersion:1,
  contentVersion:sentenceRuntime.manifest.contentVersion,
  counts,
  readinessReconciliation:{
    state:"matched",
    compared,
    targetCoverage,
    excluded:[{
      runtimeMetric:"typing-texts",
      reason:"Legacy typing-text runtime corpus has no locked E11 long-term target.",
    }],
  },
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
