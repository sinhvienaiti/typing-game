# Typing Feedback System — VFX + Keypress Audio

> Owner, 29/10/2026: proposal by ChatGPT, given to Claude as a reference ("hãy tham khảo để chúng ta có những hiệu ứng vfx hay cho typing game"). Claude's review against the live code: `docs/games/TYPING_FEEDBACK_REVIEW.md`.
## Technical Analysis & Proposal for Claude Review

**Project context:** Shared typing-game ecosystem  
**Primary references:** Typing Break visual feedback + Monkeytype keypress sound behavior  
**Purpose:** Architecture/review document for implementation planning  
**Scope:**  
- Per-character typing visual feedback  
- Word-completion feedback  
- Combo/intensity escalation  
- Keypress sound profiles  
- Audio variation and latency  
- Shared/reusable engine design  
- Performance, accessibility, licensing, and rollout strategy  

---

# 1. Executive Summary

The most important lesson from Typing Break is that **typing itself must feel like gameplay**, not like a text field placed on top of a game.

A normal typing implementation usually behaves like:

```text
keypress
  ↓
validate character
  ↓
change text color
  ↓
move caret
```

That is acceptable for a typing test, but weak for an action game.

The desired experience is closer to:

```text
KEYPRESS
   ↓
VALIDATE INPUT
   ↓
INSTANT GLYPH RESPONSE
   ├── flash
   ├── glow
   ├── scale punch
   ├── micro movement
   └── particle burst
   ↓
AUDIO RESPONSE
   ├── keypress sound
   ├── small pitch/volume variation
   └── profile-specific timbre
   ↓
WORD ENERGY BUILDS
   ↓
WORD COMPLETE
   ↓
STRONGER RELEASE EFFECT
   ↓
ATTACK / SKILL / GAMEPLAY EVENT
```

The core recommendation is to build a reusable module tentatively named:

```text
TypingFeedbackEngine
```

with two major subsystems:

```text
TypingVisualFeedback
TypingAudioFeedback
```

The engine should be reusable across:

- Space Typing
- Defense/Tower Typing
- Monkey-based practice mode where appropriate
- future RPG / cultivation typing game
- future voice + typing hybrid games
- other typing mini-games

The goal is **not to copy Typing Break or Monkeytype visually or audibly**.

The goal is to study the interaction principles and create our own system with:

- our own effects,
- our own timing,
- our own sound profiles,
- reusable architecture,
- safe asset licensing.

---

# 2. Core Design Principle: Every Keypress Is a Game Action

The player may press hundreds or thousands of keys in one session.

Therefore, even a very small improvement to one keypress is repeated many times.

This is comparable to:

- weapon recoil in shooters,
- hit sparks in fighting games,
- successful note feedback in rhythm games,
- button feedback in action games,
- damage numbers in RPGs.

For a typing game:

> **keypress feedback is one of the most important forms of game feel.**

The visual and audio systems must therefore prioritize:

1. very low perceived latency,
2. readability,
3. responsiveness,
4. variation,
5. escalation,
6. performance.

---

# 3. What the Typing Break Effect Actually Is

There is no single universal library or effect name.

Useful technical terms include:

- per-character typing feedback
- per-keystroke feedback
- glyph hit flash
- character hit flash
- reactive typography
- kinetic typography
- text glow pulse
- bloom pulse
- per-character animation
- per-character particle burst
- hit-confirmation VFX
- text impact animation
- typing game juice
- micro-interaction feedback
- game feel
- input feedback

The observed effect should be understood as a **stack of small effects**.

Example:

```text
accepted keypress
   ↓
target glyph brightness spikes
   ↓
glyph color flashes
   ↓
glyph scale briefly increases
   ↓
glow/bloom expands
   ↓
small local particles appear
   ↓
effect rapidly decays
   ↓
glyph settles into completed state
```

A possible timing envelope:

```text
0 ms       key accepted
0–25 ms    immediate brightness/color flash
20–70 ms   scale/impact peak
40–120 ms  glow peak and decay
40–160 ms  particles disperse/fade
100–200 ms glyph settles
```

These are tuning starting points, not fixed values.

---

# 4. Why the Effect Must Be Per Character

Avoid treating the entire word as one DOM/canvas object if we want strong visual feedback.

Bad model:

```text
"cultivation"
```

as a single object.

Better model:

```text
[c][u][l][t][i][v][a][t][i][o][n]
```

Each glyph should be individually addressable.

Example state:

```ts
type GlyphState =
  | "pending"
  | "active"
  | "correct"
  | "incorrect"
  | "corrected";
```

Each glyph can maintain visual metadata:

```ts
interface GlyphVisualState {
  index: number;
  state: GlyphState;
  flash: number;
  glow: number;
  scale: number;
  offsetX: number;
  offsetY: number;
  opacity: number;
}
```

