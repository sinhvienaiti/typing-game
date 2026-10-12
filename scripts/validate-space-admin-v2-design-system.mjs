import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const read = (file) => readFile(resolve(root, file), "utf8");

const [help, components, styles, shell] = await Promise.all([
  read("portal/src/admin/v2/admin-help.ts"),
  read("portal/src/admin/v2/admin-components.ts"),
  read("portal/src/admin/v2/admin-v2.css"),
  read("portal/src/admin/space-typing.ts"),
]);

// Tooltip semantics and interaction contract.
assert.match(help, /setAttribute\("role",\s*"tooltip"\)/, "AdminTooltip must expose tooltip semantics.");
assert.match(help, /aria-describedby/, "AdminTooltip must connect help text through aria-describedby.");
assert.match(help, /new AbortController\(\)/, "AdminTooltip listeners must be abortable/cleanable.");
assert.match(help, /pointerenter/, "AdminTooltip must support pointer hover.");
assert.match(help, /addEventListener\("focus"/, "AdminTooltip must support keyboard focus.");
assert.match(help, /event\.key !== "Escape"/, "AdminTooltip must support Escape dismissal.");
assert.match(help, /pointerdown/, "AdminTooltip must support outside pointer/tap dismissal.");
assert.match(help, /window\.addEventListener\("resize"/, "AdminTooltip must reposition on resize.");
assert.match(help, /window\.addEventListener\("scroll"/, "AdminTooltip must reposition on scroll.");
assert.match(help, /placeTooltip/, "AdminTooltip must use collision-aware placement logic.");

// Help drawer semantics and focus lifecycle.
assert.match(help, /setAttribute\("role",\s*"dialog"\)/, "AdminHelpDrawer must expose dialog semantics.");
assert.match(help, /aria-modal/, "AdminHelpDrawer must be modal to assistive technology.");
assert.match(help, /event\.key !== "Tab"/, "AdminHelpDrawer must trap keyboard focus.");
assert.match(help, /previousActive\?\.isConnected/, "AdminHelpDrawer must restore focus when closed.");

// Imperative-DOM route lifecycle cleanup.
assert.match(help, /observeRoot\(root: HTMLElement\)/, "AdminHelpScope must observe the rendered Admin root.");
assert.match(help, /new MutationObserver/, "AdminHelpScope must clean up when the Admin root leaves the DOM.");
assert.match(help, /this\.destroy\(\)/, "AdminHelpScope root observer must destroy stale help surfaces/listeners.");
assert.match(help, /document\.querySelectorAll\("\.st-admin-v2-tooltip,\.st-admin-v2-drawer-backdrop"\)/, "AdminHelpScope must remove stale body-level help surfaces.");
assert.match(help, /createAdminFieldShell/, "A1 must provide a reusable field/help wrapper foundation.");

// Shared screen/state primitives required before domain migration.
for (const primitive of [
  "createAdminPageHeader",
  "createAdminValidationMessage",
  "createAdminEmptyState",
  "createAdminErrorState",
  "createAdminSkeleton",
  "createAdminSearchInput",
  "createAdminFilterBar",
  "createAdminStatusChip",
  "createAdminDraftBar",
  "createAdminEntityTable",
]) {
  assert.match(components, new RegExp(`export function ${primitive}`), `Admin V2 shared primitive is missing: ${primitive}`);
}
assert.match(components, /aria-live/, "Validation messages must expose live-region behavior.");
assert.match(components, /aria-busy/, "Loading state must expose busy semantics.");
assert.match(components, /type = "search"/, "Search primitive must use a semantic search input.");
assert.match(components, /Review Changes/, "Draft lifecycle bar must support reviewing complete change scope before publish.");
assert.match(components, /publishDisabled/, "Draft lifecycle bar must support blocking unsafe publish actions.");
assert.match(components, /th\.scope = "col"/, "Entity table headers must expose column scope.");

// Shell integration: concise primary navigation, contextual help, no native-title-only help.
assert.match(shell, /import "\.\/v2\/admin-v2\.css";/, "Admin shell must load Admin V2 design-system styles.");
assert.match(shell, /AdminHelpScope/, "Admin shell must use the shared AdminHelpScope.");
assert.match(shell, /this\.help\.destroy\(\)/, "Admin shell must teardown previous help state before rerender.");
assert.match(shell, /this\.help\.observeRoot\(root\)/, "Admin shell must teardown help when leaving Admin.");
assert.match(shell, /this\.help\.tooltip\(groupButton/, "Navigation groups must expose contextual tooltip help.");
assert.match(shell, /this\.help\.tooltip\(navButton/, "Navigation items must expose contextual tooltip help.");
assert.match(shell, /this\.help\.infoIcon\(/, "Admin shell must demonstrate the reusable click/tap info trigger.");
assert.doesNotMatch(shell, /\.title\s*=/, "Admin shell must not rely on browser-native title help.");
assert.doesNotMatch(shell, /element\("small",\s*"st-admin-nav-description"/, "Permanent per-item navigation descriptions must be removed from primary DOM.");
assert.doesNotMatch(shell, /element\("small",\s*undefined,\s*group\.description/, "Permanent group descriptions must be removed from primary DOM.");
assert.doesNotMatch(shell, /PHASE B · RUNTIME INTEGRATED/, "Technical Phase B milestone text must not remain in the primary shell.");

// Space Typing visual identity/accessibility.
for (const selector of [
  ".st-admin-v2-tooltip",
  ".st-admin-v2-info",
  ".st-admin-v2-drawer-backdrop",
  ".st-admin-v2-help-drawer",
  ".st-admin-v2-field",
  ".st-admin-v2-page-head",
  ".st-admin-v2-validation",
  ".st-admin-v2-empty-state",
  ".st-admin-v2-error-state",
  ".st-admin-v2-skeleton",
  ".st-admin-v2-filter-bar",
  ".st-admin-v2-table",
  ".st-admin-v2-draft-bar",
]) {
  assert.ok(styles.includes(selector), `Admin V2 styles are missing ${selector}`);
}
assert.match(styles, /var\(--st-admin-accent/, "Admin V2 components must reuse the existing Space Typing color tokens.");
assert.match(styles, /var\(--st-admin-display/, "Admin V2 components must reuse the existing display typography.");
assert.match(styles, /prefers-reduced-motion/, "Admin V2 help must respect reduced-motion preferences.");
assert.match(styles, /\.st-admin-nav-description\{display:none!important\}/, "Legacy permanent navigation helper copy must stay hidden during A1 migration.");

console.log("Admin V2 A1 help/shared-component foundation: OK");
