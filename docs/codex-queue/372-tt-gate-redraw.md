# Phiếu 372 · Tu Tiên · Cổng ải vẽ lại (ảnh nguồn 3D, D26/M08)

Cổng ải cũ `A/props/cong-ai.png` chấm 7,55 (`docs/games/tu-tien/art-requests/demo1/JUDGING.md` dòng A17): quá cao (bị cắt ở camera chơi), không cùng bộ, hoa văn phương Tây. Cổng dùng 2 lần trên map 1 (`docs/games/tu-tien/MAP1_CONCEPT.md`). Anh đã chọn tranh màn tựa B có cổng ải hùng vĩ: `A/ui/title-key-art.v1-try2.png` (lấy kiến trúc cổng làm hướng).

**Model `gpt-6.1-sol`, mức `high`. Tối đa 8 lần `image_gen`**, `view_image` tối đa 10. Báo cáo `docs/codex-queue/372-report.md`.

## Đường dẫn
`A = games/immortality-cultivation/art-src`. Chỉ thêm `A/props/cong-ai.v2-{q,front}-final.png` (và `-raw`), một `.prompt.txt` cho mỗi ảnh final (ghi đường dẫn tham chiếu), tấm ghép `A/props/cong-ai-372-sheet.jpg`. Giữ nguyên file cũ. Cấm git ghi, sửa file có sẵn, mã, mạng ngoài, ảnh bên thứ ba.

## Tham chiếu (`view_image`)
`A/props/cong-ai.png` (thiết kế cũ), `A/ui/title-key-art.v1-try2.png` (kiến trúc cổng anh chọn), `A/kings/thiet-boi-lang-vuong.v7-q-final.png` (chuẩn ảnh), `A/concept/map1-camera.v1-try6.png` (cổng trên map nhìn từ camera chơi).

## Hình
Cổng thành đá cổ Việt: **rộng và thấp** (rộng gấp khoảng 2,2 lần cao), một vòm cửa lớn giữa, hai bệ tường hai bên, **mái ngói hai tầng cong nhẹ đẹp khi nhìn từ trên** (mái chiếm phần lớn diện tích thấy từ camera 55°), đầu đao mái kiểu Việt, đá xám vôi xanh, gỗ sẫm, ngói xám chàm, cờ phướn chàm nhỏ gắn liền. Hai ảnh: ba phần tư 32° và chính diện, cùng tỉ lệ.
Chuẩn ảnh chung (giữ đúng bộ quái đã duyệt): một nguồn sáng mềm trên phải 45°, painterly-realistic như `A/kings/thiet-boi-lang-vuong.v7-q-final.png`, góc ba phần tư 32° từ trên, nền `#00FF00` phẳng, lề ≥ 8 %, không bóng đổ, không chữ (không Hán, không Latinh), motif tiên hiệp Việt (vân mây, hồi văn, lôi văn), không Celtic, không triskelion, không sét zigzag phương Tây; cấm màu tín hiệu ở cường độ cao (đỏ tươi, cam, vàng kim, xanh ngọc); khối lớn, không chi tiết mảnh rời (để Tripo dựng).

## Kiểm và tự chấm
Script: lề, hai góc lệch chiều cao ≤ 5 %, alpha sạch. Tấm ghép: cũ | mới, và bản thu ở cỡ camera chơi (cao 90 px). Tự chấm theo mặt yếu nhất (cùng bộ, đẹp từ trên, không bị cắt, dựng Tripo được, chất Việt); dưới 8,5 vẽ lại. Báo cáo ≤ 300 chữ.

Phản biện: PASS (Sonnet, 12/11; lỗi phản biện nêu đã sửa)