This enables effects on **only the character that was just typed**.

---

# 5. Visual Feedback Hierarchy

Not every event should have the same visual weight.

If every keypress creates a huge explosion, the game becomes exhausting and unreadable.

Use a hierarchy.

---

## 5.1 Level 1 — Character Hit

Triggered for each accepted character.

Possible effects:

- short brightness flash,
- color transition,
- subtle scale punch,
- small glow pulse,
- 1–4 small particles,
- tiny vertical impulse,
- optional micro-shock ring.

Intensity:

```text
LOW
```

Purpose:

> Confirm that the input was accepted immediately.

Suggested feel:

```text
quick
crisp
small
local
readable
```

---

## 5.2 Level 2 — Correct Streak / Word Progress

Triggered after several consecutive correct characters.

Examples:

```text
3 correct
5 correct
8 correct
10 correct
```

Possible effects:

- glow intensity slowly increases,
- energy line grows under word,
- particles begin travelling toward player/weapon,
- aura around active word becomes stronger,
- subtle color progression,
- combo indicator reacts.

Intensity:

```text
LOW → MEDIUM
```

Purpose:

> Communicate that the player is building energy rather than merely filling letters.

---

## 5.3 Level 3 — Word Complete

Triggered when the entire word is completed correctly.

Possible sequence:

```text
last glyph hit
   ↓
whole word flashes
   ↓
word receives stronger bloom
   ↓
small outward ring
   ↓
energy contracts toward center
   ↓
energy transfers to player / weapon
   ↓
attack or skill executes
```

Possible effects:

- whole-word glow,
- radial burst,
- short text scale pulse,
- particle convergence,
- energy trail,
- text dissolve,
- projectile launch,
- enemy target reaction.

Intensity:

```text
MEDIUM
```

This should feel substantially stronger than a normal character.

---

## 5.4 Level 4 — Perfect Word / Combo Milestone

Examples:

- word completed with no error,
- 10-word combo,
- 25-word combo,
- very high WPM streak,
- accuracy threshold,
- critical typing event.

Possible effects:

- stronger flash,
- special particle shape,
- distinct color,
- stronger energy beam,
- brief radial distortion,
- controlled camera impulse,
- critical attack VFX.

Intensity:

```text
MEDIUM → HIGH
```

Important:

Do **not** use strong screen shake on normal keypresses.

Reserve stronger effects for meaningful events.

---

# 6. Proposed Character Animation Recipe

A good default correct-key effect could be:

```text
START
  glyph scale = 1.0

KEY ACCEPTED
  scale:      1.0 → 1.12 → 1.0
  brightness: 1.0 → 1.8 → 1.0
  glow:       0   → 0.7 → 0
  y offset:   0   → -2px → 0
  particles:  2–4
```

Duration:

```text
~100–160 ms
```

The effect must finish quickly enough for fast typists.

At 120 WPM, feedback events can overlap heavily.

Therefore:

> Effects must support overlapping execution without blocking future input.

Never wait for an animation to finish before processing the next key.

---

# 7. Error Feedback

Incorrect input should have a distinct response, but it should not overwhelm the learning information.

Possible incorrect-key effect:

```text
wrong key
   ↓
active glyph turns warning color
   ↓
short horizontal twitch
   ↓
small sharp particle
   ↓
error state remains visible
```

Avoid:

- huge red full-screen flash,
- long shake,
- excessive punishment animation,
- covering IPA/translation,
- moving the word so much that the player loses their reading position.

Example timing:

```text
shake: 50–90 ms
color: persists according to typing rules
particles: optional
```

For learning modes, readability should beat spectacle.

---

# 8. Corrected Error State

Because some game modes may allow backspace/correction, visual state should distinguish:

```text
correct first try
incorrect
corrected
```

Possible corrected appearance:

```text
correct-first-try = normal success glow
corrected         = success color but reduced sparkle
```

This allows accuracy systems to preserve meaningful feedback without punishing the user visually forever.

The visual system should **not define scoring rules**.

Instead it should receive semantic events from the typing engine:

```ts
onGlyphCorrect(...)
onGlyphIncorrect(...)
onGlyphCorrected(...)
```

This keeps feedback architecture independent from typing rules.

---

# 9. Word Energy Concept

A strong extension beyond the reference is to make typed characters visually generate gameplay energy.

Example:

```text
character typed
   ↓
tiny energy particle appears at glyph
   ↓
particle travels toward word-energy anchor
   ↓
energy meter increases
```

On word completion:

```text
stored energy
   ↓
released toward player/weapon
   ↓
projectile/skill
```

This creates a clear semantic chain:

```text
KNOWLEDGE
   ↓
TYPING
   ↓
ENERGY
   ↓
POWER
   ↓
ATTACK
```

