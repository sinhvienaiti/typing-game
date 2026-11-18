---
name: game-performance-quality
description: Measure and improve Space Typing frame time, responsiveness, Canvas/WebGL cost, asset/memory load, and quality tiers. Use for FPS regressions, profiling, High/Ultra tuning, rendering budgets, or performance acceptance.
---

# Measure the affected mode

1. Read [the profiling map](references/profiling-map.md) and current policy. Identify active renderer/mode and a reproducible workload before choosing an optimization.
2. Capture baseline HEAD, machine/GPU, browser, viewport, device/effective DPR, quality, scene, warmup and duration. Measure frame-time distribution and typing responsiveness; add draw/shader/texture, animation, particle, memory or GLB metrics when relevant.
3. Identify limiting work: CPU updates/layout/allocations, Canvas blur/pixel count, WebGL drawing/shaders/textures, decode/loading, audio or network. Do not attribute every slow frame to Three.js when Canvas is active.
4. Change the responsible existing path with minimal scope. Preserve fidelity/readability unless measurement justifies a tradeoff. Respect adaptive resolution, tiers, lazy loading, fallback and disposal; avoid parallel quality systems.
5. Measure candidate under matching conditions and compare runtime plus visual results. Repeat scene entry/restart for lifecycle/memory changes. Run relevant contract checks without substituting synthetic tests for browser measurements.
6. Report baseline/candidate evidence, bottleneck, improvement or remaining regression, and material limits. If GPU/browser execution is unavailable, finish independent work and mark runtime measurement pending.

Use [space-typing-playtest](../space-typing-playtest/SKILL.md) for execution and available generic profiler/Three.js skills for techniques. Current policy overrides obsolete hard bundle/asset byte ceilings in older plans.
