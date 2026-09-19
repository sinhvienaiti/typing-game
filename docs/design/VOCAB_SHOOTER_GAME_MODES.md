# Vocabulary Shooter - Game Modes and Engagement Design

## Document status

Date created:

~~~text
2026-09-19
~~~

Status:

~~~text
Design analysis complete.
Core requirements are confirmed.
Mode names, exact default values and some secondary tuning remain adjustable before implementation.
~~~

This document defines the next major direction for Vocabulary Shooter.

The goal is not to mechanically add a few settings. The game should feel like an actual arcade learning game: varied, responsive, visually rewarding, musically engaging and replayable, while remaining light enough to run smoothly on the user's local MacBook.

---

# 1. Confirmed product principles

The user explicitly requires the following.

## 1.1 More than one game mode

The current lives-based falling-word mode becomes only one mode.

Vocabulary Shooter should support several modes with genuinely different pressure and pacing.

## 1.2 Learning behavior remains consistent

For every mode:

~~~text
before a word is completed correctly
→ do not reveal Vietnamese
→ do not reveal IPA
→ do not pronounce the English word as the success reward

after the word is completed correctly
→ pronounce English
→ show Vietnamese
→ show IPA
→ play the mode-appropriate successful hit/removal effect
~~~

A mode may visually highlight or mark an English target, but it must not leak the VN/IPA answer before success.

## 1.3 Keyboard-first gameplay

The user should not need to reach for the mouse every time the game ends or restarts.

There must be a configurable quick-restart key based on the Monkeytype experience.

Required choices:

~~~text
Tab
Escape
~~~

## 1.4 Music and danger feedback matter

The game should have background music.

When the player is close to losing, the game should communicate danger using coordinated audio and visual feedback instead of a plain numeric warning.

## 1.5 Effects should feel rewarding

Successful typing should not look like a plain text deletion.

The user specifically wants richer effects similar in spirit to a smooth water/bubble burst seen in the reference video.

## 1.6 Beauty and performance must be balanced

Visual richness is not permission to create a heavy game.

Every future game in the platform should follow the same principle:

~~~text
attractive + responsive + performant
~~~

Do not add effects that materially hurt typing latency or frame stability.

---

# 2. Research takeaways used for the design

The design is informed by established typing/arcade patterns, without copying a single game wholesale.

Useful patterns:

- Typing shooters such as ZType use first-letter target selection, lock-on, escalating pressure, waves/lives and visible destruction.
- The Typing of the Dead combines typing with enemy urgency, timed challenge sections, speed/accuracy evaluation and strong danger presentation.
- Racing typing games such as Nitro Type make performance visible and reward steady speed/accuracy; its casual design also demonstrates that difficulty/pacing can be adapted to the player.
- The useful lesson is not to clone these games. It is to make each mode have a clear pressure model, clear feedback and a measurable result.

---

# 3. Proposed mode list

Recommended initial set:

~~~text
1. Classic Survival
2. Bounce / Relax
3. Time Attack
4. Target Rush
~~~

Names can still be renamed before implementation.

The mechanics below are the important part.

---

# 4. Mode 1 - Classic Survival

## Status

~~~text
Existing mechanic, formalized as a mode.
~~~

## Core loop

Words/enemies descend toward the player.

The player types a target to destroy it.

If an enemy reaches the danger line/player:

~~~text
lose one life
~~~

Game ends at zero lives.

## Recommended settings

~~~text
Lives:
1 / 3 / 5 / custom

Spawn rate:
slow / normal / fast / custom

Enemy speed:
slow / normal / fast

Difficulty progression:
off / gradual
~~~

Recommended default:

~~~text
Lives = 3
Difficulty progression = gradual
~~~

## Recommended progression

Do not increase difficulty every frame.

Increase pressure in small steps based on:

- elapsed time,
- cleared targets,
- or wave number.

Examples:

~~~text
slightly shorter spawn interval
slightly higher movement speed
slightly larger active-enemy cap
~~~

The ramp must be smooth.

## Result metrics

~~~text
score
correct words
missed words
accuracy
WPM
max streak
survival time
highest wave / pressure level
~~~

---

# 5. Mode 2 - Bounce / Relax

## Status

Core behavior is confirmed by the user.

The name is still adjustable.

## Core idea

Words do not chase the player and do not fall toward the player.

They move like billiard objects inside the playable rectangle.

Each word receives a velocity vector when it is spawned:

~~~text
vx
vy
~~~

After spawn, it keeps moving in that direction until a wall collision changes the vector.

