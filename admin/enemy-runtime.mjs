import { validateEnemyPolicy } from "./enemy-policy.mjs";

const DEFAULT_ENEMY_POLICY = {
  configRevision: "enemies-admin-v1",
  enemies: {},
};

export function createEnemyRuntimeEnvelope(state, config, contract) {
  const policy = structuredClone(config.content?.enemies ?? DEFAULT_ENEMY_POLICY);
  validateEnemyPolicy(policy, contract.enemies);
  return {
    protocolVersion: 1,
    activeRevision: state.activeRevision,
    applyBoundary: contract.applyBoundaries?.enemyPolicy ?? "new-session",
    policy,
  };
}
