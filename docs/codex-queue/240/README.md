# Hồ sơ phiếu 240

Báo cáo chính: [240-report.md](../240-report.md). Ảnh giao và hồ sơ trong [art-src/_review/240](../../../games/typing-survival/art-src/_review/240/).

- `generated-files.json`: chín lần sinh thành công bằng công cụ tích hợp `image_gen.imagegen`, nguồn công cụ và prompt nguyên văn. Mọi nguồn `.try*` nằm cạnh prompt tại đúng thư mục icon hoặc part.
- `jobs.json`, `jobs-retries.json`, `job-station2.json`, `job-station3.json`: các prompt theo lượt. `selection.json` ghi năm bản chọn, công thức hậu kỳ và số đo.
- `core.mjs`, `process.mjs`, `finalize-candidates.mjs`: các bước hậu kỳ đã dùng. Giữ cả ứng viên trung gian để đối chiếu. `finalize-candidates.mjs` ghi lại ứng viên đầu; căn ô đạn và chọn tháp lần cuối được mô tả đầy đủ trong `replay.mjs`.
- `replay.mjs <nhãn-mới>`: tái lập từ nguồn sinh vào `_review/240/replay-<nhãn-mới>/`, so pixel với bản giao; không ghi lại file giao. Ví dụ: `ART_MAGICK=/opt/homebrew/bin/magick node docs/codex-queue/240/replay.mjs doi-chieu-moi`.
- `deliver.mjs`: đã sao lưu bản cũ trước mọi ghi đè, rồi chép đúng năm tên. **Không chạy lại** trên bộ đã giao; kiểm đồng thời sẽ từ chối.
- `review.mjs`: ghép hai tờ xem, đọc bộ chọn; ảnh ô đạn cũ đọc từ `prev/`. Không sửa ảnh nguồn. Tờ cỡ thật là tờ chấm chính; tờ nearest chỉ giúp soi mất nét.
- `verify.mjs`: kiểm đọc MD5, bản sao cũ, khổ/kênh, prompt nguyên văn và Lanczos trực tiếp từ master. Chạy `node docs/codex-queue/240/verify.mjs`; `--save` chỉ cập nhật hồ sơ kiểm trong `_review/240/`.

`integrityPass` chỉ nói bảo toàn file, đúng khổ/kênh, đúng prompt và phép thu; **không phải** nghiệm thu mỹ thuật hay chứng nhận toàn bộ kiểm số. Ngoại lệ alpha và IoU được giữ nguyên trong báo cáo và JSON. Chưa có điểm chấm lại của Claude.
