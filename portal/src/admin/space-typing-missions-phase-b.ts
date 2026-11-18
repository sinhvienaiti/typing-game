import { isContractRecord, readMainAdminContractSection } from "./space-typing-contract-reader";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";
type MissionsContract = {
  mode: "runtime-derived-readonly";
  runtimeSources: string[];
  domains: string[];
  authorableFields: string[];
  runtimeDerivedFields: string[];
  missionIds: string[];
  missionCounterKeys: string[];
  missionDefinitionFields: string[];
  missionSourceFunctions: string[];
  missionPersistenceOwner: string;
  stageObjectiveTypes: string[];
  stageObjectiveDefinitionFields: string[];
  stageObjectiveSourceFunctions: string[];
  stageObjectivePersistenceOwner: string;
  gameplayConsumers: string[];
  rewardIntegration: string[];
  unsupportedMasterPlanFields: string[];
  recurringMissionDefinitions: false;
  dailyWeeklyAuthoring: false;
  writeCapability: false;
  previewCapability: false;
};

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
  return notice(`${label}: ${values.length ? values.join(" · ") : "none exposed"}`, tone);
}
function stringArray(value: unknown): value is string[] { return Array.isArray(value) && value.every((entry) => typeof entry === "string"); }

function validMissionsContract(value: unknown): value is MissionsContract {
  if (!isContractRecord(value) || value["mode"] !== "runtime-derived-readonly") return false;
  for (const key of [
    "runtimeSources",
    "domains",
    "authorableFields",
    "runtimeDerivedFields",
    "missionIds",
    "missionCounterKeys",
    "missionDefinitionFields",
    "missionSourceFunctions",
    "stageObjectiveTypes",
    "stageObjectiveDefinitionFields",
    "stageObjectiveSourceFunctions",
    "gameplayConsumers",
    "rewardIntegration",
    "unsupportedMasterPlanFields",
  ] as const) {
    if (!stringArray(value[key])) return false;
  }
  return typeof value["missionPersistenceOwner"] === "string" && typeof value["stageObjectivePersistenceOwner"] === "string";
}

async function fetchMissionsContract(): Promise<MissionsContract> {
  return readMainAdminContractSection<MissionsContract>("missions", "missions.read", validMissionsContract);
}

export function renderPhaseBMissions(navigate: Navigate): HTMLElement {
  const page = el("div");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Live Ops · Runtime Contract"),
    el("h1", undefined, "Missions"),
    el("p", undefined, "Inspect canonical progression missions and per-stage objectives consumed by gameplay. Definitions are code-owned; Admin exposes diagnostics without inventing Daily / Weekly rotation authoring."),
  );
  const actions = el("div", "st-admin-page-actions");
  actions.append(
    badge("RUNTIME-BACKED · READ ONLY", "good"),
    button("Stamina / Warp", () => navigate("/admin/space-typing/warp")),
    button("Daily / Weekly", () => navigate("/admin/space-typing/daily-weekly")),
  );
  header.append(copy, actions);
  page.append(header);

  const status = notice("Loading canonical Missions contract…");
  status.setAttribute("aria-live", "polite");
  const content = el("div");
  page.append(status, content);

  let loadGeneration = 0;
  const load = (): void => {
    const generation = ++loadGeneration;
    content.replaceChildren(notice("Loading mission and objective ownership…", "info"));
    setAdminStatus(status, "Loading canonical Missions contract…", "loading");
    void fetchMissionsContract().then((missions) => {
      if (generation !== loadGeneration) return;
      setAdminStatus(status, `${missions.missionIds.length} canonical progression missions · ${missions.stageObjectiveTypes.length} Stage Objective types · Admin writes closed.`, "success");
      content.replaceChildren();

      const progression = panel("Progression Missions", "Canonical code-owned registry from src/progression/missions.ts");
      progression.append(
        listNotice("Mission IDs", missions.missionIds, "good"),
        listNotice("Counters", missions.missionCounterKeys),
        listNotice("Definition fields", missions.missionDefinitionFields),
        notice(`Persistence owner: ${missions.missionPersistenceOwner}`, "good"),
        notice("Claimed missions and counters are player progression state; mission rewards are issued by the gameplay claim flow.", "info"),
      );

      const objectives = panel("Stage Objectives", "Canonical per-stage objective runtime from src/events/objectives.ts");
      objectives.append(
        listNotice("Objective types", missions.stageObjectiveTypes, "good"),
        listNotice("Definition fields", missions.stageObjectiveDefinitionFields),
        notice(`Persistence owner: ${missions.stageObjectivePersistenceOwner}`, "info"),
      );

      const integration = panel("Runtime Integration", "Admin reads ownership metadata instead of cloning mission logic");
      integration.append(
        listNotice("Progression functions", missions.missionSourceFunctions),
        listNotice("Objective functions", missions.stageObjectiveSourceFunctions),
        listNotice("Gameplay consumers", missions.gameplayConsumers, "good"),
        listNotice("Reward integration", missions.rewardIntegration, "good"),
        listNotice("Canonical sources", missions.runtimeSources),
      );

      const boundary = panel("Admin Boundary", "Unavailable recurring authoring is intentional until a canonical runtime service exists");
      boundary.append(
        listNotice("Unsupported recurring-authoring fields", missions.unsupportedMasterPlanFields, "warn"),
        notice("The progression mission definitions are real, but they are code-owned and therefore read-only here.", "warn"),
        notice("Daily / Weekly reset, rotation calendar and reward-pool authoring are unavailable in the canonical runtime.", "warn"),
        notice("Save Draft / Publish / Preview are intentionally unavailable for Missions.", "info"),
      );

      content.append(progression, objectives, integration, boundary);
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      setAdminStatus(status, "Missions contract is unavailable.", "error");
      renderAdminFailureState(content, {
        title: "Missions unavailable",
        fallbackMessage: "The canonical Missions contract could not be loaded. Check the local Admin runtime and try again.",
        error,
        onRetry: load,
      });
    });
  };

  load();
  return page;
}
