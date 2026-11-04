# Quy trình làm VFX, CGI và SFX đẹp (VFX production pipeline), 04/11/2026

Tài liệu nghiên cứu và quyết định cách làm, dùng cho mọi game trong repo; Tu Tiên Thủ Ải là ca đầu tiên. Chưa đụng mã game. Cửa vào khi làm việc là skill `game-vfx-production`; tài liệu này là phần nghiên cứu và bằng chứng phía sau skill đó.

- **Vì sao có tài liệu này.** Lời anh, 04/11/2026, sau nửa đêm: "luôn ưu tiên dùng blender hoặc fire[fly] nếu 2 thứ này làm tốt hơn bạn… cách bạn đang làm… chưa đạt đến 6 điểm… ngọn lửa bạn làm ra, nhìn như rác". Tối 03/11 anh chê hào quang kiếm thô, đứng yên, không lấp lánh, sao bốn cánh vẽ bằng shader xấu, và muốn lửa chuyển động mượt, uyển chuyển, hơi thật.
- **Nguồn nghiên cứu, nguyên văn và bảng kiểm:**
  - [`source/vfx-pipeline-chatgpt-2026-11-04.md`](source/vfx-pipeline-chatgpt-2026-11-04.md): ChatGPT, chế độ Chat, thinking High, ba lượt: nghiên cứu; tự rà soát kèm kết quả thử của Claude; nhận các ý chính của Gemini để bổ sung (vòng hai theo `AGENTS.md`, "Plan with ChatGPT and Gemini").
  - [`source/vfx-pipeline-gemini-2026-11-04.md`](source/vfx-pipeline-gemini-2026-11-04.md): Gemini (Argon, mức Cao), bốn phần: lượt đầu lỗi giữa chừng, phần sau viết tiếp trong cuộc trò chuyện mới, tự rà soát, rồi nhận các ý chính của ChatGPT.
- **Thử thật trên máy (Claude, 04/11):** Blender 5.2.2 chạy không giao diện trên Mac mini M4: mô phỏng lửa Mantaflow, render dữ liệu, tách vector chuyển động, so bốn cách nội suy khung. Script, tấm khung và số đo ở `games/immortality-cultivation/tmp/shots/overnight/vfx-pipeline/blender/` (không vào Git). Kết quả ở §3 và §5.
- **Hai lane chạy cùng đêm (bằng chứng thực tế, đọc cùng tài liệu này):** [`tu-tien/skills/BLENDER_FIRE.md`](tu-tien/skills/BLENDER_FIRE.md) (9 ứng viên lửa Blender, tự chấm 5,5–6,5) và [`tu-tien/skills/FIREFLY_OVERNIGHT_2026-11-04.md`](tu-tien/skills/FIREFLY_OVERNIGHT_2026-11-04.md) (26 ứng viên Firefly Video; bản tốt nhất `ff-a1-c5` dùng ảnh làm khung đầu, tự ước khoảng 8). Cả hai chưa qua giám khảo mù.
- **Liên quan:** chuẩn năm pha [`VFX_STANDARD.md`](VFX_STANDARD.md); kiểu lửa anh đã chọn [`tu-tien/skills/FIRE_STYLE.md`](tu-tien/skills/FIRE_STYLE.md); hào quang kiếm [`tu-tien/skills/SWORD_AURA.md`](tu-tien/skills/SWORD_AURA.md); chẩn đoán lửa rồng Dragonhold [`vfx/DRAGON_FIRE_DIAGNOSIS_2026-10-31.md`](vfx/DRAGON_FIRE_DIAGNOSIS_2026-10-31.md); âm thanh chiến đấu `.agents/skills/game-art-pipeline/references/audio.md` §5.
- **Quy ước nhãn:** **Đã kiểm** = Claude mở nguồn hoặc tự chạy; **suy luận** = ý kiến (của trợ lý hoặc của Claude), phải đo khi dựng.

## 0. Tóm tắt quyết định

1. **Tách một hiệu ứng thành bốn phần, mỗi phần lấy từ công cụ giỏi nhất cho phần đó.**
   - Hình (đường bao, khoảng trống): ảnh vẽ bằng Firefly Image, ChatGPT hoặc Gemini, hoặc một clip Firefly đã đẹp sẵn.
   - Chuyển động bên trong (lửa cuộn, khói lăn): Firefly Video hoặc mô phỏng Mantaflow.
   - Màu, độ sáng, lót tối, lõi trắng: shader, qua dải màu theo bậc.
   - Vị trí, thời điểm, hướng, xói khi tan: code.

   Code không bao giờ vẽ ra hình chính. Đây là lỗi lớn nhất của ta tới nay (§1).
2. **Thứ gì gắn vào vật hoặc chạy theo đường thì làm bằng lưới (mesh hoặc ribbon) mang texture cuộn và xói, không làm bằng thẻ flipbook.** Gồm lửa quanh lưỡi kiếm, vệt kiếm khí, vệt lửa, ấn, vòng, rồng lửa. Texture cuộn có thể là clip Firefly đã duyệt hoặc dải lửa lát liền vẽ bằng Firefly Image (1024×256, 0,25 MB). Flipbook chỉ dành cho thứ hỗn loạn và ngắn: thân lửa va chạm, khói, nổ. ChatGPT, Gemini và các bài phân tích của nghệ sĩ đều nói vậy (§2).
3. **Blender render dữ liệu, không render màu.** Ba lượt render cho ba thứ: độ nóng (xám), độ phủ (alpha) và vector chuyển động. Màu theo bậc, viền tối và lõi trắng tính ở shader. Nhờ vậy một bộ dữ liệu dùng được cho nhiều hệ và nhiều dải màu, đổi màu không phải render lại. Đã chạy được trên M4: 48 khung, độ phân giải 128, mất 3,5–4,5 phút cả mô phỏng lẫn render (§3).
4. **Mượt trước hết nhờ đủ khung và không phát chậm khi thiếu khung.** Va chạm cần 24–48 khung, không phải 14–16 khung. Khi phải phát chậm hơn tốc độ gốc thì nội suy:
   - **Tạo khung chen bằng ffmpeg `minterpolate`** (bù chuyển động, chạy trước khi đóng gói): giảm sai số 26 % so với hòa trộn hai khung (đo trên lửa thật).
   - **Vector chuyển động lấy từ vận tốc mô phỏng** (Cycles), trộn khung kiểu Lozar ở runtime: giảm 18 %, tốn ít bộ nhớ hơn.
   - Optical flow tự viết chỉ giảm 2 %: bỏ.
5. **Firefly Video là tài sản cuối khi clip đã đạt** (vệt lửa anh đã thích, khói đẹp). Nó chỉ là nguồn chuyển động khi hình của clip chung chung, và bị loại khi hình sai (bông sen đối xứng). Mới: chế độ nền trong suốt nhận **ảnh PNG trong suốt làm khung đầu**, nên có thể đưa hình đã thiết kế vào làm điểm xuất phát (Adobe, đã kiểm). Lane Firefly cùng đêm đã thử đúng cách này: khung đầu là lửa Firefly uốn thành ba nét trăng lưỡi liềm, cho bản tốt nhất đêm đó (`ff-a1-c5`, tự ước khoảng 8, chưa chấm mù).
6. **Không dùng nâng cỡ video của Firefly:** nó chạy Topaz Astra, model đối tác (đã kiểm). Chỉ dùng Firefly Upscaler cho ảnh.
7. **Sao lấp lánh, tia lửa, tàn lửa là ảnh vẽ đặt lên hạt,** không phải hình tính toán: atlas 6–10 sao vẽ, 4–8 hình vảy lửa và vệt, chạy bằng `InstancedMesh`, có quỹ đạo, kéo dài theo vận tốc, ba cỡ và kẹp cỡ theo điểm ảnh. Vòng tính toán chỉ dùng cho vạch mảnh.
8. **Lót tối và ánh sáng.**
   - Lót tối theo chất liệu, không viền đen đều.
   - Một lớp premultiplied làm được cả viền tối (alpha cao, màu tối) lẫn lõi phát sáng (alpha thấp, màu HDR), nên không tốn thêm lớp. Viền tối đứt khúc, alpha 0,35–0,75; viền đặc khắp nơi thành "miếng dán đen".
   - Chỉ lõi mảnh vượt 1,0 để bloom.
   - Bỏ dải màu nhạt "né tone map".
9. **Thứ tự sửa:**
   1. Làm một va chạm lửa của phím 1 qua phép thử ba bản: A là clip Firefly đã thích, sửa alpha và tiếp xúc; B là Mantaflow ba nguồn phát; C là hình ba lưỡi từ ảnh cộng chuyển động hữu cơ.
   2. Duyệt hình bằng ảnh xám trước, rồi tới chuyển động, màu, lấp lánh và âm thanh.
   3. Ba lượt không lên điểm thì dừng và đổi cách (§10).
10. **Chấm theo tiêu chí quan sát được** (§7). Kèm đo tự động để bắt lỗi lùi, và vẫn cần hai giám khảo mù ≥ 8,5 trên bản dựng chơi.
11. **Âm thanh:** mỗi lớp (đầu, thân, đuôi, lớp ngọt) tạo một lượt riêng bằng Firefly Generate Sound Effects, rồi chồng lớp, chia mức to và đặt đúng khung va chạm, theo `audio.md` §5 (§8).

## 1. Ta đã sai ở đâu (có bằng chứng)

