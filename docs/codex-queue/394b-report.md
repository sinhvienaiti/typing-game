# Phiếu 394b — Sửa lỗi UI sau kiểm phiếu 394

Ngày: 16/11/2026. Phiếu có PASS Sonnet; làm một làn sau 400. Quota lúc bắt đầu còn 57%. Giữ nguyên `ban-quyet.ts` và toàn bộ vòng đời chữ của 400.

**Chưa hoàn tất nghiệm thu:** đã sửa bố cục, thông báo Wave trùng, thêm test và chỗ cắm icon; còn lỗi cấp từ Ultimate ngoài phạm vi được ghi và phép đo DOM/ảnh thật bị sandbox chặn. Không coi test hình học là nghiệm thu hình ảnh.

## Đã sửa

- `games/immortality-cultivation/src/ui/styles/game-css.ts`, `src/ui/screen-zones.ts`: dời Core về `(8, 34)`, rộng 240 px; Posture sang `(256, 34)`, rộng 220 px. Health/Energy và Gold giữ hàng đầu bên trái. Dòng hồi sinh nằm trong khung trạng thái, tránh tràn xuống Core. Theo `after-coverage.json` cũ, khung thực sự giao ô trụ 0 là **Core** ở giữa mép trên, không phải Health/Energy.
- Shop dùng `21vw`, giới hạn 260–400 px; ở 1280×720 rộng 268,8 px, bắt đầu tại x = 1003,2, cách biên bảo vệ ô trụ 5 cũ khoảng 11,64 px. Ở 1920×1080 rộng 400 px, bắt đầu tại x = 1512. Cả shop chuột và shop bàn phím dùng chung CSS; chế độ đặt trụ vẫn rộng 190 px. Nội dung dài cuộn trong ngăn.
- `src/ui/hud.ts`: sự kiện `wave-start` không tạo notice nữa; giữ chip Wave thường trực. Thẻ dự báo đợt ở prep/break vẫn có tiêu đề riêng như 394.
- `src/ui/coverage.ts`: tách `fieldLandmarks()` để phép đo DOM và test dùng cùng vùng bảo vệ ô trụ/lõi/cổng; giữ nguyên thuật toán đo hợp diện tích.
- `src/ui/foe-badges.ts` mới, nối trong `src/app/app.ts`: chỗ cắm hai URL ảnh đã duyệt, đi theo anchor đầu quái từ ActorsView. Boss ưu tiên hơn elite; general dùng chung huy hiệu elite. Ẩn quái thường/chết/freed/ngoài màn, bỏ node theo serial khi slot được tái sử dụng; ảnh chưa tải hoặc lỗi luôn ẩn. `FOE_BADGE_ART = {}` nên bản hiện tại không tạo marker giả, không CSS/emoji/SVG thay art.
- `src/app/app.ts`: thêm debug reader `window.__ic.healthBars()` trả số instance, trạng thái hiển thị và lượng máu thực trong mesh, phục vụ đối chiếu ảnh. Không sửa `src/view/health-bars.ts`: điều kiện ẩn khi đầy đang đúng.

## Test và kiểm chứng

