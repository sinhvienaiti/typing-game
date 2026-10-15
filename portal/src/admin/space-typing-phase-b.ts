import { attachA8WorldStageCapabilitySummary } from "./space-typing-a8-world-stage-capabilities";
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
import { attachProductionPreviewClassification } from "./v2/preview/preview-classification";

const BASE = "/admin/space-typing";
type Navigate = (path: string) => void;

function classified(path: string, screen: HTMLElement | null): HTMLElement | null {
  return screen === null ? null : attachProductionPreviewClassification(screen, path);
}

export function renderPhaseBAdminScreen(path: string, navigate: Navigate): HTMLElement | null {
  if (path === BASE || path === `${BASE}/analytics`) return classified(path, renderPhaseBTelemetry(path));
  if (path === `${BASE}/music-library`) return classified(path, renderPhaseBMusicLibrary());
  if (path === `${BASE}/sfx`) return classified(path, renderPhaseBSfx());
  if (path === `${BASE}/stages`) return classified(path, attachA8WorldStageCapabilitySummary(renderPhaseBWorlds(navigate), "world"));
  if (path === `${BASE}/worlds-stages`) return classified(path, attachA8WorldStageCapabilitySummary(renderPhaseBStages(navigate), "stage"));
  if (path === `${BASE}/typing-content`) return classified(path, renderPhaseBTypingContent(navigate));
  if (path === `${BASE}/shop`) return classified(path, renderPhaseBShop(navigate));
  if (path === `${BASE}/currencies`) return classified(path, renderPhaseBCurrencies(navigate));
  if (path === `${BASE}/rewards`) return classified(path, renderPhaseBRewards(navigate));
  if (path === `${BASE}/warp`) return classified(path, renderPhaseBWarp(navigate));
  if (path === `${BASE}/missions`) return classified(path, renderPhaseBMissions(navigate));
  if (path === `${BASE}/daily-weekly`) return classified(path, renderPhaseBDailyWeekly());
  if (path === `${BASE}/expedition`) return classified(path, renderPhaseBExpedition());
  if (path === `${BASE}/events`) return classified(path, renderPhaseBEvents());
  if (path === `${BASE}/duel`) return classified(path, renderPhaseBDuel());
  if (path === `${BASE}/ranked`) return classified(path, renderPhaseBRanked());
  if (path === `${BASE}/alternative-modes`) return classified(path, renderPhaseBAlternativeModes());
  if (path === `${BASE}/backgrounds`) return classified(path, renderPhaseBBackgrounds());
  if (path === `${BASE}/ui-assets`) return classified(path, renderPhaseBUiAssets());
  if (path === `${BASE}/vfx`) return classified(path, renderPhaseBVfx());
  if (path === `${BASE}/settings`) return classified(path, renderPhaseBSettings(navigate));
  if (path === `${BASE}/qa`) return classified(path, renderPhaseBQa());
  if (path === `${BASE}/feature-gates` || path === `${BASE}/flags`) return classified(path, renderPhaseBFeatureGates());
  return classified(path, renderPhaseBCoreAdminScreen(path, navigate));
}
