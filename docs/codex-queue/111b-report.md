# Báo cáo 111b · Kit · Sửa bộ kiểm gói sau lần chạy thật

Ngày 29/10/2026, tại repo cha trên Mac mini; Node **v24.22.0**.
Đã sửa hai hành vi được giao. **Chưa đủ điều kiện kết thúc phiếu:**
build Last Line hiện có vẫn chứa đường tài nguyên Space, nằm ngoài hai sửa
của phiếu và ngoài phạm vi được phép ghi. Ba mục kiểm đạt đầy đủ;
mục kiểm build thật đạt phần Dragonhold, chưa đạt phần Last Line.

## File đã làm

| File | Nội dung |
| --- | --- |
| `shared/game-kit/tools/deploy/check-pack.mjs` | Manifest quyết định file từ vựng bắt buộc; thêm thống kê level không đóng gói, cờ CLI và tùy chọn API cho host nội bộ. |
| `shared/game-kit/tools/deploy/check-pack.test.mjs` | Từ 49 lên 55 ca; bổ sung các tình huống của phiếu và kiểm cờ không bỏ qua lỗi khác. |
| `shared/game-kit/DRIFT.md` | Cập nhật dòng phiếu 111 với thay đổi 111b. |
| `docs/codex-queue/111b/` | Đầu ra trước/sau, bốn lần kiểm build sau sửa, đột biến, đoạn bundle đối chiếu và trạng thái Git. |

## Hành vi sau sửa

Có `vocabulary/vocab-manifest.json`: kiểm sự hiện diện và SHA-256 của mọi
file trong `files`, kể cả file không được index nhắc tới. Level trong index
không thuộc manifest và không nằm trong gói được ghi vào
`report.vocabularyNotShipped = { count, examples }`; `examples` giữ tối đa
5 tên đầu theo thứ tự index. File thuộc manifest nhưng bị thiếu vẫn là
`missing-vocabulary`, không tính vào danh sách level không đóng gói.
Không có manifest thì giữ luật yêu cầu đủ level của index.

```sh
node shared/game-kit/tools/deploy/check-pack.mjs games/.wt-dh-codex/dist --game dragon-hold --allow-local-host --json
```

API tương ứng: `checkPack(dir, { gameId: 'dragon-hold', allowLocalHost: true })`.
`report.localHost` là tổng số lần xuất hiện chuỗi `typing-game.local` trong
HTML, JS, CSS, JSON, không phân biệt chữ hoa/thường, gồm cả subdomain.
Thống kê này có cả khi bật lẫn tắt tùy chọn. Mặc định vẫn báo `local-host`
mỗi file có chuỗi; cờ không bỏ qua các mã lỗi khác. Hai thống kê mới có
giá trị 0/danh sách rỗng khi không gặp trường hợp tương ứng.

## Bốn mục kiểm bắt buộc

1. **Test: đạt.** Cùng lệnh
   `node --test shared/game-kit/tools/deploy/check-pack.test.mjs`:
   trước sửa **49/49**, sau sửa **55/55**, cả hai mã thoát **0**,
   không ca hỏng hoặc bỏ qua. Xem [trước](111b/test-before.txt),
   [sau](111b/test-after.txt). Có ca index 100 level / manifest 3 level
   đạt với `count: 97`, ca thiếu level bắt buộc, và ca CLI/API cho host nội bộ.
2. **Build thật: đạt phần Dragonhold, chưa đạt phần Last Line.**
   Đã chạy chỉ đọc cả hai build; kết quả và đầu ra ở bảng dưới.
