import {
  buildRecallReviewDataset,
  type RecallReviewDataset,
} from "../../../shared/learning/recall-review-dataset.mjs";
import type { ReviewPlan } from "../../../shared/learning/review-session.mjs";

const PENDING_KEY = "typingGamePendingRecallReviewV1";

function requestId(): string {
  return `recall-review-${Date.now().toString(36)}-${Math.random()
    .toString(36)
    .slice(2, 9)}`;
}

export function queueRecallReview(plan: ReviewPlan): RecallReviewDataset {
  const dataset = buildRecallReviewDataset(plan, requestId());
  sessionStorage.setItem(PENDING_KEY, JSON.stringify(dataset));
  return dataset;
}

export function readPendingRecallReview(): RecallReviewDataset | null {
  const raw = sessionStorage.getItem(PENDING_KEY);
  if (raw === null) return null;

  try {
    const value = JSON.parse(raw) as Partial<RecallReviewDataset>;
    if (
      value.version !== 1 ||
      value.type !== "typing-game:learning:v1:review-dataset" ||
      typeof value.requestId !== "string" ||
      !Array.isArray(value.items)
    ) {
      return null;
    }
    return value as RecallReviewDataset;
  } catch {
    return null;
  }
}

export function clearPendingRecallReview(requestId?: string): void {
  if (requestId !== undefined) {
    const pending = readPendingRecallReview();
    if (pending !== null && pending.requestId !== requestId) return;
  }
  sessionStorage.removeItem(PENDING_KEY);
}

export function postPendingRecallReview(
  frame: HTMLIFrameElement,
  appUrl: string,
): RecallReviewDataset | null {
  const pending = readPendingRecallReview();
  const frameWindow = frame.contentWindow;
  if (pending === null || frameWindow === null) return null;

  frameWindow.postMessage(pending, new URL(appUrl).origin);
  return pending;
}
