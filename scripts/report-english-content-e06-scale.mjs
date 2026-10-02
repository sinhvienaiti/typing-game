import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  normalizeSentenceKey,
  readJson,
  tokenJaccard,
} from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const [sentencesDoc,exercisesDoc]=await Promise.all([
  readJson(path.join(root,"content","english","review-queues","typing-text-e06-sentences.json")),
  readJson(path.join(root,"content","english","review-queues","typing-text-e06-exercises.json"))
]);
const sentences=sentencesDoc.records??[];
const exercises=exercisesDoc.records??[];
const errors=[];
if (sentences.length!==1000) errors.push("E06 typing-text candidate set must contain exactly 1000 sentences");
if (exercises.length!==300) errors.push("E06 typing-text candidate set must contain exactly 300 cloze exercises");
const sentenceIds=new Set();
const sentenceKeys=new Set();
const sentenceById=new Map();
for (const sentence of sentences) {
  if (sentenceIds.has(sentence.id)) errors.push("duplicate sentence id: "+sentence.id);
  sentenceIds.add(sentence.id);
  const key=normalizeSentenceKey(sentence.text);
  if (sentenceKeys.has(key)) errors.push("duplicate normalized sentence: "+sentence.id);
  sentenceKeys.add(key);
  sentenceById.set(sentence.id,sentence);
  if (sentence.quality?.state!=="candidate") errors.push(sentence.id+": candidate corpus must remain candidate");
  if (!Array.isArray(sentence.lexicalIds)||sentence.lexicalIds.length===0) errors.push(sentence.id+": missing lexicalIds");
  for (const id of sentence.lexicalIds??[]) if (!String(id).startsWith("lex.en.")) errors.push(sentence.id+": non-stable lexical target "+id);
}
const exerciseIds=new Set();
for (const exercise of exercises) {
  if (exerciseIds.has(exercise.id)) errors.push("duplicate exercise id: "+exercise.id);
  exerciseIds.add(exercise.id);
  if (exercise.quality?.state!=="candidate") errors.push(exercise.id+": candidate exercise must remain candidate");
  if (exercise.type!=="cloze"||!exercise.prompt.includes("___")) errors.push(exercise.id+": invalid cloze prompt");
  const source=sentenceById.get(exercise.sourceSentenceIds?.[0]);
  if (!source) { errors.push(exercise.id+": missing source sentence"); continue; }
  const sourceKey=normalizeSentenceKey(source.text);
  if (!exercise.acceptedAnswers.some(answer=>sourceKey.includes(normalizeSentenceKey(answer)))) {
    errors.push(exercise.id+": accepted answer not found in source sentence");
  }
  for (const id of exercise.targetIds??[]) if (!String(id).startsWith("lex.en.")) errors.push(exercise.id+": non-stable target id "+id);
}
let nearPairs=0;
for (let i=0;i<sentences.length;i++) {
  for (let j=i+1;j<sentences.length;j++) {
    if (tokenJaccard(sentences[i].text,sentences[j].text)>=0.92) nearPairs++;
  }
}
const byCefr={};
for (const sentence of sentences) byCefr[sentence.cefr]=(byCefr[sentence.cefr]??0)+1;
console.log(JSON.stringify({
  sentences:sentences.length,
  clozeExercises:exercises.length,
  byCefr,
  nearDuplicatePairsAt092:nearPairs
},null,2));
if (nearPairs>50) errors.push("E06 candidate corpus has too many very-near duplicates at 0.92: "+nearPairs);
if (errors.length) { console.error(errors.join("\n")); process.exitCode=1; }
