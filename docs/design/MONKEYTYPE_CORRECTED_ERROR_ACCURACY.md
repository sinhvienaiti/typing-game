# Monkeytype - Corrected Error Accuracy

## Date

~~~text
2026-09-19
~~~

## Status

~~~text
Implemented on feature/en-vn-translation.
Default is off.
Original Monkeytype behavior remains unchanged unless explicitly enabled.
~~~

## Problem

Monkeytype already has Stop on Error.

The user wants Stop on Error because it forces a mistake to be corrected before moving forward.

However, while the user is already blocked on an incorrect character/word, additional keystrokes can create more accuracy penalties even though they are part of the same unresolved blocked mistake.

The user also wants a corrected mistake to stop damaging the final/live accuracy value.

---

# 1. New setting

Internal config key:

~~~text
forgiveCorrectedErrors
~~~

UI label:

~~~text
forgive corrected errors
~~~

Default:

~~~text
false
~~~

The option only applies when:

~~~text
stopOnError !== off
~~~

If it is disabled, Monkeytype keeps its original scoring behavior.

---

# 2. Letter Stop on Error

Configuration:

~~~text
stop on error = letter
forgive corrected errors = on
~~~

Example:

~~~text
target: hello

press x
→ blocked
→ one countable accuracy error

press y
→ still blocked at the same character
→ do not add another accuracy error

press h
→ correct character
→ previous blocked error is forgiven
→ live/final accuracy is restored
~~~

The blocked input event still exists in history; it is simply excluded from accuracy.

---

# 3. Word Stop on Error

Configuration:

~~~text
stop on error = word
forgive corrected errors = on
~~~

Once the current word contains an unresolved error:

~~~text
first error in the blocked word
→ can count

later wrong keys while the same word remains incorrect
→ do not repeatedly reduce accuracy
~~~

This specifically prevents the common Stop on Error problem where the user starts typing what they intended as the next word, but Monkeytype is still blocking them on the previous incorrect word and every extra key lowers accuracy.

When the current word is repaired:

~~~text
bad input removed/corrected
→ word becomes exactly correct
→ previous blocked-word accuracy error is forgiven
~~~

Correction can be recognized through normal typing or through deletion/backspace.

---

# 4. Event design

Input events can carry:

~~~text
accuracyIgnored: true
~~~

Why keep the event instead of deleting it:

- the physical input actually happened,
- replay/debug/history can still know it happened,
- timing/key activity remains truthful,
- only the accuracy meaning changes.

This is cleaner than rewriting/deleting historical input events.

---

# 5. Live accuracy

The live accuracy cache ignores events marked:

~~~text
accuracyIgnored
~~~

When a previously counted error becomes forgiven, the cache total is adjusted incrementally.

The entire test event history is not rescanned on every correction.

This keeps the feature lightweight during long typing tests.

---

# 6. Final accuracy and error history

Final:

~~~text
getAccuracy()
~~~

ignores forgiven error events.

Accuracy error-history calculations and missed-word tracking also ignore those forgiven events.

Raw physical key activity is not erased.

---

# 7. Main implementation files

~~~text
packages/schemas/src/configs.ts
frontend/src/ts/constants/default-config.ts
frontend/src/ts/config/metadata.tsx

frontend/src/ts/input/handlers/insert-text.ts
frontend/src/ts/input/handlers/delete.ts

frontend/src/ts/test/events/types.ts
frontend/src/ts/test/events/data.ts
frontend/src/ts/test/events/live-cache.ts
frontend/src/ts/test/events/stats.ts

frontend/__tests__/input/handlers/insert-text.spec.ts
frontend/__tests__/test/events/stats.spec.ts
~~~

---

# 8. Test coverage added

Tests cover:

~~~text
letter mode:
first blocked error counts
repeated same-position attempt is ignored
correct character forgives the original error

word mode:
first blocked-word error counts
additional wrong keys in same bad word are ignored
correcting the word forgives the blocked-word error

option off:
original Monkeytype scoring remains unchanged

stats:
accuracyIgnored events are excluded
live accuracy is restored
final accuracy is restored
~~~

---

# 9. Current revision and UI location

~~~text
sinhvienaiti/monkeytype
feature/en-vn-translation

9ca8c976d3883688705e58bb0e3f1626db7eae1b
~~~

