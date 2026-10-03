import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const batchManifest=await readJson(path.join(root,"content","english","batches","manifest.json"));
const contentVersion=batchManifest.contentVersion;
const shardSize=500;

async function loadRecords(relative) {
  const doc=await readJson(path.join(root,relative));
  if (!Array.isArray(doc.records)) throw new Error(relative+" must contain records[]");
  return doc.records;
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

const lexemes=await loadRecords("content/english/dictionary/lexeme-seed-pilot.json");
const topics=await loadRecords("content/english/grammar/pilot-topics.json");
const sentences=await loadRecords("content/english/sentences/pilot-sentences.json");
const exercises=await loadRecords("content/english/sentences/pilot-exercises.json");
const collocations=await loadRecords("content/english/phrases/pilot-collocations.json");
const verbPatterns=await loadRecords("content/english/phrases/pilot-verb-patterns.json");
const phrases=await loadRecords("content/english/phrases/pilot-phrases.json");

await fs.mkdir(path.join(root,"shared","dictionary"),{recursive:true});
await fs.mkdir(path.join(root,"shared","grammar"),{recursive:true});
await fs.mkdir(path.join(root,"shared","sentences"),{recursive:true});
await fs.mkdir(path.join(root,"shared","phrases"),{recursive:true});

const results=[];
results.push(await publishDataset({dataset:"dictionary",baseDir:"shared/dictionary",groups:[{id:"lexemes",dir:"lexemes",records:lexemes}]}));
results.push(await publishDataset({dataset:"grammar",baseDir:"shared/grammar",groups:[{id:"topics",dir:"topics",records:topics}]}));
results.push(await publishDataset({dataset:"sentences",baseDir:"shared/sentences",groups:[
  {id:"examples",dir:"examples",records:sentences},
  {id:"exercises",dir:"exercises",records:exercises}
]}));
results.push(await publishDataset({dataset:"phrases",baseDir:"shared/phrases",groups:[
  {id:"collocations",dir:"collocations",records:collocations},
  {id:"verb-patterns",dir:"verb-patterns",records:verbPatterns},
  {id:"phrases",dir:"items",records:phrases}
]}));

console.log("Published English content:",results.map(result=>result.dataset+"="+result.count).join(", "));
