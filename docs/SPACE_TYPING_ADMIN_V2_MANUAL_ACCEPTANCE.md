# Space Typing Admin V2 — Manual Acceptance

> Task-based manual QA checklist for Administrator-first Admin V2.
>
> Automated implementation must continue when these scenarios are safely deferrable. Manual QA becomes blocking only when a later dependency requires the observed browser behavior to be proven.

---

# A1 — Help / Tooltip / Shell Foundation

## A1-M01 — Navigation tooltip by mouse

1. Open Space Typing Admin on desktop.
2. Expand a sidebar group.
3. Hover a group label.
4. Hover an item such as Ships or Shop.

Expected:
- concise label remains the only permanent sidebar text;
- contextual tooltip appears near the hovered control;
- tooltip uses the dark Space Typing sci-fi style;
- tooltip does not cover the trigger when another placement fits;
- moving away closes non-pinned help;
- no browser-native yellow `title` tooltip appears.

## A1-M02 — Keyboard tooltip access

1. Navigate the sidebar using Tab / Shift+Tab.
2. Focus a group toggle and a navigation item.

Expected:
- visible keyboard focus remains clear;
- contextual help is available on focus without requiring a mouse;
- help is associated accessibly with the focused control;
- Escape closes visible tooltip help.

## A1-M03 — Click/tap info icon

1. Activate the info icon beside `LOCAL ADMIN · CONNECTED` with mouse click.
2. Repeat using keyboard Enter/Space.
3. On a touch-capable device or emulation, tap the icon.

Expected:
- tooltip/popover toggles open;
- content explains local Admin and draft/publish behavior in administrator language;
- a second activation closes it;
- tap/click outside closes it;
- Escape closes it and restores focus to the trigger where applicable.

## A1-M04 — Tooltip collision handling

1. Resize the viewport so the sidebar/topbar trigger is close to a window edge.
2. Open the associated tooltip.

Expected:
- tooltip flips/repositions when the preferred direction has insufficient space;
- tooltip remains inside the viewport with readable padding;
- no horizontal page overflow is introduced.

## A1-M05 — Route teardown

1. Open a tooltip.
2. Navigate to another Space Typing Admin route before interacting with the old tooltip.

Expected:
- old tooltip node disappears;
- no stale tooltip is visible on the new route;
- new route help still works;
- repeated navigation does not produce duplicated Escape/outside-click behavior.

## A1-M06 — Leaving Admin teardown

1. Open/pin a tooltip in Space Typing Admin.
2. Navigate out of Space Typing Admin to another portal surface.

Expected:
- body-level tooltip/backdrop is removed;
- no Admin overlay remains on the non-Admin page;
- returning to Admin creates one clean help lifecycle only.

## A1-M07 — Help drawer keyboard behavior

Execute once a screen uses the shared Help Drawer.

Expected:
- drawer receives initial focus;
- Tab/Shift+Tab stays inside the drawer;
- Escape closes the drawer;
- clicking/tapping the backdrop closes it;
- focus returns to the element that opened it;
- background controls are not accidentally activated while the drawer is open.

## A1-M08 — Reduced motion

1. Enable OS/browser `prefers-reduced-motion: reduce`.
2. Open tooltips/help drawer.

Expected:
- tooltip/drawer remains fully usable;
- decorative transitions/animations are suppressed.

## A1-M09 — Sidebar density

Inspect the sidebar at desktop/laptop widths.

Expected:
- no always-visible short description appears beneath every item;
- groups/items are materially less noisy than Phase B;
- labels remain scannable and do not overlap icons/chevrons;
- active route remains obvious.

---

# Future phase scenarios

The following scenarios are placeholders and become executable when their phase lands:

- change a Shop product price and preview the real gameplay result;
- schedule a discount/badge and verify conflict validation;
- replace a Ship image/model through Media Library;
- change Ship weapon/projectile/VFX/SFX without raw paths;
- upload BGM and assign it to a World/Stage;
- duplicate an entity into a draft;
- save draft without changing active runtime;
- review the complete change scope before Publish;
- publish with CAS safety;
- roll back an eligible published version;
- verify a restricted role cannot call mutation/Developer Tools APIs directly;
- verify audit log answers who/what/when/change scope;
- complete routine administrator tasks without raw JSON/path/SHA/protocol/source ownership concepts.
