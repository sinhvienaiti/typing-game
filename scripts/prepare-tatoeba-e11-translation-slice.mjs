import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  looksLikeLearningPair,
  normalizedPairKey,
  readLinks,
  readSentenceMap,
  selectNextTatoebaPairs,
  sha256File,
  tatoebaPairSourceKey,
} from "./tatoeba-pair-core.mjs";
import { readJson, stableJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const defaultOutput=path.join(root,"content","english","review-queues","tatoeba-e11-translation-next-review.json");

function parseArgs(argv) {
  const options={
    limit:24,
    englishFile:path.join(root,".cache","english-content","tatoeba","eng_sentences.tsv"),
    vietnameseFile:path.join(root,".cache","english-content","tatoeba","vie_sentences.tsv"),
    linksFile:path.join(root,".cache","english-content","tatoeba","eng-vie_links.tsv"),
    outputPath:defaultOutput,
  };
  for (let index=0;index<argv.length;index++) {
    const raw=argv[index];
    const equal=raw.indexOf("=");
    const flag=equal<0?raw:raw.slice(0,equal);
    const inlineValue=equal<0?null:raw.slice(equal+1);
    const takeValue=()=>{
      if (inlineValue!==null) return inlineValue;
      const value=argv[index+1];
      if (!value||value.startsWith("--")) throw new Error(flag+" requires a value");
      index++;
      return value;
    };
    if (flag==="--limit") options.limit=Number.parseInt(takeValue(),10);
    else if (flag==="--eng") options.englishFile=path.resolve(root,takeValue());
    else if (flag==="--vie") options.vietnameseFile=path.resolve(root,takeValue());
    else if (flag==="--links") options.linksFile=path.resolve(root,takeValue());
    else if (flag==="--output") options.outputPath=path.resolve(root,takeValue());
    else throw new Error("Unknown argument: "+raw);
  }
  if (!Number.isInteger(options.limit)||options.limit<1||options.limit>200) {
    throw new Error("--limit must be an integer from 1 to 200");
  }
  return options;
}

function quality() {
  return {
    state:"candidate",
    checks:{
      schema:{status:"pass",method:"tatoeba-e11-next-slice-v1"},
      sourcePin:{status:"pass",method:"content-sha256-pin-v1"},
      exactDuplicate:{status:"pass",method:"normalized-pair-v1"},
      translation:{status:"pending",method:"bilingual-review-required"},
      naturalness:{status:"pending",method:"editor-review-required"},
      cefr:{status:"pending",method:"cefr-review-required"},
    },
  };
}

function sourceRef(id,pin) {
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

function usedTatoebaPairKey(record) {
  if (record?.type!=="translation") return null;
  const sources=(record?.provenance?.sources??[]).filter(source=>source?.dataset==="tatoeba");
  if (sources.length<2) return null;
  const englishId=Number(sources[0]?.sourceId);
  const vietnameseId=Number(sources[1]?.sourceId);
  if (
    !Number.isSafeInteger(englishId)||englishId<=0||
    !Number.isSafeInteger(vietnameseId)||vietnameseId<=0
  ) return null;
  return tatoebaPairSourceKey({englishId,vietnameseId});
}

async function collectUsedPairKeys(batchManifest) {
  const paths=new Set();
  for (const batch of batchManifest.batches??[]) {
    for (const set of batch.recordSets??[]) {
      if (typeof set?.path==="string"&&set.path) paths.add(set.path);
    }
  }
  const keys=new Set();
  for (const relative of [...paths].sort((a,b)=>a.localeCompare(b,"en"))) {
    const document=await readJson(path.join(root,relative));
    if (!Array.isArray(document?.records)) continue;
    for (const record of document.records) {
      const key=usedTatoebaPairKey(record);
      if (key!==null) keys.add(key);
    }
  }
  return keys;
}

const options=parseArgs(process.argv.slice(2));
const [pin,batchManifest]=await Promise.all([
  readJson(path.join(root,"content","english","sources","tatoeba-eng-vie-pilot.json")),
  readJson(path.join(root,"content","english","batches","manifest.json")),
]);
const observed={
  engSentences:await sha256File(options.englishFile),
  vieSentences:await sha256File(options.vietnameseFile),
  links:await sha256File(options.linksFile),
};
for (const [key,value] of Object.entries(observed)) {
  const expected=pin.files?.[key]?.contentSha256;
  if (!expected||expected!==value) {
    throw new Error(
      "Tatoeba pinned source mismatch for "+key+": expected "+String(expected??"<missing>")+", observed "+value,
    );
  }
}

const [english,vietnamese,links,usedPairKeys]=await Promise.all([
  readSentenceMap(options.englishFile,"eng"),
  readSentenceMap(options.vietnameseFile,"vie"),
  readLinks(options.linksFile),
  collectUsedPairKeys(batchManifest),
]);

const candidates=[];
const normalizedPairs=new Set();
const normalizedEnglish=new Set();
for (const link of links) {
  const englishText=english.get(link.englishId);
  const vietnameseText=vietnamese.get(link.vietnameseId);
  if (englishText===undefined||vietnameseText===undefined) continue;
  if (!looksLikeLearningPair(englishText,vietnameseText)) continue;
  const pairKey=normalizedPairKey(englishText,vietnameseText);
  const englishKey=englishText.normalize("NFKC").trim().replace(/\s+/gu," ").toLocaleLowerCase("en-US");
  if (normalizedPairs.has(pairKey)||normalizedEnglish.has(englishKey)) continue;
  normalizedPairs.add(pairKey);
  normalizedEnglish.add(englishKey);
  candidates.push({...link,englishText,vietnameseText});
}

const selected=selectNextTatoebaPairs(candidates,options.limit,{excludeKeys:usedPairKeys});
if (selected.length<options.limit) {
  throw new Error(
    "Only "+selected.length+" unused pinned Tatoeba candidates remain; requested "+options.limit,
  );
}

const sentences=selected.map(pair=>({
  schemaVersion:1,
  id:"sent.tatoeba."+String(pair.englishId),
  text:pair.englishText,
  contexts:["translation"],
  register:["neutral"],
  quality:quality(),
  provenance:{
    sources:[sourceRef(pair.englishId,pin)],
    note:"English sentence selected from a pinned linked Tatoeba English-Vietnamese pair for E11 review.",
  },
}));
const translations=selected.map(pair=>({
  schemaVersion:1,
  id:"ex.translation.tatoeba."+String(pair.englishId)+"."+String(pair.vietnameseId),
  type:"translation",
  prompt:pair.vietnameseText,
  targetIds:["sent.tatoeba."+String(pair.englishId)],
  acceptedAnswers:[pair.englishText],
  sourceSentenceIds:["sent.tatoeba."+String(pair.englishId)],
  quality:quality(),
  provenance:{
    sources:[sourceRef(pair.englishId,pin),sourceRef(pair.vietnameseId,pin)],
    note:"Vietnamese-to-English pair selected from a pinned direct Tatoeba translation link for E11 review.",
  },
}));

const packet={
  schemaVersion:1,
  kind:"english-content-review-packet",
  batchFamily:"e11.translation-tatoeba",
  source:{
    dataset:"tatoeba",
    snapshot:pin.snapshot,
    observedContentSha256:observed,
    pinned:true,
  },
  selection:{
    strategy:"source-id-order-after-manifest-tatoeba-exclusion-v1",
    requestedLimit:options.limit,
    candidateCount:candidates.length,
    usedPairCount:usedPairKeys.size,
    remainingCandidateCount:candidates.filter(pair=>!usedPairKeys.has(tatoebaPairSourceKey(pair))).length,
    selectedPairKeys:selected.map(tatoebaPairSourceKey),
  },
  recordSets:[
    {recordSetId:"translation-sentences",records:sentences},
    {recordSetId:"translations",records:translations},
  ],
};

await fs.mkdir(path.dirname(options.outputPath),{recursive:true});
await fs.writeFile(options.outputPath,stableJson(packet),"utf8");
console.log("E11 Tatoeba next translation review slice:",JSON.stringify({
  output:path.relative(root,options.outputPath).replaceAll(path.sep,"/"),
  candidateCount:candidates.length,
  usedPairCount:usedPairKeys.size,
  selectedCount:selected.length,
  selectedPairKeys:packet.selection.selectedPairKeys,
}));
