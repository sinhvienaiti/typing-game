import "../admin-ux-fixes.css";

export type ProductionPreviewClassification =
  | "full-runtime"
  | "production-presentation"
  | "simulation-data"
  | "not-applicable";

type ClassificationDefinition = Readonly<{
  kind: ProductionPreviewClassification;
  label: string;
  detail: string;
}>;

const FULL_RUNTIME: ClassificationDefinition = Object.freeze({
  kind: "full-runtime",
  label: "FULL PRODUCTION RUNTIME PREVIEW",
  detail: "This screen exercises the child production renderer/runtime path in an isolated preview session. Preview state is never persisted.",
});
const PRESENTATION: ClassificationDefinition = Object.freeze({
  kind: "production-presentation",
  label: "PRODUCTION PRESENTATION PREVIEW",
  detail: "This screen previews canonical production presentation/assets, but does not claim to exercise a complete gameplay runtime session.",
});
const SIMULATION: ClassificationDefinition = Object.freeze({
  kind: "simulation-data",
  label: "SIMULATION / DATA PREVIEW",
  detail: "A visual renderer would be misleading here. This screen previews resolved policy, economy, scheduling or rule outcomes through canonical data/runtime logic.",
});
const NOT_APPLICABLE: ClassificationDefinition = Object.freeze({
  kind: "not-applicable",
  label: "NO VISUAL PREVIEW / N/A",
  detail: "This domain has no honest player-facing visual preview. Administrative or diagnostic data is shown without inventing presentation behavior.",
});

const CLASSIFICATIONS: Readonly<Record<string, ClassificationDefinition>> = Object.freeze({
  "/admin/space-typing": SIMULATION,
  "/admin/space-typing/analytics": SIMULATION,
  "/admin/space-typing/audio": SIMULATION,
  "/admin/space-typing/world-music": PRESENTATION,
  "/admin/space-typing/music-library": PRESENTATION,
  "/admin/space-typing/sfx": PRESENTATION,
  "/admin/space-typing/ships": FULL_RUNTIME,
  "/admin/space-typing/equipment": FULL_RUNTIME,
  "/admin/space-typing/skills": FULL_RUNTIME,
  "/admin/space-typing/enemies": FULL_RUNTIME,
  "/admin/space-typing/bosses": FULL_RUNTIME,
  "/admin/space-typing/stages": FULL_RUNTIME,
  "/admin/space-typing/worlds-stages": FULL_RUNTIME,
  "/admin/space-typing/vfx": FULL_RUNTIME,
  "/admin/space-typing/backgrounds": PRESENTATION,
  "/admin/space-typing/ui-assets": PRESENTATION,
  "/admin/space-typing/shop": SIMULATION,
  "/admin/space-typing/currencies": SIMULATION,
  "/admin/space-typing/rewards": SIMULATION,
  "/admin/space-typing/warp": SIMULATION,
  "/admin/space-typing/missions": SIMULATION,
  "/admin/space-typing/daily-weekly": SIMULATION,
  "/admin/space-typing/expedition": SIMULATION,
  "/admin/space-typing/events": SIMULATION,
  "/admin/space-typing/duel": SIMULATION,
  "/admin/space-typing/ranked": SIMULATION,
  "/admin/space-typing/alternative-modes": SIMULATION,
  "/admin/space-typing/settings": SIMULATION,
  "/admin/space-typing/feature-gates": SIMULATION,
  "/admin/space-typing/flags": SIMULATION,
  "/admin/space-typing/typing-content": NOT_APPLICABLE,
  "/admin/space-typing/history": NOT_APPLICABLE,
  "/admin/space-typing/qa": NOT_APPLICABLE,
});

const DRAFT_ACTION_PATHS = new Set([
  "/admin/space-typing/skills",
  "/admin/space-typing/equipment",
]);

function draftSource(grid: HTMLElement): HTMLSelectElement | null {
  for (const select of grid.querySelectorAll<HTMLSelectElement>("select")) {
    if ([...select.options].some((option) => option.value === "draft")) return select;
  }
  return null;
}

function attachDraftPreviewIntent(root: HTMLElement, path: string): void {
  if (!DRAFT_ACTION_PATHS.has(path) || root.dataset["draftPreviewIntent"] === "true") return;
  root.dataset["draftPreviewIntent"] = "true";

  for (const grid of root.querySelectorAll<HTMLElement>(".st-admin-runtime-preview-grid")) {
    const source = draftSource(grid);
    if (source === null) continue;
    const action = [...grid.children].find(
      (node): node is HTMLButtonElement => node instanceof HTMLButtonElement && node.classList.contains("st-admin-btn"),
    );
    if (action === undefined) continue;
    action.dataset["previewDraftAction"] = "true";
    action.textContent = "Preview draft candidate";
    action.title = "Run the current unsaved field values through the isolated production runtime.";
  }

  root.addEventListener("click", (event) => {
    if (!(event.target instanceof Element)) return;
    const action = event.target.closest<HTMLButtonElement>('button[data-preview-draft-action="true"]');
    if (action === null) return;
    const grid = action.closest<HTMLElement>(".st-admin-runtime-preview-grid");
    if (grid === null) return;
    const source = draftSource(grid);
    if (source === null || source.disabled) return;
    source.value = "draft";
  }, { capture: true });
}

export function productionPreviewClassification(path: string): ClassificationDefinition | null {
  return CLASSIFICATIONS[path] ?? null;
}

export function attachProductionPreviewClassification(root: HTMLElement, path: string): HTMLElement {
  const definition = productionPreviewClassification(path);
  if (definition === null || root.dataset["previewClassification"] !== undefined) return root;
  root.dataset["previewClassification"] = definition.kind;
  attachDraftPreviewIntent(root, path);

  const header = root.querySelector<HTMLElement>(".st-admin-page-head, .space-admin-page__header");
  if (header === null) return root;
  let actions = header.querySelector<HTMLElement>(".st-admin-page-actions, .space-admin-page__badges");
  if (actions === null) {
    actions = document.createElement("div");
    actions.className = "st-admin-page-actions";
    header.append(actions);
  }
  const badge = document.createElement("span");
  badge.className = "st-admin-status info";
  badge.textContent = definition.label;
  badge.title = definition.detail;
  badge.setAttribute("aria-label", `${definition.label}. ${definition.detail}`);
  badge.dataset["previewClassification"] = definition.kind;
  actions.prepend(badge);
  return root;
}

export const PRODUCTION_PREVIEW_CLASSIFICATIONS = CLASSIFICATIONS;
