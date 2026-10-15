import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const child = resolve(root, "games/space-typing");
const read = (path) => readFile(resolve(root, path), "utf8");
const readChild = (path) => readFile(resolve(child, path), "utf8");

const [
  capabilities,
  enemyPolicy,
  enemyPreview,
  enemyAssetPreview,
  enemyProjectilePolicy,
  enemyRegistry,
  worldRoster,
  bossPolicy,
  bossPreview,
  bossIdentity,
  enemyPage,
  enemyProductionPreview,
  bossWrapper,
  bossLegacy,
] = await Promise.all([
  readChild("src/admin/a7-enemy-boss-capabilities.ts"),
  readChild("src/admin/enemy-runtime-policy.ts"),
  readChild("src/admin/enemy-registry-preview.ts"),
  readChild("src/admin/enemy-asset-preview.ts"),
  readChild("src/combat/enemy-projectile-policy.ts"),
  readChild("src/enemies/registry.ts"),
  readChild("src/worlds/roster.ts"),
  readChild("src/admin/boss-runtime-policy.ts"),
  readChild("scripts/admin/boss-registry-preview.ts"),
  readChild("src/boss/identity.ts"),
  read("portal/src/admin/space-typing-enemies-phase-b.ts"),
  read("portal/src/admin/v2/preview/enemy-production-preview.ts"),
  read("portal/src/admin/space-typing-bosses-phase-b.ts"),
  read("portal/src/admin/space-typing-bosses-phase-b-legacy.ts"),
]);
const bossSurface = `${bossWrapper}\n${bossLegacy}`;

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
]) requireText(capabilities, `id: "${id}"`, `A7 capability ${id} is registered`);
for (const status of ["SUPPORTED NOW", "REQUIRES CANONICAL MIGRATION", "READ-ONLY REFERENCE", "DEFERRED / UNSUPPORTED"]) {
  requireText(capabilities, `status: "${status}"`, `A7 matrix preserves ${status}`);
}

requireText(enemyPolicy, "projectileMode: AdminEnemyProjectileMode | null", "Enemy runtime session carries projectileMode");
requireText(enemyPolicy, 'const POLICY_KEYS = new Set(["configRevision", "projectileMode", "enemies"])', "Enemy runtime policy accepts projectileMode");
requireText(enemyPolicy, "sanitizeProjectileMode(policy.projectileMode)", "Enemy runtime policy materializes projectileMode");
requireText(enemyProjectilePolicy, "ACTIVE_ENEMY_RUNTIME_SESSION", "Enemy projectile resolver reads active Admin session");
requireText(enemyProjectilePolicy, "resolveEnemyProjectileMode", "Enemy projectile policy exposes production resolver");
requireText(enemyProjectilePolicy, "normalEnemyProjectilesEnabled", "Enemy projectile policy exposes production consumer");
requireText(capabilities, 'productionConsumer: "src/combat/enemy-projectile-policy.ts::normalEnemyProjectilesEnabled() consumed by Game.ts"', "A7 records projectile production consumer");

requireText(enemyPolicy, "minStage?: number", "Enemy policy still preserves minStage migration data");
requireText(enemyPreview, "minStage: override?.minStage ?? base.minStage", "Enemy preview can materialize minStage candidate");
forbidText(enemyRegistry, "activeEnemyRuntimeOverride", "Bundled enemy registry must not be mistaken for Admin-aware admission resolver");
forbidText(worldRoster, "activeEnemyRuntimeOverride", "World roster must not be mistaken for consuming Enemy minStage override");
for (const token of ["rewardPower", "visual:", "spawnFx", "hitFx", "deathFx"]) requireText(enemyRegistry, token, `Enemy registry owns bundled ${token}`);

for (const token of [
  "enemyAssetPreviewPaintedKind",
  "hasPaintedEnemy",
  "production-painted-enemy",
  "must never silently",
  "pnpm art:prepare",
]) requireText(enemyAssetPreview, token, `Enemy production painted-art invariant ${token}`);
requireText(enemyAssetPreview, 'definitionId.endsWith(`-${kind}`)', "Enemy painted preview maps canonical family-kind IDs such as rainbow-scout");
requireText(enemyAssetPreview, "paintedEnemySprite(candidate.definition.family, candidate.paintedKind, \"high\")", "Enemy preview draws the exact prepared production painted asset");
forbidText(enemyAssetPreview, "production-painted-enemy-with-modular-fallback", "Painted-mapped Enemy preview must not advertise silent modular fallback");

