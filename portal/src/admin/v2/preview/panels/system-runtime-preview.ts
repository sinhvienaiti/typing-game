import "../../admin-runtime-preview-fixes.css";
import { SpaceTypingAdminApi } from "../../../api";
import { adminErrorMessage } from "../../../admin-http";

type SkillState = { cooldownRemaining?: number; charges?: number | null; usesThisStage?: number } | null;
type SkillRuntimePreview = {
  engine: "SkillEngine";
  activationReady: boolean;
  blockReason: string | null;
  energyBefore: number;
  energyAfter: number;
  initialState: SkillState;
  activatedState: SkillState;
  recoveredState: SkillState;
};
type SkillItem = {
  id: string;
  name: string;
  category: string;
  energyCost: number;
  cooldown: number;
  charges: number | null;
  runtimePreview: SkillRuntimePreview;
};
type SkillResponse = { protocolVersion: 1; skills: SkillItem[] };

const api = new SpaceTypingAdminApi();
const LIVE_PREVIEW_DELAY_MS = 180;

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

function field(label: string, control: HTMLElement): HTMLElement {
  const root = el("label", "stx-field");
  root.append(el("span", undefined, label), control);
  return root;
}

function status(root: HTMLElement, text: string, tone: "info" | "good" | "warn" | "bad" = "info"): void {
  root.className = `stx-notice ${tone}`;
  root.textContent = text;
}

function stateSummary(state: SkillState): string {
  if (!state) return "Not available";
  const cooldown = Number(state.cooldownRemaining ?? 0).toFixed(2);
  const charges = state.charges == null ? "∞" : String(state.charges);
  const uses = String(state.usesThisStage ?? 0);
  return `cooldown ${cooldown}s · charges ${charges} · stage uses ${uses}`;
}

function skillsPolicy(config: unknown): Record<string, unknown> | undefined {
  if (!config || typeof config !== "object") return undefined;
  const content = (config as { content?: unknown }).content;
  if (!content || typeof content !== "object") return undefined;
  const policy = (content as Record<string, unknown>)["skills"];
  return policy && typeof policy === "object" ? structuredClone(policy as Record<string, unknown>) : undefined;
}

async function previewSkills(policy?: Record<string, unknown>): Promise<SkillResponse> {
  return api.requestJson<SkillResponse>("/api/admin/space-typing/skills/preview", {
    method: "POST",
    body: JSON.stringify(policy ? { policy } : {}),
  });
}

