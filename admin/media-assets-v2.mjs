import { createHash, randomUUID } from "node:crypto";
import { mkdir, readFile, rename, unlink, writeFile } from "node:fs/promises";
import { extname, join } from "node:path";

export class MediaAssetError extends Error {}

export const MEDIA_REGISTRY_SCHEMA_VERSION = 1;
export const MEDIA_KINDS = Object.freeze(["image", "model", "music", "sfx", "audio", "data"]);
export const MEDIA_PROVENANCE = Object.freeze(["admin-upload", "generated-runtime", "code-owned", "external-reference"]);
export const MEDIA_STORAGE_CLASSES = Object.freeze(["admin-blob", "runtime-reference", "source-reference", "external-reference"]);
export const MEDIA_LIFECYCLES = Object.freeze(["active", "archived"]);

const ID_PATTERN = /^[a-z0-9][a-z0-9._:-]{0,159}$/;
const ROLE_PATTERN = /^[a-z][a-z0-9._-]{0,79}$/;
const SHA_PATTERN = /^[a-f0-9]{64}$/;
const MIME_PATTERN = /^[a-z0-9][a-z0-9.+-]*\/[a-z0-9][a-z0-9.+-]*$/i;
const MAX_TEXT = 500;

function canonicalize(value) {
  if (Array.isArray(value)) return value.map(canonicalize);
  if (value !== null && typeof value === "object") {
    return Object.fromEntries(Object.keys(value).sort().map((key) => [key, canonicalize(value[key])]));
  }
  return value;
}

function serialize(value) {
  return `${JSON.stringify(canonicalize(value), null, 2)}\n`;
}

function hashJson(value) {
  return createHash("sha256").update(serialize(value)).digest("hex");
}

function cleanText(value, field, { min = 1, max = MAX_TEXT } = {}) {
  if (typeof value !== "string") throw new MediaAssetError(`${field} must be a string.`);
  const text = value.trim();
  if (text.length < min || text.length > max) {
    throw new MediaAssetError(`${field} must be between ${min} and ${max} characters.`);
  }
  return text;
}

function cleanOptionalText(value, field, max = MAX_TEXT) {
  if (value === undefined || value === null || value === "") return undefined;
  return cleanText(value, field, { max });
}

function cleanId(value, field) {
  const id = cleanText(value, field, { max: 160 });
  if (!ID_PATTERN.test(id)) throw new MediaAssetError(`${field} has an invalid identifier format.`);
  return id;
}

function cleanRole(value) {
  const role = cleanText(value, "component.role", { max: 80 });
  if (!ROLE_PATTERN.test(role)) throw new MediaAssetError(`Invalid component role: ${role}.`);
  return role;
}

function oneOf(value, field, allowed) {
  if (!allowed.includes(value)) throw new MediaAssetError(`${field} must be one of: ${allowed.join(", ")}.`);
  return value;
}

function optionalPositiveNumber(value, field) {
  if (value === undefined || value === null) return undefined;
  if (typeof value !== "number" || !Number.isFinite(value) || value <= 0) {
    throw new MediaAssetError(`${field} must be a positive finite number.`);
  }
  return value;
}

function optionalPositiveInteger(value, field) {
  if (value === undefined || value === null) return undefined;
  if (!Number.isInteger(value) || value <= 0) throw new MediaAssetError(`${field} must be a positive integer.`);
  return value;
}

function normalizeTags(tags) {
  if (tags === undefined) return [];
  if (!Array.isArray(tags)) throw new MediaAssetError("tags must be an array.");
  return [...new Set(tags.map((tag, index) => cleanText(tag, `tags[${index}]`, { max: 80 }).toLowerCase()))].sort();
}

function normalizeSource(source = {}) {
  if (source === null || typeof source !== "object" || Array.isArray(source)) {
    throw new MediaAssetError("source must be an object.");
  }
  const normalized = {};
  for (const key of ["owner", "generator", "sourcePath", "license", "note"]) {
    const value = cleanOptionalText(source[key], `source.${key}`, 500);
    if (value !== undefined) normalized[key] = value;
  }
  return normalized;
}

