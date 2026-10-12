import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const [architecture, service, tests, bootstrap, bootstrapTests, http, httpTests, server, security, music, childPackage, childArtReadme, childShip3d, childAudioCheck] = await Promise.all([
  readFile("docs/SPACE_TYPING_ADMIN_V2_MEDIA_ARCHITECTURE.md", "utf8"),
  readFile("admin/media-assets-v2.mjs", "utf8"),
  readFile("admin/media-assets-v2.test.mjs", "utf8"),
  readFile("admin/media-bootstrap.mjs", "utf8"),
  readFile("admin/media-bootstrap.test.mjs", "utf8"),
  readFile("admin/media-http.mjs", "utf8"),
  readFile("admin/media-http.test.mjs", "utf8"),
  readFile("admin/server.mjs", "utf8"),
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

assert.match(bootstrap, /export async function bootstrapMediaReferences/);
assert.match(bootstrap, /runtime\.music\./, "Music bootstrap must use deterministic namespaced logical asset IDs.");
assert.match(bootstrap, /runtime\.ship-model\./, "Ship bundle bootstrap must use deterministic namespaced logical asset IDs.");
assert.match(bootstrap, /runtime\.sfx\./, "SFX bootstrap must use deterministic namespaced logical asset IDs.");
assert.match(bootstrap, /provenance: legacyAdminUpload \? "external-reference" : "code-owned"/, "Legacy Music uploads must not masquerade as canonical Media V2 admin blobs.");
assert.match(bootstrap, /provenance: "generated-runtime"/, "Ship bundle bootstrap must preserve generated-runtime provenance.");
assert.match(bootstrap, /provenance: "code-owned"/, "Static SFX bootstrap must preserve code-owned provenance.");
assert.match(bootstrap, /sha256: sha256\(bytes\)/, "Reference bootstrap must fingerprint locally available runtime bytes.");
assert.match(bootstrap, /if \(error\?\.code === "ENOENT"\) return null/, "Incomplete generated ship bundles must fail closed/skip rather than fabricate components.");
assert.doesNotMatch(bootstrap, /copyFile|rename\(|unlink\(|writeFile\(/, "Reference bootstrap must never copy/move/delete/overwrite runtime binaries.");

for (const behavior of [
  "bootstrap as reference-only assets idempotently",
  "bundle byte changes create a new immutable reference version",
  "bundles are skipped rather than fabricated",
  "pinned Space Typing runtime tree bootstraps without binary copies or duplicate versions",
]) {
  assert.ok(bootstrapTests.includes(behavior), `Media bootstrap tests are missing ${behavior}.`);
}
assert.match(bootstrapTests, /media-v2\/blobs/);
assert.match(bootstrapTests, /legacy local-admin-upload bytes must not be misrepresented as Media V2 admin blobs/);

// A3.1 backend boundary: authenticated handler, exact-version blob serving and permission/audit guarded mutations.
assert.match(http, /export function createMediaV2HttpHandler/);
assert.match(http, /MAX_MEDIA_UPLOAD_BYTES = 96 \* 1024 \* 1024/);
assert.match(http, /ADMIN_PERMISSIONS\.MEDIA_UPLOAD/);
assert.match(http, /ADMIN_PERMISSIONS\.MEDIA_DELETE/);
assert.match(http, /runAuthorizedAdminMutation/);
assert.match(http, /action: "media\.asset\.create"/);
assert.match(http, /action: "media\.asset\.version\.create"/);
assert.match(http, /action: input\.archived \? "media\.asset\.archive" : "media\.asset\.unarchive"/);
assert.match(http, /changesGameplay: false/);
assert.match(http, /private, max-age=31536000, immutable/);
assert.match(http, /reference-only/);
assert.match(http, /serializeMutation/, "Media HTTP writes must be serialized to avoid registry lost updates.");
assert.doesNotMatch(http, /hardDeleteVersion/, "Normal Media HTTP API must not expose hard-delete operations.");
for (const behavior of [
  "creates immutable assets, lists them and serves exact Admin blobs",
  "replacement creates a new version without mutating the old blob",
  "archive\/unarchive uses media.delete permission but never hard-deletes versions",
  "Media write permission fails closed and records denied audit",
  "serializes concurrent uploads so registry admissions are not lost",
]) {
  assert.match(httpTests, new RegExp(behavior), `Media HTTP tests are missing ${behavior}.`);
}

assert.match(server, /import \{ MediaAssetStore \} from "\.\/media-assets-v2\.mjs"/);
assert.match(server, /import \{ bootstrapMediaReferences \} from "\.\/media-bootstrap\.mjs"/);
assert.match(server, /import \{ createMediaV2HttpHandler \} from "\.\/media-http\.mjs"/);
assert.match(server, /new MediaAssetStore\(\{ rootDir: adminDataDir \}\)/);
assert.match(server, /await mediaAssetsV2\.initialize\(\)/);
assert.match(server, /await bootstrapMediaReferences\(\{ store: mediaAssetsV2, childRoot: resolve\(root, "games\/space-typing"\) \}\)/);
assert.match(server, /createMediaV2HttpHandler\(\{/);
assert.match(server, /if \(await handleMediaV2Request\(\{ request, response, url, actor \}\)\) return/);
assert.ok(
  server.indexOf('if (!authorized(request))') < server.indexOf('if (await handleMediaV2Request({ request, response, url, actor })) return;'),
  "Media V2 handler must stay behind the existing global Admin token check.",
);

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

console.log("Admin V2 Media foundation/API: OK (immutable store + reference bootstrap + authenticated permission/audit HTTP boundary).");
