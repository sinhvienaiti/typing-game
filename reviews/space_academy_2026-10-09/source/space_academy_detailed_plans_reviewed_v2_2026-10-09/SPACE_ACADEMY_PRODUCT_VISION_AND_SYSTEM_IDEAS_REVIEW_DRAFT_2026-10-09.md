# SPACE ACADEMY / LEARNING UNIVERSE
## Product Vision, System Ideas & Design Direction — Consolidated Review Draft

**Status:** Concept / architecture review draft  
**Date:** 2026-10-09  
**Purpose:** Consolidate the full set of ideas discussed so this document can be reviewed, challenged, simplified, and converted into implementation master plans later.

---

# 0. Executive Summary

The product should **not** be designed as “Space Typing with some English lessons added”.

The stronger long-term direction is:

> **A living online English-learning platform with a game-inspired world, social structure, identity, rewards, prestige, events, and multiple learning/game activities.**

In this model:

- **Learning is the core value.**
- **Classes and social relationships are the strongest retention layer.**
- **Identity, cosmetics, collections, rewards, shops, events, prestige, and customization make the experience enjoyable and memorable.**
- **Space Typing becomes one game/activity module inside the broader ecosystem.**
- The platform should borrow useful **meta-systems** from long-running online games—identity, shops, limited cosmetics, rankings, events, collections, social loops—but **must not become an MMO**.
- The main mental model can be a **small digital academy / school**, because people already understand classes, teachers, lessons, timetables, breaks, exams, clubs, competitions, and graduation.
- The product must remain **simple on the surface and deep underneath**.
- The world should feel alive even for a solo learner, but the platform must never fake real users. NPC/AI characters should be clearly presented as NPC/AI.
- Visuals, audio, VFX, avatar identity, and reward presentation are not side features. They are part of the **brand spine**.
- For avatars, the current preferred technical direction is **2D modular characters with light skeletal/transform animation**, not 3D and not free-roaming characters.

The central product philosophy is:

> **Learning first. Social second. Identity and rewards make both more enjoyable. Games are optional experiences around them.**

And the key retention loop is:

```text
LEARN
  ↓
MASTER
  ↓
EARN
  ↓
COLLECT / CUSTOMIZE
  ↓
SOCIALIZE / COMPETE
  ↓
UNLOCK
  ↓
RETURN TO LEARN
```

---

# 1. Product Reframing

## 1.1 Previous mental model

The project originally risked being framed as:

```text
SPACE TYPING
├── Combat
├── English lessons
├── Vocabulary
├── Listening
└── Other learning modes
```

That framing is now considered too narrow. It makes the typing combat game feel like the main product and learning/social systems feel secondary.

## 1.2 Preferred mental model

The broader platform is the main product.

```text
LEARNING UNIVERSE / SPACE ACADEMY
│
├── Learning Core
│   ├── Core English A1–C2
│   ├── IELTS
│   ├── Vocabulary
│   ├── Grammar
│   ├── Reading
│   ├── Listening
│   ├── Speaking
│   ├── Writing
│   ├── Recall
│   └── Typing
│
├── Classes & Social
│
├── Identity & Customization
│
├── Rewards / Economy / Shops
│
├── Prestige / Rankings / Events
│
└── Activities & Game Modes
    ├── Space Typing
    ├── Typing races
    ├── Vocabulary games
    ├── Recall games
    ├── Listening games
    ├── Survival challenges
    └── Future modules
```

Space Typing remains important because substantial work has already gone into its UI, visuals, audio, combat feel, backgrounds, bosses, effects, progression, and related systems. However, it is better viewed as:

> **one powerful learning/game activity inside the larger platform, not the whole platform itself.**

---

# 2. What We Borrow From Online Games — And What We Do Not

The user referenced long-running online RPGs only as examples of **why players keep returning for years**. The intention is **not** to copy an MMO.

## 2.1 Systems worth learning from

- Strong user identity
- Avatar customization
- Clothing / cosmetics
- Frames, titles, badges
- Collectible items
- Shops
- Limited-time items
- Seasonal items
- Achievement-exclusive rewards
- Leaderboards
- Rankings
- Scheduled events
- Social groups
- Friends
- Class/group chat
- Community competition
- Collections
- Reward loops
- Prestige
- Rare ownership history
- Reasons to return daily/weekly/seasonally

## 2.2 Systems we should not add without a strong product reason

- Massive open world
- Free-roaming MMO gameplay
- Deep weapon enhancement
- Gear power escalation
- Dozens of currencies
- Complex crafting trees
- Pet breeding systems
- Territory wars
- Huge RPG skill trees
- Hundreds of mandatory daily quests
- Heavy combat progression unrelated to learning
- Systems copied simply because another online game has them

A feature should generally satisfy at least two of the following:

1. Does it make learning more attractive or effective?
2. Does it improve identity, social connection, or retention?
3. Is the value worth the implementation/performance/product complexity?

If the answer is unclear, the feature should not be built.

---

# 3. Core Product Principles

## 3.1 Depth without complexity at the surface

The product can eventually contain many systems, but users should not see all of them at once.

A beginner should be able to use:

```text
Learn
Practice
Play
Profile
```

without understanding prestige systems, seasonal events, collectibles, advanced rankings, class resources, special shops, etc.

Advanced systems should appear only when relevant.

## 3.2 Progressive disclosure

Examples:

- IELTS appears when the user chooses IELTS as a goal.
- Classroom systems appear after joining a class.
- Social systems expand after users add friends.
- Events become more visible after the learner has basic familiarity.
- Competitive systems become more visible to users who show interest in them.

The interface should **grow with the user** instead of forcing the user to learn the entire product on day one.

## 3.3 Learning must remain readable and calm

The product should have a strong sci-fi / academy identity, but content surfaces must remain comfortable.

Rule:

> **Science-fiction identity at the shell; clarity at the content surface.**

Examples:

- Reading screen → almost like a high-quality e-book.
- Typing screen → minimal and focused.
- IELTS exam → serious and distraction-free.
- Reward, profile, event, class, shop → richer visual personality.

## 3.4 Every feature must earn its visual weight

The most important current action should dominate.

```text
Current learning task     Priority 1
Primary action            Priority 1
Progress                  Priority 2
Rewards                   Priority 3
Social                    Priority 3
Events                    Priority 4 unless active
Shop promotion            Priority 5
```

The shop must never visually overpower the learning task.

## 3.5 Gamification must not become manipulation

Avoid:

- Punishing users for missing a day
- Destroying long streaks after one missed session
- Excessive popups
- Fake scarcity
- Fake player activity
- Rewarding AFK
- Making users feel they must schedule their life around the platform
- Selling status that should represent genuine achievement

Prefer:

- Positive reinforcement
- Optional live bonuses
- Async/replay alternatives
- Clear scarcity rules
- Honest AI/NPC labeling
- Persistent knowledge progression

---

# 4. Target User Personas

The platform should support multiple types of users.

## 4.1 Casual learner

- 10–20 minutes/day
- Wants English improvement without complexity
- May not care about competition or social features

Needs:

- One-click continue
- Daily learning plan
- Clean interface
- Simple progress
- Optional rewards

## 4.2 Serious English learner

Needs:

- Structured CEFR progression
- Vocabulary
- Grammar
- Reading
- Listening
- Speaking
- Writing
- Recall
- Strong learning analytics

## 4.3 IELTS learner

Needs:

