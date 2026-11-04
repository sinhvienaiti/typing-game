# Firefly Video đêm 04/11/2026: hào quang kiếm và lửa (Sword × Fire)

**Trạng thái:** ứng viên, chưa chấm mù, chờ anh xem. Không sửa mã game, không commit trong repo game. Mọi điểm "~" dưới đây là Claude tự ước khi nhìn ảnh, **không** phải điểm giám khảo.

**Xem nhanh cho anh** (không vào Git):
- `games/immortality-cultivation/tmp/shots/overnight/firefly/candidates-board.jpg`: cả 26 ứng viên, mỗi ứng viên một khung mạnh nhất, ô viền vàng là bản Claude chọn.
- `.../picks-reel.mp4` (66 giây): các bản chọn chạy thật, mỗi bản trên nền đen, đá sáng `#d6d0c2`, đá sáng có lót mực, đá tối `#2a2c30`.
- `.../picks-play-size.jpg`: bản chọn ở cỡ người chơi thấy (kiếm 60–130 px, sao mũi 12–32 px, va chạm 80–160 px) và cận cảnh.

## 1. Việc được giao và lời anh

- **Lời anh (04/11, sau nửa đêm), tóm:** luôn ưu tiên Blender hoặc Firefly nếu chúng làm đẹp hơn; cách làm hiện tại chưa tới 6 điểm; ngọn lửa Claude làm "nhìn như rác". Trước đó: hào quang kiếm thô, đứng im, không lấp lánh; sao mũi vẽ bằng mã xấu; lửa phải mượt, uyển chuyển, hơi thật.
- **Việc:** làm clip Firefly Video, mỗi mục ít nhất 3 ứng viên, rồi cắt thành atlas flipbook:
  - cho hào quang kiếm ([`SWORD_AURA.md`](SWORD_AURA.md), A Wind-Silk Mantle + sao mũi của C): **M1** dải khí lụa Metal, **F1** dải lưỡi lửa Fire, **G1** sao lấp lánh thay sao mũi vẽ bằng mã;
  - cho lửa ([`FIRE_STYLE.md`](FIRE_STYLE.md) §5.5): **A1** thân lửa nét bút, **B2** tia lửa kiểu trang sức, **B3** sao lấp lánh, **C3** vòng mảnh và tia.

## 2. Cách làm

**Công cụ.** Firefly web, Generate video, model **Firefly Video** (Adobe, Commercially safe). Trang mở sẵn model đối tác Veo 3.1: đã đổi sang Firefly Video trước clip đầu. Một tab riêng, một clip một lúc, đóng tab khi xong. Không đăng nhập, không bấm đồng ý gì.

**Cài đặt.**
- Nền trong suốt: chỉ chạy ở 540p, 16:9. Lượt 1080p có bật trong suốt chạy khoảng 9 phút rồi bỏ, không ra clip, không báo lỗi.
- Nền đen: 1080p, 16:9 cho dải và tấm, 1:1 cho hiệu ứng ở giữa.
- 24 fps, 5 giây, không preset kiểu, camera hay cỡ cảnh.

**Số lượt.**
- 26 lượt ra clip, mỗi lượt một ứng viên. Mỗi clip mất 40 giây đến 5 phút.
- 2 lượt hỏng:
  - `ff-f1-c1` lần đầu ở 1080p có trong suốt;
  - `ff-b2-c1` lần đầu: trình phát giữ clip cũ, bản tải về trùng `ff-m1-c1` nên đã xóa và tạo lại.
- Không chạm giới hạn tốc độ.

**Lấy file.**
- Bộ nhận `127.0.0.1:8813`: nhận nhiều luồng, không ghi đè, chỉ nhận tên `ff-<mục>-c<k>`.
- Trang gửi bằng form POST multipart. Bộ nhận trả 204, nên tab không rời trang. Lần này form gửi vào iframe ẩn không tới được bộ nhận.
- Mỗi lần gửi đều so cỡ blob và chặn video đã gửi rồi.
- Clip gốc nằm ở `~/VFXLab/inbox/firefly/immortality-cultivation/overnight/<id>/`, không vào Git.

