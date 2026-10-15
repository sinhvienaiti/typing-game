import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const childRoot = resolve(root, "games/space-typing");
const [service, server, router, page, map, builder, library, model, adapter, controller] = await Promise.all([
  readFile(resolve(root, "admin/music-assets.mjs"), "utf8"),
  readFile(resolve(root, "admin/server.mjs"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-music-library-phase-b.ts"), "utf8"),
  readFile(resolve(root, "admin/space-typing-phase-b-map.v1.json"), "utf8").then(JSON.parse),
  readFile(resolve(childRoot, "scripts/music/build-world-music-catalog.mjs"), "utf8"),
  readFile(resolve(childRoot, "src/audio/music-library.ts"), "utf8"),
  readFile(resolve(childRoot, "src/audio/world-music-model.ts"), "utf8"),
  readFile(resolve(childRoot, "src/audio/world-music-adapter.ts"), "utf8"),
  readFile(resolve(childRoot, "src/audio/MusicController.ts"), "utf8"),
]);

assert.match(service, /public\/assets\/audio\/music/);
assert.match(service, /src\/audio\/world-music-catalog\.json/);
assert.match(service, /local-admin-upload/);
assert.match(service, /Only tracks uploaded through Local Admin may be deleted here/);
assert.match(service, /pnpm/);
assert.match(service, /music:catalog/);
assert.match(service, /96 \* 1024 \* 1024/);
assert.match(service, /world-\(0\[1-9\]\|\[1-4\]\[0-9\]\|50\)/);
assert.match(service, /duplicate|already exists/i);
assert.match(service, /await rm\(trackDir, \{ recursive: true, force: true \}\)/);

assert.match(builder, /world-music-catalog\.json/);
assert.match(builder, /public\/assets\/audio\/music/);
assert.match(builder, /duplicate track id/);
assert.match(builder, /createHash\("sha256"\)/);
assert.match(builder, /--check/);
assert.match(builder, /symlink escape/);
assert.match(builder, /loop:\s*track\.loop !== false/);

assert.match(model, /export type CatalogTrack/);
assert.match(model, /loop:\s*boolean/);
assert.match(model, /disabledTrackIds\?: readonly string\[\]/);
assert.match(model, /stages\?: Readonly<Record<string, WorldMusicPolicyEntry>>/);
assert.match(model, /worlds\?: Readonly<Record<string, WorldMusicPolicyEntry>>/);
assert.match(model, /galaxies\?: Readonly<Record<string, WorldMusicPolicyEntry>>/);
assert.match(model, /global\?: GlobalMusicPolicy/);

assert.match(library, /import catalogData from "\.\/world-music-catalog\.json"/);
assert.match(library, /materializeCatalogTrack/);
assert.match(library, /export const MUSIC_TRACKS/);
assert.match(library, /resolvePublishedWorldMusicPlaylist/);
assert.match(library, /legacyWorldPlaylist/);

assert.match(adapter, /import catalogData from "\.\/world-music-catalog\.json"/);
assert.match(adapter, /PUBLISHED_WORLD_MUSIC_POLICY/);
assert.match(adapter, /WORLD_MUSIC_CATALOG/);
assert.match(adapter, /resolveWorldMusicPlaylist/);
assert.match(adapter, /publishedMusicAssetForState/);

assert.match(controller, /from "\.\/music-library"/);
assert.match(controller, /this\.tracks = options\.tracks \?\? MUSIC_TRACKS/);

assert.match(server, /\/api\/admin\/space-typing\/music\/library/);
assert.match(server, /\/api\/admin\/space-typing\/music\/upload/);
assert.match(server, /\/api\/admin\/space-typing\/music\/tracks\//);
assert.match(router, /renderPhaseBMusicLibrary/);
assert.match(router, /if \(path === `\$\{BASE\}\/music-library`\) return decorated\(path, renderPhaseBMusicLibrary\(\)\);/);
assert.match(router, /attachProductionPreviewClassification\(screen, path\)/);
assert.match(router, /attachRoleAwareActionGates\(screen\)/);
assert.match(page, /RUNTIME CATALOG · CONNECTED/);
assert.match(page, /TEST PLAYBACK/);
assert.match(page, /Upload & rebuild catalog/);
assert.match(page, /DELETE · ADMIN UPLOADS ONLY/);
assert.match(page, /\/api\/admin\/space-typing\/music\/library/);
assert.match(page, /\/api\/admin\/space-typing\/music\/upload/);
assert.match(page, /\/api\/admin\/space-typing\/music\/tracks\//);
assert.match(page, /local-admin-upload/);
assert.match(page, /\/games\.json/);
assert.match(page, /source\.startsWith\("\/assets\/audio\/music\/"\)/);
assert.match(page, /new Audio\(productionMusicUrl/);
assert.match(page, /audio\.loop = track\.loop === true/);
assert.match(page, /<th>Source<\/th>/);
assert.match(page, /<th>Loop<\/th>/);
assert.match(page, /Context assignments and enabled\/disabled policy remain under World \/ Stage Music/);
assert.doesNotMatch(page, /trimGain[^\n]*(?:Volume|volume)/);
assert.doesNotMatch(page, /createRevision|\/publish|\/revisions/);

const row = map.screens.find((entry) => entry.route === "/admin/space-typing/music-library");
assert.ok(row, "Music Library Phase B map row is required");
assert.equal(row.domain, "music-assets");
assert.equal(row.persistence, "authored-asset-service");
assert.equal(row.applyBoundary, "catalog-rebuild");
assert.equal(row.status, "phase-b-ui-wired-runtime-catalog-authoring");

execFileSync(process.execPath, [resolve(childRoot, "scripts/music/build-world-music-catalog.mjs"), "--check"], {
  cwd: childRoot,
  stdio: "pipe",
});

console.log("Space Typing Music Library Admin validation passed: authored asset service -> deterministic catalog rebuild -> production source Test Playback; Context/Enabled stay owned by World Music policy -> canonical adapter/library -> production MusicController.");