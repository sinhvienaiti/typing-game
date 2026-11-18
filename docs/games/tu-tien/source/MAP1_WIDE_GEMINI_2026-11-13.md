# Gemini duyệt MAP1_WIDE v0.1 (13/11/2026)

- Công cụ: Gemini, chế độ **Argon, Cao**, trình duyệt trong app, tài khoản đã đăng nhập sẵn. Một lượt hỏi, Gemini tự duyệt trong cùng câu trả lời.
- Hội thoại: https://gemini.google.com/app/2edbd705c184fc3a ("Đánh giá và sửa lỗi thiết kế map Three.js").
- Không gửi ảnh nào (chỉ chữ). Câu hỏi là bản tóm tắt đủ số của MAP1_WIDE v0.1 (§1–§9), nguyên văn dưới đây.
- Ghi chú chép: câu trả lời chép từ trang; công thức KaTeX trên trang hiển thị hai lần (bản dựng + nguồn), ở đây giữ một lần, viết thẳng hàng. Chữ khác giữ nguyên.

## Bảng kiểm

| Lượt | Kết quả | Lý do (tóm) |
|---|---|---|
| Tự duyệt 1 | FAIL | Váy đất 150 m + lề chiêu 2 m tràn biên; vòng chỉ báo đè dải pan dưới |
| Tự duyệt 1 (đếm lại) | PASS | Kiểm frustum, cổng, Thiên Đàn, chunk, thời gian đi |
| Tự duyệt 2 | PASS | Kiểm UX mắt/chuột, texture unit WebGL2, ngân sách |
| **Kết luận** | **7,4/10, đồng ý B có điều kiện** | |

## Claude → Gemini (nguyên văn)

Bạn là reviewer thiết kế game. Hãy duyệt ghi chú thiết kế map (tóm tắt đủ số) cho game 3D three.js thủ thành gõ phím, chủ đề tu tiên. Chủ dự án yêu cầu (D66): map rộng hơn khung hình nhiều lần; góc 55°, FOV 28° và độ cao camera giữ nguyên; rê chuột gần mép màn hình thì camera trượt tới biên sân, buông thì đứng yên; gõ phím không bị ảnh hưởng; chiêu toả "hết màn" tính theo mép khung đang nhìn; quái ngoài khung cần chỉ báo hướng.

Yêu cầu:
1. Chấm /10 và nêu rủi ro lớn nhất (chơi khi mắt phải ở dải chữ gõ, edge-pan, chỉ báo quái ngoài khung, nhịp trận, hiệu năng WebGL).
2. Đề xuất sửa cụ thể bằng số.
3. Rồi TỰ DUYỆT câu trả lời của chính bạn (sai sót, mâu thuẫn, số vô lý). Ghi "Tự duyệt lần N: PASS/FAIL" kèm lý do; FAIL thì sửa và đếm lại từ đầu. Dừng khi có HAI PASS liên tiếp.
4. Dòng cuối: "KẾT LUẬN: <đồng ý phương án nào> — <3 sửa quan trọng nhất>".

--- GHI CHÚ MAP1_WIDE v0.1 ---

§1 Camera thật (giải ngược từ 10 điểm engine, sai số 0,3 px): nghiêng 55°, FOV dọc 28°, cự ly 52,8 m, nhìn (0;0;−2,06). Một khung trên đất là hình thang: mép trên rộng ±28,4 m, giữa ±23,4, mép dưới ±19,9; sâu 33 m. Một khung ≈ 47 × 33 m. px/m ở 1080p: 31 (xa) … 46 (gần); 720p nhân 2/3. Không thấy trời. Thanh gõ chữ (Bàn Quyết, DOM) che dưới y≈930/1080. Khi sân rộng, không fit camera theo sân (sẽ làm mọi thứ bé lại), giữ cự ly cố định; pan chỉ dịch điểm nhìn.

