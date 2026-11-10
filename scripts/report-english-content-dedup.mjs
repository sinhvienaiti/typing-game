import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  listJsonFiles,
  nearDuplicatePairs,
  normalizeSentenceKey,
  readJson,
} from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const files=[
  ...(await listJsonFiles(path.join(root,"shared","sentences"))),
  path.join(root,"content","english","sentences","pilot-sentences.json"),
];
const records=[];
const byId=new Map();
const idCollisions=[];

for (const file of files) {
  if (file.endsWith("manifest.json")) continue;
  const doc=await readJson(file);
  if (!Array.isArray(doc.records)) continue;

  for (const record of doc.records) {
    if (!record||typeof record.id!=="string"||typeof record.text!=="string") continue;
    const normalized=normalizeSentenceKey(record.text);
    const previous=byId.get(record.id);

    if (previous!==undefined) {
      if (previous.normalized!==normalized) {
        idCollisions.push({
          id:record.id,
          leftFile:previous.file,
          rightFile:file,
        });
      }
      // A published runtime shard is an intentional mirror of its canonical
      // authoring record. Count the stable ID once for content dedupe.
      continue;
    }

    byId.set(record.id,{normalized,file});
    records.push(record);
  }
}

const exact=new Map();
const duplicates=[];
for (const record of records) {
  const key=normalizeSentenceKey(record.text);
  const previous=exact.get(key);
  if (previous!==undefined) duplicates.push([previous,record.id]);
  else exact.set(key,record.id);
}
const near=nearDuplicatePairs(records,0.86);

if (idCollisions.length) {
  console.error("Sentence ID collisions with different text:");
  for (const collision of idCollisions) {
    console.error(
      collision.id+" <-> "+collision.leftFile+" <-> "+collision.rightFile,
    );
  }
  process.exitCode=1;
}
if (duplicates.length) {
  console.error("Exact sentence duplicates:");
  for (const pair of duplicates) console.error(pair.join(" <-> "));
  process.exitCode=1;
}
if (!idCollisions.length&&!duplicates.length) {
  console.log(
    "Sentence dedupe PASS: "+
    records.length+
    " unique stable IDs, 0 exact duplicates, "+
    near.length+
    " near-duplicate review candidates.",
  );
}
