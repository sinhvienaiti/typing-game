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
requireText(enemyPolicy, 'projectileMode: AdminEnemyProjectileMode | null', "Enemy runtime session carries projectileMode");
requireText(enemyPolicy, 'const POLICY_KEYS = new Set(["configRevision", "projectileMode", "enemies"])', "Enemy runtime policy accepts projectileMode");
requireText(enemyPolicy, 'sanitizeProjectileMode(policy.projectileMode)', "Enemy runtime policy materializes projectileMode");
requireText(enemyProjectilePolicy, 'ACTIVE_ENEMY_RUNTIME_SESSION', "Enemy projectile resolver reads the active published Admin session");
requireText(enemyProjectilePolicy, 'resolveEnemyProjectileMode', "Enemy projectile policy exposes a production resolver");
requireText(enemyProjectilePolicy, 'normalEnemyProjectilesEnabled', "Enemy projectile policy exposes the production enablement consumer");
requireText(capabilities, 'id: "enemy.projectile-mode"', "Enemy projectile capability exists");
requireText(capabilities, 'productionConsumer: "src/combat/enemy-projectile-policy.ts::normalEnemyProjectilesEnabled() consumed by Game.ts"', "A7 records the projectile production consumer");

// minStage currently has persistence + validation + registry preview only.
requireText(enemyPolicy, 'minStage?: number', "Enemy policy still accepts minStage for compatibility/migration");
requireText(enemyPreview, 'minStage: override?.minStage ?? base.minStage', "Enemy Admin preview can materialize a minStage candidate");
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

// A7.1 UI must expose shared capability states and fail closed around migration-only fields.
requireText(enemyPage, 'createAssetTuningCapabilityState', "Enemies use shared A7 capability UI");
requireText(enemyPage, 'label: "Normal Enemy Projectile Policy"', "Enemies expose the production-backed projectile capability");
requireText(enemyPage, 'status: "SUPPORTED NOW"', "Enemy projectile policy is visibly supported");
requireText(enemyPage, 'label: "Minimum Stage"', "Enemies expose minStage capability state");
requireText(enemyPage, 'status: "REQUIRES CANONICAL MIGRATION"', "Enemy minStage is migration-gated");
requireText(enemyPage, 'minStage.control.disabled = true', "Enemy minStage editor is fail-closed");
requireText(enemyPage, 'badge("PROJECTILES · NEW SESSION"', "Enemy new-session badge is scoped to the production-backed projectile policy");
requireText(enemyPage, 'const validated = await previewEnemies(policy)', "Enemies validate through the canonical child preview before projectile Draft creation");
requireText(enemyPage, 'api.createRevision', "Enemies retain immutable Draft creation for projectileMode");
forbidText(enemyPage, 'api.publish(', "Enemies must not bypass History with direct publish");
forbidText(enemyPage, 'Canonical runtime consumer: Enemy spawn profile minimum-stage gate', "Enemies must not claim minStage has a production consumer");
forbidText(enemyPage, 'This takes effect only for a new game session after Publish.', "Enemies must not claim minStage preview data applies at runtime");
forbidText(enemyPage, 'gameplay snapshots Enemy admission', "Enemies must not claim gameplay snapshots migration-only admission data");

requireText(bossPage, 'createAssetTuningCapabilityState', "Bosses use shared A7 capability UI");
requireText(bossPage, 'label: "Name / Title"', "Bosses expose metadata capability state");
requireText(bossPage, 'status: "REQUIRES CANONICAL MIGRATION"', "Boss metadata is visibly migration-gated");
requireText(bossPage, 'label: "Phases / Mechanics"', "Bosses expose read-only combat ownership");
requireText(bossPage, 'status: "READ-ONLY REFERENCE"', "Boss production references remain read-only");
requireText(bossPage, 'label: "Rewards / Drops"', "Bosses expose unsupported reward binding");
requireText(bossPage, 'status: "DEFERRED / UNSUPPORTED"', "Boss reward authoring remains closed");
requireText(bossPage, 'badge("PREVIEW · NO RUNTIME APPLY"', "Boss page declares preview-only authority");
requireText(bossPage, 'void previewBosses(policy)', "Bosses retain canonical preview validation for preserved migration data");
forbidText(bossPage, 'api.createRevision', "Boss page must not create Drafts while no Boss write field has a production consumer");
forbidText(bossPage, 'api.publish(', "Boss page must not publish migration-only metadata");
forbidText(bossPage, 'Published Boss identity changes are snapshotted at the new-session boundary', "Bosses must not claim migration metadata is runtime-live");
forbidText(bossPage, 'current child contract exposes only canonical `name` and `title` consumers', "Bosses must not claim name/title production consumers exist");
forbidText(bossPage, 'gameplay snapshots Boss identity', "Bosses must not claim gameplay snapshots the Admin override");

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

console.log("Space Typing Admin A7 Enemies/Bosses capability audit: PASS — projectileMode is production-backed; Enemy minStage and Boss name/title are visibly migration-gated; Boss authoring is fail-closed until real production consumers exist.");
