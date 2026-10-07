import test from "node:test";
import assert from "node:assert/strict";
import { CURRENCIES_AUDITED_CHILD_SHA, CURRENCY_FIELDS, createCurrencyCapabilityManifest } from "./currency-capability.mjs";

test("Currencies capability is pinned to the tested child and remains read-only", () => {
  const manifest = createCurrencyCapabilityManifest();
  assert.equal(manifest.auditedChildSha, CURRENCIES_AUDITED_CHILD_SHA);
  assert.equal(manifest.auditedChildSha, "57b56b4f239be74b698081638280305976639f5a");
  assert.equal(manifest.mode, "runtime-backed-readonly");
  assert.equal(manifest.authoring.enabled, false);
  assert.equal(manifest.capabilities.balanceAuthoring, false);
  assert.equal(manifest.capabilities.definitionAuthoring, false);
});

test("Currencies exposes canonical runtime IDs separately from save balance keys", () => {
  const manifest = createCurrencyCapabilityManifest();
  assert.deepEqual(manifest.runtime.currencyIds, ["credits", "alloy", "star-crystal", "quantum-core"]);
  assert.deepEqual(manifest.currencies.map((entry) => entry.id), ["credits", "alloy", "star-crystal", "quantum-core"]);
  assert.deepEqual(manifest.runtime.balanceKeys, {
    credits: "credits",
    alloy: "alloy",
    "star-crystal": "starCrystal",
    "quantum-core": "quantumCore",
  });
  for (const entry of manifest.currencies) {
    assert.equal(entry.cap, 999_999_999);
    assert.equal(entry.displayPrecision, 0);
  }
});

test("Currencies keeps unsupported metadata and analytics explicit", () => {
  const manifest = createCurrencyCapabilityManifest();
  assert.deepEqual(CURRENCY_FIELDS, ["ID", "Name", "Icon", "Cap", "Display Precision", "Color", "Enabled"]);
  const byName = new Map(manifest.fields.map((field) => [field.name, field]));
  for (const name of ["ID", "Name", "Cap", "Display Precision"]) assert.equal(byName.get(name)?.runtimeBacked, true);
  for (const name of ["Icon", "Color", "Enabled"]) assert.equal(byName.get(name)?.runtimeBacked, false);
  assert.equal(manifest.analytics.available, false);
  assert.equal(manifest.capabilities.transactionLedger, false);
  assert.deepEqual(manifest.runtime.sourceFunctions, ["stageClearCreditReward", "stageClearExpansionCurrencyReward"]);
  assert.deepEqual(manifest.runtime.sinkFunctions, ["buyShopStockEntry"]);
});
