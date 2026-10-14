import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const child = resolve(root, "games/space-typing");
const EXPECTED_CHILD_SHA = "8e1c3844faed0de1da721d8db8115712a56d311c";

const [
  capabilities,
  stagePolicy,
  stageRuntime,
  worldPolicy,
  worldRoster,
  routeRuntime,
  objectives,
  challenges,
  worldsPage,
  stagesPage,
  typingPage,
  router,
  capabilityUi,
] = await Promise.all([
  readFile(resolve(child, "src/admin/a8-world-stage-content-capabilities.ts"), "utf8"),
  readFile(resolve(child, "src/admin/stage-runtime-policy.ts"), "utf8"),
  readFile(resolve(child, "src/campaign/stage.ts"), "utf8"),
  readFile(resolve(child, "src/admin/world-runtime-policy.ts"), "utf8"),
  readFile(resolve(child, "src/worlds/roster.ts"), "utf8"),
  readFile(resolve(child, "src/campaign/route.ts"), "utf8"),
  readFile(resolve(child, "src/events/objectives.ts"), "utf8"),
  readFile(resolve(child, "src/expansion-v2/challenge.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-worlds-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-stages-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-typing-content-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-a8-world-stage-capabilities.ts"), "utf8"),
]);

function requireText(source, needle, label) {
  assert.ok(source.includes(needle), `${label}: expected ${JSON.stringify(needle)}`);
}
function forbidText(source, needle, label) {
  assert.ok(!source.includes(needle), `${label}: forbidden ${JSON.stringify(needle)}`);
}

