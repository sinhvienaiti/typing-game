import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const childRoot = resolve(root, "games/space-typing");
// A10.5 re-audit: 71de632..6c57a2b changes Ship/A10 capability work and
// isolated Admin preview modules. Expedition run/session/store ownership,
// expedition plan, Stage runtime policy and frozen Stage snapshot regression
// coverage asserted below are unchanged.
const EXPEDITION_AUDITED_CHILD_SHA = "6c57a2b7340b96a41e0f9f2b6fb5143ca532fd1c";
const readChild = (path) => readFile(resolve(childRoot, path), "utf8");
const contract = JSON.parse(await readChild("contracts/space-typing-admin-expedition.v1.json"));
const [
  page,
  router,
  server,
  phaseMapSource,
  coreSource,
  sessionSource,
  storeSource,
  planSource,
  stageRuntimePolicySource,
  stageSnapshotTestSource,
] = await Promise.all([
  readFile(resolve(root, "portal/src/admin/space-typing-expedition-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8"),
  readFile(resolve(root, "admin/server.mjs"), "utf8"),
  readFile(resolve(root, "admin/space-typing-phase-b-map.v1.json"), "utf8"),
  readChild("src/expedition/core.ts"),
  readChild("src/expedition/session.ts"),
  readChild("src/expedition/store.ts"),
  readChild("src/expansion-v2/expedition-plan.ts"),
  readChild("src/admin/stage-runtime-policy.ts"),
  readChild("tests/expedition-stage-runtime-snapshot.test.ts"),
]);
const phaseMap = JSON.parse(phaseMapSource);
const childHead = execFileSync("git", ["-C", childRoot, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();

assert.equal(childHead, EXPEDITION_AUDITED_CHILD_SHA, `Expedition audit is stale: audited=${EXPEDITION_AUDITED_CHILD_SHA} pinned-child=${childHead}. Re-audit Expedition before changing the SHA.`);
assert.equal(contract.contractRevision, "space-typing-admin-expedition-v1");
assert.equal(contract.capability, "expedition.read");
assert.equal(contract.route.path, "/admin/space-typing/expedition");
assert.equal(contract.expedition.mode, "runtime-backed-browser-persisted-run-readonly");
assert.equal(contract.expedition.runtimeOwner, "ExpeditionRun + ExpeditionSession");
assert.equal(contract.expedition.runVersion, 1);
assert.equal(contract.expedition.rulesetVersion, "expansion-v2-v1");
assert.equal(contract.expedition.contentVersion, "expansion-v2-world-01-v1");
assert.equal(contract.expedition.startKitId, "loaner-vanguard-v1");
assert.equal(contract.expedition.encounterCount, 8);
assert.deepEqual(contract.expedition.draftBeforeEncounterIndexes, [0, 2, 4, 6]);
assert.equal(contract.expedition.restAfterEncounterIndex, 3);
assert.deepEqual(contract.expedition.challengeKinds, ["prototype", "daily", "weekly", "qa"]);
assert.deepEqual(contract.expedition.phases, ["setup", "draft", "rest", "encounter", "settlement", "victory", "defeat", "abandoned"]);

const persistence = contract.expedition.persistence;
assert.equal(persistence.owner, "browser-local-storage");
assert.equal(persistence.storageKey, "spaceTypingExpeditionRunV1");
assert.equal(persistence.revisionedEnvelope, true);
assert.equal(persistence.writerOwnership, true);
assert.equal(persistence.writeVerification, true);
assert.equal(persistence.resumableNonTerminalRun, true);

const safety = contract.expedition.safety;
assert.equal(safety.campaignFixtureFrozenInRun, true);
assert.equal(safety.campaignFixtureHashChecked, true);
assert.equal(safety.adminWriteCapability, false);
assert.equal(safety.adminPublishCapability, false);
assert.equal(safety.adminRunMutationCapability, false);
assert.equal(safety.adminStorageMutationCapability, false);

for (const source of contract.expedition.runtimeSources) {
  const content = await readChild(source);
  assert.ok(content.length > 0, `Expedition runtime source is empty: ${source}`);
}
assert.match(coreSource, /weekly/);
assert.match(sessionSource, /ExpeditionSession/);
assert.match(storeSource, /spaceTypingExpeditionRunV1/);
assert.match(planSource, /expansion-v2/);

assert.match(storeSource, /stageRuntimeSnapshot/);
assert.match(storeSource, /freezeNewRunStageRuntime/);
assert.match(storeSource, /captureActiveStageRuntimeSession/);
assert.match(storeSource, /normalizePersistedStageRuntime/);
assert.match(storeSource, /materializeStageRuntimeSessionSnapshot/);
assert.match(storeSource, /armEncounterStageRuntime/);
assert.match(storeSource, /activateExpeditionStageRuntimeSession/);
assert.match(stageRuntimePolicySource, /export function materializeStageRuntimeSessionSnapshot/);
assert.match(stageRuntimePolicySource, /export function captureActiveStageRuntimeSession/);
assert.match(stageRuntimePolicySource, /export function activateExpeditionStageRuntimeSession/);
assert.match(stageRuntimePolicySource, /return bundledSession\(\)/);
assert.match(stageRuntimePolicySource, /expeditionStageRuntimeSession = null/);
assert.match(stageSnapshotTestSource, /stage-a/);
assert.match(stageSnapshotTestSource, /stage-b/);
assert.match(stageSnapshotTestSource, /legacy-run/);
assert.match(stageSnapshotTestSource, /createBundledStageConfig/);
assert.match(stageSnapshotTestSource, /loadExpeditionEnvelope/);

for (const unsupported of [
  "create or mutate Expedition runs",
  "edit Expedition encounter rules",
  "publish Expedition configuration",
  "read a player's browser-local Expedition save remotely",
  "clear or overwrite Expedition browser storage",
  "claim a centralized Expedition backend exists",
]) {
  assert.ok(contract.expedition.unsupportedAdminOperations.includes(unsupported), `Expedition unsupported boundary missing: ${unsupported}`);
}

assert.match(server, /space-typing-admin-expedition\.v1\.json/);
assert.match(server, /request\.method==="GET"&&url\.pathname==="\/api\/admin\/space-typing\/expedition\/contract"/);
for (const method of ["POST", "PUT", "PATCH", "DELETE"]) {
  assert.ok(
    !server.includes(`request.method==="${method}"&&url.pathname==="/api/admin/space-typing/expedition/`),
    `Expedition Admin service must not expose a fake ${method} run mutation endpoint`,
  );
}

assert.match(router, /renderPhaseBExpedition/);
assert.match(router, /\$\{BASE\}\/expedition`\) return decorated\(path, renderPhaseBExpedition\(\)\)/);
assert.match(router, /attachProductionPreviewClassification\(screen, path\)/);
assert.match(router, /attachRoleAwareActionGates\(screen\)/);
assert.match(page, /\/api\/admin\/space-typing\/expedition\/contract/);
assert.match(page, /RUNTIME-BACKED · READ ONLY/);
assert.match(page, /BROWSER SAVE · NO REMOTE MUTATION/);
assert.match(page, /cannot read, clear, overwrite, create, resume, settle, or publish a player's run/i);
assert.match(page, /No synthetic Expedition backend/);
assert.match(page, /Write verification:/);
assert.match(page, /Challenge kinds:/);
assert.doesNotMatch(page, /createRevision|\/publish|\/revisions|Math\.random/);
for (const method of ["POST", "PUT", "PATCH", "DELETE"]) {
  assert.ok(!page.includes(`method: "${method}"`), `Expedition UI must remain read-only (${method})`);
}

const row = phaseMap.screens.find((entry) => entry.route === "/admin/space-typing/expedition");
assert.ok(row, "Expedition Phase B map row is required");
assert.equal(row.domain, "liveOps.expedition");
assert.equal(row.persistence, "child-browser-local-expedition-run");
assert.equal(row.applyBoundary, "none");
assert.equal(row.status, "phase-b-ui-wired-runtime-backed-readonly");

console.log(`Space Typing Admin Expedition mapping: PASS (${childHead.slice(0, 12)} · browser-owned resumable run + frozen Stage runtime snapshot + legacy bundled fallback + no remote mutation backend).`);
