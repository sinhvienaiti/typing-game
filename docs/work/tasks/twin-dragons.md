# Song Long toàn sân (ô 2)

**Mục tiêu:** chiêu phủ toàn sân, không phụ thuộc map, đẹp và cân bằng.
**Cách đã chốt:** `docs/games/tu-tien/skills/DRAGON_SKILL.md` §9 (đã gộp, sau cờ `swordKey2`).
**Nghiệm thu:** số §9.8; ô 2 ≤ 45 % sát thương cả trận; video lab cho anh.
**Mã:** `main` của game `35f1b77`.

## Số bot (phiếu 272, 04/11 21:45)
- Đạt:
  - trung vị trúng 14 con; phủ 97,4 %; quạ 95,8 %;
  - đòn đầu ≤ F2; cờ tắt 36/36; bố cục 8/8.
- Trượt:
  - cân hai bên 75 % (đích ≥ 85 %);
  - ô 2 chiếm 45,99 % ở bot Chuẩn (trần 45 %).
- **Bot Chuẩn thắng 15 %.** Cần phân tích (sau 3 việc chính).
- Báo cáo: `games/.wt-ic-twin-fieldwide/tmp/skill-reach/key2-fieldwide/report.md`.

## Nhật ký
- 04/11 20:13–20:46 · Codex · 271, 271b (quét 200 bố cục), 271c (chỉ giải khi có thú trong dải).
- 04/11 21:05 · Claude · gộp `35f1b77`.
- 05/11 00:00 · Claude (làn 2) · đang quay video lab.

## 05/11 ~01:50 · Anh đổi hướng hình: rồng của skill là rồng năng lượng
- Câu anh: "nếu là kỹ năng thì nên vẽ rồng không chân thân dài hoặc chân cũng chỉ bé nhỏ… thiết kế rồng dạng hơi trong, chi tiết hơi mờ, chủ yếu là hiệu ứng, hình ảnh mượt chứ đâu cần phải lôi cả con rồng ra".
- **Bỏ:** đầu rồng 3D làm bằng Tripo (≥ 20.000 tam giác, ảnh nguồn 4 góc), xem DRAGON_SKILL §3, bảng nguồn. Chỉ làm lại nếu sau này có cận cảnh lớn.
- **Cách dựng mới:**
  - đầu: flipbook từ ảnh tĩnh anh chọn (ảnh → video: gầm, bờm lửa lay);
  - thân: dải khí lửa chạy dọc đường S (dải lửa Firefly theo kiểu câu lệnh anh chọn, cuộn dọc spline, cộng sáng, đuôi tan);
  - phủ thêm bụi sáng, sao lấp lánh và tàn lửa;
  - code chỉ đặt, căn nhịp và cho chạy.
- **Ảnh tĩnh v1** (GPT Image 2.5 Flare trong Firefly, ảnh tham chiếu đầu A chỉ dùng cho mặt và màu), nằm trong `art-src/lab/firefly-sprint-2026-11-05/stills/spirit-dragon/`:
  - `side`: "…Side view: a spirit dragon summoned by a sword skill flies from left to right across the frame, head in profile at the right with its jaw open in a roar. It is a translucent energy dragon of fire and golden light, glowing from inside, edges see-through. Behind the head the long body is a smooth ribbon of fire-qi rippling in a gentle wave, fading to transparent and breaking into sparks, embers and golden motes toward the left edge. No legs, only two small wisps of flame where the front claws would be. Speed lines of light, soft motion blur, additive glow, little hard detail. Premium donghua skill VFX, pure black background, the whole dragon inside the frame."
  - `burst`: "…An ethereal dragon spirit made almost entirely of light bursts forward toward the viewer at a three-quarter angle: a white-gold glowing head with crimson and orange rim light, horns and mane drawn as soft strokes of flame, open roaring jaw, bright eyes. The body is not solid: it is a spiralling stream of golden light and thin fire ribbons that curls back into the distance and dissolves into glitter, star glints and embers. Very translucent, layered glow like a hologram of fire, smooth gradients, soft focus, almost no hard detail, a radiant halo of light behind the head. Premium donghua ultimate-skill VFX, pure black background, the whole effect inside the frame."
  - `scurve`: "…Paint a spirit dragon summoned by a martial sword technique: a translucent, glowing energy dragon made of fire and golden light. The head is the clearest part: horns, flowing mane, open roaring jaw, glowing eyes, built of luminous flame-light with a soft inner glow, its edges see-through. The long serpentine body is a flowing ribbon of fire-qi and light that streams back in a wide S-curve, growing more transparent along its length and dissolving into sparks, embers and golden motes. Only small wispy flame claws near the chest. Soft, smooth, motion-blurred, dreamy glow, additive light, little hard detail, the feeling of a legendary dragon palm strike. Premium donghua skill VFX, pure black background, the whole dragon inside the frame."
  - Câu nào cũng mở đầu bằng: "Use the dragon head in the reference image only as the guide for the face, horns, mane and colours."
