import { SpaceTypingAdminApi } from "./api";

const api = new SpaceTypingAdminApi();
type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";
type MissionsContract = {
  mode: "runtime-derived-readonly";
  runtimeSources: string[];
  authorableFields: string[];
  runtimeDerivedFields: string[];
  objectiveTypes: string[];
  definitionFields: string[];
  sourceFunctions: string[];
  selectionOwner: string;
  gameplayConsumer: string;
  rewardIntegration: string;
  persistenceOwner: string;
  unsupportedMasterPlanFields: string[];
  recurringMissionDefinitions: false;
  dailyWeeklyAuthoring: false;
  writeCapability: false;
  previewCapability: false;
};
type AdminContract = { capabilities: string[]; missions: MissionsContract };

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}
function button(label: string, onClick: () => void, cls = "st-admin-btn"): HTMLButtonElement {
  const node = el("button", cls, label);
  node.type = "button";
  node.addEventListener("click", onClick);
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
async function fetchMissionsContract(): Promise<MissionsContract> {
  const response = await fetch("/api/admin/space-typing/contract", {
    cache: "no-store",
    headers: { "x-typing-game-admin-token": api.getToken() },
  });
  const payload = (await response.json().catch(() => ({}))) as Partial<AdminContract> & { message?: string };
  if (!response.ok) throw new Error(payload.message ?? `Missions contract request failed (${response.status})`);
  if (!payload.missions || !payload.capabilities?.includes("missions.read")) {
    throw new Error("Pinned child contract does not expose missions.read.");
  }
  return payload.missions;
}

export function renderPhaseBMissions(navigate: Navigate): HTMLElement {
  const page = el("div");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Live Ops · Runtime Contract"),
    el("h1", undefined, "Missions"),
    el("p", undefined, "Inspect the canonical Stage Objective system that gameplay actually consumes. The current runtime does not own recurring Daily / Weekly mission definitions, rotation calendars or reward pools, so Admin authoring stays intentionally closed."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(
    badge("RUNTIME-BACKED · READ ONLY", "good"),
    button("Stamina / Warp", () => navigate("/admin/space-typing/warp")),
    button("Daily / Weekly (UI mock)", () => navigate("/admin/space-typing/daily-weekly")),
  );
  header.append(copy, actions);
  page.append(header);

  const status = notice("Loading canonical Missions contract…");
  page.append(status);
  void (async () => {
    try {
      const missions = await fetchMissionsContract();
      status.className = "stx-notice good";
      status.textContent = `${missions.objectiveTypes.length} canonical Stage Objective types · runtime session state · Admin writes closed.`;

      const types = panel("Runtime Objective Types", "Canonical StageObjectiveType values from src/events/objectives.ts");
      types.append(listNotice("Objective types", missions.objectiveTypes, "good"));

      const model = panel("Definition & Runtime State", "Fields exposed by the real objective definition/state model");
      model.append(
        listNotice("Definition fields", missions.definitionFields),
        listNotice("Runtime state fields", missions.runtimeDerivedFields),
        notice(`Persistence owner: ${missions.persistenceOwner}`, "good"),
      );

      const integration = panel("Selection & Reward Integration", "Gameplay owns objective selection, progress reduction and reward factor application");
      integration.append(
        notice(`Selection owner: ${missions.selectionOwner}`, "good"),
        notice(`Gameplay consumer: ${missions.gameplayConsumer}`, "good"),
        notice(`Reward integration: ${missions.rewardIntegration}`, "good"),
        listNotice("Runtime functions", missions.sourceFunctions),
      );

      const sources = panel("Canonical Sources", "Admin reads contract metadata; it does not clone mission logic");
      sources.append(listNotice("Runtime sources", missions.runtimeSources));

      const boundary = panel("Admin Boundary", "Do not promote UI-only recurring mission concepts into runtime configuration");
      boundary.append(
        listNotice("Unsupported recurring-authoring fields", missions.unsupportedMasterPlanFields, "warn"),
        notice("Recurring mission definitions: unavailable in the canonical runtime.", "warn"),
        notice("Daily / Weekly authoring: unavailable. The existing Daily / Weekly screen is UI mock data only and is not a runtime control plane.", "warn"),
        notice("Save Draft / Publish are intentionally unavailable because no canonical persistence/apply consumer exists for mission definitions.", "warn"),
        notice("Preview is intentionally unavailable; Admin does not duplicate objective selection or progress reduction logic.", "info"),
      );

      page.append(types, model, integration, sources, boundary);
    } catch (error: unknown) {
      status.className = "stx-notice bad";
      status.textContent = `Missions contract unavailable: ${error instanceof Error ? error.message : String(error)}`;
    }
  })();
  return page;
}