This is particularly suitable for:

- Space Typing
- fantasy/cultivation typing RPG
- tower/defense typing support
- boss battles

---

# 10. Particle Strategy

Do not create a heavy particle system for every keypress.

A typing game can generate many input events per second.

Recommended approach:

```text
Object Pool
```

Example:

```ts
const glyphParticlePool = new ParticlePool(200);
```

On keypress:

```ts
pool.acquire(...)
```

When particle expires:

```ts
pool.release(...)
```

Avoid repeatedly:

```text
new Particle()
destroy()
new Particle()
destroy()
```

for every keypress.

This can cause:

- GC spikes,
- frame instability,
- memory churn.

---

# 11. Recommended Rendering Strategy

The correct implementation depends on the current game renderer.

## Option A — DOM/CSS

Good for:

- standard typing practice UI,
- low-effect modes,
- accessibility-heavy interfaces.

Can implement:

- color,
- transform,
- text-shadow,
- opacity,
- CSS keyframes.

Advantages:

- simple,
- readable,
- accessible,
- easy responsive layout.

Disadvantages:

- many particles/effects become expensive,
- bloom and complex VFX are limited.

---

## Option B — Canvas / PixiJS

Recommended for action-game typing interfaces if the game already uses canvas/WebGL.

PixiJS can handle:

- per-glyph display objects,
- filters,
- particles,
- blend modes,
- GPU rendering,
- glow/bloom,
- energy trails.

PixiJS is MIT licensed.

Useful companion:

```text
pixi-filters
```

which provides filters such as:

- GlowFilter
- BloomFilter
- AdvancedBloomFilter
- GlitchFilter
- ColorOverlayFilter
- AdjustmentFilter

For our action games, this is a strong candidate.

---

## Option C — Hybrid

Potentially best architecture:

```text
DOM
 └── learning text / IPA / translation / accessible semantics

Canvas / PixiJS
 └── glow
 └── particles
 └── energy
 └── combat effects
```

This avoids sacrificing readability for VFX.

However, synchronization must be designed carefully.

---

# 12. Animation Libraries

Potential tools:

## Motion

Useful for:

- DOM per-character transform,
- scale,
- opacity,
- spring animation,
- timelines.

License:

```text
MIT
```

Good for:

```text
typing practice / UI-heavy mode
```

---

## PixiJS

Useful for:

- game canvas,
- text,
- particles,
- filters,
- GPU rendering.

License:

```text
MIT
```

Recommended for:

```text
action-oriented typing gameplay
```

---

## pixi-filters

Useful filters:

```text
GlowFilter
BloomFilter
AdvancedBloomFilter
GlitchFilter
ColorOverlayFilter
```

Recommended particularly for the Typing Break-like glow/flash feeling.

---

## tsParticles

Can create:

- particles,
- bursts,
- confetti,
- background effects.

License:

```text
MIT
```

However, for frequent per-key effects inside an action game, a small custom pooled particle emitter may be more efficient and easier to control.

---

# 13. Do Not Overuse Bloom

A common mistake is:

```text
more glow = better VFX
```

This is false.

Too much bloom causes:

- blurred glyphs,
- difficult reading,
- visual fatigue,
- loss of hierarchy,
- poor IPA/translation readability.

Recommended hierarchy:

```text
pending glyph       = low/no glow
active glyph        = moderate highlight
just typed glyph    = short strong pulse
completed glyph     = stable low glow
word complete       = short strong whole-word glow
critical/perfect    = strongest controlled effect
```

---

# 14. Typography Requirements

Visual effects cannot compensate for poor text rendering.

Requirements:

- stable glyph positions,
- no layout shift when scale changes,
- sufficient letter spacing,
- readable at high speed,
- clear active character,
- correct Vietnamese diacritics,
- correct IPA rendering,
- no clipping from glow/scale.

Important:

Scale animations must not affect layout.

Use transform-based animation.

Do not change font-size per hit.

---

# 15. Accessibility / Reduced Effects

Add an effect intensity setting.

Suggested:

```text
Typing VFX
  Off
  Low
  Normal
  High
  Ultra
```

Recommended defaults:

```text
Normal
```

Low:

- color change,
- small scale,
- no particles.

Normal:

- flash,
- glow,
- few particles.

High:

- stronger particles,
- energy transfer.

Ultra:

- richer VFX,
- stronger combo effects.

Also support:

```text
prefers-reduced-motion
```

Reduce:

- shake,
- particle counts,
- movement,
- scaling.

Preserve essential correctness feedback.

---

# 16. Keypress Audio — What Monkeytype Does Well

The second important system is keypress sound.

Common names:

- Keypress Sound
- Keystroke Sound
- Typing Sound
- Keyboard Sound Profile
- Typing Sound Profile

