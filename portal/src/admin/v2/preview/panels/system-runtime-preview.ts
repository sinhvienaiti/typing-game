import { SpaceTypingAdminApi } from "../../../api";
import { adminErrorMessage } from "../../../admin-http";

type RuntimeKind = "skills" | "equipment";
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
type EquipmentRuntimePreview = {
  resolver: "resolveEquipmentPerks";
  stats: Record<string, number>;
  perkId: string | null;
  perkName: string | null;
  perkDescription: string | null;
  perkEffects: Record<string, number | boolean>;
};
type EquipmentItem = {
  id: string;
  name: string;
  slot: string;
  tier: number;
  stats: Record<string, number>;
  perk?: string | null;
  runtimePreview: EquipmentRuntimePreview;
};

type SkillResponse = { protocolVersion: 1; skills: SkillItem[] };
type EquipmentResponse = { protocolVersion: 1; equipment: EquipmentItem[] };

const api = new SpaceTypingAdminApi();
const CORE_STATS = ["hull", "shield", "firepower", "armor", "energy", "reactor", "focus", "ward", "luck", "salvage"] as const;

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

function objectPolicy(config: unknown, key: RuntimeKind): Record<string, unknown> | undefined {
  if (!config || typeof config !== "object") return undefined;
  const content = (config as { content?: unknown }).content;
  if (!content || typeof content !== "object") return undefined;
  const policy = (content as Record<string, unknown>)[key];
  return policy && typeof policy === "object" ? structuredClone(policy as Record<string, unknown>) : undefined;
}

async function previewSkills(policy?: Record<string, unknown>): Promise<SkillResponse> {
  return api.requestJson<SkillResponse>("/api/admin/space-typing/skills/preview", {
    method: "POST",
    body: JSON.stringify(policy ? { policy } : {}),
  });
}

async function previewEquipment(policy?: Record<string, unknown>): Promise<EquipmentResponse> {
  return api.requestJson<EquipmentResponse>("/api/admin/space-typing/equipment/preview", {
    method: "POST",
    body: JSON.stringify(policy ? { policy } : {}),
  });
}