function safeExtension(filename) {
  const extension = extname(filename || "").toLowerCase();
  return /^\.[a-z0-9]{1,12}$/.test(extension) ? extension : "";
}

function normalizeReferenceComponent(component, index) {
  if (component === null || typeof component !== "object" || Array.isArray(component)) {
    throw new MediaAssetError(`components[${index}] must be an object.`);
  }
  const role = cleanRole(component.role);
  const storageClass = oneOf(component.storageClass, `components[${index}].storageClass`, [
    "runtime-reference",
    "source-reference",
    "external-reference",
  ]);
  const mimeType = cleanText(component.mimeType, `components[${index}].mimeType`, { max: 120 }).toLowerCase();
  if (!MIME_PATTERN.test(mimeType)) throw new MediaAssetError(`components[${index}].mimeType is invalid.`);
  const sha256 = cleanOptionalText(component.sha256, `components[${index}].sha256`, 64)?.toLowerCase();
  if (sha256 !== undefined && !SHA_PATTERN.test(sha256)) throw new MediaAssetError(`components[${index}].sha256 must be SHA-256.`);
  const runtimeUrl = cleanOptionalText(component.runtimeUrl, `components[${index}].runtimeUrl`, 1200);
  const sourcePath = cleanOptionalText(component.sourcePath, `components[${index}].sourcePath`, 1200);
  if (storageClass === "runtime-reference" && runtimeUrl === undefined) {
    throw new MediaAssetError(`components[${index}] runtime-reference requires runtimeUrl.`);
  }
  if (storageClass === "source-reference" && sourcePath === undefined) {
    throw new MediaAssetError(`components[${index}] source-reference requires sourcePath.`);
  }
  if (storageClass === "external-reference" && runtimeUrl === undefined) {
    throw new MediaAssetError(`components[${index}] external-reference requires runtimeUrl.`);
  }
  const normalized = {
    role,
    mimeType,
    storageClass,
  };
  const format = cleanOptionalText(component.format, `components[${index}].format`, 32)?.toLowerCase();
  if (format !== undefined) normalized.format = format;
  if (sha256 !== undefined) normalized.sha256 = sha256;
  const byteSize = optionalPositiveInteger(component.byteSize, `components[${index}].byteSize`);
  if (byteSize !== undefined) normalized.byteSize = byteSize;
  if (runtimeUrl !== undefined) normalized.runtimeUrl = runtimeUrl;
  if (sourcePath !== undefined) normalized.sourcePath = sourcePath;
  const width = optionalPositiveInteger(component.width, `components[${index}].width`);
  const height = optionalPositiveInteger(component.height, `components[${index}].height`);
  const durationSeconds = optionalPositiveNumber(component.durationSeconds, `components[${index}].durationSeconds`);
  if (width !== undefined) normalized.width = width;
  if (height !== undefined) normalized.height = height;
  if (durationSeconds !== undefined) normalized.durationSeconds = durationSeconds;
  return normalized;
}

function versionFingerprint({ provenance, components, source }) {
  return hashJson({ provenance, components: [...components].sort((a, b) => a.role.localeCompare(b.role)), source });
}

function assertUniqueRoles(components) {
  const seen = new Set();
  for (const component of components) {
    if (seen.has(component.role)) throw new MediaAssetError(`Duplicate component role: ${component.role}.`);
    seen.add(component.role);
  }
}

function createEmptyRegistry() {
  return {
    schemaVersion: MEDIA_REGISTRY_SCHEMA_VERSION,
    assets: {},
    versions: {},
    references: {},
  };
}

async function writeJsonAtomic(path, value) {
  const temporary = `${path}.${process.pid}.${randomUUID()}.tmp`;
  await writeFile(temporary, serialize(value), "utf8");
  await rename(temporary, path);
}

