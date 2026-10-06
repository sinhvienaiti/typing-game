import { renderPhaseBAudio } from "./space-typing-audio-phase-b";
import { SpaceTypingAdminApi, type FeatureFlagConfig, type FeatureFlagScope, type GeneralSettingsConfig, type SpaceTypingAdminConfig } from "./api";

const BASE = "/admin/space-typing";
const api = new SpaceTypingAdminApi();

type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";
type Control = HTMLInputElement | HTMLSelectElement;

const DEFAULT_SYSTEM: GeneralSettingsConfig = {
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

const DEFAULT_FLAGS: Record<string, FeatureFlagConfig> = {
  "voice-mode": { enabled: true, rolloutPercent: 100, scope: "all", risk: "normal" },
  stamina: { enabled: true, rolloutPercent: 100, scope: "all", risk: "economy" },
  "pvp-reflex": { enabled: true, rolloutPercent: 100, scope: "all", risk: "competitive" },
  "pvp-word-chain": { enabled: true, rolloutPercent: 100, scope: "all", risk: "competitive" },
  "new-boss-renderer": { enabled: true, rolloutPercent: 25, scope: "cohort", risk: "normal" },
  "world-music-v2": { enabled: true, rolloutPercent: 100, scope: "all", risk: "normal" },
};

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

function btn(label: string, onClick: () => void = () => undefined, cls = "st-admin-btn"): HTMLButtonElement {
  const node = el("button", cls, label);
  node.type = "button";
  node.addEventListener("click", onClick);
  return node;
}

function badge(label: string, tone: Tone = "info"): HTMLElement {
  return el("span", `st-admin-status ${tone}`, label);
}

function header(eyebrow: string, title: string, description: string, actions: readonly HTMLElement[] = []): HTMLElement {
  const root = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(el("div", "st-admin-eyebrow", eyebrow), el("h1", undefined, title), el("p", undefined, description));
  root.append(copy);
  if (actions.length > 0) {
    const tools = el("div", "st-admin-page-actions");
    tools.append(...actions);
    root.append(tools);
  }
  return root;
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

function grid(...children: HTMLElement[]): HTMLElement {
  const root = el("div", "stx-grid");
  root.append(...children);
  return root;
}

function notice(text: string, tone: Tone = "info"): HTMLElement {
  return el("div", `stx-notice ${tone}`, text);
}

function field(label: string, value: string, options?: readonly string[], type: "text" | "number" = "text"): { root: HTMLElement; control: Control } {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label));
  let control: Control;
  if (options !== undefined) {
    const select = el("select", "st-admin-select") as HTMLSelectElement;
    for (const option of options) select.append(new Option(option, option));
    select.value = value;
    control = select;
  } else {
    const input = el("input") as HTMLInputElement;
    input.type = type;
    input.value = value;
    control = input;
  }
  control.setAttribute("aria-label", label);
  root.append(control);
  return { root, control };
}

function toggle(label: string, enabled: boolean, description?: string): { root: HTMLElement; control: HTMLButtonElement } {
  const root = el("div", "stx-toggle-row");
  const copy = el("div");
  copy.append(el("strong", undefined, label));
  if (description) copy.append(el("small", undefined, description));
  const control = el("button", `st-admin-switch${enabled ? " on" : ""}`) as HTMLButtonElement;
  control.type = "button";
  control.setAttribute("aria-label", `Toggle ${label}`);
  control.setAttribute("aria-pressed", String(enabled));
  control.append(el("i"));
  control.addEventListener("click", () => {
    control.classList.toggle("on");
    control.setAttribute("aria-pressed", String(control.classList.contains("on")));
  });
  root.append(copy, control);
  return { root, control };
}

function enabled(control: HTMLButtonElement): boolean {
  return control.getAttribute("aria-pressed") === "true";
}

function numberValue(control: Control): number {
  return Number(control.value);
}

function cloneConfig(config: SpaceTypingAdminConfig): SpaceTypingAdminConfig {
  return structuredClone(config);
}