The important idea is **not simply playing one identical click file on every key**.

A better system uses:

```text
sound profile
   ↓
multiple variants
   ↓
random sample selection
   ↓
small controlled variation
```

This reduces repetition fatigue.

---

# 17. Monkeytype as a Reference

Monkeytype exposes a `playSoundOnClick` system and has multiple selectable sound styles.

Its source shows profiles that can contain multiple sound files, with several profiles containing up to ten samples.

The click sound configuration generates paths like:

```text
sounds/click<profile>/<variant>.wav
```

Monkeytype then selects a random sound from the selected profile when playing a click.

Conceptually:

```text
keypress
   ↓
selected profile
   ↓
random sample
   ↓
play immediately
```

This is a strong interaction design reference.

We should study the architecture, but avoid blindly copying Monkeytype sound assets into independent projects.

Monkeytype source repository is GPL-3.0.

---

# 18. Why Multiple Samples Matter

Imagine one sound:

```text
click.wav
```

played 1,000 times.

The brain quickly notices exact repetition.

It becomes synthetic and annoying.

Instead:

```text
click01.wav
click02.wav
click03.wav
click04.wav
click05.wav
click06.wav
click07.wav
click08.wav
```

Random selection creates:

```text
01
05
02
07
03
03
08
04
...
```

The result feels more physical.

Further variation can include:

```text
pitch       ± small amount
volume      ± small amount
stereo pan  tiny variation, optional
```

Do not exaggerate randomization.

The objective is:

```text
natural variation
```

not:

```text
every key sounds completely different
```

---

# 19. Proposed Typing Sound Profiles

Create our own profiles.

Example base set:

```text
01_soft
02_clean
03_mechanical
04_clicky
05_deep
06_typewriter
07_arcade
08_sci_fi
09_energy
10_magic
11_fantasy
12_cultivation
```

Game-specific themes can extend them.

---

## Space Typing

Possible profiles:

```text
Nebula Soft
Quantum Click
Plasma Key
Starship Console
Cyber Crystal
```

---

## Cultivation / Fantasy

Possible profiles:

```text
Spirit Tap
Jade Click
Qi Pulse
Sword Resonance
Arcane Rune
```

---

## Defense

Possible profiles:

```text
Wooden Command
Steel Command
Crystal Command
Rune Command
```

The typing sound should support the game theme without overpowering pronunciation/audio-learning content.

---

# 20. Audio Event Hierarchy

Like visuals, audio should also have hierarchy.

## Character

```text
small keypress sound
```

## Incorrect Character

```text
different soft error cue
```

## Word Complete

```text
slightly stronger completion cue
```

## Perfect Word

```text
special success layer
```

## Combo Milestone

```text
optional tonal layer
```

## Skill Trigger

```text
combat sound, separate from typing sound
```

Do not make every character sound like an attack.

Keep typing sound:

```text
short
dry
responsive
low-volume
```

Combat audio can be larger.

---

# 21. Audio Latency Is Critical

A keypress sound played late feels wrong even if the sample is excellent.

Goal:

```text
keypress → perceived audio response immediately
```

Avoid:

```text
keypress
  ↓
async fetch file
  ↓
decode
  ↓
play
```

during gameplay.

Instead:

```text
load selected sound profile before gameplay
   ↓
decode/preload
   ↓
keypress
   ↓
play cached sound
```

---

# 22. Recommended Audio Technology

## Option A — Howler.js

Strong candidate.

Benefits:

- mature,
- browser-focused,
- simple API,
- handles playback compatibility,
- audio pooling/caching patterns,
- MIT license.

Monkeytype itself currently uses Howler in its sound controller.

Recommended when using recorded samples.

---

## Option B — Web Audio API

Use directly for:

- generated tones,
- oscillators,
- pitch control,
- gain envelopes,
- filtering,
- dynamic sound generation.

Useful nodes include:

```text
AudioContext
GainNode
OscillatorNode
BiquadFilterNode
AudioBufferSourceNode
StereoPannerNode
```

Advantages:

- no third-party dependency required for basic synthesis,
- powerful,
- very low-level control,
- generated sounds avoid external sample licensing issues.

---

## Recommended Hybrid

```text
Howler.js
   └── sample-based keyboard sounds

Web Audio API
   └── synthetic layers
   └── combo tone
   └── energy tone
   └── procedural variation
```

This is likely the best overall architecture.

---

# 23. Procedural Keypress Sound

Not every sound profile needs recorded assets.

A synthetic profile can use:

```text
oscillator
+
very short gain envelope
+
filter
+
optional noise burst
```

Example conceptual envelope:

```text
attack:  0–3 ms
decay:   20–60 ms
release: very short
```

The generated tone can vary slightly by key or row.

Example:

