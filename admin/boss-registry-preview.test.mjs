import test from "node:test";
import assert from "node:assert/strict";
import { parseBossRegistryPreviewOutput } from "./boss-registry-preview.mjs";

test("parses Bosses preview JSON after package-manager noise", () => {
  assert.deepEqual(
    parseBossRegistryPreviewOutput('noise\n{"protocolVersion":1,"configRevision":"x","bosses":[]}\n'),
    { protocolVersion: 1, configRevision: "x", bosses: [] },
  );
});

test("rejects output without a preview marker", () => {
  assert.throws(() => parseBossRegistryPreviewOutput("noise only"), /marker not found/);
});
