import { renderPhaseBVfx as renderLegacyPhaseBVfx } from "./space-typing-vfx-phase-b-legacy";
import { createCombatVfxProductionPreviewPanel } from "./v2/preview/panels/combat-vfx-production-preview";

export function renderPhaseBVfx(): HTMLElement {
  const page = renderLegacyPhaseBVfx();
  const preview = createCombatVfxProductionPreviewPanel();
  const header = page.querySelector(".st-admin-page-head");
  if (header !== null) header.insertAdjacentElement("afterend", preview.root);
  else page.prepend(preview.root);
  return page;
}
