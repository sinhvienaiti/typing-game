import type { ProductionPreviewDomainAdapter } from "../preview-contract";

export type WorldProductionPreviewScenario = "idle";
export type WorldProductionPreviewCandidate = Readonly<{ worldId: string }>;

export const worldProductionPreviewAdapter: ProductionPreviewDomainAdapter<
  WorldProductionPreviewCandidate,
  WorldProductionPreviewScenario,
  never
> = Object.freeze({
  domain: "world",
  defaultScenario: "idle",
  candidatePayload: (candidate: WorldProductionPreviewCandidate) => Object.freeze({ domain: "world", worldId: candidate.worldId }),
  scenarioPayload: () => Object.freeze({ scenario: "idle" }),
});
