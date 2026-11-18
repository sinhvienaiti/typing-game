import {
  paintedEquipmentIcon,
  paintedSkillIcon,
} from "../../../../../games/space-typing/src/ui/painted-icons";

export type ProductionRegistryIconKind = "skill" | "equipment";

export type ProductionRegistryIconPreview = Readonly<{
  root: HTMLElement;
  show: (id: string, label: string) => void;
}>;

function el<K extends keyof HTMLElementTagNameMap>(tag: K, cls?: string, text?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text !== undefined) node.textContent = text;
  return node;
}

function productionIcon(kind: ProductionRegistryIconKind, id: string): string | null {
  return kind === "skill" ? paintedSkillIcon(id) : paintedEquipmentIcon(id);
}

export function createProductionRegistryIconPreview(kind: ProductionRegistryIconKind): ProductionRegistryIconPreview {
  const root = el("section", "st-admin-runtime-visual");
  const head = el("div", "st-admin-runtime-visual__head");
  const copy = el("div");
  copy.append(
    el("strong", undefined, "Production Visual"),
    el("small", undefined, kind === "skill"
      ? "Canonical painted Skill icon resolved by the child production asset registry."
      : "Canonical painted Equipment icon resolved by the child production asset registry."),
  );
  const badge = el("span", "st-admin-badge", "CHILD ASSET · READ ONLY");
  head.append(copy, badge);

  const frame = el("div", "st-admin-runtime-visual__frame");
  frame.append(el("span", undefined, "Select an item to load its production visual."));
  const meta = el("div", "st-admin-asset-preview-status info", "Waiting for canonical production asset…");
  meta.setAttribute("aria-live", "polite");
  root.append(head, frame, meta);

  const show = (id: string, label: string): void => {
    const url = productionIcon(kind, id);
    if (url === null) {
      frame.replaceChildren(el("span", undefined, `No painted ${kind} icon is bundled for ${id}. Run the child art preparation/build pipeline before testing this visual.`));
      meta.className = "st-admin-asset-preview-status warn";
      meta.textContent = `${label} · ${id} · painted production asset unavailable in this build.`;
      return;
    }
    const image = el("img") as HTMLImageElement;
    image.src = url;
    image.alt = `${label} production ${kind} visual`;
    image.decoding = "async";
    frame.replaceChildren(image);
    meta.className = "st-admin-asset-preview-status good";
    meta.textContent = `${label} · ${id} · canonical child production painted icon.`;
  };

  return Object.freeze({ root, show });
}
