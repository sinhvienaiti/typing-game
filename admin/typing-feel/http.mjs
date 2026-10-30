// Typing Feel routes (docs/games/TYPING_FEEL_SERVICE.md §3.12, §3.13).
//   /api/admin/shared/typing-feel/*      token-checked by server.mjs before this handler;
//                                        reads for any Admin role, drafts need config.draft,
//                                        Publish and Rollback need shared.publish.
//   /api/runtime/typing-feel/preview/*   no token (<audio> and the kit's fetch cannot send
//                                        one): read-only files of a checked revision.
//   /api/runtime/typing-feel/published/* no token: read-only set files as published under
//                                        TYPING_FEEL_PUBLIC_DIR (public anyway), for Media previews.
// Both handlers return true when they answered, false otherwise (like createMediaV2HttpHandler).
import { ADMIN_PERMISSIONS, AdminAuthorizationError, hasAdminPermission, runAuthorizedAdminMutation } from "../admin-security.mjs";
import { MediaAssetError } from "../media-assets-v2.mjs";
import { AdminConflictError, AdminValidationError } from "../store.mjs";
import { TypingFeelExportError } from "./export.mjs";
import { editorOptions } from "./policy.mjs";
import { TypingFeelNotFoundError, TypingFeelNotReadyError } from "./service.mjs";

export const TYPING_FEEL_ADMIN_BASE = "/api/admin/shared/typing-feel";
export const TYPING_FEEL_RUNTIME_BASE = "/api/runtime/typing-feel";
export const TYPING_FEEL_PERMISSIONS = Object.freeze({
  draft: ADMIN_PERMISSIONS.CONFIG_DRAFT,
  publish: ADMIN_PERMISSIONS.SHARED_PUBLISH,
  rollback: ADMIN_PERMISSIONS.SHARED_PUBLISH,
});
const JSON_BODY_LIMIT = 1024 * 1024;
const PREVIEW_PATH = /^\/preview\/([a-zA-Z0-9._-]{1,120})\/keys\/((?:sets\/[a-z0-9][a-z0-9-]{0,31}\/[0-9a-f]{12}\/(?:keys-manifest\.json|preview\.ogg|(?:key|space)-[0-9]{2,3}\.ogg))|keys-manifest\.json)$/;
// The games' own published copy of one set file (any revision, hidden sets too), for the
// Media Library's player: its Typing Feel versions point at /v1/keys/sets/…, which the
// Admin and portal origins do not serve.
const PUBLISHED_PATH = /^\/published\/keys\/(sets\/[a-z0-9][a-z0-9-]{0,31}\/[0-9a-f]{12}\/(?:keys-manifest\.json|preview\.ogg|(?:key|space)-[0-9]{2,3}\.ogg))$/;

class TypingFeelHttpError extends Error {
  constructor(message, status = 400, code = "typing-feel-request") {
    super(message);
    this.status = status;
    this.code = code;
  }
}

function json(response, status, body) {
  const data = JSON.stringify(body);
  response.writeHead(status, {
    "content-type": "application/json; charset=utf-8",
    "cache-control": "no-store",
    "content-length": Buffer.byteLength(data),
  });
  response.end(data);
}

async function readJsonBody(request) {
  const chunks = [];
  let size = 0;
  for await (const chunk of request) {
    size += chunk.length;
    if (size > JSON_BODY_LIMIT) throw new TypingFeelHttpError("Request body is too large.", 413, "payload-too-large");
    chunks.push(chunk);
  }
  if (size === 0) return {};
  try {
    const value = JSON.parse(Buffer.concat(chunks).toString("utf8"));
    if (value === null || typeof value !== "object" || Array.isArray(value)) throw new Error();
    return value;
  } catch {
    throw new TypingFeelHttpError("Request body must be a JSON object.", 400, "invalid-json");
  }
}

