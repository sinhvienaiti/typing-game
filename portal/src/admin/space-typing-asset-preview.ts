const ASSET_PREVIEW_PROTOCOL_VERSION = 1 as const;
const PREVIEW_ENTRY_PATH = "/admin-preview.html";
const READY_TIMEOUT_MS = 8_000;
const COMMAND_TIMEOUT_MS = 5_000;
const TOKEN_PATTERN = /^[A-Za-z0-9._:-]{8,160}$/;
const RESPONSE_TYPES = new Set(["READY", "APPLIED", "ERROR", "DISPOSED"]);

type PreviewCommandType =
  | "LOAD_CANDIDATE"
  | "SET_SCENARIO"
  | "SET_TUNING"
  | "RESET"
  | "PAUSE"
  | "DISPOSE";

type PreviewExpectedResponseType = "APPLIED" | "DISPOSED";

export type SpaceTypingAssetPreviewScenario = "idle" | "move" | "fire";
export type SpaceTypingAssetPreviewSource = "draft" | "published";

export type SpaceTypingShipPreviewCandidate = Readonly<{
  characterId: string;
  visual: Readonly<Record<string, unknown>>;
}>;

type PreviewResponse = Readonly<{
  protocolVersion: typeof ASSET_PREVIEW_PROTOCOL_VERSION;
  previewSessionId: string;
  nonce: string;
  requestId: number;
  type: "READY" | "APPLIED" | "ERROR" | "DISPOSED";
  payload?: unknown;
}>;

type PendingRequest = {
  resolve: (payload: unknown) => void;
  reject: (error: Error) => void;
  timeout: number;
  commandType: PreviewCommandType;
  expectedType: PreviewExpectedResponseType;
};

type GameRegistry = Readonly<{
  games?: readonly Readonly<{
    id?: unknown;
    appUrl?: unknown;
  }>[];
}>;

function object(value: unknown): Record<string, unknown> | null {
  return value !== null && typeof value === "object" && !Array.isArray(value)
    ? value as Record<string, unknown>
    : null;
}

function secureToken(prefix: string): string {
  const bytes = new Uint8Array(16);
  crypto.getRandomValues(bytes);
  const body = Array.from(bytes, (byte) => byte.toString(16).padStart(2, "0")).join("");
  return `${prefix}:${body}`;
}

function safeMessage(value: unknown): string {
  const input = object(value);
  return typeof input?.message === "string" && input.message.trim().length > 0
    ? input.message
    : "Space Typing preview rejected the command.";
}

function parseResponse(
  value: unknown,
  expectedSession: string,
  expectedNonce: string,
): PreviewResponse | null {
  const input = object(value);
  if (input === null) return null;
  if (input.protocolVersion !== ASSET_PREVIEW_PROTOCOL_VERSION) return null;
  if (input.previewSessionId !== expectedSession || input.nonce !== expectedNonce) return null;
  if (!Number.isSafeInteger(input.requestId) || (input.requestId as number) < 0) return null;
  if (typeof input.type !== "string" || !RESPONSE_TYPES.has(input.type)) return null;
  return {
    protocolVersion: ASSET_PREVIEW_PROTOCOL_VERSION,
    previewSessionId: expectedSession,
    nonce: expectedNonce,
    requestId: input.requestId as number,
    type: input.type as PreviewResponse["type"],
    ...(input.payload === undefined ? {} : { payload: input.payload }),
  };
}

export async function resolveSpaceTypingAssetPreviewTarget(): Promise<Readonly<{
  origin: string;
  url: URL;
}>> {
  const response = await fetch("/games.json", { cache: "no-store", credentials: "same-origin" });
  if (!response.ok) throw new Error(`Could not load game registry (${response.status}).`);
  const registry = await response.json() as GameRegistry;
  const entry = registry.games?.find((game) => game.id === "space-typing");
  if (entry === undefined || typeof entry.appUrl !== "string") {
    throw new Error("Space Typing is missing from the canonical game registry.");
  }
  const appUrl = new URL(entry.appUrl, window.location.href);
  if (appUrl.protocol !== "https:" && appUrl.protocol !== "http:") {
    throw new Error("Space Typing preview requires an http(s) game origin.");
  }
  const previewUrl = new URL(PREVIEW_ENTRY_PATH, appUrl.origin);
  return Object.freeze({ origin: appUrl.origin, url: previewUrl });
}

export class SpaceTypingAssetPreviewBridge {
  readonly iframe: HTMLIFrameElement;
  readonly origin: string;
  readonly previewSessionId: string;
  private readonly nonce: string;
  private readonly pending = new Map<number, PendingRequest>();
  private readonly readyPromise: Promise<void>;
  private readyResolve: (() => void) | null = null;
  private readyReject: ((error: Error) => void) | null = null;
  private readyTimeout: number | null = null;
  private nextRequestId = 1;
  private ready = false;
  private disposed = false;

  private constructor(target: Readonly<{ origin: string; url: URL }>) {
    this.origin = target.origin;
    this.previewSessionId = secureToken("preview");
    this.nonce = secureToken("nonce");
    if (!TOKEN_PATTERN.test(this.previewSessionId) || !TOKEN_PATTERN.test(this.nonce)) {
      throw new Error("Could not create a valid preview session token.");
    }

    this.iframe = document.createElement("iframe");
    this.iframe.className = "st-admin-asset-preview-frame";
    this.iframe.title = "Space Typing production visual preview";
    this.iframe.setAttribute("sandbox", "allow-scripts allow-same-origin");
    this.iframe.referrerPolicy = "strict-origin";
    this.iframe.loading = "eager";
    this.iframe.allow = "";
    const url = new URL(target.url);
    url.searchParams.set("previewSession", this.previewSessionId);
    url.searchParams.set("nonce", this.nonce);
    this.iframe.src = url.href;

    this.readyPromise = new Promise<void>((resolve, reject) => {
      this.readyResolve = resolve;
      this.readyReject = reject;
    });
    this.readyTimeout = window.setTimeout(() => {
      if (this.ready) return;
      this.failReady(new Error("Space Typing preview did not become ready."));
    }, READY_TIMEOUT_MS);
    window.addEventListener("message", this.onMessage);
  }

