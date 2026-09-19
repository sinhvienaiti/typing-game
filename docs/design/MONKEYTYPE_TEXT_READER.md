# Monkeytype - Full Text Reader

## Status

Implemented and reviewed on:

~~~text
sinhvienaiti/monkeytype
branch feature/en-vn-translation
revision 943b4d9dd60f6e4f870cba3588538b8b06745210
~~~

---

# 1. Goal

Allow the user to listen to the current Monkeytype Custom Text without adding a heavy TTS dependency or downloading generated audio.

The reader is separate from the existing per-word EN-VN pronunciation feature.

---

# 2. Speech engine

Use the browser/system Web Speech API:

~~~text
SpeechSynthesis
SpeechSynthesisUtterance
~~~

Do not add:

- cloud TTS as a core dependency,
- generated MP3 downloads,
- video/audio assets for each text,
- a large WebAssembly/neural TTS model.

---

# 3. Languages

Supported reader language modes:

~~~text
auto
English (en-US)
Vietnamese (vi-VN)
~~~

Auto mode detects Vietnamese-specific marks and otherwise chooses English.

Explicit language selection exists because Vietnamese text without diacritics cannot be reliably distinguished from English by a lightweight local heuristic.

---

# 4. Local voice policy

Only browser voices with:

~~~text
localService === true
~~~

are offered.

The stored voice preference is:

~~~text
textReaderVoiceURI
~~~

If the selected voice disappears, the UI falls back to automatic selection from the remaining local voices for the chosen language.

If no matching local voice exists, the user receives a clear message.

Do not silently switch to a remote voice.

---

# 5. Reader settings

Persisted settings:

~~~text
textReaderEnabled
textReaderLanguage
textReaderVoiceURI
textReaderRate
textReaderVolume
~~~

Rate range:

~~~text
0.5 → 2.0
~~~

Volume range:

~~~text
0 → 100
~~~

---

# 6. Controls and automatic start

The settings modal uses:

~~~text
Preview / Restart
Pause / Resume
Stop
~~~

The Preview button exists only to test the selected language/voice/rate while configuring the reader.

During a real Custom Text test:

~~~text
first real typing key
→ start the full-text reader automatically
→ read the actual generated test words
~~~

This means shuffle/repeat/limit generation is respected instead of reading stale editor text.

Only one automatic start is attempted per test. Restart clears that state.

Closing the Custom Text modal stops preview reading.

Disabling the reader also stops active reading.

---

# 7. Long-text handling

The reader does not submit one huge utterance.

Text is normalized and split into bounded chunks.

Sentence boundaries are preferred.

Long sentence fragments are split by words.

A single oversized token is split into bounded pieces.

This keeps browser speech queues responsive for long Custom Text input.

---

# 8. Speech queue coordination

The full-text reader and EN-VN word pronunciation use the same browser speech engine.

During an active full-text read:

~~~text
reader state = playing / paused
→ keep tooltip/top learning cues
→ suppress per-word pronunciation
~~~

This prevents a matching dictionary word from immediately cancelling the full-text narration that just started.

When the reader is idle, normal per-word pronunciation works as before.

Starting a reader preview or a new full-text read still clears older queued speech before beginning.

This avoids overlapping speech and stale queued pronunciation.

---

# 9. Pause/cancel edge case

Some browser/OS speech implementations can remain paused after a cancellation.

The stop path therefore:

~~~text
cancel()
if paused → resume()
state → idle
~~~

This ensures a later Play/Restart or word pronunciation is not silently stuck.

---

# 10. Persistence and migration

The reader settings share:

~~~text
personalEnVnTranslationSettings
~~~

Older stored settings migrate to safe defaults:

~~~text
enabled: false
language: auto
voice: automatic local
rate: 1.0
volume: 100
~~~

---

# 11. Verification

Focused unit tests cover:

- Vietnamese auto detection,
- English auto fallback,
- explicit language override,
- chunking and word preservation,
- oversized token splitting,
- blank input.

Dedicated Custom EN-VN CI at revision 943b4d9...:

~~~text
lint PASS
stylelint PASS
local-static frontend build PASS
full frontend tests PASS
~~~
