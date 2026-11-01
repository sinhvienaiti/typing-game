# Cứu chất lượng hình, 01/11/2026: Last Line và Dragonhold

Chủ dự án nêu các vấn đề sau ngày 01/11:

- Last Line:
  - ô súng nằm quá thấp;
  - cần nữ xạ thủ và drone hỗ trợ làm nhân vật chính;
  - đạn mờ và xấu;
  - chữ trong ô súng đứng im.
- Dragonhold: cây, đá, nước, đất và quái trông "như đồ chơi", dù đang mở Ultra.
- Câu hỏi: "bạn có chấm điểm cho hình ảnh thực sự chất lượng k vậy".

Có ba người điều tra. Họ đọc mã và chụp bản chơi trong ngày 01/11, không sửa file nào được Git theo dõi.

Mức nhận là 8,5 cho mọi thứ người chơi thấy. Hệ thống dùng chung giữ mức 9 (`AGENTS.md`, `ART_ACCEPTANCE.md`). File này cũng là sổ nợ dưới 8,5 mà `ART_ACCEPTANCE.md` dòng 16 trỏ tới (mục 6).

**Cách chấm chuẩn (gọi là "chấm C" trong file này)**, áp dụng cho mọi mục bên dưới:

- Chấm trên bản build ở host chơi: `https://dragon.typing-game.local` và `https://survival.typing-game.local`. Không chấm trên dev server, không thêm tham số URL.
- Chấm ở bậc Ultra và High, sau khi đã tải lại trang. Hai độ phân giải: 1920×1080 và 1280×720.
- Dùng khung chơi thật, ở camera trận, đúng kích thước trên màn. Không chấm trên tờ ảnh phóng to (bài học 31/10: icon được 8 trên tờ 256 px, vào game ở 16–24 px chỉ còn 6,2).
- Đặt cạnh ảnh mẫu thương mại (bảng M, ART_DIRECTION 1.3), không đặt cạnh bản cũ của ta.
- Hai giám khảo mù, độc lập, đều phải cho từ 8,5 trở lên. Hệ thống dùng chung cần từ 9, chủ dự án ký cuối.
- Kèm số đo riêng của từng mục và frame time (`dh-bench`, `survival-s1-perf`).

## 1. Có chấm hình thật không? Chưa, và chấm sai chỗ

**Những gì đã chấm:**

- **Map A2 của Dragonhold** được nhận với "giám khảo trung vị 8,0" (commit `0bf5918`). Nhưng chấm theo kế hoạch map của ta, không theo mốc thương mại. Ngay ART_DIRECTION 28/10 cũng tự chấm sân 3D 3/10 và map góc nghiêng 6/10, mà không có gì chặn việc gắn vào game.
- **Đạn Last Line** do chính người làm tự chấm ngày 28/10: Heat Beam 7,5, Pulse 7. Không có giám khảo độc lập.
- Phép kiểm tự động chỉ bắt lỗi "trắng xóa ≤ 6 %". Đạn đo được 1,9–4,2 % nên qua. Lỗi thật là vệt đạn rộng và nhạt, phép kiểm không đo cái đó.

**Những gì đã bỏ sót:**

1. **Bản chơi khác bản dev.** Ở Dragonhold, ô đất và decal chỉ nạp khi chạy dev (`paint.ts:16`, `:372-375`, `artOn = import.meta.env.DEV`). Chấm trên dev thì thấy đất có texture. Trên bản chơi, đất chỉ là một mảng màu phẳng: 0 request ground hay decal, trong khi dev có 12.
2. **Phần đã sửa chưa tới tay người chơi.** Hai nhánh Dragonhold đã sửa từ 29/10 nhưng chưa gộp vào main:
   - `map-pilot`, 12 commit;
   - `dh-models`, bậc model Ultra có normal và roughness.

   Bản chơi vẫn chạy model cắt M0b: cây 700–1.599 tam giác, đá 450–800, mỗi model chỉ một ảnh màu 1024.
3. **Không ai chấm ở Ultra.**
   - Last Line: bloom và tone mapping ACES chỉ bật ở High và Ultra. Chúng làm vệt đạn rộng ra 2,5–3,5 lần và ngả trắng, nên **Ultra xấu hơn Medium**.
   - Dragonhold: Ultra chỉ đổi dpr 2, bóng 4096 và MSAA 4×. Mọi thứ làm cảnh trông như đồ chơi vẫn giữ nguyên ở Ultra: ánh sáng 3 bậc, viền mực, mip bias lá, đá sơn xám.
4. **Đổi Quality trong Cài đặt của Dragonhold chỉ có hiệu lực sau khi tải lại trang**, và game không nhắc điều này (`settings.ts:94`, `app.ts:254-256`). Nếu anh chuyển sang Ultra giữa phiên mà không tải lại, game vẫn chạy High. Chúng tôi không kiểm được anh đã tải lại hay chưa.
5. **Chưa ai chấm cảnh thế giới ở camera trận:** cây, đá, nước, đất.

Vậy "Ultra bị bóp" thật ra là hai chuyện:

- Dragonhold: Ultra chạy đúng, nhưng nội dung là bản cắt và vẽ theo kiểu đồ chơi.
- Last Line: Ultra thêm bloom nên đạn nhòe.

**Điểm thật hôm nay** (thang M: 8 là mức thương mại; mức nhận là 8,5):

- **Dragonhold: 4/10.**
  - Dev được khoảng 4,5.
  - Gộp cả hai nhánh, ước lên 5,5–6.
  - Muốn tới 8,5 phải đổi kiểu shading, làm lại nước, thêm AO, thêm mốc lớn và có model nguồn chi tiết hơn.
- **Last Line, phần trận: 4/10.** Điểm từng súng (một người chấm, sơ bộ):

  | Súng | Điểm |
  |---|---|
  | Pulse Gun | 5 |
  | Heat Beam | 4 |
  | Rail Gun | 4,5 |
  | Scatter Gun | 3,5 |
  | Star Mortar | 3,5 |

- **Last Line, nhân vật chính: 4/10.** Hiện là con tàu Vanguard lấy từ Space Typing.

## 2. Nguyên nhân gốc

### 2.1 Dragonhold, đã kiểm

