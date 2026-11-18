# Phiếu 379b · Tu Tiên · Hai hình thử: cột lôi năng lượng DÀY, ít rẽ nhánh (để anh duyệt trước khi làm video)

Anh (13/11 11:5x–12:0x): cột phải "có sự di chuyển của lôi điện… luồng điện sét đang sống"; "nên vẽ 1 2 hình cho tôi xem trước"; và: "**nó nên là 1 cột năng lượng dày, ít rẽ nhánh chứ k nên dùng dạng nhỏ mỏng, như vậy ms thể hiện được sức mạnh**, chứ mỏng như này dù bạn có ghép cũng ghép rất nhiều cột lôi mới bớt mỏng được". Phiếu 379 (bó tia mảnh, nhiều nhánh) đã huỷ vì sai hướng. Cột 367 (bện xoắn) và 378 (tia mảnh song song) đều quá mỏng.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 6 lần `image_gen`**, `view_image` tối đa 8. Báo cáo `docs/codex-queue/379b-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-energy-column.v1-try*.png`, `S/thunder-energy-column-frames.v1-try*.png`, một `.prompt.txt` cho mỗi ảnh (ghi đường dẫn tham chiếu), tấm ghép `S/thunder-energy-379b-sheet.jpg`. Cấm git ghi, sửa file có sẵn, mã.

## Tham chiếu (`view_image`)
`S/thunder-stream-a.v1-try1.png` (khổ, chân, mây nhỏ, bộ màu: giữ; **thân quá mảnh: không theo**), `S/thunder-single-bolt-a.v4-try9.png` (nét sét và màu bạch kim đã duyệt).

## Hai hình, nền đen thuần, nhìn ngang hơi từ trên (30°), bạch kim D65 (trắng ngà, vàng nhạt; không xanh, tím, cam đậm)
1. **`thunder-energy-column` 1024×1536: một cột năng lượng sét dày, đặc.** Thân cột **rộng khoảng 1/3 chiều cao**, là một khối plasma sét đặc: lõi trắng ngà sáng rực ở giữa, ra rìa chuyển vàng nhạt rồi mờ vào nền; **bề mặt thân có điện sống**: các vằn sét sáng chạy dọc và xiên trên mặt cột như dòng chảy, chỗ dồn sáng chỗ tối hơn, vài cung điện ngắn bật khỏi rìa thân rồi rút lại. **Ít rẽ nhánh**: chỉ 2–4 nhánh ngắn ở rìa, không có tia mảnh rời. Chân cột nổ chạm đất, điện bò lan và đá vụn bắn; đỉnh cột cắm vào mây mực **nhỏ, gọn** có chớp bên trong. Cảm giác: nặng, đặc, uy lực, một trụ năng lượng đang cuộn chảy, **không phải bó dây, không phải ống trơn**.
2. **`thunder-energy-column-frames` 2048×768: bốn khung liên tiếp của cùng cột** (cách nhau khoảng 0,1 s), cùng khổ, cùng chân và mây: thấy các vằn sét trên mặt cột trôi lên/xuống, chỗ dồn sáng dời đi, cung điện ở rìa bật ra rồi tắt; bề rộng thân giữ nguyên.
Không chữ, không vật khác.

## Kiểm và tự chấm
Script: lề ≥ 6 %, chân trên một hàng pixel, thân rộng ≥ 28 % chiều cao (đo bề rộng vùng sáng > 50 % ở giữa thân), trắng thuần (> 245) ≤ 10 % diện tích. Tấm ghép: cột 378 A (`S/thunder-stream-a.v1-try1.png`) | cột năng lượng mới cùng cỡ; dải bốn khung; bản thu cao 120 px. Tự chấm theo mặt yếu nhất (dày đặc uy lực, ít nhánh, thấy điện đang chạy trên mặt cột, không ra ống trơn, hợp bạch kim); dưới 8 vẽ lại. Báo cáo ≤ 200 chữ.

Phản biện: PASS (Sonnet, 13/11)
