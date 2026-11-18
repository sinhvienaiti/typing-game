# Radiance kit: geometry or VFX

> **NOT DECIDED YET (01/11/2026). Do not guess it.**
>
> The decision comes from the research the owner asked for. It is recorded with its evidence in docs/games/CHARACTER_DESIGN_GUIDE.md §7; the recipes go in docs/games/HERO_PRESENCE_VFX.md.
>
> When §7 exists, replace this note with its conclusion: the rule, the split per kit part, the test that confirmed it, and links to both docs (and to a `game-hero-presence-vfx` skill if one holds the recipes).

## Why there is no default

The owner saw a heroine with a ring painted behind the head and found it strange. He did not ask for a method; he asked for the right one, found with evidence:

- "bạn nên tìm hiểu xem cách nào làm đúng, vì tôi k biết làm gộp thành 1 ảnh như bạn thì là đúng, hay là cách khác mới đúng và hiệu quả"
- "nên tham khảo các thư viện, source, các cách làm của những người khác để tạo nên những bài học cho riêng bạn"

## Options to compare

| Option | In the image and the model | In the engine |
|---|---|---|
| A | Everything: halo, glow, motes | Nothing extra |
| B | A clean body; halo and ornaments as a separate accessory mesh | Glow, motes, ribbon motion |
| C | Halo as part of the body geometry | Glow and motes |
| D | The body only | The whole radiance kit |

## Criteria, each backed by evidence

- **Generator:** how the image-to-3D generator handles thin, ring-shaped or floating parts. Are they fused, broken or filled in?
- **Rigging:** does the part follow a bone? Does it fight the cape or the hair?
- **Readability:** does it read at the play camera size?
- **Bloom:** the bloom rule and value range of `docs/games/VFX_STANDARD.md`.
- **Frame cost:** measured per quality tier.
- **Iteration speed:** can the halo change without a new model or new sources?
- **Practice:** how professionals do it, with links that were opened and checked.

## Until the decision exists

These points hold whatever the decision turns out to be:

- **No light in the source image.**
  - The 3D source image carries no painted glow, light rays or rim light.
  - Emissive parts are painted as their colour only.
  - Whether a physical ring belongs in the source at all depends on the decision.
- **One line per kit part in the brief,** with its socket name, so either outcome can be built.
- **Test before relying on it.** Confirm the chosen option on one part. If two options are close, build that part both ways.
- **No endless redraws.** Never pack the whole kit into one picture and redraw it until it looks right.
