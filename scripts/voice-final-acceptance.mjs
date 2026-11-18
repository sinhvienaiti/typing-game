import { readFile } from "node:fs/promises";
import { pathToFileURL } from "node:url";

export const VOICE_FINAL_V2_THRESHOLDS = Object.freeze({
  minimumHumanReadings: 1_000,
  minimumAcceptanceRate: 0.95,
  minimumNegativeAudioSeconds: 3 * 60 * 60,
  maximumFalseGameplayCommits: 0,
  maximumMedianLatencyMs: 250,
  maximumP95LatencyMs: 450,
  maximumFrameP95IncreaseMs: 2,
});

export const VOICE_FINAL_V2_REQUIRED_COVERAGE = Object.freeze([
  "micPermissionLifecycle",
  "deviceReconnectAndCompetingTab",
  "targetTypesAndWrongQuietSpeech",
  "ttsPauseResumeAndTargetChurn",
  "hybridOwnershipAndStaleAudio",
  "resultsLearningAndRewardLimits",
  "reloadAndExpeditionModeGuards",
  "desktopNarrowAndHudOverlap",
  "highUltraUnderLoad",
  "browserDeviceMatrix",
  "reconnect",
  "soak",
]);

function isFiniteNonNegative(value) {
  return Number.isFinite(value) && value >= 0;
}

function isSafeNonNegativeInteger(value) {
  return Number.isSafeInteger(value) && value >= 0;
}

function addFailure(failures, code, requirement, actual) {
  failures.push({ code, requirement, actual });
}