- **Đã gửi anh:** `owner-review/2026-11-05/tu-tien/spirit-dragon/spirit-dragon-v1-sheet.jpg`.
- **Bỏ** ba ảnh rồng toàn thân có chân (v1, v2), không làm video từ chúng nữa.

## 05/11 ~02:05 · Anh: skill diện rộng là nhiều con, bay nhiều hướng, loạn cả map
- Câu anh: "chúng ta nên thiết kế dạng kỹ năng diện rộng không nên theo hướng, mà nó có nhiều con và bay nhiều hướng, 1 hồi loạn cả máp để nhìn có hiệu ứng đẹp, fantasy, cinimal hơn".
- Hệ quả cho Song Long: bỏ "hai con theo hai hành lang". Thay bằng một bầy rồng năng lượng (ví dụ 6–12 con), xuất phát từ người ra chiêu hoặc từ cổng trời, bay xoáy nhiều hướng khắp sân rồi hội về ngọc. Mỗi con là đầu (flipbook tại chỗ) cộng thân dải lửa chạy theo đường cong riêng; rồng năng lượng nên nhân nhiều con rẻ.
- Sát thương: giữ phủ toàn sân, không gắn vào đường bay từng con. Sim tính khối trúng theo sân và mật độ thú (luật skill không phụ thuộc map); hình thì chạy riêng ở phần view.
- Phải lên kế hoạch lại 271 (sim hai hành lang) và đo lại cân bằng. Thiết kế lớn: hỏi Gemini một lượt rẻ trước khi viết phiếu.
- Video thử rồng năng lượng: bản "lướt tới" làm rồng mọc 4 chân và chạy như thú; đang làm lại bản giữ dáng tại chỗ (khung đầu = khung cuối, chỉ lửa chảy).
- 02:05 Video rồng năng lượng: bản "lướt tới" (chỉ khung đầu) mọc 4 chân, chạy như thú, bỏ. Bản giữ dáng (khung đầu = khung cuối = ảnh bay ngang, câu lệnh "chỉ lửa chuyển động") đạt: trong mờ, lửa chảy, không chân. File: `art-src/lab/firefly-sprint-2026-11-05/video/spirit-dragon-side/take2-inplace.mp4`. Đã gửi anh video so và bản lặp 3 lần. Bài học: clip cho sprite trong game phải giữ dáng tại chỗ; game lo chuyển động.
- 02:30 Lab thử bầy rồng: worktree `games/.wt-ic-dragon-swarm` (nhánh `claude/dragon-swarm-lab`), link http://127.0.0.1:3058/skills-lab.html?key2=swarm (phím 2 tung, D đổi A/B). 9 con, dải uốn sóng theo đường riêng, hội về ngọc. Chưa có nổ ngọc, âm, sát thương.
- 05/11 10:50 Claude: bản thử rồng 3D năng lượng (`?key2=swarm3d`, commit `421ea5d` ở `games/.wt-ic-dragon-swarm`): model thuồng luồng, các đốt bám theo đường bay, sóng chữ S ngang mặt đất, dải lửa chảy trong thân, viền sáng, đầu nóng, tàn lửa. Link http://127.0.0.1:3058/skills-lab.html?key2=swarm3d
- 05/11 10:52 · Claude · Anh chê bản 3D lươn "như con nòng nọc". Dừng thử (luật 3 lần). Workflow wjgjtg7x7: tìm model rồng Trung Hoa có sẵn (giấy phép kiểm trên trang) + hỏi Gemini cách dựng rồng năng lượng đọc được từ trên xuống. Kết quả: `consult/twin-dragons-3d-gemini.md`.
- 05/11 11:05 · Claude · **Kết quả tìm hiểu** (workflow wjgjtg7x7):
  - **Model:** tốt nhất là "Black Ink Dragon – Stylized Model" (Meleagors, Sketchfab, CC BY đã kiểm trên trang, 21,6k tam giác, chưa rig, dáng số 8): thân dài đều, sừng, bờm. Mua được: Superhive "Animated Chinese New Year Dragon" ($36,99, rig IK, khoảng 21k tam giác). Repo không có model nào dùng được làm thân. Rig rắn CC0 Mesh2Motion (28 khớp) đã có ở `games/typing-defense/art-src/anim/mesh2motion/rig-snake.glb`.
  - **Gemini** (`consult/twin-dragons-3d-gemini.md`): đầu Tripo cộng thân ống dựng bằng Blender, `InstancedMesh` với spline trong vertex shader. Luật chống "nòng nọc":
    - bán kính đều 75 % thân;
    - đầu và bờm rộng 2,5 lần thân, sừng chữ V;
    - vây lưng là 2 dải nghiêng ±35°;
    - tỉ lệ dài/rộng 18:1;
    - blend có viền tối; nền tối đi 35 % khi chiêu chạy.
  - Chờ anh chọn: A (CC BY miễn phí, anh tải giúp vì Sketchfab cần đăng nhập), B (anh mua $36,99), C (tự dựng theo Gemini, đầu Tripo từ ảnh anh duyệt).
