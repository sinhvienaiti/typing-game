# Phiếu 165 · Wordwoven · Vẽ lại 8 icon nhà và đèn lồng, thêm 2 icon khay mép

**Nguồn:** kiểm kê hình ảnh UI map 1 (`docs/games/map1/UI_IMAGERY.md`), dàn ý `UIC-WW-R1`; chấm nhận ảnh 29/10. Chủ dự án 29/10: Codex còn nhiều hạn mức, giao thêm việc.

**Báo cáo:** `docs/codex-queue/165-report.md`, thư mục `_review/165/` của game.

**Luật hậu kỳ (bắt buộc, 29/10):** `docs/games/ART_ACCEPTANCE.md` §5: tờ "bản sinh | bản hậu kỳ" cho mỗi ảnh; công cụ không được xóa, san phẳng hay phủ phần vẽ; ngưỡng số mâu thuẫn với tranh thì dừng và ghi lại; tự chấm trên bản hậu kỳ.

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
   - `md5 -r` mọi file trong các thư mục đích trước khi ghi, lưu `_review/165/md5-before.txt`;
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
5. **Tờ xem** `_review/165-sheet.jpg`:
   - hàng 1: bản gốc ở 256 px;
   - hàng 2: cỡ 1080p trên hai nền;
   - hàng 3: cỡ 720p trên hai nền;
   - hàng 4: cạnh 4 icon có sẵn của game đó và một mảnh của ảnh tham chiếu chủ dự án, cùng cao.
   - Dưới mỗi ảnh ghi tên.
6. **KA5 tự chấm:**
   - 5 tiêu chí của ART_ACCEPTANCE §2.2 (Đúng đề, Đọc được, Hợp bộ, Hình khối, Dùng tiếp), mỗi tiêu chí 0–2;
   - chấm ở cỡ gốc và cỡ 720p;
   - "Dùng tiếp" chỉ được 2 khi mọi kiểm số đo đạt.

**Báo cáo** `docs/codex-queue/165-report.md`, tiếng Việt:
- prompt đã sửa gì từng lượt;
- bảng số đo;
- điểm KA5;
- đường dẫn tờ xem;
- chỗ nào làm khác phiếu và vì sao.

Script đã dùng lưu ở `_review/165/`, chạy lại được.

**Xong khi:**
- đủ mọi ảnh và ba bản thu;
- mọi kiểm 1–5 đạt, có số;
- KA5 ≥ 8 cho mọi ảnh;
- có báo cáo.
- **Nhận** khi Claude chấm lại ≥ 8. Claude là người chép ảnh vào `public/` khi gắn.

## Chung cho Wordwoven

**Chung cho các phiếu Wordwoven:**
- **Phong cách:** style: to take the art director's new STYLE block (bible Wordwoven; khối STYLE-UI của phiếu 115: ngọc sẫm, đá vôi chạm, vàng lá, đồng Đông Sơn).
- **Định dạng theo** `games/typing-defense/docs/art-requests/td/03-2d-scenery-ui-vfx.md` §3 (khối ICON, PORTRAIT; nền G, M; cạnh dài ≥ 1024). Không chép câu "storybook" của §3.1.
- **Ảnh tham chiếu bắt buộc đính kèm:**
  - ảnh chọn của 115 khi có (`games/typing-defense/art-src/ui/frames/`), để icon hợp khung;
  - ảnh chủ đạo 113 khi có.
- Chưa có 115 thì phiếu chờ.
- **Thư mục `_review`:** `games/typing-defense/art-src/_review/165-*.jpg` và `_review/165/`.

## Việc của phiếu này: vẽ lại bộ icon kiểu cũ cho hợp bộ mới

**Vì sao:** chấm nhận ảnh 29/10 (`docs/codex-queue/accept-29-10/verdict.md`, mục "Chỗ lệch trong cùng game"): icon mới theo hướng sử thi sẽ đứng cạnh icon kiểu cũ (viền mực, khối hoạt hình, sách tranh). Điều kiện chạy của dàn ý `UIC-WW-R1` (`docs/games/map1/UI_IMAGERY_CODEX.md` §5) đã đủ: bộ cũ dưới 8 theo mức chợ.

**Cách làm (theo §5 của dàn ý):**
- giữ nguyên tên file cũ; bản mới ghi cạnh bản cũ thành `<tên>.v2.png` (cùng `.v2.256.png`, `.v2.128.png`, `.v2.64.png`, `.v2.tryN.*`). Không ghi đè. Claude đổi sang khi gắn;
- mỗi ảnh đính kèm ảnh cũ cùng tên làm tham chiếu vật, với dòng `Keep the same object identity as the attached image. Repaint it in the new style as described.` (giữ đồ vật, đổi phong cách);
- ảnh tham chiếu phong cách bắt buộc: khung đã nhận của phiếu 115 (`ui/frames/`: banner, portrait-ring, crest, divider) và `ui/title-epic/emblem.png`.

**Ảnh:** `buildings/keep`, `archer`, `cannon`, `barracks`, `gold-mine`, `farm`; `lanterns/lantern-unlit`, `lantern-lit` (8), ở `games/typing-defense/art-src/ui/`. **Thêm hai icon mới** cho khay mép báo lời gọi ngoài màn (làn L3, 29/10): `ui/tray/tray-arrow` (mũi tên đồng chạm, chỉ ra mép màn) và `ui/tray/tray-call` (vòng ngọc có ánh lời gọi, làm nền cho icon nhà); cỡ trong game 24 / 32 px

**Chỉ được ghi:** `games/typing-defense/art-src/ui/buildings/<tên>.v2*`, `ui/lanterns/<tên>.v2*`, `ui/tray/*`, `_review/165*`, báo cáo.

**Kiểm thêm:** như luật chung, cộng tờ so cũ–mới cùng cỡ 64 px và 32 px, hai hàng; mỗi icon mới đặt cạnh 4 icon đã nhận của bộ mới.

**Xong khi:** như luật chung.
