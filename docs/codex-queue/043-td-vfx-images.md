# Phiếu 043 · Lời Gọi · Ảnh VFX: chấm lại 11 flipbook, đưa về chuẩn alpha, vẽ thêm 3 ảnh (mực giấy)

**Luật:**
- Ảnh 2D đạt từ 8 điểm (`docs/games/ART_ACCEPTANCE.md` §2.2, năm tiêu chí, mỗi tiêu chí 0–2).
- Chưa đạt thì sửa prompt rồi vẽ lại, tối đa 3 lượt mỗi ảnh.
- Chuẩn VFX: `docs/games/VFX_STANDARD.md` §4.4. Chủ đề Lời Gọi là **mực giấy**.

**Bối cảnh:**
- `games/typing-defense/art-src/vfx/` có 11 flipbook 4×4 cỡ 1254², nền phông màu (xanh lá, hồng hoặc lam), và một prompt không có ảnh (`ma-troi-sheet.prompt.txt`).
- Các ảnh này chưa từng được chấm theo mức 8. Chúng chưa có alpha sạch nên game chưa dùng được.
- Phiếu 038 (Rồng) là mẫu cách tách alpha và cách kiểm: xem `docs/codex-queue/038-dh-vfx-textures-1.md` và `038-report.md`.

**Được ghi** (`art-src` là media, không vào Git):
- Trong `games/typing-defense/art-src/vfx/`:
  - `<tên>.alpha.png` cho bản đưa về chuẩn;
  - `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` cho lượt vẽ lại;
  - `<tên mới>.png` và `<tên mới>.prompt.txt` cho ảnh mới.
- `games/typing-defense/art-src/_review/043-*.jpg` và `_review/043/`.
- `tools/art-normalize/.tmp/043/` (thư mục WORK của công cụ).
- `docs/codex-queue/043-report.md`.

**Cấm:**
- ghi đè, đổi tên, xóa file có sẵn;
- ghi vào `public/`, `media.md5`; chạy `pnpm media:push`;
- chạy git; sửa mã hay tài liệu khác;
- dev server, trình duyệt;
- đụng game khác, đụng Tu Tiên.

## Việc 1 · Chấm lại 11 ảnh có sẵn

Ảnh: `dust-puff`, `explosion`, `flame-loop`, `ink-splat`, `leaf-flakes`, `ma-troi-wisp`, `paper-scraps`, `scorch-mark`, `stone-chips`, `water-splash`, `wood-chips`.

1. Chấm theo năm tiêu chí ở cỡ nguyên và khi mỗi ô thu về 64 px, đặt trên một backdrop của game (`games/typing-defense/art-src/backdrops/w1-silverfall/*.png`, lấy một ảnh).
2. Kiểm thêm phần riêng của flipbook:
   - đủ 16 ô;
   - hình ở giữa ô, cách viền ô từ 24 px (tính ở cỡ 1024²);
   - không chạm hay vượt viền ô;
   - ảnh một lần (one-shot) có pha tan cuối;
   - ảnh lặp (`flame-loop`, `ma-troi-wisp`) có ô 16 nối liền về ô 1.
3. Ảnh dưới 8: sửa prompt, vẽ lại, tối đa 3 lượt. Giữ phần đầu prompt (phong cách bộ) **nguyên văn**, chỉ sửa phần mô tả hiệu ứng.
4. `ma-troi-sheet`: chỉ có prompt. Ghi rõ trong báo cáo; **không** vẽ ảnh này.

## Việc 2 · Đưa về chuẩn alpha (bản chọn của mỗi ảnh)

- Tách nền phông thành alpha bằng `tools/art-normalize/key-alpha.sh` (đọc README công cụ), rồi đưa về **1024 × 1024, lưới 4×4, ô 256**.
- `pad-margin.sh` chỉ hỗ trợ `1x1` và `2x2`, nên làm từng ô bằng `magick` (crop, căn giữa, ghép lại). Ghi đúng lệnh vào `<tên>.prompt.txt` của lượt chọn, hoặc vào báo cáo.
- **Giữ màu** (mực tím đen, lửa son, nước bạc), không đổi sang xám: Lời Gọi tô màu sẵn trong ảnh, khác Rồng.
- Mỗi ô có viền 4 px alpha = 0.
- Không còn viền phông: px có alpha 0,05–0,95 không được mang màu phông. Ví dụ với nền xanh lá, G không được trội hơn cả R lẫn B quá 40/255.

## Việc 3 · Ba ảnh mới

| Tên | Dạng | Nội dung |
|---|---|---|
| `ink-smoke` | Flipbook 4×4 một lần, 1024² | Một cụm khói mực tím đen bốc lên rồi loang ra, tan thành sợi mảnh ở các ô cuối. Không viền mực. |
| `brush-glyphs` | Atlas tĩnh 4×4, 1024² | 16 nét bút lông kiểu thư pháp, mỗi ô một nét: móc, chấm, phẩy, vòng… Mực đen tím. **Không có chữ đọc được, không chữ Hán, không chữ cái, không số.** |
| `paper-burn` | Ảnh xám có alpha, 512² | Mép giấy cháy nhìn từ trên: lõi trống tròn méo, viền than đen, rìa giấy cháy xém nâu dần ra ngoài, vài tàn lửa. Dùng như `scorch` của phiếu 038: lõi alpha cao, rìa tan về 0, viền ảnh 4 px alpha 0. |

- Prompt mở đầu bằng đúng đoạn phong cách bộ (hai đoạn đầu của `ink-splat.prompt.txt`).
- Nền: phông xanh lá `#00FF00` cho hai flipbook. Riêng `paper-burn` dùng nền đen như phiếu 038.
- Tách alpha như việc 2.

## Kiểm (bắt buộc)

1. **md5:** chạy `md5 -r` cho mọi file trong `art-src/vfx/` trước và sau. `diff` chỉ được có dòng của file mới.
2. **Khổ và kênh:**
   - mọi `*.alpha.png` và ảnh mới đúng khổ, có alpha (`magick identify -format '%w %h %[channels]'`);
   - `paper-burn` có độ bão hòa trung bình ≤ 0,02.
3. **Lưới:** với mỗi flipbook hay atlas, một lệnh `node` hoặc `python3` (không lưu vào repo) đọc alpha và in cho từng ô:
   - hộp bao của px alpha > 0,1;
   - khoảng cách tới viền ô.

   Mọi ô phải cách viền từ 24 px; ô vi phạm ghi rõ tên ảnh và số ô.
4. **Viền phông:** in số px vi phạm luật màu phông ở việc 2. Phải bằng 0, hoặc ghi lý do.
5. **Tờ xem nhanh** `_review/043-sheet.jpg`:
   - mỗi ảnh một hàng: bản cũ (cỡ nhỏ), bản alpha trên ô bàn cờ, bản alpha trên backdrop;
   - có nhãn tên và điểm;
   - kèm một bản nền tối `_review/043-sheet-dark.jpg`.

## Báo cáo `docs/codex-queue/043-report.md`

- Bảng `| Ảnh | Lượt | Prompt sửa gì | Điểm 5 tiêu chí | Tổng | Lưới | Viền phông | Còn thiếu |`.
- Lệnh tách alpha và lệnh ghép lưới đã dùng.
- Đầu ra năm kiểm.

**Xong khi:** 11 ảnh cũ và 3 ảnh mới đều có lượt đạt từ 8 kèm bản `.alpha`, hoặc đủ 3 lượt và đã ghi bản tốt nhất kèm lý do.
