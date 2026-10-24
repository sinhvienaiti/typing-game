import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";

const root = new URL("../", import.meta.url);
const readText = (relativePath) => readFile(new URL(relativePath, root), "utf8");
const readSurface = async (wrapperPath, legacyPath) => `${await readText(wrapperPath)}\n${await readText(legacyPath)}`;
const map = JSON.parse(await readText("admin/space-typing-phase-b-map.v1.json"));
const defaultConfig = await readText("admin/default-config.mjs");
const store = await readText("admin/store.mjs");
const api = await readText("portal/src/admin/api.ts");
const main = await readText("portal/src/admin/space-typing.ts");
const phaseBRouter = await readText("portal/src/admin/space-typing-phase-b.ts");
const phaseBCore = await readText("portal/src/admin/space-typing-phase-b-core.ts");
const settingsPhaseB = await readSurface("portal/src/admin/space-typing-settings-phase-b.ts", "portal/src/admin/space-typing-settings-phase-b-legacy.ts");
const featureGatesPhaseB = await readText("portal/src/admin/space-typing-feature-gates-phase-b.ts");
const contractReader = await readText("portal/src/admin/space-typing-contract-reader.ts");
const phaseB = `${phaseBRouter}\n${phaseBCore}`;
const stagesPhaseB = await readSurface("portal/src/admin/space-typing-stages-phase-b.ts", "portal/src/admin/space-typing-stages-phase-b-legacy.ts");
const audioPhaseB = await readText("portal/src/admin/space-typing-audio-phase-b.ts");
const sfxPhaseB = await readText("portal/src/admin/space-typing-sfx-phase-b.ts");
const worldMusicPhaseB = await readText("portal/src/admin/space-typing-world-music-phase-b.ts");
const shipsPhaseB = await readText("portal/src/admin/space-typing-ships-phase-b.ts");
const equipmentPhaseB = await readSurface("portal/src/admin/space-typing-equipment-phase-b.ts", "portal/src/admin/space-typing-equipment-phase-b-legacy.ts");
const skillsPhaseB = await readSurface("portal/src/admin/space-typing-skills-phase-b.ts", "portal/src/admin/space-typing-skills-phase-b-legacy.ts");
const enemiesPhaseB = await readText("portal/src/admin/space-typing-enemies-phase-b.ts");
const bossesPhaseB = await readSurface("portal/src/admin/space-typing-bosses-phase-b.ts", "portal/src/admin/space-typing-bosses-phase-b-legacy.ts");
const historyPhaseB = await readText("portal/src/admin/space-typing-history-phase-b.ts");
const server = await readText("admin/server.mjs");

assert.equal(map.schemaVersion, 1);
assert.equal(map.phase, "B");
assert.equal(map.contractRevision, "space-typing-admin-v1");
assert.equal(map.screens.length, 31, "Phase B mapping must cover all 31 registered Admin screens");

const routes = map.screens.map((entry) => entry.route);
assert.equal(new Set(routes).size, routes.length, "Phase B mapping routes must be unique");

