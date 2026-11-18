# Phiếu 379 · Tu Tiên · Hai hình thử: cột lôi "luồng điện đang sống" (để anh duyệt trước khi làm video)

Anh (13/11 11:4x): cột lôi "không phải dạng đổ thẳng, nó phải có sự di chuyển của lôi điện, chứ không phải hình ảnh cứng, mà nó phải cho cảm có luồng điện sét đang sống"; rồi (11:5x): "nên vẽ 1 2 hình cho tôi xem trước tránh việc sai rồi tạo video sai". Cột bện 367 đọc như lốc xoáy; cột đổ thẳng 378 nhân lên thành thanh đèn cứng. Cần hình **cho thấy chuyển động trong một ảnh tĩnh**.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 6 lần `image_gen`**, `view_image` tối đa 8. Báo cáo `docs/codex-queue/379-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-living-column.v1-try*.png`, `S/thunder-living-column-frames.v1-try*.png`, một `.prompt.txt` cho mỗi ảnh (ghi đường dẫn tham chiếu), tấm ghép `S/thunder-living-379-sheet.jpg`. Cấm git ghi, sửa file có sẵn, mã.

## Tham chiếu (`view_image`)
`S/thunder-stream-a.v1-try1.png` (khổ, chân, mây nhỏ, bộ màu: giữ), `S/thunder-column-a.v1-try1.png` (để tránh: bện xoắn đều), `S/thunder-single-bolt-a.v4-try9.png` (nét sét bạch kim đã duyệt).

## Hai hình, nền đen thuần, nhìn ngang hơi từ trên (30°), bạch kim D65 (trắng ngà, vàng nhạt; không xanh, tím, cam đậm)
1. **`thunder-living-column` 1024×1536: một cột lôi đang sống, chụp giữa chuyển động.** Thân cột là một bó sét **không đều**: các tia gấp khúc gắt, mỗi tia một nhịp khác nhau; có tia đang **leo ngược lên** dọc thân (đầu tia sáng nhất, đuôi mờ dần như vệt chuyển động), có tia đang **đánh xuống**, có tia **bật nhánh ngang** ra khỏi thân rồi gãy tắt giữa không trung; quanh thân có các cung điện nhỏ **nhảy cóc** giữa các tia; vài chỗ thân **phình sáng** (chớp) và vài chỗ **thắt tối**; chân cột điện bò lan trên đất và tia lửa bắn; mây mực nhỏ ở đỉnh có chớp bên trong. Cột đứng một chỗ, dáng tổng thể thẳng đứng, **nhưng không tia nào song song đều, không xoắn đều**: cảm giác giận dữ, hỗn loạn, đang chuyển động.
2. **`thunder-living-column-frames` 2048×768: bốn khung liên tiếp của cùng cột** (cách nhau khoảng 0,1 s) đặt cạnh nhau, để thấy các tia đổi đường đi, tia leo lên cao dần, nhánh ngang bật ra rồi tắt, chỗ phình sáng dời chỗ. Bốn khung cùng khổ, cùng vị trí chân và mây.
Không chữ, không vật khác.

## Kiểm và tự chấm
Script: lề ≥ 6 %, chân trên một hàng pixel, trắng thuần (> 245) ≤ 6 %. Tấm ghép: cột 367 | cột 378 | cột sống mới, cùng cỡ; dưới là dải bốn khung; và bản thu cao 120 px. Tự chấm theo mặt yếu nhất (nhìn một ảnh tĩnh mà thấy được điện đang chạy; không ra lốc xoáy; không ra thanh đèn; hợp bạch kim); dưới 8 vẽ lại. Báo cáo ≤ 200 chữ.

Phản biện: PASS (Sonnet, 13/11)
