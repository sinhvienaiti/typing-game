import { readFile } from "node:fs/promises";

const paths = {
  classification: "portal/src/admin/v2/preview/preview-classification.ts",
  combatVfx: "portal/src/admin/v2/preview/panels/combat-vfx-production-preview.ts",
  environments: "portal/src/admin/v2/preview/panels/world-stage-production-preview.ts",
  systems: "portal/src/admin/v2/preview/panels/system-runtime-preview.ts",
  equipment: "portal/src/admin/v2/preview/panels/equipment-runtime-preview.ts",
  productionIcon: "portal/src/admin/v2/preview/production-registry-icon.ts",
  enemyPanel: "portal/src/admin/v2/preview/enemy-production-preview.ts",
  bossPanel: "portal/src/admin/v2/preview/panels/boss-production-preview.ts",
  mediaTester: "portal/src/admin/v2/media-candidate-preview.ts",
  shipFacade: "portal/src/admin/space-typing-asset-preview.ts",
  router: "portal/src/admin/space-typing-phase-b.ts",
  vfxPage: "portal/src/admin/space-typing-vfx-phase-b.ts",
  childHost: "games/space-typing/src/admin/asset-preview-main.ts",
  childEnemy: "games/space-typing/src/admin/enemy-asset-preview.ts",
  childBoss: "games/space-typing/src/admin/boss-asset-preview.ts",
  childWorldStage: "games/space-typing/src/admin/world-stage-asset-preview.ts",
  childShots: "games/space-typing/src/vfx/player-shots.ts",
  childWorldRenderer: "games/space-typing/src/worlds/scene-renderer.ts",
};

const source = Object.fromEntries(await Promise.all(
  Object.entries(paths).map(async ([key, path]) => [key, await readFile(new URL(`../${path}`, import.meta.url), "utf8")]),
));

function requireText(input, needle, label) {
  if (!input.includes(needle)) throw new Error(`${label}: expected ${JSON.stringify(needle)}`);
}
function forbidText(input, needle, label) {
  if (input.includes(needle)) throw new Error(`${label}: forbidden ${JSON.stringify(needle)}`);
}

forbidText(source.childEnemy, "drawModularEnemy", "Enemy Admin preview must never silently fall back to the generic modular/base renderer");
forbidText(source.childEnemy, "StaticEnemyBodyCache", "Enemy Admin preview must not retain modular-body fallback state");
requireText(source.childEnemy, "paintedEnemySprite", "Enemy preview resolves prepared production painted art for canonical registry identities");
requireText(source.childEnemy, "hasPaintedEnemy", "Enemy preview fails closed when mapped painted art is absent from the build");
requireText(source.childEnemy, "drawPaintedSprite", "Enemy preview draws painted art through the production sprite renderer");
requireText(source.childEnemy, "PREVIEW_KIND_BY_ID", "Enemy preview owns explicit presentation mapping for registry ids that do not encode a runtime kind");
requireText(source.childEnemy, "PREVIEW_KIND_BY_ROLE", "Enemy preview has a deterministic role-backed painted presentation fallback");
requireText(source.childEnemy, "admin-presentation-only", "Enemy registry-to-painted mapping is explicitly presentation-only rather than gameplay authority");
requireText(source.childEnemy, "never silently falls back", "Enemy painted mappings cannot silently degrade to a modular body");
requireText(source.childEnemy, "new CombatFxSystem()", "Enemy hit/death reuses production CombatFxSystem");
requireText(source.childBoss, "drawPaintedSprite", "Boss preview reuses painted production renderer");
requireText(source.childBoss, "bossPhase", "Boss phase preview uses production CombatFxSystem");
requireText(source.childBoss, "setScenario(next", "Boss child scene owns scenario transitions without requiring candidate reload");
requireText(source.childWorldStage, "WorldSceneRenderer", "World/Stage preview reuses production WorldSceneRenderer");
requireText(source.childWorldStage, "worldForStage", "Stage preview resolves canonical production world mapping");
requireText(source.childWorldRenderer, "export class WorldSceneRenderer", "canonical production WorldSceneRenderer remains available");
requireText(source.environments, "ProductionPreviewBridge.mount", "World/Stage panels use shared isolated bridge");
forbidText(source.environments, "CanvasRenderingContext2D", "Parent World/Stage panel must not implement a renderer");

requireText(source.combatVfx, "shipProductionPreviewAdapter", "VFX panel delegates to existing Ship production adapter");
requireText(source.combatVfx, 'active.setScenario("fire")', "VFX panel exercises production fire scenario");
requireText(source.combatVfx, "api.previewShips()", "VFX context comes from canonical Ship preview data");
requireText(source.childHost, "new PlayerShotSystem<number>()", "child preview owns production PlayerShotSystem");
requireText(source.childHost, "shots.fire({", "child fire scenario uses production projectile simulation");
requireText(source.childHost, "new Sfx()", "child fire preview uses production Sfx path");
requireText(source.childHost, "AssetPreviewMutationQueue", "child Ship preview serializes async candidate/tuning mutations");
requireText(source.childHost, 'code: "STALE_PREVIEW_COMMAND"', "child preview marks superseded commands explicitly");
requireText(source.childShots, "export class PlayerShotSystem", "production projectile system remains first-class");
forbidText(source.combatVfx, "CanvasRenderingContext2D", "Parent VFX panel must not implement a second effects renderer");
requireText(source.vfxPage, "createCombatVfxProductionPreviewPanel", "VFX first-class page exposes production combat preview");

