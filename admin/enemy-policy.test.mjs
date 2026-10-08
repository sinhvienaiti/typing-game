import test from "node:test";
import assert from "node:assert/strict";
import { EnemyPolicyValidationError, validateEnemyPolicy } from "./enemy-policy.mjs";

const contract = {
  ids: ["rainbow-scout", "rainbow-dart"],
  authorableFields: ["minStage"],
  constraints: {
    minStage: { min: 1, max: 1000, integer: true },
  },
};

test("accepts canonical Enemy stage-admission overrides", () => {
  assert.equal(validateEnemyPolicy({
    configRevision: "enemies-admin-test",
    enemies: {
      "rainbow-dart": { minStage: 25 },
    },
  }, contract).configRevision, "enemies-admin-test");
});

test("accepts an empty Enemy override set", () => {
  assert.doesNotThrow(() => validateEnemyPolicy({
    configRevision: "enemies-admin-test",
    enemies: {},
  }, contract));
});

test("rejects unknown IDs, unsupported tuning fields and invalid stage bounds", () => {
  assert.throws(() => validateEnemyPolicy({
    configRevision: "enemies-admin-test",
    enemies: { unknown: { minStage: 20 } },
  }, contract), EnemyPolicyValidationError);
  assert.throws(() => validateEnemyPolicy({
    configRevision: "enemies-admin-test",
    enemies: { "rainbow-scout": { hp: 100 } },
  }, contract), /not authorable/);
  assert.throws(() => validateEnemyPolicy({
    configRevision: "enemies-admin-test",
    enemies: { "rainbow-scout": { minStage: 0 } },
  }, contract), /minStage/);
  assert.throws(() => validateEnemyPolicy({
    configRevision: "enemies-admin-test",
    enemies: { "rainbow-scout": { minStage: 10.5 } },
  }, contract), /integer/);
  assert.throws(() => validateEnemyPolicy({
    configRevision: "enemies-admin-test",
    enemies: { "rainbow-scout": { minStage: 1001 } },
  }, contract), /minStage/);
});