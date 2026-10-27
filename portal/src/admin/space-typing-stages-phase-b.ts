import { renderPhaseBStages as renderLegacyStages } from "./space-typing-stages-phase-b-legacy";
import { createStageProductionPreviewPanel } from "./v2/preview/panels/world-stage-production-preview";

type Navigate = (path: string) => void;

export function renderPhaseBStages(navigate: Navigate): HTMLElement {
  const page = renderLegacyStages(navigate);
  const preview = createStageProductionPreviewPanel();
  page.insertBefore(preview.root, page.children.item(2));
  return page;
}
