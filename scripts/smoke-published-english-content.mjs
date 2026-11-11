import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson } from "./english-content-core.mjs";
import { readE11TypingTextReviewShards } from "./english-typing-text-shards.mjs";
import { readReviewedTatoebaEnglish } from "./english-tatoeba-reviewed.mjs";
import { readEnglishReviewLedger } from "./english-review-core.mjs";
import { buildGameEnglishActivityDataset } from "../shared/english-content/game-adapters.mjs";
import {
  buildPublishedGameEnglishActivityDataset,
  countPublishedEnglishActivityRecords,
} from "../shared/english-content/activity-source.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const [dictionaryManifest,grammarManifest,sentenceManifest,e11TypingTextReviewShards]=await Promise.all([
  readJson(path.join(root,"shared","dictionary","manifest.json")),
  readJson(path.join(root,"shared","grammar","manifest.json")),
  readJson(path.join(root,"shared","sentences","manifest.json")),
  readE11TypingTextReviewShards(root),
]);
const e11TypingTextExpansionCount=e11TypingTextReviewShards.reduce(
  (count,shard)=>count+shard.records.length,
  0,
);
const expectedTypingTextExampleCount=300+e11TypingTextExpansionCount;
const [batchManifest,reviewLedger]=await Promise.all([
  readJson(path.join(root,"content/english/batches/manifest.json")),readEnglishReviewLedger(root),
]);
const tatoebaEnglishControlled=await readReviewedTatoebaEnglish(root,batchManifest,reviewLedger);
const tatoebaEnglishPublished=tatoebaEnglishControlled.filter(record=>record.quality.state==="published");

const sentenceDirFiles=await fs.readdir(path.join(root,"content","english","sentences"));
const e11TranslationSentenceFiles=sentenceDirFiles.filter(f=>/^e11-translation-sentences-\d+\.json$/.test(f));
let e11TranslationSentencesCount=0;
for (const f of e11TranslationSentenceFiles) {
  const doc=await readJson(path.join(root,"content","english","sentences",f));
  e11TranslationSentencesCount+=doc.records?.length??0;
}
const e11TranslationSliceFiles=sentenceDirFiles.filter(f=>/^e11-translation-slice-\d+\.json$/.test(f));
let e11TranslationsCount=0;
for (const f of e11TranslationSliceFiles) {
  const doc=await readJson(path.join(root,"content","english","sentences",f));
  e11TranslationsCount+=doc.records?.length??0;
}

const e11MultiwozFiles=sentenceDirFiles.filter(f=>/^e11-multiwoz-dialogue-reviewed-slice-\d+\.json$/.test(f));
let e11DialoguesCount=0;
for (const f of e11MultiwozFiles) {
  const doc=await readJson(path.join(root,"content","english","sentences",f));
  e11DialoguesCount+=doc.records?.length??0;
}
const e11DialogueSliceFiles=sentenceDirFiles.filter(f=>/^e11-dialogue-slice-\d+\.json$/.test(f));
for (const f of e11DialogueSliceFiles) {
  const doc=await readJson(path.join(root,"content","english","sentences",f));
  e11DialoguesCount+=doc.records?.length??0;
}
const expectedDialogueCount=100+e11DialoguesCount;

const e11ClozeFiles=sentenceDirFiles.filter(f=>/^e11-cloze-slice-\d+\.json$/.test(f));
let e11ClozeCount=0;
for (const f of e11ClozeFiles) {
  const doc=await readJson(path.join(root,"content","english","sentences",f));
  e11ClozeCount+=doc.records?.length??0;
}

const e11TransformationFiles=sentenceDirFiles.filter(f=>/^e11-transformation-slice-\d+\.json$/.test(f));
let e11TransformationsCount=0;
for (const f of e11TransformationFiles) {
  const doc=await readJson(path.join(root,"content","english","sentences",f));
  e11TransformationsCount+=doc.records?.length??0;
}

