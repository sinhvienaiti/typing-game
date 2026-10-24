import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createSchemaValidator, readJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const schemaDir=path.join(root,"shared","schemas","english-content");
const schemaNames=(await fs.readdir(schemaDir)).filter(name=>name.endsWith(".schema.json")).sort();
const schemas=await Promise.all(schemaNames.map(name=>readJson(path.join(schemaDir,name))));
const schemaByName=new Map(schemaNames.map((name,index)=>[name,schemas[index]]));
const {validate}=createSchemaValidator(schemas);
const errors=[];

const [batchManifest,catalog,pilot]=await Promise.all([
  readJson(path.join(root,"content","english","batches","manifest.json")),
  readJson(path.join(root,"content","english","grammar","topic-catalog.json")),
  readJson(path.join(root,"content","english","grammar","pilot-topics.json")),
]);
const catalogById=new Map((catalog.topics??[]).map(topic=>[topic.id,topic]));
const pilotTopicIds=new Set((pilot.records??[]).map(topic=>topic.id));
const seenScaleTopicIds=new Set();

const schemaBySetId={
  "grammar-topics":"grammar-topic-set.schema.json",
  examples:"sentence-set.schema.json",
  exercises:"exercise-set.schema.json",
  "common-mistakes":"common-mistake-set.schema.json",
};
function normalized(value) {
  return String(value??"").normalize("NFKC").trim().replace(/\s+/gu," ").toLocaleLowerCase("en-US");
}
async function loadSet(batch,setId) {
  const set=(batch.recordSets??[]).find(item=>item.id===setId);
  if (!set) {
    errors.push(batch.id+": missing record set "+setId);
    return {set:null,records:[]};
  }
  let doc;
  try { doc=await readJson(path.join(root,set.path)); }
  catch (error) {
    errors.push(batch.id+"/"+setId+": "+error.message);
    return {set,records:[]};
  }
  const schema=schemaByName.get(schemaBySetId[setId]);
  if (!schema) errors.push(batch.id+"/"+setId+": missing validator schema");
  else for (const problem of validate(doc,schema)) errors.push(set.path+" "+problem);
  const records=Array.isArray(doc.records)?doc.records:[];
  if (records.length!==set.expectedCount) errors.push(batch.id+"/"+setId+": expected "+set.expectedCount+" records, got "+records.length);
  for (const record of records) if (record?.quality?.state!=="draft") errors.push(String(record?.id??"<unknown>")+": grammar-scale source must remain draft");
  return {set,records};
}

const scaleBatches=(batchManifest.batches??[])
  .filter(batch=>/^e05\.grammar-scale-[a-z][0-9]-[0-9]{2}$/u.test(batch.id))
  .sort((a,b)=>a.id.localeCompare(b.id,"en"));

