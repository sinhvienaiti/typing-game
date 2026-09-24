import test from "node:test";
import assert from "node:assert/strict";

import {
  REVIEW_ERROR_MESSAGE,
  REVIEW_READY_MESSAGE,
  pendingReviewAction,
  shouldAbandonReviewOnRouteChange,
} from "./review-lifecycle.mjs";

test("ready acknowledgement retains a pending dataset for browser refresh", () => {
  assert.equal(pendingReviewAction(REVIEW_READY_MESSAGE), "retain");
  assert.equal(pendingReviewAction(REVIEW_ERROR_MESSAGE), "clear");
  assert.equal(pendingReviewAction("typing-game:speech"), "ignore");
});

test("same game refresh keeps review state while route exit abandons it", () => {
  assert.equal(
    shouldAbandonReviewOnRouteChange(
      "/games/recall",
      "/games/recall",
    ),
    false,
  );
  assert.equal(
    shouldAbandonReviewOnRouteChange(
      "/games/recall/",
      "/games/recall?refresh=1",
    ),
    false,
  );
  assert.equal(
    shouldAbandonReviewOnRouteChange(
      "/games/recall",
      "/review/session",
    ),
    true,
  );
  assert.equal(
    shouldAbandonReviewOnRouteChange(
      "/games/recall",
      "/games/space",
    ),
    true,
  );
});
