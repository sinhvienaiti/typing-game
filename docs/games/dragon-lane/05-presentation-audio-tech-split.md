# Rồng Giữ Ải — 05. Trình bày, âm thanh, kỹ thuật và tách game (23/10/2026)

> **Dành cho:** chủ dự án; AI làm hình, âm, mã; AI tách TD và Sinh Tồn ra khỏi Space Typing.
> **Trạng thái:** thiết kế. Chưa sửa mã. Làm khi chủ dự án duyệt.
> **Dựa trên:** `research/*.md`; `01-core-combat-learning.md` (luật gõ, Rồng, chữ đặc biệt); `03-our-side-shop-traps-support.md` (cửa hàng, bẫy, nhà, lính);
> Space Typing `docs/td/TYPING_DEFENSE_DESIGN.md` mục 23–25, `docs/survival/SURVIVAL_MODE_PLAN.md` mục 5–8; repo cha `e7e0e049`, Space `b9d9bd79`.
> **Phạm vi:** luật và số nằm ở 00–04. Ở đây là **cách nhìn, cách nghe, cách xây**. Khi lệch về luật, tài liệu luật thắng; số chuẩn, bảng phím ở `00-canon.md`. Mọi số là số khởi điểm.
> **Bản sửa 23/10:** tách game và kế hoạch chuyển dời đã chuyển sang `../SPLIT_PLAN.md`; kế hoạch xây sang `DESIGN.md §9`; lưu, focus, cài đặt, màn ngoài trận sang `06-other-systems.md`. Phím theo bảng Mac của 00 §6. Bậc máy không đổi luật sim.

## 0. Tóm tắt

1. Tên chốt: **Rồng Giữ Ải** (EN *Dragonhold*, id `dragon-hold`). Rừng sương vẽ tay. Hỏa Long và Bạch Long đứng trên Bệ Rồng giữa rừng, chặn **Bầy Héo** (do sương Hắc Vụ gây ra) tràn tới qua 1–4 đường và từ trên trời.
2. Hai game tách ra có chủ đề riêng: **Lời Gọi** (TD, làng chữ sách tranh Việt) và **Tuyến Cuối** (Sinh Tồn). Hướng hình, vỏ UI, âm của hai game này: `../SPLIT_PLAN.md` §1.
3. Hình: **sa bàn 3D tranh vẽ** nhìn từ trên. Ramp 3 bậc, tán khối, sương theo bán kính, tone map Neutral. Nhân vật phóng 1,4 lần cho dễ đọc.
4. Chữ luôn rõ nhất: thẻ chữ và khung học là DOM trên canvas, không rung, không bị VFX che. Không bao giờ ẩn một chữ sống. Phản hồi đi qua **`kit/feedback`** (bậc T0–T5, dừng hình không nuốt phím).
5. Mỗi lớp quái, bẫy, nhà, lính có bộ hình và bộ âm riêng. Báo trước luôn đỏ, luôn đủ lâu. Âm có 12 bus, nhạc 4 lớp, phát âm từ luôn thắng. Ngân sách High: 300 quái, ≤ 150 draw call, p95 ≤ 12 ms.
6. Kỹ thuật: **mỗi game một repo** (submodule). Mã dùng chung ở **`shared/game-kit`**, chép vào `src/kit/` bằng `kit:sync` có kiểm sha256. Kit được chép **từ** Space; Space giữ bản gốc, chưa chuyển sang shim (00 D17).
7. Kế hoạch xây theo mốc có cổng: `DESIGN.md §9`. Tách game: `../SPLIT_PLAN.md`. Bản thử dọc chạy song song với việc tách, nhiều agent mỗi làn.

## 1. Tên và chủ đề

### 1.1 Ba game mới bên cạnh Space Typing

| | Space Typing (giữ) | **Rồng Giữ Ải** | **Lời Gọi** (TD) | **Tuyến Cuối** (Sinh Tồn) |
|---|---|---|---|---|
| EN, id | Space Typing, `space-typing` | Dragonhold, `dragon-hold` | Wordwoven, `typing-defense` | Last Line, `typing-survival` |
| Cổng, host | 3004, `space.` | 3005, `dragon.` | 3006, `td.` | 3007, `survival.` |
| Bối cảnh | Phiêu lưu qua 8 thế giới sao | Đại Ngàn Sương: rừng thông, sông, tán tím lam | Miền Văn Điền (TD 22.1): ruộng bậc thang, làng tre, đèn giấy | Xem `../SPLIT_PLAN.md` §1.3 (chủ dự án chọn giữ khoa học viễn tưởng hay bỏ hẳn) |
| Góc nhìn | Ngang, cuộn | Trên xuống 55°, xoay tự do, Rồng ở giữa | Trên xuống 55°, kéo bản đồ | Hành lang cố định, bến súng ở đáy |
| Bảng màu | Neon vũ trụ | Lục rêu, lam thông, tím tán, kem nắng | Xanh mạ, vàng lúa, nâu tre, đỏ son | Thép tối, cam nóng, lam điện |
| Vỏ UI | Kính sci-fi | Gỗ khắc, vỏ cây sẫm, viền rêu | Giấy dó, mực, đèn lồng | Thép, sọc cảnh báo, đèn LED |
| Font tiêu đề | (hiện có) | Cormorant Garamond 700 | Baloo 2 (kiểm bộ dấu) | Chakra Petch 700 |
| Nhạc | Điện tử vũ trụ | Dân ca rừng giả tưởng: sáo gỗ, đàn hạc, cello, trống khung, hợp xướng | Dân gian Việt: sáo trúc, đàn tranh, trống | Industrial: synth, trống máy, bass |

- Font trong trận của cả 4 game là **Be Vietnam Pro**. **Màu ngữ nghĩa** dùng chung (mục 2.2). Mọi thứ khác là riêng.
- Tên "Rồng Giữ Ải" lấy mặc định của 01 mục 8. "Ải" vừa là cửa ải, vừa là màn chơi. Thư mục `docs/games/dragon-lane/` chuyển vào repo game ở M1 (DESIGN.md §9).

### 1.2 Thế giới

- **Đại Ngàn Sương:** rừng cổ trong sương sớm. Mỗi sinh vật có một tiếng gọi là tên thật. Rồng gọi đúng tên thì lời thành lửa, gió, khiên.
- **Bầy Héo:** sương **Hắc Vụ** (tím xám, không phát sáng) trào lên từ khe núi; cơn Héo làm sinh vật quên tên. Một **vỏ Héo** xám tro, nứt ánh vàng úa `#C8D24A`, phủ lên chúng. Hạ quái là vỡ vỏ, một đốm sáng nhỏ bay về rừng. **Không máu, không xác.** Vỏ Héo là lớp vật liệu chung; prompt ảnh 2D của mọi quái có cùng dòng MATCH (02 §1.1, 00 D02). Hắc Vụ là lớp cảnh của Hồi III (04 §2.2) và là boss cuối B20.
- Chương đi từ rìa vào sâu theo 8 kit gốc (`art-pipeline.md` mục 9). **Văn hóa:** giữ luật TD 22.1 (không đền, chùa, miếu, vật thờ).

### 1.3 Hai Rồng trên sân

| | **Hỏa Long** | **Bạch Long** |
|---|---|---|
| Model | `heroes/draconis-v2` (22.000 tam giác). Viêm Đế đổi tạm sang `draconis-v3` bản medium | `guides/draconis-v4` (31.226 tam giác) |
| Chỗ | Bay lượn 2,5 m trên Bệ Rồng (bán kính 4 m), quay đầu về quái đang khóa | Đứng trên bệ, quay về đường đông quái nhất |
| Clip dùng | Idle_Hover, Attack_L/R/Both, Cast, Boost, Hit, Death, Victory, Intro; v3: Spit, Spit_Big | Guide_Idle, Wave, Flap, Hop, Bow, Talk |
| Thiếu | Không | Hit, Down, Rise (01 mục 8). Thêm Cast nếu làm được. Blender trên lưới có sẵn |
| Tạm khi thiếu | — | Hit → chớp shader; Down → Guide_Bow giữ khung; Rise → Guide_Hop |

