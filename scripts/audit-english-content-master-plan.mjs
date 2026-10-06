import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { ENGLISH_CONTENT_CAPABILITIES } from "../shared/english-content/capabilities.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const levels=["A1","A2","B1","B2","C1","C2"];
const grammarTargets={A1:45,A2:50,B1:60,B2:60,C1:50,C2:35};

async function readJson(file){
  return JSON.parse(await fs.readFile(file,"utf8"));
}
async function loadDataset(name){
  const base=path.join(root,"shared",name);
  const manifest=await readJson(path.join(base,"manifest.json"));
  const groups={};
  for(const shard of manifest.shards??[]){
    const group=String(shard.path).split("/")[0];
    const doc=await readJson(path.join(base,shard.path));
    if(!Array.isArray(doc.records)) throw new Error(name+"/"+shard.path+" must contain records[]");
    (groups[group]??=[]).push(...doc.records);
  }
  return {manifest,groups,records:Object.values(groups).flat()};
}
async function loadCurriculum(){
  const base=path.join(root,"shared","curriculum");
  const manifest=await readJson(path.join(base,"manifest.json"));
  const topicIds=[];
  for(const shard of manifest.shards??[]){
    const doc=await readJson(path.join(base,shard.path));
    if(!Array.isArray(doc.topicIds)) throw new Error("curriculum/"+shard.path+" must contain topicIds[]");
    topicIds.push(...doc.topicIds);
  }
  return {manifest,topicIds};
}
function countBy(records,keyFn){
  const out={};
  for(const record of records){
    const key=keyFn(record);
    if(key===undefined||key===null||key==="") continue;
    out[key]=(out[key]??0)+1;
  }
  return out;
}
function recordId(record){
  return String(record?.id??record?.lexemeId??"<unknown>");
}
function hasText(value){
  return typeof value==="string"&&value.trim()!=="";
}
function noExamples(record){
  return !Array.isArray(record?.exampleIds)||record.exampleIds.length===0;
}
function addCheck(errors,condition,message){
  if(!condition) errors.push(message);
}

const [dictionary,grammar,sentences,phrases,curriculum,release]=await Promise.all([
  loadDataset("dictionary"),
  loadDataset("grammar"),
  loadDataset("sentences"),
  loadDataset("phrases"),
  loadCurriculum(),
  readJson(path.join(root,"content","english","releases","2026.10.0.json")),
]);
const lexemes=dictionary.groups.lexemes??[];
const senses=dictionary.groups.senses??[];
const topics=grammar.groups.topics??[];
const examples=sentences.groups.examples??[];
const exercises=sentences.groups.exercises??[];
const dialogues=sentences.groups.dialogues??[];
const mistakes=sentences.groups.mistakes??[];
const collocations=phrases.groups.collocations??[];
const verbPatterns=phrases.groups["verb-patterns"]??[];
const phraseItems=phrases.groups.items??[];
const phrasalVerbs=phraseItems.filter(record=>record.type==="phrasal-verb");
const chunks=phraseItems.filter(record=>record.type==="chunk");
const idioms=phraseItems.filter(record=>record.type==="idiom");
const exerciseByType=countBy(exercises,record=>record.type);
const topicsByCefr=Object.fromEntries(levels.map(level=>[level,topics.filter(topic=>topic.cefr===level).length]));
const allRuntime=[...dictionary.records,...grammar.records,...sentences.records,...phrases.records];

const publishedStateCounts=countBy(allRuntime,record=>record?.quality?.state);
const unfinishedPublishedChecks=[];
const missingProvenance=[];
const missingSourceLicense=[];
for(const record of allRuntime){
  if(record?.quality?.state==="published"){
    for(const [name,check] of Object.entries(record?.quality?.checks??{})){
      if(check?.status!=="pass"&&check?.status!=="not-applicable"){
        unfinishedPublishedChecks.push(recordId(record)+":"+name+":"+String(check?.status));
      }
    }
  }
  if(record?.quality!==undefined){
    const sources=record?.provenance?.sources;
    if(!Array.isArray(sources)||sources.length===0){
      missingProvenance.push(recordId(record));
    }else{
      for(const source of sources){
        if(!hasText(source?.license)) missingSourceLicense.push(recordId(record)+":"+String(source?.dataset??"source"));
      }
    }
  }
}