It must NOT randomly choose a new direction on its own while moving.

## Wall collision

Vertical wall:

~~~text
vx = -vx
~~~

Horizontal wall:

~~~text
vy = -vy
~~~

Corner collision:

~~~text
vx = -vx
vy = -vy
~~~

This creates the requested billiard-like reflection.

The initial angle and speed can be randomized once at spawn.

## Loss condition

This mode is controlled by the number of living words on screen.

Config:

~~~text
maxActiveWords
~~~

Example:

~~~text
maxActiveWords = 12
~~~

If a new spawn makes:

~~~text
activeWords > maxActiveWords
~~~

the run is lost.

## Why this works as a relaxed mode

Pressure comes from accumulation rather than an enemy directly approaching the player.

The user can choose which word to clear.

The screen slowly becomes busier if the player falls behind.

## Recommended settings

~~~text
Maximum active words:
5 - 30

Spawn interval:
1.0 - 10.0 seconds

Movement speed:
slow / normal / fast

Word-word physical collision:
off initially
~~~

## Important performance decision

For the first implementation, use wall collision only.

Do not implement full pairwise word-to-word billiard collision yet.

Reason:

- wall reflection is exactly the confirmed requirement,
- word-word collision is not required,
- pairwise collision adds complexity,
- it can cause overlap-resolution jitter,
- it can become O(n²) as the active count rises.

If true word-word physics is wanted later, use a spatial grid/spatial hash rather than naïve all-pairs checks.

## Danger feedback

Define occupancy:

~~~text
occupancy = activeWords / maxActiveWords
~~~

Suggested feedback:

~~~text
< 0.65
→ calm

0.65 - 0.84
→ mild tension

0.85 - 0.99
→ danger music layer + stronger UI pulse

> 1.00
→ game over
~~~

## Result metrics

~~~text
cleared words
survival duration
maximum simultaneous words
accuracy
WPM
max streak
~~~

## Optional future extension

A true no-fail Zen variant can later be added as a toggle.

It is not required for the first multi-mode implementation.

---

# 6. Mode 3 - Time Attack

## Status

Core behavior is confirmed by the user.

## Core idea

The user configures a duration.

Example:

~~~text
100 seconds
~~~

The game runs until the exact timer expires.

The goal is not survival.

The goal is to measure how much correct work was completed during the fixed period.

## Recommended movement

Reuse the current falling-enemy movement for the first version.

This keeps the mode visually active without creating another physics system.

## Important rule

A missed target does NOT end the run.

If a word reaches the miss line:

~~~text
missed += 1
remove target
continue game
~~~

There are no lives in this mode.

The timer is the game-over condition.

## Timer end

At:

~~~text
timeRemaining <= 0
~~~

stop:

- new spawns,
- typing acceptance for scoring,
- movement used for the run.

Then transition to results.

Default behavior should be exact-stop, not "finish the current word", because the user requested a fixed measurement window.

A finish-current-word option can be considered later.

## Recommended durations

Presets:

~~~text
30s
60s
100s
120s
180s
custom
~~~

Keep the user's requested 100-second case fully supported.

## Countdown feedback

Recommended:

~~~text
last 15s
→ music becomes more active

last 10s
→ visible countdown emphasis

last 5s
→ stronger pulse / countdown SFX
~~~

Do not use heavy screen effects that make the text harder to read.

## Result metrics

~~~text
duration
correct words
missed words
wrong key count
accuracy
characters typed
CPM
WPM
average completion time
max streak
~~~

This mode should become the most useful "benchmark" mode.

---

# 7. Mode 4 - Target Rush

## Status

Core behavior is confirmed by the user.

This is the mode the user described as similar to a shooting-gallery / "bắn gà" rhythm.

Recommended English working name:

~~~text
Target Rush
~~~

Other naming options:

~~~text
Spotlight Rush
Target Gallery
Rapid Target
~~~

## 7.1 Initial word pool

Before the run:

~~~text
targetCount
~~~

is configured.

Example:

~~~text
70
~~~

The game samples that many vocabulary entries.

Recommended range:

~~~text
20 - 100
~~~

The target sequence is shuffled without replacement.

Each selected entry should become the active spotlight target once.

## 7.2 Board layout

A large count such as 70 or 100 cannot be placed as large free-floating cards without creating visual clutter.

Recommended solution:

Use an adaptive target field/grid.

Dormant targets:

- low opacity,
- compact,
- readable,
- distributed in cells,
- optional small position jitter so the board does not look sterile.