**A1 c5 dùng ảnh làm khung đầu (image-to-video).**
- Khung đầu do Claude tự dựng: lấy khung 80 của chính clip lửa Firefly `ff-f1-c2` (kiểu lửa mềm anh thích), uốn bằng phép biến đổi cực thành ba nét trăng lưỡi liềm thuôn hai đầu (`crescent_frame.py`).
- Đưa ảnh vào ô "First" của Firefly bằng `input[type=file]` trong shadow DOM của `firefly-upload-with-crop#upload` và sự kiện `change`. Ảnh được phục vụ từ `127.0.0.1:8814` (có CORS).
- Firefly Video giữ đúng hình ba nét và cho lửa chuyển động mượt. Đây là cách duy nhất đêm nay cho ra lửa vừa đúng thiết kế vừa đúng chất lửa anh thích.

## 3. Xử lý thành atlas

Script nằm cạnh atlas ở `art-src/lab/vfx/<aura|fire>/source/firefly-overnight/`. Python của Audio Lab có numpy, scipy và Pillow. Không dùng AI chạy máy.

- **Clip trong suốt:** video màu của Firefly là `C = a·F + (1−a)·B` trên nền riêng của nó. Script dựng lại B từ các điểm có alpha gần 0, giải ra F, rồi lan màu đặc vào mép mềm và các texel trống. Kết quả là alpha thẳng.
- **Clip nền đen:** trừ mức đen. Có hai cách ra:
  - additive (rgb trên đen) cho vệt, sao, vòng và dải khí;
  - alpha lấy từ nền đen cho thân lửa va chạm: `alpha = smoothstep(lo, hi, max kênh)`, màu bằng rgb chia alpha, mép mềm lấy màu đặc gần nhất để không có viền tối.
- **Dải lặp theo x** (M1 c3, F1 c2, B3 c3):
  - **Lặp theo thời gian:** chọn cửa sổ có đầu và cuối giống nhau nhất, rồi hòa chéo 8 khung.
  - **M1 c3:** clip là một hình nón. Mỗi cột được kéo về cùng bề cao và bù sáng theo cột. Chỗ nối dùng hòa chéo dài 360 px, vì các vệt chạy dọc x.
  - **F1 c2 và B3 c3:** nối bằng đường cắt có sai số nhỏ nhất, một đường cho mọi khung, mép mềm 12 px với F1 c2 và 6 px với B3 c3.
  - Ở cả ba dải, chỗ nối không còn thấy khi lặp hai lần.
- **Thẻ dọc lưỡi** (M1 c4, F1 c4) và **vòng** (C3 c3): vòng lặp 24 hoặc 32 khung, hòa chéo 8 khung.
- **Hiệu ứng một lần** (A1, B2, C3 c2, G1 c2): 24–32 khung, phai ở đầu và cuối. A1 tắt bằng ăn mòn: ngưỡng trên "độ sáng × 0,65 + nhiễu mượt × 0,35" tăng dần, nên mép và đầu nét cháy hết trước, lõi nóng vỡ sau cùng. Không làm mờ đều.
- **Bộ lấp lánh** (G1 c1, G1 c3, B3 c1):
  - dò tâm sao ở từng khung rồi gom theo vị trí;
  - mỗi sao thành một hàng: một lần lóe, từ cực tiểu trước đỉnh tới cực tiểu sau đỉnh, 16 khung;
  - bỏ sao trùng và sao dính láng giềng.
- **Tấm xem và video:**
  - mọi khung (dải: mỗi 4 khung) trên nền đen, đá sáng và đá tối;
  - art additive có thêm hàng "đá sáng + lót mực": lót tối lấy từ chính mặt nạ của art. Đây là giả định về cách shader sẽ lót, không phải shader thật.

**Quy ước atlas** theo `art-src/lab/vfx/fire/manifest.json`: hàng trước, từ ô trên trái; JSON riêng cho mỗi atlas (ô, khung, fps, lặp, trộn, pivot, nguồn, xử lý, số đo). `manifest.json` của hai thư mục có thêm hai khóa:
- mục mới trong `flipbooks`;
- `fireflyOvernight`, gồm bảng ứng viên, đường dẫn clip, prompt và nhận xét.

