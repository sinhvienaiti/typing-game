import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const root = new URL("../", import.meta.url);
const map = JSON.parse(await readFile(new URL("admin/space-typing-phase-b-map.v1.json", root), "utf8"));
const defaultConfig = await readFile(new URL("admin/default-config.mjs", root), "utf8");
const store = await readFile(new URL("admin/store.mjs", root), "utf8");
const api = await readFile(new URL("portal/src/admin/api.ts", root), "utf8");
const main = await readFile(new URL("portal/src/admin/space-typing.ts", root), "utf8");
const phaseB = await readFile(new URL("portal/src/admin/space-typing-phase-b.ts", root), "utf8");
const audioPhaseB = await readFile(new URL("portal/src/admin/space-typing-audio-phase-b.ts", root), "utf8");
const worldMusicPhaseB = await readFile(new URL("portal/src/admin/space-typing-world-music-phase-b.ts", root), "utf8");
const shipsPhaseB = await readFile(new URL("portal/src/admin/space-typing-ships-phase-b.ts", root), "utf8");
const equipmentPhaseB = await readFile(new URL("portal/src/admin/space-typing-equipment-phase-b.ts", root), "utf8");
const skillsPhaseB = await readFile(new URL("portal/src/admin/space-typing-skills-phase-b.ts", root), "utf8");
const enemiesPhaseB = await readFile(new URL("portal/src/admin/space-typing-enemies-phase-b.ts", root), "utf8");
const bossesPhaseB = await readFile(new URL("portal/src/admin/space-typing-bosses-phase-b.ts", root), "utf8");
const historyPhaseB = await readFile(new URL("portal/src/admin/space-typing-history-phase-b.ts", root), "utf8");
const server = await readFile(new URL("admin/server.mjs", root), "utf8");

assert.equal(map.schemaVersion, 1);
assert.equal(map.phase, "B");
assert.equal(map.contractRevision, "space-typing-admin-v1");
assert.equal(map.screens.length, 30, "Phase B mapping must cover all 30 registered Admin screens");

const routes = map.screens.map((entry) => entry.route);
assert.equal(new Set(routes).size, routes.length, "Phase B mapping routes must be unique");

const audio = map.screens.find((entry) => entry.route === "/admin/space-typing/audio");
const worldMusic = map.screens.find((entry) => entry.route === "/admin/space-typing/world-music");
const ships = map.screens.find((entry) => entry.route === "/admin/space-typing/ships");
const equipment = map.screens.find((entry) => entry.route === "/admin/space-typing/equipment");
const skills = map.screens.find((entry) => entry.route === "/admin/space-typing/skills");
const enemies = map.screens.find((entry) => entry.route === "/admin/space-typing/enemies");
const bosses = map.screens.find((entry) => entry.route === "/admin/space-typing/bosses");
const settings = map.screens.find((entry) => entry.route === "/admin/space-typing/settings");
const flags = map.screens.find((entry) => entry.route === "/admin/space-typing/flags");
const history = map.screens.find((entry) => entry.route === "/admin/space-typing/history");
assert.equal(audio?.domain, "audio");
assert.equal(audio?.status, "phase-b-ui-wired");
assert.equal(audio?.applyBoundary, "safe-boundary");
assert.equal(worldMusic?.domain, "worldMusic");
assert.equal(worldMusic?.status, "phase-b-ui-wired-all-scopes");
assert.equal(worldMusic?.applyBoundary, "next-track-or-state");
for (const contentScreen of [ships, equipment, skills, enemies, bosses]) {
  assert.equal(contentScreen?.status, "phase-b-ui-wired-runtime-backed");
  assert.equal(contentScreen?.persistence, "immutable-revision-store");
  assert.equal(contentScreen?.applyBoundary, "new-session");
}
assert.equal(ships?.domain, "content.ships");
assert.equal(equipment?.domain, "content.equipment");
assert.equal(skills?.domain, "content.skills");
assert.equal(enemies?.domain, "content.enemies");
assert.equal(bosses?.domain, "content.bosses");
assert.equal(settings?.domain, "system");
assert.equal(settings?.status, "phase-b-ui-wired");
assert.equal(settings?.applyBoundary, "new-session");
assert.equal(flags?.domain, "featureFlags");
assert.equal(flags?.status, "phase-b-ui-wired");
assert.equal(flags?.applyBoundary, "new-session");
assert.equal(history?.domain, "revisions");
assert.equal(history?.status, "phase-b-ui-wired");
assert.equal(history?.applyBoundary, "cas-publish");