const lexemeIds=new Set(lexemes.map(record=>record.id));
const senseIds=new Set(senses.map(record=>record.id));
const lexemesWithoutSenses=lexemes.filter(record=>!Array.isArray(record.senseIds)||record.senseIds.length===0||record.senseIds.some(id=>!senseIds.has(id)));
const sensesWithoutLexeme=senses.filter(record=>!lexemeIds.has(record.lexemeId));
const sensesWithoutVi=senses.filter(record=>!hasText(record.explanationVi));
const lexemesWithoutMorphology=lexemes.filter(record=>!Array.isArray(record.forms)||record.forms.length===0||!Array.isArray(record.partsOfSpeech)||record.partsOfSpeech.length===0);
const lexemesWithoutUsageRefs=lexemes.filter(record=>!Array.isArray(record.usageRefs)||record.usageRefs.length===0);
const sensesWithoutExamples=senses.filter(noExamples);
const collocationsWithoutExamples=collocations.filter(noExamples);
const verbPatternsWithoutExamples=verbPatterns.filter(noExamples);
const phrasesWithoutExamples=phraseItems.filter(noExamples);
const phrasalMissingMetadata=phrasalVerbs.filter(record=>!hasText(record.separability)||!hasText(record.transitivity));
const grammarIds=new Set(topics.map(record=>record.id));
const curriculumIds=new Set(curriculum.topicIds);
const grammarMissingFromCurriculum=[...grammarIds].filter(id=>!curriculumIds.has(id));
const curriculumMissingRuntime=[...curriculumIds].filter(id=>!grammarIds.has(id));
const topicsWithoutExamples=topics.filter(record=>!Array.isArray(record.exampleIds)||record.exampleIds.length===0);
const topicsWithoutExercises=topics.filter(record=>!Array.isArray(record.exerciseIds)||record.exerciseIds.length===0);

const requiredCapabilities={
  monkeytype:["grammar-topic","example-typing","translation","cloze","error-correction","sentence-building","transformation","listening-typing","contextual-usage","collocation","verb-pattern","phrasal-verb","idiom","chunk"],
  recall:["vocabulary","collocation","phrasal-verb","chunk","listening-typing","contextual-usage"],
  shooter:["vocabulary","collocation","phrasal-verb","chunk","contextual-usage"],
  karaoke:["example-typing","dialogue","listening-typing","translation"],
  space:["vocabulary","collocation","phrasal-verb","chunk","grammar-challenge","contextual-usage"],
};
const missingCapabilities={};
for(const [game,required] of Object.entries(requiredCapabilities)){
  const actual=new Set(ENGLISH_CONTENT_CAPABILITIES[game]??[]);
  const missing=required.filter(activity=>!actual.has(activity));
  if(missing.length) missingCapabilities[game]=missing;
}

const versions={
  release:release.contentVersion,
  dictionary:dictionary.manifest.contentVersion,
  grammar:grammar.manifest.contentVersion,
  sentences:sentences.manifest.contentVersion,
  phrases:phrases.manifest.contentVersion,
  curriculum:curriculum.manifest.contentVersion,
};
const errors=[];
const warnings=[];
const uniqueVersions=new Set(Object.values(versions));
addCheck(errors,uniqueVersions.size===1,"Runtime manifests and release must use one contentVersion");
addCheck(errors,lexemes.length>=300,"E03 requires at least 300 published rich lexemes; got "+lexemes.length);
addCheck(errors,senses.length>=300,"E03 requires at least 300 published senses; got "+senses.length);
addCheck(errors,lexemesWithoutSenses.length===0,"E03 has lexemes with missing/broken sense links: "+lexemesWithoutSenses.length);
addCheck(errors,sensesWithoutLexeme.length===0,"E03 has senses with missing lexeme links: "+sensesWithoutLexeme.length);
addCheck(errors,sensesWithoutVi.length===0,"E03 has senses without Vietnamese explanation: "+sensesWithoutVi.length);
addCheck(errors,lexemesWithoutMorphology.length===0,"E03 has lexemes without POS/forms morphology coverage: "+lexemesWithoutMorphology.length);
addCheck(errors,sensesWithoutExamples.length===0,"E03 has senses without reviewed example links: "+sensesWithoutExamples.length);
addCheck(errors,topics.length===300,"E05 requires exactly 300 published grammar topics; got "+topics.length);
for(const level of levels) addCheck(errors,topicsByCefr[level]===grammarTargets[level],"E05 "+level+" coverage must be "+grammarTargets[level]+"; got "+topicsByCefr[level]);
addCheck(errors,grammarMissingFromCurriculum.length===0,"Published grammar topics missing from curriculum: "+grammarMissingFromCurriculum.length);
addCheck(errors,curriculumMissingRuntime.length===0,"Curriculum topics missing from published grammar runtime: "+curriculumMissingRuntime.length);
addCheck(errors,collocations.length>=100,"E04 requires at least 100 collocations; got "+collocations.length);
addCheck(errors,verbPatterns.length>=50,"E04 requires at least 50 verb patterns; got "+verbPatterns.length);
addCheck(errors,phrasalVerbs.length>=50,"E04 requires at least 50 phrasal verbs; got "+phrasalVerbs.length);
addCheck(errors,chunks.length+idioms.length>=50,"E04 requires at least 50 chunks/idioms; got "+(chunks.length+idioms.length));
addCheck(errors,phrasalMissingMetadata.length===0,"E04 phrasal verbs missing transitivity/separability metadata: "+phrasalMissingMetadata.length);
addCheck(errors,examples.length>=1000,"E06 requires at least 1000 published examples; got "+examples.length);
addCheck(errors,(exerciseByType.translation??0)>=300,"E06 requires at least 300 translation exercises; got "+(exerciseByType.translation??0));
addCheck(errors,(exerciseByType.cloze??0)>=300,"E06 requires at least 300 cloze exercises; got "+(exerciseByType.cloze??0));
addCheck(errors,(exerciseByType["error-correction"]??0)>=100,"E06 requires at least 100 correction exercises; got "+(exerciseByType["error-correction"]??0));
addCheck(errors,(exerciseByType.transformation??0)>=100,"E06 requires at least 100 transformation exercises; got "+(exerciseByType.transformation??0));
addCheck(errors,dialogues.length>=100,"E06 requires at least 100 dialogues; got "+dialogues.length);
addCheck(errors,unfinishedPublishedChecks.length===0,"Published runtime has unfinished quality checks: "+unfinishedPublishedChecks.length);
addCheck(errors,missingProvenance.length===0,"Published/runtime content has missing provenance: "+missingProvenance.length);
addCheck(errors,missingSourceLicense.length===0,"Published/runtime content has provenance sources without licenses: "+missingSourceLicense.length);
addCheck(errors,Object.keys(missingCapabilities).length===0,"E07-E09 capability matrix is incomplete");