§2 Ba phương án (sân gốc 40×26 m = một khung):
A 94×50 m (2×1,5 khung): ít đổi nhịp, nhưng chưa "nhiều lần".
B 140×66 m (3×2 khung) — ĐỀ XUẤT: mỗi phía một khung riêng có cổng và mốc; đường thú ~71 m (gấp ~3 lần ~23 m hiện nay), cần đổi nhịp sim; đất gấp 9 lần, dùng ô lặp + decal.
C 188×83 m (4×2,5): quá dài cho trận gõ 3–6 phút, mắt rời dải chữ quá lâu, chi phí ×15.

§3 Bố cục B (bắc = −z): Trận Tâm (0;0), Trận Trụ (∓6,4;−7,7), 6 ô cơ quan quanh tâm: không đổi, đều trong khung nhà. Cổng cũ (∓15;−18) thành "Ải trong" cao 5 m. Cổng ngoài (∓58;−46) cao 7 m, nơi thú xuất hiện, ngoài khung nhà. Hành lang 6 m uốn khúc: cổng ngoài → (∓48;−28) → (∓22;−22) → ải trong → Kết Giới r 9 m. Thiên Đàn (0;−40) cao ≤ 9 m: mốc chính mới, trùm xuất hiện. Vọng lâu đổ nát (−44;−12), Thác Đông x 44…56. Tường bắc z −53. Lối trời hai góc bắc. Mỗi khung pan một mốc.

§4 Edge-pan: dải mép 24 px CSS trái/phải/trên; cạnh dưới KHÔNG pan (thanh gõ ở đó). Tốc độ tăng tuyến tính theo độ sâu trong dải, tối đa 30 m/s (~0,65 khung/s; hết bề ngang clamp 93 m trong ~3,1 s); chéo chuẩn hoá. Tăng tốc 0,15 s, dừng 0,12 s; chuột phải ở trong dải 0,15 s mới bắt đầu. Kẹp điểm nhìn x ∈ [−46,6; 46,6], z ∈ [−34,5; −1,7]. Buông đứng yên. Về nhà: nút HUD, 0,35 s. Tắt khi chuột ra khỏi cửa sổ, mất focus, menu, cut-in, zoom cận. Không gắn phím nào (chữ, số, Space, Enter, mũi tên đều là phím game). Kéo chuột giữa để pan luôn có. Settings: Bật / Chậm 15 m/s / Tắt; prefers-reduced-motion mặc định Chậm.

§5 Quái: thú bộ từ cổng ngoài, đi ~71 m; thú bay từ góc bắc; trùm trên Thiên Đàn. Chỉ báo ngoài khung: mũi tên trên mép khung theo hướng tới cụm (gộp cụm 8 m), màu xám trắng / cam tinh anh / đỏ trùm hoặc sắp đánh, có số đếm, đập nhịp khi cụm tới ải trong; nhấp để pan tới. Minimap là tuỳ chọn pha sau.

§6 Anh hùng đứng (0;+3) như cũ; khung nhà giống trận hiện nay. Chiêu vẫn bắn từ anh hùng; nếu ngoài khung thì có vệt báo ở mép.

§7 "Hết màn" = hình thang mặt đất của khung đang nhìn + 2 m lề, không phải cả sân. Pan ra cổng ngoài rồi tung chiêu toàn màn là lựa chọn chiến thuật; chi phí như cũ.

§8 Hiệu năng: chỉ thấy ~1 300 m² mỗi lúc. Frustum cull ô 10×10 m; đất chunk 20×20 m, 6 vật liệu PBR lặp + mask vẽ tay 560×264 + decal. Quái ngoài khung: sim đủ, view LOD thấp nhất hoặc ẩn, không cập nhật xương, không VFX. Mốc lớn tải đầu trận. Shadow camera theo khung. Đo p95 High (trần 12 ms) khi pan liên tục với triều thú đầy.

§9 Ngoài view: sân sim phải rộng và đường mới; nhịp trận chỉnh để thời gian tới Kết Giới không gấp 3; luật cũ "camera luôn thấy toàn sân" chuyển thành "khung nhà thấy toàn phòng tuyến, quái ngoài khung luôn có chỉ báo".

