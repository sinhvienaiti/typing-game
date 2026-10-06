import {
  SpaceTypingAdminApi,
  type CoreStatKey,
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
const EQUIPMENT_SLOTS = ["weapon", "armor", "shield", "reactor", "utility", "drone", "core"] as const;

type EquipmentSlot = (typeof EQUIPMENT_SLOTS)[number];
type EquipmentTier = 1 | 2 | 3;
type EquipmentAdminOverride = {
  name?: string;
  description?: string;
  stats?: Partial<Record<CoreStatKey, number>>;
  perk?: string | null;
};
type EquipmentAdminPolicy = {
  configRevision: string;
  equipment?: Record<string, EquipmentAdminOverride>;
};
type EquipmentAdminPreviewItem = {
  id: string;
  name: string;
  slot: EquipmentSlot;
  tier: EquipmentTier;
  icon: string;
  description: string;
  stats: Partial<Record<CoreStatKey, number>>;
  perk?: string;
  overridden: boolean;
};
type EquipmentAdminPreview = {
  protocolVersion: 1;
  configRevision: string;
  equipment: EquipmentAdminPreviewItem[];
};
type EquipmentAwareConfig = SpaceTypingAdminConfig & {
  content?: NonNullable<SpaceTypingAdminConfig["content"]> & {
    equipment?: EquipmentAdminPolicy;
  };
};
type Navigate = (path: string) => void;
type Tone = "good" | "warn" | "bad" | "info";

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

function grid(...children: HTMLElement[]): HTMLElement {
  const root = el("div", "stx-grid");
  root.append(...children);
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

function descriptionField(value: string): { root: HTMLElement; control: HTMLTextAreaElement } {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, "Description"));
  const control = el("textarea") as HTMLTextAreaElement;
  control.value = value;
  control.maxLength = 320;
  control.rows = 4;
  control.setAttribute("aria-label", "Description");
  root.append(control);
  return { root, control };
}

function cloneConfig(config: SpaceTypingAdminConfig): EquipmentAwareConfig {
  return structuredClone(config) as EquipmentAwareConfig;
}

function policyFrom(config: SpaceTypingAdminConfig): EquipmentAdminPolicy {
  const content = (config as EquipmentAwareConfig).content;
  return structuredClone(content?.equipment ?? { configRevision: "equipment-admin-v1", equipment: {} });
}

function mergeEquipment(base: EquipmentAdminPreviewItem, override?: EquipmentAdminOverride): EquipmentAdminPreviewItem {
  const merged: EquipmentAdminPreviewItem = {
    ...base,
    ...(override ?? {}),
    id: base.id,
    slot: base.slot,
    tier: base.tier,
    icon: base.icon,
    stats: { ...base.stats, ...(override?.stats ?? {}) },
    overridden: override !== undefined && Object.keys(override).length > 0,
  };
  if (override?.perk === null) delete merged.perk;
  return merged;
}

async function previewEquipment(policy?: EquipmentAdminPolicy): Promise<EquipmentAdminPreview> {
  const response = await fetch("/api/admin/space-typing/equipment/preview", {
    method: "POST",
    cache: "no-store",
    headers: {
      "content-type": "application/json",
      "x-typing-game-admin-token": api.getToken(),
    },
    body: JSON.stringify(policy === undefined ? {} : { policy }),
  });
  const payload = (await response.json().catch(() => ({}))) as Record<string, unknown>;
  if (!response.ok) {
    const message = typeof payload["message"] === "string"
      ? payload["message"]
      : typeof payload["error"] === "string"
        ? payload["error"]
        : `Equipment preview failed (${response.status})`;
    throw new Error(message);
  }
  return payload as unknown as EquipmentAdminPreview;
}

function statsSummary(base: EquipmentAdminPreviewItem, effective: EquipmentAdminPreviewItem): HTMLElement {
  const root = panel("Stat Diff Preview", "Bundled child value → effective draft value");
  const rows = el("div");
  let changes = 0;
  for (const key of CORE_STATS) {
    const before = base.stats[key] ?? 0;
    const after = effective.stats[key] ?? 0;
    if (before === 0 && after === 0) continue;
    const row = el("div", "stx-toggle-row");
    const copy = el("div");
    copy.append(el("strong", undefined, key), el("small", undefined, `${before} → ${after}`));
    const delta = after - before;
    if (delta !== 0) {
      changes += 1;
      row.append(copy, badge(`${delta > 0 ? "+" : ""}${delta}`, delta > 0 ? "good" : "warn"));
    } else {
      row.append(copy, badge("UNCHANGED", "info"));
    }
    rows.append(row);
  }
  root.append(rows, notice(changes === 0 ? "No stat differences from the bundled registry." : `${changes} stat field(s) differ from the bundled registry.`, changes === 0 ? "info" : "warn"));
  return root;
}

