# Space Typing Admin UI/UX Progress

## Current State

Status: IN_PROGRESS

Parent:
- Repo: `sinhvienaiti/typing-game`
- Branch: `feat/space-typing-admin-uiux`
- HEAD: `7bed6f52279b055a25bc76d885c93e4640588fe8`

Child:
- Repo: `sinhvienaiti/space-typing`
- Branch: `feat/admin-world-music-stage-policy`
- HEAD: `ef337f682e6d6c554294a042568c43616b3b42a0`

Current milestone:
- **B06.5 — Bosses Admin → Runtime**

Completed:
- **B06.1 — Ships Admin → Runtime**
  - Child canonical contract + preview protocol
  - Parent validation + preview bridge
  - Revision-backed Admin UI
  - Runtime envelope + new-session apply boundary
  - CI coverage
- **B06.2 — Equipment Admin → Runtime**
  - Child canonical contract + preview protocol
  - Parent validation + preview bridge
  - Revision-backed Admin UI
  - Runtime envelope + new-session apply boundary
  - CI coverage
- **B06.3 — Skills Admin → Runtime**
  - Child canonical contract + preview protocol
  - Parent validation + preview bridge
  - Revision-backed Admin UI
  - Runtime envelope + new-session apply boundary
  - CI coverage
- **B06.4 — Enemies Admin → Runtime**
  - Child Enemy Admin contract added
  - 35 canonical Enemy IDs exposed
  - Only canonical authorable runtime field persisted: `minStage`
  - Child Enemy preview protocol + CLI added
  - Child runtime Enemy policy loader added
  - Enemy spawn admission now consumes published `minStage` overrides at new-session boundary
  - Parent Enemy policy validation added
  - Parent Enemy preview bridge added
  - Parent Enemy runtime envelope added
  - Parent revision store accepts `content.enemies`
  - Parent `/api/admin/space-typing/enemies/preview` endpoint added
  - Parent `/api/runtime/space-typing/enemies` endpoint added
  - Revision-backed Enemy Admin editor added at `/admin/space-typing/enemies`
  - Parent child-submodule pointer updated to the B06.4 child HEAD
  - Admin CI updated with B06.4 gates
  - Phase B mapping updated: Ships / Equipment / Skills / Enemies are runtime-backed
  - Admin CI: PASS
  - Platform CI: PASS

Current B06.5 discovery already reviewed:
- Boss source of truth is child-owned under `src/boss/**`
- Canonical boss identity model exists in `src/boss/identity.ts`
- Boss runtime model exists in `src/boss/model.ts`
- Boss visual mapping exists in `src/boss/visual-profile.ts`
- Master Admin UI/UX plan requires a dedicated Boss editor with:
  - Identity: ID, Name, World, Role, Family, Art
  - Stats: HP, Shield, Armor, Damage, Speed
  - Phase timeline: Phase 1 / Phase 2 / Phase 3-Enrage
  - Per-phase attacks, skills, spawn, movement, music, VFX, announcer
  - Rewards: credits, rare credits, equipment, drop table, first clear, repeat clear

Important B06.5 constraint:
- Do **not** blindly persist every field listed in the UI/UX master plan.
- First identify which Boss fields already have a real canonical child runtime consumer.
- Any field without a proven runtime consumer must remain read-only / preview-only until a safe canonical contract is added.
- Keep Save Draft revision-backed and Publish-gated; no direct runtime mutation from the editor.

Remaining:
- Finish B06.5 child Boss runtime-consumer audit field by field
- Decide minimal safe authorable Boss contract for the first runtime-backed slice
- Add Boss child Admin contract section
- Add Boss preview protocol + CLI
- Add Boss runtime policy loader at a new-session boundary
- Wire supported Boss policy into real boss runtime consumers
- Add child Boss policy/preview/runtime tests
- Mirror Boss contract in parent
- Add parent Boss policy validation
- Add parent Boss preview bridge
- Add parent Boss runtime envelope + endpoints
- Replace mock Boss Admin screen with revision-backed B06.5 editor
- Keep unsupported Boss UI plan fields read-only with explicit explanation
- Update Phase B mapping + validation scripts
- Update parent submodule pointer to the exact final child HEAD
- Run child CI
- Run Admin CI
- Run Platform CI
- Review exact final parent + child HEADs before moving to B06.6 Worlds & Stages

Next action:
- Continue **B06.5 — Bosses Admin → Runtime** by auditing `src/boss/identity.ts`, `src/boss/model.ts`, `src/boss/skills.ts`, `src/boss/typing-mechanics.ts`, `src/boss/visual-profile.ts`, and the actual Game/runtime call sites; then define the smallest safe Boss authorable contract instead of inventing unsupported fields.

Blocker:
- NONE
