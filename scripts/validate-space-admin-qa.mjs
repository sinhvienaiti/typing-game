import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const childRoot = resolve(root, "games/space-typing");
const QA_AUDITED_CHILD_SHA = "7a2548ae9d9ee939a59c76f63ced1b6d1b4ed662";
const contract = JSON.parse(await readFile(resolve(childRoot, "contracts/space-typing-admin-qa.v1.json"), "utf8"));
const page = await readFile(resolve(root, "portal/src/admin/space-typing-qa-phase-b.ts"), "utf8");
const router = await readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8");
const server = await readFile(resolve(root, "admin/server.mjs"), "utf8");
const nav = await readFile(resolve(root, "portal/src/admin/space-typing.ts"), "utf8");
const games = JSON.parse(await readFile(resolve(root, "portal/public/games.json"), "utf8"));
const phaseMap = JSON.parse(await readFile(resolve(root, "admin/space-typing-phase-b-map.v1.json"), "utf8"));
const childHead = execFileSync("git", ["-C", childRoot, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();

assert.equal(childHead, QA_AUDITED_CHILD_SHA, `QA audit is stale: audited=${QA_AUDITED_CHILD_SHA} pinned-child=${childHead}. Re-audit Test Lab before changing the SHA.`);
assert.equal(contract.contractRevision, "space-typing-admin-qa-v1");
assert.equal(contract.capability, "qa.execute");
assert.equal(contract.route.path, "/admin/space-typing/qa");
assert.equal(contract.qa.mode, "runtime-backed-ephemeral-sandbox");
assert.equal(contract.qa.applyBoundary, "new-qa-run");
assert.equal(contract.qa.sandboxMutationCapability, true);
assert.equal(contract.qa.productionPersistenceWriteCapability, false);
assert.equal(contract.qa.publishCapability, false);
assert.equal(contract.qa.persistence.session, "isolated-in-memory");
assert.equal(contract.qa.persistence.productionCampaign, "no-write");
assert.equal(contract.qa.safety.usesProductionGameRuntime, true);
assert.equal(contract.qa.safety.isolatedSessionState, true);
assert.equal(contract.qa.safety.productionSaveMutation, false);
assert.deepEqual(contract.qa.currentRuntimeCoverage.alternativeModes.modes, ["reflex", "word-chain"]);
assert.equal(contract.qa.currentRuntimeCoverage.alternativeModes.rankedEligible, false);
assert.equal(contract.qa.currentRuntimeCoverage.weeklyChallenge.mode, "read-only");
assert.equal(contract.qa.currentRuntimeCoverage.historicalAnalytics.scope, "current-local-profile");
assert.equal(contract.qa.currentRuntimeCoverage.historicalAnalytics.crossPlayerSupported, false);
assert.equal(contract.qa.currentRuntimeCoverage.rankedHistory.authenticationRequired, true);
assert.equal(contract.qa.currentRuntimeCoverage.rankedHistory.crossPlayerAuthorizationRequired, true);
assert.equal(contract.qa.currentRuntimeCoverage.voiceHybrid.hardwareAcceptance, "manual");

assert.match(server, /space-typing-admin-qa\.v1\.json/);
assert.match(server, /\/api\/admin\/space-typing\/qa\/contract/);
for (const method of ["POST", "PUT", "PATCH", "DELETE"]) {
  assert.ok(!server.includes(`request.method==="${method}"&&url.pathname==="/api/admin/space-typing/qa/`), `QA Admin service must not expose a fake ${method} mutation endpoint`);
}

assert.match(router, /renderPhaseBQa/);
assert.match(nav, /label:\s*"QA Sandbox"/);
assert.match(page, /Developer Test Lab/);
assert.match(page, /RUNTIME-BACKED · EPHEMERAL/);
assert.match(page, /PRODUCTION SAVE · NO WRITE/);
assert.match(page, /MIC HARDWARE · MANUAL/);
assert.match(page, /currentRuntimeCoverage/);
assert.match(page, /hardware acceptance =/i);
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

console.log(`Space Typing Admin QA mapping: PASS (${childHead.slice(0, 12)} · current-runtime coverage + isolated Test Lab + manual hardware gate).`);
