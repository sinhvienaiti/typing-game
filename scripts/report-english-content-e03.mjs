import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson } from "./english-content-core.mjs";
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const args=new Map(process.argv.slice(2).filter(v=>v.startsWith("--")).map(raw=>{const i=raw.indexOf("=");return i<0?[raw,"true"]:[raw.slice(0,i),raw.slice(i+1)];}));
const file=path.resolve(root,args.get("--file")??"content/english/review-queues/oewn-2025-pilot.json");
const requiredMapped=Number(args.get("--require-mapped")??"0");
const doc=await readJson(file);
const errors=[];
if(doc.sourceCommit!=="dc343f2683279ecbb13fab4e2fd778d7b162d287") errors.push("source commit is not pinned to the approved OEWN commit");
if(doc.publicationAllowed!==false) errors.push("review queue must not be directly publishable");
if(doc.records.length+doc.misses.length!==300) errors.push("pilot must account for exactly 300 seeds");
if(doc.sourceErrors.length!==0) errors.push("sourceErrors must be empty");
if(doc.metrics.mappedRate<requiredMapped) errors.push("mapped rate "+doc.metrics.mappedRate+" is below "+requiredMapped);
if(doc.metrics.definitionRate!==1) errors.push("every imported sense must have at least one English definition");
for(const record of doc.records) {
  if(record.quality?.state!=="candidate") errors.push(record.lexemeId+": must remain candidate");
  for(const part of record.parts) for(const sense of part.senses) {
    if(sense.explanationVi!==null) errors.push(record.lexemeId+": pinned source importer must not invent Vietnamese sense explanations");
  }
}
console.log(JSON.stringify(doc.metrics,null,2));
if(errors.length){console.error(errors.join("\n"));process.exitCode=1;}