Các khóa sẵn có giữ nguyên. Trong `fire/` có thư mục `blender/` của một agent khác, không đụng.

## 4. Ứng viên

| Id | Thấy gì | Tự ước | Atlas |
|---|---|---|---|
| `ff-m1-c1` | Trong suốt. Dải lông vũ bạc lam viền chàm, gần như đứng im | ~6 | `aura-metal-featherplates` |
| `ff-m1-c2` | Trong suốt. Năm sáu dải lụa xám gợn | ~5 | — |
| **`ff-m1-c3`** | Đen. Hình nón vệt khí bạc rất mảnh, lõi xanh, chảy nhanh, vài hạt sáng | ~7,5 | **`aura-metal-windsilk`** (dải lặp x) |
| **`ff-m1-c4`** | Đen. "Lưỡi khí lông vũ": mảnh lông bạc gân xanh hai bên một sống xanh, sợi lụa xanh hội về mũi kim | ~8 | **`aura-metal-feather-mantle`** (thẻ dọc lưỡi) |
| `ff-f1-c1` | Trong suốt. Hàng lưỡi lửa thật nhỏ, đứng thẳng, không bạt | ~6 | `aura-fire-fringe` |
| **`ff-f1-c2`** | Đen. Dòng lửa mềm cuộn quanh một đường giữa, như vệt lửa Dragonhold anh thích | ~7,5–8 | **`aura-fire-ribbon`** (dải lặp x) |
| `ff-f1-c3` | Trong suốt. Hàng lưỡi đỏ đều như cỏ | ~4 | — |
| **`ff-f1-c4`** | Đen. Lưỡi lửa mượt, hơi thật, liếm ra hai bên một đường nóng, bùng ở đầu trái, thuôn thành kim ở phải | ~8 | **`aura-fire-flame-sheath`** (thẻ dọc lưỡi) |
| `ff-g1-c1` | Đen. Khoảng 20 sao 12 tia xanh trắng | ~6 | `glint-starburst-set` |
| **`ff-g1-c2`** | Đen 1:1. Một sao (4 cánh dài + 4 cánh chéo mảnh, lõi nhỏ, quầng mềm) lớn lên rồi tắt, xoay nhẹ | ~8 | **`tip-star-glint`** |
| `ff-g1-c3` | Đen. Lưới sao vàng nhạt (4 cánh, chữ X, 8 cánh), mỗi sao lóe và đổi dáng | ~7,5 | `glint-gold-twinkle-set` (8 biến thể) |
| `ff-a1-c1` | Trong suốt. Ba nét thư pháp, rồi thành một nét dài giống logo thể thao | ~5 | — |
| `ff-a1-c2` | Trong suốt. Một sao chổi lửa nhỏ bay ngang | ~4 | — |
| `ff-a1-c3` | Đen 1:1. Nhát chém trăng lưỡi liềm anime: ba nét son cam, đủ hình ở khung 0 | ~7 | `fire-brush-slash` (phương án cách điệu) |
| `ff-a1-c4` | Đen 1:1. Lửa thật tự vẽ thành xoắn ốc, chậm | ~6 | — |
| **`ff-a1-c5`** | Khung đầu là lửa Firefly uốn thành ba nét trăng lưỡi liềm. Lửa mượt, hơi thật, quét vòng theo nhát chém | ~8 | **`fire-crescent-sweep`** |
| `ff-b2-c1` | Đen 1:1. Que pháo hoa tỏa đều 360° | ~6 | — |
| **`ff-b2-c2`** | Đen. Chùm tia lửa thật từ một điểm tỏa xuống phải, vệt mảnh, đầu nóng | ~7 | **`fire-spark-spray`** |
| `ff-b2-c3` | Đen 1:1. Vệt vàng kèm sao nhỏ, nhưng vệt ngoằn ngoèo như sét | ~6 | — |
| `ff-b2-c4` | Đen 1:1. Pháo hoa tỏa đều | ~5,5 | — |
| `ff-b3-c1` | Đen. Sao vàng có quầng tròn như lóa ống kính, thêm hình thoi xám rẻ | ~5,5 | `fire-twinkle-set` (để so) |
| `ff-b3-c2` | Đen 1:1. Sao lớn kèm vệt lóa ngang và đốm bokeh | ~5 | — |
| **`ff-b3-c3`** | Đen. Bụi vàng li ti ở thấp, sao 4 cánh lóe rồi tắt | ~7 | **`fire-gold-dust`** (dải lặp x, dư âm) |
| `ff-c3-c1` | Đen. Bốn nhóm vòng đồng tâm mảnh, nở ra, có sao ở giao điểm | ~6,5 | — |
| `ff-c3-c2` | Đen 1:1. Một vòng vàng; tia mảnh dồn vào tâm, chữ thập tia dài lóe lên | ~7 | `fire-halo-ring` (phương án một lần) |
| **`ff-c3-c3`** | Đen 1:1. Các vòng vàng mảnh như tóc, có đoạn đứt, xoay, sao nhỏ chạy trên vòng | ~7,5 | **`fire-halo-seal-loop`** |

