import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createSchemaValidator, readJson, stableJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const schemaDir=path.join(root,"shared","schemas","english-content");
const schemaNames=(await fs.readdir(schemaDir)).filter(name=>name.endsWith(".schema.json")).sort();
const schemas=await Promise.all(schemaNames.map(name=>readJson(path.join(schemaDir,name))));
const schemaByName=new Map(schemaNames.map((name,index)=>[name,schemas[index]]));
const {validate}=createSchemaValidator(schemas);
const errors=[];
const expectedSchemas=["common.schema.json","provenance.schema.json","source-manifest.schema.json","runtime-manifest.schema.json","topic-catalog.schema.json","curriculum.schema.json","grammar-topic.schema.json","lexeme.schema.json","sense.schema.json","morphology.schema.json","usage.schema.json","collocation.schema.json","verb-pattern.schema.json","phrase.schema.json","sentence.schema.json","translation-pair.schema.json","dialogue.schema.json","exercise.schema.json","common-mistake.schema.json","lexeme-set.schema.json","grammar-topic-set.schema.json","sentence-set.schema.json","exercise-set.schema.json","oewn-review-queue.schema.json"];
for (const name of expectedSchemas) {
  const schema=schemaByName.get(name);
  if (!schema) errors.push("missing schema: "+name);
  else {
    if (schema.$schema!=="https://json-schema.org/draft/2020-12/schema") errors.push(name+": must use Draft 2020-12");
    if (typeof schema.$id!=="string"||!schema.$id.startsWith("https://typing-game.local/schemas/english-content/")) errors.push(name+": invalid $id");
  }
}
async function validateFile(relative,schemaName) {
  let data;
  try { data=await readJson(path.join(root,relative)); } catch (error) { errors.push(relative+": "+error.message); return null; }
  const schema=schemaByName.get(schemaName);
  if (schema) for (const problem of validate(data,schema)) errors.push(relative+" "+problem);
  return data;
}
const sources=await validateFile("content/english/sources/manifest.json","source-manifest.schema.json");
const authorCatalog=await validateFile("content/english/grammar/topic-catalog.json","topic-catalog.schema.json");
const sharedCatalog=await validateFile("shared/curriculum/topic-catalog.json","topic-catalog.schema.json");
const expectedCounts={A1:45,A2:50,B1:60,B2:60,C1:50,C2:35};
const allIds=new Set(),titleKeys=new Set(),objectiveKeys=new Set();
if (authorCatalog) {
  if (authorCatalog.topics.length!==300) errors.push("topic catalog must contain exactly 300 topics");
  for (const topic of authorCatalog.topics) {
    if (topic.id.split(".")[1]?.toUpperCase()!==topic.cefr) errors.push(topic.id+": id/CEFR mismatch");
    if (allIds.has(topic.id)) errors.push(topic.id+": duplicate id"); allIds.add(topic.id);
    const titleKey=topic.title.normalize("NFKC").trim().toLowerCase(); if (titleKeys.has(titleKey)) errors.push(topic.id+": duplicate normalized title"); titleKeys.add(titleKey);
    const objectiveKey=topic.objective.normalize("NFKC").trim().toLowerCase(); if (objectiveKeys.has(objectiveKey)) errors.push(topic.id+": duplicate normalized objective"); objectiveKeys.add(objectiveKey);
  }
}
if (authorCatalog&&sharedCatalog&&stableJson(authorCatalog)!==stableJson(sharedCatalog)) errors.push("shared curriculum topic catalog is stale");
let total=0;
for (const cefr of Object.keys(expectedCounts)) {
  const relative="shared/curriculum/"+cefr.toLowerCase()+".json";
  const doc=await validateFile(relative,"curriculum.schema.json");
  if (!doc) continue;
  if (doc.cefr!==cefr) errors.push(relative+": CEFR mismatch");
  if (doc.topicIds.length!==expectedCounts[cefr]) errors.push(relative+": expected "+expectedCounts[cefr]+" topics");
  total+=doc.topicIds.length;
  for (const id of doc.topicIds) {
    const topic=authorCatalog?.topics.find(item=>item.id===id);
    if (!topic) errors.push(relative+": unknown topic "+id);
    else if (topic.cefr!==cefr) errors.push(relative+": topic belongs to "+topic.cefr+": "+id);
  }
}
if (total!==300) errors.push("curriculum level files must reference exactly 300 topics");
for (const relative of ["shared/dictionary/manifest.json","shared/phrases/manifest.json","shared/grammar/manifest.json","shared/sentences/manifest.json","shared/curriculum/manifest.json","shared/attribution/english-content/manifest.json"]) await validateFile(relative,"runtime-manifest.schema.json");
const legacy=await readJson(path.join(root,"shared","vocabulary","schema.json"));
if (legacy?.properties?.version?.const!==1||legacy?.properties?.entries?.items?.additionalProperties!==false) errors.push("legacy vocabulary v1 ABI changed unexpectedly");
if (!sources?.sources?.some(source=>source.id==="verbnet"&&source.publishAllowed===false)) errors.push("VerbNet publication gate must remain closed");
if (!sources?.sources?.some(source=>source.id==="cambridge-profile"&&source.publishAllowed===false)) errors.push("Cambridge source must remain reference-only");

