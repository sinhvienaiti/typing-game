import { createHash } from "node:crypto";
import { readFile, readdir } from "node:fs/promises";
import { extname, join, relative, sep } from "node:path";

const MUSIC_CATALOG = "src/audio/world-music-catalog.json";
const SHIP_3D_MANIFEST = "public/assets/space-typing/ships/3d/manifest.json";
const SHIP_3D_ROOT = "public/assets/space-typing/ships/3d";
const SFX_ROOT = "public/assets/audio/sfx";

function sha256(value) {
  return createHash("sha256").update(value).digest("hex");
}

function runtimePath(...parts) {
  return `/${parts.join("/").replaceAll("\\", "/").replace(/^\/+/, "")}`;
}

function mimeForPath(path) {
  switch (extname(path).toLowerCase()) {
    case ".ogg": return "audio/ogg";
    case ".mp3": return "audio/mpeg";
    case ".wav": return "audio/wav";
    case ".m4a": return "audio/mp4";
    case ".webm": return "audio/webm";
    case ".png": return "image/png";
    case ".webp": return "image/webp";
    case ".jpg":
    case ".jpeg": return "image/jpeg";
    case ".json": return "application/json";
    case ".bin": return "application/octet-stream";
    case ".glb": return "model/gltf-binary";
    case ".gltf": return "model/gltf+json";
    default: return "application/octet-stream";
  }
}

function formatForPath(path) {
  const extension = extname(path).toLowerCase();
  return extension ? extension.slice(1) : "bin";
}

function sanitizeIdPart(value) {
  return String(value)
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9._-]+/g, "-")
    .replace(/^-+|-+$/g, "") || "asset";
}

function compactIdPart(value, max = 96) {
  const normalized = sanitizeIdPart(value);
  if (normalized.length <= max) return normalized;
  return `${normalized.slice(0, Math.max(1, max - 13))}-${sha256(normalized).slice(0, 12)}`;
}

function roleFromPath(path) {
  if (path.length === 0) return "primary";
  return path
    .map((part) => typeof part === "number" ? String(part + 1) : sanitizeIdPart(part))
    .filter(Boolean)
    .join("-")
    .slice(0, 80) || "primary";
}

function collectPlaybackSources(value, path = [], sources = []) {
  if (Array.isArray(value)) {
    value.forEach((entry, index) => collectPlaybackSources(entry, [...path, index], sources));
    return sources;
  }
  if (value === null || typeof value !== "object") return sources;
  for (const [key, entry] of Object.entries(value)) {
    if (key === "src" && typeof entry === "string" && entry.startsWith("/")) {
      sources.push({ role: roleFromPath(path), runtimeUrl: entry });
      continue;
    }
    if (entry !== null && typeof entry === "object") collectPlaybackSources(entry, [...path, key], sources);
  }
  return sources;
}

function uniquePlaybackComponents(playback) {
  const sources = collectPlaybackSources(playback);
  const usedRoles = new Map();
  return sources.map(({ role, runtimeUrl }) => {
    const count = (usedRoles.get(role) ?? 0) + 1;
    usedRoles.set(role, count);
    const resolvedRole = count === 1 ? role : `${role}-${count}`.slice(0, 80);
    const pathWithoutQuery = runtimeUrl.split("?", 1)[0];
    return {
      role: resolvedRole,
      mimeType: mimeForPath(pathWithoutQuery),
      format: formatForPath(pathWithoutQuery),
      storageClass: "runtime-reference",
      runtimeUrl,
    };
  });
}

async function walkFiles(root) {
  let entries;
  try {
    entries = await readdir(root, { withFileTypes: true });
  } catch (error) {
    if (error?.code === "ENOENT") return [];
    throw error;
  }
  const files = [];
  for (const entry of entries.sort((a, b) => a.name.localeCompare(b.name))) {
    const absolute = join(root, entry.name);
    if (entry.isDirectory()) files.push(...await walkFiles(absolute));
    else if (entry.isFile() && !entry.name.startsWith(".")) files.push(absolute);
  }
  return files;
}

function summary() {
  return { created: 0, reused: 0, skipped: 0 };
}

function recordAdmission(result, counters) {
  if (result.created === false) counters.reused += 1;
  else counters.created += 1;
}

async function bootstrapMusic({ store, childRoot, actorId }) {
  const counters = summary();
  let catalog;
  try {
    catalog = JSON.parse(await readFile(join(childRoot, MUSIC_CATALOG), "utf8"));
  } catch (error) {
    if (error?.code === "ENOENT") return counters;
    throw error;
  }

  for (const track of Array.isArray(catalog.tracks) ? catalog.tracks : []) {
    if (!track || typeof track.id !== "string" || typeof track.title !== "string") {
      counters.skipped += 1;
      continue;
    }
    const components = uniquePlaybackComponents(track.playback);
    if (components.length === 0) {
      counters.skipped += 1;
      continue;
    }
    const legacyAdminUpload = track.metadata?.provenance === "local-admin-upload";
    const result = await store.registerReferenceAsset({
      assetId: `runtime.music.${compactIdPart(track.id, 120)}`,
      kind: "music",
      title: track.title,
      provenance: legacyAdminUpload ? "external-reference" : "code-owned",
      actorId,
      tags: ["music", legacyAdminUpload ? "legacy-admin-upload" : "runtime-catalog"],
      source: legacyAdminUpload
        ? {
            owner: "legacy-music-admin",
            generator: "MusicAssetService + world-music-catalog",
            sourcePath: MUSIC_CATALOG,
            note: "Imported by reference from legacy local-admin-upload provenance; Media V2 does not claim ownership of the existing child runtime binary.",
          }
        : {
            owner: "space-typing",
            generator: "world-music-catalog",
            sourcePath: MUSIC_CATALOG,
          },
      components,
    });
    recordAdmission(result, counters);
  }
  return counters;
}