- Goal-based preparation
- Academic/General track
- Timed practice
- Skill breakdown
- Mock exams
- Estimated band practice feedback
- Serious exam mode

## 4.4 Typing enthusiast

Needs:

- Minimal typing surface
- WPM / accuracy
- Personal bests
- Deep settings
- Themes
- Custom visual/sound profiles
- Leaderboards
- Advanced statistics

## 4.5 Social learner / social gamer

Needs:

- Class
- Friends
- Clubs
- Chat
- Class competition
- Events
- Group activities
- Cosmetics
- Prestige

## 4.6 Teacher / administrator

Needs:

- Class creation
- Lesson creation
- Scheduling
- Progress monitoring
- Student management
- Moderation
- Exam configuration
- Rewards
- Event management
- Content publishing

These personas should share the same platform but not be forced into the same interface complexity.

---

# 5. Experience Styles

A useful product-level setting:

```text
EXPERIENCE STYLE

Focus
Balanced
Immersive
```

## Focus

For serious learners:

- Minimal animation
- Minimal reward interruptions
- Reduced social notifications
- No decorative event interruptions
- Clean study surfaces

## Balanced

Default:

- Learning + light rewards
- Light social presence
- Events visible but not intrusive
- Reasonable animation

## Immersive

For users who enjoy the game/social layer:

- Richer world presentation
- NPC reactions
- Visual effects
- Event surfaces
- Collections
- Social activity
- Deeper cosmetics

The same platform can therefore appeal to people who love games and people who simply want to study.

---

# 6. School / Academy as the Organizing Metaphor

A major idea is to use a **small digital school/academy model** because the structure is naturally understandable.

The platform does not need to simulate a school physically. It uses the school model to organize complexity.

```text
Student
├── Class
├── Homeroom teacher
├── Subject teachers
├── Timetable
├── Lessons
├── Breaks
├── Friends
├── Clubs
├── Exams
├── Competitions
├── School events
└── Graduation
```

This helps organize many features that otherwise feel like unrelated game systems.

---

# 7. Space Academy Areas

Potential conceptual areas:

- Classroom
- Practice Lab
- Language Lab
- Simulation Lab
- Writing Room
- Library / Codex
- Academy Store
- Clubs
- Event area
- Exam Center
- Profile / Student Record
- Activities / Games

These can remain normal web screens. No free-roaming campus is required.

---

# 8. Class System

The class is one of the most important long-term retention systems because people return for people they know.

A class should not be only:

```text
Name
Member list
Chat
Assignments
```

It should have identity and history.

## 8.1 Example class

```text
CLASS ORION-7

Level: B1 → B2
Track: General English
Members: 24
Teacher: Professor Lyra
Specialty: Science & Technology
Class Rank: Silver III
```

## 8.2 Class identity

Potential class-specific elements:

- Name
- Banner
- Crest
- Color/theme
- Background
- NPC / teacher
- Soundtrack
- Topic personality
- Trophy shelf
- Class history
- Current goals

Classes can reuse a shared visual kit with different themes instead of requiring completely unique assets.

## 8.3 Suggested class size

Initial target:

> approximately 15–30 learners per main class.

Reasons:

- Small enough to remember classmates
- Large enough for social activity
- Teacher can manage it
- Rankings remain meaningful
- Chat remains readable

A user might belong to:

- 1 main class
- optional course(s)
- 1 club/crew-like social group

Avoid encouraging users to join dozens of classes.

---

# 9. Teacher Roles

## 9.1 Homeroom teacher

The class has a main mentor/teacher.

Responsibilities may include:

- Welcome users
- Introduce the day
- Explain class objectives
- Summarize progress
- Encourage learners
- Announce class events
- Guide review

## 9.2 Subject teachers / specialist NPCs

Possible personalities:

- General English mentor
- Grammar professor
- Vocabulary specialist
- Listening specialist
- IELTS teacher
- Writing teacher
- Speaking coach

They should have:

- Visual identity
- Voice identity
- Personality
- Typical reactions
- Teaching style
- Signature audio/VFX cues

---

# 10. NPC / AI Philosophy

NPCs are important because classes and learning environments should not feel empty.

However:

> **AI/NPC characters should never pretend to be real human players.**

They can be extremely natural while still clearly being characters.

Possible label:

```text
Professor Lyra
Academy AI Mentor
```

or lore that makes their AI/NPC nature obvious.

## 10.1 NPC qualities

NPCs can have:

- personality
- voice
- expressions
- memory of learner facts
- time-aware dialogue
- class-aware dialogue
- relationship/reputation
- seasonal outfits
- teaching specialization

## 10.2 Lightweight memory model

Instead of storing every conversation forever, NPCs can remember structured facts:

```text
goal: IELTS 7.0
strong skill: reading
weak skill: articles
preferred activity: listening
recent achievement: 1000 words mastered
last lesson: climate change
```

This is easier to control, cheaper, and more predictable.

## 10.3 NPC schedule illusion

NPC state can change with time:

- Morning
- Class time
- Lunch
- Evening study
- Late-night short session

The system does not need a true life simulation. Small contextual dialogue is enough to make the NPC feel alive.

## 10.4 AI classmates

AI classmates can help early/small classes feel active.

But they must be visibly labeled as AI.

Example:

```text
Nova
AI Cadet
```

AI classmates can differ in:

- personality
- strengths
- weaknesses
- participation frequency
- reaction style
- typical mistakes

They should never be mixed into real-player prestige leaderboards as if they were humans.

---

# 11. Class Time & Lesson Structure

Class time must be designed carefully.

A class should feel like an actual session, not a sequence of random screens.

## 11.1 Standard class example

40-minute format:

```text
00–05  ARRIVAL
       greeting / warm-up

05–10  RECALL
       previous material

10–22  CORE LESSON
       new knowledge

22–30  PRACTICE
       individual / pair / group

30–36  CLASS CHALLENGE
       collaborative / competitive activity

36–40  DEBRIEF
       progress / rewards / next step
```

## 11.2 Different session lengths

### Quick session
10–15 minutes

### Standard session
25–40 minutes

### Live class
45–60 minutes

### Exam
30–180 minutes

### Study hall
Open-ended

The teacher/admin chooses a template.

---

# 12. Lesson as a Sequence, Not a Page

Example B2 lesson:

```text
CLIMATE CHANGE — B2

ARRIVAL
↓
Warm-up question

RECALL
↓
5 phrases from last lesson

DISCOVERY
↓
short reading/audio

LANGUAGE
↓
8 phrases
1 grammar pattern

PRACTICE
↓
typing/listening/recall

COLLABORATION
↓
pair/team activity

CHALLENGE
↓
class mini-game

DEBRIEF
↓
mastery + reward

FOLLOW-UP
↓
scheduled review
```

This makes lessons feel intentional and memorable.

---

# 13. Weekly Class Structure

Example:

```text
MONDAY
Vocabulary + topic introduction

TUESDAY
Reading + listening

WEDNESDAY
Grammar + recall

THURSDAY
Speaking / writing

FRIDAY
Class challenge

SATURDAY
Optional event / game / review

SUNDAY
Review / rest
```

This is a template, not a mandatory rigid schedule.

---

# 14. Lesson Builder

Teacher/Admin should not need code.

Example:

```text
CREATE LESSON

Topic: Climate Change
Level: B2
Duration: 35 min

Objectives:
[x] Vocabulary
[x] Listening
[x] Speaking

New vocabulary: 8
Review vocabulary: 12
Grammar: Cause & effect
Final activity: Team Challenge
```

