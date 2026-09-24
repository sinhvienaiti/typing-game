import type { LearningProfile } from "../../../shared/learning/core.mjs";
import { BrowserLearningProfileStore } from "../../../shared/learning/browser-store.mjs";
import {
  buildKaraokeReviewDataset,
  type KaraokeReviewDataset,
} from "../../../shared/learning/karaoke-review-dataset.mjs";
import type { ReviewPlan } from "../../../shared/learning/review-session.mjs";

const PENDING_KEY = "typingGamePendingKaraokeReviewV1";

function requestId(): string {
  return `karaoke-review-${Date.now().toString(36)}-${Math.random()
    .toString(36)
    .slice(2, 9)}`;
}

export async function queueKaraokeReview(
  plan: ReviewPlan,
  store = new BrowserLearningProfileStore(),
): Promise<KaraokeReviewDataset> {
  const profile: LearningProfile = await store.load();
  const dataset = buildKaraokeReviewDataset(plan, profile, requestId());
  sessionStorage.setItem(PENDING_KEY, JSON.stringify(dataset));
  return dataset;
}

export function readPendingKaraokeReview(): KaraokeReviewDataset | null {
  const raw = sessionStorage.getItem(PENDING_KEY);
  if (raw === null) return null;

  try {
    const value = JSON.parse(raw) as Partial<KaraokeReviewDataset>;
    if (
      value.version !== 1 ||
      value.type !== "typing-game:learning:v1:review-dataset" ||
      typeof value.requestId !== "string" ||
      !Array.isArray(value.items)
    ) {
      return null;
    }
    return value as KaraokeReviewDataset;
  } catch {
    return null;
  }
}

export function clearPendingKaraokeReview(requestId?: string): void {
  if (requestId !== undefined) {
    const pending = readPendingKaraokeReview();
    if (pending !== null && pending.requestId !== requestId) return;
  }
  sessionStorage.removeItem(PENDING_KEY);
}

export function postPendingKaraokeReview(
  frame: HTMLIFrameElement,
  appUrl: string,
): KaraokeReviewDataset | null {
  const pending = readPendingKaraokeReview();
  const frameWindow = frame.contentWindow;
  if (pending === null || frameWindow === null) return null;

  frameWindow.postMessage(pending, new URL(appUrl).origin);
  return pending;
}
