import { isContractRecord, readMainAdminContractSection } from "./space-typing-contract-reader";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

type Tone = "good" | "warn" | "bad" | "info";
type FeatureGate = {
  id: string;
  storageKey: string;
  queryParam: string;
  defaultEnabled: boolean;
  queryOffValues: string[];
  queryOnValues: string[];
  storageDisabledValue: string;
  overridePrecedence: string[];
};
type FeatureGatesContract = {
  mode: "runtime-derived-readonly";
  runtimeSources: string[];
  authorableFields: string[];
  runtimeDerivedFields: string[];
  ids: string[];
  gates: FeatureGate[];
  sourceFunctions: string[];
  gameplayConsumer: string;
  persistenceOwner: string;
  remoteRolloutService: false;
  killSwitchService: false;
  percentageRollout: false;
  writeCapability: false;
  previewCapability: false;
  unsupportedMasterPlanFields: string[];
};

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}
function badge(label: string, tone: Tone = "info"): HTMLElement { return el("span", `st-admin-status ${tone}`, label); }
function notice(text: string, tone: Tone = "info"): HTMLElement { return el("div", `stx-notice ${tone}`, text); }
function panel(title: string, subtitle?: string): HTMLElement {
  const root = el("section", "st-admin-panel solid stx-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(el("h2", undefined, title));
  if (subtitle) copy.append(el("p", undefined, subtitle));
  head.append(copy);
  root.append(head);
  return root;
}
function listNotice(label: string, values: readonly string[], tone: Tone = "info"): HTMLElement {
  return notice(`${label}: ${values.join(" · ") || "none exposed"}`, tone);
}
function stringArray(value: unknown): value is string[] {
  return Array.isArray(value) && value.every((entry) => typeof entry === "string");
}
function isFeatureGate(value: unknown): value is FeatureGate {
  if (!isContractRecord(value)) return false;
  return typeof value["id"] === "string"
    && typeof value["storageKey"] === "string"
    && typeof value["queryParam"] === "string"
    && typeof value["defaultEnabled"] === "boolean"
    && stringArray(value["queryOffValues"])
    && stringArray(value["queryOnValues"])
    && typeof value["storageDisabledValue"] === "string"
    && stringArray(value["overridePrecedence"]);
}
function isFeatureGatesContract(value: unknown): value is FeatureGatesContract {
  if (!isContractRecord(value)) return false;
  return value["mode"] === "runtime-derived-readonly"
    && stringArray(value["runtimeSources"])
    && stringArray(value["authorableFields"])
    && stringArray(value["runtimeDerivedFields"])
    && stringArray(value["ids"])
    && Array.isArray(value["gates"])
    && value["gates"].every(isFeatureGate)
    && stringArray(value["sourceFunctions"])
    && typeof value["gameplayConsumer"] === "string"
    && typeof value["persistenceOwner"] === "string"
    && value["remoteRolloutService"] === false
    && value["killSwitchService"] === false
    && value["percentageRollout"] === false
    && value["writeCapability"] === false
    && value["previewCapability"] === false
    && stringArray(value["unsupportedMasterPlanFields"]);
}
async function fetchFeatureGatesContract(): Promise<FeatureGatesContract> {
  return readMainAdminContractSection("featureGates", "feature-gates.read", isFeatureGatesContract);
}

export function renderPhaseBFeatureGates(): HTMLElement {
  const page = el("div");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "System · Runtime Contract"),
    el("h1", undefined, "Feature Gates"),
    el("p", undefined, "Inspect feature gates actually consumed by Space Typing. Runtime currently owns browser-local gate semantics; Admin does not invent a remote rollout, targeting or kill-switch service."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("RUNTIME-BACKED · READ ONLY", "good"), badge("NO REMOTE ROLLOUT", "warn"));
  header.append(copy, actions);
  page.append(header);

  const status = notice("Loading canonical Feature Gates contract…");
  status.setAttribute("aria-live", "polite");
  const content = el("div");
  page.append(status, content);

  let loadGeneration = 0;
  const load = (): void => {
    const generation = ++loadGeneration;
    setAdminStatus(status, "Loading canonical Feature Gates contract…", "loading");
    content.replaceChildren(notice("Loading browser-local gate ownership and override semantics…", "info"));

    void fetchFeatureGatesContract().then((featureGates) => {
      if (generation !== loadGeneration) return;
      setAdminStatus(status, `${featureGates.ids.length} canonical runtime gate${featureGates.ids.length === 1 ? "" : "s"} · local override semantics · Admin writes closed.`, "success");
      const panels: HTMLElement[] = [];

      if (featureGates.gates.length === 0) {
        panels.push(panel("Runtime Gates", "The valid contract currently exposes no gate records."));
        panels[0].append(notice("No canonical runtime gates are currently exposed.", "info"));
      } else {
        for (const gate of featureGates.gates) {
          const gatePanel = panel(gate.id, "Canonical runtime gate from the pinned child contract");
          gatePanel.append(
            notice(`Storage key: ${gate.storageKey}`, "good"),
            notice(`Query parameter: ${gate.queryParam}`, "good"),
            notice(`Default: ${gate.defaultEnabled ? "enabled" : "disabled"}`),
            listNotice("Override precedence", gate.overridePrecedence),
            listNotice("Query values · ON", gate.queryOnValues),
            listNotice("Query values · OFF", gate.queryOffValues),
            notice(`localStorage disables only when value is exactly: ${gate.storageDisabledValue}`),
          );
          panels.push(gatePanel);
        }
      }

      const ownership = panel("Runtime Ownership", "What actually owns and consumes the gate");
      ownership.append(
        listNotice("Runtime sources", featureGates.runtimeSources),
        listNotice("Source functions", featureGates.sourceFunctions),
        notice(`Gameplay consumer: ${featureGates.gameplayConsumer}`, "good"),
        notice(`Persistence owner: ${featureGates.persistenceOwner}`, "good"),
        listNotice("Runtime-derived fields", featureGates.runtimeDerivedFields),
      );

      const boundary = panel("Admin Boundary", "No parallel rollout configuration is created by this UI");
      boundary.append(
        notice("Remote rollout service: unavailable by canonical runtime design", "warn"),
        notice("Percentage rollout: unavailable by canonical runtime design", "warn"),
        notice("Kill-switch service: unavailable by canonical runtime design", "warn"),
        notice(`Admin write capability: ${String(featureGates.writeCapability)}`, "info"),
        notice(`Admin preview capability: ${String(featureGates.previewCapability)}`, "info"),
        listNotice("Unsupported authoring fields", featureGates.unsupportedMasterPlanFields, "warn"),
        notice("Create Flag, rollout sliders, targeting scopes, Save Draft and Publish are intentionally unavailable until the child runtime exposes a canonical remote rollout owner.", "info"),
      );

      content.replaceChildren(...panels, ownership, boundary);
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      setAdminStatus(status, "Feature Gates service unavailable.", "error");
      renderAdminFailureState(content, {
        title: "Feature Gates unavailable",
        fallbackMessage: "Unable to load the valid canonical feature-gates.read contract.",
        error,
        onRetry: load,
      });
    });
  };

  load();
  return page;
}