- Hỏa Long hết máu là **thua ải** (01). Thanh máu Hỏa Long vì vậy to nhất ở HUD.

## 2. Hướng hình

### 2.1 Phong cách

- **Sa bàn tranh vẽ** như ảnh mẫu: khối mềm, tán gom cụm tròn, nét cọ to trên đất, nắng dịu xiên, sương lam ở rìa.
- Shader chung (`art-pipeline.md` mục 4): ramp 3 bậc, pháp tuyến cầu cho tán, rim 10–15 %, bóng có màu, sương theo bán kính, `NeutralToneMapping`, LUT theo kit và giờ, bloom ngưỡng cao chỉ cho phép và lửa.
- **Bậc nổi:** thẻ chữ, khung học → báo trước đỏ → quái, Rồng, lính → bẫy, nhà → cảnh (giảm tương phản 10–15 %) → đất → đường (sáng hơn đất một bậc).
- **Bài nheo mắt** (TD 23.1) cho mọi ảnh duyệt. Cây lớn, đá lớn, mốc: Tripo không rig. Cỏ, hoa, sỏi, phông xa: tranh 2D. Làm bài A/B cây trước khi nhân bản kit.
- Ô đặt (03: `trap`, `house`, `block`) **không vẽ vào đất**. Chúng chỉ hiện khi đang đặt hoặc khi nghỉ đợt (mục 4.5). Đúng ý chủ dự án "bản đồ không lộ bệ".

### 2.2 Màu

| Màu ngữ nghĩa (kit, chung 4 game) | Mã | Nghĩa | Cấm dùng cho |
|---|---|---|---|
| Đỏ | `#FF4A4A` | Nguy hiểm từ địch: báo trước, vùng nổ địch, gạch "gần" trên thẻ | Lá, hoa, giá không đủ tiền, phép phe ta |
| Cam | `#FFB020` | Khẩn: Từ Ngắt, bẫy sắp hỏng, lính sắp ngã | Lá gần đường |
| Vàng kim | `#FFC83A` | Vàng (tiền), rơi đồ | Khung thẻ tinh anh, phép |
| Xanh ngọc | `#7FF5E0` | Sức gõ: chữ đã gõ, đòn mạnh nhờ gõ chuẩn, Từ Kích | Nước gần đường, tán lá |

- **Màu riêng.** Phe ta: lửa Hỏa Long cam đào; phép Bạch Long kem trắng, lông vũ; bẫy gỗ nâu, dây leo lục; nhà ánh lam nhạt. Bầy Héo: vỏ xám tro, khe nứt vàng úa `#C8D24A`. **Hào quang tướng địch: nền vàng úa (màu phe Héo)** và hoa văn, icon riêng cho mỗi loại buff (kiếm, khiên, chân gió, lá, xích, mắt, thoi, trống; 02 §1.5). Không dùng đỏ, cam, vàng kim, xanh ngọc cho hào quang. Cảnh: tán tím `#8E7CC3` và lam `#6C8FD1` đặt xa đường; sông ngọc sẫm, giảm bão hòa gần đường.

### 2.3 Tỉ lệ

Nhân vật phóng **1,4 lần** so với cảnh, vùng chơi 28–32 m (01 mục 2.1). Đích ở 1080p, camera mặc định: quái bầy ≥ 26 px; quái thường 32–44 px; quái to 46–60 px; tướng địch ≥ 60 px; boss 140–220 px; lính 34–46 px; Hỏa Long 80–100 px; Bạch Long 60–70 px; nhà 70–100 px; bẫy 30–50 px. Kịch bản `dh-scale.mjs` đo hộp bao, lệch quá 20 % thì báo lỗi.

## 3. Camera

- Phối cảnh, FOV dọc 30°, luôn nhìn về Bệ Rồng, kéo trong vùng chơi + 8 m. Mặc định 55°.
- Chuột phải kéo dọc để nghiêng 40–75°, kéo ngang để xoay tự do 360°. Lăn chuột zoom 0,6–1,3 lần. Nút "về hướng chuẩn". Bàn phím (00 §6): mũi tên xoay và nghiêng, Alt + ↑ / ↓ zoom, Alt + 0 về chuẩn, bấm lại là toàn cảnh 75°. Không dùng F1, F2 (Mac). Chữ cái chỉ để gõ. Đảo chiều và độ nhạy ở cài đặt (06 §3).
- **Không bao giờ tự chạy giữa đợt.** Boss ra mắt dùng khung nhỏ 320 × 180 góc trên phải 2,5 s.
- Rung ≤ 12 px, chỉ trên canvas. Cây, mốc che đường hoặc quái có chữ thì dither 35 %. Rìa: đất kéo thêm 40 m, rừng impostor dày, sương bán kính, vignette nhẹ.

## 4. UI và HUD

### 4.1 Luật chung

- `--ui = clamp(0,8; min(rộng / 1600; cao / 900); 1,2)`. Hỗ trợ 1280 × 720 tới 2560 × 1440, DPR 1 và 2. HUD trong đợt ≤ 10 % diện tích; nghỉ đợt ≤ 15 %; thẻ chữ ≤ 6 %.
- UI là DOM, icon vẽ tay từ Codex; thiếu ảnh thì dùng icon vẽ bằng canvas. **Phím: bảng duy nhất 00 §6.**
- **Focus** (game chạy trong iframe portal): luật ở 06 §2. Trong trận không có thẻ `input`; mọi phím đi qua một router ở `window`, pha capture. Nút DOM có `tabindex=-1` và chặn `mousedown` để không lấy focus.

### 4.2 HUD trong đợt

| Thành phần | Vị trí | Cỡ (`--ui` = 1) | Nội dung |
|---|---|---|---|
| Trận | Trên trái | 320 × 60 | Vàng, Đợt n/N, Chuỗi |
| Đợt kế / boss | Trên giữa | 420 × 48 / 560 × 34 | Thẻ đợt kế (đường, họ quái, tướng địch, quái bay, nút Gọi sớm); khi có boss là thanh máu chia pha, Cụm Ấn ngay dưới |
| Hệ thống | Trên phải | 4 × 40 × 40 | Dừng, cài đặt, camera, âm |
| Hai Rồng | Dưới trái | 360 × 80 | Chân dung, máu (Hỏa Long to nhất), khiên; 4 ô kỹ năng có Chữ Chiêu; thanh Long Nộ và 2 ô Tối Thượng |
| **Khung học** | Dưới giữa | 480 × 88 | Mục 4.4; chip Từ Khẩn bám mép trên |
| Bộ Mang Theo | Dưới phải | 420 × 56 | Dải món (03 mục 4.2): icon, giá, phím; đồ tiêu hao |
| Chip mép | Mép màn | 36 × 36 + thẻ | Quái có chữ ngoài khung nhìn: chip mang từ, mũi tên (01 mục 3.1) |

- Tổng ≈ 9,7 % diện tích ở 1600 × 900 (thẻ đợt kế và thanh boss không hiện cùng lúc).
- Thanh máu: quái có chữ dùng vạch 3 px dưới thẻ (01); quái không chữ dùng lô instanced, chỉ hiện khi mất máu; lính lam; nhà hổ phách khi bị thương.

### 4.3 Thẻ chữ trên đầu quái

Luật gán chữ, ngân sách chữ (00 §5), chữ đầu duy nhất: theo 01 mục 3.2–3.3. Phần dưới đây là cách vẽ.

- **Thẻ:** nền vỏ cây sẫm `#231C17` độ đục 90 %, chữ kem `#FFF4D6`, viền 1,5 px, bóng cứng. Be Vietnam Pro 700, chữ thường; chữ đầu 800 có gạch chân. 20 px ở 1080p, ≥ 16 px ở 720p, nhân cỡ người chọn 80–150 %. Tương phản ≥ 7 : 1. Rộng tối đa 220 px. Dòng nghĩa: ≥ 15 px, tối đa 22 ký tự, tối đa 4 thẻ mang nghĩa (01 §3.1).
- Quái chưa có chữ: một **chấm mờ** trên đầu. Khi được gán chữ, chấm bật thành thẻ. Chữ bị ẩn: chip "• • •" (01 §3.3).
- Mỗi loại thẻ có **hình khung và icon riêng**, không chỉ khác màu (người mù màu đỏ–lục khó tách cam, xanh lá, đồng).

