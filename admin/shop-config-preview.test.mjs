import test from "node:test";
import assert from "node:assert/strict";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { runShopConfigPreview } from "./shop-config-preview.mjs";

const rootDir = resolve(fileURLToPath(new URL("..", import.meta.url)));
const contract = {
  runtime: { applyBoundary: "new-session+new-shop-instance" },
  previewProtocol: {
    version: 1,
    available: true,
    plannedCommand: "pnpm shop:admin-preview",
  },
};

test("canonical Shop Admin preview bridge delegates to the pinned child runtime", async () => {
  const bundled = await runShopConfigPreview({
    rootDir,
    contract,
    activeRevision: "parent-shop-preview",
    shopType: "normal",
    stage: 12,
    worldKey: "parent-preview-world",
    luck: 20,
    progression: 3,
  });

  assert.equal(bundled.kind, "space-typing-shop-runtime-preview");
  assert.equal(bundled.runtime.source, "published");
  assert.equal(bundled.runtime.activeRevision, "parent-shop-preview");
  assert.equal(bundled.runtime.applyBoundary, "new-session+new-shop-instance");
  assert.equal(bundled.request.shopType, "normal");
  assert.equal(bundled.request.stage, 12);
  assert.equal(bundled.policy.configRevision, bundled.runtime.configRevision);
  assert.ok(Array.isArray(bundled.instance.stock));

  const draft = structuredClone(bundled.policy);
  draft.configRevision = "parent-shop-draft";
  draft.generation.shopTypes.normal.itemCount = 1;
  draft.generation.shopTypes.normal.equipmentCount = 0;

  const preview = await runShopConfigPreview({
    rootDir,
    contract,
    policy: draft,
    activeRevision: "parent-shop-draft-revision",
    shopType: "normal",
    stage: 12,
    worldKey: "parent-preview-world",
  });

  assert.equal(preview.runtime.configRevision, "parent-shop-draft");
  assert.deepEqual(preview.policy, draft);
  assert.equal(preview.instance.stock.length, 1);
});