1. **Bản build không nạp ô đất và decal.** `paint.ts:16`, `:372-375`. Tám file WebP trong `dist/assets/dragon-hold/ground/pine-river/` và manifest đã có từ Codex 080, nhưng không có code nào gọi tới. Ảnh: `compare-z06-meadow-se.jpg`, `compare-z06-river-bridge.jpg`.
2. **Model bản chơi là bản cắt M0b** (`glb-served-high.json`):
   - Số tam giác: cây 700–1.599, đá 450–800, vách 800, quái 1.707–4.325.
   - Vật liệu: `r=0.9 m=0`, không có normal, không có roughness map.
   - Code main tự bỏ các map: `models.ts:98`, `scatter.ts:561` (Lambert chỉ có map), `crowd.ts:720`.
   - Ultra vẫn nạp `.high` vì manifest của dist không có bậc ultra.
   - Mức sàn của MODEL_QUALITY §2: cây 8.000, đá 2.500.
3. **Phần đã sửa nằm trên nhánh chưa gộp.**
   - `map-pilot`: 12 commit, gộp vào main không xung đột (`git merge-tree`). Gồm `b1d3e7e` (đưa ô đất vào build), `9ff3b49` (ánh A3: nắng 30°, key 4,6, sương theo độ cao, vách ×2, đất ô liu) và `51fb5b2` (đường r2).
   - `dh-models` (`92e16a3`, `9ae7ec4`, `d84a433`): 3 xung đột, ở `AGENTS.md`, `src/kit/kit-manifest.json` và `src/view/bench.ts`. Media của các bậc nằm trong `.wt-dh-models/public/assets/dragon-hold/models`, chưa có ở checkout chính.
4. **Shading kiểu "tranh đồ chơi" là có chủ ý, và Ultra không đổi gì.**
   - Ánh sáng 3 bậc, mix 0,72 (`terrain.ts:371-376`, `:470`).
   - Mọi cây, đá, cầu, đất dùng MeshLambertMaterial, thêm rim và sương (`terrain.ts:430-488`).
   - Vòm cây bị ép pháp tuyến cầu, hệ số 0,55 (`scatter.ts:416`).
   - Quái có viền mực 2,1 px (`crowd.ts:314-315`), phủ màu họ 0,2–0,3 và rim kem (`crowd.ts:402-424`, `model-specs.ts:283-289`).
   - Grade có lift màu sữa (`stage.ts:98-100`, `:151`).
   - Ảnh: `compare-z06-trees-nw.jpg`, `compare-z06-cliff-w.jpg`, `compare-foe-closeup.jpg`.
5. **Shader xóa chi tiết.**
   - `FOLIAGE_MAP_BIAS = 2.7` (`scatter.ts:108`, `:568`): texture lá chỉ còn khoảng 1/6,5 độ phân giải.
   - `STONE_PAINT` và `CLIFF_PAINT` (`scatter.ts:61-66`, `:80-85`) thay màu đá bằng một màu xám phẳng.
   - Không texture GLB nào có anisotropy, trong khi GPU cho tối đa 16. Mặt nghiêng nhìn ở camera 55° vì thế bị mờ.
6. **Ánh sáng phẳng, không có AO.**
   - Nắng ở góc 50°. Ánh trời 2,7 so với nắng 3,3 (`L2-cau.map.json:8`, `stage.ts:217`), nên trên đất phẳng nắng trực tiếp (≈ 2,5) gần bằng ánh trời.
   - Đo trên đồng cỏ: chỗ bóng L = 113, chỗ sáng L = 173.
   - Composer chỉ có Render, Bloom (đang tắt), Grade, FXAA hoặc MSAA (`stage.ts:265-279`): không có SSAO hay GTAO, không có bóng tiếp xúc.
7. **Nước là shader phẳng kiểu cartoon** (`water.ts:31-77`).
   - Hai màu theo độ sâu, vệt noise bị posterize, bọt vẽ bằng `step()` thành mảng trắng cứng.
   - Không phản chiếu, không Fresnel, không normal, không specular theo nắng.
   - Ảnh: `compare-z06-ford.jpg`, `compare-z06-pond.jpg`.
8. **Ultra gần như giống High.**
   - Ảnh bake đất 2048 cho 5,1 cm mỗi texel. Ở zoom 0,6, màn hình cần 2,8 cm mỗi pixel (1,4 cm trên Retina), nên đất bị phóng 1,8–3,6 lần.
   - Model Ultra dùng chung file `.high`.
   - Đổi Quality phải tải lại mới có hiệu lực (xem mục 1).
9. **Rừng xa là ảnh impostor 256 px, chụp từ một góc** (`impostor.ts:17`; cây xa hơn 42 m). Phần này chiếm khoảng một phần ba trên của khung nhà.

### 2.2 Dragonhold, phỏng đoán (chưa đo)

- **Camera và bố cục kiểu diorama.** Camera ở 95 m, FOV 30, pitch 55 (`maps.ts:111`). Quái cao khoảng 45 px ở 1080p. Cỏ xanh như sân bóng (`paint.ts:56-68`), không có mốc lớn, không thấy trời. Chúng tôi đoán mắt người đọc tổ hợp này thành "mô hình đồ chơi", nhưng chưa đo được.
- **Lỗi NaN ở rim quái khi bật MSAA (Ultra).** `crowd.ts:418`, `:422`, `:439` gọi `pow()` mà không có `max()`. Có thể sinh chấm tối ở mép quái. Chưa kiểm bằng mắt trên main.

### 2.3 Last Line, đã kiểm

1. **Bloom và ACES ở High/Ultra làm đạn rộng ra và ngả trắng.**
   - Code: `scene.ts:28-29`, `:303`, `:325-329`. Bloom 0,85 / 0,3 / ngưỡng 1,0, rồi OutputPass.
   - Đo Heat Beam cách tàu 11 m, ở 1080p:

     | Bậc | Bề ngang nửa đỉnh (FWHM) | Màu lõi | Độ bão hòa |
     |---|---|---|---|
     | Ultra | 86–97 px | (255,247,230), gần trắng | 0,445 |
     | Ultra, tắt bloom | 37–38 px | (255,232,194) | 0,553 |
     | Medium | 16 px | (255,255,110), vàng | 0,596 |

   - Pulse Gun: độ bão hòa 0,19 ở Ultra, 0,41 ở Medium.
   - Ảnh: `compare-bloom-tonemap-1920x1080.jpg`, `compare-ultra-medium-1920x1080.jpg`. Số đo: `tia-profile-1920x1080.json`.
