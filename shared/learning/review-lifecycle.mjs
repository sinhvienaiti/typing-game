export const REVIEW_READY_MESSAGE =
  "typing-game:learning:v1:review-ready";
export const REVIEW_ERROR_MESSAGE =
  "typing-game:learning:v1:review-error";

export function pendingReviewAction(messageType) {
  if (messageType === REVIEW_READY_MESSAGE) return "retain";
  if (messageType === REVIEW_ERROR_MESSAGE) return "clear";
  return "ignore";
}

function normalizePath(value) {
  if (typeof value !== "string") return "";
  const path = value.split(/[?#]/, 1)[0].replace(/\/$/, "");
  return path === "" ? "/" : path;
}

export function shouldAbandonReviewOnRouteChange(
  activeGamePath,
  nextPath,
) {
  const active = normalizePath(activeGamePath);
  const next = normalizePath(nextPath);
  return active !== "" && next !== "" && active !== next;
}
