# Space Typing CI Continuation Policy

This rule applies to resumable/idempotent Space Typing implementation work across tabs/workers.

## Unavailable CI log is non-blocking

If an older CI run/job is known to have failed but its diagnostic log cannot be retrieved:

1. Do **not** stop implementation only because that old log is unavailable.
2. Preserve the latest Git HEAD as source of truth and review the changed code/tests/audits normally.
3. If there is no reproducible local failure or concrete code evidence of a blocker, continue to the next safe resumable commit/unit.
4. Treat CI on the next commit as the fresh diagnostic checkpoint.
5. If the next CI fails and exposes diagnostics, fix the real root cause there.
6. Never weaken validators, tests, audits, exact-SHA guards, or runtime semantics merely to obtain a green result.
7. Record the inaccessible older failure in handoff/progress notes, but do not repeatedly block later workers on the same unavailable log.

Only stop immediately when there is concrete evidence of a real regression, a reproducible build/test failure, a destructive migration risk, or a required release/branch gate that specifically cannot be bypassed safely.
