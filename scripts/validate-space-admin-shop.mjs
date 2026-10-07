import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { createShopCapabilityManifest, SHOP_AUDITED_CHILD_SHA, SHOP_FIELDS, SHOP_TABS } from "../admin/shop-capability.mjs";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const child = resolve(root, "games/space-typing");
const manifest = createShopCapabilityManifest();
const childHead = execFileSync("git", ["-C", child, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();
assert.equal(childHead, SHOP_AUDITED_CHILD_SHA, `Shop audit is stale: manifest=${SHOP_AUDITED_CHILD_SHA} pinned-child=${childHead}. Re-audit Shop before changing the SHA.`);

const [contractText, shopState, serviceShop, credits, currencies, server, router, phaseMap, ui] = await Promise.all([
  readFile(resolve(child, "contracts/space-typing-admin.v1.json"), "utf8"),
  readFile(resolve(child, "src/shops/state.ts"), "utf8"),
  readFile(resolve(child, "src/shops/service-shop.ts"), "utf8"),
  readFile(resolve(child, "src/economy/credits.ts"), "utf8"),
  readFile(resolve(child, "src/economy/currencies.ts"), "utf8"),
  readFile(resolve(root, "admin/server.mjs"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8"),
  readFile(resolve(root, "admin/space-typing-phase-b-map.v1.json"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-shop-phase-b.ts"), "utf8"),
]);
const contract = JSON.parse(contractText);
assert.ok(contract.capabilities.includes("shop.read"), "child admin contract must expose shop.read");
assert.ok(!contract.capabilities.includes("shop.write"), "Shop authoring must stay closed until a child config consumer exists");
assert.equal(contract.shop?.mode, "runtime-derived-readonly");
assert.deepEqual(contract.shop?.authorableFields, []);
assert.equal(contract.shop?.writeCapability, false);
assert.deepEqual(contract.shop?.currencies, ["credits", "alloy", "star-crystal", "quantum-core"]);
assert.deepEqual(contract.shop?.priceStateKeys, ["credits", "alloy", "starCrystal", "quantumCore"]);
assert.deepEqual(contract.shop?.runtimeSources, ["src/shops/state.ts", "src/shops/service-shop.ts", "src/economy/credits.ts", "src/economy/currencies.ts"]);

assert.match(shopState, /export function resolveShopInstance/);
assert.match(shopState, /export function shopAvailable/);
assert.match(shopState, /export function buyShopStockEntry/);
assert.match(shopState, /export type ShopPrice/);
assert.match(shopState, /starCrystal\?: number/);
assert.match(shopState, /quantumCore\?: number/);
assert.match(shopState, /remaining: number/);
assert.match(serviceShop, /export type ServiceShopState/);
assert.match(serviceShop, /spendCredits/);
assert.match(credits, /export function spendCredits/);
assert.match(currencies, /export const EXPANSION_CURRENCY_IDS/);
assert.match(currencies, /"star-crystal"/);
assert.match(currencies, /"quantum-core"/);

assert.equal(manifest.mode, "runtime-backed-readonly");
assert.equal(manifest.authoring.enabled, false);
assert.equal(manifest.authoring.applyBoundary, "none");
assert.deepEqual(manifest.runtime.currencyIds, ["credits", "alloy", "star-crystal", "quantum-core"]);
assert.deepEqual(manifest.runtime.priceStateKeys, ["credits", "alloy", "starCrystal", "quantumCore"]);
assert.equal(SHOP_TABS.length, 6);
assert.equal(SHOP_FIELDS.length, 15);
assert.equal(manifest.fields.filter((field) => field.runtimeBacked).length, 9);
assert.equal(manifest.fields.filter((field) => !field.runtimeBacked).length, 6);
assert.ok(manifest.fields.every((field) => field.authorable === false));
assert.equal(manifest.capabilities.purchaseTransaction, true);
assert.equal(manifest.capabilities.pricing, true);
assert.equal(manifest.capabilities.currencies, true);
assert.equal(manifest.capabilities.catalogWrite, false);
assert.equal(manifest.capabilities.preview, false);

assert.match(server, /GET"&&url\.pathname==="\/api\/admin\/space-typing\/shop\/capabilities"/);
assert.doesNotMatch(server, /POST"&&url\.pathname==="\/api\/admin\/space-typing\/shop/);
assert.match(router, /renderPhaseBShop/);
assert.match(router, /\/shop`\) return renderPhaseBShop/);
assert.match(ui, /RUNTIME-BACKED · READ ONLY/);
assert.match(ui, /const runtimeCount = manifest\.fields\.filter\(\(field\) => field\.runtimeBacked\)\.length/);
assert.match(ui, /const unsupportedCount = manifest\.fields\.length - runtimeCount/);
assert.match(ui, /\$\{runtimeCount\} runtime-derived fields/);
assert.match(ui, /\$\{unsupportedCount\} unsupported fields/);
assert.match(ui, /Shop Preview/);
const map = JSON.parse(phaseMap);
const shop = map.screens.find((screen) => screen.route === "/admin/space-typing/shop");
assert.ok(shop, "Shop Phase B map row is required");
assert.equal(shop.status, "phase-b-ui-wired-runtime-backed-readonly");
assert.equal(shop.persistence, "child-runtime-state");
assert.equal(shop.applyBoundary, "none");
console.log(`Shop runtime contract valid for ${childHead}: ${SHOP_TABS.length} tabs, 9 runtime-derived fields, 6 unsupported fields, writes intentionally closed.`);
