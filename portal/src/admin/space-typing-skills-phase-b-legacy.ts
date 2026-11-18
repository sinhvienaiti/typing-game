import { SpaceTypingAdminApi, type SpaceTypingAdminConfig } from "./api";
import { adminErrorMessage } from "./admin-http";
import { AdminHelpScope, createAdminFieldShell } from "./v2/admin-help";
import { createAssetTuningCapabilityState } from "./v2/asset-tuning-studio";

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
  return {
    ...base,
    ...(override ?? {}),
    id: base.id,
    category: base.category,
    typingCondition: override?.typingCondition === undefined
      ? base.typingCondition === undefined ? undefined : { ...base.typingCondition }
      : override.typingCondition === null ? undefined : { ...override.typingCondition },
    overridden: override !== undefined && Object.keys(override).length > 0,
  };
}

async function previewSkills(policy?: SkillAdminPolicy): Promise<SkillAdminPreview> {
  const payload = await api.requestJson<SkillAdminPreview>("/api/admin/space-typing/skills/preview", {
    method: "POST",
    body: JSON.stringify(policy === undefined ? {} : { policy }),
  });
  if (payload.protocolVersion !== 1 || !Array.isArray(payload.skills)) {
    throw new Error("Skills preview response does not match the canonical Admin contract.");
  }
  return payload;
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
  const helpScope = new AdminHelpScope();
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
  status.setAttribute("aria-live", "polite");
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
  let serviceReady = false;
  let loadGeneration = 0;

  search.disabled = true;
  categoryFilter.disabled = true;

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
    const allSkills = bundled?.skills ?? activePreview?.skills ?? [];
    if (!serviceReady || allSkills.length === 0) {
      listHost.append(notice(serviceReady ? "No canonical Skills were returned by the preview." : "Load the canonical Skill registry to browse and filter Skills.", serviceReady ? "warn" : "info"));
      return;
    }
    const query = search.value.trim().toLowerCase();
    const category = categoryFilter.value;
    const skills = allSkills.filter((skill) => {
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
      const edit = button(selectedId === skill.id ? "Editing" : "Edit", () => {
        selectedId = skill.id;
        renderList();
        renderEditor();
      }, selectedId === skill.id ? "st-admin-btn primary" : "st-admin-btn");
      edit.disabled = !serviceReady;
      actions.append(edit);
      row.append(copyNode, actions);
      listHost.append(row);
    }
  };

  const renderEditor = (): void => {
    editorHost.replaceChildren();
    const base = baseSkill(selectedId);
    const skill = effectiveSkill(selectedId);
    if (!serviceReady || !base || !skill) {
      editorHost.append(notice(serviceReady ? "No Skill is selected." : "Load the active revision and canonical Skill preview before editing overrides.", serviceReady ? "warn" : "info"));
      return;
    }

    editorHost.append(notice(`ID ${skill.id} · category ${skill.category} · apply boundary: new session`, "info"));
    const capabilities = panel("Capabilities", "Only production-backed Skill controls are editable.");
    capabilities.append(
      createAssetTuningCapabilityState({
        label: "Gameplay Policy",
        status: "AVAILABLE",
        description: "Name, description, energy, cooldown, charges, stage limit and typing condition are revision-backed.",
      }),
      createAssetTuningCapabilityState({
        label: "Media / VFX",
        status: "REQUIRES CANONICAL MIGRATION",
        description: "Production effects are still code-owned; no generic Media, VFX or SFX binding is authorable yet.",
      }),
    );

    const identity = panel("Identity", "Canonical Skill identity");
    const name = field("Name", skill.name);
    (name.control as HTMLInputElement).maxLength = 100;
    name.control.addEventListener("input", () => {
      overrideFor(selectedId).name = name.control.value;
      renderList();
    });
    const category = field("Category", skill.category, SKILL_CATEGORIES);
    category.control.disabled = true;
    const categoryShell = createAdminFieldShell(helpScope, {
      label: "Category",
      control: category.control,
      help: {
        title: "Skill Category",
        content: "Owned by the child Skill registry. Admin may edit gameplay policy but cannot move a Skill between categories.",
      },
      stateMessage: "Child-owned · read only",
      stateTone: "info",
    });
    const description = descriptionField(skill.description ?? "");
    description.control.addEventListener("input", () => {
      overrideFor(selectedId).description = description.control.value;
    });
    identity.append(grid(name.root, categoryShell), description.root);

    const gameplay = panel("Runtime Costs & Limits", "Published changes apply on the next game session.");
    const energy = field("Energy Cost", String(skill.energyCost), undefined, "number");
    const cooldown = field("Cooldown", String(skill.cooldown), undefined, "number");
    const charges = field("Charges", skill.charges === null ? "" : String(skill.charges), undefined, "number");
    const perStage = field("Per-stage Limit", skill.perStageLimit === null ? "" : String(skill.perStageLimit), undefined, "number");
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
    const energyShell = createAdminFieldShell(helpScope, {
      label: "Energy Cost",
      control: energy.control,
      help: { title: "Energy Cost", content: "Energy consumed when this Skill activates. Allowed range: 0–200." },
    });
    const cooldownShell = createAdminFieldShell(helpScope, {
      label: "Cooldown",
      control: cooldown.control,
      help: { title: "Cooldown", content: "Seconds before the Skill can activate again. Allowed range: 0–300." },
    });
    const chargesShell = createAdminFieldShell(helpScope, {
      label: "Charges",
      control: charges.control,
      help: { title: "Charges", content: "Maximum activations available from the canonical Skill definition. Leave empty for unlimited." },
    });
    const perStageShell = createAdminFieldShell(helpScope, {
      label: "Per-stage Limit",
      control: perStage.control,
      help: { title: "Per-stage Limit", content: "Maximum activations during one stage. Leave empty for unlimited." },
    });
    gameplay.append(grid(energyShell, cooldownShell), grid(chargesShell, perStageShell));

    const conditionPanel = panel("Typing Condition", "Optional activation requirements");
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
    const modeShell = createAdminFieldShell(helpScope, {
      label: "Condition Mode",
      control: mode.control,
      help: {
        title: "Typing Condition Mode",
        content: "Inherit keeps the bundled condition, Override writes explicit thresholds, and None removes the condition from this published policy.",
      },
    });
    conditionPanel.append(grid(modeShell, streak.root, accuracy.root));

    const actions = el("div", "st-admin-page-actions");
    actions.append(
      button("Reset Skill Override", () => {
        if (policy.skills) delete policy.skills[selectedId];
        renderList();
        renderEditor();
        setStatus(`${selectedId} reset to bundled child values. Save Draft to persist this removal.`, "good");
      }),
      button("Validate Preview", () => {
        setStatus("Validating Skill overrides against the canonical child preview…", "info");
        void previewSkills(policy).then((preview) => {
          activePreview = preview;
          renderList();
          renderEditor();
          setStatus(`Child canonical preview accepted ${preview.skills.length} Skills for ${preview.configRevision}.`, "good");
        }).catch((error: unknown) => setStatus(adminErrorMessage(error, "The Skills preview could not be validated. Check the local Admin runtime and try again."), "bad"));
      }, "st-admin-btn primary"),
    );

    editorHost.append(capabilities, identity, gameplay, conditionPanel, diffPanel(base, skill), actions);
  };

  search.addEventListener("input", renderList);
  categoryFilter.addEventListener("change", renderList);

  const saveBar = el("div", "st-admin-sticky-save stx-savebar");
  const saveStatus = el("span", undefined, "Load the active revision before saving a Skills draft");
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
        const message = adminErrorMessage(error, "The Skills draft could not be saved. Check the local Admin runtime and try again.");
        saveStatus.textContent = `Draft rejected · ${message}`;
        setStatus(`Validation/save failed: ${message}`, "bad");
      } finally {
        save.disabled = !serviceReady;
      }
    })();
  }, "st-admin-btn primary");
  save.disabled = true;
  saveBar.append(
    el("strong", undefined, "B06.3 Skills Draft"),
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
    categoryFilter.disabled = true;
    save.disabled = true;
    saveStatus.textContent = "Load the active revision before saving a Skills draft";
    setStatus("Loading active revision and canonical child Skill registry…", "info");
    renderList();
    renderEditor();

    void Promise.all([api.getState(), previewSkills()]).then(async ([statePayload, bundledPreview]) => {
      const nextPolicy = policyFrom(statePayload.active.config);
      const nextPreview = await previewSkills(nextPolicy);
      if (generation !== loadGeneration) return;
      loadedActiveRevision = statePayload.state.activeRevision;
      bundled = bundledPreview;
      policy = nextPolicy;
      activePreview = nextPreview;
      selectedId = activePreview.skills[0]?.id ?? "";
      serviceReady = true;
      revisionBadge.className = "st-admin-status good";
      revisionBadge.textContent = `ACTIVE · ${statePayload.state.activeRevision}`;
      search.disabled = false;
      categoryFilter.disabled = false;
      save.disabled = false;
      saveStatus.textContent = "Revision-backed · no direct runtime mutation";
      renderList();
      renderEditor();
      const hasPolicy = (statePayload.active.config as SkillAwareConfig).content?.skills !== undefined;
      setStatus(
        hasPolicy
          ? `Loaded active Skills policy ${policy.configRevision}. Save Draft is isolated until History / Publish.`
          : "Active revision predates B06.3 Skills policy; bundled child registry is shown until the first draft is saved.",
        hasPolicy ? "good" : "warn",
      );
    }).catch((error: unknown) => {
      if (generation !== loadGeneration) return;
      serviceReady = false;
      loadedActiveRevision = null;
      revisionBadge.className = "st-admin-status bad";
      revisionBadge.textContent = "ACTIVE · unavailable";
      search.disabled = true;
      categoryFilter.disabled = true;
      save.disabled = true;
      listHost.replaceChildren(notice("The canonical Skill registry could not be loaded. Retry after the local Admin service is available.", "bad"));
      editorHost.replaceChildren(notice("Skill overrides are disabled until the active revision and canonical preview are loaded.", "warn"));
      status.className = "stx-notice bad";
      status.replaceChildren(document.createTextNode(adminErrorMessage(error, "The Skills Admin service is unavailable. Check the local runtime and try again.")), document.createTextNode(" "), button("Retry", load));
    });
  };

  helpScope.observeRoot(page);
  load();
  return page;
}