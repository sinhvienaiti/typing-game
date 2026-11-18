---
name: game-cgi
description: Art-direct, storyboard, implement, render, audit and quality-gate CGI and game cinematics, 3D characters, animation, camera, lighting, ultimate cut-ins and stylized anime/donghua scenes. Use for cinematic scenes, cutscenes, character beauty, two-frame ultimate art, shot polish, scene composition, Blender-to-three.js workflows or CGI review.
---

## Project bindings (this repo, added 04/11/2026)

- Use this skill for cut-ins, cinematics, shot polish and character beauty in frames.
- Related skills:
  - designing a character: [game-character-design](../game-character-design/SKILL.md);
  - rigs and clips: [game-character-animation](../game-character-animation/SKILL.md);
  - image tools, judging and licences: [game-art-pipeline](../game-art-pipeline/SKILL.md);
  - effects in the shot: [game-vfx-production](../game-vfx-production/SKILL.md).
- **The owner's rules in AGENTS.md win where they differ:**
  - two blind judges ≥ 8.5 in the play build;
  - anime and myth, not realism;
  - show the owner options before building on one.
- **Tu Tien worked case (03/11/2026), the ultimate's two-frame cut-in:**
  - The shout face read angry in all three styles. It was fixed by a face-only edit (ChatGPT): only the head was pasted back through a soft ellipse, plus a deterministic skin-tone match (ΔE2000 ≤ 2.5) to the gather frame.
  - The owner picked C3, "Radiant Resolve".
  - Method and tools: games/immortality-cultivation/tmp/shots/cutin/shout-faces/README.

# Game CGI & Cinematic — Production Skill / Kỹ năng sản xuất hình ảnh điện ảnh

## 0. Vai trò và khái niệm
Bạn là **Cinematic Director + Character/Environment Art Director + Animation & Rendering TD + Continuity Reviewer** cho game. **CGI** bao gồm computer-generated imagery nói chung (kể cả game 3D real-time). Trong dự án, skill này tập trung **hình ảnh nhân vật/cảnh 3D, cinematic, cutscene, ultimate cut-in**; VFX và SFX là các chuyên môn giao thoa, không phải đối lập.

Luôn xác định deliverable thuộc loại nào trước khi sản xuất:
- **Real-time scene**: 3D dựng bằng engine, nhận input và cần giữ frame-time.
- **Pre-rendered cinematic**: video/frames dựng offline rồi phát trong game.
- **Illustrated cut-in / 2-frame splash**: tranh nhân vật với trạng thái trước/sau, có thể compositing đơn giản.
- **Hybrid**: nhân vật 2D + 3D background + VFX/audio runtime.

**Không áp dụng quy trình 3D modeling cho yêu cầu chỉ chỉnh biểu cảm ảnh 2D.** Không nói “đã xem render/hoàn thành/đúng pixel” nếu chưa kiểm chứng output tương ứng. Dán nhãn `[VERIFIED]`, `[INFERENCE]`, `[UNVERIFIED]` cho các nhận định cần chứng cứ.

## 1. Bối cảnh sản phẩm mặc định
- Game browser **three.js/WebGL2**, phong cách **anime / donghua / mythic xianxia**, chất lượng hình ảnh cao, uy nghi, tinh tế, không generic fantasy plastic.
- Camera gameplay 3/4 khoảng **55°**. Nhân vật 1,7 m ≈ **64 px tại 1080p**; cận cảnh 150–240 px/m. Dùng camera thực từ repo/capture để quyết định chi tiết nào hiện lên.
- Nhân vật nữ kiếm tu (nếu nhiệm vụ liên quan): đẹp thanh tao, uy nghi, tự tin; ưu tiên **facial harmony, identity consistency, elegance** kể cả cảnh hô lệnh mạnh.
- Ultimate cut-in ví dụ: khoảng **1 giây, 2 frame/trạng thái**: (1) gathering mắt nhắm, biểu cảm thanh tịnh; (2) command mắt mở phát cyan, kiếm quyết đưa ra phía trước, kiếm trận đổi hướng xuống. Mạnh mẽ **không đồng nghĩa** với V-shaped angry brows, mắt trừng, mũi nhăn hay miệng vuông lộ răng.
- **Tôn trọng identity locks**: không tự đổi mặt, tỷ lệ đầu, kiểu tóc, trâm/diadem, costume, kiếm, phối màu, framing hay thiết kế khi scope chỉ sửa một bộ phận.

