# Phiếu 364 · Tu Tiên · Sửa năm ảnh kỹ năng (backlog D01–D05)

Theo `docs/work/tasks/image-backlog.md` D01–D05 và luật linh kiện của anh (AGENTS.md "Components first", 12/11): mỗi ảnh là **một linh kiện** dùng lại được, tách lớp để code tô màu và làm tan.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 12 lần `image_gen`**, `view_image` tối đa 14. Báo cáo `docs/codex-queue/364-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm đúng các tên tệp ghi ở từng việc dưới đây (và `S/metal-rift-groove.v2-try*.png` cho D05), `.prompt.txt`, tấm ghép `S/vfx-364-sheet.jpg`. Cấm git ghi, sửa file có sẵn, mã.

## Việc (tham chiếu là chính ảnh cũ)
1. **D01 dấu đất Hỏa** từ `S/fire-ground-mark.v1-try1.jpg`: hai ảnh `S/fire-ground-mark-rock.v1-try*.png` (nền đá nứt cháy tối) và `S/fire-ground-mark-glow.v1-try*.png` ( chỉ lớp lửa/than phát sáng trên nền đen thuần để cộng sáng). Nhìn thẳng từ trên, cùng khung, chồng khít.
2. **D02 dấu đất Thủy** từ `S/water-ground-mark-clean.v1-try1.jpg`: tách như trên: `S/water-ground-mark-rock.v1-try*.png` (đá ướt), `S/water-ground-mark-glow.v1-try*.png` (lớp nước sáng).
3. **D03 tuyệt kỹ Băng** từ `S/ult-ice-cold-silence-clean.v1-try1.jpg`, tách linh kiện: `S/ult-ice-crystal.v1-try*.png` (cụm nhũ băng riêng, lề ≥ 8 %, nền đen) và `S/ult-ice-crystal-mask.v1-try*.png` (mặt nạ trắng-đen cùng khung).
4. **D04 tuyệt kỹ Lôi** từ `S/ult-thunder-nine-heavens-v2.v1-try3.png`: chỉ làm lớp mây tối riêng (linh kiện phụ thuộc bố cục, được phép): `S/ult-thunder-cloud-dark.v1-try*.png`, mây không cắt mép trên, bạch kim lôi D65 (mây mực xám đen, ánh trắng ngà vàng nhạt).
5. **D05 vạch nứt sáng Kim** 2048×128 lặp liền theo trục x, tham chiếu `S/metal-rift-groove.v1-try1.*`, `S/metal-crack-star.v1-try1.*`.
Lớp phát sáng: nền đen thuần, không quầng quá 0,9 mỗi kênh. Không chữ.

## Kiểm và tự chấm
Script: lề, mép lặp D05 (cột đầu so cột cuối), hai lớp tách chồng khít. Tấm ghép trước/sau. Tự chấm theo mặt yếu nhất; dưới 8 vẽ lại. Báo cáo ≤ 300 chữ.

Phản biện: PASS (Sonnet, 12/11; lỗi phản biện nêu đã sửa)
