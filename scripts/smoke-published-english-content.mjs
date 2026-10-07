import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson } from "./english-content-core.mjs";
import { buildGameEnglishActivityDataset } from "../shared/english-content/game-adapters.mjs";
import {
  buildPublishedGameEnglishActivityDataset,
  countPublishedEnglishActivityRecords,
} from "../shared/english-content/activity-source.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const [dictionaryManifest,grammarManifest,sentenceManifest]=await Promise.all([
  readJson(path.join(root,"shared","dictionary","manifest.json")),
  readJson(path.join(root,"shared","grammar","manifest.json")),
  readJson(path.join(root,"shared","sentences","manifest.json")),
]);
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
if (sentenceManifest.count!==3401) errors.push("published sentence runtime must contain 3401 reviewed records");
if (topics.length!==300||examples.length!==1513||exercises.length!==1400||dialogues.length!==100||commonMistakes.length!==388) {
  errors.push("published runtime split must be 300 topics + 1513 examples + 1400 exercises + 100 dialogues + 388 common mistakes");
}
const tatoebaExamples=examples.filter(record=>String(record.id??"").startsWith("sent.tatoeba."));
const tatoebaTranslations=exercises.filter(record=>String(record.id??"").startsWith("ex.translation.tatoeba."));
if (tatoebaExamples.length!==300||tatoebaTranslations.length!==300) errors.push("published Tatoeba slices must expose 300 sentences + 300 translations");
const typingTextExamples=examples.filter(record=>String(record.id??"").startsWith("sent.tt."));
const typingTextCloze=exercises.filter(record=>String(record.id??"").startsWith("ex.cloze.tt."));
if (typingTextExamples.length!==300||typingTextCloze.length!==300) errors.push("published typing-text slice must expose 300 examples + 300 cloze exercises");
const correctionExercises=exercises.filter(record=>record.type==="error-correction");
const transformationExercises=exercises.filter(record=>record.type==="transformation");
if (correctionExercises.length!==100||transformationExercises.length!==100) {
  errors.push("published E06 reviewed slice must expose 100 correction + 100 transformation exercises");
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

  const monkeyCorrectionCount=await countPublishedEnglishActivityRecords(fileRuntimeLoader,"error-correction");
  if(monkeyCorrectionCount!==488) errors.push("published Monkeytype error-correction activity must expose 100 corrections + 388 common mistakes");
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
  if(karaokeDialogueCount!==100) {
    errors.push("published Karaoke dialogue activity must expose 100 reviewed dialogues");
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
  if(recallCollocations!==1680) {
    errors.push("published Recall collocation activity must expose 1680 reviewed records");
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
  if(verbPatternCount!==510) errors.push("published verb-pattern activity must expose 510 reviewed records");
  if(phrasalVerbCount!==300) errors.push("published phrasal-verb activity must expose 300 reviewed records");
  if(chunkCount!==165) errors.push("published chunk activity must expose 165 reviewed records");
  if(idiomCount!==135) errors.push("published idiom activity must expose 135 reviewed records");
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
  grammarManifestCount:grammarManifest.count,
  sentenceManifestCount:sentenceManifest.count,
  runtimeActivitySource:{
    recallVocabulary:5,
    shooterVocabulary:5,
    spaceVocabulary:5,
    spaceGrammar:5,
    karaokeTranslation:5,
    monkeyCorrection:5,
    monkeyCorrectionRecords:488,
    monkeyTransformation:5,
    karaokeExamples:5,
    karaokeDialogues:100,
    recallCollocations:560,
    verbPatterns:510,
    phrasalVerbs:280,
    chunks:155,
    idioms:125,
  },
};
console.log(JSON.stringify(report,null,2));
if (errors.length) {
  console.error(errors.join("\n"));
  process.exitCode=1;
}
