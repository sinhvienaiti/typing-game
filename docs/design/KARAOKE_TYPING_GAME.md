# Karaoke Typing Game

## Purpose

Karaoke Typing is the fourth independent game in the local typing-game platform.

Repository:

~~~text
sinhvienaiti/karaoke-typing
~~~

Platform submodule:

~~~text
games/karaoke-typing
~~~

Public route:

~~~text
https://typing-game.local/karaoke-typing
~~~

Internal origin:

~~~text
https://karaoke.typing-game.local
~~~

Development port:

~~~text
3003
~~~

## Architecture

Karaoke Typing remains an independent TypeScript/Vite application. The parent platform only owns navigation, iframe mounting, local nginx routing, build/bootstrap commands and the submodule pointer.

No source code from Monkeytype, Vocabulary Shooter or Recall Typing is modified for this game.

The game is inspired by TypingMania NEO gameplay, but the implementation is clean TypeScript code rather than a fork or copied source.

## Media

Supported sources:

~~~text
YouTube URL / video ID
local browser-supported audio
local browser-supported video
~~~

Local files are played with browser object URLs. They are not uploaded or committed to Git.

## Lyrics

Supported input:

~~~text
standard LRC
enhanced LRC word timing
~~~

The game supports a runtime lyric offset from -5s to +5s.

## Gameplay

Modes:

~~~text
Normal
Easy
Blind
Blank
~~~

Normal keeps media moving.

Easy pauses when a lyric line expires before the player finishes it.

Blind hides all target characters except the next required character.

Blank hides the target text and is intended for listening-based practice.

The result tracks score, maximum combo, correct keys, mistakes, completed lines, skipped characters and typing accuracy.

## Verification

The child repository has its own CI:

~~~text
pnpm test
pnpm build
~~~

Because Karaoke Typing is currently private while the other game repositories are public, parent CI does not attempt to clone this sibling repository with the parent repository token. Parent CI verifies the gitlink and continues testing the existing public Recall integration. Karaoke source/build correctness is enforced in the child repository CI.
