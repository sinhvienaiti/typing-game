import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson, stableJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const [oewn,vi]=await Promise.all([
  readJson(path.join(root,"content","english","review-queues","oewn-2025-pilot.json")),
  readJson(path.join(root,"content","english","review-queues","viwiktionary-en-pilot.json")),
]);
const viById=new Map((vi.records??[]).map(item=>[item.lexemeId,item]));

function normalizePos(value) {
  const key=String(value??"").toLocaleLowerCase("en-US");
  if (key==="a"||key==="s"||key==="adj"||key==="adjective") return "adj";
  if (key==="n"||key==="noun") return "noun";
  if (key==="v"||key==="verb") return "verb";
  if (key==="r"||key==="adv"||key==="adverb") return "adv";
  return key||"other";
}
function quality() {
  return {
    state:"candidate",
    checks:{
      schema:{status:"pass",method:"e03-sense-review-packet-v1"},
      sourcePin:{status:"pass",method:"upstream-pinned-sources"},
      posGrouping:{status:"pass",method:"normalized-pos-buckets-v1"},
      senseAlignment:{status:"pending",method:"bilingual-editor-alignment-required"},
      translation:{status:"pending",method:"bilingual-review-required"},
      naturalness:{status:"pending",method:"editor-review-required"},
    },
  };
}

const records=(oewn.records??[]).map(record=>{
  const viRecord=viById.get(record.lexemeId);
  const oewnParts=(record.parts??[]).map(part=>({
    pos:normalizePos(part.partOfSpeech),
    sourcePos:part.partOfSpeech,
    forms:[...(part.forms??[])],
    senses:(part.senses??[]).map(sense=>({
      senseId:sense.senseId,
      synsetId:sense.synsetId,
      definitionEn:[...(sense.definitionEn??[])],
      examples:[...(sense.sourceExamples??[])].slice(0,8),
    })),
  }));
  const viEntries=(viRecord?.entries??[]).map(entry=>({
    pos:normalizePos(entry.pos),
    sourcePos:entry.pos,
    ipa:[...(entry.ipa??[])],
    senses:(entry.senses??[]).map(sense=>({
      sourceSenseIndex:sense.sourceSenseIndex,
      glossesVi:[...(sense.glossesVi??[])],
      examples:[...(sense.examples??[])].slice(0,8),
    })),
  }));
  const positions=[...new Set([
    ...oewnParts.map(item=>item.pos),
    ...viEntries.map(item=>item.pos),
  ])].sort();
  const posReview=positions.map(pos=>({
    pos,
    oewnSenseIds:oewnParts.filter(item=>item.pos===pos).flatMap(item=>item.senses.map(sense=>sense.senseId)),
    viSenseIndexes:viEntries.filter(item=>item.pos===pos).flatMap(item=>item.senses.map(sense=>sense.sourceSenseIndex)),
    status:"pending",
  }));
  return {
    lexemeId:record.lexemeId,
    headword:record.headword,
    headwordKey:record.headwordKey,
    oewnParts,
    viEntries,
    posReview,
    quality:quality(),
  };
});
if (records.length!==300) throw new Error("E03 sense review requires exactly 300 OEWN records");

const metrics={
  requested:records.length,
  bothSources:records.filter(item=>item.viEntries.length>0).length,
  oewnOnly:records.filter(item=>item.viEntries.length===0).length,
  posOverlapRecords:records.filter(item=>{
    const left=new Set(item.oewnParts.map(part=>part.pos));
    return item.viEntries.some(entry=>left.has(entry.pos));
  }).length,
  oewnSenses:records.reduce((sum,item)=>sum+item.oewnParts.reduce((n,part)=>n+part.senses.length,0),0),
  viSenses:records.reduce((sum,item)=>sum+item.viEntries.reduce((n,entry)=>n+entry.senses.length,0),0),
};
const output=path.join(root,"content","english","review-queues","e03-sense-alignment-review.json");
await fs.writeFile(output,stableJson({schemaVersion:1,source:"oewn+viwiktionary-en",records,metrics}),"utf8");
console.log("E03 sense review packet:",JSON.stringify(metrics));
