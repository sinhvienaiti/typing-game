import {
  buildSpaceReviewDataset,
  type SpaceReviewDataset,
} from "../../../shared/learning/space-review-dataset.mjs";
import type { ReviewPlan } from "../../../shared/learning/review-session.mjs";

const PENDING_KEY = "typingGamePendingSpaceReviewV1";

function requestId(): string {
  return `space-review-${Date.now().toString(36)}-${Math.random()
    .toString(36)
    .slice(2, 9)}`;
}

export function queueSpaceReview(plan: ReviewPlan): SpaceReviewDataset {
  const dataset = buildSpaceReviewDataset(plan, requestId());
  sessionStorage.setItem(PENDING_KEY, JSON.stringify(dataset));
  return dataset;
}

export function readPendingSpaceReview(): SpaceReviewDataset | null {
  const raw = sessionStorage.getItem(PENDING_KEY);
  if (raw === null) return null;

  try {
    const value = JSON.parse(raw) as Partial<SpaceReviewDataset>;
    if (
      value.version !== 1 ||
      value.type !== "typing-game:learning:v1:review-dataset" ||
      typeof value.requestId !== "string" ||
      !Array.isArray(value.items)
    ) {
      return null;
    }
    return value as SpaceReviewDataset;
  } catch {
    return null;
  }
}

export function clearPendingSpaceReview(requestId?: string): void {
  if (requestId !== undefined) {
    const pending = readPendingSpaceReview();
    if (pending !== null && pending.requestId !== requestId) return;
  }
  sessionStorage.removeItem(PENDING_KEY);
}

export function postPendingSpaceReview(
  frame: HTMLIFrameElement,
  appUrl: string,
): SpaceReviewDataset | null {
  const pending = readPendingSpaceReview();
  const frameWindow = frame.contentWindow;
  if (pending === null || frameWindow === null) return null;

  frameWindow.postMessage(pending, new URL(appUrl).origin);
  return pending;
}
