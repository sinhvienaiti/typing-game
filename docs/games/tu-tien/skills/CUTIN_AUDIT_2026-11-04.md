# Kiểm tra cut-in tuyệt kỹ C3 theo `game-cgi` (04/11/2026)

Đối tượng: cut-in của tuyệt kỹ **Milky-Way Sword Rain · 天河劍雨** trong lab kỹ năng, phong cách **C**, mặt hô **C3 "Radiant Resolve"** (`tt-cutin-c-shout-e3-head-skin-up2x.v2-try1.png`), mã `games/immortality-cultivation/src/lab/cutin.ts` và lời gọi ở `src/lab/skills-main.ts` (`ULT_CUTIN`, `startUltimate`).

Bằng chứng: video chủ dự án `typing-game-review/owner-review/2026-11-04/tu-tien/orbit-c3/lab-orbit-c3-1280x720.mp4` (60 fps, 28,25 s; cut-in ở khoảng 20,5–22,2 s), dò cắt cảnh bằng ffmpeg, hai khung đầy đủ 1280×720 (tụ lực 21,0 s; hô 21,8 s) và tờ tổng hợp `typing-game-review/captures/tu-tien/cutin-audit/cutin-contact-sheet.jpg` (20,25–28,25 s, 6 khung/giây). Không mở trình duyệt, không tạo ảnh, không sửa mã.

Trạng thái: **PENDING EVIDENCE**. Đây là một người chấm (Claude), không mù, chấm trên video lab, không phải bản play build; chưa phải một lượt PASS theo cổng hai giám khảo của `game-cgi`.

## 1. Thời gian

| Pha | Mã (giây từ lúc bắt đầu) | Đo trên video (giây video) | Độ dài đo |
| --- | --- | --- | --- |
| Vào: lau mực trái sang phải + trượt | 0 → 0,20 (`WIPE_S`), trượt `easeOut(t/0.2)` | 20,53 (cắt cảnh, ±1 khung) | ≈ 0,2 s |
| Tụ lực (mắt nhắm, kiếm quyết trước ngực) | 0,20 → 1,08 (`shoutAt = min(1.08, 0.64 × 1.7)`) | 20,53 → 21,60 | 1,07 s (cả lau) |
| Cắt sang hô: chớp, đẩy cận, rung | 1,08; chớp 0,13 s, đẩy 0,14 s, rung 0,18 s / 8 px | 21,60 (cắt cảnh) | — |
| Hô (mắt cyan mở, tay vươn, kiếm chĩa xuống) | 1,08 → 1,56 | 21,60 → ≈ 22,1 | ≈ 0,5 s |
| Ra: dải khép về đường giữa | 1,56 → 1,70 (0,14 s) | ≈ 22,08 còn một lát nghiêng; 22,25 đã về sân | ≈ 0,1–0,15 s |
| **Tổng** | **1,70 s** (`ULT_HOLD`, `?cutin=` mặc định 1.7) | **≈ 1,65 s** | |
| Đòn đầu trên sân | chiêu chỉ phát khi `cutin.update` trả `true` (hết cut-in) | vòng kiếm xuất hiện ≈ 22,25; số sát thương đầu ≈ 22,6 | trễ ≈ 1,7–2,1 s sau phím cuối |

So với yêu cầu: `game-cgi` lấy ví dụ cut-in khoảng **1 s**; canon D58 (4) cũng ghi "khoảng 1 s", và D58 (1) đòi đòn đầu đi trong **≤ 50 ms** sau phím đúng cuối cùng. Luật chủ dự án (theo brief của phiên này): cut-in đến **sau đòn đầu tiên**. Hiện tại cut-in chạy **trước** chiêu và giữ đòn đầu lại ≈ 1,7 s.

## 2. Những gì thấy (trước khi chấm)

**Đọc ở 1280×720.** Hai nhịp đọc rõ: khung tụ lực (mắt nhắm, cằm ngẩng, kiếm quyết trước ngực, xoáy ngân hà, kiếm bay ngang) và khung hô (mắt cyan mở, miệng hô, tay vươn tới người xem, kiếm đổi hướng chĩa xuống). Mặt là điểm nhấn trong cả hai. Dải tranh chỉ chiếm khoảng 60 % chiều cao (`ART_BAND`), phần trên và dưới là sân tối, phẳng; nhãn lab góc trái trên vẫn hiện.

