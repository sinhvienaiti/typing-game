import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const read = (file) => fs.readFileSync(path.join(root, file), "utf8");
const exists = (file) => fs.existsSync(path.join(root, file));

const mainFile = "portal/src/admin/space-typing.ts";
const routerFile = "portal/src/admin/space-typing-phase-b.ts";
const coreFile = "portal/src/admin/space-typing-phase-b-core.ts";
const telemetryFile = "portal/src/admin/space-typing-telemetry-phase-b.ts";
const musicLibraryFile = "portal/src/admin/space-typing-music-library-phase-b.ts";
const worldMusicFile = "portal/src/admin/space-typing-world-music-phase-b.ts";
const dailyWeeklyFile = "portal/src/admin/space-typing-daily-weekly-phase-b.ts";
const featureGatesFile = "portal/src/admin/space-typing-feature-gates-phase-b.ts";
const historyFile = "portal/src/admin/space-typing-history-phase-b.ts";
const commandFile = "portal/src/admin/space-typing-command.ts";
const iconFile = "portal/src/admin/space-typing-icons.ts";
const uiCssFile = "portal/src/admin/space-typing-ui.css";
const phaseMapFile = "admin/space-typing-phase-b-map.v1.json";
const packageFile = "portal/package.json";

const requiredFiles = [
  mainFile,
  routerFile,
  coreFile,
  telemetryFile,
  musicLibraryFile,
  worldMusicFile,
  dailyWeeklyFile,
  featureGatesFile,
  historyFile,
  commandFile,
  iconFile,
  uiCssFile,
  phaseMapFile,
  packageFile,
];
for (const file of requiredFiles) {
  if (!exists(file)) throw new Error(`Required Admin UI file is missing: ${file}`);
}

const main = read(mainFile);
const router = read(routerFile);
const core = read(coreFile);
const telemetry = read(telemetryFile);
const musicLibrary = read(musicLibraryFile);
const worldMusic = read(worldMusicFile);
const dailyWeekly = read(dailyWeeklyFile);
const featureGates = read(featureGatesFile);
const history = read(historyFile);
const command = read(commandFile);
const icons = read(iconFile);
const css = read(uiCssFile);
const phaseMap = JSON.parse(read(phaseMapFile));
const pkg = JSON.parse(read(packageFile));

const failures = [];
const assert = (condition, message) => { if (!condition) failures.push(message); };

const routes = [
  ["Overview", ""],
  ["Analytics", "/analytics"],
  ["Audio Defaults", "/audio"],
  ["Music Library", "/music-library"],
  ["World / Stage Music", "/world-music"],
  ["Ships", "/ships"],
  ["Equipment", "/equipment"],
  ["Skills", "/skills"],
  ["Enemies", "/enemies"],
  ["Bosses", "/bosses"],
  ["Worlds & Stages", "/stages"],
  ["Typing Content", "/typing-content"],
  ["Shop", "/shop"],
  ["Currencies", "/currencies"],
  ["Rewards & Drops", "/rewards"],
  ["Stamina / Warp", "/warp"],
  ["Missions", "/missions"],
  ["Daily / Weekly", "/daily-weekly"],
  ["Expedition", "/expedition"],
  ["Events", "/events"],
  ["Duel Settings", "/duel"],
  ["Ranked", "/ranked"],
  ["Alternative Modes", "/alternative-modes"],
  ["Backgrounds", "/backgrounds"],
  ["VFX", "/vfx"],
  ["UI Assets", "/ui-assets"],
  ["General Settings", "/settings"],
  ["Feature Gates", "/feature-gates"],
  ["History & Publish", "/history"],
  ["QA Sandbox", "/qa"],
];

assert(Array.isArray(phaseMap.screens), "Phase B map screens are missing");
assert(phaseMap.screens.length === routes.length, `Phase B map must contain exactly ${routes.length} registered screens`);

for (const [label, suffix] of routes) {
  assert(main.includes(`label: "${label}"`), `Navigation is missing ${label}`);
  if (suffix === "") {
    assert(main.includes('path: ADMIN_BASE'), "Overview canonical navigation path is missing");
  } else {
    assert(main.includes(`path: \`\${ADMIN_BASE}${suffix}\``), `Navigation path is missing ${label} (${suffix})`);
  }
  assert(command.includes(`"${label}"`), `Command palette is missing ${label}`);
}

