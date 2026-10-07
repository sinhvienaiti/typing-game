import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");
const contract = JSON.parse(await read("portal/src/admin/contracts/space-typing-admin.v1.json"));
const [campaignSource, combatSource, creditsSource, currenciesSource, lootSource, pitySource, gameSource, uiSource, routerSource, phaseMapSource] = await Promise.all([
  read("games/space-typing/src/rewards/campaign-rewards.ts"),
  read("games/space-typing/src/rewards/combat-credit-drops.ts"),
  read("games/space-typing/src/economy/credits.ts"),
  read("games/space-typing/src/economy/currencies.ts"),
  read("games/space-typing/src/loot/equipment-loot.ts"),
  read("games/space-typing/src/loot/pity.ts"),
  read("games/space-typing/src/Game.ts"),
  read("portal/src/admin/space-typing-rewards-phase-b.ts"),
  read("portal/src/admin/space-typing-phase-b.ts"),
  read("admin/space-typing-phase-b-map.v1.json"),
]);

const rewards = contract.rewards;
assert(contract.capabilities.includes("rewards.read"), "Rewards contract must expose rewards.read");
assert(!contract.capabilities.includes("rewards.write"), "Rewards contract must not expose rewards.write");
assert(!contract.capabilities.includes("rewards.preview"), "Rewards contract must not expose rewards.preview");
assert(contract.routes.some((route) => route.id === "rewards" && route.path === "/admin/space-typing/rewards"), "Rewards route missing from child contract");
assert.equal(rewards.mode, "runtime-derived-readonly");
assert.deepEqual(rewards.authorableFields, []);
assert.equal(rewards.writeCapability, false);
assert.equal(rewards.previewCapability, false);
assert.equal(rewards.gameplayConsumer, "src/Game.ts");
assert.deepEqual(rewards.performanceRewardIds, ["precision", "flawless", "streak", "tempo", "objective"]);
assert.deepEqual(rewards.campaignFunctions, ["performanceReward", "sectorCheckpointReward"]);
assert.deepEqual(rewards.combatCredit.modes, ["campaign", "ascension", "hidden", "recall", "expedition", "preview", "test-lab", "duel"]);
assert.deepEqual(rewards.combatCredit.walletPolicies, {
  campaign: "real", ascension: "real", preview: "simulated", "test-lab": "simulated",
  hidden: "disabled", recall: "disabled", expedition: "disabled", duel: "disabled",
});
assert.deepEqual(rewards.combatCredit.causes, ["typed-kill", "voice-kill", "skill-kill", "boss-kill"]);
assert.deepEqual(rewards.combatCredit.tiers, ["common", "refined", "high", "elite", "mini-boss", "boss", "major-boss"]);
assert.deepEqual(rewards.combatCredit.variants, ["standard", "golden"]);
assert.equal(rewards.combatCredit.canonicalWalletCommitRequiredForRealModes, true);
assert.deepEqual(rewards.equipmentLoot.sources, ["normal", "elite", "golden", "treasure", "anomaly", "boss"]);
assert.deepEqual(rewards.equipmentLoot.gradeIds, ["aluminum", "copper", "silver", "gold", "diamond"]);
assert.deepEqual(rewards.equipmentLoot.equipmentTiers, [1, 2, 3]);
assert.deepEqual(rewards.equipmentLoot.weightTables, ["GRADE_DROP_WEIGHTS", "EQUIPMENT_TIER_WEIGHTS"]);
assert.equal(rewards.equipmentLoot.mutationHook, "onEquipmentDrop");
assert.deepEqual(rewards.pity.keys, ["golden", "treasure", "choice", "anomaly"]);
assert.deepEqual(rewards.pity.counterRange, { min: 0, max: 50, integer: true });
assert.equal(rewards.pity.mutationHook, "onLuckPityUpdate");

for (const symbol of ["performanceReward", "sectorCheckpointReward", "precision", "flawless", "streak", "tempo", "objective"]) {
  assert(campaignSource.includes(symbol), `Missing campaign reward runtime evidence ${symbol}`);
}
for (const symbol of ["resolveCreditCrystalTier", "combatCreditWeight", "combatCreditStageBudget", "combatCreditReward", "settleCombatCreditStageBase", "canonicalWalletCommit", "typed-kill", "voice-kill", "skill-kill", "boss-kill"]) {
  assert(combatSource.includes(symbol), `Missing combat-credit runtime evidence ${symbol}`);
}
for (const symbol of ["stageClearCreditReward", "addCredits"]) assert(creditsSource.includes(symbol), `Missing Credits runtime evidence ${symbol}`);
assert(currenciesSource.includes("stageClearExpansionCurrencyReward"), "Expansion currency reward owner missing");
for (const symbol of ["GRADE_DROP_WEIGHTS", "EQUIPMENT_TIER_WEIGHTS", "equipmentDropChance", "rollEquipmentGrade", "rollEquipmentDefinition", "rollEquipmentDrop"]) {
  assert(lootSource.includes(symbol), `Missing equipment-loot runtime evidence ${symbol}`);
}
for (const symbol of ["createLuckPityState", "sanitizeLuckPityState", "luckAdjustedChance", "rollLuckPity"]) {
  assert(pitySource.includes(symbol), `Missing pity runtime evidence ${symbol}`);
}
for (const symbol of ["onEquipmentDrop", "onLuckPityUpdate", "onCombatCreditReward"]) assert(gameSource.includes(symbol), `Missing gameplay mutation evidence ${symbol}`);

assert(uiSource.includes("/api/admin/space-typing/contract"), "Rewards UI must read the authenticated canonical child contract");
assert(uiSource.includes("RUNTIME-BACKED · READ ONLY"), "Rewards UI must make its read-only boundary explicit");
assert(uiSource.includes("Code-owned policy fields"), "Rewards UI must expose code-owned policy ownership");
assert(uiSource.includes("Canonical wallet commit required"), "Rewards UI must expose the real wallet boundary");
assert(!uiSource.includes("Save Draft"), "Rewards UI must not fabricate authoring");
assert(!uiSource.includes("api.createRevision"), "Rewards UI must not create config revisions");
assert(!uiSource.includes("rewards.preview"), "Rewards UI must not fabricate preview capability");
assert(routerSource.includes("renderPhaseBRewards"), "Rewards renderer is not wired");
assert(routerSource.includes("`${BASE}/rewards`"), "Rewards route is not wired");

const phaseMap = JSON.parse(phaseMapSource);
const rewardsMap = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/rewards");
assert.equal(rewardsMap?.persistence, "child-runtime-policy");
assert.equal(rewardsMap?.applyBoundary, "none");
assert.equal(rewardsMap?.status, "phase-b-ui-wired-runtime-backed-readonly");

console.log("Space Typing Rewards & Drops Admin validation passed: canonical runtime evidence, read-only policy boundary, no synthetic authoring or preview.");
