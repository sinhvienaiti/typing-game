# Báo cáo 111 · Kit · Bộ kiểm gói deploy G7

Ngày 29/10/2026, tại repo cha trên Mac mini; Node **v24.22.0**.
Đã hoàn thành bộ kiểm độc lập và năm mục kiểm của phiếu. Ba bản build
có sẵn đều bị bộ kiểm chặn vì nội dung hiện tại; không sửa các build.

## File đã làm

| File | Nội dung |
| --- | --- |
| `shared/game-kit/tools/deploy/check-pack.mjs` | API và CLI thuần thư viện chuẩn Node; chín mã lỗi cố định của phiếu. |
| `shared/game-kit/tools/deploy/check-pack.test.mjs` | 49 ca `node:test`, tạo gói giả trong `os.tmpdir()`, tự xóa sau từng ca. |
| `shared/game-kit/DRIFT.md` | Thêm một dòng phiếu 111; giữ các mục khác, gồm 102 và 107. |
| `docs/codex-queue/111/` | Đầu ra test, đột biến, ba lần kiểm build, bằng chứng và trạng thái Git. |

## API và cách gọi

```js
import { checkPack } from './check-pack.mjs';
const checked = checkPack(packageDir, {
  gameId: 'dragon-hold',
  budgets: { maxFileBytes: 25 * 1024 * 1024, maxFiles: 20_000 },
});
```

API đồng bộ, trả `{ ok, problems, report }` đúng cấu trúc được giao.
`budgets` tùy chọn: `maxFileBytes` là trần được phép bằng;
`maxFiles` là ngưỡng bắt đầu chặn. Mặc định nhận file 25 MiB,
chặn file lớn hơn 25 MiB và gói từ 20.000 file.

```sh
node shared/game-kit/tools/deploy/check-pack.mjs <thư-mục-gói> --game dragon-hold --json
```

CLI trả **0** khi đạt, **1** khi có lỗi kiểm gói, **2** khi tham số
hoặc thư mục đầu vào không dùng được. Bỏ `--json`: mỗi lỗi một dòng;
gói sạch không in gì. API ném lỗi khi đầu vào không hợp lệ hoặc không đọc được;
không đi theo symlink trong gói.

Quét chuỗi trong HTML, JS, CSS, JSON; đếm URL HTTP/HTTPS theo hostname,
gộp giao thức và cổng, bỏ `www.w3.org` cùng host máy nhà và các subdomain của nó.
Nguồn ngoài chỉ báo cáo, không chặn; URL model HTTP/HTTPS cũng chỉ báo cáo.
URL model nội bộ được bỏ query/fragment, giải mã tên file và tính tương đối
từ thư mục manifest. Manifest lồng dưới thư mục model cũng được kiểm.
JSON hoặc cấu trúc từ vựng/model hỏng được đưa vào mã lỗi tương ứng.

## Năm mục kiểm bắt buộc

1. **Test: đạt 49/49, 0 hỏng, 0 bỏ qua.** Viết test trước mã:
   [lần đỏ ban đầu](111/test-before.txt) do module chưa tồn tại;
   [lần xanh đầu](111/test-after.txt) và
   [lần xanh sau khi trả đột biến](111/test-final.txt).
   Có cả file thưa 26 MiB bằng `ftruncateSync`, biên đúng 25 MiB,
   gói thật 19.999/20.000 file, đủ ca đỏ/xanh cho từng mã, và namespace SVG/XML.
2. **Cú pháp: đạt, mã thoát 0.**
   `node --check shared/game-kit/tools/deploy/check-pack.mjs`;
   [đầu ra rỗng](111/node-check.txt), mã thoát trong [nhật ký lệnh](111/commands.json).
3. **Đã kiểm chỉ đọc cả ba build có sẵn**, không build lại.
   Số đo và phân loại lỗi ở bảng dưới; mã thoát cả ba lần là **1**.
4. **Đột biến: đạt.** Bỏ duy nhất vòng kiểm `foreign-asset`, chạy năm ca
   `^foreign-asset rejects`: **0 qua, 5 hỏng**, mã thoát **1**.
   Trả lại nguyên byte mã gốc, toàn bộ **49/49 xanh**, mã thoát **0**.
   [Đầu ra đỏ](111/mutation-foreign-asset.txt),
   [SHA-256 trước/sau giống nhau](111/mutation-summary.json).
