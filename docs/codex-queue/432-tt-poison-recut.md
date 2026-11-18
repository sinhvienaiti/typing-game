# Phiếu 432: Cắt lại clip độc nổ lớn, giữ phần khói lan rộng


Phản biện: PASS (Sonnet, 17/11)
**Owner miễn luật hạn mức (nguyên văn 16/11):** "tôi đã nói cứ cho codex làm đi, tôi sẽ reset codex sau"; 17/11: "cho codex làm việc đi, nó vẫn còn kìa".

## Bối cảnh
Clip Firefly `games/immortality-cultivation/art-src/lab/vfx/poison/firefly-raw/poison-big-burst.v3-try2.mp4` đạt B (khói xanh có khối, lan rộng sát đất, cột độc giữa; ảnh `typing-game-review/owner-review/2026-11-16/tu-tien/burst-remake/i2v/poison-big-burst.try2.sheet.jpg`). Bản -v2 cắt ở phiếu 420 chỉ còn cột mảnh vì chọn đoạn và co tỉ lệ sai. Lab hiện dùng bản độc cũ (dòng -v3 Blender đã tắt trong `games/.wt-ic-lab-all/src/lab/burst-v2.ts`).

## Việc
1. Bằng `tools/vfx-flipbook/`: lấy đoạn từ khung có khói lan rộng nhất (khoảng 1,0–3,5 s; tự chọn bằng đo diện tích sáng lớn nhất), 32 khung lưới 8×4, scale theo **bề rộng tối đa của khối khói** (không theo cột giữa), lề ≥ 10 % mọi khung, 8 khung cuối mờ về 0, pivot ở điểm chạm đất. Ghi `poison-big-burst-v5.{atlas.png,json,uastc.ktx2}`; không ghi đè bản khác.
2. `burst-v2.ts`: thay dòng `poison-big-burst` (đang tắt) bằng hậu tố "-v5", bật lại.
3. Cập nhật `docs/games/tu-tien/skills/VFX_LIBRARY.md`.

## Nghiệm thu
- Script đo: lề ≥ 10 % mọi khung; ở khung đỉnh, bề rộng vùng sáng ≥ 60 % bề rộng ô; luma khung cuối ≤ 0,02; probe nạp -v5 không 404; kiểm kiểu 0 lỗi.
- Chỉ ghi file mới trong `art-src/lab/vfx/poison/`, sửa `burst-v2.ts`, `VFX_LIBRARY.md`. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/432-report.md`.
