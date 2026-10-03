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
const expectedSchemas=["common.schema.json","provenance.schema.json","source-manifest.schema.json","runtime-manifest.schema.json","topic-catalog.schema.json","curriculum.schema.json","grammar-topic.schema.json","lexeme.schema.json","sense.schema.json","sense-set.schema.json","morphology.schema.json","usage.schema.json","collocation.schema.json","verb-pattern.schema.json","phrase.schema.json","sentence.schema.json","translation-pair.schema.json","dialogue.schema.json","exercise.schema.json","common-mistake.schema.json","lexeme-set.schema.json","grammar-topic-set.schema.json","sentence-set.schema.json","exercise-set.schema.json","oewn-review-queue.schema.json","collocation-set.schema.json","verb-pattern-set.schema.json","phrase-set.schema.json","oewn-pinned-pilot.schema.json","viwiktionary-review-queue.schema.json","tatoeba-source-pin.schema.json","tatoeba-source-report.schema.json","dialogue-set.schema.json","multiwoz-source-pin.schema.json","multiwoz-source-report.schema.json","e03-sense-review.schema.json","batch-manifest.schema.json","long-term-targets.schema.json","deprecation-map.schema.json","content-release.schema.json","common-mistake-set.schema.json","wiktextract-enrichment.schema.json","review-ledger.schema.json"];
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
function batchExpectedCount(batchId,recordSetId) {
  const batch=batchManifest?.batches?.find(item=>item.id===batchId);
  const recordSet=batch?.recordSets?.find(item=>item.id===recordSetId);
  return Number.isInteger(recordSet?.expectedCount)?recordSet.expectedCount:null;
}