const lexemePilot=await validateFile("content/english/dictionary/lexeme-seed-pilot.json","lexeme-set.schema.json");
const grammarPilot=await validateFile("content/english/grammar/pilot-topics.json","grammar-topic-set.schema.json");
const sentencePilot=await validateFile("content/english/sentences/pilot-sentences.json","sentence-set.schema.json");
const exercisePilot=await validateFile("content/english/sentences/pilot-exercises.json","exercise-set.schema.json");
const vocabLookup=await readJson(path.join(root,"shared","vocabulary","lookup.json"));
if (lexemePilot) {
  if (lexemePilot.records.length!==300) errors.push("lexeme seed pilot must contain exactly 300 records");
  const lexIds=new Set(),keys=new Set();
  for (const record of lexemePilot.records) {
    if (record.quality?.state!=="candidate") errors.push(record.id+": lexeme seed must remain candidate until enrichment/review");
    if (lexIds.has(record.id)) errors.push(record.id+": duplicate lexeme id"); lexIds.add(record.id);
    if (keys.has(record.headwordKey)) errors.push(record.id+": duplicate headwordKey"); keys.add(record.headwordKey);
    if (!Number.isInteger(vocabLookup.entries?.[record.headwordKey])) errors.push(record.id+": headwordKey is missing from legacy vocabulary lookup");
  }
}
const pilotSentenceIds=new Set((sentencePilot?.records??[]).map(item=>item.id));
const pilotExerciseIds=new Set((exercisePilot?.records??[]).map(item=>item.id));
if (grammarPilot) {
  if (grammarPilot.records.length!==12) errors.push("grammar pilot must contain exactly 12 topics");
  for (const cefr of Object.keys(expectedCounts)) {
    const count=grammarPilot.records.filter(item=>item.cefr===cefr).length;
    if (count!==2) errors.push("grammar pilot "+cefr+": expected 2 topics, got "+count);
  }
  for (const topic of grammarPilot.records) {
    if (!allIds.has(topic.id)) errors.push(topic.id+": grammar pilot id is absent from the 300-topic catalog");
    if (topic.quality?.state==="published") errors.push(topic.id+": pilot must not bypass review into published state");
    for (const id of topic.exampleIds??[]) if (!pilotSentenceIds.has(id)) errors.push(topic.id+": missing pilot sentence "+id);
    for (const id of topic.exerciseIds??[]) if (!pilotExerciseIds.has(id)) errors.push(topic.id+": missing pilot exercise "+id);
    for (const id of [...(topic.prerequisiteIds??[]),...(topic.contrastTopicIds??[])]) if (!allIds.has(id)) errors.push(topic.id+": unknown grammar reference "+id);
  }
}
if (sentencePilot) {
  if (sentencePilot.records.length!==36) errors.push("sentence pilot must contain exactly 36 records");
  for (const sentence of sentencePilot.records) {
    if (sentence.quality?.state==="published") errors.push(sentence.id+": pilot sentence must remain non-published until review");
    for (const id of sentence.grammarIds??[]) if (!allIds.has(id)) errors.push(sentence.id+": unknown grammar target "+id);
  }
}
if (exercisePilot) {
  if (exercisePilot.records.length!==24) errors.push("exercise pilot must contain exactly 24 records");
  for (const exercise of exercisePilot.records) {
    if (exercise.quality?.state==="published") errors.push(exercise.id+": pilot exercise must remain non-published until review");
    for (const id of exercise.targetIds??[]) if (id.startsWith("gr.")&&!allIds.has(id)) errors.push(exercise.id+": unknown grammar target "+id);
    for (const id of exercise.sourceSentenceIds??[]) if (!pilotSentenceIds.has(id)) errors.push(exercise.id+": unknown source sentence "+id);
  }
}


const oewnQueuePath=path.join(root,"content","english","review-queues","oewn-pilot.json");
try {
  await fs.access(oewnQueuePath);
  const oewnQueue=await validateFile("content/english/review-queues/oewn-pilot.json","oewn-review-queue.schema.json");
  if (oewnQueue) {
    if (oewnQueue.source!=="oewn") errors.push("OEWN review queue source must be oewn");
    if (oewnQueue.snapshot.startsWith("live-api") && oewnQueue.records.some(record=>record.synsets.length===0)) {
      // Empty synset lists are allowed for lookup misses; keep them visible for review rather than inventing senses.
    }
    const queueLexemeIds=new Set();
    for (const record of oewnQueue.records) {
      if (queueLexemeIds.has(record.lexemeId)) errors.push(record.lexemeId+": duplicate OEWN review-queue lexeme");
      queueLexemeIds.add(record.lexemeId);
    }
  }
} catch (error) {
  if (error?.code!=="ENOENT") errors.push("OEWN review queue validation failed: "+error.message);
}

if (errors.length) { console.error(errors.join("\n")); process.exitCode=1; }
else console.log("English content PASS: "+expectedSchemas.length+" schemas, 300 curriculum topics, legacy vocabulary ABI preserved.");
