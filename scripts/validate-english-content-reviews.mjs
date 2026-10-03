import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";
import {
  applyEnglishReviewDecision,
  buildEnglishReviewDecisionIndex,
  englishContentRecordDigest,
  englishContentRecordId,
} from "./english-review-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const [batchManifest,ledger]=await Promise.all([
  readJson(path.join(root,"content","english","batches","manifest.json")),
  readJson(path.join(root,"content","english","reviews","decisions.json")),
]);
const errors=[];
try { buildEnglishReviewDecisionIndex(ledger); } catch (error) { errors.push(error.message); }

const batchById=new Map((batchManifest.batches??[]).map(batch=>[batch.id,batch]));
let applied=0,publishDecisions=0;
for (const decision of ledger.decisions??[]) {
  const batch=batchById.get(decision.batchId);
  if (!batch) { errors.push(decision.id+": unknown batch "+decision.batchId); continue; }
  const set=batch.recordSets?.find(item=>item.id===decision.recordSetId);
  if (!set) { errors.push(decision.id+": unknown recordSet "+decision.recordSetId); continue; }
  let doc;
  try { doc=await readJson(path.join(root,set.path)); }
  catch (error) {
    if (set.generated) errors.push(decision.id+": generated source is unavailable; run its batch generator before review validation");
    else errors.push(decision.id+": "+error.message);
    continue;
  }
  const matches=(doc.records??[]).filter((record,index)=>englishContentRecordId(record,index)===decision.recordId);
  if (matches.length!==1) {
    errors.push(decision.id+": expected exactly one source record, got "+matches.length);
    continue;
  }
  const record=matches[0];
  const digest=englishContentRecordDigest(record);
  if (digest!==decision.sourceDigest) {
    errors.push(decision.id+": stale source digest; current="+digest);
    continue;
  }
  try {
    applyEnglishReviewDecision(record,decision,{requiredChecks:set.requiredChecks});
    applied++;
    if (decision.targetState==="published") publishDecisions++;
  } catch (error) {
    errors.push(error.message);
  }
}

const report={
  schemaVersion:1,
  contentVersion:batchManifest.contentVersion,
  decisions:ledger.decisions?.length??0,
  applied,
  publishDecisions,
  ledgerDigest:englishContentRecordDigest(ledger),
};
await fs.mkdir(path.join(root,"content","english","reports"),{recursive:true});
await fs.writeFile(
  path.join(root,"content","english","reports","e10-review-ledger.json"),
  stableJson(report),
  "utf8",
);
console.log(JSON.stringify(report,null,2));
if (errors.length) {
  console.error(errors.join("\n"));
  process.exitCode=1;
}
