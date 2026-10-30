# Phiếu 218 · Ba game và Monkeytype · 80 bộ tiếng phím trở lên, mỗi bộ 70–100 biến thể

**Nguồn:** chủ dự án 30/10/2026, sáng. Bản 189 chỉ ra 7 bộ (mỗi thư mục một bộ, mỗi bộ 10 phím và 3 phím cách). Chủ dự án hỏi: "sao chỉ có 7, 8 âm typing, tôi tải hơn 400 file âm cơ mà". Sau đó chốt: "làm cả hai, nhưng tăng lên thành 70–100 biến thể, 80 bộ trở lên, tầm 6 điểm trở lên cũng được rồi".

**Báo cáo:** `docs/codex-queue/218-report.md` (tiếng Việt), thư mục `docs/codex-queue/218/`.

**Sau phiếu này:** phiếu 219 (kit: danh sách 80 bộ theo họ, nhiều biến thể), rồi Claude gắn vào ba game và Monkeytype.

## Đọc trước

- `docs/codex-queue/189-keys-firefly-sets.md` và `docs/codex-queue/189-report.md`: luật cắt, làm sạch, độ to, preview 1 giây, định dạng manifest.
- `tools/audio-lab/keys/firefly.py` (lệnh `survey`, kết quả ở `tmp/keys-firefly/survey/`) và `tools/audio-lab/keys/firefly_build.py` (lệnh `build` của 189), cùng test của chúng.
- `shared/game-kit/feedback/typing-fx/audio.ts`: `keyboardFiles()` nhận `key-<số>` và `space-<số>` với số bất kỳ.

## Nguồn âm

`~/Downloads/typing-mp3/`, 408 WAV trong 9 thư mục `Adobe_2026-10-29*`. Chỉ đọc: không sửa, đổi tên, chuyển hay xóa. Khảo sát cũ đếm được khoảng 23.900 cú gõ, trong đó khoảng 8.300 cú tách sạch.

## Việc

1. **Mức nhận hạ xuống khoảng 6/10**, theo ý chủ dự án.
   - Vẫn cấm: cú bị clip; cú bị cú sau đè lên tiếng chính; đuôi phòng dài; nhiễu nền trên −60 dBFS.
   - Được nhận: tick hay rattle nhỏ trước tiếng nhả; âm sắc chưa "sang".
   - Mỗi bộ có một điểm ước lượng 0–10 tính từ số đo: độ sạch, độ đều, độ lặp, nền, đuôi. Ghi công thức trong báo cáo. Chỉ giữ bộ từ 6 điểm.
2. **Ít nhất 80 bộ, mỗi bộ nghe như một bàn phím riêng.**
   - Gom các take theo âm sắc bằng số đo khảo sát (trọng tâm phổ, năng lượng từng dải, độ tắt, độ dài cú), ưu tiên trong cùng một thư mục.
   - Mỗi bộ lấy cú từ 1–8 take gần nhau về âm sắc.
   - Hai bộ không được gần trùng (đặt ngưỡng khoảng cách, ghi số).
   - Không đủ 80 bộ đạt 6 điểm thì dừng ở số đạt được và nói rõ vì sao. Không độn bộ kém.
3. **Mỗi bộ có 70–100 biến thể phím thường** (`key-001.ogg` …) và **6–10 biến thể phím cách** (`space-01.ogg` …).
   - Không hai file có tương quan dạng sóng trên 0,95.
   - Phím cách trầm và dài hơn phím thường của chính bộ đó; thiếu thì mượn cú trầm nhất của bộ, ghi rõ.
4. **Xử lý nhẹ như 189:** cắt, fade-in tối đa 1 ms, fade-out mềm, gập mono có kiểm, lặng hóa nền, đỉnh thật ≤ −1 dBTP.
   - Một mức độ to chung cho mọi bộ, lệch trong bộ ≤ 1,5 dB.
   - Phím ≤ 180 ms, phím cách ≤ 260 ms.
5. **Tên và họ** (tiếng Anh, chữ người chơi thấy):
   - Mỗi bộ thuộc một trong 7 họ của 189 theo âm sắc: Deep, Warm, Rounded, Solid, Crisp, Clear, Bright Clack.
   - Tên là "<họ> <từ mô tả>", ví dụ "Deep Velvet", "Crisp Pebble". Từ mô tả lấy từ một danh sách tiếng Anh ghi trong báo cáo; không dùng tên hãng.
   - Không trùng tên. id kebab, ví dụ `deep-velvet`.
   - **Giữ nguyên 7 id cũ** (`deep`, `warm`, `rounded`, `solid`, `crisp`, `clear`, `bright-clack`) cho bộ tốt nhất của mỗi họ, để save cũ và mặc định Bright Clack vẫn đúng.
   - Thứ tự danh sách: theo họ từ trầm đến sáng, trong họ theo điểm từ cao xuống.
6. **Nghe thử:** mỗi bộ một `preview.ogg` dài đúng 1,0 s, cách làm như 189.
7. **Manifest:**
   - Mỗi bộ có `keys-manifest.json` như 189, thêm `family`, `score` và nguồn từng file.
   - Danh mục gốc `keys-manifest.json` liệt kê mọi bộ: `id`, `name`, `family`, `score`, `manifest`, `preview`, `order`.
   - Đọc được bằng `keyboardFiles()`. Có test chứng minh, ví dụ đọc lại theo đúng luật của `audio.ts`.
8. **Đầu ra** (media, ngoài Git; sandbox không ghi được ra ngoài repo):
   - `tmp/keys-firefly/staging-v2/keys-firefly/` (OGG Vorbis chất lượng 0,6; không cần WAV trong bản giao);
   - file nghe `tmp/keys-firefly/listen-v2/so-sanh-<họ>.mp3`: mỗi họ một file, mỗi bộ 2 giây, nối theo thứ tự danh sách.
   - Ghi tổng dung lượng. Mục tiêu dưới khoảng 70 MB; vượt thì nói rõ cách giảm (chất lượng OGG, số biến thể).
9. **Lệnh chạy lại được:** `bash tools/audio-lab/run.sh keys firefly build-v2` (hoặc thêm tùy chọn vào `build`), có test. Bản 189 vẫn chạy được như cũ.

## Cấm

- Mọi lệnh git có ghi; tải gì từ mạng; tạo âm mới bằng model.
- Sửa, chuyển, xóa file nguồn.
- Ghi vào `games/**`, `shared/**`; đụng Tu Tiên.
- Đưa âm vào Git.

## Kiểm (ghi số)

1. Số bộ đạt 6 điểm; phân bố điểm; số bộ theo họ; số biến thể mỗi bộ (nhỏ nhất, trung vị, lớn nhất).
2. Mỗi file: dài, khoảng lặng trước tiếng, LUFS-M max, đỉnh thật, nền. Ghi số xấu nhất và bảng tóm tắt; bảng đủ để trong `218/`.
3. Khoảng cách âm sắc nhỏ nhất giữa hai bộ; tương quan cặp lớn nhất trong bộ.
4. Mọi `preview.ogg` dài 1,0 s ± 10 ms.
5. Tổng dung lượng MB.
6. Test keys xanh (số test).
7. `git status --short -uall`: chỉ mã, test, tài liệu.

**Xong khi:** có từ 80 bộ đạt 6 điểm (hoặc báo rõ vì sao ít hơn), mỗi bộ 70–100 biến thể, manifest và danh mục đúng định dạng, có preview, có file nghe, test xanh.
