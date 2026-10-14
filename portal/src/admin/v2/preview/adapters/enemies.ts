import type { ProductionPreviewDomainAdapter } from "../preview-contract";

export type EnemyProductionPreviewScenario = "idle" | "hit" | "death";

export type EnemyProductionPreviewCandidate = Readonly<{
  definitionId: string;
}>;

export const enemyProductionPreviewAdapter: ProductionPreviewDomainAdapter<
  EnemyProductionPreviewCandidate,
  EnemyProductionPreviewScenario,
  never
> = Object.freeze({
  domain: "enemy",
  defaultScenario: "idle",
  candidatePayload: (candidate) => Object.freeze({
    domain: "enemy",
    definitionId: candidate.definitionId,
  }),
  scenarioPayload: (scenario) => Object.freeze({ scenario }),
});
