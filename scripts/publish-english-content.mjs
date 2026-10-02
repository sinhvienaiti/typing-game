import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const contentVersion="2026.10.0";
const shardSize=500;

async function loadRecords(relative) {
  const doc=await readJson(path.join(root,relative));
  if (!Array.isArray(doc.records)) throw new Error(relative+" must contain records[]");
  return doc.records;
}
function published(records) {
  return records.filter(record=>record?.quality?.state==="published");
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
    const records=published(group.records);
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

await fs.mkdir(path.join(root,"shared","dictionary"),{recursive:true});
await fs.mkdir(path.join(root,"shared","grammar"),{recursive:true});
await fs.mkdir(path.join(root,"shared","sentences"),{recursive:true});

const results=[];
results.push(await publishDataset({dataset:"dictionary",baseDir:"shared/dictionary",groups:[{id:"lexemes",dir:"lexemes",records:lexemes}]}));
results.push(await publishDataset({dataset:"grammar",baseDir:"shared/grammar",groups:[{id:"topics",dir:"topics",records:topics}]}));
results.push(await publishDataset({dataset:"sentences",baseDir:"shared/sentences",groups:[
  {id:"examples",dir:"examples",records:sentences},
  {id:"exercises",dir:"exercises",records:exercises}
]}));

console.log("Published English content:",results.map(result=>result.dataset+"="+result.count).join(", "));
