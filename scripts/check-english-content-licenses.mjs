import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson } from "./english-content-core.mjs";
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const manifest=await readJson(path.join(root,"content","english","sources","manifest.json"));
const errors=[],ids=new Set();
for (const source of manifest.sources??[]) {
  if (ids.has(source.id)) errors.push("duplicate source id: "+source.id); ids.add(source.id);
  if (!source.license) errors.push(source.id+": license is required");
  if (source.publishAllowed&&source.status==="blocked") errors.push(source.id+": blocked source cannot be publishAllowed");
  if (!source.publishAllowed&&source.status==="import-enabled") errors.push(source.id+": non-publishable source cannot be import-enabled");
}
for (const id of ["verbnet","cambridge-profile"]) {
  const source=manifest.sources.find(item=>item.id===id);
  if (!source||source.publishAllowed!==false) errors.push(id+": publish gate must be false");
}
if (errors.length) { console.error(errors.join("\n")); process.exitCode=1; }
else console.log("English content license gates PASS: "+manifest.sources.length+" sources.");
