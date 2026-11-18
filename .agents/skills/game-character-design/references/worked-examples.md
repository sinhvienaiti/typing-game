# Worked examples

These are game-specific. They show the procedure applied once; they are not rules for other games.

## Last Line heroine and drone (01/11/2026)

Source: `docs/games/QUALITY_RESCUE_2026-11-01.md` §4. The numbers in that doc stay the living numbers.

- **Play view, measured first.**
  - The camera has pitch 36° and FOV 42°. It sees the hero from behind, about 46° from above.
  - A hero 1.8 m tall is 47 px high at 720p and 69 px at 1080p. At 2.6 m, about 68 px and 100 px.
  - The cyan visor faces the foes, so the player never sees it.
  - What followed:
    - the back carries the identity: cape filigree, light channels on the back plate, a back core;
    - a scale of about 2.6 m was proposed to the owner;
    - a fresnel rim was considered;
    - a test at a 30° camera was proposed.
- **Reserved colours.**
  - Gold marks enemy Pack Leaders. So the hero, the drone and the guns moved from white-gold to ivory or pearl and platinum over graphite, with cyan light.
  - The cape is deep navy with thin ivory lines.
  - If the owner asks for gold, follow the owner.
- **The rejected design** (the v3 turnaround):
  - The four views were consistent, but the design was wrong: a dark full-face mask, two horn-like fins at the ears, smooth beige plates.
  - The owner wanted it "lung linh, hào quang, hoàng gia, sang trọng nhưng vẫn thể hiện rõ như 1 chiến binh", with more modern armour.
- **The direction after that feedback:**
  - a crown helm or a diadem;
  - pearl-ivory armour with platinum filigree and inset cyan light;
  - layered, segmented high-tech plates with panel lines and mechanical joints;
  - a warrior stance;
  - the drone and the guns in the same design language.
  - That evening the working idea was a halo as attached geometry, with the glow added in the engine. The researched [pipeline decision](pipeline-decision.md) supersedes it.
- **A game rule shaped the design.** Both weapon bays fire on the same tick, so one pair of hands cannot hold both guns. The hero fires bay 1 and a drone at the right shoulder fires bay 2. This changes the view only; the sim is unchanged.
- **Sockets planned at design time:**
  - hero: FX_HAND_R and FX_HAND_L, FX_CORE, FX_BACK_CORE, FX_VISOR;
  - drone: FX_EYE, FX_RING, FX_THRUST;
  - guns: FX_MUZZLE (Pulse adds _L and _R), FX_CORE, FX_GRIP, FX_SUPPORT, FX_EJECT.
- **Pipeline:**
  - Four views (front, back, left, right) of the hero for Tripo multiview; the drone's design sheet adds a top view. Firefly could not hold the design, so the views are drawn in one ChatGPT chat.
  - Face targets per class (hero, drone, gun) are in `docs/games/LESSONS_FROM_THREE_GAMES.md` §4.
  - The rig is the Mesh2Motion human, plus bone chains for the cape and the hair. No Tripo auto rig.
- **Risks recorded:**
  - the hero too small on screen;
  - cape and hair clipping through the legs or the guns;
  - frame cost, still to be measured.

## Using it in other games

Pointers only. Each game's design doc decides who the character is.

- **Characters that follow the same procedure:**
  - Dragonhold's dragons (Hỏa Long, Bạch Long);
  - Wordwoven's Draconis;
  - Tu Tien's cultivators, commanders and beast kings (`docs/games/tu-tien/art-requests/m0b/`);
  - companions and named NPCs in any later game.
- **The lenses that weigh most:**
  - Dragons: myth and legend (the noble East Asian dragon) and presence VFX.
  - Tu Tien: xianxia (ribbons, hair crowns, orbiting artefacts) and royalty.
  - Sci-fi heroes: warriors and sci-fi armour, and modern game hero design.
- **Foes and bosses:**
  - Start from `docs/games/MONSTER_MODEL_INVENTORY.md`.
  - Appeal still applies, but the friend-or-foe read flips: a foe may carry villain cues and the game's enemy colours. A hero may not.
