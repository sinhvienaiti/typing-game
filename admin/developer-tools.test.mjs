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
  assert.ok(paths.includes("/admin/space-typing/events"));
  assert.ok(paths.includes("/admin/space-typing/qa"));
  assert.ok(paths.includes("/admin/space-typing/media"));
  assert.ok(!paths.includes("/admin/space-typing/ships"), "Writable Ships must remain a primary administrator workflow");
  assert.ok(!paths.includes("/admin/space-typing/music-library"), "Writable Music Library must remain a primary administrator workflow");
  assert.ok(!paths.includes("/admin/space-typing/shop"), "A11 Shop offer authoring is now a primary Live Ops/economy workflow, not a developer-only contract dump");
});
