import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");
const contract = JSON.parse(await read("portal/src/admin/contracts/space-typing-admin.v1.json"));
const [warpSource, accountState, transactions, playerSave, auditSource, childCi, uiSource, routerSource, phaseMapSource] = await Promise.all([
  read("games/space-typing/src/economy/warp-charge.ts"),
  read("games/space-typing/src/persistence/account-state.ts"),
  read("games/space-typing/src/persistence/account-transactions.ts"),
  read("games/space-typing/src/persistence/player-save.ts"),
  read("games/space-typing/scripts/audit-warp-economy.ts"),
  read("games/space-typing/.github/workflows/ci.yml"),
  read("portal/src/admin/space-typing-warp-phase-b.ts"),
  read("portal/src/admin/space-typing-phase-b.ts"),
  read("admin/space-typing-phase-b-map.v1.json"),
]);

const warp = contract.warp;
assert(contract.capabilities.includes("warp.read"), "Warp contract must expose warp.read");
assert(!contract.capabilities.includes("warp.write"), "Warp Admin authoring must stay closed");
assert(!contract.capabilities.includes("warp.preview"), "Warp Admin preview must stay closed");
assert(contract.routes.some((route) => route.id === "stamina-warp" && route.path === "/admin/space-typing/warp"), "Stamina / Warp route missing from child contract");
assert.equal(warp.mode, "runtime-derived-readonly");
assert.equal(warp.policyVersion, "warp-v3-1");
assert.deepEqual(warp.authorableFields, []);
assert.equal(warp.writeCapability, false);
assert.equal(warp.previewCapability, false);
assert.equal(warp.playerMutationCapability, "gameplay-only");
assert.equal(warp.persistenceOwner, "PlayerSave.account.warp");
assert.equal(warp.accountStateOwner, "AccountState.warp");
assert.equal(warp.sortieCostInvariant, "activeCost + reserveCost === 10");
assert.equal(warp.auditCommand, "pnpm stamina:audit");
assert.deepEqual(warp.policy, {
  activeCap: 100,
  reserveCap: 300,
  sortieCost: 10,
  activeRegenMs: 360000,
  reserveRegenMs: 720000,
  refuelAmount: 20,
  refuelPrices: [8, 12, 18],
  refuelCurrency: "star-crystal",
  dailyRefillLimit: 3,
  dailyReset: "04:00 Vietnam",
});
assert.deepEqual(warp.codeOwnedPolicyFields, ["activeCap", "reserveCap", "cost", "activeMs", "reserveMs", "fuel", "prices"]);

for (const symbol of ["WARP_POLICY", "activeCap: 100", "reserveCap: 300", "cost: 10", "activeMs: 360_000", "reserveMs: 720_000", "fuel: 20", "prices: [8, 12, 18]", "createWarpCharge", "reconcileWarp", "spendWarp", "refuelQuote", "refuelWarp", "warpEtaMs"]) {
  assert(warpSource.includes(symbol), `Missing Warp policy/runtime evidence ${symbol}`);
}
for (const symbol of ["warp: WarpCharge", "policy: WARP_POLICY.version", "s.activeCost + s.reserveCost === 10"]) {
  assert(accountState.includes(symbol), `Missing account-state Warp evidence ${symbol}`);
}
for (const symbol of ["spendWarp", "refuelQuote", "refuelWarp", "starCrystal", "reserveConsent", "a.warp", "activeCost", "reserveCost"]) {
  assert(transactions.includes(symbol), `Missing canonical Warp transaction evidence ${symbol}`);
}
assert(playerSave.includes("account"), "PlayerSave must retain canonical account state");
for (const symbol of ["WARP_POLICY", "auditCampaign", "auditReplay", "auditPacing", "8/12/18", "daily-limited acceleration prices"]) {
  assert(auditSource.includes(symbol), `Warp audit missing evidence ${symbol}`);
}
assert(childCi.includes("Audit Warp economy"), "Child CI must run the Warp economy audit");
assert(childCi.includes("pnpm stamina:audit"), "Child CI must execute pnpm stamina:audit");

assert(uiSource.includes("/api/admin/space-typing/contract"), "Warp UI must read the authenticated canonical child contract");
assert(uiSource.includes("RUNTIME-BACKED · READ ONLY"), "Warp UI must make its read-only boundary explicit");
assert(uiSource.includes("Capacity & Regeneration"), "Warp UI must expose capacity and regeneration policy");
assert(uiSource.includes("Sortie Admission"), "Warp UI must expose sortie cost ownership");
assert(uiSource.includes("Refuel Policy"), "Warp UI must expose refuel policy as reference data");
assert(uiSource.includes("Code-owned policy fields"), "Warp UI must expose code-owned policy ownership");
assert(uiSource.includes("gameplay-only"), "Warp UI must explain gameplay-only player mutation");
assert(!uiSource.includes("api.createRevision"), "Warp UI must not create config revisions");
assert(!uiSource.includes("api.publish"), "Warp UI must not publish config revisions");
assert(!uiSource.includes("Save Draft"), "Warp UI must not fabricate authoring");
assert(!uiSource.includes("fetch(\"/api/admin/space-typing/warp"), "Warp UI must not invent a player mutation endpoint");
assert(routerSource.includes("renderPhaseBWarp"), "Warp renderer is not wired");
assert(routerSource.includes("`${BASE}/warp`"), "Warp route is not wired");

const phaseMap = JSON.parse(phaseMapSource);
const warpMap = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/warp");
assert.equal(warpMap?.persistence, "child-runtime-policy");
assert.equal(warpMap?.applyBoundary, "none");
assert.equal(warpMap?.status, "phase-b-ui-wired-runtime-backed-readonly");

console.log("Space Typing Stamina / Warp Admin validation passed: canonical WARP_POLICY, gameplay-only mutations, CI audit, read-only Admin boundary.");