export function createSkillProductionRuntimePanel(): HTMLElement {
  const root = el("section", "st-admin-panel solid stx-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(el("h2", undefined, "Production Runtime Preview"), el("p", undefined, "Exercise activation, energy, cooldown and charge behavior through the child SkillEngine."));
  head.append(copy);
  root.append(head);

  const source = el("select", "st-admin-select") as HTMLSelectElement;
  source.append(new Option("Published", "published"), new Option("Draft candidate", "draft"));
  const skillSelect = el("select", "st-admin-select") as HTMLSelectElement;
  const energy = el("input") as HTMLInputElement;
  energy.type = "number"; energy.min = "0"; energy.max = "200"; energy.step = "0.1";
  const cooldown = el("input") as HTMLInputElement;
  cooldown.type = "number"; cooldown.min = "0"; cooldown.max = "300"; cooldown.step = "0.1";
  const apply = el("button", "st-admin-btn", "Preview candidate") as HTMLButtonElement;
  apply.type = "button";
  const controls = el("div", "stx-grid");
  controls.append(field("Source", source), field("Skill", skillSelect), field("Energy cost", energy), field("Cooldown", cooldown), apply);
  const message = el("div", "stx-notice info", "Loading production Skill runtime…");
  const result = el("div", "stx-grid");
  root.append(controls, message, result);

  let publishedPolicy: Record<string, unknown> | undefined;
  let published: SkillResponse | null = null;
  let generation = 0;

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
      const text = el("div"); text.append(el("strong", undefined, label), el("small", undefined, value));
      row.append(text); result.append(row);
    }
    status(message, candidate ? "Draft candidate executed through production SkillEngine. Nothing was persisted." : "Published definition executed through production SkillEngine.", runtime.activationReady ? "good" : "warn");
  };

  const syncInputs = (): void => {
    const item = selected();
    if (!item) return;
    energy.value = String(item.energyCost);
    cooldown.value = String(item.cooldown);
    if (source.value === "published") render(item);
  };

  const load = async (): Promise<void> => {
    const current = ++generation;
    try {
      status(message, "Loading production Skill runtime…");
      const runtime = await api.getRuntime();
      const policy = objectPolicy(runtime.config, "skills");
      const response = await previewSkills(policy);
      if (current !== generation) return;
      publishedPolicy = policy;
      published = response;
      skillSelect.replaceChildren(...response.skills.map((item) => new Option(item.name, item.id)));
      syncInputs();
    } catch (error) {
      if (current === generation) status(message, adminErrorMessage(error, "Could not load Skill runtime preview."), "bad");
    }
  };

  source.addEventListener("change", syncInputs);
  skillSelect.addEventListener("change", syncInputs);
  apply.addEventListener("click", () => {
    void (async () => {
      const item = selected();
      if (!item) return;
      if (source.value === "published") { render(item); return; }
      const draft = structuredClone(publishedPolicy ?? { configRevision: "skills-admin-preview", skills: {} }) as Record<string, unknown>;
      draft.configRevision = "skills-admin-preview-draft";
      const overrides = (draft.skills && typeof draft.skills === "object" ? draft.skills : {}) as Record<string, unknown>;
      const existing = (overrides[item.id] && typeof overrides[item.id] === "object" ? overrides[item.id] : {}) as Record<string, unknown>;
      overrides[item.id] = { ...existing, energyCost: Number(energy.value), cooldown: Number(cooldown.value) };
      draft.skills = overrides;
      try {
        status(message, "Running isolated draft candidate through SkillEngine…");
        const response = await previewSkills(draft);
        const candidate = response.skills.find((entry) => entry.id === item.id);
        if (!candidate) throw new Error("Skill candidate was not returned by production preview.");
        render(candidate, true);
      } catch (error) {
        status(message, adminErrorMessage(error, "Could not preview Skill candidate."), "bad");
      }
    })();
  });
  void load();
  return root;
}

