import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (path) => readFile(resolve(root, path), "utf8");

const [acceptance, security, history, developerTools, developerToolsUi, previewStudio, previewBridge] = await Promise.all([
  read("docs/SPACE_TYPING_ADMIN_V2_MANUAL_ACCEPTANCE.md"),
  read("admin/admin-security.mjs"),
  read("portal/src/admin/space-typing-history-phase-b.ts"),
  read("admin/developer-tools.mjs"),
  read("portal/src/admin/v2/developer-tools.ts"),
  read("portal/src/admin/v2/preview/production-preview-studio.ts"),
  read("portal/src/admin/v2/preview/production-preview-bridge.ts"),
]);

assert.match(acceptance, /# A17 — Administrator end-to-end acceptance matrix/);
for (let index = 1; index <= 25; index += 1) {
  const id = `A17-M${String(index).padStart(2, "0")}`;
  assert.ok(acceptance.includes(id), `A17 acceptance scenario missing: ${id}`);
}
assert.match(acceptance, /MANUAL: QUEUED/);
assert.doesNotMatch(acceptance, /MANUAL:\s*PASS/i, "A17 must not claim browser/manual PASS from code inspection alone.");
assert.doesNotMatch(acceptance, /# Future phase scenarios/, "A17 must replace the old future-phase placeholder section.");
for (const phrase of [
  "Change a real Shop product price",
  "Ship Draft vs Published production preview",
  "Enemy/Boss combat preview",
  "Skill cast through production runtime",
  "World production environment preview",
  "Stage representative production composition",
  "Publish safely with CAS",
  "Restricted role cannot access Developer Tools",
  "Audit attribution for mutation / publish / rollback",
  "Production preview teardown leaves no orphan resources",
]) assert.ok(acceptance.includes(phrase), `Required A17 task missing: ${phrase}`);

// A13: role evaluation is server-owned and unknown roles fail closed.
assert.match(security, /ADMIN_ROLE_TEMPLATES/);
assert.match(security, /TYPING_GAME_ADMIN_ROLE/);
assert.match(security, /TYPING_GAME_ADMIN_PERMISSION_OVERRIDES/);
assert.match(security, /template\?\.permissions \?\? \[\]/);
assert.match(security, /Never trust a browser\/request header to elevate access/);
assert.match(security, /result: "denied"/);

// A14: administrator-facing compare/audit is present while CAS remains backend-owned.
for (const token of ["before", "after", "getAudit", "Publish", "Rollback", "Advanced"]) {
  assert.ok(history.includes(token), `A14 History evidence missing: ${token}`);
}
assert.match(history, /expectedActiveRevision|api\.publish|api\.rollback/);

// A15: technical surfaces are consolidated into the five named inspector areas.
const developerSections = [
  ["runtime-inspector", "Runtime Inspector"],
  ["contract-inspector", "Contract Inspector"],
  ["validation", "Validation"],
  ["asset-diagnostics", "Asset Diagnostics"],
  ["qa-sandbox", "QA Sandbox"],
];
for (const [id, label] of developerSections) {
  assert.ok(developerTools.includes(`id: "${id}"`), `Developer Tools section missing: ${id}`);
  assert.ok(developerTools.includes(`label: "${label}"`), `Developer Tools section label missing: ${label}`);
}
assert.match(developerTools, /developer\.runtime-inspect/);

// A13/A15/A17-M19: direct-route access must fail closed before any technical inspector mounts.
assert.match(developerToolsUi, /const manifest = await api\.getDeveloperToolsManifest\(\)/);
assert.match(developerToolsUi, /renderAuthorizedDeveloperTools\(root, manifest, navigate\)/);
assert.match(developerToolsUi, /do not mount any technical inspector/);
assert.match(developerToolsUi, /Developer Tools unavailable/);
const routeGate = developerToolsUi.slice(developerToolsUi.indexOf("export function renderAdminV2DeveloperTools"));
assert.ok(
  routeGate.indexOf("await api.getDeveloperToolsManifest()") < routeGate.indexOf("renderAuthorizedDeveloperTools(root, manifest, navigate)"),
  "Developer Tools must verify the server-authorized manifest before mounting technical inspectors.",
);
assert.doesNotMatch(
  routeGate.slice(0, routeGate.indexOf("await api.getDeveloperToolsManifest()")),
  /createInspector\(|api\.getState\(|api\.getRuntime\(/,
  "Developer Tools direct route must not mount or query technical inspectors before authorization succeeds.",
);

// A16/A10.5: preview UX/lifecycle remains accessible and isolated.
assert.match(previewStudio, /aria-live/);
assert.match(previewStudio, /fullscreenchange/);
assert.match(previewStudio, /keydown/);
assert.match(previewStudio, /dispose/);
assert.match(previewBridge, /candidateGeneration/);
assert.match(previewBridge, /ProductionPreviewStaleError/);
assert.match(previewBridge, /DISPOSE/);
assert.match(previewBridge, /teardown/);

console.log("Space Typing Admin A17 acceptance closure validated: 25 queued manual scenarios + A13–A16 automated safety evidence are present without fake manual PASS.");