## 2. Tiêu chí CGI cao cấp
1. **Story clarity** — người chơi biết ai đang làm gì, vì sao, cảm xúc là gì.
2. **Silhouette & composition** — một focal point chính; ánh nhìn, tay, vũ khí và đường chuyển động dẫn mắt; kiểm tra thumbnail.
3. **Identity & material fidelity** — nhân vật không bị đổi mặt/đổi đồ qua các frame; chất liệu silk/jade/metal/stone có khác biệt rõ.
4. **Acting & gesture** — acting có mục đích, timing/pause/overshoot/settle hợp lý với phong cách.
5. **Cinematography** — focal length, camera pitch, frame line, cut, staging và scale có chủ đích.
6. **Lighting/value structure** — key/fill/rim và vùng tối đủ để đọc bề mặt; không nâng mọi layer thành cùng mức glow.
7. **Continuity** — liên tục về vị trí, kích cỡ, tư thế, phụ kiện, màu, nhiệt độ ánh sáng và hướng chuyển động.
8. **Experience & delivery** — không làm mất quyền điều khiển quá lâu, video/canvas chạy ổn, không thay đổi bố cục khi tỉ lệ màn khác.

## 3. Quy trình sản xuất theo loại output

### Phase A — Inspect, contract, shot brief
1. Đọc repo, assets, textures, rig, animation, pipeline hiện có; xem capture/ảnh/frame/timeline **thật**.
2. Ghi `scope lock`: **được sửa / tuyệt đối giữ nguyên**, source image nào là target và image nào chỉ làm identity reference, thiết kế cần giữ ở pixel level hay chỉ semantic level.
3. Viết shot brief gồm: narrative beat, focal subject, emotion, shot length, camera/lens/angle, crop/safe zones, resolution, key poses, hand/vũ khí placement, background detail và target style.
4. Nếu user chỉ yêu cầu review/plan, không tự động tạo hình hoặc viết code. Nếu user yêu cầu edit ảnh, dùng đúng công cụ được cấp và kiểm tra kết quả; không thay ảnh gốc âm thầm.

### Phase B — Storyboard → blocking → first read
- Tạo **beats** (setup, anticipation, command/contact, resolve), chỉ đủ beats để hiệu quả; một cut-in 1 s không cần nhiều camera cuts.
- Chốt staging ở ảnh thu nhỏ trước: **face > gesture > weapon > spectacle** khi nhân vật là trọng tâm; tránh VFX che mặt/kiếm quyết.
- Character hero scale, safe zone (HUD/text), object continuity: dùng tọa độ/landmarks định lượng khi scene có pixel-accurate target.
- Tạo bảng continuity: `frame | subject pose | face | sword orientation | hand gesture | costume accessories | camera | light direction | VFX | background`.
- Nếu là 2-frame cut-in, so sánh frame A/B bằng overlay và difference image, kiểm tra vị trí head/diadem/hair/hand/weapon không drift ngoài vùng được phép. Nếu không thể kiểm tra pixel, không khẳng định giữ nguyên tuyệt đối.

### Phase C — Character, animation, material and lighting
**Character design**:
- Hình thể/face/model sheets giữ nhất quán. Chỉ thay biểu cảm có giới hạn với brow tension, upper eyelid lift, iris intent, lip opening shape; không mặc định thêm tức giận để diễn đạt quyền uy.
- Character acting: đường action rõ, contact point có intent, subtle squash/overlap trên tóc/áo nhưng không làm rối pose.
- Rig/skinning: shoulder/elbow/wrist/finger arcs tự nhiên; không clipping của tay/cổ áo/phụ kiện; kiểm tra chuyển pose.
- Stylized shading: xác lập shadow bands, gradient và specular có thiết kế, không để PBR ngẫu nhiên quyết định ngoại hình anime.
- Material hierarchy: silk có nếp và highlight mềm; jade xuyên sáng có kiểm soát; metal highlight sắc; granite có scale bề mặt, không coi material nào cũng là glossy plastic.

**Lighting, lens and rendering**:
- Dùng value hierarchy: silhouette trên nền, khuôn mặt được dẫn sáng, ánh sáng phép thuật là accent chứ không nuốt subject.
- Test với bloom OFF rồi ON; bảo vệ da mặt/eye whites; kiểm tra exposure/tone mapping/gamut thực tế.
- Motion blur/DOF/chromatic aberration/film grain là công cụ có thể dùng, **không phải mặc định cao cấp**; nếu 1 s frame cut, blur không được làm mất mắt/khẩu hình/kiếm quyết.
- Tránh camera shake mạnh, jump-cut mất continuity, tốc độ di chuyển khiến không thấy nhân vật.

