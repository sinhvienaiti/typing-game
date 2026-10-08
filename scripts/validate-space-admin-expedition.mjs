import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const childRoot = resolve(root, "games/space-typing");
const EXPEDITION_AUDITED_CHILD_SHA = "053ae2dde85614361ee33c023c3f0aa33049ed66";
const contract = JSON.parse(await readFile(resolve(childRoot, "contracts/space-typing-admin-expedition.v1.json"), "utf8"));
const page = await readFile(resolve(root, "portal/src/admin/space-typing-expedition-phase-b.ts"), "utf8");
const router = await readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8");
const server = await readFile(resolve(root, "admin/server.mjs"), "utf8");
const phaseMap = JSON.parse(await readFile(resolve(root, "admin/space-typing-phase-b-map.v1.json"), "utf8"));
const childHead = execFileSync("git", ["-C", childRoot, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();

assert.equal(childHead, EXPEDITION_AUDITED_CHILD_SHA, `Expedition audit is stale: audited=${EXPEDITION_AUDITED_CHILD_SHA} pinned-child=${childHead}. Re-audit Expedition before changing the SHA.`);
assert.equal(contract.contractRevision, "space-typing-admin-expedition-v1");
assert.equal(contract.capability, "expedition.read");
assert.equal(contract.route.path, "/admin/space-typing/expedition");
assert.equal(contract.expedition.mode, "runtime-backed-browser-persisted-run-readonly");
assert.equal(contract.expedition.runVersion, 1);
assert.equal(contract.expedition.rulesetVersion, "expansion-v2-v1");
assert.equal(contract.expedition.encounterCount, 8);
assert.deepEqual(contract.expedition.draftBeforeEncounterIndexes, [0, 2, 4, 6]);
assert.equal(contract.expedition.restAfterEncounterIndex, 3);
assert.equal(contract.expedition.persistence.storageKey, "spaceTypingExpeditionRunV1");
assert.equal(contract.expedition.persistence.revisionedEnvelope, true);
assert.equal(contract.expedition.persistence.writerOwnership, true);
assert.equal(contract.expedition.safety.adminWriteCapability, false);
assert.equal(contract.expedition.safety.adminPublishCapability, false);
assert.equal(contract.expedition.safety.adminRunMutationCapability, false);
assert.equal(contract.expedition.safety.adminStorageMutationCapability, false);

assert.match(server, /space-typing-admin-expedition\.v1\.json/);
assert.match(server, /request\.method==="GET"&&url\.pathname==="\/api\/admin\/space-typing\/expedition\/contract"/);
for (const method of ["POST", "PUT", "PATCH", "DELETE"]) {
  assert.ok(
    !server.includes(`request.method==="${method}"&&url.pathname==="/api/admin/space-typing/expedition/`),
    `Expedition Admin service must not expose a fake ${method} run mutation endpoint`,
  );
}

assert.match(router, /renderPhaseBExpedition/);
assert.match(router, /\$\{BASE\}\/expedition`\) return renderPhaseBExpedition\(\)/);
assert.match(page, /\/api\/admin\/space-typing\/expedition\/contract/);
assert.match(page, /RUNTIME-BACKED · READ ONLY/);
assert.match(page, /BROWSER SAVE · NO REMOTE MUTATION/);
assert.match(page, /cannot read, clear, overwrite, create, resume, settle, or publish a player's run/i);
assert.match(page, /No synthetic Expedition backend/);
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

console.log(`Space Typing Admin Expedition mapping: PASS (${childHead.slice(0, 12)} · browser-owned resumable run + no remote mutation backend).`);
