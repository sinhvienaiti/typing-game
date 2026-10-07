import { renderPhaseBAdminScreen as renderPhaseBCoreAdminScreen } from "./space-typing-phase-b-core";
import { renderPhaseBCurrencies } from "./space-typing-currencies-phase-b";
import { renderPhaseBRewards } from "./space-typing-rewards-phase-b";
import { renderPhaseBShop } from "./space-typing-shop-phase-b";
import { renderPhaseBStages } from "./space-typing-stages-phase-b";
import { renderPhaseBTypingContent } from "./space-typing-typing-content-phase-b";
import { renderPhaseBWarp } from "./space-typing-warp-phase-b";
import { renderPhaseBWorlds } from "./space-typing-worlds-phase-b";

const BASE = "/admin/space-typing";
type Navigate = (path: string) => void;

export function renderPhaseBAdminScreen(path: string, navigate: Navigate): HTMLElement | null {
  if (path === `${BASE}/stages`) return renderPhaseBWorlds(navigate);
  if (path === `${BASE}/worlds-stages`) return renderPhaseBStages(navigate);
  if (path === `${BASE}/typing-content`) return renderPhaseBTypingContent(navigate);
  if (path === `${BASE}/shop`) return renderPhaseBShop(navigate);
  if (path === `${BASE}/currencies`) return renderPhaseBCurrencies(navigate);
  if (path === `${BASE}/rewards`) return renderPhaseBRewards(navigate);
  if (path === `${BASE}/warp`) return renderPhaseBWarp(navigate);
  return renderPhaseBCoreAdminScreen(path, navigate);
}
