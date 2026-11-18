# Phím 2 bầy rồng khí: vòng ChatGPT (05/11/2026 ~16:00–16:10)

Chat: ChatGPT, chế độ Chat, suy nghĩ High, cuộc trò chuyện "Design Twin Dragons Skill". Luật duyệt kép: ChatGPT đề xuất rồi tự duyệt tới khi PASS hai lần liên tiếp; sau đó Gemini.

| Vòng | Người duyệt | Kết luận |
|---|---|---|
| Tự duyệt 1 (đúng đắn, lối chơi) | ChatGPT | PASS |
| Tự duyệt 2 (hiệu năng, hình khớp, góc cạnh) | ChatGPT | PASS |

## Claude → ChatGPT (tóm lược đúng ý; nguyên văn đã gửi gồm đủ số liệu trong `docs/work/consult/key2-qi-swarm-wiring-study.md`)

Role: senior game-systems designer for a browser typing game "Tu Tien Thu Ai" (xianxia defence; every attack comes from typed words; deterministic integer sim at 60 ticks/s, three.js view; replays and a rules hash must stay deterministic; skills must be map-agnostic: no rule may depend on a map's lanes or gates, only on field bounds, caster, foe positions and density).

Design one skill: key 2 "Twin Dragons, One Burning Pearl" becomes a swarm of 5 translucent qi dragons. The owner approved the look (lab prototype) and this damage rule: "a dragon damages every foe its body sweeps through; when the dragons reach the pearl, a strong explosion hits the whole map". Also approved: the sim itself plans each dragon's route (each dragon owns one sector of the field and flies through the densest foe groups in it), and the view draws exactly that route, so a hit happens where a dragon really passes; a release shockwave near the caster gives the first hit on F0/F1; the pearl burst covers the whole field with distance falloff (about 60 % at the field edge) and a shared budget.

Facts (verified in code): [sim 271 timings, discs, pearl rule, shares, caps; balance 272: key 2 45.99 % > 45 % cap, Standard bot 15 % wins, side balance 75 %; view lab: flown paths 4.5 m turn, coils 1.8/0.8/15 m, stagger 0.3 s, speed 11-16 x 1.3, 6.5-8.9 s; play default Medium; 10 skinned meshes vs budget 6/8] (full text as sent; see docs/work/consult/key2-qi-swarm-wiring-study.md for the facts).

Task: 1. complete design (a) integer route planning, (b) beat table, (c) damage, (d) events, (e) view contract, (f) rollout. 2. Self-review as a separate reviewer, PASS/FAIL, stop after two PASS in a row, show every verdict.


## ChatGPT (nguyên văn)


ChatGPT said:
Twin Dragons, One Burning Pearl — Five Qi Dragons

Decision: Replace ticket 271’s two scripted S-path dragons with five independently routed qi dragons. The sim owns route geometry, body poses, collisions and damage. The view is a renderer only.

1. Core invariants

Five dragons, five deterministic spatial sectors, one shared pearl.

Every dragon targets dense groups within its assigned sector. Its flight may cross other sectors.

Only the actual, visible swept body can trigger touch damage.

Each foe receives at most one touch-damage application per cast, regardless of how many dragons cross it.

The release shockwave provides an immediate local hit; the final pearl burst covers the entire field.

Routes are immutable after cast resolution. Late arrivals can still be touched and participate in the burst.

No damage decisions depend on animation quality, render FPS, map lanes or gates.

Keep the existing 8-second cooldown, three-second cast hold, boss cap and swarm-cluster cap.

2. Integer route planning
2.1 Sector ownership

Divide the rectangular field into five equal-width strips along its longer axis. Use X when width equals height.

Half-open boundaries; the last sector includes the maximum boundary.

Dragon 0–4 owns the corresponding strip.

Sector ownership governs target selection, not collision eligibility.

Turn-radius constraints may carry a dragon through another sector.

This avoids dependence on authored spawn directions or lane definitions.

2.2 Density targeting

At the resolved cast tick:

Snapshot eligible ground and sky foes, including bosses.

Partition each sector into 4 m density cells.

Score cells using groundCount + skyCount + 2 * bossCount, counting a boss as a boss rather than also as an ordinary foe.

Sort by score descending, then route cost ascending, then cell coordinates.

Select up to two separated groups per dragon.

Use each group's actual foe-position medoid as the steering target, with stable foe ID as the final tie-break.

Selection must favor reachable density, not merely the highest raw count.

Use integer comparisons throughout. Do not use floating-point atan2, runtime trigonometry, randomness or unordered iteration in authoritative planning.

2.3 Pearl selection

Preserve the current pearl placement where feasible:

H: center of the densest eligible group.

G: ground-foe centroid; use all eligible foes projected to ground when no ground foe exists.

Move from H toward G by three-fifths of the distance, limited to 12 m.

Constrain the pearl to the field's 2 m inset region.

Constrain it additionally to the reachable region within 60 m of the caster, prioritizing a feasible caster-to-pearl route.

For fields narrower than 4 m, use the available field center instead of an impossible 2 m inset.

2.4 Steering and geometry

Use one deterministic integer geometry module.

Property

	

Rule




Coordinates

	

Integer centimeters




Route sample spacing

	

0.25 m




Minimum horizontal turn radius

	

4.5 m




Heading

	

4096 quantized directions




Maximum turn per 0.25 m step

	

36 heading units




Route length limit

	

75 m




Maximum route samples

	

301




Body length

	

16 m




Body stations

	

41




Body coil

	

1.8 m lateral, 0.8 m lift, 15 m wavelength

Use a versioned integer direction lookup table. Reject any intermediate arithmetic that exceeds safe integer bounds; use checked wide-integer operations where required.

Planner:

Plain text
for dragon in 0..4:
    candidates = rankedGroups(sector[dragon])

    for anchors in [bestTwo, bestOne, none]:
        path = steer(C, anchors, P, minTurnRadius)

        path = bakeFinalCurve(path)

        if pathInsideField(path)
           and curvatureValid(path)
           and length(path) <= 75m
           and arrivalFeasible(path):
            accept(path)
            break

The final baked curve, not its unsmoothed control points, is authoritative.

Retain the lab's quadratic B-spline appearance only by baking the spline into sim samples and validating its curvature afterward. If smoothing violates the radius, retain the valid steered polyline.

The view must not independently smooth or reroute it.

2.5 Vertical targeting

Ground groups use a low flight profile; sky groups use the actual target group's altitude.

Vertical movement is interpolated using deterministic integer distances. Head movement toward an airborne medoid must enter its collision envelope. Unreachable altitude transitions cause the anchor to be dropped.

The horizontal 4.5 m turn-radius rule remains independent of altitude.

2.6 Edge cases

Case

	

Required behavior




One or two foes

	

Relevant dragons target them; remaining dragons perform deterministic sector patrols




All foes in one sector

	

One dragon concentrates there; other four patrol their sectors; global burst still hits everyone




Empty sector

	

Scenic route toward pearl, no invented damage




Sky-only

	

Sky density determines routes; pearl uses sky projection




Boss

	

Boss attracts targeting but retains its existing damage cap




Late-arriving foe

	

No replan; eligible for subsequent actual body contact and burst




Foe dies before contact

	

No touch damage




Target moves away

	

Dragon does not magically hit it




Planner cannot reach anchors

	

Remove anchors, ultimately use a direct feasible route




No eligible foe

	

Preserve existing hold behavior

A sector may be crossed by another dragon. Its ownership does not make a physically visible collision harmless.

3. Exact beat schedule

F = simulation tick after cast resolution; 60 ticks = 1 second.

Tick

	

Beat

	

Authoritative action




F0

	

Resolve

	

Freeze route plan; emit route event




F1

	

Release

	

Caster-centered shockwave, 4.5 m radius




F6

	

Launch 1

	

Dragon 0 emerges




F16

	

Launch 2

	

Dragon 1 emerges




F26

	

Launch 3

	

Dragon 2 emerges




F36

	

Launch 4

	

Dragon 3 emerges




F46

	

Launch 5

	

Dragon 4 emerges




F47–F217

	

Flight

	

Sector sweeps and body contacts




F218

	

Dive 1

	

First head enters pearl




F236

	

Dive 2

	

Second head enters pearl




F254

	

Dive 3

	

Third head enters pearl




F272

	

Dive 4

	

Fourth head enters pearl




F290

	

Dive 5

	

Fifth head enters pearl




F218–F338

	

Absorption

	

Each body retracts over 48 ticks after its own head arrives




F344

	

Pearl burst

	

Instantaneous authoritative full-field damage




F344–F386

	

Afterglow

	

42-tick outward burst animation




F390

	

End

	

Release view resources and sim cast state




F480

	

Cooldown

	

Next normal cast can resolve

Timeline

Total: 390 ticks = 6.5 seconds, leaving 90 ticks before the normal cooldown expires.

For each dragon, compute the required flight speed to reach a point 2 m before the pearl, using the time available before its final nine flight ticks. Moving speed is 14–22 m/s; if it arrives early, it holds at that staging point until the final approach. If the required speed exceeds 22 m/s, prune anchors until feasible.

The final nine ticks cover the remaining approach. Very short paths use a shortened approach and deterministic hold.

During its 48-tick dive, the head remains at the pearl while the trailing spine contracts toward it along the recorded path. The sim continues checking the visibly moving body until retraction finishes.

4. Damage design

Let W be the existing skill power unit. These are initial tuning coefficients, not empirically validated balance settings.

4.1 Three damage channels

Channel

	

Initial damage

	

Frequency




Release shockwave

	

Shared pool 0.5W

	

F1




Dragon body touch

	

0.08W per unique touched foe

	

Once per foe per cast




Pearl burst

	

Shared pool 3.0W

	

F344

Apply the existing damage modifiers, caps and rounding through the established damage machinery.

Touch is once per cast, not once per dragon. This prevents five bodies crossing the pearl from multiplying damage fivefold. The first valid geometric contact owns the touch event.

The old 20-tick re-hit gate is unnecessary for body contacts once they are limited to one per cast. It must not suppress the distinct release or pearl phase. Therefore a foe can receive at most three phase hits: release, touch and burst.

4.2 Exact touch collision

Use the actual coiled 3D spine, not a wide approximation of the head's route.

Body collision radius: 0.85 m around each spine segment, combined with the foe's actual hurtbox.

Reconstruct the same 41 spine stations in sim and view.

Use swept tests between consecutive 60 Hz poses, including foe movement, rather than testing endpoint discs only.

Use a spatial grid for broad-phase candidate selection.

Resolve first contacts in deterministic order: sub-tick contact order, dragon ID, foe ID.

Only one touch-damage application per foe per cast.

For implementation, four fixed sub-tick samples with a conservative movement envelope provide a bounded integer swept-contact approximation. Validate its maximum contact-position error against the visible body. Sweep-based collision is important here because endpoint-only overlap can miss fast motion. 
Box2D

This guarantees geometry-based contact, not a hit on every foe merely because it was selected as a route anchor.

4.3 Release shockwave

At F1, hit eligible foes whose projected position is within 4.5 m of the caster. Use a vertically visible shock dome so sky hits also read correctly.

Divide the shared 0.5W pool among those targets in stable foe-ID order, with integer-remainder allocation.

Important limitation: if every foe is farther than 4.5 m, a genuinely local caster shockwave cannot guarantee an F1 hit. Do not fabricate a remote impact to preserve the old timing metric. Such casts receive their first hit when a dragon actually reaches a foe.

4.4 Pearl burst falloff

At F344, snapshot every living foe inside the field, regardless of lane, sector or altitude.

Define normalized radial position q as distance from pearl divided by the distance from pearl to the field boundary along that same ray, scaled to 0–1000.

Then:

𝑤
𝑖
=
1000
−
⌊
400
𝑞
𝑖
1000
⌋
w
i
	​

=1000−⌊
1000
400q
i
	​

	​

⌋

Thus a foe at the pearl has weight 1000 and a foe at any field boundary has weight 600.

This provides the intended 60% edge falloff even when the pearl is off-center.

Let N be the number of burst targets. Set the integer damage pool to max(round(3W), N) where one is the smallest positive HP-damage unit. Reserve one unit per target, then distribute the remainder proportionally to the weights. Use largest remainders, ties by foe ID.

This avoids a nominal full-map explosion assigning zero damage because of integer rounding. At normal damage scales, the before-cap center-to-edge ratio approaches 100:60; at very low damage scales, the one-unit minimum necessarily flattens the ratio.

If a target has already reached an applicable damage cap, that cap still takes precedence and may reduce its actual damage to zero.

4.5 Caps and balance

Retain:

Normal foe maximum 2.5W per cast.

Boss maximum 1.5W per cast.

Existing 60% swarm-cluster rule, with all three phases grouped under one area-hit identity.

No redistribution of damage rejected by boss or cluster caps.

The release and burst have pooled budgets. Touch is deliberately per unique foe, because a hard, fixed sweep pool cannot guarantee positive damage to an unbounded number of swept foes.

Measure actual post-cap HP damage, excluding overkill.

The historical 45.99% contribution cannot be corrected reliably by reducing the burst alone. More effective density targeting may increase touch victims and therefore total damage.

Run a parameter sweep:

Parameter

	

Initial

	

Test range




releasePool

	

0.5W

	

0.3–0.7W




touchDamage

	

0.08W

	

0.06–0.12W




burstPool

	

3.0W

	

2.5–4.0W




bossCap

	

1.5W

	

Fixed




clusterCap

	

60%

	

Fixed

Acceptance: key 2 contributes no more than 45% of Standard bot damage; existing side-balance metric reaches 85%; Standard win rate improves materially over 15%.

These outcomes cannot be guaranteed by skill coefficients alone. If slot 2 remains dominant while Standard still loses, improve the other skills, bot usage or overall encounter balance rather than making this skill simultaneously weaker and responsible for saving the win rate.

5. Sim-to-view events

Introduce a versioned SwarmCastV1 event at F0.

Field

	

Payload




Identity

	

castId, casterId, castTick, slot, rulesHash




Geometry

	

Caster, pearl and field bounds in integer coordinates




Routes

	

Five ordered arrays of final baked XYZ samples




Scheduling

	

Five launch ticks, five dive ticks, retraction duration




Body

	

Geometry-profile version, coil parameters




Versioning

	

Event schema ID, deterministic checksum

Use packed integer arrays, not engine-specific object graphs. Maximum 301 samples × five dragons × 12 bytes = 18,060 bytes of route positions; with metadata the normal event stays under approximately 19 KiB. Impose a 24 KiB validation cap.

Add SwarmPhaseV1 for burst/end and extend generic hit with castId, phase, and optional dragonIndex. The existing generic hit pipeline remains authoritative for HP changes.

Route events must serialize identically in replay, with stable array ordering, endian definition and field widths. Include planner, lookup-table, collision, damage and event-schema versions in the rules hash.

6. View contract and quality

The view uses absoluteWorldTick - castTick and the recorded route. It must never:

Search for targets.

Recalculate routes from current foes.

Change the route to improve the composition.

Apply damage.

Advance simulation effects using elapsed render seconds.

The 1.8 m coil, 0.8 m lift and bone distribution must come from the same versioned integer pose function used for collision. Convert its result to floating-point mesh transforms only after authoritative geometry is resolved. Render-frame interpolation may occur between adjacent tick poses.

Tier

	

Rendering




High

	

Five skinned dragons; up to three prioritized depth prepasses: maximum eight skinned draws




Medium

	

Five single-pass skinned dragons, premultiplied transparency; no separate dragon depth prepasses: five draws




Low

	

Five flat 2D dragon/ribbon silhouettes following projected sim paths, visible pearl and screen-space burst; no skinned meshes or bloom

The Low version must preserve all five individual trajectories and the sequence of dives. It may simplify shapes, not timing or location.

Overlapping casts use distinct castId records. Rendering may downgrade older casts when the quality budget is exceeded, but must not remove their route representation or influence the sim. Expire visuals and route buffers per cast at F390.

7. Rollout and verification

Stage

	

Work

	

Release gate




1

	

Extract ticket 271 behind the play flag into configurable mechanics

	

Existing replay hashes unchanged with flag off




2

	

Implement fixed-point sectors, planner, curves, pearl placement

	

Identical routes after 10,000 replay/resimulation runs




3

	

Implement shared body pose and swept contacts

	

No off-body hits beyond specified collision tolerance; moving-foe and sky cases pass




4

	

Implement shock, touch, burst and damage caps

	

Pool conservation, target ordering, cap grouping and rounding tests pass




5

	

Add events and replay serialization

	

Byte-identical routes/hits across reloads and supported runtimes




6

	

Port lab rendering to play; add quality tiers

	

Five visible dragons, pearl and burst across High/Medium/Low




7

	

Profile and tune bots

	

1,700+ matches per candidate, with paired seeds




8

	

Enable play flag after acceptance

	

Rules hash migrated; replay compatibility explicitly versioned

Required adversarial tests include: no foes, single foe, all foes in one sector, clustered bosses, moving flyers, late spawns, simultaneous contacts, dying targets, tiny fields, field corners, casts with no nearby release target, and overlapping casts.

Record per cast: route length, group coverage, first-hit tick, unique touch victims, actual damage by phase, capped damage, side balance and performance. Preserve the Standard bot's original seeds so that changes are comparable.

8. Independent critical review
Review 1 — correctness and gameplay

VERDICT: PASS

Review 1

Correctness: Damage is based on the actual body spine; target selection cannot produce phantom hits.

Determinism: Integer routing, stable ties, frozen geometry, serialized routes and world-tick scheduling cover replay requirements.

Map independence: All spatial decisions use field bounds, positions, density and caster.

Late foes: Dynamic collision and F344 burst snapshot handle new entrants.

Damage budget: Release and burst are pooled; touch scales with actual distinct victims, with explicit cap semantics.

Timing: F390 is below the F480 cooldown.

Two documented limitations are intentional, not hidden correctness defects: an out-of-range foe cannot be hit by a 4.5 m local shockwave at F1, and the burst's exact 60% damage ratio is limited by rounding and caps.

Balance remains an empirical release gate, not a claimed result.

Review 2 — performance, visual truth and edge behavior

VERDICT: PASS

Review 2

Readability: Five staggered launches, ordered dives and a distinct final burst produce a recognizable sequence.

Route fidelity: The render path is the final sim-baked path; the view cannot alter hit geography.

Minimum turn radius: Curvature is validated after smoothing, with deterministic fallback.

Performance: Maximum route size, 41-station bodies, spatial broad-phase and tier-specific draw limits are bounded.

Low quality: Gameplay signals survive without 3D or bloom.

Overlaps: Cast identity separates effects; quality degradation cannot affect hits.

Rollout safety: The existing flag and rules-hash versioning provide a controlled migration.

Final decision: two consecutive PASS verdicts.

Proceed with this specification as the implementation candidate. Production approval remains dependent on replay, visual-performance and 1,700-match balance gates—not on the design review alone.

ChatGPT can make mistakes. Check important info.
Latest response




Thinking effort
High