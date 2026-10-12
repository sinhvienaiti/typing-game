import assert from "node:assert/strict";
import test from "node:test";
import { createDeveloperToolsManifest } from "./developer-tools.mjs";

test("Developer Tools manifest contains only explicit diagnostic migration routes", () => {
  const manifest = createDeveloperToolsManifest();
  assert.equal(manifest.version, 1);
  assert.equal(manifest.permission, "developer.runtime-inspect");
  assert.ok(manifest.sections.length >= 5);

  const tools = manifest.sections.flatMap((section) => section.tools);
  const paths = tools.map((tool) => tool.path);
  assert.equal(new Set(paths).size, paths.length, "Developer Tool paths must be unique");
  assert.ok(paths.includes("/admin/space-typing/shop"));
  assert.ok(paths.includes("/admin/space-typing/events"));
  assert.ok(paths.includes("/admin/space-typing/qa"));
  assert.ok(!paths.includes("/admin/space-typing/ships"), "Writable/revision-backed Ships must remain a primary administrator workflow");
  assert.ok(!paths.includes("/admin/space-typing/music-library"), "Writable Music Library must remain a primary administrator workflow");
});
