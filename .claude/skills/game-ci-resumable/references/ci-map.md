# CI sources and continuation

## Repository boundaries

- [Submodules](../../../../.gitmodules): `games/space-typing` is a separate repo.
  Its HEAD can differ from the parent gitlink; inspect both.
- [Parent CI](../../../../.github/workflows/ci.yml) covers integration, shared
  learning/voice, child tests and builds.
- [Game CI](../../../../games/space-typing/.github/workflows/ci.yml) covers game
  tests/build, admin bridges and domain audits.
- [Parent scripts](../../../../package.json), [game scripts](../../../../games/space-typing/package.json),
  [admin CI](../../../../.github/workflows/admin-ci.yml) and
  [continuation policy](../../../../docs/SPACE_TYPING_CI_CONTINUATION_POLICY.md)
  define actual commands/gates. Recheck after branch changes.

## Focused verification

From the parent: `pnpm validate:space-integration`, `pnpm admin:contract:validate`,
`pnpm voice:check`, `pnpm learning:test`, `pnpm admin:test` as affected.
For a game test: `pnpm --dir games/space-typing exec vitest run tests/<file>`.
Broader changes may need `pnpm --dir games/space-typing test` and `pnpm build:space`.
Read generator-based gates first: they may rewrite tracked assets. Preserve prior
modifications and avoid installers/generators for unrelated documentation work.

For agent-skills-only work: `node scripts/validate-agent-skills.mjs`,
`bash scripts/sync-agent-skills.sh --check`, `git diff --check`.

## Checkpoint contents

Record parent/child branch and SHA, scoped dirty files, intent, completed unit,
commands/results, inaccessible diagnostics, manual checks, pending external task IDs
when applicable, and next unit. Mark historic test results as historic. Exclude secrets.

The [Claude process note](../../../../games/space-typing/docs/CLAUDE_PROCESS_2026-10-17.md)
contains useful decisions but is not latest HEAD or a universal host setup. Detect
macOS/Windows/WSL tooling. New workers inspect current tree and intervening diffs,
reuse still-valid evidence, then continue. Shared-area edits need integration, not
blind file replacement.
