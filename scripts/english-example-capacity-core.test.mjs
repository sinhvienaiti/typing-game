import test from "node:test";
import assert from "node:assert/strict";
import { assessExampleSourceCapacity } from "./english-example-capacity-core.mjs";

test("insufficient total source capacity blocks completion and all later transitions", () => {
  const result = assessExampleSourceCapacity({ minimum: 100000, published: 2213, unreviewedRaw: 4588 });
  assert.equal(result.reviewState, "blocked-source-capacity");
  assert.equal(result.optimisticPublishedUpperBound, 6801);
  assert.equal(result.additionalSourceGap, 93199);
  assert.equal(result.remainingPublishedDeficit, 97787);
  assert.equal(result.step2Pass, false);
  assert.equal(result.step3Unlocked, false);
  assert.equal(result.group2Unlocked, false);
});

test("enough raw candidates never count as reviewed publication", () => {
  const result = assessExampleSourceCapacity({ minimum: 100, published: 10, unreviewedRaw: 90 });
  assert.equal(result.reviewState, "editorial-review-required");
  assert.equal(result.remainingPublishedDeficit, 90);
  assert.equal(result.step2Pass, false);
  assert.equal(result.step3Unlocked, false);
});

test("reaching a count still requires full editorial and runtime review before unlocking", () => {
  const result = assessExampleSourceCapacity({ minimum: 100, published: 100, unreviewedRaw: 0 });
  assert.equal(result.reviewState, "target-count-met-full-review-required");
  assert.equal(result.remainingPublishedDeficit, 0);
  assert.equal(result.step2Pass, false);
  assert.equal(result.group2Unlocked, false);
});

test("invalid source counts cannot bypass the capacity gate", () => {
  for (const invalid of [-1, NaN, Infinity, 1.5, "100"]) {
    assert.throws(() => assessExampleSourceCapacity({ minimum: 100, published: 1, unreviewedRaw: invalid }));
  }
  assert.throws(() => assessExampleSourceCapacity({ minimum: 0, published: 0, unreviewedRaw: 0 }));
});
