# Phiếu 207 · Last Line · Nguồn portal là biến build

Hoàn tất mã và các kiểm được giao. Production `pnpm deploy:pack` đạt
**0 lỗi, 0 chuỗi `typing-game.local`**; demo nhà cũng đạt. `pnpm check` xanh
**265/265 test, 25 file**, kit **61/61**. `dist` bàn giao là production
không đặt biến. Chờ Claude duyệt rồi commit; không chạy lệnh Git ghi.

## 1. Mốc đầu và phần 205 chưa commit

Làm trong `games/.wt-ts-codex`, nhánh `ts-codex`, HEAD trước/sau:
`184c90d3380785e5afacd7d9267942781517b3ed`. Lệnh Git và trình ghi bằng chứng
chạy từ repo cha; mọi lệnh `pnpm` chạy với cwd là worktree.

Trạng thái đầu có đúng 12 đường của phiếu 205, đối chiếu
`docs/codex-queue/205-report.md`:

- `.gitignore`, `README.md`, `vite.config.ts`;
- `src/app/main.ts`;
- `src/view/bolts.ts`, `combat.ts`, `crowd.ts`, `models.ts`, `ship.ts`;
- `docs/changelog/2026-10-30-own-models.md`;
- `public/assets/typing-survival/models/manifest.json`;
- `tests/own-models.test.ts`.

Không có đường lạ nên tiếp tục theo luật phiếu. Hai file cùng sửa được chép
**trước khi sửa** vào [before/README.md](207/before/README.md) và
[before/vite.config.ts](207/before/vite.config.ts). Giữ nguyên mục Models của
README, cấu hình server và việc bỏ plugin model Space của 205.
[Mốc đầu và hash](207/before.json), [xác minh cuối](207/verification.json).

Trên mã chưa sửa, `pnpm deploy:pack` trả mã **1**, chỉ có **1 `local-host`**,
**0 `foreign-asset`**. Bundle `assets/index-c4MEbfce.js` chứa đúng một chuỗi
`typing-game.local`, tại **offset byte 312761**. Ngữ cảnh là fallback
`https://typing-game.local` từ kit; `src/app/learning.ts:18` tạo cầu nối
không truyền nguồn. [Log build](207/deploy-pack-before.log),
[JSON kiểm gói thuần](207/pack-before.json),
[file/offset/ngữ cảnh](207/local-host-before.json).

## 2. Bảy phần việc đã làm

1. **Mốc đầu:** ghi nhánh, HEAD, trạng thái, hash các file cần giữ, build nền,
   JSON bộ kiểm và inventory dist. Log build không trộn vào JSON kiểm gói.
2. **`VITE_PORTAL_URL`:** `portalHome()` trả `null` khi không đặt, rỗng hoặc chỉ
   khoảng trắng; nhận URL HTTP(S) tuyệt đối và từ chối URL sai, giao thức khác
   hoặc user/password với lỗi có tên biến. Giữ đường/query/fragment khi chuẩn
   hóa URL; cầu nối chỉ dùng phần nguồn.
3. **Một nơi tạo cầu nối:** thêm `src/app/portal.ts` với `portalHome()` và
   `createPortalBridge()`, gameId cố định `typing-survival`. `learning.ts`
   gọi adapter này, vẫn giữ `bridge ??=` khi chơi. `resetLearningBridge()`
   cho test đóng/tạo lại cầu nối, nhận tùy chọn host/storage; không truyền
   tùy chọn thì đóng và đưa module về trạng thái khởi tạo lười.
4. **Fallback lúc build:** plugin `last-line-portal-origin` trong
   `vite.config.ts`, `enforce: "pre"`, đọc `loadEnv(mode, root, ...)`, chỉ
   xử lý đúng đường `src/kit/learning/contract.ts`. Thay một khai báo
   `PARENT_ORIGIN` bằng nguồn cấu hình hoặc `""` trong bộ nhớ. Có 0 hoặc 2
   khai báo thì hàm thay ném lỗi và plugin gọi `this.error`; không bỏ qua.
   Dùng callback thay chuỗi để ký tự `$&` của URL được giữ nguyên.
5. **README:** ghi bản phát hành không biến, demo nhà có biến, cách tắt rõ
   biến đang có và việc `--allow-local-host` không tự đặt biến. Bỏ câu nguồn
   portal còn chặn production; giữ phần 205.
6. **Changelog:** thêm
   `docs/changelog/2026-10-30-portal-origin.md`, tiếng Việt, ghi hành vi,
   nguyên nhân và số đo trước/sau.
7. **Repo cha chỉ đọc:** xác định các điểm cần cấu hình cho Play/dev ở mục 5
   dưới đây, không sửa `package.json`, `play.sh` hoặc `docs/games/**`.

