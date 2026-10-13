import "./space-typing-asset-preview.css";
import {
  SpaceTypingAdminApi,
  type CoreStatKey,
  type ShipAdminOverride,
  type ShipAdminPolicy,
  type ShipAdminPreview,
  type ShipAdminPreviewItem,
  type ShipVisualProfile,
  type SpaceTypingAdminConfig,
} from "./api";
import { adminErrorMessage } from "./admin-http";
import {
  SpaceTypingAssetPreviewBridge,
  type SpaceTypingAssetPreviewScenario,
  type SpaceTypingAssetPreviewSource,
} from "./space-typing-asset-preview";

const api = new SpaceTypingAdminApi();
const CORE_STATS: readonly CoreStatKey[] = [
  "hull",
  "shield",
  "firepower",
  "armor",
  "energy",
  "reactor",
  "focus",
  "ward",
  "luck",
  "salvage",
];
const SILHOUETTES = ["spear", "fortress", "arc", "phantom", "crown", "blade"] as const;
const COLOR_KEYS = ["primary", "secondary", "accent", "core", "engine", "glow"] as const;
const TEXT_FIELDS = [
  ["name", "Name"],
  ["role", "Role"],
  ["summary", "Summary"],
  ["passiveName", "Passive Name"],
  ["activeName", "Active Name"],
  ["ultimateName", "Ultimate Name"],
] as const;

type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";
type ShipId = string;

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

