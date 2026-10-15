import { SpaceTypingAdminApi } from "../../../api";
import { adminErrorMessage } from "../../../admin-http";

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
type EquipmentResponse = { protocolVersion: 1; equipment: EquipmentItem[] };

const api = new SpaceTypingAdminApi();
const CORE_STATS = ["hull", "shield", "firepower", "armor", "energy", "reactor", "focus", "ward", "luck", "salvage"] as const;
const MULTIPLIER_EFFECTS = new Set(["skillCostMultiplier", "cooldownRate", "hostileShotSpeed", "rageGainMultiplier"]);

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
function objectPolicy(config: unknown): Record<string, unknown> | undefined {
  if (!config || typeof config !== "object") return undefined;
  const content = (config as { content?: unknown }).content;
  if (!content || typeof content !== "object") return undefined;
  const policy = (content as Record<string, unknown>)["equipment"];
  return policy && typeof policy === "object" ? structuredClone(policy as Record<string, unknown>) : undefined;
}
async function previewEquipment(policy?: Record<string, unknown>): Promise<EquipmentResponse> {
  return api.requestJson<EquipmentResponse>("/api/admin/space-typing/equipment/preview", {
    method: "POST",
    body: JSON.stringify(policy ? { policy } : {}),
  });
}
function activePerkEffects(effects: Record<string, number | boolean>): Array<[string, number | boolean]> {
  return Object.entries(effects).filter(([key, value]) => {
    if (value === true) return true;
    if (typeof value !== "number") return false;
    return MULTIPLIER_EFFECTS.has(key) ? value !== 1 : value !== 0;
  });
}