Khi biến trống, adapter luôn đưa kit một **host không có `parent`**, kể cả
khi host thật/host giả có parent. Vì vậy không gửi bất kỳ `postMessage` nào,
không đưa nguồn rỗng tới API trình duyệt, không xả hay xóa hàng đợi. Với
portal có cấu hình, giữ nguyên hành vi gửi, kiểm nguồn nhận và xả hàng đợi
của kit; không thêm bắt tay `hello`/`ack`.

## 3. Test viết trước mã

Thêm `tests/portal.test.ts` (**18 test**) và `tests/portal-build.test.ts`
(**11 test**); không sửa `tests/learning.test.ts` (**1 test**).

- URL: không đặt/rỗng/khoảng trắng; HTTPS có đường/query/fragment, HTTP có
  cổng; chuỗi sai, đường tương đối, FTP, JavaScript, username, password và
  cả hai thông tin đăng nhập.
- `reportWord` đi qua cầu nối module với host giả có parent: hai sự kiện
  được giữ đủ với `gameId: typing-survival`; tạo lại cầu nối vẫn không xả
  hoặc xóa. Có biến thì gửi tới đúng `https://portal.example`.
- Có cấu hình thì hàng đợi cũ được xả như kit hiện tại; nhận tin đúng nguồn,
  bỏ tin sai nguồn.
- Vite thật build với `write: false`; JS sinh ra chạy trong tiến trình Node.
  Kiểm cả fallback của kit và cầu nối game cho không biến, rỗng, khoảng
  trắng, portal ngoài và demo nhà; không biến thì JS không có chuỗi local.
  Đối chiếu Buffer của `contract.ts` trước/sau từng lượt.
- Build dừng với URL sai, FTP và credentials. Hàm thay từ chối 0/2 khai báo,
  thay đúng một khai báo và giữ nguyên ký tự giá trị.

Lượt trước mã: **29 đỏ / 1 xanh, 3 file**; phần lớn đỏ vì adapter/API mới
chưa có, test learning cũ xanh. [Log](207/tests-red.log),
[JSON](207/tests-red-results.json). Khi rà phép thay chuỗi, thêm assertion
`$&` trước khi sửa: **1 đỏ / 29 xanh**
([log](207/tests-red-literal.log)). Sau cùng **30/30 xanh**, 3 file,
1,748 giây cả lệnh ([log](207/tests-green.log),
[JSON](207/tests-green-results.json)).

Mọi biến test dùng `vi.stubEnv`, gỡ sau mỗi test. Fixture nằm trong
`tmp/portal-build-*` của game, xóa trong `finally` kể cả build lỗi;
cuối cùng **0 thư mục fixture còn lại**. Không dùng server/trình duyệt/mạng.

## 4. Bảy mục kiểm và số đo

| # | Kiểm | Kết quả và bằng chứng |
| --- | --- | --- |
| 1 | Production không cờ, không biến | `pnpm deploy:pack` mã **0**, 3,101 giây; **0 `local-host`, 0 `foreign-asset`, 0 lỗi tổng** vì 205 đã có trong cây. [Log](207/deploy-pack-after.log), [JSON thuần](207/pack-after.json). |
| 2 | Quét production | Đủ **12 file HTML/JS/CSS/JSON**, **0 chuỗi `typing-game.local`**; quét mọi file trong dist cũng 0. Inventory đủ **76 file** với đường, byte, SHA-256: [production-bundle.json](207/production-bundle.json). |
| 3 | Demo nhà | `VITE_PORTAL_URL=https://typing-game.local/ pnpm deploy:pack:local` mã **0**, 2,678 giây; **0 lỗi**, 76 file, **18.274.393 B**, 2 chuỗi local được đặt rõ. [Log](207/deploy-pack-local.log), [JSON](207/pack-local.json). |
| 4 | Dựng lại production bàn giao | `pnpm deploy:pack` không biến, mã **0**, 3,174 giây; inventory khớp bản ở mục 2. Trước/sau cùng **76 file**; **18.273.794 → 18.274.078 B**, tăng **284 B**. [Trước](207/dist-before.json), [cuối](207/dist-final.json), [JSON kiểm cuối](207/pack-final.json). |
| 5 | `pnpm check` | Mã **0**, 8,319 giây; **25 file, 265/265 test**, TypeScript và Vite xanh; `verify-kit` **61/61**. Golden **18/18** xanh; test bộ bài vẫn nhận **`7f073fa2`**. Không test thời gian đỏ nên không chạy riêng ba lần. [Log](207/check.log), [lệnh](207/check.json). |
| 6 | Test liên quan | Trước mã **29 đỏ / 1 xanh**; sau **30/30 xanh**; assertion `$&` có lượt đỏ riêng trước sửa. Log/JSON ở mục 3. |
| 7 | Phạm vi và whitespace | Cuối **17 đường**: 12 đường 205 cộng 5 đường mới; 207 sở hữu 7 đường, giao 205 ở README/Vite. Không có đường lạ, không mất đường 205; `git diff --check` mã **0**. [Status](207/status-final.txt), [log diff](207/diff-check.txt), [xác minh](207/verification.json). |

