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

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const args=new Map(process.argv.slice(2).filter(value=>value.startsWith("--")).map(raw=>{
  const split=raw.indexOf("=");
  return split<0?[raw,"true"]:[raw.slice(0,split),raw.slice(split+1)];
}));
const input=path.resolve(root,args.get("--input")??".cache/english-content/viwiktionary/raw-wiktextract-data.jsonl.gz");
const output=path.resolve(root,args.get("--output")??"content/english/review-queues/viwiktionary-en-pilot.json");

const [seedDoc,sourceManifest]=await Promise.all([
  readJson(path.join(root,"content","english","dictionary","lexeme-seed-pilot.json")),
  readJson(path.join(root,"content","english","sources","manifest.json")),
]);
const source=sourceManifest.sources?.find(item=>item.id==="viwiktionary-en");
if (!source) throw new Error("viwiktionary-en source manifest entry is missing");
if (!Array.isArray(seedDoc.records)||seedDoc.records.length!==300) {
  throw new Error("Expected exactly 300 lexeme pilot seeds");
}

const hash=crypto.createHash("sha256");
for await (const chunk of fs.createReadStream(input)) hash.update(chunk);
const sourceSha256=hash.digest("hex");
if (source.checksumSha256&&source.checksumSha256!==sourceSha256) {
  throw new Error("Vietnamese Wiktionary source checksum mismatch. Expected "+source.checksumSha256+", got "+sourceSha256);
}

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

  const senses=(Array.isArray(item.senses)?item.senses:[]).flatMap((sense,index)=>{
    const glosses=(Array.isArray(sense?.glosses)?sense.glosses:[])
      .filter(value=>typeof value==="string"&&value.trim()!=="")
      .map(value=>value.normalize("NFC").trim());
    if (glosses.length===0) return [];
    const tags=[
      ...(Array.isArray(sense?.tags)?sense.tags:[]),
      ...(Array.isArray(sense?.raw_tags)?sense.raw_tags:[]),
    ].filter(value=>typeof value==="string"&&value.trim()!=="")
      .map(value=>value.normalize("NFC").trim());
    const examples=(Array.isArray(sense?.examples)?sense.examples:[])
      .flatMap(example=>{
        if (typeof example==="string") return [example];
        if (typeof example?.text==="string") return [example.text];
        return [];
      })
      .map(value=>value.normalize("NFC").trim())
      .filter(Boolean);
    return [{
      sourceSenseIndex:index,
      glossesVi:[...new Set(glosses)],
      tags:[...new Set(tags)],
      examples:[...new Set(examples)],
    }];
  });
  if (senses.length===0) continue;

  const ipa=(Array.isArray(item.sounds)?item.sounds:[])
    .flatMap(sound=>typeof sound?.ipa==="string"?[sound.ipa.normalize("NFC").trim()]:[])
    .filter(Boolean);
  let record=collected.get(key);
  if (!record) {
    record={
      lexemeId:seed.id,
      headword:seed.headword,
      headwordKey:key,
      entries:[],
      quality:{
        state:"candidate",
        checks:{
          schema:{status:"pass",method:"viwiktionary-import-v1"},
          sourcePin:{
            status:source.checksumSha256?"pass":"pending",
            method:source.checksumSha256?"sha256-manifest-v1":"checksum-probe-required",
          },
          senseAlignment:{status:"pending",method:"oewn-viwiktionary-editor-alignment-required"},
          translation:{status:"pending",method:"bilingual-review-required"},
          naturalness:{status:"pending",method:"editor-review-required"},
        },
      },
      provenance:{
        sources:[{
          dataset:"viwiktionary-en",
          sourceId:seed.headword,
          sourceUrl:source.releaseUrl,
          snapshot:source.snapshot??null,
          license:source.license,
          attribution:"Vietnamese Wiktionary via Wiktextract/Kaikki",
          modified:false,
        }],
        note:"Vietnamese gloss candidates are imported by headword and POS. They are not automatically asserted to match Open English WordNet sense ordering.",
      },
    };
    collected.set(key,record);
  }
  record.entries.push({
    pos:typeof item.pos==="string"&&item.pos.trim()?item.pos.trim():"unknown",
    ipa:[...new Set(ipa)],
    senses,
  });
}

const records=[];
const misses=[];
for (const seed of seedDoc.records) {
  const record=collected.get(seed.headwordKey);
  if (record) records.push(record);
  else misses.push({lexemeId:seed.id,headword:seed.headword,headwordKey:seed.headwordKey});
}
const metrics={
  requested:seedDoc.records.length,
  mapped:records.length,
  mappedRate:Number((records.length/seedDoc.records.length).toFixed(4)),
  entries:records.reduce((sum,record)=>sum+record.entries.length,0),
  senses:records.reduce((sum,record)=>sum+record.entries.reduce((inner,entry)=>inner+entry.senses.length,0),0),
  withIpa:records.filter(record=>record.entries.some(entry=>entry.ipa.length>0)).length,
};
const result={
  schemaVersion:1,
  source:"viwiktionary-en",
  sourceSnapshot:String(source.snapshot??"unversioned"),
  sourceSha256,
  records,
  misses,
  metrics,
};
await fsp.mkdir(path.dirname(output),{recursive:true});
await fsp.writeFile(output,stableJson(result),"utf8");
console.log("Vietnamese Wiktionary E03:",JSON.stringify(metrics),"sha256="+sourceSha256);