  static async mount(host: HTMLElement): Promise<SpaceTypingAssetPreviewBridge> {
    const target = await resolveSpaceTypingAssetPreviewTarget();
    const bridge = new SpaceTypingAssetPreviewBridge(target);
    host.replaceChildren(bridge.iframe);
    return bridge;
  }

  async waitUntilReady(): Promise<void> {
    return this.readyPromise;
  }

  async loadShip(candidate: SpaceTypingShipPreviewCandidate): Promise<unknown> {
    return this.send("LOAD_CANDIDATE", {
      domain: "ship",
      characterId: candidate.characterId,
      visual: candidate.visual,
    });
  }

  async setScenario(scenario: SpaceTypingAssetPreviewScenario): Promise<unknown> {
    return this.send("SET_SCENARIO", { scenario });
  }

  async setTuning(visual: Readonly<Record<string, unknown>>): Promise<unknown> {
    return this.send("SET_TUNING", { visual });
  }

  async setPaused(paused: boolean): Promise<unknown> {
    return this.send("PAUSE", { paused });
  }

  async reset(): Promise<unknown> {
    return this.send("RESET");
  }

  async dispose(): Promise<void> {
    if (this.disposed) return;
    try {
      if (this.ready) await this.sendNow("DISPOSE");
    } catch {
      // Local teardown remains authoritative even if the child disappears.
    } finally {
      this.teardown(new Error("Space Typing preview bridge disposed."));
    }
  }

  disposeImmediately(): void {
    if (this.disposed) return;
    this.teardown(new Error("Space Typing preview bridge disposed."));
  }

  private readonly onMessage = (event: MessageEvent<unknown>): void => {
    if (this.disposed) return;
    if (event.origin !== this.origin) return;
    if (event.source !== this.iframe.contentWindow) return;
    const response = parseResponse(event.data, this.previewSessionId, this.nonce);
    if (response === null) return;

    if (response.type === "READY") {
      if (response.requestId !== 0 || this.ready) return;
      this.ready = true;
      if (this.readyTimeout !== null) window.clearTimeout(this.readyTimeout);
      this.readyTimeout = null;
      this.readyResolve?.();
      this.readyResolve = null;
      this.readyReject = null;
      return;
    }

    const pending = this.pending.get(response.requestId);
    if (pending === undefined) return;
    this.pending.delete(response.requestId);
    window.clearTimeout(pending.timeout);
    if (response.type === "ERROR") {
      pending.reject(new Error(safeMessage(response.payload)));
      return;
    }
    if (response.type !== pending.expectedType) {
      pending.reject(new Error(
        `Space Typing preview returned ${response.type} for ${pending.commandType}; expected ${pending.expectedType}.`,
      ));
      return;
    }
    pending.resolve(response.payload);
  };

  private async send(
    type: Exclude<PreviewCommandType, "DISPOSE">,
    payload?: unknown,
  ): Promise<unknown> {
    if (this.disposed) throw new Error("Space Typing preview bridge is disposed.");
    await this.readyPromise;
    return this.sendNow(type, payload);
  }

  private sendNow(
    type: PreviewCommandType,
    payload?: unknown,
  ): Promise<unknown> {
    if (this.disposed) return Promise.reject(new Error("Space Typing preview bridge is disposed."));
    const frameWindow = this.iframe.contentWindow;
    if (frameWindow === null) return Promise.reject(new Error("Space Typing preview frame is unavailable."));
    const requestId = this.nextRequestId++;
    const expectedType: PreviewExpectedResponseType = type === "DISPOSE" ? "DISPOSED" : "APPLIED";
    const message = Object.freeze({
      protocolVersion: ASSET_PREVIEW_PROTOCOL_VERSION,
      previewSessionId: this.previewSessionId,
      nonce: this.nonce,
      requestId,
      type,
      ...(payload === undefined ? {} : { payload }),
    });

    return new Promise<unknown>((resolve, reject) => {
      const timeout = window.setTimeout(() => {
        this.pending.delete(requestId);
        reject(new Error(`Space Typing preview command ${type} timed out.`));
      }, COMMAND_TIMEOUT_MS);
      this.pending.set(requestId, { resolve, reject, timeout, commandType: type, expectedType });
      frameWindow.postMessage(message, this.origin);
    });
  }

  private failReady(error: Error): void {
    this.readyReject?.(error);
    this.readyResolve = null;
    this.readyReject = null;
    this.teardown(error);
  }

  private teardown(reason: Error): void {
    if (this.disposed) return;
    this.disposed = true;
    this.ready = false;
    if (this.readyTimeout !== null) window.clearTimeout(this.readyTimeout);
    this.readyTimeout = null;
    this.readyReject?.(reason);
    this.readyResolve = null;
    this.readyReject = null;
    window.removeEventListener("message", this.onMessage);
    for (const pending of this.pending.values()) {
      window.clearTimeout(pending.timeout);
      pending.reject(reason);
    }
    this.pending.clear();
    this.iframe.remove();
  }
}
