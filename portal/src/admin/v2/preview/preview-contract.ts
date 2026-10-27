export type ProductionPreviewSource = "draft" | "published";
export type ProductionPreviewLifecycle = "loading" | "ready" | "error" | "unsupported";

export type ProductionPreviewLifecycleState = Readonly<{
  status: ProductionPreviewLifecycle;
  message: string;
}>;

export interface ProductionPreviewDomainAdapter<TCandidate, TScenario extends string, TTuning = Readonly<Record<string, unknown>>> {
  readonly domain: string;
  readonly defaultScenario: TScenario;
  candidatePayload(candidate: TCandidate): Readonly<Record<string, unknown>>;
  scenarioPayload(scenario: TScenario): Readonly<Record<string, unknown>>;
  tuningPayload?(tuning: TTuning): Readonly<Record<string, unknown>>;
}

export type ProductionPreviewStudioActions = Readonly<{
  reset: () => void | Promise<void>;
  replay: () => void | Promise<void>;
}>;
