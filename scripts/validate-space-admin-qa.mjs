import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { createDeveloperToolsManifest } from "../admin/developer-tools.mjs";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const childRoot = resolve(root, "games/space-typing");
const QA_AUDITED_CHILD_SHA = "1fd9eed7e6c492034c2816e90a6e0bc1e8c5309d";
const readChild = (path) => readFile(resolve(childRoot, path), "utf8");
const contract = JSON.parse(await readChild("contracts/space-typing-admin-qa.v1.json"));
const [page, router, server, nav, command, gamesSource, phaseMapSource, weeklyAdmin, alternativeModes, historicalAdmin, rankedHistoryService, voiceAdapter] = await Promise.all([
  readFile(resolve(root, "portal/src/admin/space-typing-qa-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8"),
  readFile(resolve(root, "admin/server.mjs"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-command.ts"), "utf8"),
  readFile(resolve(root, "portal/public/games.json"), "utf8"),
  readFile(resolve(root, "admin/space-typing-phase-b-map.v1.json"), "utf8"),
  readChild("src/expansion-v2/weekly-challenge-admin.ts"),
  readChild("src/duel/alternative-modes.ts"),
  readChild("src/expansion-v2/historical-analytics-admin.ts"),
  readChild("server/duel/ranked-history-query-service.ts"),
  readChild("src/input/voice-adapter.ts"),
]);
const games = JSON.parse(gamesSource);
const phaseMap = JSON.parse(phaseMapSource);
const childHead = execFileSync("git", ["-C", childRoot, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();
const developerManifest = createDeveloperToolsManifest();
const developerPaths = developerManifest.sections.flatMap((section) => section.tools.map((tool) => tool.path));

assert.equal(childHead, QA_AUDITED_CHILD_SHA, `QA audit is stale: audited=${QA_AUDITED_CHILD_SHA} pinned-child=${childHead}. Re-audit Test Lab before changing the SHA.`);
assert.equal(contract.contractRevision, "space-typing-admin-qa-v1");
assert.equal(contract.capability, "qa.execute");
assert.equal(contract.route.path, "/admin/space-typing/qa");
assert.equal(contract.qa.mode, "runtime-backed-ephemeral-sandbox");
assert.equal(contract.qa.applyBoundary, "new-qa-run");
assert.equal(contract.qa.sandboxMutationCapability, true);
assert.equal(contract.qa.presetWriteCapability, true);
assert.equal(contract.qa.productionPersistenceWriteCapability, false);
assert.equal(contract.qa.publishCapability, false);
assert.equal(contract.qa.persistence.session, "isolated-in-memory");
assert.equal(contract.qa.persistence.preset, "test-lab-only-browser-local-storage");
assert.equal(contract.qa.persistence.presetKey, "spaceTypingTestLabPresetV1");
assert.equal(contract.qa.persistence.productionCampaign, "no-write");
assert.equal(contract.qa.safety.usesProductionGameRuntime, true);
assert.equal(contract.qa.safety.isolatedSessionState, true);
assert.equal(contract.qa.safety.neverAutosavesCampaignProgression, true);
assert.equal(contract.qa.safety.gameMethodsGuardedByTestLabEnabled, true);
assert.equal(contract.qa.safety.productionSaveMutation, false);

// Re-audit coverage added after the previous 8128a2 checkpoint.
const coverage = contract.qa.currentRuntimeCoverage;
assert.deepEqual(coverage.weeklyChallenge, {
  owner: "src/expansion-v2/weekly-challenge-admin.ts",
  mode: "read-only",
});
assert.deepEqual(coverage.alternativeModes, {
  owner: "src/duel/alternative-modes.ts",
  modes: ["reflex", "word-chain"],
  rankedEligible: false,
});
assert.deepEqual(coverage.historicalAnalytics, {
  owner: "src/expansion-v2/historical-analytics-admin.ts",
  scope: "current-local-profile",
  crossPlayerSupported: false,
});
assert.deepEqual(coverage.rankedHistory, {
  owner: "server/duel/ranked-history-query-service.ts",
  queryServiceAvailable: true,
  productionTransportExposed: false,
  parentAdminQueryBridge: false,
  authenticationRequired: true,
  crossPlayerAuthorizationRequired: true,
});
assert.deepEqual(coverage.voiceHybrid, {
  owner: "src/input/voice-adapter.ts",
  hardwareAcceptance: "manual",
});

assert.match(weeklyAdmin, /WEEKLY_CHALLENGE_ADMIN_MODE = "read-only"/);
assert.match(weeklyAdmin, /canMutate:\s*false/);
assert.match(alternativeModes, /"reflex"/);
assert.match(alternativeModes, /"word-chain"/);
assert.match(alternativeModes, /rankedEligible:\s*false/);
assert.match(historicalAdmin, /HISTORICAL_ANALYTICS_ADMIN_MODE = "read-only"/);
assert.match(historicalAdmin, /crossPlayerSupported:\s*false/);
assert.match(rankedHistoryService, /export class DuelRankedHistoryQueryService/);
assert.match(rankedHistoryService, /"UNAUTHENTICATED"/);
assert.match(rankedHistoryService, /authorizeCrossPlayer/);
assert.match(voiceAdapter, /export class VoiceAdapter/);
assert.match(voiceAdapter, /VoiceAcceptanceMetrics/);

for (const source of contract.qa.runtimeSources) {
  const content = await readChild(source);
  assert.ok(content.length > 0, `QA runtime source is empty: ${source}`);
}

for (const unsupported of [
  "save sandbox state into Campaign progression",
  "publish sandbox state as production config",
  "overwrite player saves",
  "persist Test Lab rewards into production wallets",
  "bypass testLabEnabled runtime guards",
  "claim Ranked history is exposed through the current Parent Admin transport",
  "claim real microphone hardware acceptance from automated QA",
]) {
  assert.ok(contract.qa.unsupportedAdminOperations.includes(unsupported), `QA unsupported boundary missing: ${unsupported}`);
}

assert.match(server, /space-typing-admin-qa\.v1\.json/);
assert.match(server, /request\.method==="GET"&&url\.pathname==="\/api\/admin\/space-typing\/qa\/contract"/);
for (const method of ["POST", "PUT", "PATCH", "DELETE"]) {
  assert.ok(
    !server.includes(`request.method==="${method}"&&url.pathname==="/api/admin/space-typing/qa/`),
    `QA Admin service must not expose a fake ${method} mutation endpoint`,
  );
}

assert.match(router, /renderPhaseBQa/);
assert.match(router, /\$\{BASE\}\/qa`\) return renderPhaseBQa\(\)/);

// A2: QA remains directly routable for migration, but is a developer/test workflow rather than a primary administrator menu item.
assert.doesNotMatch(nav, /label:\s*"QA Sandbox"/);
assert.ok(nav.includes('[`${ADMIN_BASE}/qa`]: "QA Sandbox"'), "QA Sandbox legacy direct-route metadata must remain available during migration");
assert.ok(developerPaths.includes("/admin/space-typing/qa"), "QA Sandbox must be exposed from permission-gated Developer Tools");
assert.match(command, /\["QA Sandbox",\s*`\$\{BASE\}\/qa`,\s*"Developer Tools · QA"\]/);

assert.match(page, /\/api\/admin\/space-typing\/qa\/contract/);
assert.match(page, /\/games\.json/);
assert.match(page, /Developer Test Lab/);
assert.match(page, /RUNTIME-BACKED · EPHEMERAL/);
assert.match(page, /PRODUCTION SAVE · NO WRITE/);
assert.match(page, /NO FAKE QA CRUD · NO CAMPAIGN SAVE BRIDGE/);
assert.match(page, /window\.open\(appUrl/);
assert.doesNotMatch(page, /createRevision|\/publish|\/revisions/);

const game = games.games?.find((entry) => entry.id === "space-typing");
assert.equal(game?.appUrl, "https://space.typing-game.local");

const qaMap = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/qa");
assert.ok(qaMap, "QA Sandbox Phase B map row is required");
assert.equal(qaMap.domain, "qa");
assert.equal(qaMap.persistence, "child-test-lab-isolated-session-and-preset");
assert.equal(qaMap.applyBoundary, "new-qa-run");
assert.equal(qaMap.status, "phase-b-ui-wired-runtime-backed-ephemeral-sandbox");

console.log(`Space Typing Admin QA mapping: PASS (${childHead.slice(0, 12)} · isolated Test Lab + A2 Developer Tools placement + expanded runtime coverage audited + no production write bridge).`);