function answerError(response, error) {
  if (error instanceof TypingFeelHttpError) return json(response, error.status, { error: error.code, message: error.message });
  if (error instanceof AdminAuthorizationError) return json(response, 403, { error: "forbidden", message: error.message, permission: error.permission });
  if (error instanceof TypingFeelNotReadyError) return json(response, 409, { error: "typing-feel-not-imported", message: error.message });
  if (error instanceof TypingFeelNotFoundError) return json(response, 404, { error: "not-found", message: error.message });
  if (error instanceof AdminConflictError) return json(response, 409, { error: "conflict", message: error.message });
  if (error instanceof TypingFeelExportError) return json(response, 409, { error: "export", message: error.message, problems: error.problems });
  if (error instanceof AdminValidationError) return json(response, 400, { error: "validation", message: error.message, problems: error.problems ?? [error.message] });
  if (error instanceof MediaAssetError) return json(response, 400, { error: "media-asset", message: error.message });
  return null;
}

/**
 * `typingFeel` is the start-up result of setup.mjs:
 * { status: "available" | "not-initialized" | "unavailable" | "failed", service, message }.
 */
export function createTypingFeelHttpHandler({ typingFeel, auditLog, onAuditError = () => undefined }) {
  if (!typingFeel) throw new TypeError("createTypingFeelHttpHandler requires typingFeel.");
  if (!auditLog) throw new TypeError("createTypingFeelHttpHandler requires auditLog.");

  const mutation = (actor, options) => runAuthorizedAdminMutation({ actor, auditLog, onAuditError, domain: "typing-feel", entityType: "typing-feel-revision", ...options });

  return async function handleTypingFeelRequest({ request, response, url, actor }) {
    const path = url.pathname;
    if (path !== TYPING_FEEL_ADMIN_BASE && !path.startsWith(`${TYPING_FEEL_ADMIN_BASE}/`)) return false;
    const route = path.slice(TYPING_FEEL_ADMIN_BASE.length) || "/";
    const service = typingFeel.service;
    try {
      if (!service) {
        json(response, 503, { error: "typing-feel-unavailable", status: typingFeel.status, message: typingFeel.message });
        return true;
      }
      const permissions = {
        draft: hasAdminPermission(actor, TYPING_FEEL_PERMISSIONS.draft),
        publish: hasAdminPermission(actor, TYPING_FEEL_PERMISSIONS.publish),
        rollback: hasAdminPermission(actor, TYPING_FEEL_PERMISSIONS.rollback),
      };

      if (request.method === "GET" && route === "/state") {
        json(response, 200, { ...(await service.state()), startup: typingFeel.startup ?? null, permissions, requiredPermissions: TYPING_FEEL_PERMISSIONS, options: editorOptions(service.contract) });
        return true;
      }
      if (request.method === "GET" && route === "/draft") {
        const state = await service.state();
        if (!state.initialized) throw new TypingFeelNotReadyError();
        const active = await service.revision(state.state.activeRevision);
        const draft = state.draft ? await service.revision(state.draft.revision) : null;
        json(response, 200, { activeRevision: active.revision, active, draft });
        return true;
      }
      if (request.method === "GET" && route === "/history") {
        const state = await service.state();
        const events = hasAdminPermission(actor, ADMIN_PERMISSIONS.AUDIT_READ)
          ? (await auditLog.list({ limit: 500 })).filter((event) => event.domain === "typing-feel").slice(0, 100)
          : null;
        json(response, 200, { initialized: state.initialized, history: state.history ?? [], activeRevision: state.state?.activeRevision ?? null, events, eventsHidden: events === null });
        return true;
      }
      if (request.method === "GET" && route.startsWith("/revisions/")) {
        let revisionId;
        try {
          revisionId = decodeURIComponent(route.slice("/revisions/".length));
        } catch {
          throw new TypingFeelHttpError("Invalid revision id.", 400, "validation");
        }
        json(response, 200, await service.revision(revisionId));
        return true;
      }
      if (request.method === "GET" && route === "/library") {
        await service.requireInitialized();
        const revisionId = url.searchParams.get("revision") || (await service.store.getState()).activeRevision;
        json(response, 200, await service.library(revisionId));
        return true;
      }
      if (request.method === "GET" && route === "/export/status") {
        json(response, 200, await service.exportStatus());
        return true;
      }
      if (request.method === "POST" && route === "/validate-revision") {
        const input = await readJsonBody(request);
        json(response, 200, await service.validate(input.revision));
        return true;
      }
      if (request.method === "POST" && route === "/change-scope") {
        const input = await readJsonBody(request);
        json(response, 200, await service.changeScope(input.revision));
        return true;
      }
      // Read only: what a Rollback to `targetRevision` would change against the active revision (the confirm step shows it).
      if (request.method === "POST" && route === "/rollback-change-scope") {
        const input = await readJsonBody(request);
        await service.requireInitialized();
        json(response, 200, await service.rollbackChangeScope(input.targetRevision));
        return true;
      }
      if (request.method === "POST" && route === "/revisions") {
        const input = await readJsonBody(request);
        const revision = await mutation(actor, {
          permission: TYPING_FEEL_PERMISSIONS.draft,
          action: "typing-feel.revision.create",
          changeScope: { model: "typing-feel-revision", operation: "draft", baseRevision: input.baseRevision ?? null, affects: "all games" },
          resolveEntityId: (created) => created.revision,
          operation: () => service.saveDraft({ baseRevision: input.baseRevision, config: input.config, message: input.message, author: actor.actorId }),
        });
        json(response, 201, revision);
        return true;
      }
      if (request.method === "POST" && route === "/publish") {
        const input = await readJsonBody(request);
        const changeScope = hasAdminPermission(actor, TYPING_FEEL_PERMISSIONS.publish) ? await service.changeScope(input.revision).catch(() => null) : null;
        const result = await mutation(actor, {
          permission: TYPING_FEEL_PERMISSIONS.publish,
          action: "typing-feel.publish",
          entityId: input.revision ?? null,
          changeScope,
          operation: () => service.publish({ revision: input.revision, expectedActiveRevision: input.expectedActiveRevision, actorId: actor.actorId }),
        });
        json(response, 200, result);
        return true;
      }
      if (request.method === "POST" && route === "/rollback") {
        const input = await readJsonBody(request);
        const changeScope = hasAdminPermission(actor, TYPING_FEEL_PERMISSIONS.rollback) ? await service.rollbackChangeScope(input.targetRevision).catch(() => null) : null;
        const result = await mutation(actor, {
          permission: TYPING_FEEL_PERMISSIONS.rollback,
          action: "typing-feel.rollback",
          entityId: input.targetRevision ?? null,
          changeScope,
          operation: () => service.rollback({ targetRevision: input.targetRevision, expectedActiveRevision: input.expectedActiveRevision, actorId: actor.actorId }),
        });
        json(response, 200, result);
        return true;
      }
      json(response, 404, { error: "not-found" });
      return true;
    } catch (error) {
      if (answerError(response, error) === null) throw error;
      return true;
    }
  };
}