| Loại (01 mục 3.6) | Khung | Icon |
|---|---|---|
| Quái thường | Nền tối trơn | — |
| Tinh anh | Viền **đồng** `#D08A4E` | Vương miện nhỏ |
| Tướng địch | Khung bạc, huy hiệu, chấm chuỗi Ấn Phá, ≤ 2 icon hào quang đang phát | Huy hiệu |
| Bộ phận boss | Viền **tím than** dày; chỉ đổi đỏ khi bộ phận đó đang báo đòn | Vòng ngắm |
| Từ Ngắt | Cam, nhấp nháy theo thanh niệm; **giảm chuyển động**: vòng đếm lùi, không nhấp nháy | Tia chớp |
| Từ Trợ | Xanh lá `#6CCB5F`, trên lính hoặc bẫy được cứu | Chiếc lá |
| Từ Kích (03 mục 10.3) | Nhỏ hơn, viền xanh ngọc, không rung, trên bẫy | Bánh răng |
| Từ Hỏi Nghĩa / Từ Nghe | Dòng nghĩa nghiêng + chữ đầu + số ô / icon loa + chữ đầu + số ô (04 §5.4) | Dấu hỏi / loa |
| Cụm Ấn boss | Dải lụa rộng dưới thanh boss, đồng hồ lớn, ô trả lời | — |

**Bộ xếp (view, ≤ 0,3 ms mỗi khung cho 20 thẻ):** neo ở socket đầu + 0,4 m, chiếu ra màn hình. Đặt theo ưu tiên của 01. Chồng nhau thì thử lần lượt: đẩy ngang ≤ 120 px → nâng ≤ 3 bậc 34 px kèm vạch nối (01) → chỉ **khung** thu 85 %. **Chữ đầu và từ không bao giờ mờ, không bao giờ ẩn**; tương phản 7 : 1 giữ ở mọi bước. Thẻ giữ chỗ ≥ 0,5 s để không nhảy. Vùng cấm: HUD, khung học, dải dưới thanh boss. **Mặt nạ vùng yên** (TD 23.4): hạt cộng màu quanh thẻ giảm 60 %.

**Vòng khe quanh Bệ Rồng** (mọi đường dồn về giữa, Hỏa Long cao 80–100 px che khuất): quái trong 10 m không neo thẻ trên đầu mà dùng **8–12 khe góc cố định** xếp vòng quanh bệ, theo hướng quái tới, kèm vạch nối về quái. Khe không đổi chỗ khi quái nhích. Không đặt Từ Kích, Từ Trợ trong 10 m quanh bệ.

- **Hiện:** bật 0,6 → 1,06 → 1 trong 0,15 s, bụi lá, "tách" rất nhỏ. **Khóa:** ×1,1, luôn trên cùng, quái viền sáng, Hỏa Long quay đầu.
- **Phím đúng:** chữ chuyển xanh ngọc, nảy 2 px, một đốm lửa chạy từ mõm Hỏa Long tới quái. **Phím sai:** thẻ rung ±3 px 120 ms, nền chữ kế hồng nhạt 0,15 s, tiếng "tóc" đục, không còi.
- **Xong:** chữ bung 6–10 hạt chữ cái bay theo đòn. **Quái chết khi đang gõ dở:** thẻ gập 0,2 s, khóa nhả, phím kế không mất.

### 4.4 Khung học

- DOM dưới giữa, ngoài canvas: **không rung, không hậu kỳ, không bị số đè**. Khi khóa: từ 32 px (phần đã gõ xanh ngọc), IPA 18 px, nghĩa 18 px, icon loa, chấm độ thuộc; IPA và nghĩa hiện theo 01 mục 6.3.
- **Hàng đợi có ưu tiên** (01 §6.3): xong từ mới hoặc từ độ thuộc < 40 thì ghim "từ · nghĩa ✓" ≥ 2,5 s; từ khác giữ 0,8 s; từ "Thuộc" không vào khung. Dòng nhỏ **"Vừa học"** dưới khung giữ 3 từ mới gần nhất. Tab nghe lại (01). Cuối ải: **Sổ Từ** (từ đã gặp, từ sai, nút nghe) trong màn tổng kết.
- **Font IPA:** Be Vietnam Pro bản `@fontsource` thiếu gần hết glyph IPA (ɡ ʊ ɹ ŋ ʌ ə ɪ ˈ ɔ ɑ θ ʃ ʒ ɛ ː). Dòng IPA khai một font có đủ IPA trước (Noto Sans bản có IPA, hoặc Charis SIL qua `@fontsource`), rồi mới tới Be Vietnam Pro. Kiểm bằng ảnh chụp khung học với 20 mẫu IPA (`dh-learning-frame`).

### 4.5 Cửa hàng, Xưởng Rồng, đặt món

Theo nhịp của 03 mục 4.1. Cách vẽ:

- **Chuẩn Bị (trước ải):** toàn màn, 3 cột. Trái: ảnh khung bản đồ và thẻ báo cả ải. Giữa: lưới món, kéo vào Bộ Mang Theo (6–10 ô). Phải: ô trang bị hai Rồng (03 mục 5.1), đồ tiêu hao, mức khó. **Bàn phím:** mũi tên chọn, Enter thêm hoặc bỏ món, Tab đổi cột, Esc lùi (00 §6).
- **Nghỉ đợt, trong đợt:** **không mở bảng lớn**, bản đồ luôn thấy. Dải Bộ Mang Theo và vòng menu tại ô; món khắc chế đợt kế có viền sáng. **Thẻ Ôn** (đã gộp Chợ Học): thẻ nhỏ trên giữa khi nghỉ đợt; phím 1 / 2 / 3 cho câu chọn nghĩa. Bảng chọn Long Ấn: 3 thẻ, phím 1 / 2 / 3.
- **Xưởng Rồng (ngoài ải):** màn riêng trong Làng Rồng, trang bị cố định và cấp món, giá bằng Vảy Rồng (06 §4).
- **Thẻ món:** icon 64 px, tên, giá, 2–3 chip chỉ số, chip "Khắc chế", lý do khóa. Không đủ tiền: giá xám, viền vàng mờ. **Không dùng đỏ.** Rê chuột: chỉ số trước và sau khi nâng, ảnh động nhỏ của hiệu ứng.

| Bước đặt | Hình |
|---|---|
| Chọn món hoặc bấm ô trống | Mọi ô hợp lệ hiện trên đất: ô bẫy là vạch sáng ngang đường; bệ nhà là vòng rune tròn; điểm giữ là cờ cắm. Ô không hợp lệ không hiện |
| Rê lên ô | Bóng ma model mờ 60 %, viền xanh ngọc; decal vòng tầm đúng bán kính; đoạn đường bị phủ sáng lên; số quái dự kiến qua trong đợt kế |
| Xác nhận | Chuột trái hoặc Enter (bàn phím: số 1…9 chọn món, mũi tên đổi ô, Enter đặt; 00 §6). Esc hoặc chuột phải hủy |
| Dựng 2 s (03) | Thanh tiến trên ô, bụi đất, lá bay; cỏ trong chân đế dạt ra |
| Nâng, bán | Vòng menu; bàn phím: Backquote vào chế độ sửa, `=` nâng (2 lần), `-` bán (2 lần). Số Vàng hoàn hiện trên nút. Chỉ lúc nghỉ (03 §0.1) |
| Lính chặn | Dây giữ 4 m vẽ mờ quanh điểm; 1–3 chấm khiên trên đầu là số suất chặn |

### 4.6 Báo đợt và trợ năng

