# Space Typing Game

## Status

Planned independent fifth game.

Repository:

~~~text
sinhvienaiti/space-typing
~~~

Platform target:

~~~text
games/space-typing
https://typing-game.local/space-typing
https://space.typing-game.local
development port 3004
~~~

## Product direction

Space Typing is a clean TypeScript/Canvas implementation inspired by the feel and mechanics of ZType, not a fork or asset copy.

The quality target is a modern arcade presentation with stronger visual feedback, wider desktop use and deeper integration with the typing-game learning resources.

## Shared English resources are mandatory

Space Typing must not maintain a separate built-in English word list.

The platform vocabulary source of truth is:

~~~text
shared/vocabulary/index.json
shared/vocabulary/levels/001.json
...
shared/vocabulary/levels/100.json
~~~

Current production library:

~~~text
100 levels
18,000 entries
~~~

Every official entry has:

~~~text
id
en
vi
ipa
~~~

Example runtime shape:

~~~json
{
  "id": "L003-025",
  "en": "cache",
  "vi": "bộ nhớ đệm",
  "ipa": "/kæʃ/"
}
~~~

Phrases are supported as well as single words.

Space Typing must consume this library through the same HTTP contract used by Shooter and Recall:

~~~text
/vocabulary/index.json
/vocabulary/levels/NNN.json
~~~

Normal gameplay must fetch the selected level only rather than loading all 100 levels.

## Vocabulary UX

Space Typing uses the same explicit vocabulary source contract as Shooter and Recall:

~~~text
Class
-> choose level
-> Use level
-> Applying...
-> apply
-> close dialog
-> success notice

Custom
-> optional local custom entries
-> save explicitly
-> success notice
~~~

Class/Custom tab switching alone must never silently apply a source.

The active level/source is persisted locally.

## Learning feedback

Destroying a word may show:

~~~text
English target
Vietnamese meaning
IPA
pronunciation
~~~

VI + IPA feedback must appear immediately on successful completion rather than waiting for projectile/explosion travel.

Pronunciation participates in the parent shared-music ducking contract:

~~~text
typing-game:speech
active true / false
~~~

## Shared typing-text corpus

The game may additionally use:

~~~text
shared/typing-texts/
~~~

for phrase/sentence challenge waves, boss phases or future advanced modes.

The normal arcade word mode remains vocabulary-level driven.

## Shared music

Background music is owned by the parent Portal.

Space Typing must not implement another competing background-music system.

The child may own:

~~~text
typing laser SFX
impact SFX
explosion SFX
enemy warning/projectile SFX
boss SFX
pronunciation
~~~

Parent shared music remains responsible for playlist, YouTube/local tracks, shuffle/repeat and pronunciation ducking.

## Screen and visual layout

Do not reproduce ZType's narrow portrait playfield.

The game should use the full available game iframe with a wide responsive desktop arena.

Target desktop composition:

~~~text
16:9 / wide responsive arena
usable up to roughly 1500x900 content space
center battlefield uses most of viewport
HUD stays around edges
no artificial narrow portrait column
~~~

Suggested layout:

~~~text
┌──────────────────────────────────────────────────────────┐
│ SCORE  STREAK  MULTIPLIER     WAVE/BOSS      POWER      │
│                                                          │
│       enemy             heavy enemy                      │
│              projectiles / particles                     │
│                                                          │
│                    WIDE BATTLEFIELD                      │
│                                                          │
│                         player                           │
│ ACC/WPM                                      LIVES       │
└──────────────────────────────────────────────────────────┘
~~~

Mobile/tablet may reduce density, but desktop is the primary visual target.

## Visual quality target

Required feel:

~~~text
60 FPS target
high-DPI canvas
additive glow
particle trails
impact bursts
short hit-stop
controlled screen shake
word hit knockback
enemy recoil
smooth target lock
animated power/streak meter
boss telegraphs
enemy letter/word projectiles
layered parallax/grid/star background
pause overlay with live audio controls
~~~

Effects must remain readable and must not obscure target text.

## Core gameplay systems

Planned systems:

~~~text
first-letter target acquisition
locked target typing
correct-key laser feedback
wrong-key streak/power penalty
word completion explosion
enemy knockback while typing
wave progression
streak
multiplier
power meter
special/overdrive action
enemy projectiles carrying letters/words
heavy enemies
bosses
pause/resume
results screen
accuracy
WPM
max streak
score
~~~

The implementation may study ZType behavior and public technical material for timing/game-feel reference, but must not copy ZType proprietary assets, soundtrack, SFX or unlicensed game source.

## Integration rule

Space Typing remains an independent game repository/submodule.

Adding it must not modify gameplay source of:

~~~text
Monkeytype
Vocabulary Shooter
Recall Typing
Karaoke Typing
~~~

Parent changes are limited to registry, navigation, submodule/build/bootstrap/play/nginx integration and shared contracts.
