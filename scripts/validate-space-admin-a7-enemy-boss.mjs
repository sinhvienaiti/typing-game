import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const child = resolve(root, "games/space-typing");

const [
  capabilities,
  enemyPolicy,
  enemyPreview,
  enemyProjectilePolicy,
  enemyRegistry,
  worldRoster,
  bossPolicy,
  bossPreview,
  bossIdentity,
  enemyPage,
  bossPage,
] = await Promise.all([
  readFile(resolve(child, "src/admin/a7-enemy-boss-capabilities.ts"), "utf8"),
  readFile(resolve(child, "src/admin/enemy-runtime-policy.ts"), "utf8"),
  readFile(resolve(child, "src/admin/enemy-registry-preview.ts"), "utf8"),
  readFile(resolve(child, "src/combat/enemy-projectile-policy.ts"), "utf8"),
  readFile(resolve(child, "src/enemies/registry.ts"), "utf8"),
  readFile(resolve(child, "src/worlds/roster.ts"), "utf8"),
  readFile(resolve(child, "src/admin/boss-runtime-policy.ts"), "utf8"),
  readFile(resolve(child, "scripts/admin/boss-registry-preview.ts"), "utf8"),
  readFile(resolve(child, "src/boss/identity.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-enemies-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-bosses-phase-b.ts"), "utf8"),
]);

function requireText(source, needle, label) {
  assert.ok(source.includes(needle), `${label}: expected ${JSON.stringify(needle)}`);
}

function forbidText(source, needle, label) {
  assert.ok(!source.includes(needle), `${label}: forbidden ${JSON.stringify(needle)}`);
}

for (const id of [
  "enemy.projectile-mode",
  "enemy.min-stage",
  "enemy.registry-identity-reward-visual",
  "enemy.media-vfx-binding",
  "boss.metadata-name-title",
  "boss.identity-stage-usage",
  "boss.phase-mechanics",
  "boss.media-vfx-sfx-binding",
  "boss.reward-drop-binding",
]) {
  requireText(capabilities, `id: "${id}"`, `A7 capability ${id} is registered`);
}
for (const status of [
  "SUPPORTED NOW",
  "REQUIRES CANONICAL MIGRATION",
  "READ-ONLY REFERENCE",
  "DEFERRED / UNSUPPORTED",
]) {
  requireText(capabilities, `status: "${status}"`, `A7 matrix uses ${status}`);
}

// Enemy global projectile mode is the one proven writable production seam.
requireText(enemyPolicy, 'projectileMode?: AdminEnemyProjectileMode', "Enemy Admin policy persists projectileMode");
requireText(enemyProjectilePolicy, 'ACTIVE_ENEMY_RUNTIME_SESSION', "Enemy projectile resolver reads the active published Admin session");
requireText(enemyProjectilePolicy, 'resolveEnemyProjectileMode', "Enemy projectile policy exposes a production resolver");
requireText(enemyProjectilePolicy, 'normalEnemyProjectilesEnabled', "Enemy projectile policy exposes the production enablement consumer");
requireText(capabilities, 'id: "enemy.projectile-mode"', "Enemy projectile capability exists");
requireText(capabilities, 'productionConsumer: "src/combat/enemy-projectile-policy.ts::normalEnemyProjectilesEnabled() consumed by Game.ts"', "A7 records the projectile production consumer");

// minStage currently has persistence + validation + registry preview only.
requireText(enemyPolicy, 'minStage?: number', "Enemy policy still accepts minStage for compatibility/migration");
requireText(enemyPreview, 'minStage: override?.minStage ?? definition.minStage', "Enemy Admin preview can materialize a minStage candidate");
requireText(capabilities, 'id: "enemy.min-stage"', "Enemy minStage capability exists");
requireText(capabilities, 'status: "REQUIRES CANONICAL MIGRATION"', "A7 keeps unproven authoring migration-gated");
forbidText(enemyRegistry, 'activeEnemyRuntimeOverride', "Bundled enemyDefinition must not be mistaken for an Admin-aware resolver");
forbidText(worldRoster, 'activeEnemyRuntimeOverride', "World roster must not be mistaken for consuming the Enemy Admin minStage override");

// Rich Enemy registry data is production-owned but not revision-backed authoring.
for (const token of ["rewardPower", "visual:", "spawnFx", "hitFx", "deathFx"]) {
  requireText(enemyRegistry, token, `Enemy registry owns bundled ${token}`);
}

// Boss name/title currently stop at the Admin envelope + registry preview.
requireText(bossPolicy, 'name?: string', "Boss Admin policy persists name");
requireText(bossPolicy, 'title?: string', "Boss Admin policy persists title");
requireText(bossPreview, 'authorableFields: ["name", "title"]', "Boss registry preview documents its current envelope");
requireText(capabilities, 'id: "boss.metadata-name-title"', "Boss metadata capability exists");
forbidText(bossIdentity, 'activeBossRuntimeOverride', "bossIdentityForStage must not be mistaken for consuming the Admin Boss metadata override");
requireText(bossIdentity, 'export function bossIdentityForStage', "A7 records the current bundled Boss production identity resolver");

// Existing pages retain immutable Draft creation and History-owned activation.
requireText(enemyPage, 'const validated = await previewEnemies(policy)', "Enemies validate through the canonical child preview before Draft creation");
requireText(enemyPage, 'api.createRevision', "Enemies retain immutable Draft creation");
forbidText(enemyPage, 'api.publish(', "Enemies must not bypass History with direct publish");
requireText(bossPage, 'const validated = await previewBosses(policy)', "Bosses validate through the canonical child preview before Draft creation");
requireText(bossPage, 'api.createRevision', "Bosses retain immutable Draft creation");
forbidText(bossPage, 'api.publish(', "Bosses must not bypass History with direct publish");

// Do not invent rich write seams before child runtime ownership exists.
for (const fakeField of [
  "mediaAssetVersionId",
  "imageAssetVersionId",
  "modelAssetVersionId",
  "vfxAssetVersionId",
  "sfxAssetVersionId",
  "dropTableId",
  "rewardTableId",
  "phaseAssetVersionId",
]) {
  forbidText(enemyPolicy, fakeField, `Enemy policy must not invent ${fakeField}`);
  forbidText(bossPolicy, fakeField, `Boss policy must not invent ${fakeField}`);
}

console.log("Space Typing Admin A7.0 Enemies/Bosses capability audit: PASS — projectileMode is production-backed; Enemy minStage and Boss name/title remain migration-gated until real production consumers exist; rich registry/combat/media ownership stays read-only or closed.");
