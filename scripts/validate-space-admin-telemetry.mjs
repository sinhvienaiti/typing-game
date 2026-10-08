import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const childRoot = resolve(root, "games/space-typing");
const TELEMETRY_AUDITED_CHILD_SHA = "8c2bd4736ed1ec16dcf413985be9e540d10e123e";
const contract = JSON.parse(await readFile(resolve(childRoot, "contracts/space-typing-admin-telemetry.v1.json"), "utf8"));
const page = await readFile(resolve(root, "portal/src/admin/space-typing-telemetry-phase-b.ts"), "utf8");
const router = await readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8");
const server = await readFile(resolve(root, "admin/server.mjs"), "utf8");
const phaseMap = JSON.parse(await readFile(resolve(root, "admin/space-typing-phase-b-map.v1.json"), "utf8"));
const childHead = execFileSync("git", ["-C", childRoot, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();

assert.equal(childHead, TELEMETRY_AUDITED_CHILD_SHA, `Telemetry audit is stale: audited=${TELEMETRY_AUDITED_CHILD_SHA} pinned-child=${childHead}. Re-audit telemetry before changing the SHA.`);
assert.equal(contract.contractRevision, "space-typing-admin-telemetry-v1");
assert.equal(contract.capability, "telemetry.read");
assert.deepEqual(contract.routes, [
  { id: "overview", path: "/admin/space-typing", label: "Overview" },
  { id: "analytics", path: "/admin/space-typing/analytics", label: "Analytics" },
]);
assert.equal(contract.telemetry.mode, "runtime-derived-session-readonly");
assert.equal(contract.telemetry.persistence, "session-memory-only");
assert.equal(contract.telemetry.applyBoundary, "none");
assert.equal(contract.telemetry.writeCapability, false);
assert.equal(contract.telemetry.publishCapability, false);
assert.equal(contract.telemetry.historicalAggregationCapability, false);
assert.equal(contract.telemetry.centralTelemetryBackendCapability, false);
assert.equal(contract.telemetry.performanceDiagnostics.adminReadableSnapshot, false);
assert.equal(contract.telemetry.privacy.playerIdentityCollectedByContract, false);
assert.equal(contract.telemetry.privacy.networkTransportOwnedByContract, false);
assert.equal(contract.telemetry.privacy.crossSessionRetentionOwnedByContract, false);

assert.match(server, /space-typing-admin-telemetry\.v1\.json/);
assert.match(server, /request\.method==="GET"&&url\.pathname==="\/api\/admin\/space-typing\/telemetry\/contract"/);
for (const method of ["POST", "PUT", "PATCH", "DELETE"]) {
  assert.ok(
    !server.includes(`request.method==="${method}"&&url.pathname==="/api/admin/space-typing/telemetry/`),
    `Telemetry Admin service must not expose a fake ${method} mutation endpoint`,
  );
}

assert.match(router, /renderPhaseBTelemetry/);
assert.match(router, /path === BASE \|\| path === `\$\{BASE\}\/analytics`/);
assert.match(page, /\/api\/admin\/space-typing\/telemetry\/contract/);
assert.match(page, /RUNTIME-BACKED · SESSION READ ONLY/);
assert.match(page, /NO HISTORICAL BACKEND/);
assert.match(page, /no live cross-process feed or historical telemetry store exists/i);
assert.match(page, /Admin-readable live snapshot/);
assert.doesNotMatch(page, /createRevision|\/publish|\/revisions|Math\.random/);
for (const method of ["POST", "PUT", "PATCH", "DELETE"]) {
  assert.ok(!page.includes(`method: "${method}"`), `Telemetry UI must remain read-only (${method})`);
}

for (const route of ["/admin/space-typing", "/admin/space-typing/analytics"]) {
  const row = phaseMap.screens.find((entry) => entry.route === route);
  assert.ok(row, `Telemetry Phase B map row is required: ${route}`);
  assert.equal(row.domain, "telemetry");
  assert.equal(row.persistence, "child-stage-session-runtime");
  assert.equal(row.applyBoundary, "none");
  assert.equal(row.status, "phase-b-ui-wired-runtime-backed-readonly");
}

console.log(`Space Typing Admin telemetry mapping: PASS (${childHead.slice(0, 12)} · session-only runtime contract + no synthetic historical analytics).`);