The option is now visibly rendered in:

~~~text
Settings
→ Input
→ stop on error
→ forgive corrected errors
~~~

The implementation logic already existed before this UI fix; the missing piece was that SettingsPage did not include the setting component, so users could not discover/toggle it normally.

Dedicated Custom EN-VN CI at the revision above verifies:

~~~text
lint PASS
stylelint PASS
local-static frontend build PASS
full frontend tests PASS
~~~

---

# 10. Compatibility rule

Do not change original Stop on Error accuracy behavior for users who have not enabled this option.

The feature is deliberately opt-in.

This keeps the fork easier to maintain against upstream and avoids surprising existing typing behavior.


---

# 11. Keep the first penalty without repeated penalties

A second accuracy option now exists for the user's fast-typing case.

Internal key:

~~~text
ignoreRepeatedBlockedErrors
~~~

UI label:

~~~text
ignore repeated blocked errors
~~~

Default:

~~~text
false
~~~

It requires:

~~~text
stop on error != off
~~~

The behavior is intentionally different from `forgive corrected errors`.

## Letter mode

~~~text
first wrong attempt at blocked character
→ accuracy penalty remains

second / third / later wrong attempt at the same blocked character
→ event is retained
→ accuracyIgnored = true
→ no additional accuracy penalty

correct character entered later
→ continue typing
→ DO NOT forgive the original first error
~~~

Example:

~~~text
target: hello

x
→ incorrect = 1

y
→ still blocked
→ no extra accuracy penalty

z
→ still blocked
→ no extra accuracy penalty

h
→ correct
→ original incorrect = 1 remains
~~~

This is the mode intended for fast typing where several physical keystrokes may already be queued mentally before the user notices that Stop on Error has blocked progress.

## Word mode

The same policy applies at blocked-word level:

~~~text
first error in unresolved word
→ can count

later wrong attempts while the same word remains unresolved
→ do not add more accuracy penalties

word is later repaired
→ original first penalty remains
~~~

Unlike `forgiveCorrectedErrors`, deletion/correction does not turn the original error into an ignored accuracy event.

## Relationship with forgive corrected errors

The two settings represent different scoring policies:

~~~text
ignore repeated blocked errors
→ first penalty remains

forgive corrected errors
→ first penalty can be removed after correction
~~~

The Settings UI makes them mutually exclusive when enabled so the scoring policy is unambiguous.

---

# 12. Keep first wrong letter before blocking

A separate Stop on Error presentation/input option now exists.

Internal key:

~~~text
stopOnErrorKeepFirstError
~~~

UI label:

~~~text
keep first wrong letter
~~~

Default:

~~~text
false
~~~

It only changes behavior for:

~~~text
stop on error = letter
~~~

Example:

~~~text
target: Modern

M
→ correct

a
→ expected o
→ a remains in the input
→ a is rendered as the normal Monkeytype incorrect/red character

next normal typing key
→ blocked
→ no extra character is accepted

Backspace
→ remove a

o
→ correct
→ typing can continue
~~~

The first wrong character is therefore visible and actionable instead of being immediately removed.

Implementation rule:

~~~text
before-insert
→ if current input already contains an unresolved wrong character
→ block new insertion

delete/backspace pipeline
→ unchanged
→ user can remove the wrong character normally
~~~

A defensive guard also exists in the insert handler for composition/emulated insertion paths.

---

# 13. Verification baseline after the new options

Final reviewed Monkeytype revision:

~~~text
9ca8c976d3883688705e58bb0e3f1626db7eae1b
~~~

The first CI pass found a real integration omission: every Config key must also exist in Monkeytype's command-line metadata object.

The missing entries were:

~~~text
stopOnErrorKeepFirstError
ignoreRepeatedBlockedErrors
~~~

They were added normally rather than bypassing the type/lint requirement.

Final dedicated Custom EN-VN CI:

~~~text
lint PASS
stylelint PASS
local-static production build PASS
full frontend tests PASS
~~~

Focused tests now also cover:

- first penalty retained while repeated letter-level blocked attempts are ignored,
- first penalty retained after a blocked word is repaired,
- retained first wrong character,
- blocking later input while that wrong character remains,
- continuing normally after deletion and correct re-entry,
- unresolved-input error detection.