function validateRegistry(registry) {
  if (registry === null || typeof registry !== "object" || Array.isArray(registry)) throw new MediaAssetError("Media registry must be an object.");
  if (registry.schemaVersion !== MEDIA_REGISTRY_SCHEMA_VERSION) throw new MediaAssetError(`Unsupported Media registry schema version ${registry.schemaVersion}.`);
  if (registry.assets === null || typeof registry.assets !== "object" || Array.isArray(registry.assets)) throw new MediaAssetError("Media registry assets must be an object.");
  if (registry.versions === null || typeof registry.versions !== "object" || Array.isArray(registry.versions)) throw new MediaAssetError("Media registry versions must be an object.");
  if (registry.references === null || typeof registry.references !== "object" || Array.isArray(registry.references)) throw new MediaAssetError("Media registry references must be an object.");

  for (const [assetId, asset] of Object.entries(registry.assets)) {
    cleanId(assetId, "assetId");
    if (asset.assetId !== assetId) throw new MediaAssetError(`Asset key/id mismatch for ${assetId}.`);
    oneOf(asset.kind, `${assetId}.kind`, MEDIA_KINDS);
    oneOf(asset.lifecycle, `${assetId}.lifecycle`, MEDIA_LIFECYCLES);
    cleanText(asset.title, `${assetId}.title`, { max: 240 });
    if (asset.currentVersionId !== null) {
      const version = registry.versions[asset.currentVersionId];
      if (!version || version.assetId !== assetId) throw new MediaAssetError(`${assetId}.currentVersionId must reference a version of the same asset.`);
    }
  }

  for (const [assetVersionId, version] of Object.entries(registry.versions)) {
    cleanId(assetVersionId, "assetVersionId");
    if (version.assetVersionId !== assetVersionId) throw new MediaAssetError(`Version key/id mismatch for ${assetVersionId}.`);
    const asset = registry.assets[version.assetId];
    if (!asset) throw new MediaAssetError(`Version ${assetVersionId} references missing asset ${version.assetId}.`);
    oneOf(version.provenance, `${assetVersionId}.provenance`, MEDIA_PROVENANCE);
    if (!SHA_PATTERN.test(version.contentFingerprint)) throw new MediaAssetError(`${assetVersionId}.contentFingerprint must be SHA-256.`);
    if (!Array.isArray(version.components) || version.components.length === 0) throw new MediaAssetError(`${assetVersionId}.components must not be empty.`);
    assertUniqueRoles(version.components);
    for (const component of version.components) {
      cleanRole(component.role);
      oneOf(component.storageClass, `${assetVersionId}.${component.role}.storageClass`, MEDIA_STORAGE_CLASSES);
      if (version.provenance === "admin-upload") {
        if (component.storageClass !== "admin-blob") throw new MediaAssetError(`Admin-upload version ${assetVersionId} must use admin-blob components.`);
        if (!SHA_PATTERN.test(component.sha256 || "")) throw new MediaAssetError(`Admin blob ${assetVersionId}/${component.role} requires sha256.`);
        if (!Number.isInteger(component.byteSize) || component.byteSize <= 0) throw new MediaAssetError(`Admin blob ${assetVersionId}/${component.role} requires byteSize.`);
        if (typeof component.storageKey !== "string" || !/^blobs\/[a-f0-9]{64}(?:\.[a-z0-9]{1,12})?$/.test(component.storageKey)) {
          throw new MediaAssetError(`Admin blob ${assetVersionId}/${component.role} has invalid storageKey.`);
        }
      } else if (component.storageClass === "admin-blob") {
        throw new MediaAssetError(`Reference-only version ${assetVersionId} cannot own admin-blob components.`);
      }
    }
  }

  for (const [referenceId, reference] of Object.entries(registry.references)) {
    cleanId(referenceId, "referenceId");
    if (reference.referenceId !== referenceId) throw new MediaAssetError(`Reference key/id mismatch for ${referenceId}.`);
    const asset = registry.assets[reference.assetId];
    const version = registry.versions[reference.assetVersionId];
    if (!asset || !version || version.assetId !== asset.assetId) throw new MediaAssetError(`Reference ${referenceId} targets an invalid asset/version pair.`);
    for (const field of ["domain", "entityType", "entityId", "field"]) cleanText(reference[field], `${referenceId}.${field}`, { max: 200 });
  }
  return registry;
}

