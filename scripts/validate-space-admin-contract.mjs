import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const childRoot = resolve(root, "games/space-typing");
const VISUALS_AUDITED_CHILD_SHA = "5cc2de2f0a88400ae6531dc05b67b033196126ca";
const childPath = new URL(
  "../games/space-typing/contracts/space-typing-admin.v1.json",
  import.meta.url,
);
const snapshotPath = new URL(
  "../portal/src/admin/contracts/space-typing-admin.v1.json",
  import.meta.url,
);

const [child, snapshot, backgrounds, vfx, backgroundBudgetSource, qualitySource, router, server, backgroundsUi, vfxUi, phaseMap] = await Promise.all([
  readFile(childPath, "utf8").then(JSON.parse),
  readFile(snapshotPath, "utf8").then(JSON.parse),
  readFile(resolve(childRoot, "contracts/space-typing-admin-backgrounds.v1.json"), "utf8").then(JSON.parse),
  readFile(resolve(childRoot, "contracts/space-typing-admin-vfx.v1.json"), "utf8").then(JSON.parse),
  readFile(resolve(childRoot, "src/background/budget.ts"), "utf8"),
  readFile(resolve(childRoot, "src/performance/quality.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8"),
  readFile(resolve(root, "admin/server.mjs"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-backgrounds-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-vfx-phase-b.ts"), "utf8"),
  readFile(resolve(root, "admin/space-typing-phase-b-map.v1.json"), "utf8").then(JSON.parse),
]);

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
for (const [tier, expected] of Object.entries(backgrounds.backgrounds.qualityBudgets)) {
  for (const [field, value] of Object.entries(expected)) {
    const literal = Number.isInteger(value) && Math.abs(value) >= 1000
      ? String(value).replace(/000$/, "_000")
      : String(value);
    assert.ok(
      backgroundBudgetSource.includes(`${field}: ${literal}`) || backgroundBudgetSource.includes(`${field}: ${value}`),
      `Background ${tier} budget drifted: ${field}=${value}`,
    );
  }
}

assert.equal(vfx.capability, "vfx.read");
assert.equal(vfx.vfx?.mode, "runtime-derived-readonly");
assert.equal(vfx.vfx?.runtimeOwner, "Game.ts direct VFX systems");
assert.deepEqual(vfx.vfx?.qualityTiers, ["low", "medium", "high", "ultra"]);
assert.equal(vfx.vfx?.writeCapability, false);
assert.equal(vfx.vfx?.adminPreviewWriteCapability, false);
assert.equal(vfx.vfx?.applyBoundary, "none");
assert.deepEqual(vfx.vfx?.authorableFields, []);
assert.ok(vfx.vfx?.domains?.includes("combat"));
assert.ok(vfx.vfx?.domains?.includes("player-projectiles"));
assert.ok(vfx.vfx?.domains?.includes("skill-effects"));
assert.ok(vfx.vfx?.domains?.includes("boss-effects"));
assert.ok(vfx.vfx?.domains?.includes("screen-feedback"));
for (const [tier, expected] of Object.entries(vfx.vfx.qualityProfiles)) {
  for (const [field, value] of Object.entries(expected)) {
    const normalized = String(value).replace(/000$/, "_000");
    assert.ok(
      qualitySource.includes(`${field}: ${value}`) || qualitySource.includes(`${field}: ${normalized}`),
      `VFX ${tier} quality profile drifted: ${field}=${value}`,
    );
  }
}

assert.match(router, /renderPhaseBBackgrounds/);
assert.match(router, /\$\{BASE\}\/backgrounds`\) return renderPhaseBBackgrounds\(\)/);
assert.match(router, /renderPhaseBVfx/);
assert.match(router, /\$\{BASE\}\/vfx`\) return renderPhaseBVfx\(\)/);
assert.match(server, /space-typing-admin-backgrounds\.v1\.json/);
assert.match(server, /space-typing-admin-vfx\.v1\.json/);
assert.match(server, /\/api\/admin\/space-typing\/backgrounds\/contract/);
assert.match(server, /\/api\/admin\/space-typing\/vfx\/contract/);
assert.doesNotMatch(server, /POST"&&url\.pathname==="\/api\/admin\/space-typing\/(?:backgrounds|vfx)/);
assert.match(backgroundsUi, /RUNTIME-BACKED · READ ONLY/);
assert.match(backgroundsUi, /\/api\/admin\/space-typing\/backgrounds\/contract/);
assert.doesNotMatch(backgroundsUi, /createRevision|\/publish/);
assert.match(vfxUi, /RUNTIME-BACKED · READ ONLY/);
assert.match(vfxUi, /NO FAKE VFX PROFILE/);
assert.match(vfxUi, /\/api\/admin\/space-typing\/vfx\/contract/);
assert.doesNotMatch(vfxUi, /createRevision|\/publish|type\s*=\s*["']range["']/);

const backgroundsMap = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/backgrounds");
assert.equal(backgroundsMap?.status, "phase-b-ui-wired-runtime-backed-readonly");
assert.equal(backgroundsMap?.persistence, "source-owned-compositions-and-generated-kit-manifests");
assert.equal(backgroundsMap?.applyBoundary, "none");
const vfxMap = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/vfx");
assert.equal(vfxMap?.status, "phase-b-ui-wired-runtime-backed-readonly");
assert.equal(vfxMap?.persistence, "code-owned-runtime-vfx");
assert.equal(vfxMap?.applyBoundary, "none");

console.log(
  `Space Typing Admin contracts OK: ${child.contractRevision} · visuals re-audited ${childHead.slice(0, 12)} · Backgrounds/VFX runtime-backed read-only`,
);

await import("./validate-space-admin-music-library.mjs");
