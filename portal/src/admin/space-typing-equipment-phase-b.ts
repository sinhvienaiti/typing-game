import { renderPhaseBEquipment as renderLegacyEquipment } from "./space-typing-equipment-phase-b-legacy";
import { createEquipmentProductionRuntimePanel } from "./v2/preview/panels/equipment-runtime-preview";

type Navigate = (path: string) => void;

export function renderPhaseBEquipment(navigate: Navigate): HTMLElement {
  const page = document.createElement("div");
  page.append(createEquipmentProductionRuntimePanel(), renderLegacyEquipment(navigate));
  return page;
}
