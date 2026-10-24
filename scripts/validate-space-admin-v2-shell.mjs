import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { createDeveloperToolsManifest } from "../admin/developer-tools.mjs";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (file) => readFile(resolve(root, file), "utf8");

const [shell, command, dashboard, developerTools, server, api] = await Promise.all([
  read("portal/src/admin/space-typing.ts"),
  read("portal/src/admin/space-typing-command.ts"),
  read("portal/src/admin/v2/dashboard.ts"),
  read("portal/src/admin/v2/developer-tools.ts"),
  read("admin/server.mjs"),
  read("portal/src/admin/api.ts"),
]);

// Root Dashboard must be a real V2 surface, while old Phase B routes remain available as migration routes.
assert.match(shell, /if \(path === ADMIN_BASE\) return renderAdminV2Dashboard/, "Admin root must render Dashboard V2 before the Phase B router.");
assert.match(shell, /if \(path === `\$\{ADMIN_BASE\}\/developer-tools`\) return renderAdminV2DeveloperTools/, "Developer Tools hub route is missing.");
assert.match(shell, /const phaseB = renderPhaseBAdminScreen\(path, this\.navigate\)/, "Legacy canonical routes must still delegate to Phase B during incremental migration.");
assert.match(shell, /LEGACY_ROUTE_LABELS/, "Legacy direct routes must retain breadcrumb metadata during migration.");

// Primary navigation is administrator-first and intentionally excludes developer-only/read-only inspector screens.
for (const primaryLabel of [
  "Overview",
  "Worlds & Stages",
  "Typing Content",
  "Ships",
  "Equipment",
  "Skills",
  "Enemies",
  "Bosses",
  "Music Library",
  "World / Stage Music",
  "Audio Defaults",
  "General Settings",
  "History & Publish",
  "Developer Tools",
]) {
  assert.match(shell, new RegExp(`label: "${primaryLabel.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}"`), `Primary navigation is missing ${primaryLabel}.`);
}
for (const diagnosticLabel of ["Shop", "Currencies", "Rewards & Drops", "Events", "Duel Settings", "Ranked", "Backgrounds", "VFX", "UI Assets", "QA Sandbox"]) {
  assert.doesNotMatch(shell, new RegExp(`label: "${diagnosticLabel.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}"`), `${diagnosticLabel} must not remain a primary navigation item in A2.`);
}
assert.match(shell, /requiredPermission: DEVELOPER_PERMISSION/, "Developer Tools navigation must declare its permission boundary.");
assert.match(shell, /wrapper\.hidden = true/, "Permission-gated navigation must fail closed before actor permissions load.");
assert.match(shell, /actor\.permissions\.includes\(DEVELOPER_PERMISSION\)/, "Developer Tools visibility must come from actor permissions.");

// Command palette must separate normal Admin concepts from developer diagnostics.
assert.match(command, /const PRIMARY_COMMANDS =/, "Primary command list is missing.");
assert.match(command, /const DEVELOPER_COMMANDS =/, "Developer command list is missing.");
assert.match(command, /options\.includeDeveloperTools/, "Developer commands must be conditional.");
assert.match(command, /getOptions: \(\) => AdminCommandOptions/, "Keyboard shortcut must resolve current permission-aware command options.");

// Dashboard must use only canonical data sources that exist today.
for (const sourceCall of ["api.getState()", "api.getActor()", "api.getMusicCatalogSummary()", "api.getAudit(12)"]) {
  assert.ok(dashboard.includes(sourceCall), `Dashboard is missing canonical source ${sourceCall}.`);
}
assert.match(dashboard, /revision\.relation === "draft"/, "Dashboard draft count must use real revision relations.");
assert.match(dashboard, /revision\.publishable === true/, "Dashboard publishable count must use store semantics.");
assert.match(dashboard, /state\.active\.config\.system\?\.maintenance\.enabled/, "Dashboard maintenance warning must use active canonical config.");
assert.match(dashboard, /event\.result === "success"/, "Dashboard recent activity must avoid rendering audit attempts as duplicate activity rows.");
assert.doesNotMatch(dashboard, /Math\.random|placeholder|fake metric/i, "Dashboard must not synthesize placeholder/fake metrics.");

// Developer Tools manifest must be server permission-gated and client-rendered from the backend source of truth.
assert.match(server, /url\.pathname==="\/api\/admin\/space-typing\/developer-tools\/manifest"/, "Developer Tools manifest endpoint is missing.");
assert.match(server, /requireAdminPermission\(actor, ADMIN_PERMISSIONS\.DEVELOPER_INSPECT\)/, "Developer Tools manifest endpoint must enforce developer.runtime-inspect.");
assert.match(developerTools, /api\.getDeveloperToolsManifest\(\)/, "Developer Tools UI must load the permission-gated backend manifest.");
assert.match(api, /getDeveloperToolsManifest\(\)/, "Typed Admin API is missing Developer Tools manifest support.");
assert.match(api, /getActor\(\)/, "Typed Admin API is missing actor support.");
assert.match(api, /getAudit\(limit = 8\)/, "Typed Admin API is missing audit support.");

const manifest = createDeveloperToolsManifest();
assert.equal(manifest.permission, "developer.runtime-inspect");
const devPaths = manifest.sections.flatMap((section) => section.tools.map((tool) => tool.path));
assert.ok(devPaths.includes("/admin/space-typing/shop"), "Shop runtime contract must migrate into Developer Tools until A4 makes it writable.");
assert.ok(devPaths.includes("/admin/space-typing/events"), "Events runtime diagnostics must migrate into Developer Tools until A11 provides a real scheduler.");
assert.ok(!devPaths.includes("/admin/space-typing/ships"), "Ships must remain an administrator workflow.");
assert.ok(!devPaths.includes("/admin/space-typing/music-library"), "Music Library must remain an administrator workflow.");

console.log(`Admin V2 A2 shell: OK (${manifest.sections.length} Developer Tools sections; primary navigation excludes read-only inspector screens).`);
