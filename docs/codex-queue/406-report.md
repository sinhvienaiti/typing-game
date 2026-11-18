# Phiếu 406 — Icon quái, thẻ dự báo và hiệu ứng chữ

Ngày: 16/11/2026. Phiếu có **PASS Sonnet**. Đã triển khai mã, bổ sung test và kịch bản chụp; **chưa hoàn tất nghiệm thu trình duyệt/thị giác**. Quota lúc bắt đầu còn 47%; làm một làn.

## Đã làm

- Nối **E1 Khiên ngọc** cho elite/general, **B1 Vương miện** cho boss. Thay socket DOM 394b bằng **một InstancedMesh, một material, hai texture**, không nhóm geometry và không tạo DOM theo quái. Quad luôn hướng camera; kích thước cố định theo CSS pixel, elite **30 px**, boss **32 px**, cách anchor đầu 8 px. Boss được xét trước; marker đụng marker khác bị ẩn để giảm chồng lấp. Quái thường/chết/freed/ngoài màn, anchor không còn hợp lệ và ảnh chưa tải/lỗi không tạo instance hiển thị.
- Chép nguyên bản hai PNG 48 px đã chọn cùng prompt sang `public/assets/immortality-cultivation/ui/icons/`. Đã đối chiếu byte với nguồn; Git bỏ qua các tệp này. Không sinh hoặc sửa art.
- Thẻ dự báo loại bỏ hoàn toàn ứng viên giao Shop **trước** khi tính chi phí tránh chiến trường. Dự trữ vùng drawer ngay khung đầu, đồng thời đọc DOM rect thật của Shop chuột/bàn phím. Giữ khoảng cách 8 px với drawer và đọc cỡ chữ khi tính dải đáy. Không còn chọn vị trí giao Shop chỉ vì nó có chi phí thấp hơn các vị trí khác.
- Chữ đúng nảy tới **1,22** ở giữa nhịp **80 ms**, trần 1,25; lớp chữ vàng sáng chỉ thay opacity. Vẫn chỉ nảy chữ đúng trong từ đang khóa.
- Tổng lượt lóe/tan **640 ms**, gồm lóe 40 ms. Chữ tấn công tách ra theo đường cong, đi lên **70–110 px**, xoay tối đa 10°. Chữ phòng thủ rơi **50–80 px**, nảy lại **12 px một lần** rồi tan. Tám hạt sáng theo đuôi dùng lại glint của phiếu 400; màu RGB(229,211,153), opacity tối đa 0,7.
- Một canvas overlay riêng vẽ chữ đang bay và hạt; tái dùng bản ghi lượt bay và glyph qua các Cast. Chữ gốc tiếp tục giữ chỗ trong ô. Overlay trừ vùng lõi/cổng/ô trụ/cảnh báo đang hoạt động với lề 4 px, cập nhật theo camera; các vùng bảo vệ chồng nhau không mở lại lỗ clip. Giảm chuyển động từ game hoặc hệ điều hành chỉ giữ mờ dần tại chỗ, bỏ bay/rơi/xoay/nảy/hạt/lóe vàng. Overlay cũng ẩn theo trạng thái `is-hushed`.
- Giữ thứ tự hiện → ổn định/đang gõ → giữ đích hoặc Ultimate ready → lóe → tan → từ mới. Không thêm chờ/timer vào đường phím → Cast; không sửa bộ cấp từ, Space hay mô phỏng. Cast nhanh không kéo dài lượt tan đang chạy.

## Các tệp

Trong `games/immortality-cultivation/`:

| Phần | Tệp |
| --- | --- |
| Batch icon mới | `src/view/foe-badges.ts` |
| Socket tương thích | `src/ui/foe-badges.ts` |
| Tích hợp, vùng bảo vệ và debug `foeBadges()` | `src/app/app.ts`, `src/ui/coverage.ts` |
| Vị trí thẻ dự báo | `src/ui/wave-card.ts` |
| Chuyển động và canvas mới | `src/ui/word-fx.ts`, `src/ui/word-flight.ts`, `src/ui/ban-quyet.ts` |
| CSS chữ, bỏ CSS marker DOM cũ | `src/ui/styles/word-fx-css.ts`, `src/ui/styles/game-css.ts` |
| Test icon/thẻ/chữ/canvas | `tests/ui/foe-badges.test.ts`, `wave-card.test.ts`, `word-fx.test.ts`, `word-fx-events.test.ts`, `word-fx-presenter.test.ts`, `word-flight.test.ts` |
| Chụp DOM/icon mới | `tests/ui/ui406-capture.mjs` |
| Clip, dải khung và số độ trễ | `tests/ui/word-fx-capture.mjs` |

Tài sản runtime trong `public/assets/immortality-cultivation/ui/icons/`:

- `foe-elite-jade-shield.v1-try1-48.png`, `.prompt.txt`;
- `foe-boss-imperial-crown.v1-try1-48.png`, `.prompt.txt`.

Nguồn hạt giữ nguyên: `art-src/lab/vfx/ice-ult/glint.png`.

## Kiểm chứng đã chạy

