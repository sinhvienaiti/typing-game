# Phiếu 383 · Tu Tiên · Map 1: 6 ô đất lặp và 8 decal nền (D19, D20)

Anh (13/11 18:5x): "vậy cứ làm ô đất đi". Dùng được cho mọi góc camera của map một đường (`docs/games/tu-tien/MAP1_WIDE.md` §13) và map rộng sau này. Vật liệu theo `docs/games/tu-tien/MAP1_CONCEPT.md` (hành lang đá lát mòn bóng sáng hơn; đất ngoài hành lang đá lát lớn kém đều, rêu xanh xám ở khe, phiến nứt; sân đá vôi xám xanh). Màu tín hiệu cấm trên đất: đỏ, cam, vàng kim, xanh ngọc.

Lô: 14 ảnh (6 ô + 8 decal)
Mẫu đã gửi: /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/codex-images/map1-365-sheet.jpg

**Model `gpt-6.1-sol`, mức `high`. Tối đa 20 lần `image_gen`**, `view_image` tối đa 20. Báo cáo `docs/codex-queue/383-report.md` (Codex tự viết).

## Đường dẫn
`A = games/immortality-cultivation/art-src`. Được tạo thư mục `A/ground/thanh-thach/` và `A/decals/thanh-thach/`. Chỉ thêm ảnh trong hai thư mục đó, một `.prompt.txt` cho mỗi ảnh (ghi đường dẫn tham chiếu), tấm ghép `A/ground/thanh-thach/ground-383-sheet.jpg`. Cấm git ghi, sửa file có sẵn, mã.

## Tham chiếu (`view_image`)
Chất đá và màu: `A/concept/map1-camera.v1-try6.png`, `A/concept/map1-camera.v1-try7.png` (tranh map đã vẽ); vật liệu nền CC0 trong `A/lab/lookdev/PavingStones128/`, `A/lab/lookdev/Rock035/`, `A/lab/lookdev/Moss001/` (ảnh màu trong mỗi thư mục).

## Sáu ô đất lặp, 1024×1024, nhìn thẳng từ trên, **lặp liền bốn cạnh** (làm liền bằng script: dịch nửa, vá hoặc hoà chéo, dịch về)
1. `lane-paving` đá lát hành lang, phiến chữ nhật mòn bóng, sáng hơn nền.
2. `court-paving` đá lát lớn kém đều ngoài hành lang, khe có rêu xám xanh.
3. `court-cracked` như 2 nhưng nhiều phiến nứt, mẻ góc.
4. `moss-patch` đá lát phủ rêu dày từng mảng.
5. `formation-worn` đá lát có vết khắc trận văn cổ mờ đã mòn (ký hiệu giống triện cổ, không chữ thật).
6. `rubble-edge` đá vụn, sỏi, đất lẫn ở mép sân.
Ánh sáng phẳng đều (không bóng đổ hướng), để engine chiếu sáng; độ tương phản vừa để không lấn quái và hiệu ứng.

## Tám decal nền trong suốt, 512×512 (vẽ trên `#00FF00`, tách alpha, mép mềm)
`crack-large`, `crack-small`, `moss-clump`, `leaf-litter` (lá khô tùng, nâu xám), `scorch-old` (vết cháy cũ nhạt), `water-stain`, `rubble-scatter`, `formation-glyph-ring` (vòng trận văn cổ mòn, đá khắc, không phát sáng).

## Kiểm và tự chấm
Script: mỗi ô lặp liền (hiệu cạnh trái/phải và trên/dưới nhỏ; xếp 3×3 không lộ đường nối), decal alpha sạch không viền xanh, lề ≥ 6 %. Tấm ghép: mỗi ô xếp 3×3, tám decal trên nền ô 2, và một ô thử phối (ô 1 làm hành lang, ô 2–4 xen kẽ, vài decal) ở cỡ camera chơi. Tự chấm theo mặt yếu nhất (lặp không lộ, hợp tranh map, không lấn quái, đẹp thương mại); dưới 8 vẽ lại trong hạn lượt. Báo cáo ≤ 200 chữ.

Phản biện: PASS (Sonnet, 13/11)
