import { validateSkillPolicy } from "./skill-policy.mjs";

const DEFAULT_SKILL_POLICY = {
  configRevision: "skills-admin-v1",
  skills: {},
};

export function createSkillRuntimeEnvelope(state, config, contract) {
  const policy = structuredClone(config.content?.skills ?? DEFAULT_SKILL_POLICY);
  validateSkillPolicy(policy, contract.skills);
  return {
    protocolVersion: 1,
    activeRevision: state.activeRevision,
    applyBoundary: contract.applyBoundaries?.skillPolicy ?? "new-session",
    policy,
  };
}
