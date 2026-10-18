import {
  SpaceTypingAdminApi,
  type AdminStatePayload,
  type GeneralSettingsConfig,
  type SpaceTypingAdminConfig,
} from "./api";
import { renderAdminFailureState, setAdminStatus } from "./space-typing-admin-state";

const api = new SpaceTypingAdminApi();
type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";
type Control = HTMLInputElement | HTMLSelectElement | HTMLButtonElement;

const SCHEMA_DEFAULT_SYSTEM: GeneralSettingsConfig = {
  gameDefaults: {
    defaultMode: "campaign",
    defaultShip: "vanguard",
    difficulty: "normal",
    tutorialEnabled: true,
    pronunciationDefault: true,
    autoSave: true,
  },
  network: {
    minimumVersion: "0.1.0",
    autoSaveIntervalSeconds: 30,
    reconnectWindowSeconds: 20,
    offlinePlay: true,
    telemetry: true,
  },
  maintenance: {
    enabled: false,
    message: "Scheduled maintenance",
  },
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
function badge(label: string, tone: Tone = "info"): HTMLElement {
  return el("span", `st-admin-status ${tone}`, label);
}
function panel(title: string, subtitle?: string, cls = ""): HTMLElement {
  const root = el("section", `st-admin-panel solid stx-panel ${cls}`.trim());
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(el("h2", undefined, title));
  if (subtitle) copy.append(el("p", undefined, subtitle));
  head.append(copy);
  root.append(head);
  return root;
}
function notice(text: string, tone: Tone = "info"): HTMLElement {
  return el("div", `stx-notice ${tone}`, text);
}
function grid(...children: HTMLElement[]): HTMLElement {
  const root = el("div", "stx-grid");
  root.append(...children);
  return root;
}
function field(label: string, options?: readonly string[], type: "text" | "number" = "text"): { root: HTMLElement; control: HTMLInputElement | HTMLSelectElement } {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label));
  let control: HTMLInputElement | HTMLSelectElement;
  if (options) {
    const select = el("select", "st-admin-select") as HTMLSelectElement;
    select.append(new Option("Loading active value…", ""));
    for (const option of options) select.append(new Option(option, option));
    control = select;
  } else {
    const input = el("input") as HTMLInputElement;
    input.type = type;
    input.value = "";
    input.placeholder = "Loading active value…";
    control = input;
  }
  control.disabled = true;
  control.setAttribute("aria-label", label);
  root.append(control);
  return { root, control };
}
function toggle(label: string, description?: string): { root: HTMLElement; control: HTMLButtonElement } {
  const root = el("div", "stx-toggle-row");
  const copy = el("div");
  copy.append(el("strong", undefined, label));
  if (description) copy.append(el("small", undefined, description));
  const control = el("button", "st-admin-switch") as HTMLButtonElement;
  control.type = "button";
  control.disabled = true;
  control.setAttribute("aria-label", `Toggle ${label}`);
  control.setAttribute("aria-pressed", "false");
  control.append(el("i"));
  control.addEventListener("click", () => {
    if (control.disabled) return;
    const next = control.getAttribute("aria-pressed") !== "true";
    control.setAttribute("aria-pressed", String(next));
    control.classList.toggle("on", next);
  });
  root.append(copy, control);
  return { root, control };
}
function isRecord(value: unknown): value is Record<string, unknown> {
  return value !== null && typeof value === "object" && !Array.isArray(value);
}
function validateState(value: unknown): AdminStatePayload {
  if (!isRecord(value) || !isRecord(value["state"]) || !isRecord(value["active"]) || !Array.isArray(value["history"])) {
    throw new Error("Admin state response is missing the revision state envelope.");
  }
  const state = value["state"];
  const active = value["active"];
  if (
    typeof state["activeRevision"] !== "string" ||
    typeof state["generation"] !== "number" ||
    typeof active["revision"] !== "string" ||
    !isRecord(active["config"]) ||
    active["revision"] !== state["activeRevision"]
  ) {
    throw new Error("Admin state response does not contain a consistent active revision.");
  }
  return value as unknown as AdminStatePayload;
}
function validateSystem(value: unknown): GeneralSettingsConfig | null {
  if (value === undefined) return null;
  if (!isRecord(value) || !isRecord(value["gameDefaults"]) || !isRecord(value["network"]) || !isRecord(value["maintenance"])) {
    throw new Error("Active system config has an invalid shape.");
  }
  const game = value["gameDefaults"];
  const network = value["network"];
  const maintenance = value["maintenance"];
  if (
    !["campaign", "recall", "expedition"].includes(String(game["defaultMode"])) ||
    typeof game["defaultShip"] !== "string" ||
    !["easy", "normal", "hard"].includes(String(game["difficulty"])) ||
    typeof game["tutorialEnabled"] !== "boolean" ||
    typeof game["pronunciationDefault"] !== "boolean" ||
    typeof game["autoSave"] !== "boolean" ||
    typeof network["minimumVersion"] !== "string" ||
    typeof network["autoSaveIntervalSeconds"] !== "number" ||
    typeof network["reconnectWindowSeconds"] !== "number" ||
    typeof network["offlinePlay"] !== "boolean" ||
    typeof network["telemetry"] !== "boolean" ||
    typeof maintenance["enabled"] !== "boolean" ||
    typeof maintenance["message"] !== "string"
  ) {
    throw new Error("Active system config is missing required canonical fields.");
  }
  return value as unknown as GeneralSettingsConfig;
}
function toggleValue(control: HTMLButtonElement): boolean {
  return control.getAttribute("aria-pressed") === "true";
}
function numberValue(control: HTMLInputElement | HTMLSelectElement, label: string): number {
  const value = Number(control.value);
  if (!Number.isFinite(value) || value < 0) throw new Error(`${label} must be a non-negative number.`);
  return value;
}

