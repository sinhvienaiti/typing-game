import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");
const contract = JSON.parse(await read("portal/src/admin/contracts/space-typing-admin.v1.json"));
const [missionSource, saveSource, objectiveSource, mainSource, gameSource, childAudit, childCi, uiSource, routerSource, dailyWeeklySource] = await Promise.all([
  read("games/space-typing/src/progression/missions.ts"),
  read("games/space-typing/src/persistence/player-save.ts"),
  read("games/space-typing/src/events/objectives.ts"),
  read("games/space-typing/src/main.ts"),
  read("games/space-typing/src/Game.ts"),
  read("games/space-typing/scripts/audit-admin-missions.ts"),
  read("games/space-typing/.github/workflows/ci.yml"),
  read("portal/src/admin/space-typing-missions-phase-b.ts"),
  read("portal/src/admin/space-typing-phase-b.ts"),
  read("portal/src/admin/space-typing-daily-weekly-phase-b.ts"),
]);

const missions = contract.missions;
const expectedMissionIds = ["clear-5", "clear-25", "accuracy-98x3", "shop-5", "drops-10"];
const expectedCounters = ["stageClears", "highAccuracyClears", "shopPurchases", "equipmentDrops"];
const expectedObjectiveTypes = ["survive", "accuracy", "no-miss", "protect", "commander-first", "marked-target", "elite-hunt", "speed-clear"];

assert(contract.capabilities.includes("missions.read"), "Missions contract must expose missions.read");
assert(!contract.capabilities.includes("missions.write"), "Missions authoring must stay closed while definitions are code-owned");
assert(!contract.capabilities.includes("missions.preview"), "Missions preview must stay closed without a canonical preview service");
assert(contract.routes.some((route) => route.id === "missions" && route.path === "/admin/space-typing/missions"), "Missions route missing from child contract");
assert.equal(missions.mode, "runtime-derived-readonly");
assert.deepEqual(missions.domains, ["progression-missions", "stage-objectives"]);
assert.deepEqual(missions.authorableFields, []);
assert.deepEqual(missions.missionIds, expectedMissionIds);
assert.deepEqual(missions.missionCounterKeys, expectedCounters);
assert.deepEqual(missions.stageObjectiveTypes, expectedObjectiveTypes);
assert.equal(missions.missionPersistenceOwner, "PlayerSave.progression");
assert.equal(missions.stageObjectivePersistenceOwner, "stage-session-runtime-only");
assert.deepEqual(missions.gameplayConsumers, ["src/main.ts", "src/Game.ts"]);
assert.deepEqual(missions.rewardIntegration, ["claimMission.rewardCredits", "objectiveRewardFactor"]);
assert.equal(missions.recurringMissionDefinitions, false);
assert.equal(missions.dailyWeeklyAuthoring, false);
assert.equal(missions.writeCapability, false);
assert.equal(missions.previewCapability, false);
assert.deepEqual(missions.unsupportedMasterPlanFields, ["dailyReset", "weeklyReset", "rotationCalendar", "rewardPool"]);

for (const id of expectedMissionIds) {
  assert(missionSource.includes(`\"${id}\"`), `Canonical progression mission missing: ${id}`);
}
for (const symbol of ["MISSION_REGISTRY", "createProgressionState", "recordProgressionEvent", "missionProgress", "missionClaimable", "claimMission", "syncAchievements"]) {
  assert(missionSource.includes(symbol), `Missing canonical progression mission runtime evidence ${symbol}`);
}
for (const counter of expectedCounters) {
  assert(missionSource.includes(counter), `Canonical progression counter missing: ${counter}`);
}
assert(saveSource.includes("progression: ProgressionState"), "PlayerSave must persist progression state");
assert(saveSource.includes("progression:"), "PlayerSave runtime must serialize progression state");
for (const type of expectedObjectiveTypes) {
  assert(objectiveSource.includes(`\"${type}\"`), `Canonical Stage Objective type missing: ${type}`);
}
assert(mainSource.includes("MISSION_REGISTRY"), "main.ts must consume canonical progression missions");
assert(gameSource.includes("objectiveForStage") || gameSource.includes("objectiveRewardFactor"), "Game.ts must consume canonical Stage Objective runtime");
assert(childAudit.includes("claimMission"), "Child Missions audit must exercise canonical mission claiming");
assert(childAudit.includes("Space Typing Admin Missions audit OK"), "Child Missions audit success marker missing");
assert(childCi.includes("Audit Missions contract") && childCi.includes("pnpm missions:audit"), "Child CI must run Missions audit");

assert(uiSource.includes("/api/admin/space-typing/contract"), "Missions UI must read the authenticated child contract");
assert(uiSource.includes("Progression Missions"), "Missions UI must expose canonical progression missions");
assert(uiSource.includes("Stage Objectives"), "Missions UI must expose canonical stage objectives");
assert(uiSource.includes("PlayerSave.progression") || uiSource.includes("missionPersistenceOwner"), "Missions UI must expose progression persistence ownership");
assert(uiSource.includes("RUNTIME-BACKED · READ ONLY"), "Missions UI must make the read-only boundary explicit");
assert(uiSource.includes('button("Daily / Weekly"'), "Missions UI must link to the canonical Daily / Weekly runtime-boundary screen");
assert(!uiSource.includes("UI mock"), "Missions UI must not label Daily / Weekly as a mock surface");
assert(!uiSource.includes("api.createRevision"), "Missions UI must not create config revisions");
assert(!uiSource.includes("api.publish"), "Missions UI must not publish config revisions");
assert(!uiSource.includes('button("Save Draft"'), "Missions UI must not render Save Draft");
assert(routerSource.includes("renderPhaseBMissions") && routerSource.includes("`${BASE}/missions`"), "Missions renderer route is not wired");

assert(dailyWeeklySource.includes("/api/admin/space-typing/daily-weekly/contract"), "Daily / Weekly must read the authenticated canonical sidecar contract");
assert(dailyWeeklySource.includes("DAILY · RUNTIME-BACKED"), "Daily / Weekly must expose canonical Daily runtime ownership");
assert(dailyWeeklySource.includes("WEEKLY · NOT IMPLEMENTED"), "Daily / Weekly must expose explicit Weekly runtime absence");
assert(dailyWeeklySource.includes("No synthetic live-ops authoring"), "Daily / Weekly must explain the no-authoring boundary");
assert(!dailyWeeklySource.includes("+ New Rotation"), "Daily / Weekly runtime-boundary UI must not expose fake authoring actions");

console.log("Space Typing Missions Admin validation passed: progression missions + Stage Objectives match canonical runtime; Daily/Weekly links to the canonical partial read-only boundary.");
