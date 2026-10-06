import test from "node:test";
import assert from "node:assert/strict";
import { SkillPolicyValidationError, validateSkillPolicy } from "./skill-policy.mjs";

const contract = {
  ids: ["barrier", "chain-lightning"],
  authorableFields: ["name", "description", "energyCost", "cooldown", "charges", "perStageLimit", "typingCondition"],
  constraints: {
    nameMax: 100,
    descriptionMax: 320,
    energyCost: { min: 0, max: 200 },
    cooldown: { min: 0, max: 300 },
    charges: { min: 0, max: 99, integer: true, nullable: true },
    perStageLimit: { min: 0, max: 99, integer: true, nullable: true },
    typingCondition: {
      minStreak: { min: 0, max: 999, integer: true },
      minAccuracy: { min: 0, max: 100 },
    },
  },
};

test("accepts canonical Skill overrides", () => {
  assert.equal(validateSkillPolicy({
    configRevision: "skills-admin-test",
    skills: {
      barrier: {
        name: "Hex Shield Mk.II",
        energyCost: 24,
        cooldown: 8.5,
        charges: 5,
        perStageLimit: 5,
        typingCondition: { minStreak: 10, minAccuracy: 95 },
      },
    },
  }, contract).configRevision, "skills-admin-test");
});

test("accepts nullable charges, limits and typing-condition removal", () => {
  assert.doesNotThrow(() => validateSkillPolicy({
    configRevision: "skills-admin-test",
    skills: { barrier: { charges: null, perStageLimit: null, typingCondition: null } },
  }, contract));
});

test("rejects unknown IDs, immutable fields and invalid bounds", () => {
  assert.throws(() => validateSkillPolicy({
    configRevision: "skills-admin-test",
    skills: { unknown: { energyCost: 20 } },
  }, contract), SkillPolicyValidationError);
  assert.throws(() => validateSkillPolicy({
    configRevision: "skills-admin-test",
    skills: { barrier: { category: "support" } },
  }, contract), /not authorable/);
  assert.throws(() => validateSkillPolicy({
    configRevision: "skills-admin-test",
    skills: { barrier: { energyCost: 201 } },
  }, contract), /energyCost/);
  assert.throws(() => validateSkillPolicy({
    configRevision: "skills-admin-test",
    skills: { barrier: { typingCondition: { minAccuracy: 101 } } },
  }, contract), /minAccuracy/);
});
