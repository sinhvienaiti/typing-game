import { renderPhaseBBosses as renderLegacyBosses } from "./space-typing-bosses-phase-b-legacy";
import { createBossProductionPreviewPanel } from "./v2/preview/panels/boss-production-preview";
import { wireLegacyRegistrySelection } from "./v2/preview/registry-selection-sync";

type Navigate = (path: string) => void;

export function renderPhaseBBosses(navigate: Navigate): HTMLElement {
  const page = renderLegacyBosses(navigate);
  const preview = createBossProductionPreviewPanel();
  wireLegacyRegistrySelection(page, ["View", "Viewing"], preview.selectBoss);
  const anchor = page.children.item(2);
  page.insertBefore(preview.root, anchor);
  return page;
}
