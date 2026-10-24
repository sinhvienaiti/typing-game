import type {
  ProductionPreviewDomainAdapter,
  ProductionPreviewLifecycleState,
} from "./preview-contract";

const ASSET_PREVIEW_PROTOCOL_VERSION = 1 as const;
const PREVIEW_ENTRY_PATH = "/admin-preview.html";
const READY_TIMEOUT_MS = 8_000;
const COMMAND_TIMEOUT_MS = 5_000;
const TOKEN_PATTERN = /^[A-Za-z0-9._:-]{8,160}$/;
const RESPONSE_TYPES = new Set(["READY", "APPLIED", "ERROR", "DISPOSED"]);
const STALE_COMMAND_CODE = "STALE_PREVIEW_COMMAND";

type PreviewCommandType =
  | "LOAD_CANDIDATE"
  | "SET_SCENARIO"
  | "SET_TUNING"
  | "RESET"
  | "PAUSE"
  | "DISPOSE";
type PreviewExpectedResponseType = "APPLIED" | "DISPOSED";

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

type PreviewWaiter = {
  generation: number;
  resolve: (payload: unknown) => void;
  reject: (error: Error) => void;
};

type GameRegistry = Readonly<{
  games?: readonly Readonly<{ id?: unknown; appUrl?: unknown }>[];
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
    : "Space Typing production preview rejected the command.";
}

function isStaleCommandPayload(value: unknown): boolean {
  return object(value)?.code === STALE_COMMAND_CODE;
}

