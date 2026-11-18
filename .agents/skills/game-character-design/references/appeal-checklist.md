# Character appeal checklist

Use it twice:
- **In the brief:** answer every item with a concrete choice.
- **When judging:** answer every item yes, partly or no, with one line of what you see.

A "no" is a named fault to fix before the piece goes to the judges.

The list comes from the owner's rejections of 01/11/2026 and from widely taught character-design principles. When the researched guide (docs/games/CHARACTER_DESIGN_GUIDE.md) exists, its checklist is the source: merge anything new from it into this file.

1. **Silhouette.** Fill the figure black and shrink it to play size.
   - It reads as this character, this role, and as friend, not foe.
   - It has one or two signature shapes no other character in the game has: a crest, a crown line, a cape cut, a wing, a weapon.
   - Its shape language fits the role. Heroes lean on upward lines, V-shapes and an open chest.
   - A hero carries no villain cues: no closed dark face, no horn-like fins or spikes at the head.
   - **Paired limbs stay paired in every crop.** Show both arms or forelegs, or neither. A bust or forebody crop with only one visible arm or claw reads as amputated. The owner said this of the Solar Ember Regent dragon on 04/11/2026 ("nhìn hiện tại nó như cụt 1 tay"). Brief it explicitly: name both limbs and what each does (for example the near claw grips the pearl and the far claw is braced behind it), and never write "one claw".

2. **Focal point.** The eye lands on one place first, usually the head and chest (face, crown, chest core).
   - The highest contrast and the strongest light sit there.
   - A character the camera sees from behind needs a second focal point on the back: a back core or a cape emblem.

3. **Value grouping and detail density.** Blur the image: three value groups (light, mid, dark) still read.
   - Detail clusters at the focal areas, with quiet rest areas between.
   - Below about 150 px on screen, use a few large details instead of many small ones.
   - Fails: detail scattered evenly everywhere, or large blank plates.

4. **Premium materials.** Name every material and its finish: pearl or ivory ceramic, platinum filigree, brushed metal, lacquer, silk, enamel, gemstone, emissive glass.
   - Finishes contrast: matte against polished, soft cloth against hard plate.
   - Fails: smooth plastic plates, one uniform toy-like sheen.

5. **Modern layered construction.** You can count the layers: under-suit, segmented plates with panel lines and bevels, mechanical joints, trims, inset light channels, cloth over armour.
   - Plates overlap and step, and their edges carry trims.
   - Fails: a single smooth shell.

6. **Royal or divine cues.** Rank and grace show without losing the warrior read (stance, weapon, armour). Pick cues from the research, from one coherent source culture or a deliberate blend:
   - a crown, a diadem or a crown-helm line;
   - regalia and filigree;
   - a heraldic or sacred motif;
   - a cape or celestial ribbons;
   - a halo or mandorla.

7. **Radiance kit.** The kit has four parts: a halo or mandorla, emissive channels on the armour, light motes or orbiting ornaments, and a cape or ribbons in motion. List each part with:
   - its form (geometry or VFX, per [the pipeline decision](pipeline-decision.md));
   - its anchor socket and its colour;
   - when it brightens: idle, combo, skill, victory.

8. **Colour script and reserved colours.**
   - First list the colours the game reserves for signals: enemies, enemy attacks, elite or pack-leader foes, our side, pickups. The character never uses them at high intensity.
   - Then choose a base, a secondary and an accent with rough shares (about 60/30/10), and one emissive accent hue.
   - The character must stand off the map's ground values.

9. **Readability at play size.** Look at the real on-screen height from the play camera (for example 47–100 px for the Last Line hero), from the side the camera sees.
   - Silhouette, focal accent, role and friend-or-foe all read without zoom.
   - Design hardest the side the camera sees most. If the camera sees the back, the back carries the identity.

10. **Rig and pipeline fitness.**
    - Arms leave a gap from the body.
    - Cape and hair are separate panels that do not fuse to the legs.
    - Armour plates can be locked to bones.
    - Sockets are planned for the VFX anchors: hands, core, back core, visor, halo anchor.

11. **Appeal, said plainly.**
    - Would a player take a screenshot of it?
    - Does it hold up next to the commercial references on the board?
    - "Clean but ordinary", "generic" and "simple" fail even when nothing is wrong.
