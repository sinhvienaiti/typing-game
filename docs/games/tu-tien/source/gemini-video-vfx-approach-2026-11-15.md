# Gemini: how to use video in our skill VFX (15/11/2026)

Gemini 4 Argon, High thinking, one chat (https://gemini.google.com/app/1baaafb4b256241c). The owner asked (15/11): "hướng tốt nhất để áp dụng dạng video vào game là gì, bạn hãy kêu gemini phân tích từ các nguồn có dẫn chứng đầy đủ", and the coordinator added his core question: is the fake look only missing integration, or will a video card still look like a video after full integration? No images were attached; our case was described in words only.

## Tóm tắt (300 từ)

**Kết luận chính (câu hỏi cốt lõi của anh):** cảnh giả **không chỉ** vì chưa tích hợp. Kể cả khi code đã làm đủ (quái chớp đòn, vết trên đất, ánh sáng, nhiều lớp, âm thanh), một thẻ video luôn quay mặt về camera vẫn trông như video dán lên sân nếu nó có quái hoặc cảnh vẽ sẵn, vẽ ở một góc nhìn cố định, hoặc là một khối lớn. Tích hợp chỉ sửa được phần **bên ngoài**: quái phản ứng, đất có dấu, ánh sáng, hit-stop, rung màn, âm. Nó không sửa được phần **bên trong** điểm ảnh: quái và cảnh đã nằm trong video, góc nhìn cố định so với 4 góc camera, thẻ phẳng không có thị sai, không che khuất đúng với quái đứng trong hiệu ứng (nửa sau sau quái, nửa trước trước quái), phóng to bị nhòe.

**Ngưỡng cứu được:** chỉ clip **một chất liệu vô định hình** (một cụm lửa, khói, quả cầu điện, mây mực, bọt nước) trên nền đen tuyệt đối, không vật rắn, đối xứng tròn, rồi cắt thành flipbook và rải thành 5–12 thẻ nhỏ quanh từng quái. Tia thẳng hoặc vòng dưới đất thì cứu được nếu khóa hướng (dải theo trục, mặt phẳng nằm). **Không cứu được:** vật hoặc sinh vật triệu hồi có góc cố định (10 clip), clip có đất và cảnh vẽ sẵn (7), tuyệt kỹ vẽ cả cảnh (khoảng 16).

**Cách làm đúng theo ngành:** một chiêu gồm nhiều lớp: hiệu ứng trên chính mô hình quái (chớp, vỏ băng, cháy), decal trên đất, lưới 3D + shader cuộn UV, flipbook mỗi cái một thành phần, hạt, ánh sáng cục bộ, rung camera, hit-stop, âm đúng khung. Video vẫn đúng chỗ cho cut-in 2D trên màn hình, nguồn để cắt flipbook một thành phần, chất liệu lặp (nước, dung nham), menu và giao diện.

**Cổng QA cho video AI:** không sinh vật hay cảnh lạ; viền đen thật; lề khung; đầu và cuối về 0 hoặc lặp sạch; góc nhìn trung tính (thẳng hoặc từ trên xuống); thử trong lab ở cả 4 camera trước khi dùng.

**Lộ trình:** sprint 1 làm hiệu ứng trên quái, decal đất, hit-stop chung; sprint 2 thay 17 clip lỗi; sprint 3 cắt flipbook clip sạch và dựng lại tuyệt kỹ thành bộ lớp.

## Verdicts

| Round | What | Verdict |
| --- | --- | --- |
| 1 | Full analysis, 7 questions + self-review | PASS |
| 2 | Owner's core question + review of both turns (removed 4115, downgraded the HoYoverse cut-in claim to opinion, moved 20853 off the SSIM claim) | PASS |

Two passes in a row, so the review stopped.

## Source check (Claude, opened at the source)

| Claim | Source | Result |
| --- | --- | --- |
| Combat impact is "almost entirely hit reactions" | GDC 2024 Mattson, "A Second Shot" notes PDF | **Verified**: the quote is on the page (The Last of Us shooting context). |
| Side-view and top-view flipbooks are blended for multi-angle effects | realtimevfx.com/t/flipbook-blending-side-and-top-view/27424 | **Verified**: the thread describes separate side- and top-view explosion flipbooks. |
| A baked view breaks when the camera angle differs a lot ("the trick is revealed") | simonschreibt.de/gat/lego-studs | **Partly**: the sentence is on the page, but in a reader's comment, not in Simon's article. The point stands. |
| Diablo III builds spell bodies from meshes with scrolling textures | gdcvault 1017660 | **Partly**: the session ("The VFX of Diablo", Julian Love) exists inside the TA Bootcamp; the public page does not show the content. Widely known, but not proven from that page. |
| Honkai: Star Rail uses video cut-ins | gdcvault 1035480 | **Unsupported**: it is a design talk about mass appeal. Gemini downgraded the claim itself in round 2. |

## Gemini round 2 (verbatim excerpt: the verdict and threshold)

The chat page blocks scripts from sending text to a local receiver, and the in-app browser clipboard is not shared, so the full chat could not be exported as a file. The key answer below is copied from the page text. Round 1 follows as a faithful summary with every URL.

> VERDICT: No—the fake look is NOT just missing integration; even after full code integration (per-foe hit reactions, ground decals, dynamic lighting, layering, and sound), any camera-facing video card that contains baked creatures, baked scenery, a fixed camera perspective, or a large 3D volume will STILL look like a flat video pasted over the battlefield.
>
> Code integration only fixes external context—how the 3D world, terrain, and 100 foes react around the effect. It cannot fix the internal optical and spatial physics of the pixels already baked inside a 2D card [Opinion].

What integration can fix (Gemini):
- per-foe hit flash, knockback and freeze or burn overlays;
- ground decals;
- dynamic light;
- meshes and particles layered in front of and behind the card;
- sound, hit-stop and camera shake.

What it cannot fix:
1. Baked creatures and scenery become "ghost holograms" under additive blending (Riot LoL VFX guide).
2. The fixed video perspective against 4 cameras (lego-studs; RTVFX 27424; offworld.live 360 VFX).
3. No internal parallax on a four-vertex plane (simonschreibt four-vertex-volume; RTVFX 2539).
4. No occlusion or sorting with foes inside the effect: depthTest off draws over foes, depthTest on slices them, and soft particles only soften the seam (three.js depthTest; Unreal DepthFade; Unity soft particles).
5. Scaling and duration changes blur or stutter the clip (simonschreibt how-not-to-create-textures; RTVFX 20853).

> The Salvage Rule: Code integration can save a video clip (converted into a sprite-sheet flipbook) ONLY IF the clip depicts (1) a single amorphous material on (2) pure #000000 black, with (3) zero solid objects/scenery, (4) radial or single-axis symmetry so its perspective does not break across 4 cameras, and is (5) spawned as multiple small sub-instances in 3D space so foes can stand between them.

Clip types:

| Type | What it is | Verdict and action |
| --- | --- | --- |
| A | One amorphous material on black | YES: KTX2 flipbook, 5–12 small cards per foe. |
| B | Axis beam or flat ground ring | YES with orientation lock: ribbon or crossed planes, or a flat XZ plane. |
| C | Summoned objects or creatures at a fixed angle | NO: a 3D mesh with a Fresnel shader and scrolling UVs; the video only as a 2D cut-in. |
| D | Baked ground or scenery | NO: XZ decals plus instanced rock meshes. |
| E | Whole-scene ultimates | NO: a 0.8–1.2 s 2D cut-in, plus a 3D strike built from a decal, a shockwave mesh, Type A puffs and per-foe hits. |

Gap Gemini noted: puffs drawn with depthTest on and depthWrite off on an instanced mesh, with additive or premultiplied blending, let the opaque foes occlude the puffs behind them with no CPU sorting.

## Gemini round 1 (summary, all sources kept)

1. **Video vs flipbook vs mesh.**
   - Video (VideoTexture): cut-ins, UI loops, previews and cinematics. Never as a whole-scene card in 3D [Opinion].
   - Flipbooks: one isolated element each (Unity VFX Graph Flipbook Player; Unreal render-a-flipbook 4.27).
   - Meshes with UV-panning shaders: slashes, beams, domes, wings (GDC 2013 Diablo; simonschreibt diablo-3-wings-of-angels, diablo-3-resource-bubbles).
   - Flipbook atlases let many instances play different frames in one draw call; a video texture cannot be time-offset per instance (three.js VideoTexture).
2. **Why whole-scene videos look fake.**
   - No foe reaction (GDC 2024 Mattson).
   - Baked monsters and props break silhouette and hitbox clarity (LoL VFX guide on scribd 384307037; vfxapprentice LoL tips).
   - One baked angle against 4 cameras (RTVFX 27424).
   - No parallax or depth (Unity particle rendering manual).
   - No ground conformance (three.js DecalGeometry; RTVFX valorant-decals 13160).
   - Additive washout (LoL guide).
   - No scene light.
3. **Nine layers:**
   - per-target hit flash and status shells (three.js InstancedMesh);
   - ground decals;
   - mesh and shader (simonschreibt stylized-vfx-in-rime, how-not-to-create-textures);
   - single-component flipbooks;
   - stretched billboard particles (Unity manual);
   - local light;
   - camera shake and screen effects (rime water edition);
   - hit-stop and timing envelope (GDC 2017 VFX Bootcamp 1023943; RTVFX 20853);
   - audio locked to the hit.
   Genshin GDC 1027539 is cited as a general reference.
4. **Where video stays:**
   - 2D cut-ins (the HoYoverse claim was later downgraded to opinion);
   - offline source for single-component KTX2 atlases (three.js KTX2Loader);
   - looping tileable materials (rime water);
   - out-of-combat UI.
5. **Pipeline.**
   - Assets by kind:
     - video becomes single-component KTX2 atlases (4x4 or 8x4, at most 1024), never a live VideoTexture in the world;
     - stills (rings, arrays, flares) are rotated and scaled by code;
     - meshes with GLSL for the main geometry.
   - Each element in the 4 views:
     - ground elements lie on a flat XZ plane, with a low rim so eye-level views still see them;
     - pillars use crossed planes or a cylinder plus a top cap, blended by abs(dot(view, normal)) (RTVFX 27424);
     - slashes use 3D crescents or crossed ribbons;
     - bursts use an icosphere plus isotropic puffs offset in 3D.
   - 100 foes:
     - one instanced vec4 VFX-state attribute per foe;
     - ground stamps drawn into a render target (three.js WebGLRenderTarget);
     - tight cutouts to cut overdraw [Opinion].
6. **QA gate, 6 stages [Opinion]:**
   1. Semantic purity, checked by the art lead.
   2. Black border: luminance under 0.015 in the outer 8 %, checked by script.
   3. Margins: nothing above RGB 12 in the outer 5 %.
   4. Temporal envelope: a one-shot starts and ends at 0, or a loop cross-fades cleanly (the SSIM 0.92 figure is opinion).
   5. Camera-neutral angle: front-on, top-down or isotropic, never 25–45°.
   6. A 4-camera lab test with 20 dummy foes, then owner sign-off.
7. **Migration of the 49 clips:**
   - 10 creature clips rebuilt as meshes plus cut-ins;
   - 7 scenery clips rebuilt as decals and rock meshes, or cropped if the energy part is clean;
   - about 16 whole-scene ultimates split into kits;
   - about 16 clean clips packed into KTX2 flipbooks.
   Three sprints of 2–4 days each: foe shader, decal manager and hit-stop first. Gaps noted: skinned foes need pooled per-foe uniforms or VAT to batch; a height fade instead of a depth pre-pass on weak GPUs.

## Where Claude disagrees or adds

- The "about 16 clean clips" count is Gemini's guess. Our own audit (two independent passes, 15/11) found **17 clips with problems**:
  - creatures: ult-wood-primordial-tree, ult-metal-geng, ult-ice-cold-silence, ult-fire-one-spark, ult-void, ult-blood, ult-water-profound-sea-v2, ult-star, pillar-thunder-field, pillar-light-judgement;
  - scenery: astral-kunpeng, pillar-fire-meteor, pillar-thunder-single, ult-earth-ink-peaks, ult-light, ult-poison, ult-wind-firmament.
  The 30 expansion clips are mostly isolated summons on black. Those are Type C by Gemini's rule: no stray content, but a fixed angle.
- **pillar-thunder-single**, the source the Ngũ Lôi v38 round uses, has a baked rock heap at its base. That base must be masked or cut before use.
- A cut-in that reuses a whole-scene clip still has to meet the 8.5 bar and our own art rules. "Reuse in a cut-in" is not a free pass.
- Instanced foes: our foes are skinned. Per-foe uniforms on pooled skinned meshes come before VAT. Measure first (PERF_BUDGET).

---

# Part 2: where Firefly video fits in the game (15/11, later)

The owner asked: "video áp dụng cho các hiệu ứng dạng năng lượng sẽ đẹp hơn phải không… dạng video firefly sẽ thích hợp nhất cho những đoạn nào của game, những loại nào nên dùng video, những cái nào làm cũng được không làm cũng không sao, và những cái nào không nên làm". Asked in the same chat, Gemini 4 Argon, High.

## Verdicts

| Round | What | Verdict |
| --- | --- | --- |
| 3 | Firefly vs shaders, particles and sims, plus the 4-tier table for 16 game parts | PASS |
| 4 | Strict citation and contradiction review | **No answer**: Gemini stayed on "Searching the web" for more than 8 minutes and returned nothing. The first send of this request was also lost when the tab was navigated. **So there is only one PASS, not two.** Claude's own source checks below stand in for part of that review. |

## Tóm tắt (300 từ)

**Video Firefly có đẹp hơn cho hiệu ứng năng lượng không?** Gemini trả lời **không**, với hiệu ứng nằm trong thế giới 3D. Firefly cho chuyển động kiểu tranh vẽ, nhưng:
- không tuân theo vật lý chất lỏng, nên lửa và khói "chảy như sơn";
- khung hình nhấp nháy, khó lặp mượt;
- chỉ có một góc nhìn;
- không bẻ cong theo quái hay đổi bán kính được.

Shader và hạt chạy 60 khung hình, điều khiển hoàn toàn bằng code. Blender hoặc EmberGen cho alpha thật, motion vector, và render được cả mặt bên lẫn mặt trên từ cùng một mô phỏng. Firefly chỉ hơn ở hình hiển thị trên màn hình (2D) và ở nguồn cho một cụm hiệu ứng đơn.

**Bảng 4 mức cho game mình:**

| Mức | Phần nào của game |
| --- | --- |
| **NÊN dùng video** | cut-in và cinematic; nền title và menu; màn loading; chuyển cảnh; phần cut-in 2D của tuyệt kỹ |
| **TÙY** (một flipbook đơn làm lớp phụ) | bùng nổ khi trúng; chớp lúc tung chiêu; khói khi quái chết; thác nước hoặc gợn nước dán lên lưới; một lần lóe sáng của UI |
| **TRÁNH** | tụ lực (thời gian theo tốc độ gõ); dư âm; hào quang vật phẩm; khí chất nhân vật; sương và mây; viền sáng nhiều icon cùng lúc |
| **CẤM** | phần bay của chiêu (kiếm, chém, tia); vết trên mặt đất (vẽ bằng ảnh tĩnh, code xoay); tuyệt kỹ làm thành một thẻ video cả cảnh trong thế giới |

**Quy tắc nguồn Firefly:**
- một clip chỉ một chất liệu;
- nền đen thật, hoặc tùy chọn nền trong suốt của model Firefly Video (đã kiểm: có);
- hiệu ứng nằm trong 80 % giữa khung;
- clip một lần thì đầu và cuối đen, clip lặp thì dùng cùng một ảnh đầu và cuối;
- thẻ trong thế giới chỉ dùng hình đối xứng tròn, hoặc nhìn thẳng hay từ trên xuống, không dùng góc 25–45°.

**Em không đồng ý ở hai điểm:**
1. "Firefly không bao giờ hơn" là quá tay. Thực tế đã chứng minh: cột lôi `i2v-thunder-energy-sharp-i2v5` được anh duyệt, và các cụm lửa, sét đơn đẹp hơn shader của mình. Nên giữ Firefly làm **nguồn thành phần**, nhưng phải qua cổng kiểm.
2. Gemini đề xuất Blender headless. Hướng này hợp với luật của anh, nhưng phải thử một mẫu trước rồi mới làm loạt.

## Firefly vs shaders vs sims (Gemini, condensed)

> VERDICT: No—Adobe Firefly image-to-video is NOT better than real-time shaders, particles, or Blender/EmberGen simulations for 3D in-world energy VFX; it is only superior for 2D screen-space UI/cut-ins and as a rapid ideation or single-element flipbook source when paired with heavy post-processing.

How Gemini compared the three routes:

| Criterion | What Gemini found | Better route |
| --- | --- | --- |
| Motion | Firefly: painterly, no fluid physics. Shaders: any frame rate. Sims: true vorticity, motion vectors. | Shaders for slashes, beams, qi and water flows; sims for turbulent fire and smoke. |
| Coherence and alpha | Firefly: 24 fps, 5 s, H.264 flicker. A transparent-background option exists. Sims: lossless EXR with premultiplied alpha, normals and 6-point lighting. | Shaders and sims. |
| Control | Firefly output is flat pixels. Shaders bend, scale and recolour at run time. | Shaders. |
| Loop | Firefly start/end keyframes can bounce at the seam. Shaders loop by fract(). EmberGen has a looping toggle. | Shaders and EmberGen. |
| Angle | Firefly bakes one angle. Shaders are native 3D. A VDB sim can render side and top flipbooks. | Shaders or meshes. |
| Cost | Firefly is already paid. Shaders and Blender cost nothing. EmberGen costs $300 in year one. | |
| Licence | Firefly native models are commercial-safe; partner models are not. Blender output belongs to its author. EmberGen exports are royalty-free. | All three pass. |

## Tier table (Gemini, condensed; full specifications in the skill file)

| # | Part | Tier |
| --- | --- | --- |
| 1 | Cut-ins and cinematics | SHOULD |
| 2 | Title and menu backgrounds | SHOULD |
| 3 | Loading | SHOULD |
| 4 | Screen transitions | SHOULD |
| 5 | Ultimates | SHOULD for the 2D cut-in; NEVER as one 3D card |
| 6 | Skill impact, secondary bursts | OPTIONAL |
| 7 | Skill release | OPTIONAL |
| 8 | Foe deaths | OPTIONAL |
| 9 | Map ambience | OPTIONAL for waterfalls and caustics on meshes; AVOID for fog and clouds |
| 10 | UI glow | OPTIONAL for one flare; AVOID for many icons |
| 11 | Skill charge | AVOID |
| 12 | Aftermath | AVOID |
| 13 | Item auras | AVOID |
| 14 | Character presence | AVOID |
| 15 | Skill travel | NEVER |
| 16 | Ground decals | NEVER (a Firefly Image still at 90° is fine) |

Universal source rules (Gemini):
1. Pure black, or native alpha, then crush levels.
2. One material per clip.
3. An 8–10 % margin, enforced by a vignette at atlas time.
4. A loop uses the same start and end still; a one-shot goes from black to black.
5. World cards only isotropic or orthographic, never 25–45°.

## Source check, part 2 (Claude)

| Claim | Source | Result |
| --- | --- | --- |
| Firefly Video can generate transparent-background video, 24 fps, 5 s, with start and end frames | helpx.adobe.com …/generate-videos-with-transparent-backgrounds.html | **Verified** (page updated 18 Aug 2026; needs the Firefly Video model and the "Transparent background" option). |
| EmberGen has looping sims and exports motion vectors, 6-point lighting, normals and depth | jangafx.com/software/embergen | **Verified**. |
| Blender licence: "What you create with Blender is your sole property" | blender.org/about/license | **Not found** in the page text. The claim that Blender output belongs to its author is well known, but this quote is unconfirmed. |

## Where Claude disagrees (part 2)

- "Firefly never better for 3D energy" is too broad for us.
  - The owner approved `i2v-thunder-energy-sharp-i2v5` as a column source, and Firefly's single bursts beat our hand shaders.
  - Keep Firefly as a component source (OPTIONAL tier) behind the source gate. Use shaders for structure, and Blender only after one sample.
- Gemini's round 4 review never arrived, so this part has one PASS. Treat its numbers (card caps, atlas sizes, luminance thresholds) as starting values to measure in the lab, not rules.
- Firefly's transparent-background option is new to us. Test it on one component before switching the black-background pipeline.
