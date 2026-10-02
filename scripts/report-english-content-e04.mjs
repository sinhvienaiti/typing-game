import path from "node:path";import{fileURLToPath}from"node:url";import{readJson}from"./english-content-core.mjs";
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const [c,p,f]=await Promise.all([
 readJson(path.join(root,"content","english","phrases","pilot-collocations.json")),
 readJson(path.join(root,"content","english","phrases","pilot-verb-patterns.json")),
 readJson(path.join(root,"content","english","phrases","pilot-phrases.json"))
]);
console.log(JSON.stringify({collocations:c.records.length,verbPatterns:p.records.length,phrasalVerbs:f.records.filter(x=>x.type==="phrasal-verb").length,chunksAndIdioms:f.records.filter(x=>x.type!=="phrasal-verb").length,state:"draft-review-required"},null,2));