The system can generate a schedule preview:

```text
Warm-up       4m
Review        5m
Reading       7m
Vocabulary    7m
Listening     5m
Challenge     5m
Debrief       2m
```

If the design is too dense:

```text
Warning: estimated 52 minutes
```

The teacher can drag/drop and edit.

---

# 15. Before / During / After Class

## Before

Show:

- Class start time
- Topic
- Who is online
- Teacher/NPC
- Pre-class warm-up
- Optional waiting area

## During

Switch to focus mode.

- Main lesson dominates
- Chat is secondary
- NPC reactions are subtle
- Social interruptions are reduced

## After

Summary:

```text
CLASS COMPLETE

Personal mastery +12
Class XP +480
Weekly challenge unlocked
```

Then social surfaces can become more visible again.

---

# 16. Break Time

A school-like model provides a natural place for social interaction without interrupting learning.

Break-time actions could include:

- Chat
- Reactions
- Profiles
- Shop browsing
- Outfit change
- Leaderboards
- Quick mini-games
- Friend interaction

This is preferable to having social content constantly compete with the lesson.

---

# 17. Clubs

“Club” may be more understandable than “guild” for many learners.

Examples:

- IELTS Club
- Typing Club
- Science Club
- Reading Club
- Speaking Club
- Gaming Club

A club can provide:

- Community
- Events
- Small challenges
- Shared goals
- Chat
- Cosmetic identity
- Competition

This gives social depth without forcing an MMO metaphor.

---

# 18. Class Progression

The class itself can progress.

Possible systems:

```text
Class XP
Class Level
Class Rank
Class Collection
Class Trophy
Class Theme
Class Achievements
```

Example:

```text
ORION-7
Class Level 18
Next unlock: Observatory Lv.2
Need: 2,400 Class XP
```

Individual learning contributes to shared progress.

This creates a strong reason for learners to feel that their participation matters to the group.

---

# 19. Attendance & Class Participation

Attendance should encourage presence, not punish absence.

Example:

```text
Attendance today
19 / 24
```

A shared bonus may unlock when participation reaches a threshold.

Example:

```text
20+ present
→ +10% Class XP
```

But absent students should still be able to:

- Review the lesson
- Complete async activities
- Keep their individual learning progress

Avoid making real life feel like a failure condition.

---

# 20. Class Competition

Natural school-inspired competitions can include:

- Class mastery
- Average accuracy
- Listening challenge
- Vocabulary challenge
- Typing relay
- Improvement ranking
- Attendance consistency
- Helping score

Example:

```text
ORION-7
vs
GAIA-4
```

Avoid making everything about raw speed.

---

# 21. School Terms / Seasons

An academic term can map naturally to a live-service season.

Example:

```text
ACADEMIC TERM 01
8–12 weeks
```

Contains:

- Curriculum
- Weekly themes
- Midterm
- Final exam
- Class project
- Competitions
- Seasonal cosmetics
- Graduation

Knowledge progression is permanent. Seasonal/competitive layers can reset softly.

---

# 22. Graduation & Alumni

Graduation should be an emotional event.

Example:

```text
B2-07 · TERM 03

24 students
21 graduated
Class mastery 84%
Top student: Lan
Most improved: Minh
Best helper: Huy
```

Permanent commemorative rewards:

- Class photo
- Graduation badge
- Certificate
- Yearbook entry

After graduation:

- Alumni archive
- Old class history
- Past classmates
- Reunion events
- Friend suggestions

The social graph should survive the class term.

---

# 23. Core Learning Tracks

The learning foundation should support:

- Core English A1–C2
- Vocabulary
- Grammar
- Phrases
- Collocations
- Idioms
- Reading
- Listening
- Speaking
- Writing
- Recall
- Typing
- Topic-based learning
- Weak-area practice
- Daily English
- Academic English
- Work/Tech English
- Travel English
- IELTS

---

# 24. IELTS as a First-Class Track

IELTS should be designed as a real track, not a label added to generic lessons.

Possible product:

```text
IELTS EXPEDITION

Current estimated band: 5.5
Target: 7.0
Type: Academic
Target date: ...
```

Skill breakdown:

```text
Listening  5.5 → 7.0
Reading    6.0 → 7.0
Writing    5.0 → 7.0
Speaking   5.5 → 7.0
```

## 24.1 Two IELTS modes

### Training Mode

- Explanations
- Hints
- Rewards
- Learning support
- Practice feedback

### Exam Simulation

- Serious UI
- Authentic timing
- No unnecessary game effects
- No hints
- Minimal interruption

Any AI scoring should be labeled:

> **Estimated Band / Practice Estimate**

unless there is ever an official external certification arrangement.

---

# 25. Mission-Based Learning Structure

Instead of ordinary categories such as Vocabulary/Grammar/Reading/Listening/Speaking/Writing, the platform can package learning into missions.

Example learning rhythm:

```text
SCAN
→ DECODE
→ TRAIN
→ EXECUTE
→ CHALLENGE
→ DEBRIEF
```

Example word:

```text
increasingly
```

Possible flow:

1. Hear pronunciation
2. See IPA/meaning
3. Read context
4. Practice collocation
5. Type/listen/recall
6. Encounter again in activity/game
7. Review mastery

This makes knowledge recur across the platform.

---

# 26. Typing Experience

Typing should be clean by default and inspired by what makes strong typing tools pleasant:

- Text at visual center
- Immediate feedback
- Keyboard-first flow
- Deep settings
- Personalization
- Strong themes
- Minimal default clutter

Example:

```text
SPACE ACADEMY · SIMULATOR

english   60s   adaptive        ⚙

      The development of renewable
      energy has accelerated rapidly
      during the last decade.

          76 WPM      98%

                     TAB → restart
```

## 26.1 Cockpit Studio / Typing customization

### Style
- Theme
- Font
- Font size
- Line height
- Caret
- Word spacing

### Focus
- HUD density
- Dim completed text
- Current-word highlight
- Hide timer
- Hide stats

### Feedback
- Correct sound
- Error sound
- Key sound
- Pronunciation
- Particles

### Environment
- Background
- Stars
- Parallax
- Animation intensity

### Typing
- Forgive corrected errors
- Stop on error
- Confidence mode
- Punctuation
- Numbers
- Language hints

Everything should preview instantly.

## 26.2 Style profiles

Potential presets:

- Focus
- Learning
- Speed
- Immersion
- IELTS

Settings can be remembered per activity.

---

# 27. Personalized Learning Intelligence

## 27.1 Dynamic difficulty

The system can identify weak areas.

Example:

```text
Articles       91%
Past tense     54%
Prepositions   61%
Vocabulary     83%
Listening      72%
```

Then generate a calibration mission focused on weak areas.

## 27.2 Mistake intelligence

Classify mistakes:

- Typo
- Grammar
- Collocation
- Article
- Preposition
- Pronunciation
- Recall failure
- Listening confusion

Example:

```text
recieve → receive      spelling
He go → He goes        grammar
do a decision          collocation
I bought car           article
```

Weekly summaries can generate targeted practice.

---

# 28. Knowledge / Codex / Collections

A strong idea is a “knowledge collection” that turns learning progress into something visible.

Possible collections:

- Word cards
- Phrase cards
- Grammar cards
- Topic books
- IELTS medals
- Event stamps
- Course books
- Mastery badges

