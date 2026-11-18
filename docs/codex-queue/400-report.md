# Phiếu 400 — Vòng đời chữ trên dải kỹ năng

Ngày: 16/11/2026. Phiếu đã có **PASS Sonnet**; làm một lane, giữ phần bố cục và thay đổi có sẵn từ 394. Kiểm tra quota trước khi làm: còn **63%** cửa sổ tuần.

**Đã triển khai mã và kiểm tra tự động. Chưa có clip hoặc nghiệm thu thị giác chuẩn 9:** Vite bị sandbox chặn cổng; thư mục review nằm ngoài writable roots. Không coi test DOM giả là bằng chứng hình ảnh, hiệu năng hay điểm mỹ thuật.

## Đã làm

- Chữ mới hiện trong **220 ms**, so le khoảng **16,7 ms/chữ** với các độ dài kỹ năng hiện hành; chữ đầu nhấn nhẹ. Nếu người chơi khóa từ ngay khi nó còn đang hiện, từ được đọc rõ ngay để không che phản hồi phím.
- Chỉ từ khóa nhận nảy chữ đúng: **80 ms**, đỉnh scale giới hạn **1,12**; chữ đúng vàng kim, chữ kế tiếp có gạch dưới. Lỗi lấy từ sự kiện `word-progress`, viền đỏ giảm trong **150 ms**, rung ngang tối đa **3 px**. Backspace và nhả khóa cập nhật lại màu/gạch dưới.
- Từ hồi chiêu giữ bản xem trước mờ, vòng đếm cũ và không gạch dưới. Từ đã hoàn tất nhưng đang giữ đích hoặc Ultimate đã sẵn sàng giữ nguyên cho tới sự kiện tung chiêu; **Ultimate vẫn phải Space**, không đổi bản chốt 394.
- Khi Cast được giải quyết: lóe **40 ms**, rồi từng chữ tách nhẹ, xoay và tan; tổng từ lúc lóe đến hết là **560 ms**. Strike/Pierce/Sword field/Ultimate/Seal hướng lên; Ward/Dash/Cleanse hướng xuống. Cast hết thời gian giữ đích cũng được dọn bằng vòng đời này. Từ kế tiếp chờ chữ cũ tan xong mới hiện.
- Toàn bộ chữ và hạt bị cắt trong ô/dải đáy, không bay ra chiến trường. Bốn hạt mỗi ô lấy từ **ảnh glint sẵn có của repo**, dùng alpha mask với màu `rgb(229, 211, 153)` (mọi kênh <0,9), opacity tối đa 0,7. Không sinh ảnh, âm hoặc media mới.
- Giảm chuyển động bật khi **game hoặc trình duyệt** yêu cầu; có hiệu lực cả khi đổi giữa hiệu ứng. Bỏ nảy, rung, xoay, bay/rơi và hạt; giữ mờ dần.
- Tái dùng phần tử chữ qua từng phím, tái dùng pool hạt. Chỉ animate `transform`/`opacity`; overlay viền/lóe có hình thức tĩnh và đổi opacity. Dự trữ độ rộng theo từ rộng nhất đủ điều kiện trong bộ từ của trận để đổi từ không kéo các ô bên cạnh. Canvas chỉ đo chữ, không vẽ hình.
- Hiệu ứng chỉ đọc mô phỏng và sự kiện. Không thêm timer, hàng chờ hoặc điều kiện vào đường phím → Cast; không đổi âm gõ hoặc âm chiêu. Trường hợp tự động gõ nhiều từ vào ô cooldown 0 trước khi chữ cũ tan: giữ một lượt tan đang chạy, không kéo dài lượt đó và không giữ Cast mới lại.

Nguồn hạt tái dùng, không sửa:
`games/immortality-cultivation/art-src/lab/vfx/ice-ult/glint.png`.
Đã xem ảnh và đọc nguồn/prompt đi kèm. CSS tham chiếu bằng `new URL` để Vite đóng gói asset, không cần chép media vào public hoặc Git. Đây là nguyên liệu đang có, chưa phải kết quả được chấm chuẩn 9 trong tổ hợp mới.

## File của phiếu

Trong `games/immortality-cultivation/`:

- Sửa `src/ui/ban-quyet.ts`: presenter, trạng thái chữ, giữ ô Seal đang tan, đo độ rộng ổn định.
- Thêm `src/ui/word-fx.ts`: đồng hồ và đường chuyển động thuần của lớp trình bày.
- Thêm `src/ui/word-fx-events.ts`: giữ định danh sự kiện trước khi word store tái sử dụng; chỉ bắt Cast của người chơi này.
- Thêm `src/ui/styles/word-fx-css.ts`: màu, underline, overlay viền/lóe và mask hạt.
- Thêm `tests/ui/word-fx.test.ts`, `word-fx-events.test.ts`, `word-fx-presenter.test.ts`, `word-fx-dom.ts`.
- Thêm `tests/ui/word-fx-capture.mjs`: lệnh quay CDP ngoài sandbox cho Claude, tự chạy hai kích thước và kiểm tra đã có hai Cast cùng một lỗi gõ.

