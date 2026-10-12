import test from "node:test";
import assert from "node:assert/strict";
import { createStageRuntimeEnvelope } from "./stage-runtime.mjs";

const contract={stages:{authorableFields:["enemyBudget","eliteChance","modifierSlots"],constraints:{stage:{min:1,max:1000,integer:true},enemyBudget:{minExclusive:0},eliteChance:{min:0,max:1},modifierSlots:{min:0,max:4,integer:true}}},applyBoundaries:{stagePolicy:"new-session"}};

test("runtime envelope exposes published Stage policy and authoritative difficulty with boundary",()=>{
  const result=createStageRuntimeEnvelope({activeRevision:"rev-2"},{system:{gameDefaults:{difficulty:"hard"}},content:{stages:{configRevision:"stages-v2",stages:[{stage:37,enemyBudget:88,eliteChance:0.33,modifierSlots:3}]}}},contract);
  assert.equal(result.protocolVersion,1); assert.equal(result.activeRevision,"rev-2"); assert.equal(result.applyBoundary,"new-session"); assert.deepEqual(result.gameDefaults,{difficulty:"hard"}); assert.equal(result.policy.stages[0].enemyBudget,88);
});

test("runtime envelope has deterministic bundled fallback",()=>{
  const result=createStageRuntimeEnvelope({activeRevision:"rev-1"},{},contract);
  assert.deepEqual(result.gameDefaults,{difficulty:"normal"});
  assert.deepEqual(result.policy,{configRevision:"stages-admin-v1",stages:[]});
});

test("runtime envelope rejects unknown difficulty values to the safe normal default",()=>{
  const result=createStageRuntimeEnvelope({activeRevision:"rev-3"},{system:{gameDefaults:{difficulty:"custom-client-value"}}},contract);
  assert.deepEqual(result.gameDefaults,{difficulty:"normal"});
});
