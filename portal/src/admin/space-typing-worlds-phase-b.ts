import { renderPhaseBWorlds as renderLegacyWorlds } from "./space-typing-worlds-phase-b-legacy";
import { createWorldProductionPreviewPanel } from "./v2/preview/panels/world-stage-production-preview";

type Navigate = (path: string) => void;

export function renderPhaseBWorlds(navigate: Navigate): HTMLElement {
  const page = renderLegacyWorlds(navigate);
  const preview = createWorldProductionPreviewPanel();
  page.insertBefore(preview.root, page.children.item(2));
  return page;
}
