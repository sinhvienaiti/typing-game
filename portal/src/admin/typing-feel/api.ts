// Typing Feel Admin routes (admin/typing-feel/http.mjs). Errors keep the server's
// problem list, so Save draft and Review can show every problem, one per line.
import { SpaceTypingAdminApi } from "../api";
import type {
  TypingFeelAcceptInput,
  TypingFeelAcceptResult,
  TypingFeelCapabilities,
  TypingFeelChangeScope,
  TypingFeelConfig,
  TypingFeelExportStatus,
  TypingFeelHistory,
  TypingFeelJob,
  TypingFeelJobListEntry,
  TypingFeelJobView,
  TypingFeelLibrary,
  TypingFeelPublishResult,
  TypingFeelRevision,
  TypingFeelState,
  TypingFeelUploadCheck,
  TypingFeelValidation,
} from "./types";

const BASE = "/api/admin/shared/typing-feel";

export class TypingFeelApiError extends Error {
  constructor(
    message: string,
    readonly status: number,
    readonly code: string,
    readonly problems: string[] = [],
  ) {
    super(message);
    this.name = "TypingFeelApiError";
  }
}

export function typingFeelErrorProblems(error: unknown): string[] {
  if (error instanceof TypingFeelApiError) return error.problems.length ? error.problems : [error.message];
  return [error instanceof Error ? error.message : String(error)];
}

async function request<T>(path: string, init: RequestInit = {}): Promise<T> {
  const headers = new Headers(init.headers ?? {});
  headers.set("x-typing-game-admin-token", new SpaceTypingAdminApi().getToken());
  if (typeof init.body === "string") headers.set("content-type", "application/json");
  let response: Response;
  try {
    response = await fetch(`${BASE}${path}`, { ...init, headers, cache: "no-store" });
  } catch {
    throw new TypingFeelApiError("The local Admin service could not be reached. Check that it is running, then try again.", 0, "network-error");
  }
  const text = await response.text();
  let payload: unknown = null;
  try {
    payload = text ? JSON.parse(text) : null;
  } catch {
    throw new TypingFeelApiError("The Admin service sent a response that is not JSON. Restart the local Admin service.", response.status, "invalid-json");
  }
  if (!response.ok) {
    const record = (payload ?? {}) as Record<string, unknown>;
    const problems = Array.isArray(record["problems"]) ? record["problems"].filter((item): item is string => typeof item === "string") : [];
    const message = typeof record["message"] === "string" && record["message"] ? record["message"] : `The Admin request failed (HTTP ${response.status}).`;
    throw new TypingFeelApiError(message, response.status, typeof record["error"] === "string" ? record["error"] : "http-error", problems);
  }
  return payload as T;
}

const post = <T>(path: string, body: unknown): Promise<T> => request<T>(path, { method: "POST", body: JSON.stringify(body) });

export const typingFeelApi = {
  state: () => request<TypingFeelState>("/state"),
  history: () => request<TypingFeelHistory>("/history"),
  revision: (revision: string) => request<TypingFeelRevision>(`/revisions/${encodeURIComponent(revision)}`),
  library: (revision: string) => request<TypingFeelLibrary>(`/library?revision=${encodeURIComponent(revision)}`),
  exportStatus: () => request<TypingFeelExportStatus>("/export/status"),
  saveDraft: (input: { baseRevision: string; config: TypingFeelConfig; message: string }) => post<TypingFeelRevision>("/revisions", input),
  validate: (revision: string) => post<TypingFeelValidation>("/validate-revision", { revision }),
  changeScope: (revision: string) => post<TypingFeelChangeScope>("/change-scope", { revision }),
  rollbackChangeScope: (targetRevision: string) => post<TypingFeelChangeScope>("/rollback-change-scope", { targetRevision }),
  publish: (revision: string, expectedActiveRevision: string) => post<TypingFeelPublishResult>("/publish", { revision, expectedActiveRevision }),
  rollback: (targetRevision: string, expectedActiveRevision: string) => post<TypingFeelPublishResult>("/rollback", { targetRevision, expectedActiveRevision }),
  // Add sound set (G7): capabilities, the upload check and Format jobs.
  capabilities: () => request<TypingFeelCapabilities>("/capabilities"),
  checkSource: (sourceAssetVersionId: string) => post<TypingFeelUploadCheck>("/sources/check", { sourceAssetVersionId }),
  jobs: () => request<{ jobs: TypingFeelJobListEntry[]; running: string | null }>("/jobs"),
  job: (jobId: string) => request<TypingFeelJobView>(`/jobs/${encodeURIComponent(jobId)}`),
  format: (input: { sourceAssetVersionId: string; setId?: string; name: string; family: string | null }) => post<{ jobId: string; job: TypingFeelJob }>("/jobs", { ...input, recipe: "natural-v1" }),
  accept: (jobId: string, input: TypingFeelAcceptInput) => post<TypingFeelAcceptResult>(`/jobs/${encodeURIComponent(jobId)}/accept`, input),
  discard: (jobId: string) => post<{ job: TypingFeelJob }>(`/jobs/${encodeURIComponent(jobId)}/discard`, {}),
};

/**
 * One file of a Format job as an object URL: the job routes need the Admin token,
 * which <audio> cannot send, so the page fetches with it (as media-api.ts does).
 * The caller revokes the URL.
 */
export async function jobFileUrl(jobId: string, name: string): Promise<string> {
  let response: Response;
  try {
    response = await fetch(`${BASE}/jobs/${encodeURIComponent(jobId)}/files/${encodeURIComponent(name)}`, { cache: "no-store", headers: { "x-typing-game-admin-token": new SpaceTypingAdminApi().getToken() } });
  } catch {
    throw new TypingFeelApiError("The local Admin service could not be reached.", 0, "network-error");
  }
  if (!response.ok) throw new TypingFeelApiError(`${name} could not be loaded (HTTP ${response.status}).`, response.status, "file");
  return URL.createObjectURL(await response.blob());
}

// A revision is immutable, so its library (sets with their Media facts) is cached per revision for the tab.
const libraries = new Map<string, Promise<TypingFeelLibrary>>();

export function cachedLibrary(revision: string): Promise<TypingFeelLibrary> {
  let pending = libraries.get(revision);
  if (!pending) {
    pending = typingFeelApi.library(revision);
    pending.catch(() => libraries.delete(revision));
    libraries.set(revision, pending);
  }
  return pending;
}

export function clearLibraryCache(): void {
  libraries.clear();
}