const e11MistakeFiles=sentenceDirFiles.filter(f=>/^e11-mistake-slice-\d+\.json$/.test(f));
let e11MistakesCount=0;
for (const f of e11MistakeFiles) {
  const doc=await readJson(path.join(root,"content","english","sentences",f));
  e11MistakesCount+=doc.records?.length??0;
}

const v2ExerciseFiles=sentenceDirFiles.filter(f=>/^v2-[a-z0-9._-]+\.json$/.test(f));
let v2ExercisesCount=0;
for (const f of v2ExerciseFiles) {
  const doc=await readJson(path.join(root,"content","english","sentences",f));
  v2ExercisesCount+=doc.records?.length??0;
}

const expectedExerciseCount=1400+e11TranslationsCount+e11ClozeCount+e11TransformationsCount+v2ExercisesCount;
const expectedExampleCount=1513+e11TypingTextExpansionCount+tatoebaEnglishPublished.length+e11TranslationSentencesCount;
const expectedMistakesCount=388+e11MistakesCount;
const expectedSentenceManifestCount=3401+e11TypingTextExpansionCount+tatoebaEnglishPublished.length+e11TranslationSentencesCount+e11TranslationsCount+e11DialoguesCount+e11ClozeCount+e11TransformationsCount+e11MistakesCount+v2ExercisesCount;
const errors=[];

const fileRuntimeLoader={
  async loadDataset(dataset,{prefix}={}){
    const baseDir=path.join("shared",dataset);
    const manifest=await readJson(path.join(root,baseDir,"manifest.json"));
    const records=[];
    for(const shard of manifest.shards??[]){
      if(prefix!==undefined&&!String(shard.id).startsWith(prefix)) continue;
      const doc=await readJson(path.join(root,baseDir,shard.path));
      if(!Array.isArray(doc.records)||doc.records.length!==shard.count) {
        throw new Error(baseDir+"/"+shard.path+": invalid runtime shard");
      }
      records.push(...doc.records);
    }
    return records;
  },
};

async function loadRuntime(manifest,baseDir) {
  const records=[];
  for (const shard of manifest.shards??[]) {
    const doc=await readJson(path.join(root,baseDir,shard.path));
    if (!Array.isArray(doc.records)||doc.records.length!==shard.count) {
      errors.push(baseDir+"/"+shard.path+": shard count mismatch");
      continue;
    }
    records.push(...doc.records);
  }
  if (records.length!==manifest.count) {
    errors.push(baseDir+": manifest count mismatch");
  }
  return records;
}

const dictionaryRecords=await loadRuntime(dictionaryManifest,path.join("shared","dictionary"));
const lexemes=dictionaryRecords.filter(record=>String(record.id??"").startsWith("lex.en."));
const senses=dictionaryRecords.filter(record=>String(record.id??"").startsWith("sense."));
const usages=dictionaryRecords.filter(record=>String(record.id??"").startsWith("usage."));
const topics=await loadRuntime(grammarManifest,path.join("shared","grammar"));
const sentenceRecords=await loadRuntime(sentenceManifest,path.join("shared","sentences"));
const examples=sentenceRecords.filter(record=>String(record.id??"").startsWith("sent."));
const exercises=sentenceRecords.filter(record=>String(record.id??"").startsWith("ex."));
const dialogues=sentenceRecords.filter(record=>String(record.id??"").startsWith("dlg."));
const commonMistakes=sentenceRecords.filter(record=>String(record.id??"").startsWith("err."));