| # | Lỗi | Bằng chứng trong repo | Nguyên lý bị vi phạm | Sửa |
|---|---|---|---|---|
| 1 | **Hình do code vẽ** | sao bốn cánh là hai hình thoi chéo; vòng tính bằng khoảng cách tới bán kính (`abs(length(uv) - r)`); tàn lửa là đồng xu `1 − smoothstep(0.24, 0.38, r)` (`src/view/skills/embers.ts:83`); tia lửa nan bánh xe; nứt Voronoi; áo khí của kiếm vẽ bằng shader. Anh: "xấu", "thô", "không có chút chuyển động… lấp lánh" | Hình giải tích có tần số đều, đối xứng hoàn hảo, đọc thành nét UI hoặc hình gỡ lỗi; người xem nhận ra ngay là "procedural" (cả hai trợ lý; ArtStation và RealTimeVFX) | Mọi hình chính là ảnh vẽ (§2). Code chỉ giữ nhiễu, xói, vạch mảnh, vị trí, nhịp |
| 2 | **Không thiết kế hình** | `fire-burst`: clip Firefly 16 khung, bông sen 12–15 lưỡi bằng nhau, chỉ to rồi nhỏ (`FIRE_STYLE.md` §1.1) | Hình phải có hướng, có lớn–vừa–nhỏ và khoảng trống. Bông hoa đối xứng là trang trí, không phải đòn đánh | Duyệt hình bằng ảnh xám ở 80–150 px trước mọi màu và shader (RealTimeVFX, "Block-ins and Timing") |
| 3 | **Quá ít khung, lại phát chậm** | mọi atlas lửa có 14–16 khung ở 12–24 fps (`art-src/lab/vfx/fire/manifest.json`); khi tan lại phát chậm: `slowRate` 0,32–0,5 cho lửa đất (`element-fire.ts:538`), tức chỉ còn khoảng 4–6 hình khác nhau mỗi giây | Hòa trộn hai khung không tạo chuyển động mới, chỉ ra bóng ma đôi (Lozar 2015; cả hai trợ lý) | 24–48 khung; nội suy khi phát chậm (§5) |
| 4 | **Alpha mềm hoặc alpha lấy từ độ sáng** | tỉ lệ điểm ảnh nửa trong suốt (alpha 0,05–0,5 trên tổng điểm ảnh thấy được): `fire-trail` 0,85, `fire-charge` 0,41, `fire-burst` 0,20. Lửa rồng Dragonhold lấy alpha từ độ sáng nên lửa tối thành tấm màn (`DRAGON_FIRE_DIAGNOSIS` RC1) | Mép phải sắc, khoảng chuyển 0,5–1,5 px; alpha phải lấy từ matte thật (cả hai trợ lý; Adobe cấp video alpha riêng) | Alpha từ video matte hoặc từ lượt render độ phủ, cắt ngưỡng (§3, §4) |
| 5 | **Không lót tối** | trên đá sáng, lửa sáng chồng lên nền sáng (`FIRE_STYLE.md` §1.1) | Mắt đọc độ tương phản, không đọc số điểm ảnh sáng. Riot VFX Style Guide: thêm nền tối thủ công giúp hiệu ứng nổi, dùng tiết chế (đã kiểm) | Viền tối theo chất liệu, chung một lớp premultiplied (§6) |
| 6 | **Không lấp lánh** | không có sao, vòng mảnh hay ánh chạy nào quanh hình (`FIRE_STYLE.md` §1.3) | Sự sang đến từ vài điểm sáng đặt có chủ đích | Atlas sao vẽ, nhịp lóe 2–8 khung, đặt ở mũi, chỗ giao nhau, chỗ lửa tách |
| 7 | **Màu nhạt để né tone map, không bloom ở High** | dải `#ff9e6b`, `#ffd9a0` của Dragonhold (`DRAGON_FIRE_DIAGNOSIS` RC2) | Lõi HDR mảnh cộng bloom tạo cảm giác nóng; dải nhạt làm mọi thứ lưng chừng | Sửa đường HDR và tone map; bloom nửa độ phân giải, đo chi phí (§6) |
| 8 | **Một thẻ phẳng đặt trước con thú** | hoa sen là một thẻ quay về camera, `lift 0.7`, che mất con thú (`FIRE_STYLE.md` §1.1) | Hiệu ứng phải chạm đất và chạm mục tiêu: vòng cung tiếp xúc, ánh hắt, vết cháy | Thêm lưới tiếp xúc, decal, đặt lửa quanh chứ không đè lên |
| 9 | **Quy trình** | Dragonhold sửa khoảng 9 tham số mỗi vòng chấm suốt 4 vòng mà không đổi cấu trúc; chấm tài sản rời thay vì cảnh chơi; không dựng xám; làm từng bản rồi vá dần | Ba lượt không lên điểm thì đổi cách; 3–5 ứng viên cùng lúc; chấm ở camera chơi | Phép thử A/B/C (§10), luật dừng sau ba lượt |

**Chỗ ta làm đúng, giữ lại:** công cụ cắt atlas đã lấy alpha thật từ cặp video tiền cảnh và alpha của Firefly (`tools/vfx-flipbook`, `"matte": "alpha-video"`); flipbook đã có "hold and erode" (mỗi điểm ảnh tự chuyển khung ở một thời điểm riêng) thay cho mờ dần đều; FIRE_STYLE đã chọn đúng hướng (nét lửa có hướng, viền tối, lõi ≤ 5 %, tia lửa vệt, sao). Cái thiếu là **nguồn hình**: kiểu đúng mà hình vẫn do code hoặc clip chung chung tạo ra.

## 2. Bảng quyết định: loại hiệu ứng → công cụ và quy trình → vì sao → chi phí

Chi phí: giờ làm là ước lượng cho một họ hiệu ứng khi đã có công cụ. Số GPU ms là **suy luận** của hai trợ lý (khoảng giữa), phải đo bằng `lab-element-perf.mjs`. Số MB là phép tính cho RGBA8 không nén, chưa tính mipmap (+⅓).

| Loại hiệu ứng | Công cụ và quy trình tốt nhất | Vì sao | Chi phí |
|---|---|---|---|
| **1. Thân lửa va chạm** | **Hình:** ảnh 3 lưỡi lửa cong do AI vẽ (Firefly Image, ChatGPT hoặc Gemini), trắng trên đen, duyệt ở 80–150 px. **Chuyển động:** một trong ba cách: (A) clip Firefly Video nền trong suốt, có thể dùng ảnh hình làm khung đầu; (B) Mantaflow với 3 nguồn phát có hướng; (C) hình từ ảnh cộng chuyển động bên trong lấy từ A hoặc B. **Dữ liệu:** độ nóng, độ phủ, vector chuyển động, 24–48 khung. **Runtime:** một thẻ flipbook hoặc lưới cong, dải màu theo bậc, viền tối và lõi HDR trong một lớp; thêm lưới vòng cung tiếp xúc, tia lửa, sao, một đèn điểm tiếp xúc dùng chung theo ưu tiên (không đổ bóng, tắt trong 80–120 ms) | Mô phỏng và Firefly giỏi chuyển động nhưng không tự ra hình ba lưỡi đẹp: thử Blender ra khối nổ, Firefly ra bông sen. Hình phải đi vào từ ảnh. 80.lv Flame Burst (2026): flipbook mô phỏng 8×4 vẫn phải thêm cấu trúc tự dựng để sửa bố cục | 1–2 ngày; 0,1–0,25 ms; 24 khung ô 256 px = 6 MB, 48 khung = 12 MB |
| **2. Lửa quanh lưỡi kiếm bay** | Lưới ôm lưỡi dựng bằng Blender Python (bản sao mặt lưỡi phồng 2–3 cm, kéo dài mũi, UV dọc từ chuôi tới mũi); texture lửa cuộn liền mạch lấy từ **clip vệt lửa Firefly anh đã thích** (cắt vòng lặp) cộng mặt nạ lưỡi lửa do AI vẽ; hai tốc độ cuộn; xói tách thành lưỡi ở mũi; mờ theo góc nhìn | Thẻ phẳng trên kiếm xoay thì dẹt, rời khỏi lưỡi, che lưỡi. Lưới ôm lưỡi giữ lửa dính vào kiếm ở mọi góc. Màu và chuyển động anh đã duyệt được giữ nguyên | 4–8 giờ; 0,03–0,09 ms cho 1–6 kiếm; 0,25–2 MB |
| **3. Kiếm khí, vệt chém** | Ảnh nét bút do AI vẽ (thô ở đầu, mảnh ở giữa, nhọn ở cuối), đóng gói kênh (R thân, G mép trước sáng, B nhiễu tan, A viền mực); lưới lưỡi liềm hoặc ribbon theo đường cong Bézier (Blender Python, hoặc dựng ở runtime từ vị trí mũi kiếm), UV theo độ dài cung; lộ dần, cuộn, tan từ đuôi; vài sao ở đoạn nhanh nhất | Hình nằm ở lưới, chuyển động bên trong nằm ở shader. Texture trải hết dọc cung nên mép sắc cả ở cận cảnh. Thẻ flipbook phí 90 % điểm ảnh vào góc trống | 5–10 giờ; 0,02–0,08 ms; 0,5–2 MB |
| **4. Tia lửa, tàn lửa** | Atlas 4–8 hình do AI vẽ rồi làm sạch (vệt thon, giọt có đầu, vảy méo); không dùng hình tròn. Chạy bằng `InstancedMesh`: quỹ đạo đạn đạo có cản, kéo dài theo vận tốc trên màn hình (dạng "hotdog"), 3 cỡ theo luật lũy thừa, bắn thành 2–3 chùm theo hướng đòn, lóe 1–2 khung trước khi tắt | Đường bay và cỡ do code giữ, hình do ảnh giữ. Đồng xu nổi lên như bong bóng chính là thứ anh chê | 3–6 giờ; 0,02–0,08 ms; 0,06–0,25 MB |
| **5. Sao lấp lánh** | Atlas 6–10 biến thể vẽ (sao bốn cánh trục dài trục ngắn, sao lệch, sáu cánh, vệt ngang, chấm kim) từ Firefly Image hoặc ChatGPT trên nền đen, hoặc tấm sao Firefly Video trên nền đen (FIRE_STYLE A3, B3). Chạy bằng sprite instanced: kẹp cỡ 3–8 px ở camera chơi và 10–16 px ở khoảnh khắc lớn, bật trong 1–2 khung, giữ, thu lại trong 3–5 khung, xoay nhẹ, chỉ lõi là HDR | Hình vẽ có mipmap thì không răng cưa ở 38 px/m. Hình thoi tính toán thì răng cưa và "rẻ". Khan hiếm có chủ đích mới thấy sang | 2–5 giờ; 0,01–0,04 ms; 0,06–0,25 MB |
| **6. Vòng mảnh, ấn, pháp trận** | Thiết kế ấn bằng ảnh AI (trắng đen, ít ký hiệu lớn, không chữ Hán giả); tách lớp (vòng ngoài, ký hiệu, tâm, đường sáng chạy); chuyển thành SDF (biến đổi khoảng cách bằng numpy trong Blender; ký hiệu góc nhọn dùng MSDF) hoặc dựng lại vòng chính bằng đường cong Blender. Shader quay ngược chiều, lộ theo góc, chạy sáng, tan đứt khúc; khử răng cưa bằng `fwidth` | Ảnh cho nét trang trí; SDF giữ nét 1,5 px sắc ở mọi khoảng cách và góc nghiêng. Vòng tính toán chỉ dùng cho vạch mảnh và khung bố cục | 4–10 giờ; 0,02–0,06 ms; 0,25–1 MB |
| **7. Nứt, cháy đất, vệt cắt** | Ảnh AI vẽ 4–8 biến thể trong một chuẩn bộ (nhìn từ trên xuống, nền đen) → tách kênh tự động: R hình, G tuổi/hướng lan từ tâm, B đường nóng, A độ phủ (luật "vết có thiết kế là ảnh vẽ" ở skill `game-vfx-layered` bước 3) → decal. Shader lộ nhanh từ tâm (khoảng 4 khung), nóng rồi nguội thành than, tan. Voronoi chỉ làm nhiễu phụ | Mỗi loại vết có logic riêng (cắt, đập, cháy, nứt toác). Voronoi cho ô đều như da hươu. Mép tối dưới đường sáng là bắt buộc trên đá sáng | 6–12 giờ một họ; 0,03–0,12 ms; 0,25–1 MB |
| **8. Khói** | Hai lối, chọn theo kiểu khói. **Khói nổ cuộn:** Mantaflow (M4 đủ nhanh) hoặc VDB miễn phí của JangaFX (CC0) → render độ đặc, độ phủ và ánh lửa từ dưới → atlas 16–32 khung, ô 128–256 px, 2–3 bậc giá trị, xói không đều; dùng clip Firefly khói nền trong suốt nếu clip đẹp. **Cụm khói anime:** khối cầu chồng nhau dựng bằng Blender Python, pháp tuyến chuyển từ khối bao (Data Transfer), đổ bóng 2–3 bậc (Gemini, ChatGPT nhận ở vòng hai) | Khói cuộn khó giả bằng nhiễu 2D; mô phỏng đáng công ở đây. Khói thật nhiều chi tiết thì đục và bẩn, nên phải giảm bậc | 5–10 giờ; 0,04–0,12 ms; 1,5–6 MB |
| **9. Hơi nóng méo hình** | Một pass dùng chung ở ¼ hoặc ½ độ phân giải: thẻ ghi độ lệch RG (nhiễu CC0 của Screaming Brain) vào một render target nhỏ, gộp vào pass hậu kỳ; 0,5–2 px; không méo chữ và UI; chỉ ở cận cảnh (đã quyết ở FIRE_STYLE) | Méo thật phải lấy mẫu lại ảnh nền. Chép màn hình cho mỗi đốm lửa thì phá hiệu năng | 3–8 giờ hạ tầng; 0,06–0,25 ms cả pass; 0,06–1 MB |
| **10. Rồng lửa hoặc rồng khí bay theo đường** | Đầu và thân dựng trong Blender Python (thân là ống thon theo spline, vây và bờm là ribbon); lõi tối có ghi độ sâu, viền Fresnel HDR; lửa trên thân là texture cuộn từ clip vệt lửa Firefly; tan từ đuôi thành sợi khí; vài sao ở chỗ uốn | Firefly Video không giữ được giải phẫu con rồng khi rẽ. Flipbook 2D không lượn quanh mục tiêu được. Dựng thân trong suốt mà không ghi độ sâu sẽ thành khối trắng | 12–40 giờ; 0,12–0,35 ms; 1–8 MB |
| **11. Nước, sấm (sau này)** | Nước: Mantaflow liquid hoặc Firefly Video, cộng flow-map cuộn. Sấm: tia sét Firefly Video trên nền đen hoặc nét sét AI vẽ, đặt lên ribbon hoặc flipbook ngắn chạy theo nhịp 2 khung | Như lửa: hình từ ảnh, chuyển động từ video hoặc mô phỏng | đo khi làm |
| **12. Âm thanh chiêu** | Firefly Generate Sound Effects (model Adobe), mỗi lớp một lượt; chồng lớp, chia mức to, đặt đúng khung (`audio.md` §5) | Một bản ghi duy nhất không đủ lực; Adobe khuyên tạo từng âm riêng rồi ghép | xem §8 |

