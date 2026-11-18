import type { ProductionPreviewDomainAdapter } from "../preview-contract";

export type StageProductionPreviewScenario = "idle";
export type StageProductionPreviewCandidate = Readonly<{ stage: number }>;

export const stageProductionPreviewAdapter: ProductionPreviewDomainAdapter<
  StageProductionPreviewCandidate,
  StageProductionPreviewScenario,
  never
> = Object.freeze({
  domain: "stage",
  defaultScenario: "idle",
  candidatePayload: (candidate: StageProductionPreviewCandidate) => Object.freeze({ domain: "stage", stage: candidate.stage }),
  scenarioPayload: () => Object.freeze({ scenario: "idle" }),
});
