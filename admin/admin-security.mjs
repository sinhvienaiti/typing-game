import { randomUUID } from "node:crypto";
import { appendFile, mkdir, readFile } from "node:fs/promises";
import { dirname, join } from "node:path";

export class AdminAuthorizationError extends Error {
  constructor(permission) {
    super(`Permission denied: ${permission}`);
    this.name = "AdminAuthorizationError";
    this.permission = permission;
  }
}

export const ADMIN_PERMISSIONS = Object.freeze({
  CONFIG_DRAFT: "config.draft",
  CONFIG_PUBLISH: "config.publish",
  CONFIG_ROLLBACK: "config.rollback",
  MEDIA_UPLOAD: "media.upload",
  MEDIA_DELETE: "media.delete",
  AUDIT_READ: "audit.read",
  DEVELOPER_INSPECT: "developer.runtime-inspect",
});

const SUPER_ADMIN_PERMISSIONS = Object.freeze(Object.values(ADMIN_PERMISSIONS));

function cleanText(value, fallback, max = 120) {
  if (typeof value !== "string") return fallback;
  const normalized = value.trim().replace(/\s+/g, " ");
  return normalized ? normalized.slice(0, max) : fallback;
}

export function createLocalAdminActor({
  actorId = "local-admin",
  displayName = "Local Admin",
  requestId = randomUUID(),
} = {}) {
  return Object.freeze({
    actorId: cleanText(actorId, "local-admin", 80),
    actorDisplayName: cleanText(displayName, "Local Admin", 120),
    authMethod: "local-admin-token",
    role: "super-admin",
    requestId: cleanText(requestId, randomUUID(), 120),
    permissions: SUPER_ADMIN_PERMISSIONS,
  });
}

export function createLocalAdminActorFromRequest(request) {
  const actorHeader = request.headers["x-typing-game-admin-actor-id"];
  const displayHeader = request.headers["x-typing-game-admin-actor-name"];
  const requestHeader = request.headers["x-request-id"];
  const first = (value) => Array.isArray(value) ? value[0] : value;
  return createLocalAdminActor({
    actorId: first(actorHeader),
    displayName: first(displayHeader),
    requestId: first(requestHeader),
  });
}

export function hasAdminPermission(actor, permission) {
  return Boolean(actor?.permissions?.includes(permission));
}

export function requireAdminPermission(actor, permission) {
  if (!hasAdminPermission(actor, permission)) throw new AdminAuthorizationError(permission);
}

function jsonComparable(value) {
  if (Array.isArray(value)) return value.map(jsonComparable);
  if (value !== null && typeof value === "object") {
    return Object.fromEntries(Object.keys(value).sort().map((key) => [key, jsonComparable(value[key])]));
  }
  return value;
}

function equalValue(left, right) {
  return JSON.stringify(jsonComparable(left)) === JSON.stringify(jsonComparable(right));
}

function collectChangedPaths(base, next, prefix, paths, maxPaths) {
  if (paths.length >= maxPaths || equalValue(base, next)) return;

  const baseObject = base !== null && typeof base === "object" && !Array.isArray(base);
  const nextObject = next !== null && typeof next === "object" && !Array.isArray(next);
  if (!baseObject || !nextObject) {
    paths.push(prefix || "$root");
    return;
  }

  const keys = new Set([...Object.keys(base), ...Object.keys(next)]);
  for (const key of [...keys].sort()) {
    if (paths.length >= maxPaths) return;
    collectChangedPaths(base[key], next[key], prefix ? `${prefix}.${key}` : key, paths, maxPaths);
  }
}

function domainForPath(path) {
  const parts = path.split(".");
  if (parts[0] === "content" && parts[1]) return `content.${parts[1]}`;
  if (parts[0] === "worldMusic") return "worldMusic";
  if (parts[0] === "audio") return "audio";
  if (parts[0] === "system") return "system";
  if (parts[0] === "featureFlags") return "featureFlags";
  return parts[0] || "$root";
}

