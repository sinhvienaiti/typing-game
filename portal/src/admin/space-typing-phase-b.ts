import { attachA8WorldStageCapabilitySummary } from "./space-typing-a8-world-stage-capabilities";
import { renderAdminV2Players } from "./v2/players";
import { renderAdminV2LiveopsMail } from "./v2/liveops-mail";
import { renderAdminV2ChatModeration } from "./v2/chat-moderation";
import { renderAdminV2Feedback } from "./v2/feedback";
import { renderPhaseBAdminScreen as renderPhaseBCoreAdminScreen } from "./space-typing-phase-b-core";
import { renderPhaseBAlternativeModes } from "./space-typing-alternative-modes-phase-b";
import { renderPhaseBBackgrounds } from "./space-typing-backgrounds-phase-b";
import { renderPhaseBCurrencies } from "./space-typing-currencies-phase-b";
import { renderPhaseBDailyWeekly } from "./space-typing-daily-weekly-phase-b";
import { renderPhaseBDuel } from "./space-typing-duel-phase-b";
import { renderPhaseBEvents } from "./space-typing-events-phase-b";
import { renderPhaseBExpedition } from "./space-typing-expedition-phase-b";
import { renderPhaseBFeatureGates } from "./space-typing-feature-gates-phase-b";
import { renderPhaseBMissions } from "./space-typing-missions-phase-b";
import { renderPhaseBMusicLibrary } from "./space-typing-music-library-phase-b";
import { renderPhaseBQa } from "./space-typing-qa-phase-b";
import { renderPhaseBRanked } from "./space-typing-ranked-phase-b";
import { renderPhaseBRewards } from "./space-typing-rewards-phase-b";
import { renderPhaseBSettings } from "./space-typing-settings-phase-b";
import { renderPhaseBShop } from "./space-typing-shop-phase-b";
import { renderPhaseBSfx } from "./space-typing-sfx-phase-b";
import { renderPhaseBStages } from "./space-typing-stages-phase-b";
import { renderPhaseBTelemetry } from "./space-typing-telemetry-phase-b";
import { renderPhaseBTypingContent } from "./space-typing-typing-content-phase-b";
import { renderPhaseBUiAssets } from "./space-typing-ui-assets-phase-b";
import { renderPhaseBVfx } from "./space-typing-vfx-phase-b";
import { renderPhaseBWarp } from "./space-typing-warp-phase-b";
import { renderPhaseBWorlds } from "./space-typing-worlds-phase-b";
import { renderAdminV2Roles } from "./v2/roles";
import { attachRoleAwareActionGates } from "./v2/security/permission-gates";
import { attachProductionPreviewClassification } from "./v2/preview/preview-classification";

const BASE = "/admin/space-typing";
type Navigate = (path: string) => void;

function decorated(path: string, screen: HTMLElement | null): HTMLElement | null {
  if (screen === null) return null;
  attachProductionPreviewClassification(screen, path);
  attachRoleAwareActionGates(screen);
  return screen;
}

export function renderPhaseBAdminScreen(path: string, navigate: Navigate): HTMLElement | null {
  if (path === BASE || path === `${BASE}/analytics`) return decorated(path, renderPhaseBTelemetry(path));
  if (path === `${BASE}/music-library`) return decorated(path, renderPhaseBMusicLibrary());
  if (path === `${BASE}/sfx`) return decorated(path, renderPhaseBSfx());
  if (path === `${BASE}/stages`) return decorated(path, attachA8WorldStageCapabilitySummary(renderPhaseBWorlds(navigate), "world"));
  if (path === `${BASE}/worlds-stages`) return decorated(path, attachA8WorldStageCapabilitySummary(renderPhaseBStages(navigate), "stage"));
  if (path === `${BASE}/typing-content`) return decorated(path, renderPhaseBTypingContent(navigate));
  if (path === `${BASE}/shop`) return decorated(path, renderPhaseBShop(navigate));
  if (path === `${BASE}/currencies`) return decorated(path, renderPhaseBCurrencies(navigate));
  if (path === `${BASE}/rewards`) return decorated(path, renderPhaseBRewards(navigate));
  if (path === `${BASE}/warp`) return decorated(path, renderPhaseBWarp(navigate));
  if (path === `${BASE}/missions`) return decorated(path, renderPhaseBMissions(navigate));
  if (path === `${BASE}/daily-weekly`) return decorated(path, renderPhaseBDailyWeekly());
  if (path === `${BASE}/expedition`) return decorated(path, renderPhaseBExpedition());
  if (path === `${BASE}/events`) return decorated(path, renderPhaseBEvents(navigate));
  if (path === `${BASE}/duel`) return decorated(path, renderPhaseBDuel());
  if (path === `${BASE}/ranked`) return decorated(path, renderPhaseBRanked());
  if (path === `${BASE}/alternative-modes`) return decorated(path, renderPhaseBAlternativeModes());
  if (path === `${BASE}/backgrounds`) return decorated(path, renderPhaseBBackgrounds());
  if (path === `${BASE}/ui-assets`) return decorated(path, renderPhaseBUiAssets());
  if (path === `${BASE}/vfx`) return decorated(path, renderPhaseBVfx());
  if (path === `${BASE}/settings`) return decorated(path, renderPhaseBSettings(navigate));
  if (path === `${BASE}/roles`) return decorated(path, renderAdminV2Roles());
  if (path === `${BASE}/qa`) return decorated(path, renderPhaseBQa());
  if (path === `${BASE}/feature-gates` || path === `${BASE}/flags`) return decorated(path, renderPhaseBFeatureGates());
  if (path === `${BASE}/players`) return decorated(path, renderAdminV2Players());
  if (path === `${BASE}/liveops-mail`) return decorated(path, renderAdminV2LiveopsMail());
  if (path === `${BASE}/chat`) return decorated(path, renderAdminV2ChatModeration());
  if (path === `${BASE}/feedback`) return decorated(path, renderAdminV2Feedback());
  return decorated(path, renderPhaseBCoreAdminScreen(path, navigate));
}
