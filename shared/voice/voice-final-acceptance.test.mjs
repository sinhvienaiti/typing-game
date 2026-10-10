import assert from "node:assert/strict";
import test from "node:test";
import {
  evaluateVoiceFinalAcceptance,
  VOICE_FINAL_V2_REQUIRED_COVERAGE,
} from "../../scripts/voice-final-acceptance.mjs";

function completeCoverage() {
  return Object.fromEntries(VOICE_FINAL_V2_REQUIRED_COVERAGE.map((key) => [key, true]));
}

function passingEvidence(overrides = {}) {
  return {
    humanReadings: { total: 1_000, accepted: 950 },
    negativeAudio: { seconds: 10_800, falseGameplayCommits: 0 },
    latencyMs: { median: 250, p95: 450 },
    frameP95IncreaseMs: 2,
    coverage: completeCoverage(),
    ...overrides,
  };
}

test("Final V2 acceptance passes only at or above every documented release gate", () => {
  const result = evaluateVoiceFinalAcceptance(passingEvidence());
  assert.equal(result.ready, true);
  assert.deepEqual(result.failures, []);
  assert.equal(result.metrics.acceptanceRate, 0.95);
});

test("Final V2 acceptance fails closed for incomplete synthetic/profile evidence", () => {
  const result = evaluateVoiceFinalAcceptance({
    pcmBlocks: 300,
    overflowEvents: 0,
    captureDispatch: { p95Ms: 5 },
    decodeAck: { p95Ms: 100 },
  });

  assert.equal(result.ready, false);
  assert.ok(result.failures.some((failure) => failure.code === "human-readings"));
  assert.ok(result.failures.some((failure) => failure.code === "negative-audio-duration"));
  assert.ok(result.failures.some((failure) => failure.code === "coverage:browserDeviceMatrix"));
});

test("Final V2 acceptance rejects insufficient accuracy and any false gameplay commit", () => {
  const result = evaluateVoiceFinalAcceptance(passingEvidence({
    humanReadings: { total: 1_000, accepted: 949 },
    negativeAudio: { seconds: 10_800, falseGameplayCommits: 1 },
  }));

  assert.equal(result.ready, false);
  assert.ok(result.failures.some((failure) => failure.code === "acceptance-rate"));
  assert.ok(result.failures.some((failure) => failure.code === "false-gameplay-commits"));
});

test("Final V2 acceptance rejects latency, frame or qualitative coverage regressions", () => {
  const evidence = passingEvidence();
  evidence.latencyMs = { median: 251, p95: 451 };
  evidence.frameP95IncreaseMs = 2.01;
  evidence.coverage.highUltraUnderLoad = false;

  const result = evaluateVoiceFinalAcceptance(evidence);
  const codes = new Set(result.failures.map((failure) => failure.code));
  assert.equal(result.ready, false);
  assert.ok(codes.has("median-latency"));
  assert.ok(codes.has("p95-latency"));
  assert.ok(codes.has("frame-p95-increase"));
  assert.ok(codes.has("coverage:highUltraUnderLoad"));
});

test("Final V2 acceptance validates reading counters instead of trusting a supplied percentage", () => {
  const result = evaluateVoiceFinalAcceptance(passingEvidence({
    humanReadings: { total: 900, accepted: 900, acceptanceRate: 1 },
  }));

  assert.equal(result.ready, false);
  assert.ok(result.failures.some((failure) => failure.code === "human-readings"));
  assert.equal(result.metrics.acceptanceRate, 1);
});
