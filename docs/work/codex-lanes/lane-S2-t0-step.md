# Luồng Codex 2 · T0 chia nhỏ: mỗi lần chạy làm **một bước** rồi dừng

Anh (07/11 10:00): "Giảm và chia nhỏ". Lý do: một lần chạy dài thì Codex gửi lại toàn bộ ngữ cảnh ở mỗi bước. Mỗi lần chạy dài sáng nay tốn 2,5–6,3 triệu token đầu vào. Chia nhỏ để mỗi lần bắt đầu với ngữ cảnh mới.

Việc T0 và các luật phân loại: `docs/work/codex-lanes/lane-S2-triage-and-image.md` (mục T0, mục Khoá) và `.agents/skills/game-vfx-production/references/path-to-8.md` §2, §4. **Chỉ đọc các phần đó**, không đọc lại toàn bộ tài liệu khác.

**Model `gpt-6.1-sol`, mức `high`.**

## Trạng thái đã có (lần chạy trước bị dừng giữa chừng, 09:50)
`.local/s2/checkpoint.json` (`processed`, `total`), `.local/s2/decisions.json` (đã xếp 400/640 key thành 301 việc).

## Mỗi lần chạy: làm đúng MỘT bước đầu tiên còn dang dở, ghi checkpoint, rồi dừng
1. **Còn key chưa xếp mà đã có kết quả chấm trong `.local/video-review/results/`:**
   - xếp **tối đa 80 key** từ lý do trong JSON;
   - chỉ mở tấm 6 khung khi lý do mơ hồ, **tối đa 5 tấm**.
2. **Còn key chưa xếp mà chưa có kết quả chấm** (`todo/batch-10…13`):
   - xem tấm 6 khung của **tối đa 15 key**;
   - kiểm tầng A theo `use`, rồi xếp.
3. **Đã xếp đủ 640 mà chưa ghi danh sách:**
   - ghi các dòng vào `docs/work/tasks/vfx-streams/*.md` (theo luật Khoá);
   - chạy script đếm phủ: đủ 640, không key nào trùng hay sót;
   - báo cáo bảng tổng số việc theo nhãn và theo ưu tiên vào `docs/codex-queue/laneS2-report.md`.
4. **Đã ghi xong:** ghi một dòng "T0 xong" vào báo cáo rồi dừng ngay.

Sau mỗi bước, cập nhật `.local/s2/decisions.json` và `.local/s2/checkpoint.json` ngay (ghi nguyên tử). Thêm một dòng ngắn vào `docs/codex-queue/laneS2-report.md`: bước nào, số key, còn bao nhiêu.

## Ranh giới
- **Chỉ ghi:**
  - `.local/s2/`;
  - `docs/work/tasks/vfx-streams/` (bước 3, có khoá);
  - báo cáo.
- **Không:**
  - sửa media, manifest hay mã;
  - tạo ảnh hay video;
  - lệnh git ghi, mở cổng mạng, mở trình duyệt.

## Hết hạn mức
Ghi checkpoint. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
