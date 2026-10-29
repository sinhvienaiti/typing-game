# Phiếu 152 · Last Line · Cài đặt, hồ sơ, Rift (11 ảnh, P2)

**Nguồn:** kiểm kê hình ảnh UI map 1, 29/10 (`docs/games/map1/UI_IMAGERY.md`; dàn ý `UIC-LL-4` trong `docs/games/map1/UI_IMAGERY_CODEX.md`). Chủ dự án 28/10 tối: mọi chi tiết UI phải có hình thật, không chỉ có chữ; không hình vẽ bằng mã. Hướng mỹ thuật: `docs/games/ART_DIRECTION_2026-10-28.md`.

**Chạy khi:** chủ dự án đã chọn hướng **B · Lightbearer** (29/10). Chạy sau 121 và 127, để có khối STYLE-UI và khung UI của hướng B.

**Báo cáo:** `docs/codex-queue/152-report.md`, thư mục `_review/152/` của game.

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
   - `md5 -r` mọi file trong các thư mục đích trước khi ghi, lưu `_review/152/md5-before.txt`;
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
5. **Tờ xem** `_review/152-sheet.jpg`:
   - hàng 1: bản gốc ở 256 px;
   - hàng 2: cỡ 1080p trên hai nền;
   - hàng 3: cỡ 720p trên hai nền;
   - hàng 4: cạnh 4 icon có sẵn của game đó và một mảnh của ảnh tham chiếu chủ dự án, cùng cao.
   - Dưới mỗi ảnh ghi tên.
6. **KA5 tự chấm:**
   - 5 tiêu chí của ART_ACCEPTANCE §2.2 (Đúng đề, Đọc được, Hợp bộ, Hình khối, Dùng tiếp), mỗi tiêu chí 0–2;
   - chấm ở cỡ gốc và cỡ 720p;
   - "Dùng tiếp" chỉ được 2 khi mọi kiểm số đo đạt.

**Báo cáo** `docs/codex-queue/152-report.md`, tiếng Việt:
- prompt đã sửa gì từng lượt;
- bảng số đo;
- điểm KA5;
- đường dẫn tờ xem;
- chỗ nào làm khác phiếu và vì sao.

Script đã dùng lưu ở `_review/152/`, chạy lại được.

**Xong khi:**
- đủ mọi ảnh và ba bản thu;
- mọi kiểm 1–5 đạt, có số;
- KA5 ≥ 8 cho mọi ảnh;
- có báo cáo.
- **Nhận** khi Claude chấm lại ≥ 8. Claude là người chép ảnh vào `public/` khi gắn.

## Chung cho Last Line

**Chung cho các phiếu Last Line:**
- **Hướng đã chọn (29/10): B · Lightbearer.** Khối STYLE-UI nguyên văn ở `docs/games/ART_DIRECTION_2026-10-28.md` §4.3; ảnh hướng `games/typing-survival/art-src/concepts/b-lightbearer-*.png`.
- **Phong cách:** style: to take the art director's new STYLE block (bible Last Line, khối STYLE-UI của phiếu 121 theo hướng đã chọn).
- **Định dạng theo** `games/typing-survival/docs/art-requests/015-s1-s2.md`:
  - hình khối gọn, đọc được ở 32–64 px;
  - nền trong suốt, lề 15 % như 108.
- Không chép câu "industrial pictogram… gunmetal" nếu hướng mới khác.
- **Ảnh tham chiếu bắt buộc:**
  - `games/typing-survival/art-src/ui/icons/gun-xung.norm.256.png` (cỡ vật);
  - ảnh chọn của 121 và khung của 127 khi có.
- **Thư mục `_review`:** `games/typing-survival/art-src/_review/152-*.jpg` và `_review/152/`.
- `--ui` của Last Line là 1 ở 720p và 1,5 ở 1080p.

## Việc của phiếu này

**Dòng phần tử:** LL-13, LL-14, LL-36, LL-44, LL-51.

**Chỉ được ghi:** `games/typing-survival/art-src/ui/icons/<tên>*`, `_review/152*`, báo cáo.

| Tên | Nội dung (EN) | Cỡ 720p / 1080p |
|---|---|---|
| `sfx` | a speaker grille with a spark | 20 / 30 |
| `music` | a waveform over a speaker | 20 / 30 |
| `shake` | a screen frame with motion ticks | 20 / 30 |
| `reduced-motion` | the same frame, calm, a small anchor | 20 / 30 |
| `read-aloud` | a mouth grille with sound arcs | 20 / 30 |
| `pace-director` | a dial with a hand that follows a curve | 20 / 30 |
| `quality` | a lens with three facets | 20 / 30 |
| `stat-wpm` | a speed gauge needle high | 24 / 36 |
| `stat-new-word` | a new data chip lighting up | 24 / 36 |
| `stat-evenness` | a level bar with a centred bubble | 24 / 36 |
| `rift` | a jagged violet tear in space | 24 / 36 |