Example:

```text
Technology Collection
32 / 50 discovered
18 / 50 mastered
```

This creates a collectible layer without weakening educational value.

---

# 29. Books as Progress Objects

Topic/course progression can appear as books:

- Technology I
- Travel I
- Business I
- IELTS Reading I
- Academic Vocabulary I

Each book can include:

- Chapters
- Completion %
- Mastered vocabulary
- Badges
- Final challenge

Completed books can appear on the user’s digital bookshelf. This makes knowledge visible.

---

# 30. User Identity System

Each user should have a strong digital identity.

Possible profile elements:

- Display name
- Avatar
- Outfit
- Hair
- Accessories
- Frame
- Background
- Title
- Badges
- Class
- Club
- IELTS target
- English level
- Typing record
- Learning mastery
- Favorite activity
- Achievements
- Seasonal prestige

The profile should tell a story about the learner.

---

# 31. Avatar Direction — Current Preferred Decision

## 31.1 Not 3D

3D modular avatars and walkable worlds were considered but rejected as unnecessary for this product direction because they create too much:

- Production complexity
- Clipping problems
- Rigging work
- Web performance risk
- Mobile risk
- Engineering cost

There is no current need for players to freely walk around a lobby.

## 31.2 Preferred direction

> **2D modular avatar system with very light skeletal/transform animation.**

Not full animation.

The character should look alive, not behave like an action-game character.

Possible micro-motion:

- Breathing
- Blinking
- Tiny hair sway
- Tiny cloth sway
- Slight body movement
- Eye movement
- Small reaction
- Aura/sparkle for special cosmetics

No:

- Walking
- Running
- Navigation
- Collision
- Free movement
- Physics simulation

---

# 32. 2D Avatar Layer System

Potential layers:

```text
HAIR_BACK
BODY
BOTTOM
TOP_INNER
TOP_OUTER
ARMS
SHOES
HAIR_FRONT
HEAD_ACCESSORY
FACE_ACCESSORY
HAND_ACCESSORY
BACK_ACCESSORY
AURA
```

Example outfit configuration:

```text
hair: long-black-01
topInner: academy-shirt-02
topOuter: navy-jacket-04
bottom: skirt-03
shoes: loafer-02
headAccessory: none
backAccessory: bookbag-01
```

The renderer composes layers.

---

# 33. Avatar Technical Template

All clothing should follow a shared asset template.

Example:

```text
Canvas: 1024 × 1400
Body center: x = 512
Shoulder anchor: y = ...
Waist anchor: y = ...
Foot baseline: y = ...
```

A new outfit must fit the template so it can be added without special code.

## 33.1 Hair split

Long hair should use:

```text
hair-back
body
clothing
head
hair-front
```

This handles depth naturally without complex simulation.

## 33.2 Expressions

Possible eye layers:

- Normal
- Happy
- Surprised
- Sad
- Concerned

Mouth layers:

- Normal
- Smile
- Open
- Sad

This allows NPC/player reactions with minimal performance cost.

---

# 34. Avatar Pose

V1 should use one excellent full-body pose.

Requirements:

- Clearly shows outfit
- Hands do not cover important clothing details
- Face is readable
- Balanced body silhouette
- Suitable for profile/shop/classroom

Later optional poses can include:

- Default
- Study
- Confident
- Formal
- Cute

Each additional pose should be introduced carefully because outfit compatibility must be maintained.

---

# 35. Avatar Shop Preview

The shop can use the same 2D renderer.

Selecting an item immediately replaces the corresponding layer.

Examples:

```text
Jacket A → TOP_OUTER
Hair B   → HAIR layers
Frame C  → PROFILE_FRAME
```

Potential features:

- Instant preview
- Random outfit
- Presets
- Compare owned/current
- Color variants
- Full set preview

---

# 36. Cosmetic Content Strategy

Not all cosmetics cost the same amount to produce.

## Cheap assets

- Frame
- Badge
- Icon
- Title
- Profile background
- Aura
- Color variation

## Medium assets

- Glasses
- Hats
- Bags
- Small accessories

## Expensive assets

- Hair
- Tops
- Bottoms
- Full outfits

Therefore a large shop does not require hundreds of full outfits.

Example starter inventory might contain:

- 20 hairstyles
- 30 tops
- 20 bottoms
- 10 shoes
- 30 accessories
- 50 frames
- 50 backgrounds
- many badges/titles

The combination count becomes large.

---

# 37. Item Sets

Example:

```text
ORION ACADEMY SET

Hair ribbon
Jacket
Bottom
Shoes
Frame
Badge
Background
```

Collection:

```text
6 / 7
```

Completing a set can unlock a small bonus cosmetic or title. This creates collection goals without introducing gameplay power.

---

# 38. Cosmetic Rarity

Possible rarity language:

- Common
- Refined
- Rare
- Elite
- Epic
- Legendary
- Mythic
- Limited
- Prestige

Rarity can control:

- Item frame
- Reveal sound
- Small visual effects
- Profile presentation
- Scarcity

Avoid excessive visual noise.

Example:

- Common → static
- Rare → subtle shimmer
- Epic → animated accent
- Legendary → controlled particles/aura
- Prestige → unique identity language

---

# 39. Visual / Audio Brand Spine

The platform needs a consistent brand system.

## 39.1 Visual spine

Define:

- Core colors
- Typography
- Icon language
- Panel language
- Profile cards
- Frames
- Badges
- Item cards
- Rarity
- NPC illustration style
- Character proportions
- Outfit style
- Classroom style
- Shop style
- Event style
- Reward presentation
- Motion language

## 39.2 Audio spine

Define:

- Startup signature
- UI clicks
- Hover
- Confirm
- Cancel
- Reward
- Unlock
- Achievement
- Exam
- Class
- Event
- Social notifications
- Shop
- NPC voice
- Learning feedback
- Ambient sound

## 39.3 Identity spine

Define:

- Avatar
- Nameplate
- Title
- Frame
- Badge
- Class affiliation
- Club affiliation
- Learning rank
- Seasonal status

## 39.4 Economy spine

Define:

- Currencies
- Items
- Rewards
- Shop rules
- Collections
- Scarcity
- Prestige ownership

These four layers should be coherent across every module.

---

# 40. Audio Design

Audio should be treated as a structured language rather than random sound effects.

## Brand audio

- Startup
- Major milestone
- Big achievement
- Graduation
- Season transition

## Interaction audio

- Hover
- Click
- Confirm
- Cancel
- Tab switch
- Buy
- Claim reward

## Learning audio

- Correct
- Incorrect
- Near-correct
- Mastery increase
- Review due
- Pronunciation
- Dictation replay
- Timer warning
- Exam start/end

## Social audio

- Class announcement
- Friend activity
- Chat
- Invitation
- Event reminder

## Environment audio

- Classroom ambience
- Library ambience
- Store ambience
- Exam ambience
- Study ambience
- Space Typing/combat ambience

Audio should respect user settings.

Suggested mixer categories:

```text
Master
Music
World
UI
Voice
Learning
Game
Social
```

Voice/pronunciation should have priority over background music.

---

# 41. NPC Voice

Use a hybrid approach.

## Pre-generated/high-quality core lines

Examples:

- Welcome
- Lesson start
- Lesson complete
- Congratulations
- Exam announcement
- Event announcement

## Dynamic lines

Generate/cache personalized TTS for contextual lines.

