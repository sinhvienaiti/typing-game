import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson } from "./english-content-core.mjs";
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const [doc,manifest]=await Promise.all([
  readJson(path.join(root,"content","english","review-queues","simplewiktionary-en-pilot.json")),
  readJson(path.join(root,"content","english","sources","manifest.json")),
]);
const source=manifest.sources?.find(item=>item.id==="simplewiktionary-en");
const errors=[];
if (doc.records?.length!==300) errors.push("Simple Wiktionary pilot must contain exactly 300 seed records");
if ((doc.metrics?.mappedRate??0)<0.70) errors.push("Simple Wiktionary pilot mapped rate below 70%");
if (!/^[a-f0-9]{64}$/.test(doc.sourceSha256??"")) errors.push("Simple Wiktionary source SHA-256 is invalid");
if (source?.checksumSha256&&source.checksumSha256!==doc.sourceSha256) errors.push("Simple Wiktionary queue checksum does not match source manifest");
for (const record of doc.records??[]) {
  if (record.quality?.state!=="candidate") errors.push(record.lexemeId+": morphology/usage pilot must remain candidate");
  if (source?.checksumSha256&&record.quality?.checks?.sourcePin?.status!=="pass") {
    errors.push(record.lexemeId+": pinned source must report sourcePin pass");
  }
}
console.log(JSON.stringify(doc.metrics,null,2));
if (errors.length) { console.error(errors.join("\n")); process.exitCode=1; }
