import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");
const contract = JSON.parse(await read("portal/src/admin/contracts/space-typing-admin.v1.json"));
const [featureSource, mainSource, childAudit, childCi, uiSource, routerSource, legacyCore] = await Promise.all([
  read("games/space-typing/src/expansion-v2/feature-flags.ts"),
  read("games/space-typing/src/main.ts"),
  read("games/space-typing/scripts/audit-admin-feature-gates.ts"),
  read("games/space-typing/.github/workflows/ci.yml"),
  read("portal/src/admin/space-typing-feature-gates-phase-b.ts"),
  read("portal/src/admin/space-typing-phase-b.ts"),
  read("portal/src/admin/space-typing-phase-b-core.ts"),
]);

const featureGates = contract.featureGates;
assert(contract.capabilities.includes("feature-gates.read"), "Feature Gates contract must expose feature-gates.read");
assert(!contract.capabilities.includes("feature-gates.write"), "Feature Gates write must stay closed without a remote runtime service");
assert(!contract.capabilities.includes("feature-gates.preview"), "Feature Gates preview must stay closed without a canonical preview service");
assert(contract.routes.some((route) => route.id === "feature-gates" && route.path === "/admin/space-typing/feature-gates"), "Feature Gates canonical route missing");
assert.equal(featureGates.mode, "runtime-derived-readonly");
assert.deepEqual(featureGates.authorableFields, []);
assert.deepEqual(featureGates.ids, ["expansion-v2"]);
assert.equal(featureGates.remoteRolloutService, false);
assert.equal(featureGates.killSwitchService, false);
assert.equal(featureGates.percentageRollout, false);
assert.equal(featureGates.writeCapability, false);
assert.equal(featureGates.previewCapability, false);
assert.equal(featureGates.persistenceOwner, "browser-localStorage");
assert.equal(featureGates.gameplayConsumer, "src/main.ts");

const gate = featureGates.gates.find((entry) => entry.id === "expansion-v2");
assert(gate, "expansion-v2 gate missing from contract");
assert.equal(gate.storageKey, "spaceTypingExpansionV2Enabled");
assert.equal(gate.queryParam, "expansionV2");
assert.equal(gate.defaultEnabled, true);
assert.deepEqual(gate.queryOffValues, ["off", "0", "false"]);
assert.deepEqual(gate.queryOnValues, ["on", "1", "true"]);
assert.deepEqual(gate.overridePrecedence, ["query", "localStorage", "default"]);
assert.equal(gate.storageDisabledValue, "false");

for (const evidence of ["EXPANSION_V2_FEATURE_KEY", "spaceTypingExpansionV2Enabled", "expansionV2FeatureEnabled", 'params.get("expansionV2")']) {
  assert(featureSource.includes(evidence), `Missing canonical feature-gate runtime evidence: ${evidence}`);
}
assert(mainSource.includes("expansionV2FeatureEnabled"), "main.ts must consume the canonical Expansion V2 gate");
assert(childAudit.includes("Space Typing Admin Feature Gates audit OK"), "Child Feature Gates audit success marker missing");
assert(childCi.includes("Audit Feature Gates contract") && childCi.includes("pnpm feature-gates:audit"), "Child CI must execute Feature Gates audit");

assert(uiSource.includes("/api/admin/space-typing/contract"), "Feature Gates UI must read the authenticated canonical child contract");
assert(uiSource.includes("RUNTIME-BACKED · READ ONLY"), "Feature Gates UI must expose read-only ownership");
assert(uiSource.includes("NO REMOTE ROLLOUT"), "Feature Gates UI must make remote rollout absence explicit");
assert(uiSource.includes("expansion-v2") || uiSource.includes("featureGates.gates"), "Feature Gates UI must render the canonical runtime gate");
assert(uiSource.includes("Override precedence"), "Feature Gates UI must expose query/localStorage precedence");
for (const forbidden of [
  'button("Create Flag"',
  'btn("Create Flag"',
  "api.createRevision",
  "api.publish",
  'type = "range"',
  'type="range"',
  "rolloutPercent",
]) {
  assert(!uiSource.includes(forbidden), `Runtime Feature Gates UI must not expose legacy authoring primitive: ${forbidden}`);
}
assert(routerSource.includes("renderPhaseBFeatureGates"), "Feature Gates renderer is not wired");
assert(routerSource.includes("`${BASE}/feature-gates`"), "Canonical Feature Gates route is not wired");
assert(routerSource.includes("`${BASE}/flags`"), "Legacy /flags route must be intercepted by the runtime-backed renderer");
assert(routerSource.indexOf("`${BASE}/flags`") < routerSource.indexOf("renderPhaseBCoreAdminScreen(path, navigate)"), "Legacy /flags must be intercepted before the legacy core renderer");

// Legacy revision schema may still contain historical featureFlags for backward compatibility,
// but routing must make the old writable renderer unreachable from registered Feature Gates paths.
assert(legacyCore.includes("Admin Phase B · Feature Flags draft"), "Expected legacy featureFlags compatibility code was not found; remove this guard when legacy schema is migrated away");

console.log("Space Typing Feature Gates Admin validation passed: canonical expansion-v2 gate is read-only and legacy rollout authoring is unreachable.");