## Gemini (Argon, Cao)

Điểm đánh giá: 7,4 / 10 — ĐỒNG Ý PHƯƠNG ÁN B (140×66 m, 3×2 khung) CÓ ĐIỀU KIỆN.

Bản ghi chú MAP1_WIDE v0.1 giải ngược thông số hình học camera rất chuẩn xác (trùng khớp phép chiếu phối cảnh ở góc nghiêng 55°, FOV_y = 28°, cự ly 52,8 m, khung hình thang đáy lớn ±28,4 m, giữa ±23,4 m, đáy nhỏ ±19,9 m, sâu 33,16 m) và chọn đúng Phương án B làm điểm cân bằng giữa độ mở chiến thuật với thời lượng trận 3–6 phút. Tuy nhiên, khi ghép hệ toạ độ pan với tư thế mắt nhìn thanh gõ chữ (Bàn Quyết) và giới hạn phần cứng WebGL2, tài liệu đang có 5 rủi ro thiết kế và kỹ thuật nghiêm trọng:

### 1. Năm rủi ro lớn nhất theo 5 trục trọng tâm

| Trục đánh giá | Mức độ | Phân tích rủi ro chi tiết từ số liệu MAP1_WIDE v0.1 |
|---|---|---|
| 1. Thị giác khi mắt khóa ở Bàn Quyết (y≈930/1080) | Nghiêm trọng | Tại độ phân giải 1080p, dải chữ gõ nằm ở y∈[930;1080] px, tức vùng nhìn trung tâm (foveal vision, bán kính rõ ≈150 px) của người chơi luôn neo ở đáy màn hình. Khi pan lên bắc (z_look=−34,5 m) hoặc rà chuột lên mép trên (y≤24 px), mắt phải dịch chuyển hơn 900 px (≈22° góc nhìn), làm đứt mạch đọc từ gõ ≈450–600 ms mỗi lượt chuyển mắt. Ngoài ra, ở §6, chiêu bắn từ anh hùng tại (0;+3) tới Cổng ngoài (∓58;−46) phải bay quãng đường √(58²+49²)=75,9 m; nếu giữ tốc độ đạn cũ (≈25 m/s), đạn mất 3,04 s mới tới đích, phá vỡ phản hồi gõ chữ tức thời. |
| 2. Bẫy Edge-Pan một chiều & xung đột thao tác bàn phím (§4) | Chí mạng | §4 quy định "cạnh dưới KHÔNG pan (thanh gõ ở đó)". Hệ quả: người chơi rê chuột lên mép trên (y≤24 px) để trượt camera lên biên bắc (z_look=−34,5 m), nhưng không thể dùng edge-pan để trượt ngược xuống nam! Muốn lùi camera xuống một phần hoặc về nhà, người chơi buộc phải rời tay phải khỏi bàn phím để bấm nút HUD "Về nhà" hoặc kéo chuột giữa (tốn 0,6–1,1 s chuyển tay bàn phím ↔ chuột, làm gãy chuỗi gõ). |
| 3. Chỉ báo quái ngoài khung & cắt cụt thanh chữ trên Thiên Đàn (§3, §5) | Cao | (a) Khi ở khung nhà (z_look=−2,06 m), toàn bộ cổng ngoài và hành lang bắc nằm phía trên màn hình, nên mũi tên chỉ báo dồn hết lên mép trên (y≈24 px) — cách mắt người chơi 900 px, khiến chữ số đếm trên mũi tên không thể đọc bằng thị giác ngoại vi. Ngược lại, khi pan lên bắc, chỉ báo quái ở Ải trong dồn xuống đáy màn hình sẽ bị DOM Bàn Quyết (y≥930 px) che khuất nếu không trừ lề đáy. (b) Ở góc tia nhìn mép trên 55°−14°=41°, vật cao h tại toạ độ z bị chiếu lùi về z_proj=z−h/tan41°=z−1,1504h. Nếu Trùm (cao 3,5 m + thanh chữ trên đầu 1,5 m) đứng trên mặt Thiên Đàn cao 9 m tại z=−40 m (h_tổng=14 m), đỉnh thanh chữ rơi vào z_proj=−40−1,1504×14=−56,11 m, vượt quá biên nhìn bắc tối đa (z_top=−34,5−19,47=−53,97 m) và bị cắt mất khỏi mép trên màn hình 2,14 m. |
| 4. Sai số tỷ lệ quãng đường ×4,83 làm vỡ nhịp trận (§2, §3, §9) | Cao | Tổng độ dài các đoạn gấp khúc từ Cổng ngoài (∓58;−46)→(∓48;−28)→(∓22;−22)→ Ải trong (∓15;−18) là 20,59+26,68+8,06=55,33 m. Từ Ải trong (∓15;−18) tới tâm (0;0) là √(15²+18²)=23,43 m, nhưng tới mép Kết Giới (r=9 m) chỉ là 23,43−9,0=14,43 m. Do đó, quãng đường thực tế thú bộ phải đi để chạm Kết Giới tăng từ 14,43 m lên 55,33+14,43=69,76 m (≈71 m khi bo góc) — tức gấp 4,83 lần, không phải gấp 3 lần như §2 nhẩm tính (vì §2 lấy 71 m có trừ bán kính Kết Giới chia cho 23 m chưa trừ bán kính Kết Giới). Nếu chỉ tăng đều tốc độ quái lên ×3–4,8, khi quái lọt qua Ải trong vào khung nhà (14,43 m), chúng sẽ lao vào Kết Giới trong 2,5–3,5 s, không kịp gõ phím. |
| 5. Hở biên hình thang, lẻ lưới chunk và vượt trần Sampler WebGL2 (§4, §8) | Cao | (a) Tác giả tính clamp x_look=±46,6 m bằng cách lấy nửa chiều rộng sân 70 m trừ nửa rộng giữa khung (23,4 m). Nhưng tại mép trên khung, nửa rộng hình thang là ±28,4 m, nên khi pan tới x_look=±46,6 m, hai góc trên khung nhìn vươn tới x=±(46,6+28,4)=±75,0 m (rộng 150 m), lòi ra ngoài biên sân 140 m (±70 m) mất 5,0 m mỗi bên. (b) Sân 140×66 m chia chunk đất 20×20 m bị lẻ chiều Z (66/20=3,3 chunk). (c) Diện tích hình thang thực tế là (56,8+39,8)/2×33,16=1601,6 m² (phần trên Bàn Quyết là 1464 m²), cao hơn mức ước tính 1300 m² tới 23%. (d) Phối 6 vật liệu PBR truyền thống (6×3 map=18 texture) + 2 mask + shadow/env map trong 1 pass vượt trần MAX_TEXTURE_IMAGE_UNITS = 16 của chuẩn WebGL2. |

