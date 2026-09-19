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

# 9. Current revision

~~~text
sinhvienaiti/monkeytype
feature/en-vn-translation

9ba873ac06411802979ac9fdf48b435db82eb071
~~~

The existing upstream-derived Monkey CI workflow is limited to master/non-draft or forced PR runs. No actual full CI run was produced for this feature branch during this implementation session, so verification should not be overstated.

A local follow-up can run the relevant frontend tests/build before final acceptance.

---

# 10. Compatibility rule

Do not change original Stop on Error accuracy behavior for users who have not enabled this option.

The feature is deliberately opt-in.

This keeps the fork easier to maintain against upstream and avoids surprising existing typing behavior.
