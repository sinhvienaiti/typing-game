import { renderPhaseBEquipment as renderLegacyEquipment } from "./space-typing-equipment-phase-b-legacy";
import { createEquipmentProductionRuntimePanel } from "./v2/preview/panels/equipment-runtime-preview";
import { wireLegacyRegistrySelection } from "./v2/preview/registry-selection-sync";

type Navigate = (path: string) => void;

export function renderPhaseBEquipment(navigate: Navigate): HTMLElement {
  const page = document.createElement("div");
  const preview = createEquipmentProductionRuntimePanel();
  const legacy = renderLegacyEquipment(navigate);
  wireLegacyRegistrySelection(legacy, ["Edit", "Editing"], preview.selectEquipment);
  page.append(preview.root, legacy);
  return page;
}
