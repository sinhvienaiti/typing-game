import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const read = (file) => fs.readFileSync(path.join(root, file), "utf8");
const exists = (file) => fs.existsSync(path.join(root, file));

const mainFile = "portal/src/admin/space-typing.ts";
const extendedFile = "portal/src/admin/space-typing-extended.ts";
const worldMusicFile = "portal/src/admin/space-typing-world-music-v2.ts";
const audioPhaseBFile = "portal/src/admin/space-typing-audio-phase-b.ts";
const dailyWeeklyFile = "portal/src/admin/space-typing-daily-weekly.ts";
const commandFile = "portal/src/admin/space-typing-command.ts";
const iconFile = "portal/src/admin/space-typing-icons.ts";
const dialogFile = "portal/src/admin/space-typing-dialogs.ts";
const dialogCssFile = "portal/src/admin/space-typing-dialogs.css";
const uiCssFile = "portal/src/admin/space-typing-ui.css";
const packageFile = "portal/package.json";

for (const file of [mainFile, extendedFile, worldMusicFile, audioPhaseBFile, dailyWeeklyFile, commandFile, iconFile, dialogFile, dialogCssFile, uiCssFile, packageFile]) {
  if (!exists(file)) throw new Error(`Required Admin UI file is missing: ${file}`);
}

const main = read(mainFile);
const extended = read(extendedFile);
const worldMusic = read(worldMusicFile);
const audioPhaseB = read(audioPhaseBFile);
const dailyWeekly = read(dailyWeeklyFile);
const command = read(commandFile);
const icons = read(iconFile);
const dialogs = read(dialogFile);
const css = read(uiCssFile);
const pkg = JSON.parse(read(packageFile));
const rendererSource = [main, extended, worldMusic, dailyWeekly].join("\n");
const allTs = [main, extended, worldMusic, dailyWeekly, command, icons, dialogs].join("\n");

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
  ["Feature Flags", "/flags"],
  ["History & Publish", "/history"],
  ["QA Sandbox", "/qa"],
];

const failures = [];
const assert = (condition, message) => { if (!condition) failures.push(message); };

for (const [label, suffix] of routes) {
  assert(main.includes(`label: "${label}"`), `Navigation is missing ${label}`);
  if (suffix === "") {
    assert(main.includes("if (path === ADMIN_BASE) return this.renderOverview()"), "Overview renderer is missing");
  } else {
    assert(rendererSource.includes(`\`${"${BASE}"}${suffix}\``) || rendererSource.includes(`\`${"${ADMIN_BASE}"}${suffix}\``), `Renderer registration is missing ${label} (${suffix})`);
  }
  assert(command.includes(`"${label}"`), `Command palette is missing ${label}`);
}

assert(!main.includes('phase: "planned"'), "A declared Admin route is still marked PLANNED");
assert(!allTs.includes("location.reload()"), "Admin UI still contains location.reload(), which resets mock interaction state");
assert(!allTs.includes("Object.assign(page, { append:"), "Registry helper still overwrites HTMLElement.append");
assert(!main.includes("renderPlanned("), "Stale planned-screen fallback remains in Admin renderer");
assert(!main.includes("selectedWorldId"), "Stale legacy World Music state remains in Admin renderer");
assert(!main.includes("selectedWorldState"), "Stale legacy World Music role state remains in Admin renderer");
assert(!main.includes("READY_PATHS"), "Dead READY_PATHS route bookkeeping remains");
assert(main.includes("renderUnknown("), "Unknown-route guard is missing");

assert(worldMusic.includes("multi-file playlist"), "Stage-level World Music multi-track UX is missing");
assert(worldMusic.includes("Stage Matrix"), "World Music matrix view is missing");
assert(worldMusic.includes("Fallback chain"), "World Music effective fallback preview is missing");
assert(worldMusic.includes('const fallbackParts: string[] = []') && worldMusic.includes('const galaxyLabel = `Galaxy ${String(state.galaxy).padStart(2, "0")}`') && worldMusic.includes('fallbackParts.join(" → ")'), "World Music fallback trace is not scope-aware");
assert(worldMusic.includes('previous.setAttribute("aria-label", "Previous track")') && worldMusic.includes('next.setAttribute("aria-label", "Next track")'), "World Music symbol-only preview controls need accessible names");
assert(worldMusic.includes("(world - 1) * 20 + 1"), "Selecting a World does not initialize its real first Stage");
assert(command.includes("metaKey || event.ctrlKey"), "Cmd/Ctrl+K command shortcut is missing");
assert(command.includes("currentCleanup"), "Command palette listener cleanup is missing");
assert(command.includes('event.key === "Tab"') && command.includes("previousFocus") && command.includes("focusTarget?.focus()"), "Command palette keyboard focus trap/restoration is missing");
assert(icons.includes("createElementNS"), "Line SVG Admin icon renderer is missing");

