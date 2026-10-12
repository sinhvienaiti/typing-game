# Voice Final V2 Acceptance Evidence

Updated: 2026-10-10

This document describes the **release evidence** required to close Space Typing Voice / Hybrid Final V2 acceptance. It does not replace the runtime, synthetic fake-microphone test, or the child Voice implementation status.

## Important boundary

`pnpm voice:e2e` and the profile summary are engineering diagnostics. They may prove that the Portal capture → worklet → Vosk → matcher path works under a reproducible synthetic workload, but they **must not** be used as the Final V2 release certificate.

The release validator deliberately fails closed unless the report says that the measurements came from real human/device acceptance:

```json
{
  "provenance": {
    "kind": "real-human-device",
    "synthetic": false
  }
}
```

Synthetic profiler output, missing provenance, or `synthetic: true` fails even if its numeric values happen to satisfy every threshold.

## Release thresholds

The validator implements the gates already documented by the Space Typing Voice Final V2 status:

- at least **1,000 real human readings**;
- at least **95% accepted readings**;
- at least **3 hours (10,800 seconds) of negative audio**;
- **zero false gameplay commits** during negative audio;
- end-to-end latency median **<= 250 ms**;
- end-to-end latency p95 **<= 450 ms**;
- frame p95 increase **<= 2 ms**;
- every required lifecycle, Hybrid, visual, browser/device, reconnect and soak coverage item explicitly verified.

The acceptance percentage is derived from `accepted / total`; a caller-supplied percentage is never trusted.

## Evidence file

Start with a report shaped like this and replace every placeholder with measured evidence. Keep unfinished coverage items `false`; do not mark them true merely because automated tests passed.

```json
{
  "provenance": {
    "kind": "real-human-device",
    "synthetic": false
  },
  "humanReadings": {
    "total": 0,
    "accepted": 0
  },
  "negativeAudio": {
    "seconds": 0,
    "falseGameplayCommits": 0
  },
  "latencyMs": {
    "median": 0,
    "p95": 0
  },
  "frameP95IncreaseMs": 0,
  "coverage": {
    "micPermissionLifecycle": false,
    "deviceReconnectAndCompetingTab": false,
    "targetTypesAndWrongQuietSpeech": false,
    "ttsPauseResumeAndTargetChurn": false,
    "hybridOwnershipAndStaleAudio": false,
    "resultsLearningAndRewardLimits": false,
    "reloadAndExpeditionModeGuards": false,
    "desktopNarrowAndHudOverlap": false,
    "highUltraUnderLoad": false,
    "browserDeviceMatrix": false,
    "reconnect": false,
    "soak": false
  }
}
```

A `0` latency value in the template is only a placeholder; the report is still rejected because the reading counts, negative-audio duration and coverage are incomplete.

## Run the validator

```bash
pnpm voice:acceptance -- /path/to/voice-final-v2-evidence.json
```

Exit codes:

- `0`: every documented Final V2 gate is satisfied by a report explicitly marked as real human/device evidence;
- `1`: valid JSON, but release evidence is incomplete or a threshold failed;
- `2`: missing path, unreadable file, or invalid JSON.

The command prints normalized metrics plus every failed gate so a test pass can be resumed without redoing already verified coverage.

## What must be exercised manually / on real devices

The coverage object corresponds to the current Final V2 checklist and should only be marked true after the relevant evidence exists:

- microphone grant / deny / cancel, stopping before ready, unplug/reconnect and competing-tab behavior;
- all supported target families plus wrong/quiet speech;
- TTS echo, pause/resume and target churn;
- Hybrid keyboard/voice ownership and stale old-audio protection;
- results, learning, reward/passive limits and no speech-generated WPM/streak authority;
- reload and Expedition/mode guards;
- desktop/narrow HUD placement, long transcript and toast/hotbar overlap;
- High/Ultra behavior under game load;
- intended browser/device matrix;
- reconnect behavior;
- required soak run.

Do not mark Voice Final V2 release acceptance complete until this validator returns `ready: true` from genuine measured evidence. Runtime/unit/CI success and synthetic Voice E2E remain necessary engineering evidence, not substitutes for this release gate.
