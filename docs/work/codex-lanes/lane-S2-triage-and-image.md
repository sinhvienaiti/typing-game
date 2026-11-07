# Luồng Codex 2 · Phân loại toàn kho (T0), sau đó LÀM-LẠI-ẢNH

Anh (07/11 09:30): "cái nào thực sự chưa đạt thì kêu codex xử lý lại lần lượt từng cái, cho codex chạy 3 luồng xử lý đi, list ra các việc đầy đủ vào file để nó triển khai".

Quy trình đã chốt: `.agents/skills/game-vfx-production/references/path-to-8.md`. Đọc §1, §2, §4, §5. Bản phản biện chi tiết: `docs/work/consult/codex-path-to-8.md` §6.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: `docs/codex-queue/laneS2-report.md` (tiếng Việt).

## Việc T0 · Phân loại toàn kho thành danh sách việc đầy đủ (làm trước)
- **Đầu vào:**
  - `.local/video-review/clips.json` (640 bản take);
  - các kết quả đã chấm trong `.local/video-review/results/` (467 key, `batch-01`…`09` và `redo-01`);
  - tấm 6 khung trong `.local/video-review/sheets/`;
  - hàng việc `docs/work/tasks/firefly-sprint-video.json` (trường `image`, `still`, `use`).
- **Đơn vị** là việc + vai trò + đoạn dùng (§4). Mỗi việc có đúng **một** nhãn: GIỮ-CHỈNH, LÀM-LẠI-ẢNH (ảnh `giữ`, `sửa` hoặc `mới`), LÀM-LẠI-BLENDER, BỎ; hoặc trạng thái NEE.
  - Gộp bản trùng, bản bị thay thế (v1 → v2, `-q1` → gốc) và chọn take chính theo toàn kho.
  - Nhãn DROP cũ phần lớn là take thừa, không có nghĩa cả việc bị bỏ.
- **Clip đã chấm:** định tuyến từ lý do trong JSON. Chỗ nào mơ hồ thì xem lại tấm 6 khung. **Không** viết lại nhận xét dài.
- **Clip chưa chấm** (các key trong `todo/batch-10…13.json` chưa có kết quả): xem tấm 6 khung, kiểm tầng A theo vai trò ghi trong `use`, rồi định tuyến.
- **Chẩn đoán** theo §2: ảnh sai, khớp khung sai, hay model trôi về sau. Chỉ trường hợp ảnh sai mới gắn `ảnh=sửa` hoặc `mới`.
- **Ưu tiên** theo §4:
  1. đang có đường gọi trong lab (grep id trong `games/.wt-ic-lab-all/src/lab/` và các manifest `art-src/lab/vfx/*/manifest.json`);
  2. dùng lại nhiều;
  3. thuộc chiêu mẫu năm pha;
  4. chưa nối.
- **Đầu ra:** thêm dòng vào đúng file trong `docs/work/tasks/vfx-streams/`:
  - `stream-1-keep.md`: thêm sau 20 dòng có sẵn, không đụng 20 dòng đó;
  - `stream-2-image.md`, `stream-3-blender.md`, `evidence-missing.md`, `drop.md`.
  - Mỗi dòng ghi: key hoặc việc, vai trò và đoạn đề xuất, lý do và việc cần làm, ưu tiên, trạng thái `todo`.
- Làm **từng nhóm 50 key**, ghi file sau mỗi nhóm để chạy lại được. Cuối cùng in bảng tổng: số việc mỗi nhãn, mỗi ưu tiên.
- **Đạt khi:**
  - mọi key trong `clips.json` thuộc đúng một việc có nhãn hoặc NEE, kiểm bằng script đếm: tổng khớp 640, không key nào bị bỏ sót hay trùng;
  - mỗi dòng LÀM-LẠI-ẢNH có cột ảnh;
  - không dòng nào do T0 thêm mà mang `A-PASS` (T0 chỉ định tuyến; chứng nhận là việc của luồng 1).

## Sau T0 · LÀM-LẠI-ẢNH, lần lượt từng dòng của `stream-2-image.md`
**Chưa làm phần này** cho tới khi Claude thêm dòng phiếu mới vào làn. Anh cần chọn kiểu ảnh từ 2 mẫu đã gửi (`owner-review/2026-11-07/tu-tien/still-samples/`) trước khi vẽ lô. Phiếu sau sẽ ghi cách vẽ (§5), tham chiếu nội bộ, hai mẫu trước lô, và cách Claude chạy Firefly image-to-video.

## Khoá khi ghi file danh sách (bắt buộc, 3 luồng cùng ghi)
Trước khi sửa bất kỳ file nào trong `docs/work/tasks/vfx-streams/`, phải giữ khoá. Các bước:
1. Lấy khoá bằng `mkdir docs/work/tasks/vfx-streams/.lock`. Nếu thất bại thì chờ 5 giây rồi thử lại, tối đa 5 phút.
2. Đọc lại file ngay sau khi giữ khoá, sửa, rồi ghi nguyên tử.
3. Nhả khoá bằng `rmdir docs/work/tasks/vfx-streams/.lock`.
Không giữ khoá lâu hơn thời gian ghi.

## Ranh giới
- **Chỉ ghi:**
  - các file trong `docs/work/tasks/vfx-streams/`;
  - `.local/s2/`;
  - báo cáo.
- **Không:** sửa media, manifest hay mã; lệnh git ghi; mở cổng mạng; mở trình duyệt; tạo ảnh hay video trong T0.

## Hết hạn mức
Giữ phần đã ghi; báo cáo nhóm đang dở. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
