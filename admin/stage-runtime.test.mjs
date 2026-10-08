import test from "node:test";
import assert from "node:assert/strict";
import { createStageRuntimeEnvelope } from "./stage-runtime.mjs";

const contract={stages:{authorableFields:["enemyBudget","eliteChance","modifierSlots"],constraints:{stage:{min:1,max:1000,integer:true},enemyBudget:{minExclusive:0},eliteChance:{min:0,max:1},modifierSlots:{min:0,max:4,integer:true}}},applyBoundaries:{stagePolicy:"new-session"}};

test("runtime envelope exposes only published Stage policy with boundary",()=>{
  const result=createStageRuntimeEnvelope({activeRevision:"rev-2"},{content:{stages:{configRevision:"stages-v2",stages:[{stage:37,enemyBudget:88,eliteChance:0.33,modifierSlots:3}]}}},contract);
  assert.equal(result.protocolVersion,1); assert.equal(result.activeRevision,"rev-2"); assert.equal(result.applyBoundary,"new-session"); assert.equal(result.policy.stages[0].enemyBudget,88);
});

test("runtime envelope has deterministic bundled fallback",()=>{
  const result=createStageRuntimeEnvelope({activeRevision:"rev-1"},{},contract);
  assert.deepEqual(result.policy,{configRevision:"stages-admin-v1",stages:[]});
});
