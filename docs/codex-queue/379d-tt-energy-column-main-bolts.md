# Phiếu 379d · Tu Tiên · Cột năng lượng: hẹp 1/3 và một hoặc hai đường sét chính dày

Anh xem cột năng lượng 379b (13/11 12:1x–12:2x):
- "nó lại hơi dày r, nên giảm 1/3 lại là được";
- "nên làm 1 hoặc 2 đường lôi dày làm chính, các lôi nhỏ là phụ, để nhìn rõ đường nguồn năng lượng lôi chính, chứ như ảnh trên, nó nhìn kiểu nhiều lôi nhỏ hợp thành, nhìn vẫn rất khó".
Phiếu 379c (chỉ thu hẹp) đã huỷ, gộp vào đây.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 8 lần `image_gen`**, `view_image` tối đa 10. Báo cáo `docs/codex-queue/379d-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-energy-column.v3-try*.png`, `S/thunder-energy-column-frames.v3-try*.png`, một `.prompt.txt` cho mỗi ảnh (ghi đường dẫn tham chiếu), tấm ghép `S/thunder-energy-379d-sheet.jpg`. Giữ nguyên bản v1. Cấm git ghi, sửa file có sẵn, mã.

## Tham chiếu (`view_image`)
`S/thunder-energy-column.v1-try3.png` (chất plasma, màu, chân nổ, mây: giữ), `S/thunder-single-bolt-a.v4-try9.png` (nét một tia sét chính bạch kim đã duyệt).

## Hình (giữ khổ 1024×1536, nền đen, nhìn ngang hơi từ trên 30°, bạch kim D65)
1. **`thunder-energy-column`:**
   - **Bề rộng thân khoảng 2/3 bản v1** (thân rộng khoảng 22 % chiều cao), vẽ lại hẹp chứ không kéo méo.
   - **Một hoặc hai tia sét chính dày** chạy suốt từ mây xuống chân: mỗi tia dày khoảng 1/4–1/3 bề rộng thân, lõi trắng rực, gấp khúc gắt như sét thật (không uốn mềm như khói), là thứ sáng nhất và đọc rõ nhất. Nếu hai tia: chúng tách rồi chạm nhau ở vài điểm, không xoắn đều.
   - **Tia phụ nhỏ** bám quanh và rẽ từ tia chính, mờ hơn hẳn (độ sáng khoảng 40–60 % tia chính), làm nền plasma; ít nhánh ra ngoài thân.
   - Quầng plasma vàng nhạt mờ bao quanh, ranh giới thân mềm.
   - Chân nổ chạm đất và mây nhỏ ở đỉnh như v1, thu theo cho cân với thân hẹp.
2. **`thunder-energy-column-frames` 2048×768:** bốn khung liên tiếp (cách khoảng 0,1 s), cùng chân, cùng mây: tia chính đổi đường gấp khúc giữa các khung (vẫn từ mây xuống chân), tia phụ bật và tắt quanh nó.
Không chữ, không vật khác.

## Kiểm và tự chấm
Script: bề rộng thân (ở hàng 40 %, 50 %, 60 % chiều cao thân, khoảng điểm ảnh có độ sáng > 50 % độ sáng lớn nhất của hàng, lấy trung vị) bằng 0,6–0,72 lần bản v1; lề ≥ 6 %; chân trên một hàng pixel. Tấm ghép: v1 | v3 cùng cỡ, dải bốn khung, bản thu cao 120 px (tia chính phải còn đọc rõ ở cỡ này). Tự chấm theo mặt yếu nhất (một hai tia chính rõ ràng là nguồn năng lượng, tia phụ lùi lại, hẹp đúng 2/3, đọc là sét không phải khói); dưới 8 vẽ lại. Báo cáo ≤ 200 chữ.

Phản biện: PASS (Sonnet, 13/11)
