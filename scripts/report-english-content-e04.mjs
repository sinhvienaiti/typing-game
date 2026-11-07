import path from "node:path";
import{fileURLToPath}from"node:url";
import{readJson}from"./english-content-core.mjs";
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const manifest=await readJson(path.join(root,"shared","phrases","manifest.json"));
const records=[];
for(const shard of manifest.shards??[]){const doc=await readJson(path.join(root,"shared","phrases",shard.path));records.push(...(doc.records??[]));}
const collocations=records.filter(x=>String(x.id??"").startsWith("col."));
const verbPatterns=records.filter(x=>String(x.id??"").startsWith("pat."));
const phraseItems=records.filter(x=>/^(pv|chunk|idiom)\./u.test(String(x.id??"")));
const report={total:records.length,collocations:collocations.length,verbPatterns:verbPatterns.length,phrasalVerbs:phraseItems.filter(x=>x.type==="phrasal-verb").length,chunks:phraseItems.filter(x=>x.type==="chunk").length,idioms:phraseItems.filter(x=>x.type==="idiom").length,published:records.filter(x=>x.quality?.state==="published").length,withExamples:{collocations:collocations.filter(x=>(x.exampleIds??[]).length>0).length,verbPatterns:verbPatterns.filter(x=>(x.exampleIds??[]).length>0).length,phraseItems:phraseItems.filter(x=>(x.exampleIds??[]).length>0).length}};
console.log(JSON.stringify(report,null,2));