- `pnpm exec tsc --noEmit`: **PASS**, lượt cuối sau mọi sửa mã/test.
- `node --check` cho hai kịch bản chụp: **PASS**.
- `git diff --check` trong phạm vi sửa và kiểm khoảng trắng các tệp mới: **PASS**.
- Đo trực tiếp hàm trình bày bằng Node/tsx, không chạy suite: scale **1,22**; đích tấn công **−70/−80/−90/−100/−110 px**, opacity 0 ở 640 ms; phòng thủ chữ đầu **50 → 38 → 50 px** ở các mốc rơi/chóp nảy/kết thúc. Đã kiểm danh sách vùng clip của hai keepout chồng nhau.
- Đo CPU batch Three.js với loader thay thế: **1 mesh, 1 material, 0 geometry group, 2 instance**, role **[boss, elite]**. Đây chưa phải kiểm shader/GPU hay ảnh thật.
- Hai PNG runtime và hai prompt giống nguồn từng byte; `git check-ignore` xác nhận PNG nằm ngoài Git.

**Không chạy `pnpm test`, test suite riêng hoặc build game**, theo house rule của lượt này. Các test mới/đã cập nhật đã qua typecheck, **chưa có kết quả thực thi**. Test bao phủ phân loại/ưu tiên icon, tải lỗi, tái sử dụng slot, ngoài màn/chồng marker; mọi ứng viên thẻ giao Shop bằng 0 ở hai khung và ba cỡ chữ kể cả khi chiến trường đều bị chặn; thứ tự/thời lượng/biên độ chữ; pool và clip canvas; Cast vẫn cùng tick với phím cuối. Cần Claude chạy suite trước khi nhận.

## Lệnh cho Claude ngoài sandbox

Terminal 1:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation
pnpm dev
```

Terminal 2, nghiệm thu tự động:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation
pnpm test --maxWorkers=2
pnpm exec tsc --noEmit
```

Chụp prep 1280/1920, Shop chuột và bàn phím; đo **15 DOM rect liên tiếp mỗi trạng thái**, yêu cầu mọi diện tích giao bằng 0; chụp quái elite và boss với cả hai icon đã tải:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game
.local/bin/heavy.sh --gpu node games/immortality-cultivation/src/kit/tools/cdp-run.mjs games/immortality-cultivation/tests/ui/ui406-capture.mjs --width=1920 --height=1080 --dpr=1
node scripts/review-index.mjs
```

Đầu ra: `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-16/tu-tien/406-layout-icons/`, gồm `ABOUT.md`, `measurements.json`, bốn ảnh prep và hai ảnh elite/boss. Kịch bản báo lỗi khi có giao Shop, thiếu trạng thái cần đo, marker DOM, lỗi trang/shader hoặc GPU phần mềm.

Quay tấn công/phòng thủ ở hai kích thước, có lỗi gõ và sửa bằng Backspace, xuất dải tám khung quanh mỗi lần hoàn tất; nhãn ghi thời gian thực gần nhất với mốc yêu cầu:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game
WORD_FX_TOPIC=406-word-fx WORD_FX_TICKET=406 KEY_INTERVAL_MS=67 .local/bin/heavy.sh --gpu node games/immortality-cultivation/tests/ui/word-fx-capture.mjs
```

Đầu ra: `.../owner-review/2026-11-16/tu-tien/406-word-fx/`, gồm `ABOUT.md`, hai MP4, hai JSON có số độ trễ/FPS ghi thật và bốn sheet `attack|defence-<khung>-strip.jpg`. Báo lỗi nếu độ trễ phím/Cast tối đa vượt **50 ms**, thiếu mẫu hoặc GPU phần mềm. 67 ms/phím xấp xỉ 15 phím/giây trong đoạn gõ; đây chưa thay phép đo tải dài. Video giữ timestamp CDP; encode 60 FPS có thể lặp khung, không chứng minh renderer đạt 60 FPS.

Khung làm việc nằm trong `captures/tu-tien/406-word-fx/`, từng lượt có thư mục riêng và `ABOUT.md`. Sau khi encode/sheet thành công, kịch bản chạy prune thử rồi `--apply` đúng thư mục lượt đó, giữ khung nếu xuất lỗi; xây lại review index khi kết thúc. Các lệnh trên chưa chạy end-to-end trong lượt này.

## Còn phải xem

- Chưa đo DOM thật hoặc biên độ hiển thị trên trình duyệt; chưa có ảnh, clip hay kết quả ≤50 ms. Không tạo capture ngoài writable roots và không khởi động trình duyệt theo phân công phiếu.
- Claude kiểm shader, hướng/cỡ icon ở góc máy thật và khi zoom/đông quái; kiểm chữ không che vùng bảo vệ ở camera hiện hành và khi có cảnh báo. Xem rõ phần rơi/nảy gần mép dưới viewport, độ khớp chữ DOM → canvas, hạt, cỡ chữ 100/125/150% và giảm chuyển động.
- Còn nghiệm thu trong built play host, thiết lập thật: icon đạt chuẩn art; hiệu ứng chữ cần hai giám khảo độc lập **≥9**, không mục con dưới 8,5, owner chốt cuối. Không tự nhận đạt điểm bằng số đo nguồn.
- Không bỏ hạng mục triển khai nào. Bỏ qua sinh ảnh/âm vì phiếu dùng art đã chọn và không yêu cầu âm mới. Không sửa `src/sim/`, `src/lab/`, bản đồ, scripts/docs Tu Tiên, game khác hay công cụ Audio Lab. Giữ thay đổi có sẵn của các worker; không đổi nhánh, add media, commit, push, reset, clean hoặc stash.
