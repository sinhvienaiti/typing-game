import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson } from "./english-content-core.mjs";
import { buildGameEnglishActivityDataset } from "../shared/english-content/game-adapters.mjs";
import {
  buildPublishedGameEnglishActivityDataset,
  countPublishedEnglishActivityRecords,
} from "../shared/english-content/activity-source.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const [dictionaryManifest,grammarManifest,sentenceManifest]=await Promise.all([
  readJson(path.join(root,"shared","dictionary","manifest.json")),
  readJson(path.join(root,"shared","grammar","manifest.json")),
  readJson(path.join(root,"shared","sentences","manifest.json")),
]);
const errors=[];

const fileRuntimeLoader={
  async loadDataset(dataset,{prefix}={}){
    const baseDir=path.join("shared",dataset);
    const manifest=await readJson(path.join(root,baseDir,"manifest.json"));
    const records=[];
    for(const shard of manifest.shards??[]){
      if(prefix!==undefined&&!String(shard.id).startsWith(prefix)) continue;
      const doc=await readJson(path.join(root,baseDir,shard.path));
      if(!Array.isArray(doc.records)||doc.records.length!==shard.count) {
        throw new Error(baseDir+"/"+shard.path+": invalid runtime shard");
      }
      records.push(...doc.records);
    }
    return records;
  },
};

async function loadRuntime(manifest,baseDir) {
  const records=[];
  for (const shard of manifest.shards??[]) {
    const doc=await readJson(path.join(root,baseDir,shard.path));
    if (!Array.isArray(doc.records)||doc.records.length!==shard.count) {
      errors.push(baseDir+"/"+shard.path+": shard count mismatch");
      continue;
    }
    records.push(...doc.records);
  }
  if (records.length!==manifest.count) {
    errors.push(baseDir+": manifest count mismatch");
  }
  return records;
}

const dictionaryRecords=await loadRuntime(dictionaryManifest,path.join("shared","dictionary"));
const lexemes=dictionaryRecords.filter(record=>String(record.id??"").startsWith("lex.en."));
const senses=dictionaryRecords.filter(record=>String(record.id??"").startsWith("sense."));
const topics=await loadRuntime(grammarManifest,path.join("shared","grammar"));
const sentenceRecords=await loadRuntime(sentenceManifest,path.join("shared","sentences"));
const examples=sentenceRecords.filter(record=>String(record.id??"").startsWith("sent."));
const exercises=sentenceRecords.filter(record=>String(record.id??"").startsWith("ex."));

if (dictionaryManifest.count!==20) errors.push("published dictionary runtime must contain 20 E03 records");
if (lexemes.length!==10||senses.length!==10) errors.push("published E03 runtime split must be 10 lexemes + 10 senses");
if (grammarManifest.count!==12) errors.push("published grammar runtime must contain 12 E05 topics");
if (sentenceManifest.count!==60) errors.push("published sentence runtime must contain 60 E05 records");
if (topics.length!==12||examples.length!==36||exercises.length!==24) {
  errors.push("published E05 runtime split must be 12 topics + 36 examples + 24 exercises");
}

const senseIds=new Set(senses.map(record=>record.id));
for (const record of [...lexemes,...senses]) {
  if (record.quality?.state!=="published") errors.push(record.id+": dictionary runtime record is not published");
  for (const [name,check] of Object.entries(record.quality?.checks??{})) {
    if (check?.status==="pending"||check?.status==="fail") errors.push(record.id+": unfinished dictionary quality check "+name+"="+check.status);
  }
}
for (const lexeme of lexemes) {
  if (!lexeme.vi||!lexeme.ipa||!lexeme.cefr) errors.push(lexeme.id+": published lexeme is missing vi/ipa/cefr");
  for (const id of lexeme.senseIds??[]) if (!senseIds.has(id)) errors.push(lexeme.id+": missing runtime sense "+id);
}
const topicIds=new Set(topics.map(record=>record.id));
const exampleIds=new Set(examples.map(record=>record.id));
const exerciseIds=new Set(exercises.map(record=>record.id));

for (const record of [...topics,...examples,...exercises]) {
  if (record.quality?.state!=="published") errors.push(record.id+": runtime record is not published");
  for (const [name,check] of Object.entries(record.quality?.checks??{})) {
    if (check?.status==="pending"||check?.status==="fail") {
      errors.push(record.id+": unfinished runtime quality check "+name+"="+check.status);
    }
  }
}
for (const topic of topics) {
  for (const id of topic.exampleIds??[]) if (!exampleIds.has(id)) errors.push(topic.id+": missing runtime example "+id);
  for (const id of topic.exerciseIds??[]) if (!exerciseIds.has(id)) errors.push(topic.id+": missing runtime exercise "+id);
}
for (const sentence of examples) {
  for (const id of sentence.grammarIds??[]) if (!topicIds.has(id)) errors.push(sentence.id+": missing runtime grammar "+id);
}
for (const exercise of exercises) {
  for (const id of exercise.sourceSentenceIds??[]) if (!exampleIds.has(id)) errors.push(exercise.id+": missing runtime source "+id);
  for (const id of exercise.targetIds??[]) if (id.startsWith("gr.")&&!topicIds.has(id)) errors.push(exercise.id+": missing runtime grammar target "+id);
}

