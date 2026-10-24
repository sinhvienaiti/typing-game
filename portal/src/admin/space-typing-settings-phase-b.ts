import { renderPhaseBSettings as renderLegacyPhaseBSettings } from "./space-typing-settings-phase-b-legacy";
import {
  SpaceTypingAdminApi,
  type SpaceTypingAdminConfig,
} from "./api";

type Navigate = (path: string) => void;
type TestingOverrides = {
  unlockAllStages: boolean;
  unlockAllShips: boolean;
};
type SystemWithTesting = NonNullable<SpaceTypingAdminConfig["system"]> & {
  testing?: TestingOverrides;
};

const api = new SpaceTypingAdminApi();
const DEFAULT_TESTING: TestingOverrides = {
  unlockAllStages: false,
  // Preserve the pre-policy product behavior until an administrator explicitly
  // disables the all-ship testing override in a published revision.
  unlockAllShips: true,
};
const DEFAULT_SYSTEM: NonNullable<SpaceTypingAdminConfig["system"]> = {
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

function createSwitch(label: string, description: string): {
  root: HTMLElement;
  control: HTMLButtonElement;
} {
  const root = el("div", "stx-toggle-row");
  const copy = el("div");
  copy.append(el("strong", undefined, label), el("small", undefined, description));
  const control = el("button", "st-admin-switch") as HTMLButtonElement;
  control.type = "button";
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

function applySwitch(control: HTMLButtonElement, value: boolean): void {
  control.setAttribute("aria-pressed", String(value));
  control.classList.toggle("on", value);
}

function switchValue(control: HTMLButtonElement): boolean {
  return control.getAttribute("aria-pressed") === "true";
}

function testingFromConfig(config: SpaceTypingAdminConfig): TestingOverrides {
  const system = config.system as SystemWithTesting | undefined;
  const testing = system?.testing;
  return {
    unlockAllStages: testing?.unlockAllStages === true,
    unlockAllShips:
      typeof testing?.unlockAllShips === "boolean"
        ? testing.unlockAllShips
        : DEFAULT_TESTING.unlockAllShips,
  };
}

function createTestingOverridesPanel(navigate: Navigate): HTMLElement {
  const panel = el("section", "st-admin-panel solid stx-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(
    el("h2", undefined, "Testing Overrides"),
    el(
      "p",
      undefined,
      "Published game-policy overrides for real Space Typing sessions. These are administrator controls, never player preferences.",
    ),
  );
  const historyButton = el("button", "st-admin-btn", "History / Publish") as HTMLButtonElement;
  historyButton.type = "button";
  historyButton.addEventListener("click", () => navigate("/admin/space-typing/history"));
  head.append(copy, historyButton);
  panel.append(head);

  const unlockStages = createSwitch(
    "Unlock all stages",
    "Allows Stage Select 001–1000 for testing. Locked-stage runs use the existing testing-preview path and do not advance Campaign progress or rewards.",
  );
  const unlockShips = createSwitch(
    "Unlock all ships",
    "Makes every ship selectable in Hangar for new sessions without adding ownership to player progression. When disabled, Hangar respects the player's persisted unlocked entitlement.",
  );
  unlockStages.control.disabled = true;
  unlockShips.control.disabled = true;

  const notice = el(
    "div",
    "stx-notice info",
    "Loading published testing policy…",
  );
  notice.setAttribute("aria-live", "polite");

  const save = el("button", "st-admin-btn primary", "Save Testing Draft") as HTMLButtonElement;
  save.type = "button";
  save.disabled = true;
  const discard = el("button", "st-admin-btn", "Discard") as HTMLButtonElement;
  discard.type = "button";
  discard.disabled = true;
  const actions = el("div", "st-admin-page-actions");
  actions.append(discard, save);

  panel.append(
    el(
      "div",
      "stx-notice warn",
      "Apply boundary: new game session. Save Draft alone does not affect gameplay; publish the revision, then reload/start a new Space Typing session.",
    ),
    unlockStages.root,
    unlockShips.root,
    notice,
    actions,
  );

  let activeRevision: string | null = null;
  let generation = 0;

  function setEditable(editable: boolean): void {
    unlockStages.control.disabled = !editable;
    unlockShips.control.disabled = !editable;
    save.disabled = !editable;
    discard.disabled = !editable;
  }

  async function load(): Promise<void> {
    const currentGeneration = ++generation;
    activeRevision = null;
    setEditable(false);
    notice.className = "stx-notice info";
    notice.textContent = "Loading published testing policy…";
    try {
      const payload = await api.getState();
      if (currentGeneration !== generation) return;
      const testing = testingFromConfig(payload.active.config);
      activeRevision = payload.state.activeRevision;
      applySwitch(unlockStages.control, testing.unlockAllStages);
      applySwitch(unlockShips.control, testing.unlockAllShips);
      notice.className = "stx-notice good";
      notice.textContent = `Published ${payload.state.activeRevision} · All stages ${testing.unlockAllStages ? "ON" : "OFF"} · All ships ${testing.unlockAllShips ? "ON" : "OFF"}`;
      setEditable(true);
    } catch (error: unknown) {
      if (currentGeneration !== generation) return;
      notice.className = "stx-notice bad";
      notice.textContent = error instanceof Error
        ? `Testing policy unavailable: ${error.message}`
        : "Testing policy unavailable.";
    }
  }

  discard.addEventListener("click", () => void load());
  save.addEventListener("click", () => void (async () => {
    if (activeRevision === null) return;
    setEditable(false);
    notice.className = "stx-notice info";
    notice.textContent = "Verifying active revision and saving testing draft…";
    try {
      const latest = await api.getState();
      if (latest.state.activeRevision !== activeRevision) {
        throw new Error(
          `Active revision changed from ${activeRevision} to ${latest.state.activeRevision}. Reload before saving.`,
        );
      }
      const config = structuredClone(latest.active.config) as SpaceTypingAdminConfig;
      const system = (config.system ?? DEFAULT_SYSTEM) as SystemWithTesting;
      config.system = {
        ...system,
        testing: {
          unlockAllStages: switchValue(unlockStages.control),
          unlockAllShips: switchValue(unlockShips.control),
        },
      } as NonNullable<SpaceTypingAdminConfig["system"]>;
      const revision = await api.createRevision({
        baseRevision: latest.active.revision,
        config,
        message: "Admin V2 · Testing Overrides draft",
      });
      notice.className = "stx-notice good";
      notice.textContent = `Draft ${revision.revision} saved · runtime unchanged until History / Publish.`;
    } catch (error: unknown) {
      notice.className = "stx-notice bad";
      notice.textContent = error instanceof Error
        ? `Testing draft rejected: ${error.message}`
        : "Testing draft rejected.";
    } finally {
      if (activeRevision !== null) setEditable(true);
    }
  })());

  void load();
  return panel;
}

export function renderPhaseBSettings(navigate: Navigate): HTMLElement {
  const page = renderLegacyPhaseBSettings(navigate);
  const testing = createTestingOverridesPanel(navigate);
  const access = el("section", "st-admin-panel solid stx-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(
    el("h2", undefined, "Access & Permissions"),
    el("p", undefined, "Review the server-enforced role template and effective permissions for this local Admin deployment."),
  );
  const button = el("button", "st-admin-btn", "Open Roles & Permissions") as HTMLButtonElement;
  button.type = "button";
  button.addEventListener("click", () => navigate("/admin/space-typing/roles"));
  head.append(copy, button);
  access.append(head);
  const status = el("div", "stx-notice info", "Loading effective role…");
  access.append(status);
  void api.getActor().then((actor) => {
    status.className = "stx-notice good";
    status.textContent = `${actor.actorDisplayName} · ${actor.role} · ${actor.permissions.length} effective permissions.`;
  }).catch(() => {
    status.className = "stx-notice warn";
    status.textContent = "Effective role could not be loaded. Server authorization remains authoritative.";
  });
  const header = page.querySelector(".st-admin-page-head");
  if (header !== null) {
    header.insertAdjacentElement("afterend", testing);
    testing.insertAdjacentElement("afterend", access);
  } else {
    page.prepend(access);
    page.prepend(testing);
  }
  return page;
}