```text
QWERTY row 1 → frequency range A
home row    → frequency range B
bottom row  → frequency range C
```

Or keep frequency random within a narrow musical scale.

This can create unique profiles with no external recorded sound asset.

---

# 24. Safe Licensing Strategy

For reusable core game systems, prefer:

```text
CODE
  MIT / BSD / similarly permissive libraries

AUDIO
  self-produced
  procedural generated
  CC0
```

Be cautious with assets that are only described as:

```text
free
royalty-free
free download
```

Those terms alone do not necessarily mean unrestricted reuse.

Each asset should have a recorded source and license.

---

# 25. Useful Free Audio Source — OpenGameArt Keyboard Soundpack #1

One promising example:

```text
Keyboard Soundpack #1 [Typing and Single Keystrokes]
```

The pack states:

```text
License: CC0
```

and includes:

```text
32 single keypress sounds
10 human typing sounds
7 generated typing sounds
```

The page says the keyboard was a Cherry KC 1000 and the recording used a Shure SM7B.

This is useful as:

- a prototype sound pool,
- a baseline typing profile,
- a reference for our own recorded/generated set.

Because it is CC0, it is substantially easier to reuse than assets with attribution/share-alike requirements.

Still keep the source/license record in our project documentation.

---

# 26. Proposed Asset Manifest

Do not place random downloaded sounds in the game without metadata.

Use something like:

```json
{
  "id": "keyboard_cc0_01",
  "name": "Keyboard CC0 Base",
  "source": "OpenGameArt",
  "sourceUrl": "...",
  "license": "CC0",
  "author": "unicaegames",
  "files": [
    "key-01.wav",
    "key-02.wav"
  ]
}
```

For our own generated assets:

```json
{
  "id": "space_quantum_01",
  "name": "Quantum Click",
  "source": "in-house",
  "license": "project-owned",
  "generation": "procedural"
}
```

This prevents future licensing confusion.

---

# 27. Audio Profile Architecture

Suggested structure:

```text
typing-feedback/
├── audio/
│   ├── engine/
│   │   ├── TypingAudioEngine.ts
│   │   ├── AudioPool.ts
│   │   ├── AudioProfile.ts
│   │   └── ProceduralKeySynth.ts
│   │
│   ├── profiles/
│   │   ├── soft/
│   │   ├── mechanical/
│   │   ├── sci-fi/
│   │   └── magic/
│   │
│   └── manifests/
│       └── audio-assets.json
```

Example profile:

```ts
interface TypingSoundProfile {
  id: string;
  samples?: string[];
  volume: number;
  randomPitch?: number;
  randomVolume?: number;
  mode: "samples" | "procedural" | "hybrid";
}
```

---

# 28. Shared TypingFeedbackEngine

Recommended top-level architecture:

```text
TypingFeedbackEngine
│
├── VisualFeedbackController
│   ├── GlyphAnimator
│   ├── GlyphGlowController
│   ├── GlyphParticleEmitter
│   ├── WordCompletionEffect
│   ├── ComboEffect
│   └── ErrorEffect
│
├── AudioFeedbackController
│   ├── KeypressSoundEngine
│   ├── ErrorSoundEngine
│   ├── WordCompleteSound
│   ├── ComboSound
│   └── SoundProfileManager
│
├── FeedbackIntensityController
│
└── FeedbackEventBus
```

Typing logic emits semantic events.

Example:

```ts
feedback.emit({
  type: "glyph-correct",
  glyphIndex: 4,
  position: { x, y },
  combo: 12,
  timestamp: performance.now()
});
```

The feedback engine reacts.

---

# 29. Critical Architectural Rule

The feedback system must **never own typing correctness**.

Bad:

```text
VFX system decides whether input is correct.
```

Good:

```text
TypingEngine
   ↓
produces semantic event
   ↓
TypingFeedbackEngine
   ↓
renders feedback
```

This keeps systems independent.

Example events:

```ts
type TypingFeedbackEvent =
  | GlyphCorrectEvent
  | GlyphIncorrectEvent
  | GlyphCorrectedEvent
  | WordProgressEvent
  | WordCompleteEvent
  | PerfectWordEvent
  | ComboChangedEvent
  | ComboMilestoneEvent
  | TypingResetEvent;
```

---

# 30. Why an Event-Based Architecture Matters

Different games can react differently to the same typing event.

Example:

```text
glyph-correct
```

Space Typing:

```text
blue plasma spark
```

Cultivation:

```text
golden qi spark
```

Defense:

```text
small command rune
```

Practice mode:

```text
simple white scale pulse
```

Same event.

Different skin.

Therefore:

```text
TypingFeedbackEngine = shared behavior
Theme = game-specific appearance
```

---

# 31. Theme Configuration

Example:

