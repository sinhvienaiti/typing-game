import { readFile } from "node:fs/promises";
import { MediaAssetError } from "./media-assets-v2.mjs";

export const MEDIA_RUNTIME_BASE = "/api/runtime/space-typing/media";

export class MediaRuntimeError extends Error {
  constructor(message, status = 400, code = "media-runtime") {
    super(message);
    this.status = status;
    this.code = code;
  }
}

function cleanRuntimeUrl(value, role) {
  if (typeof value !== "string" || !value.startsWith("/") || value.startsWith("//")) {
    throw new MediaRuntimeError(
      `Media component ${role} is not a same-origin runtime resource.`,
      409,
      "unsupported-runtime-component",
    );
  }
  return value;
}

function runtimeBlobUrl(component) {
  const version = encodeURIComponent(component.assetVersionId);
  const role = encodeURIComponent(component.role);
  const hash = typeof component.sha256 === "string" ? component.sha256.slice(0, 16) : "immutable";
  return `${MEDIA_RUNTIME_BASE}/blobs/${version}/${role}?v=${hash}`;
}

function publicComponent(component) {
  let runtimeUrl;
  if (component.storageClass === "admin-blob") {
    runtimeUrl = runtimeBlobUrl(component);
  } else if (component.storageClass === "runtime-reference") {
    runtimeUrl = cleanRuntimeUrl(component.runtimeUrl, component.role);
  } else {
    throw new MediaRuntimeError(
      `Media component ${component.role} cannot be consumed by production runtime.`,
      409,
      "unsupported-runtime-component",
    );
  }

  const output = {
    role: component.role,
    mimeType: component.mimeType,
    storageClass: component.storageClass,
    runtimeUrl,
  };
  for (const key of ["format", "sha256", "byteSize", "width", "height", "durationSeconds"]) {
    if (component[key] !== undefined) output[key] = component[key];
  }
  return output;
}

export async function resolveExactRuntimeMediaVersion(store, assetVersionId) {
  if (!store || typeof store.getVersion !== "function" || typeof store.resolveComponent !== "function") {
    throw new TypeError("resolveExactRuntimeMediaVersion requires a MediaAssetStore-compatible store.");
  }
  if (typeof assetVersionId !== "string" || assetVersionId.trim() === "") {
    throw new MediaRuntimeError("assetVersionId is required.", 400, "invalid-version-id");
  }

  try {
    const version = await store.getVersion(assetVersionId);
    const asset = await store.getAsset(version.assetId);
    const components = [];
    for (const component of version.components) {
      components.push(publicComponent(await store.resolveComponent(version.assetVersionId, component.role)));
    }
    return {
      schemaVersion: 1,
      assetId: version.assetId,
      assetVersionId: version.assetVersionId,
      kind: asset.kind,
      provenance: version.provenance,
      contentFingerprint: version.contentFingerprint,
      components,
    };
  } catch (error) {
    if (error instanceof MediaRuntimeError) throw error;
    if (error instanceof MediaAssetError) {
      const unknown = String(error.message).startsWith("Unknown asset version:");
      throw new MediaRuntimeError(
        error.message,
        unknown ? 404 : 400,
        unknown ? "unknown-version" : "invalid-media-version",
      );
    }
    throw error;
  }
}

function pathParts(pathname) {
  if (!pathname.startsWith(`${MEDIA_RUNTIME_BASE}/`)) return null;
  return pathname.slice(MEDIA_RUNTIME_BASE.length + 1).split("/").filter(Boolean);
}

function decode(value, label) {
  try {
    const decoded = decodeURIComponent(value);
    if (!decoded) throw new Error();
    return decoded;
  } catch {
    throw new MediaRuntimeError(`Invalid ${label}.`, 400, "invalid-path");
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

function sendBlob(response, resolved, bytes) {
  response.writeHead(200, {
    "content-type": resolved.mimeType,
    "content-length": bytes.length,
    "cache-control": "public, max-age=31536000, immutable",
    etag: `"sha256-${resolved.sha256}"`,
    "x-content-type-options": "nosniff",
  });
  response.end(bytes);
}

export function createMediaRuntimeHttpHandler({ store, readFileImpl = readFile } = {}) {
  if (!store) throw new TypeError("createMediaRuntimeHttpHandler requires store.");

  return async function handleMediaRuntimeRequest({ request, response, url }) {
    if (request.method !== "GET" || !url.pathname.startsWith(MEDIA_RUNTIME_BASE)) return false;

    try {
      const parts = pathParts(url.pathname);
      if (!parts) return false;

      if (parts[0] === "versions" && parts.length === 2) {
        const assetVersionId = decode(parts[1], "asset version id");
        json(response, 200, await resolveExactRuntimeMediaVersion(store, assetVersionId));
        return true;
      }

      if (parts[0] === "blobs" && parts.length === 3) {
        const assetVersionId = decode(parts[1], "asset version id");
        const role = decode(parts[2], "component role");
        let resolved;
        try {
          resolved = await store.resolveComponent(assetVersionId, role);
        } catch (error) {
          if (error instanceof MediaAssetError) {
            throw new MediaRuntimeError(error.message, 404, "unknown-component");
          }
          throw error;
        }
        if (resolved.storageClass !== "admin-blob" || !resolved.absolutePath) {
          throw new MediaRuntimeError(
            "Only immutable Admin-owned blobs are served by this runtime blob route.",
            409,
            "reference-only",
          );
        }
        sendBlob(response, resolved, await readFileImpl(resolved.absolutePath));
        return true;
      }

      json(response, 404, { error: "media-runtime-not-found" });
      return true;
    } catch (error) {
      if (error instanceof MediaRuntimeError) {
        json(response, error.status, { error: error.code, message: error.message });
        return true;
      }
      throw error;
    }
  };
}
