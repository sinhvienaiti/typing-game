import { SpaceTypingAdminApi, type SpaceTypingAdminConfig } from "./api";
import { adminErrorMessage } from "./admin-http";

const api = new SpaceTypingAdminApi();

type EnemyAdminOverride = {
  minStage?: number;
};
type EnemyProjectilePolicy = "auto" | "off" | "on";
type EnemyAdminPolicy = {
  configRevision: string;
  projectileMode?: EnemyProjectilePolicy;
  enemies?: Record<string, EnemyAdminOverride>;
};
type EnemyVisualProfile = {
  body: string;
  face: string;
  wings: string;
  head?: string;
  side?: string;
  aura?: string;
  orbit?: string;
  rewardMarker?: string;
  spawnFx: string;
  hitFx: string;
  deathFx: string;
};
type EnemyAdminPreviewItem = {
  id: string;
  name: string;
  family: string;
  role: string;
  rarity: "common" | "uncommon" | "rare" | "elite" | "boss";
  minStage: number;
  reward?: string;
  rewardPower?: number;
  visual: EnemyVisualProfile;
  overridden: boolean;
};
type EnemyAdminPreview = {
  protocolVersion: 1;
  configRevision: string;
  enemies: EnemyAdminPreviewItem[];
};
type EnemyAwareConfig = SpaceTypingAdminConfig & {
  content?: NonNullable<SpaceTypingAdminConfig["content"]> & {
    enemies?: EnemyAdminPolicy;
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

function field(label: string, value: string, type: "text" | "number" = "text"): { root: HTMLElement; control: HTMLInputElement } {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label));
  const control = el("input") as HTMLInputElement;
  control.type = type;
  control.value = value;
  control.setAttribute("aria-label", label);
  root.append(control);
  return { root, control };
}

function selectField<T extends string>(label: string, value: T, options: readonly { value: T; label: string }[]): { root: HTMLElement; control: HTMLSelectElement } {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label));
  const control = el("select", "st-admin-select") as HTMLSelectElement;
  control.setAttribute("aria-label", label);
  for (const option of options) control.append(new Option(option.label, option.value));
  control.value = value;
  root.append(control);
  return { root, control };
}

function readonlyField(label: string, value: string): HTMLElement {
  const entry = field(label, value);
  entry.control.disabled = true;
  return entry.root;
}

function policyFrom(config: SpaceTypingAdminConfig): EnemyAdminPolicy {
  const content = (config as EnemyAwareConfig).content;
  const policy = structuredClone(content?.enemies ?? { configRevision: "enemies-admin-v1", enemies: {} });
  policy.projectileMode ??= "auto";
  return policy;
}

function mergeEnemy(base: EnemyAdminPreviewItem, override?: EnemyAdminOverride): EnemyAdminPreviewItem {
  return {
    ...base,
    minStage: override?.minStage ?? base.minStage,
    visual: { ...base.visual },
    overridden: override !== undefined && Object.keys(override).length > 0,
  };
}

async function previewEnemies(policy?: EnemyAdminPolicy): Promise<EnemyAdminPreview> {
  const payload = await api.requestJson<EnemyAdminPreview>("/api/admin/space-typing/enemies/preview", {
    method: "POST",
    body: JSON.stringify(policy === undefined ? {} : { policy }),
  });
  if (payload.protocolVersion !== 1 || !Array.isArray(payload.enemies)) {
    throw new Error("Enemies preview response does not match the canonical Admin contract.");
  }
  return payload;
}

function visualSummary(visual: EnemyVisualProfile): string {
  return [
    `body ${visual.body}`,
    `face ${visual.face}`,
    `wings ${visual.wings}`,
    visual.head ? `head ${visual.head}` : null,
    visual.side ? `side ${visual.side}` : null,
    visual.aura ? `aura ${visual.aura}` : null,
    visual.orbit ? `orbit ${visual.orbit}` : null,
    visual.rewardMarker ? `reward ${visual.rewardMarker}` : null,
  ].filter((value): value is string => value !== null).join(" · ");
}

