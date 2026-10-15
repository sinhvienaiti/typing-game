import fs from "node:fs";
import path from "node:path";
import { createDeveloperToolsManifest } from "../admin/developer-tools.mjs";

const root = process.cwd();
const read = (file) => fs.readFileSync(path.join(root, file), "utf8");
const exists = (file) => fs.existsSync(path.join(root, file));

const mainFile = "portal/src/admin/space-typing.ts";
const routerFile = "portal/src/admin/space-typing-phase-b.ts";
const coreFile = "portal/src/admin/space-typing-phase-b-core.ts";
const telemetryFile = "portal/src/admin/space-typing-telemetry-phase-b.ts";
const musicLibraryFile = "portal/src/admin/space-typing-music-library-phase-b.ts";
const sfxFile = "portal/src/admin/space-typing-sfx-phase-b.ts";
const worldMusicFile = "portal/src/admin/space-typing-world-music-phase-b.ts";
const dailyWeeklyFile = "portal/src/admin/space-typing-daily-weekly-phase-b.ts";
const featureGatesFile = "portal/src/admin/space-typing-feature-gates-phase-b.ts";
const historyFile = "portal/src/admin/space-typing-history-phase-b.ts";
const commandFile = "portal/src/admin/space-typing-command.ts";
const iconFile = "portal/src/admin/space-typing-icons.ts";
const uiCssFile = "portal/src/admin/space-typing-ui.css";
const phaseBCssFile = "portal/src/admin/space-typing-phase-b.css";
const v2HelpFile = "portal/src/admin/v2/admin-help.ts";
const v2CssFile = "portal/src/admin/v2/admin-v2.css";
const phaseMapFile = "admin/space-typing-phase-b-map.v1.json";
const packageFile = "portal/package.json";

