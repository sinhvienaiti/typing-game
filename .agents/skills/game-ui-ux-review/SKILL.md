---
name: game-ui-ux-review
description: Review or improve rendered Space Typing player/HUD and Administrator workflows for clarity, typing visibility, feedback, responsive layout, and accessible controls. Use for UX review or UI changes; source-only review cannot establish visual acceptance.
---

# Review the player's or operator's workflow

1. Identify the exact surface, role and task: player combat, title/settings/results, Portal iframe, or Administrator editing. Read relevant [review context](references/review-map.md) and inspect current rendered screens when browser capability exists.
2. Follow the workflow with input: what the user wants, sees and can activate, what changes, and how success/error is communicated. Check before/after states; markup alone cannot establish interaction behavior.
3. For play, inspect typing visibility, hierarchy, HUD overlap, feedback, contrast, motion clutter and modal interruption. Check actual viewport and a narrower supported layout; do not expand a desktop task into a mobile redesign.
4. For Admin, inspect entity selection, labels, editable/read-only states, validation, media picker/preview, Draft/Publish state and async recovery. Keep useful help near fields and avoid permanent implementation clutter. Preserve [Admin capability boundaries](../admin-runtime-authoring/SKILL.md).
5. Reuse design tokens, components, tooltips and patterns. Fix the smallest cause and recheck the affected flow, keyboard focus, scaling and overlays.
6. Report concrete findings with route, state, viewport and visual/interaction evidence. Separate observed defects, source-inferred risks and untested cases. If visual tools are unavailable, finish independent source checks and mark visual acceptance pending.

Use [space-typing-playtest](../space-typing-playtest/SKILL.md) for execution, and available generic UI skills for techniques without overriding project contracts.
