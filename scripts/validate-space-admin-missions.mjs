import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");
const contract = JSON.parse(await read("portal/src/admin/contracts/space-typing-admin.v1.json"));
const [objectiveSource, gameSource, childAudit, childCi, uiSource, routerSource, dailyWeeklySource, phaseMapSource] = await Promise.all([
  read("games/space-typing/src/events/objectives.ts"),
  read("games/space-typing/src/Game.ts"),
  read("games/space-typing/scripts/audit-admin-missions.ts"),
  read("games/space-typing/.github/workflows/ci.yml"),
  read("portal/src/admin/space-typing-missions-phase-b.ts"),
  read("portal/src/admin/space-typing-phase-b.ts"),
  read("portal/src/admin/space-typing-daily-weekly.ts"),
  read("admin/space-typing-phase-b-map.v1.json"),
]);

const missions = contract.missions;
const expectedTypes = [
  "survive",
  "accuracy",
  "no-miss",
  "protect",
  "commander-first",
  "marked-target",
  "elite-hunt",
  "speed-clear",
];

assert(contract.capabilities.includes("missions.read"), "Missions contract must expose missions.read");
assert(!contract.capabilities.includes("missions.write"), "Missions authoring must stay closed without a canonical runtime seam");
assert(!contract.capabilities.includes("missions.preview"), "Missions preview must stay closed without a canonical runtime seam");
assert(contract.routes.some((route) => route.id === "missions" && route.path === "/admin/space-typing/missions"), "Missions route missing from child contract");
assert.equal(missions.mode, "runtime-derived-readonly");
assert.deepEqual(missions.authorableFields, []);
assert.deepEqual(missions.objectiveTypes, expectedTypes);
assert.equal(missions.selectionOwner, "objectiveForStage");
assert.equal(missions.gameplayConsumer, "src/Game.ts");
assert.equal(missions.rewardIntegration, "objectiveRewardFactor");
assert.equal(missions.persistenceOwner, "stage-session-runtime-only");
assert.equal(missions.recurringMissionDefinitions, false);
assert.equal(missions.dailyWeeklyAuthoring, false);
assert.equal(missions.writeCapability, false);
assert.equal(missions.previewCapability, false);
assert.deepEqual(missions.unsupportedMasterPlanFields, ["missionDefinition", "dailyReset", "weeklyReset", "rotationCalendar", "rewardPool"]);

for (const symbol of [
  "STAGE_OBJECTIVE_TYPES",
  "StageObjectiveDefinition",
  "StageObjectiveState",
  "objectiveForStage",
  "createStageObjectiveState",
  "reduceStageObjective",
  "objectiveForcesCommander",
  "objectiveForcesElite",
  "requiredObjectiveAllowsFinish",
  "objectiveProgressText",
  "objectiveRewardFactor",
]) {
  assert(objectiveSource.includes(symbol), `Missing canonical Stage Objective runtime evidence ${symbol}`);
}
for (const type of expectedTypes) {
  assert(objectiveSource.includes(`\"${type}\"`), `Canonical Stage Objective type missing: ${type}`);
}
assert(gameSource.includes("objectiveForStage") || gameSource.includes("objectiveRewardFactor"), "Game.ts must consume canonical Stage Objective runtime");
assert(childAudit.includes("Space Typing Admin Missions audit OK"), "Child Missions audit script missing expected success marker");
assert(childCi.includes("Audit Missions contract"), "Child CI must run the Missions contract audit");
assert(childCi.includes("pnpm missions:audit"), "Child CI must execute pnpm missions:audit");

assert(uiSource.includes("/api/admin/space-typing/contract"), "Missions UI must read the authenticated canonical child contract");
assert(uiSource.includes("RUNTIME-BACKED · READ ONLY"), "Missions UI must make its read-only boundary explicit");
assert(uiSource.includes("Runtime Objective Types"), "Missions UI must expose canonical objective types");
assert(uiSource.includes("Selection & Reward Integration"), "Missions UI must expose gameplay ownership");
assert(uiSource.includes("Admin Boundary"), "Missions UI must explain unsupported recurring authoring");
assert(uiSource.includes("Daily / Weekly (UI mock)"), "Missions UI must label Daily / Weekly as mock when linking to it");
assert(!uiSource.includes("api.createRevision"), "Missions UI must not create config revisions");
assert(!uiSource.includes("api.publish"), "Missions UI must not publish config revisions");
assert(!uiSource.includes('button("Save Draft"'), "Missions UI must not render a Save Draft authoring control");
assert(routerSource.includes("renderPhaseBMissions"), "Missions renderer is not wired");
assert(routerSource.includes("`${BASE}/missions`"), "Missions route is not wired");

assert(dailyWeeklySource.includes("UI MOCK · NOT RUNTIME CONNECTED"), "Daily / Weekly must be explicitly labeled as disconnected mock UI");
assert(dailyWeeklySource.includes("Authoring is disabled"), "Daily / Weekly must explain its authoring boundary");
assert(!dailyWeeklySource.includes("+ New Rotation"), "Disconnected Daily / Weekly UI must not expose fake authoring actions");
assert(!dailyWeeklySource.includes("Rotation Calendar\""), "Disconnected Daily / Weekly UI must not expose fake calendar actions");

const phaseMap = JSON.parse(phaseMapSource);
const missionsMap = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/missions");
assert.equal(missionsMap?.persistence, "child-runtime-session");
assert.equal(missionsMap?.applyBoundary, "none");
assert.equal(missionsMap?.status, "phase-b-ui-wired-runtime-backed-readonly");
const recurringMap = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/daily-weekly");
assert.equal(recurringMap?.persistence, "none");
assert.equal(recurringMap?.applyBoundary, "none");
assert.equal(recurringMap?.status, "ui-prototype-not-runtime-connected");

console.log("Space Typing Missions Admin validation passed: canonical Stage Objectives, read-only contract, recurring authoring closed, Daily / Weekly mock isolated.");
