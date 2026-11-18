import type { ProductionPreviewDomainAdapter } from "../preview-contract";

export type BossProductionPreviewScenario = "idle" | "phase" | "hit" | "death";
export type BossProductionPreviewCandidate = Readonly<{ bossId: string }>;

export const bossProductionPreviewAdapter: ProductionPreviewDomainAdapter<
  BossProductionPreviewCandidate,
  BossProductionPreviewScenario,
  never
> = Object.freeze({
  domain: "boss",
  defaultScenario: "idle",
  candidatePayload: (candidate: BossProductionPreviewCandidate) => Object.freeze({ domain: "boss", bossId: candidate.bossId }),
  scenarioPayload: (scenario: BossProductionPreviewScenario) => Object.freeze({ scenario }),
});