**Mặt và liên tục.** Danh tính giữ được: tóc, trâm, hoa văn hạc trên áo, quầng vàng sau đầu như nhau. Khung hô thay cả tư thế (tay từ trước ngực ra vươn thẳng) và nền (kiếm đổi hướng): đó là đổi có chủ ý theo `game-cgi` (kiếm trận đổi hướng xuống). Đầu xê dịch nhẹ giữa hai khung (neo mặt gather 0.24/0.38 so với shout 0.31/0.233 của ảnh khác kích cỡ); chưa đo overlay hay ảnh hiệu nên không khẳng định khớp. Mặt C3 thanh tao, quyền uy, không giận: không vi phạm cổng biểu cảm.

**Thời gian.** 1,65–1,7 s, dài hơn mốc ~1 s. Nhịp tụ lực 1,07 s là ảnh tĩnh (chỉ có trượt parallax và hạt), nên cảm giác chờ. Nhịp hô ≈ 0,5 s ổn nhưng bị khép sớm.

**Chuyển cảnh.** Vào: lau mực có vết bắn, khá tốt nhưng mảnh, không có vệt sáng dẫn đầu. Cắt sang hô: chớp trắng, đẩy cận, rung 8 px: có lực. Ra: dải khép về đường giữa trong 0,14 s và trượt nghiêng; không có quét sáng, không có mảnh mực tan, sân hiện lại đột ngột.

**Lớp hào quang quanh khung.** Hào quang có trong **tranh** (quầng vàng, sao lấp lánh, xoáy ngân hà). Khung dải thì **trơn**: hai đường viền vàng mảnh, không phát sáng, không có mép mực sáng, không vệt sáng chạy dọc mép, không hạt bay ra ngoài dải. 26 hạt sao và 18 vệt tốc độ của mã gần như không thấy trên nền tranh sáng. Ngoài dải chỉ có sân tối: không có tia sáng, không bloom, không mảnh kiếm.

**Chữ gọi chiêu.** Hán tự trắng nét bút + "MILKY-WAY SWORD RAIN" chữ chân vàng ở góc phải dưới, ấn đỏ đóng khi hô. Đọc được nhờ bóng tối, nhưng chữ nhỏ (≈ 3–4 % chiều cao), nằm đè lên vùng kiếm và núi bận rộn, chữ vàng trên nền cyan kém tương phản; không có tấm nền, nét mực lót, vệt sáng quét qua chữ hay lấp lánh. Trông như phụ đề, chưa như tên tuyệt kỹ.

**Nối với sân.** Thế giới tối đi dưới cut-in (`ultDark`), sau đó vòng kiếm và mưa kiếm rơi. Nhưng không có cầu nối hình ảnh: kiếm trong tranh chĩa xuống mà không có thanh nào bay ra khỏi dải, không có vệt sáng kéo tiếp xuống sân, màu cyan của tranh không thành chớp màn hình lúc mưa kiếm chạm. Cut-in và chiêu là hai cảnh nối tiếp, không phải một động tác.

## 3. Điểm theo bảng `game-cgi` (một người chấm, chưa mù)

| Hạng mục | Trọng số | Điểm | Lý do |
| --- | ---: | ---: | --- |
| Composition & storytelling | 25 % | 7,5 | Hai nhịp rõ, mặt là tiêu điểm; dải chỉ 60 % màn, chữ nằm trên vùng bận, không có nhịp "kết" nối sang sân. |
| Character animation & acting | 20 % | 7,5 | Mặt C3 đẹp, đúng "radiant resolve"; nhưng là hai ảnh tĩnh, nhịp tụ lực 1,07 s không có chuyển động nào trên nhân vật (tóc, tay áo, mắt). |
| Cinematography | 15 % | 7,0 | Một dải, trượt parallax, đẩy cận khi hô; không đẩy về mắt, không khung phụ, không đổi cỡ cảnh. |
| Art direction & identity | 15 % | 8,5 | Tranh đạt mức thị trường, danh tính và trang phục nhất quán, đúng anime/donghua thần thoại. |
| Lighting & rendering | 10 % | 7,0 | Ánh sáng trong tranh tốt; viền dải trơn, không phát sáng, chữ phẳng, hạt mã quá yếu. |
| Pacing & transitions | 10 % | 6,0 | 1,7 s so với ~1 s; giữ đòn đầu ≈ 1,7 s (trái D58 và luật "sau đòn đầu"); ra cảnh đột ngột. |
| Delivery & runtime | 5 % | 8,0 | Có preload, thời gian tất định, `?cutin=` dưới 0,6 s bỏ tranh; chưa đo dung lượng ảnh 3671×1713 và thời gian giải mã. |
| **Tổng có trọng số** | | **7,4** | Dưới 8,5. |