2. **Đạn chỉ là gradient mềm vẽ bằng mã.**
   - Atlas 128 px (`fx.ts:20`, `:54`). Shader dải không có lõi phẳng, không texture, không nhiễu (`fx.ts:252-262`).
   - Lõi Heat Beam có cường độ 0,55 và chỉ 6 % trắng, tối hơn quầng của chính nó (1,3) (`beams.ts:210-213`, `gun-rules.ts:64`).
   - Ngôi sao Rail Gun cao 34 % chiều cao màn (`beams.ts:72`). Ở khung f05, nó làm sáng 56 % sân.
   - Vệt Pulse dài 0,18 m với 90 % lõi trắng (`shots.ts:413`). Lóe trúng có bán kính 126 px, gấp 1,47 lần mức FEEL §4.2.
3. **Màu súng trùng màu quái và sân.**
   - Heat Beam dùng `PALETTE.hot`, cùng màu với gân quái thường, vạch sàn và vệt sáng của hố đen (`shots.ts:92`, `scene.ts:143-155`, `crowd.ts:112`).
   - Pulse trùng màu ống dẫn trên tường và gân quái trinh sát.
   - Vòng điểm rơi của Star Mortar dùng màu đỏ của địch (`shots.ts:456`).
   - Cả ba trái VFX_STANDARD dòng 397 và §3.6.3.
4. **"Khói" xám được vẽ cộng sáng**, nên làm sân sáng thêm thành sương sữa thay vì tối đi (`shots.ts:202`, `:222`, `:236`). Pool khói trộn thường đã có sẵn nhưng không dùng ở đây.
5. **Thiếu pha.**
   - Scatter không có pha gồng (A) và dư âm (F); viên đạn chỉ là một dải 0,16 m.
   - Rail không có F.
   - Star Mortar không gồng ở tàu, không có đèn lúc phóng, và vệt bay chỉ phủ 8 % đường cung.
6. **High/Ultra không có MSAA.** EffectComposer tạo render target không có samples (`scene.ts:325`).
7. **Ô súng nằm ở 70,6–84,4 % chiều cao màn** (`hud.ts:225-236`), trong khi nửa số quái ở trên mức 31–33 %. Từ chữ trong ô lên tâm bầy quái lệch 503 px theo chiều dọc ở 1080p, tức 47 % chiều cao. Bản thử chỉ còn lệch 65 px. Ảnh: `layout-mock-sheet.jpg`, `layout-mock-c-sheet.jpg`.
8. **Chữ chờ đứng im hoàn toàn.** `.sv-word` không có animation (`survival.css:94`). Chữ chờ của kit cũng tĩnh (`typing-fx/css.ts:23`). Chỉ có chữ đầu nảy lên khi gõ sai (`hud.ts:368-373`).
9. **Chưa có nhân vật chính.** Người chơi điều khiển tàu Vanguard (`ship.ts:56`, `models.ts:24`). Trong manifest không có GLB nhân vật, drone hay súng.

### 2.4 Last Line, phỏng đoán

- **Vụ nổ Star Mortar có mép cắt thẳng.** Có thể billboard chui xuống dưới khối sàn, trong khi glow cộng sáng không mờ dần theo mặt sàn (`fx.ts:116`). Chưa tách thí nghiệm. Ảnh: `compare-zoom-phao-burst-1920x1080.jpg`.
- **"Nhấp nháy, nhấp nhô" anh thấy ở Typing Break** (Tholus, Steam 27/01/2026) nhiều khả năng là hiệu ứng theo phím: T1 chữ đóng dấu, T3 viền ô nổ rồi co, T8 viền ô thở. Bản soi video của ta (`TYPING_BREAK_STUDY.md` §2.1) thấy ô đứng im khi chờ.
- **Ảnh anh gửi gần như chắc là** `games/typing-survival/art-src/ui/screens-epic/results-lose-bg.png` (nền màn thua). Chưa đối chiếu với ảnh gốc.

## 3. Kế hoạch sửa

Chữ D là Dragonhold, L là Last Line, O là việc chờ chủ dự án.

Hai làn chạy song song, mỗi game một làn. Mỗi làn một người kiểm (parallel-testing: không quá 3).

### Đợt 1: hôm nay (sửa code, thắng lớn nhất về hình)

| # | Việc | Vì sao | Ai | Công | Chấm thế nào |
|---|---|---|---|---|---|
| D1 | Gộp `map-pilot` vào main (0 xung đột), build lại dist | Đưa ô đất và decal (`b1d3e7e`), ánh A3, đất ô liu, vách ×2 và đường r2 tới bản chơi | Claude | 3–4 giờ | `dh-ground-tiles` trên host chơi; số request ground/decal > 0; cặp ảnh trước/sau cùng camera (bộ `compare-z06-*`); chấm C |
| D2 | Gộp `dh-models`: sửa 3 xung đột, đồng bộ kit bằng `sync-game-kit` (không sửa tay), chép 128 file media theo changelog model-tiers §11 | Model có bậc Ultra/High/Medium từ file gốc Tripo, có normal và roughness; sửa luôn NaN ở rim quái | Claude; người điều phối chép media và chạy `media:push` | 0,5 ngày | `pnpm check`, `dh-bench`, `dh-crowd`; Ultra phải nạp `.ultra.glb`, material có normalMap và roughnessMap; cận cảnh cây, đá, quái ở 1080p; chấm C |
| D3 | High/Ultra: `FOLIAGE_MAP_BIAS` còn 0–0,5; sơn đá đổi thành tint ≤ 0,3; anisotropy 8 (High) và 16 (Ultra) cho mọi map GLB trong `models.ts` | Lá đang ở khoảng 1/6,5 độ phân giải; vách thành khối kem trơn | Claude | vài giờ | Trước/sau `compare-z06-trees-nw`, `compare-z06-cliff-w`; chấm C |
| D4 | Đổi Quality thì hiện "Restart to apply" và tự tải lại trang | Hiện chọn Ultra giữa phiên không có hiệu lực | Claude | 1–2 giờ | Kiểm tay: chọn Ultra, trang tải lại, renderer báo dpr 2, shadow 4096, MSAA 4 |
| L1 | Bloom và tone map: chỉ lõi mảnh ở HDR 3–6 được bloom; quầng, haze, cột sàn giữ ≤ 0,9; bloom strength 0,4–0,5, radius 0,1–0,15; thử AgX hoặc Neutral thay ACES. Làm trên nhánh, gộp khi có O4 | Lý do số một khiến đạn mờ ở Ultra | Claude | 0,5–1 ngày | Mục tiêu đề xuất: Heat Beam FWHM ≤ 30 px ở 11 m (1080p); lõi giữ màu, không về kem trắng; bão hòa ≥ 0,6; phần sân bị sáng không quá Medium hôm nay; trắng xóa ≤ 6 %; frame time |
| L2 | Composer High/Ultra dùng `WebGLRenderTarget` có `samples: 4` | High/Ultra hiện không có khử răng cưa | Claude | 2–3 giờ | Frame time trước/sau; mép đạn và mép quái ở 1080p, dpr 1 |
| L3 | Khói của Scatter và Star Mortar chuyển sang pool khói trộn thường (smokeBody, soot), đặt sau lớp sáng | Khói đang cộng sáng thành sương sữa | Claude | 2–3 giờ | Tờ khung f5–f8: khói làm sân tối đi, không sáng thêm |
| L4 | Nâng ô súng: ô 1–2 ở 30–44 %, ô 3–4 ở 47–58 % chiều cao, nằm ngoài hai tường. Dùng bản A (cách mép màn 2,5 %); ô khóa thu thành chip | Mắt đang phải nhảy 47 % chiều cao màn giữa chữ và quái | Claude | 0,5–1 ngày | Lệch dọc chữ–bầy ≤ 10 % ở 720p, 1080p và 4:3; không che làn; kiểm protectedRects, chip rift, số sát thương; chơi hết chương 1; chấm C |

