# Phiếu 254 · Tu Tiên · Khung đầu cho áo khí Metal quanh kiếm (Wind-Silk Mantle) và vòng ấn lửa (Halo Seal)

> **TẠM GIỮ, KHÔNG CHẠY (04/11/2026).** Phiếu này chờ kết quả thí điểm 252 và phải viết lại theo bản phản biện 04/11 (các mục 3, 4, 9, 10, 11, 12, 15). Hai điểm chính:
> - **Vòng ấn** là ảnh tĩnh do shader xoay, nở, tắt; không đi qua Firefly Video (`VFX_PRODUCTION_PIPELINE.md` §4 mục 1: ấn cần nét chính xác). Sinh ảnh vuông 1024, hai vòng kẹp dải hoa văn cách nhau 15–20 % R.
> - **Áo khí Metal** gắn vào lưỡi kiếm, nên theo §0.2 là lưới mang texture cuộn. Ảnh vẽ chỉ làm texture, phải xem lại cách dùng trước khi vẽ.

**Nguồn và luật:**
- **Luật chung của đợt: mục "Luật chung của đợt 252–254" trong `docs/codex-queue/252-tt-first-frame-fire-impact.md`.** Mục đó gồm:
  - đường dẫn được ghi, các điều cấm;
  - tham chiếu được xem, gu của chủ dự án;
  - định dạng ảnh, Kiểm 1–7, giới hạn 3 lượt, cách báo hết hạn mức.

  Phiếu này chỉ ghi chỗ khác.
- Thiết kế đã chọn: `docs/games/tu-tien/skills/SWORD_AURA.md` §3.A "Wind-Silk Mantle". Chủ dự án chọn "A + sao mũi của C".
- Hai bài chấm đêm 04/11: `judge-1.md`, `judge-2.md` trong `games/immortality-cultivation/tmp/shots/overnight/`.

**Báo cáo:** `docs/codex-queue/254-report.md` và `docs/codex-queue/254/`. Model `gpt-6.1-sol`, mức `high`.

## Món 1: `metal-mantle` (áo khí bạc lam may quanh lưỡi kiếm), 3 biến thể

Bản tốt nhất đêm qua là `aura-metal-feather-mantle` (`ff-m1-c4`), được 7 và 6,5. Hai giám khảo khen tạo hình sang nhất, nhưng chê:
- áo **đặc và trắng**, đọc thành một chiếc lông vũ chứ không phải khí;
- áo sẽ che lưỡi kiếm thật, và trắng xóa trên đá sáng;
- hình gần đứng im.

Họ cần thân áo **trong suốt**, chỉ sáng ở mép và gân, có lấp lánh.

**Bố cục chung (như phiếu 253):**
- Trục kiếm trống nằm ngang giữa khung, dài khoảng 70 % bề ngang. Mũi bên phải, chuôi bên trái. Không vẽ kiếm.
- Hai hàng **mảnh khí sắc** xếp sát hai mép trục như lông vũ hay vảy, nghiêng về sau. Mép mỗi mảnh là **một đường sáng mảnh** bạc trắng; gân giữa mảnh xanh lam nhạt.
- **Thân mảnh gần như trong suốt:** chỉ một làn lam chàm rất mờ.
- Hai đường may của áo hội lại thành **mũi kim** sáng ở quá mũi kiếm một chút.
- Ở khoảng 25 % từ trái có một **khe cổ áo trống** (chỗ vòng ngọc của kiếm thật lộ ra). Mép áo ở khe cuộn nhẹ hình mây.
- Từ đầu trái, áo đổ ra thành **một dải lụa mảnh** bay về sau.
- Rải vài điểm lóe nhỏ dọc các mép sáng.

Màu: bạc trắng ở mép; lam bạc khoảng `#4F9ED9` (sắc khoảng 200°) ở gân; chàm rất mờ ở thân. **Không vàng, không ngọc bích, không xanh bạc hà, không xanh lục.**

| Biến thể | Ý riêng (EN) |
|---|---|
| `v1` | overlapping translucent qi plates like the feathers of a crane's wing laid flush along both edges of the empty blade line |
| `v2` | long slender qi blades like folded silk, layered in a staggered rhythm, their sharp edges catching light |
| `v3` | small scale-like qi plates close to the blade that grow longer and more feather-like toward the left end, where they release into the silk ribbon |

Câu chung ở cuối prompt:

> Each plate is glass-clear in its body, drawn only by a thin luminous silver-white rim and a faint pale silver-blue central vein, with a very faint indigo haze inside. The two hems meet in a bright needle point just past the right end. A small empty collar gap a quarter of the way from the left edge with softly cloud-curled hem edges, and one thin silk ribbon streaming off the left end. A few tiny sharp sparkles along the rims. Elegant, luxurious premium anime xianxia game effect; no gold, no jade green, no mint, no sword or metal drawn, the blade axis is empty. Pure black background, wide empty margins, no text, no frame.

Kiểm thêm:
- **Kiểm 8, thân trong.** Trong vùng bao của áo, điểm có luma ≥ 0,5 chiếm ≤ 25 % diện tích sáng (luma > 0,1). Áo phải là đường nét, không phải khối trắng.
- **Kiểm 9, màu.** Trung vị sắc (hue) của các điểm có độ bão hòa ≥ 0,2 nằm trong 185°–225°. Không có điểm nào bão hòa ≥ 0,3 với sắc 30°–160° (vàng, xanh lục).
- **Kiểm 10, khe cổ áo.** Ở cột cách mép trái của dải sáng 22–28 %, có một đoạn trống (luma < 0,1) dài ít nhất 40 % bề cao của dải.

## Món 2: `fire-halo-seal` (vòng ấn mảnh cho đòn lửa lớn), 3 biến thể

Chủ dự án chọn vòng Halo Seal mảnh, chỉ cho đòn lớn. Bản đêm qua `fire-halo-seal-loop` được 7 và 6,5, nhưng:
- chung chung, không có hoa văn ấn;
- ở cỡ chơi các vòng gộp thành một vành dày;
- có bốn vạch lạ trong lòng vòng;
- vòng hơi méo.

**Bố cục chung:**
- Một vòng tròn đúng, nhìn thẳng mặt, đường kính khoảng 70 % bề cao khung, ở giữa.
- 2–3 vòng đồng tâm **mảnh như sợi tóc**, cách nhau đủ rộng để ở 150 px vẫn tách được (khoảng cách ≥ 6 % bán kính).
- Mỗi vòng có **2–3 khuyết** hở rõ, các khuyết của các vòng so le nhau.
- Giữa hai vòng là **dải hoa văn ấn**: các vạch khắc đều, móc mây nhỏ, điểm ngọc nhỏ. **Không chữ, không chữ Hán, không ký tự.**
- Lòng vòng trống hoàn toàn.
- Màu theo lửa: viền trắng vàng, quầng cam hổ phách, chân son mờ. Không dùng vàng tiền `#FFC83A` làm màu chính.

| Biến thể | Ý riêng (EN) |
|---|---|
| `v1` | two hairline rings with a band of evenly spaced engraved ticks and tiny cloud-scroll hooks between them |
| `v2` | three hairline rings, the middle one carrying a sparse chain of small diamond-shaped jewel points |
| `v3` | two hairline rings joined by fine curving flame-feather strokes that run around the band like a woven seal |

Câu chung ở cuối prompt:

> A perfectly round seal halo seen straight on, made of hairline rings of white-gold light with a soft orange-amber glow, each ring broken by two or three clean open gaps placed out of step between rings. The centre is completely empty. Elegant, luxurious, premium anime xianxia game effect, radiant but delicate, a few tiny sharp sparkles on the rings. No letters, no characters, no symbols of any writing system. Pure black background, wide empty margins, no text, no frame.

Kiểm thêm:
- **Kiểm 8, tròn.** Fit đường tròn cho vòng ngoài. Sai lệch bán kính ≤ 1,5 % ở mọi góc.
- **Kiểm 9, lòng trống.** Trong 55 % bán kính tính từ tâm, không có điểm luma > 0,1.
- **Kiểm 10, vòng tách nhau ở 150 px.** Thu nhỏ còn 150 px rồi đo mặt cắt theo bán kính ở 8 góc. Phải thấy ≥ 2 đỉnh sáng tách nhau, có rãnh giữa tối hơn đỉnh ít nhất 35 %.

## Nhận
- Thư mục `metal-mantle/selected/` có 3 biến thể và `fire-halo-seal/selected/` có 3 biến thể, mỗi biến thể đủ ba file.
- Tấm xem `tmp/shots/codex-first-frames/metal-mantle-sheet.jpg` và `fire-halo-seal-sheet.jpg`.
- Báo cáo ghi số Kiểm 1–10, prompt từng lượt, điểm tự chấm, và biến thể nên đưa vào Firefly trước.