Example:

> “Your listening improved this week.”

Full lip-sync is not required initially.

Portraits can use:

- Blinking
- Expression change
- Simple mouth movement

---

# 42. VFX Language

Effects should communicate meaning.

Example:

```text
Correct        → soft cyan pulse
Mastery        → gold ring
Rare unlock    → purple reveal
Legendary      → signature reveal
Achievement    → academy crest
```

If everything is “epic”, nothing feels epic.

Reserve large effects for genuinely important moments.

---

# 43. Reward System

Reward design needs its own detailed master plan.

The system should reward:

- Learning
- Consistency
- Improvement
- Social contribution
- Achievement
- Competition
- Events

without becoming manipulative.

---

# 44. Daily Check-In

Example:

```text
DAILY CHECK-IN

Day 1   Credits
Day 2   Credits
Day 3   Item fragment
Day 4   Credits
Day 5   Crystal
Day 6   Rare reward
Day 7   Weekly chest
```

Avoid resetting all progress after one missed day.

Track separately:

- Monthly attendance
- Weekly consistency
- Lifetime activity
- Streak

---

# 45. Active Session Rewards

Avoid rewarding pure online time because users can AFK.

Instead:

```text
15 min active learning → Reward I
30 min active learning → Reward II
60 min active learning → Reward III
```

Only count meaningful activity. Use daily caps.

---

# 46. Daily Activity Meter

Example:

```text
TODAY

Reading          ✓ +15
Review           ✓ +10
Typing           ✓ +15
Listening        ○ +15
Class activity   ✓ +20
Game             ✓ +15

Activity
75 / 100
```

Milestones:

```text
20   Credits
40   Item fragment
60   Crystal
80   Rare reward
100  Daily chest
```

Users should have multiple valid ways to reach the target. Do not require every mode.

---

# 47. Weekly Rewards

Weekly systems can reward:

- Number of active days
- Review completion
- Class activity
- Personal goal completion
- Improvement
- Variety

Possible rewards:

- Credits
- Crystals
- Cosmetic fragment
- Class contribution
- Weekly chest

---

# 48. Long-Term Rewards

Sources:

- Mastery
- Achievements
- Books completed
- Collections
- Certifications
- Class graduation
- Long-term consistency
- Personal best milestones

---

# 49. Reward Center

Avoid interrupting users constantly.

A central reward inbox can show:

```text
5 rewards ready

Daily activity
Class mission
Weekly review
Achievement
Event participation
```

Users claim when convenient.

Only rare/high-value rewards deserve large ceremonies.

---

# 50. Economy

The economy should remain understandable.

A simple public-facing currency model is preferred.

## Credits

Common currency.

Earned from:

- Learning
- Practice
- Class activities
- Games
- Events

Used for:

- Avatar cosmetics
- Frames
- Backgrounds
- Stationery skins
- Themes
- Small customization

## Crystals

Rarer.

Earned from:

- Higher mastery
- Weekly milestones
- Events
- Achievements
- Limited activities

Used for:

- Rare cosmetics
- Premium-looking themes
- Limited visuals

## Event Token

Appears only when an event is active.

## Context-specific resources

Class resources, crafting-like fragments, etc. should appear only inside the relevant system instead of cluttering the main UI.

---

# 51. Shop System

The shop should create goals without becoming the product.

Possible sections:

- Featured
- Avatar
- Outfits
- Frames
- Themes
- Typing
- Study items
- Backgrounds
- Limited
- Event
- Achievement/Prestige

Potential thematic shops:

- Academy Store
- Fashion Store
- Stationery Store
- Theme Store
- Event Store
- Class Store
- Honor/Prestige Store

The user should understand:

> “I want that item, so I have a reason to complete these activities.”

---

# 52. Stationery as a Signature Cosmetic System

A unique idea is to turn ordinary study objects into collectible cosmetics.

Possible items:

- Pens
- Fountain pens
- Mechanical pencils
- Highlighters
- Notebooks
- Binders
- Sticky notes
- Bookmarks
- Flashcard skins
- Stamps
- Ink colors

Examples:

- Pen changes caret/input style
- Notebook changes Recall/Vocabulary note surface
- Highlighter changes article highlight appearance
- Bookmark appears in Codex
- Stamp appears in completion/certification
- Binder changes class material presentation

This creates a “learning-object prestige” that suits the product better than RPG weapons.

---

# 53. Limited & Seasonal Items

Scarcity can create memory and status.

Types:

## Time-limited
Available only during an event period.

## Achievement-limited
Available only after a difficult achievement.

## Rank-limited
Top 100, Top 10, Champion.

## Quantity-limited
Example:

```text
Founder Frame
#042 / 1000
```

## Historical participation
Example:

```text
First Academy Festival 2027
```

Scarcity rules must be honest.

Clearly mark:

```text
Season Exclusive
Event Exclusive
May Return
Permanent
```

No fake scarcity.

---

# 54. Prestige System

Prestige deserves its own system because users want to be recognized for difficult accomplishments.

Principle:

> Some rewards must never be purchasable.

Examples:

- Season Champion
- Top 10
- Top 100
- Tournament winner
- World/Server record
- Perfect challenge
- First major completion
- Certification achievement
- Long-term mastery
- Historic event participation

---

# 55. Ranking Center

Do not use one universal leaderboard only.

Possible views:

```text
GLOBAL
SEASON
WEEKLY
CLASS
CLUB
REGION
FRIENDS
LEVEL BRACKET
CEFR BRACKET
IELTS BRACKET
```

Possible categories:

- English mastery
- Vocabulary
- Listening
- Reading
- Speaking
- Writing
- IELTS
- Typing speed
- Typing accuracy
- Space Typing
- Class contribution
- Helping/reputation
- Achievements
- Collections

This gives many users a meaningful competitive surface.

---

# 56. Personal Best & Improvement Prestige

Not everyone can be Top 10 globally.

The product should also celebrate:

- Personal best
- Most improved
- Consistency
- Best comeback
- Helping classmates
- First major milestone

Example:

```text
Personal Best
72 → 78 WPM
```

This keeps competition motivating rather than discouraging.

---

# 57. Hall of Fame

Past achievements should remain visible.

Example:

```text
HALL OF FAME
SEASON 01

Champion
Toan

#2 Minh
#3 An

Highest WPM
...

Best Accuracy
...

Top Class
...
```

A later season should not erase history.

Prestige becomes part of the platform’s shared history.

---

# 58. Exclusive Prestige Cosmetics

Examples:

- Champion frame
- Top 100 badge
- Graduation seal
- Perfect Listening badge
- Typing Grandmaster title
- Special aura

Achievement-linked prestige cosmetics should be non-tradeable if trading ever exists.

A purchased cosmetic and a performance-earned prestige cosmetic should have visibly different design languages.

---

# 59. Item Provenance

Rare/prestige items can show:

```text
CELESTIAL SCHOLAR FRAME

PRESTIGE · LEGACY
Season 3
Top 10

Owner: ...
Acquired: ...
Serial: #07 / 10
Tradeable: No
```

This gives items history and emotional value.

---

# 60. Tournaments & Exams

Possible competitive formats:

```text
QUALIFIER
↓
TOP 256
↓
TOP 64
↓
TOP 16
↓
SEMIFINAL
↓
FINAL
```

Potential competitions:

- Typing
- Listening
- Vocabulary
- Mixed English
- IELTS practice
- Class competition
- Space Typing

