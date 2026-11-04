# Designing a skill kit

How to design or redesign a whole set of skills (a school, a weapon family, an element) so that it reads as powerful and distinct, before any VFX is built.

Worked example: Tu Tien's catalog V2 (03/11/2026), `docs/games/tu-tien/skills/SKILL_CATALOG_V2.md`. It came after the owner rejected a 43-skill catalog as boring ("các kỹ năng hiện tại của bạn quá chán"). The sources are in `docs/games/tu-tien/skills/source/`.

## 1. Research the culture the game comes from

- **Use the fans' own sources.** For a xianxia or wuxia game, research Chinese games, novels and donghua in Chinese: Bilibili, Baidu Baike, Zhihu, NGA, TapTap, 17173, Gamersky, Qidian.
  - Search the fans' words for a defining scene or the most handsome skill (名场面, 最帅技能).
  - For each weapon and element, collect 3–5 moves fans rate highest: the source with a link, what fans praise, the visual signature in one line, and the trick that makes it overwhelming.
- **Two AIs, in the owner's double review** ([agent-orchestration](../../agent-orchestration/SKILL.md), 04/11/2026). ChatGPT (Chat, thinking High) analyses and passes its own review twice in a row. Then Gemini (4 Argon, High) reviews that and passes twice in a row. Then Claude verifies and decides. Neither assistant is an authority (game-art-pipeline).
- **One long brief, in parts.** Part 1 is research. Parts 2–4 are the kits, a few schools each. The brief says to wait for "Part n", so one reply never truncates.
  - Get files out through the local receiver after each part (game-art-pipeline browser-ai-tools §4).

## 2. Brief: what every skill must state

- **Names:** a code, the native name and an English name (players read English).
- **Its source** and the one-line fantasy.
- **Shape and reach:** the area (mark the field-wide ones), and the silhouette at the game's play camera (for example 40 px at 55°).
- **Timeline** from the last key, in seconds and 60 Hz frames, where F0 already does something.
- **The five VFX phases** (charge while typing, release, travel, impact, aftermath) and the screen-effect tier.
- **The foe's reaction and its death look.**
- **The callout** (native language, or a wordless shout for small skills) and the sound layers.
- **Build difficulty** (S, M or L).

## 3. Rules the research produced

1. Change the world, not only the projectile: sky, ground, light, plants, surrounding weapons.
2. Give each school a law (an authority), not a damage type: Sword commands, Sabre executes, Spear is a vector, Metal is edge, Wood is life, Water is domain, Fire is compression, Earth is mass, Thunder is judgment, Wind is atmosphere, Ice is stillness.
3. One giant readable idea first, detail second.
4. Numbers must become geometry: many weapons form rings, gates, rivers or constellations.
5. Use scale contrast: something tiny carries an absurd consequence.
6. F0 is already lethal, and the spectacle keeps unfolding.
7. Sound is a power ladder: breath and shouts for small skills; a chant, then a hush, a signature sound and the impact for big ones.
8. Strong skills leave a before and after on the field.
9. The victims sell the power: whole packs bow, freeze or look up.
10. An ultimate has one moment of impossible calm before the release.

## 4. Structure that answered "more power, more area"

- **Each school escalates** from weapon technique (basic, slot 1) to battlefield authority (slots 2 and 4) to a mythic phenomenon (the ultimate).
- **One field-wide self-hunting skill per school,** plus a field-wide ultimate with a cut-in. Mid skills are wide (about 20–26 m on a 40 × 26 m field).
- **Slot 1 may be wider than a first draft suggests.** Gemini's slot 1 skills were 14–18 m against ChatGPT's 6–11 m. Tune the reach in the lab, then balance with bots.

## 5. Self-review before anyone builds

Ask the author AI for its 5 strongest showpieces, the weakest or most overlapping skills, and what to cut or merge. Then check it yourself. The patterns that showed up:
- **Several precise single-target basics:** one shared code path, with different art.
- **Two field hunters with the same body** (dragons and serpents): change one to a different behaviour, for example a seal network.
- **Too many "vanish, move 12 m, reappear" dashes:** turn some into guards or counters that fit the element.
- **Two remote-judgment hunters:** make their rhythms differ, slow inevitability against rapid fire.
- **A generic giant avatar ultimate:** make the world itself the weapon instead.

## 6. Hard rules

- **Never copy a famous technique's name or exact choreography.** Gemini repeatedly reused novel names (一剑仙人跪, 两袖青蛇, Soumetsu). Keep the principle, write an original name.
- **The owner approves the catalog before any skill is built.** Canon numbers (damage, cooldowns, areas) change only after his approval, then through bot balancing on every BALANCE.md metric.
- **Build the strongest showpiece first** in the lab, with the full power layer (SKILL.md, "Power layer"), and show it to the owner.
