import type { ProductionPreviewDomainAdapter } from "../preview-contract";

export type ShipProductionPreviewScenario = "idle" | "move" | "fire";
export type ShipProductionPreviewSource = "draft" | "published";

export type ShipProductionPreviewCandidate = Readonly<{
  characterId: string;
  visual: Readonly<Record<string, unknown>>;
  imageAssetVersionId?: string;
  reliefAssetVersionId?: string | null;
  projectileArchetype?: string;
}>;

export const shipProductionPreviewAdapter: ProductionPreviewDomainAdapter<
  ShipProductionPreviewCandidate,
  ShipProductionPreviewScenario,
  Readonly<Record<string, unknown>>
> = Object.freeze({
  domain: "ship",
  defaultScenario: "idle",
  candidatePayload: (candidate) => Object.freeze({
    domain: "ship",
    characterId: candidate.characterId,
    visual: candidate.visual,
    ...(candidate.imageAssetVersionId === undefined
      ? {}
      : { imageAssetVersionId: candidate.imageAssetVersionId }),
    ...(candidate.reliefAssetVersionId === undefined
      ? {}
      : { reliefAssetVersionId: candidate.reliefAssetVersionId }),
    ...(candidate.projectileArchetype === undefined
      ? {}
      : { projectileArchetype: candidate.projectileArchetype }),
  }),
  scenarioPayload: (scenario) => Object.freeze({ scenario }),
  tuningPayload: (visual) => Object.freeze({ visual }),
});