- 05/11 11:10 · Claude · Kiểm lại trang Black Ink Dragon (Meleagors): licence "CC Attribution" (by), "Author must be credited. Commercial use is allowed.", 21.636 mặt, không rig, không thẻ noai hay createdwithai; tải miễn phí nhưng cần đăng nhập. Gửi anh link để anh tự tải (định dạng glTF/GLB) và gửi lại.
- 05/11 11:15 · Claude · Anh yêu cầu 5 ảnh 2D rồng năng lượng có đầu, thân, đuôi và 2 chân nhỏ phía trước. Đã vẽ bằng GPT Image trong Firefly (tham chiếu spirit-dragon.unified.v1-try3): `stills/spirit-dragon/energy-dragon.legs2.v1-try1..5.png`; tấm `owner-review/.../spirit-dragon/energy-dragon-2legs-5.jpg`. Cũng có 3 ảnh nguồn dạng khối cho Tripo (`sculpt-source.v1-try1..3.png`), chưa gửi, chờ anh duyệt kiểu năng lượng trước.
- 05/11 11:37 · Claude · Theo ý anh (thân gần thẳng, xương lo độ uốn), đã vẽ 4 ảnh bằng GPT Image trong Firefly, tham chiếu `energy-dragon.legs2.v1-try2.png`, lưu ở `stills/spirit-dragon/`:
  - `energy-straight.side` và `energy-straight.34`: kiểu năng lượng;
  - `sculpt-straight.side` và `sculpt-straight.34`: dạng khối cho Tripo.
  - Tấm: `owner-review/.../spirit-dragon/dragon-straight-4.jpg`.
  - Đề xuất Tripo từ `sculpt-straight.34`. Chờ anh duyệt trước khi tốn khoảng 40 credit Tripo.
- 05/11 11:45 · Claude · Anh chê kiểu năng lượng "đậm quá, phải xuyên thấu", rồi thêm "phải hiển thị tốt ở nhiều góc nhìn, thân hình phải đều và đẹp". Đã vẽ 3 ảnh xuyên thấu (`stills/spirit-dragon/see-through.v1-try1..3.png`):
  - thân gần như trong suốt, viền sáng mảnh, vài dòng lửa mảnh bên trong;
  - nền đá hoặc trời nhìn xuyên qua thân;
  - câu lệnh: phần ID cũ cộng "see-through spirit dragon of light: mostly transparent, thin glowing rim lines…, a few faint thin flame currents inside…, ground clearly visible through".
  - Kế hoạch 3D để đẹp ở mọi góc:
    - model Tripo thân tròn đều từ ảnh khối `sculpt-straight.34`;
    - shader: viền fresnel (luôn ra đường viền ở mọi góc), lõi gần trong suốt, dòng lửa mảnh cuộn dọc thân;
    - kiểm ở camera chơi, nhìn ngang và xoay quanh.
