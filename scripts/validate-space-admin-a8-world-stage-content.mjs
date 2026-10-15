import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const child = resolve(root, "games/space-typing");
// A8 authority re-audit: dcba99b..f8b74d0 changes only the child Enemy
// Admin production-preview painted-art resolution/fallback behavior. World/Stage
// capability, policy and runtime ownership files are unchanged.
const EXPECTED_CHILD_SHA = "f8b74d0fe3a52d5b0d2cbc9fbfcb78509edc677b";
const read = (path) => readFile(resolve(root, path), "utf8");
const readChild = (path) => readFile(resolve(child, path), "utf8");

const [
  capabilities,
  stagePolicy,
  stageRuntime,
  worldPolicy,
  worldRoster,
  routeRuntime,
  objectives,
  challenges,
  worldsWrapper,
  worldsLegacy,
  stagesWrapper,
  stagesLegacy,
  typingPage,
  router,
  capabilityUi,
] = await Promise.all([
  readChild("src/admin/a8-world-stage-content-capabilities.ts"),
  readChild("src/admin/stage-runtime-policy.ts"),
  readChild("src/campaign/stage.ts"),
  readChild("src/admin/world-runtime-policy.ts"),
  readChild("src/worlds/roster.ts"),
  readChild("src/campaign/route.ts"),
  readChild("src/events/objectives.ts"),
  readChild("src/expansion-v2/challenge.ts"),
  read("portal/src/admin/space-typing-worlds-phase-b.ts"),
  read("portal/src/admin/space-typing-worlds-phase-b-legacy.ts"),
  read("portal/src/admin/space-typing-stages-phase-b.ts"),
  read("portal/src/admin/space-typing-stages-phase-b-legacy.ts"),
  read("portal/src/admin/space-typing-typing-content-phase-b.ts"),
  read("portal/src/admin/space-typing-phase-b.ts"),
  read("portal/src/admin/space-typing-a8-world-stage-capabilities.ts"),
]);
const worldsSurface = `${worldsWrapper}\n${worldsLegacy}`;
const stagesSurface = `${stagesWrapper}\n${stagesLegacy}`;

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
]) requireText(capabilities, `id: "${id}"`, `A8 capability ${id} is registered`);
for (const status of ["SUPPORTED NOW", "READ-ONLY REFERENCE", "DEFERRED / UNSUPPORTED"]) {
  requireText(capabilities, `status: "${status}"`, `A8 matrix preserves ${status}`);
}

for (const field of ["enemyBudget", "eliteChance", "modifierSlots"]) {
  requireText(stagePolicy, field, `Stage policy owns ${field}`);
  requireText(stagesSurface, field, `Stage Admin exposes ${field}`);
}
requireText(stageRuntime, 'import { activeStageRuntimeOverride } from "../admin/stage-runtime-policy"', "Production Stage factory reads published Admin session");
requireText(stageRuntime, "export function createStageConfig(", "Production Stage factory remains canonical entry point");
requireText(stageRuntime, "activeStageRuntimeOverride(normalizeStage(stage))", "Production Stage factory resolves active override");
requireText(stageRuntime, "return resolveStageConfig(createBundledStageConfigInternal(stage), override);", "Production Stage factory applies validated override fields");
requireText(stageRuntime, "export function createBundledStageConfig(stage: number)", "Admin preview retains bundled baseline");
requireText(stagePolicy, "materializeStageRuntimeSessionSnapshot", "Stage policy validates frozen Expedition snapshots");
requireText(stagePolicy, "captureActiveStageRuntimeSession", "Stage policy exposes immutable page-session capture");
requireText(stagePolicy, "activateExpeditionStageRuntimeSession", "Stage policy exposes explicit Expedition boundary");
requireText(stagePolicy, "expeditionStageRuntimeSession = null", "Expedition override cannot leak into normal Campaign creation");

requireText(stagesWrapper, "renderLegacyStages", "Stage wrapper retains established editor");
requireText(stagesWrapper, "createStageProductionPreviewPanel", "Stage wrapper attaches child production composition preview");
requireText(stagesSurface, "/api/admin/space-typing/stages/preview", "Stage Admin validates through canonical child preview");
requireText(stagesSurface, "api.createRevision", "Stage Admin uses immutable Draft creation");
forbidText(stagesSurface, "api.publish(", "Stage Admin cannot direct-publish");
requireText(stagesSurface, "Reload this screen before saving to avoid overwriting newer published changes", "Stage Admin retains stale-active protection");

