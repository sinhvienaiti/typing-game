import { AdminHttpError, requestAdminJson } from "./admin-http";

export type AudioCategoryDefaults = {
  typing: number;
  combat: number;
  warnings: number;
  ui: number;
  rewards: number;
};

export type AudioDefaults = {
  master: number;
  pronunciation: number;
  music: number;
  ambient: number;
  sfx: number;
  /** Legacy revisions may omit this B03 field. Child runtime supports 0..2. */
  credit?: number;
  announcer: number;
  /** Legacy revisions may omit these B03 category preferences. */
  categories?: Partial<AudioCategoryDefaults>;
};

export type PlaylistSelectionMode = "shuffle-bag" | "ordered";
export type PlaylistAssignment =
  | { kind: "inherit" }
  | { kind: "replace"; trackIds: string[]; selectionMode?: PlaylistSelectionMode };
export type WorldMusicBossPolicy = {
  common?: PlaylistAssignment;
  mini?: PlaylistAssignment;
  world?: PlaylistAssignment;
  major?: PlaylistAssignment;
};
export type WorldMusicPolicyEntry = {
  normal?: PlaylistAssignment;
  boss?: WorldMusicBossPolicy;
};
export type WorldMusicPolicy = {
  configRevision: string;
  disabledTrackIds?: string[];
  stages?: Record<string, WorldMusicPolicyEntry>;
  worlds?: Record<string, WorldMusicPolicyEntry>;
  galaxies?: Record<string, WorldMusicPolicyEntry>;
  global?: WorldMusicPolicyEntry;
};

export type GeneralSettingsConfig = {
  gameDefaults: {
    defaultMode: "campaign" | "recall" | "expedition";
    defaultShip: string;
    difficulty: "easy" | "normal" | "hard";
    tutorialEnabled: boolean;
    pronunciationDefault: boolean;
    autoSave: boolean;
  };
  network: {
    minimumVersion: string;
    autoSaveIntervalSeconds: number;
    reconnectWindowSeconds: number;
    offlinePlay: boolean;
    telemetry: boolean;
  };
  maintenance: {
    enabled: boolean;
    message: string;
  };
};

export type FeatureFlagScope = "all" | "new-players" | "cohort" | "environment" | "accounts";
export type FeatureFlagRisk = "normal" | "economy" | "competitive" | "save";
export type FeatureFlagConfig = {
  enabled: boolean;
  rolloutPercent: number;
  scope: FeatureFlagScope;
  risk: FeatureFlagRisk;
};

export type CoreStatKey =
  | "hull"
  | "shield"
  | "firepower"
  | "armor"
  | "energy"
  | "reactor"
  | "focus"
  | "ward"
  | "luck"
  | "salvage";

export type ShipVisualProfile = {
  silhouette: "spear" | "fortress" | "arc" | "phantom" | "crown" | "blade";
  primary: string;
  secondary: string;
  accent: string;
  core: string;
  engine: string;
  glow: string;
  wingSpan: number;
  bodyLength: number;
  engineCount: 1 | 2 | 3;
};

export type ShipAdminOverride = {
  name?: string;
  unlockStage?: number;
  role?: string;
  summary?: string;
  passiveName?: string;
  activeName?: string;
  ultimateName?: string;
  imageAssetVersionId?: string;
  reliefAssetVersionId?: string;
  projectileArchetype?: string;
  statBonus?: Partial<Record<CoreStatKey, number>>;
  visual?: Partial<ShipVisualProfile>;
};

export type ShipAdminPolicy = {
  configRevision: string;
  ships?: Record<string, ShipAdminOverride>;
};

export type ShipAdminPreviewItem = {
  id: string;
  name: string;
  unlockStage: number;
  role: string;
  summary: string;
  passiveName: string;
  activeName: string;
  ultimateName: string;
  imageAssetVersionId?: string;
  reliefAssetVersionId?: string;
  projectileArchetype?: string;
  statBonus: Partial<Record<CoreStatKey, number>>;
  visual: ShipVisualProfile;
  assetId: string;
  overridden: boolean;
};

export type ShipAdminPreview = {
  protocolVersion: 1;
  configRevision: string;
  ships: ShipAdminPreviewItem[];
};

