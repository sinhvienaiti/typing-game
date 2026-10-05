export type QaEnvironment = "local" | "development" | "preview" | "test";
export type QaStageMode = "allow" | "force";

export type QaSessionOverrides = {
  stageAccess?: { stage: number; mode: QaStageMode };
  shipPreview?: string;
  unlimitedWarp?: boolean;
};

export type QaIssuedSession = {
  id: string;
  gameId: "space-typing";
  environment: QaEnvironment;
  targetSessionId: string;
  actorId: string;
  issuedAtMs: number;
  expiresAtMs: number;
  generation: number;
  overrides: QaSessionOverrides;
  bearer: string;
};

export type QaListedSession = Omit<QaIssuedSession, "bearer"> & {
  revoked: boolean;
  expired: boolean;
  consumeCount: number;
};

export const QA_RUNTIME_READY = "space-typing:qa-runtime-ready";
export const QA_RUNTIME_CAPABILITY = "space-typing:qa-capability";
export const QA_RUNTIME_ACCEPTED = "space-typing:qa-capability-accepted";

export function validQaStage(stage: number): boolean {
  return Number.isSafeInteger(stage) && stage >= 1 && stage <= 1000;
}

export function createQaLaunchNonce(): string {
  return crypto.randomUUID();
}

/**
 * The launch URL contains no bearer and therefore grants no authority. The
 * child must announce an exact runtime session through postMessage before the
 * Admin page issues a bound capability.
 */
export function qaLaunchUrl(baseUrl: string, launchNonce: string): string {
  const url = new URL(baseUrl, window.location.href);
  url.searchParams.set("qa", "1");
  url.searchParams.set("qaLaunch", launchNonce);
  return url.toString();
}

export function expectedQaOrigin(baseUrl: string): string {
  return new URL(baseUrl, window.location.href).origin;
}

export function isQaRuntimeReadyMessage(
  value: unknown,
  launchNonce: string,
): value is { type: typeof QA_RUNTIME_READY; runtimeSessionId: string; launchNonce: string; environment: QaEnvironment } {
  if (!value || typeof value !== "object") return false;
  const message = value as Record<string, unknown>;
  return (
    message.type === QA_RUNTIME_READY &&
    message.launchNonce === launchNonce &&
    typeof message.runtimeSessionId === "string" &&
    message.runtimeSessionId.length > 0 &&
    ["local", "development", "preview", "test"].includes(String(message.environment))
  );
}
