import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { createRequire } from "node:module";
import vm from "node:vm";

const root = resolve(import.meta.dirname, "..");
const read = (path) => readFileSync(resolve(root, path), "utf8");
const require = createRequire(resolve(root, "portal/package.json"));
const ts = require("typescript");
// Execute the real area definitions, redirect function and both legacy routers.
// Leaf DOM renderers are stubs: this verifies route resolution, not visual QA.
const modules = new Set([
  "portal/src/admin/admin-shell.ts",
  "portal/src/admin/areas/registry.ts",
  "portal/src/admin/areas/space-typing.ts",
  "portal/src/admin/areas/shared.ts",
  "portal/src/admin/space-typing-phase-b.ts",
  "portal/src/admin/space-typing-phase-b-core.ts",
].map((path) => resolve(root, path)));
const cache = new Map();
const attachCalls = [];
function load(file) {
  if (cache.has(file)) return cache.get(file).exports;
  const module = { exports: {} };
  cache.set(file, module);
  const js = ts.transpileModule(readFileSync(file, "utf8"), { compilerOptions: { target: ts.ScriptTarget.ES2022, module: ts.ModuleKind.CommonJS } }).outputText;
  const localRequire = (name) => {
    const target = resolve(dirname(file), `${name}.ts`);
    if (modules.has(target)) return load(target);
    return new Proxy({}, { get: (_object, key) => {
      if (key === "__esModule") return true;
      if (String(key).startsWith("attach")) return (screen, ...args) => { attachCalls.push([String(key), screen?.renderer, ...args]); return screen; };
      return function () { return { renderer: String(key) }; };
    } });
  };
  vm.runInNewContext(`(function(require, module, exports) { ${js}\n})`, {}, { filename: file })(localRequire, module, module.exports);
  return module.exports;
}
const registry = load(resolve(root, "portal/src/admin/areas/registry.ts"));
const shell = load(resolve(root, "portal/src/admin/admin-shell.ts"));
const { ADMIN_AREAS, ADMINISTRATION, areaForPath, renderAdministrationPage } = registry;
const context = { navigate() {}, help: {} };
const render = (path) => {
  const normalized = shell.normalizedAdminPath(path);
  return renderAdministrationPage(normalized, context) ?? areaForPath(normalized).renderPage(normalized, context);
};
assert.deepEqual(Array.from(ADMIN_AREAS, (area) => area.id), ["shared", "space-typing"], "Only implemented areas belong in the registry");
for (const area of ADMIN_AREAS) {
  for (const field of ["id", "label", "base", "navGroups", "renderPage"]) assert.ok(area[field], `${area.id}: missing ${field}`);
  assert.ok(area.renderPage(area.base, context), `${area.id}: base route has no renderer`);
}
assert.equal(shell.normalizedAdminPath("/admin"), "/admin/shared");
assert.equal(shell.normalizedAdminPath("/admin/"), "/admin/shared");
assert.equal(shell.normalizedAdminPath("/admin/space-typing/media/"), "/admin/media");
for (const [from, to] of Object.entries({
  "/admin/space-typing/media": "/admin/media",
  "/admin/space-typing/roles": "/admin/roles",
  "/admin/space-typing/typing-content": "/admin/shared/learning-content",
  "/admin/space-typing/flags": "/admin/space-typing/feature-gates",
})) {
  assert.equal(shell.normalizedAdminPath(from), to);
  assert.ok(render(from), `Legacy route has no renderer: ${from}`);
  if (!from.endsWith("/flags")) assert.equal(shell.ADMIN_ROUTE_REDIRECTS[from], to, "Moved routes must be in the redirect table");
}
const shellSource = read("portal/src/admin/admin-shell.ts");
assert.match(shellSource, /history\.replaceState/);
assert.match(shellSource, /const groups = \[\.\.\.area\.navGroups, ADMINISTRATION\]/, "Administration must be last in every area");
assert.equal(ADMINISTRATION.label, "Administration");
assert.deepEqual(Array.from(ADMINISTRATION.items, (item) => item.path), ["/admin/media", "/admin/roles"]);
let navCount = 0;
for (const area of ADMIN_AREAS) {
  for (const group of [...area.navGroups, ADMINISTRATION]) {
    for (const item of group.items) {
      assert.ok(render(item.path), `${area.label}: dead navigation route ${item.path}`);
      assert.doesNotMatch(item.path, /\/audit$|keyboard-sounds|typing-effects|\/release$/);
      navCount++;
    }
  }
}
const legacy = JSON.parse(read("admin/space-typing-phase-b-map.v1.json")).screens.map((row) => row.route);
legacy.push("/admin/space-typing/media", "/admin/space-typing/roles", "/admin/space-typing/players", "/admin/space-typing/liveops-mail", "/admin/space-typing/chat", "/admin/space-typing/feedback", "/admin/space-typing/developer-tools", "/admin/space-typing/flags");
for (const path of legacy) assert.ok(render(path), `Unresolved old URL: ${path}`);
for (const path of ["/admin/shared/not-a-page", "/admin/space-typing/not-a-page", "/admin/audit"]) assert.equal(render(path), null, `Unknown route incorrectly resolves: ${path}`);
const main = read("portal/src/main.ts");
assert.match(main, /makeButton\("Admin", "\/admin"\)/);
assert.doesNotMatch(main, /Space Admin/);
assert.match(main, /path === "\/admin" \|\| path\.startsWith\("\/admin\/"\)/);
assert.match(main, /from "\.\/admin\/admin-shell"/);
const command = read("portal/src/admin/space-typing-command.ts");
for (const path of ["/admin/shared", "/admin/shared/learning-content", "/admin/media", "/admin/roles"]) assert.ok(command.includes(`"${path}"`), `Command palette missing ${path}`);
assert.match(command, /"\/admin\/shared\/learning-content": "Typing Content\b/, "Searching the old name Typing Content must find Learning Content");
assert.match(command, /COMMAND_KEYWORDS\[path\]/, "Command search must include the hidden keywords");

// Administration pages keep the area they were opened from; a direct load starts in All games.
assert.equal(areaForPath("/admin/media").id, "shared");
assert.equal(areaForPath("/admin/roles", "space-typing").id, "space-typing");
assert.equal(areaForPath("/admin/media", "retired-area").id, "shared");
assert.equal(areaForPath("/admin/space-typing/ships", "shared").id, "space-typing");
const sessionStore = new Map();
const session = () => ({ getItem: (key) => sessionStore.get(key) ?? null, setItem: (key, value) => sessionStore.set(key, String(value)) });
const areaIds = (memory, paths) => paths.map((path) => memory.areaFor(shell.normalizedAdminPath(path)).id);
const tab = new shell.AdminAreaMemory(session);
assert.deepEqual(areaIds(tab, ["/admin/space-typing/ships", "/admin/media", "/admin/roles", "/admin/space-typing/media"]), Array(4).fill("space-typing"), "Media/Roles from the Space sidebar keep Space");
assert.deepEqual(areaIds(new shell.AdminAreaMemory(session), ["/admin/roles"]), ["space-typing"], "A reload in the same tab keeps the area");
assert.deepEqual(areaIds(tab, ["/admin/shared", "/admin/media"]), ["shared", "shared"]);
assert.deepEqual(areaIds(new shell.AdminAreaMemory(() => ({ getItem: () => null, setItem() {} })), ["/admin/media"]), ["shared"], "Direct load defaults to All games");
const blocked = new shell.AdminAreaMemory(() => { throw new Error("storage blocked"); });
assert.deepEqual(areaIds(blocked, ["/admin/roles", "/admin/space-typing", "/admin/media"]), ["shared", "space-typing", "space-typing"], "Blocked storage still remembers in memory");
assert.equal(new shell.AdminAreaMemory().areaFor("/admin/media").id, "shared", "No sessionStorage global: falls back to All games");
assert.match(shellSource, /private readonly areas = new AdminAreaMemory\(\)/);
assert.match(shellSource, /isAdministrationPath\(path\) \? "Administration"/, "Administration breadcrumb stays");

// Space pages probe the cheap status route, never the Typing Feel overview.
assert.match(shellSource, /getAdminStatus\(\)/);
assert.doesNotMatch(shellSource, /getSharedOverview/, "The shell must not wait on the overview (it reads Typing Feel files)");
assert.ok(shellSource.includes("Space Typing failed to start — see the Admin server log"));
assert.ok(shellSource.includes("Space Typing is not checked out"));
assert.match(shellSource, /selector\.setAttribute\("role", "group"\)/);
assert.match(shellSource, /"st-admin-brand-logo", "TG"/);

// Learning Content keeps the Phase B decoration it had in the Space area.
attachCalls.length = 0;
assert.ok(render("/admin/shared/learning-content"));
assert.deepEqual(attachCalls.map(([name, renderer, ...args]) => [name, renderer, ...args]), [
  ["attachProductionPreviewClassification", "renderPhaseBTypingContent", "/admin/shared/learning-content"],
  ["attachRoleAwareActionGates", "renderPhaseBTypingContent"],
]);
const classification = load(resolve(root, "portal/src/admin/v2/preview/preview-classification.ts"));
assert.equal(classification.productionPreviewClassification("/admin/shared/learning-content")?.kind, "not-applicable");
console.log(`Admin shared IA: PASS (${ADMIN_AREAS.length} areas, ${navCount} nav entries, ${legacy.length} old URLs; real routers with leaf DOM renderers stubbed).`);