**Tỉ lệ lưới so với flipbook ở game thương mại:** Gemini đoán 75–85 % là lưới. ChatGPT không đưa con số và nói không có nguồn công khai cho Genshin hay HSR. Cả hai đều chỉ là **suy luận**. Điều đã kiểm được là các nghệ sĩ làm hiệu ứng anime dùng lưới với texture cuộn và xói cho chém, tia và vệt (80.lv Rayane Saada 2024; Soenke Seidel 2021; diễn đàn Unity 2022), và dùng flipbook cho thân lửa, khói, nổ (80.lv Flame Burst 2026). Kế hoạch của ta: khoảng 60–70 % họ hiệu ứng là lưới, ribbon và mặt nạ; 20–30 % flipbook; còn lại là decal và hậu kỳ.

## 3. Công thức Blender: lửa Mantaflow → flipbook (đã chạy thử)

### 3.1 Kết quả thử đêm 04/11

Script: `games/immortality-cultivation/tmp/shots/overnight/vfx-pipeline/blender/fire_burst_flipbook.py` (mô phỏng và render), `post.py` (tô màu thử, tấm khung, thử vector), `of_test.py` (optical flow), `mci_test.py` (ffmpeg). Lệnh:

```bash
.local/bin/heavy.sh --cores=8 /Applications/Blender.app/Contents/MacOS/Blender -b \
  --python <dir>/fire_burst_flipbook.py -- <out> 128 48 heat,mv 1.4 CYCLES
```

| Lượt | Thiết lập | Thời gian | Kết quả |
|---|---|---|---|
| 1 (r96) | độ phân giải 96, 48 khung; một lượt render gồm cả phát sáng lẫn hấp thụ | 1 phút 43 giây | độ nóng gần như mất: lớp hấp thụ ăn hết ánh phát sáng. **Bài học:** tách hai lượt render |
| 2 (r128) | 128; lượt phát sáng riêng, lượt hấp thụ riêng; vector lấy trong EEVEE | 3 phút 41 giây | dải màu bậc và mép sắc đều chạy được; lửa bay lên khỏi khung; vector toàn số 0: **EEVEE không đọc thuộc tính `velocity`** |
| 3 (r128b) | 128; lực nổi thấp hơn, khung rộng hơn; vector lấy trong **Cycles** | 4 phút 28 giây | lửa có viền tối, mép sắc, bậc màu rõ (`r128b/post/sheet-styled-light.png`, `sheet-styled-dark.png`); vector dùng được (§5.2). **Hình vẫn là một khối nổ xoắn, chưa thành ba lưỡi cong:** đủ ba lượt cho câu hỏi hình, dừng theo luật (§10) |

EEVEE render một khung 256 px mất khoảng 0,2 giây; lâu là ở khâu mô phỏng. Ở độ phân giải 128, máy M4 đủ để quét 6 bộ tham số trong khoảng nửa giờ.

**Lane Blender cùng đêm** ([`BLENDER_FIRE.md`](tu-tien/skills/BLENDER_FIRE.md)) đi xa hơn lượt thử này: nguồn lửa chạy theo cung như nét bút, miền mỏng 2,5D, 9 ứng viên, tự chấm 5,5–6,5. Kết luận giống ở đây: mô phỏng ở độ phân giải máy M4 cho chuyển động mềm nhưng hình bo tròn; thêm nhiễu wavelet thì mép lấm tấm như bông cải. Lane đó cũng đo: vector chuyển động giúp đoán khung sau sai ít hơn 36–43 % so với không dịch ở B1, 14–16 % ở dải lửa B2, dưới 4 % ở lửa đất B3, vì lửa đất đổi hình chủ yếu do cháy chứ không do trôi. Vậy vector chỉ đáng làm cho lửa có hướng bay rõ.

### 3.2 Từng bước (bản đã chạy, cộng chỗ sửa cho lưỡi lửa)

1. **Cảnh trống, chạy không giao diện:** `bpy.ops.wm.read_factory_settings(use_empty=True)`; số khung 1–48 ở 24 fps. Mọi thứ dựng bằng Python, không mở giao diện.
2. **Miền (domain):** hình hộp vừa khít hiệu ứng (thử: cạnh 3,6 m). Thiết lập: `domain_type='GAS'`; `resolution_max` 64 để dựng thô, 128 cho bản chính; `cache_type='ALL'`; `cache_data_format='OPENVDB'`; `use_noise=False` cho tới khi hình đạt. Cạnh dài nhất của miền quyết định cỡ voxel, nên miền thừa là phí độ phân giải (Blender manual). Lane Blender cùng đêm dùng **miền mỏng theo chiều sâu (2,5D)** cho nét lửa gọn và bake nhanh: 21 giây ở độ phân giải 128, 177 giây ở 448 (`art-src/lab/vfx/fire/blender/README.md`).
3. **Nguồn phát, đây là chỗ quyết định hình.**
   - **Bản thử:** một quả cầu, `flow_type='BOTH'`, `INFLOW`, đẩy theo pháp tuyến 2,6 cộng hướng (3,2; 0; 1,4), nhiên liệu tắt ở khung 9, thêm lực rối 9. Kết quả là một khối nổ.
   - **Cho lưỡi lửa** (ChatGPT lượt 2, khớp bài EmberGen anime trên 80.lv 2024 "giữ hình đơn giản, voxel to, nhiễu lớn nhưng tiết chế"): **ba nguồn phát nhỏ hình elip** (bán kính 0,08–0,14 m), mỗi nguồn có vận tốc riêng: giữa (0,2; 0; 3,2), trái (−0,8; 0; 2,4), phải (0,85; 0; 2,1); nhiên liệu tương đối 1 / 0,7 / 0,8. **Cho mỗi nguồn chạy theo đường cong trong khung 1–6** và tắt ở các khung khác nhau (Gemini vòng hai: trái tắt ở khung 4, phải ở 5, giữa ở 6, tự ra thứ bậc dài–vừa–ngắn; thêm thành phần chiều sâu y −0,35 / +0,25 / −0,2 m/s để ba lưỡi so le cả theo chiều sâu dưới góc 55°).
   - Thông số miền: `vorticity` 0–0,08 (cao thì nhiều xoáy nhỏ, thấp thì hình mượt), `flame_vorticity` 0,05–0,15, `burning_rate` 0,4 (lửa dài hơn), `flame_smoke` 0,08, `alpha` 0,1, `beta` 0,4 (lực nổi thấp để lửa đi theo hướng đòn, không bốc lên như lửa trại); chưa bật noise, chưa bật guide.
   - Nếu các lưỡi vẫn nhập làm một: rút ngắn thời gian phát, tách nguồn xa hơn, giảm xoáy. Sau ba lượt vẫn nhập thì **áp hình từ ảnh lên** (bước 7), không ép mô phỏng tự ra hình.