function diffPanel(base: EnemyAdminPreviewItem, effective: EnemyAdminPreviewItem): HTMLElement {
  const root = panel("Runtime Diff Preview", "Bundled child admission → effective draft admission");
  const row = el("div", "stx-toggle-row");
  const copy = el("div");
  copy.append(el("strong", undefined, "Minimum Stage"), el("small", undefined, `${base.minStage} → ${effective.minStage}`));
  const changed = base.minStage !== effective.minStage;
  row.append(copy, badge(changed ? "CHANGED" : "UNCHANGED", changed ? "warn" : "info"));
  root.append(row, notice(
    changed
      ? "Stage admission differs from the bundled registry. This takes effect only for a new game session after Publish."
      : "No runtime admission difference from the bundled Enemy registry.",
    changed ? "warn" : "info",
  ));
  return root;
}

export function renderPhaseBEnemies(navigate: Navigate): HTMLElement {
  const page = el("div");
  const revisionBadge = badge("ACTIVE · loading", "info");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Game Content · Canonical Enemy Registry · B06.4"),
    el("h1", undefined, "Enemies"),
    el("p", undefined, "Author canonical Enemy admission and normal-enemy projectile policy through immutable revisions. Identity, taxonomy, rewards and visuals remain child-owned."),
  );
  header.append(copy, revisionBadge);
  page.append(header);

  const status = notice("Loading active revision and canonical child Enemy registry…", "info");
  status.setAttribute("aria-live", "polite");

  const projectilePolicyPanel = panel("Combat Projectile Policy", "Admin authority · applies on the next game session after Publish");
  const projectileMode = selectField<EnemyProjectilePolicy>("Normal Enemy Projectiles", "auto", [
    { value: "auto", label: "Auto · follow canonical difficulty" },
    { value: "off", label: "Off · disable normal-enemy projectiles" },
    { value: "on", label: "On · enable normal-enemy projectiles" },
  ]);
  projectileMode.control.disabled = true;
  projectilePolicyPanel.append(
    grid(
      projectileMode.root,
      readonlyField("Boss Projectiles", "Always enabled · child-owned combat rule"),
    ),
    notice("This published value is authoritative over the legacy hidden player setting. LocalStorage or DevTools cannot override it while the platform runtime is published. `Auto` preserves the canonical difficulty-driven behavior.", "info"),
  );

  const filterBar = el("div", "st-admin-filterbar");
  const search = el("input", "st-admin-search") as HTMLInputElement;
  search.placeholder = "Search enemies…";
  search.setAttribute("aria-label", "Search Enemies");
  const familyFilter = el("select", "st-admin-select") as HTMLSelectElement;
  familyFilter.setAttribute("aria-label", "Enemy family filter");
  const roleFilter = el("select", "st-admin-select") as HTMLSelectElement;
  roleFilter.setAttribute("aria-label", "Enemy role filter");
  filterBar.append(search, familyFilter, roleFilter, el("div", "st-admin-filter-spacer"), badge("APPLY · NEW SESSION", "info"));

  const body = el("div", "stx-grid");
  const listPanel = panel("Canonical Enemies", "35 child-owned Enemy definitions · immutable identity / taxonomy / visuals / rewards");
  const listHost = el("div");
  listPanel.append(listHost);
  const editorPanel = panel("Enemy Admission Override", "`content.enemies.enemies.<id>.minStage` plus the global projectile policy are persisted in B06.4");
  const editorHost = el("div");
  editorPanel.append(editorHost);
  body.append(listPanel, editorPanel);
  page.append(status, projectilePolicyPanel, filterBar, body);

  let loadedActiveRevision: string | null = null;
  let bundled: EnemyAdminPreview | null = null;
  let activePreview: EnemyAdminPreview | null = null;
  let selectedId = "";
  let policy: EnemyAdminPolicy = { configRevision: "enemies-admin-v1", projectileMode: "auto", enemies: {} };
  let serviceReady = false;
  let loadGeneration = 0;

  search.disabled = true;
  familyFilter.disabled = true;
  roleFilter.disabled = true;

  const setStatus = (text: string, tone: Tone = "info"): void => {
    status.className = `stx-notice ${tone}`;
    status.textContent = text;
  };

  projectileMode.control.addEventListener("change", () => {
    if (!serviceReady) return;
    const value = projectileMode.control.value;
    if (value !== "auto" && value !== "off" && value !== "on") return;
    policy.projectileMode = value;
    setStatus(`Normal-enemy projectile draft changed to ${value}. Save Draft and Publish to make it authoritative for new sessions.`, "warn");
  });

  const baseEnemy = (id: string): EnemyAdminPreviewItem | undefined => bundled?.enemies.find((enemy) => enemy.id === id);
  const effectiveEnemy = (id: string): EnemyAdminPreviewItem | undefined => {
    const base = baseEnemy(id);
    if (!base) return activePreview?.enemies.find((enemy) => enemy.id === id);
    return mergeEnemy(base, policy.enemies?.[id]);
  };

  const rebuildFilters = (): void => {
    const selectedFamily = familyFilter.value || "all";
    const selectedRole = roleFilter.value || "all";
    const source = bundled?.enemies ?? activePreview?.enemies ?? [];
    familyFilter.replaceChildren(new Option("All families", "all"));
    roleFilter.replaceChildren(new Option("All roles", "all"));
    for (const family of Array.from(new Set(source.map((enemy) => enemy.family))).sort()) familyFilter.append(new Option(family, family));
    for (const role of Array.from(new Set(source.map((enemy) => enemy.role))).sort()) roleFilter.append(new Option(role, role));
    familyFilter.value = Array.from(familyFilter.options).some((option) => option.value === selectedFamily) ? selectedFamily : "all";
    roleFilter.value = Array.from(roleFilter.options).some((option) => option.value === selectedRole) ? selectedRole : "all";
  };

  const renderList = (): void => {
    listHost.replaceChildren();
    const allEnemies = bundled?.enemies ?? activePreview?.enemies ?? [];
    if (!serviceReady || allEnemies.length === 0) {
      listHost.append(notice(serviceReady ? "No canonical Enemy definitions were returned by the preview." : "Load the canonical Enemy registry to browse and filter definitions.", serviceReady ? "warn" : "info"));
      return;
    }
    const query = search.value.trim().toLowerCase();
    const family = familyFilter.value || "all";
    const role = roleFilter.value || "all";
    const enemies = allEnemies.filter((enemy) => {
      const familyMatch = family === "all" || enemy.family === family;
      const roleMatch = role === "all" || enemy.role === role;
      const queryMatch = query.length === 0 || `${enemy.id} ${enemy.name} ${enemy.family} ${enemy.role} ${enemy.rarity}`.toLowerCase().includes(query);
      return familyMatch && roleMatch && queryMatch;
    });
    if (enemies.length === 0) {
      listHost.append(notice("No Enemy definitions match the current filters.", "warn"));
      return;
    }
    for (const enemy of enemies) {
      const current = effectiveEnemy(enemy.id) ?? enemy;
      const row = el("div", "stx-toggle-row");
      const copyNode = el("div");
      copyNode.append(
        el("strong", undefined, current.name),
        el("small", undefined, `${enemy.id} · ${enemy.family} · ${enemy.role} · ${enemy.rarity} · stage ${current.minStage}+`),
      );
      const actions = el("div");
      if (policy.enemies?.[enemy.id] && Object.keys(policy.enemies[enemy.id]).length > 0) actions.append(badge("OVERRIDE", "warn"));
      const edit = button(selectedId === enemy.id ? "Editing" : "Edit", () => {
        selectedId = enemy.id;
        renderList();
        renderEditor();
      }, selectedId === enemy.id ? "st-admin-btn primary" : "st-admin-btn");
      edit.disabled = !serviceReady;
      actions.append(edit);
      row.append(copyNode, actions);
      listHost.append(row);
    }
  };

  const renderEditor = (): void => {
    editorHost.replaceChildren();
    const base = baseEnemy(selectedId);
    const enemy = effectiveEnemy(selectedId);
    if (!serviceReady || !base || !enemy) {
      editorHost.append(notice(serviceReady ? "No Enemy is selected." : "Load the active revision and canonical Enemy preview before editing admission.", serviceReady ? "warn" : "info"));
      return;
    }

    editorHost.append(notice(`ID ${enemy.id} · ${enemy.family}/${enemy.role}/${enemy.rarity} · apply boundary: new session`, "info"));
    editorHost.append(notice(
      "HP, Shield, Armor, Speed, Damage, AI, Spawn Weight, Skills, per-enemy projectile definitions, VFX, SFX, Drop Table and Enabled remain read-only because the current child Enemy contract does not expose canonical authorable runtime fields for them. The global normal-enemy projectile switch is managed by Combat Projectile Policy above.",
      "warn",
    ));

    const identity = panel("Canonical Identity & Taxonomy", "Child-owned and immutable in B06.4");
    identity.append(grid(
      readonlyField("Name", enemy.name),
      readonlyField("Family", enemy.family),
      readonlyField("Role", enemy.role),
      readonlyField("Rarity", enemy.rarity),
    ));

    const admission = panel("Stage Admission", "Canonical runtime consumer: Enemy spawn profile minimum-stage gate");
    const minStage = field("Minimum Stage", String(enemy.minStage), "number");
    minStage.control.min = "1";
    minStage.control.max = "1000";
    minStage.control.step = "1";
    minStage.control.addEventListener("input", () => {
      policy.enemies ??= {};
      policy.enemies[selectedId] ??= {};
      policy.enemies[selectedId].minStage = Number(minStage.control.value);
      renderList();
    });
    admission.append(minStage.root, notice("Valid range: Stage 1–1000. A higher value delays admission; a lower value allows this Enemy definition earlier where the existing spawn selection chooses it.", "info"));

    const rewards = panel("Rewards", "Canonical child definition · read-only in this slice");
    rewards.append(grid(
      readonlyField("Reward", enemy.reward ?? "—"),
      readonlyField("Reward Power", enemy.rewardPower === undefined ? "—" : String(enemy.rewardPower)),
    ));

    const visuals = panel("Visual Profile", "Canonical child presentation · read-only");
    visuals.append(
      notice(visualSummary(enemy.visual), "info"),
      grid(
        readonlyField("Spawn FX", enemy.visual.spawnFx),
        readonlyField("Hit FX", enemy.visual.hitFx),
        readonlyField("Death FX", enemy.visual.deathFx),
      ),
    );

    const actions = el("div", "st-admin-page-actions");
    actions.append(
      button("Reset Enemy Override", () => {
        if (policy.enemies) delete policy.enemies[selectedId];
        renderList();
        renderEditor();
        setStatus(`${selectedId} reset to bundled child admission. Save Draft to persist this removal.`, "good");
      }),
      button("Validate Preview", () => {
        setStatus("Validating Enemy admission and projectile policy against the canonical child preview…", "info");
        void previewEnemies(policy).then((preview) => {
          activePreview = preview;
          renderList();
          renderEditor();
          setStatus(`Child canonical preview accepted ${preview.enemies.length} Enemy definitions and projectile policy for ${preview.configRevision}.`, "good");
        }).catch((error: unknown) => setStatus(adminErrorMessage(error, "The Enemies preview could not be validated. Check the local Admin runtime and try again."), "bad"));
      }, "st-admin-btn primary"),
    );

    editorHost.append(identity, admission, rewards, visuals, diffPanel(base, enemy), actions);
  };

  search.addEventListener("input", renderList);
  familyFilter.addEventListener("change", renderList);
  roleFilter.addEventListener("change", renderList);

  const saveBar = el("div", "st-admin-sticky-save stx-savebar");
  const saveStatus = el("span", undefined, "Load the active revision before saving an Enemy draft");
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
        const validated = await previewEnemies(policy);
        const config = structuredClone(payload.active.config) as EnemyAwareConfig;
        config.content = { ...(config.content ?? {}), enemies: structuredClone(policy) };
        const revision = await api.createRevision({
          baseRevision: payload.active.revision,
          config,
          message: "Admin Phase B · B06.4 Enemy admission + projectile policy draft",
        });
        activePreview = validated;
        saveStatus.textContent = `Draft saved · ${revision.revision} · runtime unchanged`;
        setStatus(`Draft ${revision.revision} passed child preview + server validation. Publish from History to activate it; gameplay snapshots Enemy admission and projectile policy only when a new session starts.`, "good");
      } catch (error: unknown) {
        const message = adminErrorMessage(error, "The Enemy draft could not be saved. Check the local Admin runtime and try again.");
        saveStatus.textContent = `Draft rejected · ${message}`;
        setStatus(`Validation/save failed: ${message}`, "bad");
      } finally {
        save.disabled = !serviceReady;
      }
    })();
  }, "st-admin-btn primary");
  save.disabled = true;
  saveBar.append(
    el("strong", undefined, "B06.4 Enemy + Combat Draft"),
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
    search.disabled = true;
    familyFilter.disabled = true;
    roleFilter.disabled = true;
    projectileMode.control.disabled = true;
    projectileMode.control.value = "auto";
    save.disabled = true;
    saveStatus.textContent = "Load the active revision before saving an Enemy draft";
    setStatus("Loading active revision and canonical child Enemy registry…", "info");
    rebuildFilters();
    renderList();
    renderEditor();

    void Promise.all([api.getState(), previewEnemies()]).then(async ([statePayload, bundledPreview]) => {
      const nextPolicy = policyFrom(statePayload.active.config);
      const nextPreview = await previewEnemies(nextPolicy);
      if (generation !== loadGeneration) return;
      loadedActiveRevision = statePayload.state.activeRevision;
      bundled = bundledPreview;
      policy = nextPolicy;
      activePreview = nextPreview;
      selectedId = activePreview.enemies[0]?.id ?? "";
      serviceReady = true;
      revisionBadge.className = "st-admin-status good";
      revisionBadge.textContent = `ACTIVE · ${statePayload.state.activeRevision}`;
      search.disabled = false;
      familyFilter.disabled = false;
      roleFilter.disabled = false;
      projectileMode.control.value = policy.projectileMode ?? "auto";
      projectileMode.control.disabled = false;
      save.disabled = false;
      saveStatus.textContent = "Revision-backed · no direct runtime mutation";
      rebuildFilters();
      renderList();
      renderEditor();
      const hasPolicy = (statePayload.active.config as EnemyAwareConfig).content?.enemies !== undefined;
      setStatus(
        hasPolicy
          ? `Loaded active Enemy policy ${policy.configRevision} · normal-enemy projectiles: ${policy.projectileMode ?? "auto"}. Save Draft is isolated until History / Publish.`
          : "Active revision predates B06.4 Enemy policy; bundled admission plus Admin-owned auto projectile behavior are shown until the first draft is saved.",
        hasPolicy ? "good" : "warn",
      );
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      serviceReady = false;
      loadedActiveRevision = null;
      revisionBadge.className = "st-admin-status bad";
      revisionBadge.textContent = "ACTIVE · unavailable";
      search.disabled = true;
      familyFilter.disabled = true;
      roleFilter.disabled = true;
      projectileMode.control.disabled = true;
      save.disabled = true;
      listHost.replaceChildren(notice("The canonical Enemy registry could not be loaded. Retry after the local Admin service is available.", "bad"));
      editorHost.replaceChildren(notice("Enemy admission overrides are disabled until the active revision and canonical preview are loaded.", "warn"));
      status.className = "stx-notice bad";
      status.replaceChildren(document.createTextNode(adminErrorMessage(error, "The Enemies Admin service is unavailable. Check the local runtime and try again.")), document.createTextNode(" "), button("Retry", load));
    });
  };

  load();
  return page;
}