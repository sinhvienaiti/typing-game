import { SpaceTypingAdminApi, type SpaceTypingAdminConfig } from "./api";
import { adminErrorMessage } from "./admin-http";

const api = new SpaceTypingAdminApi();
type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";
type WorldOverride = { enemyRoster: string[] };
type WorldPolicy = { configRevision: string; worlds: Record<string, WorldOverride> };
type WorldPreviewItem = {
  id: string;
  name: string;
  galaxy: number;
  stageStart: number;
  stageEnd: number;
  enemyFamilies: string[];
  enemyRoster: string[];
  elitePool: string[];
  sampleEnemyId: string;
  overridden: boolean;
};
type WorldPreview = {
  protocolVersion: 1;
  configRevision: string;
  authorableFields: ["enemyRoster"];
  structuralFields: string[];
  worlds: WorldPreviewItem[];
};
type WorldAwareConfig = SpaceTypingAdminConfig & {
  content?: NonNullable<SpaceTypingAdminConfig["content"]> & { worlds?: WorldPolicy };
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

function notice(text: string, tone: Tone = "info"): HTMLElement {
  return el("div", `stx-notice ${tone}`, text);
}

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

function readonlyField(label: string, value: string): HTMLElement {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label));
  const input = el("input") as HTMLInputElement;
  input.value = value;
  input.disabled = true;
  input.setAttribute("aria-label", label);
  root.append(input);
  return root;
}

function grid(...children: HTMLElement[]): HTMLElement {
  const root = el("div", "stx-grid");
  root.append(...children);
  return root;
}

function policyFrom(config: SpaceTypingAdminConfig): WorldPolicy {
  return structuredClone((config as WorldAwareConfig).content?.worlds ?? {
    configRevision: "worlds-admin-v1",
    worlds: {},
  });
}

function rosterText(values: readonly string[]): string {
  return values.join("\n");
}

function parseRoster(value: string): string[] {
  return value.split(/[\n,]+/).map((entry) => entry.trim()).filter(Boolean);
}

async function previewWorlds(policy?: WorldPolicy): Promise<WorldPreview> {
  const payload = await api.requestJson<WorldPreview>("/api/admin/space-typing/worlds/preview", {
    method: "POST",
    body: JSON.stringify(policy === undefined ? {} : { policy }),
  });
  if (
    payload.protocolVersion !== 1 ||
    !Array.isArray(payload.worlds) ||
    !Array.isArray(payload.authorableFields) ||
    !payload.authorableFields.includes("enemyRoster")
  ) {
    throw new Error("World preview response does not match the canonical Admin contract.");
  }
  return payload;
}

