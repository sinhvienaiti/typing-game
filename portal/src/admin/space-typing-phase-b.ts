import { renderPhaseBAdminScreen as renderPhaseBCoreAdminScreen } from "./space-typing-phase-b-core";
import { renderPhaseBAlternativeModes } from "./space-typing-alternative-modes-phase-b";
import { renderPhaseBBackgrounds } from "./space-typing-backgrounds-phase-b";
import { renderPhaseBCurrencies } from "./space-typing-currencies-phase-b";
import { renderPhaseBDuel } from "./space-typing-duel-phase-b";
import { renderPhaseBEvents } from "./space-typing-events-phase-b";
import { renderPhaseBFeatureGates } from "./space-typing-feature-gates-phase-b";
import { renderPhaseBMissions } from "./space-typing-missions-phase-b";
import { renderPhaseBRanked } from "./space-typing-ranked-phase-b";
import { renderPhaseBRewards } from "./space-typing-rewards-phase-b";
import { renderPhaseBShop } from "./space-typing-shop-phase-b";
import { renderPhaseBStages } from "./space-typing-stages-phase-b";
import { renderPhaseBTypingContent } from "./space-typing-typing-content-phase-b";
import { renderPhaseBUiAssets } from "./space-typing-ui-assets-phase-b";
import { renderPhaseBVfx } from "./space-typing-vfx-phase-b";
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
  if (path === `${BASE}/missions`) return renderPhaseBMissions(navigate);
  if (path === `${BASE}/events`) return renderPhaseBEvents();
  if (path === `${BASE}/duel`) return renderPhaseBDuel();
  if (path === `${BASE}/ranked`) return renderPhaseBRanked();
  if (path === `${BASE}/alternative-modes`) return renderPhaseBAlternativeModes();
  if (path === `${BASE}/backgrounds`) return renderPhaseBBackgrounds();
  if (path === `${BASE}/ui-assets`) return renderPhaseBUiAssets();
  if (path === `${BASE}/vfx`) return renderPhaseBVfx();
  if (path === `${BASE}/feature-gates` || path === `${BASE}/flags`) return renderPhaseBFeatureGates();
  return renderPhaseBCoreAdminScreen(path, navigate);
}
