export const REVIEW_READY_MESSAGE:
  "typing-game:learning:v1:review-ready";
export const REVIEW_ERROR_MESSAGE:
  "typing-game:learning:v1:review-error";

export function pendingReviewAction(
  messageType: unknown,
): "retain" | "clear" | "ignore";

export function shouldAbandonReviewOnRouteChange(
  activeGamePath: string,
  nextPath: string,
): boolean;
