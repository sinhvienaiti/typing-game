import { validateWorldPolicy } from "./world-policy.mjs";

const DEFAULT_WORLD_POLICY = { configRevision: "worlds-admin-v1", worlds: {} };

export function createWorldRuntimeEnvelope(state, config, contract) {
  const policy = structuredClone(config.content?.worlds ?? DEFAULT_WORLD_POLICY);
  validateWorldPolicy(policy, contract.worlds, contract.enemies);
  return {
    protocolVersion: 1,
    activeRevision: state.activeRevision,
    applyBoundary: contract.applyBoundaries?.worldPolicy ?? "new-session",
    policy,
  };
}