Finals can have spectators/replays later.

---

# 61. Scheduled Events

Timed events can create shared moments.

Examples:

```text
12:00  Lunch Quick Challenge
18:30  Academy Quiz
20:00  Class Activity
20:30  Special Event
21:00  Typing Tournament
21:30  Listening Challenge
```

However, events should not punish users who cannot attend.

Preferred pattern:

- Live version → extra excitement / modest bonus
- Async/replay version → still meaningful

This preserves excitement without turning the product into an obligation.

---

# 62. Event Calendar

Users should have a clear calendar.

Example:

```text
MONDAY
19:30  B2 Class
20:30  Class Challenge

WEDNESDAY
19:30  B2 Class
21:00  IELTS Speaking

SATURDAY
20:00  Typing Tournament
```

Scheduling must be timezone-aware.

---

# 63. School Events

The school metaphor naturally supports:

- Academy Festival
- Exam Week
- Graduation
- Sports/Skill Day
- Class Championship
- Club event
- Seasonal festival

For example, “Sports Day” might contain:

- Typing Sprint
- Listening Relay
- Vocabulary Survival
- Team Quiz
- Space Typing activity

---

# 64. Social System

Social is important because people often return for people they know.

Potential social layers:

- Friends
- Classmates
- Class chat
- Clubs
- Study rooms
- Challenges
- Reactions
- Shared achievements
- Class history

## 64.1 Chat surfaces

Possible channels:

- Class
- Lesson
- Questions
- Resources
- Club
- Friends
- Event

Avoid building an enormous Discord clone at the beginning.

## 64.2 Moderation

Any chat/social system should support:

- Report
- Mute
- Block
- Rate limiting
- Classroom moderation
- Admin moderation
- Age/privacy controls where appropriate

---

# 65. Social Presence

The product can feel alive without overwhelming the screen.

Examples:

```text
Friends online: 7
Class online: 9 / 24
New class message: 3
```

Subtle presence is often enough.

---

# 66. Study Rooms

Possible rooms:

- IELTS Reading 7+
- B2 Vocabulary
- Typing 100 WPM
- Late Night Study
- Listening Practice

Users can study together without needing a persistent virtual world.

---

# 67. Friend Challenges

Async challenges are useful because users do not need to be online at the same time.

Examples:

- Typing 60 sec
- Vocabulary B2
- Listening
- Recall
- IELTS reading mini-task

Result:

```text
TOAN   92
MINH   89
```

This creates social interaction with low infrastructure cost.

---

# 68. Group Activities / Mini-Games

Game-like learning activities should reinforce knowledge.

Potential examples:

- Word Hunt
- Phrase Forge
- Listening Survival
- Typing Race
- Recall Challenge
- Signal Match
- Team Quiz
- Relay Typing
- Class Challenge
- Space Typing

Avoid adding mini-games simply for quantity.

Each mode should have a clear educational role.

---

# 69. Space Typing’s Role

Space Typing remains one of the major game modes.

It can reinforce recently learned material.

Example:

```text
Lesson completed
→ “Reinforce today’s vocabulary in Space Typing?”
```

The same words/phrases can reappear in:

- Typing
- Listening
- Recall
- Class challenge
- Space Typing
- Review

This repetition strengthens mastery.

---

# 70. Content & Learning Data Foundation

The broader English-learning platform should reuse the existing content direction:

- Vocabulary senses
- Phrases
- Collocations
- Grammar
- Patterns
- Examples
- Sentences
- Exercises
- Mistakes
- Dialogues
- Translations
- Listening practice

The compact vocabulary system can remain a stable ABI while richer content lives in dedicated learning structures.

Learning content should have:

- Schemas
- Provenance
- Licensing
- Attribution
- Stable IDs
- Validation
- Deduplication
- Review status

---

# 71. Content Sources & Licensing

Do not republish proprietary educational/news content without rights.

Preferred sources:

- Owned/original content
- Public domain
- CC0
- CC BY
- CC BY-SA where compatible
- Carefully verified open sources

Avoid casually copying:

- Proprietary news articles
- Proprietary dictionary examples
- Copyrighted course content
- Restricted audio

Suggested strategy:

- Curated open material where appropriate
- Mostly original/adapted learning content

---

# 72. Media Production Strategy

## Audio

Use owned/generateable TTS/audio.

Potential approach:

- High-quality en-US + en-GB
- Pre-generate common content
- Generate rare/custom content on demand
- Cache deterministic assets
- Opus preferred
- Word/sentence timing for karaoke/shadowing where useful

## Images

Use for:

- Concrete vocabulary
- Article hero images
- Topic art
- Characters
- NPCs
- Classroom identity
- Rewards
- Event banners

Do not require an image for every abstract word.

## Storage

Long-term architecture can use:

- Git for schemas/content manifests
- Database for runtime/user state
- Object storage/CDN for media
- IndexedDB/local cache
- Search infrastructure only when needed

---

# 73. Performance Philosophy

Performance must be a product constraint from the beginning.

Do not:

- Preload every game mode
- Preload all outfits
- Load every NPC image
- Run many animations on Home
- Open every realtime connection unnecessarily

Preferred architecture:

```text
CORE SHELL
  ↓
lazy-load feature module
```

Examples:

- User has not opened avatar shop → do not load the full catalog.
- User has not opened Space Typing → do not load combat assets.
- User has not opened class social → do not load all class media.
- User has not opened event page → do not load event animation bundle.

---

# 74. Asset Performance Budgets

Each screen/module should have explicit budgets:

- Initial JS
- CSS
- Images
- Audio preload
- Animation count
- Memory
- Network
- Rendering cost

Every asset should justify its cost.

---

# 75. Mobile as a First-Class Experience

Mobile should not be “desktop squeezed smaller”.

Mobile may prioritize:

- Review
- Reading
- Listening
- Voice
- Chat
- Shop
- Profile
- Class activity

Desktop may be stronger for:

- Typing
- Writing
- Full IELTS mock
- Space Typing/combat
- complex dashboards

The learning product should remain usable even if richer cosmetic/world effects are disabled.

---

# 76. Reward / Economy Anti-Patterns to Avoid

Avoid:

- 10–20 permanent currencies
- Reward spam
- Meaningless XP
- AFK farming
- Forced daily grind
- Mandatory game participation for learning cosmetics
- Fake rarity
- Pay-to-win
- Purchasable prestige
- Reward loops that encourage shallow repetition instead of mastery

Rewards should favor:

- Real learning
- Improvement
- Consistency
- Mastery
- Contribution
- Optional challenge

---

# 77. Prestige Integrity

Competitive/prestige systems require anti-cheat.

Particularly for typing:

Potential checks:

- Paste detection
- Automation signals
- Impossible timing
- Telemetry consistency
- Run signatures
- Server-side validation
- Suspicious-run review

Casual results can be stored normally.

High-prestige results may be marked:

```text
Competitive Verified ✓
```

Unverified/suspicious results should not enter serious rankings.

---

# 78. Admin / Game Master / Learning Operations Console

The admin system should eventually manage far more than static settings.

Potential areas:

- Classes
- Teachers
- Lessons
- Curricula
- Exams
- Events
- Rewards
- Currencies
- Shops
- Items
- Cosmetics
- Avatars
- Frames
- Badges
- Titles
- NPCs
- AI personality settings
- Timetables
- Seasonal content
- Class competition
- Leaderboards
- Chat moderation
- Notifications
- Audio/media assignments