5. **Phạm vi kit: đạt.**
   `git status --short -uall -- shared/game-kit` cuối cùng chỉ có
   `DRIFT.md` và hai file mới được phép ghi; [đầu ra](111/git-status.txt).
   Lúc bắt đầu có thay đổi đồng thời ở các file model/CDP của phiếu khác;
   không sửa các file đó. Không chạy lệnh Git có ghi.

## Kết quả trên build thật

| Build và `--game` | File | Byte | Lỗi chặn | Đầu ra |
| --- | ---: | ---: | --- | --- |
| `games/.wt-ts-codex/dist`, `typing-survival` | 51 | 1.516.154 | 1 `foreign-asset`, 1 `local-host`, 97 `missing-vocabulary` | [JSON](111/typing-survival.json) |
| `games/.wt-dh-codex/dist`, `dragon-hold` | 215 | 27.955.130 | 1 `local-host` | [JSON](111/dragon-hold.json) |
| `games/typing-defense/dist`, `typing-defense` | 123 | 20.962.466 | 1 `local-host`, 95 `missing-vocabulary` | [JSON](111/typing-defense.json) |

Đã đối chiếu trực tiếp chuỗi và file trong gói; lưu
[đoạn mã, danh sách level thiếu và số mục manifest](111/build-evidence.json).

- **Last Line:** `assets/index-ZZnwFqb9.js` có nguyên URL
  `/assets/space-typing/models/manifest.json` và `https://typing-game.local`.
  Index có 100 level, thiếu thật `levels/004.json`–`100.json`.
  Cả 5 mục SHA-256 của manifest đều khớp; gói không có manifest model riêng
  dưới `assets/typing-survival/models/`, nên kiểm model chưa có mục để đối chiếu.
- **Dragonhold:** `assets/index-CwYuvb7m.js` có host máy nhà trong hằng
  bridge và URL portal. Đủ 100 level, cả 102 mục SHA-256 đều khớp;
  hai manifest `kit3`/`m0b` có tổng 64 URL bậc model, không thiếu file.
- **Wordwoven:** `assets/learn-BS0ByE3O.js` có host máy nhà.
  Index có 100 level, thiếu thật `levels/006.json`–`100.json`.
  Cả 7 mục SHA-256 đều khớp; manifest model có 68 URL bậc, không thiếu file.

**Không thấy lỗi chặn báo nhầm theo hợp đồng của phiếu.** Bộ kiểm bắt chuỗi
trong bundle, kể cả hằng có thể chưa được dùng; không xác nhận request runtime.
Index trỏ tới level không có vẫn là lỗi, dù game hiện chỉ dùng vài level.
Không nới luật để các build cũ qua cổng. Ca query `?v=`, URL tương đối và
namespace `www.w3.org` đều đã có test xanh.

`report.external` của Last Line có `kit.invalid` × 1; Dragonhold có
`kit.invalid`, `catlikecoding.com`, `developer.download.nvidia.com`, mỗi host × 1;
Wordwoven rỗng. Đây là số lần chuỗi URL xuất hiện, gồm host làm gốc phân tích
URL và liên kết tài liệu trong bundle, không phải số request mạng.
Tổng cỡ Dragonhold hơn 25 MiB không gây lỗi: ngưỡng này áp dụng cho từng file.

## Phần để Claude nối tiếp

Chưa chạy `kit:sync`, chưa nối `deploy:pack`, chưa sửa game, chưa mở server,
trình duyệt hay mạng; không chạy build/bộ test của game và không đụng Tu Tiên.
Không có ảnh hoặc âm thanh trong phạm vi phiếu này.

Claude cần đồng bộ kit và nối bộ kiểm vào ba game. Trước khi nhận G7,
cần xử lý host máy nhà ở cả ba bundle, đường model Space ở Last Line,
và đóng gói đủ level mà index công bố ở Last Line/Wordwoven hoặc tạo index
phù hợp với bộ từ được gói cùng manifest hash tương ứng.
