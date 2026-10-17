import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const [sources,batches,deprecations,attribution]=await Promise.all([
  readJson(path.join(root,"content","english","sources","manifest.json")),
  readJson(path.join(root,"content","english","batches","manifest.json")),
  readJson(path.join(root,"content","english","migrations","deprecations.json")),
  readJson(path.join(root,"shared","attribution","english-content","manifest.json")),
]);
const errors=[];
const runtimeFiles=[
  "shared/dictionary/manifest.json",
  "shared/grammar/manifest.json",
  "shared/sentences/manifest.json",
  "shared/phrases/manifest.json",
  "shared/attribution/english-content/manifest.json",
];
const runtime=[];
const publishedSourceIds=new Set();
for (const relative of runtimeFiles) {
  const manifest=await readJson(path.join(root,relative));
  runtime.push({path:relative,dataset:manifest.dataset,count:manifest.count,contentVersion:manifest.contentVersion});
  if (manifest.contentVersion!==batches.contentVersion) {
    errors.push(relative+": stale contentVersion "+manifest.contentVersion);
  }
  if (manifest.dataset!=="attribution.english-content") {
    const baseDir=path.dirname(relative);
    for (const shard of manifest.shards??[]) {
      const shardDoc=await readJson(path.join(root,baseDir,shard.path));
      for (const record of shardDoc.records??[]) {
        for (const source of record?.provenance?.sources??[]) {
          if (typeof source?.dataset==="string"&&source.dataset!=="") {
            publishedSourceIds.add(source.dataset);
          }
        }
      }
    }
  }
}
const runtimePublished=runtime
  .filter(item=>item.dataset!=="attribution.english-content")
  .reduce((sum,item)=>sum+item.count,0);
if (runtimePublished===0&&attribution.count!==0) {
  errors.push("attribution runtime must be empty when no rich records are published");
}
const sourceById=new Map((sources.sources??[]).map(source=>[source.id,source]));
const attributionRequiredSourceIds=[...publishedSourceIds]
  .filter(id=>sourceById.get(id)?.attributionRequired===true)
  .sort();
if (attributionRequiredSourceIds.length>0&&attribution.count===0) {
  errors.push(
    "published rich content requires attribution for runtime sources: "+
    attributionRequiredSourceIds.join(", ")
  );
}
if (runtimePublished>0&&attributionRequiredSourceIds.length===0&&attribution.count!==0) {
  errors.push("attribution runtime contains entries although published records require no attribution");
}

const sourceAudit=sources.sources.map(source=>{
  const pinned=Boolean(source.checksumSha256||source.sourceCommit||source.snapshot);
  if (source.status==="blocked"&&source.publishAllowed!==false) {
    errors.push(source.id+": blocked source cannot allow publication");
  }
  return {
    id:source.id,
    publishAllowed:source.publishAllowed,
    attributionRequired:source.attributionRequired,
    status:source.status,
    pinned,
    snapshot:source.snapshot??null,
  };
});

const oldIds=new Set(),replacementIds=new Set();
const graph=new Map();
for (const mapping of deprecations.mappings??[]) {
  if (oldIds.has(mapping.oldId)) errors.push("duplicate deprecated oldId: "+mapping.oldId);
  oldIds.add(mapping.oldId);
  if (mapping.replacementId===mapping.oldId) errors.push(mapping.oldId+": replacement cannot equal oldId");
  if (mapping.replacementId!==null) {
    replacementIds.add(mapping.replacementId);
    graph.set(mapping.oldId,mapping.replacementId);
  }
}
for (const start of graph.keys()) {
  const seen=new Set([start]);
  let current=graph.get(start);
  while (current!==undefined&&graph.has(current)) {
    if (seen.has(current)) {
      errors.push("deprecation cycle detected at "+start);
      break;
    }
    seen.add(current);
    current=graph.get(current);
  }
}

const audit={
  schemaVersion:1,
  contentVersion:batches.contentVersion,
  runtime,
  runtimePublished,
  publishedSourceIds:[...publishedSourceIds].sort(),
  attributionRequiredSourceIds,
  sourceAudit,
  deprecations:{count:deprecations.mappings?.length??0,replacementIds:[...replacementIds].sort()},
};
await fs.mkdir(path.join(root,"content","english","reports"),{recursive:true});
await fs.writeFile(
  path.join(root,"content","english","reports","e12-maintenance-audit.json"),
  stableJson(audit),
  "utf8",
);
console.log(JSON.stringify(audit,null,2));
if (errors.length) {
  console.error(errors.join("\n"));
  process.exitCode=1;
}