- Nghỉ đợt: mỗi đường có cờ ở mép rừng với icon họ quái, số con, huy hiệu tướng địch. Đường bay vẽ nét chấm trên không. Đầu đợt: banner 1,2 s "Đợt 7 · 3 đường · có tướng địch", tiếng tù và rừng.
- **Trợ năng:** rung 0–100 %; giảm chuyển động (tắt cả nhấp nháy Từ Ngắt); cường độ lóe; tắt tách màu; mật độ hạt; số sát thương bật, tắt hoặc chỉ số lớn; cỡ thẻ và khung học; ẩn hiện IPA và nghĩa; âm lượng phát âm riêng; hoa văn mù màu; phụ đề âm; **chế độ khay**. Bảng cài đặt đầy đủ với giá trị mặc định: 06 §3.
- **Chế độ khay:** một dải riêng rộng hết màn, nằm ngay trên HUD đáy (không nhét trong khung học 480 px): 2 hàng × 8 chip, xếp theo đe dọa. Mỗi chip có từ, mũi tên chỉ hướng quái và số mét. Chip đang khóa thì quái tương ứng sáng viền. Bỏ thẻ trên đầu quái, chỉ giữ chấm màu.

### 4.7 Màn ngoài trận

Tiêu đề, chọn hồ sơ, bản đồ Hành Trình 520 nút, Làng Rồng (Hang Rồng, Thư Viện Rồng, Xưởng Rồng), kết ải, màn thua, menu tạm dừng, cài đặt, màn nạp, Sổ Quái, Sổ Món, Sổ Từ, Sổ Trang Bị, chọn Lời Thề và Vương Miện: danh sách, sơ đồ đi giữa các màn, bố cục theo vỏ gỗ khắc, đường bàn phím và kịch bản kiểm `dh-meta-screens` ở **06 §4**.

## 5. Phản hồi chiến đấu (`kit/feedback`)

Sim phát sự kiện ngữ nghĩa: `KEY_OK`, `KEY_BAD`, `WORD_DONE{quality}`, `HIT{tier,pos,dir,dmg,quality,material}`, `KILL{class,material}`, `TRAP_FIRE{kind,count}`, `HOUSE_PULSE`, `DRAGON_HIT`, `BOSS_PHASE`, `ULT`. Kit đổi sự kiện thành hình và tiếng theo **hồ sơ `dragon`**. Luật không biết có bao nhiêu hạt.

| Bậc | Khi nào | Trauma | Dừng hình | Hạt | Số | Tiếng |
|---|---|---|---|---|---|---|
| T0 | Phím đúng | 0 | 0 | 2–3 đốm lửa | — | Phím |
| T1 | Đòn Tốt, Vừa; bẫy liên tục; Xung nhà | +0,03 | 0 | Tia nhỏ | Nhỏ 0,45 s | Đầu nhọn + thân |
| T2 | Hạ quái thường; bẫy nổ ≤ 4 con; từ cụm bầy | +0,08 | 12 ms | Sao 8 tia, vụn chất liệu | Vừa | + trầm ngắn |
| T3 | Chớp, Hoàn hảo; Phun Lửa, Thiên Hỏa, Gió Cuốn; bẫy giam | +0,16 | 35 ms | Sóng tròn, mảnh vỡ | To, "HOÀN HẢO" | + trầm |
| T4 | Hạ tướng địch; bẫy nổ ≥ 8 con; đủ chuỗi bẫy; Long Hống | +0,30 | 45 ms | Sóng kép | To, gộp | + đuôi vang |
| T5 | Tối Thượng; boss đổi pha; phá bộ phận boss | +0,55 | 70 ms | Vòng chữ, lóe, tách màu 60 ms | Rất to | Riêng, câu nhạc |

- **Dừng hình** chỉ làm thế giới chậm (tốc 0,05). Thẻ, khung học, HUD vẫn chạy. Chỉ từ T2; hai lần cách ≥ 150 ms; quét ≥ 30 con trong 0,5 s thì một lần 25 ms.
- **Phím không bao giờ bị nuốt.** Phím vào lõi gõ ngay. Đòn của từ vừa xong xếp hàng, bắn khi thế giới chạy lại (≤ 70 ms). Hợp với luật xếp hàng đòn khi Rồng bị choáng của 03 mục 2.2.
- **Trauma:** rung = trauma², ≤ 12 px; xung có hướng 2–6 px, lò xo 120 ms. Hỏa Long bị đánh: viền màn tối 120 ms, không nhòe chữ.
- **Số:** WebGL instanced, một atlas. Gộp theo mục tiêu 150 ms; sát thương nhịp gộp 0,3 s ("×6"). Né khung học, thẻ, thanh boss. **Không có chí mạng ngẫu nhiên** (00 D03). Đòn Chớp, Hoàn hảo: số to hơn, trắng viền xanh ngọc. Đòn bẫy, lính: số nhỏ, kem. Không dùng vàng kim cho số (vàng kim là tiền).
- **Phản ứng quái** (thuộc tính instanced, không thêm draw call): lóe 1–4 khung, giật lùi giả theo lò xo, co giãn 0,91 / 1,07 trong 120 ms, lắc choáng từ T3. Tướng địch, boss, lính (SkinnedMesh) chơi thêm clip `Hit`.
- **Mảnh vỡ** theo chất liệu (mục 6.3), nằm trên đất 6 s. Chết hàng loạt: một vụ nổ cỡ √N cho N con cùng chỗ.

## 6. VFX và CGI theo thực thể

**Ngữ pháp một đòn:** lên đòn (lóe nhỏ ở nguồn) → phát (lóe miệng) → bay (đạn instanced, ribbon chung) → trúng (lóe 60 ms, hình chính, mảnh chất liệu, tiếng nhiều lớp) → dư âm (khói, vết cháy decal, lá rơi). Đòn mạnh nhờ chữ có đầu đạn xanh ngọc và vệt là chính các chữ cái của từ. Báo trước của phe ta (Thiên Hỏa) màu cam nhạt viền trắng, không bao giờ đỏ.

### 6.1 Hai Rồng (kỹ năng theo 01 mục 2.4)

| Việc | Clip | Hình | Bậc | Tiếng |
|---|---|---|---|---|
| Đòn gõ | Attack_L/R xen kẽ; Attack_Both khi Chớp, khi hạ quái Vừa trở lên, hoặc quái trong 6 m | Cầu lửa `skills/dragon-fireball` 18 m/s, ribbon chữ cái, nổ 1,5 m | T1–T3 | Phụt, vút, nổ |
| Lửa Chữ (nội tại) | — | Quái bị đốt có ngọn lửa nhỏ trên lưng, số nhịp | T1 | Lửa lách tách |
| Phun Lửa | Attack_Both | Nón 60° dài 12 m, lửa cuộn theo gió, đất cháy decal | T3 | Gầm + lửa xèo |
| Thiên Hỏa | Cast | Bóng báo 0,8 s, khối lửa rơi, vòng 4 m, sao choáng | T3 | Rít rơi, nổ trầm |
| Viêm Đế | Intro (lửa che 0,3 s đổi model) → Spit; kết Spit_Big | Mỗi từ một tia xuyên 2 × 22 m dọc đường; kết nổ 7 m | T5 | Câu nhạc riêng |
| Khiên Lông Vũ | Guide_Bow | Vòm lông vũ kem trong suốt trên Hỏa Long và lính; chớp khi đỡ | T2 | Chuông gió |
| Gió Cuốn | Guide_Flap | Vòng gió 9 m, lá xoáy, quái trượt lùi; quái bay rơi xuống | T3 | Gió giật |
| Lời Thề Bạch Vũ | Guide_Talk → Guide_Wave | Vòng lông vũ 20 m; hào quang địch vỡ "kính"; phe ta sáng | T5 | Hợp xướng |
| Thầy Rồng, Từ Trợ | Guide_Wave | Dải sáng từ tay Bạch Long tới đích, lá non mọc | T1 | Đàn hạc |
| Long Hống (Từ Khẩn) | Boost / Guide_Flap | Sóng gầm 10 m, quái văng 6 m | T4 | Gầm lớn |
| Bạch Long chặn, đánh trả | Guide_Idle + Flap ngắn | Khiên lông nhỏ khi đỡ, vệt cánh quét | T1 | "Phạch" |
| Bị đánh / kiệt sức / thắng | Hit / Death, Bow giữ khung / Victory, Hop → Wave | Viền đỏ 80 ms, vảy hoặc lông bay / đáp xuống bệ / xoay 3 s | — | Gầm đau, thở dài, kèn thắng |

### 6.2 Quái theo lớp