### 2. Đề xuất sửa cụ thể bằng số (Bản nháp đề xuất ban đầu)

**Sửa hình học biên sân, Clamp Camera & Chiều cao Thiên Đàn (§1, §3, §4):**

Giữ nguyên bố cục gameplay 140×66 m, nhưng nới váy địa hình (terrain skirt) lên 150×72 m (x∈[−75;+75] m, z∈[−58;+14] m) để che kín hai tai trên của hình thang camera.

Chỉnh clamp điểm nhìn: x_look∈[−46,6;+46,6] m, z_look∈[−36,5;−2,06] m (khóa biên nam đúng bằng tâm khung nhà z=−2,06 m để không lệch khung chuẩn; nới biên bắc từ −34,5 m lên −36,5 m để đỉnh khung đạt z_top=−55,97 m).

Dịch Tường bắc từ z=−53 m lên z=−56,0 m.

Tách độ cao Thiên Đàn tại (0;−40): mặt sàn nơi Trùm đứng cao ≤3,0 m (để đỉnh thanh chữ của Trùm ở cao độ 3,0+3,5+1,5=8,0 m chỉ chiếu lùi về z_proj=−40−1,1504×8=−49,2 m, cách mép trên màn hình 120 px an toàn); phần cổng vòm trang trí phía sau Thiên Đàn (z=−43 m) được cao tối đa 8,5 m.