The goal is to avoid hard-coding every operational change.

---

# 79. Reward Simulator

Admin tooling should include an economy simulator.

Example input:

```text
Profile:
B1 learner
30 min/day
5 days/week
```

Expected output:

```text
Weekly Credits
Monthly Crystals
Expected item unlock rate
Average class contribution
```

This helps detect:

- Inflation
- Rewards that are too slow
- Rewards that are too fast
- Poor currency sinks

---

# 80. Lesson Simulator

Teacher/admin can preview lesson timing.

Example:

```text
Warm-up       5m
Reading       9m
Vocabulary    8m
Practice      8m
Debrief       5m
Total        35m
```

If estimated duration exceeds target, warn the teacher.

---

# 81. LiveOps Admin

Admin should configure:

- Event start/end
- Recurrence
- Region/timezone
- Eligibility
- Reward tables
- Announcements
- Class schedule
- Exam schedule
- Seasonal item availability
- Shop rotations

Avoid deploys for every new event.

---

# 82. Proposed Master Plan Document Split

This consolidated file should eventually be broken into implementation-oriented plans:

```text
01_PLATFORM_PRODUCT_MASTER_PLAN.md

02_CLASSROOM_LESSON_SOCIAL_MASTER_PLAN.md

03_REWARD_ECONOMY_SHOP_MASTER_PLAN.md

04_NPC_AI_LIVING_WORLD_MASTER_PLAN.md

05_LIVEOPS_EVENT_PRESTIGE_MASTER_PLAN.md

06_VISUAL_AUDIO_BRAND_BIBLE.md

07_AVATAR_IDENTITY_COSMETICS_MASTER_PLAN.md

08_IELTS_TRACK_MASTER_PLAN.md

09_TYPING_SIMULATOR_CUSTOMIZATION_MASTER_PLAN.md
```

The exact split can change after review.

---

# 83. Recommended Build Order

A safe phased approach:

## Phase 0 — Product & Design Foundation

- Product architecture
- Brand direction
- UX principles
- Persona definitions
- Feature boundaries
- Content architecture
- Performance budgets

## Phase 1 — Identity Foundation

- Profile
- 2D modular avatar
- Clothing slots
- Frames
- Badges
- Titles
- Inventory
- Basic shop preview

## Phase 2 — Reward & Economy Foundation

- Credits
- Crystals
- Daily activity
- Weekly activity
- Reward center
- Basic shop
- Item ownership

## Phase 3 — Learning Core Integration

- Daily plan
- Missions
- Lessons
- Review
- Codex
- Progress
- Typing simulator
- Learning analytics

## Phase 4 — Class Foundation

- Class model
- Timetable
- Teacher/NPC
- Class chat
- Lesson schedule
- Attendance
- Shared class progress

## Phase 5 — Social & Events

- Friends
- Challenges
- Class competitions
- Events
- Leaderboards
- Seasonal content

## Phase 6 — Advanced Prestige / LiveOps

- Hall of Fame
- Tournaments
- Limited prestige items
- Historical achievements
- Advanced admin
- Economy simulation

## Phase 7 — More Game Modules

- Space Typing integrations
- Additional typing/recall/listening game modes
- Group challenges
- Future activities

This order avoids building a giant “game world” before validating whether the core learning/social/product loop works.

---

# 84. Important Non-Goals / Current Rejections

Unless later review changes them, the current direction does **not** prioritize:

- 3D avatars
- Free-roaming characters
- 3D academy world
- WASD movement
- Physics-based clothing
- MMO open world
- Heavy RPG stat systems
- Complex gear enhancement
- Huge crafting systems
- Mandatory pets
- Dozens of currencies
- Social systems that interrupt every lesson
- Game-first UI that reduces learning clarity

---

# 85. Core UX Example — Simple Learner

A user with 15 minutes:

```text
HOME

Continue today’s lesson
[ CONTINUE · 12 min ]

Quick Practice
[ 5 min ]

Play
[ Space Typing ]

Progress: 68%
```

They can ignore Shop, Events, Rankings, Class competition, and Collections and still have a complete product.

---

# 86. Core UX Example — Social Learner

A social user may see:

```text
Tonight

19:30  Class
20:10  Break
20:20  Listening Lab

Class B2-07
9 / 24 online

3 classmates improved their PB today
```

After class:

- Chat
- Compare progress
- Challenge friend
- Browse cosmetics
- Join class event

---

# 87. Core UX Example — Competitive User

A competitive user may focus on:

- Ranked typing
- IELTS challenge
- Class competition
- Seasonal leaderboard
- Personal records
- Prestige cosmetics
- Hall of Fame

But this should not change the experience for users who do not care about competition.

---

# 88. Core UX Example — Cosmetic / Collector User

A collector may:

- Complete lessons
- Earn Credits
- Earn limited event token
- Buy outfit
- Complete a set
- Customize avatar
- Display rare frame
- Collect badges/books
- Return for shop rotation

The learning activity remains the source of progression.

---

# 89. Core UX Example — Teacher

Teacher flow:

```text
My Class
→ Schedule
→ Create Lesson
→ Preview Timing
→ Publish
→ Run Class
→ Review Progress
→ Assign Follow-up
```

Teacher-facing UI should be professional and clean.

The teacher does not need to interact with many consumer-game systems.

---

# 90. Brand Direction

A possible unique identity is:

> **Modern sci-fi academy + high-quality learning surfaces + collectible academic identity.**

Important distinction:

The brand should not mean:

- Every panel glows
- Every screen uses holograms
- Every interaction has particles

Instead, brand comes from:

- Terminology
- Characters
- Audio identity
- Icon language
- Avatar style
- Progression
- Collections
- School/academy structure
- Subtle motion
- Consistent visual hierarchy

---

# 91. Why “Academic Objects” Matter

Instead of copying RPG swords/armor, the platform can turn learning objects into desirable status items:

- Books
- Pens
- Notebooks
- Stamps
- Certificates
- Frames
- Highlighters
- Study themes
- School uniforms
- Club outfits
- Graduation cosmetics

This is more coherent with the product and can become a strong brand signature.

---

# 92. Recognition & Status

Users want to be seen.

The platform should provide multiple kinds of recognition:

- High rank
- Improvement
- Consistency
- Mastery
- Helping others
- Class contribution
- Certification
- Tournament achievement
- Rare collection
- Historical participation

This prevents status from being reserved only for the fastest or most hardcore users.

---

# 93. What Must Never Be Sold

Do not sell:

- Top 1 badge
- Tournament trophy
- Verified record
- World/season first
- Mastery certificate
- Earned IELTS practice achievement
- Graduation proof
- Achievement-exclusive title

These items derive their value from proof. Selling them would destroy the prestige system.

---

# 94. What Can Be Purchased With Earned Credits

The preferred economy is primarily cosmetic.

Examples:

- Standard outfits
- Hair
- Accessories
- Profile frames
- Backgrounds
- Themes
- Stationery skins
- Avatar poses
- Emotes
- Decorative effects

Credits earned through participation should have meaningful sinks so rewards feel valuable.

---

# 95. “Living Even When Alone” Principle

A solo user should still feel that the environment is active through:

- Teacher/NPC greeting
- Time-aware dialogue
- Class schedule
- Upcoming event list
- Recent class activity
- NPC reactions
- Daily plan
- Seasonal visuals

But this must not involve fake humans.

---

