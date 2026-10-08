import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");
const eventsContract = JSON.parse(await read("games/space-typing/contracts/space-typing-admin-events.v1.json"));
const [stageScheduler, galaxyHazards, rareTargets, anomaly, recallBonus, rewardChoice, gameSource, uiSource, routerSource, shellSource, serverSource, phaseMapSource] = await Promise.all([
  read("games/space-typing/src/events/stage-scheduler.ts"),
  read("games/space-typing/src/events/galaxy-hazards.ts"),
  read("games/space-typing/src/events/rare-targets.ts"),
  read("games/space-typing/src/events/anomaly.ts"),
  read("games/space-typing/src/events/recall-bonus.ts"),
  read("games/space-typing/src/events/reward-choice.ts"),
  read("games/space-typing/src/Game.ts"),
  read("portal/src/admin/space-typing-events-phase-b.ts"),
  read("portal/src/admin/space-typing-phase-b.ts"),
  read("portal/src/admin/space-typing.ts"),
  read("admin/server.mjs"),
  read("admin/space-typing-phase-b-map.v1.json"),
]);

const events = eventsContract.events;
assert.equal(eventsContract.contractRevision, "space-typing-admin-events-v1");
assert.equal(eventsContract.capability, "events.read");
assert.deepEqual(eventsContract.route, { id: "events", path: "/admin/space-typing/events", label: "Events" });
assert.equal(events.mode, "runtime-derived-readonly");
assert.deepEqual(events.authorableFields, []);
assert.deepEqual(events.stageRandomEventIds, ["fast-enemies", "armored-enemies", "low-shield", "double-supply", "projectile-storm"]);
assert.deepEqual(events.galaxyModifierIds, ["supply-run", "training-window", "ion-storm", "debris-field", "solar-flare", "gravity-tide", "gauntlet-pressure"]);
assert.equal(events.scheduledLiveOpsService, false);
assert.equal(events.calendarService, false);
assert.equal(events.writeCapability, false);
assert.equal(events.previewCapability, false);
assert.equal(events.persistenceOwner, "stage-session-runtime-only");

for (const [source, symbols] of [
  [stageScheduler, ["STAGE_RANDOM_EVENT_IDS", "scheduleStageRandomEvents", "combineStageEventEffects"]],
  [galaxyHazards, ["galaxyStageModifiers", "supply-run", "training-window", "gauntlet-pressure"]],
  [rareTargets, ["goldenEnemyChance", "treasureDroneChance"]],
  [anomaly, ["anomalyCrateChance"]],
  [recallBonus, ["shouldScheduleRecallBonus"]],
  [rewardChoice, ["rewardChoiceCrateChance"]],
]) {
  for (const symbol of symbols) assert(source.includes(symbol), `Missing Events runtime evidence: ${symbol}`);
}
for (const symbol of events.sourceFunctions) {
  assert(gameSource.includes(symbol), `Game.ts missing Events runtime consumer: ${symbol}`);
}

assert(uiSource.includes("/api/admin/space-typing/events/contract"), "Events UI must read the canonical child sidecar contract");
assert(uiSource.includes("RUNTIME-BACKED · READ ONLY"), "Events UI must expose read-only runtime ownership");
assert(uiSource.includes("NO CALENDAR SERVICE"), "Events UI must expose absence of a calendar service");
assert(!uiSource.includes("api.createRevision"), "Events UI must not create synthetic revisions");
assert(!uiSource.includes("api.publish"), "Events UI must not publish synthetic Live Ops config");
assert(!uiSource.includes('type = "range"'), "Events UI must not expose unsupported rollout/range authoring");
assert(!uiSource.includes("Event Enabled"), "Events UI must not expose fake runtime enable toggles");
assert(routerSource.includes("renderPhaseBEvents"), "Events renderer is not wired into Phase B");
assert(routerSource.includes("`${BASE}/events`"), "Events route is not wired into Phase B");
const phaseBCall = 'const phaseB = renderPhaseBAdminScreen(path, this.navigate);';
assert(shellSource.includes(phaseBCall), "Space Typing shell must invoke the Phase B router");
assert(shellSource.includes('if (phaseB !== null) return phaseB;'), "Space Typing shell must return the canonical Phase B renderer");
assert(!shellSource.includes("renderExtendedAdminScreen"), "Legacy Events/mock renderer must not remain reachable from the production shell");
assert(shellSource.includes("return this.renderUnknown(path);"), "Unknown Admin routes must terminate at the explicit unknown-route guard");
assert(serverSource.includes("space-typing-admin-events.v1.json"), "Admin server must load Events from the pinned child contract");
assert(serverSource.includes("/api/admin/space-typing/events/contract"), "Admin server Events contract endpoint is missing");

const phaseMap = JSON.parse(phaseMapSource);
const row = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/events");
assert.equal(row?.domain, "runtime.events");
assert.equal(row?.persistence, "child-stage-session-runtime");
assert.equal(row?.applyBoundary, "none");
assert.equal(row?.status, "phase-b-ui-wired-runtime-backed-readonly");

console.log("Space Typing Events Admin validation passed: canonical stage runtime events are read-only and no legacy calendar/mock fallback is reachable.");