Active target:

- strong cyan/blue glow,
- clear scale/outline change,
- easy to find immediately.

Danger target:

- amber → red,
- detached from its original cell,
- begins moving toward the player.

This supports 50-100 words while keeping rendering predictable.

## 7.3 Two-stage timing

Two settings:

~~~text
focusWindowSec
impactWindowSec
~~~

User example:

~~~text
focusWindowSec = 3
impactWindowSec = 2
~~~

Total time from initial activation to player impact:

~~~text
5 seconds
~~~

## 7.4 Fixed target cadence

The next spotlight target must NOT wait for the previous word to be completed.

At each focus deadline:

~~~text
current spotlight ends
→ next target is spotlighted immediately
~~~

This happens whether the old word was completed or not.

This requirement is important.

## 7.5 Successful word before focus deadline

If the player completes the target inside the initial focus window:

~~~text
word is destroyed
→ pronunciation
→ VN + IPA reveal
→ success effect
~~~

The next scheduled spotlight still follows the global cadence.

This keeps the mode rhythmic rather than letting a fast typist consume the entire pool instantly.

## 7.6 Unfinished word at focus deadline

At the end of the focus window:

~~~text
old target
→ enters DANGER state
→ begins a direct dive toward the player over impactWindowSec

at the same moment
→ a new target becomes the spotlight
~~~

The old target remains typable during the dive.

Therefore with:

~~~text
3s focus + 2s dive
~~~

the player truly has up to:

~~~text
5s total
~~~

to save that word.

## 7.7 Late save

If a danger word is completed during the dive:

~~~text
destroy it before impact
→ pronunciation
→ VN + IPA reveal
→ stronger "clutch save" effect
~~~

Track this separately as:

~~~text
lateSave
~~~

This gives the mode a satisfying rescue moment.

## 7.8 Failure

If any danger word reaches the player:

~~~text
impact explosion
→ game over
~~~

One impact is enough for the initial design.

## 7.9 Multiple simultaneous danger targets

It is possible for another spotlight deadline to occur while an older danger target is still alive.

That is intentional pressure.

Do not pause the global cadence waiting for the old word.

## 7.10 Input targeting priority

Eligible targets in this mode:

~~~text
current spotlight target
danger targets
~~~

Dormant targets should not be typable.

Recommended priority when there is no current typing lock:

~~~text
1. matching danger target with smallest time-to-impact
2. current spotlight target
~~~

Once a target is locked by typing, keep the lock until:

- completion,
- explicit unlock,
- target removal.

This avoids ambiguous first letters while still letting the player rescue the most dangerous word.

## 7.11 Recommended settings

~~~text
Target count:
20 - 100
default proposal: 70

Focus window:
1.5 - 6.0s
default proposal: 3.0s

Impact window:
1.0 - 4.0s
default proposal: 2.0s
~~~

The default values are proposals, not yet permanently locked.

## 7.12 Result metrics

If the full pool is survived:

~~~text
targets cleared
normal clears
late saves
wrong key count
accuracy
average response time
max streak
total duration
~~~

If the player is hit:

also show:

~~~text
failed word
time reached
targets completed before failure
~~~

---

# 8. Universal quick-restart design

## Confirmed requirement

The user wants a setting similar to Monkeytype:

~~~text
quickRestartKey = Tab | Escape
~~~

## Conflict with current Escape behavior

Shooter currently uses Escape to unlock a target.

Recommended conflict-free behavior:

~~~text
Quick Restart = Tab
→ Escape remains Unlock

Quick Restart = Escape
→ Tab automatically becomes Unlock
~~~

This keeps both actions available without asking the user to configure two conflicting keys.

## Input safety

Quick restart must be ignored when focus is inside:

- input,
- textarea,
- select,
- open configuration dialog.

When handled by the game:

~~~text
event.preventDefault()
~~~

must be used for Tab so the browser does not move focus.

The quick-restart key should:

- restart an active run,
- start a new run from game-over/results,
- avoid requiring a mouse click.

---

# 9. Unified settings structure

The current flat settings object should evolve into:

~~~text
general
classic
bounce
timeAttack
targetRush
~~~

Recommended conceptual structure:

~~~text
general:
  pronunciation
  accent
  speech rate
  speech volume
  reveal duration
  graphics quality
  music enabled
  music volume
  SFX volume
  danger audio enabled
  quick restart key

classic:
  lives
  spawn interval
  movement speed
  gradual difficulty

bounce:
  max active words
  spawn interval
  movement speed

