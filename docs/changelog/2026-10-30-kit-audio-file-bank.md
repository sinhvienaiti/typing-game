# 30/10/2026 · Kit âm thanh từ file theo manifest (phiếu 198)

## Yêu cầu

Đưa khả năng đọc manifest v1/v2, chọn biến thể, giải mã lười và nhạc qua bus
vào `shared/game-kit/audio/`, theo `AUDIO_PIPELINE.md` §5.3, §6.1 E/G,
§6.3 mục 1 và §11. Last Line và Wordwoven cần đường nhận file Firefly;
phiếu này chỉ sửa nguồn kit, chưa ghép vào game.

## Quyết định và cách thực hiện

- `manifest.ts` chuẩn hóa từng mục, bỏ riêng mục hỏng; phiên bản chưa hỗ trợ
  làm rỗng manifest. Bộ tải không ném khi HTTP/mạng/JSON lỗi. Metadata không
  mang chính sách mix.
- `variants.ts` chọn ngẫu nhiên tránh bản vừa phát, tiêm RNG được; cửa sổ
  tránh mặc định 1, đặt 2 theo id cho phím đúng. `variant` là chỉ số từ 0
  trong manifest; không đổi chỉ số khi một biến thể tải lỗi.
- `file-bank.ts` có `FileBank` và `LayeredBank`: metadata → lần lượt các id
  ưu tiên → bảng URL cũ và bản ghi rồng. Các id khác và nhạc tải khi được gọi.
  Cache URL và hàng đợi chung giới hạn mặc định 4 việc fetch/giải mã. Độ dài
  buffer thắng metadata; chênh hơn 20 ms được ghi thống kê.
- `SceneAudio`: file manifest thắng URL bảng, bảng giữ bus/gain/gap. `play`
  trả độ dài theo tốc độ thực (giữ dao động ±5 % cũ). Khi file chưa sẵn,
  gọi móc hiện có của game hoặc im; không phát bù. Loop chỉ lấy buffer.
- Móc `missing` là đường chuyển tiếp có gắn cờ theo luật chủ dự án 28/10,
  không thêm công thức tổng hợp. Thống kê đếm file/móc/im theo id, xóa móc
  từng id sau khi file được duyệt và qua kiểm trong bản trộn.
- `musicBus` nối riêng thẳng ra loa; nhạc chịu `musicVolume` và gain/duck
  bus, không chịu master SFX. Không khai thì đường nhạc cũ giữ nguyên.
  Crossfade giữ các hằng số 0,4/0,6 giây và dừng nhạc cũ sau 2 giây;
  lượt nhạc đang tải bị hủy đúng khi dừng hoặc chọn lượt mới.

## File thay đổi

- Thêm `audio/manifest.ts`, `variants.ts`, `file-bank.ts` và bốn file test
  tương ứng theo phiếu; dùng `fake-audio.test-helper.ts` cho fetch/context giả.
- Sửa `audio/scene-audio.ts`, `audio/index.ts`.
- Một mục README và một dòng DRIFT; không sửa test `scene-audio.test.ts` cũ.
- Báo cáo: `docs/codex-queue/198-report.md`; log và kiểm phạm vi trong `198/`.

## Lệnh kiểm và kết quả

| Lệnh | Kết quả |
|---|---|
| `pnpm kit:test` trước | 56 file, 867 test qua |
| `pnpm kit:test` sau | 60 file, 898 test qua |
| `pnpm --dir shared/game-kit exec vitest run audio/` | 6 file, 41 test qua; 31 test mới |
| `pnpm --dir shared/game-kit typecheck` | 0 lỗi |
| `git diff --quiet shared/game-kit/audio/scene-audio.test.ts` | Mã thoát 0; bốn test cũ qua |
| Import `../` trong `audio/*.ts` | 0 dòng |
| Công thức tổng hợp mới | 0; chỉ thêm dòng cấp noise cho móc bằng mẫu cũ, `scene-audio.ts:201` |

Test viết trước mã; log đỏ đầu tiên và các ca cạnh bổ sung được giữ trong
thư mục phiếu. Tất cả fetch/context đều giả, không dùng mạng, dev server,
trình duyệt, build hay bộ test của game. Không chạy `kit:sync`, `kit:check`
hoặc lệnh Git ghi.

## Việc còn lại

Claude duyệt, commit, đồng bộ kit vào Last Line (`main`) và Dragonhold.
Dragonhold vẫn dùng bank riêng cho tới phiếu chuyển. Wordwoven đợi gộp
`td-keys` (`81baf46`, đã khai module audio) vào `a2-days` rồi đồng bộ.
Khi có file Firefly, mở phiếu gắn Last Line `hit.sub`/`hit.tail` và kiểm
mức trong bản trộn, thời điểm, chất lượng nghe. Xem báo cáo để biết API,
luật xóa móc và đối chiếu các làn đang bẩn.