await validateFile("content/english/targets/long-term.json","long-term-targets.schema.json");
await validateFile("content/english/migrations/deprecations.json","deprecation-map.schema.json");
await validateFile("content/english/releases/2026.10.0.json","content-release.schema.json");
await validateFile("content/english/reviews/decisions.json","review-ledger.schema.json");
const reviewShardDir=path.join(root,"content","english","reviews","decisions.d");
try {
  const reviewShardNames=(await fs.readdir(reviewShardDir))
    .filter(name=>name.endsWith(".json"))
    .sort((a,b)=>a.localeCompare(b,"en"));
  for (const name of reviewShardNames) {
    await validateFile("content/english/reviews/decisions.d/"+name,"review-ledger.schema.json");
  }
} catch (error) {
  if (error?.code!=="ENOENT") errors.push("review ledger shard validation failed: "+error.message);
}
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
const reviewedLexemes=await validateFile("content/english/dictionary/e03-reviewed-lexemes.json","lexeme-set.schema.json");
const reviewedSenses=await validateFile("content/english/dictionary/e03-reviewed-senses.json","sense-set.schema.json");
const grammarPilot=await validateFile("content/english/grammar/pilot-topics.json","grammar-topic-set.schema.json");
const sentencePilot=await validateFile("content/english/sentences/pilot-sentences.json","sentence-set.schema.json");
const exercisePilot=await validateFile("content/english/sentences/pilot-exercises.json","exercise-set.schema.json");
const reviewedE06Exercises=await validateFile("content/english/sentences/e06-reviewed-exercises.json","exercise-set.schema.json");
const reviewedTranslationSentences=await validateFile("content/english/sentences/e06-reviewed-translation-sentences.json","sentence-set.schema.json");
const reviewedTranslations=await validateFile("content/english/sentences/e06-reviewed-translations.json","exercise-set.schema.json");
const reviewedTypingTextSentences=await validateFile("content/english/sentences/e06-reviewed-typing-text-sentences.json","sentence-set.schema.json");
const reviewedCloze=await validateFile("content/english/sentences/e06-reviewed-cloze.json","exercise-set.schema.json");
const reviewedDialogues=await validateFile("content/english/sentences/e06-reviewed-dialogues.json","dialogue-set.schema.json");
const reviewedCommonMistakes=await validateFile("content/english/sentences/e06-reviewed-common-mistakes.json","common-mistake-set.schema.json");
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
if (reviewedLexemes&&reviewedSenses) {
  const expectedReviewedLexemes=batchExpectedCount("e03.lexical-reviewed-slice","reviewed-lexemes");
  const expectedReviewedSenses=batchExpectedCount("e03.lexical-reviewed-slice","reviewed-senses");
  if (expectedReviewedLexemes===null||reviewedLexemes.records.length!==expectedReviewedLexemes) errors.push("E03 reviewed lexeme slice must match the controlled batch expectedCount");
  if (expectedReviewedSenses===null||reviewedSenses.records.length!==expectedReviewedSenses) errors.push("E03 reviewed sense slice must match the controlled batch expectedCount");
  if (expectedReviewedLexemes!==expectedReviewedSenses) errors.push("E03 reviewed lexeme/sense controlled counts must stay paired");
  const senseIds=new Set(reviewedSenses.records.map(item=>item.id));
  const reviewedKeys=new Set();
  for (const record of reviewedLexemes.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E03 reviewed-source lexeme must remain draft; publication is ledger-overlay only");
    if (!record.vi||!record.ipa||!record.cefr) errors.push(record.id+": reviewed lexeme requires vi/ipa/cefr display metadata");
    if (reviewedKeys.has(record.headwordKey)) errors.push(record.id+": duplicate reviewed headwordKey");
    reviewedKeys.add(record.headwordKey);
    for (const id of record.senseIds??[]) if (!senseIds.has(id)) errors.push(record.id+": missing reviewed sense "+id);
  }
  const reviewedLexIds=new Set(reviewedLexemes.records.map(item=>item.id));
  for (const sense of reviewedSenses.records) {
    if (sense.quality?.state!=="draft") errors.push(sense.id+": E03 reviewed-source sense must remain draft; publication is ledger-overlay only");
    if (!reviewedLexIds.has(sense.lexemeId)) errors.push(sense.id+": unknown reviewed lexeme "+sense.lexemeId);
    if (!sense.cefr) errors.push(sense.id+": reviewed sense requires CEFR");
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
if (reviewedTranslationSentences&&reviewedTranslations) {
  const expectedTranslationSentences=batchExpectedCount("e06.translation-reviewed-slice","reviewed-translation-sentences");
  const expectedTranslations=batchExpectedCount("e06.translation-reviewed-slice","reviewed-translations");
  if (expectedTranslationSentences===null||expectedTranslations===null||
      reviewedTranslationSentences.records.length!==expectedTranslationSentences||
      reviewedTranslations.records.length!==expectedTranslations) {
    errors.push("E06 reviewed translation slice must match the controlled batch expectedCount");
  }
  if (expectedTranslationSentences!==expectedTranslations) errors.push("E06 reviewed translation sentence/exercise counts must stay paired");
  const sentenceIds=new Set(reviewedTranslationSentences.records.map(item=>item.id));
  for (const sentence of reviewedTranslationSentences.records) {
    if (sentence.quality?.state!=="draft") errors.push(sentence.id+": reviewed translation sentence must remain draft; publication is ledger-overlay only");
    if (!sentence.cefr) errors.push(sentence.id+": reviewed translation sentence requires CEFR");
  }
  for (const exercise of reviewedTranslations.records) {
    if (exercise.quality?.state!=="draft") errors.push(exercise.id+": reviewed translation exercise must remain draft; publication is ledger-overlay only");
    if (exercise.type!=="translation") errors.push(exercise.id+": reviewed translation exercise type mismatch");
    if (!exercise.cefr) errors.push(exercise.id+": reviewed translation exercise requires CEFR");
    const sourceId=exercise.sourceSentenceIds?.[0];
    if (!sentenceIds.has(sourceId)) errors.push(exercise.id+": reviewed translation source is missing "+sourceId);
    if (exercise.targetIds?.[0]!==sourceId) errors.push(exercise.id+": translation target must be its source sentence id");
  }
}
if (reviewedTypingTextSentences&&reviewedCloze) {
  const expectedTypingSentences=batchExpectedCount("e06.typing-text-reviewed-slice","reviewed-typing-text-sentences");
  const expectedTypingCloze=batchExpectedCount("e06.typing-text-reviewed-slice","reviewed-cloze");
  if (expectedTypingSentences===null||reviewedTypingTextSentences.records.length!==expectedTypingSentences) errors.push("E06 reviewed typing-text sentence slice must match controlled batch expectedCount");
  if (expectedTypingCloze===null||reviewedCloze.records.length!==expectedTypingCloze) errors.push("E06 reviewed cloze slice must match controlled batch expectedCount");
  if (expectedTypingSentences!==expectedTypingCloze) errors.push("E06 reviewed typing-text sentence/cloze counts must stay paired");
  const typingSentenceIds=new Set(reviewedTypingTextSentences.records.map(item=>item.id));
  const seedLexemeIds=new Set((lexemePilot?.records??[]).map(item=>item.id));
  for (const sentence of reviewedTypingTextSentences.records) {
    if (sentence.quality?.state!=="draft") errors.push(sentence.id+": reviewed typing-text sentence must remain draft; publication is ledger-overlay only");
    if (sentence.cefr!=="A1") errors.push(sentence.id+": first reviewed typing-text slice is intentionally A1-only");
    if (!(sentence.provenance?.sources??[]).some(source=>source.dataset==="project-original")) errors.push(sentence.id+": reviewed typing-text sentence must retain project-original provenance");
  }
  for (const exercise of reviewedCloze.records) {
    if (exercise.quality?.state!=="draft") errors.push(exercise.id+": reviewed cloze must remain draft; publication is ledger-overlay only");
    if (exercise.type!=="cloze") errors.push(exercise.id+": reviewed typing-text exercise must be cloze");
    const sourceId=exercise.sourceSentenceIds?.[0];
    if (!typingSentenceIds.has(sourceId)) errors.push(exercise.id+": reviewed cloze source sentence is missing "+sourceId);
    const targetId=exercise.targetIds?.[0];
    if (!seedLexemeIds.has(targetId)) errors.push(exercise.id+": reviewed cloze target is not a stable E03 seed lexeme "+String(targetId));
    if (!String(exercise.prompt??"").includes("___")) errors.push(exercise.id+": reviewed cloze prompt must contain the blank marker");
  }
}
if (reviewedDialogues) {
  const expectedReviewedDialogues=batchExpectedCount("e06.dialogue-reviewed-slice","reviewed-dialogues");
  if (expectedReviewedDialogues===null||reviewedDialogues.records.length!==expectedReviewedDialogues) errors.push("E06 reviewed dialogue slice must match the controlled batch expectedCount");
  const ids=new Set(),normalized=new Set();
  for (const dialogue of reviewedDialogues.records) {
    if (dialogue.quality?.state!=="draft") errors.push(dialogue.id+": reviewed dialogue must remain draft; publication is ledger-overlay only");
    if (ids.has(dialogue.id)) errors.push(dialogue.id+": duplicate reviewed dialogue id");
    ids.add(dialogue.id);
    if (dialogue.turns.length<4||dialogue.turns.length>10) errors.push(dialogue.id+": reviewed dialogue turn count outside 4..10");
    let previous="";
    for (const turn of dialogue.turns) {
      if (turn.speaker===previous) errors.push(dialogue.id+": reviewed dialogue speakers must alternate");
      previous=turn.speaker;
    }
    const key=dialogue.turns.map(turn=>String(turn.text).normalize("NFKC").trim().replace(/\s+/gu," ").toLocaleLowerCase("en-US")).join("\u0000");
    if (normalized.has(key)) errors.push(dialogue.id+": duplicate normalized reviewed dialogue");
    normalized.add(key);
    if (!(dialogue.provenance?.sources??[]).some(source=>source.dataset==="multiwoz"&&source.snapshot==="fe0c8e65cfcd8462bd33c86e35f21addc84ca82b"&&source.license==="MIT")) {
      errors.push(dialogue.id+": reviewed dialogue must retain pinned MultiWOZ MIT provenance");
    }
  }
}
if (reviewedE06Exercises) {
  const expectedReviewedExercises=batchExpectedCount("e06.grammar-reviewed-slice","reviewed-exercises");
  if (expectedReviewedExercises===null||reviewedE06Exercises.records.length!==expectedReviewedExercises) errors.push("E06 reviewed exercise slice must match the controlled batch expectedCount");
  const ids=new Set();
  const topicCounts=new Map();
  let corrections=0,transformations=0;
  for (const exercise of reviewedE06Exercises.records) {
    if (exercise.quality?.state!=="draft") errors.push(exercise.id+": E06 reviewed source must remain draft; publication is ledger-overlay only");
    if (ids.has(exercise.id)) errors.push(exercise.id+": duplicate E06 reviewed exercise id");
    ids.add(exercise.id);
    if (exercise.type==="error-correction") corrections++;
    else if (exercise.type==="transformation") transformations++;
    else errors.push(exercise.id+": E06 reviewed slice supports correction/transformation only");
    const grammarId=(exercise.targetIds??[]).find(id=>id.startsWith("gr."));
    if (!grammarId||!allIds.has(grammarId)) errors.push(exercise.id+": invalid grammar target");
    else topicCounts.set(grammarId,(topicCounts.get(grammarId)??0)+1);
    for (const id of exercise.sourceSentenceIds??[]) if (!pilotSentenceIds.has(id)) errors.push(exercise.id+": source must be a published pilot sentence "+id);
  }
  const expectedPerType=expectedReviewedExercises===null?null:expectedReviewedExercises/2;
  if (!Number.isInteger(expectedPerType)||corrections!==expectedPerType||transformations!==expectedPerType) {
    errors.push("E06 reviewed slice must remain evenly split between corrections and transformations");
  }
  const topicTotal=grammarPilot?.records?.length??0;
  const expectedPerTopic=expectedReviewedExercises===null||topicTotal===0?null:expectedReviewedExercises/topicTotal;
  if (!Number.isInteger(expectedPerTopic)) errors.push("E06 reviewed slice controlled count must divide evenly across published grammar topics");
  else for (const topic of grammarPilot?.records??[]) if ((topicCounts.get(topic.id)??0)!==expectedPerTopic) errors.push("E06 reviewed slice must contain "+expectedPerTopic+" exercises for "+topic.id);
}
if (reviewedCommonMistakes) {
  const expected=batchExpectedCount("e06.common-mistake-reviewed-slice","reviewed-common-mistakes");
  if (expected===null||reviewedCommonMistakes.records.length!==expected) errors.push("E06 reviewed common-mistake slice count mismatch");
  const topicCounts=new Map(),ids=new Set(),forms=new Set();
  for (const record of reviewedCommonMistakes.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": reviewed common mistake must remain draft");
    if (ids.has(record.id)) errors.push(record.id+": duplicate reviewed common-mistake id");
    ids.add(record.id);
    const form=String(record.incorrect??"").normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (forms.has(form)) errors.push(record.id+": duplicate reviewed common-mistake form");
    forms.add(form);
    if (record.corrections?.length!==1) errors.push(record.id+": one canonical correction is required");
    if (record.evidenceType!=="pedagogical") errors.push(record.id+": pedagogical evidenceType is required");
    if (!String(record.explanationVi??"").trim()) errors.push(record.id+": Vietnamese explanation is required");
    const grammarId=record.targetIds?.[0];
    if (!grammarId||!allIds.has(grammarId)) errors.push(record.id+": invalid grammar target");
    else topicCounts.set(grammarId,(topicCounts.get(grammarId)??0)+1);
  }
  if (expected!==null&&grammarPilot?.records?.length) {
    for (const topic of grammarPilot.records) {
      const count=topicCounts.get(topic.id)??0;
      if (count<6) errors.push("E06 reviewed common-mistake coverage must keep at least 6 records for "+topic.id);
    }
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
const scaleCollocations=await validateFile("content/english/phrases/e04-scale-01-collocations.json","collocation-set.schema.json");
const scaleVerbPatterns=await validateFile("content/english/phrases/e04-scale-01-verb-patterns.json","verb-pattern-set.schema.json");
const scalePhrases=await validateFile("content/english/phrases/e04-scale-01-phrases.json","phrase-set.schema.json");
const scale02Collocations=await validateFile("content/english/phrases/e04-scale-02-collocations.json","collocation-set.schema.json");
const scale02VerbPatterns=await validateFile("content/english/phrases/e04-scale-02-verb-patterns.json","verb-pattern-set.schema.json");
const scale02Phrases=await validateFile("content/english/phrases/e04-scale-02-phrases.json","phrase-set.schema.json");
const scale03Collocations=await validateFile("content/english/phrases/e04-scale-03-collocations.json","collocation-set.schema.json");
const scale03VerbPatterns=await validateFile("content/english/phrases/e04-scale-03-verb-patterns.json","verb-pattern-set.schema.json");
const scale03Phrases=await validateFile("content/english/phrases/e04-scale-03-phrases.json","phrase-set.schema.json");
const scale04Collocations=await validateFile("content/english/phrases/e04-scale-04-collocations.json","collocation-set.schema.json");
const scale04VerbPatterns=await validateFile("content/english/phrases/e04-scale-04-verb-patterns.json","verb-pattern-set.schema.json");
const scale04Phrases=await validateFile("content/english/phrases/e04-scale-04-phrases.json","phrase-set.schema.json");
const scale05Collocations=await validateFile("content/english/phrases/e04-scale-05-collocations.json","collocation-set.schema.json");
const scale05VerbPatterns=await validateFile("content/english/phrases/e04-scale-05-verb-patterns.json","verb-pattern-set.schema.json");
const scale05Phrases=await validateFile("content/english/phrases/e04-scale-05-phrases.json","phrase-set.schema.json");
const scale06Collocations=await validateFile("content/english/phrases/e04-scale-06-collocations.json","collocation-set.schema.json");
const scale06VerbPatterns=await validateFile("content/english/phrases/e04-scale-06-verb-patterns.json","verb-pattern-set.schema.json");
const scale06Phrases=await validateFile("content/english/phrases/e04-scale-06-phrases.json","phrase-set.schema.json");
const scale07Collocations=await validateFile("content/english/phrases/e04-scale-07-collocations.json","collocation-set.schema.json");
const scale07VerbPatterns=await validateFile("content/english/phrases/e04-scale-07-verb-patterns.json","verb-pattern-set.schema.json");
const scale07Phrases=await validateFile("content/english/phrases/e04-scale-07-phrases.json","phrase-set.schema.json");
const scale08Collocations=await validateFile("content/english/phrases/e04-scale-08-collocations.json","collocation-set.schema.json");
const scale08VerbPatterns=await validateFile("content/english/phrases/e04-scale-08-verb-patterns.json","verb-pattern-set.schema.json");
const scale08Phrases=await validateFile("content/english/phrases/e04-scale-08-phrases.json","phrase-set.schema.json");
const scale09Collocations=await validateFile("content/english/phrases/e04-scale-09-collocations.json","collocation-set.schema.json");
const scale09VerbPatterns=await validateFile("content/english/phrases/e04-scale-09-verb-patterns.json","verb-pattern-set.schema.json");
const scale09Phrases=await validateFile("content/english/phrases/e04-scale-09-phrases.json","phrase-set.schema.json");
const scale10Collocations=await validateFile("content/english/phrases/e04-scale-10-collocations.json","collocation-set.schema.json");
const scale10VerbPatterns=await validateFile("content/english/phrases/e04-scale-10-verb-patterns.json","verb-pattern-set.schema.json");
const scale10Phrases=await validateFile("content/english/phrases/e04-scale-10-phrases.json","phrase-set.schema.json");
const scale11Collocations=await validateFile("content/english/phrases/e04-scale-11-collocations.json","collocation-set.schema.json");
const scale11VerbPatterns=await validateFile("content/english/phrases/e04-scale-11-verb-patterns.json","verb-pattern-set.schema.json");
const scale11Phrases=await validateFile("content/english/phrases/e04-scale-11-phrases.json","phrase-set.schema.json");
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

if (scaleCollocations&&scaleVerbPatterns&&scalePhrases) {
  const expectedCollocations=batchExpectedCount("e04.phrase-pattern-scale-01","scale-collocations");
  const expectedVerbPatterns=batchExpectedCount("e04.phrase-pattern-scale-01","scale-verb-patterns");
  const expectedPhrases=batchExpectedCount("e04.phrase-pattern-scale-01","scale-phrases");
  if (scaleCollocations.records.length!==expectedCollocations) errors.push("E04 scale collocation count mismatch");
  if (scaleVerbPatterns.records.length!==expectedVerbPatterns) errors.push("E04 scale verb-pattern count mismatch");
  if (scalePhrases.records.length!==expectedPhrases) errors.push("E04 scale phrase count mismatch");

  const collocationTexts=new Set((collocationPilot?.records??[]).map(record=>record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const collocationIds=new Set((collocationPilot?.records??[]).map(record=>record.id));
  for (const record of scaleCollocations.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale collocation must remain draft");
    if (collocationIds.has(record.id)) errors.push(record.id+": duplicate collocation id across E04 batches");
    collocationIds.add(record.id);
    const key=record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (collocationTexts.has(key)) errors.push(record.id+": duplicate collocation text across E04 batches");
    collocationTexts.add(key);
    if (!(record.headwordKeys??[]).some(headword=>Number.isInteger(vocabLookup.entries?.[headword]))) errors.push(record.id+": scale collocation has no legacy vocabulary headword");
  }

  const patternKeys=new Set((verbPatternPilot?.records??[]).map(record=>record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US")));
  const patternIds=new Set((verbPatternPilot?.records??[]).map(record=>record.id));
  for (const record of scaleVerbPatterns.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale verb pattern must remain draft");
    if (patternIds.has(record.id)) errors.push(record.id+": duplicate verb-pattern id across E04 batches");
    patternIds.add(record.id);
    if (!Number.isInteger(vocabLookup.entries?.[record.lemma])) errors.push(record.id+": scale verb-pattern lemma missing from legacy vocabulary: "+record.lemma);
    const key=record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US");
    if (patternKeys.has(key)) errors.push(record.id+": duplicate lemma/frame across E04 batches");
    patternKeys.add(key);
  }

  const phraseKeys=new Set((phrasePilot?.records??[]).map(record=>record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const phraseIds=new Set((phrasePilot?.records??[]).map(record=>record.id));
  for (const record of scalePhrases.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale phrase must remain draft");
    if (phraseIds.has(record.id)) errors.push(record.id+": duplicate phrase id across E04 batches");
    phraseIds.add(record.id);
    const key=record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (phraseKeys.has(key)) errors.push(record.id+": duplicate phrase key across E04 batches");
    phraseKeys.add(key);
  }
  if (scalePhrases.records.filter(record=>record.type==="phrasal-verb").length!==10) errors.push("E04 scale phrases must contain 10 phrasal verbs");
  if (scalePhrases.records.filter(record=>record.type==="chunk").length!==5) errors.push("E04 scale phrases must contain 5 chunks");
  if (scalePhrases.records.filter(record=>record.type==="idiom").length!==5) errors.push("E04 scale phrases must contain 5 idioms");
}


if (scale02Collocations&&scale02VerbPatterns&&scale02Phrases) {
  const expectedCollocations=batchExpectedCount("e04.phrase-pattern-scale-02","scale-collocations");
  const expectedVerbPatterns=batchExpectedCount("e04.phrase-pattern-scale-02","scale-verb-patterns");
  const expectedPhrases=batchExpectedCount("e04.phrase-pattern-scale-02","scale-phrases");
  if (scale02Collocations.records.length!==expectedCollocations) errors.push("E04 scale 02 collocation count mismatch");
  if (scale02VerbPatterns.records.length!==expectedVerbPatterns) errors.push("E04 scale 02 verb-pattern count mismatch");
  if (scale02Phrases.records.length!==expectedPhrases) errors.push("E04 scale 02 phrase count mismatch");

  const collocationTexts=new Set([...(collocationPilot?.records??[]),...(scaleCollocations?.records??[])].map(record=>record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const collocationIds=new Set([...(collocationPilot?.records??[]),...(scaleCollocations?.records??[])].map(record=>record.id));
  for (const record of scale02Collocations.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 02 collocation must remain draft");
    if (collocationIds.has(record.id)) errors.push(record.id+": duplicate collocation id across E04 batches");
    collocationIds.add(record.id);
    const key=record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (collocationTexts.has(key)) errors.push(record.id+": duplicate collocation text across E04 batches");
    collocationTexts.add(key);
    if (!(record.headwordKeys??[]).some(headword=>Number.isInteger(vocabLookup.entries?.[headword]))) errors.push(record.id+": scale 02 collocation has no legacy vocabulary headword");
  }

  const patternKeys=new Set([...(verbPatternPilot?.records??[]),...(scaleVerbPatterns?.records??[])].map(record=>record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US")));
  const patternIds=new Set([...(verbPatternPilot?.records??[]),...(scaleVerbPatterns?.records??[])].map(record=>record.id));
  for (const record of scale02VerbPatterns.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 02 verb pattern must remain draft");
    if (patternIds.has(record.id)) errors.push(record.id+": duplicate verb-pattern id across E04 batches");
    patternIds.add(record.id);
    if (!Number.isInteger(vocabLookup.entries?.[record.lemma])) errors.push(record.id+": scale 02 verb-pattern lemma missing from legacy vocabulary: "+record.lemma);
    const key=record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US");
    if (patternKeys.has(key)) errors.push(record.id+": duplicate lemma/frame across E04 batches");
    patternKeys.add(key);
  }

  const phraseKeys=new Set([...(phrasePilot?.records??[]),...(scalePhrases?.records??[])].map(record=>record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const phraseIds=new Set([...(phrasePilot?.records??[]),...(scalePhrases?.records??[])].map(record=>record.id));
  for (const record of scale02Phrases.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 02 phrase must remain draft");
    if (phraseIds.has(record.id)) errors.push(record.id+": duplicate phrase id across E04 batches");
    phraseIds.add(record.id);
    const key=record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (phraseKeys.has(key)) errors.push(record.id+": duplicate phrase key across E04 batches");
    phraseKeys.add(key);
  }
  if (scale02Phrases.records.filter(record=>record.type==="phrasal-verb").length!==10) errors.push("E04 scale 02 phrases must contain 10 phrasal verbs");
  if (scale02Phrases.records.filter(record=>record.type==="chunk").length!==5) errors.push("E04 scale 02 phrases must contain 5 chunks");
  if (scale02Phrases.records.filter(record=>record.type==="idiom").length!==5) errors.push("E04 scale 02 phrases must contain 5 idioms");
}


if (scale03Collocations&&scale03VerbPatterns&&scale03Phrases) {
  const expectedCollocations=batchExpectedCount("e04.phrase-pattern-scale-03","scale-collocations");
  const expectedVerbPatterns=batchExpectedCount("e04.phrase-pattern-scale-03","scale-verb-patterns");
  const expectedPhrases=batchExpectedCount("e04.phrase-pattern-scale-03","scale-phrases");
  if (scale03Collocations.records.length!==expectedCollocations) errors.push("E04 scale 03 collocation count mismatch");
  if (scale03VerbPatterns.records.length!==expectedVerbPatterns) errors.push("E04 scale 03 verb-pattern count mismatch");
  if (scale03Phrases.records.length!==expectedPhrases) errors.push("E04 scale 03 phrase count mismatch");

  const priorCollocations=[...(collocationPilot?.records??[]),...(scaleCollocations?.records??[]),...(scale02Collocations?.records??[])];
  const collocationTexts=new Set(priorCollocations.map(record=>record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const collocationIds=new Set(priorCollocations.map(record=>record.id));
  for (const record of scale03Collocations.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 03 collocation must remain draft");
    if (collocationIds.has(record.id)) errors.push(record.id+": duplicate collocation id across E04 batches");
    collocationIds.add(record.id);
    const key=record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (collocationTexts.has(key)) errors.push(record.id+": duplicate collocation text across E04 batches");
    collocationTexts.add(key);
    if (!(record.headwordKeys??[]).some(headword=>Number.isInteger(vocabLookup.entries?.[headword]))) errors.push(record.id+": scale 03 collocation has no legacy vocabulary headword");
  }

  const priorPatterns=[...(verbPatternPilot?.records??[]),...(scaleVerbPatterns?.records??[]),...(scale02VerbPatterns?.records??[])];
  const patternKeys=new Set(priorPatterns.map(record=>record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US")));
  const patternIds=new Set(priorPatterns.map(record=>record.id));
  for (const record of scale03VerbPatterns.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 03 verb pattern must remain draft");
    if (patternIds.has(record.id)) errors.push(record.id+": duplicate verb-pattern id across E04 batches");
    patternIds.add(record.id);
    if (!Number.isInteger(vocabLookup.entries?.[record.lemma])) errors.push(record.id+": scale 03 verb-pattern lemma missing from legacy vocabulary: "+record.lemma);
    const key=record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US");
    if (patternKeys.has(key)) errors.push(record.id+": duplicate lemma/frame across E04 batches");
    patternKeys.add(key);
  }

  const priorPhrases=[...(phrasePilot?.records??[]),...(scalePhrases?.records??[]),...(scale02Phrases?.records??[])];
  const phraseKeys=new Set(priorPhrases.map(record=>record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const phraseIds=new Set(priorPhrases.map(record=>record.id));
  for (const record of scale03Phrases.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 03 phrase must remain draft");
    if (phraseIds.has(record.id)) errors.push(record.id+": duplicate phrase id across E04 batches");
    phraseIds.add(record.id);
    const key=record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (phraseKeys.has(key)) errors.push(record.id+": duplicate phrase key across E04 batches");
    phraseKeys.add(key);
  }
  if (scale03Phrases.records.filter(record=>record.type==="phrasal-verb").length!==10) errors.push("E04 scale 03 phrases must contain 10 phrasal verbs");
  if (scale03Phrases.records.filter(record=>record.type==="chunk").length!==5) errors.push("E04 scale 03 phrases must contain 5 chunks");
  if (scale03Phrases.records.filter(record=>record.type==="idiom").length!==5) errors.push("E04 scale 03 phrases must contain 5 idioms");
}


if (scale04Collocations&&scale04VerbPatterns&&scale04Phrases) {
  const expectedCollocations=batchExpectedCount("e04.phrase-pattern-scale-04","scale-collocations");
  const expectedVerbPatterns=batchExpectedCount("e04.phrase-pattern-scale-04","scale-verb-patterns");
  const expectedPhrases=batchExpectedCount("e04.phrase-pattern-scale-04","scale-phrases");
  if (scale04Collocations.records.length!==expectedCollocations) errors.push("E04 scale 04 collocation count mismatch");
  if (scale04VerbPatterns.records.length!==expectedVerbPatterns) errors.push("E04 scale 04 verb-pattern count mismatch");
  if (scale04Phrases.records.length!==expectedPhrases) errors.push("E04 scale 04 phrase count mismatch");

  const priorCollocations=[...(collocationPilot?.records??[]),...(scaleCollocations?.records??[]),...(scale02Collocations?.records??[]),...(scale03Collocations?.records??[])];
  const collocationTexts=new Set(priorCollocations.map(record=>record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const collocationIds=new Set(priorCollocations.map(record=>record.id));
  for (const record of scale04Collocations.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 04 collocation must remain draft");
    if (collocationIds.has(record.id)) errors.push(record.id+": duplicate collocation id across E04 batches");
    collocationIds.add(record.id);
    const key=record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (collocationTexts.has(key)) errors.push(record.id+": duplicate collocation text across E04 batches");
    collocationTexts.add(key);
    if (!(record.headwordKeys??[]).some(headword=>Number.isInteger(vocabLookup.entries?.[headword]))) errors.push(record.id+": scale 04 collocation has no legacy vocabulary headword");
  }

  const priorPatterns=[...(verbPatternPilot?.records??[]),...(scaleVerbPatterns?.records??[]),...(scale02VerbPatterns?.records??[]),...(scale03VerbPatterns?.records??[])];
  const patternKeys=new Set(priorPatterns.map(record=>record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US")));
  const patternIds=new Set(priorPatterns.map(record=>record.id));
  for (const record of scale04VerbPatterns.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 04 verb pattern must remain draft");
    if (patternIds.has(record.id)) errors.push(record.id+": duplicate verb-pattern id across E04 batches");
    patternIds.add(record.id);
    if (!Number.isInteger(vocabLookup.entries?.[record.lemma])) errors.push(record.id+": scale 04 verb-pattern lemma missing from legacy vocabulary: "+record.lemma);
    const key=record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US");
    if (patternKeys.has(key)) errors.push(record.id+": duplicate lemma/frame across E04 batches");
    patternKeys.add(key);
  }

  const priorPhrases=[...(phrasePilot?.records??[]),...(scalePhrases?.records??[]),...(scale02Phrases?.records??[]),...(scale03Phrases?.records??[])];
  const phraseKeys=new Set(priorPhrases.map(record=>record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const phraseIds=new Set(priorPhrases.map(record=>record.id));
  for (const record of scale04Phrases.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 04 phrase must remain draft");
    if (phraseIds.has(record.id)) errors.push(record.id+": duplicate phrase id across E04 batches");
    phraseIds.add(record.id);
    const key=record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (phraseKeys.has(key)) errors.push(record.id+": duplicate phrase key across E04 batches");
    phraseKeys.add(key);
  }
  if (scale04Phrases.records.filter(record=>record.type==="phrasal-verb").length!==10) errors.push("E04 scale 04 phrases must contain 10 phrasal verbs");
  if (scale04Phrases.records.filter(record=>record.type==="chunk").length!==5) errors.push("E04 scale 04 phrases must contain 5 chunks");
  if (scale04Phrases.records.filter(record=>record.type==="idiom").length!==5) errors.push("E04 scale 04 phrases must contain 5 idioms");
}


if (scale05Collocations&&scale05VerbPatterns&&scale05Phrases) {
  const expectedCollocations=batchExpectedCount("e04.phrase-pattern-scale-05","scale-collocations");
  const expectedVerbPatterns=batchExpectedCount("e04.phrase-pattern-scale-05","scale-verb-patterns");
  const expectedPhrases=batchExpectedCount("e04.phrase-pattern-scale-05","scale-phrases");
  if (scale05Collocations.records.length!==expectedCollocations) errors.push("E04 scale 05 collocation count mismatch");
  if (scale05VerbPatterns.records.length!==expectedVerbPatterns) errors.push("E04 scale 05 verb-pattern count mismatch");
  if (scale05Phrases.records.length!==expectedPhrases) errors.push("E04 scale 05 phrase count mismatch");

  const priorCollocations=[...(collocationPilot?.records??[]),...(scaleCollocations?.records??[]),...(scale02Collocations?.records??[]),...(scale03Collocations?.records??[]),...(scale04Collocations?.records??[])];
  const collocationTexts=new Set(priorCollocations.map(record=>record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const collocationIds=new Set(priorCollocations.map(record=>record.id));
  for (const record of scale05Collocations.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 05 collocation must remain draft");
    if (collocationIds.has(record.id)) errors.push(record.id+": duplicate collocation id across E04 batches");
    collocationIds.add(record.id);
    const key=record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (collocationTexts.has(key)) errors.push(record.id+": duplicate collocation text across E04 batches");
    collocationTexts.add(key);
    if (!(record.headwordKeys??[]).some(headword=>Number.isInteger(vocabLookup.entries?.[headword]))) errors.push(record.id+": scale 05 collocation has no legacy vocabulary headword");
  }

  const priorPatterns=[...(verbPatternPilot?.records??[]),...(scaleVerbPatterns?.records??[]),...(scale02VerbPatterns?.records??[]),...(scale03VerbPatterns?.records??[]),...(scale04VerbPatterns?.records??[])];
  const patternKeys=new Set(priorPatterns.map(record=>record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US")));
  const patternIds=new Set(priorPatterns.map(record=>record.id));
  for (const record of scale05VerbPatterns.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 05 verb pattern must remain draft");
    if (patternIds.has(record.id)) errors.push(record.id+": duplicate verb-pattern id across E04 batches");
    patternIds.add(record.id);
    if (!Number.isInteger(vocabLookup.entries?.[record.lemma])) errors.push(record.id+": scale 05 verb-pattern lemma missing from legacy vocabulary: "+record.lemma);
    const key=record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US");
    if (patternKeys.has(key)) errors.push(record.id+": duplicate lemma/frame across E04 batches");
    patternKeys.add(key);
  }

  const priorPhrases=[...(phrasePilot?.records??[]),...(scalePhrases?.records??[]),...(scale02Phrases?.records??[]),...(scale03Phrases?.records??[]),...(scale04Phrases?.records??[])];
  const phraseKeys=new Set(priorPhrases.map(record=>record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const phraseIds=new Set(priorPhrases.map(record=>record.id));
  for (const record of scale05Phrases.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 05 phrase must remain draft");
    if (phraseIds.has(record.id)) errors.push(record.id+": duplicate phrase id across E04 batches");
    phraseIds.add(record.id);
    const key=record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (phraseKeys.has(key)) errors.push(record.id+": duplicate phrase key across E04 batches");
    phraseKeys.add(key);
  }
  if (scale05Phrases.records.filter(record=>record.type==="phrasal-verb").length!==10) errors.push("E04 scale 05 phrases must contain 10 phrasal verbs");
  if (scale05Phrases.records.filter(record=>record.type==="chunk").length!==5) errors.push("E04 scale 05 phrases must contain 5 chunks");
  if (scale05Phrases.records.filter(record=>record.type==="idiom").length!==5) errors.push("E04 scale 05 phrases must contain 5 idioms");
}


if (scale06Collocations&&scale06VerbPatterns&&scale06Phrases) {
  const expectedCollocations=batchExpectedCount("e04.phrase-pattern-scale-06","scale-collocations");
  const expectedVerbPatterns=batchExpectedCount("e04.phrase-pattern-scale-06","scale-verb-patterns");
  const expectedPhrases=batchExpectedCount("e04.phrase-pattern-scale-06","scale-phrases");
  if (scale06Collocations.records.length!==expectedCollocations) errors.push("E04 scale 06 collocation count mismatch");
  if (scale06VerbPatterns.records.length!==expectedVerbPatterns) errors.push("E04 scale 06 verb-pattern count mismatch");
  if (scale06Phrases.records.length!==expectedPhrases) errors.push("E04 scale 06 phrase count mismatch");

  const priorCollocations=[...(collocationPilot?.records??[]),...(scaleCollocations?.records??[]),...(scale02Collocations?.records??[]),...(scale03Collocations?.records??[]),...(scale04Collocations?.records??[]),...(scale05Collocations?.records??[])];
  const collocationTexts=new Set(priorCollocations.map(record=>record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const collocationIds=new Set(priorCollocations.map(record=>record.id));
  for (const record of scale06Collocations.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 06 collocation must remain draft");
    if (collocationIds.has(record.id)) errors.push(record.id+": duplicate collocation id across E04 batches");
    collocationIds.add(record.id);
    const key=record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (collocationTexts.has(key)) errors.push(record.id+": duplicate collocation text across E04 batches");
    collocationTexts.add(key);
    if (!(record.headwordKeys??[]).some(headword=>Number.isInteger(vocabLookup.entries?.[headword]))) errors.push(record.id+": scale 06 collocation has no legacy vocabulary headword");
  }

  const priorPatterns=[...(verbPatternPilot?.records??[]),...(scaleVerbPatterns?.records??[]),...(scale02VerbPatterns?.records??[]),...(scale03VerbPatterns?.records??[]),...(scale04VerbPatterns?.records??[]),...(scale05VerbPatterns?.records??[])];
  const patternKeys=new Set(priorPatterns.map(record=>record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US")));
  const patternIds=new Set(priorPatterns.map(record=>record.id));
  for (const record of scale06VerbPatterns.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 06 verb pattern must remain draft");
    if (patternIds.has(record.id)) errors.push(record.id+": duplicate verb-pattern id across E04 batches");
    patternIds.add(record.id);
    if (!Number.isInteger(vocabLookup.entries?.[record.lemma])) errors.push(record.id+": scale 06 verb-pattern lemma missing from legacy vocabulary: "+record.lemma);
    const key=record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US");
    if (patternKeys.has(key)) errors.push(record.id+": duplicate lemma/frame across E04 batches");
    patternKeys.add(key);
  }

  const priorPhrases=[...(phrasePilot?.records??[]),...(scalePhrases?.records??[]),...(scale02Phrases?.records??[]),...(scale03Phrases?.records??[]),...(scale04Phrases?.records??[]),...(scale05Phrases?.records??[])];
  const phraseKeys=new Set(priorPhrases.map(record=>record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const phraseIds=new Set(priorPhrases.map(record=>record.id));
  for (const record of scale06Phrases.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 06 phrase must remain draft");
    if (phraseIds.has(record.id)) errors.push(record.id+": duplicate phrase id across E04 batches");
    phraseIds.add(record.id);
    const key=record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (phraseKeys.has(key)) errors.push(record.id+": duplicate phrase key across E04 batches");
    phraseKeys.add(key);
  }
  if (scale06Phrases.records.filter(record=>record.type==="phrasal-verb").length!==10) errors.push("E04 scale 06 phrases must contain 10 phrasal verbs");
  if (scale06Phrases.records.filter(record=>record.type==="chunk").length!==5) errors.push("E04 scale 06 phrases must contain 5 chunks");
  if (scale06Phrases.records.filter(record=>record.type==="idiom").length!==5) errors.push("E04 scale 06 phrases must contain 5 idioms");
}



if (scale07Collocations&&scale07VerbPatterns&&scale07Phrases) {
  const expectedCollocations=batchExpectedCount("e04.phrase-pattern-scale-07","scale-collocations");
  const expectedVerbPatterns=batchExpectedCount("e04.phrase-pattern-scale-07","scale-verb-patterns");
  const expectedPhrases=batchExpectedCount("e04.phrase-pattern-scale-07","scale-phrases");
  if (scale07Collocations.records.length!==expectedCollocations) errors.push("E04 scale 07 collocation count mismatch");
  if (scale07VerbPatterns.records.length!==expectedVerbPatterns) errors.push("E04 scale 07 verb-pattern count mismatch");
  if (scale07Phrases.records.length!==expectedPhrases) errors.push("E04 scale 07 phrase count mismatch");

  const priorCollocations=[...(collocationPilot?.records??[]),...(scaleCollocations?.records??[]),...(scale02Collocations?.records??[]),...(scale03Collocations?.records??[]),...(scale04Collocations?.records??[]),...(scale05Collocations?.records??[]),...(scale06Collocations?.records??[])];
  const collocationTexts=new Set(priorCollocations.map(record=>record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const collocationIds=new Set(priorCollocations.map(record=>record.id));
  for (const record of scale07Collocations.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 07 collocation must remain draft");
    if (collocationIds.has(record.id)) errors.push(record.id+": duplicate collocation id across E04 batches");
    collocationIds.add(record.id);
    const key=record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (collocationTexts.has(key)) errors.push(record.id+": duplicate collocation text across E04 batches");
    collocationTexts.add(key);
    if (!(record.headwordKeys??[]).some(headword=>Number.isInteger(vocabLookup.entries?.[headword]))) errors.push(record.id+": scale 07 collocation has no legacy vocabulary headword");
  }

  const priorPatterns=[...(verbPatternPilot?.records??[]),...(scaleVerbPatterns?.records??[]),...(scale02VerbPatterns?.records??[]),...(scale03VerbPatterns?.records??[]),...(scale04VerbPatterns?.records??[]),...(scale05VerbPatterns?.records??[]),...(scale06VerbPatterns?.records??[])];
  const patternKeys=new Set(priorPatterns.map(record=>record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US")));
  const patternIds=new Set(priorPatterns.map(record=>record.id));
  for (const record of scale07VerbPatterns.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 07 verb pattern must remain draft");
    if (patternIds.has(record.id)) errors.push(record.id+": duplicate verb-pattern id across E04 batches");
    patternIds.add(record.id);
    if (!Number.isInteger(vocabLookup.entries?.[record.lemma])) errors.push(record.id+": scale 07 verb-pattern lemma missing from legacy vocabulary: "+record.lemma);
    const key=record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US");
    if (patternKeys.has(key)) errors.push(record.id+": duplicate lemma/frame across E04 batches");
    patternKeys.add(key);
  }

  const priorPhrases=[...(phrasePilot?.records??[]),...(scalePhrases?.records??[]),...(scale02Phrases?.records??[]),...(scale03Phrases?.records??[]),...(scale04Phrases?.records??[]),...(scale05Phrases?.records??[]),...(scale06Phrases?.records??[])];
  const phraseKeys=new Set(priorPhrases.map(record=>record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const phraseIds=new Set(priorPhrases.map(record=>record.id));
  for (const record of scale07Phrases.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 07 phrase must remain draft");
    if (phraseIds.has(record.id)) errors.push(record.id+": duplicate phrase id across E04 batches");
    phraseIds.add(record.id);
    const key=record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (phraseKeys.has(key)) errors.push(record.id+": duplicate phrase key across E04 batches");
    phraseKeys.add(key);
  }
  if (scale07Phrases.records.filter(record=>record.type==="phrasal-verb").length!==10) errors.push("E04 scale 07 phrases must contain 10 phrasal verbs");
  if (scale07Phrases.records.filter(record=>record.type==="chunk").length!==5) errors.push("E04 scale 07 phrases must contain 5 chunks");
  if (scale07Phrases.records.filter(record=>record.type==="idiom").length!==5) errors.push("E04 scale 07 phrases must contain 5 idioms");
}



if (scale08Collocations&&scale08VerbPatterns&&scale08Phrases) {
  const expectedCollocations=batchExpectedCount("e04.phrase-pattern-scale-08","scale-collocations");
  const expectedVerbPatterns=batchExpectedCount("e04.phrase-pattern-scale-08","scale-verb-patterns");
  const expectedPhrases=batchExpectedCount("e04.phrase-pattern-scale-08","scale-phrases");
  if (scale08Collocations.records.length!==expectedCollocations) errors.push("E04 scale 08 collocation count mismatch");
  if (scale08VerbPatterns.records.length!==expectedVerbPatterns) errors.push("E04 scale 08 verb-pattern count mismatch");
  if (scale08Phrases.records.length!==expectedPhrases) errors.push("E04 scale 08 phrase count mismatch");

  const priorCollocations=[...(collocationPilot?.records??[]),...(scaleCollocations?.records??[]),...(scale02Collocations?.records??[]),...(scale03Collocations?.records??[]),...(scale04Collocations?.records??[]),...(scale05Collocations?.records??[]),...(scale06Collocations?.records??[]),...(scale07Collocations?.records??[])];
  const collocationTexts=new Set(priorCollocations.map(record=>record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const collocationIds=new Set(priorCollocations.map(record=>record.id));
  for (const record of scale08Collocations.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 08 collocation must remain draft");
    if (collocationIds.has(record.id)) errors.push(record.id+": duplicate collocation id across E04 batches");
    collocationIds.add(record.id);
    const key=record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (collocationTexts.has(key)) errors.push(record.id+": duplicate collocation text across E04 batches");
    collocationTexts.add(key);
    if (!(record.headwordKeys??[]).some(headword=>Number.isInteger(vocabLookup.entries?.[headword]))) errors.push(record.id+": scale 08 collocation has no legacy vocabulary headword");
  }

  const priorPatterns=[...(verbPatternPilot?.records??[]),...(scaleVerbPatterns?.records??[]),...(scale02VerbPatterns?.records??[]),...(scale03VerbPatterns?.records??[]),...(scale04VerbPatterns?.records??[]),...(scale05VerbPatterns?.records??[]),...(scale06VerbPatterns?.records??[]),...(scale07VerbPatterns?.records??[])];
  const patternKeys=new Set(priorPatterns.map(record=>record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US")));
  const patternIds=new Set(priorPatterns.map(record=>record.id));
  for (const record of scale08VerbPatterns.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 08 verb pattern must remain draft");
    if (patternIds.has(record.id)) errors.push(record.id+": duplicate verb-pattern id across E04 batches");
    patternIds.add(record.id);
    if (!Number.isInteger(vocabLookup.entries?.[record.lemma])) errors.push(record.id+": scale 08 verb-pattern lemma missing from legacy vocabulary: "+record.lemma);
    const key=record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US");
    if (patternKeys.has(key)) errors.push(record.id+": duplicate lemma/frame across E04 batches");
    patternKeys.add(key);
  }

  const priorPhrases=[...(phrasePilot?.records??[]),...(scalePhrases?.records??[]),...(scale02Phrases?.records??[]),...(scale03Phrases?.records??[]),...(scale04Phrases?.records??[]),...(scale05Phrases?.records??[]),...(scale06Phrases?.records??[]),...(scale07Phrases?.records??[])];
  const phraseKeys=new Set(priorPhrases.map(record=>record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const phraseIds=new Set(priorPhrases.map(record=>record.id));
  for (const record of scale08Phrases.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 08 phrase must remain draft");
    if (phraseIds.has(record.id)) errors.push(record.id+": duplicate phrase id across E04 batches");
    phraseIds.add(record.id);
    const key=record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (phraseKeys.has(key)) errors.push(record.id+": duplicate phrase key across E04 batches");
    phraseKeys.add(key);
  }
  if (scale08Phrases.records.filter(record=>record.type==="phrasal-verb").length!==10) errors.push("E04 scale 08 phrases must contain 10 phrasal verbs");
  if (scale08Phrases.records.filter(record=>record.type==="chunk").length!==5) errors.push("E04 scale 08 phrases must contain 5 chunks");
  if (scale08Phrases.records.filter(record=>record.type==="idiom").length!==5) errors.push("E04 scale 08 phrases must contain 5 idioms");
}



if (scale09Collocations&&scale09VerbPatterns&&scale09Phrases) {
  const expectedCollocations=batchExpectedCount("e04.phrase-pattern-scale-09","scale-collocations");
  const expectedVerbPatterns=batchExpectedCount("e04.phrase-pattern-scale-09","scale-verb-patterns");
  const expectedPhrases=batchExpectedCount("e04.phrase-pattern-scale-09","scale-phrases");
  if (scale09Collocations.records.length!==expectedCollocations) errors.push("E04 scale 09 collocation count mismatch");
  if (scale09VerbPatterns.records.length!==expectedVerbPatterns) errors.push("E04 scale 09 verb-pattern count mismatch");
  if (scale09Phrases.records.length!==expectedPhrases) errors.push("E04 scale 09 phrase count mismatch");

  const priorCollocations=[...(collocationPilot?.records??[]),...(scaleCollocations?.records??[]),...(scale02Collocations?.records??[]),...(scale03Collocations?.records??[]),...(scale04Collocations?.records??[]),...(scale05Collocations?.records??[]),...(scale06Collocations?.records??[]),...(scale07Collocations?.records??[]),...(scale08Collocations?.records??[])];
  const collocationTexts=new Set(priorCollocations.map(record=>record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const collocationIds=new Set(priorCollocations.map(record=>record.id));
  for (const record of scale09Collocations.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 09 collocation must remain draft");
    if (collocationIds.has(record.id)) errors.push(record.id+": duplicate collocation id across E04 batches");
    collocationIds.add(record.id);
    const key=record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (collocationTexts.has(key)) errors.push(record.id+": duplicate collocation text across E04 batches");
    collocationTexts.add(key);
    if (!(record.headwordKeys??[]).some(headword=>Number.isInteger(vocabLookup.entries?.[headword]))) errors.push(record.id+": scale 09 collocation has no legacy vocabulary headword");
  }

  const priorPatterns=[...(verbPatternPilot?.records??[]),...(scaleVerbPatterns?.records??[]),...(scale02VerbPatterns?.records??[]),...(scale03VerbPatterns?.records??[]),...(scale04VerbPatterns?.records??[]),...(scale05VerbPatterns?.records??[]),...(scale06VerbPatterns?.records??[]),...(scale07VerbPatterns?.records??[]),...(scale08VerbPatterns?.records??[])];
  const patternKeys=new Set(priorPatterns.map(record=>record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US")));
  const patternIds=new Set(priorPatterns.map(record=>record.id));
  for (const record of scale09VerbPatterns.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 09 verb pattern must remain draft");
    if (patternIds.has(record.id)) errors.push(record.id+": duplicate verb-pattern id across E04 batches");
    patternIds.add(record.id);
    if (!Number.isInteger(vocabLookup.entries?.[record.lemma])) errors.push(record.id+": scale 09 verb-pattern lemma missing from legacy vocabulary: "+record.lemma);
    const key=record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US");
    if (patternKeys.has(key)) errors.push(record.id+": duplicate lemma/frame across E04 batches");
    patternKeys.add(key);
  }

  const priorPhrases=[...(phrasePilot?.records??[]),...(scalePhrases?.records??[]),...(scale02Phrases?.records??[]),...(scale03Phrases?.records??[]),...(scale04Phrases?.records??[]),...(scale05Phrases?.records??[]),...(scale06Phrases?.records??[]),...(scale07Phrases?.records??[]),...(scale08Phrases?.records??[])];
  const phraseKeys=new Set(priorPhrases.map(record=>record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const phraseIds=new Set(priorPhrases.map(record=>record.id));
  for (const record of scale09Phrases.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 09 phrase must remain draft");
    if (phraseIds.has(record.id)) errors.push(record.id+": duplicate phrase id across E04 batches");
    phraseIds.add(record.id);
    const key=record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (phraseKeys.has(key)) errors.push(record.id+": duplicate phrase key across E04 batches");
    phraseKeys.add(key);
  }
  if (scale09Phrases.records.filter(record=>record.type==="phrasal-verb").length!==10) errors.push("E04 scale 09 phrases must contain 10 phrasal verbs");
  if (scale09Phrases.records.filter(record=>record.type==="chunk").length!==5) errors.push("E04 scale 09 phrases must contain 5 chunks");
  if (scale09Phrases.records.filter(record=>record.type==="idiom").length!==5) errors.push("E04 scale 09 phrases must contain 5 idioms");
}



if (scale10Collocations&&scale10VerbPatterns&&scale10Phrases) {
  const expectedCollocations=batchExpectedCount("e04.phrase-pattern-scale-10","scale-collocations");
  const expectedVerbPatterns=batchExpectedCount("e04.phrase-pattern-scale-10","scale-verb-patterns");
  const expectedPhrases=batchExpectedCount("e04.phrase-pattern-scale-10","scale-phrases");
  if (scale10Collocations.records.length!==expectedCollocations) errors.push("E04 scale 10 collocation count mismatch");
  if (scale10VerbPatterns.records.length!==expectedVerbPatterns) errors.push("E04 scale 10 verb-pattern count mismatch");
  if (scale10Phrases.records.length!==expectedPhrases) errors.push("E04 scale 10 phrase count mismatch");

  const priorCollocations=[...(collocationPilot?.records??[]),...(scaleCollocations?.records??[]),...(scale02Collocations?.records??[]),...(scale03Collocations?.records??[]),...(scale04Collocations?.records??[]),...(scale05Collocations?.records??[]),...(scale06Collocations?.records??[]),...(scale07Collocations?.records??[]),...(scale08Collocations?.records??[]),...(scale09Collocations?.records??[])];
  const collocationTexts=new Set(priorCollocations.map(record=>record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const collocationIds=new Set(priorCollocations.map(record=>record.id));
  for (const record of scale10Collocations.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 10 collocation must remain draft");
    if (collocationIds.has(record.id)) errors.push(record.id+": duplicate collocation id across E04 batches");
    collocationIds.add(record.id);
    const key=record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (collocationTexts.has(key)) errors.push(record.id+": duplicate collocation text across E04 batches");
    collocationTexts.add(key);
    if (!(record.headwordKeys??[]).some(headword=>Number.isInteger(vocabLookup.entries?.[headword]))) errors.push(record.id+": scale 10 collocation has no legacy vocabulary headword");
  }

  const priorPatterns=[...(verbPatternPilot?.records??[]),...(scaleVerbPatterns?.records??[]),...(scale02VerbPatterns?.records??[]),...(scale03VerbPatterns?.records??[]),...(scale04VerbPatterns?.records??[]),...(scale05VerbPatterns?.records??[]),...(scale06VerbPatterns?.records??[]),...(scale07VerbPatterns?.records??[]),...(scale08VerbPatterns?.records??[]),...(scale09VerbPatterns?.records??[])];
  const patternKeys=new Set(priorPatterns.map(record=>record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US")));
  const patternIds=new Set(priorPatterns.map(record=>record.id));
  for (const record of scale10VerbPatterns.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 10 verb pattern must remain draft");
    if (patternIds.has(record.id)) errors.push(record.id+": duplicate verb-pattern id across E04 batches");
    patternIds.add(record.id);
    if (!Number.isInteger(vocabLookup.entries?.[record.lemma])) errors.push(record.id+": scale 10 verb-pattern lemma missing from legacy vocabulary: "+record.lemma);
    const key=record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US");
    if (patternKeys.has(key)) errors.push(record.id+": duplicate lemma/frame across E04 batches");
    patternKeys.add(key);
  }

  const priorPhrases=[...(phrasePilot?.records??[]),...(scalePhrases?.records??[]),...(scale02Phrases?.records??[]),...(scale03Phrases?.records??[]),...(scale04Phrases?.records??[]),...(scale05Phrases?.records??[]),...(scale06Phrases?.records??[]),...(scale07Phrases?.records??[]),...(scale08Phrases?.records??[]),...(scale09Phrases?.records??[])];
  const phraseKeys=new Set(priorPhrases.map(record=>record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const phraseIds=new Set(priorPhrases.map(record=>record.id));
  for (const record of scale10Phrases.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 10 phrase must remain draft");
    if (phraseIds.has(record.id)) errors.push(record.id+": duplicate phrase id across E04 batches");
    phraseIds.add(record.id);
    const key=record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (phraseKeys.has(key)) errors.push(record.id+": duplicate phrase key across E04 batches");
    phraseKeys.add(key);
  }
  if (scale10Phrases.records.filter(record=>record.type==="phrasal-verb").length!==10) errors.push("E04 scale 10 phrases must contain 10 phrasal verbs");
  if (scale10Phrases.records.filter(record=>record.type==="chunk").length!==5) errors.push("E04 scale 10 phrases must contain 5 chunks");
  if (scale10Phrases.records.filter(record=>record.type==="idiom").length!==5) errors.push("E04 scale 10 phrases must contain 5 idioms");
}


if (scale11Collocations&&scale11VerbPatterns&&scale11Phrases) {
  const expectedCollocations=batchExpectedCount("e04.phrase-pattern-scale-11","scale-collocations");
  const expectedVerbPatterns=batchExpectedCount("e04.phrase-pattern-scale-11","scale-verb-patterns");
  const expectedPhrases=batchExpectedCount("e04.phrase-pattern-scale-11","scale-phrases");
  if (scale11Collocations.records.length!==expectedCollocations) errors.push("E04 scale 11 collocation count mismatch");
  if (scale11VerbPatterns.records.length!==expectedVerbPatterns) errors.push("E04 scale 11 verb-pattern count mismatch");
  if (scale11Phrases.records.length!==expectedPhrases) errors.push("E04 scale 11 phrase count mismatch");

  const priorCollocations=[...(collocationPilot?.records??[]),...(scaleCollocations?.records??[]),...(scale02Collocations?.records??[]),...(scale03Collocations?.records??[]),...(scale04Collocations?.records??[]),...(scale05Collocations?.records??[]),...(scale06Collocations?.records??[]),...(scale07Collocations?.records??[]),...(scale08Collocations?.records??[]),...(scale09Collocations?.records??[]),...(scale10Collocations?.records??[])];
  const collocationTexts=new Set(priorCollocations.map(record=>record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const collocationIds=new Set(priorCollocations.map(record=>record.id));
  for (const record of scale11Collocations.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 11 collocation must remain draft");
    if (collocationIds.has(record.id)) errors.push(record.id+": duplicate collocation id across E04 batches");
    collocationIds.add(record.id);
    const key=record.text.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (collocationTexts.has(key)) errors.push(record.id+": duplicate collocation text across E04 batches");
    collocationTexts.add(key);
    if (!(record.headwordKeys??[]).some(headword=>Number.isInteger(vocabLookup.entries?.[headword]))) errors.push(record.id+": scale 11 collocation has no legacy vocabulary headword");
  }

  const priorPatterns=[...(verbPatternPilot?.records??[]),...(scaleVerbPatterns?.records??[]),...(scale02VerbPatterns?.records??[]),...(scale03VerbPatterns?.records??[]),...(scale04VerbPatterns?.records??[]),...(scale05VerbPatterns?.records??[]),...(scale06VerbPatterns?.records??[]),...(scale07VerbPatterns?.records??[]),...(scale08VerbPatterns?.records??[]),...(scale09VerbPatterns?.records??[]),...(scale10VerbPatterns?.records??[])];
  const patternKeys=new Set(priorPatterns.map(record=>record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US")));
  const patternIds=new Set(priorPatterns.map(record=>record.id));
  for (const record of scale11VerbPatterns.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 11 verb pattern must remain draft");
    if (patternIds.has(record.id)) errors.push(record.id+": duplicate verb-pattern id across E04 batches");
    patternIds.add(record.id);
    if (!Number.isInteger(vocabLookup.entries?.[record.lemma])) errors.push(record.id+": scale 11 verb-pattern lemma missing from legacy vocabulary: "+record.lemma);
    const key=record.lemma+"\u0000"+record.frame.toLocaleLowerCase("en-US");
    if (patternKeys.has(key)) errors.push(record.id+": duplicate lemma/frame across E04 batches");
    patternKeys.add(key);
  }

  const priorPhrases=[...(phrasePilot?.records??[]),...(scalePhrases?.records??[]),...(scale02Phrases?.records??[]),...(scale03Phrases?.records??[]),...(scale04Phrases?.records??[]),...(scale05Phrases?.records??[]),...(scale06Phrases?.records??[]),...(scale07Phrases?.records??[]),...(scale08Phrases?.records??[]),...(scale09Phrases?.records??[]),...(scale10Phrases?.records??[])];
  const phraseKeys=new Set(priorPhrases.map(record=>record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US")));
  const phraseIds=new Set(priorPhrases.map(record=>record.id));
  for (const record of scale11Phrases.records) {
    if (record.quality?.state!=="draft") errors.push(record.id+": E04 scale 11 phrase must remain draft");
    if (phraseIds.has(record.id)) errors.push(record.id+": duplicate phrase id across E04 batches");
    phraseIds.add(record.id);
    const key=record.key.normalize("NFKC").trim().toLocaleLowerCase("en-US");
    if (phraseKeys.has(key)) errors.push(record.id+": duplicate phrase key across E04 batches");
    phraseKeys.add(key);
  }
  if (scale11Phrases.records.filter(record=>record.type==="phrasal-verb").length!==10) errors.push("E04 scale 11 phrases must contain 10 phrasal verbs");
  if (scale11Phrases.records.filter(record=>record.type==="chunk").length!==5) errors.push("E04 scale 11 phrases must contain 5 chunks");
  if (scale11Phrases.records.filter(record=>record.type==="idiom").length!==5) errors.push("E04 scale 11 phrases must contain 5 idioms");
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