export function renderPhaseBWorlds(navigate: Navigate): HTMLElement {
  const page = el("div");
  const revisionBadge = badge("ACTIVE · loading");
  const dirtyBadge = badge("CLEAN", "good");
  const validationBadge = badge("NOT VALIDATED");

  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Game Content · World Runtime · B06.6"),
    el("h1", undefined, "Worlds & Stages · World Roster"),
    el("p", undefined, "Manage the verified World enemy-roster override while keeping World identity, Galaxy placement, stage ranges and enemy-family structure owned by the child runtime."),
  );
  const actions = el("div", "st-admin-page-actions");
  const stageOverridesButton = button("Stage Overrides", () => navigate("/admin/space-typing/worlds-stages"));
  actions.append(
    dirtyBadge,
    validationBadge,
    revisionBadge,
    stageOverridesButton,
    button("History / Publish", () => navigate("/admin/space-typing/history")),
  );
  header.append(copy, actions);
  page.append(header);

  const status = notice("Loading active revision and canonical World registry…");
  status.setAttribute("aria-live", "polite");
  page.append(status);

  const shell = el("div", "stx-grid");
  const listPanel = panel("Canonical Worlds", "50 child-owned Worlds · choose a World to inspect its runtime-backed enemy roster");
  const listHost = el("div");
  listPanel.append(listHost);
  const editorPanel = panel("World Enemy Roster", "One verified gameplay-backed authoring field: enemyRoster");
  const editorHost = el("div");
  editorPanel.append(editorHost);
  shell.append(listPanel, editorPanel);
  page.append(shell);

  let loadedActiveRevision: string | null = null;
  let bundled: WorldPreview | null = null;
  let activePreview: WorldPreview | null = null;
  let selectedId = "world-01";
  let policy: WorldPolicy = { configRevision: "worlds-admin-v1", worlds: {} };
  let baseline = "";
  let validated: string | null = null;
  let serviceReady = false;
  let loadGeneration = 0;

  const setStatus = (text: string, tone: Tone = "info"): void => {
    status.className = `stx-notice ${tone}`;
    status.textContent = text;
  };

  const baseWorld = (): WorldPreviewItem | undefined => bundled?.worlds.find((world) => world.id === selectedId);
  const effectiveWorld = (): WorldPreviewItem | undefined => activePreview?.worlds.find((world) => world.id === selectedId) ?? baseWorld();

  const refreshBadges = (): void => {
    const serialized = JSON.stringify(policy);
    const dirty = serialized !== baseline;
    dirtyBadge.textContent = dirty ? "DIRTY" : "CLEAN";
    dirtyBadge.className = `st-admin-status ${dirty ? "warn" : "good"}`;
    const valid = validated === serialized;
    validationBadge.textContent = valid ? "PREVIEW VALID" : "NOT VALIDATED";
    validationBadge.className = `st-admin-status ${valid ? "good" : "info"}`;
  };

  const renderList = (): void => {
    listHost.replaceChildren();
    const worlds = bundled?.worlds ?? [];
    if (!serviceReady || worlds.length === 0) {
      listHost.append(notice(
        serviceReady ? "No canonical Worlds were returned by the preview." : "Load the canonical World registry to browse World rosters.",
        serviceReady ? "warn" : "info",
      ));
      return;
    }

    for (const world of worlds) {
      const row = el("div", "stx-toggle-row");
      const rowCopy = el("div");
      rowCopy.append(
        el("strong", undefined, `${world.id} · ${world.name}`),
        el("small", undefined, `Galaxy ${world.galaxy} · Stages ${world.stageStart}–${world.stageEnd} · ${world.enemyRoster.length} bundled enemies`),
      );
      const rowActions = el("div");
      if (policy.worlds[world.id]) rowActions.append(badge("OVERRIDE", "warn"));
      const edit = button(selectedId === world.id ? "Editing" : "Edit", () => {
        selectedId = world.id;
        renderList();
        renderEditor();
      }, selectedId === world.id ? "st-admin-btn primary" : "st-admin-btn");
      edit.disabled = !serviceReady;
      rowActions.append(edit);
      row.append(rowCopy, rowActions);
      listHost.append(row);
    }
  };

  const renderEditor = (): void => {
    editorHost.replaceChildren();
    const base = baseWorld();
    if (!serviceReady || !base) {
      editorHost.append(notice(
        serviceReady ? "No World is selected." : "Load the active revision and canonical World preview before editing the enemy roster.",
        serviceReady ? "warn" : "info",
      ));
      return;
    }

    const override = policy.worlds[selectedId];
    const effectiveRoster = override?.enemyRoster ?? base.enemyRoster;
    editorHost.append(
      notice(`${base.id} · ${base.name} · Galaxy ${base.galaxy} · Stages ${base.stageStart}–${base.stageEnd}`, "info"),
      notice("World ID, Galaxy, stage range and enemy-family structure are immutable. The child preview validates every roster member against the canonical World family contract.", "warn"),
    );

    const structural = panel("Structural Identity", "Read-only canonical child fields");
    structural.append(grid(
      readonlyField("World ID", base.id),
      readonlyField("Galaxy", String(base.galaxy)),
      readonlyField("Stage Start", String(base.stageStart)),
      readonlyField("Stage End", String(base.stageEnd)),
      readonlyField("Enemy Families", base.enemyFamilies.join(", ")),
    ));

    const rosterPanel = panel("Gameplay Enemy Roster", "Enter one enemy ID per line, or separate IDs with commas");
    const label = el("label", "stx-field");
    label.append(el("span", undefined, "Enemy Roster"));
    const textarea = el("textarea") as HTMLTextAreaElement;
    textarea.value = rosterText(effectiveRoster);
    textarea.rows = Math.min(14, Math.max(6, effectiveRoster.length));
    textarea.setAttribute("aria-label", "World enemy roster");
    label.append(textarea);
    const rosterMeta = notice(`Bundled: ${base.enemyRoster.length} entries · Effective: ${effectiveRoster.length} · Gameplay sample: ${effectiveWorld()?.sampleEnemyId ?? base.sampleEnemyId}`, "info");
    rosterPanel.append(label, rosterMeta);
    textarea.addEventListener("input", () => {
      const next = parseRoster(textarea.value);
      if (next.length === 0) delete policy.worlds[selectedId];
      else policy.worlds[selectedId] = { enemyRoster: next };
      validated = null;
      activePreview = null;
      refreshBadges();
      renderList();
      rosterMeta.textContent = `Bundled: ${base.enemyRoster.length} entries · Draft: ${next.length}`;
    });

    const diff = panel("Bundled → Draft Diff", "Roster membership feeds the actual World enemy selector");
    const before = new Set(base.enemyRoster);
    const after = new Set(effectiveRoster);
    const added = effectiveRoster.filter((id) => !before.has(id));
    const removed = base.enemyRoster.filter((id) => !after.has(id));
    diff.append(
      notice(`Added: ${added.length ? added.join(", ") : "none"}`, added.length ? "warn" : "info"),
      notice(`Removed: ${removed.length ? removed.join(", ") : "none"}`, removed.length ? "warn" : "info"),
    );

    const editorActions = el("div", "st-admin-page-actions");
    editorActions.append(
      button("Reset World Override", () => {
        delete policy.worlds[selectedId];
        validated = null;
        activePreview = null;
        refreshBadges();
        renderList();
        renderEditor();
        setStatus(`${selectedId} reset to the bundled roster. Save Draft to persist the removal.`, "good");
      }),
      button("Validate Preview", () => {
        setStatus("Running canonical child World preview…");
        void previewWorlds(policy).then((preview) => {
          activePreview = preview;
          validated = JSON.stringify(policy);
          refreshBadges();
          renderList();
          renderEditor();
          const world = preview.worlds.find((entry) => entry.id === selectedId);
          setStatus(`Child preview accepted ${preview.worlds.length} Worlds; gameplay sample for ${selectedId}: ${world?.sampleEnemyId ?? "n/a"}.`, "good");
        }).catch((error: unknown) => {
          validated = null;
          refreshBadges();
          setStatus(adminErrorMessage(error, "The World roster preview could not be validated. Check the local Admin runtime and try again."), "bad");
        });
      }, "st-admin-btn primary"),
    );

    editorHost.append(structural, rosterPanel, diff, editorActions);
  };

  const saveBar = el("div", "st-admin-sticky-save stx-savebar");
  const saveStatus = el("span", undefined, "Load the active revision before saving a World roster draft");
  const save = button("Save Draft", () => {
    void (async () => {
      if (!serviceReady) return;
      save.disabled = true;
      saveStatus.textContent = "Validating canonical child preview…";
      try {
        const preview = await previewWorlds(policy);
        activePreview = preview;
        validated = JSON.stringify(policy);
        const current = await api.getState();
        if (loadedActiveRevision === null || current.state.activeRevision !== loadedActiveRevision) {
          throw new Error(`Active revision changed from ${loadedActiveRevision ?? "not-loaded"} to ${current.state.activeRevision}. Reload this screen before saving to avoid overwriting newer published changes.`);
        }
        const config = structuredClone(current.active.config) as WorldAwareConfig;
        config.content ??= {};
        config.content.worlds = structuredClone(policy);
        const revision = await api.createRevision({
          baseRevision: current.active.revision,
          config,
          message: "Admin Phase B · B06.6 World roster draft",
        });
        baseline = JSON.stringify(policy);
        refreshBadges();
        saveStatus.textContent = `Draft saved · ${revision.revision} · runtime unchanged`;
        setStatus(`Draft ${revision.revision} created. Review and Publish from History to activate it for new sessions.`, "good");
      } catch (error: unknown) {
        const message = adminErrorMessage(error, "The World roster draft could not be saved. Check the local Admin runtime and try again.");
        saveStatus.textContent = `Draft rejected · ${message}`;
        setStatus(`Validation/save failed: ${message}`, "bad");
      } finally {
        save.disabled = !serviceReady;
      }
    })();
  }, "st-admin-btn primary");
  save.disabled = true;
  saveBar.append(
    el("strong", undefined, "B06.6 World Draft"),
    saveStatus,
    el("div", "grow"),
    button("Discard", () => navigate(location.pathname)),
    save,
  );
  page.append(saveBar);

  const load = (): void => {
    const generation = ++loadGeneration;
    serviceReady = false;
    loadedActiveRevision = null;
    bundled = null;
    activePreview = null;
    revisionBadge.className = "st-admin-status info";
    revisionBadge.textContent = "ACTIVE · loading";
    stageOverridesButton.disabled = false;
    save.disabled = true;
    saveStatus.textContent = "Load the active revision before saving a World roster draft";
    setStatus("Loading active revision and canonical World registry…", "info");
    renderList();
    renderEditor();

    void Promise.all([api.getState(), previewWorlds()]).then(async ([state, bundledPreview]) => {
      const nextPolicy = policyFrom(state.active.config);
      const nextPreview = await previewWorlds(nextPolicy);
      if (generation !== loadGeneration) return;
      loadedActiveRevision = state.state.activeRevision;
      bundled = bundledPreview;
      policy = nextPolicy;
      baseline = JSON.stringify(policy);
      activePreview = nextPreview;
      validated = JSON.stringify(policy);
      selectedId = Object.keys(policy.worlds)[0] ?? bundledPreview.worlds[0]?.id ?? "world-01";
      serviceReady = true;
      revisionBadge.className = "st-admin-status good";
      revisionBadge.textContent = `ACTIVE · ${state.state.activeRevision}`;
      save.disabled = false;
      saveStatus.textContent = "Revision-backed · no direct runtime mutation";
      refreshBadges();
      renderList();
      renderEditor();
      const hasPolicy = (state.active.config as WorldAwareConfig).content?.worlds !== undefined;
      setStatus(
        hasPolicy
          ? `Loaded active World policy ${policy.configRevision}. ${Object.keys(policy.worlds).length} explicit override(s); Save Draft remains isolated until Publish.`
          : "Active revision predates the World roster policy. Bundled child rosters remain the fallback until the first World draft is saved.",
        hasPolicy ? "good" : "warn",
      );
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      serviceReady = false;
      loadedActiveRevision = null;
      revisionBadge.className = "st-admin-status bad";
      revisionBadge.textContent = "ACTIVE · unavailable";
      save.disabled = true;
      listHost.replaceChildren(notice("The canonical World registry could not be loaded. Retry after the local Admin service is available.", "bad"));
      editorHost.replaceChildren(notice("World roster editing is disabled until the active revision and canonical preview are loaded.", "warn"));
      status.className = "stx-notice bad";
      status.replaceChildren(
        document.createTextNode(adminErrorMessage(error, "The Worlds Admin service is unavailable. Check the local runtime and try again.")),
        document.createTextNode(" "),
        button("Retry", load),
      );
    });
  };

  load();
  return page;
}