const requiredFiles = [
  mainFile,
  routerFile,
  coreFile,
  telemetryFile,
  musicLibraryFile,
  sfxFile,
  worldMusicFile,
  dailyWeeklyFile,
  featureGatesFile,
  historyFile,
  commandFile,
  iconFile,
  uiCssFile,
  phaseBCssFile,
  v2HelpFile,
  v2CssFile,
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
const sfx = read(sfxFile);
const worldMusic = read(worldMusicFile);
const dailyWeekly = read(dailyWeeklyFile);
const featureGates = read(featureGatesFile);
const history = read(historyFile);
const command = read(commandFile);
const icons = read(iconFile);
const css = read(uiCssFile);
const phaseBCss = read(phaseBCssFile);
const v2Help = read(v2HelpFile);
const v2Css = read(v2CssFile);
const phaseMap = JSON.parse(read(phaseMapFile));
const pkg = JSON.parse(read(packageFile));
const developerManifest = createDeveloperToolsManifest();

const failures = [];
const assert = (condition, message) => { if (!condition) failures.push(message); };

const routes = [
  ["Overview", ""],
  ["Analytics", "/analytics"],
  ["Audio Defaults", "/audio"],
  ["Music Library", "/music-library"],
  ["SFX", "/sfx"],
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
  ["Live Ops", "/events"],
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

const primaryRoutes = new Map([
  ["Overview", ""],
  ["Audio Defaults", "/audio"],
  ["Music Library", "/music-library"],
  ["SFX", "/sfx"],
  ["World / Stage Music", "/world-music"],
  ["Ships", "/ships"],
  ["Equipment", "/equipment"],
  ["Skills", "/skills"],
  ["Enemies", "/enemies"],
  ["Bosses", "/bosses"],
  ["Worlds & Stages", "/stages"],
  ["Typing Content", "/typing-content"],
  ["Shop", "/shop"],
  ["Live Ops", "/events"],
  ["General Settings", "/settings"],
  ["History & Publish", "/history"],
]);
const v2OnlyPrimaryRoutes = new Map([
  ["Media Library", "/media"],
  ["Roles & Permissions", "/roles"],
]);
const developerRoutes = new Map(routes.filter(([label]) => !primaryRoutes.has(label)));
const developerManifestPaths = new Set(
  developerManifest.sections.flatMap((section) => section.tools.map((tool) => tool.path)),
);

assert(Array.isArray(phaseMap.screens), "Phase B map screens are missing");
assert(phaseMap.screens.length === routes.length, `Phase B map must contain exactly ${routes.length} registered legacy/canonical routes during A2 migration`);

// A2/A11/A15 navigation contract: administrator workflows stay primary; diagnostics stay permission-gated.
for (const [label, suffix] of primaryRoutes) {
  assert(main.includes(`label: "${label}"`), `Primary administrator navigation is missing ${label}`);
  if (suffix === "") {
    assert(main.includes("path: ADMIN_BASE"), "Overview canonical primary path is missing");
  } else {
    assert(main.includes(`path: \`\${ADMIN_BASE}${suffix}\``), `Primary administrator navigation path is missing ${label} (${suffix})`);
  }
  assert(command.includes(`"${label}"`), `Primary command palette is missing ${label}`);
}
for (const [label, suffix] of v2OnlyPrimaryRoutes) {
  assert(main.includes(`label: "${label}"`), `Admin V2 primary navigation is missing ${label}`);
  assert(main.includes(`path: \`\${ADMIN_BASE}${suffix}\``), `Admin V2 primary navigation path is missing ${label} (${suffix})`);
  assert(command.includes(`"${label}"`), `Primary command palette is missing ${label}`);
}

for (const [label, suffix] of developerRoutes) {
  const absolutePath = `/admin/space-typing${suffix}`;
  const legacyKey = '[`${ADMIN_BASE}' + suffix + '`]';
  assert(!main.includes(`label: "${label}"`), `${label} must not be restored as a primary administrator navigation item`);
  assert(command.includes(`"${label}"`), `Developer command palette is missing ${label}`);
  assert(developerManifestPaths.has(absolutePath), `Developer Tools manifest is missing ${label} (${absolutePath})`);
  assert(main.includes(legacyKey), `Legacy breadcrumb/direct-route metadata is missing ${label} (${suffix})`);
}
assert(!developerManifestPaths.has("/admin/space-typing/shop"), "Shop must remain an administrator workflow rather than a Developer Tools-only surface");
assert(main.includes('label: "Developer Tools"'), "Primary navigation is missing permission-gated Developer Tools entry");
assert(main.includes('requiredPermission: DEVELOPER_PERMISSION'), "Developer Tools primary entry is not permission-gated");

// The shell must still delegate to canonical Phase B runtime owners while V2 migrates presentation incrementally.
assert(main.includes('const phaseB = renderPhaseBAdminScreen(path, this.navigate);'), "Main Admin shell does not delegate legacy/direct routes to the Phase B router");
assert(main.includes('if (phaseB !== null) return phaseB;'), "Main Admin shell does not return the canonical Phase B renderer result");
assert(main.includes('if (path === ADMIN_BASE) return renderAdminV2Dashboard'), "Admin root does not render the real-data V2 Dashboard before Phase B fallback");
assert(main.includes('if (path === `${ADMIN_BASE}/developer-tools`) return renderAdminV2DeveloperTools'), "Developer Tools hub route is missing");
assert(!main.includes('if (path === ADMIN_BASE) return this.renderOverview()'), "Legacy mock Overview still preempts Dashboard V2");
assert(!main.includes('renderExtendedAdminScreen'), "Legacy extended renderer remains reachable from the production Admin shell");
assert(!main.includes('renderWorldMusicV2'), "Legacy World Music mock renderer remains reachable from the production Admin shell");
assert(!main.includes('renderDailyWeekly'), "Legacy Daily/Weekly mock renderer remains reachable from the production Admin shell");
assert(!main.includes('openMusicUploadMockDialog'), "Legacy Music Library mock workflow remains reachable from the production Admin shell");
assert(!main.includes('space-typing-mock'), "Production Admin shell still imports mock data");
assert(!main.includes('UI MOCK DATA'), "Production Admin shell still advertises mock data");
assert(main.includes('return this.renderUnknown(path);'), "Unknown-route guard is missing");
assert(main.includes('if (path === `${ADMIN_BASE}/flags`) return `${ADMIN_BASE}/feature-gates`;'), "Legacy Feature Flags alias is not normalized to canonical Feature Gates route");

// A1/A2 shell behavior: permanent developer-style helper copy is replaced with reusable contextual help.
assert(main.includes('import "./v2/admin-v2.css";'), "Admin V2 styles are not loaded by the canonical shell");
assert(main.includes('AdminHelpScope'), "Canonical shell does not use the Admin V2 help scope");
assert(main.includes('this.help.tooltip(groupButton'), "Navigation groups are missing shared tooltip help");
assert(main.includes('this.help.tooltip(navButton'), "Navigation items are missing shared tooltip help");
assert(main.includes('this.help.infoIcon({'), "Topbar does not use the shared click/tap info icon");
assert(main.includes('this.help.observeRoot(root);'), "Admin V2 help surfaces are not tied to root teardown");
assert(!main.includes('PHASE B · RUNTIME INTEGRATED'), "Technical Phase B milestone text leaked back into the primary shell");
assert(!main.includes('element("small", "st-admin-nav-description"'), "Permanent navigation short descriptions leaked back into the primary shell");
assert(!main.includes('groupButton.title ='), "Navigation group help regressed to browser-native title text");
assert(!main.includes('navButton.title ='), "Navigation item help regressed to browser-native title text");
assert(!main.includes('runtime.title ='), "Topbar help regressed to browser-native title text");
assert(v2Help.includes('aria-describedby'), "Admin V2 tooltip is missing accessible help association");
assert(v2Help.includes('new AbortController()'), "Admin V2 tooltip listeners are not explicitly cleanable");
assert(v2Help.includes('new MutationObserver'), "Admin V2 help scope does not clean up when leaving Admin");
assert(v2Css.includes('.st-admin-v2-tooltip'), "Admin V2 tooltip styling is missing");
assert(v2Css.includes('.st-admin-v2-info'), "Admin V2 info-icon styling is missing");
assert(v2Css.includes('prefers-reduced-motion'), "Admin V2 help system does not respect reduced-motion preferences");

// Shared presentation dependencies must be owned by the canonical shell, never by dead mock modules.
assert(main.includes('import "./space-typing-phase-b.css";'), "Canonical Admin shell does not load shared Phase B styles");
for (const fontImport of [
  '@fontsource/exo-2/600.css',
  '@fontsource/exo-2/700.css',
  '@fontsource/exo-2/800.css',
  '@fontsource/be-vietnam-pro/400.css',
  '@fontsource/be-vietnam-pro/500.css',
  '@fontsource/be-vietnam-pro/600.css',
  '@fontsource/be-vietnam-pro/700.css',
]) {
  assert(main.includes(`import "${fontImport}";`), `Canonical Admin shell is missing bundled font import ${fontImport}`);
}
for (const selector of [".stx-panel", ".stx-grid", ".stx-field", ".stx-notice", ".stx-revision-list"]) {
  assert(phaseBCss.includes(selector), `Canonical Phase B stylesheet is missing ${selector}`);
}
const forbiddenLegacyFiles = [
  "portal/src/admin/space-typing-mock.ts",
  "portal/src/admin/space-typing-extended.ts",
  "portal/src/admin/space-typing-extended.css",
  "portal/src/admin/space-typing-daily-weekly.ts",
  "portal/src/admin/space-typing-dialogs.ts",
  "portal/src/admin/space-typing-dialogs.css",
  "portal/src/admin/space-typing-world-music-v2.ts",
];
for (const file of forbiddenLegacyFiles) {
  assert(!exists(file), `Dead legacy Admin module must be removed: ${file}`);
}

// Canonical routes are decorated centrally so preview classification and role-aware gates cannot be bypassed.
assert(router.includes('attachProductionPreviewClassification(screen, path);'), "Phase B router no longer applies production-preview classification centrally");
assert(router.includes('attachRoleAwareActionGates(screen);'), "Phase B router no longer applies role-aware action gates centrally");
assert(router.includes('if (path === BASE || path === `${BASE}/analytics`) return decorated(path, renderPhaseBTelemetry(path));'), "Overview/Analytics canonical telemetry owner is missing");
assert(router.includes('if (path === `${BASE}/music-library`) return decorated(path, renderPhaseBMusicLibrary());'), "Music Library is not routed to the runtime catalog surface");
assert(router.includes('if (path === `${BASE}/sfx`) return decorated(path, renderPhaseBSfx());'), "SFX is not routed to the production sample catalog surface");
assert(router.includes('if (path === `${BASE}/daily-weekly`) return decorated(path, renderPhaseBDailyWeekly());'), "Daily/Weekly is not routed to the canonical runtime-boundary surface");
assert(router.includes('if (path === `${BASE}/feature-gates` || path === `${BASE}/flags`) return decorated(path, renderPhaseBFeatureGates());'), "Feature Gates canonical/legacy route handling is missing");
assert(router.includes('return decorated(path, renderPhaseBCoreAdminScreen(path, navigate));'), "Phase B core fallback for revision-backed screens is missing");

assert(telemetry.includes('/api/admin/space-typing/telemetry/contract'), "Telemetry screen is not bound to the authenticated telemetry contract");
assert(telemetry.includes('RUNTIME-BACKED · READ ONLY'), "Telemetry runtime read-only badge is missing");
assert(telemetry.includes('LOCAL PROFILE HISTORY'), "Telemetry local-profile historical ownership badge is missing");
assert(telemetry.includes('NO CENTRAL BACKEND'), "Telemetry central-backend boundary badge is missing");
assert(!telemetry.includes('NO HISTORICAL BACKEND'), "Telemetry screen still claims historical analytics are absent even though local-profile history exists");
assert(musicLibrary.includes('/api/admin/space-typing/music/library'), "Music Library does not read the canonical Admin music catalog endpoint");
assert(musicLibrary.includes('/api/admin/space-typing/music/upload'), "Music Library upload does not use the canonical Admin asset service");
assert(sfx.includes('createAdminSfxCatalog'), "SFX screen does not use the pinned child production SAMPLE_SFX read model");
assert(sfx.includes('RUNTIME-BACKED · READ ONLY'), "SFX read-only runtime badge is missing");
assert(sfx.includes('TEST PLAYBACK'), "SFX Test Playback capability is missing");
assert(sfx.includes('NO FAKE SFX POLICY'), "SFX unsupported-authoring boundary is not visible");
assert(sfx.includes('new Audio(productionSampleUrl'), "SFX preview does not play the canonical production asset URL");
assert(!sfx.includes('createRevision') && !sfx.includes('/publish') && !sfx.includes('/revisions'), "SFX page must not expose fake revision/publish authoring");
assert(worldMusic.includes('previewWorldMusic'), "World Music Phase B screen does not use canonical preview resolution");
assert(dailyWeekly.includes('/api/admin/space-typing/daily-weekly/contract'), "Daily/Weekly screen is not bound to the child runtime contract");
assert(featureGates.includes('/api/admin/space-typing/feature-gates/contract') || featureGates.includes('feature-gates'), "Feature Gates runtime ownership surface is missing");
assert(history.includes('validateRevision'), "History/Publish screen does not validate immutable revisions before mutation");

// Interaction/accessibility guards retained from the UI milestone, now against production surfaces.
assert(command.includes('metaKey || event.ctrlKey'), "Cmd/Ctrl+K command shortcut is missing");
assert(command.includes('currentCleanup'), "Command palette listener cleanup is missing");
assert(command.includes('event.key === "Tab"') && command.includes('previousFocus') && command.includes('focusTarget?.focus()'), "Command palette keyboard focus trap/restoration is missing");
assert(command.includes('`${BASE}/feature-gates`'), "Permission-aware command palette lost the Feature Gates direct route");
assert(command.includes('const PRIMARY_COMMANDS =') && command.includes('const DEVELOPER_COMMANDS ='), "Command palette does not separate administrator and developer concepts");
assert(command.includes('options.includeDeveloperTools'), "Developer commands are not permission-aware");
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

console.log(`Space Typing Admin UI contract: PASS (${routes.length} canonical Phase B routes preserved; administrator primary navigation separated from permission-gated Developer Tools).`);