Cổng cứng: danh tính PASS; biểu cảm PASS; đọc được PASS; liên tục **PENDING** (chưa có overlay/ảnh hiệu); kỹ thuật PENDING (chưa đo trên play build). Cổng ngành: appeal ≈ 8,0 (tranh 8,5 bị kéo xuống bởi khung trơn và chữ phụ đề), bố cục 7,5, đọc 8,0. Kết luận: **chưa đạt 8,5**, cần một vòng cải tiến.

## 4. Các lỗ hổng cụ thể

1. **G1 — Thứ tự sai so với luật:** cut-in chạy trước chiêu và chặn đòn đầu ≈ 1,7 s. Cần: phím cuối → đòn/kiếm đầu ≤ 50 ms → cut-in phủ lên khoảnh khắc trúng đầu tiên → mưa kiếm chính.
2. **G2 — Quá dài:** 1,7 s, nhịp tụ lực tĩnh 1,07 s. Mục tiêu ≈ 1,0–1,1 s (tụ ≈ 0,45, hô ≈ 0,45, ra ≈ 0,15).
3. **G3 — Khung dải trơn:** hai đường vàng mảnh, không có mép mực sáng, vệt sáng chạy viền, lấp lánh ở góc, hạt bay khỏi dải. Trái luật "không gì trần trụi" và "hiệu ứng quanh mọi vật".
4. **G4 — Hạt mã không thấy:** 26 sao và 18 vệt tốc độ biến mất trên tranh sáng; lớp hào quang thật nằm trong tranh chứ không trong lớp động.
5. **G5 — Chữ gọi chiêu như phụ đề:** nhỏ, trên vùng bận, vàng trên cyan; không tấm nền, nét mực lót, quét sáng, lấp lánh.
6. **G6 — Ra cảnh đột ngột:** khép 0,14 s về đường giữa, không quét sáng, không mực tan, không nối màu.
7. **G7 — Không cầu nối với sân:** kiếm trong tranh không bay ra; không có vệt sáng hay chớp cyan dẫn mắt từ dải xuống điểm rơi.
8. **G8 — Nhân vật tĩnh trong nhịp tụ lực:** không có tóc, ruy băng, tay áo hay ánh mắt chuyển động; không đẩy cận về mắt khi hô.
9. **G9 — Liên tục chưa có bằng chứng:** chưa có overlay A/B, ảnh hiệu và bảng liên tục theo `game-cgi` §3.
10. **G10 — Nhãn lab và nền ngoài dải:** nhãn lab đè lên khung; phần sân ngoài dải tối phẳng, không có lớp tối có kết cấu hay tia sáng.

## 5. Brief cho vòng cải tiến (giao thức hai lần duyệt)

Dán nguyên khối dưới vào ChatGPT (Chat mode, thinking High) theo `.agents/skills/agent-orchestration/references/double-review.md` §1, rồi tự duyệt §2 hai lần, handoff §2b, Gemini §3. Lưu câu trả lời nguyên văn kèm bảng kiểm vào `docs/games/tu-tien/source/`.

