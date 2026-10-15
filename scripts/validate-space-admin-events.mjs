import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");
const eventsContract = JSON.parse(await read("games/space-typing/contracts/space-typing-admin-events.v1.json"));
const [stageScheduler, galaxyHazards, rareTargets, anomaly, recallBonus, rewardChoice, gameSource, uiSource, routerSource, shellSource, serverSource, phaseMapSource, shopCapabilitySource] = await Promise.all([
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
  read("admin/shop-capability.mjs"),
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

// A11 Live Ops: use only real owners. Gameplay Events remain read-only; Shop owns unscheduled offer promotion fields.
assert(uiSource.includes("/api/admin/space-typing/events/contract"), "Live Ops UI must read the canonical child Events sidecar contract");
assert(uiSource.includes("/api/admin/space-typing/shop/capabilities"), "Live Ops UI must discover the canonical Shop offer owner");
assert(uiSource.includes("Promotions & Discounts"), "A11 must expose the real Promotions/Discounts ownership surface");
assert(uiSource.includes("Announcements"), "A11 must explicitly classify Announcements rather than omit or fabricate them");
assert(uiSource.includes("Open Shop offers"), "A11 promotions must delegate to the canonical Shop editor");
assert(uiSource.includes("NO CALENDAR SERVICE"), "Live Ops UI must expose absence of a calendar service");
assert(uiSource.includes("NO FAKE ANNOUNCEMENTS"), "Live Ops UI must expose absence of an announcement service");
assert(shopCapabilitySource.includes('"Original Price"'), "Shop capability must retain compare-at/original price ownership");
assert(shopCapabilitySource.includes('"Badge / Label"'), "Shop capability must retain promotion badge ownership");
assert(shopCapabilitySource.includes("offerWrite: authoringEnabled"), "Shop capability must gate offer authoring on the canonical policy/preview seam");
assert(shopCapabilitySource.includes("schedules: false"), "Shop capability must not fabricate scheduling");
assert(!uiSource.includes("api.createRevision"), "Live Ops page must not create synthetic Event/Announcement revisions");
assert(!uiSource.includes("api.publish"), "Live Ops page must not publish synthetic Live Ops config");
assert(!uiSource.includes('type = "range"'), "Live Ops page must not expose unsupported rollout/range authoring");
assert(!uiSource.includes("Event Enabled"), "Live Ops page must not expose fake runtime event enable toggles");
assert(!uiSource.includes("Discount Percent"), "Discount percentage must stay derived from Price and Original Price");
assert(!uiSource.includes("Start At"), "A11 must not fabricate schedule start controls");
assert(!uiSource.includes("End At"), "A11 must not fabricate schedule end controls");

assert(routerSource.includes("renderPhaseBEvents"), "Events/Live Ops renderer is not wired into Phase B");
assert(routerSource.includes("renderPhaseBEvents(navigate)"), "Live Ops must receive canonical navigation for Shop ownership handoff");
assert(routerSource.includes("`${BASE}/events`"), "Events route is not wired into Phase B");
const phaseBCall = 'const phaseB = renderPhaseBAdminScreen(path, this.navigate);';
assert(shellSource.includes(phaseBCall), "Space Typing shell must invoke the Phase B router");
assert(shellSource.includes('if (phaseB !== null) return phaseB;'), "Space Typing shell must return the canonical Phase B renderer");
assert(!shellSource.includes("renderExtendedAdminScreen"), "Legacy Events/mock renderer must not remain reachable from the production shell");
assert(shellSource.includes("return this.renderUnknown(path);"), "Unknown Admin routes must terminate at the explicit unknown-route guard");
assert(serverSource.includes("space-typing-admin-events.v1.json"), "Admin server must load Events from the pinned child contract");
assert(serverSource.includes("/api/admin/space-typing/events/contract"), "Admin server Events contract endpoint is missing");
assert(serverSource.includes("/api/admin/space-typing/shop/capabilities"), "Admin server Shop capability endpoint is missing");

const phaseMap = JSON.parse(phaseMapSource);
const row = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/events");
assert.equal(row?.domain, "runtime.events");
assert.equal(row?.persistence, "child-stage-session-runtime");
assert.equal(row?.applyBoundary, "none");
assert.equal(row?.status, "phase-b-ui-wired-runtime-backed-readonly");

console.log("Space Typing A11 Live Ops validation passed: runtime Events stay read-only, Shop owns unscheduled promotion fields, and no calendar/announcement backend is fabricated.");