requireText(source.shipFacade, "private latestCandidate", "Ships facade tracks the latest production candidate operation");
requireText(source.shipFacade, "this.latestCandidate = operation", "Ships facade updates candidate ordering on every load");
requireText(source.shipFacade, "await this.latestCandidate", "Ships scenario/tuning waits for candidate materialization");

requireText(source.bossPanel, "let latestCandidate: Promise<unknown> = Promise.resolve()", "Boss preview tracks the latest production candidate operation");
requireText(source.bossPanel, "latestCandidate = operation", "Boss preview updates candidate ordering before awaiting materialization");
requireText(source.bossPanel, "await latestCandidate", "Boss scenario transitions wait for candidate materialization");
requireText(source.bossPanel, 'scenario.control.addEventListener("change", () => void applyScenario().catch(reportError))', "Boss scenario changes use the dedicated scenario command path");
forbidText(source.bossPanel, 'scenario.control.addEventListener("change", () => void loadSelectedBoss()', "Boss scenario changes must not reload the candidate");
requireText(source.bossPanel, "st-admin-production-preview-shell--hero", "Boss production preview keeps the renderer as the primary hero surface");
requireText(source.bossPanel, "st-admin-preview-media-tools", "Boss Media candidate QA remains a secondary collapsible tool");

requireText(source.bossPanel, "createImageMediaCandidateTester", "Boss preview retains the separate preview-only Media V2 QA tester while Boss media binding is migration-gated");
forbidText(source.enemyPanel, "createImageMediaCandidateTester", "Enemy primary production preview must resolve canonical child art automatically");
forbidText(source.enemyPanel, "Choose candidate image", "Enemy primary production preview must not ask administrators to choose a temporary image");
requireText(source.enemyPanel, "canonical painted art resolved automatically", "Enemy Admin explains automatic child-owned painted-art resolution");
requireText(source.mediaTester, 'allowedKinds: ["image"]', "Media candidate tester remains image-only for domains that still expose the separate QA surface");
requireText(source.mediaTester, "preview-only", "Media candidate tester clearly marks temporary QA semantics");
requireText(source.mediaTester, "MediaAdminApi", "Media candidate tester resolves exact Media V2 preview bytes through the canonical Admin media API");

requireText(source.systems, '"/api/admin/space-typing/skills/preview"', "Skill preview uses canonical preview endpoint");
requireText(source.systems, "production SkillEngine", "Skill UI states production engine ownership");
requireText(source.systems, "let previewGeneration = 0", "Skill draft preview has independent latest-request-wins generation control");
requireText(source.systems, "const current = ++previewGeneration", "Skill draft preview advances only the preview generation");
requireText(source.systems, "if (current !== previewGeneration) return", "Skill preview ignores stale draft responses");
requireText(source.systems, "scheduleDraftPreview", "Skill draft inputs drive debounced live runtime preview");
requireText(source.systems, 'createProductionRegistryIconPreview("skill")', "Skill preview pairs production runtime behavior with canonical child-painted visual");
requireText(source.systems, "selectSkill", "Skill live preview exposes selection synchronization for the authoring registry");
requireText(source.equipment, '"/api/admin/space-typing/equipment/preview"', "Equipment preview uses canonical preview endpoint");
requireText(source.equipment, "MULTIPLIER_EFFECTS", "Equipment effect baseline distinguishes neutral multipliers from active count=1 effects");
requireText(source.equipment, "Nothing was persisted", "Equipment Draft preview remains isolated");
requireText(source.equipment, "let previewGeneration = 0", "Equipment draft preview has independent latest-request-wins generation control");
requireText(source.equipment, "const current = ++previewGeneration", "Equipment draft preview advances only the preview generation");
requireText(source.equipment, "if (current !== previewGeneration) return", "Equipment preview ignores stale draft responses");
requireText(source.equipment, "scheduleDraftPreview", "Equipment draft inputs drive debounced live runtime preview");
requireText(source.equipment, 'createProductionRegistryIconPreview("equipment")', "Equipment preview pairs production resolver behavior with canonical child-painted visual");
requireText(source.equipment, "selectEquipment", "Equipment live preview exposes selection synchronization for the authoring registry");
for (const token of ["paintedSkillIcon", "paintedEquipmentIcon", "CHILD ASSET · READ ONLY"]) {
  requireText(source.productionIcon, token, `Skill/Equipment production visual helper ${token}`);
}

for (const kind of ["full-runtime", "production-presentation", "simulation-data", "not-applicable"]) {
  requireText(source.classification, `kind: "${kind}"`, `classification ${kind} exists`);
}
for (const route of [
  "/admin/space-typing/audio",
  "/admin/space-typing/world-music",
  "/admin/space-typing/sfx",
  "/admin/space-typing/ships",
  "/admin/space-typing/equipment",
  "/admin/space-typing/skills",
  "/admin/space-typing/enemies",
  "/admin/space-typing/bosses",
  "/admin/space-typing/stages",
  "/admin/space-typing/worlds-stages",
  "/admin/space-typing/vfx",
  "/admin/space-typing/shop",
  "/admin/space-typing/currencies",
  "/admin/space-typing/rewards",
  "/admin/space-typing/events",
  "/admin/space-typing/duel",
  "/admin/space-typing/ranked",
  "/admin/space-typing/settings",
  "/admin/space-typing/feature-gates",
  "/admin/space-typing/typing-content",
  "/admin/space-typing/history",
  "/admin/space-typing/qa",
]) {
  requireText(source.classification, `"${route}"`, `preview strategy is explicit for ${route}`);
}
requireText(source.router, "attachProductionPreviewClassification", "classification is attached at the first-class router");

console.log("Space Typing Admin A10.5 production preview core coverage + classification validation passed.");
