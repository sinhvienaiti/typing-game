import { SpaceTypingAdminApi, type SpaceTypingAdminConfig } from "./api";

const api = new SpaceTypingAdminApi();

type BossAdminOverride = {
  name?: string;
  title?: string;
};
type BossAdminPolicy = {
  configRevision: string;
  bosses?: Record<string, BossAdminOverride>;
};
type BossAdminPreviewItem = {
  id: string;
  name: string;
  title: string;
  role: string;
  rank: string;
  family: string;
  overridden: boolean;
};
type BossAdminPreview = {
  protocolVersion: 1;
  configRevision: string;
  authorableFields: ["name", "title"];
  bosses: BossAdminPreviewItem[];
};
type BossAwareConfig = SpaceTypingAdminConfig & {
  content?: NonNullable<SpaceTypingAdminConfig["content"]> & {
    bosses?: BossAdminPolicy;
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

function field(label: string, value: string, maxLength?: number): { root: HTMLElement; control: HTMLInputElement } {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label));
  const control = el("input") as HTMLInputElement;
  control.type = "text";
  control.value = value;
  if (maxLength !== undefined) control.maxLength = maxLength;
  control.setAttribute("aria-label", label);
  root.append(control);
  return { root, control };
}

function readonlyField(label: string, value: string): HTMLElement {
  const entry = field(label, value);
  entry.control.disabled = true;
  return entry.root;
}

function policyFrom(config: SpaceTypingAdminConfig): BossAdminPolicy {
  const content = (config as BossAwareConfig).content;
  return structuredClone(content?.bosses ?? { configRevision: "bosses-admin-v1", bosses: {} });
}

function mergeBoss(base: BossAdminPreviewItem, override?: BossAdminOverride): BossAdminPreviewItem {
  return {
    ...base,
    name: override?.name ?? base.name,
    title: override?.title ?? base.title,
    overridden: override !== undefined && Object.keys(override).length > 0,
  };
}