if(lexemesWithoutUsageRefs.length) warnings.push("Lexemes without usageRefs: "+lexemesWithoutUsageRefs.length);
if(collocationsWithoutExamples.length) warnings.push("Collocations without exampleIds: "+collocationsWithoutExamples.length);
if(verbPatternsWithoutExamples.length) warnings.push("Verb patterns without exampleIds: "+verbPatternsWithoutExamples.length);
if(phrasesWithoutExamples.length) warnings.push("Phrase items without exampleIds: "+phrasesWithoutExamples.length);
if(topicsWithoutExamples.length) warnings.push("Grammar topics without exampleIds: "+topicsWithoutExamples.length);
if(topicsWithoutExercises.length) warnings.push("Grammar topics without exerciseIds: "+topicsWithoutExercises.length);

const report={
  schemaVersion:1,
  contentVersion:release.contentVersion,
  status:errors.length===0?"pass":"fail",
  versions,
  runtimeCounts:{
    dictionary:dictionary.manifest.count,
    grammar:grammar.manifest.count,
    sentences:sentences.manifest.count,
    phrases:phrases.manifest.count,
    curriculum:curriculum.manifest.count,
  },
  e03:{
    lexemes:lexemes.length,
    senses:senses.length,
    lexemesWithoutSenses:lexemesWithoutSenses.length,
    sensesWithoutLexeme:sensesWithoutLexeme.length,
    sensesWithoutVietnameseExplanation:sensesWithoutVi.length,
    lexemesWithoutMorphology:lexemesWithoutMorphology.length,
    lexemesWithoutUsageRefs:lexemesWithoutUsageRefs.length,
    sensesWithoutExamples:sensesWithoutExamples.length,
  },
  e04:{
    collocations:collocations.length,
    verbPatterns:verbPatterns.length,
    phrasalVerbs:phrasalVerbs.length,
    chunks:chunks.length,
    idioms:idioms.length,
    phrasalVerbsMissingMetadata:phrasalMissingMetadata.length,
    collocationsWithoutExamples:collocationsWithoutExamples.length,
    verbPatternsWithoutExamples:verbPatternsWithoutExamples.length,
    phraseItemsWithoutExamples:phrasesWithoutExamples.length,
  },
  e05:{topics:topics.length,topicsByCefr,grammarMissingFromCurriculum:grammarMissingFromCurriculum.length,curriculumMissingRuntime:curriculumMissingRuntime.length},
  e06:{examples:examples.length,exercises:exercises.length,exerciseByType,dialogues:dialogues.length,mistakes:mistakes.length},
  e07to09:{capabilities:ENGLISH_CONTENT_CAPABILITIES,missingCapabilities},
  quality:{stateCounts:publishedStateCounts,unfinishedPublishedChecks:unfinishedPublishedChecks.length,missingProvenance:missingProvenance.length,missingSourceLicense:missingSourceLicense.length},
  warnings,
  errors,
};
await fs.mkdir(path.join(root,"content","english","reports"),{recursive:true});
await fs.writeFile(path.join(root,"content","english","reports","master-plan-acceptance.json"),JSON.stringify(report,null,2)+"\n","utf8");
console.log(JSON.stringify(report,null,2));
if(errors.length){
  console.error("\nMaster-plan acceptance failures:\n"+errors.map(error=>"- "+error).join("\n"));
  process.exitCode=1;
}