function field(label: string, value: string, options?: readonly string[], type: "text" | "number" = "text"): { root: HTMLElement; control: HTMLInputElement | HTMLSelectElement } {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label));
  let control: HTMLInputElement | HTMLSelectElement;
  if (options) {
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

function grid(...children: HTMLElement[]): HTMLElement {
  const root = el("div", "stx-grid");
  root.append(...children);
  return root;
}

function cloneConfig(config: SpaceTypingAdminConfig): SpaceTypingAdminConfig {
  return structuredClone(config);
}

function mergeShip(base: ShipAdminPreviewItem, override?: ShipAdminOverride): ShipAdminPreviewItem {
  return {
    ...base,
    ...(override ?? {}),
    id: base.id,
    assetId: base.assetId,
    statBonus: { ...base.statBonus, ...(override?.statBonus ?? {}) },
    visual: { ...base.visual, ...(override?.visual ?? {}) },
    overridden: override !== undefined && Object.keys(override).length > 0,
  };
}

function policyFrom(config: SpaceTypingAdminConfig): ShipAdminPolicy {
  return structuredClone(config.content?.ships ?? { configRevision: "ships-admin-v1", ships: {} });
}

function previewVisual(ship: ShipAdminPreviewItem): Readonly<Record<string, unknown>> {
  return structuredClone(ship.visual) as unknown as Readonly<Record<string, unknown>>;
}

export function renderPhaseBShips(navigate: Navigate): HTMLElement {
  const page = el("div");
  const revisionBadge = badge("ACTIVE · loading", "info");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Game Content · Runtime-backed Registry · B06.1"),
    el("h1", undefined, "Ships"),
    el("p", undefined, "Author identity metadata, progression discovery milestones, combat stat bonuses and visual profiles against the child runtime registry. Selection remains independent of Campaign unlock milestones."),
  );
  header.append(copy, revisionBadge);
  page.append(header);

  const status = notice("Loading active revision and canonical child ship registry…", "info");
  status.setAttribute("aria-live", "polite");

  const previewPanel = panel(
    "Production Visual Preview",
    "A5.0 isolated preview · Draft and Published use the child production renderer without changing PlayerSave, Shop state, active revision or Media current.",
  );
  previewPanel.classList.add("st-admin-asset-preview-panel");
  const previewToolbar = el("div", "st-admin-asset-preview-toolbar");
  const draftPreviewButton = button("Draft", () => selectPreviewSource("draft"), "st-admin-btn primary");
  const publishedPreviewButton = button("Published", () => selectPreviewSource("published"));
  const idlePreviewButton = button("Idle", () => selectPreviewScenario("idle"), "st-admin-btn primary");
  const movePreviewButton = button("Move", () => selectPreviewScenario("move"));
  const firePreviewButton = button("Fire", () => selectPreviewScenario("fire"));
  previewToolbar.append(
    el("strong", undefined, "Source"),
    draftPreviewButton,
    publishedPreviewButton,
    el("strong", undefined, "Scenario"),
    idlePreviewButton,
    movePreviewButton,
    firePreviewButton,
  );
  const previewHost = el("div", "st-admin-asset-preview-stage");
  const previewStatus = el("div", "st-admin-asset-preview-status", "Waiting for the canonical fleet before starting preview…");
  previewStatus.setAttribute("aria-live", "polite");
  previewPanel.append(previewToolbar, previewHost, previewStatus);

  const body = el("div", "stx-grid");
  const listPanel = panel("Canonical Fleet", "11 child-owned ship IDs · IDs and asset IDs are immutable");
  const listHost = el("div");
  listPanel.append(listHost);
  const editorPanel = panel("Ship Override", "Only authored differences are persisted in `content.ships.ships.<id>`");
  const editorHost = el("div");
  editorPanel.append(editorHost);
  body.append(listPanel, editorPanel);
  page.append(status, previewPanel, body);

  let loadedActiveRevision: string | null = null;
  let bundled: ShipAdminPreview | null = null;
  let publishedPreview: ShipAdminPreview | null = null;
  let selectedId: ShipId = "vanguard";
  let policy: ShipAdminPolicy = { configRevision: "ships-admin-v1", ships: {} };
  let serviceReady = false;
  let loadGeneration = 0;
  let previewSource: SpaceTypingAssetPreviewSource = "draft";
  let previewScenario: SpaceTypingAssetPreviewScenario = "idle";
  let previewGeneration = 0;
  let previewBridge: SpaceTypingAssetPreviewBridge | null = null;
  let previewBridgePromise: Promise<SpaceTypingAssetPreviewBridge> | null = null;

  const setStatus = (text: string, tone: Tone = "info"): void => {
    status.className = `stx-notice ${tone}`;
    status.textContent = text;
  };

  const setPreviewStatus = (text: string, tone: Tone = "info"): void => {
    previewStatus.className = `st-admin-asset-preview-status ${tone}`;
    previewStatus.textContent = text;
  };

  const overrideFor = (id: ShipId): ShipAdminOverride => {
    policy.ships ??= {};
    policy.ships[id] ??= {};
    return policy.ships[id];
  };

  const baseShip = (id: ShipId): ShipAdminPreviewItem | undefined =>
    bundled?.ships.find((ship) => ship.id === id);

  const effectiveShip = (id: ShipId): ShipAdminPreviewItem | undefined => {
    const base = baseShip(id);
    if (!base) return publishedPreview?.ships.find((ship) => ship.id === id);
    return mergeShip(base, policy.ships?.[id]);
  };

  const previewShip = (): ShipAdminPreviewItem | undefined =>
    previewSource === "published"
      ? publishedPreview?.ships.find((ship) => ship.id === selectedId)
      : effectiveShip(selectedId);

  function refreshPreviewButtons(): void {
    draftPreviewButton.classList.toggle("primary", previewSource === "draft");
    publishedPreviewButton.classList.toggle("primary", previewSource === "published");
    idlePreviewButton.classList.toggle("primary", previewScenario === "idle");
    movePreviewButton.classList.toggle("primary", previewScenario === "move");
    firePreviewButton.classList.toggle("primary", previewScenario === "fire");
  }

  async function ensurePreviewBridge(): Promise<SpaceTypingAssetPreviewBridge> {
    if (previewBridge !== null) return previewBridge;
    if (previewBridgePromise !== null) return previewBridgePromise;
    setPreviewStatus("Connecting to isolated child production preview…", "info");
    const mountPromise = SpaceTypingAssetPreviewBridge.mount(previewHost).then(async (bridge) => {
      if (!page.isConnected) {
        bridge.disposeImmediately();
        throw new Error("Ships page was closed before preview became ready.");
      }
      previewBridge = bridge;
      await bridge.waitUntilReady();
      return bridge;
    }).catch((error: unknown) => {
      if (previewBridge?.iframe.isConnected === false) previewBridge = null;
      previewBridgePromise = null;
      throw error;
    });
    previewBridgePromise = mountPromise;
    return mountPromise;
  }

  function syncPreview(): void {
    const generation = ++previewGeneration;
    refreshPreviewButtons();
    if (!serviceReady) {
      setPreviewStatus("Waiting for active revision and canonical ship registry…", "info");
      return;
    }
    const ship = previewShip();
    if (ship === undefined) {
      setPreviewStatus(`No ${previewSource} preview candidate exists for ${selectedId}.`, "warn");
      return;
    }
    setPreviewStatus(`Loading ${previewSource} · ${ship.id} · ${previewScenario} through production renderer…`, "info");
    void ensurePreviewBridge().then(async (bridge) => {
      if (generation !== previewGeneration || !page.isConnected) return;
      await bridge.loadShip({ characterId: ship.id, visual: previewVisual(ship) });
      if (generation !== previewGeneration || !page.isConnected) return;
      await bridge.setScenario(previewScenario);
      if (generation !== previewGeneration || !page.isConnected) return;
      setPreviewStatus(`${previewSource === "draft" ? "Draft" : "Published"} · ${ship.id} · ${previewScenario} · production renderer`, "good");
    }).catch((error: unknown) => {
      if (generation !== previewGeneration || !page.isConnected) return;
      setPreviewStatus(error instanceof Error ? error.message : String(error), "bad");
    });
  }

  function selectPreviewSource(source: SpaceTypingAssetPreviewSource): void {
    if (previewSource === source) return;
    previewSource = source;
    syncPreview();
  }

  function selectPreviewScenario(scenario: SpaceTypingAssetPreviewScenario): void {
    if (previewScenario === scenario) return;
    previewScenario = scenario;
    const generation = ++previewGeneration;
    refreshPreviewButtons();
    const bridge = previewBridge;
    if (bridge === null) {
      syncPreview();
      return;
    }
    setPreviewStatus(`Switching to ${scenario} production scenario…`, "info");
    void bridge.setScenario(scenario).then(() => {
      if (generation !== previewGeneration || !page.isConnected) return;
      const ship = previewShip();
      setPreviewStatus(`${previewSource === "draft" ? "Draft" : "Published"} · ${ship?.id ?? selectedId} · ${scenario} · production renderer`, "good");
    }).catch((error: unknown) => {
      if (generation !== previewGeneration || !page.isConnected) return;
      setPreviewStatus(error instanceof Error ? error.message : String(error), "bad");
    });
  }

  const renderList = (): void => {
    listHost.replaceChildren();
    const ships = bundled?.ships ?? publishedPreview?.ships ?? [];
    if (ships.length === 0) {
      listHost.append(notice(serviceReady ? "No canonical ships were returned by the preview." : "Load the canonical ship registry to browse the fleet.", serviceReady ? "warn" : "info"));
      return;
    }
    for (const ship of ships) {
      const current = effectiveShip(ship.id) ?? ship;
      const row = el("div", "stx-toggle-row");
      const copyNode = el("div");
      copyNode.append(el("strong", undefined, current.name), el("small", undefined, `${ship.id} · ${current.assetId} · stage ${current.unlockStage}`));
      const actions = el("div");
      if (policy.ships?.[ship.id] && Object.keys(policy.ships[ship.id]).length > 0) actions.append(badge("OVERRIDE", "warn"));
      const select = button(selectedId === ship.id ? "Editing" : "Edit", () => {
        selectedId = ship.id;
        renderList();
        renderEditor();
        syncPreview();
      }, selectedId === ship.id ? "st-admin-btn primary" : "st-admin-btn");
      select.disabled = !serviceReady;
      actions.append(select);
      row.append(copyNode, actions);
      listHost.append(row);
    }
  };

  const bindText = (control: HTMLInputElement | HTMLSelectElement, key: keyof ShipAdminOverride): void => {
    control.addEventListener("input", () => {
      (overrideFor(selectedId) as Record<string, unknown>)[key] = control.value;
      renderList();
    });
  };

  const renderEditor = (): void => {
    editorHost.replaceChildren();
    const ship = effectiveShip(selectedId);
    if (!serviceReady || !ship) {
      editorHost.append(notice(serviceReady ? "No ship is available for editing." : "Load the active revision and canonical ship preview before editing overrides.", serviceReady ? "warn" : "info"));
      return;
    }

    const identity = el("div", "stx-notice info", `ID ${ship.id} · asset ${ship.assetId} · apply boundary: new session`);
    editorHost.append(identity);

    const metadata = panel("Identity & Discovery", "`unlockStage` updates discovery/progression metadata only; it does not prevent selecting the ship.");
    const metaFields: HTMLElement[] = [];
    for (const [key, label] of TEXT_FIELDS) {
      const item = field(label, String(ship[key]));
      bindText(item.control, key);
      metaFields.push(item.root);
    }
    const unlock = field("Unlock / Discovery Stage", String(ship.unlockStage), undefined, "number");
    (unlock.control as HTMLInputElement).min = "1";
    (unlock.control as HTMLInputElement).max = "1000";
    unlock.control.addEventListener("input", () => {
      overrideFor(selectedId).unlockStage = Number(unlock.control.value);
      renderList();
    });
    metadata.append(grid(metaFields[0], unlock.root, metaFields[1]), grid(metaFields[2], metaFields[3], metaFields[4]), metaFields[5]);

    const stats = panel("Combat Stat Bonuses", "Child `characterStatBonus()` keys · allowed range -100..100");
    const statFields: HTMLElement[] = [];
    for (const key of CORE_STATS) {
      const item = field(key, String(ship.statBonus[key] ?? 0), undefined, "number");
      const input = item.control as HTMLInputElement;
      input.min = "-100";
      input.max = "100";
      input.step = "0.1";
      input.addEventListener("input", () => {
        const override = overrideFor(selectedId);
        override.statBonus ??= {};
        override.statBonus[key] = Number(input.value);
      });
      statFields.push(item.root);
    }
    for (let index = 0; index < statFields.length; index += 3) stats.append(grid(...statFields.slice(index, index + 3)));

    const visual = panel("Visual Profile", "Procedural/profile fallback fields consumed by the child production renderer; unsaved preview remains ephemeral.");
    const silhouette = field("Silhouette", ship.visual.silhouette, SILHOUETTES);
    silhouette.control.addEventListener("change", () => {
      const override = overrideFor(selectedId);
      override.visual ??= {};
      override.visual.silhouette = silhouette.control.value as ShipVisualProfile["silhouette"];
      syncPreview();
    });
    const visualFields: HTMLElement[] = [silhouette.root];
    for (const key of COLOR_KEYS) {
      const item = field(key, ship.visual[key]);
      item.control.addEventListener("input", () => {
        const override = overrideFor(selectedId);
        override.visual ??= {};
        override.visual[key] = item.control.value;
        syncPreview();
      });
      visualFields.push(item.root);
    }
    for (const key of ["wingSpan", "bodyLength"] as const) {
      const item = field(key, String(ship.visual[key]), undefined, "number");
      const input = item.control as HTMLInputElement;
      input.min = "0.5";
      input.max = "2";
      input.step = "0.01";
      input.addEventListener("input", () => {
        const override = overrideFor(selectedId);
        override.visual ??= {};
        override.visual[key] = Number(input.value);
        syncPreview();
      });
      visualFields.push(item.root);
    }
    const engines = field("engineCount", String(ship.visual.engineCount), ["1", "2", "3"]);
    engines.control.addEventListener("change", () => {
      const override = overrideFor(selectedId);
      override.visual ??= {};
      override.visual.engineCount = Number(engines.control.value) as 1 | 2 | 3;
      syncPreview();
    });
    visualFields.push(engines.root);
    for (let index = 0; index < visualFields.length; index += 3) visual.append(grid(...visualFields.slice(index, index + 3)));

    const actions = el("div", "st-admin-page-actions");
    actions.append(
      button("Reset Ship Override", () => {
        if (policy.ships) delete policy.ships[selectedId];
        renderList();
        renderEditor();
        syncPreview();
        setStatus(`${selectedId} reset to bundled child runtime values. Save Draft to persist this removal.`, "good");
      }),
      button("Validate Draft", () => {
        setStatus("Validating current Draft ship overrides against the canonical child policy…", "info");
        void api.previewShips({ policy }).then((validatedDraft) => {
          renderList();
          renderEditor();
          syncPreview();
          setStatus(`Child canonical policy accepted Draft ${validatedDraft.configRevision} with ${validatedDraft.ships.length} ships. Published preview remains the active revision.`, "good");
        }).catch((error: unknown) => setStatus(adminErrorMessage(error, "The Draft ship policy could not be validated. Check the local Admin runtime and try again."), "bad"));
      }, "st-admin-btn primary"),
    );
    editorHost.append(metadata, stats, visual, actions);
  };

  const saveBar = el("div", "st-admin-sticky-save stx-savebar");
  const saveStatus = el("span", undefined, "Load the active revision before saving a ship draft");
  const save = button("Save Draft", () => {
    void (async () => {
      if (!serviceReady) return;
      save.disabled = true;
      saveStatus.textContent = "Validating against child runtime…";
      try {
        const payload = await api.getState();
        if (loadedActiveRevision === null || loadedActiveRevision !== payload.state.activeRevision) {
          throw new Error(`Active revision changed from ${loadedActiveRevision ?? "not-loaded"} to ${payload.state.activeRevision}. Reload this screen before saving to avoid overwriting newer published changes.`);
        }
        await api.previewShips({ policy });
        const config = cloneConfig(payload.active.config);
        config.content = { ...(config.content ?? {}), ships: structuredClone(policy) };
        const revision = await api.createRevision({
          baseRevision: payload.active.revision,
          config,
          message: "Admin Phase B · B06.1 Ships registry draft",
        });
        saveStatus.textContent = `Draft saved · ${revision.revision} · runtime unchanged`;
        setStatus(`Draft ${revision.revision} passed child policy + server validation. Published preview still reflects active ${loadedActiveRevision}; publish from History to change runtime policy. Gameplay apply boundary is a new session.`, "good");
      } catch (error: unknown) {
        const message = adminErrorMessage(error, "The Ships draft could not be saved. Check the local Admin runtime and try again.");
        saveStatus.textContent = `Draft rejected · ${message}`;
        setStatus(`Validation/save failed: ${message}`, "bad");
      } finally {
        save.disabled = !serviceReady;
      }
    })();
  }, "st-admin-btn primary");
  save.disabled = true;
  saveBar.append(el("strong", undefined, "B06.1 Ships Draft"), saveStatus, el("div", "grow"), button("Discard", () => navigate(location.pathname)), save);
  page.append(saveBar);

  const load = (): void => {
    const generation = ++loadGeneration;
    ++previewGeneration;
    serviceReady = false;
    loadedActiveRevision = null;
    bundled = null;
    publishedPreview = null;
    revisionBadge.className = "st-admin-status info";
    revisionBadge.textContent = "ACTIVE · loading";
    setStatus("Loading active revision and canonical child ship registry…", "info");
    setPreviewStatus("Waiting for active revision and canonical ship registry…", "info");
    saveStatus.textContent = "Load the active revision before saving a ship draft";
    save.disabled = true;
    renderList();
    renderEditor();

    void Promise.all([api.getState(), api.previewShips()]).then(async ([statePayload, bundledPreview]) => {
      const nextPolicy = policyFrom(statePayload.active.config);
      const nextPublishedPreview = await api.previewShips({ policy: nextPolicy });
      if (generation !== loadGeneration) return;
      loadedActiveRevision = statePayload.state.activeRevision;
      bundled = bundledPreview;
      policy = nextPolicy;
      publishedPreview = nextPublishedPreview;
      serviceReady = true;
      selectedId = publishedPreview.ships[0]?.id ?? "vanguard";
      revisionBadge.className = "st-admin-status good";
      revisionBadge.textContent = `ACTIVE · ${statePayload.state.activeRevision}`;
      saveStatus.textContent = "Revision-backed · no direct runtime mutation";
      save.disabled = false;
      renderList();
      renderEditor();
      syncPreview();
      setStatus(
        statePayload.active.config.content?.ships
          ? `Loaded active Ships policy ${policy.configRevision}. Draft is isolated until History / Publish; Published preview is pinned to active ${statePayload.state.activeRevision}.`
          : "Active revision predates B06.1 Ships policy; bundled child registry is shown until the first draft is saved.",
        statePayload.active.config.content?.ships ? "good" : "warn",
      );
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      ++previewGeneration;
      serviceReady = false;
      loadedActiveRevision = null;
      revisionBadge.className = "st-admin-status bad";
      revisionBadge.textContent = "ACTIVE · unavailable";
      save.disabled = true;
      setPreviewStatus("Preview is disabled until the canonical fleet is available.", "bad");
      listHost.replaceChildren(notice("The canonical fleet could not be loaded. Retry after the local Admin service is available.", "bad"));
      editorHost.replaceChildren(notice("Ship overrides are disabled until the active revision and canonical preview are loaded.", "warn"));
      status.className = "stx-notice bad";
      status.replaceChildren(document.createTextNode(adminErrorMessage(error, "The Ships Admin service is unavailable. Check the local runtime and try again.")), document.createTextNode(" "), button("Retry", load));
    });
  };

  const lifecycleObserver = new MutationObserver(() => {
    if (page.isConnected) return;
    lifecycleObserver.disconnect();
    ++previewGeneration;
    previewBridge?.disposeImmediately();
    previewBridge = null;
    previewBridgePromise = null;
  });
  queueMicrotask(() => {
    if (page.isConnected) {
      lifecycleObserver.observe(document.body, { childList: true, subtree: true });
    } else {
      previewBridge?.disposeImmediately();
      previewBridge = null;
      previewBridgePromise = null;
    }
  });

  refreshPreviewButtons();
  load();
  return page;
}