export type SpaceTypingAdminConfig = {
  contractRevision: string;
  configSchemaVersion: number;
  worldMusicCatalogSchemaVersion: number;
  audio: {
    profileId: string;
    defaults: AudioDefaults;
  };
  worldMusic: {
    policyRevision: string;
    assignments: Record<string, unknown>;
    /** Additive B04.2 canonical policy: Global + Galaxy + World + Stage. */
    publishedPolicy?: WorldMusicPolicy;
  };
  /** Additive B06 content namespace; legacy v1 revisions may omit it. */
  content?: {
    ships?: ShipAdminPolicy;
  } & Record<string, unknown>;
  /** Additive Phase B namespace; optional for compatibility with pre-Phase-B local revisions. */
  system?: GeneralSettingsConfig;
  /** Additive Phase B namespace; optional for compatibility with pre-Phase-B local revisions. */
  featureFlags?: Record<string, FeatureFlagConfig>;
};

export type AdminRevisionRelation = "active" | "ancestor" | "draft";

export type AdminRevision = {
  revision: string;
  parentRevision: string | null;
  createdAt: string;
  author: string;
  message: string;
  config: SpaceTypingAdminConfig;
  active?: boolean;
  relation?: AdminRevisionRelation;
  publishable?: boolean;
  rollbackEligible?: boolean;
};

export type AdminChangeScope = {
  model: "whole-config-revision";
  baseRevision: string | null;
  targetRevision: string | null;
  changed: boolean;
  changedPathCount: number;
  truncated: boolean;
  domains: string[];
  changedPaths: string[];
  publishWarning: string;
};

export type AdminRevisionValidation = {
  revision: string;
  valid: true;
  activeRevision: string;
  parentRevision: string | null;
  relation: AdminRevisionRelation;
  publishable: boolean;
  rollbackEligible: boolean;
  changeScope?: AdminChangeScope;
};

export type AdminStatePayload = {
  state: {
    version: number;
    activeRevision: string;
    generation: number;
    updatedAt: string;
  };
  active: AdminRevision;
  history: AdminRevision[];
};

export type AdminRuntimePayload = {
  activeRevision: string;
  config: SpaceTypingAdminConfig;
};

export type AdminActor = {
  actorId: string;
  actorDisplayName: string;
  authMethod: string;
  role: string;
  requestId: string;
  permissions: string[];
};

export type AdminAuditEvent = {
  schemaVersion: number;
  eventId: string;
  timestamp: string;
  actor: null | {
    actorId: string;
    actorDisplayName: string;
    authMethod: string;
    role: string;
  };
  requestId: string | null;
  action: string;
  domain: string;
  entityType: string | null;
  entityId: string | null;
  changeScope: unknown;
  result: "attempt" | "success" | "denied" | "error";
  error: string | null;
};

export type AdminAuditPayload = {
  events: AdminAuditEvent[];
};

export type AdminMusicCatalogSummary = {
  schemaVersion: number;
  manifestRevision: string;
  tracks: Array<{
    id: string;
    title: string;
    uploadedByAdmin: boolean;
  } & Record<string, unknown>>;
};

export type DeveloperToolLink = {
  label: string;
  path: string;
  description: string;
};

export type DeveloperToolSection = {
  id: string;
  label: string;
  description: string;
  tools: DeveloperToolLink[];
};

export type DeveloperToolsManifest = {
  version: 1;
  permission: "developer.runtime-inspect";
  sections: DeveloperToolSection[];
};

export type WorldMusicPreviewState = {
  state: "normal" | "mini" | "world" | "major";
  trackIds: string[];
  tracks: Array<{ id: string; title: string; playbackKind: "single" | "stems" }>;
  trackCount: number;
  selectionMode: "shuffle-bag" | "ordered";
  resolvedFrom: string;
  fallbackTrace: string[];
  badges: string[];
};

export type WorldMusicPreview = {
  protocolVersion: 1;
  configRevision: string;
  manifestRevision: string;
  musicMode: "map" | "random";
  stageNumber?: number;
  worlds: Array<{
    worldId: string;
    name: string;
    galaxy: number;
    stageRange: [number, number];
    states: {
      normal: WorldMusicPreviewState;
      mini: WorldMusicPreviewState;
      world: WorldMusicPreviewState;
      major: WorldMusicPreviewState;
    };
  }>;
};

