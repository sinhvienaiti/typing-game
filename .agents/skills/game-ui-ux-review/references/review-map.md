# UI review map

## Read relevant context

- Player intent: [UI/UX content plan](../../../../games/space-typing/docs/SPACE_TYPING_UI_UX_CONTENT_PLAN.md), [round 2 polish](../../../../games/space-typing/docs/UI_POLISH_ROUND2_2026-10-04.md), [command deck](../../../../games/space-typing/docs/COMMAND_DECK_UIUX_AUDIO_2026-10-16.md). Dated plans contain deferred work; confirm routes/behavior in current source.
- Current implementation: [Space UI](../../../../games/space-typing/src/ui/), [main integration](../../../../games/space-typing/src/main.ts), [Portal](../../../../portal/src/).
- Administrator: [manual acceptance](../../../../docs/SPACE_TYPING_ADMIN_V2_MANUAL_ACCEPTANCE.md), [remediation](../../../../docs/SPACE_TYPING_ADMIN_RUNTIME_UIUX_REMEDIATION_PLAN.md), [components](../../../../portal/src/admin/v2/admin-components.ts), [help](../../../../portal/src/admin/v2/admin-help.ts), [dialogs](../../../../portal/src/admin/v2/admin-dialog.ts), [picker](../../../../portal/src/admin/v2/asset-picker.ts).
- Evidence: [visual guide](../../../../games/space-typing/docs/VISUAL_TESTING.md), [Batch F procedure](../../../../games/space-typing/docs/UI_UX_BATCH_F_BROWSER_QA.md). A procedure/checkpoint does not prove today's screen.

| Surface | Exercise | Observe |
| --- | --- | --- |
| Gameplay | Start, target, type wrong then correct, use a skill, overlap effects | Words/caret/progress stay readable; warnings/HUD avoid target lane; next action remains clear |
| Menus/results | Keyboard navigation, open/close overlay, review result and return | Visible/restored focus; clear selected/disabled states; no leaked gameplay input; understandable next action |
| Portal | Actual embedded game size and standalone child | Header/iframe clipping, scaling and overlays in the user's surface; child-only capture does not prove Portal fit |
| Administrator | Select entity, edit supported field, preview, trigger validation/API error, save authorized draft | Useful labels, editable/read-only distinction, visible progress, actionable errors, retained state and no stale preview |
| Media | Select compatible version, preview, clear/restore if supported | Version/fallback are understandable; candidate and published apply boundary consume the selection |
| Resize/motion | Supported sizes and reduced-motion controls | No clipped actions, hidden text, HUD collision or unnecessary animation |

Record findings as `observation → effect on task → correction → recheck`. Use severity when it helps prioritize. Do not convert aesthetic preferences into gameplay requirements.

Existing regressions include [results layout](../../../../games/space-typing/tests/stage-results-layout.test.ts), [title](../../../../games/space-typing/tests/title-home.test.ts), [tooltip](../../../../games/space-typing/tests/holo-tooltip.test.ts), [input priority](../../../../games/space-typing/tests/game-input-priority.test.ts), and [Admin preview lifecycle](../../../../games/space-typing/tests/admin-asset-preview-lifecycle.test.ts). They protect contracts but do not replace rendered review.
