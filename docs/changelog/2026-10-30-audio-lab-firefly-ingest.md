# Audio Lab: nhận WAV Adobe Firefly của chủ dự án

Phiếu 217 thêm `run.sh firefly ingest`, `listen`, `status` cho Dragonhold, Wordwoven và Last Line. Inbox chỉ đọc; mọi đường inbox/đầu ra đều phải chỉ rõ. Tách take cấu hình được, raw L1 giữ nguyên ngưỡng, loại cú chồng và tương quan cao, xếp hạng theo một bảng trọng số, dựng công thức một lớp qua build rồi kiểm final L1. Thiếu take không nhân bản hoặc đổi cao độ.

Bản nghe MP3 192 kbps dài 20 giây, fade cuối 50 ms; dùng context khi có chỗ và đủ giọng cache, nếu thiếu thì sequence. Status hiển thị cả id chưa có nguồn, id lạ và file bỏ qua. Không ghi giọng mới, không tự gắn âm vào game hoặc release.

Thêm lớp `LicenseRef-Adobe-Firefly-owner` với điều kiện `adobe-model` theo quyết định chủ dự án 29/10. Dòng sổ và bản ghi quyết định đi qua luồng copies hiện có tới release. Chặn model thiếu/đối tác và quyền phát lại file thô. **Chờ Claude xác nhận lớp, họ model, cờ chấm cục bộ và bổ sung bản lưu điều khoản Adobe có ngày**; ghi chú hiện có không thay thế điều khoản chính thức.

Kết quả test, demo kỹ thuật, kiểm dựng lại và giới hạn sandbox: [`217-report.md`](../codex-queue/217-report.md). Chưa đánh giá chất lượng nghe trên WAV thật của chủ dự án.
