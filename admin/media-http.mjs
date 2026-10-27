import { readFile } from "node:fs/promises";
import { ADMIN_PERMISSIONS, runAuthorizedAdminMutation } from "./admin-security.mjs";
import { MediaAssetError } from "./media-assets-v2.mjs";

export const MAX_MEDIA_UPLOAD_BYTES = 96 * 1024 * 1024;
const JSON_BODY_LIMIT = 64 * 1024;
const MEDIA_BASE = "/api/admin/space-typing/media";

class MediaHttpError extends Error {
  constructor(message, status = 400, code = "media-request") {
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

async function readBody(request, maxBytes) {
  const chunks = [];
  let size = 0;
  for await (const chunk of request) {
    size += chunk.length;
    if (size > maxBytes) throw new MediaHttpError("Media request body is too large.", 413, "payload-too-large");
    chunks.push(chunk);
  }
  return Buffer.concat(chunks);
}

async function readJsonBody(request) {
  const bytes = await readBody(request, JSON_BODY_LIMIT);
  if (bytes.length === 0) return {};
  try {
    return JSON.parse(bytes.toString("utf8"));
  } catch {
    throw new MediaHttpError("Media request body must be valid JSON.", 400, "invalid-json");
  }
}

function header(request, name, required = false) {
  const value = request.headers[name];
  const text = Array.isArray(value) ? value[0] : value;
  if (required && (typeof text !== "string" || !text.trim())) {
    throw new MediaHttpError(`Missing ${name} header.`, 400, "missing-header");
  }
  return typeof text === "string" ? text.trim() : undefined;
}

function parseTags(value) {
  if (!value) return [];
  return value.split(",").map((tag) => tag.trim()).filter(Boolean);
}

function decodeSegment(value, label) {
  try {
    const decoded = decodeURIComponent(value);
    if (!decoded) throw new Error();
    return decoded;
  } catch {
    throw new MediaHttpError(`Invalid ${label}.`, 400, "invalid-path");
  }
}

function mediaPathParts(pathname) {
  if (!pathname.startsWith(`${MEDIA_BASE}/`)) return null;
  return pathname.slice(MEDIA_BASE.length + 1).split("/").filter(Boolean);
}

function filterAssets(assets, searchParams) {
  const kind = searchParams.get("kind")?.trim();
  const query = searchParams.get("q")?.trim().toLowerCase();
  return assets.filter((asset) => !kind || asset.kind === kind).filter((asset) => {
    if (!query) return true;
    return [asset.assetId, asset.title, ...(asset.tags ?? [])].some((value) => String(value).toLowerCase().includes(query));
  });
}

function sendBlob(response, resolved, bytes) {
  response.writeHead(200, {
    "content-type": resolved.mimeType,
    "content-length": bytes.length,
    "cache-control": "private, max-age=31536000, immutable",
    etag: `"sha256-${resolved.sha256}"`,
    "x-content-type-options": "nosniff",
  });
  response.end(bytes);
}

export function createMediaV2HttpHandler({ store, auditLog, onAuditError = () => undefined } = {}) {
  if (!store) throw new TypeError("createMediaV2HttpHandler requires store.");
  if (!auditLog) throw new TypeError("createMediaV2HttpHandler requires auditLog.");

  // Serialize Media writes so independent HTTP read-modify-write mutations cannot lose one another.
  let mutationTail = Promise.resolve();
  const serializeMutation = (operation) => {
    const next = mutationTail.then(operation, operation);
    mutationTail = next.then(() => undefined, () => undefined);
    return next;
  };

  const requireAdminOwnedAsset = async (assetId) => {
    const asset = await store.getAsset(assetId);
    if (!asset.currentVersionId) {
      throw new MediaHttpError("This media asset has no current version and cannot be modified from the normal Media workflow.", 409, "read-only-owner");
    }
    const currentVersion = await store.getVersion(asset.currentVersionId);
    if (currentVersion.provenance !== "admin-upload") {
      throw new MediaHttpError(
        "This media asset is owned by the Space Typing runtime/project and is reference-only in Admin. Upload a new Admin-owned asset instead of replacing or archiving it.",
        409,
        "read-only-owner",
      );
    }
    return { asset, currentVersion };
  };

  return async function handleMediaV2Request({ request, response, url, actor }) {
    if (!url.pathname.startsWith(MEDIA_BASE)) return false;

    try {
      if (request.method === "GET" && url.pathname === `${MEDIA_BASE}/assets`) {
        const includeArchived = url.searchParams.get("includeArchived") === "true";
        const assets = filterAssets(await store.listAssets({ includeArchived }), url.searchParams);
        json(response, 200, { schemaVersion: 1, assets });
        return true;
      }

      const parts = mediaPathParts(url.pathname);
      if (!parts) return false;

      if (request.method === "GET" && parts[0] === "assets" && parts.length === 2) {
        const assetId = decodeSegment(parts[1], "asset id");
        const [asset, versions, references] = await Promise.all([
          store.getAsset(assetId),
          store.listVersions(assetId),
          store.listReferences({ assetId }),
        ]);
        json(response, 200, { schemaVersion: 1, asset, versions, references });
        return true;
      }

      if (request.method === "GET" && parts[0] === "assets" && parts[2] === "versions" && parts.length === 3) {
        const assetId = decodeSegment(parts[1], "asset id");
        json(response, 200, { schemaVersion: 1, versions: await store.listVersions(assetId) });
        return true;
      }

      if (request.method === "GET" && parts[0] === "assets" && parts[2] === "references" && parts.length === 3) {
        const assetId = decodeSegment(parts[1], "asset id");
        json(response, 200, { schemaVersion: 1, references: await store.listReferences({ assetId }) });
        return true;
      }

      if (request.method === "GET" && parts[0] === "versions" && parts.length === 2) {
        const assetVersionId = decodeSegment(parts[1], "asset version id");
        const [version, references] = await Promise.all([
          store.getVersion(assetVersionId),
          store.listReferences({ assetVersionId }),
        ]);
        json(response, 200, { schemaVersion: 1, version, references });
        return true;
      }

      if (request.method === "GET" && parts[0] === "blobs" && parts.length === 3) {
        const assetVersionId = decodeSegment(parts[1], "asset version id");
        const role = decodeSegment(parts[2], "component role");
        const resolved = await store.resolveComponent(assetVersionId, role);
        if (resolved.storageClass !== "admin-blob" || !resolved.absolutePath) {
          throw new MediaHttpError("This media component is owned by the runtime/project and must use its canonical runtime URL.", 409, "reference-only");
        }
        sendBlob(response, resolved, await readFile(resolved.absolutePath));
        return true;
      }

      if (request.method === "POST" && url.pathname === `${MEDIA_BASE}/assets`) {
        const kind = header(request, "x-media-kind", true);
        const title = header(request, "x-media-title", true);
        const fileName = header(request, "x-media-file-name", true);
        const mimeType = header(request, "content-type", true);
        const tags = parseTags(header(request, "x-media-tags"));
        const bytes = await readBody(request, MAX_MEDIA_UPLOAD_BYTES);
        const result = await serializeMutation(() => runAuthorizedAdminMutation({
          actor,
          permission: ADMIN_PERMISSIONS.MEDIA_UPLOAD,
          auditLog,
          onAuditError,
          action: "media.asset.create",
          domain: "media",
          entityType: "media-asset",
          changeScope: { model: "media-version", operation: "create-asset", kind, changesGameplay: false },
          resolveEntityId: (created) => created.asset.assetId,
          resolveChangeScope: (created) => ({
            model: "media-version",
            operation: "create-asset",
            assetId: created.asset.assetId,
            assetVersionId: created.version.assetVersionId,
            kind: created.asset.kind,
            changesGameplay: false,
          }),
          operation: () => store.createUploadAsset({
            kind,
            title,
            filename: fileName,
            mimeType,
            buffer: bytes,
            actorId: actor.actorId,
            tags,
          }),
        }));
        json(response, 201, result);
        return true;
      }

      if (request.method === "POST" && parts[0] === "assets" && parts[2] === "versions" && parts.length === 3) {
        const assetId = decodeSegment(parts[1], "asset id");
        await requireAdminOwnedAsset(assetId);
        const fileName = header(request, "x-media-file-name", true);
        const mimeType = header(request, "content-type", true);
        const role = header(request, "x-media-role") || "primary";
        const bytes = await readBody(request, MAX_MEDIA_UPLOAD_BYTES);
        const result = await serializeMutation(() => runAuthorizedAdminMutation({
          actor,
          permission: ADMIN_PERMISSIONS.MEDIA_UPLOAD,
          auditLog,
          onAuditError,
          action: "media.asset.version.create",
          domain: "media",
          entityType: "media-asset",
          entityId: assetId,
          changeScope: { model: "media-version", operation: "create-version", assetId, changesGameplay: false },
          resolveChangeScope: (created) => ({
            model: "media-version",
            operation: "create-version",
            assetId,
            assetVersionId: created.version.assetVersionId,
            changesGameplay: false,
          }),
          operation: () => store.createUploadVersion({
            assetId,
            filename: fileName,
            mimeType,
            buffer: bytes,
            role,
            actorId: actor.actorId,
          }),
        }));
        json(response, 201, result);
        return true;
      }

      if (request.method === "POST" && parts[0] === "assets" && parts[2] === "archive" && parts.length === 3) {
        const assetId = decodeSegment(parts[1], "asset id");
        await requireAdminOwnedAsset(assetId);
        const input = await readJsonBody(request);
        if (typeof input.archived !== "boolean") throw new MediaHttpError("archive request requires boolean archived.", 400, "validation");
        const result = await serializeMutation(() => runAuthorizedAdminMutation({
          actor,
          permission: ADMIN_PERMISSIONS.MEDIA_DELETE,
          auditLog,
          onAuditError,
          action: input.archived ? "media.asset.archive" : "media.asset.unarchive",
          domain: "media",
          entityType: "media-asset",
          entityId: assetId,
          changeScope: { model: "media-lifecycle", operation: input.archived ? "archive" : "unarchive", assetId, changesGameplay: false },
          operation: () => store.archiveAsset(assetId, { actorId: actor.actorId, archived: input.archived }),
        }));
        json(response, 200, result);
        return true;
      }

      json(response, 404, { error: "media-not-found" });
      return true;
    } catch (error) {
      if (error instanceof MediaHttpError) {
        json(response, error.status, { error: error.code, message: error.message });
        return true;
      }
      if (error instanceof MediaAssetError) {
        json(response, 400, { error: "media-asset", message: error.message });
        return true;
      }
      throw error;
    }
  };
}