export class MediaAssetStore {
  constructor({ rootDir, now = () => new Date(), uuid = randomUUID } = {}) {
    if (!rootDir) throw new MediaAssetError("MediaAssetStore rootDir is required.");
    this.rootDir = rootDir;
    this.mediaRoot = join(rootDir, "media-v2");
    this.registryPath = join(this.mediaRoot, "registry.json");
    this.blobsDir = join(this.mediaRoot, "blobs");
    this.now = now;
    this.uuid = uuid;
  }

  async initialize() {
    await mkdir(this.blobsDir, { recursive: true });
    try {
      const registry = validateRegistry(JSON.parse(await readFile(this.registryPath, "utf8")));
      return structuredClone(registry);
    } catch (error) {
      if (error?.code !== "ENOENT") throw error;
    }
    const registry = createEmptyRegistry();
    try {
      await writeFile(this.registryPath, serialize(registry), { encoding: "utf8", flag: "wx" });
    } catch (error) {
      if (error?.code !== "EEXIST") throw error;
    }
    return this.readRegistry();
  }

  async readRegistry() {
    try {
      return validateRegistry(JSON.parse(await readFile(this.registryPath, "utf8")));
    } catch (error) {
      if (error?.code === "ENOENT") {
        await this.initialize();
        return validateRegistry(JSON.parse(await readFile(this.registryPath, "utf8")));
      }
      throw error;
    }
  }

  async writeRegistry(registry) {
    validateRegistry(registry);
    await writeJsonAtomic(this.registryPath, registry);
  }

  async listAssets({ includeArchived = false } = {}) {
    const registry = await this.readRegistry();
    return Object.values(registry.assets)
      .filter((asset) => includeArchived || asset.lifecycle !== "archived")
      .sort((a, b) => a.title.localeCompare(b.title) || a.assetId.localeCompare(b.assetId))
      .map((asset) => ({
        ...structuredClone(asset),
        versionCount: Object.values(registry.versions).filter((version) => version.assetId === asset.assetId).length,
        referenceCount: Object.values(registry.references).filter((reference) => reference.assetId === asset.assetId).length,
      }));
  }

  async getAsset(assetId) {
    const registry = await this.readRegistry();
    const asset = registry.assets[cleanId(assetId, "assetId")];
    if (!asset) throw new MediaAssetError(`Unknown asset: ${assetId}.`);
    return structuredClone(asset);
  }

  async listVersions(assetId) {
    const id = cleanId(assetId, "assetId");
    const registry = await this.readRegistry();
    if (!registry.assets[id]) throw new MediaAssetError(`Unknown asset: ${id}.`);
    return Object.values(registry.versions)
      .filter((version) => version.assetId === id)
      .sort((a, b) => b.createdAt.localeCompare(a.createdAt) || b.assetVersionId.localeCompare(a.assetVersionId))
      .map((version) => structuredClone(version));
  }

  async getVersion(assetVersionId) {
    const registry = await this.readRegistry();
    const version = registry.versions[cleanId(assetVersionId, "assetVersionId")];
    if (!version) throw new MediaAssetError(`Unknown asset version: ${assetVersionId}.`);
    return structuredClone(version);
  }