# 96. Social Retention Principle

The strongest long-term loop may come from:

```text
User joins class
→ recognizes classmates
→ chats with them
→ attends lessons together
→ competes/cooperates
→ builds shared history
→ invites friends back
→ returns because others are there
```

The product should deliberately support these relationships.

---

# 97. Learning Retention Principle

The product should also work for someone who never engages socially.

Loop:

```text
Goal
→ lesson
→ practice
→ feedback
→ review
→ mastery
→ progress
```

Social/game systems must enhance, not replace, this core.

---

# 98. Reward Retention Principle

Reward loop:

```text
Learn
→ earn
→ buy/collect
→ customize identity
→ receive recognition
→ set new goal
→ return
```

The reward should feel meaningful because it connects to a user-visible identity or collection.

---

# 99. Event Retention Principle

Event loop:

```text
Know event is coming
→ choose whether to join
→ shared moment
→ reward / memory
→ profile/history
→ future anticipation
```

Avoid:

```text
miss event
→ lose critical progress forever
```

---

# 100. Final Design Thesis

The project should aim to become:

> **A serious English-learning platform that can feel like a living social game world without requiring the user to become a gamer.**

A casual learner should be able to use it simply.

A serious learner should be able to study deeply.

An IELTS learner should have professional tools.

A typing enthusiast should have excellent typing UX.

A social user should find people, classes, and activities.

A collector should have cosmetics and collections.

A competitive user should have rankings and prestige.

A teacher should have strong class/lesson tools.

All of them should still belong to the same coherent product.

---

# 101. Product Philosophy Statements to Preserve

> **Learning first. Social second. Identity and rewards make both more enjoyable. Games are optional experiences around them.**

> **Depth without complexity at the surface.**

> **Science-fiction identity at the shell; clarity at the content surface.**

> **Every feature must earn its visual weight.**

> **A class is not a chat room around lessons. It is a persistent social environment with identity, routine, shared history, and shared progression.**

> **The platform should feel alive even when the learner is alone, social when others are present, rewarding without becoming manipulative, and educational even when it feels like play.**

> **Prestige must be earned, not purchased.**

> **Space Typing is an important game mode, not the entire platform.**

> **The world does not need to be a 3D world to feel alive.**

> **The avatar does not need to walk to create identity.**

---

# 102. Open Questions for Claude Review

The reviewer should challenge the plan rather than simply approve it.

## Product

1. Is “Space Academy” the right primary mental model?
2. Are there better organizing metaphors that preserve the same strengths?
3. Which systems are still unnecessarily complex?
4. Which systems are missing?
5. Which features should be explicitly postponed?

## Learning

6. Does the class/lesson structure support serious learning outcomes?
7. Where could gamification damage learning quality?
8. Is the IELTS approach sufficiently separated from casual gamification?
9. How should CEFR and topic tracks coexist?

## Social

10. Is the class size assumption reasonable?
11. How should real teachers, AI teachers, and self-study classes coexist?
12. How should users be matched into classes?
13. How can class social bonds form without becoming noisy or unsafe?
14. Which chat functions belong in V1?

## NPC / AI

15. What is the best technical model for contextual NPC memory?
16. How do we keep NPCs natural without pretending they are human?
17. What content/moderation boundaries are needed?
18. Which NPC roles create real user value?

## Rewards / Economy

19. Are Credits + Crystals + contextual tokens enough?
20. What should the earning/spending ratios look like?
21. How can inflation be prevented?
22. Which reward systems should be V1 vs later?
23. How do we prevent grinding from replacing learning?

## Prestige

24. Which rankings are meaningful and fair?
25. How should verified competitive results work?
26. What prestige items should be permanently exclusive?
27. How should Hall of Fame/history be designed?

## Avatar / Cosmetics

28. Is layered 2D the right long-term choice?
29. Should the implementation use DOM/CSS, Canvas, PixiJS, Rive, Spine, or another renderer?
30. How should outfit masking/layer standards work?
31. What asset resolution/file size budgets should be enforced?
32. How can artists efficiently create hundreds of compatible items?

## Audio / Visual

33. What should the core art direction be?
34. How do we make it feel premium rather than “educational website with sci-fi skin”?
35. What audio identity is distinctive enough to be memorable?
36. What effects should be intentionally restrained?

## Architecture / Performance

37. Which modules should be separately lazy-loaded?
38. Which data should be real-time?
39. Which social features require WebSocket infrastructure?
40. What initial performance budgets should be locked?
41. What should mobile degrade gracefully?

## Admin

42. Which admin functions are essential to avoid hard-coded LiveOps?
43. How should Lesson Builder and Event Builder share components?
44. How should reward/economy simulation be implemented?
45. What audit/versioning is needed for class/reward/event configuration?

---

# 103. Suggested Review Output From Claude

A useful review should return:

1. **What is strong and should be preserved**
2. **What is overdesigned**
3. **What is missing**
4. **Contradictions**
5. **Technical risks**
6. **UX risks**
7. **Learning-quality risks**
8. **Performance risks**
9. **Moderation/safety risks**
10. **V1 / V2 / V3 recommended scope**
11. **Recommended architecture**
12. **Recommended design system**
13. **Recommended avatar stack**
14. **Recommended audio/media pipeline**
15. **Recommended economy model**
16. **Recommended class model**
17. **Recommended admin model**
18. **A revised implementation roadmap**

The reviewer should be encouraged to reject ideas that do not justify their complexity.

---

# 104. Current Direction to Treat as Most Important

Unless review finds a better solution, the highest-priority ideas are:

1. The main product is larger than Space Typing.
2. Learning quality cannot be sacrificed for game systems.
3. Social/class relationships are a key long-term retention mechanism.
4. The school/academy model is a strong way to organize complexity.
5. Rewards/economy/shop/prestige need detailed standalone planning.
6. Identity and cosmetics are important, but primarily cosmetic/status—not RPG power.
7. Limited/prestige items must preserve genuine achievement.
8. NPCs should feel alive but must not impersonate real users.
9. User-facing complexity must remain low through progressive disclosure.
10. 2D layered modular avatars are preferred over 3D.
11. Characters do not need to walk.
12. Light idle motion/expression is sufficient.
13. Visual/audio quality is a core product requirement.
14. Performance budgets and lazy loading must be built in from the beginning.
15. Admin/LiveOps tooling is required for long-term scalability.
16. Space Typing should integrate with learning but remain one optional activity among many.
17. A user who only wants to learn should never be forced to interact with game-heavy systems.

---

# 105. Closing Vision

The end state should not feel like:

> “An English website with some game features.”

Nor should it feel like:

> “An MMO that happens to contain English exercises.”

The desired feeling is closer to:

> **A beautiful digital learning world where classes, teachers, friends, progress, customization, collections, competition, rewards, and optional games all reinforce the learner’s real growth.**

The user should be able to say:

- “I come back because my class is there.”
- “I want to improve because I can see my progress.”
- “I want that limited frame, so I’ll finish this week’s goals.”
- “I like how my avatar/profile looks.”
- “I want to beat my friend.”
- “I want to graduate this class.”
- “I want to improve my IELTS score.”
- “I want to break my typing record.”
- “I want to play Space Typing for a while.”
- “I want to collect the last item in this set.”

But underneath all of those motivations, the platform should keep producing the same fundamental outcome:

> **The user learns more English, remembers it better, practices more consistently, and develops a long-term relationship with the learning community.**
