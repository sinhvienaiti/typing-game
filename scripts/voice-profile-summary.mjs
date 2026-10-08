const round = (value) => Math.round(value * 100) / 100;

export function summarizeLatencySamples(values) {
  const samples = (Array.isArray(values) ? values : [])
    .filter((value) => Number.isFinite(value) && value >= 0)
    .sort((a, b) => a - b);
  if (samples.length === 0) {
    return { count: 0, p50Ms: null, p95Ms: null, maxMs: null };
  }
  const percentile = (fraction) => {
    const index = Math.max(0, Math.ceil(samples.length * fraction) - 1);
    return round(samples[index]);
  };
  return {
    count: samples.length,
    p50Ms: percentile(0.5),
    p95Ms: percentile(0.95),
    maxMs: round(samples.at(-1)),
  };
}

export function summarizeVoiceProfile(profile = {}) {
  return {
    pcmBlocks: Number.isSafeInteger(profile.pcmBlocks) ? profile.pcmBlocks : 0,
    overflowEvents: Number.isSafeInteger(profile.overflowEvents) ? profile.overflowEvents : 0,
    maxPending: Number.isSafeInteger(profile.maxPending) ? profile.maxPending : 0,
    captureDispatch: summarizeLatencySamples(profile.captureDispatchMs),
    decodeAck: summarizeLatencySamples(profile.decodeAckMs),
    eventLoopLag: summarizeLatencySamples(profile.eventLoopLagMs),
  };
}