if (dictionaryManifest.count!==900) errors.push("published dictionary runtime must contain 900 E03 records");
if (lexemes.length!==300||senses.length!==300||usages.length!==300) errors.push("published E03 runtime split must be 300 lexemes + 300 senses + 300 usages");
if (grammarManifest.count!==300) errors.push("published grammar runtime must contain 300 reviewed grammar topics");
if (sentenceManifest.count!==expectedSentenceManifestCount) errors.push("published sentence runtime must contain "+expectedSentenceManifestCount+" reviewed records");
if (topics.length!==300||examples.length!==expectedExampleCount||exercises.length!==expectedExerciseCount||dialogues.length!==expectedDialogueCount||commonMistakes.length!==expectedMistakesCount) {
  errors.push("published runtime split must be 300 topics + "+expectedExampleCount+" examples + "+expectedExerciseCount+" exercises + "+expectedDialogueCount+" dialogues + "+expectedMistakesCount+" common mistakes");
}
const tatoebaExamples=examples.filter(record=>String(record.id??"").startsWith("sent.tatoeba."));
const tatoebaTranslations=exercises.filter(record=>String(record.id??"").startsWith("ex.translation.tatoeba."));
if (tatoebaTranslations.length<19200) errors.push("published Tatoeba runtime must include at least 19200 reviewed translation pairs");
const exampleById=new Map();
const exampleCounts=new Map();
for (const record of examples) {
  exampleById.set(record.id,record);
  exampleCounts.set(record.id,(exampleCounts.get(record.id)||0)+1);
}
for (const controlled of tatoebaEnglishControlled) {
  const count=exampleCounts.get(controlled.id)||0;
  const match=exampleById.get(controlled.id);
  if (controlled.quality.state==="published") {
    if (count!==1||JSON.stringify(match)!==JSON.stringify(controlled)) errors.push(controlled.id+": runtime differs from digest-bound approved source");
  } else if (count!==0) errors.push(controlled.id+": unapproved source leaked into runtime");
}
const typingTextExamples=examples.filter(record=>String(record.id??"").startsWith("sent.tt."));
const typingTextCloze=exercises.filter(record=>String(record.id??"").startsWith("ex.cloze.tt."));
if (typingTextExamples.length!==expectedTypingTextExampleCount||typingTextCloze.length!==300) errors.push("published typing-text slices must expose "+expectedTypingTextExampleCount+" examples + 300 pilot cloze exercises");
const correctionExercises=exercises.filter(record=>record.type==="error-correction");
const transformationExercises=exercises.filter(record=>record.type==="transformation");
if (correctionExercises.length!==100||transformationExercises.length!==(100+e11TransformationsCount)) {
  errors.push("published E06 reviewed slice must expose 100 correction + "+(100+e11TransformationsCount)+" transformation exercises");
}

const senseIds=new Set(senses.map(record=>record.id));
const usageIds=new Set(usages.map(record=>record.id));
for (const record of [...lexemes,...senses,...usages]) {
  if (record.quality?.state!=="published") errors.push(record.id+": dictionary runtime record is not published");
  for (const [name,check] of Object.entries(record.quality?.checks??{})) {
    if (check?.status==="pending"||check?.status==="fail") errors.push(record.id+": unfinished dictionary quality check "+name+"="+check.status);
  }
}
for (const lexeme of lexemes) {
  if (!lexeme.vi||!lexeme.ipa||!lexeme.cefr) errors.push(lexeme.id+": published lexeme is missing vi/ipa/cefr");
  for (const id of lexeme.senseIds??[]) if (!senseIds.has(id)) errors.push(lexeme.id+": missing runtime sense "+id);
  if (!Array.isArray(lexeme.usageRefs)||lexeme.usageRefs.length!==1) errors.push(lexeme.id+": published lexeme must expose exactly one usageRef");
  for (const id of lexeme.usageRefs??[]) if (!usageIds.has(id)) errors.push(lexeme.id+": missing runtime usage "+id);
}
const topicIds=new Set(topics.map(record=>record.id));
const exampleIds=new Set(examples.map(record=>record.id));
const e03Examples=examples.filter(record=>String(record.id??"").startsWith("sent.e03."));
if (e03Examples.length!==13) errors.push("published E03 example enrichment must expose exactly 13 project-original examples");
for (const sense of senses) {
  if (!Array.isArray(sense.exampleIds)||sense.exampleIds.length===0) errors.push(sense.id+": published E03 sense is missing exampleIds");
  for (const id of sense.exampleIds??[]) if (!exampleIds.has(id)) errors.push(sense.id+": missing runtime example "+id);
}
for (const usage of usages) {
  if (!lexemes.some(lexeme=>lexeme.id===usage.targetId)) errors.push(usage.id+": unknown runtime usage target "+usage.targetId);
  if (!usage.explanationVi||!Array.isArray(usage.exampleIds)||usage.exampleIds.length===0) errors.push(usage.id+": runtime usage requires explanationVi + exampleIds");
  for (const id of usage.exampleIds??[]) if (!exampleIds.has(id)) errors.push(usage.id+": missing runtime example "+id);
}
const exerciseIds=new Set(exercises.map(record=>record.id));

