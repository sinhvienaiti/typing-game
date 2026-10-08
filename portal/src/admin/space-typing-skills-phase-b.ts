import { SpaceTypingAdminApi, type SpaceTypingAdminConfig } from "./api";

const api = new SpaceTypingAdminApi();
const SKILL_CATEGORIES = ["offensive", "defensive", "support"] as const;

type SkillCategory = (typeof SKILL_CATEGORIES)[number];
type SkillTypingCondition = { minStreak?: number; minAccuracy?: number };
type SkillAdminOverride = {
  name?: string;
  description?: string;
  energyCost?: number;
  cooldown?: number;
  charges?: number | null;
  perStageLimit?: number | null;
  typingCondition?: SkillTypingCondition | null;
};
type SkillAdminPolicy = {
  configRevision: string;
  skills?: Record<string, SkillAdminOverride>;
};
type SkillAdminPreviewItem = {
  id: string;
  name: string;
  description?: string;
  energyCost: number;
  cooldown: number;
  charges: number | null;
  perStageLimit: number | null;
  typingCondition?: SkillTypingCondition;
  category: SkillCategory;
  overridden: boolean;
};
type SkillAdminPreview = {
  protocolVersion: 1;
  configRevision: string;
  skills: SkillAdminPreviewItem[];
};
type SkillAwareConfig = SpaceTypingAdminConfig & {
  content?: NonNullable<SpaceTypingAdminConfig["content"]> & {
    skills?: SkillAdminPolicy;
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

function policyFrom(config: SpaceTypingAdminConfig): SkillAdminPolicy {
  const content = (config as SkillAwareConfig).content;
  return structuredClone(content?.skills ?? { configRevision: "skills-admin-v1", skills: {} });
}

function mergeSkill(base: SkillAdminPreviewItem, override?: SkillAdminOverride): SkillAdminPreviewItem {
  const merged: SkillAdminPreviewItem = {
    ...base,
    ...(override ?? {}),
    id: base.id,
    category: base.category,
    typingCondition: override?.typingCondition === undefined
      ? base.typingCondition === undefined ? undefined : { ...base.typingCondition }
      : override.typingCondition === null ? undefined : { ...override.typingCondition },
    overridden: override !== undefined && Object.keys(override).length > 0,
  };
  return merged;
}

async function previewSkills(policy?: SkillAdminPolicy): Promise<SkillAdminPreview> {
  const response = await fetch("/api/admin/space-typing/skills/preview", {
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
        : `Skills preview failed (${response.status})`;
    throw new Error(message);
  }
  return payload as unknown as SkillAdminPreview;
}

function valueLabel(value: unknown): string {
  if (value === undefined) return "—";
  if (value === null) return "∞";
  if (typeof value === "object") return JSON.stringify(value);
  return String(value);
}

function diffPanel(base: SkillAdminPreviewItem, effective: SkillAdminPreviewItem): HTMLElement {
  const root = panel("Runtime Diff Preview", "Bundled child definition → effective draft definition");
  const rows: Array<[string, unknown, unknown]> = [
    ["Name", base.name, effective.name],
    ["Energy Cost", base.energyCost, effective.energyCost],
    ["Cooldown", base.cooldown, effective.cooldown],
    ["Charges", base.charges, effective.charges],
    ["Per-stage Limit", base.perStageLimit, effective.perStageLimit],
    ["Typing Condition", base.typingCondition, effective.typingCondition],
  ];
  let changes = 0;
  for (const [label, before, after] of rows) {
    const beforeText = valueLabel(before);
    const afterText = valueLabel(after);
    const changed = beforeText !== afterText;
    if (changed) changes += 1;
    const row = el("div", "stx-toggle-row");
    const copy = el("div");
    copy.append(el("strong", undefined, label), el("small", undefined, `${beforeText} → ${afterText}`));
    row.append(copy, badge(changed ? "CHANGED" : "UNCHANGED", changed ? "warn" : "info"));
    root.append(row);
  }
  root.append(notice(changes === 0 ? "No runtime differences from the bundled skill definition." : `${changes} runtime field(s) differ from the bundled definition.`, changes === 0 ? "info" : "warn"));
  return root;
}

export function renderPhaseBSkills(navigate: Navigate): HTMLElement {
  const page = el("div");
  const revisionBadge = badge("ACTIVE · loading", "info");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Game Content · Canonical Skill Registry · B06.3"),
    el("h1", undefined, "Skills"),
    el("p", undefined, "Author the canonical combat Skill definitions through immutable revisions. The published policy is snapshotted once per game session; Save Draft never mutates the live session."),
  );
  header.append(copy, revisionBadge);
  page.append(header);

  const status = notice("Loading active revision and canonical child Skill registry…", "info");
  const filterBar = el("div", "st-admin-filterbar");
  const search = el("input", "st-admin-search") as HTMLInputElement;
  search.placeholder = "Search skills…";
  search.setAttribute("aria-label", "Search Skills");
  const categoryFilter = el("select", "st-admin-select") as HTMLSelectElement;
  categoryFilter.setAttribute("aria-label", "Skill category filter");
  categoryFilter.append(new Option("All categories", "all"));
  for (const category of SKILL_CATEGORIES) categoryFilter.append(new Option(category, category));
  filterBar.append(search, categoryFilter, el("div", "st-admin-filter-spacer"), badge("APPLY · NEW SESSION", "info"));

  const body = el("div", "stx-grid");
  const listPanel = panel("Canonical Skills", "15 child-owned combat skills · immutable ID / category");
  const listHost = el("div");
  listPanel.append(listHost);
  const editorPanel = panel("Skill Override", "Only authored differences are persisted in `content.skills.skills.<id>`");
  const editorHost = el("div");
  editorPanel.append(editorHost);
  body.append(listPanel, editorPanel);
  page.append(status, filterBar, body);

  let loadedActiveRevision: string | null = null;
  let bundled: SkillAdminPreview | null = null;
  let activePreview: SkillAdminPreview | null = null;
  let selectedId = "";
  let policy: SkillAdminPolicy = { configRevision: "skills-admin-v1", skills: {} };

  const setStatus = (text: string, tone: Tone = "info"): void => {
    status.className = `stx-notice ${tone}`;
    status.textContent = text;
  };

  const overrideFor = (id: string): SkillAdminOverride => {
    policy.skills ??= {};
    policy.skills[id] ??= {};
    return policy.skills[id];
  };

  const baseSkill = (id: string): SkillAdminPreviewItem | undefined => bundled?.skills.find((skill) => skill.id === id);
  const effectiveSkill = (id: string): SkillAdminPreviewItem | undefined => {
    const base = baseSkill(id);
    if (!base) return activePreview?.skills.find((skill) => skill.id === id);
    return mergeSkill(base, policy.skills?.[id]);
  };

  const renderList = (): void => {
    listHost.replaceChildren();
    const query = search.value.trim().toLowerCase();
    const category = categoryFilter.value;
    const skills = (bundled?.skills ?? activePreview?.skills ?? []).filter((skill) => {
      const categoryMatch = category === "all" || skill.category === category;
      const queryMatch = query.length === 0 || `${skill.id} ${skill.name} ${skill.category}`.toLowerCase().includes(query);
      return categoryMatch && queryMatch;
    });
    if (skills.length === 0) {
      listHost.append(notice("No Skills match the current filters.", "warn"));
      return;
    }
    for (const skill of skills) {
      const current = effectiveSkill(skill.id) ?? skill;
      const row = el("div", "stx-toggle-row");
      const copyNode = el("div");
      copyNode.append(
        el("strong", undefined, current.name),
        el("small", undefined, `${skill.id} · ${skill.category} · ${current.energyCost} energy · ${current.cooldown}s cooldown`),
      );
      const actions = el("div");
      if (policy.skills?.[skill.id] && Object.keys(policy.skills[skill.id]).length > 0) actions.append(badge("OVERRIDE", "warn"));
      actions.append(button(selectedId === skill.id ? "Editing" : "Edit", () => {
        selectedId = skill.id;
        renderList();
        renderEditor();
      }, selectedId === skill.id ? "st-admin-btn primary" : "st-admin-btn"));
      row.append(copyNode, actions);
      listHost.append(row);
    }
  };

  const renderEditor = (): void => {
    editorHost.replaceChildren();
    const base = baseSkill(selectedId);
    const skill = effectiveSkill(selectedId);
    if (!base || !skill) {
      editorHost.append(notice("Skill registry has not finished loading.", "warn"));
      return;
    }

    editorHost.append(notice(`ID ${skill.id} · category ${skill.category} · apply boundary: new session`, "info"));
    editorHost.append(notice("The master UI plan also lists behavior/presentation fields such as damage, radius, duration, projectile, VFX, SFX and camera effects. B06.3 does not persist those generically until the child runtime exposes canonical typed fields for them.", "warn"));

    const identity = panel("Identity", "Name and description are authorable; ID and category remain child-owned.");
    const name = field("Name", skill.name);
    (name.control as HTMLInputElement).maxLength = 100;
    name.control.addEventListener("input", () => {
      overrideFor(selectedId).name = name.control.value;
      renderList();
    });
    const category = field("Category (immutable)", skill.category, SKILL_CATEGORIES);
    category.control.disabled = true;
    const description = descriptionField(skill.description ?? "");
    description.control.addEventListener("input", () => {
      overrideFor(selectedId).description = description.control.value;
    });
    identity.append(grid(name.root, category.root), description.root);

    const gameplay = panel("Runtime Costs & Limits", "Validated against the child SkillDefinition contract");
    const energy = field("Energy Cost", String(skill.energyCost), undefined, "number");
    const cooldown = field("Cooldown (seconds)", String(skill.cooldown), undefined, "number");
    const charges = field("Charges (blank = unlimited)", skill.charges === null ? "" : String(skill.charges), undefined, "number");
    const perStage = field("Per-stage Limit (blank = unlimited)", skill.perStageLimit === null ? "" : String(skill.perStageLimit), undefined, "number");
    const energyInput = energy.control as HTMLInputElement;
    energyInput.min = "0"; energyInput.max = "200"; energyInput.step = "0.1";
    const cooldownInput = cooldown.control as HTMLInputElement;
    cooldownInput.min = "0"; cooldownInput.max = "300"; cooldownInput.step = "0.1";
    const chargesInput = charges.control as HTMLInputElement;
    chargesInput.min = "0"; chargesInput.max = "99"; chargesInput.step = "1";
    const perStageInput = perStage.control as HTMLInputElement;
    perStageInput.min = "0"; perStageInput.max = "99"; perStageInput.step = "1";
    energy.control.addEventListener("input", () => { overrideFor(selectedId).energyCost = Number(energy.control.value); renderList(); });
    cooldown.control.addEventListener("input", () => { overrideFor(selectedId).cooldown = Number(cooldown.control.value); renderList(); });
    charges.control.addEventListener("input", () => { overrideFor(selectedId).charges = charges.control.value.trim() === "" ? null : Number(charges.control.value); });
    perStage.control.addEventListener("input", () => { overrideFor(selectedId).perStageLimit = perStage.control.value.trim() === "" ? null : Number(perStage.control.value); });
    gameplay.append(grid(energy.root, cooldown.root), grid(charges.root, perStage.root));

    const conditionPanel = panel("Typing Condition", "Inherit bundled condition, explicitly override it, or remove it for this published policy.");
    const currentOverride = policy.skills?.[selectedId]?.typingCondition;
    const modeValue = currentOverride === null ? "none" : currentOverride === undefined ? "inherit" : "override";
    const mode = field("Condition Mode", modeValue, ["inherit", "override", "none"]);
    const streak = field("Minimum Streak", String(skill.typingCondition?.minStreak ?? ""), undefined, "number");
    const accuracy = field("Minimum Accuracy %", String(skill.typingCondition?.minAccuracy ?? ""), undefined, "number");
    const streakInput = streak.control as HTMLInputElement;
    streakInput.min = "0"; streakInput.max = "999"; streakInput.step = "1";
    const accuracyInput = accuracy.control as HTMLInputElement;
    accuracyInput.min = "0"; accuracyInput.max = "100"; accuracyInput.step = "0.1";
    const syncConditionControls = (): void => {
      const editing = mode.control.value === "override";
      streak.control.disabled = !editing;
      accuracy.control.disabled = !editing;
    };
    const writeCondition = (): void => {
      if (mode.control.value === "inherit") {
        delete overrideFor(selectedId).typingCondition;
      } else if (mode.control.value === "none") {
        overrideFor(selectedId).typingCondition = null;
      } else {
        const condition: SkillTypingCondition = {};
        if (streak.control.value.trim() !== "") condition.minStreak = Number(streak.control.value);
        if (accuracy.control.value.trim() !== "") condition.minAccuracy = Number(accuracy.control.value);
        overrideFor(selectedId).typingCondition = condition;
      }
    };
    mode.control.addEventListener("change", () => { writeCondition(); syncConditionControls(); renderList(); });
    streak.control.addEventListener("input", writeCondition);
    accuracy.control.addEventListener("input", writeCondition);
    syncConditionControls();
    conditionPanel.append(grid(mode.root, streak.root, accuracy.root));

    const actions = el("div", "st-admin-page-actions");
    actions.append(
      button("Reset Skill Override", () => {
        if (policy.skills) delete policy.skills[selectedId];
        renderList();
        renderEditor();
        setStatus(`${selectedId} reset to bundled child values. Save Draft to persist this removal.`, "good");
      }),
      button("Validate Preview", () => {
        void previewSkills(policy).then((preview) => {
          activePreview = preview;
          renderList();
          renderEditor();
          setStatus(`Child canonical preview accepted ${preview.skills.length} Skills for ${preview.configRevision}.`, "good");
        }).catch((error: unknown) => setStatus(`Preview rejected: ${error instanceof Error ? error.message : String(error)}`, "bad"));
      }, "st-admin-btn primary"),
    );

    editorHost.append(identity, gameplay, conditionPanel, diffPanel(base, skill), actions);
  };

  search.addEventListener("input", renderList);
  categoryFilter.addEventListener("change", renderList);

  void Promise.all([api.getState(), previewSkills()]).then(async ([statePayload, bundledPreview]) => {
    loadedActiveRevision = statePayload.state.activeRevision;
    revisionBadge.textContent = `ACTIVE · ${statePayload.state.activeRevision}`;
    bundled = bundledPreview;
    policy = policyFrom(statePayload.active.config);
    activePreview = await previewSkills(policy);
    selectedId = activePreview.skills[0]?.id ?? "";
    renderList();
    renderEditor();
    const hasPolicy = (statePayload.active.config as SkillAwareConfig).content?.skills !== undefined;
    setStatus(
      hasPolicy
        ? `Loaded active Skills policy ${policy.configRevision}. Save Draft is isolated until History / Publish.`
        : "Active revision predates B06.3 Skills policy; bundled child registry is shown until the first draft is saved.",
      hasPolicy ? "good" : "warn",
    );
  }).catch((error: unknown) => setStatus(`Skills Admin unavailable: ${error instanceof Error ? error.message : String(error)}`, "bad"));

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
        const validated = await previewSkills(policy);
        const config = structuredClone(payload.active.config) as SkillAwareConfig;
        config.content = { ...(config.content ?? {}), skills: structuredClone(policy) };
        const revision = await api.createRevision({
          baseRevision: payload.active.revision,
          config,
          message: "Admin Phase B · B06.3 Skills registry draft",
        });
        activePreview = validated;
        saveStatus.textContent = `Draft saved · ${revision.revision} · runtime unchanged`;
        setStatus(`Draft ${revision.revision} passed child preview + server validation. Publish from History to activate it; gameplay snapshots the published Skill policy only on the next session.`, "good");
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
    el("strong", undefined, "B06.3 Skills Draft"),
    saveStatus,
    el("div", "grow"),
    button("Discard", () => navigate(location.pathname)),
    save,
  );
  page.append(saveBar);
  return page;
}