function assertStableActiveRevision(loadedActiveRevision: string | null, currentActiveRevision: string): void {
  if (loadedActiveRevision === null) {
    throw new Error("Active revision has not finished loading. Reload this screen before saving.");
  }
  if (loadedActiveRevision !== currentActiveRevision) {
    throw new Error(`Active revision changed from ${loadedActiveRevision} to ${currentActiveRevision}. Reload this screen before saving to avoid overwriting newer published changes.`);
  }
}

function saveBar(navigate: Navigate, save: (button: HTMLButtonElement, status: HTMLElement) => Promise<void>): HTMLElement {
  const root = el("div", "st-admin-sticky-save stx-savebar");
  const status = el("span", undefined, "Revision-backed · Save Draft does not publish runtime");
  const saveButton = btn("Save Draft", () => void save(saveButton, status), "st-admin-btn primary");
  root.append(el("strong", undefined, "Phase B Draft"), status, el("div", "grow"), btn("Discard", () => navigate(location.pathname)), saveButton);
  return root;
}

function runtimeStatus(): { root: HTMLElement; set: (text: string, tone?: Tone) => void } {
  const root = notice("Loading active revision…", "info");
  return {
    root,
    set(text, tone = "info") {
      root.className = `stx-notice ${tone}`;
      root.textContent = text;
    },
  };
}

