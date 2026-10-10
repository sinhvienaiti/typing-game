import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";
import { englishContentRecordId, englishContentReviewSourceDigest } from "./english-review-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const targetDoc=await readJson(path.join(root,"content","english","targets","long-term.json"));
const batchManifest=await readJson(path.join(root,"content","english","batches","manifest.json"));
const errors=[];
const rows=[];
const seenTargets=new Set();

function recordKey(record,index) {
  const id=record?.id??record?.lexemeId;
  return typeof id==="string"&&id.trim()!==""?id:"#"+String(index+1);
}
function selectCollection(doc,source) {
  const values=doc?.[source.collection];
  if (!Array.isArray(values)) throw new TypeError(source.path+" does not contain "+source.collection+"[]");
  if (source.filterField===undefined) return values;
  const wanted=new Set(source.filterValues??[]);
  return values.filter(item=>wanted.has(String(item?.[source.filterField])));
}
function sourceKey(source) {
  return [
    source.path,
    source.collection,
    source.filterField??"",
    [...(source.filterValues??[])].sort((a,b)=>String(a).localeCompare(String(b),"en")).join("\u0000"),
  ].join("\u0001");
}
function e04ManifestSources(targetId) {
  const sources=[];
  for (const batch of batchManifest.batches??[]) {
    if (batch?.phase!=="E04"||batch?.category!=="phrases") continue;
    for (const set of batch.recordSets??[]) {
      const setId=String(set?.id??"");
      const relative=String(set?.path??"");
      if (!relative) continue;
      if (targetId==="collocations"&&(setId==="collocations"||setId==="scale-collocations")) {
        sources.push({path:relative,collection:"records"});
      } else if (targetId==="verb-patterns"&&(setId==="verb-patterns"||setId==="scale-verb-patterns")) {
        sources.push({path:relative,collection:"records"});
      } else if (targetId==="phrasal-verbs"&&(setId==="phrases"||setId==="scale-phrases")) {
        sources.push({path:relative,collection:"records",filterField:"type",filterValues:["phrasal-verb"]});
      } else if (targetId==="idioms-chunks"&&(setId==="phrases"||setId==="scale-phrases")) {
        sources.push({path:relative,collection:"records",filterField:"type",filterValues:["idiom","chunk"]});
      }
    }
  }
  return sources;
}
function sourcesForTarget(target) {
  const merged=[...(target.sources??[]),...e04ManifestSources(target.id)];
  const seen=new Set();
  return merged.filter(source=>{
    const key=sourceKey(source);
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });
}
function pendingChecks(record) {
  return Object.entries(record?.quality?.checks??{})
    .filter(([,check])=>check?.status==="pending")
    .map(([name])=>name)
    .sort((a,b)=>a.localeCompare(b,"en"));
}
function reviewPreview(record,recordSetId) {
  if (recordSetId==="grammar-topics") return {title:record.title,objective:record.objective,concept:record.concept,formulae:record.formulae};
  if (recordSetId==="examples") return {text:record.text,grammarIds:record.grammarIds};
  if (recordSetId==="exercises") return {type:record.type,prompt:record.prompt,acceptedAnswers:record.acceptedAnswers,targetIds:record.targetIds,sourceSentenceIds:record.sourceSentenceIds};
  return {incorrect:record.incorrect,corrections:record.corrections,explanationVi:record.explanationVi,targetIds:record.targetIds};
}
async function buildGrammarReviewPacket(slice) {
  const batchId="e05.grammar-scale-"+slice;
  const sets=[
    ["grammar-topics","content/english/grammar/e05-scale-"+slice+"-topics.json",8],
    ["examples","content/english/sentences/e05-scale-"+slice+"-sentences.json",24],
    ["exercises","content/english/sentences/e05-scale-"+slice+"-exercises.json",16],
    ["common-mistakes","content/english/sentences/e05-scale-"+slice+"-common-mistakes.json",8],
  ];
  const recordSets=[];
  for (const [recordSetId,relative,expectedCount] of sets) {
    let doc;
    try { doc=await readJson(path.join(root,relative)); }
    catch (error) { errors.push(batchId+": "+error.message); continue; }
    const records=doc.records??[];
    if (records.length!==expectedCount) errors.push(batchId+"/"+recordSetId+": expected "+expectedCount+" records, got "+records.length);
    recordSets.push({
      recordSetId,path:relative,expectedCount,
      records:records.map((record,index)=>({
        recordId:englishContentRecordId(record,index),sourceDigest:englishContentReviewSourceDigest(record),
        state:record?.quality?.state,pendingChecks:pendingChecks(record),preview:reviewPreview(record,recordSetId),
      })),
    });
  }
  return {batchId,slice,recordSets};
}
async function readSnapshotText(relative) { return fs.readFile(path.join(root,relative),"utf8"); }

