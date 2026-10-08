import { SpaceTypingAdminApi, type SpaceTypingAdminConfig } from "./api";

const api = new SpaceTypingAdminApi();

type StageOverride = {
  stage: number;
  enemyBudget?: number;
  eliteChance?: number;
  modifierSlots?: number;
};

type StagePolicy = {
  configRevision: string;
  stages: StageOverride[];
};

type StagePreviewItem = {
  stage: number;
  galaxy: number;
  stageInGalaxy: number;
  role: string;
  seed: number;
  enemyBudget: number;
  eliteChance: number;
  modifierSlots: number;
  pacingBudget: number;
  overridden: boolean;
};

type StagePreview = {
  protocolVersion: 1;
  configRevision: string;
  authorableFields: ["enemyBudget", "eliteChance", "modifierSlots"];
  stages: StagePreviewItem[];
};

type StageAwareConfig = SpaceTypingAdminConfig & {
  content?: NonNullable<SpaceTypingAdminConfig["content"]> & {
    stages?: StagePolicy;
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

function numberField(label: string, value: number, options: { min?: number; max?: number; step?: number; disabled?: boolean } = {}): { root: HTMLElement; control: HTMLInputElement } {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label));
  const control = el("input") as HTMLInputElement;
  control.type = "number";
  control.value = String(value);
  if (options.min !== undefined) control.min = String(options.min);
  if (options.max !== undefined) control.max = String(options.max);
  if (options.step !== undefined) control.step = String(options.step);
  control.disabled = options.disabled ?? false;
  control.setAttribute("aria-label", label);
  root.append(control);
  return { root, control };
}

function readonlyField(label: string, value: string): HTMLElement {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label));
  const control = el("input") as HTMLInputElement;
  control.type = "text";
  control.value = value;
  control.disabled = true;
  root.append(control);
  return root;
}

function grid(...children: HTMLElement[]): HTMLElement {
  const root = el("div", "stx-grid");
  root.append(...children);
  return root;
}

function policyFrom(config: SpaceTypingAdminConfig): StagePolicy {
  return structuredClone((config as StageAwareConfig).content?.stages ?? {
    configRevision: "stages-admin-v1",
    stages: [],
  });
}

function overrideFor(policy: StagePolicy, stage: number): StageOverride | undefined {
  return policy.stages.find((entry) => entry.stage === stage);
}

function setOverride(policy: StagePolicy, stage: number, override: Omit<StageOverride, "stage">): void {
  const index = policy.stages.findIndex((entry) => entry.stage === stage);
  const next = { stage, ...override };
  if (index >= 0) policy.stages[index] = next;
  else policy.stages.push(next);
  policy.stages.sort((left, right) => left.stage - right.stage);
}

function removeOverride(policy: StagePolicy, stage: number): void {
  policy.stages = policy.stages.filter((entry) => entry.stage !== stage);
}