/** No-token, read-only preview of a checked revision's export (§3.12), served before the token check. */
export function createTypingFeelRuntimeHandler({ typingFeel }) {
  return async function handleTypingFeelRuntimeRequest({ request, response, url }) {
    const path = url.pathname;
    if (!path.startsWith(`${TYPING_FEEL_RUNTIME_BASE}/`)) return false;
    try {
      if (request.method !== "GET" && request.method !== "HEAD") {
        json(response, 405, { error: "method-not-allowed" });
        return true;
      }
      const route = path.slice(TYPING_FEEL_RUNTIME_BASE.length);
      const match = PREVIEW_PATH.exec(route);
      const published = match ? null : PUBLISHED_PATH.exec(route);
      if (!match && !published) {
        json(response, 404, { error: "not-found" });
        return true;
      }
      if (!typingFeel.service) {
        json(response, 503, { error: "typing-feel-unavailable", status: typingFeel.status });
        return true;
      }
      const file = match ? await typingFeel.service.previewFile(match[1], match[2]) : await typingFeel.service.publishedFile(published[1]);
      if (!file) {
        json(response, 404, { error: "not-found" });
        return true;
      }
      response.writeHead(200, {
        "content-type": file.contentType,
        "content-length": file.body.length,
        "cache-control": "no-store",
        "x-content-type-options": "nosniff",
      });
      response.end(request.method === "HEAD" ? undefined : file.body);
      return true;
    } catch (error) {
      if (answerError(response, error) === null) throw error;
      return true;
    }
  };
}
