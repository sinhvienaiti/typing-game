import test from "node:test";
import assert from "node:assert/strict";
import { validateEquipmentPolicy, EquipmentPolicyValidationError } from "./equipment-policy.mjs";

const contract = {
  ids: ["pulse-laser-mk1", "arc-projector-mk2"],
  authorableFields: ["name", "description", "stats", "perk"],
  coreStatKeys: ["hull", "shield", "firepower", "armor", "energy", "reactor", "focus", "ward", "luck", "salvage"],
  perkIds: ["arc-emitter"],
  constraints: {
    nameMax: 100,
    descriptionMax: 320,
    statBonus: { min: -100, max: 100 },
  },
};

test("accepts canonical equipment overrides", () => {
  assert.doesNotThrow(() => validateEquipmentPolicy({
    configRevision: "equipment-admin-v1",
    equipment: {
      "arc-projector-mk2": {
        name: "Arc Projector Admin",
        description: "Reviewed description",
        stats: { firepower: 20, focus: 5 },
        perk: "arc-emitter",
      },
    },
  }, contract));
});

test("accepts explicit perk removal", () => {
  assert.doesNotThrow(() => validateEquipmentPolicy({
    configRevision: "equipment-admin-v1",
    equipment: { "arc-projector-mk2": { perk: null } },
  }, contract));
});

test("rejects unknown ids, fields, stats and perks", () => {
  for (const policy of [
    { configRevision: "equipment-admin-v1", equipment: { unknown: { name: "Nope" } } },
    { configRevision: "equipment-admin-v1", equipment: { "pulse-laser-mk1": { tier: 3 } } },
    { configRevision: "equipment-admin-v1", equipment: { "pulse-laser-mk1": { stats: { speed: 5 } } } },
    { configRevision: "equipment-admin-v1", equipment: { "arc-projector-mk2": { perk: "bad-perk" } } },
  ]) {
    assert.throws(() => validateEquipmentPolicy(policy, contract), EquipmentPolicyValidationError);
  }
});
