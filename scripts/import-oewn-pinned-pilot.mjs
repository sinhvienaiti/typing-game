import fs from "node:fs/promises";
import path from "node:path";
import { execFileSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";
import { normalizeOewnLemma, OEWN_LEXFILE_NAMES, parseOewnEntryYaml, parseOewnSynsetYaml } from "./oewn-pinned-core.mjs";

const EXPECTED_COMMIT="dc343f2683279ecbb13fab4e2fd778d7b162d287";
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const args=new Map(process.argv.slice(2).filter(v=>v.startsWith("--")).map(raw=>{
  const i=raw.indexOf("="); return i<0?[raw,"true"]:[raw.slice(0,i),raw.slice(i+1)];
}));
const sourceDir=path.resolve(root,args.get("--source-dir")??".cache/english-content/oewn");
const output=path.resolve(root,args.get("--output")??"content/english/review-queues/oewn-2025-pilot.json");
const yamlDir=path.join(sourceDir,"src","yaml");

let sourceCommit;
try { sourceCommit=execFileSync("git",["-C",sourceDir,"rev-parse","HEAD"],{encoding:"utf8"}).trim(); }
catch { throw new Error("OEWN source checkout is missing or is not a Git checkout: "+sourceDir); }
if (sourceCommit!==EXPECTED_COMMIT) throw new Error("OEWN source commit mismatch. Expected "+EXPECTED_COMMIT+", got "+sourceCommit);

const [seedDoc,level1,level2]=await Promise.all([
  readJson(path.join(root,"content","english","dictionary","lexeme-seed-pilot.json")),
  readJson(path.join(root,"shared","vocabulary","levels","001.json")),
  readJson(path.join(root,"shared","vocabulary","levels","002.json"))
]);
if (!Array.isArray(seedDoc.records)||seedDoc.records.length!==300) throw new Error("Expected exactly 300 lexeme pilot seeds");
const legacyByKey=new Map([...level1.entries,...level2.entries].map(entry=>[normalizeOewnLemma(entry.en),entry]));
const targetKeys=new Set(seedDoc.records.map(record=>record.headwordKey));
const entryMaps=new Map();
const entryFiles=new Map();
for (const key of targetKeys) {
  const first=key[0]?.toLowerCase();
  if (!/^[a-z]$/.test(first)) continue;
  if (!entryFiles.has(first)) entryFiles.set(first,new Set());
  entryFiles.get(first).add(key);
}
for (const [letter,keys] of [...entryFiles].sort(([a],[b])=>a.localeCompare(b))) {
  const file=path.join(yamlDir,"entries-"+letter+".yaml");
  const parsed=parseOewnEntryYaml(await fs.readFile(file,"utf8"),keys);
  for (const [key,value] of parsed) entryMaps.set(key,{...value,sourceFile:path.relative(sourceDir,file)});
}

const wantedByLexFile=new Map();
for (const value of entryMaps.values()) {
  for (const part of Object.values(value.parts)) {
    for (const sense of part.senses) {
      if (!Number.isInteger(sense.lexFileNumber)||!OEWN_LEXFILE_NAMES[sense.lexFileNumber]) continue;
      if (!wantedByLexFile.has(sense.lexFileNumber)) wantedByLexFile.set(sense.lexFileNumber,new Set());
      wantedByLexFile.get(sense.lexFileNumber).add(sense.synsetId);
    }
  }
}
const synsets=new Map();
for (const [lexFileNumber,ids] of [...wantedByLexFile].sort(([a],[b])=>a-b)) {
  const name=OEWN_LEXFILE_NAMES[lexFileNumber];
  const file=path.join(yamlDir,name);
  const parsed=parseOewnSynsetYaml(await fs.readFile(file,"utf8"),ids);
  for (const [id,value] of parsed) synsets.set(id,{...value,sourceFile:path.relative(sourceDir,file)});
}

const records=[],misses=[],sourceErrors=[];
for (const seed of seedDoc.records) {
  const entry=entryMaps.get(seed.headwordKey);
  const legacy=legacyByKey.get(seed.headwordKey);
  if (!entry) {
    misses.push({lexemeId:seed.id,headword:seed.headword,headwordKey:seed.headwordKey,reason:"entry-not-found"});
    continue;
  }
  const parts=[];
  for (const [partOfSpeech,data] of Object.entries(entry.parts)) {
    const senses=[];
    for (const sense of data.senses) {
      const synset=synsets.get(sense.synsetId);
      if (!synset) {
        sourceErrors.push({lexemeId:seed.id,senseId:sense.senseId,synsetId:sense.synsetId,message:"synset-not-found"});
        continue;
      }
      senses.push({
        senseId:sense.senseId,
        synsetId:sense.synsetId,
        lexFileNumber:sense.lexFileNumber,
        definitionEn:synset.definitions,
        explanationVi:null,
        sourceExamples:synset.examples,
        memberLemmas:synset.members,
        ili:synset.ili,
        sourceFile:synset.sourceFile
      });
    }
    parts.push({partOfSpeech,forms:data.forms,pronunciations:data.pronunciations,senses});
  }
  records.push({
    lexemeId:seed.id,
    legacyVocabularyRefs:seed.legacyVocabularyRefs,
    headword:seed.headword,
    headwordKey:seed.headwordKey,
    legacyVi:legacy?.vi??null,
    legacyIpa:legacy?.ipa??null,
    sourceEntryFile:entry.sourceFile,
    parts,
    quality:{
      state:"candidate",
      checks:{
        sourcePin:{status:"pass",method:"git-commit-sha"},
        sourceParse:{status:"pass",method:"oewn-yaml-parser-v1"},
        vietnameseSense:{status:"pending",method:"bilingual-review-required"},
        cefr:{status:"pending",method:"cefr-review-required"},
        naturalness:{status:"pending",method:"sense-selection-review-required"}
      }
    }
  });
}
const totalSenses=records.reduce((sum,record)=>sum+record.parts.reduce((partSum,part)=>partSum+part.senses.length,0),0);
const sensesWithDefinitions=records.reduce((sum,record)=>sum+record.parts.reduce((partSum,part)=>partSum+part.senses.filter(sense=>sense.definitionEn.length>0).length,0),0);
const result={
  schemaVersion:1,
  source:"oewn",
  release:"2025-edition",
  sourceRepository:"globalwordnet/english-wordnet",
  sourceCommit,
  publicationAllowed:false,
  records,
  misses,
  sourceErrors,
  metrics:{
    requested:seedDoc.records.length,
    mapped:records.length,
    mappedRate:Number((records.length/seedDoc.records.length).toFixed(4)),
    totalSenses,
    sensesWithDefinitions,
    definitionRate:totalSenses===0?0:Number((sensesWithDefinitions/totalSenses).toFixed(4)),
    withPronunciation:records.filter(record=>record.parts.some(part=>part.pronunciations.length>0)).length,
    withMorphology:records.filter(record=>record.parts.some(part=>part.forms.length>0)).length,
    withSourceExamples:records.filter(record=>record.parts.some(part=>part.senses.some(sense=>sense.sourceExamples.length>0))).length
  }
};
await fs.mkdir(path.dirname(output),{recursive:true});
await fs.writeFile(output,stableJson(result),"utf8");
console.log("Pinned OEWN E03:",JSON.stringify(result.metrics),"=>",path.relative(root,output));
if (sourceErrors.length>0) process.exitCode=1;
