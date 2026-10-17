import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createSchemaValidator, readJson, stableJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const schemaDir=path.join(root,"shared","schemas","english-content");
const [commonSchema,batchSchema,manifest]=await Promise.all([
  readJson(path.join(schemaDir,"common.schema.json")),
  readJson(path.join(schemaDir,"batch-manifest.schema.json")),
  readJson(path.join(root,"content","english","batches","manifest.json")),
]);
const {validate}=createSchemaValidator([commonSchema,batchSchema]);
const errors=[...validate(manifest,batchSchema)];
const report={
  schemaVersion:1,
  contentVersion:manifest.contentVersion,
  batches:[],
  totals:{records:0,byState:{},byCefr:{}},
};

function recordId(record,index) {
  const value=record?.id??record?.lexemeId;
  return typeof value==="string"&&value.trim()!==""?value:"#"+String(index+1);
}
function addCounter(target,key,amount=1) {
  target[key]=(target[key]??0)+amount;
}
function checksReadyForPublication(record,requiredChecks) {
  const checks=record?.quality?.checks??{};
  for (const name of requiredChecks) {
    const status=checks?.[name]?.status;
    if (status!=="pass"&&status!=="not-applicable") return false;
  }
  for (const check of Object.values(checks)) {
    if (check?.status==="fail"||check?.status==="pending") return false;
  }
  return true;
}

const batchIds=new Set();
for (const batch of manifest.batches??[]) {
  if (batchIds.has(batch.id)) errors.push(batch.id+": duplicate batch id");
  batchIds.add(batch.id);
  const setIds=new Set();
  const batchReport={
    id:batch.id,
    phase:batch.phase,
    state:batch.state,
    category:batch.category,
    records:0,
    recordSets:[],
    byState:{},
    byCefr:{},
    requiredBeforePublish:[...batch.requiredBeforePublish],
  };

  for (const set of batch.recordSets??[]) {
    if (setIds.has(set.id)) errors.push(batch.id+": duplicate recordSet id "+set.id);
    setIds.add(set.id);
    let doc;
    try {
      doc=await readJson(path.join(root,set.path));
    } catch (error) {
      errors.push(batch.id+"/"+set.id+": "+error.message);
      continue;
    }
    if (!Array.isArray(doc.records)) {
      errors.push(batch.id+"/"+set.id+": file must contain records[]");
      continue;
    }
    if (doc.records.length!==set.expectedCount) {
      errors.push(batch.id+"/"+set.id+": expected "+set.expectedCount+" records, got "+doc.records.length);
    }
    const ids=new Set(),setStates={},setCefr={};
    for (let index=0;index<doc.records.length;index++) {
      const record=doc.records[index];
      const id=recordId(record,index);
      if (ids.has(id)) errors.push(batch.id+"/"+set.id+": duplicate record id "+id);
      ids.add(id);

      const state=record?.quality?.state;
      if (!set.allowedQualityStates.includes(state)) {
        errors.push(batch.id+"/"+set.id+"/"+id+": quality state "+String(state)+" is not allowed");
      }
      addCounter(setStates,String(state));
      addCounter(batchReport.byState,String(state));
      addCounter(report.totals.byState,String(state));

      const cefr=record?.cefr;
      if (typeof cefr==="string") {
        addCounter(setCefr,cefr);
        addCounter(batchReport.byCefr,cefr);
        addCounter(report.totals.byCefr,cefr);
        if (batch.cefr.length>0&&!batch.cefr.includes(cefr)) {
          errors.push(batch.id+"/"+set.id+"/"+id+": CEFR "+cefr+" is outside batch scope");
        }
      }

      const checks=record?.quality?.checks??{};
      for (const required of set.requiredChecks) {
        if (!checks?.[required]) {
          errors.push(batch.id+"/"+set.id+"/"+id+": missing required quality check "+required);
        } else if (checks[required].status==="fail") {
          errors.push(batch.id+"/"+set.id+"/"+id+": required quality check failed: "+required);
        }
      }
      if (batch.state==="published") {
        if (state!=="published") errors.push(batch.id+"/"+set.id+"/"+id+": published batch contains non-published record");
        if (!checksReadyForPublication(record,set.requiredChecks)) {
          errors.push(batch.id+"/"+set.id+"/"+id+": published record has unfinished quality checks");
        }
      }
    }
    batchReport.records+=doc.records.length;
    report.totals.records+=doc.records.length;
    batchReport.recordSets.push({
      id:set.id,
      path:set.path,
      generated:set.generated,
      expectedCount:set.expectedCount,
      actualCount:doc.records.length,
      byState:setStates,
      byCefr:setCefr,
      digest:stableJson(doc).length,
    });
  }

  for (const smoke of batch.gameSmokes??[]) {
    if (!setIds.has(smoke.recordSetId)) {
      errors.push(batch.id+": game smoke references unknown recordSet "+smoke.recordSetId);
    }
  }
  report.batches.push(batchReport);
}

await fs.mkdir(path.join(root,"content","english","reports"),{recursive:true});
await fs.writeFile(
  path.join(root,"content","english","reports","e10-batch-report.json"),
  stableJson(report),
  "utf8",
);
console.log(JSON.stringify(report,null,2));
if (errors.length) {
  console.error(errors.join("\n"));
  process.exitCode=1;
}
