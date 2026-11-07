import crypto from "node:crypto";
import fs from "node:fs";
import fsp from "node:fs/promises";
import path from "node:path";
import readline from "node:readline";
import zlib from "node:zlib";
import { fileURLToPath } from "node:url";
import {
  normalizeEnglishKey,
  readJson,
  stableJson,
} from "./english-content-core.mjs";
import {
  cleanStrings,
  parseWiktextractForms,
  parseWiktextractIpa,
  parseWiktextractSenses,
} from "./wiktextract-enrichment-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const args=new Map(process.argv.slice(2).filter(value=>value.startsWith("--")).map(raw=>{
  const split=raw.indexOf("=");
  return split<0?[raw,"true"]:[raw.slice(0,split),raw.slice(split+1)];
}));
const input=path.resolve(root,args.get("--input")??".cache/english-content/simplewiktionary/raw-wiktextract-data.jsonl.gz");
const output=path.resolve(root,args.get("--output")??"content/english/review-queues/simplewiktionary-en-pilot.json");
const allowUnpinned=args.get("--allow-unpinned")==="true";

const [seedDoc,sourceManifest]=await Promise.all([
  readJson(path.join(root,"content","english","dictionary","lexeme-seed-pilot.json")),
  readJson(path.join(root,"content","english","sources","manifest.json")),
]);
const source=sourceManifest.sources?.find(item=>item.id==="simplewiktionary-en");
if (!source) throw new Error("simplewiktionary-en source manifest entry is missing");
if (!Array.isArray(seedDoc.records)||seedDoc.records.length!==300) throw new Error("Expected exactly 300 lexeme pilot seeds");

const hash=crypto.createHash("sha256");
for await (const chunk of fs.createReadStream(input)) hash.update(chunk);
const sourceSha256=hash.digest("hex");
if (source.checksumSha256&&source.checksumSha256!==sourceSha256) {
  throw new Error("Simple Wiktionary checksum mismatch. Expected "+source.checksumSha256+", got "+sourceSha256);
}
if (!source.checksumSha256&&!allowUnpinned) {
  throw new Error("Simple Wiktionary checksum is not pinned. Use --allow-unpinned only for the first CI probe.");
}
const sourcePinned=Boolean(source.checksumSha256);

const seedsByKey=new Map(seedDoc.records.map(record=>[record.headwordKey,record]));
const collected=new Map();
const stream=fs.createReadStream(input).pipe(zlib.createGunzip());
const lines=readline.createInterface({input:stream,crlfDelay:Infinity});
for await (const line of lines) {
  if (!line.trim()) continue;
  const item=JSON.parse(line);
  if (item?.lang_code!=="en"||typeof item.word!=="string") continue;
  const key=normalizeEnglishKey(item.word);
  const seed=seedsByKey.get(key);
  if (!seed) continue;
  const forms=parseWiktextractForms(item);
  const senses=parseWiktextractSenses(item);
  const ipa=parseWiktextractIpa(item);
  if (forms.length===0&&senses.length===0&&ipa.length===0) continue;

  let record=collected.get(key);
  if (!record) {
    record={seed,entries:[]};
    collected.set(key,record);
  }
  record.entries.push({
    pos:typeof item.pos==="string"&&item.pos.trim()?item.pos.trim():"unknown",
    forms,
    ipa,
    senses,
  });
}

const records=seedDoc.records.map(seed=>{
  const found=collected.get(seed.headwordKey);
  const entries=found?.entries??[];
  const hasUsage=entries.some(entry=>entry.senses.some(sense=>sense.tags.length>0));
  return {
    lexemeId:seed.id,
    headword:seed.headword,
    headwordKey:seed.headwordKey,
    mapped:entries.length>0,
    entries,
    quality:{
      state:"candidate",
      checks:{
        schema:{status:"pass",method:"simplewiktionary-import-v1"},
        sourcePin:{
          status:sourcePinned?"pass":"pending",
          method:sourcePinned?"sha256-manifest-v1":"first-probe-checksum-required",
        },
        morphologyUsageReview:{status:"pending",method:"lexicographer-review-required"},
        naturalness:{status:"pending",method:"editor-review-required"},
      },
    },
    provenance:{
      sources:[{
        dataset:"simplewiktionary-en",
        sourceId:seed.headword,
        sourceUrl:source.releaseUrl,
        snapshot:source.snapshot??null,
        license:source.license,
        attribution:"Simple English Wiktionary via Wiktextract/Kaikki",
        modified:false,
      }],
      note:hasUsage
        ?"Forms and usage labels are source candidates only; they require review before joining the canonical lexeme."
        :"Source entry found without explicit usage labels; no usage label is invented.",
    },
  };
});

const metrics={
  requested:records.length,
  mapped:records.filter(record=>record.mapped).length,
  mappedRate:Number((records.filter(record=>record.mapped).length/records.length).toFixed(4)),
  entries:records.reduce((sum,record)=>sum+record.entries.length,0),
  forms:records.reduce((sum,record)=>sum+record.entries.reduce((n,entry)=>n+entry.forms.length,0),0),
  senses:records.reduce((sum,record)=>sum+record.entries.reduce((n,entry)=>n+entry.senses.length,0),0),
  withForms:records.filter(record=>record.entries.some(entry=>entry.forms.length>0)).length,
  withUsageLabels:records.filter(record=>record.entries.some(entry=>entry.senses.some(sense=>sense.tags.length>0))).length,
  withIpa:records.filter(record=>record.entries.some(entry=>entry.ipa.length>0)).length,
};
await fsp.mkdir(path.dirname(output),{recursive:true});
await fsp.writeFile(output,stableJson({
  schemaVersion:1,
  source:"simplewiktionary-en",
  sourceSnapshot:String(source.snapshot??"unversioned"),
  sourceSha256,
  records,
  metrics,
}),"utf8");
console.log("Simple Wiktionary E03:",JSON.stringify(metrics),"sha256="+sourceSha256);
