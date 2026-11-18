# Phiếu 276 · Tu Tiên · Âm: lọc 424 take Firefly bằng số đo, mỗi việc chọn 2 take để anh nghe

**Loại việc:** âm và công cụ (`gpt-6.1-sol`, mức `xhigh`). Phiếu ngắn theo luật làm gọn 05/11. Không đụng sim, canon hay cân bằng, nên không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/276-report.md`.

## Bối cảnh
- Ngày 05/11, Firefly Generate Sound Effects (model Adobe Firefly Audio) tạo 424 take WAV (48 kHz stereo) cho 83 việc. Chưa ai nghe take nào.
- Anh nghe là cổng cuối, nhưng không thể nghe hết 424 take. Máy chỉ lọc và xếp hạng bằng số đo, rồi đưa anh nghe 2 take tốt nhất mỗi việc.
- Âm chiến đấu phải mạnh, nhiều lớp, có độ vang. Luật "nhỏ, mềm" chỉ dành cho tiếng phím (`.agents/skills/game-art-pipeline/references/audio.md` §5).

## Đầu vào (chỉ đọc)
- Take: `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/sound/<id>/take<N>.wav`, kèm `take<N>.prompt.txt`.
- Danh sách việc: `docs/work/tasks/firefly-sprint-sound.json`, mỗi việc có `id`, `group`, `priority`, `seconds`, `why`, `prompt`.
- Tiếng hô: `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/callouts/<id>/take<N>.wav` (4 câu × 3 take). Chỉ đo, không xếp hạng.
- Audio Lab: `tools/audio-lab/critic/README.md`.
  - Chỉ dùng các lớp không cần model học máy: L1 cổng vệ sinh, L1b dò lỗi do mô hình tạo, L2 đặc trưng.
  - **Không** chạy L3–L5 hay bất kỳ model AI local nào (luật của anh ngày 03/11: không chạy AI nặng trên máy).
  - Nếu CLI không tách riêng được các lớp này, viết một script nhỏ đo cùng các số.

## Việc
1. **Đo mỗi take:**
   - độ to tích hợp (LUFS), true peak, số mẫu bị cắt đỉnh, lệch DC;
   - khoảng lặng ở đầu (ms), thời gian tấn công (từ -40 lên -6 dB so với đỉnh), độ dài đuôi tới -60 dB;
   - crest factor, trọng tâm phổ, năng lượng dưới 120 Hz;
   - với việc có chữ `loop` trong `id`: chênh mức và chênh phổ giữa 100 ms đầu và 100 ms cuối;
   - cặp take gần trùng nhau trong cùng việc (tương quan cao), đánh dấu là trùng.
2. **Cổng loại:** cắt đỉnh, lặng đầu trên 60 ms (trừ việc loop hoặc drone), file gần như im lặng, take trùng. Take bị loại vẫn ghi rõ lý do.
3. **Xếp hạng trong từng việc** bằng luật đơn giản, ghi trong báo cáo:
   - **Tiếng trúng, nổ, chém** (`impact`, `hit`, `burst`, `slash`, `crack`, `boom`, `clash`, `ignite`, `release`): tấn công nhanh, crest cao, đủ năng lượng thấp.
   - **Đuôi, drone, vang** (`tail`, `drone`, `echo`, `swell`, `rumble`): đuôi dài, liền, không có đột biến.
   - **Loop:** mối nối liền.
   - **Lấp lánh, vút** (`sparkle`, `glint`, `shimmer`, `whoosh`, `flyby`): phổ sáng, tấn công gọn.
   - Còn lại: theo luật gần nhất, có ghi chú.
4. **Đầu ra cho anh nghe** (ghi trong repo; Claude chuyển sang thư mục review):
   - `.local/codex-runs/276-out/picks.json` và `picks.md`: mỗi việc có hạng, số đo và lý do loại của từng take; 2 take đứng đầu đánh dấu `listen`.
   - Mỗi `group` trong danh sách việc một file MP3: nối take hạng 1 của từng việc theo thứ tự `priority`, cách nhau 0,8 s lặng, 192 kbps. Thêm `ORDER-<group>.txt` ghi giây bắt đầu, `id` và số take.
   - Một file MP3 thứ hai cho mỗi group, nối take hạng 2.
   - Không chuẩn hóa, không EQ, không cắt vào bên trong take. Giữ nguyên âm như Firefly tạo ra; chỉ đổi định dạng khi nối.

### Được ghi
`.local/codex-runs/276-out/**`, script mới trong `.local/codex-runs/276-out/tools/`, và `docs/codex-queue/276-report.md`.

### Cấm
- Sửa hay ghi đè bất kỳ WAV nào trong `art-src`.
- Lệnh git ghi; sửa file ngoài danh sách được ghi.
- Mở cổng mạng; tải gói mới.
- Chạy model AI local.

## Kiểm bắt buộc
1. Đủ 424 take (cộng 12 tiếng hô) có số đo, hoặc có lý do vì sao thiếu.
2. Mỗi việc có ít nhất 1 take `listen`, hoặc ghi rõ "cả việc bị loại" kèm lý do.
3. Mỗi file MP3: `ffprobe` đọc được, độ dài khớp tổng trong file `ORDER` (sai lệch ≤ 0,1 s).
4. MD5 của mọi WAV trong `art-src/.../sound/` không đổi (so trước và sau).

## Claude làm sau
Chép MP3 và `ORDER` sang `typing-game-review/owner-review/2026-11-05/tu-tien/firefly-sound-picks/`, gửi anh nghe theo group, ghi các take anh chọn.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