- 05/11 11:35 · Claude · Tripo xong (task 9a293267, 40 credit, ví API 930 → 890): model rồng thẳng, có sừng, bờm, 2 chân trước, vây đuôi (`art-src/3d/skills/energy-dragon/energy-dragon-body.tripo.glb`). Blender gắn 40 xương dọc sống (`rig_spine.py`) → `art-src/lab/models/energy-dragon/energy-dragon.rig.glb`. Lab: `?key2=energy` (`dragon-swarm-energy.ts`).
- 05/11 11:42 · Claude · Rồng 3D xuyên thấu (`?key2=energy`, commit trong `games/.wt-ic-dragon-swarm`), 4 vòng chỉnh shader:
  - v1: cộng sáng chồng thành khối trắng;
  - v2: thêm lớp ghi độ sâu trước (depth prepass) thì sạch, nhưng quá mờ;
  - v3: sáng lên thì vỡ thành mảnh lấp lánh, do các sợi lửa của model Tripo;
  - v4: thân làm mịn bằng voxel remesh, thêm dải lửa dọc sống lưng, nhưng vẫn mờ ở camera chơi và dải lộ mảng phẳng.
  - Video `owner-review/.../spirit-dragon/energy-dragon-3d-v2.mp4`, tự chấm chưa đạt.
  - **Dừng theo luật 3 lần.** Đề xuất cho anh:
    - làm đẹp **một** con rồng lớn, bay chậm, trong lab cận trước;
    - thân nửa trong (lõi sáng đặc khoảng 60 %, viền và đuôi trong), rồng to hơn so với sân;
    - ít con hơn (4–6), có hồn rồi mới nhân lên.
- 05/11 12:06 · Claude · Anh chê "quá mờ, khó nhìn đâu là đầu đâu là đuôi", rồi "chỉnh lại cho đẹp hơn". Bản v4 (commit `29df570`):
  - thân nửa trong, màu chuyển từ đầu vàng sáng xuống đuôi đỏ;
  - đốm sáng dẫn ở đầu (`flare_01`, CC0);
  - lớp nền tối mờ dưới thân để màu lửa đậm;
  - lửa trong thân mềm, không sọc;
  - model làm mịn lại (voxel 0,0025, làm trơn 20 lượt);
  - bỏ phần làm thân dày thêm (đè giật thành sọc);
  - 16 m, bay 5 s, 6 con.
  - Video `owner-review/.../spirit-dragon/energy-dragon-3d-v4.mp4`. Claude thấy: camera chơi đọc rõ; nhìn ngang và xoay quanh ra dáng rồng 3D lửa. Chưa chấm mù, chưa có nổ ngọc và âm thanh.
- 05/11 12:38 · Claude · v5: sửa lỗi bay lùi (xương gắn ngược; đầu đặt bằng mắt, shell3), sóng uốn tăng dần về đuôi, nghiêng khi rẽ, bay lên xuống, bớt đậm. Video `energy-dragon-3d-v5.mp4` (camera theo 1 con + cả bầy ở camera chơi). Còn nhạt ở camera chơi.
- 05/11 12:45 · Claude · Anh chê v5 "cực kỳ xấu" rồi chốt "chi tiết vẫn rất quan trọng… hơi trong suốt nhưng vẫn rõ chi tiết". v6 (commit `94ffa78`):
  - dùng model Tripo gốc (`energy-dragon.full.rig.glb`, 40 xương, đầu đặt `pos`) với texture lửa của chính nó, cho phát sáng (`uGlow` 1,35), viền vàng, mép hơi trong (alpha 0,62–1);
  - xương xoay theo góc nhỏ nhất từ tư thế nghỉ, nên đầu không còn bị vặn;
  - chiều đặt đầu (`pos` hay `neg`) phải kiểm bằng mắt cho từng model, vì dấu trục PCA đổi giữa các model.
  - Video `owner-review/.../spirit-dragon/energy-dragon-3d-v6.mp4`.
