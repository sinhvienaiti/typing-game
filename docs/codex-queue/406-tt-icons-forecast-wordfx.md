# Phiếu 406: Nối icon tinh anh/boss, sửa thẻ dự báo đè Shop, làm hiệu ứng chữ sống động hơn


Phản biện: PASS (Sonnet, 16/11)
## Bối cảnh
- Owner 16/11/2026 chọn icon: tinh anh **E1 Khiên ngọc**, boss **B1 Vương miện** (bảng `games/immortality-cultivation/art-src/ui/icons/foe-icons-sheet-401.jpg`, file nguồn và bản 32/48 px cùng thư mục, E1 = `foe-elite-jade-shield*` (tên đúng xem bằng ls), B1 = `foe-boss-imperial-crown.v1-try1*`; xem `401-report.md`).
- Agent Claude chụp kiểm 400 + 394b: ở 1920×1080 lúc chuẩn bị, thẻ dự báo đợt đè đáy ngăn Shop (khoảng x 1510–1910, y 795–925).
- Hiệu ứng chữ 400 đúng các bước nhưng còn nhạt so với chuẩn 9 của hệ dùng chung (`docs/games/SHARED_SYSTEMS_BAR.md`): chữ chỉ bay lên ~22 px, nảy vàng gần như không thấy. Ảnh: `typing-game-review/owner-review/2026-11-16/tu-tien/word-fx/`. Owner muốn chữ "sống động".

## Việc (trong `games/immortality-cultivation/`)
1. Nối icon E1 vào quái tinh anh, B1 vào boss, ở chỗ cắm phiếu 394b đã để sẵn. Icon nổi trên đầu quái, cỡ 28–32 px ở 1080p, luôn quay về camera, không che quái khác quá mức; dùng chung một instanced/sprite batch, không mỗi quái một phần tử DOM. Copy icon vào `public/assets/` theo cách các icon HUD khác được nạp (không đưa media vào Git).
2. Thẻ dự báo đợt không đè Shop ở 1280×720 và 1920×1080 (đo bằng DOM rect, giao cắt = 0).
3. Hiệu ứng chữ sống động hơn, giữ thứ tự trạng thái và luật ≤ 50 ms của 400:
   - chữ gõ đúng nảy rõ (scale 1,18–1,25 trong ~80 ms, có chút sáng vàng);
   - gõ xong: từ tấn công tách chữ bay lên 70–110 px theo đường cong, xoay nhẹ, kèm vệt hạt sáng; từ phòng thủ rơi 50–80 px như rụng xuống, nảy nhẹ một lần; mờ hết trong 0,55–0,7 s;
   - chữ bay được phép vượt ra ngoài ô (overlay riêng) nhưng không đè lõi, cổng, ô trụ, cảnh báo;
   - giảm chuyển động vẫn chỉ mờ dần.
   Chỉ dùng `transform`/`opacity` hoặc canvas overlay có pool.

## Nghiệm thu
- `pnpm test` và typecheck sạch; test cho icon theo loại quái, giao cắt Shop = 0, thời lượng và biên độ hiệu ứng.
- Để lệnh chụp cho Claude (sandbox chặn trình duyệt): khung lúc chuẩn bị ở 1920, dải khung hiệu ứng chữ tấn công và phòng thủ, quái tinh anh và boss mang icon.
- Chỉ sửa `src/ui/`, `src/view/` (file icon mới, `actors.ts` nếu cần), `src/app/app.ts` nếu cần, test. Không đụng `src/sim/`, `src/lab/`, bản đồ. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/406-report.md`.
