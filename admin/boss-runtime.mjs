import { validateBossPolicy } from "./boss-policy.mjs";

const DEFAULT_BOSS_POLICY = {
  configRevision: "bosses-admin-v1",
  bosses: {},
};

export function createBossRuntimeEnvelope(state, config, contract) {
  const policy = structuredClone(config.content?.bosses ?? DEFAULT_BOSS_POLICY);
  validateBossPolicy(policy, contract.bosses);
  return {
    protocolVersion: 1,
    activeRevision: state.activeRevision,
    applyBoundary: contract.applyBoundaries?.bossPolicy ?? "new-session",
    policy,
  };
}
