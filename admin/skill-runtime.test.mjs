import test from "node:test";
import assert from "node:assert/strict";
import { createSkillRuntimeEnvelope } from "./skill-runtime.mjs";

const contract = {
  skills: {
    ids: ["barrier"],
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
  },
  applyBoundaries: { skillPolicy: "new-session" },
};

test("builds a published Skill runtime envelope", () => {
  const envelope = createSkillRuntimeEnvelope(
    { activeRevision: "r7" },
    { content: { skills: { configRevision: "skills-admin-test", skills: { barrier: { energyCost: 24 } } } } },
    contract,
  );
  assert.deepEqual(envelope, {
    protocolVersion: 1,
    activeRevision: "r7",
    applyBoundary: "new-session",
    policy: {
      configRevision: "skills-admin-test",
      skills: { barrier: { energyCost: 24 } },
    },
  });
});

test("uses the safe empty Skill policy for legacy revisions", () => {
  const envelope = createSkillRuntimeEnvelope({ activeRevision: "legacy" }, {}, contract);
  assert.equal(envelope.policy.configRevision, "skills-admin-v1");
  assert.deepEqual(envelope.policy.skills, {});
});
