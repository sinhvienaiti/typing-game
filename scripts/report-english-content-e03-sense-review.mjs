import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson } from "./english-content-core.mjs";
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const doc=await readJson(path.join(root,"content","english","review-queues","e03-sense-alignment-review.json"));
const errors=[];
if (doc.records?.length!==300) errors.push("E03 sense review must contain 300 records");
if ((doc.metrics?.bothSources??0)<290) errors.push("E03 bilingual source coverage fell below 290/300");
if ((doc.metrics?.posOverlapRecords??0)<250) errors.push("E03 POS overlap fell below 250/300");
for (const record of doc.records??[]) {
  if (record.quality?.state!=="candidate") errors.push(record.lexemeId+": review packet must remain candidate");
  if (record.quality?.checks?.senseAlignment?.status!=="pending") errors.push(record.lexemeId+": sense alignment must remain pending until editorial review");
}
console.log(JSON.stringify(doc.metrics,null,2));
if (errors.length) { console.error(errors.join("\n")); process.exitCode=1; }