  async createUploadAsset({ kind, title, filename, mimeType, buffer, actorId = "local-admin", tags = [] }) {
    const assetId = `media.${this.uuid()}`;
    const now = this.now().toISOString();
    const registry = await this.readRegistry();
    registry.assets[assetId] = {
      assetId,
      kind: oneOf(kind, "kind", MEDIA_KINDS),
      title: cleanText(title, "title", { max: 240 }),
      lifecycle: "active",
      currentVersionId: null,
      tags: normalizeTags(tags),
      createdAt: now,
      createdBy: cleanText(actorId, "actorId", { max: 120 }),
      updatedAt: now,
      updatedBy: cleanText(actorId, "actorId", { max: 120 }),
    };
    await this.writeRegistry(registry);
    return this.createUploadVersion({ assetId, filename, mimeType, buffer, actorId, makeCurrent: true });
  }

  async createUploadVersion({ assetId, filename, mimeType, buffer, actorId = "local-admin", role = "primary", makeCurrent = true, width, height, durationSeconds }) {
    const id = cleanId(assetId, "assetId");
    if (!Buffer.isBuffer(buffer) || buffer.length === 0) throw new MediaAssetError("buffer must contain uploaded bytes.");
    const cleanMime = cleanText(mimeType, "mimeType", { max: 120 }).toLowerCase();
    if (!MIME_PATTERN.test(cleanMime)) throw new MediaAssetError("mimeType is invalid.");
    const registry = await this.readRegistry();
    const asset = registry.assets[id];
    if (!asset) throw new MediaAssetError(`Unknown asset: ${id}.`);

    const sha256 = createHash("sha256").update(buffer).digest("hex");
    const extension = safeExtension(filename);
    const storageKey = `blobs/${sha256}${extension}`;
    const absolute = join(this.mediaRoot, storageKey);
    try {
      await writeFile(absolute, buffer, { flag: "wx" });
    } catch (error) {
      if (error?.code !== "EEXIST") throw error;
      const existing = await readFile(absolute);
      const existingHash = createHash("sha256").update(existing).digest("hex");
      if (existingHash !== sha256) throw new MediaAssetError(`Blob collision detected for ${storageKey}.`);
    }

    const component = {
      role: cleanRole(role),
      mimeType: cleanMime,
      format: extension ? extension.slice(1) : cleanMime.split("/")[1]?.split("+")[0] || "bin",
      byteSize: buffer.length,
      sha256,
      storageClass: "admin-blob",
      storageKey,
    };
    const normalizedWidth = optionalPositiveInteger(width, "width");
    const normalizedHeight = optionalPositiveInteger(height, "height");
    const normalizedDuration = optionalPositiveNumber(durationSeconds, "durationSeconds");
    if (normalizedWidth !== undefined) component.width = normalizedWidth;
    if (normalizedHeight !== undefined) component.height = normalizedHeight;
    if (normalizedDuration !== undefined) component.durationSeconds = normalizedDuration;

    const now = this.now().toISOString();
    const assetVersionId = `media-version.${this.uuid()}`;
    const source = { owner: "admin-media-v2", sourcePath: cleanOptionalText(filename, "filename", 500) ?? "upload" };
    const version = {
      assetVersionId,
      assetId: id,
      provenance: "admin-upload",
      storageClass: "admin-blob",
      contentFingerprint: versionFingerprint({ provenance: "admin-upload", components: [component], source }),
      components: [component],
      source,
      createdAt: now,
      createdBy: cleanText(actorId, "actorId", { max: 120 }),
    };
    registry.versions[assetVersionId] = version;
    if (makeCurrent) {
      asset.currentVersionId = assetVersionId;
      asset.updatedAt = now;
      asset.updatedBy = version.createdBy;
    }
    await this.writeRegistry(registry);
    return { asset: structuredClone(asset), version: structuredClone(version) };
  }

