import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const childRoot = resolve(root, "games/space-typing");
// A10.5 re-audit: 4f62c94..6c57a2b changes only isolated Admin preview
// runtime modules for Enemy/Boss/Skill/Equipment/World/Stage. Background/VFX
// ownership, contracts and Admin write boundaries are unchanged; VFX stays
// runtime-backed read-only and Backgrounds stays runtime-derived read-only.
const VISUALS_AUDITED_CHILD_SHA = "6c57a2b7340b96a41e0f9f2b6fb5143ca532fd1c";
const childPath = new URL("../games/space-typing/contracts/space-typing-admin.v1.json", import.meta.url);
const snapshotPath = new URL("../portal/src/admin/contracts/space-typing-admin.v1.json", import.meta.url);

const [child, snapshot, backgrounds, vfx, router, server, backgroundsUi, vfxUi, vfxUiLegacy, phaseMap] = await Promise.all([
  readFile(childPath, "utf8").then(JSON.parse),
  readFile(snapshotPath, "utf8").then(JSON.parse),
  readFile(resolve(childRoot, "contracts/space-typing-admin-backgrounds.v1.json"), "utf8").then(JSON.parse),
  readFile(resolve(childRoot, "contracts/space-typing-admin-vfx.v1.json"), "utf8").then(JSON.parse),
  readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8"),
  readFile(resolve(root, "admin/server.mjs"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-backgrounds-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-vfx-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-vfx-phase-b-legacy.ts"), "utf8"),
  readFile(resolve(root, "admin/space-typing-phase-b-map.v1.json"), "utf8").then(JSON.parse),
]);
const vfxUiSurface = `${vfxUi}\n${vfxUiLegacy}`;

assert.equal(child.contractRevision, "space-typing-admin-v1");
assert.equal(child.schemaVersion, 1);
assert.equal(child.gameId, "space-typing");
assert.deepEqual(snapshot, child);

const childHead = execFileSync("git", ["-C", childRoot, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();
assert.equal(childHead, VISUALS_AUDITED_CHILD_SHA, `Visuals audit is stale: audited=${VISUALS_AUDITED_CHILD_SHA} pinned-child=${childHead}. Re-audit Backgrounds/VFX before changing this SHA.`);

assert.equal(backgrounds.capability, "backgrounds.read");
assert.equal(backgrounds.backgrounds?.mode, "runtime-derived-readonly");
assert.equal(backgrounds.backgrounds?.writeCapability, false);
assert.equal(backgrounds.backgrounds?.adminPreviewWriteCapability, false);
assert.equal(backgrounds.backgrounds?.applyBoundary, "none");
assert.deepEqual(backgrounds.backgrounds?.authorableFields, []);
assert.equal(backgrounds.backgrounds?.preview?.productionRenderer, true);

assert.equal(vfx.capability, "vfx.read");
assert.equal(vfx.vfx?.mode, "runtime-derived-readonly");
assert.equal(vfx.vfx?.runtimeOwner, "Game.ts direct VFX systems");
assert.deepEqual(vfx.vfx?.qualityTiers, ["low", "medium", "high", "ultra"]);
assert.equal(vfx.vfx?.writeCapability, false);
assert.equal(vfx.vfx?.adminPreviewWriteCapability, false);
assert.equal(vfx.vfx?.applyBoundary, "none");
assert.deepEqual(vfx.vfx?.authorableFields, []);
for (const domain of ["combat", "player-projectiles", "skill-effects", "boss-effects", "screen-feedback"]) {
  assert.ok(vfx.vfx?.domains?.includes(domain), `VFX domain missing: ${domain}`);
}

// A13/A10.5 route decoration is now part of the canonical shell. Keep exact
// route->renderer ownership while also protecting preview classification and
// role-aware action gates instead of freezing the old undecorated return text.
assert.match(router, /renderPhaseBBackgrounds/);
assert.match(router, /if \(path === `\$\{BASE\}\/backgrounds`\) return decorated\(path, renderPhaseBBackgrounds\(\)\);/);
assert.match(router, /renderPhaseBVfx/);
assert.match(router, /if \(path === `\$\{BASE\}\/vfx`\) return decorated\(path, renderPhaseBVfx\(\)\);/);
assert.match(router, /attachProductionPreviewClassification\(screen, path\)/);
assert.match(router, /attachRoleAwareActionGates\(screen\)/);

assert.match(server, /space-typing-admin-backgrounds\.v1\.json/);
assert.match(server, /space-typing-admin-vfx\.v1\.json/);
assert.match(server, /\/api\/admin\/space-typing\/backgrounds\/contract/);
assert.match(server, /\/api\/admin\/space-typing\/vfx\/contract/);
assert.doesNotMatch(server, /POST"&&url\.pathname==="\/api\/admin\/space-typing\/(?:backgrounds|vfx)/);
assert.match(backgroundsUi, /RUNTIME-BACKED · READ ONLY/);
assert.match(backgroundsUi, /\/api\/admin\/space-typing\/backgrounds\/contract/);
assert.doesNotMatch(backgroundsUi, /createRevision|\/publish/);

// A10.5 wraps the canonical read-only VFX inspector with a child-owned production
// combat preview. Validate both layers instead of freezing the old one-file presentation.
assert.match(vfxUi, /renderLegacyPhaseBVfx/);
assert.match(vfxUi, /createCombatVfxProductionPreviewPanel/);
assert.match(vfxUiSurface, /RUNTIME-BACKED · READ ONLY/);
assert.match(vfxUiSurface, /NO FAKE VFX PROFILE/);
assert.match(vfxUiSurface, /\/api\/admin\/space-typing\/vfx\/contract/);
assert.doesNotMatch(vfxUiSurface, /createRevision|\/publish|type\s*=\s*["']range["']/);

const backgroundsMap = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/backgrounds");
assert.equal(backgroundsMap?.status, "phase-b-ui-wired-runtime-backed-readonly");
assert.equal(backgroundsMap?.persistence, "source-owned-compositions-and-generated-kit-manifests");
assert.equal(backgroundsMap?.applyBoundary, "none");
const vfxMap = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/vfx");
assert.equal(vfxMap?.status, "phase-b-ui-wired-runtime-backed-readonly");
assert.equal(vfxMap?.persistence, "code-owned-runtime-vfx");
assert.equal(vfxMap?.applyBoundary, "none");

console.log(`Space Typing Admin contract core OK: ${child.contractRevision} · visuals pinned ${childHead.slice(0, 12)} · decorated Backgrounds/VFX routes remain runtime-backed read-only`);