### Đợt 2: tuần này

| # | Việc | Vì sao | Ai | Công | Chấm thế nào |
|---|---|---|---|---|---|
| D5 | Look "Epic" cho High/Ultra, đặt sau một cờ: MeshStandardMaterial dùng normal và roughness; ramp ≤ 0,25 hoặc tắt; rim mảnh; viền mực tắt hoặc 1 px; phủ màu quái ≤ 0,1; grade bỏ lift, tăng tương phản. Bật mặc định khi có O1 | Đây là gốc của cảm giác "đồ chơi" | Claude | 2–4 ngày, 2–3 vòng chấm | Ảnh cùng camera đặt cạnh ảnh mẫu; sau khi bật mặc định thì chấm C (không còn cờ) |
| D6 | GTAO hoặc N8AO ở High/Ultra (tốn ≤ 2 ms), normal map cho ô đất, tăng tương phản mid, sương theo độ cao | Ánh sáng đang phẳng, không có AO | Claude | 1–2 ngày | `dh-bench` (Ultra main hiện 12,75–13,77 ms); tương phản bóng/sáng trên đồng cỏ (hôm nay L 113/173); chấm C |
| D7 | Shader nước mới: hai lớp normal trôi, Fresnel, specular theo nắng, màu và bọt theo khoảng cách tới bờ, bọt mềm; Ultra thêm phản chiếu | Nước đang phẳng như cartoon | Claude; texture CC0 hoặc `waternormals` của three (MIT), ghi vào `THIRD_PARTY.md` | 1–2 ngày | Trước/sau `compare-z06-pond`, `ford`, `river-bridge`; chấm C |
| D8 | Cho Ultra khác High thật: bake đất 4096 hoặc vẽ ô đất trực tiếp gần camera; LOD scatter xa hơn; impostor 512 px, 8 góc, có atlas normal (hoặc lưới Medium tới 70–85 m) | Đất đang bị phóng 1,8–3,6 lần; rừng xa chỉ chụp một góc | Claude | 1,5–2 ngày | `dh-bench` Ultra; ảnh ở zoom 0,6; chấm C |
| D9 | Thử model từ gói miễn phí dùng thương mại được (Poly Haven, Quaternius, KayKit; chủ dự án cho phép 01/11): thông, đá, vách | File gốc Tripo chỉ 2.786–9.922 tam giác, nên Ultra vẫn chỉ ở mức trung bình | Claude: tìm gói, kiểm giấy phép trên trang nguồn, ghi `THIRD_PARTY.md`, thử trong cảnh | 1 ngày | Chấm C trên một vùng cảnh. Không tới 8,5 thì chuyển sang O2 |
| L5 | Làm lại đạn 5 súng, đủ năm pha, nhiều lớp; phần mã làm trước (quy cách ở dưới bảng) | Đạn hiện chỉ là gradient mềm | Claude | 3–5 ngày | VFX_STANDARD §5.6; tờ khung từng súng ở 720p và 1080p; số đo ghi dưới bảng; chấm C |
| L6 | Thêm pha thiếu: gồng ở nòng cho Scatter, Rail, Mortar (dùng lại CHARGE); đèn lúc phóng Mortar; vệt suốt đường cung; dư âm (decal, khói tối) | Scatter, Rail, Mortar chưa đủ năm pha (TS-M1-16) | Claude | gộp vào L5 | Bảng kiểm năm pha của từng súng |
| L7 | Gân quái đổi sang màu phe địch (tím hoặc đỏ thẫm), theo VFX_STANDARD dòng 397. Vòng điểm rơi Mortar đổi sang cam nhạt viền trắng, vì đỏ chỉ dành cho đòn của quái (§3.6.3) | Heat Beam đang chìm vào màu quái và sàn | Claude, sau khi có sắc màu từ O5 | 0,5 ngày | Tương phản thẻ chữ ≥ 7:1; tờ khung Heat Beam bắn vào bầy quái; chấm C |
| L8 | Chữ "sống" trong ô súng: làm trong game trước, thử ở `tools/typing-feedback-lab/` (quy cách ở dưới bảng) | Chữ chờ đang tĩnh hoàn toàn | Claude | 1 ngày; 2–3 ngày nếu đưa vào kit | Chơi thật ở 720p và 1080p: lỗi gõ không tăng so với bản tĩnh; có thể tắt bằng chế độ giảm chuyển động (WCAG 2.2.2). Nếu đưa vào kit: hai giám khảo cùng từ 9, chủ dự án ký (O8) |
| L9 | Vụ nổ Mortar: mờ dần theo mặt sàn, soft particle, giới hạn cỡ billboard | Có mép cắt thẳng | Claude | vài giờ | Trước/sau `compare-zoom-phao-burst` |
| L10 | Flipbook cho đạn: lóe nòng, tóe tia lửa, cầu lửa 6×6 ở 1024², khói, dải lửa 512×128 liền mép, dải điện | Shader một mình không đủ chất liệu | Clip: Claude làm bằng Firefly Video trong tab của chủ dự án (không tốn credit, có giới hạn tốc độ). Texture tĩnh: Antigravity (Codex đang hết hạn mức). Cần O6 trước | 1–2 buổi tạo, Claude ingest | Chấm trong game, không chấm clip rời |