- 05/11 12:56 · Claude · Ảnh nguồn mới có đủ giải phẫu rồng (vảy, tấm bụng, vây lưng, bờm, sừng, râu, 2 chân trước, vây đuôi), thân gần thẳng: `stills/spirit-dragon/detailed-source.v1-try1..3.png` (GPT Image trong Firefly, tham chiếu dragon-body.v2-try1 anh chọn). Gửi anh duyệt trước khi chạy Tripo.

## 05/11 13:40 · Rồng khí theo ảnh mẫu của anh
- Anh chê ảnh nguồn đỏ đặc ("sao nhìn vẫn xấu… phải là rồng dạng năng lượng như kiểu hình bóng"), gửi mẫu rồng khí xanh trong suốt (Cái Bang Rồng): "dựa vào đó mà tạo prompt, thay màu lại cho phù hợp".
- ChatGPT (Chat, High) vẽ 3 bản trong một chat, mẫu chỉ tả bằng lời (không đưa ảnh game khác vào AI), đổi sang vàng lửa: `stills/spirit-dragon/qi-dragon.v1-try1..3.png` (+ `.prompt.txt`). Tấm gửi anh: `owner-review/2026-11-05/tu-tien/spirit-dragon/qi-dragon-3.jpg`. Claude đề xuất ảnh 3 (vàng trắng, nhìn từ trên, gần mẫu nhất).
- ChatGPT tra 12 mẫu (JX3 Cái Bang, Nghịch Thủy Hàn, Dragonstrike của Hanzo…) và cách dựng: thân tối trong (alpha), mặt nạ nét vảy phát sáng + viền fresnel, cộng sáng chỉ ở nét mảnh, depthWrite tắt cho lớp trong. Chat: "Research Translucent Qi Dragons".
- Sau khi anh chọn: Tripo dựng từ ảnh (texture mang nét sáng) → shader: độ sáng texture làm nét phát sáng và độ đục, lòng thân xuyên thấu, viền fresnel → khung xương, bay uốn mượt. Nếu hình khối Tripo bị nhòe vì quầng sáng, xin ChatGPT bản đặc cùng con rồng chỉ để lấy hình khối.

## 05/11 14:20 · Rồng khí 3D v1
- Tripo từ ảnh 3 (task `10ae70bb`, 40 credit, ví 850): `art-src/3d/skills/qi-dragon/`. Cắt các dải râu/khí mảnh dài (`strands_mark.py`, theo độ dày + độ dài), khung 40 xương (`rig_spine.py`, đầu `neg`) → `art-src/lab/models/qi-dragon/qi-dragon.rig.glb`.
- Lab `?key2=energy` (mặc định `dragonLook=qi`): nét sáng = texture sáng hơn mip mờ của chính nó, thân trong (premultiplied), viền vàng trắng; bơi xoắn khóa theo quỹ đạo; rồng chảy ra từ người ra chiêu, lặn vào ngọc. Commit lab `0a151f2`.
- Video `owner-review/2026-11-05/tu-tien/spirit-dragon/qi-dragon-3d-v1.mp4` (16 s). Giám khảo mù 6,0 / 6,3 (`captures/tu-tien/qi-dragon/judge-r1`). Sửa tiếp: đầu nổi (mắt, sừng, sáng nhất), vân vảy có hàng lối, dải màu đầu→đuôi, vây không đục, tách làn bay, thân thon, lớp lấp lánh.