Mọi báo trước **đỏ**, vạch đầy dần, **≥ 0,5 s**. Báo đòn boss theo công thức của 01 mục 3.6 (tối thiểu 4 s).

| Lớp | Di chuyển | Đòn | Báo trước | Trúng đòn | Chết |
|---|---|---|---|---|---|
| Bộ binh cận chiến (2 chân) | Đi, chạy khi < 8 m | Chém quạt 90° | Cung đỏ dưới chân 0,5 s | Giật lùi, `Enemy_Hit` | Ngã, vỏ vỡ |
| Xạ thủ (2 chân) | Dừng ở Vòng Bắn | Bắn gai, tên, đá | Tia ngắm đỏ 0,6 s | Lùi một bước | Ngã ngửa |
| Thú xung kích (4 chân) | Phi nước đại | Húc, đẩy lính | Vạch đỏ thẳng + bụi chân 0,6 s | Trượt chân | Lăn, bụi |
| Thú bầy (4 chân) | Lúp xúp theo bầy | Cắn nhanh | Không (sát thương nhỏ) | Chùn | Tan nhanh |
| Bay quấy | Lượn 3–6 m, đốm bóng nhỏ dần | Bổ nhào | Vòng đỏ dưới đất 0,5 s | Chao cánh | Rơi xoáy |
| Nổ cảm tử | Lăn, bò | Tự nổ 2,5 m | Phồng, nhấp nháy đỏ 0,8 s | — | Chết trước: xì hơi vô hại |
| Phá bẫy | Đi cạnh đường | Gặm bẫy, cắt dây | Icon búa trên thẻ, bẫy rung | Lùi | Ngã |
| Pháp sư Héo | Đứng sau đội | Hồi, buff | Thanh niệm + Từ Ngắt | Ngắt phép, lóe | Tan sương |
| Tướng địch | Đi giữa đội, mang cờ | Đòn riêng + hào quang | Vòng hào quang trên đất; chiêu: cột sáng màu hào quang, tên chiêu 1 s | `Hit` thật | Đốm sáng lớn, câu nhạc; mọi hào quang tắt kèm tiếng "vỡ kính" |

- Quái nhận hào quang: rim màu hào quang 20 %, icon trên thẻ. Lần áp: xung vòng từ tướng địch, trống ngắn.
- Giam, chậm, đẩy, đóng băng: thuộc tính instanced (màu, rung, nghiêng). Không đổi clip.

### 6.3 Chất liệu (tiếng trúng → cách chết)

Lá héo "xào" → bung lá vàng úa · Gỗ mục "cộp" → nứt dọc, dăm gỗ · Đá rêu "cộc" → vỡ khối · Lông thú "thịch" → lông bay, khói hồn · Vỏ côn trùng "rắc" → mảnh vỏ bóng · Hồn sương "vút" thủy tinh → tan sương · Bùn đầm "bọp" → sụp thành vũng 4 s · Pha lê Héo "keng" → mảnh vàng úa lấp lánh. Mọi cái chết kết thúc bằng một đốm sáng nhỏ bay về rừng.

### 6.4 Boss

| Nhịp | Hình | Âm |
|---|---|---|
| Ra mắt | Khung nhỏ 2,5 s, `Boss_Intro`; rừng rung, chim bay | Gầm + câu mở |
| Báo đòn, Cụm Ấn | Decal đỏ đúng cỡ, vạch đầy dần; dải Cụm Ấn dưới thanh máu | Rít báo, nhạc −3 dB |
| Đổi pha (ngưỡng theo 02 §4.3) | T5; vạch máu vỡ; sóng đẩy cảnh; LUT và sương đổi trong 1,5 s | Nhạc sang stem pha ở ô nhịp kế |
| Buff quân theo pha (02 §4.5) | Cột sáng vàng úa ≥ 1 s, icon buff hiện trên thẻ quân | Gầm, trống ngắn |
| Phá bộ phận | Bộ phận vỡ thành mảng, mất kiểu đánh tương ứng | "Rắc" lớn |
| Chết | Chậm 0,4 s, vỏ Héo nứt từng mảng, đốm sáng lớn, rừng sáng lại | Kết boss |

### 6.5 Bẫy (03 mục 7) theo lớp hình

| Lớp | Bẫy | Chờ | Kích, tác dụng | Nạp lại |
|---|---|---|---|---|
| Liên tục | Gai Chông, Bùn Lầy | Gai nhú, mặt bùn sủi | Gai trồi theo nhịp; chân quái dính bùn, bước chậm | — |
| Nổ | Mìn Ấn, Bom Hạt Thông | Rune mờ dưới đất; quả thông thở | Lóe, cột lửa hoặc nhựa, sóng tròn đúng bán kính, T3–T4 | Vỏ rỗng, vòng đồng hồ |
| Đẩy, kéo | Cọc Bật, Hố Gió | Khúc gỗ nằm; xoáy lá nhẹ | Cọc bật quái văng; xoáy hút về tâm | Cọc dựng lại |
| Giam | Lưới Dây Leo, Lồng Đá, Lưới Phóng | Dây leo ẩn; khung đá; trụ có cuộn lưới | Rễ bọc, lồng đá trồi; lưới kéo quái bay xuống | Rễ rút xuống |
| Khống chế vùng | Nấm Độc, Ấn Băng | Mũ nấm; rune sương | Mây bào tử 6 s; khối băng bọc quái | Nấm nhú lại |
| Trụ đánh | Cột Sét | Cột có cuộn dây | Tia sét nhảy 5 con | Cuộn sáng dần |

- Chuỗi bẫy (03 mục 7.4): mỗi mắt xích nối một sợi sáng tới mắt xích kế, nốt đi lên; đủ chuỗi là T4.
- Cộng Hưởng (03 mục 10.2): đòn từ rút giờ hồi của bẫy thì một tia xanh ngọc nhỏ bay từ quái vào bẫy. Chuỗi phe ta (03 mục 10.4): vệt sáng chạy dọc các ô bẫy và bệ nhà, đổi màu theo bậc.

### 6.6 Nhà và lính (03 mục 8–9)

| Nhóm | Ví dụ | Chờ | Hoạt động | Hỏng, ngã |
|---|---|---|---|---|
| Hào quang | Cột Chậm, Chuông Gió, Đài Khuếch Chữ | Rune thở chậm | Vòng tầm sáng; Xung khi đủ 5 Năng: sóng vòng | Nứt, khói, ánh tắt dần |
| Hồi, khiên | Nhà Thuốc Lá, Vòm Khiên, Gốc Gọi Hồn, Đèn Đom Đóm, Chuông Bạc | Giọt sáng lơ lửng | Giọt bay tới đồng minh; vòm bật | Như trên |
| Hỗ trợ bẫy | Lò Rèn Dã Chiến | Bễ phì khói | Tia lửa nhỏ bay tới bẫy | Như trên |
| Vàng, trinh sát | Giếng Vàng, Tháp Canh | Gợn nước; cờ bay | Đồng vàng bay về ô Vàng; mắt cú đánh dấu quái | Như trên |
| Lính chặn | Vệ Binh Rêu, Gấu Khiên Đá, Người Rơm Mồi | Đứng thủ | Đỡ khiên, quét; khiêu khích: vòng cam nhạt tỏa ra | Ngã thành nụ cây, hồi sinh tại chỗ có vòng giờ |
| Lính hỗ trợ | Thợ Bẫy Sóc, Thầy Lang Nấm, Pháp Sư Dây Leo, Thợ Săn Cú | Việc nhỏ lặp lại | Sóc sửa bẫy; nấm rắc bào tử hồi; dây leo giam; cú bắn tên | Như trên |

### 6.7 Phim và cảnh

C0 chuyển động UI (banner, chân dung, ảnh trượt Tối Thượng) và C1 trong trận (boss ra mắt khung nhỏ, Tối Thượng, thắng thua) có từ bản thử. C2: bay lướt mở ải 4–6 s theo các đường, thắng thì Victory và camera xoay 3 s, Esc bỏ qua. C3: tranh truyện mỗi chương 3–6 tấm 16 : 9 từ Codex, phụ đề, giọng kể. C4: phim dựng sẵn trong Blender từ model Tripo, sau bản thử.