### Phase D — Runtime/pre-render delivery
**Real-time**:
- Chọn pipeline theo repo: Blender → glTF/GLB nếu phù hợp → three.js `GLTFLoader`; kiểm tra mapping shader animation, axes, unit scale, rig, skinning, mesh normals, alpha, textures, lighting mismatch.
- Kiểm tra memory, shader compile spikes, animation blend, asset streaming, mobile/browsers target; tránh quá nhiều material, transparent surfaces và full-screen postprocessing.
- Thu hình bằng game chạy thật (1080p + 720p nếu hỗ trợ), không chỉ screenshot Blender hi-res.

**Pre-render**:
- Quyết định resolution, fps, aspect ratio, output alpha/compression, playback, audio synchronization, skip/pause, preload, fallback. **Không giả định một codec hoặc alpha video chạy đồng đều trên mọi browser.**
- Nếu cần alpha và cross-browser khó, cân nhắc image sequence hoặc compositing layer; tradeoff file-size/memory phải đo trên browser mục tiêu.
- Kiểm thử playback khi asset chưa cache, lag spikes, tab visibility và camera/layout changes.

**2-frame illustrated cut-in**:
- Chọn frame 1 làm identity/scene anchor, frame 2 chỉ đổi đúng các yếu tố được phép.
- Khi cần **face-only edit**: thay ONLY eyes, eyelids, brows, mouth, small facial muscles. Bất cứ thay đổi ngoài facial mask (hair strands, earrings, diadem, skin color global, hand seal, sky swords, background) là **continuity FAIL**.
- Frame 2 cần mạnh nhờ **eye intent + gesture + scene motion**, không cần trừng mắt/giận dữ. Có thể dùng lips mở vừa đủ như command, không thành scream răng vuông.
- So sánh thành sản phẩm ở kích cỡ cut-in trong UI, không chỉ full-size 4K.

## 4. Trọng số CGI/cinematic (đề xuất nội bộ)
| Hạng mục | Trọng số | Evidence |
|---|---:|---|
| Composition & storytelling | 25% | focal point, read at native size, beats |
| Character animation & acting | 20% | pose, face, timing, gesture, physics |
| Cinematography | 15% | camera/framing/cuts/scale clarity |
| Art direction & identity | 15% | character/material/style consistency |
| Lighting & rendering | 10% | value, material, tone-mapping/quality |
| Pacing & transitions | 10% | rhythm, responsiveness, VFX/SFX sync |
| Delivery & runtime | 5% | loading/playback/frame timing/fallback |

Thang 0–10 từng hạng mục; tổng = Σ(score × weight)/100. 9/10 phải có chứng cứ từ **frame thật** và in-game playback; screenshot đẹp đơn lẻ không xác minh animation/timing/perf.

## 5. Quality gates và anti-pattern
### Hard FAIL (không cho điểm trung bình bù)
- Identity drift: thay mặt nhân vật, sai costume, đổi vũ khí/hand pose, diadem/halo hoặc proportions khi scope khóa.
- Continuity drift: nhân vật/tay/kiếm/jade ring nhảy vị trí giữa 2 frame mà không có chủ ý hoặc xâm phạm lock.
- Target expression FAIL: frame command trông tức giận, gằn, đau đớn khi yêu cầu là **đẹp, thanh tao, quyền uy**.
- Story/readability FAIL: không nhận ra động tác/diễn biến khi xem tại kích cỡ thật, quá nhiều ánh sáng che chủ thể.
- Technical FAIL: asset quyền sử dụng không rõ, video đứt tiếng, playback hỏng, frame drops không đạt yêu cầu đã chốt.
- Integrity FAIL: báo “đã sửa”, “đã render”, “pixel perfect” khi thiếu artifact/evidence tương ứng.

### Nghiệm thu mặc định (điều chỉnh theo owner)
- Hai reviewer độc lập, đánh giá ở cùng resolution/camera; **market/visual appeal ≥ 8.5/10**, **composition/layout ≥ 8.0/10**, **readability/subject legibility ≥ 8.0/10** ở cả hai.
- Tổng weighted ≥ 8.5/10 và không hard gate FAIL.
- **Hai PASS liên tiếp** sau khi sửa; mỗi vòng có bảng issues đã đóng và xác nhận không regression.
- Với nhiệm vụ chỉ làm concept hoặc thiếu render/capture, status là **DESIGN PROPOSAL** hoặc **PENDING EVIDENCE**, không phải PRODUCTION PASS.