  async registerReferenceAsset({ assetId, kind, title, provenance, components, actorId = "bootstrap", tags = [], source = {} }) {
    const id = cleanId(assetId, "assetId");
    const normalizedProvenance = oneOf(provenance, "provenance", MEDIA_PROVENANCE.filter((value) => value !== "admin-upload"));
    if (!Array.isArray(components) || components.length === 0) throw new MediaAssetError("components must not be empty.");
    const normalizedComponents = components.map(normalizeReferenceComponent).sort((a, b) => a.role.localeCompare(b.role));
    assertUniqueRoles(normalizedComponents);
    const normalizedSource = normalizeSource(source);
    const fingerprint = versionFingerprint({ provenance: normalizedProvenance, components: normalizedComponents, source: normalizedSource });
    const registry = await this.readRegistry();
    const now = this.now().toISOString();
    let asset = registry.assets[id];
    if (!asset) {
      asset = {
        assetId: id,
        kind: oneOf(kind, "kind", MEDIA_KINDS),
        title: cleanText(title, "title", { max: 240 }),
        lifecycle: "active",
        currentVersionId: null,
        tags: normalizeTags(tags),
        createdAt: now,
        createdBy: cleanText(actorId, "actorId", { max: 120 }),
        updatedAt: now,
        updatedBy: cleanText(actorId, "actorId", { max: 120 }),
      };
      registry.assets[id] = asset;
    } else {
      if (asset.kind !== kind) throw new MediaAssetError(`Asset ${id} kind is ${asset.kind}, not ${kind}.`);
      const existing = Object.values(registry.versions).find((version) => version.assetId === id && version.contentFingerprint === fingerprint);
      if (existing) return { asset: structuredClone(asset), version: structuredClone(existing), created: false };
      asset.title = cleanText(title, "title", { max: 240 });
      asset.tags = normalizeTags(tags);
      asset.updatedAt = now;
      asset.updatedBy = cleanText(actorId, "actorId", { max: 120 });
    }

    const assetVersionId = `media-version.${this.uuid()}`;
    const version = {
      assetVersionId,
      assetId: id,
      provenance: normalizedProvenance,
      storageClass: normalizedComponents[0].storageClass,
      contentFingerprint: fingerprint,
      components: normalizedComponents,
      source: normalizedSource,
      createdAt: now,
      createdBy: cleanText(actorId, "actorId", { max: 120 }),
    };
    registry.versions[assetVersionId] = version;
    asset.currentVersionId = assetVersionId;
    await this.writeRegistry(registry);
    return { asset: structuredClone(asset), version: structuredClone(version), created: true };
  }

  async archiveAsset(assetId, { actorId = "local-admin", archived = true } = {}) {
    const id = cleanId(assetId, "assetId");
    const registry = await this.readRegistry();
    const asset = registry.assets[id];
    if (!asset) throw new MediaAssetError(`Unknown asset: ${id}.`);
    asset.lifecycle = archived ? "archived" : "active";
    asset.updatedAt = this.now().toISOString();
    asset.updatedBy = cleanText(actorId, "actorId", { max: 120 });
    await this.writeRegistry(registry);
    return structuredClone(asset);
  }

  async addReference({ assetId, assetVersionId, domain, entityType, entityId, field, revisionId, actorId = "local-admin" }) {
    const id = cleanId(assetId, "assetId");
    const versionId = cleanId(assetVersionId, "assetVersionId");
    const registry = await this.readRegistry();
    const asset = registry.assets[id];
    const version = registry.versions[versionId];
    if (!asset || !version || version.assetId !== id) throw new MediaAssetError("Reference asset/version pair is invalid.");
    const normalized = {
      domain: cleanText(domain, "domain", { max: 200 }),
      entityType: cleanText(entityType, "entityType", { max: 200 }),
      entityId: cleanText(entityId, "entityId", { max: 200 }),
      field: cleanText(field, "field", { max: 200 }),
      revisionId: cleanOptionalText(revisionId, "revisionId", 200),
    };
    const duplicate = Object.values(registry.references).find((reference) =>
      reference.assetId === id &&
      reference.assetVersionId === versionId &&
      reference.domain === normalized.domain &&
      reference.entityType === normalized.entityType &&
      reference.entityId === normalized.entityId &&
      reference.field === normalized.field &&
      (reference.revisionId ?? undefined) === normalized.revisionId
    );
    if (duplicate) return structuredClone(duplicate);
    const referenceId = `media-ref.${this.uuid()}`;
    const reference = {
      referenceId,
      assetId: id,
      assetVersionId: versionId,
      domain: normalized.domain,
      entityType: normalized.entityType,
      entityId: normalized.entityId,
      field: normalized.field,
      createdAt: this.now().toISOString(),
      createdBy: cleanText(actorId, "actorId", { max: 120 }),
    };
    if (normalized.revisionId !== undefined) reference.revisionId = normalized.revisionId;
    registry.references[referenceId] = reference;
    await this.writeRegistry(registry);
    return structuredClone(reference);
  }