Đầy đủ (prompt, cài đặt, nhận xét): `fireflyOvernight` trong hai `manifest.json`, và `source/firefly-overnight/<id>.prompt.txt` cùng `.settings.txt`.

## 5. Chọn mỗi mục và vì sao (so với thanh 8,5 của anh)

- **M1:** hai bản bổ nhau.
  - `ff-m1-c4` (thẻ) là bản gần thiết kế Wind-Silk Mantle nhất: mảnh áo sắc, đường sống, sợi lụa hội về mũi kim. Nó sang và có phong cách. Nhưng hình bóng cố định, không lặp theo x. Mảnh lông sáng và trông đặc, nên shader phải giữ mặt lưỡi trần và thân ≤ 0,9.
  - `ff-m1-c3` (dải lặp x) là vệt lụa khí rất mảnh, chảy nhanh, thật sự lấp lánh. Nó hợp làm thân áo cuộn theo U. Là additive nên trên đá sáng cần lót mực.
  - Ở 60 px, cả hai chỉ còn một vệt sáng; các mảnh chỉ đọc ra từ khoảng 130 px.
  - Claude nghĩ hai bản có thể tới 8 khi vào shader có khe mực, đường may và sao. Bản thân art chưa phải 8,5 nếu đứng một mình.
- **F1:** cũng hai bản.
  - `ff-f1-c4` (thẻ) có lửa mượt, hơi thật, liếm hai bên lưỡi, thành kim ở mũi. Cùng bố cục với thẻ M1, nên một shader dùng chung được.
  - `ff-f1-c2` (dải lặp x) gần nhất với vệt lửa Dragonhold anh khen.
  - Cả hai cần lót bồ hóng trên đá sáng. Có lót thì đọc tốt (hàng "light + ink").
- **G1:** `ff-g1-c2`. Đúng thứ được xin: cánh dài mảnh, lõi nhỏ sáng, quầng mềm, lớn lên mượt rồi tắt. Đây là mặt nạ trắng, nhuộm theo hệ (Metal xanh lam, Fire trắng vàng). Ở 12 px vẫn ra hình sao. `glint-gold-twinkle-set` (từ `ff-g1-c3`) là bộ biến thể cho các sao phụ.
- **A1:** `ff-a1-c5`. Đây là bản đầu tiên vừa đúng ba nét Brushfire vừa đúng chất lửa mềm hơi thật anh thích.
  - Clip không tự tách nét. Phần tắt là ăn mòn do Claude thêm vào; ăn mòn ở shader sẽ đẹp hơn.
  - `fire-brush-slash` (`ff-a1-c3`) giữ làm phương án cách điệu anime: sắc, nhanh, nhưng phẳng.
- **B2:** `ff-b2-c2`. Tia lửa thật, mượt, có hướng, nhưng màu cam đều, chưa có đầu trắng vàng, chưa có sao. Khoảng 7, chưa đạt. Dừng sau 4 lượt không lên điểm; cách tốt hơn ở §6.
- **B3:**
  - Mọi lượt B3 đều trượt sang lóa ống kính hoặc bokeh.
  - Sao lấp lánh đẹp nhất đêm nay là `glint-gold-twinkle-set` (từ `ff-g1-c3`), dùng được cho cả Fire.
  - `fire-gold-dust` (`ff-b3-c3`) là bụi vàng dư âm (FIRE_STYLE B: "bụi vàng lấp lánh"), khoảng 7.
