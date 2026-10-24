---
name: admin-runtime-authoring
description: Change Space Typing Administrator authoring, media selection, validation, publishing, and production previews while preserving the Admin-to-runtime authority chain. Use for Admin editing workflows or config changes; use gameplay skills for player combat rules.
---

# Administrator authoring

Treat Admin as an operator's editing tool. Start with the task and current source; a field in a form or a historical plan does not prove production consumes it.

1. Read the relevant entries in [the authority map](references/authority-map.md). Identify parent Admin and child runtime repositories, current checkouts, and the canonical owner of the requested field.
2. Trace `Admin UI → validated schema → persisted revision → preview/runtime bridge → resolver → production consumer → apply boundary`. Record missing links before exposing a writable control. Use executable capability matrices to distinguish supported editing, migration required, read-only reference, and unsupported work.
3. Reuse the existing registry, revision lifecycle, and Media V2 picker. Preserve exact immutable asset-version bindings, Draft/Published isolation, conflict detection, rollback, and the domain's apply boundary. Do not invent a second Portal-only registry or renderer to make a form appear functional.
4. Make the operator workflow clear: select an entity, edit supported values, see validation, preview the candidate, save a draft, publish when authorized, and verify effective runtime. Use picker plus preview for supported media fields; put useful implementation metadata in contextual help.
5. Verify the affected schema/resolver and publish/preview boundary with focused checks. Then inspect the rendered workflow through [space-typing-playtest](../space-typing-playtest/SKILL.md), including loading/error states and preview teardown. Distinguish registry/data previews from production visual previews in the report.

Use [game-ui-ux-review](../game-ui-ux-review/SKILL.md) for operator usability. Available generic UI/game skills can help implement a component; project contracts decide ownership and supported capabilities.
