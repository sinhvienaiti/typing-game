import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const [batchManifest,deprecations]=await Promise.all([
  readJson(path.join(root,"content","english","batches","manifest.json")),
  readJson(path.join(root,"content","english","migrations","deprecations.json")),
]);
const runtimeFiles={
  dictionary:"shared/dictionary/manifest.json",
  grammar:"shared/grammar/manifest.json",
  sentences:"shared/sentences/manifest.json",
  phrases:"shared/phrases/manifest.json",
  attribution:"shared/attribution/english-content/manifest.json",
};
const runtimeCounts={};
for (const [name,relative] of Object.entries(runtimeFiles)) {
  const manifest=await readJson(path.join(root,relative));
  if (manifest.contentVersion!==batchManifest.contentVersion) {
    throw new Error(relative+": contentVersion does not match controlled batch manifest");
  }
  runtimeCounts[name]=manifest.count;
}
const batchStates={};
for (const batch of batchManifest.batches??[]) {
  batchStates[batch.state]=(batchStates[batch.state]??0)+1;
}
const totalRuntime=Object.entries(runtimeCounts)
  .filter(([key])=>key!=="attribution")
  .reduce((sum,[,value])=>sum+value,0);
const notes=totalRuntime===0
  ?[
      "Rich-content architecture and pilot pipelines are versioned, but no rich records are published in this release.",
      "Legacy shared/vocabulary remains the production vocabulary ABI and is unchanged by this release."
    ]
  :[
      "Runtime counts reflect records that passed the reviewed-only publication gate.",
      "Legacy shared/vocabulary remains backward compatible; rich content ships as sidecar datasets."
    ];
const release={
  schemaVersion:1,
  contentVersion:batchManifest.contentVersion,
  runtimeCounts,
  batchStates,
  migrationCount:deprecations.mappings?.length??0,
  notes,
};
const output=path.join(root,"content","english","releases",batchManifest.contentVersion+".json");
await fs.mkdir(path.dirname(output),{recursive:true});
await fs.writeFile(output,stableJson(release),"utf8");
console.log(JSON.stringify(release,null,2));
