# Phiếu 376 · Tu Tiên · Sửa hai linh kiện: thân rồng dày hơn, Phong Ấn Võng to trong khung

1. **Rồng năng lượng (phiếu 375):** đầu đạt, nhưng khi nối thử, thân và đuôi quá mảnh so với đầu (đọc như xương sống hay con rết). Vẽ lại **thân và đuôi**, giữ nguyên đầu và chân.
2. **Phong Ấn Võng (phiếu 374):** vật chỉ chiếm khoảng 20 % bề ngang khung, quá nhỏ. Vẽ lại hai góc cho vật chiếm 70–80 % bề ngang, giữ nguyên thiết kế.
Điều phối thấy hai lỗi này khi xem tấm ghép (13/11 07:2x). Ảnh chờ anh duyệt trước khi dùng.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 10 lần `image_gen`**, `view_image` tối đa 12. Báo cáo `docs/codex-queue/376-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`, `A = games/immortality-cultivation/art-src`. Chỉ thêm `S/energy-dragon-{body,tail}.v2-try*.png`, `A/mechanisms/phong-an-vong.v3-{q,front}-final.png` (và `-raw`), một `.prompt.txt` cho mỗi ảnh (ghi đường dẫn tham chiếu), tấm ghép `S/energy-dragon-376-sheet.jpg` và `A/mechanisms/phong-an-vong-376-sheet.jpg`. Giữ nguyên mọi bản cũ. Cấm git ghi, sửa file có sẵn, mã, mạng ngoài, ảnh bên thứ ba.

## Tham chiếu (`view_image`)
`S/energy-dragon-head.v1-try2.png` (đầu dùng chính thức), `S/energy-dragon-body.v1-try1.png`, `S/energy-dragon-tail.v1-try1.png`, `S/energy-dragon-375-sheet.jpg`; `A/mechanisms/phong-an-vong.v2-q-final.png`, `A/mechanisms/phong-an-vong.v2-front-final.png`.

## Sửa
- **Thân rồng** 2048×512 lặp liền theo x: bề dày thân **bằng khoảng 70 % chiều cao cổ ở mép nối với đầu** (gấp khoảng 2,5 lần bản 1), vảy nét sáng lớn hơn, vây lưng rõ, bụng có đường gân sáng; nét sáng bạch kim như đầu. Mép trái khớp cổ của đầu, làm lặp liền bằng script (dịch nửa, hoà chéo, dịch về).
- **Đuôi** 1024×512: bắt đầu bằng đúng bề dày thân mới ở mép trái, thon dần, tan thành tia năng lượng.
- **Phong Ấn Võng:** giữ khung đồng lưới dày, bốn chân đá, ngọc góc; vật chiếm 70–80 % bề ngang khung, lề ≥ 8 %, nền `#00FF00`, cùng chuẩn ảnh với bản 2.

## Kiểm và tự chấm
Script: thân lặp liền (hiệu cột đầu/cuối), mép thân khớp đầu và đuôi, Phong Ấn Võng chiếm 70–80 % bề ngang và lề ≥ 8 %. Tấm ghép: con rồng nối thử (đầu + 3 thân + đuôi) bản 1 | bản 2; Phong Ấn Võng cũ | mới. Tự chấm theo mặt yếu nhất; dưới 8 vẽ lại. Báo cáo ≤ 200 chữ.

Phản biện: PASS (Sonnet, 13/11)
