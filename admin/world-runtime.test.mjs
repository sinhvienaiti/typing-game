import test from "node:test";
import assert from "node:assert/strict";
import { createWorldRuntimeEnvelope } from "./world-runtime.mjs";

const contract={worlds:{count:50,authorableFields:["enemyRoster"],constraints:{enemyRoster:{minItems:1,maxItems:64,unique:true}}},enemies:{ids:["rainbow-dart"]},applyBoundaries:{worldPolicy:"new-session"}};

test("runtime envelope exposes only published World policy with boundary",()=>{
  const result=createWorldRuntimeEnvelope({activeRevision:"rev-2"},{content:{worlds:{configRevision:"worlds-v2",worlds:{"world-01":{enemyRoster:["rainbow-dart"]}}}}},contract);
  assert.equal(result.protocolVersion,1); assert.equal(result.activeRevision,"rev-2"); assert.equal(result.applyBoundary,"new-session"); assert.deepEqual(result.policy.worlds["world-01"].enemyRoster,["rainbow-dart"]);
});

test("runtime envelope has deterministic bundled fallback",()=>{
  const result=createWorldRuntimeEnvelope({activeRevision:"rev-1"},{},contract);
  assert.deepEqual(result.policy,{configRevision:"worlds-admin-v1",worlds:{}});
});
