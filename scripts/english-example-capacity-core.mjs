export function assessExampleSourceCapacity({ minimum, published, unreviewedRaw }) {
  for (const [name, value] of Object.entries({ minimum, published, unreviewedRaw })) {
    if (!Number.isSafeInteger(value) || value < 0 || (name === "minimum" && value === 0)) {
      throw new TypeError(`${name} must be a valid nonnegative integer; minimum must be positive`);
    }
  }
  const upperBound = published + unreviewedRaw;
  if (!Number.isSafeInteger(upperBound)) throw new TypeError("Capacity exceeds safe integer range");
  return {
    reviewState: published >= minimum ? "target-count-met-full-review-required" :
      upperBound < minimum ? "blocked-source-capacity" : "editorial-review-required",
    remainingPublishedDeficit: Math.max(0, minimum - published),
    optimisticPublishedUpperBound: upperBound,
    additionalSourceGap: Math.max(0, minimum - upperBound),
    // Source availability and record counts cannot approve an editorial step.
    step2Pass: false,
    step3Unlocked: false,
    group2Unlocked: false,
  };
}
