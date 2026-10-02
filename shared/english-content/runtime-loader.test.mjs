import test from "node:test";
import assert from "node:assert/strict";
import {createEnglishRuntimeLoader,parseRuntimeManifest} from "./runtime-loader.mjs";
import {datasetForEnglishContentId,createEnglishReviewItemResolver} from "./review-item.mjs";
import {supportsEnglishActivity,listEnglishActivities} from "./capabilities.mjs";

test("runtime manifest validates counts",()=>{
  assert.equal(parseRuntimeManifest({schemaVersion:1,contentVersion:"2026.10.0",dataset:"phrases",count:2,shards:[{id:"p-0",path:"p/000.json",count:2}]},"phrases").count,2);
  assert.throws(()=>parseRuntimeManifest({schemaVersion:1,contentVersion:"x",dataset:"phrases",count:2,shards:[]},"phrases"));
});
test("runtime loader caches bounded manifest and shard",async()=>{
  const calls=[];
  const payloads={
    "/shared/phrases/manifest.json":{schemaVersion:1,contentVersion:"2026.10.0",dataset:"phrases",count:1,shards:[{id:"phrases-000",path:"items/000.json",count:1}]},
    "/shared/phrases/items/000.json":{schemaVersion:1,records:[{id:"pv.00000001",text:"get up"}]}
  };
  const fetcher=async input=>{calls.push(input);return {ok:true,status:200,json:async()=>payloads[input]};};
  const loader=createEnglishRuntimeLoader({fetcher});
  assert.equal((await loader.loadDataset("phrases")).length,1);
  assert.equal((await loader.loadDataset("phrases")).length,1);
  assert.equal(calls.length,2);
});
test("review item routes stable ids",async()=>{
  assert.equal(datasetForEnglishContentId("col.00000001"),"phrases");
  assert.equal(datasetForEnglishContentId("gr.a1.x"),"grammar");
  assert.equal(datasetForEnglishContentId("unknown.x"),null);
  const resolver=createEnglishReviewItemResolver({findById:async(dataset,id)=>dataset==="phrases"?{id}:null});
  assert.equal((await resolver("pv.00000001")).dataset,"phrases");
});
test("capability routing is explicit per game",()=>{
  assert.equal(supportsEnglishActivity("monkeytype","sentence-building"),true);
  assert.equal(supportsEnglishActivity("shooter","sentence-building"),false);
  assert.ok(listEnglishActivities("space").includes("grammar-challenge"));
});
