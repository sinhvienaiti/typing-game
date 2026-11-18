# Phiếu 428: Cắt 2 giây đầu clip vương miện máu thành flipbook -v4 và thay vào lab


Phản biện: PASS (Sonnet, 16/11)

**Owner miễn luật hạn mức 16/11/2026 22:4x (nguyên văn):** "tôi đã nói cứ cho codex làm đi, tôi sẽ reset codex sau". Phiếu này được làm dù Codex còn dưới 15 %; không dừng vì hạn mức.
## Bối cảnh
Owner 16/11 chọn mẫu ảnh 1 (`games/immortality-cultivation/art-src/lab/vfx/blood/stills-55/blood-crown.v2-try1.png`) làm khung đầu. Firefly cho `blood/firefly-raw/blood-big-burst.v5-try2.mp4`: ~2 s đầu đẹp (vương miện bóng 55°, nhánh đầu tròn), sau đó thành vòng gai thẳng, tràn lề và không tắt. Ảnh kiểm: `typing-game-review/owner-review/2026-11-16/tu-tien/burst-remake/blood-crown/`.

## Việc
1. Bằng `tools/vfx-flipbook/` (như phiếu 419/420/424): chỉ lấy đoạn 0–2,0 s của `games/immortality-cultivation/art-src/lab/vfx/blood/firefly-raw/blood-big-burst.v5-try2.mp4`, 32 khung (lưới 8×4), tách nền đen, lề ≥ 10 % mọi khung (thu nhỏ nếu cần), 8 khung cuối mờ dần về 0 (tail fade trong atlas), pivot ở điểm chạm đất, giữ phối cảnh. Ghi `blood-big-burst-v4.{atlas.png,json,uastc.ktx2}`; không ghi đè bản khác.
2. `games/.wt-ic-lab-all/src/lab/burst-v2.ts`: đổi dòng `blood-big-burst` sang hậu tố "-v4"; giữ nguyên các lớp giọt và vũng máu trong `burst-layers.ts` và sắc đỏ thẫm.
3. Cập nhật `docs/games/tu-tien/skills/VFX_LIBRARY.md`.

## Nghiệm thu
- Script đo: mọi khung PNG lề ≥ 10 %; luma khung cuối ≤ 0,02; json cùng khoá atlas cũ; probe nạp `-v4` không 404; kiểm kiểu 0 lỗi.
- Ảnh 8 khung trong `typing-game-review/captures/tu-tien/burst-v4/` (nếu sandbox chặn, `/private/tmp` + ghi đường dẫn).
- Chỉ ghi file mới trong `art-src/lab/vfx/blood/`, sửa `burst-v2.ts`, `VFX_LIBRARY.md`. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/428-report.md`.