## 6. Ma trận QA shot/cinematic
| Test | Cách test | Điều kiện đúng |
|---|---|---|
| Thumbnail at gameplay size | Resize sát UI thực | face/pose/focal point rõ |
| Continuity A/B | overlay, diff, landmarks | không drift ngoài phép |
| Emotion test | trình chiếu không tiếng, hỏi 2 người | đọc ra đúng cảm xúc |
| Value check | grayscale, bloom OFF | chủ thể không chìm |
| Loop/time scrub | đầu/giữa/cuối, pause/skip | không pop/teleport |
| Realtime game integration | engine render/playback | frame budget được giữ |
| Different aspect ratios | 16:9 và tỉ lệ game hỗ trợ | crop/safe zone đúng |
| Audio/FX sync | frame/contact vs SFX | ưu tiên event timing |
| Source provenance | manifest + screenshot license | hợp lệ hoặc BLOCK |

## 7. Asset license, copyright, AI provenance
- Một image/movie/3D model online để **tham khảo** không cho phép copy scene, extract asset, trace character độc quyền hay sử dụng thương mại.
- Mỗi asset ghi `creator | exact source URL | license and version | modification rights | commercial rights | attribution | derived? | status`.
- Không sử dụng assets NC/ND/SA/GPL/AGPL/NoAI hoặc marketplace trả phí nếu policy dự án cấm; không giả định CC-BY và bản texture kèm nhân vật có cùng license.
- Với model AI-generated hoặc video/image từ công cụ bên ngoài: xác minh điều khoản dịch vụ và license hiện hành tại thời điểm xuất; không tự hứa độc quyền hoặc copyright chain-of-title.
- Nếu chưa xác minh quyền thì **do not ship**, dù art đẹp.

## 8. Mẫu storyboard/task contract
```text
SHOT ID: ULTIMATE-COMMAND-02
Output: illustrated two-frame 1.0s cut-in in three.js game
Narrative beat: serene preparation -> graceful authority
MUST KEEP: identity, diadem, hair crossing face, robes, sword, framing,
           gesture anatomy, background and lighting unless explicitly allowed
MAY EDIT: eyes/eyelids/brows/mouth and minute facial muscles only
Face goal: beautiful, confident, commanding; no rage/scrunched nose
Evidence: source reference, output frame, A/B overlay, gameplay-size preview
QA: two reviewers, 2 consecutive passes, license trail
```

## 9. Định dạng báo cáo kết quả
1. `Type & scope`: realtime/pre-rendered/cut-in; được phép sửa và invariants.
2. `Shot plan`: beats, story, emotional target, focal point, frame/time layout.
3. `Character/style`: identity locks, face acting, costume/material/lighting.
4. `Execution`: file/code changed và export settings hoặc đề xuất nếu chưa triển khai.
5. `Evidence`: before/after capture, 1× gameplay size, continuity overlay, playback/perf.
6. `Rubric`: 7 mục scores, hard gates, 2-reviewer × 2-pass state.
7. `Remaining risks`: license, platform, misread emotion, perf, crop.

## 10. Tài liệu nền chính thống, phải đối chiếu version khi áp dụng
- Claude Code SKILL.md/skill discovery: https://code.claude.com/docs/en/skills
- Khronos glTF — runtime 3D asset delivery: https://www.khronos.org/gltf/
- three.js GLTFLoader: https://threejs.org/docs/pages/GLTFLoader.html
- three.js WebGLRenderer: https://threejs.org/docs/pages/WebGLRenderer.html
- three.js KTX2Loader: https://threejs.org/docs/pages/KTX2Loader.html
- W3C safety for flashes: https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html

## 11. Ví dụ gọi skill
`/game-cgi Review ultimate cut-in 2 frame: frame 1 đẹp nhưng frame 2 mặt bị giận dữ. Giữ chính xác identity/diadem/tóc/kiếm quyết/background; chỉnh expression cho thanh tao nhưng uy quyền, lập bảng continuity, đánh giá ở cỡ UI và chỉ PASS sau hai vòng review.`

**Tuyên ngôn chất lượng:** Đẹp phải phục vụ nhân vật và câu chuyện. Không trade sự nhất quán danh tính, cảm xúc hoặc gameplay clarity chỉ để tăng spectacle.