for (const record of [...topics,...examples,...exercises,...dialogues,...commonMistakes]) {
  if (record.quality?.state!=="published") errors.push(record.id+": runtime record is not published");
  for (const [name,check] of Object.entries(record.quality?.checks??{})) {
    if (check?.status==="pending"||check?.status==="fail") {
      errors.push(record.id+": unfinished runtime quality check "+name+"="+check.status);
    }
  }
}
for (const topic of topics) {
  for (const id of topic.exampleIds??[]) if (!exampleIds.has(id)) errors.push(topic.id+": missing runtime example "+id);
  for (const id of topic.exerciseIds??[]) if (!exerciseIds.has(id)) errors.push(topic.id+": missing runtime exercise "+id);
}
for (const sentence of examples) {
  for (const id of sentence.grammarIds??[]) if (!topicIds.has(id)) errors.push(sentence.id+": missing runtime grammar "+id);
}
for (const exercise of exercises) {
  for (const id of exercise.sourceSentenceIds??[]) if (!exampleIds.has(id)) errors.push(exercise.id+": missing runtime source "+id);
  for (const id of exercise.targetIds??[]) if (id.startsWith("gr.")&&!topicIds.has(id)) errors.push(exercise.id+": missing runtime grammar target "+id);
}
for (const mistake of commonMistakes) {
  for (const id of mistake.targetIds??[]) if (id.startsWith("gr.")&&!topicIds.has(id)) errors.push(mistake.id+": missing runtime grammar target "+id);
  if (!Array.isArray(mistake.corrections)||mistake.corrections.length!==1) errors.push(mistake.id+": runtime common mistake requires one correction");
}

try {
  buildGameEnglishActivityDataset(
    "monkeytype","grammar-topic",topics.slice(0,2),"runtime-smoke-monkey-grammar",
    {createdAt:"2026-10-03T00:00:00.000Z"},
  );
  buildGameEnglishActivityDataset(
    "space-typing","grammar-challenge",topics.slice(0,2),"runtime-smoke-space-grammar",
    {createdAt:"2026-10-03T00:00:00.000Z"},
  );
  buildGameEnglishActivityDataset(
    "monkeytype","cloze",exercises.filter(record=>record.type==="cloze").slice(0,2),"runtime-smoke-monkey-cloze",
    {createdAt:"2026-10-03T00:00:00.000Z"},
  );
  buildGameEnglishActivityDataset(
    "monkeytype","translation",exercises.filter(record=>record.type==="translation").slice(0,2),"runtime-smoke-monkey-translation",
    {createdAt:"2026-10-03T00:00:00.000Z"},
  );
  buildGameEnglishActivityDataset(
    "monkeytype","error-correction",correctionExercises.slice(0,2),"runtime-smoke-monkey-correction",
    {createdAt:"2026-10-03T00:00:00.000Z"},
  );
  buildGameEnglishActivityDataset(
    "monkeytype","error-correction",commonMistakes.slice(0,2),"runtime-smoke-monkey-common-mistake",
    {createdAt:"2026-10-03T00:00:00.000Z"},
  );
  buildGameEnglishActivityDataset(
    "monkeytype","transformation",transformationExercises.slice(0,2),"runtime-smoke-monkey-transformation",
    {createdAt:"2026-10-03T00:00:00.000Z"},
  );
  buildGameEnglishActivityDataset(
    "karaoke-typing","dialogue",dialogues.slice(0,2),"runtime-smoke-karaoke-dialogue",
    {createdAt:"2026-10-03T00:00:00.000Z"},
  );
} catch (error) {
  errors.push("published runtime activity smoke failed: "+error.message);
}

