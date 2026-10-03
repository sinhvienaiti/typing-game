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
const expectedSchemas=["common.schema.json","provenance.schema.json","source-manifest.schema.json","runtime-manifest.schema.json","topic-catalog.schema.json","curriculum.schema.json","grammar-topic.schema.json","lexeme.schema.json","sense.schema.json","morphology.schema.json","usage.schema.json","collocation.schema.json","verb-pattern.schema.json","phrase.schema.json","sentence.schema.json","translation-pair.schema.json","dialogue.schema.json","exercise.schema.json","common-mistake.schema.json","lexeme-set.schema.json","grammar-topic-set.schema.json","sentence-set.schema.json","exercise-set.schema.json","oewn-review-queue.schema.json","collocation-set.schema.json","verb-pattern-set.schema.json","phrase-set.schema.json","oewn-pinned-pilot.schema.json","viwiktionary-review-queue.schema.json","tatoeba-source-pin.schema.json","tatoeba-source-report.schema.json","dialogue-set.schema.json","multiwoz-source-pin.schema.json","multiwoz-source-report.schema.json","e03-sense-review.schema.json","batch-manifest.schema.json","long-term-targets.schema.json","deprecation-map.schema.json","content-release.schema.json","common-mistake-set.schema.json","wiktextract-enrichment.schema.json","review-ledger.schema.json"];
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
const batchManifest=await validateFile("content/english/batches/manifest.json","batch-manifest.schema.json");
await validateFile("content/english/targets/long-term.json","long-term-targets.schema.json");
await validateFile("content/english/migrations/deprecations.json","deprecation-map.schema.json");
await validateFile("content/english/releases/2026.10.0.json","content-release.schema.json");
await validateFile("content/english/reviews/decisions.json","review-ledger.schema.json");
await validateFile("content/english/sources/tatoeba-eng-vie-pilot.json","tatoeba-source-pin.schema.json");
await validateFile("content/english/sources/multiwoz-e06-dialogue.json","multiwoz-source-pin.schema.json");
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
if (batchManifest?.contentVersion!=="2026.10.0") errors.push("controlled batch contentVersion must remain 2026.10.0 until an explicit release bump");
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



const collocationPilot=await validateFile("content/english/phrases/pilot-collocations.json","collocation-set.schema.json");
const verbPatternPilot=await validateFile("content/english/phrases/pilot-verb-patterns.json","verb-pattern-set.schema.json");
const phrasePilot=await validateFile("content/english/phrases/pilot-phrases.json","phrase-set.schema.json");
function requireUnique(records,key,label) {
  const seen=new Set();
  for (const record of records??[]) {
    const value=String(record?.[key]??"").normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (!value) { errors.push(label+": empty "+key+" on "+(record?.id??"unknown")); continue; }
    if (seen.has(value)) errors.push(label+": duplicate "+key+" "+value);
    seen.add(value);
  }
}
if (collocationPilot) {
  if (collocationPilot.records.length!==100) errors.push("E04 collocation pilot must contain exactly 100 records");
  requireUnique(collocationPilot.records,"id","collocations");
  requireUnique(collocationPilot.records,"text","collocations");
  for (const record of collocationPilot.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 collocation must remain draft before review");
    if (!(record.headwordKeys??[]).some(key=>Number.isInteger(vocabLookup.entries?.[key]))) errors.push(record.id+": no headwordKey resolves to legacy vocabulary");
  }
}
if (verbPatternPilot) {
  if (verbPatternPilot.records.length!==50) errors.push("E04 verb-pattern pilot must contain exactly 50 records");
  requireUnique(verbPatternPilot.records,"id","verb patterns");
  const combo=new Set();
  for (const record of verbPatternPilot.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 verb pattern must remain draft before review");
    if (!Number.isInteger(vocabLookup.entries?.[record.lemma])) errors.push(record.id+": lemma is missing from legacy vocabulary: "+record.lemma);
    const key=record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US");
    if (combo.has(key)) errors.push(record.id+": duplicate lemma/frame");
    combo.add(key);
  }
}
if (phrasePilot) {
  if (phrasePilot.records.length!==100) errors.push("E04 phrase pilot must contain exactly 100 records (50 phrasal verbs + 50 chunks/idioms)");
  requireUnique(phrasePilot.records,"id","phrases");
  requireUnique(phrasePilot.records,"key","phrases");
  const pvCount=phrasePilot.records.filter(record=>record.type==="phrasal-verb").length;
  const chunkIdiomCount=phrasePilot.records.filter(record=>record.type==="chunk"||record.type==="idiom").length;
  if (pvCount!==50) errors.push("E04 phrase pilot must contain exactly 50 phrasal verbs");
  if (chunkIdiomCount!==50) errors.push("E04 phrase pilot must contain exactly 50 chunks/idioms");
  for (const record of phrasePilot.records) if (record.quality?.state!=="draft") errors.push(record.id+": E04 phrase must remain draft before review");
}