for (const target of targetDoc.targets??[]) {
  if (seenTargets.has(target.id)) errors.push("duplicate long-term target id: "+target.id);
  seenTargets.add(target.id);
  if (target.maximum!==undefined&&target.maximum<target.minimum) errors.push(target.id+": maximum is below minimum");
  const unique=new Set();
  const sourceCounts=[];
  const targetSources=sourcesForTarget(target);
  for (const source of targetSources) {
    let doc;
    try { doc=await readJson(path.join(root,source.path)); }
    catch (error) { errors.push(target.id+": "+error.message); continue; }
    let records;
    try { records=selectCollection(doc,source); }
    catch (error) { errors.push(target.id+": "+error.message); continue; }
    records.forEach((record,index)=>unique.add(recordKey(record,index)+"@"+source.path));
    sourceCounts.push({path:source.path,count:records.length});
  }
  const current=unique.size;
  if (target.maximum!==undefined&&current>target.maximum) errors.push(target.id+": current count "+current+" exceeds maximum "+target.maximum);
  rows.push({
    id:target.id,label:target.label,current,minimum:target.minimum,
    ...(target.maximum===undefined?{}:{maximum:target.maximum}),
    completionPercent:target.minimum===0?100:Number(Math.min(100,(current/target.minimum)*100).toFixed(2)),
    minimumReached:current>=target.minimum,sourceCounts,
  });
}

const expected={
  "grammar-topics":[300,320],"verb-patterns":[500,1000],"collocations":[5000,null],"phrasal-verbs":[1000,null],
  "idioms-chunks":[2000,null],"common-mistakes":[2000,null],"example-sentences":[100000,null],"translation-pairs":[20000,null],
  "cloze-exercises":[30000,null],"sentence-transformations":[10000,null],"dialogue-examples":[10000,null],
};
for (const [id,[minimum,maximum]] of Object.entries(expected)) {
  const target=targetDoc.targets?.find(item=>item.id===id);
  if (!target) errors.push("missing locked long-term target: "+id);
  else {
    if (target.minimum!==minimum) errors.push(id+": minimum drifted from locked master-plan target");
    if ((target.maximum??null)!==maximum) errors.push(id+": maximum drifted from locked master-plan target");
  }
}

const pendingGrammarReview=[];
const snapshotPaths=[
  "content/english/batches/manifest.json",
  "content/english/grammar/e05-scale-b1-08-topics.json",
  "content/english/sentences/e05-scale-b1-08-sentences.json",
  "content/english/sentences/e05-scale-b1-08-exercises.json",
  "content/english/sentences/e05-scale-b1-08-common-mistakes.json",
  "scripts/publish-english-content.mjs",
  "scripts/smoke-published-english-content.mjs",
  "content/english/releases/2026.10.0.json",
  "shared/grammar/manifest.json",
  "shared/grammar/topics/000.json",
  "shared/sentences/manifest.json",
  "shared/sentences/examples/000.json",
  "shared/sentences/examples/001.json",
  "shared/sentences/exercises/000.json",
  "shared/sentences/exercises/001.json",
  "shared/sentences/mistakes/000.json"
];
const publicationSnapshot={};
for (const relative of snapshotPaths) publicationSnapshot[relative]=await readSnapshotText(relative);

const output={schemaVersion:1,targets:rows,pendingGrammarReview,publicationSnapshot};
await fs.mkdir(path.join(root,"content","english","reports"),{recursive:true});
await fs.writeFile(path.join(root,"content","english","reports","e11-readiness.json"),stableJson(output),"utf8");
console.log(JSON.stringify({
  schemaVersion:output.schemaVersion,
  targets:rows.length,
  pendingGrammarReview:pendingGrammarReview.map(packet=>({batchId:packet.batchId,records:packet.recordSets.reduce((sum,set)=>sum+set.records.length,0)})),
  publicationSnapshotFiles:Object.keys(publicationSnapshot).length,
},null,2));
if (errors.length) {
  console.error(errors.join("\n"));
  process.exitCode=1;
}