4. **Mô phỏng (bake) không giao diện:**
   ```python
   with bpy.context.temp_override(object=dom, active_object=dom, selected_objects=[dom]):
       bpy.ops.fluid.bake_all()
   bpy.ops.wm.save_as_mainfile(filepath=out + '/scene.blend')
   ```
5. **Camera:** trực giao, nghiêng đúng góc chơi (Tu Tiên: 55°), `ortho_scale` chừa lề 6–8 %. Thêm một camera nhìn thẳng để chẩn đoán: nhìn thẳng thấy ba luồng, nhưng ở góc chơi các luồng có thể chồng lên nhau theo chiều sâu.
6. **Render dữ liệu, ba lượt, `film_transparent=True`, EXR 32 bit, `view_transform='Standard'`:**
   - **Độ nóng:** khối chỉ phát sáng, cường độ bằng thuộc tính `flame` × k (thử k = 1,4; k = 3 làm lõi trắng quá rộng). Không có lớp hấp thụ. Render bằng EEVEE.
   - **Độ phủ:** khối chỉ hấp thụ, màu đen, mật độ = `density` × 4 + `flame` × 8; alpha của phim chính là độ phủ, gồm cả muội than, tức lớp lót tối. Render bằng EEVEE.
   - **Vector chuyển động:** chỉ dùng **Cycles** (EEVEE trả 0). Phát sáng = trọng số × (v·phải × s + 0,5; v·lên × s + 0,5), với v là thuộc tính `velocity`; một lượt nữa chỉ phát trọng số; chia hai ảnh cho nhau ra vector trung bình theo trọng số (trọng số = `flame` + 0,3 × `density`). Cycles 16 mẫu, CPU.
   - Volume Info chỉ có Color, Density, Flame, Temperature. `velocity` là một lưới riêng, đọc bằng nút Attribute (đã kiểm: manual 5.2 và lượt chạy thử).
   - Nếu xuất PNG thay cho EXR thì đặt `view_transform='Raw'` (Gemini): AgX mặc định nén vùng sáng và làm hỏng dữ liệu. EXR không áp view transform nên không bị.
   - Gemini (vòng hai) đề xuất gộp lượt độ nóng và lượt độ phủ thành một lượt EEVEE. **Không làm:** lượt r96 cho thấy lớp hấp thụ làm tối phần phát sáng, nên dữ liệu không còn thuần; mỗi khung chỉ tốn 0,2 giây, gộp lại không tiết kiệm đáng kể.
7. **Hậu kỳ, tô thử và áp hình** (Blender Python có numpy):
   - Chuẩn hóa theo cả chuỗi, không theo từng khung, để độ sáng không nhấp nháy.
   - Cắt ngưỡng độ phủ 0,30–0,40 cho mép sắc; chỗ nào có lửa thấy được thì đặc.
   - Dải màu 6 bậc (bảng A của FIRE_STYLE: `#1E0A0C`, `#6E1414`, `#D2401C`, `#FF7A26`, `#FFB43A`, `#FFF8E0`); viền tối là dải độ phủ nằm ngoài vùng lửa; lõi trắng ≤ 5 %; nới mép 1 px nếu mảnh quá.
   - **Áp hình** (cách C): dùng mặt nạ ba lưỡi lấy từ ảnh. Đó là phân vai giữa chuyển động vật lý và thiết kế hình, không phải gian lận.
   - **Mặt nạ phải sống** (Gemini vòng hai): nhân lửa đang chuyển động với một mặt nạ đứng yên trông như lửa chạy sau tấm bìa khoét lỗ. Đổi mặt nạ thành SDF cộng dải gốc → mũi: lưỡi bốc lên từ gốc, tan từ mũi vào, UV hơi uốn theo nhịp. Không "advect" mặt nạ bằng vận tốc từng khung: ảnh sẽ nhòe sau 4–6 khung (cả hai trợ lý cùng cảnh báo).
8. **Đóng gói:**
   - Atlas 6×4 (24 khung) hoặc 8×6 (48 khung), ô 256 px, chừa lề 4–8 px mỗi ô.
   - Ô ghi R = độ nóng, A = độ phủ, G và B để trống hoặc ghi nhiễu xói; màu tính ở shader.
   - Vector: atlas RG riêng ở ½ hoặc ¼ độ phân giải, không nén, `NoColorSpace`.
   - Ghi JSON như các atlas hiện có (`flipbook.ts`), cộng một hàng manifest và đường dẫn script bên cạnh.
9. **Kiểm trước khi ai chấm:**
   - Bản xám ở 80–150 px có đủ ba lưỡi và hai khe ≥ 3 px không.
   - Tỉ lệ phần nhạt (alpha 0,05–0,5) dưới 0,15; trắng ≤ 5 %.
   - Phát ở tốc độ thật và ở 0,25×, trên đá sáng và nền tối.
   - Đặt cạnh clip Firefly anh đã thích.

### 3.3 Grease Pencil, Geometry Nodes, VDB

- **Grease Pencil:** ChatGPT lượt 1 gọi đây là bước "thiết yếu" để vẽ tay hình lửa và nhát chém. Agent không có bút vẽ, nên **không dùng làm bước bắt buộc**. Grease Pencil chỉ là nơi chứa nét dựng bằng Python (ChatGPT lượt 2 đã rút lại).
- **Geometry Nodes, đường cong:** dựng ribbon, lưới lưỡi liềm, vỏ lưỡi kiếm, thân rồng từ đường Bézier, có UV theo độ dài cung. Mọi tham số nằm trong script, chạy lại được.
- **Ribbon 2,5D render ra atlas** (ChatGPT lượt 2): vài dải thon xoắn có texture lửa mô phỏng chạy qua, render từ camera chơi ra 24–48 khung. Ứng viên mạnh cho vỏ lửa quanh kiếm và vệt lửa có hướng.
- **VDB của JangaFX (CC0):** nguồn khói và lửa có sẵn khi mô phỏng của ta chưa đẹp. Chỉ dùng các file trong danh sách miễn phí, ghi một hàng `THIRD_PARTY.md` cho mỗi file.
- **Six-way lighting cho khói** (nướng sáng sáu hướng vào hai texture RGBA; Unity docs, blog 20/01/2023): **chưa làm**. Khói của ta nhỏ; một atlas đã có sáng sẵn cộng 2–3 bậc là đủ.

## 4. Công thức Firefly: video và ảnh → flipbook

1. **Chọn vai của clip trước khi tạo.** Bảng dưới theo ChatGPT lượt 2, Claude đồng ý:

   | Tình huống | Vai của Firefly |
   |---|---|
   | Clip đẹp ở cỡ chơi, lặp hoặc tan đúng, đi theo hành động | **Tài sản cuối**: giữ nguyên chất, chỉ sửa khi có lỗi thấy được |
   | Chuyển động bên trong đẹp nhưng hình chung chung | Nguồn chuyển động bên trong; hình lấy từ ảnh |
   | Hình sai về gốc (bông sen đối xứng) | Loại, hoặc chỉ để tham chiếu |
   | Lửa cần dính vào lưỡi kiếm | Texture cuối, đặt trên lưới ôm lưỡi |
   | Ấn cần nét chính xác | Không dùng video; dùng ảnh và SDF |
   | Rồng cần giữ giải phẫu | Chỉ làm texture lửa phụ |

   Gemini nói thêm một điều khớp với kinh nghiệm của ta: Firefly Video giỏi **dòng chảy liên tục** (vệt lửa, dải năng lượng, hào quang bốc lên), yếu ở **nổ một lần tỏa tròn** (clip kéo dài 5 s, không có cú bật 0,3 s). Vệt lửa anh thích và bông sen anh chê đúng là hai trường hợp đó.

2. **Đưa hình vào video.**
   - Chế độ nền trong suốt nhận **ảnh PNG trong suốt làm khung đầu và khung cuối** (helpx, cập nhật 18/08/2026, đã kiểm).
   - Vẽ trước hình ba lưỡi (Firefly Image hoặc ChatGPT), đưa vào làm khung đầu, rồi prompt cho lửa cuộn, uốn, tách mà vẫn giữ bố cục.
   - Không chắc giữ được hình suốt clip, nên coi đây là máy tạo ứng viên (ChatGPT lượt 2).
   - **Đã có bằng chứng** (`FIREFLY_OVERNIGHT_2026-11-04.md`): khung đầu dựng từ chính lửa Firefly mềm (uốn bằng biến đổi cực thành ba nét trăng lưỡi liềm, `crescent_frame.py`) cho clip `ff-a1-c5` lửa mượt, hơi thật, quét theo nhát chém, tự ước khoảng 8. Lane đó cũng xác nhận nền trong suốt chỉ chạy ở 540p, 16:9: lượt 1080p có bật trong suốt chạy khoảng 9 phút rồi bỏ.
3. **Prompt:**
   - Dưới 600 ký tự, camera tĩnh, một hiệu ứng ở giữa chiếm 65–75 % khung, ≤ 4 chủ thể.
   - Thân lửa dùng nền trong suốt; tia lửa và sao dùng nền đen phẳng.
   - Tả hình bằng hình học (số lưỡi, cong về đâu, khe hở) chứ không chỉ viết "lửa anime đẹp".
   - Cấm "cinematic", "realistic", "volumetric", "lens flare", "bokeh"; không gọi tên game hay studio.
   - Mẫu: FIRE_STYLE §5.5 (A1–C3) và ba prompt của ChatGPT lượt 1 (E2: va chạm, vệt lửa, khói).
4. **Tạo 3–5 bản mỗi món cùng lúc.** Firefly giới hạn tốc độ: gặp giới hạn thì đợi rồi làm tiếp.
5. **Lấy file ra** qua bộ nhận cục bộ (`browser-ai-tools.md` §4). Lấy **cả video tiền cảnh lẫn video alpha**.
6. **Cắt** bằng `tools/vfx-flipbook` (`"matte": "alpha-video"`, `endAtGap`):
   - Lấy alpha thật từ video matte và gỡ màu nền Firefly khỏi mép (công cụ đã làm, `FIREFLY_VFX_LIST.md` §5).
   - **Cắt ở đúng 24 fps gốc, giữ 24–32 khung cho va chạm, 48 khung cho bậc chất lượng cao** (hiện chỉ giữ 14–16).
   - Giữ gốc va chạm cố định, để hình tự chuyển động quanh gốc. Không căn tâm theo đốm sáng nhất.
   - Chừa lề ô 4–8 px; chuẩn hóa theo cả chuỗi.