try {
  buildGameEnglishActivityDataset(
    "monkeytype","grammar-topic",topics.slice(0,2),"runtime-smoke-monkey-grammar",
    {createdAt:"2026-10-03T00:00:00.000Z"},
  );
  buildGameEnglishActivityDataset(
    "space-typing","grammar-challenge",topics.slice(0,2),"runtime-smoke-space-grammar",
    {createdAt:"2026-10-03T00:00:00.000Z"},
  );
  buildGameEnglishActivityDataset(
    "monkeytype","cloze",exercises.filter(record=>record.type==="cloze").slice(0,2),"runtime-smoke-monkey-cloze",
    {createdAt:"2026-10-03T00:00:00.000Z"},
  );
  buildGameEnglishActivityDataset(
    "monkeytype","translation",exercises.filter(record=>record.type==="translation").slice(0,2),"runtime-smoke-monkey-translation",
    {createdAt:"2026-10-03T00:00:00.000Z"},
  );
} catch (error) {
  errors.push("published runtime activity smoke failed: "+error.message);
}

try {
  for (const [gameId,capability] of [["recall-typing","recall"],["vocab-shooter","shooter"],["space-typing","space"]]) {
    const vocabulary=await buildPublishedGameEnglishActivityDataset(
      fileRuntimeLoader,
      gameId,
      capability,
      "vocabulary",
      "runtime-source-"+gameId+"-vocabulary",
      {limit:5,createdAt:"2026-10-03T00:00:00.000Z"},
    );
    if (vocabulary.items.length!==5) errors.push(gameId+": published vocabulary source must return 5 items");
  }

  const spaceGrammar=await buildPublishedGameEnglishActivityDataset(
    fileRuntimeLoader,
    "space-typing",
    "space",
    "grammar-challenge",
    "runtime-source-space-grammar",
    {limit:5,createdAt:"2026-10-03T00:00:00.000Z"},
  );
  if(spaceGrammar.items.length!==5) {
    errors.push("published activity source must return 5 bounded Space grammar items");
  }

  const karaokeTranslation=await buildPublishedGameEnglishActivityDataset(
    fileRuntimeLoader,
    "karaoke-typing",
    "karaoke",
    "translation",
    "runtime-source-karaoke-translation",
    {limit:5,createdAt:"2026-10-03T00:00:00.000Z"},
  );
  if(karaokeTranslation.items.length!==5) {
    errors.push("published activity source must return 5 bounded Karaoke translation items");
  }

  const karaokeExamples=await buildPublishedGameEnglishActivityDataset(
    fileRuntimeLoader,
    "karaoke-typing",
    "karaoke",
    "example-typing",
    "runtime-source-karaoke-examples",
    {limit:5,createdAt:"2026-10-03T00:00:00.000Z"},
  );
  if(karaokeExamples.items.length!==5) {
    errors.push("published activity source must return 5 bounded Karaoke example items");
  }

  const recallCollocations=await countPublishedEnglishActivityRecords(
    fileRuntimeLoader,
    "collocation",
  );
  if(recallCollocations!==100) {
    errors.push("published Recall collocation activity must expose 100 reviewed records");
  }
  const recallDataset=await buildPublishedGameEnglishActivityDataset(
    fileRuntimeLoader,
    "recall-typing",
    "recall",
    "collocation",
    "runtime-source-recall-collocation",
    {limit:5,createdAt:"2026-10-03T00:00:00.000Z"},
  );
  if(recallDataset.items.length!==5) {
    errors.push("published activity source must return 5 bounded Recall collocation items");
  }
} catch (error) {
  errors.push("published activity source routing smoke failed: "+error.message);
}

const report={
  dictionaryLexemes:lexemes.length,
  dictionarySenses:senses.length,
  dictionaryManifestCount:dictionaryManifest.count,
  grammarTopics:topics.length,
  examples:examples.length,
  exercises:exercises.length,
  grammarManifestCount:grammarManifest.count,
  sentenceManifestCount:sentenceManifest.count,
  runtimeActivitySource:{
    recallVocabulary:5,
    shooterVocabulary:5,
    spaceVocabulary:5,
    spaceGrammar:5,
    karaokeTranslation:5,
    karaokeExamples:5,
    recallCollocations:100,
  },
};
console.log(JSON.stringify(report,null,2));
if (errors.length) {
  console.error(errors.join("\n"));
  process.exitCode=1;
}