export function renderPhaseBEquipment(navigate: Navigate): HTMLElement {
  const page = el("div");
  const revisionBadge = badge("ACTIVE · loading", "info");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Game Content · Canonical Equipment Registry · B06.2"),
    el("h1", undefined, "Equipment"),
    el("p", undefined, "Edit the child-owned Equipment registry through revision-backed overrides. IDs, slots, tiers and icons stay immutable; the current canonical contract authorizes name, description, core stat bonuses and perk only."),
  );
  header.append(copy, revisionBadge);
  page.append(header);

  const status = notice("Loading active revision and canonical child Equipment registry…", "info");
  const filterBar = el("div", "st-admin-filterbar");
  const search = el("input", "st-admin-search") as HTMLInputElement;
  search.placeholder = "Search equipment…";
  search.setAttribute("aria-label", "Search Equipment");
  const slotFilter = el("select", "st-admin-select") as HTMLSelectElement;
  slotFilter.setAttribute("aria-label", "Equipment slot filter");
  slotFilter.append(new Option("All slots", "all"));
  for (const slot of EQUIPMENT_SLOTS) slotFilter.append(new Option(slot, slot));
  filterBar.append(search, slotFilter, el("div", "st-admin-filter-spacer"), badge("APPLY · NEW SESSION", "info"));

  const body = el("div", "stx-grid");
  const listPanel = panel("Canonical Equipment", "Child registry · immutable ID / slot / tier / icon");
  const listHost = el("div");
  listPanel.append(listHost);
  const editorPanel = panel("Equipment Override", "Only authored differences are persisted in `content.equipment.equipment.<id>`");
  const editorHost = el("div");
  editorPanel.append(editorHost);
  body.append(listPanel, editorPanel);
  page.append(status, filterBar, body);

  let loadedActiveRevision: string | null = null;
  let bundled: EquipmentAdminPreview | null = null;
  let activePreview: EquipmentAdminPreview | null = null;
  let selectedId = "";
  let policy: EquipmentAdminPolicy = { configRevision: "equipment-admin-v1", equipment: {} };

  const setStatus = (text: string, tone: Tone = "info"): void => {
    status.className = `stx-notice ${tone}`;
    status.textContent = text;
  };

  const overrideFor = (id: string): EquipmentAdminOverride => {
    policy.equipment ??= {};
    policy.equipment[id] ??= {};
    return policy.equipment[id];
  };

  const baseEquipment = (id: string): EquipmentAdminPreviewItem | undefined =>
    bundled?.equipment.find((item) => item.id === id);

  const effectiveEquipment = (id: string): EquipmentAdminPreviewItem | undefined => {
    const base = baseEquipment(id);
    if (!base) return activePreview?.equipment.find((item) => item.id === id);
    return mergeEquipment(base, policy.equipment?.[id]);
  };

  const renderList = (): void => {
    listHost.replaceChildren();
    const query = search.value.trim().toLowerCase();
    const slot = slotFilter.value;
    const items = (bundled?.equipment ?? activePreview?.equipment ?? []).filter((item) => {
      const matchesSlot = slot === "all" || item.slot === slot;
      const matchesQuery = query.length === 0 || `${item.id} ${item.name} ${item.slot} ${item.perk ?? ""}`.toLowerCase().includes(query);
      return matchesSlot && matchesQuery;
    });
    if (items.length === 0) {
      listHost.append(notice("No Equipment records match the current filters.", "warn"));
      return;
    }
    for (const item of items) {
      const current = effectiveEquipment(item.id) ?? item;
      const row = el("div", "stx-toggle-row");
      const copyNode = el("div");
      copyNode.append(
        el("strong", undefined, `${current.icon} ${current.name}`),
        el("small", undefined, `${item.id} · ${item.slot} · Mk.${item.tier}${current.perk ? ` · ${current.perk}` : ""}`),
      );
      const actions = el("div");
      if (policy.equipment?.[item.id] && Object.keys(policy.equipment[item.id]).length > 0) actions.append(badge("OVERRIDE", "warn"));
      actions.append(button(selectedId === item.id ? "Editing" : "Edit", () => {
        selectedId = item.id;
        renderList();
        renderEditor();
      }, selectedId === item.id ? "st-admin-btn primary" : "st-admin-btn"));
      row.append(copyNode, actions);
      listHost.append(row);
    }
  };

  const renderEditor = (): void => {
    editorHost.replaceChildren();
    const base = baseEquipment(selectedId);
    const item = effectiveEquipment(selectedId);
    if (!base || !item) {
      editorHost.append(notice("Equipment registry has not finished loading.", "warn"));
      return;
    }

    editorHost.append(notice(`ID ${item.id} · slot ${item.slot} · Mk.${item.tier} · icon ${item.icon} · apply boundary: new session`, "info"));
    editorHost.append(notice("The master UI plan contains future acquisition/rarity/upgrade fields. B06.2 intentionally does not persist those until the child runtime exposes a canonical contract for them.", "warn"));

    const identity = panel("Identity", "Name and description are authorable; ID / slot / tier / icon remain child-owned.");
    const name = field("Name", item.name);
    (name.control as HTMLInputElement).maxLength = 100;
    name.control.addEventListener("input", () => {
      overrideFor(selectedId).name = name.control.value;
      renderList();
    });
    const description = descriptionField(item.description);
    description.control.addEventListener("input", () => {
      overrideFor(selectedId).description = description.control.value;
    });
    identity.append(grid(name.root, field("Slot (immutable)", item.slot, EQUIPMENT_SLOTS).root, field("Tier (immutable)", String(item.tier), ["1", "2", "3"]).root), description.root);
    for (const control of identity.querySelectorAll<HTMLInputElement | HTMLSelectElement>("select")) control.disabled = true;

    const stats = panel("Core Stat Bonuses", "Canonical child stat keys · allowed range -100..100");
    const statFields: HTMLElement[] = [];
    for (const key of CORE_STATS) {
      const entry = field(key, String(item.stats[key] ?? 0), undefined, "number");
      const input = entry.control as HTMLInputElement;
      input.min = "-100";
      input.max = "100";
      input.step = "0.1";
      input.addEventListener("input", () => {
        const override = overrideFor(selectedId);
        override.stats ??= {};
        override.stats[key] = Number(input.value);
      });
      statFields.push(entry.root);
    }
    for (let index = 0; index < statFields.length; index += 3) stats.append(grid(...statFields.slice(index, index + 3)));

    const perkIds = Array.from(new Set((bundled?.equipment ?? []).map((candidate) => candidate.perk).filter((value): value is string => typeof value === "string"))).sort();
    const perk = field("Perk", item.perk ?? "__none__", ["__none__", ...perkIds]);
    perk.control.addEventListener("change", () => {
      overrideFor(selectedId).perk = perk.control.value === "__none__" ? null : perk.control.value;
      renderList();
    });
    const perkPanel = panel("Perk", "Mk.II / Mk.III behavior hook from the canonical child perk registry.");
    perkPanel.append(perk.root, notice(item.perk ? `Effective perk: ${item.perk}` : "No effective perk.", item.perk ? "good" : "info"));

    const actions = el("div", "st-admin-page-actions");
    actions.append(
      button("Reset Equipment Override", () => {
        if (policy.equipment) delete policy.equipment[selectedId];
        renderList();
        renderEditor();
        setStatus(`${selectedId} reset to bundled child values. Save Draft to persist this removal.`, "good");
      }),
      button("Validate Preview", () => {
        void previewEquipment(policy).then((preview) => {
          activePreview = preview;
          renderList();
          renderEditor();
          setStatus(`Child canonical preview accepted ${preview.equipment.length} Equipment records for ${preview.configRevision}.`, "good");
        }).catch((error: unknown) => setStatus(`Preview rejected: ${error instanceof Error ? error.message : String(error)}`, "bad"));
      }, "st-admin-btn primary"),
    );

    editorHost.append(identity, stats, perkPanel, statsSummary(base, item), actions);
  };

  search.addEventListener("input", renderList);
  slotFilter.addEventListener("change", renderList);

  void Promise.all([api.getState(), previewEquipment()]).then(async ([statePayload, bundledPreview]) => {
    loadedActiveRevision = statePayload.state.activeRevision;
    revisionBadge.textContent = `ACTIVE · ${statePayload.state.activeRevision}`;
    bundled = bundledPreview;
    policy = policyFrom(statePayload.active.config);
    activePreview = await previewEquipment(policy);
    selectedId = activePreview.equipment[0]?.id ?? "";
    renderList();
    renderEditor();
    const hasPolicy = (statePayload.active.config as EquipmentAwareConfig).content?.equipment !== undefined;
    setStatus(
      hasPolicy
        ? `Loaded active Equipment policy ${policy.configRevision}. Save Draft is isolated until History / Publish.`
        : "Active revision predates B06.2 Equipment policy; bundled child registry is shown until the first draft is saved.",
      hasPolicy ? "good" : "warn",
    );
  }).catch((error: unknown) => setStatus(`Equipment Admin unavailable: ${error instanceof Error ? error.message : String(error)}`, "bad"));

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
        const validated = await previewEquipment(policy);
        const config = cloneConfig(payload.active.config);
        config.content = { ...(config.content ?? {}), equipment: structuredClone(policy) };
        const revision = await api.createRevision({
          baseRevision: payload.active.revision,
          config,
          message: "Admin Phase B · B06.2 Equipment registry draft",
        });
        activePreview = validated;
        saveStatus.textContent = `Draft saved · ${revision.revision} · runtime unchanged`;
        setStatus(`Draft ${revision.revision} passed child preview + server validation. Publish from History to activate it; gameplay reads the published policy only when a new session starts.`, "good");
      } catch (error: unknown) {
        const message = error instanceof Error ? error.message : String(error);
        saveStatus.textContent = `Draft rejected · ${message}`;
        setStatus(`Validation/save failed: ${message}`, "bad");
      } finally {
        save.disabled = false;
      }
    })();
  }, "st-admin-btn primary");
  saveBar.append(
    el("strong", undefined, "B06.2 Equipment Draft"),
    saveStatus,
    el("div", "grow"),
    button("Discard", () => navigate(location.pathname)),
    save,
  );
  page.append(saveBar);
  return page;
}
