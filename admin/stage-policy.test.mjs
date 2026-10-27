import test from "node:test";
import assert from "node:assert/strict";
import { StagePolicyValidationError, validateStagePolicy } from "./stage-policy.mjs";

const contract = {
  authorableFields: ["enemyBudget", "eliteChance", "modifierSlots"],
  constraints: {
    stage: { min: 1, max: 1000, integer: true },
    enemyBudget: { minExclusive: 0 },
    eliteChance: { min: 0, max: 1 },
    modifierSlots: { min: 0, max: 4, integer: true },
  },
};

test("accepts canonical Stage gameplay overrides", () => {
  const policy = { configRevision:"stages-test", stages:[{ stage:37, enemyBudget:88, eliteChance:0.33, modifierSlots:3 }] };
  assert.equal(validateStagePolicy(policy, contract), policy);
});

test("accepts empty Stage overrides", () => assert.doesNotThrow(() => validateStagePolicy({ configRevision:"stages-test", stages:[] }, contract)));

test("rejects stage range errors, duplicates and structural fields", () => {
  assert.throws(() => validateStagePolicy({ configRevision:"stages-test", stages:[{stage:0,enemyBudget:40}] }, contract), StagePolicyValidationError);
  assert.throws(() => validateStagePolicy({ configRevision:"stages-test", stages:[{stage:12,enemyBudget:40},{stage:12,enemyBudget:41}] }, contract), /Duplicate stage/);
  assert.throws(() => validateStagePolicy({ configRevision:"stages-test", stages:[{stage:12,role:"boss"}] }, contract), /not authorable/);
});

test("rejects malformed gameplay values and empty records", () => {
  assert.throws(() => validateStagePolicy({ configRevision:"stages-test", stages:[{stage:12,enemyBudget:0}] }, contract), /greater than/);
  assert.throws(() => validateStagePolicy({ configRevision:"stages-test", stages:[{stage:12,eliteChance:1.1}] }, contract), /between/);
  assert.throws(() => validateStagePolicy({ configRevision:"stages-test", stages:[{stage:12,modifierSlots:2.5}] }, contract), /integer/);
  assert.throws(() => validateStagePolicy({ configRevision:"stages-test", stages:[{stage:12}] }, contract), /at least one/);
});
