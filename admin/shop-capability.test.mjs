import test from "node:test";
import assert from "node:assert/strict";
import {
  createShopCapabilityManifest,
  SHOP_AUDITED_CHILD_SHA,
  SHOP_FIELDS,
  SHOP_TABS,
} from "./shop-capability.mjs";

const contract = {
  configNamespace: "economy.shop",
  runtime: {
    endpoint: "/api/runtime/space-typing/shop",
    applyBoundary: "new-session+new-shop-instance",
    fallback: "bundled-policy",
  },
  previewProtocol: {
    version: 1,
    available: true,
    plannedCommand: "pnpm shop:admin-preview",
    mutation: false,
  },
  ids: {
    shopTypes: ["normal", "station", "traveling", "black-market", "hidden", "event", "service"],
  },
  currencies: ["credits", "alloy", "starCrystal", "quantumCore"],
  authorableSections: ["generation", "pricing", "availability", "offers", "services"],
  deferredCapabilities: ["schedule-window", "daily-purchase-limit", "weekly-purchase-limit", "bundle-transaction"],
};

test("Shop capability manifest opens only canonical runtime-backed authoring seams", () => {
  const manifest = createShopCapabilityManifest(contract);
  assert.equal(manifest.protocolVersion, 4);
  assert.equal(manifest.mode, "runtime-backed-authoring");
  assert.equal(manifest.auditedChildSha, SHOP_AUDITED_CHILD_SHA);
  assert.equal(manifest.auditedChildSha, "a4ffb5b60a3b93830fbd5e1510865e00f431203a");
  assert.deepEqual(manifest.tabs, SHOP_TABS);
  assert.deepEqual(manifest.fields.map((field) => field.name), SHOP_FIELDS);

  const authorable = manifest.fields.filter((field) => field.authorable).map((field) => field.name);
  assert.deepEqual(authorable, ["Price", "Original Price", "Stock", "Availability", "Requirement", "Badge / Label", "Enabled"]);
  assert.equal(manifest.fields.find((field) => field.name === "Discount")?.authorable, false);
  assert.equal(manifest.fields.find((field) => field.name === "Daily Limit")?.source, "unsupported");
  assert.equal(manifest.fields.find((field) => field.name === "Item")?.source, "registry-owned");

  assert.deepEqual(manifest.authoring.sections, contract.authorableSections);
  assert.equal(manifest.authoring.enabled, true);
  assert.equal(manifest.authoring.applyBoundary, "new-session+new-shop-instance");
  assert.equal(manifest.authoring.persistence, "admin-revision-store");
  assert.equal(manifest.preview.available, true);
  assert.equal(manifest.preview.command, "pnpm shop:admin-preview");
  assert.equal(manifest.preview.mutation, false);
});

test("Shop capability manifest keeps deferred runtime concepts closed", () => {
  const manifest = createShopCapabilityManifest(contract);
  assert.equal(manifest.capabilities.catalogWrite, true);
  assert.equal(manifest.capabilities.offerWrite, true);
  assert.equal(manifest.capabilities.servicePricingWrite, true);
  assert.equal(manifest.capabilities.preview, true);
  assert.equal(manifest.capabilities.schedules, false);
  assert.equal(manifest.capabilities.bundles, false);
  assert.equal(manifest.capabilities.transactionHistory, false);
  assert.deepEqual(manifest.deferredCapabilities, contract.deferredCapabilities);
});

test("Shop authoring fails closed when the child preview contract is unavailable", () => {
  const manifest = createShopCapabilityManifest({
    ...contract,
    previewProtocol: { ...contract.previewProtocol, available: false },
  });
  assert.equal(manifest.mode, "runtime-backed-readonly");
  assert.equal(manifest.authoring.enabled, false);
  assert.equal(manifest.preview.available, false);
  assert.ok(manifest.fields.every((field) => field.authorable === false));
});