for (const entry of map.screens) {
  assert.ok(entry.route.startsWith("/admin/space-typing"), `Invalid Admin route: ${entry.route}`);
  assert.ok(entry.screen, `Missing screen label for ${entry.route}`);
  assert.ok(entry.domain, `Missing domain for ${entry.route}`);
  assert.ok(entry.persistence, `Missing persistence owner for ${entry.route}`);
  assert.ok(entry.applyBoundary, `Missing apply boundary for ${entry.route}`);
  assert.ok(entry.status, `Missing Phase B status for ${entry.route}`);
}

assert.match(defaultConfig, /\bsystem:\s*\{/);
assert.match(defaultConfig, /\bfeatureFlags:\s*\{/);
assert.match(defaultConfig, /\benemies:\s*\{/);
assert.match(defaultConfig, /\bbosses:\s*\{/);
assert.match(store, /config\.system !== undefined/);
assert.match(store, /validateSystem\(config\.system\)/);
assert.match(store, /config\.featureFlags !== undefined/);
assert.match(store, /validateFeatureFlags\(config\.featureFlags\)/);
assert.match(store, /rolloutPercent/);
assert.match(store, /new-players/);
assert.match(store, /competitive/);
assert.match(api, /export type GeneralSettingsConfig/);
assert.match(api, /export type FeatureFlagConfig/);
assert.match(api, /getRuntime\(\): Promise<AdminRuntimePayload>/);
assert.match(main, /renderPhaseBAdminScreen/);
assert.match(main, /if \(phaseB !== null\) return phaseB/);
assert.match(phaseB, /Admin Phase B · General Settings draft/);
assert.match(phaseB, /Admin Phase B · Feature Flags draft/);
assert.match(phaseB, /api\.createRevision/);
assert.doesNotMatch(phaseB, /api\.publish/);
assert.match(phaseB, /runtime unchanged/);
assert.match(phaseB, /renderPhaseBAudio/);
assert.match(audioPhaseB, /Admin Phase B · Audio Defaults draft/);
assert.match(audioPhaseB, /api\.createRevision/);
assert.doesNotMatch(audioPhaseB, /api\.publish/);
assert.match(audioPhaseB, /spaceTypingSettingsV1/);
assert.match(audioPhaseB, /PRONUNCIATION_DUCK/);
assert.match(audioPhaseB, /assertStableActiveRevision/);
assert.match(phaseB, /renderPhaseBWorldMusic/);
assert.match(worldMusicPhaseB, /B04\.2 World Music Draft/);
assert.match(worldMusicPhaseB, /api\.previewWorldMusic/);
assert.match(worldMusicPhaseB, /api\.createRevision/);
assert.doesNotMatch(worldMusicPhaseB, /api\.publish/);
assert.doesNotMatch(worldMusicPhaseB, /GALAXY \/ STAGE BLOCKED/);
assert.match(worldMusicPhaseB, /type Scope = "global" \| "galaxy" \| "world" \| "stage"/);
assert.match(worldMusicPhaseB, /policy\.galaxies/);
assert.match(worldMusicPhaseB, /policy\.stages/);
assert.match(worldMusicPhaseB, /stageNumber/);
assert.match(worldMusicPhaseB, /assertStableActiveRevision/);

assert.match(phaseB, /renderPhaseBShips/);
assert.match(shipsPhaseB, /B06\.1/);
assert.match(shipsPhaseB, /api\.createRevision/);
assert.doesNotMatch(shipsPhaseB, /api\.publish/);
assert.match(phaseB, /renderPhaseBEquipment/);
assert.match(equipmentPhaseB, /B06\.2/);
assert.match(equipmentPhaseB, /api\.createRevision/);
assert.doesNotMatch(equipmentPhaseB, /api\.publish/);
assert.match(phaseB, /renderPhaseBSkills/);
assert.match(skillsPhaseB, /B06\.3/);
assert.match(skillsPhaseB, /api\.createRevision/);
assert.doesNotMatch(skillsPhaseB, /api\.publish/);
assert.match(phaseB, /renderPhaseBEnemies/);
assert.match(enemiesPhaseB, /B06\.4/);
assert.match(enemiesPhaseB, /\/api\/admin\/space-typing\/enemies\/preview/);
assert.match(enemiesPhaseB, /Minimum Stage/);
assert.match(enemiesPhaseB, /minStage/);
assert.match(enemiesPhaseB, /Admin Phase B · B06\.4 Enemy admission draft/);
assert.match(enemiesPhaseB, /HP, Shield, Armor, Speed, Damage, AI, Spawn Weight, Skills, Projectiles, VFX, SFX, Drop Table and Enabled/);
assert.match(enemiesPhaseB, /api\.createRevision/);
assert.doesNotMatch(enemiesPhaseB, /api\.publish/);
assert.match(server, /\/api\/runtime\/space-typing\/enemies/);
assert.match(server, /\/api\/admin\/space-typing\/enemies\/preview/);

assert.match(phaseB, /renderPhaseBBosses/);
assert.match(phaseB, /\$\{BASE\}\/bosses/);
assert.match(bossesPhaseB, /B06\.5/);
assert.match(bossesPhaseB, /\/api\/admin\/space-typing\/bosses\/preview/);
assert.match(bossesPhaseB, /Name/);
assert.match(bossesPhaseB, /Title/);
assert.match(bossesPhaseB, /name.*100/si);
assert.match(bossesPhaseB, /title.*160/si);
assert.match(bossesPhaseB, /Admin Phase B · B06\.5 Boss identity draft/);
assert.match(bossesPhaseB, /HP, Shield, Armor, Damage, Speed/);
assert.match(bossesPhaseB, /api\.createRevision/);
assert.doesNotMatch(bossesPhaseB, /api\.publish/);
assert.match(server, /\/api\/runtime\/space-typing\/bosses/);
assert.match(server, /\/api\/admin\/space-typing\/bosses\/preview/);

assert.match(phaseB, /assertStableActiveRevision/);
assert.match(phaseB, /loadedActiveRevision/);
assert.match(phaseB, /Reload this screen before saving to avoid overwriting newer published changes/);
assert.match(phaseB, /renderPhaseBHistory/);
assert.match(historyPhaseB, /api\.validateRevision/);
assert.match(historyPhaseB, /api\.publish/);
assert.match(historyPhaseB, /api\.rollback/);
assert.match(historyPhaseB, /window\.confirm/);
assert.match(historyPhaseB, /publishable/);
assert.match(historyPhaseB, /rollbackEligible/);
assert.match(historyPhaseB, /diffValues/);
assert.match(store, /target\.parentRevision !== state\.activeRevision/);
assert.match(store, /must be a published ancestor/);
assert.match(server, /validate-revision/);
assert.match(api, /validateRevision\(revision: string\)/);

const dangerous = map.screens.filter((entry) =>
  entry.domain.startsWith("economy.") || entry.domain.startsWith("pvp.") || entry.domain === "system" || entry.domain === "featureFlags",
);
for (const entry of dangerous) {
  assert.notEqual(entry.applyBoundary, "immediate", `${entry.screen} must not use immediate production apply`);
}

console.log(`Space Typing Admin Phase B mapping: PASS (${map.screens.length} screens, B01-B06.5 runtime-backed domains ready).`);
