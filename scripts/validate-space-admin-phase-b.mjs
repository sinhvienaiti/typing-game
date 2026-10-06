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

assert.equal(map.schemaVersion, 1);
assert.equal(map.phase, "B");
assert.equal(map.contractRevision, "space-typing-admin-v1");
assert.equal(map.screens.length, 30, "Phase B mapping must cover all 30 registered Admin screens");

const routes = map.screens.map((entry) => entry.route);
assert.equal(new Set(routes).size, routes.length, "Phase B mapping routes must be unique");

const audio = map.screens.find((entry) => entry.route === "/admin/space-typing/audio");
const worldMusic = map.screens.find((entry) => entry.route === "/admin/space-typing/world-music");
const settings = map.screens.find((entry) => entry.route === "/admin/space-typing/settings");
const flags = map.screens.find((entry) => entry.route === "/admin/space-typing/flags");
assert.equal(audio?.domain, "audio");
assert.equal(audio?.status, "phase-b-ui-wired");
assert.equal(audio?.applyBoundary, "safe-boundary");
assert.equal(worldMusic?.domain, "worldMusic");
assert.equal(worldMusic?.status, "phase-b-ui-wired-global-world");
assert.equal(worldMusic?.applyBoundary, "next-track-or-state");
assert.equal(settings?.domain, "system");
assert.equal(settings?.status, "phase-b-ui-wired");
assert.equal(settings?.applyBoundary, "new-session");
assert.equal(flags?.domain, "featureFlags");
assert.equal(flags?.status, "phase-b-ui-wired");
assert.equal(flags?.applyBoundary, "new-session");

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
assert.match(worldMusicPhaseB, /B04\.1 World Music Draft/);
assert.match(worldMusicPhaseB, /api\.previewWorldMusic/);
assert.match(worldMusicPhaseB, /api\.createRevision/);
assert.doesNotMatch(worldMusicPhaseB, /api\.publish/);
assert.match(worldMusicPhaseB, /GALAXY \/ STAGE BLOCKED/);
assert.match(worldMusicPhaseB, /WorldMusicPolicy v1 has no galaxy\/stage keys/);
assert.match(worldMusicPhaseB, /assertStableActiveRevision/);
assert.match(phaseB, /assertStableActiveRevision/);
assert.match(phaseB, /loadedActiveRevision/);
assert.match(phaseB, /Reload this screen before saving to avoid overwriting newer published changes/);

const dangerous = map.screens.filter((entry) =>
  entry.domain.startsWith("economy.") || entry.domain.startsWith("pvp.") || entry.domain === "system" || entry.domain === "featureFlags",
);
for (const entry of dangerous) {
  assert.notEqual(entry.applyBoundary, "immediate", `${entry.screen} must not use immediate production apply`);
}

console.log(`Space Typing Admin Phase B mapping: PASS (${map.screens.length} screens, B01-B04.1 revision-backed domains ready).`);