Giữ nguyên SHA-256 **62 file kit kể cả manifest**, **20 file sim**,
**9 file content**, **1 golden**. `verify-kit` đếm 61 file nội dung, không
đếm chính manifest nên hai con số kit khác nhau. `contract.ts` trước/sau:
`ab538e415b5f0df24578bc1c4a31dd46719aaafefbd43718166cae1d8cb19c15`.
Golden `tests/golden/s0-trace.json` trước/sau:
`42e4e5a9534bc78a0c252353ea7ee4670a1bec9e43eb42ef38c886aade530eea`.
[Hash trước](207/before.json), [hash sau](207/after.json).

Vite còn cảnh báo chunk trên 500 kB; không chặn build, không thuộc phiếu.
Thông tin `kit.invalid` và 97 level từ vựng không đóng gói không nằm trong
`problems`, giống nền. Bộ kiểm gói giữ nguyên byte.

## 5. Repo cha cần Claude đặt biến

Chỉ đọc các vị trí sau; nguồn nhà cần truyền rõ
`VITE_PORTAL_URL=https://typing-game.local/` trong luồng local:

| Vị trí hiện tại | Việc cần làm |
| --- | --- |
| `package.json:78`, `build:survival` | Hiện gọi build game mà không truyền biến; luồng Play/local phải đưa biến tới lệnh này, giữ khả năng build phát hành không biến. |
| `package.json:23`, `build:local` | Bước `typing-survival pnpm build:survival` cần nhận biến nguồn nhà khi build cả bộ local. |
| `package.json:77`, `dev:survival:app` | Thêm biến nguồn nhà cùng các biến DEV trước `pnpm dev`. |
| `play.sh:324–335`, mục Tuyến Cuối; gọi `build:survival` ở dòng **328** | Bảo đảm nhánh build local truyền biến; dựng lại dist khi chuyển cấu hình nguồn, tránh dùng lại gói production cũ. |

[Dòng script package](207/parent-package-json.json),
[đoạn Play](207/parent-play-sh.json). Nếu chưa đặt biến, **Play và dev ở
máy nhà giữ sự kiện học trong hàng đợi, không gửi về portal**.

Claude sửa `docs/games/DEPLOY_INDEPENDENCE.md` §9: bước A hiện ở dòng 198
còn ghi `VITE_PORTAL_ORIGINS` dạng danh sách và mặc định nguồn nhà; phiếu này
dùng **`VITE_PORTAL_URL` một URL**, mặc định tắt gửi. Các mô tả kiểm/build
liên quan ở dòng 201, 205, 225 cũng cần đồng bộ. Không sửa các dòng đó trong
phiếu; bước B bắt tay/ack vẫn là việc kit riêng.

## 6. Bàn giao, phần bỏ qua và cần duyệt

- Chỉ sửa 7 đường game liệt kê ở `owned207Paths` trong xác minh, cộng báo
  cáo/bằng chứng `207*` tại repo cha. Không sửa main, input, type-fx, audio,
  kit, luật chơi, nội dung hoặc media. Trạng thái repo cha ngoài `207*`
  không đổi so với mốc đầu của phiên.
- Không chạy server, trình duyệt, mạng, build/test game khác, `kit:sync`,
  tạo `.env*`, nới bộ kiểm hay tạo media theo lệnh cấm. Không thêm nút về
  portal, không làm `hello`/`ack`, không chạm Tu Tiên hoặc worktree khác.
  Mã Dragonhold 187 chỉ được đọc làm mẫu theo chỉ định.
- Chưa chứng nhận toàn bộ G7 về HTTP/server tĩnh hoặc cảm quan; phiên này
  kiểm build/bundle và mã thực thi trong Node đúng phạm vi đã giao.
- Claude cần duyệt plugin biên dịch và việc dùng host không có parent khi
  tắt portal, tách phần 205/207 rồi commit. [207-only.patch](207/207-only.patch)
  là bản vá riêng tính từ trạng thái 205 đã có; hai bản sao `before/` giúp
  tách README/Vite. Chưa commit, push hoặc gộp.
- **Thứ tự đề nghị: 205 → 207 → 191.** 205 và 207 cùng `ts-codex`; gộp
  model riêng trước, rồi cấu hình portal; sau đó gộp làn `.wt-ts-typefx`
  của 191 và kiểm lại. 207 không sửa file 191 sở hữu; phần `main.ts` giữa
  205 và 191 do Claude đối chiếu khi gộp, không xử lý trong phiếu này.

[run.py](207/run.py) ghi lệnh, thời gian, mã thoát và inventory;
[verify.py](207/verify.py) kiểm phạm vi/hash và tạo bản vá bàn giao.
