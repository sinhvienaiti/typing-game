import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const read = (file) => fs.readFileSync(path.join(root, file), "utf8");
const exists = (file) => fs.existsSync(path.join(root, file));

const mainFile = "portal/src/admin/space-typing.ts";
const extendedFile = "portal/src/admin/space-typing-extended.ts";
const worldMusicFile = "portal/src/admin/space-typing-world-music-v2.ts";
const dailyWeeklyFile = "portal/src/admin/space-typing-daily-weekly.ts";
const commandFile = "portal/src/admin/space-typing-command.ts";
const iconFile = "portal/src/admin/space-typing-icons.ts";
const uiCssFile = "portal/src/admin/space-typing-ui.css";
const packageFile = "portal/package.json";

for (const file of [mainFile, extendedFile, worldMusicFile, dailyWeeklyFile, commandFile, iconFile, uiCssFile, packageFile]) {
  if (!exists(file)) throw new Error(`Required Admin UI file is missing: ${file}`);
}

const main = read(mainFile);
const extended = read(extendedFile);
const worldMusic = read(worldMusicFile);
const dailyWeekly = read(dailyWeeklyFile);
const command = read(commandFile);
const icons = read(iconFile);
const css = read(uiCssFile);
const pkg = JSON.parse(read(packageFile));
const rendererSource = [main, extended, worldMusic, dailyWeekly].join("\n");
const allTs = [main, extended, worldMusic, dailyWeekly, command, icons].join("\n");

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
  assert(command.includes(`"${label}"`) || label === "Daily / Weekly", `Command palette is missing ${label}`);
}

assert(!main.includes('phase: "planned"'), "A declared Admin route is still marked PLANNED");
assert(!allTs.includes("location.reload()"), "Admin UI still contains location.reload(), which resets mock interaction state");
assert(!allTs.includes("Object.assign(page, { append:"), "Registry helper still overwrites HTMLElement.append");
assert(!main.includes("renderPlanned("), "Stale planned-screen fallback remains in Admin renderer");
assert(main.includes("renderUnknown("), "Unknown-route guard is missing");
assert(worldMusic.includes("multi-file playlist"), "Stage-level World Music multi-track UX is missing");
assert(worldMusic.includes("Stage Matrix"), "World Music matrix view is missing");
assert(worldMusic.includes("Fallback chain"), "World Music effective fallback preview is missing");
assert(command.includes("metaKey || event.ctrlKey"), "Cmd/Ctrl+K command shortcut is missing");
assert(icons.includes("createElementNS"), "Line SVG Admin icon renderer is missing");
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
  assert(!/^wire-space-admin-.*\.mjs$/i.test(entry), `Temporary Admin wiring script remains: ${entry}`);
}

if (failures.length > 0) {
  console.error("Space Typing Admin UI contract validation failed:");
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log(`Space Typing Admin UI contract: PASS (${routes.length} registered screens).`);
