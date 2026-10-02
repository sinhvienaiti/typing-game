import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  lexicalTokens,
  normalizeEnglishKey,
  normalizeSentenceKey,
  readJson,
  stableJson,
} from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const sentenceLimit=1000;
const exerciseLimit=300;
const outDir=path.join(root,"content","english","review-queues");
const sentenceOutput=path.join(outDir,"typing-text-e06-sentences.json");
const exerciseOutput=path.join(outDir,"typing-text-e06-exercises.json");

function sentenceChunks(text) {
  return String(text)
    .normalize("NFC")
    .match(/[^.!?]+(?:[.!?]+|$)/gu)
    ?.map(value=>value.trim())
    .filter(Boolean)??[];
}
function escapeRegExp(value) {
  return value.replace(/[|\\{}()[\]^$+*?.-]/g,"\\$&");
}
function targetMatch(text,target) {
  const escaped=escapeRegExp(target).replace(/\s+/g,"\\s+");
  const regex=new RegExp("(^|[^\\p{L}\\p{N}])("+escaped+")(?=$|[^\\p{L}\\p{N}])","iu");
  const match=regex.exec(text);
  if (!match) return null;
  const prefix=match[1]??"";
  const value=match[2]??"";
  const start=match.index+prefix.length;
  return {start,end:start+value.length,value};
}
function unique(values) {
  return [...new Set(values.filter(Boolean))];
}
function quality() {
  return {
    state:"candidate",
    checks:{
      schema:{status:"pass",method:"typing-text-e06-generator-v1"},
      sourceText:{status:"pass",method:"project-typing-text-source"},
      targetPresence:{status:"pass",method:"whole-phrase-boundary-v1"},
      exactDuplicate:{status:"pass",method:"normalized-sentence-key-v1"},
      naturalness:{status:"pending",method:"sampled-editor-review-required"},
      cefr:{status:"pending",method:"cefr-review-required"}
    }
  };
}
function provenance(file,passageId,sentenceIndex) {
  return {
    sources:[{
      dataset:"project-original",
      sourceId:passageId+":sentence:"+String(sentenceIndex+1),
      sourceUrl:"shared/typing-texts/"+file,
      snapshot:"2026-10",
      license:"LicenseRef-Project-Original",
      modified:false
    }],
    note:"Derived deterministically from existing project-authored typing-text passages; sentence text is not rewritten."
  };
}

const [index,registry]=await Promise.all([
  readJson(path.join(root,"shared","typing-texts","index.json")),
  readJson(path.join(root,"content","english","id-registry.json"))
]);
const lexemeByKey=new Map(
  Object.entries(registry.entries??{})
    .filter(([key,id])=>key.startsWith("lex:")&&String(id).startsWith("lex.en."))
    .map(([key,id])=>[key.slice(4),id])
);
const targetKeys=[...lexemeByKey.keys()].sort((a,b)=>
  b.split(" ").length-a.split(" ").length||b.length-a.length||a.localeCompare(b)
);

const candidates=[];
const seenText=new Set();
for (const levelMeta of index.levels??[]) {
  const file=String(levelMeta.file);
  const doc=await readJson(path.join(root,"shared","typing-texts",file));
  for (const passage of doc.passages??[]) {
    const passageTargets=new Set(
      (passage.targetWords??[]).map(normalizeEnglishKey).filter(key=>lexemeByKey.has(key))
    );
    const allowedTargets=targetKeys.filter(key=>passageTargets.has(key));
    const sentences=sentenceChunks(passage.text);
    for (let sentenceIndex=0;sentenceIndex<sentences.length;sentenceIndex++) {
      const text=sentences[sentenceIndex];
      const tokenCount=lexicalTokens(text).length;
      if (tokenCount<5||tokenCount>40) continue;
      const textKey=normalizeSentenceKey(text);
      if (seenText.has(textKey)) continue;
      const matches=[];
      for (const target of allowedTargets) {
        const match=targetMatch(text,target);
        if (match) matches.push({target,lexemeId:lexemeByKey.get(target),...match});
      }
      seenText.add(textKey);
      const sourceStem=String(passage.id).toLocaleLowerCase("en-US");
      const sentenceId="sent.tt."+sourceStem+"."+String(sentenceIndex+1).padStart(3,"0");
      const lexicalIds=unique(matches.map(item=>item.lexemeId));
      const contexts=unique([passage.topic,passage.style,passage.setting,passage.tone]).slice(0,8);
      candidates.push({
        record:{
          schemaVersion:1,
          id:sentenceId,
          text,
          cefr:doc.cefr,
          contexts,
          register:["neutral"],
          ...(lexicalIds.length===0?{}:{lexicalIds}),
          quality:quality(),
          provenance:provenance(file,passage.id,sentenceIndex)
        },
        level:doc.level,
        passageId:passage.id,
        sentenceIndex,
        matches
      });
    }
  }
}
if (candidates.length<sentenceLimit) {
  throw new Error("Typing-text corpus produced only "+candidates.length+" unique training sentences; need "+sentenceLimit);
}
const targetBearing=candidates.filter(candidate=>candidate.matches.length>0);
if (targetBearing.length<exerciseLimit) {
  throw new Error("Typing-text corpus produced only "+targetBearing.length+" stable-target sentences; need "+exerciseLimit+" for cloze");
}

