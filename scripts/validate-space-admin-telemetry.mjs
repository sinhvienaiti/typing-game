import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const childRoot = resolve(root, "games/space-typing");
const TELEMETRY_AUDITED_CHILD_SHA = "7a2548ae9d9ee939a59c76f63ced1b6d1b4ed662";
const readChild = (path) => readFile(resolve(childRoot, path), "utf8");
const contract = JSON.parse(await readChild("contracts/space-typing-admin-telemetry.v1.json"));
const [historicalAdminSource, historicalSummarySource, page, router, server, phaseMapSource] = await Promise.all([
  readChild("src/expansion-v2/historical-analytics-admin.ts"),
  readChild("src/expansion-v2/historical-analytics-summary.ts"),
  readFile(resolve(root, "portal/src/admin/space-typing-telemetry-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8"),
  readFile(resolve(root, "admin/server.mjs"), "utf8"),
  readFile(resolve(root, "admin/space-typing-phase-b-map.v1.json"), "utf8"),
]);
const childHead = execFileSync("git", ["-C", childRoot, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();

assert.equal(childHead, TELEMETRY_AUDITED_CHILD_SHA, `Telemetry audit is stale: audited=${TELEMETRY_AUDITED_CHILD_SHA} pinned-child=${childHead}. Re-audit current telemetry before changing the SHA.`);
assert.equal(contract.contractRevision, "space-typing-admin-telemetry-v1");
assert.equal(contract.capability, "telemetry.read");
assert.equal(contract.telemetry.mode, "runtime-derived-readonly");
assert.equal(contract.telemetry.persistence, "session-memory-plus-local-profile-history");
assert.equal(contract.telemetry.applyBoundary, "none");
assert.equal(contract.telemetry.writeCapability, false);
assert.equal(contract.telemetry.publishCapability, false);
assert.equal(contract.telemetry.historicalAggregationCapability, true);
assert.equal(contract.telemetry.centralTelemetryBackendCapability, false);
assert.equal(contract.telemetry.historical.available, true);
assert.equal(contract.telemetry.historical.mode, "local-profile-persisted-readonly");
assert.equal(contract.telemetry.historical.scope, "current-local-profile");
assert.equal(contract.telemetry.historical.crossPlayerSupported, false);
assert.equal(contract.telemetry.historical.centralTelemetryBackendCapability, false);
assert.equal(contract.telemetry.historical.writeCapability, false);
assert.equal(contract.telemetry.historical.liveTelemetryFallbackWhenEmpty, false);
assert.equal(contract.telemetry.privacy.crossPlayerAggregation, false);
assert.equal(contract.telemetry.performanceDiagnostics.adminReadableSnapshot, false);

assert.match(historicalAdminSource, /HISTORICAL_ANALYTICS_ADMIN_MODE = "read-only"/);
assert.match(historicalAdminSource, /canMutate: false/);
assert.match(historicalAdminSource, /crossPlayerSupported: false/);
assert.match(historicalAdminSource, /local profile/i);
assert.match(historicalSummarySource, /historical/i);

assert.match(server, /space-typing-admin-telemetry\.v1\.json/);
assert.match(server, /\/api\/admin\/space-typing\/telemetry\/contract/);
for (const method of ["POST", "PUT", "PATCH", "DELETE"]) {
  assert.ok(!server.includes(`request.method==="${method}"&&url.pathname==="/api/admin/space-typing/telemetry/`), `Telemetry Admin service must not expose a fake ${method} mutation endpoint`);
}

assert.match(router, /renderPhaseBTelemetry/);
assert.match(page, /HISTORY · LOCAL PROFILE ONLY/);
assert.match(page, /CROSS-PLAYER · UNSUPPORTED/);
assert.match(page, /current-local-profile/);
assert.match(page, /does not fabricate browser-local history/i);
assert.doesNotMatch(page, /NO HISTORICAL BACKEND/);
assert.doesNotMatch(page, /createRevision|\/publish|\/revisions|Math\.random/);

const phaseMap = JSON.parse(phaseMapSource);
for (const route of ["/admin/space-typing", "/admin/space-typing/analytics"]) {
  const row = phaseMap.screens.find((entry) => entry.route === route);
  assert.ok(row, `Telemetry Phase B map row is required: ${route}`);
  assert.equal(row.domain, "telemetry");
  assert.equal(row.persistence, "child-stage-session-and-local-profile-history");
  assert.equal(row.applyBoundary, "none");
  assert.equal(row.status, "phase-b-ui-wired-runtime-backed-readonly");
}

console.log(`Space Typing Admin telemetry mapping: PASS (${childHead.slice(0, 12)} · live session + local-profile historical read-only; cross-player fail-closed).`);
