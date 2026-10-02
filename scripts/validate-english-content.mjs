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
const expectedSchemas=["common.schema.json","provenance.schema.json","source-manifest.schema.json","runtime-manifest.schema.json","topic-catalog.schema.json","curriculum.schema.json","grammar-topic.schema.json","lexeme.schema.json","sense.schema.json","morphology.schema.json","usage.schema.json","collocation.schema.json","verb-pattern.schema.json","phrase.schema.json","sentence.schema.json","translation-pair.schema.json","dialogue.schema.json","exercise.schema.json","common-mistake.schema.json"];
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
if (errors.length) { console.error(errors.join("\n")); process.exitCode=1; }
else console.log("English content PASS: "+expectedSchemas.length+" schemas, 300 curriculum topics, legacy vocabulary ABI preserved.");
