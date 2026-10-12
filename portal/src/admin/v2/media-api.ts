import { SpaceTypingAdminApi } from "../api";

export type MediaKind = "image" | "model" | "music" | "sfx" | "audio" | "data";
export type MediaLifecycle = "active" | "archived";
export type MediaProvenance = "admin-upload" | "generated-runtime" | "code-owned" | "external-reference";
export type MediaStorageClass = "admin-blob" | "runtime-reference" | "source-reference" | "external-reference";

export type MediaComponent = {
  role: string;
  mimeType: string;
  format?: string;
  byteSize?: number;
  sha256?: string;
  storageClass: MediaStorageClass;
  storageKey?: string;
  runtimeUrl?: string;
  sourcePath?: string;
  width?: number;
  height?: number;
  durationSeconds?: number;
};

export type MediaAsset = {
  assetId: string;
  kind: MediaKind;
  title: string;
  lifecycle: MediaLifecycle;
  currentVersionId: string | null;
  tags: string[];
  createdAt: string;
  createdBy: string;
  updatedAt: string;
  updatedBy: string;
  versionCount?: number;
  referenceCount?: number;
};

export type MediaVersion = {
  assetVersionId: string;
  assetId: string;
  provenance: MediaProvenance;
  storageClass: MediaStorageClass;
  contentFingerprint: string;
  components: MediaComponent[];
  source: {
    owner?: string;
    generator?: string;
    sourcePath?: string;
    license?: string;
    note?: string;
  };
  createdAt: string;
  createdBy: string;
};

export type MediaReference = {
  referenceId: string;
  assetId: string;
  assetVersionId: string;
  domain: string;
  entityType: string;
  entityId: string;
  field: string;
  revisionId?: string;
  createdAt: string;
  createdBy: string;
};

export type MediaAssetListPayload = {
  schemaVersion: 1;
  assets: MediaAsset[];
};

export type MediaAssetDetailPayload = {
  schemaVersion: 1;
  asset: MediaAsset;
  versions: MediaVersion[];
  references: MediaReference[];
};

export type MediaVersionDetailPayload = {
  schemaVersion: 1;
  version: MediaVersion;
  references: MediaReference[];
};

export type MediaMutationPayload = {
  asset: MediaAsset;
  version: MediaVersion;
};

export type MediaPreviewHandle = {
  url: string;
  revoke: () => void;
};

export type MediaAssetQuery = {
  kind?: MediaKind | "all";
  query?: string;
  includeArchived?: boolean;
};

export type CreateMediaAssetInput = {
  kind: MediaKind;
  title: string;
  tags?: string[];
};

const MEDIA_BASE = "/api/admin/space-typing/media";

function encode(value: string): string {
  return encodeURIComponent(value);
}

function mediaErrorMessage(payload: unknown, fallback: string): string {
  if (payload && typeof payload === "object") {
    const record = payload as Record<string, unknown>;
    if (typeof record.message === "string" && record.message.trim()) return record.message.trim();
    if (typeof record.error === "string" && record.error.trim()) return record.error.trim();
  }
  return fallback;
}

export class MediaAdminApi {
  constructor(private readonly admin = new SpaceTypingAdminApi()) {}

  listAssets(query: MediaAssetQuery = {}): Promise<MediaAssetListPayload> {
    const params = new URLSearchParams();
    if (query.kind && query.kind !== "all") params.set("kind", query.kind);
    if (query.query?.trim()) params.set("q", query.query.trim());
    if (query.includeArchived) params.set("includeArchived", "true");
    const suffix = params.size ? `?${params.toString()}` : "";
    return this.admin.requestJson<MediaAssetListPayload>(`${MEDIA_BASE}/assets${suffix}`);
  }

  getAsset(assetId: string): Promise<MediaAssetDetailPayload> {
    return this.admin.requestJson<MediaAssetDetailPayload>(`${MEDIA_BASE}/assets/${encode(assetId)}`);
  }

  getVersion(assetVersionId: string): Promise<MediaVersionDetailPayload> {
    return this.admin.requestJson<MediaVersionDetailPayload>(`${MEDIA_BASE}/versions/${encode(assetVersionId)}`);
  }

  createAsset(file: File, input: CreateMediaAssetInput): Promise<MediaMutationPayload> {
    return this.admin.requestJson<MediaMutationPayload>(`${MEDIA_BASE}/assets`, {
      method: "POST",
      headers: {
        "content-type": file.type || "application/octet-stream",
        "x-media-kind": input.kind,
        "x-media-title": input.title.trim(),
        "x-media-file-name": file.name,
        ...(input.tags?.length ? { "x-media-tags": input.tags.join(",") } : {}),
      },
      body: file,
    });
  }

  createVersion(assetId: string, file: File, role = "primary"): Promise<MediaMutationPayload> {
    return this.admin.requestJson<MediaMutationPayload>(`${MEDIA_BASE}/assets/${encode(assetId)}/versions`, {
      method: "POST",
      headers: {
        "content-type": file.type || "application/octet-stream",
        "x-media-file-name": file.name,
        "x-media-role": role,
      },
      body: file,
    });
  }

  setArchived(assetId: string, archived: boolean): Promise<MediaAsset> {
    return this.admin.requestJson<MediaAsset>(`${MEDIA_BASE}/assets/${encode(assetId)}/archive`, {
      method: "POST",
      body: JSON.stringify({ archived }),
    });
  }

  async previewHandle(assetVersionId: string, component: MediaComponent): Promise<MediaPreviewHandle | null> {
    if (component.runtimeUrl) {
      return { url: component.runtimeUrl, revoke: () => undefined };
    }
    if (component.storageClass !== "admin-blob") return null;

    const path = `${MEDIA_BASE}/blobs/${encode(assetVersionId)}/${encode(component.role)}`;
    const response = await fetch(path, {
      method: "GET",
      cache: "no-store",
      headers: { "x-typing-game-admin-token": this.admin.getToken() },
    });
    if (!response.ok) {
      let payload: unknown = null;
      try { payload = await response.json(); } catch { /* binary/error body may not be JSON */ }
      throw new Error(mediaErrorMessage(payload, `Unable to load media preview (HTTP ${response.status}).`));
    }
    const url = URL.createObjectURL(await response.blob());
    return { url, revoke: () => URL.revokeObjectURL(url) };
  }
}
