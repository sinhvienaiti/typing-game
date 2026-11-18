# Phiếu 316 · Tu Tiên · Ảnh 2D: bộ biểu tượng kỹ năng đợt 1 (Kiếm 0–7, cột trụ và tuyệt kỹ phím 8), 2 hướng, có tự chấm ở cỡ thật

Anh (06/11): "các ảnh hướng biểu tượng kỹ năng đều đẹp, nếu có thể cứ làm cả 2". Hai hướng **ink-gold** và **jewel-crest** của phiếu 314 (mẫu đạt: `D/ink-gold-meteor-rain-fire.v1-try1.png`, `D/jewel-crest-meteor-rain-fire.v1-try1.png`). Đợt này: 8 chiêu Kiếm và 17 mục phím 8, mỗi chiêu 2 biểu tượng.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 50 lần gọi `image_gen` (25 chiêu × 2 hướng), cộng tối đa 6 lần vẽ lại cho biểu tượng tự chấm dưới 8.** Báo cáo: `docs/codex-queue/316-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`D = games/immortality-cultivation/art-src/lab/ui/skill-icons`. `S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. **Được ghi:** chỉ thêm file mới vào `D` (`cp -n`) và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài làm tham chiếu.

## Danh sách chiêu (tự đọc, mỗi chiêu một hình chính)
- **Kiếm, phím 0–7:** bảng "Kiếm" trong `docs/games/tu-tien/skills/PRODUCTION_LIST_2026-11-05.md` §2 (Phi Kiếm, Ngự Kiếm Quyết, Song Long, Hồi Kiếm Hộ Thân, Lưu Quang Bộ, Lạc Kiếm Trận, tuyệt kỹ Thiên Hà Kiếm Vũ, Vạn Phong Thính Chiếu). Chất liệu mặc định là Kim (ánh thép bạc, vàng nhạt).
- **Phím 8 (17 mục):** các tệp `games/immortality-cultivation/art-src/lab/vfx/ult/manifest.json` (mỗi mục có id và ảnh nguồn). Đối chiếu tên trong `PRODUCTION_LIST_2026-11-05.md` §4 (tuyệt kỹ của hệ) và §7 (cột trụ).
- Với mỗi chiêu, mở ảnh nguồn trong `S/` nếu có (ảnh anh đã duyệt), rồi rút ra **một hình chính đậm, đơn giản** đọc được ở 32 px. Ví dụ: một thanh kiếm bay có vệt; hai con rồng khí xoắn; vòm kiếm che; cột sét giáng; biển xoáy. Ghi câu mô tả hình chính vào `.prompt.txt`.
- Lưỡi liềm (nếu có) quay **mặt lồi về phía trước** theo hướng bay.

## Cách làm mỗi biểu tượng
1. Mở bằng `view_image` ảnh mẫu đạt của hướng đó và ảnh nguồn của chiêu (nếu có).
2. Gọi `image_gen`, khổ vuông, prompt giống phiếu 314. Thay `<FRAME>` theo hướng (giữ nguyên văn của 314) và `<MOTIF>` bằng câu hình chính, trong màu của hệ chiêu đó.
3. Chép `cp -n` thành `D/<hướng>-<id chiêu, tiếng Anh, kebab-case>.v1-try1.png`. Tạo thêm bản `-48` và `-32`. Ghi `.prompt.txt`.
4. **Tự chấm ở 32 và 48 px:** đọc ra chiêu gì, độ cuốn hút, khung và hình có tách bạch không, sạch. Dưới 8 thì vẽ lại một lần.
5. Ghép tấm `D/icons-batch1-<hướng>.png`: lưới các bản 48 px kèm tên chiêu tiếng Anh, trên nền #15171c.

## Xong khi
- Đủ biểu tượng cho 25 chiêu × 2 hướng, cộng bản thu nhỏ và 2 tấm ghép.
- Báo cáo có bảng: chiêu, hình chính, điểm 32 px của từng hướng.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
