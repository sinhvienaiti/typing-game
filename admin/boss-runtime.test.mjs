import test from "node:test";
import assert from "node:assert/strict";
import { createBossRuntimeEnvelope } from "./boss-runtime.mjs";

const contract={bosses:{ids:["tyrant-g01"],authorableFields:["name","title"],constraints:{nameMax:100,titleMax:160}},applyBoundaries:{bossPolicy:"new-session"}};

test("runtime envelope exposes only published Boss policy with boundary",()=>{
  const result=createBossRuntimeEnvelope({activeRevision:"rev-2"},{content:{bosses:{configRevision:"bosses-v2",bosses:{"tyrant-g01":{name:"Nova",title:"The First"}}}}},contract);
  assert.equal(result.protocolVersion,1); assert.equal(result.activeRevision,"rev-2"); assert.equal(result.applyBoundary,"new-session"); assert.equal(result.policy.bosses["tyrant-g01"].name,"Nova");
});

test("runtime envelope has deterministic bundled fallback",()=>{
  const result=createBossRuntimeEnvelope({activeRevision:"rev-1"},{},contract);
  assert.deepEqual(result.policy,{configRevision:"bosses-admin-v1",bosses:{}});
});