requireText(worldPolicy, 'const AUTHORABLE_KEYS = new Set(["enemyRoster"])', "World policy exposes only enemyRoster");
requireText(worldRoster, "activeWorldRuntimeOverride", "Production World roster reads published Admin session");
requireText(worldRoster, "resolveWorldProfileForRuntime", "Production World roster uses canonical runtime resolver");
requireText(worldRoster, "export function worldProfileForRuntimeStage(", "Production World authority helper exists");
requireText(worldRoster, "worldProfileForRuntimeStage(stage)", "Production spawn path resolves effective World before selection");
requireText(worldsWrapper, "renderLegacyWorlds", "World wrapper retains established editor");
requireText(worldsWrapper, "createWorldProductionPreviewPanel", "World wrapper attaches child production environment preview");
requireText(worldsSurface, "/api/admin/space-typing/worlds/preview", "World Admin validates through canonical child preview");
requireText(worldsSurface, "enemyRoster", "World Admin exposes supported roster field");
requireText(worldsSurface, "api.createRevision", "World Admin uses immutable Draft creation");
forbidText(worldsSurface, "api.publish(", "World Admin cannot direct-publish");
requireText(worldsSurface, "Reload this screen before saving to avoid overwriting newer published changes", "World Admin retains stale-active protection");

requireText(router, 'attachA8WorldStageCapabilitySummary(renderPhaseBWorlds(navigate), "world")', "World route carries A8 capability summary");
requireText(router, 'attachA8WorldStageCapabilitySummary(renderPhaseBStages(navigate), "stage")', "Stage route carries A8 capability summary");
requireText(worldsSurface, 'navigate("/admin/space-typing/worlds-stages")', "World editor links to Stage editor");
requireText(stagesSurface, 'navigate("/admin/space-typing/stages")', "Stage editor links to World editor");
for (const label of ["World Enemy Roster", "Stage Gameplay Tuning", "Routes", "Objectives", "Daily / Weekly Challenges", "Typing Assignment"]) {
  requireText(capabilityUi, label, `A8 UI surfaces ${label}`);
}
requireText(capabilityUi, "AUTHORITY VERIFIED", "A8 UI declares verified authority boundary");
requireText(capabilityUi, "READ-ONLY REFERENCE", "A8 UI visibly marks read-only adjacent systems");
requireText(capabilityUi, "DEFERRED / UNSUPPORTED", "A8 UI visibly marks unsupported Typing assignment");
requireText(capabilityUi, "World Music, Backgrounds and Rewards remain separate canonical Admin domains", "A8 preserves dedicated domain ownership");

requireText(routeRuntime, "export function createRouteGraph(", "Routes stay deterministic runtime state");
requireText(routeRuntime, "export function isValidRouteGraph(", "Routes retain runtime validation");
requireText(objectives, "export function objectiveForStage(", "Objectives stay code-derived from Stage/Difficulty");
requireText(challenges, "export function dailySeed(", "Daily challenge identity stays deterministic");
requireText(challenges, "export function weeklyChallengeIdentity(", "Weekly challenge identity stays deterministic");
requireText(typingPage, "Editing is intentionally disabled here", "Typing Content remains canonical read/reference only");
forbidText(typingPage, "api.createRevision", "Typing Content cannot create fake Stage assignment Drafts");

for (const fakeField of ["routeGraph", "objectiveType", "objectiveRewardFactor", "challengeSeed", "challengeSchedule", "typingContentId", "vocabularyAssignmentId", "typingTextAssignmentId"]) {
  forbidText(stagePolicy, fakeField, `Stage policy must not invent ${fakeField}`);
  forbidText(worldPolicy, fakeField, `World policy must not invent ${fakeField}`);
}

console.log(`Space Typing Admin A8: PASS · child ${childHead.slice(0, 12)} · World roster/Stage tuning remain production-backed while A10.5 adds child-owned World/Stage rendering; adjacent Routes/Objectives/Challenges/Typing remain read-only/deferred.`);