**Sửa cơ chế Edge-Pan 2 chiều & Tự trả khung khi gõ (§4):**

Mở dải Edge-Pan cạnh dưới ngay sát trên Bàn Quyết: Đặt vùng nhận diện edge-pan dưới tại y_css∈[906;930] px (dải cao 24 px ngay phía trên DOM Bàn Quyết), và ngắt pan ngay khi y_css>930 px (khi chuột đi vào thanh gõ).

Tự động thu hồi camera khi gõ (Auto-Tether): Khi camera đang ở ngoài khung nhà (‖L−L0‖≥1,5 m), nếu người chơi gõ liên tục ≥3 ký tự (hoặc sau 2,2 s kể từ lúc ngừng di chuột) mà chuột không nằm trong dải edge-pan, camera tự động trượt mượt về khung nhà (0;0;−2,06) trong 0,35 s (hàm mượt cubic-out).

Bổ sung phím tắt Tab (hoặc giữ Tab để nhòm nhanh vị trí cụm quái nguy hiểm nhất, nhả Tab tự trả về nhà trong 0,25 s) — không xung đột với phím chữ, số, Space, Enter hay mũi tên.

**Sửa vận tốc hành quân 2 pha & Tốc độ đạn viễn chinh (§5, §6, §9):**

Vận tốc quái 2 pha (Two-Zone Pacing): Giữ tốc độ chuẩn trong khung nhà v_in=1,0×v0 (ví dụ 1,6 m/s, đi 14,43 m từ Ải trong tới Kết Giới mất 9,02 s). Trên hành lang ngoài (55,33 m từ Cổng ngoài tới Ải trong), áp hiệu ứng "Tật Hành Ngoài Ải" nhân tốc độ lên v_out=2,6×v0=4,16 m/s (đi hết 55,33 m trong 13,30 s). Tổng thời gian từ lúc sinh ra tới Kết Giới là 13,30+9,02=22,32 s (chỉ gấp 2,47 lần thay vì 4,83 lần), và ngay khi bước qua Ải trong (∓15;−18), quái giảm tốc về 1,0×v0 trong 0,4 s.

Giới hạn thời gian bay của chiêu từ Anh hùng (§6): Áp công thức vận tốc đạn thích ứng theo khoảng cách D: v_proj=max(30 m/s, D/0,22 s), đảm bảo mọi đòn đánh từ (0;+3) tới Cổng ngoài (D=75,9 m) chạm mục tiêu trong tối đa 220 ms; đồng thời khóa máu dự kiến (pre-commit damage lock) lên thanh chữ mục tiêu trong vòng ≤30 ms ngay khi gõ xong từ.

**Sửa vị trí Chỉ báo quái ngoài khung trong tầm mắt ngoại vi (§5):**

Thay vì đẩy mũi tên lên sát mép màn hình (y=24 px, cách thanh gõ 906 px), neo toàn bộ chỉ báo hướng lên một Vòng cung HUD bán elip quanh Bàn Quyết có tâm tại (960;900) px, bán kính ngang Rx=420 px, bán kính dọc Ry=220 px (tức chỉ báo luôn nằm trong dải y∈[680;895] px, cách mắt người chơi chỉ 180–250 px≈4,5°–6° góc nhìn).