timeAttack:
  duration
  spawn interval
  movement speed

targetRush:
  target count
  focus window
  impact window
~~~

When this is implemented, preserve/migrate existing settings rather than silently discarding the user's current configuration.

Add a settings schema version.

---

# 10. Mode-selection UI

Recommended layout above/before Start:

~~~text
[ Classic ] [ Bounce ] [ Time Attack ] [ Target Rush ]
~~~

Selecting a mode changes only the mode-specific settings panel.

Do not show all settings for all modes simultaneously.

Suggested hierarchy:

~~~text
Game Mode

General
- pronunciation
- music
- SFX
- graphics
- quick restart

Current Mode
- only settings relevant to selected mode
~~~

This keeps the configuration understandable.

---

# 11. Results screen

A single reusable results component should exist.

Common metrics:

~~~text
Mode
Correct words
Missed words
Wrong keys
Accuracy
WPM
Characters
Max streak
Elapsed time
Average response time
~~~

Mode-specific metrics can be added below.

The result screen should be keyboard-friendly:

~~~text
quick restart key
→ immediately replay same mode/settings
~~~

Do not force mouse interaction.

---

# 12. Audio design

## 12.1 Goals

Audio should provide:

- atmosphere,
- success reward,
- danger awareness,
- countdown urgency,
- mode identity.

It should not become noisy or create audio lag.

## 12.2 Recommended layers

Use a small number of layers:

~~~text
base music
action/danger layer
SFX
~~~

Do not start a new full music track for every danger event.

Crossfade/ramp a danger layer smoothly.

## 12.3 Mode-specific danger input

Expose a normalized:

~~~text
dangerLevel = 0..1
~~~

Examples:

Classic:

~~~text
lowest enemy distance + remaining lives
~~~

Bounce:

~~~text
activeWords / maxActiveWords
~~~

Time Attack:

~~~text
remaining time
~~~

Target Rush:

~~~text
minimum time-to-impact of danger targets
~~~

AudioManager should react to dangerLevel rather than knowing every mode's internal rules.

## 12.4 Suggested audio transitions

~~~text
0.00 - 0.59
→ calm base

0.60 - 0.79
→ slight action layer

0.80 - 0.94
→ danger layer

0.95 - 1.00
→ alarm pulse / critical mix
~~~

Transitions should use volume ramps, not abrupt starts/stops.

## 12.5 Asset policy

When real music/SFX assets are added:

- use assets with clear licenses,
- prefer CC0 or otherwise suitable licenses,
- record attribution/license in the repository,
- do not import random copyrighted music.

---

# 13. Visual effect design

## 13.1 Correct-letter effect

Keep this subtle.

Examples:

- tiny muzzle flash,
- short laser trail,
- small target spark,
- typed prefix color change.

Do not create a full explosion for every key.

## 13.2 Correct-word effect

This is the main reward.

Recommended "bubble burst" composition:

~~~text
1 expanding translucent ring
+
a small number of liquid-like droplets
+
short center flash
+
projectile impact
+
VN/IPA reveal card
~~~

The effect should feel like a water/bubble pop rather than a generic flat fade.

## 13.3 Late-save effect

Target Rush danger save can have:

- stronger ring,
- faster outward droplets,
- short edge flash,
- distinctive success SFX.

It should feel more rewarding than an ordinary clear.

## 13.4 Player-impact effect

Use a stronger impact/explosion and danger audio, but keep text readability.

Avoid long screen shake.

---

# 14. Effect performance budget

Graphics quality must change budgets, not completely different gameplay.

Example particle budgets:

~~~text
Performance:
small burst, around 8-12 droplets

Balanced:
around 16-22 droplets

Quality:
around 24-32 droplets
~~~

Maintain a global live-particle cap.

Do not use expensive blur/filter operations on every moving particle.

Prefer:

- simple Canvas primitives,
- cached/pre-rendered sprites,
- pooled/reused effect objects where useful.

Do not allocate large temporary arrays every frame.

---

# 15. Background presentation

The star field can remain, but each mode can have a small visual identity without creating a new heavy renderer.

Examples:

Classic:

~~~text
forward-moving space pressure
~~~

Bounce:

~~~text
calmer floating field
~~~

Time Attack:

~~~text
subtle timer pulse / speed lines near the end
~~~

Target Rush:

~~~text
shooting-gallery target grid / scanning highlight
~~~

Keep the same rendering engine and asset system.

---

# 16. Recommended small architecture refactor before implementing modes

