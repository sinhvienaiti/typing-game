import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const [
  architecture,
  service,
  tests,
  bootstrap,
  bootstrapTests,
  http,
  httpTests,
  ownershipTests,
  server,
  security,
  music,
  portalApi,
  library,
  libraryStyles,
  picker,
  pickerStyles,
  shell,
  command,
  childPackage,
  childArtReadme,
  childShip3d,
  childAudioCheck,
] = await Promise.all([
  readFile("docs/SPACE_TYPING_ADMIN_V2_MEDIA_ARCHITECTURE.md", "utf8"),
  readFile("admin/media-assets-v2.mjs", "utf8"),
  readFile("admin/media-assets-v2.test.mjs", "utf8"),
  readFile("admin/media-bootstrap.mjs", "utf8"),
  readFile("admin/media-bootstrap.test.mjs", "utf8"),
  readFile("admin/media-http.mjs", "utf8"),
  readFile("admin/media-http.test.mjs", "utf8"),
  readFile("admin/media-http-ownership.test.mjs", "utf8"),
  readFile("admin/server.mjs", "utf8"),
  readFile("admin/admin-security.mjs", "utf8"),
  readFile("admin/music-assets.mjs", "utf8"),
  readFile("portal/src/admin/v2/media-api.ts", "utf8"),
  readFile("portal/src/admin/v2/media-library.ts", "utf8"),
  readFile("portal/src/admin/v2/media-library.css", "utf8"),
  readFile("portal/src/admin/v2/asset-picker.ts", "utf8"),
  readFile("portal/src/admin/v2/asset-picker.css", "utf8"),
  readFile("portal/src/admin/space-typing.ts", "utf8"),
  readFile("portal/src/admin/space-typing-command.ts", "utf8"),
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

// A3.0 canonical immutable store.
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

// A3.0 reference-only bootstrap.
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
assert.match(http, /requireAdminOwnedAsset/, "Runtime/project-owned Media assets must be guarded from normal mutations.");
assert.match(http, /currentVersion\.provenance !== "admin-upload"/, "Only Admin-owned assets may accept normal replacement/archive mutations.");
assert.match(http, /read-only-owner/, "Reference-owned mutation rejection must expose a stable conflict code.");
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
assert.match(ownershipTests, /runtime-owned Media V2 assets reject replacement and archive mutations/);
assert.match(ownershipTests, /read-only-owner/);
assert.match(ownershipTests, /must not create a shadow Admin version/);

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

// A3.1 Portal client: no raw unauthenticated admin-blob URL assumptions.
assert.match(portalApi, /export class MediaAdminApi/);
assert.match(portalApi, /listAssets\(/);
assert.match(portalApi, /getAsset\(/);
assert.match(portalApi, /getVersion\(/);
assert.match(portalApi, /createAsset\(/);
assert.match(portalApi, /createVersion\(/);
assert.match(portalApi, /setArchived\(/);
assert.match(portalApi, /previewHandle\(/);
assert.match(portalApi, /x-typing-game-admin-token/, "Admin-owned blob previews must include the Admin token.");
assert.match(portalApi, /URL\.createObjectURL/, "Authenticated Admin blob previews must use an Object URL rather than unauthenticated img src.");
assert.match(portalApi, /URL\.revokeObjectURL/, "Object URL previews must expose cleanup.");
assert.match(portalApi, /component\.runtimeUrl/, "Reference-only media must keep its canonical runtime URL.");

// A3.1 Media Library administrator workflow.
assert.match(library, /export function renderAdminV2MediaLibrary/);
assert.match(library, /title: "Media Library"/);
assert.match(library, /createAdminSearchInput/);
assert.match(library, /createAdminEntityTable/);
assert.match(library, /Upload new media/);
assert.match(library, /upload creates library media only/i, "Upload workflow must state that upload alone does not alter gameplay.");
assert.match(library, /version\.provenance === "admin-upload"/, "Replace/archive controls must be ownership-aware.");
assert.match(library, /actor\.permissions\.includes\("media\.upload"\)/, "Upload UI must respect server permission state.");
assert.match(library, /actor\.permissions\.includes\("media\.delete"\)/, "Archive UI must respect server permission state.");
assert.match(library, /Upload new version/);
assert.match(library, /openAdminConfirmDialog/);
assert.match(library, /Read-only here\./, "Runtime/project-owned assets need an administrator-readable read-only explanation.");
assert.match(library, /document\.createElement|element\("details"/, "Technical metadata must be progressively disclosed rather than always visible.");
assert.match(library, /renderUsage/);
assert.match(library, /renderVersions/);
assert.match(library, /MutationObserver/, "Media preview Object URLs must be cleaned up on route teardown.");
assert.doesNotMatch(library, /hardDelete|hard delete/i, "Normal Media Library UI must not expose hard-delete workflow.");
assert.match(libraryStyles, /\.st-admin-v2-media-workspace/);
assert.match(libraryStyles, /\.st-admin-v2-media-preview/);
assert.match(libraryStyles, /@media\(max-width:1050px\)/);

// A3.1 exact-version Asset Picker contract for future Shop/Ships/etc.
assert.match(picker, /export type MediaAssetSelection/);
assert.match(picker, /asset: MediaAsset/);
assert.match(picker, /version: MediaVersion/);
assert.match(picker, /export function openAdminMediaAssetPicker/);
assert.match(picker, /allowedKinds/);
assert.match(picker, /selectedAssetVersionId/);
assert.match(picker, /Use selected version/);
assert.match(picker, /exact immutable media version/i);
assert.match(picker, /onSelect\(\{ asset: selectedAsset\.asset, version: selectedVersion \}\)/, "Picker must return an exact logical-asset/version pair.");
assert.match(picker, /event\.key === "Escape"/);
assert.match(picker, /event\.key !== "Tab"/);
assert.match(picker, /previousActive\?\.isConnected/, "Picker must restore focus.");
assert.match(picker, /previewHandle/, "Picker must preview through the authenticated/canonical Media client.");
assert.match(pickerStyles, /\.st-admin-v2-picker-backdrop/);
assert.match(pickerStyles, /\.st-admin-v2-picker-version\.selected/);
assert.match(pickerStyles, /@media\(max-width:780px\)/);

// Shell/command navigation: Media V2 is a real administrator workflow, not a Developer Tools inspector.
assert.match(shell, /import \{ renderAdminV2MediaLibrary \} from "\.\/v2\/media-library"/);
assert.match(shell, /label: "Media Library", path: `\$\{ADMIN_BASE\}\/media`/);
assert.match(shell, /if \(path === `\$\{ADMIN_BASE\}\/media`\) return renderAdminV2MediaLibrary\(this\.help\)/);
assert.match(command, /\["Media Library", `\$\{BASE\}\/media`, "Media"\]/);

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

console.log("Admin V2 A3.1 Media Library/Asset Picker: OK (immutable store + read-only runtime ownership + authenticated Portal workflow + exact-version picker).");