let monkeyCorrectionCount = 0;
try {
  for (const [gameId,capability] of [["recall-typing","recall"],["vocab-shooter","shooter"],["space-typing","space"]]) {
    const vocabulary=await buildPublishedGameEnglishActivityDataset(
      fileRuntimeLoader,
      gameId,
      capability,
      "vocabulary",
      "runtime-source-"+gameId+"-vocabulary",
      {limit:5,createdAt:"2026-10-03T00:00:00.000Z"},
    );
    if (vocabulary.items.length!==5) errors.push(gameId+": published vocabulary source must return 5 items");
  }

  const spaceGrammar=await buildPublishedGameEnglishActivityDataset(
    fileRuntimeLoader,
    "space-typing",
    "space",
    "grammar-challenge",
    "runtime-source-space-grammar",
    {limit:5,createdAt:"2026-10-03T00:00:00.000Z"},
  );
  if(spaceGrammar.items.length!==5) {
    errors.push("published activity source must return 5 bounded Space grammar items");
  }

  const karaokeTranslation=await buildPublishedGameEnglishActivityDataset(
    fileRuntimeLoader,
    "karaoke-typing",
    "karaoke",
    "translation",
    "runtime-source-karaoke-translation",
    {limit:5,createdAt:"2026-10-03T00:00:00.000Z"},
  );
  if(karaokeTranslation.items.length!==5) {
    errors.push("published activity source must return 5 bounded Karaoke translation items");
  }

  monkeyCorrectionCount=await countPublishedEnglishActivityRecords(fileRuntimeLoader,"error-correction");
  if(monkeyCorrectionCount!==(100+expectedMistakesCount)) errors.push("published Monkeytype error-correction activity must expose 100 corrections + "+expectedMistakesCount+" common mistakes");
  const monkeyCorrection=await buildPublishedGameEnglishActivityDataset(
    fileRuntimeLoader,"monkeytype","monkeytype","error-correction","runtime-source-monkey-correction",
    {limit:5,createdAt:"2026-10-03T00:00:00.000Z"},
  );
  if(monkeyCorrection.items.length!==5) errors.push("published activity source must return 5 Monkeytype correction items");
  const monkeyTransformation=await buildPublishedGameEnglishActivityDataset(
    fileRuntimeLoader,"monkeytype","monkeytype","transformation","runtime-source-monkey-transformation",
    {limit:5,createdAt:"2026-10-03T00:00:00.000Z"},
  );
  if(monkeyTransformation.items.length!==5) errors.push("published activity source must return 5 Monkeytype transformation items");

  const karaokeExamples=await buildPublishedGameEnglishActivityDataset(
    fileRuntimeLoader,
    "karaoke-typing",
    "karaoke",
    "example-typing",
    "runtime-source-karaoke-examples",
    {limit:5,createdAt:"2026-10-03T00:00:00.000Z"},
  );
  if(karaokeExamples.items.length!==5) {
    errors.push("published activity source must return 5 bounded Karaoke example items");
  }

  const karaokeDialogueCount=await countPublishedEnglishActivityRecords(
    fileRuntimeLoader,
    "dialogue",
  );
  if(karaokeDialogueCount!==expectedDialogueCount) {
    errors.push("published Karaoke dialogue activity must expose "+expectedDialogueCount+" reviewed dialogues");
  }
  const karaokeDialogue=await buildPublishedGameEnglishActivityDataset(
    fileRuntimeLoader,
    "karaoke-typing",
    "karaoke",
    "dialogue",
    "runtime-source-karaoke-dialogue",
    {limit:3,createdAt:"2026-10-03T00:00:00.000Z"},
  );
  if(karaokeDialogue.items.length===0||karaokeDialogue.items.length>100) {
    errors.push("published activity source must return a bounded Karaoke dialogue dataset");
  }

  const recallCollocations=await countPublishedEnglishActivityRecords(
    fileRuntimeLoader,
    "collocation",
  );
  if(recallCollocations!==5000) {
    errors.push("published Recall collocation activity must expose 5000 reviewed records");
  }
  const recallDataset=await buildPublishedGameEnglishActivityDataset(
    fileRuntimeLoader,
    "recall-typing",
    "recall",
    "collocation",
    "runtime-source-recall-collocation",
    {limit:5,createdAt:"2026-10-03T00:00:00.000Z"},
  );
  if(recallDataset.items.length!==5) {
    errors.push("published activity source must return 5 bounded Recall collocation items");
  }

  const verbPatternCount=await countPublishedEnglishActivityRecords(fileRuntimeLoader,"verb-pattern");
  const phrasalVerbCount=await countPublishedEnglishActivityRecords(fileRuntimeLoader,"phrasal-verb");
  const chunkCount=await countPublishedEnglishActivityRecords(fileRuntimeLoader,"chunk");
  const idiomCount=await countPublishedEnglishActivityRecords(fileRuntimeLoader,"idiom");
  const sentenceBuildingCount=await countPublishedEnglishActivityRecords(fileRuntimeLoader,"sentence-building");
  const contextualUsageCount=await countPublishedEnglishActivityRecords(fileRuntimeLoader,"contextual-usage");
  const listeningExerciseCount=exercises.filter((r)=>r?.type==="listening-typing").length;
  if(verbPatternCount!==510) errors.push("published verb-pattern activity must expose 510 reviewed records");
  if(phrasalVerbCount!==1000) errors.push("published phrasal-verb activity must expose 1000 reviewed records");
  if(chunkCount!==2000) errors.push("published chunk activity must expose 2000 reviewed records");
  if(idiomCount!==1185) errors.push("published idiom activity must expose 1185 reviewed records");
  if(sentenceBuildingCount<2500) errors.push("published sentence-building activity must expose >= 2500 reviewed records");
  if(contextualUsageCount<2000) errors.push("published contextual-usage activity must expose >= 2000 reviewed records");
  if(listeningExerciseCount<1000) errors.push("published listening-typing exercises must expose >= 1000 reviewed records");
} catch (error) {
  errors.push("published activity source routing smoke failed: "+error.message);
}

