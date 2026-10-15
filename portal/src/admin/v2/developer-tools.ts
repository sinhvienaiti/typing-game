import "./developer-tools.css";
import { SpaceTypingAdminApi, type DeveloperToolsManifest } from "../api";
import { adminErrorMessage } from "../admin-http";
import type { AdminHelpScope } from "./admin-help";
import {
  createAdminCardGrid,
  createAdminErrorState,
  createAdminPageHeader,
  createAdminSkeleton,
  createAdminStatusChip,
} from "./admin-components";

const api = new SpaceTypingAdminApi();
const CONTRACTS = Object.freeze([
  ["Events / Live Ops", "/api/admin/space-typing/events/contract"],
  ["Duel", "/api/admin/space-typing/duel/contract"],
  ["Ranked", "/api/admin/space-typing/ranked/contract"],
  ["Alternative Modes", "/api/admin/space-typing/alternative-modes/contract"],
  ["Backgrounds", "/api/admin/space-typing/backgrounds/contract"],
  ["VFX", "/api/admin/space-typing/vfx/contract"],
  ["UI Assets", "/api/admin/space-typing/ui-assets/contract"],
  ["QA Sandbox", "/api/admin/space-typing/qa/contract"],
] as const);

function element<K extends keyof HTMLElementTagNameMap>(tag: K, className?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className !== undefined) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}
function notice(text: string, tone: "good" | "warn" | "bad" | "info" = "info"): HTMLElement {
  return element("div", `stx-notice ${tone}`, text);
}
function renderManifest(body: HTMLElement, manifest: DeveloperToolsManifest, navigate: (path: string) => void): void {
  const sections = manifest.sections.map((section) => {
    const card = element("section", "st-admin-v2-dev-card");
    const head = element("div", "st-admin-v2-dev-card-head");
    head.append(element("h2", undefined, section.label), createAdminStatusChip("Developer", "warn"));
    card.append(head, element("p", "st-admin-v2-dev-description", section.description));
    const tools = element("div", "st-admin-v2-dev-links");
    for (const tool of section.tools) {
      const button = element("button", "st-admin-v2-dev-link");
      button.type = "button";
      const copy = element("span");
      copy.append(element("strong", undefined, tool.label), element("small", undefined, tool.description));
      button.append(copy, element("span", "st-admin-v2-dev-arrow", "→"));
      button.addEventListener("click", () => navigate(tool.path));
      tools.append(button);
    }
    card.append(tools);
    return card;
  });
  body.replaceChildren(createAdminCardGrid(...sections));
}