async function shipBundleComponents(childRoot, shipId) {
  const definitions = [
    ["color", "color.webp"],
    ["emissive", "emissive.webp"],
    ["height", "height.bin"],
    ["model", "model.json"],
  ];
  const components = [];
  for (const [role, fileName] of definitions) {
    const diskPath = join(childRoot, SHIP_3D_ROOT, shipId, fileName);
    let bytes;
    try {
      bytes = await readFile(diskPath);
    } catch (error) {
      if (error?.code === "ENOENT") return null;
      throw error;
    }
    if (bytes.length === 0) return null;
    components.push({
      role,
      mimeType: mimeForPath(fileName),
      format: formatForPath(fileName),
      byteSize: bytes.length,
      sha256: sha256(bytes),
      storageClass: "runtime-reference",
      runtimeUrl: runtimePath("assets/space-typing/ships/3d", shipId, fileName),
    });
  }
  return components;
}

async function bootstrapShip3d({ store, childRoot, actorId }) {
  const counters = summary();
  let manifest;
  try {
    manifest = JSON.parse(await readFile(join(childRoot, SHIP_3D_MANIFEST), "utf8"));
  } catch (error) {
    if (error?.code === "ENOENT") return counters;
    throw error;
  }

  for (const rawId of Array.isArray(manifest.ships) ? manifest.ships : []) {
    if (typeof rawId !== "string" || rawId.trim() === "") {
      counters.skipped += 1;
      continue;
    }
    const shipId = compactIdPart(rawId, 100);
    const components = await shipBundleComponents(childRoot, shipId);
    if (components === null) {
      counters.skipped += 1;
      continue;
    }
    const result = await store.registerReferenceAsset({
      assetId: `runtime.ship-model.${shipId}`,
      kind: "model",
      title: `${rawId.replace(/[-_]+/g, " ").replace(/\b\w/g, (letter) => letter.toUpperCase())} 3D Ship`,
      provenance: "generated-runtime",
      actorId,
      tags: ["ship", "3d", "generated"],
      source: {
        owner: "space-typing",
        generator: "pnpm ship3d:prepare",
        sourcePath: `art-src/ships/${shipId}-top-hd.png`,
        note: "Source art is local/heavy and is not owned by Media V2; this record references generated runtime output only.",
      },
      components,
    });
    recordAdmission(result, counters);
  }
  return counters;
}

async function bootstrapSfx({ store, childRoot, actorId }) {
  const counters = summary();
  const root = join(childRoot, SFX_ROOT);
  for (const absolute of await walkFiles(root)) {
    const relativePath = relative(root, absolute).split(sep).join("/");
    const extension = extname(relativePath).toLowerCase();
    if (![".ogg", ".mp3", ".wav", ".m4a", ".webm"].includes(extension)) {
      counters.skipped += 1;
      continue;
    }
    const bytes = await readFile(absolute);
    if (bytes.length === 0) {
      counters.skipped += 1;
      continue;
    }
    const pathDigest = sha256(relativePath).slice(0, 12);
    const titleBase = relativePath.slice(0, -extension.length).replaceAll("/", " / ").replace(/[-_]+/g, " ");
    const result = await store.registerReferenceAsset({
      assetId: `runtime.sfx.${compactIdPart(relativePath.slice(0, -extension.length), 110)}.${pathDigest}`,
      kind: "sfx",
      title: titleBase.replace(/\b\w/g, (letter) => letter.toUpperCase()),
      provenance: "code-owned",
      actorId,
      tags: ["sfx", "runtime-static"],
      source: {
        owner: "space-typing",
        sourcePath: `${SFX_ROOT}/${relativePath}`,
        note: "Indexed as reference-only code-owned audio; Media V2 must not overwrite the project file in place.",
      },
      components: [{
        role: "primary",
        mimeType: mimeForPath(relativePath),
        format: formatForPath(relativePath),
        byteSize: bytes.length,
        sha256: sha256(bytes),
        storageClass: "runtime-reference",
        runtimeUrl: runtimePath("assets/audio/sfx", relativePath),
      }],
    });
    recordAdmission(result, counters);
  }
  return counters;
}

export async function bootstrapMediaReferences({ store, childRoot, actorId = "media-bootstrap" }) {
  if (!store || typeof store.registerReferenceAsset !== "function") throw new TypeError("bootstrapMediaReferences requires a MediaAssetStore-compatible store.");
  if (typeof childRoot !== "string" || childRoot.trim() === "") throw new TypeError("bootstrapMediaReferences requires childRoot.");

  const [music, shipModels, sfx] = await Promise.all([
    bootstrapMusic({ store, childRoot, actorId }),
    bootstrapShip3d({ store, childRoot, actorId }),
    bootstrapSfx({ store, childRoot, actorId }),
  ]);
  return {
    schemaVersion: 1,
    source: "space-typing-runtime-reference-bootstrap",
    music,
    shipModels,
    sfx,
    totals: {
      created: music.created + shipModels.created + sfx.created,
      reused: music.reused + shipModels.reused + sfx.reused,
      skipped: music.skipped + shipModels.skipped + sfx.skipped,
    },
  };
}
