import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");
const contract = JSON.parse(await read("portal/src/admin/contracts/space-typing-admin.v1.json"));
const [creditsSource, currenciesSource, shopSource, manifestSource, uiSource, routerSource] = await Promise.all([
  read("games/space-typing/src/economy/credits.ts"),
  read("games/space-typing/src/economy/currencies.ts"),
  read("games/space-typing/src/shops/state.ts"),
  read("admin/currency-capability.mjs"),
  read("portal/src/admin/space-typing-currencies-phase-b.ts"),
  read("portal/src/admin/space-typing-phase-b.ts"),
]);

const canonicalIds = ["credits", "alloy", "star-crystal", "quantum-core"];
const balanceKeys = {
  credits: "credits",
  alloy: "alloy",
  "star-crystal": "starCrystal",
  "quantum-core": "quantumCore",
};
const auditedChildSha = "c975de0818f90db5632d6caa731bc038fb199e5c";

assert(contract.capabilities.includes("currencies.read"), "Currencies contract must expose currencies.read");
assert(!contract.capabilities.includes("currencies.write"), "Currencies contract must not expose currencies.write");
assert(contract.routes.some((route) => route.id === "currencies" && route.path === "/admin/space-typing/currencies"), "Currencies route missing from child contract");
assert.deepEqual(contract.currencies.ids, canonicalIds);
assert.deepEqual(contract.shop.currencies, canonicalIds);
assert.deepEqual(contract.currencies.balanceKeys, balanceKeys);
assert.deepEqual(contract.shop.priceStateKeys, ["credits", "alloy", "starCrystal", "quantumCore"]);
assert.equal(contract.currencies.writeCapability, false);
assert.equal(contract.currencies.analytics.available, false);
assert.equal(contract.currencies.displayPrecision, 0);
for (const id of contract.currencies.ids) assert.equal(contract.currencies.caps[id], 999999999, `Unexpected cap for ${id}`);

assert(creditsSource.includes("MAX_CREDITS = 999_999_999"), "Credits cap owner missing");
for (const symbol of ["stageClearCreditReward", "spendCredits"]) assert(creditsSource.includes(symbol), `Missing Credits runtime symbol ${symbol}`);
for (const symbol of ["EXPANSION_CURRENCY_IDS", '"star-crystal"', '"quantum-core"', "starCrystal", "quantumCore", "stageClearExpansionCurrencyReward", "999_999_999"]) assert(currenciesSource.includes(symbol), `Missing expansion currency runtime evidence ${symbol}`);
assert(shopSource.includes("buyShopStockEntry"), "Shop currency sink owner missing");

assert(manifestSource.includes(auditedChildSha), "Parent currency manifest must pin the tested child SHA");
for (const id of canonicalIds) assert(manifestSource.includes(`\"${id}\"`), `Parent manifest missing canonical ID ${id}`);
for (const key of ["starCrystal", "quantumCore"]) assert(manifestSource.includes(`\"${key}\"`), `Parent manifest missing save balance key ${key}`);
assert(manifestSource.includes("stageClearExpansionCurrencyReward"), "Parent manifest must expose the canonical expansion reward source");

assert(uiSource.includes("/api/admin/space-typing/currencies/capabilities"), "Currencies UI must use the authenticated capability endpoint");
assert(uiSource.includes("RUNTIME-BACKED · READ ONLY"), "Currencies UI must make its boundary explicit");
assert(uiSource.includes("Economy Analytics"), "Currencies UI must explain analytics availability");
assert(!uiSource.includes("Save Draft"), "Currencies must remain read-only");
assert(routerSource.includes("renderPhaseBCurrencies"), "Currencies renderer is not wired");
assert(routerSource.includes("`${BASE}/currencies`"), "Currencies route is not wired");

console.log("Space Typing Currencies Admin validation passed: canonical IDs + balance-key mapping, runtime-backed, read-only, no synthetic analytics.");
