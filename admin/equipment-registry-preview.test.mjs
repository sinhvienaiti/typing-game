import test from "node:test";
import assert from "node:assert/strict";
import { parseEquipmentRegistryPreviewOutput } from "./equipment-registry-preview.mjs";

test("parses equipment preview JSON after package-manager noise", () => {
  const preview = parseEquipmentRegistryPreviewOutput(`noise\n{\n  "protocolVersion": 1,\n  "configRevision": "equipment-admin-v1",\n  "equipment": []\n}\n`);
  assert.equal(preview.protocolVersion, 1);
  assert.equal(preview.configRevision, "equipment-admin-v1");
  assert.deepEqual(preview.equipment, []);
});

test("rejects output without a preview marker", () => {
  assert.throws(() => parseEquipmentRegistryPreviewOutput("not-json"), /marker/);
});
