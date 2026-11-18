# Tripo: from an accepted source to a model in the game

The owner, 01/11/2026: "Chắc chắn xác nhận đầy đủ r hãy tạo vì credit có giới hạn rất ít". Later the same day: "Chờ ảnh đạt 8,5". Credits are scarce, and a weak source cannot become a good model. The current list, configuration and credit log are in [TRIPO_TODO.md](../../../../docs/games/TRIPO_TODO.md). Floors and the order for cutting are in [MODEL_QUALITY.md](../../../../docs/games/MODEL_QUALITY.md).

## 1. Before spending a credit

1. **Reuse first.** For foes, search `docs/games/MONSTER_MODEL_INVENTORY.md` and every game's `art-src/3d/`. Retexture, recolour, rescale or re-rig before generating.
2. **Source accepted.** Two blind judges both gave the source image 8.5 or more for market level, appeal **and** Tripo fitness ([judging.md](judging.md) §3). A Tripo-fit source has:
   - one connected solid object with a flat base;
   - a three-quarter view from about 30° above;
   - no ground, shadow or key fringe;
   - nothing floating. A halo or ring must be attached by struts; the glow is added in the engine.
   - thin parts thickened enough to survive meshing.
   For characters and drones, Tripo multiview needs the four consistent views from one ChatGPT chat ([briefs-and-sets.md](briefs-and-sets.md) §3).
3. **The model list is written down**, with class, `face_limit` and credit cost per model, in the game's Tripo log.

## 2. Wallet and configuration

- **Wallet order:**
  1. The developer API first: the `tripo` CLI at `/opt/homebrew/bin/tripo` is already logged in. Check `tripo balance`; it showed 970 credits on 01/11. If it reports no login, stop and tell the owner.
  2. The web Studio second. It is a separate wallet, and the owner is signed in at tripo3d.ai.
  - Never log in, top up or change the profile yourself.
- **Configuration** (checked with `--dry-run` on 01/11):
  - model v3.1 (`v3.1-20260211`);
  - `texture_quality=detailed` (HD), `pbr=true`;
  - geometry `standard`;
  - an explicit `face_limit` per class (table below).
- **Never use** smart low-poly, quad, or more than one candidate (`-n` above 1 pays for each).
  - Detailed geometry costs +20 credits. Consider it only for the main hero, and only if the first test shows it is needed.
- **Cost:** about 40 credits per model with detailed texture. Smart low-poly would add +10 and quad +5; both stay off.

```bash
# dry run: no upload, no credits; check model, texture, pbr, texture_quality, face_limit, no smart_low_poly
tripo make <source.png> --model tripo-v3.1 -p texture_quality=detailed -p pbr=true -p face_limit=<n> \
  --name <id> -o <scratch>/tripo/<id> --dry-run
```

TRIPO_TODO.md records the same settings in the `tripo generate image-to-model` form. Whichever form you use, the dry-run output must show every value above before you drop `--dry-run`.

## 3. Face limit by class

The owner: "đừng có chơi số face ở mức cao nhất, nó chỉ nên được nâng cao hơn để đẹp hơn so với trước". Use neither the maximum nor the old 2–4k.

| Class | face_limit |
|---|---:|
| Main hero, big landmark (gate, dragon statue) | 50,000 |
| Large building, wall, tower | 30,000–35,000 |
| Ruined arch, drone | 25,000 |
| Normal foe | 15,000–25,000 |
| Hand-held gun | 15,000 |
| Small prop (brazier and the like) | 12,000 |

## 4. One model first

1. Generate **one** model.
2. Inspect it:
   - the triangle count;
   - the maps: base colour 2048, normal map and roughness map present;
   - a Blender turntable from three angles: holes, melted parts, a wrong back.
3. Log the credits before and after in the game's Tripo log.
4. Only then generate the rest of the list, one model at a time with logging.

## 5. After generation

- **Originals** go to the game's `art-src/3d/`, mirroring the 2D source path. Never put them in Git.
- **Blender cleanup and rig are ours.** So are clips, procedural motion, crowd animation and VFX: Tripo provides the look only.
- **Runtime tiers follow MODEL_QUALITY.md:**
  - Floors: no model the player sees up close goes under 2,000 triangles. High floors are 20k for heroes, dragons and bosses; 6k for foes; 8k for buildings and large trees; 2.5k for small props.
  - Keep the normal and roughness maps and 2048 colour textures on High.
  - Ultra uses 100 % of the original.
  - Cut only when measured frame time breaks the game's budget, in this order: instancing, LOD, texture compression, tiers, and High decimation last.
- **Existing models stay as they are** until the owner asks. When he does, the cheap fix is to reprocess from the originals in `art-src/3d/`.
- **Judge the model in the play build at 8.5** ([judging.md](judging.md) §4).

## 6. Lessons

- **Plastic look (29/10).** Our own processing step cut foes by 58 % and trees by 84–91 %, deleted the normal, roughness and AO maps, and set a flat roughness of 0.9. The Tripo originals were fine.
- **No good source, no good model.** On 01/11 three rounds of Dragonhold landmark sources failed at 5–8.3. No credits were spent, which was correct.
- **Free ready-made models did not save it** for a matched set: 58 licence-checked candidates scored 7 at best and did not form one set ([licences.md](licences.md) §5).
