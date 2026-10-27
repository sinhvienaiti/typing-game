---
name: game-ci-resumable
description: Resume Typing Game or Space Typing CI and Git work; use for outdated checkpoints, remote updates or concurrent workers while preserving current HEAD, dirty work and verification gates.
---

# Resumable CI and Git work

1. Identify the owning repository. Record branch, HEAD and dirty paths in parent
   and affected submodule. For remote-branch work, fetch and inspect upstream when
   available; fetch failure does not make an old local checkpoint current. State
   the freshness limitation.
2. Compare checkpoint with current HEAD, recent commits and diff. Continue from
   current source, preserving newer worker changes. Do not reset, revert, stash or
   switch away from work to recreate an old checkpoint. If HEAD advances during
   the task, inspect intervening changes before integrating your edits.
3. Read the [CI source map](references/ci-map.md) and current workflow/package
   scripts. Reproduce on the present tree, then make a narrow fix without weakening
   assertions, exact-SHA gates or runtime semantics.
4. Missing historic CI diagnostics are non-blocking by themselves: reproduce locally
   or inspect current source/workflow, record the missing evidence and continue
   the next safe requested unit. Actual reproducible failures, destructive data
   risk and required release gates still need resolution. Fresh CI is useful only
   when commit/push is already authorized; this skill grants no such permission.
5. After a small blocker is fixed, continue the next planned unit within scope.
   Track native IME, microphone and other machine-dependent checks separately so
   independent implementation can proceed where safe.
6. Run relevant checks, inspect `git diff --check` and status, and leave a checkpoint:
   changed files, exact tested revision plus dirty work, validation, pending manual
   checks and next action. Keep steps resumable/idempotent; do not claim tests ran
   against a newer untested tree.
