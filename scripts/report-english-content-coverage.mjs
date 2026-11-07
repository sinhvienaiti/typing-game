import path from "node:path";
import { fileURLToPath } from "node:url";
import { readJson } from "./english-content-core.mjs";
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const catalog=await readJson(path.join(root,"shared","curriculum","topic-catalog.json"));
const manifests={};
for (const name of ["dictionary","phrases","grammar","sentences","curriculum"]) manifests[name]=await readJson(path.join(root,"shared",name,"manifest.json"));
const counts=Object.fromEntries(["A1","A2","B1","B2","C1","C2"].map(level=>[level,catalog.topics.filter(topic=>topic.cefr===level).length]));
console.log(JSON.stringify({curriculumTopics:catalog.topics.length,topicsByCefr:counts,runtimeCounts:Object.fromEntries(Object.entries(manifests).map(([key,value])=>[key,value.count]))},null,2));
