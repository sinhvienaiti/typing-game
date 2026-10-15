import test from "node:test";
import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import {
  createShopCapabilityManifest,
  SHOP_AUDITED_CHILD_SHA,
  SHOP_FIELDS,
  SHOP_TABS,
} from "./shop-capability.mjs";
import { createCurrencyCapabilityManifest } from "./currency-capability.mjs";
import {
  A10_UNLOCK_ECONOMY_AUDITED_CHILD_SHA,
  createUnlockEconomyCapabilityManifest,
} from "./unlock-economy-capability.mjs";

const AUDITED_CHILD_SHA = "b75cec6cf94208de58341e9d59a1777cddd6c064";

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
  assert.equal(manifest.auditedChildSha, AUDITED_CHILD_SHA);
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

test("A10 unlock/economy truth map mirrors the pinned child and never invents player-state authoring", () => {
  const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
  const child = resolve(root, "games/space-typing");
  const childHead = execFileSync("git", ["-C", child, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();
  assert.equal(childHead, AUDITED_CHILD_SHA);
  assert.equal(childHead, A10_UNLOCK_ECONOMY_AUDITED_CHILD_SHA);
  assert.equal(SHOP_AUDITED_CHILD_SHA, A10_UNLOCK_ECONOMY_AUDITED_CHILD_SHA);

  const childCapabilities = readFileSync(resolve(child, "src/admin/a10-unlock-economy-capabilities.ts"), "utf8");
  for (const id of ["ship.unlock-stage", "shop.policy", "wallet.currency-balances", "player.ownership-entitlements", "loot.equipment-drop-tables", "reward.combat-credit-drop-policy"]) {
    assert.ok(childCapabilities.includes(`id: \"${id}\"`), `Pinned child A10 capability is missing ${id}`);
  }
  assert.ok(childCapabilities.includes('productionConsumer: "src/characters/state.ts::unlockCharactersForStage()"'));
  assert.ok(childCapabilities.includes('applyBoundary: "new-session+new-shop-instance"'));

  const manifest = createUnlockEconomyCapabilityManifest();
  assert.equal(manifest.protocolVersion, 1);
  assert.equal(manifest.milestone, "A10.0");
  assert.equal(manifest.auditedChildSha, childHead);
  assert.deepEqual(manifest.authorableIds, ["ship.unlock-stage", "shop.policy"]);
  assert.ok(manifest.readOnlyIds.includes("wallet.currency-balances"));
  assert.ok(manifest.readOnlyIds.includes("player.ownership-entitlements"));
  assert.ok(manifest.readOnlyIds.includes("loot.equipment-drop-tables"));
  assert.equal(manifest.invariants.walletMutationFromContentAdmin, false);
  assert.equal(manifest.invariants.entitlementMutationFromContentAdmin, false);
  assert.equal(manifest.invariants.fakeRewardOrDropPublishing, false);

  const currencies = createCurrencyCapabilityManifest();
  assert.equal(currencies.capabilities.balanceAuthoring, false);
  assert.equal(currencies.capabilities.definitionAuthoring, false);
  assert.equal(currencies.authoring.enabled, false);
});