7. **Mượt khi phải phát chậm:** chạy `minterpolate` **trên ảnh RGBA trước khi đóng gói**. Claude đã thử: alpha đi cùng chuyển động, không lệch với màu. Mép sinh ra một ít điểm ảnh nửa trong suốt, nên cắt ngưỡng alpha lại sau khi nội suy. Không nội suy riêng video màu và video alpha (ChatGPT cảnh báo lệch mép).
   ```bash
   ffmpeg -framerate 24 -i f_%04d.png -vf "minterpolate=fps=48:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1" g_%04d.png
   ```
   Soát kỹ các mũi lửa mới mọc: nội suy dễ làm méo chúng. Mũi nào méo thì bỏ khung đó.
8. **Vòng lặp:**
   - Ưu tiên một lần chạy (va chạm vốn không lặp).
   - Cần lặp thì chọn một đoạn 16–32 khung có khối ổn định, rồi cho texture chạy độc lập với hình.
   - Cuối cùng mới hòa đoạn chồng giữa cuối và đầu, kiểm mối nối bằng mắt. Hòa khung cuối với khung đầu không đủ để chứng minh liền mạch.
9. **Nâng cỡ:**
   - Video: **không** (Topaz Astra là model đối tác; đã kiểm trên adobe.com `/products/firefly/partner-models/topaz.html`).
   - Ảnh: Firefly Upscaler (model Adobe), chỉ dùng khi cần đường bao sạch trước khi làm mặt nạ.
   - Ô 256 px đang hiện ở 80 px thì không cần nâng cỡ.
10. **Khi nào dùng Firefly Image thay cho video:** sao lấp lánh, ấn, vết nứt và vết cháy, hình bao lưỡi lửa, nét kiếm khí, tức những thứ cần thiết kế tĩnh hơn là cần chuyển động. Tạo nhiều bản trắng đen, chọn theo hình bao, rồi làm sạch tự động (cắt ngưỡng, bỏ mảnh vụn, đo khe hở ở 64, 128 và 256 px). Ảnh tạo ra chưa phải mặt nạ dùng ngay được.

## 5. Chuyển động mượt

### 5.1 Số khung

| Hiệu ứng | Khung nguồn | Phát | Ghi chú |
|---|---|---|---|
| Va chạm thường của phím gõ | 24 (bậc chất lượng thấp), 48 (cao) | 24–30 fps; tổng 12–20 khung game ở 60 Hz | phần lớn thời gian nằm ở pha bung, pha tan dùng xói |
| Va chạm lớn | 32–48 | 24–30 fps | nội suy khi phát chậm |
| Lửa cháy liên tục | 16–32, lặp | 18–30 fps | texture chạy riêng, hình cố định |
| Khói | 16–32 | 16–24 fps | ô 128–256 px |
| Nét vẽ (kiếm khí, sét) | 6–12 hình | 12–24 hình mỗi giây, không hòa trộn | hình giữ theo nhịp 2 khung; lưới mang nó vẫn chạy mượt ở 60 fps |
| Sao, tia lửa | 1–8 | do shader điều khiển | không cần flipbook |

**Luật:** không bao giờ phát flipbook chậm hơn tốc độ gốc của nó mà không nội suy. Phần "đọng lại" của hiệu ứng dùng xói và nguội màu, không dùng phát chậm.

### 5.2 Bốn cách lấp khoảng giữa hai khung, đã đo

Đo trên 48 khung lửa Mantaflow (r128b), ô 256 px:
- **Cách đo:** dùng khung chẵn làm flipbook, khung lẻ làm đáp án đúng, tính sai số tuyệt đối trung bình trên độ nóng và độ phủ, chỉ ở vùng có lửa.
- **Script thử:** `post.py`, `of_test.py`, `mci_test.py`; số liệu ở `r128b/post/*.json`.

| Cách | Sai số so với hòa trộn thường | Chi phí runtime | Kết luận |
|---|---|---|---|
| Hòa trộn hai khung (đang dùng) | 0 % (mốc) | 2 lần đọc texture | bóng ma đôi ở mép đang chuyển động |
| Optical flow tự viết (Lucas–Kanade bằng numpy) | −2 % (dùng vector riêng cho mỗi chiều); +7 % (một vector cho cả hai chiều) | 4 lần đọc | **bỏ**; OpenCV (miễn phí, không phải AI) chưa cài và ta không muốn thêm phụ thuộc; TFlow, Twixtor, Slate đều trả tiền |
| **Vector từ vận tốc mô phỏng** (Cycles, trộn khung kiểu Lozar) | **−18 %** (hệ số tìm bằng quét; đổi dấu thì tệ hơn) | 4 lần đọc + 1 atlas RG nhỏ | **dùng cho lửa Mantaflow ở bậc thấp, hoặc khi cần đổi tốc độ phát** |
| **Khung chen offline bằng ffmpeg `minterpolate`** (bù chuyển động) | **−26 %** | như hòa trộn thường, nhưng atlas gấp đôi | **dùng ở bậc cao khi đủ bộ nhớ**; cũng là cách duy nhất cho clip Firefly |

**Lưu ý (ChatGPT lượt 2, Claude đồng ý):** sai số điểm ảnh thấp hơn chưa chắc là đẹp hơn. Nội suy có thể làm mép rung hoặc mũi lửa méo. Quyết định cuối nằm ở mắt người xem ở camera chơi, cùng với ngân sách texture: 24 khung là 6 MB, 48 khung là 12 MB, atlas vector RG8 ở ½ độ phân giải là 0,75 MB.

### 5.3 Công thức trộn khung bằng vector (Lozar 2015, đã kiểm)

Nếu nội dung đi một đoạn d từ khung A sang khung B, thì ở thời điểm t (0 → 1) giữa hai khung:

```glsl
// flowA: vector của khung A (A -> B), flowB: vector của khung B (B -> khung kế), đơn vị UV của ô
vec4 a = texture(uAtlas, cellUv(frameA, uv - flowA * t));
vec4 b = texture(uAtlas, cellUv(frameB, uv + flowB * (1.0 - t)));
vec4 c = mix(a, b, t);   // trộn trên dữ liệu premultiplied
```

- **Dấu:** lấy mẫu A ở `uv − d·t` và B ở `uv + d·(1 − t)`. Sai dấu thì sai số tăng; lượt thử đã xác nhận điều này.
- **Mã hóa:** RG = 0,5 + d/(2·D), với D là độ dời lớn nhất (thử ±8–16 px cho mỗi ô 256 px). Texture tuyến tính (`NoColorSpace`), không nén. Lozar cảnh báo: nén làm vỡ vector, sRGB làm lệch điểm 0.
- **Mép:** cho vector loang ra ngoài vùng lửa vài px (Lozar làm vậy với vector của FumeFX), che theo alpha, và kẹp UV trong ô để không lấy mẫu sang ô bên cạnh.
- **Hệ số:** với dữ liệu thử (ô 256 px, miền 3,6 m), độ dời tốt nhất là khoảng 0,08 × (thành phần vận tốc của lưới `velocity`) điểm ảnh mỗi khung, tìm bằng quét từ 0 tới 2,5 lần. Hệ số phụ thuộc cỡ miền, cỡ ô và tốc độ khung, nên mỗi atlas đo lại và ghi hệ số của nó vào JSON, không đoán.

### 5.4 Xói thay cho mờ dần, và bốn lớp chuyển động

- **Xói** (Gemini, khớp kỹ thuật "alpha erosion" của Simon Trümpler 2017):

  ```glsl
  float e = pow(life, 1.4);
  float a = smoothstep(e, e + w, M);                   // M: mặt nạ hình, w: 0,02–0,08
  float ramp = clamp((M - e) / max(1.0 - e, 1e-3), 0.0, 1.0);  // tô màu lại phần còn sống
  ```

  Mỗi mảnh còn lại giữ đủ viền tối, thân và lõi cho tới khung nó biến mất, không mờ thành sương cam.
- **Bốn lớp chuyển động** chồng lên nhau (ChatGPT): đối tượng di chuyển (quỹ đạo), đỉnh lưới hoặc ribbon (đường bao), UV và shader (dòng chảy bên trong), flipbook (thay đổi cục bộ phức tạp).
- **Chống cảm giác "GIF lặp"** (Gemini):
  - nắn UV bằng nhiễu tần số thấp;
  - đường cong thời gian phi tuyến: bung nhanh (khung 1–6 khoảng 36 fps), đọng lâu (khoảng 14 fps);
  - lật và xoay ngẫu nhiên mỗi lần sinh;
  - lưới nở theo đường ease-out.
- **Nhịp 2 khung** (Gemini): với nét vẽ hoặc flipbook cel thì tắt hòa trộn (`floor`), để hình bật như hoạt hình chính, còn lưới mang nó vẫn chạy mượt 60 fps. Hai trợ lý cùng ý: quỹ đạo, ribbon và tia lửa luôn chạy 60 fps; chỉ hình vẽ mới được giữ khung. ChatGPT (vòng hai) chặn một lỗi: không giữ khung cho clip lửa Firefly anh đã thích và cho lửa Mantaflow; chúng đẹp nhờ chuyển động liền.

## 6. Giữ chất anime và donghua

1. **Dải màu theo bậc bằng LUT 1D** (256×1, mỗi hệ một dòng):
   - Texture chỉ chứa dữ liệu xám; màu tính ở shader.
   - 4–6 bậc với chỗ chuyển gắt.
   - Lõi trắng chỉ ở 15–20 % trên cùng của thang độ nóng, và ≤ 5 % diện tích ở camera chơi.
   - Hai trợ lý cùng đề xuất; trùng với FIRE_STYLE §4.1.
