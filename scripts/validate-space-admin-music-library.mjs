import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const childRoot = resolve(root, "games/space-typing");
const [service, server, router, page, map, builder, runtime, controller] = await Promise.all([
  readFile(resolve(root, "admin/music-assets.mjs"), "utf8"),
  readFile(resolve(root, "admin/server.mjs"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-music-library-phase-b.ts"), "utf8"),
  readFile(resolve(root, "admin/space-typing-phase-b-map.v1.json"), "utf8").then(JSON.parse),
  readFile(resolve(childRoot, "scripts/music/build-world-music-catalog.mjs"), "utf8"),
  readFile(resolve(childRoot, "src/audio/world-music-runtime.ts"), "utf8"),
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

assert.match(runtime, /import catalogData from "\.\/world-music-catalog\.json"/);
assert.match(runtime, /BUNDLED_WORLD_MUSIC_CATALOG/);
assert.match(runtime, /materializeRuntimeMusicTracks/);
assert.match(controller, /BUNDLED_WORLD_MUSIC_CATALOG/);
assert.match(controller, /this\.catalog = options\.catalog/);
assert.match(controller, /materializeRuntimeMusicTracks\(this\.catalog/);

assert.match(server, /\/api\/admin\/space-typing\/music\/library/);
assert.match(server, /\/api\/admin\/space-typing\/music\/upload/);
assert.match(server, /\/api\/admin\/space-typing\/music\/tracks\//);
assert.match(router, /renderPhaseBMusicLibrary/);
assert.match(router, /\$\{BASE\}\/music-library`\) return renderPhaseBMusicLibrary\(\)/);
assert.match(page, /RUNTIME CATALOG · CONNECTED/);
assert.match(page, /Upload & rebuild catalog/);
assert.match(page, /DELETE · ADMIN UPLOADS ONLY/);
assert.match(page, /\/api\/admin\/space-typing\/music\/library/);
assert.match(page, /\/api\/admin\/space-typing\/music\/upload/);
assert.match(page, /\/api\/admin\/space-typing\/music\/tracks\//);
assert.match(page, /local-admin-upload/);
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

console.log("Space Typing Music Library Admin validation passed: authored asset service -> deterministic catalog rebuild -> production MusicController runtime catalog.");