assert(main.includes("openMusicUploadMockDialog"), "Music Library upload mock workflow is not wired");
assert(extended.includes("openPublishReviewDialog"), "History publish confirmation workflow is not wired");
assert(extended.includes("openRollbackReviewDialog"), "History rollback confirmation workflow is not wired");
assert(dialogs.includes('fileInput.multiple = true'), "Music upload workflow does not support multi-file selection");
assert(dialogs.includes("Authored Metadata"), "Music upload metadata review is missing");
assert(dialogs.includes("Validation Preview"), "Music upload validation preview is missing");
assert(dialogs.includes("I reviewed the validation result and change summary"), "Publish acknowledgement gate is missing");
assert(dialogs.includes("I understand the active configuration will point to"), "Rollback acknowledgement gate is missing");

assert(audioPhaseB.includes('input.setAttribute("aria-label", label)'), "Audio range aria-label is missing");
assert(audioPhaseB.includes("Existing player settings in spaceTypingSettingsV1 always win"), "Audio default-only player-preference rule is missing");
assert(main.includes('search.setAttribute("aria-label", "Search music library")'), "Music search aria-label is missing");
assert(main.includes('type.setAttribute("aria-label", "Filter music by type")'), "Music type filter aria-label is missing");
assert(main.includes('status.setAttribute("aria-label", "Filter music by status")'), "Music status filter aria-label is missing");
assert(main.includes('play.setAttribute("aria-label", "Play track preview")'), "Music Library symbol-only preview control needs an accessible name");
assert(main.includes('preview.setAttribute("aria-label", `Open ${track.title} track details`)') && main.includes('event.stopPropagation()'), "Music Library table action is not keyboard accessible");
assert(main.includes('control.setAttribute("aria-pressed", String(index === 0))'), "Dashboard segmented aria state is missing");
assert(extended.includes('input.setAttribute("aria-label", label)'), "Extended range aria-label is missing");
assert(extended.includes('control.setAttribute("aria-pressed", String(enabled))'), "Extended toggle aria state is missing");
assert(worldMusic.includes('stageBtn.setAttribute("aria-pressed", String(state.stages.has(stageNumber)))'), "World Music stage aria state is missing");
assert(worldMusic.includes('assignment: "replace" as "inherit" | "replace"'), "World Music assignment mock state is missing");
assert(worldMusic.includes('inherit.setAttribute("aria-pressed", String(state.assignment === "inherit"))') && worldMusic.includes('replace.setAttribute("aria-pressed", String(state.assignment === "replace"))'), "World Music assignment segmented aria state is missing");
assert(worldMusic.includes('Configured: ${configured} · Effective source: ${resolvedSource}'), "World Music effective playlist does not reflect assignment state");
assert(extended.includes('publish.disabled = selectedStatus !== "Draft"'), "History Publish must be limited to Draft revisions");
assert(extended.includes('const rollbackEligible = selectedStatus === "Published" && uiState.selectedRevision !== "r127"'), "History Rollback must be limited to older Published revisions");

assert(css.includes("--holo-display: var(--st-admin-display)"), "Game Holo token aliases are missing");
assert(css.includes(":focus-visible"), "Admin focus-visible accessibility style is missing");
assert(css.includes("prefers-reduced-motion"), "Admin reduced-motion handling is missing");
assert(pkg.dependencies?.["@fontsource/exo-2"], "Portal does not bundle Exo 2");
assert(pkg.dependencies?.["@fontsource/be-vietnam-pro"], "Portal does not bundle Be Vietnam Pro");

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

console.log(`Space Typing Admin UI contract: PASS (${routes.length} registered screens + operational mock workflows + final A11y/state guards).`);