- **C3:** `ff-c3-c3`. Vòng mảnh như tóc, có đoạn đứt, sao chạy trên vòng, đúng đề C3. Vòng không tự nở: shader cho nở và tắt. Trên đá sáng có lót mực thì quầng ngả nâu đục; nên giảm lót hoặc chỉ lót sát nét. `fire-halo-ring` (`ff-c3-c2`) là phương án lóe một lần có tia.

Không bản nào được nói là đạt 8,5. Thanh của anh chỉ tính ở bản dựng chơi, với hai giám khảo mù. Mấy bản ~8 ở trên là chỗ tốt nhất để bắt đầu dựng.

## 6. Giới hạn, việc chưa làm, cách tốt hơn

- **Chưa làm:** chưa giám khảo mù, chưa gắn vào lab (bước sau, agent khác), chưa xem trong bản dựng chơi. Hàng "lót mực" là giả định.
- **B2 dừng ở lượt 4:** Firefly cứ ra chùm tỏa đều 360°, hoặc tia lửa thật màu cam đều. Cách tốt hơn, theo thứ tự nên thử:
  1. image-to-video như A1 c5, với khung đầu là 2–3 chùm vệt có hướng, đầu trắng vàng, dựng từ chính `ff-b2-c2`;
  2. hạt Blender: chùm hình nón, trọng lực, vệt bằng motion blur, nhiệt dọc vệt;
  3. trong shader: dùng `fire-spark-spray` và đặt `tip-star-glint` nhuộm vàng ở đầu vệt sáng nhất.
- **A1 còn mở rộng được** bằng cùng cách image-to-video: hai nét, bốn nét, cong ngược, nhát ngang. Mỗi biến thể chỉ cần một khung đầu mới từ `crescent_frame.py`.
- **Lót tối:** mọi art additive (dải M1 và F1, sao, vòng, tia lửa) trắng xóa trên đá sáng nếu không có lót mực hoặc bồ hóng ở shader.
- **Atlas lớn:** atlas lớn nhất 2048 × 4096 (dải 32 khung 1024 × 256). Cần đo bộ nhớ và thời gian khung khi gắn; có thể giảm còn 16 khung hoặc ô 768.
- **Bài học Firefly** (nên ghi vào `game-art-pipeline/references/browser-ai-tools.md` §5; đêm nay không sửa vì ngoài phạm vi):
  - 1080p cộng trong suốt hỏng mà không báo;
  - khi một lượt hỏng, trình phát vẫn giữ clip cũ, nên phải so cỡ blob;
  - form POST trên trang chính cộng bộ nhận trả 204 gửi được, còn form vào iframe ẩn thì không;
  - trang mở sẵn model đối tác;
  - ô khung đầu nhận file qua `firefly-upload-with-crop#upload`.

## 7. Tệp

- **Atlas và JSON:**
  - `games/immortality-cultivation/art-src/lab/vfx/aura/`: `aura-metal-feather-mantle`, `aura-metal-windsilk`, `aura-metal-featherplates`, `aura-fire-flame-sheath`, `aura-fire-ribbon`, `aura-fire-fringe`, `tip-star-glint`, `glint-gold-twinkle-set`, `glint-starburst-set`;
  - `games/immortality-cultivation/art-src/lab/vfx/fire/`: `fire-crescent-sweep`, `fire-brush-slash`, `fire-spark-spray`, `fire-gold-dust`, `fire-twinkle-set`, `fire-halo-seal-loop`, `fire-halo-ring`.
- **Prompt, cài đặt, script, khung đầu A1 c5:** `.../source/firefly-overnight/` trong mỗi thư mục.
- **Tấm xem và video:** `games/immortality-cultivation/tmp/shots/overnight/firefly/`. Mỗi atlas có `<atlas>.sheet.jpg` và `<atlas>.preview.mp4`, cộng ba tệp tổng ở đầu tài liệu. Khung thô và ảnh chẩn đoán của Claude đã xóa.
- **Clip gốc:** `~/VFXLab/inbox/firefly/immortality-cultivation/overnight/<id>/`.
