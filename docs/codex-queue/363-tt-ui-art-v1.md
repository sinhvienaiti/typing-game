# Phiếu 363 · Tu Tiên · UI: hai hướng khung mẫu, icon tuyệt kỹ Ám, 12 icon HUD

Bản chơi chưa có khung UI và icon HUD (`docs/work/tasks/image-backlog.md` D13, D15, D16). Anh đã khen hai hướng icon ink-gold và jewel-crest ngày 06/11.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 18 lần `image_gen`**, `view_image` tối đa 20. Báo cáo `docs/codex-queue/363-report.md`.

## Đường dẫn
`A = games/immortality-cultivation/art-src`. Được tạo thư mục mới `A/ui/frames/`, `A/ui/icons/`. Chỉ thêm `A/ui/frames/*.v1-try*.png`, `A/ui/icons/*.v1-try*.png` (và bản thu `*-48.png`, `*-32.png`), `A/lab/ui/skill-icons/ult-dark-*.v1-try*.png`, `.prompt.txt`, tấm ghép `A/ui/ui-363-sheet.jpg`. Cấm git ghi, sửa file có sẵn, mã.

## Tham chiếu (`view_image`)
`A/lab/ui/skill-icons/ink-gold-*.png` và `jewel-crest-*.png` (hai hướng icon; khung icon tuyệt kỹ mẫu: `ink-gold-ult-blood.v1-try1.png`), `A/identity/kiem-tu-portrait.png`, `A/identity/thanh-thach-ai-55.png` (bảng màu thế giới).

## Việc
1. **Khung mẫu, hai hướng** (ink-gold và jewel-crest): một bảng 9-slice "Bàn Quyết" 1024×768 mỗi hướng, góc và cạnh có hoa văn mây hồi văn, giữa trơn để chữ đè, nền trong suốt (vẽ nền `#00FF00` rồi tách). Chỉ hai ảnh này, để anh chọn hướng trước khi làm cả bộ 8 khung.
2. **Icon tuyệt kỹ Ám `ult-dark`**, hai hướng như trên, 256 px, cùng khung với `ink-gold-ult-blood.v1-try1.png`. Tên: `ult-dark-ink-gold.v1-try*.png`, `ult-dark-jewel-crest.v1-try*.png`.
3. **12 icon HUD** 256 px theo hướng ink-gold: tên tệp `hud-<tên>.v1-try*.png`: `talisman-heal` (đan phù hồi khí), `talisman-shield` (phù hộ thân), `talisman-haste` (phù tốc hành); `trap-sword-stake` (Kiếm Thung), `trap-thunder-pillar` (Lôi Phù Trụ), `trap-seal-net` (Phong Ấn Võng); `coin-spirit-stone` (linh thạch), `coin-jade` (ngọc), `coin-merit` (công đức); `settings` (bánh răng kiểu la bàn cổ), `sound`, `sound-muted`. Đọc được ở 32 px (tự thu xuống và kiểm).
Không chữ Hán, không chữ Latinh trên icon. Lề ≥ 8 %.

## Kiểm và tự chấm
Tấm ghép: hai khung, hai icon Ám, 12 icon ở 256/48/32 px. Tự chấm theo mặt yếu nhất (đọc ở 32 px, cùng bộ, sang trọng, hợp bảng màu); dưới 8 vẽ lại trong hạn lượt. Báo cáo ≤ 300 chữ.

Phản biện: PASS (Sonnet, 12/11; lỗi phản biện nêu đã sửa)
