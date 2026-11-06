# Làn Codex 1 · Gắn ấn vẽ tay của 13 hệ vào lab, đổi theo hệ đang chọn

Anh (06/11 23:40): "Duyệt, gắn vào lab". Đây là 13 bộ ấn làn 3 vừa vẽ, mỗi bộ 7 dáng như bộ Kim, ảnh nằm trong `S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`; báo cáo `docs/codex-queue/lane3-report.md` ghi bản chọn từng ảnh. Bộ Kim đã có trong lab từ phiếu 328.

**Model `gpt-6.1-sol`, mức `xhigh`.** Báo cáo: `docs/codex-queue/lane1d-report.md` (tiếng Việt, ngắn). Làm lần lượt từng việc; mỗi việc tự kiểm theo "Đạt khi" rồi mới sang việc kế tiếp.

## Nơi làm và ranh giới
- Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all` (lab chung: panel gọn, thanh chiêu, A/B, ấn Kim, Song Long).
- **Được ghi:**
  - `src/view/skills/painted-sigils.ts`, `src/view/skills/fxkit.ts`, `src/view/skills/sword-rain.ts`, `src/view/skills/sword-skills.ts`;
  - `scripts/vfx/sigil-masks-lib.ts`, `scripts/vfx/sigil-masks.ts`;
  - test trong `tests/view/`;
  - thư mục media mới `art-src/lab/vfx/sigils/<hệ>/` và báo cáo.
- `src/lab/skills-main.ts` chỉ sửa khi bắt buộc để báo cho ấn biết hệ đổi; ghi rõ trong báo cáo.
- **Cấm:** sửa ảnh trong `S`; sửa bộ Kim đã có trong `art-src/lab/vfx/sigils/`; lệnh git ghi; mở cổng mạng; mở trình duyệt.

## Danh sách việc
### Việc 1 · Mặt nạ cho 13 hệ
- Chạy script mặt nạ của phiếu 328 cho 7 ảnh mỗi hệ. Hỏa dùng `fire-sigil-hex.v1-try1.png` và `fire-sigil-line.v1-try1.png` của phiếu 327, cộng 5 ảnh của làn 3. Các hệ khác dùng đúng bản chọn trong `lane3-report.md`.
- Ra `art-src/lab/vfx/sigils/<hệ>/` kèm `manifest.json` cùng lược đồ với bộ Kim. Mã hệ: `fire water thunder wind ice earth wood light dark poison blood void star`.
- **Màu:** tranh mỗi hệ đã có màu riêng, nên bộ của 12 hệ (trừ Kim) giữ **màu của chính tranh** (RGB cộng sáng, nền đen là trong suốt), lấy độ sáng làm kênh ăn mòn. Manifest ghi `mode: "color"`. Bộ Kim giữ cách cũ: mặt nạ và tô màu bằng mã.
- **Đạt khi:**
  - đủ 13 × 7 mặt nạ, không mặt nạ nào bị cắt mép;
  - tổng bộ nhớ GPU mỗi bộ ghi vào báo cáo (bộ Kim khoảng 27 MB);
  - script chạy lại cho ra file giống từng byte.

### Việc 2 · Lab đổi bộ ấn theo hệ
- Hệ đổi (phím E, ô chọn Element) thì ấn và vết nứt, rãnh của phím 2–6 dùng bộ của hệ đó:
  - nạp lười lần đầu dùng;
  - giữ tối đa 2 bộ trong bộ nhớ (bộ Kim và bộ đang dùng), giải phóng bộ cũ khi đổi tiếp.
- Hệ chưa có bộ hoặc nạp lỗi thì dùng bộ Kim, rồi tới hình code, kèm cảnh báo console.
- `?sigil=code` vẫn ép hình code để so A/B.
- Shader nhánh `mode: "color"`:
  - lấy màu từ texture;
  - giữ hiện dần, nhịp sáng, ăn mòn về 0 (công thức `(1 − fade) · 1.1 − 0.1` như phiếu 328), không tô thêm màu.
- **Đạt khi:**
  - test thuần trên node cho việc chọn bộ theo hệ, quay về khi thiếu, giới hạn 2 bộ, đọc manifest `mode: "color"`;
  - `npx tsc --noEmit` sạch;
  - `npx vitest run --maxWorkers=4` toàn bộ qua (trước việc này: 113 file, 1.270 test).

## Hết hạn mức
Giữ file, ghi báo cáo phần đã xong. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
