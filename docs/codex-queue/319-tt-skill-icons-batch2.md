# Phiếu 319 · Tu Tiên · Ảnh 2D: bộ biểu tượng kỹ năng đợt 2 (30 chiêu mở rộng A1–D8), 2 hướng, có tự chấm ở cỡ thật

Anh (06/11): "các ảnh hướng biểu tượng kỹ năng đều đẹp, nếu có thể cứ làm cả 2". Đợt 1 (phiếu 316) đã xong 25 chiêu. Đợt này làm 30 chiêu mở rộng anh duyệt 05/11 20:20, mỗi chiêu 2 biểu tượng, đúng cách làm và hai câu FRAME của phiếu 314/316.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 60 lần gọi `image_gen` (30 chiêu × 2 hướng), cộng tối đa 6 lần vẽ lại cho biểu tượng tự chấm dưới 8.** Báo cáo: `docs/codex-queue/319-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`D = games/immortality-cultivation/art-src/lab/ui/skill-icons`. `S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. **Được ghi:** chỉ thêm file mới vào `D` (`cp -n`) và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài làm tham chiếu.

## Danh sách chiêu
- 30 mục trong `games/immortality-cultivation/art-src/lab/vfx/expansion/manifest.json` (mỗi mục có `code` A1–D8 và id). Tên tiếng Anh và mô tả ở bảng của `docs/games/tu-tien/skills/SKILLS_EXPANSION_2026-11-05.md`.
- Ảnh anh đã duyệt của mỗi chiêu: `S/<id>.v1-try1.png` (ví dụ `S/myriad-lotus-domain.v1-try1.png`). Mở ảnh này bằng `view_image` trước khi vẽ.
- Mỗi chiêu rút ra **một hình chính đậm, đơn giản** đọc được ở 32 px:
  - A (diện rộng): hình dạng của trận, ví dụ đóa sen, vết nứt chéo, lưới sét lục giác.
  - B (pháp tướng): bóng bán thân pháp tướng có dáng đặc trưng (ba đầu sáu tay, xòe tay, kiếm vòng sau lưng).
  - C (thần thú): đầu hoặc dáng vồ của thần thú, bằng năng lượng trong suốt, không phải con vật thật.
  - D (pháp bảo): chính pháp bảo đó (ấn, chuông, hồ lô, đỉnh, tháp, gương, dải lụa, cờ).

  Ghi câu mô tả hình chính vào `.prompt.txt`.

## Cách làm mỗi biểu tượng
1. Mở bằng `view_image`: ảnh mẫu đạt của hướng (`D/ink-gold-meteor-rain-fire.v1-try1.png` hoặc `D/jewel-crest-meteor-rain-fire.v1-try1.png`) và ảnh của chiêu trong `S/`.
2. Gọi `image_gen`, khổ vuông, prompt giống phiếu 314. Thay `<FRAME>` theo hướng (giữ nguyên văn của 314) và `<MOTIF>` bằng câu hình chính, trong màu của hệ chính của chiêu (hệ đầu tiên trong bảng).
3. Chép `cp -n` thành `D/<hướng>-<id>.v1-try1.png`, với id lấy từ manifest. Tạo thêm bản `-48` và `-32`. Ghi `.prompt.txt` (công cụ, ảnh tham chiếu, prompt, khổ thật).
4. **Tự chấm ở 32 và 48 px:** đọc ra chiêu gì, độ cuốn hút và sang trọng, khung và hình có tách bạch không, sạch. Dưới 8 thì vẽ lại một lần (`-try2`) và chọn bản điểm cao hơn.
5. Ghép tấm `D/icons-batch2-<hướng>.png`: lưới các bản 48 px kèm mã và tên chiêu tiếng Anh, trên nền #15171c. Kiểm tấm ghép bằng `view_image` trước khi báo cáo (đợt 1 từng lệch ô vì cách căn chữ của ImageMagick).

## Xong khi
- Đủ biểu tượng cho 30 chiêu × 2 hướng, cộng bản thu nhỏ và 2 tấm ghép đúng ô.
- Báo cáo có bảng: mã, chiêu, hình chính, điểm 32 và 48 px của từng hướng; ghi rõ chiêu nào phải vẽ lại.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