const multiwozDialoguePath=path.join(root,"content","english","review-queues","multiwoz-e06-dialogues.json");
try {
  await fs.access(multiwozDialoguePath);
  const dialogues=await validateFile("content/english/review-queues/multiwoz-e06-dialogues.json","dialogue-set.schema.json");
  await validateFile("content/english/review-queues/multiwoz-e06-source-report.json","multiwoz-source-report.schema.json");
  if (dialogues?.records.length!==100) errors.push("E06 MultiWOZ pilot must contain exactly 100 dialogues");
  for (const record of dialogues?.records??[]) {
    if (record.quality?.state!=="candidate") errors.push(record.id+": E06 dialogue must remain candidate");
    if (record.turns.length<4||record.turns.length>10) errors.push(record.id+": E06 dialogue turn count outside 4..10");
  }
} catch (error) {
  if (error?.code!=="ENOENT") errors.push("E06 MultiWOZ validation failed: "+error.message);
}

const commonMistakePath=path.join(root,"content","english","review-queues","grammar-e06-common-mistakes.json");
try {
  await fs.access(commonMistakePath);
  const commonMistakes=await validateFile("content/english/review-queues/grammar-e06-common-mistakes.json","common-mistake-set.schema.json");
  if (commonMistakes?.records.length!==100) errors.push("E06 common mistakes must contain exactly 100 records");
  for (const record of commonMistakes?.records??[]) {
    if (record.quality?.state!=="candidate") errors.push(record.id+": E06 common mistake must remain candidate");
  }
} catch (error) {
  if (error?.code!=="ENOENT") errors.push("E06 common-mistake validation failed: "+error.message);
}

const grammarCorrectionPath=path.join(root,"content","english","review-queues","grammar-e06-corrections.json");
try {
  await fs.access(grammarCorrectionPath);
  const corrections=await validateFile("content/english/review-queues/grammar-e06-corrections.json","exercise-set.schema.json");
  const transformations=await validateFile("content/english/review-queues/grammar-e06-transformations.json","exercise-set.schema.json");
  if (corrections?.records.length!==100) errors.push("E06 grammar corrections must contain exactly 100 records");
  if (transformations?.records.length!==100) errors.push("E06 grammar transformations must contain exactly 100 records");
  for (const record of corrections?.records??[]) {
    if (record.type!=="error-correction") errors.push(record.id+": E06 correction type mismatch");
    if (record.quality?.state!=="candidate") errors.push(record.id+": E06 correction must remain candidate");
  }
  for (const record of transformations?.records??[]) {
    if (record.type!=="transformation") errors.push(record.id+": E06 transformation type mismatch");
    if (record.quality?.state!=="candidate") errors.push(record.id+": E06 transformation must remain candidate");
  }
} catch (error) {
  if (error?.code!=="ENOENT") errors.push("E06 grammar candidate validation failed: "+error.message);
}