## 7. Âm thanh

```
music · ambience · world (đạn, nổ) · enemies · heroes · traps · allies · dialogue · typing · pronunciation · ui · warnings
→ master → limiter (ngưỡng −3 dB, tỉ lệ 20, attack 1–3 ms)
Vang: một ConvolverNode chung, tạo bằng mã theo kit (rừng thông 0,9 s, rừng phép 1,2 s, hẻm 1,6 s, đầm 0,8 s).
```
- `kit/audio` mở rộng `SceneAudio` (hiện một kênh) thành bộ trộn nhiều bus; luật nhóm và nhường tiếng lấy từ `src/audio/mix.ts`.
- Mỗi tiếng là một bản ghi manifest như TD 24.2. **Thiếu file thì dùng tiếng tổng hợp hoặc CC0 có sẵn.**
- **Ưu tiên:** P0 phát âm từ (luôn phát) → P1 báo đòn boss, quái sắp đánh Rồng, Hỏa Long dưới 35 % (luôn phát, cắt P4–P5) → P2 gõ (không bị P3–P5 che) → P3 kỹ năng Rồng, tướng địch xuất hiện, chuỗi bẫy → P4 đạn, nổ, bẫy, đòn quái → P5 bước chân, gầm vặt, môi trường.
- Cùng lúc ≤ 32 tiếng (Low 16). Cùng tiếng ≤ 4 lần mỗi 100 ms. Nổ ≤ 4 trong 120 ms. Gầm quái ≤ 2, chờ chung 0,4 s. Tiếng hạ dồn thành chuỗi nốt đi lên.
- **Va chạm:** đầu nhọn (~20 ms) + thân + đuôi + trầm (T2+) + mảnh chất liệu; 3–6 biến thể, tốc 0,96–1,04, ±1,5 dB, lệch 0–12 ms; trúng N quái trong 50 ms thì một tiếng nặng + lớp "nhiều mục tiêu"; gom 30–45 ms.

### 7.1 Bộ âm theo quái

**Bộ âm làm theo lớp, không theo loài** (9 lớp ở mục 6.2): mỗi lớp có `audio/sets/<lớp>.json` đủ các khe: `spawn`, `step`, `windup`, `attack`, `hit` (theo chất liệu), `death` (vỡ vỏ + đốm sáng "linh"), `skill`, `buffed`. Mỗi loài dùng bộ của lớp, đổi cao độ theo cỡ, chất liệu theo họ, thêm 1 tiếng giọng riêng. Tướng và boss có bộ riêng (02 §3.4, §4.5). Hơn 6 con cùng loại đang đi thì `step` đổi sang vòng lặp bầy. Danh sách âm theo lát, nguồn và giấy phép: `DESIGN.md §7`.

Chất giọng theo lớp (bước · giọng · đòn): bộ binh bước nhẹ, giáp lách cách · hự, gầm gừ · chém "xoẹt"; xạ thủ bước nhẹ · hô ngắn · dây bật, gai rít; thú xung kích vó nặng · khịt, gầm · húc "huỵch"; thú bầy lộp độp nhanh · rít nhỏ · cắn "phập"; bay vỗ cánh theo cỡ · kêu cao · bổ nhào rít; nổ cảm tử lăn lục cục · cười khúc khích · xì rồi nổ; pháp sư Héo lướt · thì thầm · phép ngân; tướng địch bước nặng · hô lệnh có vang · trống trận khi áp hào quang.

### 7.2 Gõ, nhạc, nhường tiếng

- **Gõ:** phím đúng tổng hợp bằng mã (gỗ và chuông nhỏ), mỗi chữ nâng 1 bán cung, tối đa 12; bắt đầu < 20 ms, dài < 60 ms. Phím sai "tóc" đục −12 dB, không còi. IME: chỉ phát khi chữ đã xác nhận. Xong từ: nốt ngũ cung cùng giọng nhạc đang phát (như `credit-sound.ts`).

- **Nhạc 4 lớp:** Rừng (pad, đàn hạc, sáo gỗ; Chuẩn Bị và nghỉ đợt) → + Đợt (trống khung, ostinato cello) → + Dồn (trống lớn, dây nhanh; đợt cuối hoặc Hỏa Long dưới 35 %) → + mô-típ kèn đồng 8 ô nhịp khi có tướng địch. Boss có bản riêng, mỗi pha một stem, câu mở 2–5 s. Thắng, thua có đoạn kết ngắn.
- Các lớp cùng BPM, cùng giọng, cùng điểm đầu; chuyển lớp mờ 2 s ở đầu ô nhịp. **Mỗi kit 1 bản 4 lớp** (8 kit + lớp Hắc Vụ biến tấu = 9 bản), **mỗi boss chương 1 bản** (dùng chung theo cặp kit ở Hồi I, riêng ở boss lớn). Bản thử dọc: 1 bản 2 lớp + 1 bản boss. Render stem bằng `scripts/music/render-songs.mjs`.

| Khi | Hạ | Thời gian |
|---|---|---|
| Phát âm từ | music −4, world −6, enemies −6, traps −6, heroes −3 dB; hoãn thoại | Xuống 80 ms, lên 400 ms |
| Thoại Rồng, người kể | music −6, ambience −6, enemies −6 dB | Xuống 100 ms, lên 500 ms |
| Báo đòn boss, Cụm Ấn | world −4, music −3 dB; tắt P5; không phát âm (01) | Theo cửa sổ |
| Tạm dừng | world, enemies qua lọc thấp 800 Hz | — |

- Phát âm theo 01 mục 6.4: một kênh, có hàng chờ, cách nhau ≥ 2,5 s. Thoại Bạch Long và người kể: 06 §6 (giọng, phụ đề). **Nguồn:** theo TD 24.9 (WAV gốc ngoài Git, OGG trong game, giọng −16 LUFS, nhạc −18, nền −26; công cụ AI có gói thương mại, ghi công cụ, ngày, prompt; lên Drive bằng `pnpm media:push`).

## 8. Ngân sách hiệu năng (Mac Apple Silicon, 1080p)

**Luật sim không biết bậc máy (00 D10).** Trần quái sống (220) và ngân sách chữ (00 §5) là hằng số của luật. Bậc chỉ đổi **cách vẽ**.

| Mục | Low | Medium | High | Ultra |
|---|---|---|---|---|
| Quái vẽ đầy đủ (đám đông có xương) | 100 | 160 | 220 | 220 |
| Quái thừa (ngoài số vẽ đầy đủ) | Impostor hoặc chấm | Impostor | — | — |
| SkinnedMesh (chỉ hai Rồng, tướng địch, boss) | 4 | 6 | 8 | 10 |
| Lính chặn | Đám đông có xương | Như Low | Như Low | Như Low |
| Chữ sống (luật sim, mọi bậc) | ≤ 16 | ≤ 16 | ≤ 16 | ≤ 16 |
| Hạt chiến đấu / số sống / mảnh vỡ | 600 / 50 / 150 | 1.500 / 100 / 400 | 3.000 / 160 / 600 | 4.500 / 200 / 900 |
| Tam giác prop (trần theo tam giác, không theo số món) | 0,25 M | 0,5 M | 0,9 M | 1,4 M |
| Tam giác tổng (gồm bóng) | 0,5 M | 1 M | 2 M | 3 M |
| Draw call | ≤ 80 | ≤ 110 | ≤ 150 | ≤ 190 |
| Bộ nhớ GPU | ≤ 300 MB | ≤ 450 MB | ≤ 700 MB | ≤ 900 MB |
| Tiếng cùng lúc | 16 | 24 | 32 | 32 |

