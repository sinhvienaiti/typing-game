# Phiếu 367 · Tu Tiên · Linh kiện: cột lôi (bó sợi sét bện thẳng đứng), 3 biến thể

Anh (12/11 18:3x, sau Ngũ Lôi v23): "liên quan tới việc toả lôi điện ra 8 hướng, bạn nên tạo những dạng hình cột để phù hợp hơn, chứ hình hiện tại bạn đang dùng, nó dạng nhành cây, k hợp cho việc đó lắm". Tám cột đang dùng tia đơn đánh từ trời (toả nhánh như cành cây). Cần **một linh kiện cột** cho cột chạy ngang trên đất.
Giữ luật anh 07/11 (ghi ở `docs/work/tasks/five-thunder-lab.md`, mục "Anh nói gì"): cột sét **chỉ là tia sét**, không vỏ trụ, không ống sáng. Vì vậy cột là **một bó nhiều sợi sét xoắn bện** thành thân cột, có khe tối giữa các sợi; **không** ống sáng trơn, không vỏ trụ, không hình học phẳng.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 10 lần `image_gen`**, `view_image` tối đa 12. Báo cáo `docs/codex-queue/367-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-column-{a,b,c}.v1-try*.png`, `S/thunder-column-{a,b,c}-core.v1-try*.png`, mỗi ảnh một `.prompt.txt` (ghi đường dẫn tham chiếu), tấm ghép `S/thunder-column-367-sheet.jpg`. Cấm git ghi, sửa file có sẵn, mã.

## Tham chiếu (`view_image`)
`S/thunder-single-bolt-a.v4-try9.png` (nét sét bạch kim đã duyệt: lấy chất nét, bỏ hình cành), `S/thunder-five-cloud-ink.v4-try2.png` (mây mực cho ngọn cột), `S/thunder-trail-rock.v1-try*.png` (đá sân cho chân cột). Bộ màu D65 trong `docs/games/tu-tien/00-canon.md`: trắng ngà, vàng nhạt, mây mực xám đen; không xanh, tím, cam đậm.

## Ba biến thể (`a`, `b`, `c`), khổ dọc 1024×1536
Nhìn ngang hơi từ trên (camera 30° từ trên), một cột đứng giữa khung:
- **Thân:** 6–10 sợi sét bạch kim xoắn bện quanh một trục thẳng đứng, sợi chạy dọc từ chân lên ngọn, cao gấp khoảng 4 lần bề ngang; vài sợi ngắn văng ra ngoài thân rồi quay lại; **chỉ sợi, không phân nhánh** (bộ D65 cho tia trời có nhiều nhánh mảnh, nhưng cột này không có nhánh nào); khe tối giữa các sợi.
- **Chân:** quầng điện sát đất toả ngang, đá vụn và bụi bắn lên thấp; chân cột phẳng trên một đường đất (để code đặt lên sân).
- **Ngọn:** tan vào một mảng mây mực nhỏ ở mép trên (lề ≥ 6 %).
- Khác nhau giữa a, b, c: kiểu bện (xoắn chặt / lỏng / hai bó quấn nhau), độ dày, số sợi văng ra.
Nền đen thuần (để cộng sáng). Không chữ, không vật khác.
**Ảnh `-core`:** sửa từ chính ảnh cột đã chọn, chỉ giữ các lõi sợi trắng mảnh trên nền đen, chồng khít, để code làm nhấp nháy riêng.

## Kiểm và tự chấm
Script: lề, chân cột nằm trên một hàng pixel (độ lệch ≤ 2 % chiều cao), ảnh core chồng khít (so mặt nạ), trắng thuần (> 245) ≤ 6 % diện tích. Tấm ghép: ba cột + bản thu về cao 120 px đặt cạnh nhau để xem ở camera chơi. Tự chấm theo mặt yếu nhất (đọc ra là cột, không ra cành cây, không ra ống trơn, hợp bộ bạch kim, ba biến thể khác rõ); dưới 8 vẽ lại. Báo cáo ≤ 300 chữ.

Phản biện: PASS (Sonnet, 12/11; hai sửa đã làm)