const audio = map.screens.find((entry) => entry.route === "/admin/space-typing/audio");
const sfx = map.screens.find((entry) => entry.route === "/admin/space-typing/sfx");
const worldMusic = map.screens.find((entry) => entry.route === "/admin/space-typing/world-music");
const ships = map.screens.find((entry) => entry.route === "/admin/space-typing/ships");
const equipment = map.screens.find((entry) => entry.route === "/admin/space-typing/equipment");
const skills = map.screens.find((entry) => entry.route === "/admin/space-typing/skills");
const enemies = map.screens.find((entry) => entry.route === "/admin/space-typing/enemies");
const bosses = map.screens.find((entry) => entry.route === "/admin/space-typing/bosses");
const stages = map.screens.find((entry) => entry.route === "/admin/space-typing/stages");
const settings = map.screens.find((entry) => entry.route === "/admin/space-typing/settings");
const featureGates = map.screens.find((entry) => entry.route === "/admin/space-typing/feature-gates");
const history = map.screens.find((entry) => entry.route === "/admin/space-typing/history");
assert.equal(audio?.domain, "audio");
assert.equal(audio?.status, "phase-b-ui-wired");
assert.equal(audio?.applyBoundary, "safe-boundary");
assert.equal(sfx?.domain, "audio.sfx");
assert.equal(sfx?.status, "phase-b-ui-wired-runtime-backed-readonly-preview");
assert.equal(sfx?.persistence, "child-code-owned-sample-bank");
assert.equal(sfx?.applyBoundary, "none");
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
assert.equal(stages?.domain, "content.stages");
assert.equal(stages?.persistence, "immutable-revision-store");
assert.equal(stages?.applyBoundary, "new-session");
assert.equal(settings?.domain, "system");
assert.equal(settings?.status, "phase-b-ui-wired");
assert.equal(settings?.applyBoundary, "new-session");
assert.equal(featureGates?.domain, "runtime.featureGates");
assert.equal(featureGates?.status, "phase-b-ui-wired-runtime-backed-readonly");
assert.equal(featureGates?.persistence, "child-browser-local-storage");
assert.equal(featureGates?.applyBoundary, "none");
assert.equal(featureGates?.legacyRouteAlias, "/admin/space-typing/flags");
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
assert.match(defaultConfig, /projectileMode:\s*"auto"/);
assert.match(defaultConfig, /\bbosses:\s*\{/);
assert.match(defaultConfig, /\bstages:\s*\{/);
assert.match(store, /config\.system !== undefined/);
assert.match(store, /validateSystem\(config\.system\)/);
assert.match(store, /config\.featureFlags !== undefined/);
assert.match(store, /validateFeatureFlags\(config\.featureFlags\)/);
assert.match(api, /export type GeneralSettingsConfig/);
assert.match(api, /export type FeatureFlagConfig/);
assert.match(api, /getRuntime\(\): Promise<AdminRuntimePayload>/);
assert.match(main, /renderPhaseBAdminScreen/);
assert.match(main, /if \(phaseB !== null\) return phaseB/);

assert.match(phaseBRouter, /attachProductionPreviewClassification\(screen, path\)/);
assert.match(phaseBRouter, /attachRoleAwareActionGates\(screen\)/);

assert.match(phaseBRouter, /renderPhaseBSettings/);
assert.match(phaseBRouter, /\$\{BASE\}\/settings`\) return decorated\(path, renderPhaseBSettings\(navigate\)\)/);
assert.ok(
  phaseBRouter.indexOf("`${BASE}/settings`") < phaseBRouter.indexOf("return decorated(path, renderPhaseBCoreAdminScreen(path, navigate));"),
  "General Settings must be intercepted before the legacy core renderer",
);
assert.match(settingsPhaseB, /Admin Phase B · General Settings draft/);
assert.match(settingsPhaseB, /space-typing-settings-phase-b-legacy/);
assert.match(settingsPhaseB, /Access & Permissions/);
assert.match(settingsPhaseB, /api\.createRevision/);
assert.doesNotMatch(settingsPhaseB, /api\.publish/);
assert.match(settingsPhaseB, /loadedActiveRevision/);
assert.match(settingsPhaseB, /ACTIVE · unavailable/);
assert.match(settingsPhaseB, /renderAdminFailureState/);
assert.match(settingsPhaseB, /schema defaults/i);
assert.match(settingsPhaseB, /runtime unchanged/);

assert.match(phaseBRouter, /renderPhaseBFeatureGates/);
assert.match(phaseBRouter, /\$\{BASE\}\/feature-gates/);
assert.match(phaseBRouter, /\$\{BASE\}\/flags/);
assert.match(featureGatesPhaseB, /RUNTIME-BACKED · READ ONLY/);
assert.match(featureGatesPhaseB, /NO REMOTE ROLLOUT/);
assert.match(featureGatesPhaseB, /readMainAdminContractSection/);
assert.match(featureGatesPhaseB, /readMainAdminContractSection\("featureGates", "feature-gates\.read"/);
assert.match(contractReader, /\/api\/admin\/space-typing\/contract/);
assert.match(contractReader, /api\.requestJson<unknown>/);
assert.match(contractReader, /Array\.isArray\(payload\["capabilities"\]\)/);
assert.doesNotMatch(featureGatesPhaseB, /api\.createRevision/);
assert.doesNotMatch(featureGatesPhaseB, /api\.publish/);
assert.doesNotMatch(featureGatesPhaseB, /rolloutPercent/);
assert.doesNotMatch(featureGatesPhaseB, /type\s*=\s*["']range["']/);

assert.match(phaseB, /renderPhaseBAudio/);
assert.match(audioPhaseB, /Admin Phase B · Audio Defaults draft/);
assert.match(audioPhaseB, /api\.createRevision/);
assert.doesNotMatch(audioPhaseB, /api\.publish/);
assert.match(audioPhaseB, /spaceTypingSettingsV1/);
assert.match(audioPhaseB, /PRONUNCIATION_DUCK/);
assert.match(audioPhaseB, /assertStableActiveRevision/);

assert.match(phaseBRouter, /renderPhaseBSfx/);
assert.match(phaseBRouter, /\$\{BASE\}\/sfx`\) return decorated\(path, renderPhaseBSfx\(\)\)/);
assert.match(sfxPhaseB, /createAdminSfxCatalog/);
assert.match(sfxPhaseB, /RUNTIME-BACKED · READ ONLY/);
assert.match(sfxPhaseB, /TEST PLAYBACK/);
assert.match(sfxPhaseB, /NO FAKE SFX POLICY/);
assert.match(sfxPhaseB, /Runtime Gain/);
assert.match(sfxPhaseB, /Pool/);
assert.match(sfxPhaseB, /new Audio\(productionSampleUrl/);
assert.doesNotMatch(sfxPhaseB, /api\.createRevision/);
assert.doesNotMatch(sfxPhaseB, /api\.publish/);

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
assert.match(equipmentPhaseB, /space-typing-equipment-phase-b-legacy/);
assert.match(equipmentPhaseB, /createEquipmentProductionRuntimePanel/);
assert.match(equipmentPhaseB, /api\.createRevision/);
assert.doesNotMatch(equipmentPhaseB, /api\.publish/);
assert.match(phaseB, /renderPhaseBSkills/);
assert.match(skillsPhaseB, /B06\.3/);
assert.match(skillsPhaseB, /space-typing-skills-phase-b-legacy/);
assert.match(skillsPhaseB, /createSkillProductionRuntimePanel/);
assert.match(skillsPhaseB, /api\.createRevision/);
assert.doesNotMatch(skillsPhaseB, /api\.publish/);

assert.match(phaseB, /renderPhaseBEnemies/);
assert.match(enemiesPhaseB, /B06\.4/);
assert.match(enemiesPhaseB, /\/api\/admin\/space-typing\/enemies\/preview/);
assert.match(enemiesPhaseB, /Minimum Stage/);
assert.match(enemiesPhaseB, /minStage/);
assert.match(enemiesPhaseB, /Admin A7 · Enemy projectile policy draft/);
assert.match(enemiesPhaseB, /Normal Enemy Projectiles/);
assert.match(enemiesPhaseB, /projectileMode/);
assert.match(enemiesPhaseB, /PROJECTILES · NEW SESSION/);
assert.match(enemiesPhaseB, /REQUIRES CANONICAL MIGRATION/);
assert.match(enemiesPhaseB, /minStage\.control\.disabled = true/);
assert.match(enemiesPhaseB, /api\.createRevision/);
assert.doesNotMatch(enemiesPhaseB, /api\.publish/);
assert.doesNotMatch(enemiesPhaseB, /Canonical runtime consumer: Enemy spawn profile minimum-stage gate/);
assert.doesNotMatch(enemiesPhaseB, /gameplay snapshots Enemy admission/);
assert.match(server, /\/api\/runtime\/space-typing\/enemies/);
assert.match(server, /\/api\/admin\/space-typing\/enemies\/preview/);

assert.match(phaseB, /renderPhaseBBosses/);
assert.match(phaseB, /\$\{BASE\}\/bosses/);
assert.match(bossesPhaseB, /B06\.5/);
assert.match(bossesPhaseB, /space-typing-bosses-phase-b-legacy/);
assert.match(bossesPhaseB, /createBossProductionPreviewPanel/);
assert.match(bossesPhaseB, /\/api\/admin\/space-typing\/bosses\/preview/);
assert.match(bossesPhaseB, /Name/);
assert.match(bossesPhaseB, /Title/);
assert.match(bossesPhaseB, /PREVIEW · NO RUNTIME APPLY/);
assert.match(bossesPhaseB, /Name \/ Title/);
assert.match(bossesPhaseB, /REQUIRES CANONICAL MIGRATION/);
assert.match(bossesPhaseB, /Phases \/ Mechanics/);
assert.match(bossesPhaseB, /Rewards \/ Drops/);
assert.doesNotMatch(bossesPhaseB, /api\.createRevision/);
assert.doesNotMatch(bossesPhaseB, /api\.publish/);
assert.doesNotMatch(bossesPhaseB, /Admin Phase B · B06\.5 Boss identity draft/);
assert.doesNotMatch(bossesPhaseB, /gameplay snapshots Boss identity/);
assert.match(server, /\/api\/runtime\/space-typing\/bosses/);
assert.match(server, /\/api\/admin\/space-typing\/bosses\/preview/);

assert.match(phaseBRouter, /renderPhaseBStages/);
assert.match(phaseBRouter, /\$\{BASE\}\/stages/);
assert.match(stagesPhaseB, /B06\.6/);
assert.match(stagesPhaseB, /space-typing-stages-phase-b-legacy/);
assert.match(stagesPhaseB, /createStageProductionPreviewPanel/);
assert.match(stagesPhaseB, /\/api\/admin\/space-typing\/stages\/preview/);
assert.match(stagesPhaseB, /enemyBudget/);
assert.match(stagesPhaseB, /eliteChance/);
assert.match(stagesPhaseB, /modifierSlots/);
assert.match(stagesPhaseB, /api\.createRevision/);
assert.doesNotMatch(stagesPhaseB, /api\.publish/);
assert.match(server, /\/api\/runtime\/space-typing\/stages/);
assert.match(server, /\/api\/admin\/space-typing\/stages\/preview/);

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
  entry.domain.startsWith("economy.") || entry.domain.startsWith("pvp.") || entry.domain === "system" || entry.domain === "runtime.featureGates",
);
for (const entry of dangerous) {
  assert.notEqual(entry.applyBoundary, "immediate", `${entry.screen} must not use immediate production apply`);
}

console.log(`Space Typing Admin Phase B mapping: PASS (${map.screens.length} screens, retained Phase B implementations audited through their V2 wrappers, A9 SFX production catalog/Test Playback read-only, A7 Enemy projectile-only authoring + fail-closed Bosses, fail-closed General Settings, runtime-backed Feature Gates via safe shared contract reader).`);
