import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");
const contract = JSON.parse(await read("games/space-typing/contracts/space-typing-admin-ranked.v1.json"));
const [rankedSource, authoritySource, serviceSource, wsSource, uiSource, routerSource, shellSource, serverSource, phaseMapSource] = await Promise.all([
  read("games/space-typing/src/duel/ranked.ts"),
  read("games/space-typing/src/duel/authority.ts"),
  read("games/space-typing/server/duel/ranked-service.ts"),
  read("games/space-typing/server/duel/ws-server.ts"),
  read("portal/src/admin/space-typing-ranked-phase-b.ts"),
  read("portal/src/admin/space-typing-phase-b.ts"),
  read("portal/src/admin/space-typing.ts"),
  read("admin/server.mjs"),
  read("admin/space-typing-phase-b-map.v1.json"),
]);

const ranked = contract.ranked;
assert.equal(contract.contractRevision, "space-typing-admin-ranked-v1");
assert.equal(contract.capability, "ranked.read");
assert.deepEqual(contract.route, { id: "ranked", path: "/admin/space-typing/ranked", label: "Ranked" });
assert.equal(ranked.mode, "runtime-derived-readonly");
assert.deepEqual(ranked.authorableFields, []);
assert.equal(ranked.writeCapability, false);
assert.equal(ranked.previewCapability, false);
assert.equal(ranked.seasonService, false);
assert.equal(ranked.rewardTableService, false);

assert.deepEqual(ranked.ruleset, {
  id: "ranked-standard-v1",
  combatProfile: "normalized",
  matchLengthSeconds: 240,
  roundFormat: 3,
  hazardLevel: "standard",
  mysteryFrequency: "standard",
  fateFrequency: "standard",
  modifier: "standard",
  allowPveStatScaling: false,
  allowPveLuckPity: false,
  allowCampaignCreditMinting: false,
  normalizedLoadoutBudget: 3,
  mapPool: ["frost-wastes", "inferno-rift", "tempest-prime", "ocean-abyss", "terra-core", "celestial-void"],
});
assert.deepEqual(ranked.rating, {
  base: 1000,
  min: 400,
  max: 2600,
  typingWeight: 0.4,
  duelWeight: 0.6,
  provisionalMatches: 20,
  experiencedMatches: 80,
  kFactors: [40, 28, 20],
});
assert.deepEqual(ranked.matchmaking, {
  initialAllowedGap: 90,
  gapIncreaseEverySeconds: 10,
  gapIncrease: 35,
  maxAllowedGap: 450,
  reconnectGraceMs: 30000,
});

for (const symbol of [
  "DUEL_RANKED_BASE_RATING = 1000",
  "DUEL_RANKED_MIN_RATING = 400",
  "DUEL_RANKED_MAX_RATING = 2600",
  "DUEL_RANKED_RECONNECT_GRACE_MS = 30_000",
  "DUEL_RANKED_RULESET",
  'id: "ranked-standard-v1"',
  "typingRating * 0.4 + safe.duelRating * 0.6",
  "90 + Math.floor(waitSeconds / 10) * 35",
  "Math.min(\n    450",
  "own.matchesPlayed < 20",
  "own.matchesPlayed < 80",
]) assert(rankedSource.includes(symbol), `Ranked runtime evidence missing: ${symbol}`);
for (const symbol of ["startRankedMatch", "rankedParticipant", "finishRankedForfeit"]) {
  assert(authoritySource.includes(symbol), `Ranked authority evidence missing: ${symbol}`);
}
for (const symbol of ["DuelRankedProfileStore", "InMemoryDuelRankedProfileStore", "JsonFileDuelRankedProfileStore", "DuelRankedService"]) {
  assert(serviceSource.includes(symbol), `Ranked service evidence missing: ${symbol}`);
}
for (const symbol of ["DUEL_RANKED_DATA_PATH", "new InMemoryDuelRankedProfileStore()", "new JsonFileDuelRankedProfileStore("]) {
  assert(wsSource.includes(symbol), `Ranked persistence wiring missing: ${symbol}`);
}

assert(uiSource.includes("/api/admin/space-typing/ranked/contract"), "Ranked UI must read canonical child sidecar contract");
assert(uiSource.includes("RUNTIME-BACKED · READ ONLY"), "Ranked UI must expose read-only Admin ownership");
assert(uiSource.includes("NO SEASON SERVICE"), "Ranked UI must expose absence of a season service");
assert(uiSource.includes("Canonical Ruleset"), "Ranked UI must show the canonical ruleset");
assert(uiSource.includes("Profile Persistence"), "Ranked UI must show profile persistence ownership");
assert(!uiSource.includes("Save UI Draft"), "Ranked Phase B UI must not expose synthetic revision writes");
assert(!uiSource.includes('type = "range"'), "Ranked Phase B UI must not expose free-form range controls");
assert(!uiSource.includes("api.createRevision"), "Ranked Phase B UI must not write Admin revisions");
assert(!uiSource.includes("api.publish"), "Ranked Phase B UI must not publish synthetic Ranked policy");

assert(routerSource.includes("renderPhaseBRanked"), "Ranked renderer is not wired into Phase B");
assert(routerSource.includes("`${BASE}/ranked`"), "Ranked route is not wired into Phase B");
const phaseBCall = "const phaseB = renderPhaseBAdminScreen(path, this.navigate);";
assert(shellSource.includes(phaseBCall), "Space Typing shell must invoke the Phase B router");
assert(shellSource.includes("if (phaseB !== null) return phaseB;"), "Space Typing shell must return the canonical Phase B renderer");
assert(!shellSource.includes("renderExtendedAdminScreen"), "Legacy Ranked/mock renderer must not remain reachable from the production shell");
assert(shellSource.includes("return this.renderUnknown(path);"), "Unknown Admin routes must terminate at the explicit unknown-route guard");
assert(serverSource.includes("space-typing-admin-ranked.v1.json"), "Admin server must load Ranked from pinned child contract");
assert(serverSource.includes("/api/admin/space-typing/ranked/contract"), "Admin server Ranked contract endpoint is missing");

const phaseMap = JSON.parse(phaseMapSource);
const row = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/ranked");
assert.equal(row?.domain, "runtime.ranked");
assert.equal(row?.persistence, "child-duel-server-profile-store");
assert.equal(row?.applyBoundary, "none");
assert.equal(row?.status, "phase-b-ui-wired-runtime-backed-readonly");

for (const unsupported of [
  "seasonId",
  "seasonName",
  "seasonStartsAt",
  "seasonEndsAt",
  "placementMatches",
  "manualMatchmakingSpread",
  "rankedEnabled",
  "modeEnableToggles",
  "tierThresholds",
  "seasonRewards",
  "playerDistribution",
]) assert(ranked.unsupportedAdminMockFields.includes(unsupported), `Ranked unsupported mock field missing: ${unsupported}`);

console.log("Space Typing Ranked Admin validation passed: authority-owned rules/rating/persistence are read-only and legacy season authoring is unreachable.");
