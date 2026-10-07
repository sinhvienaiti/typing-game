import { renderPhaseBAdminScreen as renderPhaseBCoreAdminScreen } from "./space-typing-phase-b-core";
import { renderPhaseBStages } from "./space-typing-stages-phase-b";

const BASE = "/admin/space-typing";
type Navigate = (path: string) => void;

export function renderPhaseBAdminScreen(path: string, navigate: Navigate): HTMLElement | null {
  if (path === `${BASE}/stages` || path === `${BASE}/worlds-stages`) return renderPhaseBStages(navigate);
  return renderPhaseBCoreAdminScreen(path, navigate);
}
