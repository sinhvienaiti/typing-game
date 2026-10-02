import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  looksLikeLearningPair,
  normalizedPairKey,
  readLinks,
  readSentenceMap,
  selectEvenly,
  sha256File,
} from "./tatoeba-pair-core.mjs";
import { stableJson, readJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const args=new Map(process.argv.slice(2).filter(value=>value.startsWith("--")).map(raw=>{
  const split=raw.indexOf("=");
  return split<0?[raw,"true"]:[raw.slice(0,split),raw.slice(split+1)];
}));
const englishFile=path.resolve(root,args.get("--eng")??".cache/english-content/tatoeba/eng_sentences.tsv");
const vietnameseFile=path.resolve(root,args.get("--vie")??".cache/english-content/tatoeba/vie_sentences.tsv");
const linksFile=path.resolve(root,args.get("--links")??".cache/english-content/tatoeba/eng-vie_links.tsv");
const outDir=path.resolve(root,args.get("--output-dir")??"content/english/review-queues");
const limit=Math.min(1000,Math.max(1,Number(args.get("--limit")??300)));

const pin=await readJson(path.join(root,"content","english","sources","tatoeba-eng-vie-pilot.json"));
const observed={
  engSentences:await sha256File(englishFile),
  vieSentences:await sha256File(vietnameseFile),
  links:await sha256File(linksFile),
};
let sourcePinned=true;
for (const key of Object.keys(observed)) {
  const expected=pin.files?.[key]?.contentSha256;
  if (!expected) sourcePinned=false;
  else if (expected!==observed[key]) {
    throw new Error("Tatoeba "+key+" content checksum mismatch. Expected "+expected+", got "+observed[key]);
  }
}

const [english,vietnamese,links]=await Promise.all([
  readSentenceMap(englishFile,"eng"),
  readSentenceMap(vietnameseFile,"vie"),
  readLinks(linksFile),
]);

const candidates=[];
const pairKeys=new Set();
const englishKeys=new Set();
for (const link of links) {
  const englishText=english.get(link.englishId);
  const vietnameseText=vietnamese.get(link.vietnameseId);
  if (englishText===undefined||vietnameseText===undefined) continue;
  if (!looksLikeLearningPair(englishText,vietnameseText)) continue;
  const pairKey=normalizedPairKey(englishText,vietnameseText);
  const englishKey=englishText.normalize("NFKC").trim().replace(/\s+/gu," ").toLocaleLowerCase("en-US");
  if (pairKeys.has(pairKey)||englishKeys.has(englishKey)) continue;
  pairKeys.add(pairKey);
  englishKeys.add(englishKey);
  candidates.push({...link,englishText,vietnameseText});
}
candidates.sort((a,b)=>a.englishId-b.englishId||a.vietnameseId-b.vietnameseId);
if (candidates.length<limit) {
  throw new Error("Only "+candidates.length+" Tatoeba EN-VI candidates passed filters; need "+limit);
}
const selected=selectEvenly(candidates,limit);

function quality() {
  return {
    state:"candidate",
    checks:{
      schema:{status:"pass",method:"tatoeba-e06-import-v1"},
      sourcePin:{
        status:sourcePinned?"pass":"pending",
        method:sourcePinned?"content-sha256-pin-v1":"checksum-probe-required",
      },
      exactDuplicate:{status:"pass",method:"normalized-pair-v1"},
      translation:{status:"pending",method:"bilingual-review-required"},
      naturalness:{status:"pending",method:"editor-review-required"},
      cefr:{status:"pending",method:"cefr-review-required"},
    },
  };
}
function sourceRef(id) {
  return {
    dataset:"tatoeba",
    sourceId:String(id),
    sourceUrl:"https://tatoeba.org/en/sentences/show/"+String(id),
    snapshot:pin.snapshot,
    license:pin.license,
    attribution:"Tatoeba sentence #"+String(id),
    modified:false,
  };
}

const sentences=selected.map(pair=>({
  schemaVersion:1,
  id:"sent.tatoeba."+String(pair.englishId),
  text:pair.englishText,
  contexts:["translation"],
  register:["neutral"],
  quality:quality(),
  provenance:{
    sources:[sourceRef(pair.englishId)],
    note:"English sentence selected from a linked Tatoeba English-Vietnamese pair.",
  },
}));
const exercises=selected.map(pair=>({
  schemaVersion:1,
  id:"ex.translation.tatoeba."+String(pair.englishId)+"."+String(pair.vietnameseId),
  type:"translation",
  prompt:pair.vietnameseText,
  targetIds:["sent.tatoeba."+String(pair.englishId)],
  acceptedAnswers:[pair.englishText],
  sourceSentenceIds:["sent.tatoeba."+String(pair.englishId)],
  quality:quality(),
  provenance:{
    sources:[sourceRef(pair.englishId),sourceRef(pair.vietnameseId)],
    note:"Vietnamese-to-English translation pair selected from a direct Tatoeba translation link.",
  },
}));
const report={
  schemaVersion:1,
  source:"tatoeba",
  snapshot:pin.snapshot,
  observedContentSha256:observed,
  sourcePinned,
  candidatePairs:candidates.length,
  selectedPairs:selected.length,
};

await fs.mkdir(outDir,{recursive:true});
await Promise.all([
  fs.writeFile(path.join(outDir,"tatoeba-e06-sentences.json"),stableJson({schemaVersion:1,records:sentences}),"utf8"),
  fs.writeFile(path.join(outDir,"tatoeba-e06-translations.json"),stableJson({schemaVersion:1,records:exercises}),"utf8"),
  fs.writeFile(path.join(outDir,"tatoeba-e06-source-report.json"),stableJson(report),"utf8"),
]);
console.log("Tatoeba E06 translation pilot:",JSON.stringify(report));