export function renderPhaseBSettings(navigate: Navigate): HTMLElement {
  const page = el("div");
  const revisionBadge = badge("ACTIVE · loading", "info");
  const generationBadge = badge("GEN · —", "info");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "System · Global Configuration · Phase B"),
    el("h1", undefined, "General Settings"),
    el("p", undefined, "Revision-backed configuration. Editors stay locked until the authoritative active revision is loaded; Save Draft never changes production until History / Publish succeeds."),
  );
  const headActions = el("div", "st-admin-page-actions");
  headActions.append(revisionBadge, generationBadge, button("History / Publish", () => navigate("/admin/space-typing/history")));
  header.append(copy, headActions);
  page.append(header);

  const status = notice("Loading authoritative active revision…", "info");
  status.setAttribute("aria-live", "polite");
  const failureHost = el("div");

  const mode = field("Default Mode", ["campaign", "recall", "expedition"]);
  const ship = field("Default Ship");
  const difficulty = field("Difficulty", ["easy", "normal", "hard"]);
  const tutorial = toggle("Tutorial Enabled", "New-player tutorial default for new sessions.");
  const pronunciation = toggle("Pronunciation Default", "Default pronunciation preference; this does not duck BGM/music.");
  const autoSave = toggle("Auto Save", "Gameplay save preference for new sessions.");
  const minimumVersion = field("Minimum Version");
  const autoSaveInterval = field("Auto-save Interval (seconds)", undefined, "number");
  const reconnectWindow = field("Reconnect Window (seconds)", undefined, "number");
  const offlinePlay = toggle("Offline Play", "Allow supported browser-local play paths.");
  const telemetry = toggle("Telemetry", "Runtime telemetry preference; availability still depends on the runtime owner.");
  const maintenance = toggle("Maintenance Mode", "High risk: this becomes live only after explicit publish.");
  const maintenanceMessage = field("Maintenance Message");

  const game = panel("Game Defaults", "Canonical system.gameDefaults");
  game.append(grid(mode.root, ship.root, difficulty.root), grid(tutorial.root, pronunciation.root, autoSave.root));
  const network = panel("System & Network", "Canonical system.network");
  network.append(grid(minimumVersion.root, autoSaveInterval.root, reconnectWindow.root), grid(offlinePlay.root, telemetry.root));
  const danger = panel("Maintenance", "Canonical system.maintenance · publish-gated", "stx-danger-panel");
  danger.append(
    maintenance.root,
    maintenanceMessage.root,
    notice("Drafting maintenance settings does not change the active runtime. Review and explicit Publish are required.", "warn"),
  );
  const editorHost = el("div");
  editorHost.append(grid(game, network), danger);

  const saveStatus = el("span", undefined, "Waiting for authoritative active revision…");
  const discardButton = button("Discard", () => load(), "st-admin-btn");
  const saveButton = button("Save Draft", () => void saveDraft(), "st-admin-btn primary");
  saveButton.disabled = true;
  discardButton.disabled = true;
  const saveBar = el("div", "st-admin-sticky-save stx-savebar");
  saveBar.append(el("strong", undefined, "Phase B Draft"), saveStatus, el("div", "grow"), discardButton, saveButton);
  page.append(status, failureHost, editorHost, saveBar);

  const controls: Control[] = [
    mode.control, ship.control, difficulty.control, tutorial.control, pronunciation.control, autoSave.control,
    minimumVersion.control, autoSaveInterval.control, reconnectWindow.control, offlinePlay.control, telemetry.control,
    maintenance.control, maintenanceMessage.control,
  ];

  let loadedState: AdminStatePayload | null = null;
  let loadedActiveRevision: string | null = null;
  let loadGeneration = 0;

  function setEditable(editable: boolean): void {
    for (const control of controls) control.disabled = !editable;
    saveButton.disabled = !editable;
    discardButton.disabled = !editable;
  }
  function applyToggle(control: HTMLButtonElement, checked: boolean): void {
    control.setAttribute("aria-pressed", String(checked));
    control.classList.toggle("on", checked);
  }
  function applySystem(value: GeneralSettingsConfig): void {
    mode.control.value = value.gameDefaults.defaultMode;
    ship.control.value = value.gameDefaults.defaultShip;
    difficulty.control.value = value.gameDefaults.difficulty;
    applyToggle(tutorial.control, value.gameDefaults.tutorialEnabled);
    applyToggle(pronunciation.control, value.gameDefaults.pronunciationDefault);
    applyToggle(autoSave.control, value.gameDefaults.autoSave);
    minimumVersion.control.value = value.network.minimumVersion;
    autoSaveInterval.control.value = String(value.network.autoSaveIntervalSeconds);
    reconnectWindow.control.value = String(value.network.reconnectWindowSeconds);
    applyToggle(offlinePlay.control, value.network.offlinePlay);
    applyToggle(telemetry.control, value.network.telemetry);
    applyToggle(maintenance.control, value.maintenance.enabled);
    maintenanceMessage.control.value = value.maintenance.message;
  }
  function collectSystem(): GeneralSettingsConfig {
    if (!loadedActiveRevision) throw new Error("Authoritative active revision is not loaded.");
    const selectedMode = mode.control.value;
    const selectedDifficulty = difficulty.control.value;
    if (!(["campaign", "recall", "expedition"] as string[]).includes(selectedMode)) throw new Error("Default Mode is invalid.");
    if (!(["easy", "normal", "hard"] as string[]).includes(selectedDifficulty)) throw new Error("Difficulty is invalid.");
    const defaultShip = ship.control.value.trim();
    const minVersion = minimumVersion.control.value.trim();
    const message = maintenanceMessage.control.value.trim();
    if (!defaultShip) throw new Error("Default Ship is required.");
    if (!minVersion) throw new Error("Minimum Version is required.");
    if (toggleValue(maintenance.control) && !message) throw new Error("Maintenance Message is required when Maintenance Mode is enabled.");
    return {
      gameDefaults: {
        defaultMode: selectedMode as GeneralSettingsConfig["gameDefaults"]["defaultMode"],
        defaultShip,
        difficulty: selectedDifficulty as GeneralSettingsConfig["gameDefaults"]["difficulty"],
        tutorialEnabled: toggleValue(tutorial.control),
        pronunciationDefault: toggleValue(pronunciation.control),
        autoSave: toggleValue(autoSave.control),
      },
      network: {
        minimumVersion: minVersion,
        autoSaveIntervalSeconds: numberValue(autoSaveInterval.control, "Auto-save Interval"),
        reconnectWindowSeconds: numberValue(reconnectWindow.control, "Reconnect Window"),
        offlinePlay: toggleValue(offlinePlay.control),
        telemetry: toggleValue(telemetry.control),
      },
      maintenance: {
        enabled: toggleValue(maintenance.control),
        message,
      },
    };
  }
  async function load(): Promise<void> {
    const generation = ++loadGeneration;
    loadedState = null;
    loadedActiveRevision = null;
    setEditable(false);
    failureHost.replaceChildren();
    revisionBadge.textContent = "ACTIVE · loading";
    revisionBadge.className = "st-admin-status info";
    generationBadge.textContent = "GEN · —";
    generationBadge.className = "st-admin-status info";
    saveStatus.textContent = "Waiting for authoritative active revision…";
    setAdminStatus(status, "Loading authoritative active revision…", "loading");
    try {
      const payload = validateState(await api.getState());
      if (generation !== loadGeneration) return;
      const system = validateSystem(payload.active.config.system);
      loadedState = payload;
      loadedActiveRevision = payload.state.activeRevision;
      applySystem(system ?? SCHEMA_DEFAULT_SYSTEM);
      revisionBadge.textContent = `ACTIVE · ${payload.state.activeRevision}`;
      revisionBadge.className = "st-admin-status good";
      generationBadge.textContent = `GEN · ${payload.state.generation}`;
      generationBadge.className = "st-admin-status good";
      if (system) {
        setAdminStatus(status, "Loaded canonical General Settings from the authoritative active revision.", "success");
        saveStatus.textContent = "Revision-backed · Save Draft does not publish runtime";
      } else {
        setAdminStatus(status, "Active revision is authoritative but predates system config. Showing schema defaults as an explicit first-draft baseline.", "warning");
        saveStatus.textContent = "Schema defaults · active baseline confirmed · draft required before publish";
      }
      setEditable(true);
    } catch (error: unknown) {
      if (generation !== loadGeneration) return;
      revisionBadge.textContent = "ACTIVE · unavailable";
      revisionBadge.className = "st-admin-status bad";
      generationBadge.textContent = "GEN · unavailable";
      generationBadge.className = "st-admin-status bad";
      setAdminStatus(status, "General Settings service unavailable. Editing and Save Draft are locked.", "error");
      renderAdminFailureState(failureHost, {
        title: "General Settings unavailable",
        fallbackMessage: "Unable to load the authoritative active revision. No fallback values are editable until the service recovers.",
        error,
        onRetry: () => void load(),
      });
    }
  }
  async function saveDraft(): Promise<void> {
    if (!loadedState || !loadedActiveRevision) return;
    setEditable(false);
    saveStatus.textContent = "Verifying active revision and saving immutable draft…";
    try {
      const latest = validateState(await api.getState());
      if (latest.state.activeRevision !== loadedActiveRevision) {
        throw new Error(`Active revision changed from ${loadedActiveRevision} to ${latest.state.activeRevision}. Reload before saving.`);
      }
      const config = structuredClone(latest.active.config) as SpaceTypingAdminConfig;
      // Keep system keys this form does not edit (e.g. system.testing from the Testing panel).
      config.system = { ...config.system, ...collectSystem() };
      const revision = await api.createRevision({
        baseRevision: latest.active.revision,
        config,
        message: "Admin Phase B · General Settings draft",
      });
      saveStatus.textContent = `Draft saved · ${revision.revision} · runtime unchanged`;
      setAdminStatus(status, `Draft ${revision.revision} created from active ${latest.active.revision}. Review and Publish from History when ready.`, "success");
    } catch (error: unknown) {
      const message = error instanceof Error ? error.message : "Unable to save General Settings draft.";
      saveStatus.textContent = `Draft rejected · ${message}`;
      setAdminStatus(status, `General Settings draft rejected: ${message}`, "error");
    } finally {
      if (loadedActiveRevision) setEditable(true);
    }
  }

  void load();
  return page;
}