**Quy cách L5, từng súng**

- **Pulse Gun:**
  - Đầu đạn plasma hình viên nhộng 0,5 × 0,12 m (≥ 28 × 8 px ở 1080p).
  - Lõi xanh-trắng HDR, chiếm ≤ 25 % bề ngang; vỏ xanh điện bão hòa.
  - Ribbon thon 1,5–2 m, có nhiễu nhấp nháy.
  - Lúc trúng: lóe ≤ 40 px, 6–10 tia lửa, vòng sóng 0,6 m.
- **Heat Beam:**
  - Lõi vàng-trắng HDR 0,10–0,14 m, mép sắc.
  - Thân cam-đỏ bão hòa 0,5 m, nhiễu FBM cuộn 12–20 m/s, mép ăn mòn.
  - Haze nằm dưới ngưỡng bloom.
  - Cột sàn 3,6 m thu lại thành rãnh cháy hẹp, kèm vệt xém tối trộn thường.
  - Điểm chạm có lóe và bắn tóe.
- **Scatter Gun:**
  - 3 lưỡi lửa flipbook.
  - 7 viên sáng (≥ 20 × 6 px ở 720p), vệt 1,2 m.
  - Khói tối.
- **Rail Gun:**
  - Lõi trắng-tím HDR 0,06 m, thân tím điện 0,25 m.
  - Hai ribbon xoắn quanh đường bắn.
  - Ngôi sao ≤ 12 % chiều cao màn.
  - Khói tối dọc đường bắn trong 0,6 s, vết xém trên sàn.
- **Star Mortar:**
  - Đầu đạn sáng, vệt lửa-khói suốt đường cung.
  - Cầu lửa đúng bán kính 2,5 m (±10 %).
  - Cột khói tối, hố cháy có vết nứt sáng.

**Quy cách L8**

- Mỗi chữ cái là một span; chỉ animate transform và opacity.
- Sóng 1,5 px ở 720p (2 px ở 1080p), chu kỳ 2,4 s, mỗi chữ lệch pha 0,12 rad.
- Chữ đầu thở sáng theo màu súng, 0,4 → 0,9, chu kỳ 1,6 s.
- Vệt sáng quét qua mỗi 2,8–3,4 s; các ô lệch nhịp nhau.
- Đứng im 120 ms khi một từ bị khóa.
- Không xoay, không phóng quá 1,03, không mờ dưới 0,85.
- Chế độ giảm chuyển động: chỉ còn quầng tĩnh.
- Thêm các hiệu ứng theo phím của Typing Break: T1 (chữ đóng dấu 2,6× → 1× trong 50 ms), T3, T7 và T8.

### Đợt 3: cần chủ dự án

| # | Quyết định hay việc tay | Đề xuất của Claude |
|---|---|---|
| O1 | Bỏ kiểu "painted toy diorama" (art-pipeline 05 §2.1) để theo ART_DIRECTION 3.2 painterly-realistic ở High/Ultra | Duyệt. Claude đưa ảnh so cùng camera (D5) trước khi bật mặc định |
| O2 | Nếu D9 không tới 8,5: dựng lại cây, đá, quái trên Tripo web ở mức mặt cao nhất, PBR 2K có normal. Cùng lúc dựng 6 model mốc của phiếu 124 (khoảng 180 credit) | Thử gói miễn phí trước. Mốc thì làm ngay, vì không có gói thay được cổng ải hay tượng rồng |
| O3 | Thử camera Dragonhold ở zoom 0,85, pitch 50 (quái hiện chỉ khoảng 45 px) | Claude thử và chụp; anh duyệt nếu lối chơi đổi |
| O4 | Sửa VFX_STANDARD dòng 379 ("giữ bloom… không sửa bloom"), vì chính bloom làm đạn nhòe | Duyệt. L1 chỉ gộp khi có câu này |
| O5 | Sắc phe địch cho quái Last Line: tím hay đỏ thẫm | Tím (tách xa nhất khỏi cam của Heat Beam và lam của Pulse) |
| O6 | Danh sách flipbook Firefly của L10 (mã và số lượng) | Duyệt 6 loại ở L10 |
| O7 | Ô súng: bản A (an toàn) hay bản C (sát tường, gần hơn, nhưng ô khóa đè lên dải sọc ở mép tường) | Làm A trước; anh xem ảnh `compare-mock-c` nếu muốn C |
| O8 | Ký cuối cho chữ "sống" nếu đưa vào kit dùng chung | Ký sau khi hai giám khảo cùng từ 9 |
| O9 | Xác nhận changelog model-tiers mục 12: ở camera chơi, cây xa vẽ lưới Medium 4.000 tam giác, đá xa dưới 2.000 | Xác nhận |
| O10 | Các quyết định cho nhân vật Last Line | Xem mục 4.2 |

## 4. Last Line: nhân vật chính (nữ xạ thủ và drone)

### 4.1 Hôm nay

- **Người chơi điều khiển tàu Vanguard**, khoảng 100×80 px ở 720p. Bản Ultra 720p có 34 draw call và 344.080 tam giác.
- **Camera ở góc pitch 36°, FOV 42** (`scene.ts:40-44`). Nhân vật sẽ được nhìn từ sau lưng, chếch 46° từ trên xuống.
  - Chiều cao trên màn theo tỉ lệ nhân vật:

    | Cao thật | 720p | 1080p |
    |---|---|---|
    | 1,8 m | 47 px | 69 px |
    | 2,6 m | khoảng 68 px | 100 px |

  - Kính cyan quay về phía quái nên người chơi không thấy.
- **Đã có:**
  - Hướng B, Lightbearer (chủ dự án chọn 29/10, ART_DIRECTION §4.3).
  - Ảnh nguồn Tripo của phiếu 156: `games/typing-survival/art-src/models-src/lightbearer-{front,back,left}.png` và `sentinel-{pulse,heat,scatter,rail,mortar}.png`.
  - Tờ tư thế của phiếu 181: `art-src/anim-ref/keyposes-lightbearer.png`.
  - `results-lose-bg.png` (nữ anh hùng quỳ, súng canh trắng vàng mắt cyan) và `menu-bg.png`. "Robot hỗ trợ" mà anh nói chính là súng canh của ta.
- **Chưa có:**
  - GLB nhân vật, drone hay súng.
  - Kit `shared/game-kit/anim/`.
- **Ràng buộc:** các bến cùng bắn trong một tick (`weapons.ts:163-185`), nên một đôi tay không cầm được cả hai súng.