```text
Role: you are the analyst for a game project. Research, analyse and propose a concrete solution.
If you need clarifications, ask all of them in one message before you start.

Goal: raise the ultimate-skill cut-in of "Tu Tien Thu Ai" (a browser xianxia typing-defence game, three.js + DOM overlay) from about 7.4/10 to at least 8.5/10 from two independent blind judges, in the built play host at 1280x720, with two consecutive passes. The cut-in belongs to the ultimate "Milky-Way Sword Rain / 天河劍雨" of the heroine (a sword cultivator: black hair, gold diadem, navy and white robe with cranes, gold halo behind her head).

Facts and current state (measured 04/11/2026 from a 60 fps capture and the code):
- Two illustrated frames shown in one slanted band covering about 60% of screen height (rest of the screen is the dimmed battlefield):
  - frame A "gather": eyes closed, chin raised, two-finger sword seal at her chest, a cyan galaxy swirl with flying swords pointing right; painted gold halo and sparkles inside the painting.
  - frame B "shout" (chosen face "C3 Radiant Resolve"): cyan eyes open, mouth open, arm extended toward the viewer with the sword seal, the swords now pointing down. Same identity, deliberate pose change.
- Timeline now (total 1.70 s, the game and typing timer are paused):
  - ink-splash wipe in 0.20 s, then a static gather hold to 1.08 s;
  - at 1.08 s a white flash 0.13 s, punch-in 0.14 s and an 8 px shake 0.18 s cut to the shout;
  - shout hold to 1.56 s, then the band closes to its middle line in 0.14 s.
- The skill only fires when the cut-in ends, so the first sword lands about 1.7-2.1 s after the player's last correct key.
- The band edges are two thin flat gold lines. Code adds 26 star motes and 18 speed lines, but they are invisible over the bright painting. Outside the band: flat dark battlefield, no light.
- Callout: white brush hanzi plus "MILKY-WAY SWORD RAIN" in small gold serif (about 3-4% of screen height), bottom right over a busy area of swords and mountains; a red seal stamps on the shout. Readable but reads like a subtitle.
- Exit: the band closes and the battlefield reappears with no sweep. Nothing visually links the painted swords to the sword rain on the field.

Constraints (owner rules):
- First hit within 50 ms of the last correct key; the cut-in comes AFTER the first hit, about 1 s long, pausing game and typing timer; on-screen text stays legible (never blurred, darkened or blown out).
- Every visible object and every skill phase carries a radiance layer: glints and star twinkles, fine motes and glitter, soft halos and light rings (at most 0.9 per channel), shimmering rims, thin light rays. Nothing ships bare.
- Effect looks come from art tools (Adobe Firefly Image/Video, Blender renders to flipbooks, painted channel-packed masks); code only places, times and animates them. Code-drawn flames, auras, stars or cracks were rejected as crude.
- Keep the two existing paintings and the C3 face exactly (no identity, diadem, hair, robe or hand change); new layers dress them, never cover her face or hands.
- Player-facing text in English; hanzi allowed as the calligraphic name. No emoji, no CSS-shape stand-ins.
- Fast attack, slow decay: hold the peak, burn down by erosion, never a quick plain fade. Browser budget: the cut-in must not drop frames on a Mac mini M4 at 1280x720.

Already decided by the owner (do not reopen): style C, shout face C3; anime/donghua mythic look; two-frame illustrated cut-in (not a 3D cinematic); English callout with hanzi.

Taste: anime/donghua and myth, radiant, luxurious, stylish, modern, captivating; never realism as the goal; never plain.

What we think must change (challenge or improve these):
1. Order and length: first sword hits at once, then the cut-in about 1.0-1.1 s (gather about 0.45 s, shout about 0.45 s, exit about 0.15 s), then the main sword rain.
2. An ink-light frame for the band: painted ink-brush edges with a glowing inner rim, light streaks running along the edges, star glints at the corners, motes drifting out of the band.
3. Transition sweeps: an entry sweep (ink stroke with a bright leading edge), a light-slash cut to the shout, and an exit where the band shatters or dissolves into ink and light that streams down onto the battlefield.
4. Light layers over the paintings: god rays or a halo bloom behind her head, an eye glint on the shout, sparkle motes that read over a bright painting (dark-edged or additive with size and contrast tuned).
5. A premium callout plate: brush-stroke backing, larger name, a light sweep across the letters, glints, the seal stamp with a ring burst.
6. A bridge to the field: painted swords that fly out of the band toward the impact point, a cyan screen flash when the rain lands.
7. Subtle life in the gather hold: hair, ribbon and sleeve sway (painted layer split or mesh warp), a slow push toward her eyes.

Deliver:
1) analysis of the problem and its causes;
2) the solution as ordered steps with the reason for each, including for every new art layer: its name, what to paint, the tool (Firefly Image, Firefly Video, Blender, painted mask), the size and format (PNG sequence, atlas, channel-packed mask), and how code animates it;
3) a beat-by-beat timeline table in seconds (beat, layers on screen, art assets, sound cue, camera);
4) the checks: two blind judges at 1280x720 in the play host, scores per game-cgi category (composition 25, acting 20, cinematography 15, art direction 15, lighting 10, pacing and transitions 10, delivery 5), appeal at least 8.5, composition and readability at least 8.0, an A/B continuity overlay with a difference image, frame-time measurement, first-hit latency at most 50 ms;
5) risks and how to check each;
6) what you are not sure about.

Cite a source for every factual claim (game references with cut-ins, such as Genshin Impact, Honkai Star Rail, Wuthering Waves, Arknights, Blue Archive, and donghua openings, with links).
```

Bước sau brief: gửi handoff của ChatGPT cho Gemini (4 Argon, High), cho mỗi bên xem ý chính của bên kia một vòng, kiểm các khẳng định ở nguồn, gộp thành một kế hoạch ghi rõ đóng góp và chỗ bất đồng, rồi mới vẽ lớp mới (Firefly/Blender) và dựng trong lab. Chủ dự án duyệt mẫu trước khi nối vào game.
