import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson } from "./english-content-core.mjs";
import { buildGameEnglishActivityDataset } from "../shared/english-content/game-adapters.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const manifest=await readJson(path.join(root,"content","english","batches","manifest.json"));
const errors=[];
const results=[];

for (const batch of manifest.batches??[]) {
  const byId=new Map((batch.recordSets??[]).map(set=>[set.id,set]));
  for (const smoke of batch.gameSmokes??[]) {
    const set=byId.get(smoke.recordSetId);
    if (!set) {
      errors.push(batch.id+": missing smoke record set "+smoke.recordSetId);
      continue;
    }
    let doc;
    try {
      doc=await readJson(path.join(root,set.path));
    } catch (error) {
      errors.push(batch.id+"/"+smoke.recordSetId+": "+error.message);
      continue;
    }
    const records=(doc.records??[]).slice(0,smoke.sampleCount);
    if (records.length!==smoke.sampleCount) {
      errors.push(batch.id+"/"+smoke.recordSetId+": insufficient records for smoke sample");
      continue;
    }
    try {
      const dataset=buildGameEnglishActivityDataset(
        smoke.gameId,
        smoke.activity,
        records,
        "e10-"+batch.id+"-"+smoke.gameId+"-"+smoke.activity,
        {allowUnpublished:true,createdAt:"2026-10-03T00:00:00.000Z"},
      );
      if (dataset.items.length===0||dataset.items.length>100) {
        throw new Error("adapter produced invalid item count "+dataset.items.length);
      }
      results.push({
        batchId:batch.id,
        gameId:smoke.gameId,
        activity:smoke.activity,
        sourceRecords:records.length,
        activityItems:dataset.items.length,
      });
    } catch (error) {
      errors.push(batch.id+"/"+smoke.gameId+"/"+smoke.activity+": "+error.message);
    }
  }
}
console.log(JSON.stringify({smokes:results},null,2));
if (errors.length) {
  console.error(errors.join("\n"));
  process.exitCode=1;
}
