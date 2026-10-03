import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { stableJson } from "./english-content-core.mjs";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const sourcePath=path.join(root,"content","english","grammar","topic-catalog.json");
const source=JSON.parse(await fs.readFile(sourcePath,"utf8"));
if (source.schemaVersion!==1||!Array.isArray(source.topics)||source.topics.length!==300) throw new Error("Expected 300-topic authoring catalog v1");
const outputDir=path.join(root,"shared","curriculum");
await fs.mkdir(outputDir,{recursive:true});
await fs.writeFile(path.join(outputDir,"topic-catalog.json"),stableJson(source),"utf8");
const levels=["A1","A2","B1","B2","C1","C2"];
const expected={A1:45,A2:50,B1:60,B2:60,C1:50,C2:35};
const shards=[];
for (const cefr of levels) {
  const topicIds=source.topics.filter(topic=>topic.cefr===cefr).map(topic=>topic.id);
  if (topicIds.length!==expected[cefr]) throw new Error(cefr+" expected "+expected[cefr]+" topics, got "+topicIds.length);
  const file=cefr.toLowerCase()+".json";
  await fs.writeFile(path.join(outputDir,file),stableJson({schemaVersion:1,cefr,topicIds}),"utf8");
  shards.push({id:cefr,path:file,count:topicIds.length});
}
await fs.writeFile(path.join(outputDir,"manifest.json"),stableJson({schemaVersion:1,contentVersion:"2026.10.0",dataset:"curriculum",count:source.topics.length,shards}),"utf8");
console.log("Generated shared curriculum: "+source.topics.length+" topics.");