2. **Mép sắc nhưng không răng cưa:** `smoothstep(t − aa, t + aa, mask)` với `aa = fwidth(mask)`, cho khoảng chuyển 0,5–1,5 px ở hình 40–200 px. Trong cùng một hình được có mép sắc (đường bao), mép mềm hẹp (chuyển màu bên trong), mép vỡ (lúc tan) và sợi sáng (lõi).
3. **Viền tối và lõi sáng trong một lớp** (Gemini C.2, Claude kiểm bằng phương trình hòa trộn):
   - Dùng blend premultiplied `ONE, ONE_MINUS_SRC_ALPHA`: `out = src.rgb + dst.rgb·(1 − src.a)`.
   - Ở mép ngoài, xuất màu tối với alpha cao: nền đá bị che, thành viền tối. Bắt đầu ở 0,35–0,75 và đứt khúc; alpha 0,85–0,9 chỉ ở vùng tiếp xúc, vì viền đặc khắp nơi thành "miếng dán đen" trên đá sáng (ChatGPT vòng hai).
   - Ở lõi, xuất màu HDR với alpha 0,15–0,25 (hoặc 0): ánh sáng được cộng lên trên (không hẳn là cộng sáng: alpha vẫn che nền một phần).
   - Alpha hòa trộn lấy từ một đường cong riêng theo dải màu, tách khỏi độ phủ khi xói (ChatGPT vòng hai).
   - Một lần vẽ làm cả hai việc, đúng với trần ≤ 2 lớp. Shader `rgba` của ta đã trộn premultiplied, chỉ cần cho alpha của lõi hạ xuống theo dải màu.
   - Riot VFX Style Guide (2017, đã kiểm qua trích đoạn PDF chính thức): thêm nền tối thủ công giúp hiệu ứng nổi, nhưng phải tiết chế, vì lạm dụng sẽ đè các hiệu ứng khác khi giao tranh đông. Với dòng sông kiếm phím 7, viền tối chỉ đặt ở đòn chính và kiếm dẫn đầu.
   - **Viền tối theo chất liệu** (ChatGPT): kiếm khí Metal có nét mực chàm mảnh ở mép trước; lửa có viền đỏ nâu đứt khúc và khe cháy; sao không có viền; vết nứt có đường rạch tối với đường sáng mảnh hơn ở giữa; khói là khối giá trị thấp, không viền vẽ.
4. **HDR và bloom:**
   - Toàn cảnh ở HDR tuyến tính; chỉ lõi mảnh, điểm tiếp xúc và vài sao vượt 1,0. Thân ≤ 0,9 (đã là luật ở FIRE_STYLE §4).
   - `UnrealBloomPass` với ngưỡng khoảng 1,0–1,5, chạy ở ½ độ phân giải cho bậc giữa; `OutputPass` làm tone map cuối (three.js docs, theo ChatGPT đã mở; Claude chưa mở lại).
   - **Phải đo chi phí:** bloom nhiều tầng mipmap không rẻ.
   - Bỏ dải màu nhạt "né tone map": sửa đường HDR thay vì làm nhạt màu.
5. **Ngôn ngữ hình:**
   - Lớn–vừa–nhỏ khoảng 50–65 / 25–35 / 10–15 % độ nhấn.
   - Đường cong chữ S dài, đầu nhọn thon; khoảng trống 10–25 %.
   - Ở 100 px phải còn hai khe ≥ 3 px.
   - Tu tiên thì ưu tiên sợi khí thon, vương miện lệch, chi tiết trang trí có kiểm soát; tránh nổ hình gai truyện tranh và các thùy giống nhau.
   - Hình chuẩn được duyệt bằng ảnh xám trước (RealTimeVFX "Block-ins and Timing", 2025, đã kiểm).
6. **Nhịp** (khung ở 60 Hz, ChatGPT lượt 1; chuẩn chung ở VFX_STANDARD §3.4):

   | Khung | Pha |
   |---|---|
   | −5 → −2 | nén, hút vào |
   | −1 | điểm tiếp xúc sáng gọn |
   | 0 | đỉnh: chớp ngắn |
   | 1–3 | bung lệch về một phía |
   | 4–8 | lưỡi lửa uốn, tách, rời |
   | 9–17 | lõi sụp, mảnh còn bay ra ngoài |
   | 18–30 | khói, tàn lửa, vết còn lại tan |

   Đòn gõ phím lặp lại thì bỏ gần hết phần chuẩn bị, tổng 12–20 khung. Gemini đề xuất đặt phần "chuẩn bị" vào ngay khung 0 để không trễ phím: một sao lóe ở mũi kiếm cộng tiếng tách, khung 1 là chớp va chạm, khung 2–4 giữ hình gần đứng yên cho mắt kịp đọc, khung 5–16 tan theo ease-out. Kiếm và va chạm luôn khớp sự kiện gameplay, sai lệch không quá ±1 khung.

7. **Biến mô phỏng hoặc clip thật thành anime:**
   - chọn vài khối lửa lớn dễ nhận ra;
   - đơn giản hóa chi tiết, áp hướng cho đường bao;
   - lượng tử hóa màu, gom chỗ sáng lại;
   - sửa nhịp và chỗ vỡ mép;
   - ghi dữ liệu, để engine lo chuyển động lưới.

   Voxel to, nhiễu lớn nhưng tiết chế, nong khói cho đặc, ít bậc màu (80.lv, bài EmberGen anime, 01/11/2024, đã kiểm). Clip anh đã thích thì không "toon hóa" quá tay: lửa hơi thật trong chuyển động là đúng ý anh.

## 7. Thang chấm: điều gì tách 6 điểm khỏi 8,5

Chấm ở cỡ người chơi thấy (camera chơi, khoảng 38 px/m, và cận cảnh), trên đá sáng và nền tối, ở tốc độ thật và 0,25×, đặt cạnh đoạn phim chính thức của Genshin Impact, Honkai: Star Rail, Wuthering Waves hoặc Naraka ở cùng cỡ trên màn hình. Giám khảo ghi điều mình thấy trước khi cho điểm (`judging.md`). Dưới đây là tiêu chí quan sát được cho từng mặt, gộp từ hai trợ lý và từ các phiếu chấm cũ của ta.

| Mặt | 4/10 | 6/10 | 7/10 | 8,5/10 | 9,5/10 |
|---|---|---|---|---|---|
| **Hình** | hình học thuần (vòng, hình thoi, đồng xu), đối xứng hoàn hảo | đọc được nhưng chung chung; thùy đều, không hướng | có hướng và có thiết kế, nhưng một phần còn chung chung | một khối chính có hướng, 2–3 khối phụ, mảnh nhỏ, khe hở rõ; ở 80 px vẫn đọc ra cử chỉ | có một khoảnh khắc đặc trưng người ta muốn cắt clip chia sẻ |
| **Chuyển động** | nhảy khung, bật, hoặc chỉ to nhỏ | mượt nhưng như GIF lặp; bên trong đứng yên | có sống bên trong, đôi chỗ cứng hoặc lộ mối lặp | bung nhanh, đọng có chủ đích, tan bằng tách mảnh; bên trong luôn cuộn; không bóng ma ở 0,25× | mọi lớp có nhịp riêng mà vẫn khớp nhau; đẹp cả khi soi từng khung |
| **Mép và alpha** | mép răng cưa hoặc viền nền; alpha lấy từ độ sáng | mép mềm như phun sơn, sương mờ lớn | mép sắc ở thân, còn vài chỗ mờ | mép sắc 0,5–1,5 px, phần nhạt < 15 %, không viền sai màu | các kiểu mép (sắc, vỡ, sợi sáng) dùng đúng chỗ |
| **Màu và giá trị** | phẳng, nhạt hoặc trắng xóa | một dải chuyển mượt, lõi trắng rộng | có bậc, lõi gọn, đôi chỗ lưng chừng trên nền sáng | 4–6 bậc, lõi ≤ 5 %, viền tối giữ độ đọc trên đá sáng, không đụng màu tín hiệu | bảng màu riêng, nhận ra ngay mà vẫn hợp thế giới |
| **Lớp và tiếp xúc** | một tấm dán, không chạm gì | có lớp phụ nhưng rời nhau, che mục tiêu | chạm đất hoặc chạm mục tiêu nhưng yếu | tiếp xúc, ánh hắt, vết lại trên đất; mục tiêu vẫn thấy rõ; ≤ 2 lớp trong suốt | hệ quả vật lý thuyết phục (mảnh vỡ, khói, vết) mà không rối |
| **Lấp lánh** | không có, hoặc rắc kim tuyến khắp nơi | vài chấm tròn đều nhau | có sao nhưng dày hoặc cứng | vài sao vẽ, đặt ở mũi, chỗ giao và chỗ tách; lóe 2–8 khung; khan hiếm có chủ đích | sang như trang sức: điểm, quạt, vòng, bụi theo nhịp |
| **Dễ đọc trong trận** | che chữ, che địch | đọc được một mình, rối khi đông | đọc được khi đông, đôi lúc che | đọc được với 20–50 địch và nhiều đòn chồng nhau; chữ và mục tiêu luôn rõ | như 8,5, cộng thêm thứ bậc rõ giữa các chiêu |
| **Hợp phong cách** | đồ gói tài sản chung chung | đẹp riêng lẻ nhưng lạc giữa game | hợp màu nhưng chưa có chất tu tiên | đúng chất anime, donghua và thần thoại; hợp kiếm, nhân vật, đất | tạo bản sắc cho game |

**Trượt ngay, bất kể các mặt khác:**
- hình chính do code vẽ;
- che mất vũ khí hoặc nhân vật thật;
- dùng màu tín hiệu đã dành riêng;
- trắng xóa màn hình;
- bật khung hoặc nhảy khung thấy được;
- mặt "dễ đọc trong trận" dưới 7.

**Lời giám khảo → lỗi thường nằm ở đâu** (ChatGPT, khớp phiếu chấm Dragonhold):

| Giám khảo nói | Lỗi thường gặp |
|---|---|
| "như game mobile" | thẻ phẳng, đồ gói hạt chung chung |
| "procedural" | vòng tròn hoàn hảo, đối xứng, sao tính toán |
| "mờ" | alpha mềm, hòa trộn khung, chuyển mép rộng |
| "như miếng dán" | không có tiếp xúc, không có chiều sâu |
| "như GIF" | cả hình lặp hoặc to nhỏ như nhau |
| "như sơn, như mực" | sai hình thái của lửa hoặc vết cháy |
| "không mạnh" | đỉnh yếu, không có phần chuẩn bị, không có lớp đầu âm |
| "rối" | mọi lớp tranh nhau |
| "không sang" | không có điểm sáng chọn lọc |

**Đo tự động để bắt lỗi lùi** (ChatGPT lượt 2). Không thay giám khảo; chạy sau mỗi lần sửa ở cùng camera, cùng khung, cùng mục tiêu:
- khung bao và tâm;
- diện tích và tính liên thông của khe hở (bắt lưỡi lửa nhập thành cục);
- tỉ lệ phần nhạt; tỉ lệ trắng xóa;
- độ dốc của mép;
- độ nhấp nháy của mép theo thời gian;
- ms GPU, số lệnh vẽ, texture đang nằm trong bộ nhớ;
- viền 2 px ngoài cùng của mỗi ô atlas có alpha bằng 0 (Gemini vòng hai; manifest đã có `cellBorderAlphaMax`): lửa chạm mép ô là dấu hiệu "flipbook rẻ" rõ nhất;
- không phạt độ nhấp nháy ở các khung cố ý giữ theo nhịp 2 khung.

