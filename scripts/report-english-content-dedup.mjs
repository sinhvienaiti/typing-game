import path from "node:path";
import { fileURLToPath } from "node:url";
import { listJsonFiles, nearDuplicatePairs, normalizeSentenceKey, readJson } from "./english-content-core.mjs";
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const files=await listJsonFiles(path.join(root,"shared","sentences")); const records=[];
for (const file of files) {
  if (file.endsWith("manifest.json")) continue;
  const doc=await readJson(file);
  if (Array.isArray(doc.records)) for (const record of doc.records) if (record&&typeof record.id==="string"&&typeof record.text==="string") records.push(record);
}
const exact=new Map(),duplicates=[];
for (const record of records) {
  const key=normalizeSentenceKey(record.text),previous=exact.get(key);
  if (previous) duplicates.push([previous,record.id]); else exact.set(key,record.id);
}
const near=nearDuplicatePairs(records,0.86);
if (duplicates.length) { console.error("Exact sentence duplicates:"); for (const pair of duplicates) console.error(pair.join(" <-> ")); process.exitCode=1; }
else console.log("Sentence dedupe PASS: "+records.length+" records, 0 exact duplicates, "+near.length+" near-duplicate review candidates.");
