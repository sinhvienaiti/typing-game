import assert from "node:assert/strict";
import test from "node:test";
import { createDeveloperToolsManifest } from "./developer-tools.mjs";

test("A15 Developer Tools manifest exposes the five consolidated diagnostic workspaces", () => {
  const manifest = createDeveloperToolsManifest();
  assert.equal(manifest.version, 2);
  assert.equal(manifest.permission, "developer.runtime-inspect");
  assert.deepEqual(manifest.sections.map((section) => section.id), [
    "runtime-inspector",
    "contract-inspector",
    "validation",
    "asset-diagnostics",
    "qa-sandbox",
  ]);

  const tools = manifest.sections.flatMap((section) => section.tools);
  const paths = tools.map((tool) => tool.path);
  assert.equal(new Set(paths).size, paths.length, "Developer Tool paths must be unique");
  for (const path of [
    "/admin/space-typing/analytics",
    "/admin/space-typing/currencies",
    "/admin/space-typing/rewards",
    "/admin/space-typing/warp",
    "/admin/space-typing/expedition",
    "/admin/space-typing/missions",
    "/admin/space-typing/daily-weekly",
    "/admin/space-typing/events",
    "/admin/space-typing/duel",
    "/admin/space-typing/ranked",
    "/admin/space-typing/alternative-modes",
    "/admin/space-typing/feature-gates",
    "/admin/space-typing/media",
    "/admin/space-typing/backgrounds",
    "/admin/space-typing/vfx",
    "/admin/space-typing/ui-assets",
    "/admin/space-typing/qa",
  ]) assert.ok(paths.includes(path), `A15 diagnostic route missing: ${path}`);

  assert.ok(!paths.includes("/admin/space-typing/ships"), "Writable Ships must remain a primary administrator workflow");
  assert.ok(!paths.includes("/admin/space-typing/music-library"), "Writable Music Library must remain a primary administrator workflow");
  assert.ok(!paths.includes("/admin/space-typing/shop"), "A11 Shop offer authoring is a primary Live Ops/economy workflow, not a developer-only contract dump");
  assert.ok(!paths.includes("/admin/space-typing/roles"), "A13 Roles & Permissions must remain a normal System workflow");
});