export function evaluateVoiceFinalAcceptance(report) {
  const value = report && typeof report === "object" && !Array.isArray(report) ? report : {};
  const failures = [];

  const provenance = value.provenance && typeof value.provenance === "object" && !Array.isArray(value.provenance)
    ? value.provenance
    : {};
  if (provenance.kind !== "real-human-device" || provenance.synthetic !== false) {
    addFailure(
      failures,
      "provenance",
      "evidence must be explicitly recorded from real human/device acceptance (synthetic=false)",
      {
        kind: provenance.kind ?? null,
        synthetic: provenance.synthetic ?? null,
      },
    );
  }

  const totalReadings = value.humanReadings?.total;
  const acceptedReadings = value.humanReadings?.accepted;
  const validReadingCounts =
    isSafeNonNegativeInteger(totalReadings) &&
    isSafeNonNegativeInteger(acceptedReadings) &&
    acceptedReadings <= totalReadings;
  const acceptanceRate = validReadingCounts && totalReadings > 0
    ? acceptedReadings / totalReadings
    : null;

  if (!validReadingCounts || totalReadings < VOICE_FINAL_V2_THRESHOLDS.minimumHumanReadings) {
    addFailure(
      failures,
      "human-readings",
      `at least ${VOICE_FINAL_V2_THRESHOLDS.minimumHumanReadings} real human readings`,
      validReadingCounts ? totalReadings : null,
    );
  }
  if (acceptanceRate === null || acceptanceRate < VOICE_FINAL_V2_THRESHOLDS.minimumAcceptanceRate) {
    addFailure(
      failures,
      "acceptance-rate",
      `at least ${VOICE_FINAL_V2_THRESHOLDS.minimumAcceptanceRate * 100}% accepted human readings`,
      acceptanceRate,
    );
  }

  const negativeAudioSeconds = value.negativeAudio?.seconds;
  if (
    !isFiniteNonNegative(negativeAudioSeconds) ||
    negativeAudioSeconds < VOICE_FINAL_V2_THRESHOLDS.minimumNegativeAudioSeconds
  ) {
    addFailure(
      failures,
      "negative-audio-duration",
      `at least ${VOICE_FINAL_V2_THRESHOLDS.minimumNegativeAudioSeconds} seconds of negative audio`,
      isFiniteNonNegative(negativeAudioSeconds) ? negativeAudioSeconds : null,
    );
  }

  const falseGameplayCommits = value.negativeAudio?.falseGameplayCommits;
  if (
    !isSafeNonNegativeInteger(falseGameplayCommits) ||
    falseGameplayCommits > VOICE_FINAL_V2_THRESHOLDS.maximumFalseGameplayCommits
  ) {
    addFailure(
      failures,
      "false-gameplay-commits",
      "zero false gameplay commits during negative audio",
      isSafeNonNegativeInteger(falseGameplayCommits) ? falseGameplayCommits : null,
    );
  }

  const medianLatencyMs = value.latencyMs?.median;
  if (
    !isFiniteNonNegative(medianLatencyMs) ||
    medianLatencyMs > VOICE_FINAL_V2_THRESHOLDS.maximumMedianLatencyMs
  ) {
    addFailure(
      failures,
      "median-latency",
      `end-to-end median latency <= ${VOICE_FINAL_V2_THRESHOLDS.maximumMedianLatencyMs} ms`,
      isFiniteNonNegative(medianLatencyMs) ? medianLatencyMs : null,
    );
  }

  const p95LatencyMs = value.latencyMs?.p95;
  if (
    !isFiniteNonNegative(p95LatencyMs) ||
    p95LatencyMs > VOICE_FINAL_V2_THRESHOLDS.maximumP95LatencyMs
  ) {
    addFailure(
      failures,
      "p95-latency",
      `end-to-end p95 latency <= ${VOICE_FINAL_V2_THRESHOLDS.maximumP95LatencyMs} ms`,
      isFiniteNonNegative(p95LatencyMs) ? p95LatencyMs : null,
    );
  }

  const frameP95IncreaseMs = value.frameP95IncreaseMs;
  if (
    !isFiniteNonNegative(frameP95IncreaseMs) ||
    frameP95IncreaseMs > VOICE_FINAL_V2_THRESHOLDS.maximumFrameP95IncreaseMs
  ) {
    addFailure(
      failures,
      "frame-p95-increase",
      `frame p95 increase <= ${VOICE_FINAL_V2_THRESHOLDS.maximumFrameP95IncreaseMs} ms`,
      isFiniteNonNegative(frameP95IncreaseMs) ? frameP95IncreaseMs : null,
    );
  }

  const coverage = value.coverage && typeof value.coverage === "object" && !Array.isArray(value.coverage)
    ? value.coverage
    : {};
  for (const key of VOICE_FINAL_V2_REQUIRED_COVERAGE) {
    if (coverage[key] !== true) {
      addFailure(failures, `coverage:${key}`, `${key} must be explicitly verified`, coverage[key] ?? null);
    }
  }

  return {
    ready: failures.length === 0,
    provenance: {
      kind: provenance.kind ?? null,
      synthetic: provenance.synthetic ?? null,
    },
    metrics: {
      totalReadings: validReadingCounts ? totalReadings : null,
      acceptedReadings: validReadingCounts ? acceptedReadings : null,
      acceptanceRate,
      negativeAudioSeconds: isFiniteNonNegative(negativeAudioSeconds) ? negativeAudioSeconds : null,
      falseGameplayCommits: isSafeNonNegativeInteger(falseGameplayCommits) ? falseGameplayCommits : null,
      medianLatencyMs: isFiniteNonNegative(medianLatencyMs) ? medianLatencyMs : null,
      p95LatencyMs: isFiniteNonNegative(p95LatencyMs) ? p95LatencyMs : null,
      frameP95IncreaseMs: isFiniteNonNegative(frameP95IncreaseMs) ? frameP95IncreaseMs : null,
    },
    failures,
  };
}

async function runCli() {
  const reportPath = process.argv[2];
  if (!reportPath) {
    console.error("Usage: pnpm voice:acceptance -- /path/to/voice-final-v2-evidence.json");
    process.exitCode = 2;
    return;
  }

  try {
    const report = JSON.parse(await readFile(reportPath, "utf8"));
    const result = evaluateVoiceFinalAcceptance(report);
    console.log(JSON.stringify(result, null, 2));
    process.exitCode = result.ready ? 0 : 1;
  } catch (error) {
    console.error(error instanceof Error ? error.message : String(error));
    process.exitCode = 2;
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  await runCli();
}
