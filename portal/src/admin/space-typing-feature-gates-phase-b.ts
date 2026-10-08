import { SpaceTypingAdminApi } from "./api";

const api = new SpaceTypingAdminApi();
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
type AdminContract = { capabilities: string[]; featureGates: FeatureGatesContract };

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
function listNotice(label: string, values: string[], tone: Tone = "info"): HTMLElement {
  return notice(`${label}: ${values.join(" · ")}`, tone);
}
async function fetchFeatureGatesContract(): Promise<FeatureGatesContract> {
  const response = await fetch("/api/admin/space-typing/contract", {
    cache: "no-store",
    headers: { "x-typing-game-admin-token": api.getToken() },
  });
  const payload = (await response.json().catch(() => ({}))) as Partial<AdminContract> & { message?: string };
  if (!response.ok) throw new Error(payload.message ?? `Feature Gates contract request failed (${response.status})`);
  if (!payload.featureGates || !payload.capabilities?.includes("feature-gates.read")) {
    throw new Error("Pinned child contract does not expose feature-gates.read.");
  }
  return payload.featureGates;
}

export function renderPhaseBFeatureGates(): HTMLElement {
  const page = el("div");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "System · Runtime Contract"),
    el("h1", undefined, "Feature Gates"),
    el("p", undefined, "Inspect feature gates actually consumed by Space Typing. Runtime currently owns a browser-local Expansion V2 gate only; there is no remote rollout, percentage rollout, audience targeting or kill-switch service to author from Admin."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(badge("RUNTIME-BACKED · READ ONLY", "good"), badge("NO REMOTE ROLLOUT", "warn"));
  header.append(copy, actions);
  page.append(header);

  const status = notice("Loading canonical Feature Gates contract…");
  page.append(status);
  void (async () => {
    try {
      const featureGates = await fetchFeatureGatesContract();
      status.className = "stx-notice good";
      status.textContent = `${featureGates.ids.length} canonical runtime gate · local browser override semantics · Admin writes closed.`;

      for (const gate of featureGates.gates) {
        const gatePanel = panel(gate.id, "Canonical runtime gate from src/expansion-v2/feature-flags.ts");
        gatePanel.append(
          notice(`Storage key: ${gate.storageKey}`, "good"),
          notice(`Query parameter: ${gate.queryParam}`, "good"),
          notice(`Default: ${gate.defaultEnabled ? "enabled" : "disabled"}`),
          listNotice("Override precedence", gate.overridePrecedence),
          listNotice("Query values · ON", gate.queryOnValues),
          listNotice("Query values · OFF", gate.queryOffValues),
          notice(`localStorage disables only when value is exactly: ${gate.storageDisabledValue}`),
        );
        page.append(gatePanel);
      }

      const ownership = panel("Runtime Ownership", "What actually owns and consumes the gate");
      ownership.append(
        listNotice("Runtime sources", featureGates.runtimeSources),
        listNotice("Source functions", featureGates.sourceFunctions),
        notice(`Gameplay consumer: ${featureGates.gameplayConsumer}`, "good"),
        notice(`Persistence owner: ${featureGates.persistenceOwner}`, "good"),
      );

      const boundary = panel("Admin Boundary", "No parallel rollout configuration is created by this UI");
      boundary.append(
        notice("Remote rollout service: unavailable", "warn"),
        notice("Percentage rollout: unavailable", "warn"),
        notice("Kill-switch service: unavailable", "warn"),
        listNotice("Unsupported authoring fields", featureGates.unsupportedMasterPlanFields, "warn"),
        notice("Create Flag, rollout sliders, targeting scopes, toggles, Save Draft and Publish are intentionally unavailable here.", "info"),
      );
      page.append(ownership, boundary);
    } catch (error: unknown) {
      status.className = "stx-notice bad";
      status.textContent = `Feature Gates contract unavailable: ${error instanceof Error ? error.message : String(error)}`;
    }
  })();
  return page;
}
