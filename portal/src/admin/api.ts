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
  worlds?: Record<string, WorldMusicPolicyEntry>;
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
    /** Additive B04.1 canonical policy. Child v1 currently supports Global + World only. */
    publishedPolicy?: WorldMusicPolicy;
  };
  /** Additive Phase B namespace; optional for compatibility with pre-Phase-B local revisions. */
  system?: GeneralSettingsConfig;
  /** Additive Phase B namespace; optional for compatibility with pre-Phase-B local revisions. */
  featureFlags?: Record<string, FeatureFlagConfig>;
};

export type AdminRevision = {
  revision: string;
  parentRevision: string | null;
  createdAt: string;
  author: string;
  message: string;
  config: SpaceTypingAdminConfig;
  active?: boolean;
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

export class AdminApiError extends Error {
  readonly status: number;

  constructor(status: number, message: string) {
    super(message);
    this.status = status;
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

  private async request<T>(path: string, init?: RequestInit): Promise<T> {
    const response = await fetch(path, {
      ...init,
      cache: "no-store",
      headers: {
        "content-type": "application/json",
        "x-typing-game-admin-token": this.token,
        ...(init?.headers ?? {}),
      },
    });
    const payload = (await response.json().catch(() => ({}))) as Record<string, unknown>;
    if (!response.ok) {
      const message =
        typeof payload["message"] === "string"
          ? payload["message"]
          : typeof payload["error"] === "string"
            ? payload["error"]
            : `Admin request failed (${response.status})`;
      throw new AdminApiError(response.status, message);
    }
    return payload as T;
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
  } = {}): Promise<WorldMusicPreview> {
    return this.request<WorldMusicPreview>("/api/admin/space-typing/world-music/preview", {
      method: "POST",
      body: JSON.stringify(input),
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