- **Prop:** LOD 40 % tam giác ngoài 30 m; vòng rừng ngoài vùng chơi là impostor. Trần tính theo tam giác, nên kit nhiều cây lớn có ít cây hơn.
- **Đích đo:** khung ở trần High trung bình ≤ 8 ms, p95 ≤ 12 ms; một bước sim 60 Hz ở đỉnh ≤ 0,3 ms headless (00 §8); bộ xếp 20 thẻ ≤ 0,3 ms; phím tới hình ≤ 1 khung, phím tới đòn ≤ 50 ms (≤ 70 ms khi đang dừng hình); nạp ải cùng kit ≤ 1 s, kit mới ≤ 5 s; âm đã giải mã 40–60 MB, nạp theo chương.
- Không cấp phát trong trận. Chạm trần hiệu ứng: hiệu ứng ưu tiên cao thay ưu tiên thấp.
- **Mốc đo cũ không đủ:** Defense V4 đo 442 quái **InstancedMesh tĩnh, không xương** (3,7 ms, 108 draw call). Đám đông có xương, trộn 2 clip, 8 loài chưa từng đo. Vì vậy **bài đo là việc đầu tiên của M0** (DESIGN.md §9): `defense-bench` thêm chế độ `bones` và `vat`, 220–300 quái Tripo thật đủ ba dáng, đo ở High trên Mac và ở Low trên laptop yếu. Trần quái vẽ đầy đủ ở bảng trên chỉ chốt sau bài đo; nếu Low không gánh nổi 100 thì hạ trần luật chung rồi chạy lại bot.

## 9. Kiến trúc kỹ thuật

### 9.1 Mười hai quyết định

1. **Mỗi game một repo**, gắn vào repo cha là submodule `games/<id>`, như 5 game hiện có.
2. **`shared/game-kit`** ở repo cha là nguồn chuẩn của mã dùng chung: TS, không media, có test riêng.
3. Kit được **chép** vào `src/kit/` từng game bằng `pnpm kit:sync`, kèm `kit-manifest.json` (phiên bản, sha256 từng file). Mẫu giống `scripts/sync-space-voice-contract.mjs`.
4. Hai lớp kiểm: `pnpm check` của game kiểm `src/kit` không bị sửa tay; `pnpm kit:check` ở repo cha kiểm mọi game ở bản kit mới nhất hoặc bản ghim có lý do.
5. **Không game nào import `games/space-typing/src`.** Test ranh giới chặn.
6. `three@0.170.0` ghim ở mọi game. Kit khai `three` là peer.
7. Sim tất định 60 Hz thuần TS theo luật TD 25.1.5 cho cả 3 game mới.
8. Thẻ chữ, khung học là DOM trên canvas.
9. Model của game ở `/assets/dragon-hold/models/`, manifest riêng, lên Drive qua `pnpm media:push` (bộ media riêng của game). **Ba GLB Rồng** (v2, v3 medium, v4) được chép vào bộ media này (00 D22), nên game không phụ thuộc thư mục media của Space khi chạy. Alias `/assets/space-typing/models/` chỉ dùng tạm cho hình giữ chỗ trong hộp cát dev. Viêm Đế: nạp sẵn v3 lúc vào ải để không khựng.
10. Mỗi game gửi sự kiện học bằng `gameId` của chính nó.
11. Defense V4, Campaign 3D **ở lại Space**. Phần hình V4 (camera, crowd, vfx, terrain, painter, sounds) được **chép** vào Rồng Giữ Ải, ghi nguồn đầu file.
12. Mỗi bước có cổng. Sau mỗi bước, Space vẫn build và chạy như cũ.

### 9.2 Kit

| Thư mục kit | Nguồn ở Space | Đổi gì |
|---|---|---|
| `input/` | `scene3d/keys.ts`, `logic.ts` (`typingText`, `normalizeWord`) | Bỏ type `Enemy`; type riêng |
| `vocab/` | `vocabulary.ts`, `scene3d/words.ts` | `baseUrl` là tham số (mặc định `/vocabulary/`) |
| `typing/` | `td/typing/*` (bản 1A6) | Hằng số thành `TypingConfig`; nhận RNG |
| `platform/` | `platform/{rng,frame-loop,safe-storage,canvas-state}.ts` | Không |
| `learning/` | `learning/shared.ts` + `shared/learning/message-contract.mjs` | **`gameId` là tham số**; bridge postMessage, shared-music |
| `speech/` | `speech.ts` | Cài đặt hẹp `{ enabled, rate, volume }` |
| `three/` | `render3d/model-loader.ts`, `model-contracts.ts`, `scene3d/{hero,particles,materials,textures,util}.ts`, phần sân khấu của `space.ts`, `ui/title-guide-scene.ts` | `manifestUrl` là tham số, nạp nhiều manifest; `ModelKind` mở rộng được (`units`, `props`); bỏ trời sao |
| `feedback/` | `src/feedback/*` của Sinh Tồn (S0) | Hồ sơ theo game (`ship`, `dragon`, `td`); `kill-translation` |
| `audio/` | `scene3d/sfx.ts`, `audio/mix.ts`, `audio/credit-sound.ts` | Bộ trộn nhiều bus, nhận bảng âm |
| `ui/` | (mới) | Màu ngữ nghĩa, `--ui`, font chữ trận, khung học cơ bản |
| `tools/` | `scripts/visual/cdp-run.mjs`; plugin Vite phục vụ model chung (mới) | Chỉ dùng lúc build, kiểm |

Không vào kit: `enemies/*`, `campaign/*`, `worlds/*`, `defense/*`, `ui/*` của Space, `types.ts`.

### 9.3 Space Typing vẫn chạy

**Đã đổi (00 D17, `../SPLIT_PLAN.md` §4):** kit được **chép từ** Space; Space giữ nguyên bản gốc và không dùng kit ở giai đoạn này. `kit:check` chỉ báo độ lệch giữa kit và bản gốc trong Space. Việc cho Space dùng kit qua shim (mô tả dưới) **hoãn** tới khi ba game mới chạy ổn, và chỉ làm nếu độ lệch gây lỗi thật.

- (Hoãn) `pnpm kit:sync --target games/space-typing` chép kit vào `src/kit/`. File cũ thành shim, ví dụ `src/scene3d/keys.ts` chỉ còn `export * from "../kit/input/keys";`. Tên export giữ nguyên.
- `src/learning/shared.ts` gọi `createLearningEmitter({ gameId: "space-typing" })`.
- Test hiện có không sửa một dòng: `campaign3d-keys`, `credit-*`, `defense-frame-error`, `mode-isolation`, `td-boundary` (tới khi TD rời đi).
- Kịch bản hình Campaign 3D, Defense chụp trước và sau; lệch điểm ảnh vượt ngưỡng thì dừng. Changelog Space theo luật changelog.

### 9.4 Ranh giới mỗi game mới (`tests/<id>-boundary.test.ts`)

Chỉ import `src/**` của chính nó, `src/kit/**`, `three`, `three/examples/jsm/*`, `@fontsource/*`; không đường dẫn `../space-typing`. `sim/`, `typing/`, `content/` cấm `three`, `window`, `document`, `Date`, `performance`, `localStorage`, `Math.random`, lượng giác, `pow`, `hypot`, `**`. Chuỗi `/assets/` bắt đầu bằng `/assets/<id>/` hoặc `/assets/space-typing/models/`. Mọi file trong `src/kit/` khớp sha256 của `kit-manifest.json`.

### 9.5 Rồng Giữ Ải: cây thư mục

```
games/dragon-hold/
  index.html vite.config.ts package.json tsconfig.json AGENTS.md .gitignore (public/assets/**, art-src/** trừ README, manifest)
  src/kit/      chép từ shared/game-kit, không sửa tay
  src/app/      main, session, input (router phím), save, learning, settings
  src/sim/      thuần TS: world, waves, spawn, flow, block, combat, projectiles, traps, houses, units, auras, skills, boss, economy, words, events, hash
  src/content/  types, schema, compile, hash; data/*.json (heroes, enemies, generals, bosses, traps, houses, units, items, kits)
  src/stages/   sinh ải từ 16 mẫu bố cục + kit + seed; validate-map; mã băm bố cục
  src/view/     stage, camera, terrain, water, scatter (BatchedMesh), crowd (texture xương), actors, heroes, traps, houses, telegraphs, hpbars, fx
  src/ui/       hud, tags, learning-frame, prep, shop-strip, placement, wave-card, results, word-book, dh.css
  src/audio/    bank, music, sets/*.json
  scripts/      stages:gen, stages:validate, dh:balance, prepare-ground, prepare-kit, visual/scenarios/dh-*.mjs
  tests/        dh-boundary, sim, golden, content, stages, tags-layout, feedback-keys
  docs/         design/ (chuyển từ docs/games/dragon-lane ở M1), changelog/
```

