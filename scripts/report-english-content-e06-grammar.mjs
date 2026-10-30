import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const [sourceDoc,correctionDoc,transformationDoc]=await Promise.all([
  readJson(path.join(root,"content","english","sentences","pilot-sentences.json")),
  readJson(path.join(root,"content","english","review-queues","grammar-e06-corrections.json")),
  readJson(path.join(root,"content","english","review-queues","grammar-e06-transformations.json")),
]);
const sourceById=new Map(sourceDoc.records.map(item=>[item.id,item]));
const corrections=correctionDoc.records??[];
const transformations=transformationDoc.records??[];
const errors=[];
function normalized(value) {
  return String(value).normalize("NFKC").trim().replace(/\s+/gu," ").toLocaleLowerCase("en-US");
}
function checkCommon(records,type,count) {
  if (records.length!==count) errors.push(type+": expected "+count+", got "+records.length);
  const ids=new Set(),prompts=new Set();
  const grammarCounts=new Map();
  for (const record of records) {
    if (record.type!==type) errors.push(record.id+": wrong type "+record.type);
    if (record.quality?.state!=="candidate") errors.push(record.id+": must remain candidate");
    if (ids.has(record.id)) errors.push(record.id+": duplicate id");
    ids.add(record.id);
    const promptKey=normalized(record.prompt);
    if (prompts.has(promptKey)) errors.push(record.id+": duplicate normalized prompt");
    prompts.add(promptKey);
    const source=sourceById.get(record.sourceSentenceIds?.[0]);
    if (!source) {
      errors.push(record.id+": missing source sentence");
      continue;
    }
    const grammarId=source.grammarIds?.[0];
    if (record.targetIds?.length!==1||record.targetIds[0]!==grammarId) {
      errors.push(record.id+": target grammar does not match source");
    }
    grammarCounts.set(grammarId,(grammarCounts.get(grammarId)??0)+1);
    if (record.acceptedAnswers.length!==1) errors.push(record.id+": expected one canonical answer");
  }
  for (const grammarId of new Set(sourceDoc.records.flatMap(item=>item.grammarIds??[]))) {
    if ((grammarCounts.get(grammarId)??0)<6) errors.push(type+": insufficient coverage for "+grammarId);
  }
  return Object.fromEntries([...grammarCounts.entries()].sort());
}
const correctionCoverage=checkCommon(corrections,"error-correction",100);
for (const record of corrections) {
  const source=sourceById.get(record.sourceSentenceIds?.[0]);
  if (!source) continue;
  if (normalized(record.prompt)===normalized(source.text)) errors.push(record.id+": correction prompt equals source");
  if (normalized(record.acceptedAnswers[0])!==normalized(source.text)) errors.push(record.id+": correction answer must restore source sentence");
}
const transformationCoverage=checkCommon(transformations,"transformation",100);
for (const record of transformations) {
  const source=sourceById.get(record.sourceSentenceIds?.[0]);
  if (!source) continue;
  if (normalized(record.prompt)===normalized(record.acceptedAnswers[0])) errors.push(record.id+": transformation prompt equals answer");
}
console.log(JSON.stringify({
  corrections:corrections.length,
  transformations:transformations.length,
  correctionCoverage,
  transformationCoverage,
},null,2));
if (errors.length) { console.error(errors.join("\n")); process.exitCode=1; }
