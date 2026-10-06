import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { normalizeSentenceKey } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");

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
  return {manifest,groups};
}
function add(map,key,value){
  if(typeof key!=="string"||key==="") return;
  const values=map.get(key)??[];
  if(!values.includes(value)) values.push(value);
  map.set(key,values);
}
function boundedContains(sentence,needle){
  const sentenceKey=normalizeSentenceKey(sentence);
  const needleKey=normalizeSentenceKey(needle);
  if(!needleKey) return false;
  return (" "+sentenceKey+" ").includes(" "+needleKey+" ");
}
function summarize(records,candidatesById){
  const withCandidates=records.filter(record=>(candidatesById.get(record.id)?.length??0)>0);
  const withoutCandidates=records.filter(record=>(candidatesById.get(record.id)?.length??0)===0);
  return {
    total:records.length,
    withCandidates:withCandidates.length,
    withoutCandidates:withoutCandidates.length,
    coverage:records.length===0?1:Number((withCandidates.length/records.length).toFixed(4)),
    sampleMatched:withCandidates.slice(0,10).map(record=>({id:record.id,exampleIds:candidatesById.get(record.id).slice(0,5)})),
    sampleMissing:withoutCandidates.slice(0,25).map(record=>record.id),
  };
}

const [dictionary,sentences,phrases]=await Promise.all([
  loadDataset("dictionary"),
  loadDataset("sentences"),
  loadDataset("phrases"),
]);
const lexemes=dictionary.groups.lexemes??[];
const senses=dictionary.groups.senses??[];
const examples=(sentences.groups.examples??[]).filter(record=>record?.quality?.state==="published");
const collocations=phrases.groups.collocations??[];
const verbPatterns=phrases.groups["verb-patterns"]??[];
const phraseItems=phrases.groups.items??[];

const examplesByLexeme=new Map();
for(const example of examples){
  for(const lexicalId of example.lexicalIds??[]) add(examplesByLexeme,lexicalId,example.id);
}
const lexemeCandidates=new Map();
for(const lexeme of lexemes) lexemeCandidates.set(lexeme.id,(examplesByLexeme.get(lexeme.id)??[]).slice(0,5));
const senseCandidates=new Map();
for(const sense of senses) senseCandidates.set(sense.id,(examplesByLexeme.get(sense.lexemeId)??[]).slice(0,5));

const missingLexemes=lexemes.filter(record=>(lexemeCandidates.get(record.id)?.length??0)===0);
const fallbackHeadwordEvidence=missingLexemes.map(lexeme=>({
  id:lexeme.id,
  headword:lexeme.headword,
  vi:lexeme.vi,
  cefr:lexeme.cefr,
  senseIds:lexeme.senseIds,
  candidates:examples
    .filter(example=>boundedContains(example.text,lexeme.headword))
    .slice(0,10)
    .map(example=>({id:example.id,text:example.text,cefr:example.cefr,lexicalIds:example.lexicalIds??[]})),
}));

const collocationCandidates=new Map();
for(const record of collocations){
  const matches=[];
  for(const example of examples){
    if(boundedContains(example.text,record.text)) matches.push(example.id);
    if(matches.length===5) break;
  }
  collocationCandidates.set(record.id,matches);
}
const phraseCandidates=new Map();
for(const record of phraseItems){
  const matches=[];
  for(const example of examples){
    if(boundedContains(example.text,record.text)) matches.push(example.id);
    if(matches.length===5) break;
  }
  phraseCandidates.set(record.id,matches);
}
const verbPatternLemmaCandidates=new Map();
for(const record of verbPatterns){
  const matches=[];
  for(const example of examples){
    if(boundedContains(example.text,record.lemma)) matches.push(example.id);
    if(matches.length===5) break;
  }
  verbPatternLemmaCandidates.set(record.id,matches);
}

const report={
  schemaVersion:1,
  contentVersion:dictionary.manifest.contentVersion,
  method:{
    lexemeAndSense:"explicit published sentence.lexicalIds only",
    fallbackLexemeEvidence:"whole-headword boundary match for manual review only",
    collocationAndPhrase:"normalized whole-phrase boundary match against published examples",
    verbPattern:"lemma-only candidate discovery; NOT safe for automatic linking without frame review",
  },
  examplesScanned:examples.length,
  lexemes:summarize(lexemes,lexemeCandidates),
  senses:summarize(senses,senseCandidates),
  e03FallbackHeadwordEvidence:fallbackHeadwordEvidence,
  collocations:summarize(collocations,collocationCandidates),
  phraseItems:summarize(phraseItems,phraseCandidates),
  verbPatternsLemmaEvidence:summarize(verbPatterns,verbPatternLemmaCandidates),
};
await fs.mkdir(path.join(root,"content","english","reports"),{recursive:true});
await fs.writeFile(path.join(root,"content","english","reports","enrichment-link-evidence.json"),JSON.stringify(report,null,2)+"\n","utf8");
console.log(JSON.stringify(report,null,2));
