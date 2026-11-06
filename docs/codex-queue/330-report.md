# Phiếu 330 · Âm Firefly theo hệ cho lab

Đã thêm **122 thư mục sự kiện, 366 file Ogg Vorbis**, tổng 25.960.199 byte. Mỗi thư mục dùng `take1.wav`–`take3.wav`, đổi thành `01.ogg`–`03.ogg`; giữ nguyên 48 kHz, stereo và độ dài, không cắt hoặc chuẩn hóa.

- Script: `games/.wt-ic-lab-panel/scripts/audio/lab-element-sounds.mjs`.
- Âm: `games/immortality-cultivation/art-src/lab/audio/<sự-kiện>/01.ogg`–`03.ogg`, theo bảng dưới.
- Cùng thư mục âm: gộp `manifest.json`; bổ sung `SOURCES.json.events` và `SOURCES.json.fireflySprint20261105.events`, giữ cấu trúc `variants → layers`, ghi việc nguồn, đường dẫn take, tệp prompt và nguyên văn prompt của từng take.
- FFmpeg trên máy thiếu `libvorbis`; script ưu tiên nó khi có, còn lần chạy này dùng encoder `vorbis` sẵn có với `-strict experimental -q:a 5`. Không cài thêm gói.

**M** = đã gắn mới, 3 file; **C** = bỏ vì thư mục đã có, giữ nguyên; **T** = bỏ vì thiếu việc nguồn.

| Hệ | cast | release | release-dash | flyby | impact-flesh | impact-stone | impact-spirit | world-open | world-climax | world-close |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| metal | C | C | C | C | C | C | C | C | C | C |
| fire | T | M | M | C | C | C | C | C | C | C |
| water | M | M | M | M | M | M | M | M | M | M |
| thunder | M | M | M | M | M | M | M | M | M | M |
| wind | M | M | M | M | M | M | M | M | M | M |
| ice | M | M | M | M | M | M | M | M | M | M |
| dark | M | M | M | M | M | M | M | M | M | M |
| light | M | M | M | M | M | M | M | M | M | M |
| wood | M | M | M | M | M | M | M | M | M | M |
| earth | M | M | M | M | M | M | M | M | M | M |
| poison | M | M | M | M | M | M | M | M | M | M |
| blood | M | M | M | M | M | M | M | M | M | M |
| void | M | M | M | M | M | M | M | M | M | M |
| star | M | M | M | M | M | M | M | M | M | M |

Hậu tố lấy từ 14 kit đăng ký trong `src/view/skills/elements.ts` của worktree lab. **Kim có `sound: ""`** (`element-metal.ts:154`): đích thực tế là các thư mục chung đã có, nên giữ cả 10 ô; không tự tạo hậu tố `metal` mà mã lab không dùng. Các hệ khác dùng hậu tố đúng tên ở bảng. Hỏa thiếu việc `tt-sfx-fire-cast`, nên `cast-fire` tiếp tục quay về âm chung. Tổng: **122 M, 17 C, 1 T**.

Kiểm tra:

- `node --check games/.wt-ic-lab-panel/scripts/audio/lab-element-sounds.mjs`: PASS.
- `--dry-run`: 122 ADD, 17 EXISTS, 1 NO_JOB, 366 file; sau đó chạy thật hoàn tất.
- `JSON.parse` cả hai tệp JSON: PASS; manifest có **156 sự kiện, 455 file được liệt kê**, mọi file đều tồn tại.
- Đối chiếu nguồn/prompt của cả 366 biến thể: PASS. `ffprobe` xác nhận Vorbis, 48 kHz, 2 kênh; chênh độ dài so với WAV bằng **0**. Giải mã đầy đủ bằng FFmpeg: **366/366 PASS**.
- SHA-256 của toàn bộ 97 tệp cũ ngoài hai JSON không đổi; mọi mục manifest và dữ liệu SOURCES cũ giữ nguyên.
- Chạy thật lần nữa: 139 EXISTS, 1 NO_JOB, 0 file mới; hash của toàn bộ cây âm, kể cả hai JSON, không đổi.

**Chủ dự án cần nghe trong lab (NOT LISTENED)**, nhất là mức âm và cảm giác của các hệ mới. Nếu muốn Kim có bộ Firefly riêng, cần phiếu khác cho hậu tố/mã lab hoặc thay âm chung; phiếu này cấm cả hai. Không sửa mã lab hay nguồn Firefly, không chạy build/test suite của game, không mở cổng mạng hoặc dùng lệnh Git ghi.
