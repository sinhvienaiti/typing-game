import path from "node:path";
import { fileURLToPath } from "node:url";
import { normalizeSentenceKey, readJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const [sentencesDoc,exercisesDoc,sourceReport,pin]=await Promise.all([
  readJson(path.join(root,"content","english","review-queues","tatoeba-e06-sentences.json")),
  readJson(path.join(root,"content","english","review-queues","tatoeba-e06-translations.json")),
  readJson(path.join(root,"content","english","review-queues","tatoeba-e06-source-report.json")),
  readJson(path.join(root,"content","english","sources","tatoeba-eng-vie-pilot.json")),
]);
const sentences=sentencesDoc.records??[];
const exercises=exercisesDoc.records??[];
const errors=[];
if (sentences.length!==300) errors.push("Tatoeba E06 pilot must contain exactly 300 English sentences");
if (exercises.length!==300) errors.push("Tatoeba E06 pilot must contain exactly 300 translation exercises");
const sentenceIds=new Set();
const textKeys=new Set();
for (const sentence of sentences) {
  if (sentenceIds.has(sentence.id)) errors.push("duplicate sentence id: "+sentence.id);
  sentenceIds.add(sentence.id);
  const key=normalizeSentenceKey(sentence.text);
  if (textKeys.has(key)) errors.push("duplicate normalized English sentence: "+sentence.id);
  textKeys.add(key);
  if (sentence.quality?.state!=="candidate") errors.push(sentence.id+": must remain candidate");
}
const exerciseIds=new Set();
for (const exercise of exercises) {
  if (exerciseIds.has(exercise.id)) errors.push("duplicate exercise id: "+exercise.id);
  exerciseIds.add(exercise.id);
  if (exercise.type!=="translation") errors.push(exercise.id+": must be translation");
  if (exercise.quality?.state!=="candidate") errors.push(exercise.id+": must remain candidate");
  const sourceId=exercise.sourceSentenceIds?.[0];
  if (!sentenceIds.has(sourceId)) errors.push(exercise.id+": missing source sentence "+sourceId);
}
for (const key of ["engSentences","vieSentences","links"]) {
  const observed=sourceReport.observedContentSha256?.[key];
  if (!/^[a-f0-9]{64}$/.test(observed??"")) errors.push("invalid observed SHA-256 for "+key);
  const expected=pin.files?.[key]?.contentSha256;
  if (expected&&expected!==observed) errors.push("pinned SHA-256 mismatch for "+key);
}
console.log(JSON.stringify(sourceReport,null,2));
if (errors.length) { console.error(errors.join("\n")); process.exitCode=1; }