**Giao thức:** hai giám khảo mù độc lập ≥ 8,5 trên bản dựng chơi, không cờ URL (luật của anh). ChatGPT đề xuất thêm "hai vòng đạt liên tiếp". Claude **không thêm**: luật của anh là đủ, và nhiễu giữa các vòng chấm (±0,5, `DRAGON_FIRE_DIAGNOSIS` RC5) sẽ được xử lý bằng clip chấm cố định.

## 8. Âm thanh: làm chiêu nghe có lực

Luật đầy đủ ở `.agents/skills/game-art-pipeline/references/audio.md` §5. Tài liệu này chỉ thêm phần hai trợ lý góp, sau khi đã đối chiếu với luật đó.

- **Ba phần của một đòn trúng:**
  - đầu (transient), 5–40 ms, là tiếng tiếp xúc;
  - thân, 60–250 ms, là chất liệu và khối lượng (lửa: tiếng bùng cuốn; kim loại: tiếng ngân của lưỡi);
  - đuôi, 0,1–0,7 s cho đòn thường và dài hơn cho đòn lớn (`audio.md` §5.3).
  
  Ba phần không lên đỉnh cùng một lúc; thân trễ 2–5 ms, lớp trầm trễ 4–8 ms.
- **Firefly Generate Sound Effects:** Adobe khuyên tạo **từng âm một rồi chồng lớp** (đã kiểm 02/11). Mỗi chiêu tạo ba lượt riêng (đầu, thân, đuôi hoặc lấp lánh); mỗi lượt cho 4 bản. Ba prompt mẫu của ChatGPT (lửa: tiếng nổ giòn ngắn, khối lửa bùng, đuôi tàn lửa lách tách) nằm ở `source/`. Phải sửa theo `audio.md` §5.6: không viết "small", "quiet", "soft"; với chiêu lớn thì đuôi dài và vang.
- **Lớp ngọt mang chất tu tiên** (Gemini): chuông đồng ngân, đàn tranh (guzheng) lướt, tàn lửa lách tách, đặt sau thân 15–40 ms. Hợp hướng "anime và thần thoại, không phải âm thật" của `audio.md` §5. Không dùng các con số compressor và ducking của Gemini (compressor tổng tỉ lệ 4, hạ nhạc −8 dB): `audio.md` §5.1 và §5.4 đã đo là chúng làm bẹp mix; nhạc chỉ hạ −4 tới −6 dB.
- **Voice to sound effects** (Adobe, theo kết quả tìm kiếm): ghi giọng để dẫn nhịp và độ mạnh. Agent không ghi giọng được, nên đây là việc anh có thể làm cho chiêu tuyệt kỹ nếu muốn.
- **Web Audio:**
  - Kích âm từ cùng sự kiện gameplay đã kích khung va chạm, rồi đo độ trễ nghe được.
  - Chia bus (gõ phím, vũ khí, va chạm, hệ, lớp ngọt, nhạc).
  - Đổi cao độ ±3–6 %; giới hạn số tiếng giống nhau chạy cùng lúc.
  - Khi đông địch: một tiếng đầu nổi bật cộng vài tiếng phụ nhỏ hơn, không phải mười tiếng nổ to bằng nhau.
- **Nguồn CC0:** Kenney Impact Sounds (CC0, theo cả hai trợ lý); Freesound chỉ lấy các file ghi rõ CC0. Gói Sonniss không phải CC0; luật repo cấm đưa cho AI (`licences.md` §4).

## 9. ChatGPT và Gemini khác nhau ở đâu; chỗ Claude không đồng ý

| Chủ đề | ChatGPT | Gemini | Claude chọn |
|---|---|---|---|
| Vai của Firefly Video | lượt 1: chủ yếu là tham chiếu chuyển động; lượt 2 sửa: tài sản cuối khi clip đạt | phần 1–2: chỉ là texture cuộn trên lưới (rồng, vỏ kiếm), kể cả vệt lửa anh thích cũng nên thay bằng lưới; phần 3 tự sửa: giữ clip đạt, chỉ nâng shader | **cả hai sau khi tự rà soát:** clip đạt thì dùng thẳng; anh đã thích một clip |
| Nguồn hình | lượt 1: Grease Pencil vẽ tay; lượt 2: ảnh AI → mặt nạ → đường cong Blender | Grease Pencil, Geometry Nodes, ảnh AI vẽ rồi dò nét | **ảnh AI → mặt nạ → đường cong hoặc SDF:** agent không vẽ tay được |
| Vector chuyển động cho lửa mô phỏng | lượt 1: pass Vector vô dụng, dùng optical flow; lượt 2 nhận đường `velocity` của ta | pass Vector vô dụng; OpenCV Farneback bằng script 25 dòng | **vận tốc mô phỏng (Cycles), hoặc khung chen của ffmpeg:** đã đo. OpenCV không có sẵn trên máy, còn optical flow tự viết thì yếu |
| Phát flipbook | nội suy khi cần, không bắt buộc | hai lối: nhịp 2 khung không hòa trộn, hoặc trộn bằng vector | **cả hai, tùy loại:** nét vẽ theo nhịp 2 khung, lửa và khói thì nội suy |
| Viền tối | phải theo chất liệu; "mọi lửa cần viền đen" là sai | một lớp premultiplied: mép alpha cao màu tối, lõi alpha thấp HDR | **gộp cả hai:** một lớp, viền theo chất liệu |
| Tỉ lệ lưới / flipbook | không có số công khai; tự đề xuất 60–70 % lưới | 75–85 % lưới (tự ghi là suy luận) | coi cả hai là suy luận; theo kế hoạch 60–70 % |
| Nâng cỡ video Firefly | lượt 1 gợi ý dùng, lượt 2 sửa thành cấm | không đề cập | **cấm** (Topaz Astra, đã kiểm) |
| Số ms GPU và giờ làm | tự rút lại ở lượt 2 | ghi là suy luận | chỉ dùng làm điểm xuất phát, đo bằng `lab-element-perf.mjs` |
| Nguồn trích | đa số đúng; vài trang ArtStation Claude không mở được | **nhiều link ghi "checked now" không đỡ câu được trích:** trang Blender manual tiếng Nhật về cache bị dẫn cho thông tin dải màu; bài Zelda trên 80.lv bị dẫn cho "khói thật trông bẩn" và "trải lưỡi liềm thành dải" (bài không nói vậy); trang hướng dẫn tạo video Firefly bị dẫn cho "Firefly ra bông sen đối xứng". Phần 3 nhận lỗi, nhưng hai câu sửa mới lại trích sai (bài của Seidel, hướng dẫn vòng lặp của Adobe) | tin ChatGPT hơn về nguồn; với Gemini thì chỉ lấy kỹ thuật đã kiểm được hoặc kiểm bằng toán (phương trình hòa trộn) |

### 9.1 Mỗi bên góp gì vào kế hoạch này

- **ChatGPT:**
  - tách hình khỏi chuyển động;
  - quy trình cho agent không vẽ tay (ảnh → mặt nạ → đường cong Blender);
  - bảng vai của Firefly (tài sản cuối, nguồn chuyển động, loại);
  - ba nguồn phát Mantaflow và ma trận thử M1–M6; phép thử A/B/C;
  - đo tự động chống lỗi lùi; lót tối theo chất liệu; bảng lời giám khảo → lỗi;
  - cảnh báo "sai số điểm ảnh thấp chưa chắc đẹp"; ribbon 2,5D render ra atlas;
  - tự tìm ra bộ nâng cỡ video là Topaz và khung đầu PNG của Firefly (lượt 2);
  - vòng hai: chặn viền tối quá đặc, nhịp giữ khung cho lửa Firefly, khung chớp che địch; tách alpha xói khỏi alpha hòa trộn; MSDF cho góc nhọn; dải lửa lát phải được làm liền mạch offline.
- **Gemini:**
  - một lớp premultiplied làm cả viền tối lẫn lõi HDR; xói có tô màu lại;
  - atlas vector ở độ phân giải thấp, tuyến tính, không nén;
  - nhịp 2 khung cho hình vẽ cùng chuyển động lưới 60 fps;
  - khung 0 lóe sao cộng tiếng tách cho game gõ phím;
  - Firefly giỏi dòng chảy liên tục, yếu ở nổ tỏa tròn;
  - dải lửa lát liền từ Firefly Image cho ribbon và vỏ kiếm; SDF tạo từ ảnh cho ấn và vết nứt;
  - đèn điểm 120 ms khi va chạm; `view_transform='Raw'` cho dữ liệu; xem trước ở độ phân giải 64;
  - âm kiếm thẳng (jian), reverb song song, nén nhẹ;
  - vòng hai: mặt nạ hình phải sống (SDF cộng dải gốc → mũi); kiểm viền 2 px của ô; vỏ kiếm dựng lưới sống chứ không render ribbon ra atlas; ba nguồn phát so le chiều sâu, tắt lệch khung.
- **Claude:**
  - chạy thử Blender trên M4: tách hai lượt render, vận tốc chỉ đọc được trong Cycles, thời gian thật;
  - đo bốn cách lấp khung; thử `minterpolate` giữ alpha;
  - kiểm nguồn: bắt bộ nâng cỡ là Topaz, các link trích sai của Gemini, quy tắc 70/20/10 không có thật;
  - đối chiếu mọi đề xuất với luật repo (không tên studio, không hình do code vẽ, `audio.md` §5).

### 9.2 Chỗ Claude không đồng ý với cả hai

- **"Hình từ mô phỏng":** cả hai coi Mantaflow là nguồn chính cho lửa va chạm. Lượt thử cho thấy mô phỏng chưa tự ra hình ba lưỡi, nên hình phải đi vào từ ảnh (ChatGPT lượt 2 đồng ý sau khi thấy kết quả).
- **Sao dùng nút Glare của Blender** (Gemini): nút Glare ra kiểu ống kính máy ảnh. FIRE_STYLE đã loại "lens flare", nên sao nên là ảnh vẽ có thiết kế.
- **Vết nứt bake từ Voronoi của Blender** (Gemini): vẫn là Voronoi. Theo luật của skill `game-vfx-layered` (bước 3), vết nứt là ảnh vẽ; Voronoi chỉ làm nhiễu phụ.

### 9.3 Vòng hai: mỗi bên nhận ý chính của bên kia

Theo `AGENTS.md` ("Plan with ChatGPT and Gemini", luật của anh ngày 04/11), Claude gửi mỗi trợ lý danh sách ý chính của trợ lý kia để đánh giá và gộp (nguyên văn ở hai file `source/`).