### 4.2 Quyết định cần anh

1. **Chia bến:**
   - Nhân vật bắn súng của bến 1 (thẻ trái).
   - Drone ở vai phải bắn súng của bến 2 (thẻ phải) và làm việc hỗ trợ.
   - Chỉ đổi phần hiển thị: sim, ván vàng s0 và hash chương giữ nguyên.
   - Đề xuất: duyệt.
2. **Súng cầm tay (5 model mới) hay súng đeo tay** (dùng thẳng 5 ảnh sentinel của 156). Đề xuất: cầm tay, đúng ý "nhân vật cầm súng" và có animation riêng cho từng súng.
3. **Tỉ lệ:** nhân vật khoảng 2,6 m, drone 0,9–1,0 m. Đề xuất: duyệt.
4. **Thử camera 30°**, sau khi chốt bố cục ô súng (L4). Ở góc này, người 2,5 m cao 107 px ở 720p và quái to thêm 30–50 %. Đây là số tính ra, chưa thử trong trình duyệt.
5. **Bỏ tàu Vanguard khỏi trận.**
6. **Tên thật cho nhân vật** (Lightbearer là tên tạm), và sửa bible §4.3: hiện ghi hai súng canh và tay giơ phép.
7. **Dựng 7 model trên Tripo web**, khoảng 1–2 giờ:
   - nhân vật, drone và 5 súng;
   - khoảng 210 credit, khoảng 300 nếu phải làm lại.

Quaternius UAL1 (CC0) không cần anh duyệt riêng: lệnh 01/11 đã cho phép gói miễn phí dùng thương mại được (`docs/OWNER_QUEUE.md`). Claude sẽ kiểm giấy phép trên trang nguồn và ghi vào `THIRD_PARTY.md`.

### 4.3 Các bước

| Bước | Ai | Việc | Công |
|---|---|---|---|
| 0 | Chủ dự án | Quyết các mục 4.2 | — |
| 1 | Claude | Thử tỉ lệ bằng hình nộm Mannequin (`human-base-animations.glb` của Mesh2Motion), chỉ ở `?debug=1`, không phát hành | 0,5 ngày |
| 2 | Antigravity (Codex khi có lại hạn mức) | Vẽ nhân vật bản 2 nhìn trước, sau, trái, phải, cho khớp ảnh anh gửi (mũ màu than, áo choàng chỉ vàng, tóc dài). Drone nhìn trước, sau, cạnh, trên. 5 súng cầm tay. Tờ tư thế từng súng (nhắm, đỉnh bắn, thu), nhìn từ camera trận và từ cạnh. Một ô kiểm nhìn từ sau, chếch 45°, ở 256 px. Claude chấm, mỗi ảnh phải ≥ 8,5 | 14–18 ảnh, 1,5–2 ngày |
| 3 | Chủ dự án, Tripo web | 7 model. Nhân vật và drone dùng multiview; mỗi súng một ảnh. Chọn mức mặt cao nhất, PBR 2K có normal map. Tắt Smart Low Poly và Auto Rig. Xuất GLB vào `art-src/3d/` | 1–2 giờ |
| 4 | Claude, Blender | Xem chi tiết dưới bảng | 2–3 ngày |
| 5 | Claude | Clip theo mục 4.5, kiểm trong Anim Lab | 3–4 ngày |
| 6 | Claude | `hero.ts` và `drone.ts` theo giao diện Pilot (mục 4.7), định tuyến theo bến, VFX năm pha ở nòng thật, `warm.ts` biên dịch shader mới | 4–5 ngày |
| 7 | Claude, hai giám khảo, chủ dự án | Chụp ở 720p và 1080p, đo perf. Model phải ≥ 8,5; animation nhân vật là hệ dùng chung nên cần hai giám khảo cùng ≥ 9. Chủ dự án duyệt cuối | 1 ngày |

Việc của Claude ở bước 4:

- Dọn mesh, đổi đơn vị sang mét.
- Làm các bậc Ultra/High/Medium theo MODEL_QUALITY §2b; nhân vật chính ở bậc High phải ≥ 20.000 tam giác.
- Rig người của Mesh2Motion (66 xương), trọng số bone heat, khóa mũ và các mảnh giáp. Không dùng auto rig của Tripo (CHARACTER_ANIMATION §5.3).
- Thêm chuỗi xương cho áo choàng (3 vạt × 4 xương) và cho tóc.
- Đặt socket:
  - Nhân vật: `FX_HAND_R/L`, `FX_CORE`, `FX_BACK_CORE`, `FX_VISOR`.
  - Súng: `FX_MUZZLE` (Pulse có thêm `_L/_R`), `FX_CORE`, `FX_GRIP`, `FX_SUPPORT`, `FX_EJECT`.
  - Drone: `FX_EYE`, `FX_RING`, `FX_THRUST`.

Tổng công:

| Ai | Công |
|---|---|
| Antigravity hoặc Codex | 1,5–2 ngày |
| Chủ dự án | 1–2 giờ trên Tripo, 210–300 credit |
| Claude | 12–15 ngày |

Bản chơi được đầu tiên có khoảng 4–5 ngày sau khi có GLB.

### 4.4 Prompt cho Tripo

> **Sửa màu 01/11, khoảng 07:55** (theo ChatGPT duyệt map 1 Last Line): vàng dành cho Pack Leader. Nhân vật, drone và súng dùng **gốm ngà và graphite**, không dùng vàng hay trắng-vàng. Áo choàng xanh đen, chỉ có đường ngà rất mảnh, bỏ viền vàng. Drone là giọt nước nhọn hơn, chỉ một khe cyan hẹp. Ở mọi prompt dưới đây, đọc "white-gold" thành "ivory".

Giữ nguyên văn các khối MODEL, TAIL-HERO và TAIL-GUN, nền `#00FF00` và phép kiểm 1254 px của phiếu `docs/codex-queue/156-ts-lightbearer-tripo.md`.

**Nhân vật.** Dùng MODEL và TAIL-HERO, bốn góc trước, sau, trái, phải. Đính kèm `results-lose-bg.png`, `menu-bg.png` và `lightbearer-front.png`.

