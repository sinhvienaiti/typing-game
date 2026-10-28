# Phiếu 139 · Dragonhold · Bản đồ và thẻ chữ (11 ảnh, P1)

**Nguồn:** kiểm kê hình ảnh UI map 1, 29/10 (`docs/games/map1/UI_IMAGERY.md`; dàn ý `UIC-DH-3` trong `docs/games/map1/UI_IMAGERY_CODEX.md`). Chủ dự án 28/10 tối: mọi chi tiết UI phải có hình thật, không chỉ có chữ; không hình vẽ bằng mã. Hướng mỹ thuật: `docs/games/ART_DIRECTION_2026-10-28.md`.

**Báo cáo:** `docs/codex-queue/139-report.md`, thư mục `_review/139/` của game.

## Luật chung (phiếu ảnh)

**Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.

**Luật điểm:**
- Ảnh 2D đạt từ 8 điểm (`docs/games/ART_ACCEPTANCE.md` §2.2), chấm **so với game thương mại**.
- Tham chiếu mức hoàn thiện: `games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp`.
  - Xem HUD của ảnh đó: icon kỹ năng tròn trong vòng kim loại, khung chân dung có huy hiệu, icon hệ thống rõ nét.
  - Lấy mức hoàn thiện, không chép nội dung.
- Lỗi sửa được thì sửa bằng công cụ trước: ImageMagick 7, `tools/art-normalize`, script riêng.
- Chưa đạt thì sửa prompt đúng chỗ thiếu. Tối đa **3 lượt sinh mỗi ảnh**.

**Lượt sinh và file:**
- Mọi lượt giữ `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3).
- Bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`.
- **File giao mỗi ảnh:**
  - `<tên>.png`: bản gốc 1024 × 1024, sRGB, RGBA sau khi tách nền;
  - `<tên>.256.png`, `<tên>.128.png`, `<tên>.64.png`: thu Lanczos trực tiếp từ bản gốc;
  - không làm nét bản 64.

**Prompt:**
- Viết bằng tiếng Anh.
- Mỗi prompt = khối STYLE mới của AD cho game đó + khối KIND (ICON, PORTRAIT hay PART) của phiếu + phần riêng của ảnh + dòng nền.
- **style: to take the art director's new STYLE block.**

**Nền:**
- Theo tài liệu định dạng của game:
  - Dragonhold và Wordwoven: nền khóa phẳng `#FF00FF` (M) hay `#00FF00` (G). Chọn màu không có trong vật. Rồi tách alpha.
  - Last Line: nền trong suốt như bộ 015. Công cụ không cho trong suốt thì dùng M rồi tách.
- **Lề:** vật nằm giữa. Hộp bao (alpha > 16) có cạnh dài bằng 68–72 % cạnh ảnh, lệch tâm ≤ 2 %. Như phiếu 108.

**Cấm:**
- chữ, số, chữ cái, logo, chữ ký, khung hay viền vẽ trong ảnh. Tên tiếng Anh do game đặt bằng font;
- ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`;
- mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo);
- dev server, trình duyệt, mạng ngoài công cụ tạo ảnh;
- ghi vào game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
- đụng `.wt-*`.

**Kiểm bắt buộc, ghi số vào báo cáo:**
1. **KA1 md5:**
   - `md5 -r` mọi file trong các thư mục đích trước khi ghi, lưu `_review/139/md5-before.txt`;
   - chạy lại sau khi giao, lưu `md5-after.txt`;
   - `diff` chỉ có dòng thêm.
2. **Khổ:**
   - `magick identify -format '%f %wx%h %[channels]\n'` cho mọi file giao;
   - bản gốc 1024², `srgba`; ba bản thu đúng 256², 128², 64².
3. **Alpha sạch:**
   - ngoài dải mép 3 px quanh vật, mọi pixel có alpha 0 hay 255;
   - pixel có alpha > 0 mang màu nền khóa (hue lệch ≤ 15° so với màu khóa, S > 0,5) chiếm ≤ 0,2 %;
   - ghi hai số đó cho từng ảnh.
4. **Đọc được ở cỡ trong game:**
   - thu bản gốc về đúng cỡ 720p và 1080p ghi trong bảng của phiếu;
   - đặt lên màu nền HUD của game:
     - Dragonhold: vỏ cây `#2b2118` và kem `#f1e3c4`;
     - Wordwoven: ngọc sẫm và đá vôi (lấy từ `panel-large` của 115 khi có; tạm dùng `#1f3b33`, `#e8e1cf`);
     - Last Line: than chì `#14181f` và thép sáng `#8c96a3`;
   - **tương phản:** chênh luma trung bình giữa vật và nền ≥ 0,25 trên ít nhất một trong hai nền tối;
   - **dáng riêng:** ở 32 px, mặt nạ alpha của hai ảnh bất kỳ trong phiếu có IoU ≤ 0,80. Cặp sáng/tắt của cùng một vật thì ngược lại, IoU ≥ 0,95;
   - ghi bảng IoU lớn nhất từng ảnh.