3. **Đột biến: đạt.** Trong bản sao tạm dưới thư mục bằng chứng, đổi
   `const hasVocabManifest = files.has(vocabManifest);` thành
   `const hasVocabManifest = false;`, rồi chạy riêng ca
   `missing-vocabulary accepts a 3 level manifest with a 100 level pinned index`.
   Kết quả **1 ca, 0 qua, 1 hỏng**, mã thoát **1**, với 97 lỗi thiếu level.
   [Đầu ra đỏ](111b/mutation-manifest.txt), [tóm tắt](111b/mutation-summary.json).
   SHA-256 nguồn thật trước/sau giống nhau; đã xóa hai bản sao tạm do mình tạo.
4. **Phạm vi kit: đạt.**
   `git status --short -uall -- shared/game-kit` chỉ có ba file được phép:
   `DRIFT.md`, `tools/deploy/check-pack.mjs`, `tools/deploy/check-pack.test.mjs`.
   [Đầu ra](111b/git-status.txt). `git diff --check` trên các file được giao
   cũng đạt, mã thoát **0**. Không chạy lệnh Git có ghi.

## Kết quả trên build thật

Mọi lần chạy dùng `node shared/game-kit/tools/deploy/check-pack.mjs <dist>
--game <id> --json`, thêm `--allow-local-host` ở các hàng có cờ.
Lệnh đầy đủ, mã thoát và stderr ở [nhật ký](111b/commands.json).

| Build / chế độ | File | Byte | Mã thoát | Lỗi còn lại | Đầu ra |
| --- | ---: | ---: | ---: | --- | --- |
| Last Line · mặc định | 51 | 1.519.782 | 1 | 1 `foreign-asset`, 1 `local-host` | [JSON](111b/typing-survival.json) |
| Last Line · có cờ | 51 | 1.519.782 | 1 | 1 `foreign-asset` | [JSON](111b/typing-survival-allow-local-host.json) |
| Dragonhold · có cờ | 229 | 29.948.980 | 0 | Không | [JSON](111b/dragon-hold-allow-local-host.json) |
| Dragonhold · mặc định | 229 | 29.948.980 | 1 | 1 `local-host` | [JSON](111b/dragon-hold-default.json) |

Last Line dùng `games/.wt-ts-codex/dist --game typing-survival`:
**97 lỗi `missing-vocabulary` trước sửa đã hết**; báo cáo ghi
`vocabularyNotShipped.count: 97`, năm tên đầu `levels/004.json` tới
`levels/008.json`, `localHost: 1`.
Bundle `assets/index-BLtWX-3u.js` vẫn có `/assets/space-typing/` và
`typing-game.local`. Cờ cho host nội bộ chỉ bỏ được lỗi thứ hai.

Dragonhold dùng `games/.wt-dh-codex/dist --game dragon-hold`:
`localHost: 2`, `vocabularyNotShipped.count: 0`. Có cờ thì `ok: true`,
`problems: []`; mặc định vẫn chặn bundle `assets/index-BRh_Fs8R.js`.
Đây là hai lần gặp chuỗi trong một file, nên mặc định có một lỗi `local-host`.

Đã lưu [đoạn bundle và SHA-256](111b/build-evidence.json), cùng JSON kiểm
[Last Line trước sửa](111b/typing-survival-before.json) và
[Dragonhold trước sửa](111b/dragon-hold-before.json).

## Phần bỏ qua và việc chủ dự án cần xem

Không bỏ mục kiểm nào. Theo giới hạn phiếu, không sửa `games/**`, không
build lại hay chạy bộ test game; không chạy `kit:sync`, server, trình duyệt,
mạng hoặc đụng Tu Tiên. Không có ảnh/âm thanh cần tạo trong phiếu mã này.

Chủ dự án cần cung cấp build Last Line đã xử lý đường tài nguyên Space;
nếu muốn kiểm mặc định đạt thì build đó cũng cần xử lý host nội bộ.
Nếu là bản demo nội bộ, dùng cờ mới để cho phép host. Không thể xác nhận
Last Line đạt trên build hiện có mà vẫn giữ luật `foreign-asset` của bộ kiểm
và giới hạn chỉ sửa các đường dẫn được giao.
