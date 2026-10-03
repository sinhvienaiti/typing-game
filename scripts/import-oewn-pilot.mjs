import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { normalizeEnglishKey, readJson, stableJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const args=new Map(process.argv.slice(2).map(raw=>{
  const [key,...rest]=raw.split("=");
  return [key,rest.join("=")];
}));
const limitRaw=args.get("--limit");
const concurrencyRaw=args.get("--concurrency");
const limit=limitRaw===undefined?300:Number(limitRaw);
const concurrency=concurrencyRaw===undefined?4:Number(concurrencyRaw);
if (!Number.isInteger(limit)||limit<1||limit>300) throw new Error("--limit must be an integer from 1 to 300");
if (!Number.isInteger(concurrency)||concurrency<1||concurrency>8) throw new Error("--concurrency must be an integer from 1 to 8");

const sourceManifest=await readJson(path.join(root,"content","english","sources","manifest.json"));
const source=sourceManifest.sources.find(item=>item.id==="oewn");
if (!source||typeof source.apiTemplate!=="string"||!source.apiTemplate.includes("{lemma}")) throw new Error("OEWN apiTemplate is not configured");
if (!source.snapshot) throw new Error("OEWN release snapshot is not pinned");
if (!process.argv.includes("--allow-live-api")) {
  throw new Error("The OEWN lemma API is a live endpoint, not the pinned 2025 release. Re-run with --allow-live-api to create a non-publishable review queue, or use the pinned full-release importer when publication is required.");
}

const pilot=await readJson(path.join(root,"content","english","dictionary","lexeme-seed-pilot.json"));
const seeds=pilot.records.slice(0,limit);
const records=new Array(seeds.length);
const errors=[];

function strings(value) {
  return Array.isArray(value)?value.filter(item=>typeof item==="string"&&item.trim()!=="").map(item=>item.trim()):[];
}
function normalizeSynset(synset,headwordKey) {
  if (!synset||typeof synset!=="object") return null;
  const members=Array.isArray(synset.members)?synset.members:[];
  const targetMembers=members.filter(member=>member&&typeof member==="object"&&normalizeEnglishKey(member.lemma??"")===headwordKey);
  const sourceSenseIds=[...new Set(targetMembers.flatMap(member=>{
    const id=member?.sense?.id;
    return typeof id==="string"&&id.trim()!==""?[id]:[];
  }))];
  const pronunciations=[];
  const seenPron=new Set();
  for (const member of targetMembers) {
    for (const pronunciation of Array.isArray(member.pronunciation)?member.pronunciation:[]) {
      if (!pronunciation||typeof pronunciation!=="object"||typeof pronunciation.value!=="string"||pronunciation.value.trim()==="") continue;
      const value=pronunciation.value.trim();
      const variety=typeof pronunciation.variety==="string"&&pronunciation.variety.trim()!==""?pronunciation.variety.trim():null;
      const key=value+"\u0000"+(variety??"");
      if (seenPron.has(key)) continue;
      seenPron.add(key); pronunciations.push({value,variety});
    }
  }
  const synsetId=typeof synset.id==="string"?synset.id.trim():"";
  const pos=typeof synset.partOfSpeech==="string"?synset.partOfSpeech.trim():"";
  if (!synsetId||!pos) return null;
  return {
    synsetId,
    ili:typeof synset.ili==="string"&&synset.ili.trim()!==""?synset.ili.trim():null,
    lexname:typeof synset.lexname==="string"&&synset.lexname.trim()!==""?synset.lexname.trim():null,
    partOfSpeech:pos,
    definitions:strings(synset.definition),
    examples:strings(synset.example),
    memberLemmas:[...new Set(members.flatMap(member=>typeof member?.lemma==="string"&&member.lemma.trim()!==""?[member.lemma.trim()]:[]))],
    sourceSenseIds,
    pronunciations
  };
}

async function fetchSeed(seed,index) {
  const encoded=encodeURIComponent(seed.headword);
  const sourceUrl=source.apiTemplate.replace("{lemma}",encoded);
  try {
    const response=await fetch(sourceUrl,{headers:{Accept:"application/json"}});
    if (!response.ok) throw new Error("HTTP "+response.status);
    const payload=await response.json();
    if (!Array.isArray(payload)) throw new Error("OEWN lemma response must be an array");
    const synsets=payload.map(item=>normalizeSynset(item,seed.headwordKey)).filter(Boolean);
    records[index]={lexemeId:seed.id,headword:seed.headword,headwordKey:seed.headwordKey,sourceUrl,synsets};
  } catch (error) {
    errors.push({lexemeId:seed.id,headword:seed.headword,message:error instanceof Error?error.message:String(error)});
  }
}

let next=0;
async function worker() {
  while (true) {
    const index=next++;
    if (index>=seeds.length) return;
    await fetchSeed(seeds[index],index);
  }
}
await Promise.all(Array.from({length:Math.min(concurrency,seeds.length)},()=>worker()));

const output={
  schemaVersion:1,
  source:"oewn",
  snapshot:"live-api-unpinned",
  records:records.filter(Boolean),
  errors:errors.sort((a,b)=>a.lexemeId.localeCompare(b.lexemeId))
};
const target=path.join(root,"content","english","review-queues","oewn-pilot.json");
await fs.mkdir(path.dirname(target),{recursive:true});
await fs.writeFile(target,stableJson(output),"utf8");
console.log("OEWN pilot import:",output.records.length+" records,",output.errors.length+" errors -> "+path.relative(root,target));
if (output.records.length===0) process.exitCode=1;