export function createSkillProductionRuntimePanel(): HTMLElement {
  const root = el("section", "st-admin-panel solid stx-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(
    el("h2", undefined, "Live Production Runtime Preview"),
    el("p", undefined, "Exercise activation, energy, cooldown and charge behavior live through the child production SkillEngine."),
  );
  head.append(copy);
  root.append(head);

  const source = el("select", "st-admin-select") as HTMLSelectElement;
  source.append(new Option("Published", "published"), new Option("Draft candidate · live", "draft"));
  const skillSelect = el("select", "st-admin-select") as HTMLSelectElement;
  const energy = el("input") as HTMLInputElement;
  energy.type = "number";
  energy.min = "0";
  energy.max = "200";
  energy.step = "0.1";
  const cooldown = el("input") as HTMLInputElement;
  cooldown.type = "number";
  cooldown.min = "0";
  cooldown.max = "300";
  cooldown.step = "0.1";
  const apply = el("button", "st-admin-btn", "Refresh preview") as HTMLButtonElement;
  apply.type = "button";
  const controls = el("div", "stx-grid st-admin-runtime-preview-grid");
  controls.append(field("Source", source), field("Skill", skillSelect), field("Energy cost", energy), field("Cooldown", cooldown), apply);
  const message = el("div", "stx-notice info", "Loading production Skill runtime…");
  message.setAttribute("aria-live", "polite");
  const result = el("div", "stx-grid");
  root.append(controls, message, result);

  let publishedPolicy: Record<string, unknown> | undefined;
  let published: SkillResponse | null = null;
  let previewGeneration = 0;
  let previewTimer: ReturnType<typeof setTimeout> | null = null;
  let disposed = false;

  const selected = (): SkillItem | undefined => published?.skills.find((item) => item.id === skillSelect.value);

  const render = (item: SkillItem, candidate = false): void => {
    result.replaceChildren();
    const runtime = item.runtimePreview;
    const rows: Array<[string, string]> = [
      ["Skill", `${item.name} · ${item.category}`],
      ["Activation", runtime.activationReady ? "READY" : `BLOCKED · ${runtime.blockReason ?? "unknown reason"}`],
      ["Energy", `${runtime.energyBefore} → ${runtime.energyAfter}`],
      ["Before", stateSummary(runtime.initialState)],
      ["After activation", stateSummary(runtime.activatedState)],
      ["After cooldown", stateSummary(runtime.recoveredState)],
    ];
    for (const [label, value] of rows) {
      const row = el("div", "stx-toggle-row");
      const text = el("div");
      text.append(el("strong", undefined, label), el("small", undefined, value));
      row.append(text);
      result.append(row);
    }
    status(
      message,
      candidate
        ? "Draft candidate executed live through production SkillEngine. Nothing was persisted."
        : "Published definition executed through production SkillEngine.",
      runtime.activationReady ? "good" : "warn",
    );
  };

  const cancelTimer = (): void => {
    if (previewTimer !== null) clearTimeout(previewTimer);
    previewTimer = null;
  };

  const invalidatePendingPreview = (): void => {
    previewGeneration += 1;
    cancelTimer();
    if (source.value === "draft" && published !== null) {
      status(message, "Draft candidate changed · live runtime preview is refreshing…", "info");
    }
  };

  const runDraftPreview = async (): Promise<void> => {
    const item = selected();
    if (!item || source.value !== "draft" || disposed) return;
    const current = ++previewGeneration;
    const itemId = item.id;
    const draft = structuredClone(publishedPolicy ?? { configRevision: "skills-admin-preview", skills: {} }) as Record<string, unknown>;
    draft.configRevision = "skills-admin-preview-draft";
    const overrides = (draft.skills && typeof draft.skills === "object" ? draft.skills : {}) as Record<string, unknown>;
    const existing = (overrides[itemId] && typeof overrides[itemId] === "object" ? overrides[itemId] : {}) as Record<string, unknown>;
    overrides[itemId] = { ...existing, energyCost: Number(energy.value), cooldown: Number(cooldown.value) };
    draft.skills = overrides;
    try {
      status(message, "Running live isolated draft candidate through production SkillEngine…");
      const response = await previewSkills(draft);
      if (current !== previewGeneration) return;
      const candidate = response.skills.find((entry) => entry.id === itemId);
      if (!candidate) throw new Error("Skill candidate was not returned by production preview.");
      render(candidate, true);
    } catch (error) {
      if (current === previewGeneration) status(message, adminErrorMessage(error, "Could not preview Skill candidate."), "bad");
    }
  };

  const scheduleDraftPreview = (delay = LIVE_PREVIEW_DELAY_MS): void => {
    cancelTimer();
    if (source.value !== "draft" || published === null || disposed) return;
    previewTimer = setTimeout(() => {
      previewTimer = null;
      void runDraftPreview();
    }, delay);
  };

  const syncInputs = (previewDraft = true): void => {
    const item = selected();
    if (!item) return;
    energy.value = String(item.energyCost);
    cooldown.value = String(item.cooldown);
    if (source.value === "published") render(item);
    else if (previewDraft) scheduleDraftPreview(0);
  };

  const setControlsDisabled = (disabled: boolean): void => {
    source.disabled = disabled;
    skillSelect.disabled = disabled;
    energy.disabled = disabled;
    cooldown.disabled = disabled;
    apply.disabled = disabled;
  };
  setControlsDisabled(true);

  const load = async (): Promise<void> => {
    try {
      status(message, "Loading production Skill runtime…");
      const runtime = await api.getRuntime();
      const policy = skillsPolicy(runtime.config);
      const response = await previewSkills(policy);
      if (disposed) return;
      publishedPolicy = policy;
      published = response;
      skillSelect.replaceChildren(...response.skills.map((item) => new Option(item.name, item.id)));
      setControlsDisabled(false);
      syncInputs(false);
      const item = selected();
      if (item) render(item);
    } catch (error) {
      if (!disposed) status(message, adminErrorMessage(error, "Could not load Skill runtime preview."), "bad");
    }
  };

  source.addEventListener("change", () => {
    invalidatePendingPreview();
    syncInputs();
  });
  skillSelect.addEventListener("change", () => {
    invalidatePendingPreview();
    syncInputs();
  });
  energy.addEventListener("input", () => {
    invalidatePendingPreview();
    scheduleDraftPreview();
  });
  cooldown.addEventListener("input", () => {
    invalidatePendingPreview();
    scheduleDraftPreview();
  });
  apply.addEventListener("click", () => {
    invalidatePendingPreview();
    if (source.value === "published") {
      const item = selected();
      if (item) render(item);
    } else {
      void runDraftPreview();
    }
  });

  const observer = new MutationObserver(() => {
    if (root.isConnected || disposed) return;
    disposed = true;
    previewGeneration += 1;
    cancelTimer();
    observer.disconnect();
  });
  observer.observe(document.documentElement, { childList: true, subtree: true });

  void load();
  return root;
}
