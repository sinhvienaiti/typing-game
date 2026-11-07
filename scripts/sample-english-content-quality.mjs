import crypto from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const manifest=await readJson(path.join(root,"content","english","batches","manifest.json"));
const samples=[];
function idOf(record,index) {
  const value=record?.id??record?.lexemeId;
  return typeof value==="string"&&value.trim()!==""?value:"#"+String(index+1);
}
function score(value) {
  return crypto.createHash("sha256").update(value).digest("hex");
}
for (const batch of manifest.batches??[]) {
  for (const set of batch.recordSets??[]) {
    let doc;
    try {
      doc=await readJson(path.join(root,set.path));
    } catch {
      continue;
    }
    const ranked=(doc.records??[]).map((record,index)=>({
      id:idOf(record,index),
      qualityState:record?.quality?.state??null,
      hash:score(batch.id+"\u0000"+set.id+"\u0000"+idOf(record,index)),
    })).sort((a,b)=>a.hash.localeCompare(b.hash));
    const take=Math.min(3,ranked.length);
    for (const item of ranked.slice(0,take)) {
      samples.push({
        batchId:batch.id,
        recordSetId:set.id,
        path:set.path,
        recordId:item.id,
        qualityState:item.qualityState,
        reviewStatus:"pending",
      });
    }
  }
}
const output={schemaVersion:1,contentVersion:manifest.contentVersion,samples};
await fs.mkdir(path.join(root,"content","english","reports"),{recursive:true});
await fs.writeFile(
  path.join(root,"content","english","reports","e12-quality-sample.json"),
  stableJson(output),
  "utf8",
);
console.log(JSON.stringify({sampleCount:samples.length},null,2));
