import test from "node:test";
import assert from "node:assert/strict";
import { WorldPolicyValidationError, validateWorldPolicy } from "./world-policy.mjs";

const worlds = { count:50, authorableFields:["enemyRoster"], constraints:{enemyRoster:{minItems:1,maxItems:64,unique:true}} };
const enemies = { ids:["rainbow-scout","rainbow-dart","imp-spark"] };

test("accepts canonical World roster overrides", () => {
  assert.equal(validateWorldPolicy({configRevision:"worlds-test",worlds:{"world-01":{enemyRoster:["rainbow-dart"]}}},worlds,enemies).configRevision,"worlds-test");
});

test("rejects unknown Worlds, enemy IDs, duplicates and unsupported fields", () => {
  assert.throws(() => validateWorldPolicy({configRevision:"worlds-test",worlds:{"world-51":{enemyRoster:["rainbow-dart"]}}},worlds,enemies), WorldPolicyValidationError);
  assert.throws(() => validateWorldPolicy({configRevision:"worlds-test",worlds:{"world-01":{enemyRoster:["missing"]}}},worlds,enemies), /Unknown enemy/);
  assert.throws(() => validateWorldPolicy({configRevision:"worlds-test",worlds:{"world-01":{enemyRoster:["rainbow-dart","rainbow-dart"]}}},worlds,enemies), /Duplicate enemy/);
  assert.throws(() => validateWorldPolicy({configRevision:"worlds-test",worlds:{"world-01":{enemyRoster:["rainbow-dart"],name:"X"}}},worlds,enemies), /not authorable/);
});