## 05/11 14:45 · Rồng khí 3D v2
- Anh chỉ lỗi (14:30): "khi rồng quay lại, nó bị vặn xoắn người khiến vỡ hình". Đo được: gập 130° và vặn 177° giữa hai đốt ở khúc quay chữ U. Sửa: quỹ đạo bay được "lái" (bước 0,25 m, rẽ tối đa theo bán kính 4,5 m), xương đặt theo khung sống lưng truyền từ đầu xuống đuôi, kẹp gập 0,3 rad giữ độ dài, xoắn nhỏ lại ở khúc gắt. Đo sau: gập ≤ 17°, vặn ≤ 57° (rất hiếm), vệt đuôi ≤ 1,7 m/khung (trước 7,7). Lab `cc44bdd`.
- Sửa theo giám khảo v1: tấm vảy lưỡi liềm vẽ bằng GPT Image trong Firefly từ ảnh 3 (`qi-scales.png`), dải màu đầu vàng trắng → đuôi cam, đầu sáng nhất, vây không đục, mỏng dần khi sát camera, vệt râu và vệt đuôi, mỗi con một làn độ cao, thân thon 0,8.
- Video `owner-review/2026-11-05/tu-tien/spirit-dragon/qi-dragon-3d-v2.mp4` (16 s).

## 05/11 15:00 · Rồng khí 3D v3 (giật, ngọc)
- Giám khảo v2: 4,8 / 6,3. "Bóp dẹt" họ thấy là đầu rồng lặn vào ngọc vô hình; đầu trắng xù; thân như lưới; mất vây đuôi; rối giữa sân.
- Anh (14:50): "hơi giật giật". Đo trên xương thật: gia tốc thân p99 2,48 → 0,07, xoay đột ngột 129° → 31° (p99 4,8°). Gốc: biên độ xoắn tụt bậc theo độ cong của quỹ đạo lái; đầu lật khi chúc thẳng đứng; vòng quanh ngọc không trúng (đường bay tới 130 m). Video v2 còn giật do đoạn chậm 36→60 hình/giây nhân đôi khung.
- Sửa: bỏ giảm xoắn theo độ cong (xoắn 1,8 m < bán kính quay 4,5 m), bảng độ dài 5 cm, "lưng" đầu mang qua từng khung, nghiêng theo khung sống lưng, điểm đón 7 m + lao vào ngọc thu hẹp theo khoảng cách. Ngọc phát sáng (cầu fresnel + quầng + vòng Kenney CC0), lóe khi mỗi con vào, nổ cuối. 5 con lượn xoáy cùng chiều theo góc riêng. Đầu vàng, bờm dịu, đường sống lưng, dải bụng, lòng vảy, giữ vây đuôi, bỏ vệt đuôi, đầu to 1,25. Lab `624b181`.
- Video `qi-dragon-3d-v3.mp4` (16 s), quay chậm thật bước 1/100 s.

