import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");
const contract = JSON.parse(await read("games/space-typing/contracts/space-typing-admin-duel.v1.json"));
const [roomSource, rulesSource, modelSource, botsSource, localMatchSource, timingSource, uiSource, routerSource, shellSource, serverSource, phaseMapSource] = await Promise.all([
  read("games/space-typing/src/duel/room.ts"),
  read("games/space-typing/src/duel/rules.ts"),
  read("games/space-typing/src/duel/model.ts"),
  read("games/space-typing/src/duel/bots.ts"),
  read("games/space-typing/src/duel/local-match.ts"),
  read("games/space-typing/src/duel/presentation-timing.ts"),
  read("portal/src/admin/space-typing-duel-phase-b.ts"),
  read("portal/src/admin/space-typing-phase-b.ts"),
  read("portal/src/admin/space-typing.ts"),
  read("admin/server.mjs"),
  read("admin/space-typing-phase-b-map.v1.json"),
]);

const duel = contract.duel;
assert.equal(contract.contractRevision, "space-typing-admin-duel-v1");
assert.equal(contract.capability, "duel.read");
assert.deepEqual(contract.route, { id: "duel", path: "/admin/space-typing/duel", label: "Duel Settings" });
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

for (const symbol of [
  "DuelRoomSettingsInput",
  "validateDuelRoomSettings",
  "defaultDuelRoomSettings",
  "createPracticeDuelRoom",
  "Only the room owner can change settings.",
  "[180, 240, 300]",
  "[1, 3, 5]",
  '"fixed"',
  '"random"',
  '"vote"',
]) assert(roomSource.includes(symbol), `Duel room runtime evidence missing: ${symbol}`);
for (const id of duel.roomSettings.mapIds) assert(roomSource.includes(`\"${id}\"`), `Duel map id missing from room runtime: ${id}`);
for (const modifier of duel.roomSettings.modifiers) assert(roomSource.includes(`\"${modifier}\"`), `Duel modifier missing from room runtime: ${modifier}`);
for (const symbol of ["duelRuntimeTuning", "specialFrequencyMultiplier", "hazardLevelTuning", "sudden-death", "cataclysm-rush"]) assert(rulesSource.includes(symbol), `Duel rules runtime evidence missing: ${symbol}`);
for (const symbol of ["DUEL_CONTENT_VERSION", "DUEL_DEFAULT_REGULATION_SECONDS", "DUEL_HARD_OVERTIME_SECONDS"]) assert(modelSource.includes(symbol), `Duel model constant missing: ${symbol}`);
for (const personality of duel.bot.personalities) assert(botsSource.includes(`\"${personality}\"`), `Duel bot personality missing: ${personality}`);
for (const symbol of ["duelRuntimeTuning", "room.settings.matchLengthSeconds", "DuelEngine", "DuelBot"]) assert(localMatchSource.includes(symbol), `Duel local-match consumer missing: ${symbol}`);
for (const symbol of ["DUEL_PROJECTILE_BASE_TRAVEL_MS = 860", "DUEL_CANNON_TRAVEL_MS = 600", "DUEL_ROUND_BREAK_SECONDS = 5", "Damage still resolves on this authority clock"]) assert(timingSource.includes(symbol), `Duel authority timing evidence missing: ${symbol}`);

assert(uiSource.includes("/api/admin/space-typing/duel/contract"), "Duel UI must read the canonical child sidecar contract");
assert(uiSource.includes("RUNTIME-BACKED · READ ONLY"), "Duel UI must expose read-only Admin ownership");
assert(uiSource.includes("ROOM OWNER CONFIG"), "Duel UI must distinguish room-owner config from Admin config");
assert(uiSource.includes("Damage resolves on authority clock"), "Duel UI must explain authority timing");
assert(!uiSource.includes('type = "range"'), "Duel Phase B UI must not expose free-form range controls");
assert(!uiSource.includes("api.createRevision"), "Duel Phase B UI must not write Admin revisions");
assert(!uiSource.includes("api.publish"), "Duel Phase B UI must not publish a synthetic Duel policy");
assert(!uiSource.includes("api.rollback"), "Duel Phase B UI must not mutate the active Admin revision pointer");

assert(routerSource.includes("renderPhaseBDuel"), "Duel renderer is not wired into Phase B");
assert(routerSource.includes("`${BASE}/duel`"), "Duel route is not wired into Phase B");
const phaseBCall = "const phaseB = renderPhaseBAdminScreen(path, this.navigate);";
assert(shellSource.includes(phaseBCall), "Space Typing shell must invoke the Phase B router");
assert(shellSource.includes("if (phaseB !== null) return phaseB;"), "Space Typing shell must return the canonical Phase B renderer");
assert(!shellSource.includes("renderExtendedAdminScreen"), "Legacy Duel/mock renderer must not remain reachable from the production shell");
assert(shellSource.includes("return this.renderUnknown(path);"), "Unknown Admin routes must terminate at the explicit unknown-route guard");
assert(serverSource.includes("space-typing-admin-duel.v1.json"), "Admin server must load Duel from the pinned child contract");
assert(serverSource.includes("/api/admin/space-typing/duel/contract"), "Admin server Duel contract endpoint is missing");

const phaseMap = JSON.parse(phaseMapSource);
const row = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/duel");
assert.equal(row?.domain, "runtime.duel");
assert.equal(row?.persistence, "child-duel-room-session-runtime");
assert.equal(row?.applyBoundary, "none");
assert.equal(row?.status, "phase-b-ui-wired-runtime-backed-readonly");

for (const unsupported of [
  "lives",
  "globalMatchTimeMinutes",
  "roundWindowSeconds",
  "manualProjectileImpactDelayMs",
  "burnFxToggle",
  "largeKoExplosionToggle",
  "announcerMilestonesToggle",
]) assert(duel.unsupportedAdminMockFields.includes(unsupported), `Duel unsupported mock field missing: ${unsupported}`);

console.log("Space Typing Duel Admin validation passed: room-owner runtime rules + authority timing are read-only in Admin and legacy mock authoring is unreachable.");