  async removeReference(referenceId) {
    const id = cleanId(referenceId, "referenceId");
    const registry = await this.readRegistry();
    const reference = registry.references[id];
    if (!reference) throw new MediaAssetError(`Unknown media reference: ${id}.`);
    delete registry.references[id];
    await this.writeRegistry(registry);
    return structuredClone(reference);
  }

  async listReferences({ assetId, assetVersionId } = {}) {
    const registry = await this.readRegistry();
    return Object.values(registry.references)
      .filter((reference) => assetId === undefined || reference.assetId === assetId)
      .filter((reference) => assetVersionId === undefined || reference.assetVersionId === assetVersionId)
      .sort((a, b) => a.createdAt.localeCompare(b.createdAt) || a.referenceId.localeCompare(b.referenceId))
      .map((reference) => structuredClone(reference));
  }

  async hardDeleteVersion(assetVersionId) {
    const versionId = cleanId(assetVersionId, "assetVersionId");
    const registry = await this.readRegistry();
    const version = registry.versions[versionId];
    if (!version) throw new MediaAssetError(`Unknown asset version: ${versionId}.`);
    if (version.provenance !== "admin-upload") throw new MediaAssetError("Only unreferenced Admin-upload versions are eligible for hard deletion.");
    const references = Object.values(registry.references).filter((reference) => reference.assetVersionId === versionId);
    if (references.length > 0) throw new MediaAssetError(`Asset version ${versionId} is referenced and cannot be hard-deleted.`);
    const asset = registry.assets[version.assetId];
    if (asset.currentVersionId === versionId) throw new MediaAssetError(`Asset version ${versionId} is current and cannot be hard-deleted.`);

    delete registry.versions[versionId];
    await this.writeRegistry(registry);

    for (const component of version.components) {
      const reused = Object.values(registry.versions).some((candidate) => candidate.components.some((item) => item.storageKey === component.storageKey));
      if (!reused && component.storageClass === "admin-blob") {
        try {
          await unlink(join(this.mediaRoot, component.storageKey));
        } catch (error) {
          if (error?.code !== "ENOENT") throw error;
        }
      }
    }
    return structuredClone(version);
  }

  async resolveComponent(assetVersionId, role = "primary") {
    const version = await this.getVersion(assetVersionId);
    const component = version.components.find((candidate) => candidate.role === role);
    if (!component) throw new MediaAssetError(`Asset version ${assetVersionId} has no ${role} component.`);
    if (component.storageClass === "admin-blob") {
      return {
        ...structuredClone(component),
        assetVersionId: version.assetVersionId,
        assetId: version.assetId,
        absolutePath: join(this.mediaRoot, component.storageKey),
        runtimeUrl: `/api/admin/space-typing/media/blobs/${encodeURIComponent(version.assetVersionId)}/${encodeURIComponent(component.role)}?v=${component.sha256.slice(0, 16)}`,
      };
    }
    return {
      ...structuredClone(component),
      assetVersionId: version.assetVersionId,
      assetId: version.assetId,
    };
  }
}
