import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");
const contract = JSON.parse(await read("games/space-typing/contracts/space-typing-admin-duel.v1.json"));
const [roomSource, rulesSource, modelSource, botsSource, localMatchSource, timingSource, uiSource, routerSource, shellSource, serverSource, phaseMapSource] = await Promise.all([
  read("games/space-typing/src/duel/room.ts"), read("games/space-typing/src/duel/rules.ts"), read("games/space-typing/src/duel/model.ts"),
  read("games/space-typing/src/duel/bots.ts"), read("games/space-typing/src/duel/local-match.ts"), read("games/space-typing/src/duel/presentation-timing.ts"),
  read("portal/src/admin/space-typing-duel-phase-b.ts"), read("portal/src/admin/space-typing-phase-b.ts"), read("portal/src/admin/space-typing.ts"),
  read("admin/server.mjs"), read("admin/space-typing-phase-b-map.v1.json"),
]);

const duel = contract.duel;
assert.equal(contract.contractRevision, "space-typing-admin-duel-v1");
assert.equal(contract.capability, "duel.read");
assert.equal(duel.mode, "runtime-derived-readonly");
assert.deepEqual(duel.authorableFields, []);
assert.equal(duel.persistenceOwner, "duel-room-session-runtime");
assert.equal(duel.roomOwnerWriteCapability, true);
assert.equal(duel.writeCapability, false);
assert.equal(duel.previewCapability, false);
assert.deepEqual(duel.roomSettings.matchLengthSeconds, [180, 240, 300]);
assert.deepEqual(duel.roomSettings.roundFormats, [1, 3, 5]);
assert.deepEqual(duel.roomSettings.mapSelectionModes, ["fixed", "random", "vote"]);
assert.deepEqual(duel.roomSettings.mapIds, ["frost-wastes", "inferno-rift", "tempest-prime", "ocean-abyss", "terra-core", "celestial-void"]);
assert.deepEqual(duel.roomSettings.hazardLevels, ["low", "standard", "high"]);
assert.deepEqual(duel.roomSettings.specialFrequencies, ["off", "low", "standard", "high"]);
assert.deepEqual(duel.roomSettings.seedModes, ["random", "fixed"]);
assert.deepEqual(duel.roomSettings.modifiers, ["standard", "high-hazard", "mystery-storm", "weapon-frenzy", "support-rich", "sudden-death", "cataclysm-rush"]);

for (const symbol of ["DuelRoomSettingsInput", "validateDuelRoomSettings", "defaultDuelRoomSettings", "export class DuelRoom", "Only the room owner can change settings.", "[180, 240, 300]", "[1, 3, 5]"]) {
  assert(roomSource.includes(symbol), `Duel room runtime evidence missing: ${symbol}`);
}
for (const symbol of ["duelRuntimeTuning", "specialFrequencyMultiplier", "hazardLevelTuning", "sudden-death", "cataclysm-rush"]) assert(rulesSource.includes(symbol), `Duel rules runtime evidence missing: ${symbol}`);
for (const symbol of ["DUEL_CONTENT_VERSION", "DUEL_DEFAULT_REGULATION_SECONDS", "DUEL_HARD_OVERTIME_SECONDS"]) assert(modelSource.includes(symbol), `Duel model constant missing: ${symbol}`);
for (const personality of duel.bot.personalities) assert(botsSource.includes(`\"${personality}\"`), `Duel bot personality missing: ${personality}`);
for (const symbol of ["duelRuntimeTuning", "room.settings.matchLengthSeconds", "DuelEngine", "DuelBot"]) assert(localMatchSource.includes(symbol), `Duel local-match consumer missing: ${symbol}`);
for (const symbol of ["DUEL_PROJECTILE_BASE_TRAVEL_MS = 860", "DUEL_CANNON_TRAVEL_MS = 600", "DUEL_ROUND_BREAK_SECONDS = 5", "Damage still resolves on this authority clock"]) assert(timingSource.includes(symbol), `Duel authority timing evidence missing: ${symbol}`);

assert(uiSource.includes('from "../../../games/space-typing/src/duel/room"'), "Duel A12 UI must import the production room module directly");
assert(uiSource.includes("validateDuelRoomSettings(candidate)"), "Duel A12 scenario must use production validation");
assert(uiSource.includes("defaultDuelRoomSettings()"), "Duel A12 scenario must seed from production defaults");
assert(uiSource.includes("new DuelRoom({"), "Duel A12 scenario must instantiate the production room runtime in isolation");
assert(uiSource.includes("room.setBot({"), "Duel A12 Practice scenario must use production bot normalization");
assert(uiSource.includes("room.snapshot()"), "Duel A12 result must come from the production room snapshot");
assert(uiSource.includes("PRODUCTION RULE VALIDATION"), "Duel A12 UI must identify its production-rule seam");
assert(uiSource.includes("NO ADMIN PERSISTENCE"), "Duel A12 UI must state that scenario controls are non-persistent");
assert(uiSource.includes("Room Scenario"), "Duel A12 UI must expose safe scenario controls");
assert(uiSource.includes("Advanced authority & runtime details"), "low-level authority details must be progressively disclosed");
assert(!uiSource.includes('type = "range"'), "Duel A12 UI must not expose free-form tuning sliders");
assert(!uiSource.includes("api.createRevision"), "Duel A12 UI must not write Admin revisions");
assert(!uiSource.includes("api.publish"), "Duel A12 UI must not publish a synthetic Duel policy");
assert(!uiSource.includes("manualProjectileImpactDelayMs"), "unsupported impact timing must not become a control");

assert(routerSource.includes("renderPhaseBDuel"), "Duel renderer is not wired into Phase B");
assert(routerSource.includes("`${BASE}/duel`"), "Duel route is not wired into Phase B");
assert(shellSource.includes("const phaseB = renderPhaseBAdminScreen(path, this.navigate);"), "Space Typing shell must invoke Phase B router");
assert(!shellSource.includes("renderExtendedAdminScreen"), "Legacy Duel/mock renderer must remain unreachable");
assert(serverSource.includes("/api/admin/space-typing/duel/contract"), "Admin server Duel contract endpoint is missing");
const phaseMap = JSON.parse(phaseMapSource);
const row = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/duel");
assert.equal(row?.domain, "runtime.duel");
assert.equal(row?.persistence, "child-duel-room-session-runtime");
assert.equal(row?.applyBoundary, "none");
for (const unsupported of ["lives", "globalMatchTimeMinutes", "roundWindowSeconds", "manualProjectileImpactDelayMs", "burnFxToggle", "largeKoExplosionToggle", "announcerMilestonesToggle"]) assert(duel.unsupportedAdminMockFields.includes(unsupported), `Duel unsupported mock field missing: ${unsupported}`);

console.log("Space Typing A12 Duel validation passed: safe session controls instantiate production DuelRoom and no synthetic Admin policy is created.");