// The shell must be Phase-B-only. Legacy mock renderers must never preempt the canonical router.
assert(main.includes('const phaseB = renderPhaseBAdminScreen(path, this.navigate);'), "Main Admin shell does not delegate to the Phase B router");
assert(main.includes('if (phaseB !== null) return phaseB;'), "Main Admin shell does not return the canonical Phase B renderer result");
assert(!main.includes('if (path === ADMIN_BASE) return this.renderOverview()'), "Legacy mock Overview still preempts Phase B telemetry");
assert(!main.includes('renderExtendedAdminScreen'), "Legacy extended renderer remains reachable from the production Admin shell");
assert(!main.includes('renderWorldMusicV2'), "Legacy World Music mock renderer remains reachable from the production Admin shell");
assert(!main.includes('renderDailyWeekly'), "Legacy Daily/Weekly mock renderer remains reachable from the production Admin shell");
assert(!main.includes('openMusicUploadMockDialog'), "Legacy Music Library mock workflow remains reachable from the production Admin shell");
assert(!main.includes('space-typing-mock'), "Production Admin shell still imports mock data");
assert(!main.includes('UI MOCK DATA'), "Production Admin shell still advertises mock data");
assert(main.includes('PHASE B · RUNTIME INTEGRATED'), "Runtime-integrated Phase B shell badge is missing");
assert(main.includes('return this.renderUnknown(path);'), "Unknown-route guard is missing");
assert(main.includes('if (path === `${ADMIN_BASE}/flags`) return `${ADMIN_BASE}/feature-gates`;'), "Legacy Feature Flags alias is not normalized to canonical Feature Gates route");

// Canonical root and critical routes must resolve to their runtime-backed Phase B owners.
assert(router.includes('if (path === BASE || path === `${BASE}/analytics`) return renderPhaseBTelemetry(path);'), "Overview/Analytics are not routed to runtime telemetry");
assert(router.includes('if (path === `${BASE}/music-library`) return renderPhaseBMusicLibrary();'), "Music Library is not routed to the runtime catalog surface");
assert(router.includes('if (path === `${BASE}/daily-weekly`) return renderPhaseBDailyWeekly();'), "Daily/Weekly is not routed to the canonical runtime-boundary surface");
assert(router.includes('if (path === `${BASE}/feature-gates` || path === `${BASE}/flags`) return renderPhaseBFeatureGates();'), "Feature Gates canonical/legacy route handling is missing");
assert(router.includes('return renderPhaseBCoreAdminScreen(path, navigate);'), "Phase B core fallback for revision-backed screens is missing");

assert(telemetry.includes('/api/admin/space-typing/telemetry/contract'), "Telemetry screen is not bound to the authenticated telemetry contract");
assert(telemetry.includes('RUNTIME-BACKED · SESSION READ ONLY'), "Telemetry runtime boundary badge is missing");
assert(musicLibrary.includes('/api/admin/space-typing/music/library'), "Music Library does not read the canonical Admin music catalog endpoint");
assert(musicLibrary.includes('/api/admin/space-typing/music/upload'), "Music Library upload does not use the canonical Admin asset service");
assert(worldMusic.includes('previewWorldMusic'), "World Music Phase B screen does not use canonical preview resolution");
assert(dailyWeekly.includes('/api/admin/space-typing/daily-weekly/contract'), "Daily/Weekly screen is not bound to the child runtime contract");
assert(featureGates.includes('/api/admin/space-typing/feature-gates/contract') || featureGates.includes('feature-gates'), "Feature Gates runtime ownership surface is missing");
assert(history.includes('validateRevision'), "History/Publish screen does not validate immutable revisions before mutation");

// Interaction/accessibility guards retained from the UI milestone, now against production surfaces.
assert(command.includes('metaKey || event.ctrlKey'), "Cmd/Ctrl+K command shortcut is missing");
assert(command.includes('currentCleanup'), "Command palette listener cleanup is missing");
assert(command.includes('event.key === "Tab"') && command.includes('previousFocus') && command.includes('focusTarget?.focus()'), "Command palette keyboard focus trap/restoration is missing");
assert(command.includes('`${BASE}/feature-gates`'), "Command palette still targets the legacy /flags route");
assert(icons.includes('createElementNS'), "Line SVG Admin icon renderer is missing");
assert(css.includes(':focus-visible'), "Admin focus-visible accessibility style is missing");
assert(css.includes('prefers-reduced-motion'), "Admin reduced-motion handling is missing");
assert(pkg.dependencies?.["@fontsource/exo-2"], "Portal does not bundle Exo 2");
assert(pkg.dependencies?.["@fontsource/be-vietnam-pro"], "Portal does not bundle Be Vietnam Pro");

const forbiddenStatuses = ["backend-foundation", "ui-prototype-not-runtime-connected"];
for (const row of phaseMap.screens) {
  for (const status of forbiddenStatuses) {
    assert(row.status !== status, `Phase B map still contains unfinished status ${status}: ${row.route}`);
  }
  assert(!String(row.status).startsWith("mapped-awaiting-"), `Phase B map still contains mapped-awaiting status: ${row.route}`);
}

const workflowDir = path.join(root, ".github/workflows");
if (fs.existsSync(workflowDir)) {
  for (const entry of fs.readdirSync(workflowDir)) {
    assert(!/admin-ui-.*-once\.ya?ml$/i.test(entry), `Temporary one-shot workflow remains: ${entry}`);
  }
}
for (const entry of fs.readdirSync(path.join(root, "scripts"))) {
  assert(!/^(?:wire|apply)-space-admin-.*\.mjs$/i.test(entry), `Temporary Admin one-shot script remains: ${entry}`);
}

if (failures.length > 0) {
  console.error("Space Typing Admin UI contract validation failed:");
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log(`Space Typing Admin UI contract: PASS (${routes.length} Phase B screens + canonical runtime routing + accessibility/regression guards).`);
