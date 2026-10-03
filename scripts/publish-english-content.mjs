import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";
import { overlayEnglishReviewDecisions } from "./english-review-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const [batchManifest,reviewLedger]=await Promise.all([
  readJson(path.join(root,"content","english","batches","manifest.json")),
  readJson(path.join(root,"content","english","reviews","decisions.json")),
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
const topics=await loadRecords("content/english/grammar/pilot-topics.json");
const sentences=await loadRecords("content/english/sentences/pilot-sentences.json");
const exercises=await loadRecords("content/english/sentences/pilot-exercises.json");
const reviewedE06Exercises=await loadRecords("content/english/sentences/e06-reviewed-exercises.json");
const reviewedTranslationSentences=await loadRecords("content/english/sentences/e06-reviewed-translation-sentences.json");
const reviewedTranslations=await loadRecords("content/english/sentences/e06-reviewed-translations.json");
const reviewedTypingTextSentences=await loadRecords("content/english/sentences/e06-reviewed-typing-text-sentences.json");
const reviewedCloze=await loadRecords("content/english/sentences/e06-reviewed-cloze.json");
const reviewedDialogues=await loadRecords("content/english/sentences/e06-reviewed-dialogues.json");
const reviewedCommonMistakes=await loadRecords("content/english/sentences/e06-reviewed-common-mistakes.json");
const collocations=await loadRecords("content/english/phrases/pilot-collocations.json");
const verbPatterns=await loadRecords("content/english/phrases/pilot-verb-patterns.json");
const phrases=await loadRecords("content/english/phrases/pilot-phrases.json");
const scaleCollocations=await loadRecords("content/english/phrases/e04-scale-01-collocations.json");
const scaleVerbPatterns=await loadRecords("content/english/phrases/e04-scale-01-verb-patterns.json");
const scalePhrases=await loadRecords("content/english/phrases/e04-scale-01-phrases.json");
const scale02Collocations=await loadRecords("content/english/phrases/e04-scale-02-collocations.json");
const scale02VerbPatterns=await loadRecords("content/english/phrases/e04-scale-02-verb-patterns.json");
const scale02Phrases=await loadRecords("content/english/phrases/e04-scale-02-phrases.json");
const scale03Collocations=await loadRecords("content/english/phrases/e04-scale-03-collocations.json");
const scale03VerbPatterns=await loadRecords("content/english/phrases/e04-scale-03-verb-patterns.json");
const scale03Phrases=await loadRecords("content/english/phrases/e04-scale-03-phrases.json");
const scale04Collocations=await loadRecords("content/english/phrases/e04-scale-04-collocations.json");
const scale04VerbPatterns=await loadRecords("content/english/phrases/e04-scale-04-verb-patterns.json");
const scale04Phrases=await loadRecords("content/english/phrases/e04-scale-04-phrases.json");
const scale05Collocations=await loadRecords("content/english/phrases/e04-scale-05-collocations.json");
const scale05VerbPatterns=await loadRecords("content/english/phrases/e04-scale-05-verb-patterns.json");
const scale05Phrases=await loadRecords("content/english/phrases/e04-scale-05-phrases.json");
const scale06Collocations=await loadRecords("content/english/phrases/e04-scale-06-collocations.json");
const scale06VerbPatterns=await loadRecords("content/english/phrases/e04-scale-06-verb-patterns.json");
const scale06Phrases=await loadRecords("content/english/phrases/e04-scale-06-phrases.json");

await fs.mkdir(path.join(root,"shared","dictionary"),{recursive:true});
await fs.mkdir(path.join(root,"shared","grammar"),{recursive:true});
await fs.mkdir(path.join(root,"shared","sentences"),{recursive:true});
await fs.mkdir(path.join(root,"shared","phrases"),{recursive:true});

const results=[];
results.push(await publishDataset({dataset:"dictionary",baseDir:"shared/dictionary",groups:[
  {id:"lexemes",dir:"lexemes",records:lexemes},
  {id:"senses",dir:"senses",records:senses}
]}));
results.push(await publishDataset({dataset:"grammar",baseDir:"shared/grammar",groups:[{id:"topics",dir:"topics",records:topics}]}));
results.push(await publishDataset({dataset:"sentences",baseDir:"shared/sentences",groups:[
  {id:"examples",dir:"examples",records:[...sentences,...reviewedTranslationSentences,...reviewedTypingTextSentences]},
  {id:"exercises",dir:"exercises",records:[...exercises,...reviewedE06Exercises,...reviewedTranslations,...reviewedCloze]},
  {id:"dialogues",dir:"dialogues",records:reviewedDialogues},
  {id:"mistakes",dir:"mistakes",records:reviewedCommonMistakes}
]}));
results.push(await publishDataset({dataset:"phrases",baseDir:"shared/phrases",groups:[
  {id:"collocations",dir:"collocations",records:[...collocations,...scaleCollocations,...scale02Collocations,...scale03Collocations,...scale04Collocations,...scale05Collocations,...scale06Collocations]},
  {id:"verb-patterns",dir:"verb-patterns",records:[...verbPatterns,...scaleVerbPatterns,...scale02VerbPatterns,...scale03VerbPatterns,...scale04VerbPatterns,...scale05VerbPatterns,...scale06VerbPatterns]},
  {id:"phrases",dir:"items",records:[...phrases,...scalePhrases,...scale02Phrases,...scale03Phrases,...scale04Phrases,...scale05Phrases,...scale06Phrases]}
]}));

console.log("Published English content:",results.map(result=>result.dataset+"="+result.count).join(", "));