function renderSettings(navigate: Navigate): HTMLElement {
  const page = el("div");
  const revisionBadge = badge("ACTIVE · loading", "info");
  page.append(header(
    "System · Global Configuration · Phase B",
    "General Settings",
    "Revision-backed configuration. Save Draft creates an immutable revision; production runtime changes only after the History / Publish CAS gate.",
    [revisionBadge],
  ));

  let loadedActiveRevision: string | null = null;
  const state = structuredClone(DEFAULT_SYSTEM);
  const mode = field("Default Mode", state.gameDefaults.defaultMode, ["campaign", "recall", "expedition"]);
  const ship = field("Default Ship", state.gameDefaults.defaultShip);
  const difficulty = field("Difficulty", state.gameDefaults.difficulty, ["easy", "normal", "hard"]);
  const tutorial = toggle("Tutorial Enabled", state.gameDefaults.tutorialEnabled);
  const pronunciation = toggle("Pronunciation Default", state.gameDefaults.pronunciationDefault);
  const autoSave = toggle("Auto Save", state.gameDefaults.autoSave);

  const minimumVersion = field("Minimum Version", state.network.minimumVersion);
  const autoSaveInterval = field("Auto-save Interval (seconds)", String(state.network.autoSaveIntervalSeconds), undefined, "number");
  const reconnectWindow = field("Reconnect Window (seconds)", String(state.network.reconnectWindowSeconds), undefined, "number");
  const offlinePlay = toggle("Offline Play", state.network.offlinePlay);
  const telemetry = toggle("Telemetry", state.network.telemetry);

  const maintenance = toggle("Maintenance Mode", state.maintenance.enabled, "Dangerous: becomes active only after Publish.");
  const maintenanceMessage = field("Maintenance Message", state.maintenance.message);

  const game = panel("Game Defaults", "Canonical `system.gameDefaults`");
  game.append(grid(mode.root, ship.root, difficulty.root), grid(tutorial.root, pronunciation.root, autoSave.root));
  const network = panel("System & Network", "Canonical `system.network`");
  network.append(grid(minimumVersion.root, autoSaveInterval.root, reconnectWindow.root), grid(offlinePlay.root, telemetry.root));
  const danger = panel("Maintenance", "Canonical `system.maintenance` · publish-gated", "stx-danger-panel");
  danger.append(maintenance.root, maintenanceMessage.root, notice("Save Draft is safe: maintenance never changes the active revision until explicit Publish succeeds.", "warn"));
  const status = runtimeStatus();
  page.append(status.root, grid(game, network), danger);

  const applySystem = (value: GeneralSettingsConfig): void => {
    mode.control.value = value.gameDefaults.defaultMode;
    ship.control.value = value.gameDefaults.defaultShip;
    difficulty.control.value = value.gameDefaults.difficulty;
    for (const [control, checked] of [[tutorial.control, value.gameDefaults.tutorialEnabled], [pronunciation.control, value.gameDefaults.pronunciationDefault], [autoSave.control, value.gameDefaults.autoSave], [offlinePlay.control, value.network.offlinePlay], [telemetry.control, value.network.telemetry], [maintenance.control, value.maintenance.enabled]] as const) {
      control.classList.toggle("on", checked);
      control.setAttribute("aria-pressed", String(checked));
    }
    minimumVersion.control.value = value.network.minimumVersion;
    autoSaveInterval.control.value = String(value.network.autoSaveIntervalSeconds);
    reconnectWindow.control.value = String(value.network.reconnectWindowSeconds);
    maintenanceMessage.control.value = value.maintenance.message;
  };

  void api.getState().then((payload) => {
    loadedActiveRevision = payload.state.activeRevision;
    revisionBadge.textContent = `ACTIVE · ${payload.state.activeRevision}`;
    applySystem(payload.active.config.system ?? DEFAULT_SYSTEM);
    status.set(payload.active.config.system ? "Loaded canonical system config from active revision." : "Active revision predates Phase B system config; showing additive defaults until first draft is saved.", payload.active.config.system ? "good" : "warn");
  }).catch((error: unknown) => status.set(`Admin service unavailable: ${error instanceof Error ? error.message : String(error)}`, "bad"));

  page.append(saveBar(navigate, async (button, saveStatus) => {
    button.disabled = true;
    saveStatus.textContent = "Saving immutable draft…";
    try {
      const payload = await api.getState();
      assertStableActiveRevision(loadedActiveRevision, payload.state.activeRevision);
      const config = cloneConfig(payload.active.config);
      config.system = {
        gameDefaults: {
          defaultMode: mode.control.value as GeneralSettingsConfig["gameDefaults"]["defaultMode"],
          defaultShip: ship.control.value.trim(),
          difficulty: difficulty.control.value as GeneralSettingsConfig["gameDefaults"]["difficulty"],
          tutorialEnabled: enabled(tutorial.control),
          pronunciationDefault: enabled(pronunciation.control),
          autoSave: enabled(autoSave.control),
        },
        network: {
          minimumVersion: minimumVersion.control.value.trim(),
          autoSaveIntervalSeconds: numberValue(autoSaveInterval.control),
          reconnectWindowSeconds: numberValue(reconnectWindow.control),
          offlinePlay: enabled(offlinePlay.control),
          telemetry: enabled(telemetry.control),
        },
        maintenance: {
          enabled: enabled(maintenance.control),
          message: maintenanceMessage.control.value.trim(),
        },
      };
      const revision = await api.createRevision({ baseRevision: payload.active.revision, config, message: "Admin Phase B · General Settings draft" });
      saveStatus.textContent = `Draft saved · ${revision.revision} · runtime unchanged`;
      status.set(`Draft ${revision.revision} created from active ${payload.active.revision}. Publish it from History only after review.`, "good");
    } catch (error: unknown) {
      const message = error instanceof Error ? error.message : String(error);
      saveStatus.textContent = `Draft rejected · ${message}`;
      status.set(`Validation/save failed: ${message}`, "bad");
    } finally {
      button.disabled = false;
    }
  }));
  return page;
}

function humanizeFlag(id: string): string {
  return id.split("-").map((part) => part.charAt(0).toUpperCase() + part.slice(1)).join(" ");
}

