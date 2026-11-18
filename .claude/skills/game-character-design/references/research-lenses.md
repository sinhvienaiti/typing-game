# Research lenses for character design

**Status, 01/11/2026.** Two researched docs were planned as the research record:
- docs/games/CHARACTER_DESIGN_GUIDE.md: the checklist, the design devices, and the pipeline decision in its §7;
- docs/games/HERO_PRESENCE_VFX.md: libraries and recipes for presence effects (if a `game-hero-presence-vfx` skill exists, use its recipes).

If they exist, read them first and reuse their findings. Then merge anything reusable into this skill (this file, [the appeal checklist](appeal-checklist.md), [the pipeline decision](pipeline-decision.md)): docs keep the record and the living numbers, the skill keeps the method. If they do not exist, research with the lenses below.

## How to research

- **Write the questions first,** three to five that the design must answer. For example:
  - What makes this role read as noble in this game's world?
  - Which motifs fit that world?
  - How do commercial games keep a hero readable at this camera size?
- **Run two tracks in parallel** when the decision matters: your own web search, and ChatGPT as a second opinion.
- **ChatGPT:** chatgpt.com in Chat mode, thinking High, never Work.
  - Ask for a URL behind each claim, and image references where it can.
  - Open the cited pages (WebFetch or a browser tab). Mark each key claim verified, partly verified, unsupported or wrong.
  - Add what it missed, write your own evaluation, and say where you disagree. Weigh its art reviews; never copy them.
  - The owner's words: "bạn và chatgpt chỉ là trao đổi và tham khảo, chứ k phải cái gì chatgpt đưa bạn cũng k xác nhận lại mà đồng ý ngay là k nên".
- **Browser rules:**
  - Never sign in or type passwords. If a tool is signed out, stop and tell the owner.
  - Use your own tab and close it after.
  - The in-app browser cannot upload local files to ChatGPT. Ask the owner to attach the reference images.
- **Write a research note** in the game's docs or the brief:
  - the questions;
  - findings per lens, with links and verification marks;
  - the devices you will use and why;
  - the devices you reject and why.

## Lenses

1. **Myth and legend: how sacred light becomes a shape.**
   - Sacred light: the nimbus around the head, the mandorla around the whole body, the flame aureole of Buddhist art.
   - Winged and armoured guardian figures.
   - Dragons: noble beings in East Asian myth, threats in European myth.
   - Look for shapes and emblems.

2. **Xianxia and wuxia.**
   - Celestial ribbons floating around the body, as on the Dunhuang flying apsaras.
   - Hair crowns.
   - Layered robes over armour.
   - Flying swords and orbiting artefacts.
   - Lotus and cloud motifs, cultivation auras.
   - Look at donghua, commercial games of the genre and classical painting.

3. **Royalty and fashion.**
   - Crowns, diadems and circlets; regalia; capes and their cut.
   - Filigree, enamel and gem settings; heraldry.
   - Couture structure: layering, asymmetry, a strong shoulder and waist line.
   - Find out why a piece reads expensive: material contrast, trims, restraint.

4. **Warriors and sci-fi armour.**
   - Real armour construction: lames, pauldrons, gorgets.
   - Modern hard-surface design: panel lines, mechanical joints, inset lights, segmented plates.
   - How sci-fi heroes keep a face or an elegant visor instead of a dark full mask.

5. **Modern game hero design.** How commercial games build hero appeal at their camera:
   - shape language, the focal point, the colour script, rim light;
   - the hero's back under a third-person camera.
   - Prefer sources that explain why: studio art blogs, GDC talks, ArtStation breakdowns, 80.lv interviews.

6. **Presence VFX.** How pros make a character radiant without washing it out:
   - fresnel rim and emissive masks;
   - additive cards for halos and particles for motes;
   - bones or cloth for ribbons and capes;
   - bloom only on thin HDR cores.
   - Look for three.js examples, particle libraries (three.quarks, for example; check the licence first), shader breakdowns and engine docs.
   - Record each recipe as a reusable lesson, with a test page that renders and scores each layer on its own.

## What the research must decide

- The devices for checklist items 1–8.
- The geometry-or-VFX split for the radiance kit ([pipeline decision](pipeline-decision.md)), backed by evidence and a small test.
- Two or three distinct directions to show the owner.
