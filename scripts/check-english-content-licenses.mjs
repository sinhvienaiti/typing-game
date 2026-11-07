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
for (const id of ["verbnet","cambridge-profile","viwiktionary-en","simplewiktionary-en"]) {
  const source=manifest.sources.find(item=>item.id===id);
  if (!source||source.publishAllowed!==false) errors.push(id+": publish gate must be false");
}
const multiwozSource=manifest.sources.find(item=>item.id==="multiwoz");
if (!multiwozSource||multiwozSource.license!=="MIT"||multiwozSource.publishAllowed!==true||multiwozSource.attributionRequired!==true||!multiwozSource.sourceCommit) {
  errors.push("multiwoz: pinned MIT source with attribution is required");
}
const tatoebaSource=manifest.sources.find(item=>item.id==="tatoeba");
if (!tatoebaSource||tatoebaSource.publishAllowed!==true||tatoebaSource.attributionRequired!==true) {
  errors.push("tatoeba: publication must require attribution");
}
// This checks the approved pin's metadata without fetching mutable exports.
// Raw-byte SHA-256 verification remains mandatory in import-tatoeba-e06-translations.mjs.
const tatoebaPin=await readJson(path.join(root,"content","english","sources","tatoeba-eng-vie-pilot.json"));
if (
  tatoebaPin.schemaVersion!==1||
  tatoebaPin.source!=="tatoeba"||
  !tatoebaPin.snapshot?.trim()||
  tatoebaPin.license!=="CC-BY-2.0-FR"||
  !tatoebaPin.attribution?.trim()
) errors.push("tatoeba: approved E06 source pin metadata is invalid");
for (const key of ["engSentences","vieSentences","links"]) {
  const entry=tatoebaPin.files?.[key];
  if (!entry||!/^[a-f0-9]{64}$/.test(entry.contentSha256??"")) {
    errors.push("tatoeba: missing or malformed pinned content SHA-256 for "+key);
  }
  if (!entry?.url?.startsWith("https://")) {
    errors.push("tatoeba: approved source URL must use HTTPS for "+key);
  }
}
const simpleSource=manifest.sources.find(item=>item.id==="simplewiktionary-en");
if (!simpleSource?.checksumSha256||!/^[a-f0-9]{64}$/.test(simpleSource.checksumSha256)) {
  errors.push("simplewiktionary-en: pinned checksum is required");
}
const viSource=manifest.sources.find(item=>item.id==="viwiktionary-en");
if (!viSource?.checksumSha256||!/^[a-f0-9]{64}$/.test(viSource.checksumSha256)) {
  errors.push("viwiktionary-en: pinned checksum is required");

}
if (errors.length) { console.error(errors.join("\n")); process.exitCode=1; }
else console.log("English content license gates PASS: "+manifest.sources.length+" sources.");
