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
4. Hover an item such as Ships or Music Library.

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

# A2 — Administrator Shell / Dashboard / Developer Tools

## A2-M01 — Dashboard uses real Admin data only

1. Open `/admin/space-typing`.
2. Note the live generation, draft count, music count and signed-in actor.
3. Open History & Publish and compare draft/live state.
4. Open Music Library and compare the catalog size.

Expected:
- Dashboard values correspond to real revision-store and music-catalog data;
- no random/demo/placeholder KPI appears;
- publishable and stale draft counts match History semantics;
- maintenance warning appears only when the active revision has maintenance enabled.

## A2-M02 — Dashboard loading, empty and error states

1. Reload Dashboard normally.
2. On a fresh local Admin profile with no successful audit activity, inspect Recent Admin Activity.
3. Temporarily stop the Admin service and reload Dashboard, then restore the service and use Retry.

Expected:
- loading skeleton is visible while canonical data is loading;
- no-activity state is explicit and not presented as an error;
- service failure produces a clear administrator-facing error state;
- retry returns to the Dashboard without stale overlays or duplicate content.

## A2-M03 — Administrator-first primary navigation

Inspect the normal sidebar.

Expected:
- normal Admin navigation contains Dashboard, Content, Gameplay, Media and System workflows that currently have real administrator value;
- Shop runtime contract, currencies diagnostics, rewards diagnostics, missions diagnostics, PvP diagnostics, Backgrounds/VFX/UI Assets diagnostics and QA Sandbox do not appear as normal administrator menu items;
- technical routes were not deleted: they remain reachable from Developer Tools for an authorized actor.

## A2-M04 — Developer Tools permission-aware visibility

Run with an actor/token configuration that does not expose `developer.runtime-inspect` when such a restricted local test actor is available.

Expected:
- Developer Tools group fails closed while actor permissions are unresolved;
- unauthorized actor does not receive the Developer Tools manifest;
- Developer Tools command-palette entries are omitted when permission is absent;
- normal administrator workflows remain usable.

Current local default actor is Super Admin, so this scenario may remain deferred until a restricted actor fixture is introduced.

## A2-M05 — Developer Tools organization

1. Open Developer Tools as the local Super Admin.
2. Inspect Runtime & Telemetry, Economy Diagnostics, Live Ops Diagnostics, PvP Diagnostics, Visual Diagnostics and QA/Test Lab.
3. Open at least one tool from each section.

Expected:
- technical screens are grouped by purpose instead of mixed into normal navigation;
- descriptions make it clear that diagnostics are not editable Admin capabilities;
- existing canonical direct routes still load their runtime-backed/read-only surfaces;
- no fake Shop editor, fake event scheduler or fake player backend is introduced.

## A2-M06 — Command palette separation

1. Open `Cmd/Ctrl+K` as the default local Super Admin.
2. Search for `Ships`, `History`, `Shop`, `Events`, `VFX` and `QA`.

Expected:
- administrator workflows are available as normal commands;
- technical commands are available only because the current actor has Developer Tools permission;
- command result labels/groups clearly distinguish Developer Tools concepts;
- keyboard navigation, Escape and focus restoration continue to work.

## A2-M07 — Direct legacy migration routes

Directly open representative technical URLs such as:
- `/admin/space-typing/shop`
- `/admin/space-typing/events`
- `/admin/space-typing/backgrounds`
- `/admin/space-typing/qa`

Expected:
- route still resolves during migration;
- breadcrumb remains understandable;
- route is not re-added to the primary administrator sidebar;
- underlying Phase B ownership/runtime safety behavior remains unchanged.

## A2-M08 — Responsive shell after navigation reduction

Check desktop, laptop and narrow viewport widths.

Expected:
- shorter administrator-first sidebar remains scannable;
- Dashboard cards/attention/activity/quick actions do not force horizontal page overflow;
- Developer Tools cards/links remain readable;
- tooltips and command palette remain usable after resize.

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