Không sửa `src/lab/`, `src/view/ground.ts`, bản đồ, mô phỏng, âm thanh, kit hoặc docs Tu Tiên. Không đổi nhánh, commit, push, reset, clean hoặc stash. Những thay đổi có sẵn của worker khác được giữ nguyên.

## Kiểm chứng

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation
pnpm test --maxWorkers=2 tests/ui/word-fx.test.ts tests/ui/word-fx-events.test.ts tests/ui/word-fx-presenter.test.ts tests/ui/ban-quyet.test.ts tests/boundary.test.ts
pnpm exec tsc --noEmit
node --check tests/ui/word-fx-capture.mjs
git diff --check -- src/ui/ban-quyet.ts
```

- **5 file / 33 test PASS**, lượt cuối 1,85 s; trong đó 14 test mới cho mô hình/sự kiện/presenter, 6 test Bàn Quyết hiện có và 13 test boundary.
- Typecheck: **PASS**. Kiểm tra cú pháp scenario, diff và khoảng trắng các file mới: **PASS**.
- Có kiểm tra thứ tự hiện → ổn định → lóe → tan → từ mới; thời lượng và giới hạn scale/rung; giữ node và pool khi gõ/sai/Backspace; không underline khi cooldown; Seal biến mất và Seal còn lại; giảm chuyển động từ hai nguồn và khi đổi giữa lượt.
- Test mô phỏng chứng minh phím cuối đã tăng Cast ngay trong tick đó, trước mọi frame presenter; ô 1 vẫn có thể Cast lần tiếp theo mà không đợi 560 ms. Test riêng giữ đúng chờ đích và Ultimate → Space.
- **Không chạy toàn bộ `pnpm test` hoặc build game** theo house rules của lượt này. Lệnh test chỉ chọn các file liên quan ở trên; kết quả không thay thế lần kiểm tra toàn game của Claude.

## Clip còn thiếu và lệnh cho Claude

`pnpm dev` đã dừng, không để lại server:

```text
Error: listen EPERM: operation not permitted 127.0.0.1:3008
```

Chưa tạo thư mục `owner-review/.../word-fx/`, `ABOUT.md` hoặc bất kỳ khung/clip nào ở ngoài sandbox. Script quay mới chỉ qua kiểm tra cú pháp, **chưa chạy end-to-end**.

Chạy ngoài sandbox ở hai terminal:

```sh
# Terminal 1
cd /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation
pnpm dev
```

```sh
# Terminal 2; Chrome và ffmpeg trên Mac, không dùng URL flag chất lượng
cd /Volumes/SS990TPRO/htdocs/typing-game
.local/bin/heavy.sh --gpu node games/immortality-cultivation/tests/ui/word-fx-capture.mjs
```

Script dùng input CDP trên trang chơi, thêm quái sống đủ lâu gần người chơi làm fixture; quay từ tấn công có một lỗi được sửa bằng Backspace rồi từ phòng thủ. Đầu ra:

`/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-16/tu-tien/word-fx/`

- `ABOUT.md`, `word-fx-1280x720.mp4`, `word-fx-1920x1080.mp4` và JSON ghi từ, số Cast/lỗi, số khung, FPS ghi thật.
- Giữ timestamp CDP để video chạy đúng tốc độ; encode 60 FPS có thể lặp khung khi Chrome ghi chậm. Không dùng nhãn 60 FPS để khẳng định hiệu năng render.
- Khung làm việc nằm trong topic riêng ở `captures/tu-tien/word-fx/`; sau khi encode thành công, script chạy prune thử rồi `--apply` đúng thư mục riêng vừa tạo. Nếu encode lỗi, giữ khung. Script xây lại review index khi kết thúc.

Claude cần xem trực tiếp cả hai clip: chữ/hint/cooldown đọc được, hướng bay/rơi và lóe hợp nhịp chiêu; kiểm tra text scale 100/125/150%, giảm chuyển động, giao với lõi/cổng/trụ/cảnh báo và frame time ở 15 phím/giây. Sau preflight còn cần **hai giám khảo độc lập ≥9**, không hạng mục con dưới 8,5, trong built play host ở thiết lập người chơi; owner chốt cuối. Chưa có điểm hoặc nghiệm thu thị giác cho phiếu này.
