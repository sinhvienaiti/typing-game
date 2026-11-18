# Phiếu 369 · Tu Tiên · UI jewel-crest: 7 khung còn lại và 12 icon HUD theo viền jewel-crest

Anh chọn kiểu **jewel-crest** cho toàn bộ giao diện (12/11 20:2x). Mẫu đã duyệt là khung "Bàn Quyết" và icon tuyệt kỹ Ám jewel-crest của phiếu 363. 12 icon HUD của 363 đang dùng viền ink-gold, nên vẽ lại theo viền jewel-crest; giữ nguyên vật bên trong mỗi icon.

Lô: 19 ảnh (7 khung + 12 icon)
Mẫu đã gửi: /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/codex-images/ui-two-styles.jpg

**Model `gpt-6.1-sol`, mức `high`. Tối đa 28 lần `image_gen`**, `view_image` tối đa 30. Báo cáo `docs/codex-queue/369-report.md`.

## Đường dẫn
`A = games/immortality-cultivation/art-src`. Chỉ thêm `A/ui/frames/<tên>-jewel-crest.v1-try*.png`, `A/ui/icons/hud-<tên>-jewel-crest.v1-try*.png` và bản thu `-48.png`, `-32.png` (chỉ cho icon), một `.prompt.txt` cho mỗi ảnh (ghi đường dẫn tham chiếu), tấm ghép `A/ui/ui-369-sheet.jpg`. Giữ nguyên mọi file của 363. Cấm git ghi, sửa file có sẵn, mã.

## Tham chiếu (`view_image`)
Kiểu đã duyệt: `A/ui/frames/ban-quyet-jewel-crest.v1-try1.png`, `A/lab/ui/skill-icons/ult-dark-jewel-crest.v1-try1.png`. Vật bên trong icon (giữ nguyên): `A/ui/icons/hud-*.v1-try*.png` của phiếu 363 (báo cáo `docs/codex-queue/363-report.md` ghi try đã chọn).

## Bảy khung 9-slice (theo đúng viền, ngọc góc, dải hoa văn chàm của Bàn Quyết)
| Tên | Khổ | Dùng |
|---|---|---|
| `hud-bar` | 2048×256 | thanh HUD dưới |
| `wave-card` | 768×384 | thẻ đợt quái |
| `shop` | 1024×1024 | cửa hàng |
| `harvest` | 1024×768 | bảng Thu Hoạch |
| `menu` | 768×1024 | menu dọc |
| `settings` | 1024×768 | bảng Settings |
| `sound` | 768×768 | bảng Sound |
Giữa khung trơn, tối đủ để chữ trắng đè lên đọc rõ; góc và cạnh tách được thành 9 ô (góc vuông, cạnh lặp được). Vẽ trên nền `#00FF00` rồi tách alpha, không viền xanh.

## Mười hai icon
Cùng tên với 363 (`talisman-heal`, `talisman-shield`, `talisman-haste`, `trap-sword-stake`, `trap-thunder-pillar`, `trap-seal-net`, `coin-spirit-stone`, `coin-jade`, `coin-merit`, `settings`, `sound`, `sound-muted`), 256 px, viền tròn jewel-crest giống icon Ám jewel-crest; vật bên trong giữ như bản 363. Đọc được ở 32 px.
Không chữ Hán, không chữ Latinh trên khung hay icon. Lề ≥ 8 %.

## Kiểm và tự chấm
Script: lề, alpha sạch, cạnh khung lặp liền (so cột/hàng biên), bản thu 48/32. Tấm ghép: 8 khung (cả Bàn Quyết) cùng tỉ lệ thu, 12 icon ở 256/48/32. Tự chấm theo mặt yếu nhất (cùng bộ với mẫu, đọc ở 32 px, chữ đè đọc được, sang trọng); dưới 8 vẽ lại. Báo cáo ≤ 300 chữ.

Phản biện: PASS (Sonnet, 12/11; bản thu chỉ cho icon)