export function createEquipmentProductionRuntimePanel(): HTMLElement {
  const root = el("section", "st-admin-panel solid stx-panel");
  const head = el("div", "st-admin-panel-head");
  const copy = el("div");
  copy.append(
    el("h2", undefined, "Production Runtime Preview"),
    el("p", undefined, "Resolve effective stats and perk behavior through the same equipment resolver gameplay uses."),
  );
  head.append(copy);
  root.append(head);

  const source = el("select", "st-admin-select") as HTMLSelectElement;
  source.append(new Option("Published", "published"), new Option("Draft candidate", "draft"));
  const equipmentSelect = el("select", "st-admin-select") as HTMLSelectElement;
  const statSelect = el("select", "st-admin-select") as HTMLSelectElement;
  statSelect.append(...CORE_STATS.map((key) => new Option(key.replace(/(^|-)\w/g, (match) => match.toUpperCase()), key)));
  const statValue = el("input") as HTMLInputElement;
  statValue.type = "number";
  statValue.min = "-100";
  statValue.max = "100";
  statValue.step = "0.1";
  const perkSelect = el("select", "st-admin-select") as HTMLSelectElement;
  const apply = el("button", "st-admin-btn", "Preview candidate") as HTMLButtonElement;
  apply.type = "button";
  const controls = el("div", "stx-grid");
  controls.append(field("Source", source), field("Equipment", equipmentSelect), field("Stat", statSelect), field("Value", statValue), field("Perk", perkSelect), apply);
  const message = el("div", "stx-notice info", "Loading production Equipment runtime…");
  const result = el("div", "stx-grid");
  root.append(controls, message, result);

  let publishedPolicy: Record<string, unknown> | undefined;
  let published: EquipmentResponse | null = null;
  let previewGeneration = 0;
  const selected = (): EquipmentItem | undefined => published?.equipment.find((item) => item.id === equipmentSelect.value);

  const render = (item: EquipmentItem, candidate = false): void => {
    result.replaceChildren();
    const runtime = item.runtimePreview;
    const enabledEffects = activePerkEffects(runtime.perkEffects);
    const rows: Array<[string, string]> = [
      ["Equipment", `${item.name} · ${item.slot} · Mk.${item.tier}`],
      ["Effective stats", Object.entries(runtime.stats).filter(([, value]) => value !== 0).map(([key, value]) => `${key} ${value >= 0 ? "+" : ""}${value}`).join(" · ") || "No stat bonus"],
      ["Perk", runtime.perkName ?? "No perk"],
      ["Perk behavior", runtime.perkDescription ?? "No production perk behavior"],
      ["Resolved effects", enabledEffects.map(([key, value]) => `${key}: ${String(value)}`).join(" · ") || "No active perk effects"],
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
      candidate ? "Draft candidate resolved through production equipment perks. Nothing was persisted." : "Published equipment resolved through production gameplay logic.",
      "good",
    );
  };

  const syncInputs = (): void => {
    const item = selected();
    if (!item) return;
    statValue.value = String(item.stats[statSelect.value] ?? 0);
    perkSelect.value = item.runtimePreview.perkId ?? "";
    if (source.value === "published") render(item);
  };

  const invalidatePendingPreview = (): void => {
    previewGeneration += 1;
  };

  const load = async (): Promise<void> => {
    try {
      status(message, "Loading production Equipment runtime…");
      const runtime = await api.getRuntime();
      const policy = objectPolicy(runtime.config);
      const response = await previewEquipment(policy);
      publishedPolicy = policy;
      published = response;
      equipmentSelect.replaceChildren(...response.equipment.map((item) => new Option(item.name, item.id)));
      const unique = new Map<string, string>();
      for (const item of response.equipment) {
        if (item.runtimePreview.perkId) unique.set(item.runtimePreview.perkId, item.runtimePreview.perkName ?? item.runtimePreview.perkId);
      }
      perkSelect.replaceChildren(
        new Option("No perk", ""),
        ...[...unique.entries()].sort((a, b) => a[1].localeCompare(b[1])).map(([id, label]) => new Option(label, id)),
      );
      syncInputs();
    } catch (error) {
      status(message, adminErrorMessage(error, "Could not load Equipment runtime preview."), "bad");
    }
  };

  source.addEventListener("change", () => {
    invalidatePendingPreview();
    syncInputs();
  });
  equipmentSelect.addEventListener("change", () => {
    invalidatePendingPreview();
    syncInputs();
  });
  statSelect.addEventListener("change", () => {
    invalidatePendingPreview();
    syncInputs();
  });
  statValue.addEventListener("input", invalidatePendingPreview);
  perkSelect.addEventListener("change", invalidatePendingPreview);
  apply.addEventListener("click", () => {
    void (async () => {
      const item = selected();
      if (!item) return;
      if (source.value === "published") {
        invalidatePendingPreview();
        render(item);
        return;
      }
      const current = ++previewGeneration;
      const itemId = item.id;
      const draft = structuredClone(publishedPolicy ?? { configRevision: "equipment-admin-preview", equipment: {} }) as Record<string, unknown>;
      draft["configRevision"] = "equipment-admin-preview-draft";
      const overrides = (draft["equipment"] && typeof draft["equipment"] === "object" ? draft["equipment"] : {}) as Record<string, unknown>;
      const currentOverride = (overrides[itemId] && typeof overrides[itemId] === "object" ? overrides[itemId] : {}) as Record<string, unknown>;
      const stats = (currentOverride["stats"] && typeof currentOverride["stats"] === "object" ? currentOverride["stats"] : {}) as Record<string, unknown>;
      overrides[itemId] = {
        ...currentOverride,
        stats: { ...stats, [statSelect.value]: Number(statValue.value) },
        perk: perkSelect.value || null,
      };
      draft["equipment"] = overrides;
      try {
        status(message, "Resolving isolated draft candidate through production equipment logic…");
        const response = await previewEquipment(draft);
        if (current !== previewGeneration) return;
        const candidate = response.equipment.find((entry) => entry.id === itemId);
        if (!candidate) throw new Error("Equipment candidate was not returned by production preview.");
        render(candidate, true);
      } catch (error) {
        if (current === previewGeneration) status(message, adminErrorMessage(error, "Could not preview Equipment candidate."), "bad");
      }
    })();
  });

  void load();
  return root;
}