export function describeConfigChangeScope({
  baseRevision = null,
  targetRevision = null,
  baseConfig,
  targetConfig,
  maxPaths = 200,
}) {
  const changedPaths = [];
  collectChangedPaths(baseConfig, targetConfig, "", changedPaths, maxPaths);
  const domains = [...new Set(changedPaths.map(domainForPath))].sort();
  return Object.freeze({
    model: "whole-config-revision",
    baseRevision,
    targetRevision,
    changed: changedPaths.length > 0,
    changedPathCount: changedPaths.length,
    truncated: changedPaths.length >= maxPaths,
    domains,
    changedPaths,
    publishWarning: changedPaths.length > 0
      ? "Publishing activates the complete target revision, including every changed path listed in this scope."
      : "No config changes were detected between the base and target revision.",
  });
}

export class LocalAdminAuditLog {
  constructor({ rootDir, now = () => new Date(), idFactory = randomUUID } = {}) {
    if (!rootDir) throw new TypeError("LocalAdminAuditLog requires rootDir.");
    this.path = join(rootDir, "audit", "events.jsonl");
    this.now = now;
    this.idFactory = idFactory;
  }

  async record({ actor, action, domain, entityType = null, entityId = null, changeScope = null, result = "success", error = null }) {
    const event = {
      schemaVersion: 1,
      eventId: this.idFactory(),
      timestamp: this.now().toISOString(),
      actor: actor ? {
        actorId: actor.actorId,
        actorDisplayName: actor.actorDisplayName,
        authMethod: actor.authMethod,
        role: actor.role,
      } : null,
      requestId: actor?.requestId ?? null,
      action,
      domain,
      entityType,
      entityId,
      changeScope,
      result,
      error: error ? String(error).slice(0, 500) : null,
    };
    await mkdir(dirname(this.path), { recursive: true });
    await appendFile(this.path, `${JSON.stringify(event)}\n`, "utf8");
    return event;
  }

  async list({ limit = 100 } = {}) {
    let raw;
    try {
      raw = await readFile(this.path, "utf8");
    } catch (error) {
      if (error?.code === "ENOENT") return [];
      throw error;
    }
    const events = raw.split("\n").filter(Boolean).map((line) => JSON.parse(line));
    return events.slice(-Math.max(1, Math.min(500, limit))).reverse();
  }
}

async function recordAuditBestEffort(auditLog, event, onAuditError) {
  try {
    await auditLog.record(event);
    return true;
  } catch (error) {
    onAuditError(error);
    return false;
  }
}

export async function runAuthorizedAdminMutation({
  actor,
  permission,
  auditLog,
  action,
  domain,
  entityType = null,
  entityId = null,
  changeScope = null,
  resolveEntityId = null,
  resolveChangeScope = null,
  onAuditError = () => undefined,
  operation,
}) {
  try {
    requireAdminPermission(actor, permission);
  } catch (error) {
    await recordAuditBestEffort(auditLog, {
      actor,
      action,
      domain,
      entityType,
      entityId,
      changeScope,
      result: "denied",
      error: error instanceof Error ? error.message : String(error),
    }, onAuditError);
    throw error;
  }

  // A durable attempt record is written before mutation. If this write fails, the mutation is not run.
  // This prevents a successful mutation from being completely absent from the audit stream.
  await auditLog.record({
    actor,
    action,
    domain,
    entityType,
    entityId,
    changeScope,
    result: "attempt",
  });

  let value;
  try {
    value = await operation();
  } catch (error) {
    await recordAuditBestEffort(auditLog, {
      actor,
      action,
      domain,
      entityType,
      entityId,
      changeScope,
      result: "error",
      error: error instanceof Error ? error.message : String(error),
    }, onAuditError);
    throw error;
  }

  const resolvedEntityId = typeof resolveEntityId === "function"
    ? resolveEntityId(value)
    : entityId;
  const resolvedChangeScope = typeof resolveChangeScope === "function"
    ? resolveChangeScope(value)
    : changeScope;

  // Do not report a completed mutation as failed only because the final audit append failed.
  // The durable pre-mutation attempt remains, and the caller can surface/log the audit degradation.
  await recordAuditBestEffort(auditLog, {
    actor,
    action,
    domain,
    entityType,
    entityId: resolvedEntityId ?? null,
    changeScope: resolvedChangeScope ?? null,
    result: "success",
  }, onAuditError);

  return value;
}
