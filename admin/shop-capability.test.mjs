import test from "node:test";
import assert from "node:assert/strict";
import { createShopCapabilityManifest, SHOP_AUDITED_CHILD_SHA, SHOP_FIELDS, SHOP_TABS } from "./shop-capability.mjs";

test("Shop capability manifest mirrors the master-plan surface without inventing runtime authoring", () => {
  const manifest = createShopCapabilityManifest();
  assert.equal(manifest.protocolVersion, 1);
  assert.equal(manifest.mode, "runtime-audited-readonly");
  assert.equal(manifest.auditedChildSha, SHOP_AUDITED_CHILD_SHA);
  assert.deepEqual(manifest.tabs, ["Catalog", "Featured", "Daily", "Weekly", "Bundles", "History"]);
  assert.equal(SHOP_TABS.length, 6);
  assert.equal(SHOP_FIELDS.length, 15);
  assert.deepEqual(SHOP_FIELDS, [
    "ID", "Item", "Category", "Price", "Currency", "Original Price", "Discount", "Purchase Limit",
    "Daily Limit", "Weekly Limit", "Availability", "Requirement", "Featured", "Sort Order", "Enabled",
  ]);
  assert.equal(manifest.authoring.enabled, false);
  assert.equal(manifest.authoring.applyBoundary, "none");
  assert.equal(manifest.authoring.persistence, "runtime-audit-manifest");
  assert.ok(manifest.fields.every((field) => field.authorable === false));
  assert.deepEqual(manifest.capabilities, {
    catalogRead: false,
    catalogWrite: false,
    purchaseTransaction: false,
    pricing: false,
    currencies: false,
    limits: false,
    schedules: false,
    bundles: false,
    transactionHistory: false,
    preview: false,
  });
});

test("Shop runtime-adjacent domains are explicitly not claimed as purchasable", () => {
  const manifest = createShopCapabilityManifest();
  assert.deepEqual(manifest.linkedRuntimeDomains.map((entry) => entry.id), ["ships", "equipment", "skills"]);
  assert.ok(manifest.linkedRuntimeDomains.every((entry) => entry.relationship.includes("not proven purchasable")));
  assert.ok(manifest.evidence.every((entry) => entry.found === false));
});