export function createEquipmentProductionRuntimePanel(): HTMLElement {
  const root = el("section", "st-admin-panel solid stx-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(el("h2", undefined, "Production Runtime Preview"), el("p", undefined, "Resolve effective stats and perk behavior through the same equipment resolver gameplay uses."));
  head.append(copy); root.append(head);

  const source = el("select", "st-admin-select") as HTMLSelectElement;
  source.append(new Option("Published", "published"), new Option("Draft candidate", "draft"));
  const equipmentSelect = el("select", "st-admin-select") as HTMLSelectElement;
  const statSelect = el("select", "st-admin-select") as HTMLSelectElement;
  statSelect.append(...CORE_STATS.map((key) => new Option(key.replace(/(^|-)\w/g, (m) => m.toUpperCase()), key)));
  const statValue = el("input") as HTMLInputElement;
  statValue.type = "number"; statValue.min = "-100"; statValue.max = "100"; statValue.step = "0.1";
  const perkSelect = el("select", "st-admin-select") as HTMLSelectElement;
  const apply = el("button", "st-admin-btn", "Preview candidate") as HTMLButtonElement; apply.type = "button";
  const controls = el("div", "stx-grid");
  controls.append(field("Source", source), field("Equipment", equipmentSelect), field("Stat", statSelect), field("Value", statValue), field("Perk", perkSelect), apply);
  const message = el("div", "stx-notice info", "Loading production Equipment runtime…");
  const result = el("div", "stx-grid");
  root.append(controls, message, result);

  let publishedPolicy: Record<string, unknown> | undefined;
  let published: EquipmentResponse | null = null;
  let perkOptions: Array<{ id: string; label: string }> = [];
  let generation = 0;
  const selected = (): EquipmentItem | undefined => published?.equipment.find((item) => item.id === equipmentSelect.value);

  const render = (item: EquipmentItem, candidate = false): void => {
    result.replaceChildren();
    const runtime = item.runtimePreview;
    const enabledEffects = Object.entries(runtime.perkEffects).filter(([, value]) => value === true || (typeof value === "number" && value !== 0 && value !== 1));
    const rows: Array<[string, string]> = [
      ["Equipment", `${item.name} · ${item.slot} · Mk.${item.tier}`],
      ["Effective stats", Object.entries(runtime.stats).filter(([, value]) => value !== 0).map(([key, value]) => `${key} ${value >= 0 ? "+" : ""}${value}`).join(" · ") || "No stat bonus"],
      ["Perk", runtime.perkName ?? "No perk"],
      ["Perk behavior", runtime.perkDescription ?? "No production perk behavior"],
      ["Resolved effects", enabledEffects.map(([key, value]) => `${key}: ${String(value)}`).join(" · ") || "No active perk effects"],
    ];
    for (const [label, value] of rows) {
      const row = el("div", "stx-toggle-row");
      const text = el("div"); text.append(el("strong", undefined, label), el("small", undefined, value));
      row.append(text); result.append(row);
    }
    status(message, candidate ? "Draft candidate resolved through production equipment perks. Nothing was persisted." : "Published equipment resolved through production gameplay logic.", "good");
  };

  const syncInputs = (): void => {
    const item = selected();
    if (!item) return;
    statValue.value = String(item.stats[statSelect.value] ?? 0);
    perkSelect.value = item.runtimePreview.perkId ?? "";
    if (source.value === "published") render(item);
  };

  const load = async (): Promise<void> => {
    const current = ++generation;
    try {
      status(message, "Loading production Equipment runtime…");
      const runtime = await api.getRuntime();
      const policy = objectPolicy(runtime.config, "equipment");
      const response = await previewEquipment(policy);
      if (current !== generation) return;
      publishedPolicy = policy;
      published = response;
      equipmentSelect.replaceChildren(...response.equipment.map((item) => new Option(item.name, item.id)));
      const unique = new Map<string, string>();
      for (const item of response.equipment) if (item.runtimePreview.perkId) unique.set(item.runtimePreview.perkId, item.runtimePreview.perkName ?? item.runtimePreview.perkId);
      perkOptions = [...unique.entries()].map(([id, label]) => ({ id, label })).sort((a, b) => a.label.localeCompare(b.label));
      perkSelect.replaceChildren(new Option("No perk", ""), ...perkOptions.map((entry) => new Option(entry.label, entry.id)));
      syncInputs();
    } catch (error) {
      if (current === generation) status(message, adminErrorMessage(error, "Could not load Equipment runtime preview."), "bad");
    }
  };

  source.addEventListener("change", syncInputs);
  equipmentSelect.addEventListener("change", syncInputs);
  statSelect.addEventListener("change", syncInputs);
  apply.addEventListener("click", () => {
    void (async () => {
      const item = selected();
      if (!item) return;
      if (source.value === "published") { render(item); return; }
      const draft = structuredClone(publishedPolicy ?? { configRevision: "equipment-admin-preview", equipment: {} }) as Record<string, unknown>;
      draft.configRevision = "equipment-admin-preview-draft";
      const overrides = (draft.equipment && typeof draft.equipment === "object" ? draft.equipment : {}) as Record<string, unknown>;
      const existing = (overrides[item.id] && typeof overrides[item.id] === "object" ? overrides[item.id] : {}) as Record<string, unknown>;
      const stats = (existing.stats && typeof existing.stats === "object" ? existing.stats : {}) as Record<string, unknown>;
      overrides[item.id] = { ...existing, stats: { ...stats, [statSelect.value]: Number(statValue.value) }, perk: perkSelect.value || null };
      draft.equipment = overrides;
      try {
        status(message, "Resolving isolated draft candidate through production equipment logic…");
        const response = await previewEquipment(draft);
        const candidate = response.equipment.find((entry) => entry.id === item.id);
        if (!candidate) throw new Error("Equipment candidate was not returned by production preview.");
        render(candidate, true);
      } catch (error) {
        status(message, adminErrorMessage(error, "Could not preview Equipment candidate."), "bad");
      }
    })();
  });
  void load();
  return root;
}
