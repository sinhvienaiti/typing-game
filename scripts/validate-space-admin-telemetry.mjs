import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const childRoot = resolve(root, "games/space-typing");
const TELEMETRY_AUDITED_CHILD_SHA = "da3971d4863a6e2aaf5f8323f34015693883aba9";
const readChild = (path) => readFile(resolve(childRoot, path), "utf8");
const contract = JSON.parse(await readChild("contracts/space-typing-admin-telemetry.v1.json"));
const [page, router, server, phaseMapSource, historicalAdmin, historicalAnalytics, historicalSummary] = await Promise.all([
  readFile(resolve(root, "portal/src/admin/space-typing-telemetry-phase-b.ts"), "utf8"),
  readFile(resolve(root, "portal/src/admin/space-typing-phase-b.ts"), "utf8"),
  readFile(resolve(root, "admin/server.mjs"), "utf8"),
  readFile(resolve(root, "admin/space-typing-phase-b-map.v1.json"), "utf8"),
  readChild("src/expansion-v2/historical-analytics-admin.ts"),
  readChild("src/expansion-v2/historical-analytics.ts"),
  readChild("src/expansion-v2/historical-analytics-summary.ts"),
]);
const phaseMap = JSON.parse(phaseMapSource);
const childHead = execFileSync("git", ["-C", childRoot, "rev-parse", "HEAD"], { encoding: "utf8" }).trim();

assert.equal(childHead, TELEMETRY_AUDITED_CHILD_SHA, `Telemetry audit is stale: audited=${TELEMETRY_AUDITED_CHILD_SHA} pinned-child=${childHead}. Re-audit telemetry before changing the SHA.`);
assert.equal(contract.contractRevision, "space-typing-admin-telemetry-v1");
assert.equal(contract.capability, "telemetry.read");
assert.deepEqual(contract.routes, [
  { id: "overview", path: "/admin/space-typing", label: "Overview" },
  { id: "analytics", path: "/admin/space-typing/analytics", label: "Analytics" },
]);
assert.equal(contract.telemetry.mode, "runtime-derived-readonly");
assert.equal(contract.telemetry.persistence, "session-memory-plus-local-profile-history");
assert.equal(contract.telemetry.applyBoundary, "none");
assert.equal(contract.telemetry.writeCapability, false);
assert.equal(contract.telemetry.publishCapability, false);
assert.equal(contract.telemetry.historicalAggregationCapability, true);
assert.equal(contract.telemetry.centralTelemetryBackendCapability, false);
assert.equal(contract.telemetry.performanceDiagnostics.adminReadableSnapshot, false);

assert.deepEqual(contract.telemetry.historical, {
  available: true,
  mode: "local-profile-persisted-readonly",
  persistenceOwner: "ExpansionV2Profile.history",
  scope: "current-local-profile",
  crossPlayerSupported: false,
  centralTelemetryBackendCapability: false,
  writeCapability: false,
  liveTelemetryFallbackWhenEmpty: false,
});
assert.equal(contract.telemetry.privacy.playerIdentityCollectedByContract, false);
assert.equal(contract.telemetry.privacy.networkTransportOwnedByContract, false);
assert.equal(contract.telemetry.privacy.crossSessionRetentionOwnedByContract, true);
assert.equal(contract.telemetry.privacy.crossSessionRetentionScope, "browser-local-current-profile-only");
assert.equal(contract.telemetry.privacy.crossPlayerAggregation, false);

assert.match(historicalAdmin, /HISTORICAL_ANALYTICS_ADMIN_MODE = "read-only"/);
assert.match(historicalAdmin, /crossPlayerSupported:\s*false/);
assert.match(historicalAdmin, /Metrics are derived only from persisted historical events in the current player profile/);
assert.match(historicalAnalytics, /HistoricalAggregate/);
assert.match(historicalSummary, /HistoricalAnalyticsSummaryV1/);
for (const source of contract.telemetry.runtimeSources) {
  const content = await readChild(source);
  assert.ok(content.length > 0, `Telemetry runtime source is empty: ${source}`);
}
for (const unsupported of [
  "query global or cross-player historical analytics",
  "export server-side telemetry events without a backend owner",
  "mutate gameplay through analytics controls",
  "publish telemetry-derived gameplay configuration",
  "claim adaptive render internals are an Admin-readable live feed",
  "fabricate historical rows from live telemetry",
]) {
  assert.ok(contract.telemetry.unsupportedAdminOperations.includes(unsupported), `Telemetry unsupported boundary missing: ${unsupported}`);
}

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
assert.match(page, /RUNTIME-BACKED · READ ONLY/);
assert.match(page, /LOCAL PROFILE HISTORY/);
assert.match(page, /NO CENTRAL BACKEND/);
assert.match(page, /persisted history for the current browser-local profile/);
assert.match(page, /Historical rows come only from persisted ExpansionV2Profile history/);
assert.match(page, /Admin-readable live snapshot/);
assert.doesNotMatch(page, /NO HISTORICAL BACKEND/);
assert.doesNotMatch(page, /No live cross-process feed or historical telemetry store exists/);
assert.doesNotMatch(page, /createRevision|\/publish|\/revisions|Math\.random/);
for (const method of ["POST", "PUT", "PATCH", "DELETE"]) {
  assert.ok(!page.includes(`method: "${method}"`), `Telemetry UI must remain read-only (${method})`);
}

for (const route of ["/admin/space-typing", "/admin/space-typing/analytics"]) {
  const row = phaseMap.screens.find((entry) => entry.route === route);
  assert.ok(row, `Telemetry Phase B map row is required: ${route}`);
  assert.equal(row.domain, "telemetry");
  assert.equal(row.persistence, "child-session-runtime-and-local-profile-history");
  assert.equal(row.applyBoundary, "none");
  assert.equal(row.status, "phase-b-ui-wired-runtime-backed-readonly");
}

console.log(`Space Typing Admin telemetry mapping: PASS (${childHead.slice(0, 12)} · session telemetry + local-profile historical analytics read-only; no synthetic central/cross-player backend).`);
