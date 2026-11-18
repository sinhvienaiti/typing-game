import type { MediaAsset, MediaComponent, MediaVersion } from "./v2/media-api";

const EXACT_VERSION_ID = /^media-version\.[A-Za-z0-9][A-Za-z0-9._:-]{0,159}$/;
const SHA256 = /^[a-f0-9]{64}$/;

const REQUIRED_RELIEF_COMPONENTS = Object.freeze({
  color: "image/webp",
  emissive: "image/webp",
  height: "application/octet-stream",
  model: "application/json",
} as const);

type ReliefComponentRole = keyof typeof REQUIRED_RELIEF_COMPONENTS;

function requiredRole(role: string): role is ReliefComponentRole {
  return Object.prototype.hasOwnProperty.call(REQUIRED_RELIEF_COMPONENTS, role);
}

function compatibleComponent(component: MediaComponent): boolean {
  if (!requiredRole(component.role)) return true;
  return component.mimeType === REQUIRED_RELIEF_COMPONENTS[component.role]
    && typeof component.sha256 === "string"
    && SHA256.test(component.sha256);
}

/**
 * Parent-side discovery filter for A5.4. This intentionally mirrors only the
 * metadata that Media Admin owns. The child exact-version resolver remains
 * authoritative for runtime URLs, same-origin policy and materialization.
 */
export function isSpaceTypingReliefMediaVersionCompatible(
  asset: MediaAsset,
  version: MediaVersion,
): boolean {
  if (asset.kind !== "model" || version.assetId !== asset.assetId) return false;
  if (!EXACT_VERSION_ID.test(version.assetVersionId)) return false;
  if (!SHA256.test(version.contentFingerprint)) return false;

  const seen = new Set<ReliefComponentRole>();
  for (const component of version.components) {
    if (!requiredRole(component.role)) continue;
    if (seen.has(component.role) || !compatibleComponent(component)) return false;
    seen.add(component.role);
  }

  return (Object.keys(REQUIRED_RELIEF_COMPONENTS) as ReliefComponentRole[])
    .every((role) => seen.has(role));
}

export function reliefMediaCompatibilityLabel(version: MediaVersion): string {
  return isExactMediaVersionId(version.assetVersionId)
    ? `Exact version · ${version.assetVersionId}`
    : "Incompatible Media version";
}

export function isExactMediaVersionId(value: string): boolean {
  return EXACT_VERSION_ID.test(value);
}
