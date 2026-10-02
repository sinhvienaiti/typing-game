import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const queue=await readJson(path.join(root,"content","english","review-queues","viwiktionary-en-pilot.json"));
const errors=[];
if (queue.source!=="viwiktionary-en") errors.push("unexpected source id");
if (queue.records.length+queue.misses.length!==300) errors.push("queue must account for exactly 300 pilot lexemes");
if (!/^[a-f0-9]{64}$/.test(queue.sourceSha256)) errors.push("source SHA-256 is invalid");
const seen=new Set();
for (const record of queue.records) {
  if (seen.has(record.lexemeId)) errors.push("duplicate lexeme: "+record.lexemeId);
  seen.add(record.lexemeId);
  if (record.quality?.state!=="candidate") errors.push(record.lexemeId+": must remain candidate");
  if (!record.entries.some(entry=>entry.senses.length>0)) errors.push(record.lexemeId+": has no Vietnamese sense glosses");
}
console.log(JSON.stringify(queue.metrics,null,2));
console.log("sourceSha256="+queue.sourceSha256);
if (errors.length) { console.error(errors.join("\n")); process.exitCode=1; }
