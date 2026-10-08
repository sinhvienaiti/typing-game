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
  const body = el("div", "stx-grid");
  const listPanel = panel("Canonical Fleet", "11 child-owned ship IDs · IDs and asset IDs are immutable");
  const listHost = el("div");
  listPanel.append(listHost);
  const editorPanel = panel("Ship Override", "Only authored differences are persisted in `content.ships.ships.<id>`");
  const editorHost = el("div");
  editorPanel.append(editorHost);
  body.append(listPanel, editorPanel);
  page.append(status, body);

  let loadedActiveRevision: string | null = null;
  let bundled: ShipAdminPreview | null = null;
  let activePreview: ShipAdminPreview | null = null;
  let selectedId: ShipId = "vanguard";
  let policy: ShipAdminPolicy = { configRevision: "ships-admin-v1", ships: {} };

  const setStatus = (text: string, tone: Tone = "info"): void => {
    status.className = `stx-notice ${tone}`;
    status.textContent = text;
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
    if (!base) return activePreview?.ships.find((ship) => ship.id === id);
    return mergeShip(base, policy.ships?.[id]);
  };

  const renderList = (): void => {
    listHost.replaceChildren();
    const ships = bundled?.ships ?? activePreview?.ships ?? [];
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
      }, selectedId === ship.id ? "st-admin-btn primary" : "st-admin-btn");
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
    if (!ship) {
      editorHost.append(notice("Ship registry has not finished loading.", "warn"));
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

    const visual = panel("Visual Profile", "Procedural/profile fallback fields consumed by the child renderer; asset identity stays derived from ship ID.");
    const silhouette = field("Silhouette", ship.visual.silhouette, SILHOUETTES);
    silhouette.control.addEventListener("change", () => {
      const override = overrideFor(selectedId);
      override.visual ??= {};
      override.visual.silhouette = silhouette.control.value as ShipVisualProfile["silhouette"];
    });
    const visualFields: HTMLElement[] = [silhouette.root];
    for (const key of COLOR_KEYS) {
      const item = field(key, ship.visual[key]);
      item.control.addEventListener("input", () => {
        const override = overrideFor(selectedId);
        override.visual ??= {};
        override.visual[key] = item.control.value;
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
      });
      visualFields.push(item.root);
    }
    const engines = field("engineCount", String(ship.visual.engineCount), ["1", "2", "3"]);
    engines.control.addEventListener("change", () => {
      const override = overrideFor(selectedId);
      override.visual ??= {};
      override.visual.engineCount = Number(engines.control.value) as 1 | 2 | 3;
    });
    visualFields.push(engines.root);
    for (let index = 0; index < visualFields.length; index += 3) visual.append(grid(...visualFields.slice(index, index + 3)));

    const actions = el("div", "st-admin-page-actions");
    actions.append(
      button("Reset Ship Override", () => {
        if (policy.ships) delete policy.ships[selectedId];
        renderList();
        renderEditor();
        setStatus(`${selectedId} reset to bundled child runtime values. Save Draft to persist this removal.`, "good");
      }),
      button("Validate Preview", () => {
        void api.previewShips({ policy }).then((preview) => {
          activePreview = preview;
          renderList();
          renderEditor();
          setStatus(`Child canonical preview accepted ${preview.ships.length} ships for ${preview.configRevision}.`, "good");
        }).catch((error: unknown) => setStatus(`Preview rejected: ${error instanceof Error ? error.message : String(error)}`, "bad"));
      }, "st-admin-btn primary"),
    );
    editorHost.append(metadata, stats, visual, actions);
  };

  void Promise.all([api.getState(), api.previewShips()]).then(async ([statePayload, bundledPreview]) => {
    loadedActiveRevision = statePayload.state.activeRevision;
    revisionBadge.textContent = `ACTIVE · ${statePayload.state.activeRevision}`;
    bundled = bundledPreview;
    policy = policyFrom(statePayload.active.config);
    activePreview = await api.previewShips({ policy });
    selectedId = activePreview.ships[0]?.id ?? "vanguard";
    renderList();
    renderEditor();
    setStatus(
      statePayload.active.config.content?.ships
        ? `Loaded active Ships policy ${policy.configRevision}. Save Draft is isolated until History / Publish.`
        : "Active revision predates B06.1 Ships policy; bundled child registry is shown until the first draft is saved.",
      statePayload.active.config.content?.ships ? "good" : "warn",
    );
  }).catch((error: unknown) => setStatus(`Ships Admin unavailable: ${error instanceof Error ? error.message : String(error)}`, "bad"));

  const saveBar = el("div", "st-admin-sticky-save stx-savebar");
  const saveStatus = el("span", undefined, "Revision-backed · no direct runtime mutation");
  const save = button("Save Draft", () => {
    void (async () => {
      save.disabled = true;
      saveStatus.textContent = "Validating against child runtime…";
      try {
        const payload = await api.getState();
        if (loadedActiveRevision === null || loadedActiveRevision !== payload.state.activeRevision) {
          throw new Error(`Active revision changed from ${loadedActiveRevision ?? "not-loaded"} to ${payload.state.activeRevision}. Reload this screen before saving to avoid overwriting newer published changes.`);
        }
        const validated = await api.previewShips({ policy });
        const config = cloneConfig(payload.active.config);
        config.content = { ...(config.content ?? {}), ships: structuredClone(policy) };
        const revision = await api.createRevision({
          baseRevision: payload.active.revision,
          config,
          message: "Admin Phase B · B06.1 Ships registry draft",
        });
        activePreview = validated;
        saveStatus.textContent = `Draft saved · ${revision.revision} · runtime unchanged`;
        setStatus(`Draft ${revision.revision} passed child preview + server validation. Publish from History to make it the active Admin policy; gameplay apply boundary is a new session.`, "good");
      } catch (error: unknown) {
        const message = error instanceof Error ? error.message : String(error);
        saveStatus.textContent = `Draft rejected · ${message}`;
        setStatus(`Validation/save failed: ${message}`, "bad");
      } finally {
        save.disabled = false;
      }
    })();
  }, "st-admin-btn primary");
  saveBar.append(el("strong", undefined, "B06.1 Ships Draft"), saveStatus, el("div", "grow"), button("Discard", () => navigate(location.pathname)), save);
  page.append(saveBar);
  return page;
}