const tatoebaSentencePath=path.join(root,"content","english","review-queues","tatoeba-e06-sentences.json");
try {
  await fs.access(tatoebaSentencePath);
  const tatoebaSentences=await validateFile("content/english/review-queues/tatoeba-e06-sentences.json","sentence-set.schema.json");
  const tatoebaExercises=await validateFile("content/english/review-queues/tatoeba-e06-translations.json","exercise-set.schema.json");
  await validateFile("content/english/review-queues/tatoeba-e06-source-report.json","tatoeba-source-report.schema.json");
  if (tatoebaSentences?.records.length!==300) errors.push("Tatoeba E06 must contain 300 English sentences");
  if (tatoebaExercises?.records.length!==300) errors.push("Tatoeba E06 must contain 300 translation exercises");
  for (const record of tatoebaSentences?.records??[]) {
    if (record.quality?.state!=="candidate") errors.push(record.id+": Tatoeba sentence must remain candidate");
  }
  for (const record of tatoebaExercises?.records??[]) {
    if (record.type!=="translation") errors.push(record.id+": Tatoeba exercise must be translation");
    if (record.quality?.state!=="candidate") errors.push(record.id+": Tatoeba translation must remain candidate");
  }
} catch (error) {
  if (error?.code!=="ENOENT") errors.push("Tatoeba E06 validation failed: "+error.message);
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


function normalizedText(value) {
  return String(value).normalize("NFC").trim().replace(/\s+/g," ").replace(/\s+([,.;:!?])/g,"$1").toLocaleLowerCase("en-US");
}
const sentenceById=new Map((sentencePilot?.records??[]).map(item=>[item.id,item]));
if (exercisePilot) {
  for (const exercise of exercisePilot.records) {
    if (exercise.type==="cloze") {
      if (!exercise.prompt.includes("___")) errors.push(exercise.id+": cloze prompt must contain ___");
      const source=sentenceById.get(exercise.sourceSentenceIds?.[0]);
      if (source&&!exercise.acceptedAnswers.some(answer=>normalizedText(source.text).includes(normalizedText(answer)))) {
        errors.push(exercise.id+": no accepted cloze answer occurs in its source sentence");
      }
    }
    if (exercise.type==="translation") {
      const sourceTexts=(exercise.sourceSentenceIds??[]).map(id=>sentenceById.get(id)?.text).filter(Boolean).map(normalizedText);
      if (sourceTexts.length>0&&!exercise.acceptedAnswers.some(answer=>sourceTexts.includes(normalizedText(answer)))) {
        errors.push(exercise.id+": translation accepted answer does not match any linked English source sentence");
      }
    }
  }
}




const typingTextSentencePath=path.join(root,"content","english","review-queues","typing-text-e06-sentences.json");
const typingTextExercisePath=path.join(root,"content","english","review-queues","typing-text-e06-exercises.json");
try {
  await fs.access(typingTextSentencePath);
  await fs.access(typingTextExercisePath);
  const derivedSentences=await validateFile("content/english/review-queues/typing-text-e06-sentences.json","sentence-set.schema.json");
  const derivedExercises=await validateFile("content/english/review-queues/typing-text-e06-exercises.json","exercise-set.schema.json");
  if (derivedSentences&&derivedExercises) {
    if (derivedSentences.records.length!==1000) errors.push("derived E06 corpus must contain exactly 1000 sentences");
    if (derivedExercises.records.length!==300) errors.push("derived E06 corpus must contain exactly 300 exercises");
    const derivedById=new Map(derivedSentences.records.map(item=>[item.id,item]));
    let stableTargetSentenceCount=0;
    for (const sentence of derivedSentences.records) {
      if (sentence.quality?.state!=="candidate") errors.push(sentence.id+": derived E06 sentence must remain candidate");
      if ((sentence.lexicalIds??[]).length>0) stableTargetSentenceCount++;
    }
    if (stableTargetSentenceCount<300) errors.push("derived E06 corpus must retain at least 300 stable-target sentences");
    for (const exercise of derivedExercises.records) {
      if (exercise.quality?.state!=="candidate") errors.push(exercise.id+": derived E06 exercise must remain candidate");
      if (exercise.type!=="cloze"||!exercise.prompt.includes("___")) errors.push(exercise.id+": derived E06 exercise must be cloze");
      const source=derivedById.get(exercise.sourceSentenceIds?.[0]);
      if (!source) errors.push(exercise.id+": derived E06 source sentence is missing");
      else if (!exercise.acceptedAnswers.some(answer=>normalizedText(source.text).includes(normalizedText(answer)))) {
        errors.push(exercise.id+": derived E06 accepted answer is absent from source sentence");
      }
    }
  }
} catch (error) {
  if (error?.code!=="ENOENT") errors.push("derived E06 validation failed: "+error.message);
}


const e03SenseReviewPath=path.join(root,"content","english","review-queues","e03-sense-alignment-review.json");
try {
  await fs.access(e03SenseReviewPath);
  const packet=await validateFile("content/english/review-queues/e03-sense-alignment-review.json","e03-sense-review.schema.json");
  if (packet?.records.length!==300) errors.push("E03 sense review packet must contain exactly 300 records");
  if ((packet?.metrics?.bothSources??0)<290) errors.push("E03 bilingual source coverage below 290/300");
  for (const record of packet?.records??[]) {
    if (record.quality?.state!=="candidate") errors.push(record.lexemeId+": E03 sense review must remain candidate");
    if (record.quality?.checks?.senseAlignment?.status!=="pending") errors.push(record.lexemeId+": E03 sense alignment must remain pending");
  }
} catch (error) {
  if (error?.code!=="ENOENT") errors.push("E03 sense review validation failed: "+error.message);
}

const simpleWiktionaryPath=path.join(root,"content","english","review-queues","simplewiktionary-en-pilot.json");
try {
  await fs.access(simpleWiktionaryPath);
  const simpleQueue=await validateFile("content/english/review-queues/simplewiktionary-en-pilot.json","wiktextract-enrichment.schema.json");
  if (simpleQueue?.records.length!==300) errors.push("Simple Wiktionary pilot must contain exactly 300 seed records");
  for (const record of simpleQueue?.records??[]) {
    if (record.quality?.state!=="candidate") errors.push(record.lexemeId+": Simple Wiktionary enrichment must remain candidate");
  }
} catch (error) {
  if (error?.code!=="ENOENT") errors.push("Simple Wiktionary enrichment validation failed: "+error.message);
}

const viWiktionaryQueuePath=path.join(root,"content","english","review-queues","viwiktionary-en-pilot.json");
try {
  await fs.access(viWiktionaryQueuePath);
  const viQueue=await validateFile("content/english/review-queues/viwiktionary-en-pilot.json","viwiktionary-review-queue.schema.json");
  if (viQueue) {
    if (viQueue.records.length+viQueue.misses.length!==300) errors.push("Vietnamese Wiktionary queue must account for 300 lexical seeds");
    const source=sources?.sources?.find(item=>item.id==="viwiktionary-en");
    if (source?.checksumSha256&&source.checksumSha256!==viQueue.sourceSha256) errors.push("Vietnamese Wiktionary queue checksum does not match source manifest");
    for (const record of viQueue.records) {
      if (record.quality?.state!=="candidate") errors.push(record.lexemeId+": Vietnamese Wiktionary import must remain candidate");
      if (!Number.isInteger(vocabLookup.entries?.[record.headwordKey])) errors.push(record.lexemeId+": Vietnamese Wiktionary headword missing from legacy lookup");
    }
  }
} catch (error) {
  if (error?.code!=="ENOENT") errors.push("Vietnamese Wiktionary queue validation failed: "+error.message);
}

const oewnPinnedPilotPath=path.join(root,"content","english","review-queues","oewn-2025-pilot.json");
try {
  await fs.access(oewnPinnedPilotPath);
  const pinned=await validateFile("content/english/review-queues/oewn-2025-pilot.json","oewn-pinned-pilot.schema.json");
  if (pinned) {
    if (pinned.records.length+pinned.misses.length!==300) errors.push("pinned OEWN pilot must account for 300 seeds");
    const seen=new Set();
    for (const record of pinned.records) {
      if (seen.has(record.lexemeId)) errors.push(record.lexemeId+": duplicate pinned OEWN lexeme");
      seen.add(record.lexemeId);
      if (!Number.isInteger(vocabLookup.entries?.[record.headwordKey])) errors.push(record.lexemeId+": pinned OEWN headword missing from legacy lookup");
      if (record.quality?.state!=="candidate") errors.push(record.lexemeId+": pinned OEWN data must remain candidate");
    }
  }
} catch (error) {
  if (error?.code!=="ENOENT") errors.push("pinned OEWN pilot validation failed: "+error.message);
}

if (errors.length) { console.error(errors.join("\n")); process.exitCode=1; }
else console.log("English content PASS: "+expectedSchemas.length+" schemas, 300 curriculum topics, legacy vocabulary ABI preserved.");