- `pnpm test --maxWorkers=2`: **100 file, 1028 test PASS**, 18,36 s. Chạy toàn bộ test theo yêu cầu nghiệm thu cụ thể của phiếu; không chạy build.
- `pnpm exec tsc --noEmit`: **PASS**. Một lỗi ép kiểu ở fixture test mới đã sửa trước lượt typecheck cuối.
- `node --check tests/ui/ui-layout394b-capture.mjs` và `git diff --check`: PASS.
- `tests/ui/screen-zones.test.ts`: thêm kiểm tra prep/combat trên Camera B thật của renderer, ở 1280×720 và 1920×1080, mỗi cỡ chữ 100/125/150%; các hình chữ nhật panel đã khai báo giao ô trụ/lõi/cổng **0 px²**.
- `tests/view/health-bars.test.ts`: thêm nhóm gồm elite đầy máu, elite bị thương, boss đầy máu và boss bị thương; chỉ hai con bị thương được locate và tạo instance, đúng lượng máu và vị trí. Hồi đầy hoặc thay serial bằng quái đầy máu xóa instance cũ. Đây là kiểm tra CPU/mesh, chưa phải ảnh thật.
- `tests/ui/hud.test.ts`: wave-start không sinh dòng số đợt thứ hai.
- `tests/ui/foe-badges.test.ts` mới: phân vai, ưu tiên boss, không art thì không node, lỗi tải, ngoài màn và tái sử dụng slot.
- `tests/ui/word-fx-presenter.test.ts`: thêm test Ultimate **đã được bộ cấp từ phân chỗ**: đầy năng lượng hiện từ, gõ xong giữ `Ultimate ready · Space`, không Cast tự động; giữ nguyên hiệu ứng 400. Test này không giải quyết trường hợp hết chỗ dưới đây.

## Ultimate còn lỗi trong phạm vi mô phỏng

Đã tái hiện một nguyên nhân chắc chắn bằng API thật, không mock: preset `relax`, bốn từ kỹ năng đã hiện, thêm một Seal, rồi tăng năng lượng lên 100. Kết quả: `liveCap = 5`, ledger có 5 từ; ô 5 vẫn `state = waiting`, `kitSlot = -1`, `text = ""`, UI ghi `Waiting for slot`.

`src/sim/words.ts:allocate()` chỉ cho Cleanse/Seal cấp bách thay từ khác khi đầy cap; Ultimate không có quyền này. Presenter không thể hiện một từ gõ được khi sim chưa cấp từ. Đổi nhãn hoặc tự cấp từ trong UI/app sẽ che lỗi và làm sai quyền sở hữu mô phỏng/replay.

**Chưa sửa `src/sim/words.ts` vì phiếu chỉ cho ghi `src/ui/`, `src/view/health-bars.ts`, `src/app/app.ts` và test.** Đã gửi câu hỏi xin mở thêm riêng file này; chưa có trả lời lúc bàn giao. Cần phiếu/mở phạm vi cho bộ cấp từ: ưu tiên Ultimate đầy năng lượng, chọn từ chưa gõ/chưa khóa có thể thay, vẫn giữ cap và các ràng buộc chữ cái. Cần thêm regression ở trạng thái đầy cap và đang khóa từ; không tăng cap để lách lỗi.

Lệnh tái hiện từ thư mục game:

```sh
node --import tsx --input-type=module -e 'import {makeWorld,addBeast} from "./tests/typing/world-fixture.ts"; import {stepWords,dealSeal,slotEntry} from "./src/sim/words.ts"; import {banQuyetView} from "./src/ui/ban-quyet.ts"; const {world}=makeWorld({preset:"relax"}); stepWords(world); dealSeal(world,0,addBeast(world)); world.seats[0].chanNguyenPm=100000; stepWords(world); console.log(JSON.stringify({cap:world.words.liveCap,live:world.words.ledgers[0].total,ultimate:slotEntry(world,0,5),cell:banQuyetView(world,0).slots[4]},null,2));'
```

## Bốn trạng thái và lệnh chụp cho Claude

`pnpm dev` bị chặn trước khi có server:

```text
Error: listen EPERM: operation not permitted 127.0.0.1:3008
```

Không có server để lại, không chụp/ghi file vào thư mục review ngoài writable roots. Chưa có số che màn sau 394b bằng `getBoundingClientRect`.

| Khung / trạng thái | Giao landmark trong test hình học | DOM % sau 394b | Giao landmark bằng DOM thật |
| --- | --- | --- | --- |
| 1280×720, prep | 0 px² | Chưa đo | Chưa đo |
| 1280×720, combat căng | 0 px² | Chưa đo | Chưa đo |
| 1920×1080, prep | 0 px² | Chưa đo | Chưa đo |
| 1920×1080, combat căng | 0 px² | Chưa đo | Chưa đo |

