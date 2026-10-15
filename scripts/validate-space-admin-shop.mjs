import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { createShopCapabilityManifest, SHOP_AUDITED_CHILD_SHA, SHOP_FIELDS, SHOP_TABS } from "../admin/shop-capability.mjs";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const child = resolve(root, "games/space-typing");
const childHead = execFileSync("git", ["-C", child, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();
assert.equal(childHead, SHOP_AUDITED_CHILD_SHA, `Shop audit is stale: manifest=${SHOP_AUDITED_CHILD_SHA} pinned-child=${childHead}. Re-audit Shop before changing the SHA.`);

const [generalContract, shopContract, shopPolicy, shopRuntimePolicy, shopPreview, shopState, serviceShop, credits, currencies, server, router, phaseMap, ui] = await Promise.all([
  readFile(resolve(child, "contracts/space-typing-admin.v1.json"), "utf8").then(JSON.parse),
  readFile(resolve(child, "contracts/space-typing-admin-shop.v1.json"), "utf8").then(JSON.parse),
  readFile(resolve(child, "src/shops/policy.ts"), "utf8"),
  readFile(resolve(child, "src/admin/shop-runtime-policy.ts"), "utf8"),
  readFile(resolve(child, "src/admin/shop-runtime-preview.ts"), "utf8"),
  readFile(resolve(child, "src/shops/state.ts"), "utf8"),
  readFile(resolve(child, "src/shops/service-shop.ts"), "utf8"),
  readFile(resolve(child, "src/economy/credits.ts"), "utf8"),
  readFile(resolve(child, "src/economy/currencies.ts"), "utf8"),
  readFile(resolve(root, "admin/server.mjs"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8"),
  readFile(resolve(root, "admin/space-typing-phase-b-map.v1.json"), "utf8").then(JSON.parse),
  readFile(resolve(root, "portal/src/admin/space-typing-shop-phase-b.ts"), "utf8"),
]);

assert.ok(generalContract.capabilities.includes("shop.read"), "legacy umbrella contract must keep Shop discovery/read capability");
assert.equal(shopContract.schemaVersion, 1);
assert.equal(shopContract.configNamespace, "economy.shop");
assert.deepEqual(shopContract.runtime, {
  endpoint: "/api/runtime/space-typing/shop",
  applyBoundary: "new-session+new-shop-instance",
  fallback: "bundled-policy",
});
assert.deepEqual(shopContract.previewProtocol, {
  version: 1,
  available: true,
  plannedCommand: "pnpm shop:admin-preview",
  mutation: false,
});
assert.deepEqual(shopContract.authorableSections, ["generation", "pricing", "availability", "offers", "services"]);
for (const deferred of ["schedule-window", "daily-purchase-limit", "weekly-purchase-limit", "bundle-transaction"]) {
  assert.ok(shopContract.deferredCapabilities.includes(deferred), `deferred Shop capability must remain explicit: ${deferred}`);
}
assert.deepEqual(shopContract.currencies, ["credits", "alloy", "starCrystal", "quantumCore"]);
assert.deepEqual(shopContract.ids.shopTypes, ["normal", "station", "traveling", "black-market", "hidden", "event", "service"]);
assert.equal(shopContract.catalog.items.length, shopContract.ids.itemIds.length, "Shop item catalog must cover every canonical item ID");
assert.equal(shopContract.catalog.equipment.length, shopContract.ids.equipmentIds.length, "Shop equipment catalog must cover every canonical equipment ID");
assert.equal(shopContract.catalog.grades.length, shopContract.ids.gradeIds.length, "Shop grade catalog must cover every canonical grade ID");
assert.deepEqual(shopContract.catalog.items.map((entry) => entry.id), shopContract.ids.itemIds);
assert.deepEqual(shopContract.catalog.equipment.map((entry) => entry.id), shopContract.ids.equipmentIds);
assert.deepEqual(shopContract.catalog.grades.map((entry) => entry.id), shopContract.ids.gradeIds);
assert.deepEqual(shopContract.catalog.sourceOfTruth, {
  items: "src/items/registry.ts#ITEM_REGISTRY",
  equipment: "src/equipment/registry.ts#EQUIPMENT_REGISTRY",
  grades: "src/grades.ts#GRADE_PRESENTATION",
});

assert.match(shopPolicy, /export type ShopAdminPolicyV1/);
assert.match(shopPolicy, /export const BUNDLED_SHOP_POLICY/);
assert.match(shopPolicy, /compareAtPriceByShopType/);
assert.match(shopPolicy, /compareAtPriceByShopTypeAndGrade/);
assert.match(shopRuntimePolicy, /export function materializeShopRuntimeSession/);
assert.match(shopPreview, /export function previewShopRuntime/);
assert.match(shopPreview, /materializeShopRuntimeSession/);
assert.match(shopPreview, /resolveShopInstance/);
assert.match(shopPreview, /shopAvailable/);
assert.match(shopPreview, /policy:\s*session\.policy/);
assert.match(shopState, /export function resolveShopInstance/);
assert.match(shopState, /export function shopAvailable/);
assert.match(shopState, /export function buyShopStockEntry/);
assert.match(shopState, /remaining: number/);
assert.match(shopState, /compareAtPrice\?: ShopBasePrice \| null/);
assert.match(shopState, /badge\?: string \| null/);
assert.match(serviceShop, /export type ServiceShopState/);
assert.match(serviceShop, /spendCredits/);
assert.match(credits, /export function spendCredits/);
assert.match(currencies, /export const EXPANSION_CURRENCY_IDS/);

const manifest = createShopCapabilityManifest(shopContract);
assert.equal(manifest.protocolVersion, 4);
assert.equal(manifest.mode, "runtime-backed-authoring");
assert.equal(manifest.auditedChildSha, childHead);
assert.deepEqual(manifest.tabs, SHOP_TABS);
assert.deepEqual(manifest.fields.map((field) => field.name), SHOP_FIELDS);
assert.equal(manifest.authoring.enabled, true);
assert.equal(manifest.authoring.configNamespace, "economy.shop");
assert.deepEqual(manifest.authoring.sections, shopContract.authorableSections);
assert.equal(manifest.authoring.applyBoundary, "new-session+new-shop-instance");
assert.equal(manifest.authoring.persistence, "admin-revision-store");
assert.equal(manifest.preview.available, true);
assert.equal(manifest.preview.protocolVersion, 1);
assert.equal(manifest.preview.command, "pnpm shop:admin-preview");
assert.equal(manifest.preview.mutation, false);
assert.equal(manifest.capabilities.catalogWrite, true);
assert.equal(manifest.capabilities.offerWrite, true);
assert.equal(manifest.capabilities.servicePricingWrite, true);
assert.equal(manifest.capabilities.preview, true);
assert.equal(manifest.capabilities.schedules, false);
assert.equal(manifest.capabilities.bundles, false);
assert.equal(manifest.capabilities.transactionHistory, false);
assert.deepEqual(
  manifest.fields.filter((field) => field.authorable).map((field) => field.name),
  ["Price", "Original Price", "Stock", "Availability", "Requirement", "Badge / Label", "Enabled"],
);
assert.equal(manifest.fields.find((field) => field.name === "Discount")?.source, "runtime-derived");
assert.equal(manifest.fields.find((field) => field.name === "Discount")?.authorable, false);
for (const name of ["Daily Limit", "Weekly Limit", "Featured", "Sort Order"]) {
  assert.equal(manifest.fields.find((field) => field.name === name)?.source, "unsupported");
  assert.equal(manifest.fields.find((field) => field.name === name)?.authorable, false);
}

assert.match(server, /createShopCapabilityManifest\(shopContract\)/);
assert.match(server, /runShopConfigPreview/);
assert.match(server, /request\.method==="POST"&&url\.pathname==="\/api\/admin\/space-typing\/shop\/preview"/);
assert.match(server, /policy:\s*input\.policy\s*\?\?\s*active\.economy\?\.shop/);
assert.doesNotMatch(server, /\/api\/admin\/space-typing\/shop\/(?:save|publish|write)/, "Shop must use generic immutable revisions rather than a direct write endpoint");

assert.match(router, /renderPhaseBShop/);
assert.match(router, /\$\{BASE\}\/shop`\) return decorated\(path, renderPhaseBShop\(navigate\)\)/);
assert.match(router, /attachProductionPreviewClassification\(screen, path\)/);
assert.match(router, /attachRoleAwareActionGates\(screen\)/);
assert.match(ui, /protocolVersion:\s*4/);
assert.match(ui, /\/api\/admin\/space-typing\/shop\/capabilities/);
assert.match(ui, /\/api\/admin\/space-typing\/shop\/contract/);
assert.match(ui, /\/api\/admin\/space-typing\/shop\/preview/);
assert.match(ui, /config\.economy\.shop\s*=\s*nextPolicy/);
assert.match(ui, /api\.createRevision/);
assert.match(ui, /api\.validateRevision/);
assert.match(ui, /api\.publish/);
assert.match(ui, /Product Catalog/);
assert.match(ui, /Equipment Grade Chances/);
assert.match(ui, /catalog\.items/);
assert.match(ui, /catalog\.equipment/);
assert.match(ui, /catalog\.grades/);
assert.match(ui, /stock\.price\.badge/);
assert.match(ui, /stock\.price\.compareAtPrice/);
assert.match(ui, /Original \/ compare-at price/);
assert.match(ui, /Badge \/ label/);
assert.match(ui, /existing persisted Shop instances keep their original prices\/stock|Existing persisted Shop instances keep their original prices\/stock/);
assert.doesNotMatch(ui, /RUNTIME-BACKED · READ ONLY/);

const map = phaseMap.screens.find((screen) => screen.route === "/admin/space-typing/shop");
assert.ok(map, "Shop Phase B map row is required");
assert.equal(map.status, "phase-b-ui-wired-runtime-backed-authoring");
assert.equal(map.persistence, "immutable-revision-store");
assert.equal(map.applyBoundary, "new-session+new-shop-instance");

console.log(`Shop Admin A4.1 contract valid for ${childHead}: registry-backed catalog + grade weights + production merchandising preview + immutable revision authoring enabled; deferred capabilities remain closed.`);
