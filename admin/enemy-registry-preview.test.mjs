import test from "node:test";
import assert from "node:assert/strict";
import { parseEnemyRegistryPreviewOutput } from "./enemy-registry-preview.mjs";

test("parses Enemies preview JSON after package-manager noise", () => {
  assert.deepEqual(
    parseEnemyRegistryPreviewOutput('noise\n{"protocolVersion":1,"configRevision":"x","enemies":[]}\n'),
    { protocolVersion: 1, configRevision: "x", enemies: [] },
  );
});

test("rejects output without a preview marker", () => {
  assert.throws(() => parseEnemyRegistryPreviewOutput("noise only"), /marker not found/);
});