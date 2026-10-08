import { validateStagePolicy } from "./stage-policy.mjs";

const DEFAULT_STAGE_POLICY = {
  configRevision: "stages-admin-v1",
  stages: [],
};

export function createStageRuntimeEnvelope(state, config, contract) {
  const policy = structuredClone(config.content?.stages ?? DEFAULT_STAGE_POLICY);
  validateStagePolicy(policy, contract.stages);
  return {
    protocolVersion: 1,
    activeRevision: state.activeRevision,
    applyBoundary: contract.applyBoundaries?.stagePolicy ?? "new-session",
    policy,
  };
}