> The Lightbearer, a slim female armoured guardian: white-gold ceramic armour plates over a dark graphite bodysuit; a dark graphite helmet covering the whole head with a glowing electric-cyan visor slit and two swept white-gold crest fins; a short bundle of long dark hair falling from the back of the helmet to the shoulder blades; a deep-navy cape with fine white-gold filigree lines and a gold hem, hanging from both shoulders in three separate panels that end at mid-calf and never cover the arms; thin cyan light lines along the armour seams, down the back plate and along the cape edges; a small glowing cyan core on the chest and a matching one between the shoulder blades; empty open armoured hands.

Chữ cho ô text của Tripo, nếu cần:

> female sci-fi guardian, white-gold ceramic armour, dark graphite helmet with cyan visor, navy three-panel cape with gold filigree, A-pose, empty hands, game hero asset

Thêm một ô kiểm, không đưa vào Tripo: nhìn từ sau, chếch 45° từ trên, ở 256 px. Ô này phải đọc ra được áo choàng, các đường cyan và hai vây mũ.

**Drone.** Dùng TAIL-GUN, bốn góc trước, sau, cạnh trái, trên. Đính kèm drone cắt từ `menu-bg.png` và `results-lose-bg.png`.

> A floating support drone companion about 0.9 m long: a smooth white-gold ceramic teardrop shell over a dark graphite core, one large round glowing electric-cyan eye lens at the front, two short swept stabiliser fins, a cyan light ring and a small thruster glow on its back, a slim weapon emitter under the eye; no legs, no arms, no stand.

**Năm súng cầm tay.** Dùng TAIL-GUN, nhìn ba phần tư từ hơi cao, không có tay cầm vào. Đính kèm `sentinel-*` của 156 và icon `gun-*`. Câu chung cho cả năm súng:

> white-gold ceramic shell over graphite, hand-held, one connected solid object

| Súng | Prompt |
|---|---|
| Pulse Gun | "compact twin-barrel energy carbine, short front grip, cyan energy ring round both muzzles, about 0.7 m" |
| Heat Beam | "two-handed beam projector with a long focusing lens barrel, an orange-gold core seen through a window on top, side carry handle, about 1.0 m" |
| Scatter Gun | "wide shotgun with five short barrels in a flat fan, pump grip, cyan vents, about 0.8 m" |
| Rail Gun | "long rifle with two parallel rails and cyan coils between them, shoulder stock, top scope, about 1.3 m" |
| Star Mortar | "shoulder-carried launcher, short wide tube ringed by star-shaped vents, grip and shoulder rest, heavy white-gold armour, about 1.0 m" |

### 4.5 Animation

Nguồn clip CC0 có sẵn trên máy: `games/typing-defense/art-src/anim/mesh2motion/human-{base,addon}-animations.glb`, gồm 87 và 75 clip. Bộ này không có clip súng trường hai tay, bơm shotgun hay ống phóng vác vai. Mọi clip bắn đều phát sự kiện release. Phần nâng súng tua theo tiến độ gõ (pha A).

**Clip chung**

| Clip | Dùng khi | Gốc hoặc ghi chú |
|---|---|---|
| Idle_Combat | đứng chờ | Idle_A hoặc Idle_Shield, thêm lò xo áo choàng |
| Idle_Fidget | đứng lâu | |
| Strafe_L/R | trôi ngang ±1,6 m | |
| Xoay thân | nhắm ±50° | thủ tục: cột sống và hông |
| Load | xong một từ | 0,35 s, tay trái kéo vòng ký hiệu vào súng |
| KeyPulse | mỗi phím đúng | clip cộng, nhẹ |
| Hit_Light | trúng đòn thường | Hit_Chest |
| Hit_Heavy | bị phá phòng tuyến (breach) | Hit_Knockback |
| Drain_Flinch | bị hút giáp (drain) | Idle Hurt |
| Kneel/Rise | giáp thấp | |
| Intro | vào trận | Land_Three_Point |
| Victory | thắng | Victory, Victory Fist Pump |
| Defeat | thua | quỳ cúi đầu như `results-lose-bg`, Kneeling Tired. Không có clip chết |

**Theo súng**

| Súng | Clip | Gốc hoặc ghi chú |
|---|---|---|
| Pulse Gun | PG_Raise | 0,15 s, tua theo tiến độ gõ |
| | PG_AimLoop | trộn Pistol_Aim Up/Neutral/Down theo độ sâu mục tiêu |
| | Giật từng viên | lò xo cộng: 0,05 m, 1,2° |
| | PG_Reload | Pistol_Reload |
| | PG_Lower | |
| Heat Beam | HB_Brace | 0,2 s, gốc Two-hand Blast |
| | HB_BurnLoop | IK nhắm theo beamX, rung 0,02 m ở 12 Hz |
| | HB_Vent | pha F: xả hơi, lùi nửa bước |
| | HB_Lower | |
| Scatter Gun | SG_Hip | |
| | SG_Fire | mỗi loạt; giật 0,28 m, 4° |
| | SG_Pump | clip cộng 0,18 s |
| | SG_Lower | |
| Rail Gun | RG_Shoulder | 0,25 s |
| | RG_ArmedLoop | |
| | RG_Charge | 0,15 s |
| | RG_Fire | giật 0,4 m, 5°, về trong 0,26 s |
| | RG_Cycle | |
| | RG_Lower | |
| | | gốc chung của Rail: Bow Pull Hold/Release |
| Star Mortar | SM_Plant | quỳ một gối, ống trên vai phải chếch 45° |
| | SM_Fire | thân nén 0,08 m |
| | SM_Reload | 0,4 s |
| | SM_Rise | |

**Drone** không rig, chuyển động bằng mã:

- lơ lửng, bám vai phải (x +0,9 đến +1,0; y 2,1–2,3; z 0,3);
- xoay về mục tiêu, giật dọc trục theo số KICK;
- quay nhanh khi Rail nạp, nghiêng xuống khi Heat Beam cháy, bật lên khi Star Mortar bắn;
- vòng sáng đổi màu theo súng.

Phần súng có thể nhẹ đi nếu UAL1 có clip súng; điều này chưa kiểm.

### 4.6 Drone hỗ trợ (chỉ hiển thị, sim không đổi)

1. Bắn súng của bến 2.
2. Khi có gói sửa giáp (`EV.support`): bay lên đón gói, ghé lưng nhân vật, hiện vòng xanh.
3. Khi quái trinh sát bắn (`EV.foeShot`): kẻ vạch ngắm tới viên đạn, lóe khi viên đạn bị bắn hạ (`shotDown`).
4. Khi nhân vật trúng đòn, bị phá phòng tuyến hay bị hút giáp (`playerHit`, `breach`, `drain`): lóe khiên lục giác lam phía trước nhân vật.
5. Khi có rift: quay về phía rift và phát nhịp báo.
6. Theo chuỗi gõ: vòng sáng, áo choàng và lõi lưng sáng dần.
7. Thắng: drone lượn quanh nhân vật. Thua: drone rơi, tắt đèn bên cạnh nhân vật đang quỳ.

