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

export const ADMIN_PERMISSION_CATALOG = Object.freeze([
  { id: ADMIN_PERMISSIONS.CONFIG_DRAFT, label: "Create drafts", group: "Configuration", dangerous: false },
  { id: ADMIN_PERMISSIONS.CONFIG_PUBLISH, label: "Publish configuration", group: "Configuration", dangerous: true },
  { id: ADMIN_PERMISSIONS.CONFIG_ROLLBACK, label: "Roll back published configuration", group: "Configuration", dangerous: true },
  { id: ADMIN_PERMISSIONS.MEDIA_UPLOAD, label: "Upload media", group: "Media", dangerous: false },
  { id: ADMIN_PERMISSIONS.MEDIA_DELETE, label: "Archive / delete Admin media", group: "Media", dangerous: true },
  { id: ADMIN_PERMISSIONS.AUDIT_READ, label: "Read audit history", group: "Governance", dangerous: false },
  { id: ADMIN_PERMISSIONS.DEVELOPER_INSPECT, label: "Open Developer Tools", group: "Developer", dangerous: true },
]);

const SUPER_ADMIN_PERMISSIONS = Object.freeze(Object.values(ADMIN_PERMISSIONS));
const KNOWN_PERMISSIONS = new Set(SUPER_ADMIN_PERMISSIONS);

export const ADMIN_ROLE_TEMPLATES = Object.freeze([
  Object.freeze({ id: "super-admin", label: "Super Admin", description: "Full local administration and Developer Tools access.", permissions: SUPER_ADMIN_PERMISSIONS }),
  Object.freeze({ id: "publisher", label: "Publisher", description: "Prepare, publish and roll back configuration with audit visibility.", permissions: Object.freeze([ADMIN_PERMISSIONS.CONFIG_DRAFT, ADMIN_PERMISSIONS.CONFIG_PUBLISH, ADMIN_PERMISSIONS.CONFIG_ROLLBACK, ADMIN_PERMISSIONS.AUDIT_READ]) }),
  Object.freeze({ id: "editor", label: "Content Editor", description: "Prepare revision-backed changes and upload media, without publish or destructive media access.", permissions: Object.freeze([ADMIN_PERMISSIONS.CONFIG_DRAFT, ADMIN_PERMISSIONS.MEDIA_UPLOAD, ADMIN_PERMISSIONS.AUDIT_READ]) }),
  Object.freeze({ id: "media-manager", label: "Media Manager", description: "Upload and retire Admin-managed media without configuration publish rights.", permissions: Object.freeze([ADMIN_PERMISSIONS.MEDIA_UPLOAD, ADMIN_PERMISSIONS.MEDIA_DELETE, ADMIN_PERMISSIONS.AUDIT_READ]) }),
  Object.freeze({ id: "developer", label: "Developer / QA", description: "Read-oriented audit and Developer Tools access without configuration mutation.", permissions: Object.freeze([ADMIN_PERMISSIONS.AUDIT_READ, ADMIN_PERMISSIONS.DEVELOPER_INSPECT]) }),
  Object.freeze({ id: "viewer", label: "Viewer", description: "Normal read-only administration without audit, mutation or Developer Tools permissions.", permissions: Object.freeze([]) }),
]);

function roleTemplate(role) {
  return ADMIN_ROLE_TEMPLATES.find((entry) => entry.id === role) ?? null;
}

function permissionOverrides(raw) {
  if (typeof raw !== "string" || raw.trim() === "") return [];
  return raw.split(",").map((entry) => entry.trim()).filter(Boolean).map((entry) => {
    const operation = entry.startsWith("-") ? "remove" : "add";
    const permission = entry.replace(/^[+-]/, "");
    if (!KNOWN_PERMISSIONS.has(permission)) throw new TypeError(`Unknown Admin permission override: ${permission}`);
    return Object.freeze({ operation, permission });
  });
}

export function resolveAdminRolePermissions(role, overrideText = "") {
  const template = roleTemplate(role);
  const permissions = new Set(template?.permissions ?? []);
  const overrides = permissionOverrides(overrideText);
  for (const override of overrides) {
    if (override.operation === "remove") permissions.delete(override.permission);
    else permissions.add(override.permission);
  }
  return Object.freeze({
    roleKnown: template !== null,
    permissions: Object.freeze(SUPER_ADMIN_PERMISSIONS.filter((permission) => permissions.has(permission))),
    overrides: Object.freeze(overrides),
  });
}

function cleanText(value, fallback, max = 120) {
  if (typeof value !== "string") return fallback;
  const normalized = value.trim().replace(/\s+/g, " ");
  return normalized ? normalized.slice(0, max) : fallback;
}

export function createLocalAdminActor({
  actorId = "local-admin",
  displayName = "Local Admin",
  requestId = randomUUID(),
  role = "super-admin",
  permissionOverrideText = "",
} = {}) {
  const resolved = resolveAdminRolePermissions(role, permissionOverrideText);
  return Object.freeze({
    actorId: cleanText(actorId, "local-admin", 80),
    actorDisplayName: cleanText(displayName, "Local Admin", 120),
    authMethod: "local-admin-token",
    role: cleanText(role, "viewer", 80),
    roleKnown: resolved.roleKnown,
    requestId: cleanText(requestId, randomUUID(), 120),
    permissions: resolved.permissions,
    permissionOverrides: resolved.overrides,
    permissionCatalog: ADMIN_PERMISSION_CATALOG,
    roleTemplates: ADMIN_ROLE_TEMPLATES,
    roleAssignmentOwner: "deployment",
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
    // Role/permission ownership is server-side. Never trust a browser/request header to elevate access.
    role: process.env.TYPING_GAME_ADMIN_ROLE || "super-admin",
    permissionOverrideText: process.env.TYPING_GAME_ADMIN_PERMISSION_OVERRIDES || "",
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

export function describeConfigChangeScope({ baseRevision = null, targetRevision = null, baseConfig, targetConfig, maxPaths = 200 }) {
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
      actor: actor ? { actorId: actor.actorId, actorDisplayName: actor.actorDisplayName, authMethod: actor.authMethod, role: actor.role } : null,
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

export async function runAuthorizedAdminMutation({ actor, permission, auditLog, action, domain, entityType = null, entityId = null, changeScope = null, resolveEntityId = null, resolveChangeScope = null, onAuditError = () => undefined, operation }) {
  try {
    requireAdminPermission(actor, permission);
  } catch (error) {
    await recordAuditBestEffort(auditLog, { actor, action, domain, entityType, entityId, changeScope, result: "denied", error: error instanceof Error ? error.message : String(error) }, onAuditError);
    throw error;
  }
  await auditLog.record({ actor, action, domain, entityType, entityId, changeScope, result: "attempt" });
  let value;
  try {
    value = await operation();
  } catch (error) {
    await recordAuditBestEffort(auditLog, { actor, action, domain, entityType, entityId, changeScope, result: "error", error: error instanceof Error ? error.message : String(error) }, onAuditError);
    throw error;
  }
  const resolvedEntityId = typeof resolveEntityId === "function" ? resolveEntityId(value) : entityId;
  const resolvedChangeScope = typeof resolveChangeScope === "function" ? resolveChangeScope(value) : changeScope;
  await recordAuditBestEffort(auditLog, { actor, action, domain, entityType, entityId: resolvedEntityId ?? null, changeScope: resolvedChangeScope ?? null, result: "success" }, onAuditError);
  return value;
}