for (const batch of scaleBatches) {
  if (!Array.isArray(batch.cefr)||batch.cefr.length!==1) {
    errors.push(batch.id+": grammar-scale batch must declare exactly one CEFR level");
    continue;
  }
  const cefr=batch.cefr[0];
  const topicSet=await loadSet(batch,"grammar-topics");
  const exampleSet=await loadSet(batch,"examples");
  const exerciseSet=await loadSet(batch,"exercises");
  const mistakeSet=await loadSet(batch,"common-mistakes");
  const topics=topicSet.records, examples=exampleSet.records, exercises=exerciseSet.records, mistakes=mistakeSet.records;
  const n=topics.length;
  if (exampleSet.set&&exampleSet.set.expectedCount!==n*3) errors.push(batch.id+": examples expectedCount must equal topics*3");
  if (exerciseSet.set&&exerciseSet.set.expectedCount!==n*2) errors.push(batch.id+": exercises expectedCount must equal topics*2");
  if (mistakeSet.set&&mistakeSet.set.expectedCount!==n) errors.push(batch.id+": common-mistakes expectedCount must equal topics");

  const topicIds=new Set(topics.map(record=>record.id));
  const exampleIds=new Set(examples.map(record=>record.id));
  const exerciseIds=new Set(exercises.map(record=>record.id));
  const mistakeIds=new Set(mistakes.map(record=>record.id));
  const exampleCounts=new Map(),exerciseCounts=new Map(),mistakeCounts=new Map();
  const localSentenceKeys=new Set();

  for (const topic of topics) {
    const catalogTopic=catalogById.get(topic.id);
    if (!catalogTopic) errors.push(topic.id+": grammar-scale topic is not in the 300-topic catalog");
    else if (catalogTopic.cefr!==cefr||topic.cefr!==cefr) errors.push(topic.id+": grammar-scale CEFR mismatch");
    if (pilotTopicIds.has(topic.id)) errors.push(topic.id+": grammar-scale topic duplicates original pilot topic");
    if (seenScaleTopicIds.has(topic.id)) errors.push(topic.id+": grammar-scale topic appears in multiple batches");
    seenScaleTopicIds.add(topic.id);
    if (!String(topic.concept?.en??"").trim()||!String(topic.concept?.vi??"").trim()) errors.push(topic.id+": bilingual concept is required");
    if (!Array.isArray(topic.formulae)||topic.formulae.length===0) errors.push(topic.id+": formulae are required");
    if (!Array.isArray(topic.whenToUse)||topic.whenToUse.length===0) errors.push(topic.id+": whenToUse is required");
    if ((topic.exampleIds??[]).length!==3) errors.push(topic.id+": grammar-scale topic requires 3 examples");
    if ((topic.exerciseIds??[]).length!==2) errors.push(topic.id+": grammar-scale topic requires 2 exercises");
    if ((topic.commonMistakeIds??[]).length!==1) errors.push(topic.id+": grammar-scale topic requires 1 common mistake");
    for (const id of topic.exampleIds??[]) if (!exampleIds.has(id)) errors.push(topic.id+": missing linked example "+id);
    for (const id of topic.exerciseIds??[]) if (!exerciseIds.has(id)) errors.push(topic.id+": missing linked exercise "+id);
    for (const id of topic.commonMistakeIds??[]) if (!mistakeIds.has(id)) errors.push(topic.id+": missing linked common mistake "+id);
    for (const id of [...(topic.prerequisiteIds??[]),...(topic.contrastTopicIds??[])]) if (!catalogById.has(id)) errors.push(topic.id+": unknown grammar reference "+id);
  }

  for (const sentence of examples) {
    if (sentence.cefr!==cefr||(sentence.grammarIds??[]).length!==1||!topicIds.has(sentence.grammarIds[0])) errors.push(sentence.id+": invalid grammar-scale example link");
    const key=normalized(sentence.text);
    if (!key) errors.push(sentence.id+": empty example text");
    if (localSentenceKeys.has(key)) errors.push(sentence.id+": exact duplicate example inside "+batch.id);
    localSentenceKeys.add(key);
    const topicId=sentence.grammarIds?.[0];
    if (topicId) exampleCounts.set(topicId,(exampleCounts.get(topicId)??0)+1);
  }

  let cloze=0,translation=0;
  const exampleById=new Map(examples.map(record=>[record.id,record]));
  for (const exercise of exercises) {
    const topicId=exercise.targetIds?.[0];
    const sourceId=exercise.sourceSentenceIds?.[0];
    const source=exampleById.get(sourceId);
    if (exercise.cefr!==cefr||(exercise.targetIds??[]).length!==1||!topicIds.has(topicId)) errors.push(exercise.id+": invalid grammar-scale exercise target");
    if ((exercise.sourceSentenceIds??[]).length!==1||!source) errors.push(exercise.id+": invalid grammar-scale source sentence");
    if (!Array.isArray(exercise.acceptedAnswers)||exercise.acceptedAnswers.length===0) errors.push(exercise.id+": acceptedAnswers are required");
    if (exercise.type==="cloze") {
      cloze++;
      if (!String(exercise.prompt??"").includes("___")) errors.push(exercise.id+": cloze prompt must contain ___");
    } else if (exercise.type==="translation") {
      translation++;
      if (source&&normalized(exercise.acceptedAnswers?.[0])!==normalized(source.text)) errors.push(exercise.id+": translation answer must match its source sentence");
    } else errors.push(exercise.id+": grammar-scale exercise must be cloze or translation");
    if (topicId) exerciseCounts.set(topicId,(exerciseCounts.get(topicId)??0)+1);
  }
  if (cloze!==n||translation!==n) errors.push(batch.id+": exercise mix must be "+n+" cloze + "+n+" translation");

  for (const mistake of mistakes) {
    const topicId=mistake.targetIds?.[0];
    if ((mistake.targetIds??[]).length!==1||!topicIds.has(topicId)) errors.push(mistake.id+": invalid grammar-scale mistake target");
    if (mistake.evidenceType!=="pedagogical") errors.push(mistake.id+": grammar-scale mistake must be pedagogical");
    if (!Array.isArray(mistake.corrections)||mistake.corrections.length!==1) errors.push(mistake.id+": grammar-scale mistake requires exactly one correction");
    if (!String(mistake.explanationVi??"").trim()) errors.push(mistake.id+": Vietnamese explanation is required");
    if (topicId) mistakeCounts.set(topicId,(mistakeCounts.get(topicId)??0)+1);
  }

  for (const id of topicIds) {
    if ((exampleCounts.get(id)??0)!==3) errors.push(id+": grammar-scale topic must own 3 examples");
    if ((exerciseCounts.get(id)??0)!==2) errors.push(id+": grammar-scale topic must own 2 exercises");
    if ((mistakeCounts.get(id)??0)!==1) errors.push(id+": grammar-scale topic must own 1 common mistake");
  }
}

if (errors.length) {
  console.error(errors.join("\n"));
  process.exitCode=1;
} else {
  console.log(JSON.stringify({schemaVersion:1,grammarScaleBatches:scaleBatches.length,grammarScaleTopics:seenScaleTopicIds.size,status:"ok"},null,2));
}
