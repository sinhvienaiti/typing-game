import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const [architecture, service, tests, security, music, childPackage, childArtReadme, childShip3d, childAudioCheck] = await Promise.all([
  readFile("docs/SPACE_TYPING_ADMIN_V2_MEDIA_ARCHITECTURE.md", "utf8"),
  readFile("admin/media-assets-v2.mjs", "utf8"),
  readFile("admin/media-assets-v2.test.mjs", "utf8"),
  readFile("admin/admin-security.mjs", "utf8"),
  readFile("admin/music-assets.mjs", "utf8"),
  readFile("games/space-typing/package.json", "utf8"),
  readFile("games/space-typing/art-src/README.md", "utf8"),
  readFile("games/space-typing/scripts/bg-art/prepare-ship-3d.mjs", "utf8"),
  readFile("games/space-typing/scripts/check-audio-assets.mjs", "utf8"),
]);

for (const phrase of [
  "logical asset + immutable asset version",
  "Production references MUST NOT silently follow “latest”",
  "generated-runtime",
  "code-owned",
  "external-reference",
  "admin-upload",
  "Reference model (`usedBy`)",
  "No in-place binary overwrite",
  "Rollback contract",
  "Generated bundle policy",
  "Procedural VFX",
]) {
  assert.ok(architecture.includes(phrase), `Media architecture is missing locked decision: ${phrase}`);
}

assert.match(service, /export class MediaAssetStore/);
assert.match(service, /MEDIA_REGISTRY_SCHEMA_VERSION = 1/);
assert.match(service, /MEDIA_KINDS = Object\.freeze\(\["image", "model", "music", "sfx", "audio", "data"\]\)/);
assert.match(service, /MEDIA_PROVENANCE = Object\.freeze\(\["admin-upload", "generated-runtime", "code-owned", "external-reference"\]\)/);
assert.match(service, /join\(rootDir, "media-v2"\)/, "Media V2 store must live under Admin data root rather than child source tree.");
assert.match(service, /createUploadVersion/);
assert.match(service, /registerReferenceAsset/);
assert.match(service, /contentFingerprint/);
assert.match(service, /addReference/);
assert.match(service, /archiveAsset/);
assert.match(service, /hardDeleteVersion/);
assert.match(service, /is referenced and cannot be hard-deleted/);
assert.match(service, /Only unreferenced Admin-upload versions are eligible/);
assert.match(service, /runtimeUrl: `\/api\/admin\/space-typing\/media\/blobs\/\$\{encodeURIComponent\(version\.assetVersionId\)\}/);
assert.doesNotMatch(service, /art-src\//, "Canonical Media store must not directly mutate local heavy source-art paths.");
assert.doesNotMatch(service, /public\/assets\/space-typing/, "Canonical Media store must not hard-code generated runtime output as its writable blob owner.");

for (const behavior of [
  "replacement creates immutable versions",
  "references preserve historical versions",
  "generated multi-component bundles bootstrap idempotently",
  "archive hides an asset",
  "reference admission rejects mismatched asset/version pairs",
]) {
  assert.ok(tests.includes(behavior), `Media V2 tests are missing ${behavior}.`);
}

assert.match(security, /MEDIA_UPLOAD: "media\.upload"/);
assert.match(security, /MEDIA_DELETE: "media\.delete"/);
assert.match(music, /provenance: "local-admin-upload"/);
assert.match(childPackage, /"ship3d:prepare": "node scripts\/bg-art\/prepare-ship-3d\.mjs"/);
assert.match(childPackage, /"combat-vfx:prepare": "node scripts\/bg-art\/prepare-combat-vfx\.mjs"/);
assert.match(childArtReadme, /art-src\//);
assert.match(childArtReadme, /không đưa lên Git|Git bỏ qua/);
assert.match(childShip3d, /color\.webp/);
assert.match(childShip3d, /emissive\.webp/);
assert.match(childShip3d, /height\.bin/);
assert.match(childShip3d, /model\.json/);
assert.match(childShip3d, /manifest\.json/);
assert.match(childAudioCheck, /public\/assets\/audio\/sfx/);
assert.match(childAudioCheck, /createHash\("sha256"\)/);

console.log("Admin V2 A3.0 Media architecture foundation: OK (immutable logical/version model + reference-only bootstrap + bundle/reference/delete guards).");
