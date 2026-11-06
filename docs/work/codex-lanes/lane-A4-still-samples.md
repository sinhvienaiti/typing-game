# Làn Codex A · Việc A4 · Vẽ 2 ảnh mẫu để làm video bằng image-to-video

Bối cảnh (07/11 03:25):
- Đợt làm thử `redo-01` cho thấy làm lại video chỉ bằng prompt không lên được 8 điểm (0/10, trung bình 5,60 → 5,95).
- Làn C khuyên vẽ ảnh nội bộ được anh chọn để khoá hình, rồi làm image-to-video từ ảnh đó.
- Theo luật của anh, trước mọi lô phải có 2 mẫu cho anh xem.

Việc này **chỉ vẽ 2 mẫu**, chưa làm lô.

**Model `gpt-6.1-sol`, mức `high`** (vẽ ảnh). Báo cáo: `docs/codex-queue/laneA4-report.md` (tiếng Việt, ngắn).

## Hai ảnh (lời tả gốc trong `stillBrief` của `.local/video-review/results/batch-0*.json`)
1. **`boss-entrance-vortex`:**
   - cổng xoáy năng lượng đỏ thẫm và đen, lỗ giữa tròn hoặc oval dọc, rõ ràng;
   - dáng oai nghiêm, bất đối xứng có chủ đích;
   - nhiều dải khí đỏ trong suốt xoắn quanh tâm tối;
   - quầng mềm, tia mảnh, sao nhỏ, đốm sáng;
   - nền đen thuần, lề rộng, khổ 1:1.
2. **`blood-ring-burst`:**
   - vòng xung kích Huyết nằm trên mặt phẳng nhìn từ camera cao 55 độ, hình ellipse rõ, tâm rỗng đen;
   - vành huyết quang mảnh nhiều tầng, sương đỏ sẫm, giọt nhỏ, bụi pha lê đỏ;
   - viền lung linh, quầng mềm, sao nhỏ;
   - nền đen thuần, lề đủ cho vòng nở, khổ 1:1.

## Luật vẽ
- **Bắt buộc dùng ảnh tham chiếu của ta, không vẽ chỉ từ prompt.** Lấy 2–3 ảnh đã duyệt, ghi đường dẫn vào prompt:
  - bộ quái và boss của phiếu 321 (đường dẫn trong `docs/codex-queue/321-report.md`), để khớp màu đỏ Lang Vương;
  - bộ ấn Huyết của làn 3 (`art-src/lab/vfx/sigils/blood/`, nguồn ghi trong `docs/codex-queue/lane3-report.md`), để khớp nét huyết quang;
  - một khung đẹp nhất của chính clip cũ (`.local/video-review/sheets/<job>__take1.jpg`), chỉ để giữ bố cục.
- Chất lượng: phong cách anime/donghua thần thoại, sang, nhiều lớp, bùng nổ. Không ảnh của bên thứ ba, không chữ, không logo.
- Mỗi ảnh vẽ 2 bản (`try1`, `try2`), tự chấm thang 10 theo thước chấm ở `lane-C-video-review.md`. Bản ≥ 8 là ứng viên.
- Lưu `<job>-still.v1-try<k>.png` kèm `.prompt.txt` vào `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/`.
- Ghép 4 ảnh thành một tấm `.local/still-samples-0711/samples.jpg` để Claude gửi anh.

## Ranh giới
- **Chỉ ghi:** các ảnh mới nói trên, `.local/still-samples-0711/`, báo cáo.
- **Không:** sửa ảnh cũ, video hay mã; lệnh git ghi; mở trình duyệt.

## Hết hạn mức
Khi image_gen báo hết lượt, giữ file đã có và ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`). Làm xong thì không ghi.
