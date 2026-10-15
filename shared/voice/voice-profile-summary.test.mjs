import assert from "node:assert/strict";
import test from "node:test";
import {
  summarizeLatencySamples,
  summarizeVoiceProfile,
} from "../../scripts/voice-profile-summary.mjs";

test("voice profile latency summary ignores invalid samples and reports stable percentiles", () => {
  assert.deepEqual(
    summarizeLatencySamples([40, 10, Number.NaN, -1, 30, 20]),
    { count: 4, p50Ms: 20, p95Ms: 40, maxMs: 40 },
  );
  assert.deepEqual(summarizeLatencySamples([]), {
    count: 0,
    p50Ms: null,
    p95Ms: null,
    maxMs: null,
  });
});

test("voice profile summary keeps counters separate from timing evidence", () => {
  assert.deepEqual(
    summarizeVoiceProfile({
      pcmBlocks: 12,
      overflowEvents: 2,
      maxPending: 7,
      captureDispatchMs: [1, 2, 3],
      decodeAckMs: [80, 120, 100],
      eventLoopLagMs: [0, 5, 10],
    }),
    {
      pcmBlocks: 12,
      overflowEvents: 2,
      maxPending: 7,
      captureDispatch: { count: 3, p50Ms: 2, p95Ms: 3, maxMs: 3 },
      decodeAck: { count: 3, p50Ms: 100, p95Ms: 120, maxMs: 120 },
      eventLoopLag: { count: 3, p50Ms: 5, p95Ms: 10, maxMs: 10 },
    },
  );
});