async function previewStages(policy?: StagePolicy): Promise<StagePreview> {
  const response = await fetch("/api/admin/space-typing/stages/preview", {
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
        : `Stages preview failed (${response.status})`;
    throw new Error(message);
  }
  return payload as unknown as StagePreview;
}

export function renderPhaseBStages(navigate: Navigate): HTMLElement {
  const page = el("div");
  const revisionBadge = badge("ACTIVE · loading", "info");
  const dirtyBadge = badge("CLEAN", "good");
  const validationBadge = badge("NOT VALIDATED", "info");
  const header = el("header", "st-admin-page-head");
  const copy = el("div", "st-admin-page-head-copy");
  copy.append(
    el("div", "st-admin-eyebrow", "Game Content · Campaign Runtime · B06.6"),
    el("h1", undefined, "Worlds & Stages"),
    el("p", undefined, "Revision-backed Stage runtime overrides for the 1000-stage campaign. B06.6 currently exposes only gameplay-backed enemy budget, elite chance and modifier slots; structural campaign identity remains child-runtime owned."),
  );
  const headerActions = el("div", "st-admin-page-actions");
  headerActions.append(dirtyBadge, validationBadge, revisionBadge, button("History / Publish", () => navigate("/admin/space-typing/history")));
  header.append(copy, headerActions);
  page.append(header);

  const status = notice("Loading active revision and bundled Stage runtime preview…", "info");
  page.append(status);

  const navigator = panel("Stage Navigator", "1000 stages · 50 worlds · 10 galaxies · 20 stages per world");
  const stageInput = numberField("Stage", 1, { min: 1, max: 1000, step: 1 });
  const navActions = el("div", "st-admin-page-actions");
  navActions.append(
    button("← Previous", () => selectStage(selectedStage - 1)),
    button("Next →", () => selectStage(selectedStage + 1)),
  );
  navigator.append(grid(stageInput.root, readonlyField("World", "loading")), navActions);
  page.append(navigator);

  const editorShell = el("div", "stx-grid");
  const editor = panel("Stage Runtime Override", "Only fields with verified gameplay consumers are writable");
  const editorHost = el("div");
  editor.append(editorHost);
  const diff = panel("Bundled → Draft Runtime Diff", "Pacing proof is produced by the pinned child command");
  const diffHost = el("div");
  diff.append(diffHost);
  editorShell.append(editor, diff);
  page.append(editorShell);

  let loadedActiveRevision: string | null = null;
  let selectedStage = 1;
  let bundled: StagePreview | null = null;
  let validatedPreview: StagePreview | null = null;
  let policy: StagePolicy = { configRevision: "stages-admin-v1", stages: [] };
  let baselinePolicy = JSON.stringify(policy);
  let validatedPolicy: string | null = null;

  const setStatus = (text: string, tone: Tone = "info"): void => {
    status.className = `stx-notice ${tone}`;
    status.textContent = text;
  };

  const currentBundled = (): StagePreviewItem | undefined => bundled?.stages.find((entry) => entry.stage === selectedStage);
  const currentEffective = (): StagePreviewItem | undefined => {
    const previewed = validatedPreview?.stages.find((entry) => entry.stage === selectedStage);
    if (previewed && validatedPolicy === JSON.stringify(policy)) return previewed;
    const base = currentBundled();
    if (!base) return undefined;
    const override = overrideFor(policy, selectedStage);
    return {
      ...base,
      enemyBudget: override?.enemyBudget ?? base.enemyBudget,
      eliteChance: override?.eliteChance ?? base.eliteChance,
      modifierSlots: override?.modifierSlots ?? base.modifierSlots,
      pacingBudget: override?.enemyBudget ?? base.pacingBudget,
      overridden: override !== undefined,
    };
  };

  const refreshBadges = (): void => {
    const dirty = JSON.stringify(policy) !== baselinePolicy;
    dirtyBadge.textContent = dirty ? "DIRTY" : "CLEAN";
    dirtyBadge.className = `st-admin-status ${dirty ? "warn" : "good"}`;
    const valid = validatedPolicy === JSON.stringify(policy);
    validationBadge.textContent = valid ? "PREVIEW VALID" : "NOT VALIDATED";
    validationBadge.className = `st-admin-status ${valid ? "good" : "info"}`;
  };

  const renderDiff = (): void => {
    diffHost.replaceChildren();
    const base = currentBundled();
    const effective = currentEffective();
    if (!base || !effective) {
      diffHost.append(notice("Stage preview is still loading.", "info"));
      return;
    }
    for (const [label, before, after] of [
      ["Enemy Budget", base.enemyBudget, effective.enemyBudget],
      ["Elite Chance", base.eliteChance, effective.eliteChance],
      ["Modifier Slots", base.modifierSlots, effective.modifierSlots],
      ["Pacing Budget", base.pacingBudget, effective.pacingBudget],
    ] as const) {
      const row = el("div", "stx-toggle-row");
      const copyNode = el("div");
      copyNode.append(el("strong", undefined, label), el("small", undefined, `${before} → ${after}`));
      row.append(copyNode, badge(before === after ? "UNCHANGED" : "CHANGED", before === after ? "info" : "warn"));
      diffHost.append(row);
    }
    diffHost.append(notice("Publish is applied at the new-session boundary. Draft/preview never mutates a running gameplay session.", "info"));
  };

  const renderEditor = (): void => {
    editorHost.replaceChildren();
    const base = currentBundled();
    const effective = currentEffective();
    if (!base || !effective) {
      editorHost.append(notice("Canonical child Stage registry has not finished loading.", "warn"));
      renderDiff();
      return;
    }
    const world = Math.ceil(selectedStage / 20);
    editorHost.append(
      notice(`Stage ${selectedStage} · World ${world} · Galaxy ${base.galaxy} · ${base.role} · seed ${base.seed}`, "info"),
      notice("Stage number, Galaxy, stage-in-Galaxy, role and seed are immutable in this slice. World registry authoring remains the next B06.6 vertical slice.", "warn"),
    );

    const structural = panel("Structural Identity", "Read-only child runtime invariants");
    structural.append(grid(
      readonlyField("Stage", String(base.stage)),
      readonlyField("World", String(world)),
      readonlyField("Galaxy", String(base.galaxy)),
      readonlyField("Stage in Galaxy", String(base.stageInGalaxy)),
      readonlyField("Role", base.role),
      readonlyField("Seed", String(base.seed)),
    ));

    const gameplay = panel("Gameplay-backed Overrides", "Server + child validation enforce safe ranges");
    const enemyBudget = numberField("Enemy Budget", effective.enemyBudget, { min: 0.000001, step: 1 });
    const eliteChance = numberField("Elite Chance", effective.eliteChance, { min: 0, max: 1, step: 0.01 });
    const modifierSlots = numberField("Modifier Slots", effective.modifierSlots, { min: 0, max: 4, step: 1 });
    const applyInputs = (): void => {
      setOverride(policy, selectedStage, {
        enemyBudget: Number(enemyBudget.control.value),
        eliteChance: Number(eliteChance.control.value),
        modifierSlots: Number(modifierSlots.control.value),
      });
      validatedPolicy = null;
      validatedPreview = null;
      refreshBadges();
      renderDiff();
    };
    enemyBudget.control.addEventListener("input", applyInputs);
    eliteChance.control.addEventListener("input", applyInputs);
    modifierSlots.control.addEventListener("input", applyInputs);
    gameplay.append(grid(enemyBudget.root, eliteChance.root, modifierSlots.root));

    const actions = el("div", "st-admin-page-actions");
    actions.append(
      button("Remove Stage Override", () => {
        removeOverride(policy, selectedStage);
        validatedPolicy = null;
        validatedPreview = null;
        refreshBadges();
        renderEditor();
        setStatus(`Stage ${selectedStage} will fall back to bundled runtime values after this draft is published.`, "good");
      }),
      button("Validate Preview", () => {
        setStatus("Running canonical child Stage preview…", "info");
        void previewStages(policy).then((preview) => {
          validatedPreview = preview;
          validatedPolicy = JSON.stringify(policy);
          refreshBadges();
          renderEditor();
          setStatus(`Child preview accepted ${preview.stages.length} stages for ${preview.configRevision}.`, "good");
        }).catch((error: unknown) => {
          validatedPolicy = null;
          refreshBadges();
          setStatus(`Preview rejected: ${error instanceof Error ? error.message : String(error)}`, "bad");
        });
      }, "st-admin-btn primary"),
    );
    editorHost.append(structural, gameplay, actions);
    renderDiff();
  };

  function selectStage(stage: number): void {
    selectedStage = Math.min(1000, Math.max(1, Math.trunc(stage || 1)));
    stageInput.control.value = String(selectedStage);
    const worldControl = navigator.querySelectorAll<HTMLInputElement>("input")[1];
    if (worldControl) worldControl.value = String(Math.ceil(selectedStage / 20));
    renderEditor();
  }

  stageInput.control.addEventListener("change", () => selectStage(Number(stageInput.control.value)));

  void Promise.all([api.getState(), previewStages()]).then(async ([statePayload, bundledPreview]) => {
    loadedActiveRevision = statePayload.state.activeRevision;
    revisionBadge.textContent = `ACTIVE · ${statePayload.state.activeRevision}`;
    bundled = bundledPreview;
    policy = policyFrom(statePayload.active.config);
    baselinePolicy = JSON.stringify(policy);
    validatedPreview = await previewStages(policy);
    validatedPolicy = JSON.stringify(policy);
    selectStage(policy.stages[0]?.stage ?? 1);
    refreshBadges();
    const hasPolicy = (statePayload.active.config as StageAwareConfig).content?.stages !== undefined;
    setStatus(
      hasPolicy
        ? `Loaded active Stage policy ${policy.configRevision}. ${policy.stages.length} explicit override(s); Save Draft remains isolated until History / Publish.`
        : "Active revision predates B06.6 Stage policy. Bundled child values are the fallback until the first Stage draft is saved.",
      hasPolicy ? "good" : "warn",
    );
  }).catch((error: unknown) => setStatus(`Stages Admin unavailable: ${error instanceof Error ? error.message : String(error)}`, "bad"));

  const saveBar = el("div", "st-admin-sticky-save stx-savebar");
  const saveStatus = el("span", undefined, "Revision-backed · runtime unchanged until Publish");
  const save = button("Save Draft", () => {
    void (async () => {
      save.disabled = true;
      saveStatus.textContent = "Validating canonical child preview…";
      try {
        const preview = await previewStages(policy);
        validatedPreview = preview;
        validatedPolicy = JSON.stringify(policy);
        const payload = await api.getState();
        if (loadedActiveRevision === null || payload.state.activeRevision !== loadedActiveRevision) {
          throw new Error(`Active revision changed from ${loadedActiveRevision ?? "loading"} to ${payload.state.activeRevision}. Reload before saving.`);
        }
        const config = structuredClone(payload.active.config);
        const editable = config as StageAwareConfig;
        editable.content ??= {};
        editable.content.stages = structuredClone(policy);
        const revision = await api.createRevision({
          baseRevision: payload.active.revision,
          config,
          message: `B06.6 Stage policy draft · ${policy.stages.length} override(s)`,
        });
        baselinePolicy = JSON.stringify(policy);
        refreshBadges();
        saveStatus.textContent = `Draft saved · ${revision.revision} · runtime unchanged`;
        setStatus(`Draft ${revision.revision} created. Review and Publish from History to activate it for new sessions.`, "good");
      } catch (error: unknown) {
        const message = error instanceof Error ? error.message : String(error);
        saveStatus.textContent = `Draft rejected · ${message}`;
        setStatus(`Validation/save failed: ${message}`, "bad");
      } finally {
        save.disabled = false;
      }
    })();
  }, "st-admin-btn primary");
  saveBar.append(el("strong", undefined, "B06.6 Stage Draft"), saveStatus, el("div", "grow"), button("Discard", () => navigate(location.pathname)), button("History / Publish", () => navigate("/admin/space-typing/history")), save);
  page.append(saveBar);
  return page;
}
