import {
  buildShooterReviewDataset,
  type ShooterReviewDataset,
} from "../../../shared/learning/shooter-review-dataset.mjs";
import type { ReviewPlan } from "../../../shared/learning/review-session.mjs";

const PENDING_KEY = "typingGamePendingShooterReviewV1";

function requestId(): string {
  return `shooter-review-${Date.now().toString(36)}-${Math.random()
    .toString(36)
    .slice(2, 9)}`;
}

export function queueShooterReview(plan: ReviewPlan): ShooterReviewDataset {
  const dataset = buildShooterReviewDataset(plan, requestId());
  sessionStorage.setItem(PENDING_KEY, JSON.stringify(dataset));
  return dataset;
}

export function readPendingShooterReview(): ShooterReviewDataset | null {
  const raw = sessionStorage.getItem(PENDING_KEY);
  if (raw === null) return null;

  try {
    const value = JSON.parse(raw) as Partial<ShooterReviewDataset>;
    if (
      value.version !== 1 ||
      value.type !== "typing-game:learning:v1:review-dataset" ||
      typeof value.requestId !== "string" ||
      !Array.isArray(value.items)
    ) {
      return null;
    }
    return value as ShooterReviewDataset;
  } catch {
    return null;
  }
}

export function clearPendingShooterReview(requestId?: string): void {
  if (requestId !== undefined) {
    const pending = readPendingShooterReview();
    if (pending !== null && pending.requestId !== requestId) return;
  }
  sessionStorage.removeItem(PENDING_KEY);
}

export function postPendingShooterReview(
  frame: HTMLIFrameElement,
  appUrl: string,
): ShooterReviewDataset | null {
  const pending = readPendingShooterReview();
  const frameWindow = frame.contentWindow;
  if (pending === null || frameWindow === null) return null;

  frameWindow.postMessage(pending, new URL(appUrl).origin);
  return pending;
}
