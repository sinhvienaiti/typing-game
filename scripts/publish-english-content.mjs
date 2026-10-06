import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";
import { overlayEnglishReviewDecisions, readEnglishReviewLedger } from "./english-review-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const [batchManifest,reviewLedger]=await Promise.all([
  readJson(path.join(root,"content","english","batches","manifest.json")),
  readEnglishReviewLedger(root),
]);
const contentVersion=batchManifest.contentVersion;
const batchSetsByPath=new Map();
for (const batch of batchManifest.batches??[]) {
  for (const set of batch.recordSets??[]) {
    batchSetsByPath.set(set.path,{batchId:batch.id,recordSetId:set.id,requiredChecks:set.requiredChecks??[]});
  }
}
const shardSize=500;

async function loadRecords(relative) {
  const doc=await readJson(path.join(root,relative));
  if (!Array.isArray(doc.records)) throw new Error(relative+" must contain records[]");
  const context=batchSetsByPath.get(relative);
  return context===undefined
    ?doc.records
    :overlayEnglishReviewDecisions(doc.records,reviewLedger,context);
}
function published(records,label) {
  const result=[];
  for (const record of records) {
    if (record?.quality?.state!=="published") continue;
    const checks=Object.values(record?.quality?.checks??{});
    const unfinished=checks.find(check=>check?.status==="pending"||check?.status==="fail");
    if (unfinished) {
      throw new Error(label+": published record "+String(record?.id??record?.lexemeId??"<unknown>")+" has unfinished quality checks");
    }
    result.push(record);
  }
  return result;
}
async function resetDir(relative) {
  const target=path.join(root,relative);
  await fs.rm(target,{recursive:true,force:true});
  await fs.mkdir(target,{recursive:true});
}
async function publishDataset({dataset,baseDir,groups}) {
  const shards=[];
  let count=0;
  for (const group of groups) {
    const records=published(group.records,dataset+"/"+group.id);
    count+=records.length;
    const dir=path.join(root,baseDir,group.dir);
    await fs.rm(dir,{recursive:true,force:true});
    if (records.length===0) continue;
    await fs.mkdir(dir,{recursive:true});
    for (let offset=0;offset<records.length;offset+=shardSize) {
      const slice=records.slice(offset,offset+shardSize);
      const shardNo=String(Math.floor(offset/shardSize)).padStart(3,"0");
      const file=shardNo+".json";
      await fs.writeFile(path.join(dir,file),stableJson({schemaVersion:1,records:slice}),"utf8");
      shards.push({id:group.id+"-"+shardNo,path:group.dir+"/"+file,count:slice.length});
    }
  }
  await fs.writeFile(path.join(root,baseDir,"manifest.json"),stableJson({schemaVersion:1,contentVersion,dataset,count,shards}),"utf8");
  return {dataset,count,shards:shards.length};
}

const lexemes=await loadRecords("content/english/dictionary/e03-reviewed-lexemes.json");
const senses=await loadRecords("content/english/dictionary/e03-reviewed-senses.json");
const usages=await loadRecords("content/english/dictionary/e03-reviewed-usages.json");
const e03Examples=await loadRecords("content/english/sentences/e03-reviewed-examples.json");
const topics=await loadRecords("content/english/grammar/pilot-topics.json");
const sentences=await loadRecords("content/english/sentences/pilot-sentences.json");
const exercises=await loadRecords("content/english/sentences/pilot-exercises.json");
const grammarScaleTopics=[];
const grammarScaleSentences=[];
const grammarScaleExercises=[];
const grammarScaleMistakes=[];
const grammarScaleBatches=(batchManifest.batches??[]).filter(batch=>/^e05\.grammar-scale-[a-z][0-9]-[0-9]{2}$/u.test(batch.id)).sort((a,b)=>a.id.localeCompare(b.id,"en"));
for (const batch of grammarScaleBatches) {
  const sets=new Map((batch.recordSets??[]).map(set=>[set.id,set]));
  grammarScaleTopics.push(...await loadRecords(sets.get("grammar-topics").path));
  grammarScaleSentences.push(...await loadRecords(sets.get("examples").path));
  grammarScaleExercises.push(...await loadRecords(sets.get("exercises").path));
  grammarScaleMistakes.push(...await loadRecords(sets.get("common-mistakes").path));
}
const reviewedE06Exercises=await loadRecords("content/english/sentences/e06-reviewed-exercises.json");
const reviewedTranslationSentences=await loadRecords("content/english/sentences/e06-reviewed-translation-sentences.json");
const reviewedTranslations=await loadRecords("content/english/sentences/e06-reviewed-translations.json");
const reviewedTypingTextSentences=await loadRecords("content/english/sentences/e06-reviewed-typing-text-sentences.json");
const reviewedCloze=await loadRecords("content/english/sentences/e06-reviewed-cloze.json");
const reviewedDialogues=await loadRecords("content/english/sentences/e06-reviewed-dialogues.json");
const reviewedCommonMistakes=await loadRecords("content/english/sentences/e06-reviewed-common-mistakes.json");
const e04Collocations=[];
const e04VerbPatterns=[];
const e04Phrases=[];
const e04Batches=(batchManifest.batches??[]).filter(batch=>batch.phase==="E04"&&batch.category==="phrases").sort((a,b)=>a.id.localeCompare(b.id,"en"));
for (const batch of e04Batches) {
  for (const set of batch.recordSets??[]) {
    if (set.id==="collocations"||set.id==="scale-collocations") e04Collocations.push(...await loadRecords(set.path));
    else if (set.id==="verb-patterns"||set.id==="scale-verb-patterns") e04VerbPatterns.push(...await loadRecords(set.path));
    else if (set.id==="phrases"||set.id==="scale-phrases") e04Phrases.push(...await loadRecords(set.path));
  }
}

await fs.mkdir(path.join(root,"shared","dictionary"),{recursive:true});
await fs.mkdir(path.join(root,"shared","grammar"),{recursive:true});
await fs.mkdir(path.join(root,"shared","sentences"),{recursive:true});
await fs.mkdir(path.join(root,"shared","phrases"),{recursive:true});

const results=[];
results.push(await publishDataset({dataset:"dictionary",baseDir:"shared/dictionary",groups:[
  {id:"lexemes",dir:"lexemes",records:lexemes},
  {id:"senses",dir:"senses",records:senses},
  {id:"usages",dir:"usages",records:usages}
]}));
results.push(await publishDataset({dataset:"grammar",baseDir:"shared/grammar",groups:[{id:"topics",dir:"topics",records:[...topics,...grammarScaleTopics]}]}));
results.push(await publishDataset({dataset:"sentences",baseDir:"shared/sentences",groups:[
  {id:"examples",dir:"examples",records:[...e03Examples,...sentences,...grammarScaleSentences,...reviewedTranslationSentences,...reviewedTypingTextSentences]},
  {id:"exercises",dir:"exercises",records:[...exercises,...grammarScaleExercises,...reviewedE06Exercises,...reviewedTranslations,...reviewedCloze]},
  {id:"dialogues",dir:"dialogues",records:reviewedDialogues},
  {id:"mistakes",dir:"mistakes",records:[...reviewedCommonMistakes,...grammarScaleMistakes]}
]}));
results.push(await publishDataset({dataset:"phrases",baseDir:"shared/phrases",groups:[
  {id:"collocations",dir:"collocations",records:e04Collocations},
  {id:"verb-patterns",dir:"verb-patterns",records:e04VerbPatterns},
  {id:"phrases",dir:"items",records:e04Phrases}
]}));

console.log("Published English content:",results.map(result=>result.dataset+"="+result.count).join(", "));