async function previewBosses(policy?: BossAdminPolicy): Promise<BossAdminPreview> {
  const response = await fetch("/api/admin/space-typing/bosses/preview", {
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
        : `Bosses preview failed (${response.status})`;
    throw new Error(message);
  }
  return payload as unknown as BossAdminPreview;
}

function diffPanel(base: BossAdminPreviewItem, effective: BossAdminPreviewItem): HTMLElement {
  const root = panel("Runtime Diff Preview", "Bundled canonical identity → effective draft identity");
  for (const [label, before, after] of [
    ["Name", base.name, effective.name],
    ["Title", base.title, effective.title],
  ] as const) {
    const row = el("div", "stx-toggle-row");
    const copy = el("div");
    copy.append(el("strong", undefined, label), el("small", undefined, `${before} → ${after}`));
    const changed = before !== after;
    row.append(copy, badge(changed ? "CHANGED" : "UNCHANGED", changed ? "warn" : "info"));
    root.append(row);
  }
  root.append(notice(
    "Published Boss identity changes are snapshotted at the new-session boundary. Draft and preview never mutate the current gameplay session.",
    "info",
  ));
  return root;
}

export function renderPhaseBBosses(navigate: Navigate): HTMLElement {
  const page = el("div");
  const revisionBadge = badge("ACTIVE · loading", "info");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Game Content · Canonical Boss Registry · B06.5"),
    el("h1", undefined, "Bosses"),
    el("p", undefined, "Revision-backed Boss identity authoring. Only canonical name/title overrides are writable in B06.5; combat stats, phases, rewards, visuals and audio remain child-runtime owned until they have explicit canonical consumers."),
  );
  header.append(copy, revisionBadge);
  page.append(header);

  const status = notice("Loading active revision and canonical child Boss registry…", "info");
  const filterBar = el("div", "st-admin-filterbar");
  const search = el("input", "st-admin-search") as HTMLInputElement;
  search.placeholder = "Search bosses…";
  search.setAttribute("aria-label", "Search Bosses");
  const familyFilter = el("select", "st-admin-select") as HTMLSelectElement;
  familyFilter.setAttribute("aria-label", "Boss family filter");
  const roleFilter = el("select", "st-admin-select") as HTMLSelectElement;
  roleFilter.setAttribute("aria-label", "Boss role filter");
  filterBar.append(search, familyFilter, roleFilter, el("div", "st-admin-filter-spacer"), badge("APPLY · NEW SESSION", "info"));

  const body = el("div", "stx-grid");
  const listPanel = panel("Canonical Bosses", "26 child-owned Boss identities · name/title are the only B06.5 authorable fields");
  const listHost = el("div");
  listPanel.append(listHost);
  const editorPanel = panel("Boss Identity Override", "Persists only `content.bosses.bosses.<id>.name/title`");
  const editorHost = el("div");
  editorPanel.append(editorHost);
  body.append(listPanel, editorPanel);
  page.append(status, filterBar, body);

  let loadedActiveRevision: string | null = null;
  let bundled: BossAdminPreview | null = null;
  let activePreview: BossAdminPreview | null = null;
  let selectedId = "";
  let policy: BossAdminPolicy = { configRevision: "bosses-admin-v1", bosses: {} };

  const setStatus = (text: string, tone: Tone = "info"): void => {
    status.className = `stx-notice ${tone}`;
    status.textContent = text;
  };

  const baseBoss = (id: string): BossAdminPreviewItem | undefined => bundled?.bosses.find((boss) => boss.id === id);
  const effectiveBoss = (id: string): BossAdminPreviewItem | undefined => {
    const base = baseBoss(id);
    if (!base) return activePreview?.bosses.find((boss) => boss.id === id);
    return mergeBoss(base, policy.bosses?.[id]);
  };

  const rebuildFilters = (): void => {
    const selectedFamily = familyFilter.value || "all";
    const selectedRole = roleFilter.value || "all";
    const source = bundled?.bosses ?? activePreview?.bosses ?? [];
    familyFilter.replaceChildren(new Option("All families", "all"));
    roleFilter.replaceChildren(new Option("All roles", "all"));
    for (const family of Array.from(new Set(source.map((boss) => boss.family))).sort()) familyFilter.append(new Option(family, family));
    for (const role of Array.from(new Set(source.map((boss) => boss.role))).sort()) roleFilter.append(new Option(role, role));
    familyFilter.value = Array.from(familyFilter.options).some((option) => option.value === selectedFamily) ? selectedFamily : "all";
    roleFilter.value = Array.from(roleFilter.options).some((option) => option.value === selectedRole) ? selectedRole : "all";
  };

  const renderList = (): void => {
    listHost.replaceChildren();
    const query = search.value.trim().toLowerCase();
    const family = familyFilter.value || "all";
    const role = roleFilter.value || "all";
    const bosses = (bundled?.bosses ?? activePreview?.bosses ?? []).filter((boss) => {
      const familyMatch = family === "all" || boss.family === family;
      const roleMatch = role === "all" || boss.role === role;
      const queryMatch = query.length === 0 || `${boss.id} ${boss.name} ${boss.title} ${boss.family} ${boss.role} ${boss.rank}`.toLowerCase().includes(query);
      return familyMatch && roleMatch && queryMatch;
    });
    if (bosses.length === 0) {
      listHost.append(notice("No Boss definitions match the current filters.", "warn"));
      return;
    }
    for (const boss of bosses) {
      const current = effectiveBoss(boss.id) ?? boss;
      const row = el("div", "stx-toggle-row");
      const copyNode = el("div");
      copyNode.append(
        el("strong", undefined, current.name),
        el("small", undefined, `${boss.id} · ${current.title} · ${boss.family} · ${boss.role} · ${boss.rank}`),
      );
      const actions = el("div");
      if (policy.bosses?.[boss.id] && Object.keys(policy.bosses[boss.id]).length > 0) actions.append(badge("OVERRIDE", "warn"));
      actions.append(button(selectedId === boss.id ? "Editing" : "Edit", () => {
        selectedId = boss.id;
        renderList();
        renderEditor();
      }, selectedId === boss.id ? "st-admin-btn primary" : "st-admin-btn"));
      row.append(copyNode, actions);
      listHost.append(row);
    }
  };

  const updateOverride = (id: string, base: BossAdminPreviewItem, name: string, title: string): void => {
    const normalizedName = name.trim();
    const normalizedTitle = title.trim();
    const next: BossAdminOverride = {};
    if (normalizedName !== base.name) next.name = normalizedName;
    if (normalizedTitle !== base.title) next.title = normalizedTitle;
    policy.bosses ??= {};
    if (Object.keys(next).length === 0) delete policy.bosses[id];
    else policy.bosses[id] = next;
  };

  const renderEditor = (): void => {
    editorHost.replaceChildren();
    const base = baseBoss(selectedId);
    const boss = effectiveBoss(selectedId);
    if (!base || !boss) {
      editorHost.append(notice("Boss registry has not finished loading.", "warn"));
      return;
    }

    editorHost.append(notice(`ID ${boss.id} · ${boss.family}/${boss.role}/${boss.rank} · apply boundary: new session`, "info"));
    editorHost.append(notice(
      "HP, Shield, Armor, Damage, Speed, phase thresholds, skills, projectiles, VFX, SFX and rewards are intentionally read-only/not persisted. The current child contract exposes only canonical `name` and `title` consumers.",
      "warn",
    ));

    const identity = panel("Canonical Identity", "Only Name and Title are authorable in B06.5");
    const name = field("Name", boss.name, 100);
    const title = field("Title", boss.title, 160);
    const immutable = grid(
      readonlyField("Family", boss.family),
      readonlyField("Role", boss.role),
      readonlyField("Rank", boss.rank),
    );
    const onInput = (): void => {
      updateOverride(selectedId, base, name.control.value, title.control.value);
      renderList();
    };
    name.control.addEventListener("input", onInput);
    title.control.addEventListener("input", onInput);
    identity.append(grid(name.root, title.root), immutable, notice("Server constraints: Name ≤ 100 characters, Title ≤ 160 characters; blank values are rejected.", "info"));

    const actions = el("div", "st-admin-page-actions");
    actions.append(
      button("Reset Boss Override", () => {
        if (policy.bosses) delete policy.bosses[selectedId];
        renderList();
        renderEditor();
        setStatus(`${selectedId} reset to bundled child identity. Save Draft to persist this removal.`, "good");
      }),
      button("Validate Preview", () => {
        void previewBosses(policy).then((preview) => {
          activePreview = preview;
          renderList();
          renderEditor();
          setStatus(`Child canonical preview accepted ${preview.bosses.length} Boss definitions for ${preview.configRevision}.`, "good");
        }).catch((error: unknown) => setStatus(`Preview rejected: ${error instanceof Error ? error.message : String(error)}`, "bad"));
      }, "st-admin-btn primary"),
    );

    editorHost.append(identity, diffPanel(base, boss), actions);
  };

  search.addEventListener("input", renderList);
  familyFilter.addEventListener("change", renderList);
  roleFilter.addEventListener("change", renderList);

  void Promise.all([api.getState(), previewBosses()]).then(async ([statePayload, bundledPreview]) => {
    loadedActiveRevision = statePayload.state.activeRevision;
    revisionBadge.textContent = `ACTIVE · ${statePayload.state.activeRevision}`;
    bundled = bundledPreview;
    policy = policyFrom(statePayload.active.config);
    activePreview = await previewBosses(policy);
    selectedId = activePreview.bosses[0]?.id ?? "";
    rebuildFilters();
    renderList();
    renderEditor();
    const hasPolicy = (statePayload.active.config as BossAwareConfig).content?.bosses !== undefined;
    setStatus(
      hasPolicy
        ? `Loaded active Boss identity policy ${policy.configRevision}. Save Draft is isolated until History / Publish.`
        : "Active revision predates B06.5 Boss policy; bundled child identities are shown until the first draft is saved.",
      hasPolicy ? "good" : "warn",
    );
  }).catch((error: unknown) => setStatus(`Bosses Admin unavailable: ${error instanceof Error ? error.message : String(error)}`, "bad"));

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
        const validated = await previewBosses(policy);
        const config = structuredClone(payload.active.config) as BossAwareConfig;
        config.content = { ...(config.content ?? {}), bosses: structuredClone(policy) };
        const revision = await api.createRevision({
          baseRevision: payload.active.revision,
          config,
          message: "Admin Phase B · B06.5 Boss identity draft",
        });
        activePreview = validated;
        saveStatus.textContent = `Draft saved · ${revision.revision} · runtime unchanged`;
        setStatus(`Draft ${revision.revision} passed child preview + server validation. Publish from History to activate it; gameplay snapshots Boss identity only when a new session starts.`, "good");
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
    el("strong", undefined, "B06.5 Boss Draft"),
    saveStatus,
    el("div", "grow"),
    button("Discard", () => navigate(location.pathname)),
    save,
  );
  page.append(saveBar);
  return page;
}