function parseResponse(value: unknown, expectedSession: string, expectedNonce: string): PreviewResponse | null {
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

export async function resolveSpaceTypingProductionPreviewTarget(): Promise<Readonly<{
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
  return Object.freeze({
    origin: appUrl.origin,
    url: new URL(PREVIEW_ENTRY_PATH, appUrl.origin),
  });
}

export class ProductionPreviewStaleError extends Error {
  constructor() {
    super("Production preview operation was superseded by newer Admin input.");
    this.name = "ProductionPreviewStaleError";
  }
}

/**
 * Shared isolated iframe transport for production-backed Admin previews.
 * Domain adapters serialize candidates/scenarios only; renderer/runtime ownership stays in the child.
 */
export class ProductionPreviewBridge<TCandidate, TScenario extends string, TTuning = Readonly<Record<string, unknown>>> {
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
  private candidateGeneration = 0;
  private queuedCandidate: TCandidate | null = null;
  private queuedFrame: number | null = null;
  private readonly queuedWaiters: PreviewWaiter[] = [];
  private lastCandidate: TCandidate | null = null;
  private lastScenario: TScenario;
  private lifecycle: ProductionPreviewLifecycleState = Object.freeze({
    status: "loading",
    message: "Connecting to isolated child production preview…",
  });

  private constructor(
    target: Readonly<{ origin: string; url: URL }>,
    private readonly adapter: ProductionPreviewDomainAdapter<TCandidate, TScenario, TTuning>,
  ) {
    this.lastScenario = adapter.defaultScenario;
    this.origin = target.origin;
    this.previewSessionId = secureToken("preview");
    this.nonce = secureToken("nonce");
    if (!TOKEN_PATTERN.test(this.previewSessionId) || !TOKEN_PATTERN.test(this.nonce)) {
      throw new Error("Could not create a valid preview session token.");
    }

    this.iframe = document.createElement("iframe");
    this.iframe.className = "st-admin-asset-preview-frame";
    this.iframe.title = `${adapter.domain} production preview`;
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

  static async mount<TCandidate, TScenario extends string, TTuning = Readonly<Record<string, unknown>>>(
    host: HTMLElement,
    adapter: ProductionPreviewDomainAdapter<TCandidate, TScenario, TTuning>,
  ): Promise<ProductionPreviewBridge<TCandidate, TScenario, TTuning>> {
    const target = await resolveSpaceTypingProductionPreviewTarget();
    const bridge = new ProductionPreviewBridge(target, adapter);
    host.replaceChildren(bridge.iframe);
    return bridge;
  }

  getLifecycle(): ProductionPreviewLifecycleState {
    return this.lifecycle;
  }

  async waitUntilReady(): Promise<void> {
    return this.readyPromise;
  }

  loadCandidate(candidate: TCandidate): Promise<unknown> {
    if (this.disposed) return Promise.reject(new Error("Production preview bridge is disposed."));
    const generation = ++this.candidateGeneration;
    this.lastCandidate = candidate;
    this.queuedCandidate = candidate;
    const result = new Promise<unknown>((resolve, reject) => {
      this.queuedWaiters.push({ generation, resolve, reject });
    });
    if (this.queuedFrame === null) {
      this.queuedFrame = window.requestAnimationFrame(() => {
        this.queuedFrame = null;
        const flushGeneration = this.candidateGeneration;
        const nextCandidate = this.queuedCandidate;
        this.queuedCandidate = null;
        const queued = this.queuedWaiters.splice(0);
        const waiters: PreviewWaiter[] = [];
        for (const waiter of queued) {
          if (waiter.generation === flushGeneration) waiters.push(waiter);
          else waiter.reject(new ProductionPreviewStaleError());
        }
        if (waiters.length === 0) return;
        if (nextCandidate === null) {
          const error = new Error("Production preview candidate queue was empty.");
          for (const waiter of waiters) waiter.reject(error);
          return;
        }
        void this.send("LOAD_CANDIDATE", this.adapter.candidatePayload(nextCandidate)).then(
          (payload) => {
            if (flushGeneration !== this.candidateGeneration) {
              const stale = new ProductionPreviewStaleError();
              for (const waiter of waiters) waiter.reject(stale);
              return;
            }
            for (const waiter of waiters) waiter.resolve(payload);
          },
          (error: unknown) => {
            if (flushGeneration !== this.candidateGeneration) {
              const stale = new ProductionPreviewStaleError();
              for (const waiter of waiters) waiter.reject(stale);
              return;
            }
            const failure = error instanceof Error ? error : new Error(String(error));
            for (const waiter of waiters) waiter.reject(failure);
          },
        );
      });
    }
    return result;
  }

  async setScenario(scenario: TScenario): Promise<unknown> {
    this.lastScenario = scenario;
    return this.send("SET_SCENARIO", this.adapter.scenarioPayload(scenario));
  }

  async setTuning(tuning: TTuning): Promise<unknown> {
    if (this.adapter.tuningPayload === undefined) {
      throw new Error(`${this.adapter.domain} production preview does not support live tuning.`);
    }
    return this.send("SET_TUNING", this.adapter.tuningPayload(tuning));
  }

  async setPaused(paused: boolean): Promise<unknown> {
    return this.send("PAUSE", { paused });
  }

  async reset(): Promise<unknown> {
    ++this.candidateGeneration;
    this.invalidateQueuedCandidate(new ProductionPreviewStaleError());
    this.lastCandidate = null;
    this.lastScenario = this.adapter.defaultScenario;
    return this.send("RESET");
  }

  async replay(): Promise<void> {
    const candidate = this.lastCandidate;
    if (candidate === null) throw new Error("Load a production preview candidate before replaying it.");
    const scenario = this.lastScenario;
    const generation = ++this.candidateGeneration;
    this.invalidateQueuedCandidate(new ProductionPreviewStaleError());
    await this.send("RESET");
    if (generation !== this.candidateGeneration) throw new ProductionPreviewStaleError();
    await this.send("LOAD_CANDIDATE", this.adapter.candidatePayload(candidate));
    if (generation !== this.candidateGeneration) throw new ProductionPreviewStaleError();
    await this.send("SET_SCENARIO", this.adapter.scenarioPayload(scenario));
  }

  async dispose(): Promise<void> {
    if (this.disposed) return;
    try {
      if (this.ready) await this.sendNow("DISPOSE");
    } catch {
      // Local teardown remains authoritative if the isolated child disappears.
    } finally {
      this.teardown(new Error("Production preview bridge disposed."));
    }
  }

  disposeImmediately(): void {
    if (this.disposed) return;
    this.teardown(new Error("Production preview bridge disposed."));
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
      this.lifecycle = Object.freeze({ status: "ready", message: "Production preview ready." });
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
      pending.reject(
        isStaleCommandPayload(response.payload)
          ? new ProductionPreviewStaleError()
          : new Error(safeMessage(response.payload)),
      );
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

  private async send(type: Exclude<PreviewCommandType, "DISPOSE">, payload?: unknown): Promise<unknown> {
    if (this.disposed) throw new Error("Production preview bridge is disposed.");
    await this.readyPromise;
    return this.sendNow(type, payload);
  }

  private sendNow(type: PreviewCommandType, payload?: unknown): Promise<unknown> {
    if (this.disposed) return Promise.reject(new Error("Production preview bridge is disposed."));
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

  private invalidateQueuedCandidate(reason: Error): void {
    if (this.queuedFrame !== null) window.cancelAnimationFrame(this.queuedFrame);
    this.queuedFrame = null;
    this.queuedCandidate = null;
    for (const waiter of this.queuedWaiters.splice(0)) waiter.reject(reason);
  }

  private failReady(error: Error): void {
    this.lifecycle = Object.freeze({ status: "error", message: error.message });
    this.readyReject?.(error);
    this.readyResolve = null;
    this.readyReject = null;
    this.teardown(error);
  }

  private teardown(reason: Error): void {
    if (this.disposed) return;
    this.disposed = true;
    this.ready = false;
    ++this.candidateGeneration;
    if (this.readyTimeout !== null) window.clearTimeout(this.readyTimeout);
    this.readyTimeout = null;
    this.invalidateQueuedCandidate(reason);
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
