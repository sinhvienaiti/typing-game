import test from "node:test";
import assert from "node:assert/strict";
import { createShopCapabilityManifest, SHOP_AUDITED_CHILD_SHA, SHOP_FIELDS, SHOP_TABS } from "./shop-capability.mjs";

const RUNTIME_FIELDS = ["ID", "Item", "Category", "Price", "Currency", "Purchase Limit", "Availability", "Requirement", "Enabled"];
const UNSUPPORTED_FIELDS = ["Original Price", "Discount", "Daily Limit", "Weekly Limit", "Featured", "Sort Order"];

test("Shop capability manifest mirrors the master-plan surface and real runtime ownership", () => {
  const manifest = createShopCapabilityManifest();
  assert.equal(manifest.protocolVersion, 3);
  assert.equal(manifest.mode, "runtime-backed-readonly");
  assert.equal(manifest.auditedChildSha, SHOP_AUDITED_CHILD_SHA);
  assert.equal(manifest.auditedChildSha, "ac8014537a0b56e964175e7b31f92c97fa0f5afa");
  assert.deepEqual(manifest.tabs, ["Catalog", "Featured", "Daily", "Weekly", "Bundles", "History"]);
  assert.equal(SHOP_TABS.length, 6);
  assert.equal(SHOP_FIELDS.length, 15);
  assert.deepEqual(SHOP_FIELDS, [
    "ID", "Item", "Category", "Price", "Currency", "Original Price", "Discount", "Purchase Limit",
    "Daily Limit", "Weekly Limit", "Availability", "Requirement", "Featured", "Sort Order", "Enabled",
  ]);
  assert.deepEqual(manifest.fields.filter((field) => field.runtimeBacked).map((field) => field.name), RUNTIME_FIELDS);
  assert.deepEqual(manifest.fields.filter((field) => !field.runtimeBacked).map((field) => field.name), UNSUPPORTED_FIELDS);
  assert.ok(manifest.fields.every((field) => field.authorable === false));
  assert.equal(manifest.authoring.enabled, false);
  assert.equal(manifest.authoring.applyBoundary, "none");
  assert.equal(manifest.authoring.persistence, "child-runtime-state");
});

test("Shop capabilities keep canonical currency IDs separate from runtime price state keys", () => {
  const manifest = createShopCapabilityManifest();
  assert.deepEqual(manifest.capabilities, {
    runtimeCatalogGeneration: true,
    purchaseTransaction: true,
    pricing: true,
    currencies: true,
    stockRemaining: true,
    availability: true,
    serviceShop: true,
    catalogWrite: false,
    schedules: false,
    bundles: false,
    transactionHistory: false,
    preview: false,
  });
  assert.deepEqual(manifest.runtime.currencyIds, ["credits", "alloy", "star-crystal", "quantum-core"]);
  assert.deepEqual(manifest.runtime.priceStateKeys, ["credits", "alloy", "starCrystal", "quantumCore"]);
  assert.deepEqual(manifest.runtime.shopTypes, ["normal", "station", "traveling", "black-market", "hidden", "event", "service"]);
  assert.deepEqual(manifest.runtime.stockKinds, ["item", "equipment"]);
  assert.equal(manifest.runtime.refreshBoundary, "sector-instance");
  assert.equal(manifest.runtime.persistenceOwner, "PlayerSave.shopState");
  assert.ok(manifest.evidence.filter((entry) => entry.id !== "authoring-seam").every((entry) => entry.found === true));
  assert.equal(manifest.evidence.find((entry) => entry.id === "authoring-seam")?.found, false);
});