const candidateByLevel=new Map();
for (const candidate of candidates) {
  if (!candidateByLevel.has(candidate.level)) candidateByLevel.set(candidate.level,[]);
  candidateByLevel.get(candidate.level).push(candidate);
}
for (const group of candidateByLevel.values()) {
  group.sort((left,right)=>
    Number(right.matches.length>0)-Number(left.matches.length>0)||
    left.passageId.localeCompare(right.passageId)||
    left.sentenceIndex-right.sentenceIndex
  );
}
const selected=[];
let sentenceRound=0;
while (selected.length<sentenceLimit) {
  let added=false;
  for (const level of [...candidateByLevel.keys()].sort((a,b)=>a-b)) {
    const candidate=candidateByLevel.get(level)?.[sentenceRound];
    if (!candidate) continue;
    selected.push(candidate);
    added=true;
    if (selected.length>=sentenceLimit) break;
  }
  if (!added) break;
  sentenceRound++;
}
const selectedByLevel=new Map();
for (const candidate of selected.filter(item=>item.matches.length>0)) {
  if (!selectedByLevel.has(candidate.level)) selectedByLevel.set(candidate.level,[]);
  selectedByLevel.get(candidate.level).push(candidate);
}
const selectedTargetCount=[...selectedByLevel.values()].reduce((sum,group)=>sum+group.length,0);
if (selectedTargetCount<exerciseLimit) {
  throw new Error("Selected 1000-sentence corpus retained only "+selectedTargetCount+" stable-target sentences; need "+exerciseLimit);
}
const exerciseCandidates=[];
let round=0;
while (exerciseCandidates.length<exerciseLimit) {
  let added=false;
  for (const level of [...selectedByLevel.keys()].sort((a,b)=>a-b)) {
    const group=selectedByLevel.get(level);
    const candidate=group?.[round];
    if (!candidate) continue;
    exerciseCandidates.push(candidate);
    added=true;
    if (exerciseCandidates.length>=exerciseLimit) break;
  }
  if (!added) break;
  round++;
}
if (exerciseCandidates.length<exerciseLimit) {
  throw new Error("Unable to spread "+exerciseLimit+" cloze exercises across selected sentence corpus");
}

const exercises=exerciseCandidates.map(candidate=>{
  const best=[...candidate.matches].sort((a,b)=>
    b.target.split(" ").length-a.target.split(" ").length||
    b.target.length-a.target.length||
    a.start-b.start
  )[0];
  const prompt=
    candidate.record.text.slice(0,best.start)+"___"+candidate.record.text.slice(best.end);
  const sourceFile=String(candidate.record.provenance.sources[0].sourceUrl).replace(/^shared\/typing-texts\//,"");
  return {
    schemaVersion:1,
    id:"ex.cloze.tt."+String(candidate.passageId).toLocaleLowerCase("en-US")+"."+String(candidate.sentenceIndex+1).padStart(3,"0"),
    type:"cloze",
    prompt,
    targetIds:[best.lexemeId],
    acceptedAnswers:[best.target],
    sourceSentenceIds:[candidate.record.id],
    cefr:candidate.record.cefr,
    quality:quality(),
    provenance:provenance(sourceFile,candidate.passageId,candidate.sentenceIndex)
  };
});

await fs.mkdir(outDir,{recursive:true});
await Promise.all([
  fs.writeFile(sentenceOutput,stableJson({schemaVersion:1,records:selected.map(item=>item.record)}),"utf8"),
  fs.writeFile(exerciseOutput,stableJson({schemaVersion:1,records:exercises}),"utf8")
]);
const byCefr=Object.fromEntries(
  [...new Set(selected.map(item=>item.record.cefr))].sort().map(cefr=>[
    cefr,
    selected.filter(item=>item.record.cefr===cefr).length
  ])
);
console.log("E06 typing-text candidates:",JSON.stringify({
  sourceLevels:index.availableLevels,
  availableCandidateSentences:candidates.length,
  stableTargetSentences:targetBearing.length,
  selectedStableTargetSentences:selectedTargetCount,
  sentences:selected.length,
  clozeExercises:exercises.length,
  byCefr
}));