Cỡ chữ số đếm cụm quái ≥20 px bold, độ tương phản nền ≥7:1; chỉ dùng màu đỏ cho trạng thái nguy cấp/Trùm sát Kết Giới, tinh anh dùng cam hổ phách (#FF9F1C), quái thường dùng trắng ngọc (#E8F1F5).

**Sửa kiến trúc Chunk, PBR Splatting & Shadow Frustum (§8):**

Đổi kích thước chunk đất và lưới frustum cull về cùng hệ ước số của 150×72 m: chia thành 10×6=60 chunk, mỗi chunk 15×12 m (hoặc lưới cull 7,5×6 m), triệt tiêu hoàn toàn chunk lẻ.

Thay 6 bộ texture PBR rời bằng sampler2DArray (1 mảng Albedo+Roughness + 1 mảng Normal RG = chỉ tốn 2 texture unit thay vì 18) kết hợp 1 texture ID/Weight 560×264 px RGBA8; giới hạn tối đa 3 lớp hoà trộn mỗi pixel.

Cắt Scissor/Viewport WebGL tại y_css≤930 px (bỏ vẽ 1920×150 px bị Bàn Quyết che), tiết kiệm 13,9% lượng pixel fragment shader.

Chống rung bóng (shadow swimming) khi pan: khóa tâm Shadow Camera dịch chuyển theo bội số nguyên của kích thước texel bóng Δsnap=64 m/2048=0,03125 m.

### 3. Quy trình Tự duyệt (Self-Audit)

**Tự duyệt lần 1: FAIL**

Lý do FAIL (phát hiện 2 mâu thuẫn số học trong chính đề xuất ở Mục 2):

Lỗi hở biên váy địa hình 150 m khi kết hợp với vùng đệm chiêu "Hết màn" (§7): Ở Mục 2.1, tôi đề xuất váy địa hình rộng 150 m (x∈[−75,0;+75,0] m) với x_look∈[−46,6;+46,6] m. Tại x_look=±46,6 m và z_look=−36,5 m, góc trên khung nhìn chạm đúng x=±(46,6+28,35)=±74,95 m (chỉ còn dư 0,05 m). Nhưng theo §7, chiêu toả "Hết màn" = hình thang mặt đất của khung đang nhìn + 2 m lề, tức vòng decal/VFX của chiêu toàn màn sẽ tràn ra tới x=±(74,95+2,0)=±76,95 m và z=−55,97−2,0=−57,97 m! Ngoài ra, 150 m chia cho bước lưới chuẩn 16 m bị lẻ, và 560×264 px mask nếu phủ lên 150×72 m sẽ làm méo tỷ lệ texel vuông (150/560=0,268 m/px theo trục X so với 72/264=0,273 m/px theo trục Z).

Lỗi xung đột giữa vùng click của Vòng cung Chỉ báo (y∈[680;895] px) và dải Edge-Pan dưới (y∈[906;930] px): Khi có quái lọt xuống phía nam khung nhìn (lúc người chơi đang pan lên bắc tại z_look=−36,5 m), mũi tên chỉ báo hướng nam trên vòng cung tâm (960;900) px sẽ quay xuống dưới (tức y>900 px), đè trực tiếp lên dải Edge-Pan dưới y∈[906;930] px! Khi người chơi rê chuột xuống để bấm vào mũi tên chỉ báo (nhấp để pan tới), chuột sẽ kích hoạt nhầm Edge-Pan dưới hoặc ngược lại.

Sửa lỗi và chuẩn hoá lại thông số (Đếm lại từ đầu = 0):

Chuẩn hoá kích thước Váy địa hình (Terrain Skirt), Mask & Clamp X:

Giữ vùng chơi (Playable Arena) đúng 140×66 m (x∈[−70;+70] m, z∈[−54;+12] m), nhưng thu hẹp nhẹ clamp ngang về x_look∈[−43,6;+43,6] m (vẫn thấy trọn Cổng ngoài tại x=±58 m với lề ngoài 43,6+26,35−58=11,95 m rộng rãi) VÀ mở rộng Váy địa hình (Terrain Mesh) thành 160×72 m (x∈[−80;+80] m, z∈[−58;+14] m), chia thành 10×6=60 chunk kích thước chẵn 16×12 m (lưới cull 8×6 m).

Kiểm tra biên với x_look=±43,6 m: góc trên khung nhìn đạt ±(43,6+28,35)=±71,95 m; cộng thêm 2,0 m lề chiêu "Hết màn" (§7) đạt ±73,95 m, nằm gọn trong biên địa hình ±80,0 m (dư 6,05 m an toàn).

Đổi độ phân giải Mask vẽ tay từ 560×264 px thành 640×288 px phủ toàn bộ 160×72 m, giữ mật độ texel vuông tuyệt đối 4,0 px/m (0,25×0,25 m/px) trên cả hai trục X và Z.

Tách bạch Vòng cung Chỉ báo và Dải Edge-Pan dưới:

Đặt tâm Vòng cung bán elip chỉ báo tại (960;860) px, bán kính ngang Rx=400 px, bán kính dọc trên Ry_top=180 px (y_min=680 px) và kẹp cứng đáy chỉ báo tại y_max=880 px.

Giữa biên dưới của chỉ báo (y=880 px) và biên trên của dải Edge-Pan dưới (y∈[906;930] px) có một khoảng đệm chết 26 px (y∈[880;906] px), đảm bảo thao tác nhấp chuột vào mũi tên chỉ báo (y≤880 px) không bao giờ chạm vào vùng kích hoạt Edge-Pan dưới (y≥906 px).

**Tự duyệt lần 1 (đếm lại từ đầu): PASS**

Lý do PASS (kiểm tra chéo toàn bộ hình học 3D, toạ độ frustum và động học đường đi):

Kiểm tra Frustum & Biên địa hình: Với x_look∈[−43,6;+43,6] m và z_look∈[−36,5;−2,06] m, hình thang mặt đất cộng 2 m lề chiêu "Hết màn" quét trong miền x∈[−73,95;+73,95] m và z∈[−57,97;+13,63] m, nằm hoàn toàn bên trong lưới địa hình 160×72 m (x∈[−80;+80] m, z∈[−58;+14] m).

Kiểm tra hiển thị Cổng ngoài & Thiên Đàn: Tại x_look=±43,6 m, z_look=−36,5 m, Cổng ngoài (∓58;−46) cao 7 m có đỉnh chiếu về z_proj=−46−1,1504×7=−54,05 m (nằm dưới mép trên z_top=−55,97 m khoảng 1,92 m mặt đất, tức cách mép trên màn hình ≈60 px). Trùm trên sàn Thiên Đàn (0;−40) cao 3,0 m có thanh chữ ở cao độ 8,0 m chiếu về z_proj=−49,2 m (cách mép trên màn hình ≈210 px).

Kiểm tra chia lưới Chunk & Mask: 160×72 m chia 10×6=60 chunk kích thước 16×12 m (chẵn tuyệt đối); mask 640×288 px đạt đúng 4 px/m ở cả hai chiều.

Kiểm tra thời gian di chuyển của quái: Đoạn ngoài 55,33 m ở vận tốc 4,16 m/s mất 13,30 s; đoạn trong 14,43 m ở vận tốc 1,60 m/s mất 9,02 s; tổng cộng 22,32 s, giữ nguyên nhịp gõ phòng thủ 9,02 s trong khung nhà.

**Tự duyệt lần 2 (liên tiếp): PASS**

Lý do PASS (kiểm tra ngân sách hiệu năng WebGL2, UX gõ phím và tính nhất quán nội tại):

Kiểm tra UX mắt nhìn & chuột: Khoảng cách từ thanh gõ Bàn Quyết (y=930 px) tới dải Edge-Pan dưới (y∈[906;930] px) bằng 0 px, tới vòng cung chỉ báo (y∈[680;880] px) chỉ 50–250 px (nằm trọn trong vùng nhìn cận trung tâm, đọc được số đếm cỡ 20 px mà không mất dấu dòng chữ đang gõ), và có vùng đệm tách biệt 26 px (y∈[880;906] px) chống bấm nhầm.

Kiểm tra giới hạn WebGL2 & Frame Time: sampler2DArray gom 6 vật liệu PBR vào 2 bind slot + 1 splat mask + 1 shadow map + 1 env map = 5 texture units (dưới xa ngưỡng 16 của WebGL2). Cắt Scissor tại y_css≤930 px giảm 13,9% tải fragment, kết hợp bước nhảy Shadow Camera Δsnap=0,03125 m giữ p95 frame time ổn định dưới trần 12 ms khi pan ở tốc độ tối đa 30 m/s.

Kiểm tra đầy đủ 4 yêu cầu của đề bài: Đã chấm điểm /10, phân tích đủ 5 nhóm rủi ro, đưa ra thông số sửa chữa chính xác, thực hiện tự duyệt với chuỗi đếm lại hợp lệ đạt 2 PASS liên tiếp, và sẵn sàng xuất dòng kết luận cuối theo đúng cú pháp.

KẾT LUẬN: Đồng ý phương án B (sân chơi 140×66 m mở rộng váy địa hình 160×72 m, 3×2 khung) — (1) Mở dải Edge-Pan cạnh dưới tại y ∈ [906; 930] px ngay trên Bàn Quyết kèm tự thu hồi camera về khung nhà sau 2,2 s hoặc 3 ký tự gõ và ghim vòng cung chỉ báo quái vào vùng cận mắt y ∈ [680; 880] px; (2) Chuẩn hoá clamp điểm nhìn x ∈ [−43,6; +43,6] m, z ∈ [−36,5; −2,06] m, hạ sàn đứng của Trùm trên Thiên Đàn xuống ≤ 3,0 m và chia 60 chunk 16×12 m (mask 640×288 px) để không cắt thanh chữ hay hở biên hình thang; (3) Áp dụng tốc độ hành quân 2 pha (ngoài ải ×2,6 = 4,16 m/s trong 13,3 s, qua Ải trong về ×1,0 = 1,6 m/s trong 9,0 s) kết hợp gom 6 vật liệu PBR vào sampler2DArray, cắt Scissor tại y ≤ 930 px và khóa bước nhảy Shadow Camera theo texel 0,03125 m.

## Claude kiểm và quyết (13/11/2026)

| Ý Gemini | Kiểm | Quyết |
|---|---|---|
| Hở biên ±5 m ở góc trên | Đúng (đã ghi trong v0.1 là chỗ vẽ vực) | Nhận: váy đất 160 × 72 m, clamp x ±43,6 |
| Thiên Đàn 9 m + trùm bị cắt | Hợp lý về hình học | Nhận: sàn trùm ≤ 3 m, vòm sau ≤ 8,5 m; tường bắc z −56 |
| Không có pan nam | Đúng | Nhận dải dưới y 906–930 (1080p) |
| Tự về nhà sau 3 ký tự / 2,2 s | **Trái D66** ("buông thì đứng yên, không tự quay về") | Bác. Thay bằng nút "về nhà" + nhấp chỉ báo; đưa câu hỏi cho anh |
| Phím Tab nhòm | Tab trong trình duyệt đổi focus, rủi ro với Bàn Quyết; luật "không phím" | Bác ở MVP, ghi là câu hỏi mở |
| Gấp 4,83 chứ không 3 | Đúng cách tính tới mép Kết Giới | Nhận số; nhịp hai pha là đề xuất cho bước sim, không chốt ở đây |
| Đạn bay 220 ms mọi khoảng cách | Hướng đúng (phản hồi gõ phải tức thì); con số là việc của VFX/sim | Ghi là yêu cầu: sát thương chốt ngay khi gõ xong, hình bay ≤ 0,3 s |
| Chỉ báo trên vòng cung gần Bàn Quyết | Tốt cho mắt, nhưng có thể che hành lang gần Kết Giới | Nhận ý, đặt chỉ báo ở vòng cung y 680–880 dạng mảnh, ≤ 40 % đục; thử trong lab |
| Diện tích 1 600 m² | Đúng (1 300 là phần không bị che) | Sửa số |
| sampler2DArray, scissor, snap bóng | Kỹ thuật hợp lý; scissor tuỳ HUD trong suốt | Ghi vào §8 như hướng, đo khi dựng |
| Số 450–600 ms chuyển mắt, 25 m/s đạn cũ | Không kiểm được nguồn | Không dùng làm căn cứ |