5. **Tờ xem** `_review/139-sheet.jpg`:
   - hàng 1: bản gốc ở 256 px;
   - hàng 2: cỡ 1080p trên hai nền;
   - hàng 3: cỡ 720p trên hai nền;
   - hàng 4: cạnh 4 icon có sẵn của game đó và một mảnh của ảnh tham chiếu chủ dự án, cùng cao.
   - Dưới mỗi ảnh ghi tên.
6. **KA5 tự chấm:**
   - 5 tiêu chí của ART_ACCEPTANCE §2.2 (Đúng đề, Đọc được, Hợp bộ, Hình khối, Dùng tiếp), mỗi tiêu chí 0–2;
   - chấm ở cỡ gốc và cỡ 720p;
   - "Dùng tiếp" chỉ được 2 khi mọi kiểm số đo đạt.

**Báo cáo** `docs/codex-queue/139-report.md`, tiếng Việt:
- prompt đã sửa gì từng lượt;
- bảng số đo;
- điểm KA5;
- đường dẫn tờ xem;
- chỗ nào làm khác phiếu và vì sao.

Script đã dùng lưu ở `_review/139/`, chạy lại được.

**Xong khi:**
- đủ mọi ảnh và ba bản thu;
- mọi kiểm 1–5 đạt, có số;
- KA5 ≥ 8 cho mọi ảnh;
- có báo cáo.
- **Nhận** khi Claude chấm lại ≥ 8. Claude là người chép ảnh vào `public/` khi gắn.

## Chung cho Dragonhold

**Chung cho các phiếu Dragonhold:**
- **Phong cách:** style: to take the art director's new STYLE block (bible Dragonhold; khối STYLE-UI của phiếu 119: sử thi, ải núi, đá granite, lửa than hồng).
- **Định dạng theo** `docs/games/dragon-lane/art-requests/m0/05-icons.md`:
  - đọc được ở 32–64 px;
  - mỗi icon có dáng riêng, không chỉ khác màu (mù màu đỏ–lục, 05 §4.3);
  - nền M hay G.
- Không chép câu "storybook… misty pine forest".
- **Ảnh tham chiếu bắt buộc:**
  - `games/dragon-hold/art-src/ui/icons/skill-fire-breath.png` và `gold.png`, để xem cỡ vật trong ô;
  - ảnh chọn của 119 khi có.
- **Thư mục `_review`:** `games/dragon-hold/art-src/_review/139-*.jpg` và `_review/139/`.

## Việc của phiếu này

**Dòng phần tử:** DH-29, DH-31, DH-41, DH-43, DH-47, DH-49, DH-50.

**Chỉ được ghi:** `games/dragon-hold/art-src/ui/icons/<tên>*`, `_review/139*`, báo cáo.

| Tên | Nội dung (EN) | Cỡ 720p / 1080p |
|---|---|---|
| `lane-bridge` | an old stone arch bridge (Bridge Road) | 16 / 24 |
| `lane-stream` | a fast stream between rocks (Stream Road) | 16 / 24 |
| `lane-sky` | a spread bat-like wing (sky lane, flyers) | 16 / 24 |
| `slot-trap` | a square iron trap frame set in earth | 24 / 36 |
| `slot-house` | a round granite foundation pad | 24 / 36 |
| `slot-hold` | a planted war banner pole on a stone base (hold point) | 24 / 36 |
| `seal-lit` | a violet blight seal stone, glowing (Break Seal pip) | 10 / 14 |
| `seal-unlit` | the same seal stone, dark and cracked | 10 / 14 |
| `flag-pull` | a hand pulling a blight banner out of the ground | 18 / 22 |
| `swarm` | a cluster of three thorn ants (swarm tag) | 18 / 22 |
| `edge-arrow` | a short ember arrowhead (off-screen foe) | 10 / 14 |

**Kiểm riêng:**
- `slot-trap`, `slot-house`, `slot-hold` đọc được ở 24 px trên ảnh mặt đất của `sheet-04-words-crowd.jpg`.
- Cặp `seal-lit` và `seal-unlit` IoU ≥ 0,95.
