import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { normalizeSentenceKey } from "./english-content-core.mjs";
import { englishContentReviewSourceDigest } from "./english-review-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const batchManifestPath=path.join(root,"content","english","batches","manifest.json");
const reviewBasePath=path.join(root,"content","english","reviews","decisions.json");
const reviewShardDir=path.join(root,"content","english","reviews","decisions.d");

async function readJson(file){return JSON.parse(await fs.readFile(file,"utf8"));}
async function writeJson(file,value){await fs.writeFile(file,JSON.stringify(value,null,2)+"\n","utf8");}
function boundedContains(sentence,needle){
  const sentenceKey=normalizeSentenceKey(sentence);
  const needleKey=normalizeSentenceKey(needle);
  return needleKey!==""&&(" "+sentenceKey+" ").includes(" "+needleKey+" ");
}
function decisionKey(batchId,recordSetId,recordId){return batchId+"\u0000"+recordSetId+"\u0000"+recordId;}

const [batchManifest,sentenceManifest]=await Promise.all([
  readJson(batchManifestPath),
  readJson(path.join(root,"shared","sentences","manifest.json")),
]);
const examples=[];
for(const shard of sentenceManifest.shards??[]){
  if(!String(shard.path).startsWith("examples/")) continue;
  const doc=await readJson(path.join(root,"shared","sentences",shard.path));
  for(const record of doc.records??[]){
    if(record?.quality?.state==="published"&&typeof record?.text==="string") examples.push(record);
  }
}
if(examples.length!==1513) throw new Error(`E04 linkage drift: expected 1513 published examples, got ${examples.length}`);

const reviewPaths=[reviewBasePath];
try{
  for(const name of (await fs.readdir(reviewShardDir)).filter(name=>name.endsWith(".json")).sort((a,b)=>a.localeCompare(b,"en"))){
    reviewPaths.push(path.join(reviewShardDir,name));
  }
}catch(error){if(error?.code!=="ENOENT") throw error;}
const reviewDocs=new Map();
const reviewIndex=new Map();
for(const file of reviewPaths){
  const doc=await readJson(file);
  reviewDocs.set(file,doc);
  for(const decision of doc.decisions??[]){
    const key=decisionKey(decision.batchId,decision.recordSetId,decision.recordId);
    if(reviewIndex.has(key)) throw new Error(`duplicate review decision target: ${key}`);
    reviewIndex.set(key,{file,decision});
  }
}

const changedReviewFiles=new Set();
const changedSourceFiles=[];
let linkedCollocations=0;
let linkedPhraseItems=0;
let linkedExampleRefs=0;
const linkedRecords=[];

for(const batch of batchManifest.batches??[]){
  if(batch.phase!=="E04"||batch.category!=="phrases") continue;
  for(const set of batch.recordSets??[]){
    const isCollocation=set.id==="collocations"||set.id==="scale-collocations";
    const isPhrase=set.id==="phrases"||set.id==="scale-phrases";
    if(!isCollocation&&!isPhrase) continue;
    const sourcePath=path.join(root,set.path);
    const doc=await readJson(sourcePath);
    let fileChanged=false;
    for(const record of doc.records??[]){
      if(!record||typeof record.id!=="string"||typeof record.text!=="string") continue;
      if(Array.isArray(record.exampleIds)&&record.exampleIds.length>0) continue;
      const matches=[];
      for(const example of examples){
        if(boundedContains(example.text,record.text)) matches.push(example.id);
        if(matches.length===5) break;
      }
      if(matches.length===0) continue;
      record.exampleIds=matches;
      const key=decisionKey(batch.id,set.id,record.id);
      const target=reviewIndex.get(key);
      if(!target) throw new Error(`missing review decision for ${batch.id}/${set.id}/${record.id}`);
      if(target.decision.targetState!=="published") throw new Error(`link target is not published: ${target.decision.id}`);
      target.decision.sourceDigest=englishContentReviewSourceDigest(record);
      target.decision.checks={
        ...(target.decision.checks??{}),
        exampleLink:{status:"pass",method:"published-whole-phrase-boundary-match-v1"},
      };
      const evidenceNote="Example IDs added only from normalized whole-phrase boundary matches against already-published sentence examples.";
      if(!String(target.decision.note??"").includes(evidenceNote)) target.decision.note=String(target.decision.note??"").trim()+" "+evidenceNote;
      changedReviewFiles.add(target.file);
      fileChanged=true;
      linkedExampleRefs+=matches.length;
      if(isCollocation) linkedCollocations+=1; else linkedPhraseItems+=1;
      linkedRecords.push({id:record.id,text:record.text,exampleIds:matches,batchId:batch.id,recordSetId:set.id});
    }
    if(fileChanged){
      await writeJson(sourcePath,doc);
      changedSourceFiles.push(set.path);
    }
  }
}

if(linkedCollocations!==8||linkedPhraseItems!==26){
  throw new Error(`E04 safe-link evidence drift: expected 8 collocations + 26 phrase items, got ${linkedCollocations} + ${linkedPhraseItems}`);
}
for(const file of changedReviewFiles) await writeJson(file,reviewDocs.get(file));

const report={
  schemaVersion:1,
  method:"published-whole-phrase-boundary-match-v1",
  publishedExamplesScanned:examples.length,
  linkedCollocations,
  linkedPhraseItems,
  linkedExampleRefs,
  changedSourceFiles:changedSourceFiles.sort(),
  changedReviewFiles:[...changedReviewFiles].map(file=>path.relative(root,file)).sort(),
  linkedRecords,
};
await fs.mkdir(path.join(root,"content","english","reports"),{recursive:true});
await writeJson(path.join(root,"content","english","reports","e04-safe-example-links.json"),report);
console.log(JSON.stringify(report,null,2));
