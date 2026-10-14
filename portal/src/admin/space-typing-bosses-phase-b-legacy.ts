import { SpaceTypingAdminApi, type SpaceTypingAdminConfig } from "./api";
import { adminErrorMessage } from "./admin-http";
import { createAssetTuningCapabilityState } from "./v2/asset-tuning-studio";

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

function field(label: string, value: string): { root: HTMLElement; control: HTMLInputElement } {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label));
  const control = el("input") as HTMLInputElement;
  control.type = "text";
  control.value = value;
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
  const payload = await api.requestJson<BossAdminPreview>("/api/admin/space-typing/bosses/preview", {
    method: "POST",
    body: JSON.stringify(policy === undefined ? {} : { policy }),
  });
  if (payload.protocolVersion !== 1 || !Array.isArray(payload.bosses)) {
    throw new Error("Bosses preview response does not match the canonical Admin contract.");
  }
  return payload;
}

function diffPanel(base: BossAdminPreviewItem, effective: BossAdminPreviewItem): HTMLElement {
  const root = panel("Registry Preview Diff", "Bundled Boss identity → persisted Admin preview candidate");
  for (const [label, before, after] of [
    ["Name", base.name, effective.name],
    ["Title", base.title, effective.title],
  ] as const) {
    const row = el("div", "stx-toggle-row");
    const copy = el("div");
    copy.append(el("strong", undefined, label), el("small", undefined, `${before} → ${after}`));
    const changed = before !== after;
    row.append(copy, badge(changed ? "MIGRATION DATA" : "UNCHANGED", changed ? "warn" : "info"));
    root.append(row);
  }
  root.append(notice(
    "Preview-only migration data. Production bossIdentityForStage() still resolves bundled identities and does not consume these Admin overrides.",
    "warn",
  ));
  return root;
}

