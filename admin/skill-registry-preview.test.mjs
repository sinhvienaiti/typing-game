import test from "node:test";
import assert from "node:assert/strict";
import { parseSkillRegistryPreviewOutput } from "./skill-registry-preview.mjs";

test("parses Skills preview JSON after package-manager noise", () => {
  assert.deepEqual(
    parseSkillRegistryPreviewOutput('noise\n{"protocolVersion":1,"configRevision":"x","skills":[]}\n'),
    { protocolVersion: 1, configRevision: "x", skills: [] },
  );
});

test("rejects output without a preview marker", () => {
  assert.throws(() => parseSkillRegistryPreviewOutput("noise only"), /marker not found/);
});
