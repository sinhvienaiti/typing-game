import { validateWorldPolicy } from "./world-policy.mjs";

const DEFAULT_WORLD_POLICY = { configRevision: "worlds-admin-v1", worlds: {} };
const DEFAULT_TESTING_POLICY = Object.freeze({
  unlockAllStages: false,
  unlockAllShips: true,
});

function testingPolicy(config) {
  const testing = config?.system?.testing;
  return {
    unlockAllStages: testing?.unlockAllStages === true,
    unlockAllShips:
      typeof testing?.unlockAllShips === "boolean"
        ? testing.unlockAllShips
        : DEFAULT_TESTING_POLICY.unlockAllShips,
  };
}

export function createWorldRuntimeEnvelope(state, config, contract) {
  const policy = structuredClone(config.content?.worlds ?? DEFAULT_WORLD_POLICY);
  validateWorldPolicy(policy, contract.worlds, contract.enemies);
  return {
    protocolVersion: 1,
    activeRevision: state.activeRevision,
    applyBoundary: contract.applyBoundaries?.worldPolicy ?? "new-session",
    policy,
    testing: testingPolicy(config),
  };
}