Nếu drone giúp thật trong luật chơi (khiên đỡ giáp, nhặt mảnh) thì sim đổi. Khi đó phải cân lại B1–B9, ván vàng `s0-trace` và hash 152 lượt chương. Để việc này sang R2.

### 4.7 Cắm vào code

Giao diện Pilot, cho cả `hero.ts` và `drone.ts`:

```
muzzle(out, which, bay)
core(out, bay)
kick(name, side, bay)
cue(prio, x, z)
hurt()
boost()
drawFx()
```

Chỗ phải đổi:

- `shots.ts:132-240`;
- `beams.ts:62`, `:91`, `:138`, `:191`: Heat Beam và Rail lấy nòng theo bến;
- `typing-feel.ts:144-357`: tia ký tự đi vào `FX_CORE` của súng thuộc bến đang nạp;
- `combat.ts:219-254`, `:416`;
- `main.ts:94`.

Ràng buộc:

- Nhân vật đứng ở z ≈ 0; mũi súng không vượt `NOSE_MAX_Z` (2,1) của sim.
- Nhân vật nằm trong cột trống 324 px (`hud.ts:66`).
- Mục mới trong manifest: `heroes/lightbearer`, `props/drone`, `props/gun-*`.
- Chế độ giảm chuyển động: không trôi, không lao, độ giật × 0,3.

Kiểm:

- Trace s0 và hash chương giống hệt trước.
- `survival-s1-perf` có programsSteady.
- `survival-feel`: f8 và nền dưới dòng chữ tăng ≤ +0,02.

### 4.8 Rủi ro

- **Nhân vật quá nhỏ.** Cách giảm: tỉ lệ 2,6 m; thiết kế đọc được từ lưng (hoa văn vàng trên áo choàng, đường cyan trên giáp lưng, lõi lưng); viền fresnel; cân nhắc camera 30°.
- **Áo choàng và tóc xuyên qua chân hay súng.** Cách giảm: chia vạt, thêm xương va chạm, bảng kiểm giãn lưới trong Anim Lab.
- **Clip súng tự làm khó đạt 9.** Cách giảm: dùng UAL1 nếu có clip súng, dùng tờ tư thế làm khung.
- **Perf.** Ước tính thêm 60–100 nghìn tam giác (+20–30 %) và khoảng 8 draw call. Phải đo bằng `survival-s1-perf`.
- **Bố cục.** Bố cục HUD (L4) phải chốt cùng vị trí nhân vật.
- **Ảnh menu và kết quả.** Đổi bible thì có thể phải vẽ lại một phần các ảnh này.

## 5. Ảnh chụp và số đo

Tất cả nằm trong `tmp/` của từng game. Ảnh thô đã xóa bằng `capture-prune`.

**Dragonhold** (`/Users/toandx/htdocs/typing-game/games/dragon-hold/tmp/diag-0111/`):

- `compare-home-play-vs-dev.jpg`, `sheet-closeups-play-vs-dev.jpg`
- `compare-z06-trees-nw.jpg`, `compare-z06-trees-sw.jpg`, `compare-z06-cliff-w.jpg`
- `compare-z06-river-bridge.jpg`, `compare-z06-pond.jpg`, `compare-z06-ford.jpg`, `compare-z06-meadow-se.jpg`
- `compare-foe-closeup.jpg`, `compare-game-wave-play.jpg`, `compare-game-wave-dev.jpg`
- `numbers.json`, `glb-served-high.json`

Hai ảnh từ các nhánh chưa gộp:

- `/Users/toandx/htdocs/typing-game/games/.wt-dh-models/tmp/model-tiers/sheets/game-camera-high-before-after.jpg`
- `/Users/toandx/htdocs/typing-game/games/.wt-dh-mappilot/tmp/map-pilot-r2/compare-road2/1280x720-default-vs-ref.jpg`

**Last Line** (`/Users/toandx/htdocs/typing-game/games/typing-survival/tmp/diag-0111/`):

- Đạn:
  - `sheets/sheet-closeup-{xung,tia,tan,ray,phao}-1920x1080.jpg`
  - `guns-1080/1920x1080/sheet-f5-{xung,tia,tan,ray,phao}-1920x1080.jpg`
- Bloom: `sheets/compare-bloom-tonemap-1920x1080.jpg`, `sheets/compare-ultra-medium-1920x1080.jpg`
- Vụ nổ Mortar: `sheets/compare-zoom-phao-burst-1920x1080.jpg`
- Bố cục:
  - `sheets/layout-mock-sheet.jpg`, `sheets/layout-mock-c-sheet.jpg`
  - `sheets/compare-{now,mock-a,mock-c}-1920x1080.png`
- Số đo:
  - `vfx-numbers-1920x1080.json`, `tia-profile-1920x1080.json`
  - `layout/1280x720/layout-natural.json`, `layout/1920x1080/layout-mock.json`, `layout-c/1920x1080/layout-mock.json`
- Nhân vật: `hero/sheet-hero-scale-720.jpg`, `hero/sheet-hero-refs.jpg`, `hero/hero-today-{1280x720,1920x1080}.json`, `hero/hero-today.mjs`

## 6. Sổ nợ dưới 8,5

| Game | Mục | Điểm hôm nay | Nơi xử lý |
|---|---|---|---|
| Dragonhold | Cảnh thế giới: đất, cây, đá, nước, quái | 4 | D1–D9, O1–O3 |
| Dragonhold | Màn tựa 119 | 7,5 | phiếu 251 |
| Dragonhold | Lửa rồng C, mặc định | 7 và 7,5 | gói VFX có sẵn (`ASSET_SEARCH_BRIEF.md`) |
| Last Line | Đạn 5 súng | 3,5–5 | L1–L3, L5–L7, L9, L10 |
| Last Line | Ô súng thấp, chữ chờ tĩnh | — | L4, L8 |
| Last Line | Nhân vật chính (tàu Vanguard) | 4 | mục 4 |
| Last Line | 5 icon phiếu 247, gắn tạm | dưới 8,5 | giao lại khi có hạn mức |
| Wordwoven | Map 3D của map 1 | dưới 8,5 | `docs/OWNER_QUEUE.md` |
