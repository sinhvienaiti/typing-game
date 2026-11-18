# Phiếu 419: Cắt 7 clip Firefly mới đạt thành flipbook (bản -v2, không ghi đè bản cũ)


Phản biện: PASS (Sonnet, 16/11)
## Bối cảnh
Owner 16/11 duyệt làm lại clip bùng nổ ("Lửa đạt, Kim làm lại"). Loạt Firefly (`typing-game-review/owner-review/2026-11-16/tu-tien/burst-remake/batch-sheets.jpg`, `docs/work/tasks/video-production-list.md`) có các bản đạt B/B+ sau. Công cụ: `tools/vfx-flipbook/` (`run.sh`, cấu hình `immortality-cultivation.json`), cách đóng gói như các atlas cũ (lưới 8×4, 32 khung, KTX2 + json) và như phiếu 414.

## Việc
Cắt đúng 7 clip, nguồn trong `games/immortality-cultivation/art-src/lab/vfx/<hệ>/firefly-raw/`:
| Clip | Nguồn | Ghi chú |
|---|---|---|
| fire-impact | `fire/firefly-raw/fire-impact.v1-try2.mp4` | chỉ dùng ~3 s đầu (sau đó tia chạm mép) |
| fire-big-burst | `fire/firefly-raw/fire-big-burst.v2-try1.mp4` | |
| earth-ring-burst | `earth/firefly-raw/earth-ring-burst.v2-try1.mp4` | |
| metal-impact | `metal/firefly-raw/metal-impact.v2-try1.mp4` | |
| metal-big-burst | `metal/firefly-raw/metal-big-burst.v2-try1.mp4` | |
| void-big-burst | `void/firefly-raw/void-big-burst.v2-try1.mp4` | |
| wind-ring-burst | `wind/firefly-raw/wind-ring-burst.v2-try2.mp4` | bắt đầu to: chọn đoạn và thu nhỏ để lề ≥ 10 % |
Mỗi clip: chọn đoạn đẹp nhất (tối đa 32 khung), tách nền đen thành alpha/additive như atlas cùng loại, đảm bảo lề ≥ 10 % mọi khung (thu nhỏ nếu cần), có tail fade cuối (clip Firefly không tự tắt về đen). Ghi `<clip>-v2.atlas.png`, `.json`, `.uastc.ktx2` cạnh bản cũ; **không ghi đè** bản cũ. Cập nhật `docs/games/tu-tien/skills/VFX_LIBRARY.md`.

## Nghiệm thu
- Script đo lề ≥ 10 % mọi khung cho cả 7 bản (in số); json đúng định dạng atlas cũ (cùng khoá).
- Ảnh ghép 8 khung mỗi clip (bản cũ | bản -v2) trong `typing-game-review/captures/tu-tien/burst-v2/` có `ABOUT.md`; nếu sandbox chặn ghi, để ở `/private/tmp` và ghi đường dẫn trong báo cáo.
- Chỉ ghi file mới trong `art-src/lab/vfx/<hệ>/` và `VFX_LIBRARY.md`. Không sửa code, không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/419-report.md`.
