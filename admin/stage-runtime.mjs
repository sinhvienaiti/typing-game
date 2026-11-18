import { validateStagePolicy } from "./stage-policy.mjs";

const DEFAULT_STAGE_POLICY = {
  configRevision: "stages-admin-v1",
  stages: [],
};

const ADMIN_DIFFICULTIES = new Set(["easy", "normal", "hard"]);

function runtimeGameDefaults(config) {
  const difficulty = config.system?.gameDefaults?.difficulty;
  return {
    difficulty: ADMIN_DIFFICULTIES.has(difficulty) ? difficulty : "normal",
  };
}

export function createStageRuntimeEnvelope(state, config, contract) {
  const policy = structuredClone(config.content?.stages ?? DEFAULT_STAGE_POLICY);
  validateStagePolicy(policy, contract.stages);
  return {
    protocolVersion: 1,
    activeRevision: state.activeRevision,
    applyBoundary: contract.applyBoundaries?.stagePolicy ?? "new-session",
    gameDefaults: runtimeGameDefaults(config),
    policy,
  };
}
