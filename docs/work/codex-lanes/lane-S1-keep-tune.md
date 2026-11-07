# Luồng Codex 1 · GIỮ-CHỈNH: kiểm tầng A theo vai trò, dựng bản dẫn xuất và recipe

Anh (07/11 09:30): "những ảnh, video đã đạt về cơ bản, chỉ còn bước dùng blender hoặc chỉnh lại gì đó để lên trên 8 thì giữ lại cho codex chỉnh … cho codex chạy 3 luồng xử lý".

Quy trình đã chốt: `.agents/skills/game-vfx-production/references/path-to-8.md`. Đọc **§1** (5 ô tầng A và ngưỡng), **§2**, **§4** trước.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: `docs/codex-queue/laneS1-report.md` (tiếng Việt). Mỗi việc một đoạn ≤ 6 dòng.

## Danh sách việc
`docs/work/tasks/vfx-streams/stream-1-keep.md`:
- làm **lần lượt từng dòng** có trạng thái `todo`, theo thứ tự;
- mỗi dòng **tự kiểm xong** mới sang dòng kế;
- cập nhật cột trạng thái ngay khi xong một dòng: ghi nguyên tử, chỉ sửa đúng ô trạng thái và ô ghi chú của dòng đó;
- luồng 2 có thể thêm dòng mới ở cuối bảng. Đọc lại file trước mỗi dòng.

## Mỗi việc
1. **Nối nguồn:** key → video `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/video/<job>/take<N>.mp4` → `.prompt.txt` → ảnh đầu (nếu có) → nơi dùng trong lab (grep id trong `games/.wt-ic-lab-all/src/lab/`, các manifest `art-src/lab/vfx/*/manifest.json`). Ghi SHA-256 nguồn.
2. **Soi từng khung** trong đoạn đề xuất (ffmpeg trích mọi khung vào `.local/s1/<job>/frames/`, xoá khi xong). Chốt `in`/`out` theo số khung ở 24 fps.
3. **Kiểm tầng A theo vai trò ghi ở dòng**, đủ 5 ô và có số đo: lề, độ trôi tâm, đổi cỡ, nền p99, alpha mép, khung cuối, chỗ nối nếu là vòng lặp. Đo trên vùng hiệu ứng, không đo cả nền đen.
4. **Dựng bản dẫn xuất** vào `games/immortality-cultivation/art-src/lab/vfx-redo-2026-11-07/keep/<job>/v1/`:
   - clip cắt và chỉnh nhịp (`.mp4`, giữ 1080p);
   - nếu cần matte thì có RGBA;
   - flipbook cắt bằng `tools/vfx-flipbook` (`VFXLAB_HOME=.local/vfxlab-s1`), có KTX2 (`run.sh ktx2`);
   - `recipe.md` ghi: in/out, mọi phép xử lý, đường bao engine đề xuất (scale, alpha, reveal, ăn mòn, thời lượng), lớp còn thiếu (ghi id lớp phụ nếu cần luồng 3 làm), cách ghép vào pha nào;
   - tấm so nguồn và bản dẫn xuất (6 khung).
5. **Kết luận:**
   - `A-PASS`: có bản dẫn xuất và recipe;
   - `A-FAIL→S2`: hình sai, thêm một dòng vào `stream-2-image.md` kèm lý do;
   - `A-FAIL→S3`: chất liệu hỏng, thêm vào `stream-3-blender.md`;
   - `NEE`: thiếu bằng chứng, thêm vào `evidence-missing.md`.
   - **Không tự chấm điểm vẻ đẹp tầng B**; tầng B chấm ở bản ghép.

## Khoá khi ghi file danh sách (bắt buộc, 3 luồng cùng ghi)
Trước khi sửa bất kỳ file nào trong `docs/work/tasks/vfx-streams/`, phải giữ khoá. Các bước:
1. Lấy khoá bằng `mkdir docs/work/tasks/vfx-streams/.lock`. Nếu thất bại thì chờ 5 giây rồi thử lại, tối đa 5 phút.
2. Đọc lại file ngay sau khi giữ khoá, sửa, rồi ghi nguyên tử.
3. Nhả khoá bằng `rmdir docs/work/tasks/vfx-streams/.lock`.
Không giữ khoá lâu hơn thời gian ghi.

## Ranh giới
- **Chỉ ghi:**
  - `art-src/lab/vfx-redo-2026-11-07/keep/`;
  - `.local/s1/`, `.local/vfxlab-s1/`;
  - các file danh sách trong `docs/work/tasks/vfx-streams/` (đúng ô của mình, và thêm dòng chuyển luồng);
  - báo cáo.
- **Không sửa:**
  - video, ảnh nguồn gốc;
  - mọi `manifest.json` đang dùng;
  - mã lab hay game. Việc gắn vào lab do Claude làm.
- **Không:** lệnh git ghi, mở cổng mạng, mở trình duyệt, gọi Blender trực tiếp. Blender chỉ qua `.local/blender-queue/`, nhưng lớp Blender là việc của luồng 3.

## Hết hạn mức
Giữ file, cập nhật trạng thái dòng đang làm thành `doing` kèm ghi chú dừng ở đâu. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