### 9.6 Chuyển TD và Sinh Tồn

**Đã chuyển sang `../SPLIT_PLAN.md` §6–§7**, cập nhật theo trạng thái repo ngày 23/10: S0 của Sinh Tồn đã commit (`86f007e2`, `5ed6aba2`, `d1148572`, `eff07a3e` trên `feat/survival-s0`), nên tách được ngay; TD chỉ tách ở ranh giới mốc (đóng R3, gộp, đóng băng, rồi `filter-repo`). Không chuyển dữ liệu lưu (00 D18).

### 9.7 Portal và hạ tầng

**Đã chuyển sang `../SPLIT_PLAN.md` §9–§10** (mục `games.json`, trường `group`, nginx, `setup-nginx.sh`, `package.json`, `play.sh`, `dev.sh`, `bootstrap.sh`, `validate-play-mode`, `.gitmodules`, media nhiều game, công cụ model, `AGENTS.md`).

## 10. Kiểm tra

- **Tự động:** `pnpm kit:test` (từng module, `gameId` bắt buộc); `pnpm check` từng game và `pnpm kit:check` (đồng bộ kit); `tests/<id>-boundary.test.ts` (mục 9.4); `tests/golden/*` (cùng seed ra cùng mã băm); `pnpm dh:balance` (bot 25 / 35 / 60 WPM) và `pnpm stages:validate` (`validate-map` mọi ải); `tests/tags-layout.test.ts` (không chồng, không ẩn chữ sống).
- **Portal:** 3 `gameId` được nhận, origin sai bị từ chối; `validate-portal-layout` ở 1280 và 1920.

**Kịch bản hình** (`scripts/visual/scenarios/dh-*.mjs`, gõ thật qua CDP, chạy được khi chỉ có manifest; mọi kịch bản: không lỗi console, draw call trong ngân sách):

| Kịch bản | Đạt khi |
|---|---|
| `dh-words` | 220 quái, 4 đường cùng dồn về bệ, 16 chữ sống, 1280 × 720 và 1920 × 1080, cỡ thẻ 100 % và 150 %: không chồng, cỡ ≥ 16 px, tương phản ≥ 7 : 1, diện tích ≤ 6 %, vòng khe quanh bệ đúng; thêm một lượt giả lập mù màu deuteranopia: mọi loại thẻ tách được nhờ icon |
| `dh-learning-frame` | Bão T4–T5: 0 lần số hoặc hạt đè khung học; từ mới ghim ≥ 2,5 s; 20 mẫu IPA đúng font |
| `dh-hitstop-keys` | Gõ 120 WPM trong bão T5: 0 phím mất, phím tới đòn ≤ 70 ms |
| `dh-placement` | Ô hiện đúng lúc, bóng ma, vòng tầm, dựng 2 s; đường bàn phím 00 §6: số, mũi tên, Enter, Backquote, `=`, `-`, Esc |
| `dh-prep-shop` | Mọi chữ vừa khung ở 1280 × 720; món khắc chế được làm sáng; font tiêu đề đủ dấu tiếng Việt |
| `dh-camera`, `dh-scale` | 3 góc × 4 hướng; dither; không lộ rìa; cỡ px theo mục 2.3 |
| `dh-vfx-tiers` | Ảnh chụp chậm T1–T5 trên đất sáng và tối, hiệu ứng thấy rõ |
| `dh-telegraphs`, `dh-boss` | Báo trước ≥ 0,5 s; Cụm Ấn theo công thức 01; ra mắt, đổi pha, buff quân, chết |
| `dh-perf` | 220 quái đám đông có xương ở High: trung bình ≤ 8 ms, p95 ≤ 12 ms; Low trên laptop yếu |
| `dh-ime`, `dh-keyboard-only` | Telex, VNI; bố cục phím Mac và Linux; Alt + 1…9, Alt + 0, mũi tên, Tab, Enter, Backquote; qua một ải chỉ bằng bàn phím, kể cả Lều Chuẩn Bị, Long Ấn, Thẻ Ôn |
| `dh-focus` | Bấm HUD, bấm dải món, alt-tab, bấm thanh nav của portal rồi quay lại: tự dừng, che chữ, "bấm để tiếp" lấy lại focus, đồng hồ đứng yên (06 §2) |
| `dh-meta-screens` | Mọi màn ngoài trận ở 1280 × 720 và 1920 × 1080; đi hết bằng bàn phím (06 §4) |
| `dh-audio-duck` | Mức các bus khi phát âm đúng bảng 7.2 |
| Tai người | Âm thanh, nhạc: chủ dự án quyết |

## 11. Kế hoạch xây và tách (đã chuyển)

Kế hoạch 11 bước cũ (M0–M10) đặt bản thử dọc sau toàn bộ việc tách game và cho Space dùng shim. Đã thay bằng:

- **Mốc xây Rồng Giữ Ải** (M0 bản thử dọc 1 bản đồ 2 đường, 10 đợt, chạy song song với việc tách; rồi M1…M8 tới 520 ải), cổng của từng mốc và bảng làn song song cho nhiều agent: **`DESIGN.md` §9**.
- **Tách ba game** (kit chép từ Space, tách Sinh Tồn ngay, tách TD ở ranh giới mốc, hạ tầng, portal, dọn Space): **`../SPLIT_PLAN.md`**.
- Luật chung giữ nguyên: mỗi bước một nhánh; đổi kit đi qua repo cha rồi `kit:sync`; không agent nào sửa `src/kit/` trong game; không đụng `games/.wt-*` đang có người làm.

## 12. Rủi ro

- **Kit lệch với bản gốc trong Space:** `kit:check` báo độ lệch; sửa lỗi ở một nơi thì ghi việc cần chép sang nơi kia.
- **Model Rồng nằm trong Space:** đã chép 3 GLB vào bộ media của game (00 D22). Hình giữ chỗ trong hộp cát vẫn qua alias, chỉ ở dev.
- **Tách khi làn TD, Sinh Tồn đang làm dở:** chỉ tách từ nhánh đã commit, ở ranh giới mốc, không đụng `games/.wt-*` (`../SPLIT_PLAN.md` §7).
- **Đám đông có xương chưa từng đo:** bài đo ở đầu M0 (mục 8).
- **Rừng tím lam làm chìm quái và chữ:** vỏ Héo xám vàng úa, rim cho quái, thẻ nền tối, bài nheo mắt. **Âm ồn khi 300 quái:** vòng lặp bầy, trần tiếng, gom va chạm.

## Câu hỏi

| # | Câu hỏi | Mặc định nếu chưa trả lời |
|---|---|---|
| 1 | Tên: **Rồng Giữ Ải** (`dragon-hold`), **Lời Gọi** (`typing-defense`), **Tuyến Cuối** (`typing-survival`)? | Dùng đúng các tên này (00 D01) |
| 2 | Ba repo mới công khai hay riêng tư? | Công khai như 5 repo cũ (Git không có media, không có bí mật) |
| 3 | Đặt món vào **ô có sẵn** (03) thay vì đặt tự do như anh từng muốn cho Defense (21/10)? | Ô có sẵn, nhưng ô không vẽ vào đất, chỉ hiện khi đặt hoặc nghỉ đợt |
| 4 | ~~Phím trùng Alt + 4/5/6~~ | Đã chốt: kỹ năng Alt + 1…6, đồ tiêu hao Alt + 7/8/9 (00 §6) |
| 5 | ~~Chuyển lưu TD, Sinh Tồn~~ | Đã chốt: không chuyển, vì chưa có người chơi thật (00 D18) |
| 6 | Nav portal gom 8 game thành "Luyện gõ" và "Game chiến đấu"? | Có |
| 7 | Model dùng chung giữ trong Space hay chuyển ra `shared/models`? | Giữ trong Space; riêng 3 GLB Rồng chép vào media của Rồng Giữ Ải (00 D22) |
| 8 | ~~Đổi tên "Đền Gọi Hồn"~~ | Đã chốt: "Gốc Gọi Hồn" (`revive-root`) |