Do not put all four modes into a single growing Game.ts with large if/switch blocks everywhere.

At the same time, do not build a large framework.

Recommended middle ground:

~~~text
src/game/
├── Game.ts
├── mode-types.ts
└── modes/
    ├── ClassicMode.ts
    ├── BounceMode.ts
    ├── TimeAttackMode.ts
    └── TargetRushMode.ts

src/audio/
└── AudioManager.ts

src/effects/
└── EffectsManager.ts
~~~

Game.ts should keep shared responsibilities:

- input dispatch,
- render loop,
- common target rendering,
- global score/result wiring,
- mode lifecycle.

Each mode should own:

- spawn rules,
- motion rule,
- timer/lives/cap rule,
- failure condition,
- mode-specific statistics,
- dangerLevel calculation.

This is enough separation without over-engineering.

---

# 17. Common target state

A shared target model can use states similar to:

~~~text
dormant
active
danger
pending
destroyed
~~~

Movement can be represented by mode-specific values such as:

~~~text
x
y
vx
vy
~~~

Target Rush uses stationary/dive states.

Bounce uses continuous velocity reflection.

Classic/Time Attack use downward movement.

Avoid making separate unrelated target implementations for every mode unless behavior truly diverges.

---

# 18. Adaptive pacing - recommended optional enhancement

Research into typing games suggests that progression and skill-adjusted pacing can keep sessions engaging.

Recommended optional feature for later:

~~~text
Adaptive Pace
~~~

Suitable for:

- Classic,
- Bounce.

Not recommended for Target Rush when the user explicitly configures 3s + 2s timing; those values should remain exact.

Possible approach:

- evaluate recent 15-20 completed targets,
- consider accuracy and completion time,
- adjust spawn interval/speed slowly,
- limit each adjustment to a small percentage.

Do not change difficulty after every word.

Default can remain off until the user chooses it.

---

# 19. Additional future modes suggested by the analysis

These are not part of the first multi-mode implementation.

## 19.1 Boss Phrase

One large enemy with a long phrase or several stages.

Useful for longer technical phrases and sentence practice.

## 19.2 Combo Rush

Short fixed run focused on maintaining an accuracy/streak multiplier.

## 19.3 Mistake Review

Prioritize words that the player previously missed or typed slowly.

This is more educationally useful after statistics/history are implemented.

Do not build these before the four primary modes are stable.

---

# 20. Cross-game rule for future games

The user's broader product rule is now:

When designing a new learning game, do not merely implement the literal minimum mechanic.

Before implementation:

1. identify the learning goal,
2. analyze comparable successful game mechanics,
3. improve pacing and feedback,
4. add attractive but purposeful visual/audio reward,
5. design keyboard-first controls,
6. define useful result metrics,
7. set explicit performance budgets,
8. avoid unnecessary backend/architecture complexity,
9. keep effects and performance in balance.

A new game should be fun enough to encourage practice, but never at the cost of sluggish input or a stuttering local machine.

---

# 21. Recommended implementation order

Do not implement every feature at once.

Recommended order:

~~~text
Phase 1
→ refactor small mode-controller structure
→ mode selector
→ Classic remains behavior-compatible
→ quick restart

Phase 2
→ Bounce mode
→ wall-reflection physics
→ occupancy failure

Phase 3
→ Time Attack
→ timer/results metrics

Phase 4
→ Target Rush
→ target board
→ fixed spotlight cadence
→ danger dive
→ late save

Phase 5
→ unified results polish
→ background music
→ dynamic danger audio

Phase 6
→ bubble/liquid success effects
→ per-quality effect budgets
→ final performance profiling
~~~

This order keeps the game testable after every phase.

---

# 22. Definition of "good enough" before calling the multi-mode work complete

All of the following should be true:

- all four modes can be selected and replayed without mouse dependency,
- no mode reveals VN/IPA before full correct English,
- pronunciation stays synchronized with successful targets,
- the configured mode timing is exact,
- Target Rush changes spotlight on schedule even if the old word is unfinished,
- the old Target Rush word remains savable during its dive window,
- Bounce words move by velocity/reflection, not random steering,
- Time Attack always reaches its configured duration unless manually restarted,
- results are correct for each mode,
- music transitions do not queue/overlap incorrectly,
- effects are visually rewarding,
- Balanced graphics is smooth on the user's local MacBook,
- Performance mode remains available,
- hidden/inactive game loops do not waste CPU,
- existing vocabulary editor/import/export still works,
- settings migrate without losing the user's previous configuration.

---

# End of design