```ts
interface TypingFeedbackTheme {
  glyphCorrect: {
    glowStrength: number;
    scalePeak: number;
    particlePreset: string;
  };

  glyphError: {
    shakeStrength: number;
    particlePreset: string;
  };

  wordComplete: {
    flashStrength: number;
    burstPreset: string;
  };

  audioProfile: string;
}
```

Possible themes:

```text
space
fantasy
cultivation
defense
minimal
practice
```

---

# 32. Intensity Scaling

Effects can respond to gameplay state.

Example:

```text
combo 0–4
   ↓
normal

combo 5–9
   ↓
+10% glow

combo 10–19
   ↓
+particles

combo 20+
   ↓
stronger energy trail
```

Do not simply increase everything infinitely.

Use capped curves.

Example:

```ts
const comboFactor = Math.min(combo / 20, 1);
```

---

# 33. Performance Budget

Typing feedback must remain stable during:

- high WPM,
- multiple enemies,
- projectiles,
- animated backgrounds,
- VFX-heavy combat.

Recommended target:

```text
60 FPS minimum
```

where hardware allows.

For capable devices:

```text
120 FPS compatibility
```

Important optimizations:

- object pooling,
- avoid allocations per key,
- reuse filters,
- reuse audio buffers,
- avoid DOM layout on keypress,
- use transforms,
- cap particles,
- avoid excessive blur radius,
- avoid creating AudioContext repeatedly,
- preload selected sound profile only,
- optional quality levels.

---

# 34. Feedback Quality Levels

Suggested runtime quality:

```text
Low
Medium
High
Ultra
```

Low:

```text
simple color
scale
no particles
minimal glow
```

Medium:

```text
small glow
few particles
```

High:

```text
bloom
energy particles
trails
```

Ultra:

```text
richer effects
more particles
additional word-complete distortion
```

Gameplay logic remains identical.

---

# 35. Visual and Audio Must Be Synchronized

A good keypress should feel like one event.

Bad:

```text
0 ms    glyph reacts
90 ms   sound plays
```

Better:

```text
0 ms    input accepted
0–10 ms visual starts
0–15 ms audio starts
```

Exact browser/audio timing will vary, but perceived synchronization is important.

Both systems should consume the same feedback event.

---

# 36. Suggested Event Flow

Example correct character:

```text
keydown
   ↓
TypingEngine.validate()
   ↓
result = correct
   ↓
FeedbackEventBus.emit("glyph-correct")
   ├─────────────┬─────────────┐
   ↓             ↓             ↓
Glyph VFX     Keypress SFX   Combo logic
   ↓             ↓
particles      audio pool
glow
scale
```

Word complete:

```text
last glyph correct
   ↓
TypingEngine emits:
   glyph-correct
   word-complete
   ↓
Character effect
   +
Word completion effect
   +
Completion sound
   +
Gameplay attack event
```

---

# 37. Important: Avoid Double-Feedback Chaos

When the final character completes a word, several effects may happen at once.

Possible problem:

```text
glyph explosion
+
word explosion
+
combo explosion
+
attack explosion
+
screen shake
+
damage flash
```

Result:

```text
visual noise
```

Need effect arbitration.

Example:

```text
word complete suppresses some normal glyph particles
combo milestone upgrades word-complete effect instead of adding another full effect
```

Use:

```text
effect priority
```

Suggested:

```text
glyph            priority 1
word complete    priority 2
perfect          priority 3
combo milestone  priority 4
boss finisher    priority 5
```

Higher-level effects may replace lower-level layers.

---

# 38. Learning UI Protection

Our games can display:

- target word,
- IPA,
- pronunciation,
- Vietnamese translation,
- learning hints.

These must remain readable.

Therefore define protected zones.

Example:

```text
TypingTextZone
IPAZone
TranslationZone
```

Particles should not remain over these zones for long.

Strong combat VFX should occur:

```text
behind text
or
outside text
```

unless it is the brief glyph effect itself.

---

# 39. Proposed UI Settings

Example settings panel:

```text
Typing Feedback
──────────────────────────────

Typing VFX
[ Off | Low | Normal | High | Ultra ]

Keypress Sound
[ Off | On ]

Sound Profile
[ Soft ▼ ]

Typing Sound Volume
[──────●────]

Error Feedback
[ On ]

Word Complete Effect
[ On ]

Combo Effects
[ On ]
```

Game themes may expose different profile choices.

---

# 40. MVP Recommendation

Do not implement everything at once.

## Phase 1 — Core Character Feedback

Implement:

- per-character representation,
- correct flash,
- scale punch,
- active glyph highlight,
- error state,
- reduced motion support.

Success criteria:

```text
Typing instantly feels more responsive.
```

---

## Phase 2 — Glow + Small Particles

Implement:

- glow pulse,
- pooled particles,
- effect intensity setting.