## 05/11 15:25 · v4, đầu sạch, tốc độ
- v4 (`3294bed`): vảy lưỡi liềm không còn vân kính nứt, tầng màu, ngọc xà cừ có xoáy, đốm đất (sau bỏ vì giám khảo coi là vết bẩn). Giám khảo vòng 4: 6,8 / 6,1. Lỗi 4 vòng liền: đầu búi xù → hỏi ChatGPT (`consult/qi-dragon-head-chatgpt.md`), Claude chốt vẽ lại cả con với đầu sạch (không ghép đầu).
- Ảnh đầu sạch (ChatGPT, cùng chat ảnh 3): `stills/spirit-dragon/qi-dragon.v2-try1.png` (đầu nghiêng, Claude đề xuất cho Tripo), `v2-try2.png` (đầu nhìn từ trên). Tấm gửi anh: `qi-dragon-clean-head-2.jpg`. Chờ anh chọn rồi Tripo + `strands_mark.py` + `rig_spine.py` (slim 0,8, head 1,25).
- Anh hỏi tăng tốc (15:15). Đo 4 lượt × 5 con ở 1,0× / 1,3× / 1,6×: chiêu 8,9 / 7,4 / 6,5 s; mỗi khung 0,21 / 0,27 / 0,34 m; xoay đốt p50 2,8 / 3,7 / 4,6°; giật xoay p99 4,7 / 5,6 / 7,1°; gập tối đa 20° như nhau. Video `qi-dragon-speed-compare.mp4`. Claude đề xuất 1,3×.
- Codex 288 (`a143db2`): 106 test chuyển động; 2 lỗi mở (bán kính 3–3,8 m do nội suy, lật khi xuất phát thẳng đứng) → Codex 289 đang sửa (đừng sửa `dragon-swarm-energy.ts` tới khi 289 xong).
- 15:30 Codex 289 (`claude/dragon-swarm-lab`, commit sau `a143db2`): B-spline bậc hai cho quỹ đạo (bán kính nhỏ nhất 4,45 m), lưng ngang khi xuất phát thẳng đứng; 106 test thường, 1085/1085. Lab đo lại: giật xoay p99 2,15° (trước 4,7°), gia tốc p99 0,039, max 0,19.
- 15:35 Anh: giữ rồng hiện tại, không vẽ lại đầu. Kế: đặt tốc độ 1,3× (sau Codex 290), rồi nối bầy rồng khí vào chiêu phím 2 thật (thay hình của 271, khớp nhịp sát thương toàn sân).
- 15:45 Codex 290 (làm ấm bầy rồng lúc nạp): khung phím 2 đầu tiên 3,6 ms CPU trong lab (khung thường 0,5). Tốc độ mặc định 1,3×. Test xoay mỗi khung nhân theo tốc độ. Lab `HEAD` sau `fc3b3f7`.
- 15:50 Đọc mã nối vào game: `consult/key2-qi-swarm-wiring-study.md`. Thiết kế lớn (sim toàn sân theo vùng, bảng nhịp, sự kiện, presenter, tầng chất lượng, asset) → vòng ChatGPT + Gemini theo luật.
- 15:55 Anh đề xuất: "rồng lướt qua quái nào thì gây sát thương quái đó, và khi rồng tới ngọc, sẽ gây ra 1 vụ nổ mạnh cả map". Claude đồng ý và đề xuất kèm: (1) sim tự vạch đường 5 con (mỗi con một vùng, xuyên các đám quái đông nhất; từ biên sân + vị trí quái, không theo hành lang map), view vẽ đúng đường đó; (2) sóng xung kích lúc thả trúng ngay quái gần người (≤ F1); (3) nổ ngọc cả sân, gần ngọc mạnh hơn (mép ~60 %), chung quỹ sát thương, trần phím 2 ≤ 45 %, trần boss. Chiêu ~4–5 s ở 1,3×. Chờ anh đồng ý rồi mới qua vòng ChatGPT + Gemini.
- 16:25 Codex 292: script tầng chơi (`scripts/models/qi-dragon-tiers.mjs`): High 1,29 MB (texture GPU 27 MB), Medium 0,82 MB (11 MB), đủ 25.990 tam giác, 40 xương; Medium trong lab nhìn như bản gốc (`captures/.../qi-dragon/tier-ab.jpg`). Media chưa push (`pnpm media:push` khi đưa vào game).
- 16:20 Thiết kế sát thương: dùng bản ChatGPT (2 PASS), bỏ lượt Gemini theo lời anh (một trợ lý). Nguyên văn: `docs/games/tu-tien/source/key2-qi-swarm-chatgpt-2026-11-05.md`.
- 05/11 16:55 · Claude · Phiếu 293: phản biện vòng 1 FAIL (7 lỗi, đã sửa), vòng 2 (workflow critic + adversary) FAIL: vòng lượn chờ 6 m quanh ngọc ra ngoài sân thật 40 × 26 m (ngọc chỉ lùi 2 m khỏi biên; đường C→P thường 15–25 m < 13T ≈ 39 m nên vòng chờ là ca thường); đầu rồng ở tick lao mâu thuẫn (điểm 2 m trước ngọc hay ngọc); bộ ba kiểm bán kính lấn vào vùng lặn. Kết quả đầy đủ: `subagents/workflows/wf_7ea3e0eb-17c/journal.jsonl` của phiên. **Nghĩ lại mai (vòng 3 là vòng cuối):** bỏ vòng chờ; tick lao của từng rồng = thả + ⌈L / v⌉ với v cố định khoảng 16 m/s (kẹp 13–20), nổ ngọc = max(tick lao) + 32, hết = nổ + 40; kiểm trong sân trên đường nền với lề 1,8 m. Anh đã dặn code để mai, nên đỗ tới mai.
