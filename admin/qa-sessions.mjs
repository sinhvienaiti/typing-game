import { createHash, randomBytes, randomUUID, timingSafeEqual } from "node:crypto";

const QA_ENVIRONMENTS = new Set(["local", "development", "preview", "test"]);
const MIN_TTL_MS = 30_000;
const MAX_TTL_MS = 30 * 60_000;
const DEFAULT_TTL_MS = 10 * 60_000;
const MAX_SESSIONS = 128;

export class QaSessionValidationError extends Error {}
export class QaSessionNotFoundError extends Error {}

function text(value, label, max = 200) {
  if (typeof value !== "string" || value.length === 0 || value.length > max) {
    throw new QaSessionValidationError(`${label} must be a non-empty string.`);
  }
  return value;
}

function positiveInteger(value, label) {
  if (!Number.isSafeInteger(value) || value < 1) {
    throw new QaSessionValidationError(`${label} must be a positive integer.`);
  }
  return value;
}

function validStage(value) {
  return Number.isSafeInteger(value) && value >= 1 && value <= 1000;
}

function sanitizeOverrides(value = {}) {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    throw new QaSessionValidationError("overrides must be an object.");
  }
  const overrides = {};
  if (value.stageAccess !== undefined) {
    if (!value.stageAccess || typeof value.stageAccess !== "object" || Array.isArray(value.stageAccess)) {
      throw new QaSessionValidationError("overrides.stageAccess must be an object.");
    }
    if (!validStage(value.stageAccess.stage) || !["allow", "force"].includes(value.stageAccess.mode)) {
      throw new QaSessionValidationError("overrides.stageAccess requires stage 1..1000 and mode allow|force.");
    }
    overrides.stageAccess = {
      stage: value.stageAccess.stage,
      mode: value.stageAccess.mode,
    };
  }
  if (value.shipPreview !== undefined) {
    overrides.shipPreview = text(value.shipPreview, "overrides.shipPreview", 100);
  }
  if (value.unlimitedWarp !== undefined) {
    if (typeof value.unlimitedWarp !== "boolean") {
      throw new QaSessionValidationError("overrides.unlimitedWarp must be boolean.");
    }
    overrides.unlimitedWarp = value.unlimitedWarp;
  }
  return overrides;
}

function bearerHash(value) {
  return createHash("sha256").update(value).digest();
}

function bearerMatches(stored, provided) {
  if (typeof provided !== "string" || provided.length < 32 || provided.length > 256) return false;
  const candidate = bearerHash(provided);
  return candidate.length === stored.length && timingSafeEqual(candidate, stored);
}

function publicSession(record, nowMs) {
  return {
    id: record.id,
    gameId: "space-typing",
    environment: record.environment,
    targetSessionId: record.targetSessionId,
    actorId: record.actorId,
    issuedAtMs: record.issuedAtMs,
    expiresAtMs: record.expiresAtMs,
    generation: record.generation,
    overrides: structuredClone(record.overrides),
    revoked: record.revoked,
    expired: nowMs >= record.expiresAtMs,
    consumeCount: record.consumeCount,
  };
}

export class QaSessionStore {
  #sessions = new Map();
  #generationByTarget = new Map();

  constructor({ now = Date.now } = {}) {
    this.now = now;
  }

  #prune() {
    const nowMs = this.now();
    for (const [id, record] of this.#sessions) {
      if (record.revoked || nowMs >= record.expiresAtMs + MAX_TTL_MS) {
        this.#sessions.delete(id);
      }
    }
    if (this.#sessions.size <= MAX_SESSIONS) return;
    const oldest = [...this.#sessions.values()]
      .sort((a, b) => a.issuedAtMs - b.issuedAtMs)
      .slice(0, this.#sessions.size - MAX_SESSIONS);
    for (const record of oldest) this.#sessions.delete(record.id);
  }

  issue(input, actorId = "admin") {
    this.#prune();
    if (!input || typeof input !== "object" || Array.isArray(input)) {
      throw new QaSessionValidationError("QA session request must be an object.");
    }
    const targetSessionId = text(input.targetSessionId, "targetSessionId");
    const environment = text(input.environment, "environment", 32);
    if (!QA_ENVIRONMENTS.has(environment)) {
      throw new QaSessionValidationError("QA sessions are disabled in this environment.");
    }
    const ttlMs = input.ttlMs === undefined ? DEFAULT_TTL_MS : positiveInteger(input.ttlMs, "ttlMs");
    if (ttlMs < MIN_TTL_MS || ttlMs > MAX_TTL_MS) {
      throw new QaSessionValidationError(`ttlMs must be between ${MIN_TTL_MS} and ${MAX_TTL_MS}.`);
    }
    const generation = (this.#generationByTarget.get(targetSessionId) ?? 0) + 1;
    this.#generationByTarget.set(targetSessionId, generation);
    for (const record of this.#sessions.values()) {
      if (record.targetSessionId === targetSessionId && !record.revoked) record.revoked = true;
    }
    const issuedAtMs = this.now();
    const bearer = randomBytes(32).toString("base64url");
    const record = {
      id: randomUUID(),
      targetSessionId,
      environment,
      actorId: text(actorId, "actorId"),
      issuedAtMs,
      expiresAtMs: issuedAtMs + ttlMs,
      generation,
      overrides: sanitizeOverrides(input.overrides),
      bearerHash: bearerHash(bearer),
      revoked: false,
      consumeCount: 0,
    };
    this.#sessions.set(record.id, record);
    return { ...publicSession(record, issuedAtMs), bearer };
  }

  list() {
    this.#prune();
    const nowMs = this.now();
    return [...this.#sessions.values()]
      .map((record) => publicSession(record, nowMs))
      .sort((a, b) => b.issuedAtMs - a.issuedAtMs);
  }

  revoke(id) {
    const record = this.#sessions.get(text(id, "id"));
    if (!record) throw new QaSessionNotFoundError("QA session not found.");
    record.revoked = true;
    return publicSession(record, this.now());
  }

  consume(input) {
    this.#prune();
    if (!input || typeof input !== "object" || Array.isArray(input)) {
      throw new QaSessionValidationError("QA capability exchange must be an object.");
    }
    const id = text(input.id, "id");
    const targetSessionId = text(input.targetSessionId, "targetSessionId");
    const environment = text(input.environment, "environment", 32);
    const record = this.#sessions.get(id);
    const nowMs = this.now();
    if (
      !record ||
      record.revoked ||
      nowMs >= record.expiresAtMs ||
      record.targetSessionId !== targetSessionId ||
      record.environment !== environment ||
      !bearerMatches(record.bearerHash, input.bearer)
    ) {
      throw new QaSessionNotFoundError("QA capability is unavailable, expired, revoked, or out of scope.");
    }
    record.consumeCount += 1;
    return {
      version: 1,
      id: record.id,
      gameId: "space-typing",
      environment: record.environment,
      targetSessionId: record.targetSessionId,
      actorId: record.actorId,
      issuedAtMs: record.issuedAtMs,
      expiresAtMs: record.expiresAtMs,
      generation: record.generation,
      overrides: structuredClone(record.overrides),
    };
  }
}