export function renderPhaseBBosses(_navigate: Navigate): HTMLElement {
  const page = el("div");
  const revisionBadge = badge("ACTIVE · loading", "info");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Game Content · Canonical Boss Registry · B06.5 · A7"),
    el("h1", undefined, "Bosses"),
    el("p", undefined, "Inspect canonical Boss identity, stage usage and combat ownership. Existing name/title overrides remain preserved migration data, but A7 closes Boss authoring until a production identity consumer is wired."),
  );
  header.append(copy, revisionBadge);
  page.append(header);

  const status = notice("Loading active revision and canonical child Boss registry…", "info");
  status.setAttribute("aria-live", "polite");
  const filterBar = el("div", "st-admin-filterbar");
  const search = el("input", "st-admin-search") as HTMLInputElement;
  search.placeholder = "Search bosses…";
  search.setAttribute("aria-label", "Search Bosses");
  const familyFilter = el("select", "st-admin-select") as HTMLSelectElement;
  familyFilter.setAttribute("aria-label", "Boss family filter");
  const roleFilter = el("select", "st-admin-select") as HTMLSelectElement;
  roleFilter.setAttribute("aria-label", "Boss role filter");
  filterBar.append(search, familyFilter, roleFilter, el("div", "st-admin-filter-spacer"), badge("PREVIEW · NO RUNTIME APPLY", "warn"));

  const body = el("div", "stx-grid");
  const listPanel = panel("Canonical Bosses", "26 child-owned Boss identities · bundled production authority");
  const listHost = el("div");
  listPanel.append(listHost);
  const editorPanel = panel("Boss Registry & Capabilities", "A7 fail-closed: no Boss write field has a proven production consumer yet");
  const editorHost = el("div");
  editorPanel.append(editorHost);
  body.append(listPanel, editorPanel);
  page.append(status, filterBar, body);

  let bundled: BossAdminPreview | null = null;
  let activePreview: BossAdminPreview | null = null;
  let selectedId = "";
  let policy: BossAdminPolicy = { configRevision: "bosses-admin-v1", bosses: {} };
  let serviceReady = false;
  let loadGeneration = 0;

  search.disabled = true;
  familyFilter.disabled = true;
  roleFilter.disabled = true;

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
    const allBosses = bundled?.bosses ?? activePreview?.bosses ?? [];
    if (!serviceReady || allBosses.length === 0) {
      listHost.append(notice(serviceReady ? "No canonical Boss definitions were returned by the preview." : "Load the canonical Boss registry to browse and filter identities.", serviceReady ? "warn" : "info"));
      return;
    }
    const query = search.value.trim().toLowerCase();
    const family = familyFilter.value || "all";
    const role = roleFilter.value || "all";
    const bosses = allBosses.filter((boss) => {
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
      if (policy.bosses?.[boss.id] && Object.keys(policy.bosses[boss.id]).length > 0) actions.append(badge("MIGRATION DATA", "warn"));
      const view = button(selectedId === boss.id ? "Viewing" : "View", () => {
        selectedId = boss.id;
        renderList();
        renderEditor();
      }, selectedId === boss.id ? "st-admin-btn primary" : "st-admin-btn");
      view.disabled = !serviceReady;
      actions.append(view);
      row.append(copyNode, actions);
      listHost.append(row);
    }
  };

  const renderEditor = (): void => {
    editorHost.replaceChildren();
    const base = baseBoss(selectedId);
    const boss = effectiveBoss(selectedId);
    if (!serviceReady || !base || !boss) {
      editorHost.append(notice(serviceReady ? "No Boss is selected." : "Load the active revision and canonical Boss preview before inspecting capabilities.", serviceReady ? "warn" : "info"));
      return;
    }

    editorHost.append(notice(`ID ${boss.id} · ${boss.family}/${boss.role}/${boss.rank} · production Admin write boundary: none`, "info"));

    const capabilities = panel("Capabilities", "A7 authority is based on production consumers, not preview availability.");
    capabilities.append(
      createAssetTuningCapabilityState({
        label: "Name / Title",
        status: "REQUIRES CANONICAL MIGRATION",
        description: "Existing overrides are preserved and previewable, but production bossIdentityForStage() does not consume them yet.",
      }),
      createAssetTuningCapabilityState({
        label: "Identity / Stage Usage",
        status: "READ-ONLY REFERENCE",
        description: "ID, role, rank, family and stage selection are bundled Boss/campaign authority.",
      }),
      createAssetTuningCapabilityState({
        label: "Phases / Mechanics",
        status: "READ-ONLY REFERENCE",
        description: "Phase thresholds, projectile patterns, typing mechanics and skills remain production code authority.",
      }),
      createAssetTuningCapabilityState({
        label: "Media / VFX / SFX",
        status: "REQUIRES CANONICAL MIGRATION",
        description: "No immutable Media V2 Boss art/GLB/VFX/SFX binding is owned by the current Admin policy.",
      }),
      createAssetTuningCapabilityState({
        label: "Rewards / Drops",
        status: "DEFERRED / UNSUPPORTED",
        description: "There is no canonical per-Boss Admin reward/drop relationship in the current runtime contract.",
      }),
    );

    const identity = panel("Canonical Identity", "Migration preview is read-only until production identity wiring exists");
    identity.append(
      grid(
        readonlyField("Name", boss.name),
        readonlyField("Title", boss.title),
      ),
      grid(
        readonlyField("Family", boss.family),
        readonlyField("Role", boss.role),
        readonlyField("Rank", boss.rank),
      ),
      notice("Name/title values shown here may include an older persisted Admin override. A7 preserves that data but does not offer an authoring control because gameplay still resolves the bundled Boss identity.", "warn"),
    );

    const actions = el("div", "st-admin-page-actions");
    actions.append(
      button("Validate Preview", () => {
        setStatus("Validating preserved Boss migration data against the canonical child registry preview…", "info");
        void previewBosses(policy).then((preview) => {
          activePreview = preview;
          renderList();
          renderEditor();
          setStatus(`Child canonical preview accepted ${preview.bosses.length} Boss definitions for ${preview.configRevision}. This confirms preview compatibility, not production runtime authority.`, "good");
        }).catch((error: unknown) => setStatus(adminErrorMessage(error, "The Bosses preview could not be validated. Check the local Admin runtime and try again."), "bad"));
      }, "st-admin-btn primary"),
    );

    editorHost.append(capabilities, identity, diffPanel(base, boss), actions);
  };

  search.addEventListener("input", renderList);
  familyFilter.addEventListener("change", renderList);
  roleFilter.addEventListener("change", renderList);

  const boundary = panel("A7 Publish Boundary", "No production-backed Boss authoring seam is open in this checkpoint");
  boundary.append(notice("Draft/Publish authoring is intentionally disabled on this page. Existing persisted name/title migration data remains visible and previewable, but changing it would imply runtime authority that the child game does not yet have.", "warn"));
  page.append(boundary);

  const load = (): void => {
    const generation = ++loadGeneration;
    serviceReady = false;
    bundled = null;
    activePreview = null;
    revisionBadge.className = "st-admin-status info";
    revisionBadge.textContent = "ACTIVE · loading";
    search.disabled = true;
    familyFilter.disabled = true;
    roleFilter.disabled = true;
    setStatus("Loading active revision and canonical child Boss registry…", "info");
    rebuildFilters();
    renderList();
    renderEditor();

    void Promise.all([api.getState(), previewBosses()]).then(async ([statePayload, bundledPreview]) => {
      const nextPolicy = policyFrom(statePayload.active.config);
      const nextPreview = await previewBosses(nextPolicy);
      if (generation !== loadGeneration) return;
      bundled = bundledPreview;
      policy = nextPolicy;
      activePreview = nextPreview;
      selectedId = activePreview.bosses[0]?.id ?? "";
      serviceReady = true;
      revisionBadge.className = "st-admin-status good";
      revisionBadge.textContent = `ACTIVE · ${statePayload.state.activeRevision}`;
      search.disabled = false;
      familyFilter.disabled = false;
      roleFilter.disabled = false;
      rebuildFilters();
      renderList();
      renderEditor();
      const hasPolicy = (statePayload.active.config as BossAwareConfig).content?.bosses !== undefined;
      setStatus(
        hasPolicy
          ? `Loaded Boss migration policy ${policy.configRevision}. Name/title overrides are preserved for preview only; production bossIdentityForStage() remains bundled-authoritative.`
          : "No Boss migration policy is stored in the active revision. Bundled child identities are production-authoritative and this A7 page is read-only.",
        hasPolicy ? "warn" : "good",
      );
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      serviceReady = false;
      revisionBadge.className = "st-admin-status bad";
      revisionBadge.textContent = "ACTIVE · unavailable";
      search.disabled = true;
      familyFilter.disabled = true;
      roleFilter.disabled = true;
      listHost.replaceChildren(notice("The canonical Boss registry could not be loaded. Retry after the local Admin service is available.", "bad"));
      editorHost.replaceChildren(notice("Boss capability inspection is disabled until the active revision and canonical preview are loaded.", "warn"));
      status.className = "stx-notice bad";
      status.replaceChildren(document.createTextNode(adminErrorMessage(error, "The Bosses Admin service is unavailable. Check the local runtime and try again.")), document.createTextNode(" "), button("Retry", load));
    });
  };

  load();
  return page;
}