function renderFlags(navigate: Navigate): HTMLElement {
  const page = el("div");
  const revisionBadge = badge("ACTIVE · loading", "info");
  page.append(header(
    "System · Controlled Rollout · Phase B",
    "Feature Flags",
    "Revision-backed rollouts. Economy/competitive flags remain publish-gated and use a new-session boundary; Save Draft never changes live admission.",
    [revisionBadge],
  ));
  let loadedActiveRevision: string | null = null;
  const status = runtimeStatus();
  const host = el("div", "stx-flag-list");
  page.append(status.root, host);

  let renderedFlags: Record<string, FeatureFlagConfig> = structuredClone(DEFAULT_FLAGS);
  const controls = new Map<string, { rollout: HTMLInputElement; scope: HTMLSelectElement; enabled: HTMLButtonElement; risk: FeatureFlagConfig["risk"] }>();

  const render = (flags: Record<string, FeatureFlagConfig>): void => {
    renderedFlags = structuredClone(flags);
    controls.clear();
    host.replaceChildren();
    for (const [id, flag] of Object.entries(flags).sort(([a], [b]) => a.localeCompare(b))) {
      const row = panel(humanizeFlag(id), id);
      const rolloutWrap = el("div", "stx-range");
      const rolloutTop = el("div");
      const rolloutValue = el("strong", undefined, `${flag.rolloutPercent}%`);
      rolloutTop.append(el("span", undefined, "Rollout"), rolloutValue);
      const rollout = el("input") as HTMLInputElement;
      rollout.type = "range";
      rollout.min = "0";
      rollout.max = "100";
      rollout.value = String(flag.rolloutPercent);
      rollout.setAttribute("aria-label", `${humanizeFlag(id)} rollout percent`);
      rollout.addEventListener("input", () => { rolloutValue.textContent = `${rollout.value}%`; });
      rolloutWrap.append(rolloutTop, rollout);

      const scopeField = field("Scope", flag.scope, ["all", "new-players", "cohort", "environment", "accounts"]);
      const enabledToggle = toggle("Enabled", flag.enabled);
      const riskTone: Tone = flag.risk === "normal" ? "info" : "warn";
      const body = el("div", "stx-flag-row");
      body.append(rolloutWrap, scopeField.root, badge(flag.risk.toUpperCase(), riskTone), enabledToggle.root);
      row.append(body);
      host.append(row);
      controls.set(id, { rollout, scope: scopeField.control as HTMLSelectElement, enabled: enabledToggle.control, risk: flag.risk });
    }
  };
  render(renderedFlags);

  void api.getState().then((payload) => {
    loadedActiveRevision = payload.state.activeRevision;
    revisionBadge.textContent = `ACTIVE · ${payload.state.activeRevision}`;
    render(payload.active.config.featureFlags ?? DEFAULT_FLAGS);
    status.set(payload.active.config.featureFlags ? "Loaded canonical feature flags from active revision." : "Active revision predates Phase B flags; showing additive defaults until first draft is saved.", payload.active.config.featureFlags ? "good" : "warn");
  }).catch((error: unknown) => status.set(`Admin service unavailable: ${error instanceof Error ? error.message : String(error)}`, "bad"));

  page.append(saveBar(navigate, async (button, saveStatus) => {
    button.disabled = true;
    saveStatus.textContent = "Saving immutable rollout draft…";
    try {
      const payload = await api.getState();
      assertStableActiveRevision(loadedActiveRevision, payload.state.activeRevision);
      const config = cloneConfig(payload.active.config);
      const nextFlags: Record<string, FeatureFlagConfig> = structuredClone(payload.active.config.featureFlags ?? renderedFlags);
      for (const [id, control] of controls) {
        nextFlags[id] = {
          enabled: enabled(control.enabled),
          rolloutPercent: Number(control.rollout.value),
          scope: control.scope.value as FeatureFlagScope,
          risk: control.risk,
        };
      }
      config.featureFlags = nextFlags;
      const revision = await api.createRevision({ baseRevision: payload.active.revision, config, message: "Admin Phase B · Feature Flags draft" });
      saveStatus.textContent = `Draft saved · ${revision.revision} · runtime unchanged`;
      status.set(`Draft ${revision.revision} created. Economy/competitive changes remain inactive until explicit Publish.`, "good");
    } catch (error: unknown) {
      const message = error instanceof Error ? error.message : String(error);
      saveStatus.textContent = `Draft rejected · ${message}`;
      status.set(`Validation/save failed: ${message}`, "bad");
    } finally {
      button.disabled = false;
    }
  }));
  return page;
}

export function renderPhaseBAdminScreen(path: string, navigate: Navigate): HTMLElement | null {
  if (path === `${BASE}/audio`) return renderPhaseBAudio(navigate);
  if (path === `${BASE}/settings`) return renderSettings(navigate);
  if (path === `${BASE}/flags`) return renderFlags(navigate);
  return null;
}