Success criteria:

```text
Fast typing remains readable and smooth.
```

---

## Phase 3 — Word Completion

Implement:

- whole-word pulse,
- energy convergence,
- word completion VFX.

Success criteria:

```text
Completing a word feels meaningfully stronger than typing one character.
```

---

## Phase 4 — Keypress Audio

Implement:

- sound profile manager,
- preload,
- random variant selection,
- volume setting,
- error sound,
- word-complete sound.

Start with:

```text
1 CC0 sample profile
1 procedural profile
```

Success criteria:

```text
No obvious repeated-click fatigue.
No noticeable latency.
```

---

## Phase 5 — Theme System

Implement:

```text
space theme
minimal theme
```

Then prove that the same event system can render both.

Success criteria:

```text
shared core requires no game-specific branching.
```

---

## Phase 6 — Advanced Energy / Combo

Implement:

- energy travel,
- combo intensity,
- perfect-word effect,
- attack synchronization.

---

# 41. What Claude Should Review

Claude should not merely say whether this idea is good.

Please review the following specific questions.

## Architecture

1. Is `TypingFeedbackEngine` the right abstraction?
2. Should visual and audio feedback share one event bus?
3. Should the shared package be game-agnostic?
4. What existing typing architecture should own event emission?
5. How can this integrate without breaking current typing rules?

## Rendering

6. What renderer is currently used in each game?
7. Should glyphs remain DOM, PixiJS, or hybrid?
8. What is the lowest-risk way to add per-glyph effects?
9. Are pixi-filters appropriate for the current renderer?
10. How should particle pooling be implemented?

## Performance

11. What is the maximum expected key event rate?
12. What effect budget is safe during combat?
13. What should be disabled on low-end hardware?
14. How should FPS degradation be detected?
15. How should animations behave at 120+ WPM?

## Audio

16. Is Howler already installed anywhere?
17. Would direct Web Audio be preferable in the existing stack?
18. How should sounds be preloaded?
19. How many simultaneous keypress sounds should be allowed?
20. How should overlapping sounds be capped/pooled?

## UX

21. Is the suggested feedback hierarchy correct?
22. Are error effects too distracting?
23. How can IPA/translation remain readable?
24. Should combo effects modify or replace normal key effects?
25. What should the default VFX/audio intensity be?

## Licensing

26. Audit every proposed dependency.
27. Do not assume “free” means safe.
28. Record asset source/license in a manifest.
29. Avoid blindly copying Monkeytype assets into independent projects.
30. Prefer our own procedural/CC0 audio assets.

---

# 42. Acceptance Criteria

A first production-quality version should satisfy:

### Responsiveness

- glyph reacts immediately after valid input,
- no animation blocks future keys,
- no obvious audio delay.

### Readability

- active glyph remains clear,
- IPA remains readable,
- translation remains readable,
- effects do not obscure next letters.

### Performance

- no major FPS drop during fast typing,
- particle system does not allocate excessively,
- audio does not create uncontrolled overlap.

### Visual Hierarchy

The player can visually distinguish:

```text
normal character
wrong character
word complete
perfect word
combo milestone
```

### Audio Hierarchy

The player can audibly distinguish:

```text
normal key
error
word complete
```

without sound becoming tiring.

### Reusability

At least two themes can use the same feedback engine without copying core logic.

---

# 43. Suggested Prototype Test

Build a standalone debug scene before integrating deeply into combat.

Scene:

```text
Target:
interstellar

IPA:
example placeholder

Translation:
example placeholder
```

Debug controls:

```text
VFX intensity
particle count
glow strength
scale strength
animation duration
sound profile
volume
combo
simulate perfect
simulate error
```

Show performance:

```text
FPS
active particles
active sounds
keypress events/sec
```

This allows Claude/us to tune game feel without repeatedly entering full gameplay.

---

# 44. A/B Comparison Requirement

Prototype should include:

```text
A = current typing feedback
B = new typing feedback
```

Allow instant switching.

Evaluate:

- responsiveness,
- readability,
- perceived impact,
- fatigue after several minutes,
- distraction,
- FPS.

The system should not be accepted merely because screenshots look better.

It must feel better during actual typing.

---

# 45. Suggested Initial Tuning

Starting values only:

```text
glyph scale peak:       1.08–1.14
glyph flash:            40–80 ms
glyph settle:           100–160 ms
particle count/key:     2–4
particle life:          120–300 ms
word complete:          180–350 ms
error shake:            40–90 ms
```

Audio:

```text
keypress variants:      6–12
keypress volume:        low
pitch randomization:    subtle
volume randomization:   subtle
```

These must be adjusted by playtesting.

---

# 46. What NOT to Do

Avoid these implementation mistakes.

## Visual

Do not:

- make every key explode,
- use full-screen flashes per key,
- use strong camera shake per key,
- animate font-size causing layout shift,
- blur text excessively,
- spawn unlimited particles,
- wait for animation completion before accepting another key,
- mix typing correctness into VFX code.

## Audio

Do not:

- load a file from network on each key,
- play one exact click thousands of times,
- use very loud mechanical clicks by default,
- let dozens of old key sounds overlap indefinitely,
- use unclear-license audio,
- assume Monkeytype assets can simply be copied everywhere.

---

# 47. Recommended Technical Direction

Initial recommendation for Claude to validate against the existing codebase:

```text
TypingEngine
   ↓
TypingFeedbackEventBus
   ↓
┌───────────────────────────────┐
│ TypingFeedbackEngine          │
├───────────────────────────────┤
│ VisualFeedbackController      │
│ AudioFeedbackController       │
│ FeedbackIntensityController   │
│ ThemeController               │
└───────────────────────────────┘
         ↓               ↓
    Pixi/DOM VFX     Howler/WebAudio
```

For action games:

```text
Visual:
PixiJS + lightweight custom pooled particles
+ selected pixi-filters where justified

Audio:
Howler.js for sample playback
+ Web Audio API for procedural/synthetic layers
```

For practice/minimal typing:

```text
DOM/CSS or Motion
+ reduced feedback profile
```

---

# 48. Long-Term Opportunity

If implemented cleanly, this should become a reusable internal framework rather than a one-game feature.

Potential package:

```text
packages/typing-feedback/
```

with:

```text
core/
visual/
audio/
themes/
adapters/
```

Games consume it through adapters.

Example:

```text
SpaceTypingAdapter
DefenseTypingAdapter
CultivationTypingAdapter
PracticeTypingAdapter
```

This gives future typing games a high-quality baseline immediately.

---

# 49. Final Design Goal

The final experience should make the player feel:

```text
I press a key
→ the game instantly acknowledges me

I type accurately
→ energy visibly builds

I complete a word
→ the game releases that energy

I maintain a streak
→ the world responds more strongly
```

The system should reinforce the central fantasy:

> **Typing is not a UI operation. Typing is the player's weapon/action system.**

Visual feedback, audio feedback, combat feedback, and learning feedback should all support that idea without sacrificing readability or performance.

---

# 50. Reference Links / License Notes

These links are for Claude to independently verify before implementation.

## Visual / animation

### PixiJS
https://github.com/pixijs/pixijs

Current repository states MIT license.

### PixiJS Filters
https://github.com/pixijs/filters

Includes filters such as BloomFilter, AdvancedBloomFilter, GlowFilter, GlitchFilter, etc.

### Motion
https://github.com/motiondivision/motion

Open-source animation library for JavaScript/React/Vue. Repository states MIT license.

### tsParticles
https://github.com/tsparticles/tsparticles

Particle library. Repository states MIT license.

---

## Audio

### Howler.js
https://github.com/goldfire/howler.js

Browser audio library. Repository states MIT license.

### Web Audio API
https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API

Native browser audio API.

### OpenGameArt — Keyboard Soundpack #1
https://opengameart.org/content/keyboard-soundpack-1-typing-and-single-keystrokes

Page currently lists:

```text
License: CC0
32 single keypress sounds
10 human typing sounds
7 generated sounds
```

Good candidate for prototype/reference.

---

## Reference implementation

### Monkeytype
https://github.com/monkeytypegame/monkeytype

Useful files to inspect include concepts around:

```text
playSoundOnClick
sounds configuration
sound controller
random click-sample selection
Howler usage
Web Audio oscillator usage
```

The repository is currently GPL-3.0 licensed.

Use it as an architectural/reference study unless the license implications of copying code/assets are intentionally accepted.

---

# 51. Request to Claude

Please perform a critical review of this proposal against the **current live codebase**, not only against this document.

Required review output:

1. Current typing rendering architecture.
2. Current renderer/library stack.
3. Existing feedback/VFX code that can be reused.
4. Existing audio stack that can be reused.
5. Conflicts or weaknesses in this proposal.
6. Better alternatives if available.
7. Recommended final architecture.
8. Exact integration points.
9. Performance risks.
10. Licensing/dependency risks.
11. Implementation phases.
12. Files/modules likely to be created or modified.
13. Test plan.
14. Rollback strategy.
15. Recommendation: APPROVE / APPROVE WITH CHANGES / REJECT.

Do **not** begin a large refactor solely because this document suggests one.

First inspect the live project and determine whether the same result can be achieved with lower complexity.

The priority order is:

```text
1. typing correctness
2. input latency
3. readability / learning UX
4. stable performance
5. satisfying feedback
6. visual spectacle
```

Visual spectacle must never damage items 1–4.
