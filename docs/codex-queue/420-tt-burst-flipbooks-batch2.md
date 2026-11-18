# Phiếu 420: Cắt 10 clip Firefly (ảnh 55° → video) thành flipbook (bản -v2, không ghi đè bản cũ)


Phản biện: PASS (Sonnet, 16/11; sau khi sửa tiêu đề lặp và dòng PASS chép nhầm từ 419)

## Bối cảnh
Owner 16/11 duyệt làm lại clip bùng nổ ("Lửa đạt, Kim làm lại"). Loạt Firefly (`typing-game-review/owner-review/2026-11-16/tu-tien/burst-remake/batch-sheets.jpg`, `docs/work/tasks/video-production-list.md`) có các bản đạt B/B+ sau. Công cụ: `tools/vfx-flipbook/` (`run.sh`, cấu hình `immortality-cultivation.json`), cách đóng gói như các atlas cũ (lưới 8×4, 32 khung, KTX2 + json) và như phiếu 414.

## Việc
Cắt đúng 10 clip, nguồn trong `games/immortality-cultivation/art-src/lab/vfx/<hệ>/firefly-raw/`:
| Clip | Nguồn | Ghi chú |
|---|---|---|
| dark-ring-burst | `dark/firefly-raw/dark-ring-burst.v3-try2.mp4` | dùng 2–3 s đầu (về cuối tràn lề) |
| water-ring-burst | `water/firefly-raw/water-ring-burst.v3-try1.mp4` | dùng 2–3 s đầu (về cuối tràn lề) |
| poison-big-burst | `poison/firefly-raw/poison-big-burst.v3-try2.mp4` | dùng 2–3 s đầu (về cuối tràn lề) |
| poison-ring-burst | `poison/firefly-raw/poison-ring-burst.v3-try1.mp4` | dùng 2–3 s đầu (về cuối tràn lề) |
| blood-big-burst | `blood/firefly-raw/blood-big-burst.v3-try2.mp4` | dùng 2–3 s đầu (về cuối tràn lề) |
| wood-big-burst | `wood/firefly-raw/wood-big-burst.v3-try2.mp4` | dùng 2–3 s đầu (về cuối tràn lề) |
| dark-big-burst-white | `dark/firefly-raw/dark-big-burst-white.v3-try2.mp4` | dùng 2–3 s đầu (về cuối tràn lề) |
| dark-ground-impact-white | `dark/firefly-raw/dark-ground-impact-white.v3-try1.mp4` | dùng 2–3 s đầu (về cuối tràn lề) |
| thunder-impact | `thunder/firefly-raw/thunder-impact.v3-try1.mp4` | dùng 2–3 s đầu (về cuối tràn lề) |
| star-ring-burst | `star/firefly-raw/star-ring-burst.v3-try1.mp4` | dùng 2–3 s đầu (về cuối tràn lề) |
Mỗi clip: chọn đoạn đẹp nhất (tối đa 32 khung), tách nền đen thành alpha/additive như atlas cùng loại, đảm bảo lề ≥ 10 % mọi khung (thu nhỏ nếu cần), có tail fade cuối (clip Firefly không tự tắt về đen); giữ đúng phối cảnh bầu dục 55° (không xoay, không ép tròn); vòng/chạm đất đặt pivot ở điểm chạm đất. Ghi `<clip>-v2.atlas.png`, `.json`, `.uastc.ktx2` cạnh bản cũ; **không ghi đè** bản cũ. Cập nhật `docs/games/tu-tien/skills/VFX_LIBRARY.md`.

## Nghiệm thu
- Script đo lề ≥ 10 % mọi khung cho cả 10 bản (in số); json đúng định dạng atlas cũ (cùng khoá).
- Ảnh ghép 8 khung mỗi clip (bản cũ | bản -v2) trong `typing-game-review/captures/tu-tien/burst-v2b/` có `ABOUT.md`; nếu sandbox chặn ghi, để ở `/private/tmp` và ghi đường dẫn trong báo cáo.
- Chỉ ghi file mới trong `art-src/lab/vfx/<hệ>/` và `VFX_LIBRARY.md`. Không sửa code, không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/420-report.md`.
