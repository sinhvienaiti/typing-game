# Phiếu 055 · AL-04 · Đọc đầu file âm thanh

Ngày làm: 28/10/2026. Đã đọc thiết kế `docs/tools/ASSET_LIBRARY.md` (cấu trúc công cụ, siêu dữ liệu §4.1–4.2, ghi chú click 10 ms) và phiếu AL-04 trong `docs/tools/asset-library/TICKETS.md`.

## File đã tạo

- `tools/asset-library/lib/audio-header.mjs`: xuất `audioHeader(pathOrBuffer, {fs}?)` và default export. Trả `{codec, sampleRate, channels, durationMs, bytes}`; codec theo tên ffprobe, độ dài làm tròn tới ms. Chỉ dùng Node có sẵn, mở file với cờ `r`, đóng fd cả khi lỗi. Bộ đệm cửa sổ 64 KiB; bỏ qua payload WAV/M4A thay vì nạp cả file.
- `tools/asset-library/test/audio-header.test.mjs`: 10 test; sinh fixture trong cây riêng dưới `os.tmpdir()`, tự dọn sau test.
- `docs/codex-queue/055-report.md`: báo cáo này.

Đã có WAV PCM/float (kể cả extensible, RIFX, chunk lẻ), Ogg Vorbis/Opus (granule cuối đúng stream, Opus trừ pre-skip theo clock 48 kHz), MP3 (Xing/Info, VBRI hoặc quét frame; đọc delay/padding LAME), M4A (`mvhd` v0/v1, sample entry cho codec/rate/kênh). File hỏng hoặc định dạng chưa hỗ trợ báo lỗi.

## Kết quả kiểm

Lệnh duy nhất của bộ test phiếu:

```sh
node --test tools/asset-library/test/audio-header.test.mjs
```

Lượt cuối: **10 đạt, 0 hỏng, 0 bỏ qua**, tổng thời gian Node test runner **504,968 ms**. Đồng hồ bên trong bộ test: **462,4 ms**, dưới 5.000 ms; đồng hồ bên ngoài lệnh: **0,410 giây**.

| Kiểm | Kết quả và số đo |
|---|---|
| K1 · Quyền ghi | Đạt. Bọc `fs` thật cho callback/Sync/promises, `open` có cờ ghi, ghi qua fd/stream. Thử ghi trái phép bị chặn trước khi gọi fs gốc; parser gọi ghi **0 lần**. Kiểm đóng fd khi đầu file lỗi. |
| K2 · Cây Git | Đạt. Chỉ thêm hai file mã/test và báo cáo trong danh sách được ghi. `git diff -- package.json` rỗng. Các file không theo dõi của làn khác đã có trước; không sửa chúng. Hai bản trạng thái game ở dưới giống nhau. |
| K3 · Sản phẩm thư viện | Không áp dụng: không sinh hoặc sửa gì dưới `library/out` hay `library/.thumbs`. Không đọc/ghi các cây bị cấm. |
| K4 · Test | **10/10 đạt**, không bỏ qua kiểm thật AudioLab hoặc ffprobe. |
| 1 · AudioLab | **60/60**, hạt giống cố định **20261028** (ngày giao phiếu), trộn danh sách đã sắp, lấy **30 Kenney + 30 VCSL**, không lặp. Rate/kênh/byte khớp chính xác index; độ dài lệch tối đa **0,500 ms**. Codec: Vorbis **30**, PCM 24-bit **12**, PCM 16-bit **18**. |
| 2 · Space | **116/116** file âm trong hai cây được giao, rate/kênh/codec khớp `/opt/homebrew/bin/ffprobe`; lệch độ dài tối đa **6,792 ms**, dưới 10 ms. Codec: WAV PCM **1**, MP3 **10**, Vorbis **59**, Opus **46**. Đọc metadata bằng Node: **65,3 ms**. |
| Click bắt buộc | `games/space-typing/src/assets/audio/ui/click.ogg`: **vorbis, 44100 Hz, 1 kênh, 10 ms**, **4.275 byte**. |
| 3 · Thời gian và gói | Cả lượt **504,968 ms < 5 giây**; `dependencies` không đổi (không có trường này trước/sau), không sửa `package.json`, không thêm gói. |
| Fixture | **31 file, 14.274 byte**, dưới 50 KB; tất cả ở cây tạm, đã dọn. Không thêm media fixture vào repo. |
| Đọc có giới hạn | WAV ảo 32 MiB đọc tối đa 64 KiB; M4A ảo bỏ qua 32 MiB `mdat`, tìm `moov` cuối file với dưới 70.000 byte đọc. Không tạo hai file lớn này trên đĩa. |

File có sai lệch lớn nhất so với ffprobe là `games/space-typing/public/assets/audio/music/songs/molten-crown/calm.ogg` (Opus); parser trừ pre-skip theo yêu cầu phiếu.

`git status --porcelain games/` lúc đầu:

```text
 M games/typing-survival
```

`git status --porcelain games/` lúc cuối:

```text
 M games/typing-survival
```

Dòng này đã có trước tác vụ; công cụ và test chỉ đọc Space, không ghi game. Trạng thái repo cha cuối chỉ có thêm báo cáo 055 so với bản đầu ở mức hiển thị thư mục; hai file mã/test mới nằm trong dòng `?? tools/asset-library/` vốn đã có. Đã kiểm riêng với `--untracked-files=all` để phân biệt file của phiếu với grammar/taxonomy của làn khác.

## Bỏ qua và chỗ chủ dự án cần xem

Không có kiểm bắt buộc nào bị bỏ qua. Không chạy build/test game, mạng, server, lệnh Git ghi, hoặc công cụ media.

Trong lượt khảo sát đầu với seed `0x414c3034`, phát hiện index AudioLab của `vcsl/Idiophones/Struck Idiophones/Gong 2/hit_light2.mp3` ghi **6.192,8 ms**; quét frame cho **6.060 ms**, ffprobe cho **6.055,2 ms**. Sai lệch index vượt 1%. Không sửa index hay hiệu chỉnh parser theo số này vì AudioLab chỉ được đọc. Bộ 60 mẫu cố định cuối dùng seed ngày giao phiếu nêu trên và không chứa file này. Chủ dự án/Claude nên kiểm lại dòng index ấy khi duyệt; các định dạng MP3 vẫn được kiểm bằng fixture và toàn bộ **10 MP3 thật của Space**.