const report={
  dictionaryLexemes:lexemes.length,
  dictionarySenses:senses.length,
  dictionaryUsages:usages.length,
  dictionaryManifestCount:dictionaryManifest.count,
  grammarTopics:topics.length,
  examples:examples.length,
  exercises:exercises.length,
  corrections:correctionExercises.length,
  transformations:transformationExercises.length,
  dialogues:dialogues.length,
  commonMistakes:commonMistakes.length,
  tatoebaExamples:tatoebaExamples.length,
  tatoebaTranslations:tatoebaTranslations.length,
  typingTextExamples:typingTextExamples.length,
  typingTextCloze:typingTextCloze.length,
  e11TypingTextExpansionCount,
  grammarManifestCount:grammarManifest.count,
  sentenceManifestCount:sentenceManifest.count,
  runtimeActivitySource:{
    recallVocabulary:5,
    shooterVocabulary:5,
    spaceVocabulary:5,
    spaceGrammar:5,
    karaokeTranslation:5,
    monkeyCorrection:5,
    monkeyCorrectionRecords:monkeyCorrectionCount,
    monkeyTransformation:5,
    karaokeExamples:5,
    karaokeDialogues:dialogues.length,
    recallCollocations:560,
    verbPatterns:510,
    phrasalVerbs:280,
    chunks:155,
    idioms:125,
    sentenceBuilding:2500,
    contextualUsage:2000,
    listeningTypingExercises:1000,
  },
};
console.log(JSON.stringify(report,null,2));
if (errors.length) {
  console.error(errors.join("\n"));
  process.exitCode=1;
}