Thêm `games/immortality-cultivation/tests/ui/ui-layout394b-capture.mjs`. Kịch bản chụp bốn trạng thái, đo hợp DOM rect bằng `window.__ic.layout()`, ghi mọi giao cắt; combat có 30 quái fixture xen kẽ đầy máu/bị thương, hai Seal và Cleanse. Đối chiếu lượng máu trong mesh với toàn bộ quái bị thương, không có instance đầy máu. Ghi ô Ultimate trước khi gõ và sau khi gõ; nếu sim không cấp từ, giữ nguyên bằng chứng và báo FAIL. Không sửa fixture để giả Ultimate ready. Ghi ảnh và JSON trước khi báo lỗi để Claude vẫn xem đủ các trạng thái đã chạy.

Terminal 1, ngoài sandbox:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation
pnpm dev
```

Terminal 2, Chrome macOS, không URL flag chất lượng:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game
.local/bin/heavy.sh --gpu node games/immortality-cultivation/src/kit/tools/cdp-run.mjs games/immortality-cultivation/tests/ui/ui-layout394b-capture.mjs --width=1280 --height=720 --dpr=1
node scripts/review-index.mjs
```

Đầu ra riêng, không ghi đè ảnh 394:

`/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-16/tu-tien/ui-layout-394b/`

Gồm `ABOUT.md`, `after-coverage.json` (các mảng `records`, `failures`) và bốn ảnh `after-<khung>-<prep|combat-stress>.png`. Chỉ giữ ảnh báo cáo, không sinh dãy khung thô. Kịch bản mới qua kiểm tra cú pháp, **chưa chạy end-to-end**. Còn phải nhìn ảnh xác nhận quái đầy máu không có thanh và xem khả năng đọc/cuộn shop; các phép đo DOM không thay việc này. Cần kiểm tiếp cỡ chữ lớn, giảm chuyển động và clip của 400 trong built play host trước nghiệm thu thị giác.

## Chính xác art cần cho phiếu icon

Chưa có URL art được duyệt; không tạo ảnh mới trong phiếu sửa mã. Phiếu ảnh 401 đã có trong hàng việc; cần owner chọn và duyệt trước khi điền `FOE_BADGE_ART`.

| Vai trò / khóa cắm | Số art dùng cuối | Kích thước trong game (CSS px) | Tệp alpha để dùng ở DPR 1 / DPR 2 |
| --- | --- | --- | --- |
| Elite và general / `elite` | 1 | 24×24 | 24×24 và 48×48 PNG |
| Boss / `boss` | 1 | 32×32 | 32×32 và 64×64 PNG |

Tổng **2 hình huy hiệu độc lập**, **4 tệp kích thước runtime**; nguồn 1024×1024 giữ ngoài Git. Bản 32/48 px của 401 vẫn dùng cho sheet chọn ảnh; cần bổ sung xuất 24 px cho elite và 64 px cho boss nếu dùng đầy đủ DPR 2. Không cần ba icon riêng cho ba tính chất elite. Icon trong suốt, không chữ; đọc rõ trên nền đá tối. Chỗ cắm chỉ đặt ảnh, không tự tạo hào quang/vương miện bằng CSS.

## Phạm vi bàn giao

Chỉ ghi các file UI/app/test nêu trên và báo cáo này. Không sửa mã mô phỏng, `src/lab/`, bản đồ, scripts hoặc docs Tu Tiên, âm thanh, game khác. Không sửa `ban-quyet.ts` của 400. Không tạo media, đổi nhánh, commit, push, reset, clean hoặc stash; giữ thay đổi sẵn có của các worker khác.

Owner/Claude cần xử lý ba phần còn mở: quyền sửa bộ cấp từ Ultimate; chạy bốn capture và điền số DOM thật; duyệt hai huy hiệu của 401. Chưa đánh dấu 394b hoàn tất.