const TOKEN_KEY = "typing-game:space-admin-token";

export class AdminApiError extends AdminHttpError {
  constructor(status: number, message: string, source?: AdminHttpError) {
    super(message, {
      code: source?.code ?? "http-error",
      method: source?.method ?? "REQUEST",
      path: source?.path ?? "/api/admin/space-typing",
      status,
      contentType: source?.contentType ?? "application/json",
    });
    this.name = "AdminApiError";
  }
}

export class SpaceTypingAdminApi {
  private token = localStorage.getItem(TOKEN_KEY) ?? "local-dev";

  getToken(): string {
    return this.token;
  }

  setToken(token: string): void {
    this.token = token.trim() || "local-dev";
    localStorage.setItem(TOKEN_KEY, this.token);
  }

  requestJson<T>(path: string, init?: RequestInit): Promise<T> {
    return this.request<T>(path, init);
  }

  private async request<T>(path: string, init?: RequestInit): Promise<T> {
    try {
      return await requestAdminJson<T>(path, {
        token: this.token,
        init,
      });
    } catch (error) {
      if (error instanceof AdminHttpError) {
        throw new AdminApiError(error.status, error.message, error);
      }
      throw error;
    }
  }

  getActor(): Promise<AdminActor> {
    return this.request<AdminActor>("/api/admin/space-typing/actor");
  }

  getAudit(limit = 8): Promise<AdminAuditPayload> {
    const safeLimit = Math.max(1, Math.min(100, Math.trunc(limit)));
    return this.request<AdminAuditPayload>(`/api/admin/space-typing/audit?limit=${safeLimit}`);
  }

  getDeveloperToolsManifest(): Promise<DeveloperToolsManifest> {
    return this.request<DeveloperToolsManifest>("/api/admin/space-typing/developer-tools/manifest");
  }

  getMusicCatalogSummary(): Promise<AdminMusicCatalogSummary> {
    return this.request<AdminMusicCatalogSummary>("/api/admin/space-typing/music/library");
  }

  getState(): Promise<AdminStatePayload> {
    return this.request<AdminStatePayload>("/api/admin/space-typing/state");
  }

  getRuntime(): Promise<AdminRuntimePayload> {
    return this.request<AdminRuntimePayload>("/api/admin/space-typing/runtime");
  }

  previewWorldMusic(input: {
    publishedPolicy?: WorldMusicPolicy;
    musicMode?: "map" | "random";
    stageNumber?: number;
  } = {}): Promise<WorldMusicPreview> {
    return this.request<WorldMusicPreview>("/api/admin/space-typing/world-music/preview", {
      method: "POST",
      body: JSON.stringify(input),
    });
  }

  previewShips(input: { policy?: ShipAdminPolicy } = {}): Promise<ShipAdminPreview> {
    return this.request<ShipAdminPreview>("/api/admin/space-typing/ships/preview", {
      method: "POST",
      body: JSON.stringify(input),
    });
  }

  validateRevision(revision: string): Promise<AdminRevisionValidation> {
    return this.request<AdminRevisionValidation>("/api/admin/space-typing/validate-revision", {
      method: "POST",
      body: JSON.stringify({ revision }),
    });
  }

  createRevision(input: {
    baseRevision: string;
    config: SpaceTypingAdminConfig;
    message: string;
  }): Promise<AdminRevision> {
    return this.request<AdminRevision>("/api/admin/space-typing/revisions", {
      method: "POST",
      body: JSON.stringify(input),
    });
  }

  publish(revision: string, expectedActiveRevision: string): Promise<AdminStatePayload["state"]> {
    return this.request<AdminStatePayload["state"]>("/api/admin/space-typing/publish", {
      method: "POST",
      body: JSON.stringify({ revision, expectedActiveRevision }),
    });
  }

  rollback(targetRevision: string, expectedActiveRevision: string): Promise<AdminStatePayload["state"]> {
    return this.request<AdminStatePayload["state"]>("/api/admin/space-typing/rollback", {
      method: "POST",
      body: JSON.stringify({ targetRevision, expectedActiveRevision }),
    });
  }
}