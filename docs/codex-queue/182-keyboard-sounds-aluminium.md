# Phiếu 182 · Ba game · Tiếng phím của bàn phím nhôm cao cấp (5 hồ sơ, mức 9)

**Nguồn:** chủ dự án 29/10/2026, sau khi nghe năm hồ sơ Claude làm bằng Stable Audio 3: "âm nghe chán thật, xạn, nghe rất nhựa, cái clack nghe đúng kiểu nhựa lởm, bàn phím gõ âm hay phải theo phím nhôm chất lượng cao… xào xạc quá lởm". Chủ dự án tin Codex sẽ làm hay hơn và giao phiếu này cho Codex.

**Báo cáo:** `docs/codex-queue/182-report.md` (tiếng Việt), thư mục `docs/codex-queue/182/`.

## Mục tiêu

Năm hồ sơ tiếng phím cho mục "Keyboard sound" trong cài đặt của cả ba game. Mỗi hồ sơ nghe như **bàn phím vỏ nhôm cao cấp thật**: chắc, trầm, sạch, đắt tiền; không nhựa, không rẻ, không xì, không xào xạc.

| id | Tên người chơi thấy | Hướng âm |
|---|---|---|
| `creamy` | Creamy Linear | switch tuyến tính lube, keycap PBT dày, tiếng đáy êm, tròn, trầm |
| `thock` | Deep Thock | switch tactile, plate đồng thau hoặc PC, vỏ nhôm nặng; tiếng "thock" trầm vang ngắn |
| `marbly` | Marbly | plate POM, switch tuyến tính; tiếng "lăn bi" mượt, mịn |
| `clack` | Clean Clack | keycap ABS dày trên vỏ nhôm; sáng, giòn nhưng chắc, không nhựa |
| `dome` | Soft Dome | phím điện dung kiểu Topre trên vỏ nhôm; tiếng tròn, êm, tắt nhanh |

Mức nhận: **từ 9** (`docs/games/SHARED_SYSTEMS_BAR.md`); chủ dự án nghe là cổng cuối.

## Đọc trước

- `tools/audio-lab/SESSION_KEYS.md`: lượt trước của Claude, kết quả chủ dự án trả cả năm, ghi chú bàn giao (đường ống, ứng viên, nghiên cứu bản thu nhôm).
- `tools/audio-lab/KEYS_SOURCES.md`: bản thu CC0 đã kiểm giấy phép (chưa tải).
- `tools/audio-lab/keys/` (mã đường ống: cắt cú gõ, số đo, chọn, câu gõ thử) và `tools/audio-lab/README.md`.
- `docs/games/SHARED_SYSTEMS_BAR.md` §5 (giấy phép: chỉ CC0, hoặc CC-BY có ghi công; không GPL, không NC, không tài sản của game khác).

## Việc

1. **Báo trước tiên, trong báo cáo:** công cụ âm thanh nào Codex có trong phiên này (tạo âm, sửa âm, chạy Python, ffmpeg, mạng). Nếu Codex có công cụ tạo âm riêng, dùng nó; nếu không, nói thẳng và làm các mục còn lại.
2. **Tạo hoặc dựng ứng viên** cho năm hồ sơ, bằng công cụ tốt nhất Codex có. Mỗi hồ sơ cần `key-01` … `key-10` và `space-01` … `space-03`:
   - mỗi file là một cú gõ (nhấn và nhả của cùng một phím), mono, 48 kHz; phím ≤ 180 ms, phím cách ≤ 260 ms; đầu tiếng ≤ 2 ms, tiếng chính tới trong 15 ms;
   - các biến thể nghe như cùng một bàn phím, khác phím: lệch nhỏ cao độ, âm sắc, nhịp; không hai file giống hệt, không file lạc;
   - cân độ to giữa các hồ sơ (mục tiêu như lượt trước: −27 LUFS-M max cho mỗi file, câu gõ 60 WPM khoảng −25 LUFS-I).
3. **Làm sạch** (bắt buộc, chỗ lượt trước hỏng): không còn nhiễu nền giữa các cú gõ, không tiếng xì 4–8 kHz, không xoáy pha, không tiếng sột soạt; giữ phần trầm 150–400 Hz chắc và phần trên sạch. Viết chuỗi làm sạch thành script chạy lại được trong `tools/audio-lab/keys/` (có test).
4. **Bản thu thật:** không tải gì về. Nếu tìm được bản thu CC0 hay CC-BY của bàn phím nhôm cao cấp tốt hơn danh sách `KEYS_SOURCES.md`, ghi tên, URL, giấy phép (kiểm tại trang nguồn), định dạng, cỡ, bàn phím, switch, plate, keycap vào báo cáo để Claude xin chủ dự án duyệt.
5. **File nghe cho chủ dự án** (chủ dự án đang ở máy khác, nghe qua file): mỗi hồ sơ một file `<id>-20s.mp3` dài 20 giây, gõ xen 60 và 100 từ/phút như trong game (biến thể xoay vòng, lệch tốc độ ±3 %, mức ±8 %), MP3 192 kbps stereo. Thêm `so-sanh-5-ban-phim.mp3`: năm hồ sơ nối nhau, mỗi hồ sơ 6 giây.

## Nơi ghi

- Âm thanh là media, không vào Git: ghi vào `tmp/keys-codex/<id>/` trong repo cha (thư mục đã bị Git bỏ qua): `key-01.wav` … `space-03.wav` (48 kHz 24-bit mono), bản chạy `.ogg` (Vorbis, chất lượng 0,6), `keys-manifest.json` (id, tên người chơi thấy, file, độ to, độ dài, nguồn từng file, giấy phép), và file nghe 20 giây ở `tmp/keys-codex/listen/`.
- Mã và test: `tools/audio-lab/keys/` (chỉ thêm, không xóa mã của Claude).
- Báo cáo và số đo: `docs/codex-queue/182-report.md`, `docs/codex-queue/182/`.

## Cấm

- Mọi lệnh git có ghi; tải file âm thanh từ mạng; dùng âm của Monkeytype, Mechvibes hay gói không rõ giấy phép; ghi vào `games/**`, `shared/game-kit/**`; đụng Tu Tiên.

## Kiểm (bắt buộc, ghi số)

1. Mỗi file: dài, đầu tiếng, LUFS-M max, đỉnh thật (≤ −1 dBTP), nhiễu nền giữa các cú gõ (≤ −70 dBFS), năng lượng 4–8 kHz so với 150–400 Hz.
2. Độ đều trong hồ sơ: lệch LUFS ≤ 1 dB; không hai file có tương quan dạng sóng > 0,95.
3. Phổ trung bình mỗi hồ sơ, vẽ thành ảnh `182/spectra.png`, cạnh phổ của lượt Claude bị trả, để thấy đã bớt xì và bớt nhựa.
4. Tự nghe bằng số đo không đủ: ghi rõ chỗ nào Codex không chắc, để chủ dự án nghe.

**Xong khi:** năm hồ sơ đủ file và manifest, qua mục kiểm 1–3, có file nghe 20 giây. **Nhận** khi chủ dự án nghe và chấm từ 9.
