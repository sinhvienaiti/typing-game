# Profiling sources and invariants

Read [Code Quality and Performance Rules](../../../../games/space-typing/docs/CODE_QUALITY_AND_PERFORMANCE_RULES.md) first. It supersedes earlier hard JavaScript/CSS/build/audio/Ship V3 byte ceilings. Growth remains a review signal; correctness, measurements and maintainability decide acceptance. Preserve integrity checks.

| Concern | Source | Evidence |
| --- | --- | --- |
| Profiles/frame reports | [quality.ts](../../../../games/space-typing/src/performance/quality.ts) | Average FPS/frame time, p95, slow-frame ratio and effective DPR; read current values rather than duplicating limits |
| Adaptive resolution | [adaptive-resolution.ts](../../../../games/space-typing/src/performance/adaptive-resolution.ts) | Sustained-load downshift/recovery, pixel workload and crispness |
| Baseline/candidate gate | [Batch F gate](../../../../games/space-typing/src/test-lab/batch-f-performance-gate.ts), [procedure](../../../../games/space-typing/docs/UI_UX_BATCH_F_BROWSER_QA.md) | Matched machine/browser/viewport/DPR/quality and export; recorded checkpoint SHAs are historical |
| Duel pressure | [Duel performance](../../../../games/space-typing/src/duel/performance.ts), [tests](../../../../games/space-typing/tests/duel-performance.test.ts) | Representative attack/particle/network load and actual impact semantics |
| Models/textures | [Contracts](../../../../games/space-typing/src/render3d/model-contracts.ts), [loader](../../../../games/space-typing/src/render3d/model-loader.ts) | Transfer versus decoded memory, tiers, first-load stalls, disposal and fallback |
| Canvas/backgrounds | [Evaluations](../../../../games/space-typing/scripts/visual/evals/), [visual guide](../../../../games/space-typing/docs/VISUAL_TESTING.md) | Canvas CPU cost, effective DPR, textures and same-run stress comparisons |
| Defense benchmark | [V2 draft](../../../../games/space-typing/docs/SPACE_TYPING_DEFENSE_PLAN_V2_2026-10-18.md), [bench](../../../../games/space-typing/src/bench/defense-bench.ts) | Rendering feasibility only; not implemented Rift Defense gameplay or network performance |

## Interpretation

- High/Ultra differ in resolution and effects. Record canvas dimensions/effective DPR, not just setting name.
- Canvas blur/shadows scale with physical pixels. WebGL shader/draw-call advice applies only to measured active WebGL paths.
- Caches, loading, background tabs, thermal state and headless/software GPU affect results. Compare in one run and disclose limits; avoid cool-baseline/hot-candidate comparisons.
- Synthetic tests protect algorithms/caps; they do not establish player FPS or input latency.
- Capture visual before/after for fidelity tradeoffs. Smaller files with unchanged runtime cost are not automatically faster.
- Inspect build/report scripts before interpreting metric failures. Do not restore historical byte ceilings or bypass required format/provenance checks.

From repo root select relevant checks:

```bash
pnpm --dir games/space-typing test tests/performance-quality.test.ts tests/adaptive-resolution.test.ts
pnpm --dir games/space-typing test tests/duel-performance.test.ts
```

[Batch F tests](../../../../games/space-typing/tests/batch-f-performance-gate.test.ts), [M22 stress](../../../../games/space-typing/tests/m22-runtime-stress.test.ts) and [bundle reporter](../../../../games/space-typing/scripts/report-bundle-metrics.mjs) are additional tools; confirm they cover the active mode.
