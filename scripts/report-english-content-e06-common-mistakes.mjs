import path from "node:path";
import { fileURLToPath } from "node:url";
import { normalizeSentenceKey, readJson } from "./english-content-core.mjs";
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const [doc,topicsDoc]=await Promise.all([
  readJson(path.join(root,"content","english","review-queues","grammar-e06-common-mistakes.json")),
  readJson(path.join(root,"content","english","grammar","pilot-topics.json")),
]);
const errors=[],ids=new Set(),incorrectKeys=new Set(),coverage={};
const topicIds=new Set((topicsDoc.records??[]).map(topic=>topic.id));
for (const record of doc.records??[]) {
  if (ids.has(record.id)) errors.push("duplicate common-mistake id: "+record.id);
  ids.add(record.id);
  const key=normalizeSentenceKey(record.incorrect);
  if (incorrectKeys.has(key)) errors.push(record.id+": duplicate incorrect sentence");
  incorrectKeys.add(key);
  if (record.quality?.state!=="candidate") errors.push(record.id+": must remain candidate");
  if (record.corrections?.length!==1) errors.push(record.id+": expected one canonical correction");
  const grammarId=record.targetIds?.[0];
  if (!topicIds.has(grammarId)) errors.push(record.id+": unknown grammar target "+String(grammarId));
  coverage[grammarId]=(coverage[grammarId]??0)+1;
}
if ((doc.records??[]).length!==100) errors.push("E06 common-mistake pilot must contain exactly 100 records");
for (const grammarId of topicIds) {
  if ((coverage[grammarId]??0)<6) errors.push("insufficient common-mistake coverage for "+grammarId);
}
console.log(JSON.stringify({count:doc.records?.length??0,coverage},null,2));
if (errors.length) { console.error(errors.join("\n")); process.exitCode=1; }