- **Gemini đánh giá 11 ý của ChatGPT:** nhận 6, sửa 4, bỏ 1.
  - Nhận: Mantaflow ba nguồn phát (thêm chiều sâu y, tắt lệch khung); `minterpolate` khi đủ bộ nhớ và vector khi thiếu; bảng vai của Firefly và lệnh cấm Topaz; ấn ghép vòng dựng bằng code với hoa văn do AI vẽ; phép thử A/B/C; viền tối theo chất liệu (gợi ý màu: chàm `#0A1526` cho Metal, đỏ nâu cháy `#2A0805` đứt khúc cho Fire, không viền cho sao).
  - Sửa: mặt nạ hình phải sống, không đứng yên; gộp hai lượt EEVEE; đo tự động thêm kiểm viền ô; ribbon 2,5D chỉ render ra atlas cho va chạm, còn vỏ kiếm thì dựng lưới sống.
  - Bỏ: "advect" mặt nạ bằng vận tốc.
  - Claude không theo đề xuất gộp hai lượt EEVEE (§3.2 bước 6).
- **ChatGPT đánh giá 12 ý của Gemini:** nhận 5, sửa 6, bỏ 1.
  - Nhận: xói có tô màu lại; Firefly cho dòng chảy và ảnh làm khung đầu; dải lửa lát liền trên lưới cuộn (cách tiết kiệm bộ nhớ tốt nhất cho vỏ kiếm và vệt dài: 1024×256 R8 chỉ 0,25 MB); đèn tiếp xúc và vòng méo nóng ở đòn lửa lớn; khói bằng cụm khối cầu có pháp tuyến chuyển từ khối bao (một lựa chọn mới bên cạnh flipbook).
  - Sửa:
    - viền tối alpha 0,88 khắp viền dễ thành "miếng dán đen" trên đá sáng: dùng 0,35–0,75 và đứt khúc, alpha cao chỉ ở vùng tiếp xúc; lõi alpha thấp không thật sự là cộng sáng, vẫn che nền một phần;
    - tách độ phủ khi xói khỏi alpha hòa trộn (một đường cong alpha riêng theo dải màu);
    - nhịp 12–15 hình mỗi giây chỉ cho hình vẽ; áp cho clip Firefly anh đã thích sẽ làm nó xấu đi;
    - khung chớp 125 % có thể che địch và làm vùng trúng trông to hơn thật; tiếng va chạm đặt ở khung tiếp xúc, không ở khung lóe sao;
    - SDF chỉ cho ấn và đường cắt mảnh; góc nhọn dùng MSDF (`msdfgen`); vết cháy vẫn là mặt nạ vẽ;
    - "¼ độ phân giải" phải nói rõ: thử 128² rồi 64² cho mỗi ô màu 256².
  - Bỏ: con số 75–85 % lưới.
  - ChatGPT nhắc lại: `minterpolate` (−26 %) vẫn là mốc phải vượt.

## 10. Việc tiếp theo

1. **Phép thử quyết định, một va chạm lửa phím 1, ba bản cùng lúc** (ChatGPT lượt 2; Claude đồng ý). Cùng thời lượng, camera, mục tiêu, nền và ngân sách:
   - **A:** clip Firefly đạt nhất hiện có, bắt đầu từ `ff-a1-c5` (`fire-crescent-sweep`, lane Firefly đêm 04/11), sửa alpha, thêm tiếp xúc và viền tối.
   - **B:** Mantaflow, bắt đầu từ `blender-b1-v15` của lane Blender, cộng ba nguồn phát có hướng; quét 6 bộ M1–M6 (ChatGPT lượt 2, §5.8), dữ liệu theo §3; khung chen bằng `minterpolate` hoặc vector.
   - **C:** hình ba lưỡi từ ảnh (Firefly Image, ChatGPT; 4 bản; chọn bằng đo khe hở) cộng chuyển động bên trong lấy từ A hoặc B.

   Duyệt hình bằng ảnh xám trước, rồi tới màu, lấp lánh, âm thanh. Gửi anh tấm khung và video 0,25× của cả ba trước khi chọn. Ba lượt không lên điểm thì dừng và bàn cách khác với ChatGPT và Gemini.
2. **Song song, không đụng mã game:**
   - sao và tia lửa thay cho sao và đồng xu do code vẽ: xem trước các tấm lane Firefly đã làm (`glint-gold-twinkle-set` từ `ff-g1-c3`, tự ước khoảng 7,5; `fire-gold-dust`, `fire-spark-spray`); chỗ còn thiếu thì tạo atlas sao 6–10 biến thể và tia lửa 4–8 hình bằng Firefly Image hoặc ChatGPT;
   - cắt vòng lặp từ clip vệt lửa Firefly đã duyệt làm texture lửa quanh lưỡi kiếm.
3. **Mã game (agent khác, bước sau):**
   - flipbook đọc dữ liệu xám cộng LUT bậc;
   - blend premultiplied một lớp có viền tối và lõi HDR;
   - trộn khung bằng vector (atlas RG);
   - đường cong thời gian phi tuyến;
   - `InstancedMesh` cho tia lửa và sao;
   - bloom ½ độ phân giải ở bậc giữa (đo trước);
   - mọi texture vector dùng `NoColorSpace`.
4. **Cập nhật skill `game-vfx-production`** (agent khác hoặc lượt sau) theo các điểm đã kiểm ở đây:
   - Firefly là tài sản cuối khi đạt;
   - khung đầu PNG cho Firefly Video;
   - cấm nâng cỡ video;
   - Blender render dữ liệu, vector chỉ lấy từ Cycles;
   - `minterpolate` trên RGBA;
   - ngưỡng: 24–48 khung, phần nhạt < 15 %, lõi ≤ 5 %, hai khe ≥ 3 px ở 100 px.
5. Thêm hàng `THIRD_PARTY.md` cho mọi file CC0 khi dùng thật (VDB của JangaFX, nhiễu Screaming Brain).

## Nguồn (đã kiểm ngày 04/11/2026 trừ khi ghi khác)

| Nguồn | Dùng cho | Trạng thái |
|---|---|---|
| Adobe helpx, "Generate videos with transparent backgrounds" (cập nhật 18/08/2026) | model Firefly Video; zip gồm video tiền cảnh và video alpha; 24 fps, 5 s; khung đầu và khung cuối là PNG trong suốt | Đã kiểm (mở trong trình duyệt) |
| Adobe helpx, "Upscale videos" (16/06/2026); adobe.com `/products/firefly/partner-models/topaz.html` | nâng cỡ video là Topaz Astra, model đối tác | Đã kiểm |
| Blender 5.0 release notes, Cycles | null-scattering là mặc định; bật lại kiểu cũ bằng "Biased"; khói và lửa dùng NanoVDB | Đã kiểm |
| Blender 5.2 manual: Render Passes; Fluid Domain Settings, Gas, Fire; Principled Volume; Volume Info; EEVEE Volumes; Fluid Cache | pass Vector; vorticity; reaction speed; các đầu ra của Volume Info; cache | Đã kiểm |
| Klemen Lozar, "Frame Blending with Motion Vectors" (16/03/2015) | trộn khung bằng vector; mã hóa; không nén; tắt sRGB | Đã kiểm |
| `ffmpeg -h filter=minterpolate` (bản trên máy) | `mi_mode=mci`, `mc_mode`, `me_mode`, `vsbmc` | Đã kiểm, cộng lượt thử RGBA |
| 80.lv, Rayane Saada, tia lửa anime (15/03/2024) | lưới, texture cuộn, xói, mặt nạ, khúc xạ | Đã kiểm |
| 80.lv, Kirill Anchikov, Flame Burst (20/01/2026) | flipbook EmberGen 8×4 cộng cấu trúc tự dựng; ribbon có khúc xạ | Đã kiểm |
| 80.lv, nổ anime bằng EmberGen, Nello Fontani (01/11/2024) | voxel to, nhiễu tiết chế, ít bậc màu, nong khói | Đã kiểm |
| 80.lv, Soenke Seidel, VFX kiểu Zelda (21/01/2021) | dải lưới cong mang texture cuộn; tan bằng flow map | Đã kiểm (không đỡ các câu Gemini gán cho bài) |
| RealTimeVFX, "Block-ins and Timing" (28/10/2025) | dựng xám, hình đơn giản, nhịp trước | Đã kiểm |
| Simon Trümpler, simonschreibt.de (07/06/2017) và trang Unreal Fest Europe 2018 | xói alpha theo ngưỡng; texture đơn giản, méo UV, lưới | Đã kiểm |
| Diễn đàn Unity, "How do I make vfx for attacks in Anime style?" (25/04/2022) | texture nhát chém cuộn trên đĩa lưới; xói alpha | Đã kiểm |
| VFX Apprentice, tóm tắt hướng dẫn VFX của League (22/10/2026) | tiêu điểm, giá trị, chuẩn bị–va chạm–tan, chỉ chớp chính mới ở đỉnh sáng | Đã kiểm |
| Unity VFX Graph, six-way lighting; blog 20/01/2023 | nướng sáng sáu hướng cho khói | Đã kiểm (qua tìm kiếm) |
| MDN, `EXT_disjoint_timer_query` | WebGL2 dùng `EXT_disjoint_timer_query_webgl2` | Đã kiểm |
| three.js docs: UnrealBloomPass, OutputPass, quản lý màu | bloom, tone map, không gian màu | Theo ChatGPT (đã mở); Claude chưa mở lại |
| Hazel Stagner, Johan Nydahl, Adam Gothard (ArtStation) | đĩa đen dưới nhát chém, nhiễu cuộn, decal đóng gói kênh | **Chưa kiểm** (ArtStation chặn công cụ) |
| Riot "Clarity in League", VFX Style Guide; Sheila Stipnieks; Unity Labs và JangaFX CC0 | thứ bậc, xói, giấy phép | Đã kiểm 01–03/11 (`FIRE_STYLE.md` §2, `FREE_ASSET_SOURCES.md` §7) |
| Riot VFX Style Guide, PDF trên nexus.leagueoflegends.com (2017) | nền tối thủ công giúp hiệu ứng nổi, dùng tiết chế | Đã kiểm (trích đoạn qua tìm kiếm, 04/11) |
| Lượt thử Blender và ffmpeg của Claude (04/11) | thời gian trên M4, vector từ `velocity`, so bốn cách nội suy, alpha qua `minterpolate` | Tự chạy; script và số liệu ở `games/immortality-cultivation/tmp/shots/overnight/vfx-pipeline/blender/` |
