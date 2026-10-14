import { renderPhaseBBosses as renderLegacyBosses } from "./space-typing-bosses-phase-b-legacy";
import { createBossProductionPreviewPanel } from "./v2/preview/panels/boss-production-preview";

type Navigate = (path: string) => void;

export function renderPhaseBBosses(navigate: Navigate): HTMLElement {
  const page = renderLegacyBosses(navigate);
  const preview = createBossProductionPreviewPanel();
  const anchor = page.children.item(2);
  page.insertBefore(preview.root, anchor);
  return page;
}