function createInspector(navigate: (path: string) => void): HTMLElement {
  const shell = element("div", "stx-grid");

  const runtime = element("section", "st-admin-panel solid stx-panel");
  const runtimeHead = element("div", "st-admin-panel-head");
  runtimeHead.append(element("div", undefined, "Runtime Inspector"));
  const runtimeBody = element("div", "stx-stack");
  runtime.append(runtimeHead, runtimeBody);

  const contracts = element("section", "st-admin-panel solid stx-panel");
  const contractHead = element("div", "st-admin-panel-head");
  contractHead.append(element("div", undefined, "Contract Inspector"));
  const select = element("select", "st-admin-select") as HTMLSelectElement;
  for (const [label, path] of CONTRACTS) select.append(new Option(label, path));
  const inspect = element("button", "st-admin-btn", "Inspect contract") as HTMLButtonElement;
  inspect.type = "button";
  const contractOutput = element("pre", "stx-diff");
  contractOutput.textContent = "Choose a canonical contract to inspect.";
  contractHead.append(select, inspect);
  contracts.append(contractHead, contractOutput);

  const validation = element("section", "st-admin-panel solid stx-panel");
  const validationHead = element("div", "st-admin-panel-head");
  validationHead.append(element("div", undefined, "Validation"));
  const validate = element("button", "st-admin-btn", "Validate published revision") as HTMLButtonElement;
  validate.type = "button";
  validationHead.append(validate);
  const validationBody = notice("Validation has not been run.");
  validation.append(validationHead, validationBody);

  const assets = element("section", "st-admin-panel solid stx-panel");
  assets.append(
    element("h2", undefined, "Asset Diagnostics"),
    notice("Media provenance, background composition, representative production VFX and UI asset diagnostics are centralized under Developer Tools."),
  );
  const assetActions = element("div", "st-admin-page-actions");
  for (const [label, path] of [["Media Library", "/admin/space-typing/media"], ["Backgrounds", "/admin/space-typing/backgrounds"], ["VFX", "/admin/space-typing/vfx"], ["UI Assets", "/admin/space-typing/ui-assets"]] as const) {
    const button = element("button", "st-admin-btn", label) as HTMLButtonElement;
    button.type = "button";
    button.addEventListener("click", () => navigate(path));
    assetActions.append(button);
  }
  assets.append(assetActions);

  const qa = element("section", "st-admin-panel solid stx-panel");
  qa.append(element("h2", undefined, "QA Sandbox"), notice("Isolated test scenarios live here rather than in normal administrator workflows."));
  const qaButton = element("button", "st-admin-btn", "Open QA Sandbox") as HTMLButtonElement;
  qaButton.type = "button";
  qaButton.addEventListener("click", () => navigate("/admin/space-typing/qa"));
  qa.append(qaButton);

  inspect.addEventListener("click", () => {
    inspect.disabled = true;
    contractOutput.textContent = "Loading canonical contract…";
    void api.requestJson<unknown>(select.value).then((value) => {
      contractOutput.textContent = JSON.stringify(value, null, 2);
    }).catch((error: unknown) => {
      contractOutput.textContent = adminErrorMessage(error, "Contract could not be loaded.");
    }).finally(() => { inspect.disabled = false; });
  });

  validate.addEventListener("click", () => {
    validate.disabled = true;
    validationBody.className = "stx-notice info";
    validationBody.textContent = "Validating the current published revision…";
    void api.getState().then((state) => api.validateRevision(state.state.activeRevision)).then((result) => {
      validationBody.className = "stx-notice good";
      validationBody.textContent = `PASS · ${result.revision} · relation ${result.relation} · ${result.changeScope?.changedPathCount ?? 0} scoped changes.`;
    }).catch((error: unknown) => {
      validationBody.className = "stx-notice bad";
      validationBody.textContent = adminErrorMessage(error, "Validation failed.");
    }).finally(() => { validate.disabled = false; });
  });

  void Promise.all([api.getActor(), api.getState(), api.getRuntime()]).then(([actor, state, runtimePayload]) => {
    if (!runtime.isConnected) return;
    runtimeBody.replaceChildren(
      notice(`${actor.actorDisplayName} · role ${actor.role} · ${actor.permissions.length} effective permissions`, "good"),
      notice(`Published revision: ${state.state.activeRevision} · generation ${state.state.generation}`),
      notice(`Runtime revision: ${runtimePayload.activeRevision} · config schema ${runtimePayload.config.configSchemaVersion}`),
    );
  }).catch((error: unknown) => {
    if (!runtime.isConnected) return;
    runtimeBody.replaceChildren(notice(adminErrorMessage(error, "Runtime inspection unavailable."), "bad"));
  });

  shell.append(runtime, contracts, validation, assets, qa);
  return shell;
}

function renderAuthorizedDeveloperTools(
  root: HTMLElement,
  manifest: DeveloperToolsManifest,
  navigate: (path: string) => void,
): void {
  const warning = element("div", "st-admin-v2-dev-warning");
  warning.append(createAdminStatusChip("Technical", "warn"), element("span", undefined, "Raw JSON and implementation ownership belong here, not on primary administrator screens."));

  const directoryHead = element("h2", undefined, "Diagnostic Directory");
  const body = element("div", "st-admin-v2-dev-body");
  renderManifest(body, manifest, navigate);

  root.append(warning, createInspector(navigate), directoryHead, body);
}

export function renderAdminV2DeveloperTools(navigate: (path: string) => void, helpScope: AdminHelpScope): HTMLElement {
  const root = element("section", "st-admin-v2-developer-tools");
  root.append(createAdminPageHeader({
    eyebrow: "System",
    title: "Developer Tools",
    subtitle: "Runtime Inspector, Contract Inspector, Validation, Asset Diagnostics and QA Sandbox are centralized here so normal administrator workflows stay product-focused.",
    helpScope,
    help: {
      title: "Developer-only area",
      content: "These tools intentionally expose runtime IDs, contracts and diagnostics. Access requires developer.runtime-inspect and they never substitute for missing administrator authoring capabilities.",
    },
  }));

  const accessBody = element("div", "st-admin-v2-dev-body");
  accessBody.setAttribute("aria-live", "polite");
  accessBody.append(createAdminSkeleton(5));
  root.append(accessBody);

  requestAnimationFrame(async () => {
    try {
      // Fail closed on direct-route access: do not mount any technical inspector,
      // links or runtime requests until the server-authorized manifest succeeds.
      const manifest = await api.getDeveloperToolsManifest();
      if (!root.isConnected) return;
      accessBody.remove();
      renderAuthorizedDeveloperTools(root, manifest, navigate);
    } catch (error) {
      if (!root.isConnected) return;
      accessBody.replaceChildren(createAdminErrorState({
        title: "Developer Tools unavailable",
        message: adminErrorMessage(error, "You do not have permission to inspect developer diagnostics."),
      }));
    }
  });

  return root;
}