requireText(bossPolicy, "name?: string", "Boss policy preserves name migration data");
requireText(bossPolicy, "title?: string", "Boss policy preserves title migration data");
requireText(bossPreview, 'authorableFields: ["name", "title"]', "Boss registry preview documents preserved envelope");
forbidText(bossIdentity, "activeBossRuntimeOverride", "bossIdentityForStage must not be mistaken for consuming Admin Boss metadata");
requireText(bossIdentity, "export function bossIdentityForStage", "Bundled Boss production identity resolver remains canonical");

for (const token of [
  "createAssetTuningCapabilityState",
  'label: "Normal Enemy Projectile Policy"',
  'label: "Minimum Stage"',
  'minStage.control.disabled = true',
  "const validated = await previewEnemies(policy)",
  "api.createRevision",
  "createEnemyProductionPreview",
]) requireText(enemyPage, token, `Enemy Admin evidence ${token}`);
forbidText(enemyPage, "api.publish(", "Enemy editor cannot bypass History with direct publish");
forbidText(enemyPage, "Canonical runtime consumer: Enemy spawn profile minimum-stage gate", "Enemy page must not invent minStage runtime ownership");

for (const token of [
  "canonical painted art resolved automatically",
  "Enemy art is resolved automatically by the child production renderer",
  "canonical child-owned art",
  "ProductionPreviewBridge.mount",
]) requireText(enemyProductionPreview, token, `Enemy production preview UX ${token}`);
forbidText(enemyProductionPreview, "createImageMediaCandidateTester", "Enemy primary preview must not ask administrators to choose a temporary image");
forbidText(enemyProductionPreview, "Choose candidate image", "Enemy primary preview must not expose candidate-image QA picker copy");
forbidText(enemyProductionPreview, "Media V2 tester", "Enemy primary preview must not present temporary Media QA as production art ownership");

requireText(bossWrapper, "renderLegacyBosses", "Boss wrapper retains established canonical inspector");
requireText(bossWrapper, "createBossProductionPreviewPanel", "Boss wrapper attaches production preview panel");
for (const token of [
  "createAssetTuningCapabilityState",
  'label: "Name / Title"',
  'label: "Phases / Mechanics"',
  'label: "Rewards / Drops"',
  'badge("PREVIEW · NO RUNTIME APPLY"',
  "void previewBosses(policy)",
]) requireText(bossSurface, token, `Boss composed surface evidence ${token}`);
requireText(bossSurface, 'status: "REQUIRES CANONICAL MIGRATION"', "Boss metadata remains migration-gated");
requireText(bossSurface, 'status: "READ-ONLY REFERENCE"', "Boss production mechanics remain read-only");
requireText(bossSurface, 'status: "DEFERRED / UNSUPPORTED"', "Boss reward binding remains closed");
forbidText(bossSurface, "api.createRevision", "Boss page must not create Drafts without a production identity consumer");
forbidText(bossSurface, "api.publish(", "Boss page must not publish migration-only metadata");
forbidText(bossSurface, "gameplay snapshots Boss identity", "Boss page must not claim migration data is runtime authority");

for (const fakeField of ["mediaAssetVersionId", "imageAssetVersionId", "modelAssetVersionId", "vfxAssetVersionId", "sfxAssetVersionId", "dropTableId", "rewardTableId", "phaseAssetVersionId"]) {
  forbidText(enemyPolicy, fakeField, `Enemy policy must not invent ${fakeField}`);
  forbidText(bossPolicy, fakeField, `Boss policy must not invent ${fakeField}`);
}

console.log("Space Typing Admin A7: PASS — Enemy projectile authoring remains production-backed; Enemy painted art is automatic/fail-closed instead of manual QA replacement; Boss preview ownership remains child production-backed.");