const childHead = execFileSync("git", ["-C", child, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();
assert.equal(childHead, EXPECTED_CHILD_SHA, `A8 authority audit is stale: audited=${EXPECTED_CHILD_SHA} pinned-child=${childHead}`);

for (const id of [
  "world.enemy-roster",
  "world.structure-presentation-rewards",
  "stage.gameplay-tuning",
  "route.graph",
  "objective.definition",
  "challenge.daily-weekly-identity",
  "typing.catalog-reference",
  "typing.stage-assignment",
  "world.media-reward-relationship-authoring",
]) {
  requireText(capabilities, `id: "${id}"`, `A8 capability ${id} is registered`);
}
for (const status of ["SUPPORTED NOW", "READ-ONLY REFERENCE", "DEFERRED / UNSUPPORTED"]) {
  requireText(capabilities, `status: "${status}"`, `A8 matrix uses ${status}`);
}

// Stage authority: only the three validated tuning fields reach production.
for (const field of ["enemyBudget", "eliteChance", "modifierSlots"]) {
  requireText(stagePolicy, field, `Stage policy owns ${field}`);
  requireText(stagesPage, field, `Stage Admin exposes ${field}`);
}
requireText(stageRuntime, 'import { activeStageRuntimeOverride } from "../admin/stage-runtime-policy"', "Production Stage factory reads the published Admin session");
requireText(stageRuntime, "export function createStageConfig(", "Production Stage factory remains the canonical entry point");
requireText(stageRuntime, "activeStageRuntimeOverride(normalizeStage(stage))", "Production Stage factory resolves the active override");
requireText(stageRuntime, "return resolveStageConfig(createBundledStageConfigInternal(stage), override);", "Production Stage factory applies validated override fields");
requireText(stageRuntime, "export function createBundledStageConfig(stage: number)", "Admin preview keeps a bundled baseline");
requireText(stageRuntime, "return createBundledStageConfigInternal(stage);", "Bundled preview baseline does not recursively consume active runtime policy");
requireText(stagePolicy, "materializeStageRuntimeSessionSnapshot", "Stage policy validates frozen Expedition snapshots");
requireText(stagePolicy, "captureActiveStageRuntimeSession", "Stage policy exposes immutable page-session capture for new Expedition runs");
requireText(stagePolicy, "activateExpeditionStageRuntimeSession", "Stage policy exposes an explicit Expedition override boundary");
requireText(stagePolicy, "expeditionStageRuntimeSession = null", "Expedition override is one-shot and cannot leak into normal Campaign stage creation");
requireText(stagesPage, "/api/admin/space-typing/stages/preview", "Stage Admin validates through canonical child preview");
requireText(stagesPage, "api.createRevision", "Stage Admin uses immutable Draft creation");
forbidText(stagesPage, "api.publish(", "Stage Admin cannot direct-publish");
requireText(stagesPage, "Reload this screen before saving to avoid overwriting newer published changes", "Stage Admin has stale-active protection");

// World authority: enemyRoster is resolved before production selection.
requireText(worldPolicy, 'const AUTHORABLE_KEYS = new Set(["enemyRoster"])', "World policy exposes only enemyRoster");
requireText(worldRoster, "activeWorldRuntimeOverride", "Production World roster reads the published Admin session");
requireText(worldRoster, "resolveWorldProfileForRuntime", "Production World roster uses the canonical runtime resolver");
requireText(worldRoster, "export function worldProfileForRuntimeStage(", "Production World authority helper exists");
requireText(worldRoster, "worldProfileForRuntimeStage(stage)", "Production spawn path resolves effective World before selection");
requireText(worldsPage, "/api/admin/space-typing/worlds/preview", "World Admin validates through canonical child preview");
requireText(worldsPage, "enemyRoster", "World Admin exposes the supported roster field");
requireText(worldsPage, "api.createRevision", "World Admin uses immutable Draft creation");
forbidText(worldsPage, "api.publish(", "World Admin cannot direct-publish");
requireText(worldsPage, "Reload this screen before saving to avoid overwriting newer published changes", "World Admin has stale-active protection");

requireText(router, 'attachA8WorldStageCapabilitySummary(renderPhaseBWorlds(navigate), "world")', "World Roster route carries the A8 capability summary");
requireText(router, 'attachA8WorldStageCapabilitySummary(renderPhaseBStages(navigate), "stage")', "Stage Overrides route carries the A8 capability summary");
requireText(worldsPage, 'navigate("/admin/space-typing/worlds-stages")', "World editor links to Stage editor");
requireText(stagesPage, 'navigate("/admin/space-typing/stages")', "Stage editor links to World editor");
for (const label of ["World Enemy Roster", "Stage Gameplay Tuning", "Routes", "Objectives", "Daily / Weekly Challenges", "Typing Assignment"]) {
  requireText(capabilityUi, label, `A8 UI surfaces ${label}`);
}
requireText(capabilityUi, "AUTHORITY VERIFIED", "A8 UI declares verified authority boundary");
requireText(capabilityUi, "READ-ONLY REFERENCE", "A8 UI visibly marks read-only adjacent systems");
requireText(capabilityUi, "DEFERRED / UNSUPPORTED", "A8 UI visibly marks unsupported Typing assignment");
requireText(capabilityUi, "World Music, Backgrounds and Rewards remain separate canonical Admin domains", "A8 UI preserves dedicated domain ownership");

requireText(routeRuntime, "export function createRouteGraph(", "Routes stay deterministic runtime state");
requireText(routeRuntime, "export function isValidRouteGraph(", "Routes retain runtime validation");
requireText(objectives, "export function objectiveForStage(", "Objectives stay code-derived from Stage/Difficulty");
requireText(challenges, "export function dailySeed(", "Daily challenge identity stays deterministic");
requireText(challenges, "export function weeklyChallengeIdentity(", "Weekly challenge identity stays deterministic");
requireText(typingPage, "Editing is intentionally disabled here", "Typing Content remains canonical read/reference only");
forbidText(typingPage, "api.createRevision", "Typing Content cannot create fake Stage assignment Drafts");

for (const fakeField of [
  "routeGraph",
  "objectiveType",
  "objectiveRewardFactor",
  "challengeSeed",
  "challengeSchedule",
  "typingContentId",
  "vocabularyAssignmentId",
  "typingTextAssignmentId",
]) {
  forbidText(stagePolicy, fakeField, `Stage policy must not invent ${fakeField}`);
  forbidText(worldPolicy, fakeField, `World policy must not invent ${fakeField}`);
}

console.log(`Space Typing Admin A8 World/Stage content authority audit: PASS · child ${childHead.slice(0, 12)} · World roster + Stage tuning production-backed; Expedition consumes frozen Stage snapshots; Routes/Objectives/Challenges/Typing assignment remain read-only/deferred.`);
