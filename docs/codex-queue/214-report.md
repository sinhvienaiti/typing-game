# Phiếu 214 · Cổng game: tên tiếng Anh và đường ảnh thật

Ngày 30/10/2026 · Repo cha · Nhánh `feat/space-typing-admin-uiux`.

## Kết quả và mốc tiếp tục

Đã hoàn tất phần mã, nhãn console, test và changelog. Ba thẻ dùng tên
Dragonhold, Wordwoven, Last Line; ảnh lấy từ nguồn riêng của game và tự
ẩn khi lỗi, không có glyph dự phòng cho mục có `art`. Sáu mục cũ giữ
nguyên hoàn toàn, kể cả Tu Tiên; mọi id, path, appUrl, group và thứ tự
giữ nguyên. Chưa có nghiệm thu bố cục bằng trình duyệt: đó là bước Claude
làm tiếp theo phiếu, không thuộc lượt thực hiện này.

Giữ nguyên `214/git-before.txt`, `214/status-before.txt` và log lượt đầu.
HEAD lượt đầu là `3faec9dd61b2bc76367e1a212b18f5249d6b064f`; lượt chạy lại
là `7afe7933bbd49155cea58e66c806a86a89f1c256`. Hai commit chen giữa chỉ
đổi tài liệu bàn giao/phiếu; không đổi nguồn portal hay hai script.
Đã đọc diff phần làm dở, giữ phần đúng và chỉnh độ ưu tiên selector CSS
của tiêu đề cạnh icon. Không đổi nhánh hay tạo worktree.

Trong lúc hoàn tất, HEAD tiến lên `b646d8550b71ddb9f39bdd77ffbbf43941cafcb9`
do commit bàn giao của tác nhân khác. Đã đối chiếu: chỉ đổi
`docs/HANDOFF_CURRENT.md`, không đổi nguồn đã test/build hay các lệnh kiểm.
Chứng cứ ở `214/head-advance.txt`, `214/head-after.txt`; kết quả vẫn áp
dụng cho mã hiện tại cùng phần thay đổi chưa commit của phiếu.

## Ba mô tả và nguồn danh từ

Số ký tự tính cả khoảng trắng và dấu chấm cuối. Mỗi câu có 50–110 ký tự,
một dấu chấm kết câu, không chữ Việt có dấu, không emoji.

| Game | Câu chọn | Ký tự |
|---|---|---:|
| Dragonhold | Type English words to unleash dragon fire and defend a misty forest from the Blight Horde. | 90 |
| Wordwoven | Type tower card words to power towers and defend a realm of mist and limestone peaks. | 85 |
| Last Line | Type words to reload guns and repel the Black Hole Horde on a causeway at the edge of a black hole. | 99 |

| Danh từ/cụm danh từ | Nguồn file:dòng |
|---|---|
| Dragonhold: English words, dragon fire, Blight Horde | `games/dragon-hold/index.html:6` có nguyên các cụm; `docs/games/dragon-lane/DESIGN.md:9` chốt gõ từ trên đầu quái để rồng phun lửa. |
| Dragonhold: misty forest | `docs/games/dragon-lane/DESIGN.md:28` chốt Đại Ngàn Sương, rừng thông; `:29` có sương và sinh vật rừng. Đây là cách mô tả cảnh quan, không đặt tên vùng mới. |
| Wordwoven: tower card words, towers | `games/typing-defense/src/ui/sheets.ts:42` có “Type tower card words (Power)”; `games/typing-defense/src/ui/tips.ts:17` có tháp gọi trợ giúp và gõ để bắn. `games/typing-defense/docs/td/TYPING_DEFENSE_DESIGN.md:28` chốt nhà phát chữ, gõ đúng thì tháp bắn. |
| Wordwoven: realm, mist, limestone peaks | `docs/games/ART_DIRECTION_2026-10-28.md:130` (§2.1) chốt cõi huyền ảo, đá vôi, các đỉnh và sương dày. Các từ mô tả địa hình không phải tên riêng mới. |
| Last Line: words, guns, Black Hole Horde | `games/typing-survival/src/app/main.ts:282` có nguyên câu gõ từ nạp súng và phe địch; `docs/games/NAMES_EN.md:23` chốt tên phe là Black Hole Horde. |
| Last Line: causeway, edge, black hole | `docs/games/ART_DIRECTION_2026-10-28.md:324` (§4.3) có “last causeway … at the edge of a black hole”; `:320` xác nhận chủ dự án chọn hướng B · Lightbearer. Câu không đưa tàu, phi công hay hạm đội vào mô tả. |

Đã đọc các phần nguồn yêu cầu, kiểm bằng `grep` trong nguồn game/index;
chứng cứ ở `214/noun-grep.txt` và `214/noun-sources.txt`. Tên phe Last Line
theo NAMES_EN và mã hiện tại, không theo tên Hollow Swarm cũ trong prompt art.

## Helper, ghép giao diện và CSS

- `resolveGameArt` kiểm riêng icon/bìa: đúng tiền tố của game, chặn `..`,
  dấu gạch chéo ngược, `//`, `?`, `#`; kiểm lại tiền tố sau chuẩn hóa URL
  và cùng nguồn `appUrl`. Thiếu/sai giá trị hoặc URL nền lỗi trả `null`.
- `gameCardModel` giữ title/description, metadata icon 192×192 với alt
  rỗng và bìa 1600×900 với alt `<Name> cover art`. Có trường `art` thì
  glyph luôn `null`, kể cả khi art rỗng hoặc còn kèm icon cũ.
- Helper không DOM, không import lúc chạy, enum hay namespace; Node 24
  nạp thẳng `.ts`. Listener lỗi dùng `{ once: true }`, ẩn ảnh rồi gọi móc
  ẩn khung bìa; test dùng đối tượng giả, không thêm gói.
- Hai chỗ dựng giao diện dùng model; không còn `game.icon` trong main.
  Mỗi ảnh đặt đủ src, alt, width, height, lazy và async; gắn listener trước
  src. Icon menu nằm trong span `.nav-game-icon` cũ; lỗi chỉ làm ảnh ẩn,
  span giữ chỗ để nhãn vẫn thẳng hàng.
- CSS mới dành sẵn khung bìa 16:9 trong lúc tải, bo góc và object-fit;
  icon 48 px cạnh tiêu đề và 1,25 em trong menu. Khi lỗi bìa, bỏ hàng bìa
  để trở về bố cục chữ. Giữ min-height 230 px và bố cục glyph cũ. Không
  sửa khai báo cũ; chỉ bổ sung `flex-shrink: 0` cho span icon ở menu gọn
  để giữ chỗ khi thiếu ảnh. Các gradient nền sẵn có không thay đổi; không
  thêm hình CSS, ảnh hoặc ký tự thay thế.

## Bảng bàn giao ảnh cho Claude

Ảnh của phiếu 177 chưa được duyệt nên ghi thư mục nguồn và bản 192,
không tự đặt tên file nguồn. Bìa của phiếu 176 cần chuyển PNG thành WebP.
Cổng chỉ lưu URL, không chứa ảnh game.

| Phiếu | Nguồn | Đích trong repo game |
|---|---|---|
| 177 | `games/dragon-hold/art-src/ui/app-icon/` · bản 192 | `games/dragon-hold/public/assets/dragon-hold/portal/icon-192.png` |
| 176 | `games/dragon-hold/art-src/ui/cover/cover-wide.png` | `games/dragon-hold/public/assets/dragon-hold/portal/cover-wide.webp` |
| 177 | `games/typing-defense/art-src/ui/app-icon/` · bản 192 | `games/typing-defense/public/assets/typing-defense/portal/icon-192.png` |
| 176 | `games/typing-defense/art-src/ui/cover/cover-wide.png` | `games/typing-defense/public/assets/typing-defense/portal/cover-wide.webp` |
| 177 | `games/typing-survival/art-src/ui/app-icon/` · bản 192 | `games/typing-survival/public/assets/typing-survival/portal/icon-192.png` |
| 176 | `games/typing-survival/art-src/ui/cover/cover-wide.png` | `games/typing-survival/public/assets/typing-survival/portal/cover-wide.webp` |

Last Line **chưa có thư mục `public/assets/typing-survival/`**. Claude tạo
khi gắn ảnh; sau khi duyệt/chuyển/chép ảnh thì chạy `media:push`. URL tính
trên appUrl của từng game, ví dụ icon Dragonhold là
`https://dragon.typing-game.local/assets/dragon-hold/portal/icon-192.png`.

## Tám mục kiểm

| Mục | Kết quả có số | Chứng cứ trong `214/` |
|---|---|---|
| 1. Test trước/sau | Nền 11 qua, 0 lỗi; đỏ trước mã 14 qua, **37 lỗi** trên 51 test; sau **51 qua, 0 lỗi**. 40 test mới, 11 learning bridge cũ đều qua. | `before/portal-test.*`, `before/portal-test-red.*`, `after/portal-test.*` |
| 2. Build portal | Thoát **0** trước và sau; byte ở bảng dưới. | `before/build-existing-deps.*`, `before/bundle-bytes.json`, `after/build.*`, `after/bundle-bytes.json` |
| 3. Tích hợp | `validate:space-integration` và `validate:play-mode`: **0** trước và sau. | `before/space-integration.*`, `before/play-mode.*`, `after/space-integration.*`, `after/play-mode.*` |
| 4. Hai script | Hai lệnh `bash -n`: **0**; **0 dòng** còn ba tên Việt cũ; **6 dòng** nhãn Tu Tiên giống HEAD. | `after/game-dir-syntax.*`, `after/bootstrap-syntax.*`, `verification.json` |
| 5. Registry diff | Chỉ **3 mục**, mỗi mục chỉ đổi `name`, `description`, bỏ `icon`, thêm `art`; **6 mục** cũ deepEqual fixture/HEAD. | `games-json.diff`, `verification.json` |
| 6. Emoji còn lại | **6 dòng** icon ở games.json và **1 dòng** thương hiệu ở main.ts, liệt kê dưới. | `emoji-remaining.txt` |
| 7. Ngoài phạm vi | **12 dòng** tên Việt trong play.sh/dev.sh được liệt kê dưới; không sửa. | `old-names-out-of-scope.txt` |
| 8. Phạm vi/khoảng trắng | Danh sách file do 214 sửa/tạo chỉ có đường được phép; `git diff --check` thoát **0**, kiểm riêng file untracked có **0 thông báo lỗi khoảng trắng**. Status toàn cây có thêm **5 file phiếu 194** so mốc đầu, gồm **2 file** xuất hiện trong lúc chạy lại; không phải do 214 tạo. | `status-after.txt`, `status-delta.json`, `diff-check.txt`, `files.txt` |

| Tài nguyên chính | Trước | Sau | Chênh lệch |
|---|---:|---:|---:|
| JS | 607.871 byte · `index-BaulQS2b.js` | 609.295 byte · `index-CUNiqGGe.js` | +1.424 byte |
| CSS | 127.133 byte · `index-Dwz_TM51.css` | 127.854 byte · `index-CnQYlBjB.css` | +721 byte |

Lượt đầu `before/build.log` thoát 1 vì pnpm tự gọi bước kiểm/cài dependency
và thiếu TTY; `before/build-existing-deps.log` thoát 0 là mốc build thật.
Lượt sau chạy `env pnpm_config_verify_deps_before_run=false pnpm --dir
portal build` để dùng dependency sẵn có, không cài gói hay truy cập mạng.
Build có cảnh báo chunk >500 kB đã có từ mốc trước; không mở rộng phiếu
để sửa cách chia bundle.

Kiểm file untracked dùng `git diff --no-index --check /dev/null <file>`:
mã 1 chỉ báo file mới có nội dung khác `/dev/null`; không có thông báo
khoảng trắng. `diff-check.txt` giữ mã thô của từng lệnh, không đổi thành 0.

So với `status-before.txt`, năm dòng thêm ngoài phạm vi là:

```text
docs/codex-queue/194/resume3-before.json
docs/codex-queue/194/resume3-start-status.txt
docs/codex-queue/194/resume3-start.diff
docs/codex-queue/194/resume3-preserved.json
docs/codex-queue/194/verification-previous.json
```

Ba file đầu đã có trong `status-resume.txt` trước khi sửa ở lượt chạy lại;
hai file sau do công việc đồng thời xuất hiện trong lúc làm. Không xóa
hay chỉnh chúng; do đó không tuyên bố status toàn cây chỉ có phần chênh
của 214 so với mốc đầu hoặc mốc chạy lại. File `status-delta.json` giữ cả
hai phép so sánh; đây là ngoại lệ khách quan của mục kiểm 8 trong cây dùng
chung, không thể làm sạch bằng cách đụng file tác nhân khác.

## Emoji và nhãn còn lại ngoài phạm vi

```text
portal/public/games.json:9: icon cũ của Monkeytype
portal/public/games.json:18: icon cũ của Vocabulary Shooter
portal/public/games.json:27: icon cũ của Recall Typing
portal/public/games.json:36: icon cũ của Karaoke Typing
portal/public/games.json:45: icon cũ của Space Typing
portal/public/games.json:90: icon cũ của Tu Tiên Thủ Ải
portal/src/main.ts:111: thương hiệu ⌨ typing games
```

```text
play.sh:298: Rồng Giữ Ải
play.sh:300: Rồng Giữ Ải
play.sh:311: Lời Gọi
play.sh:313: Lời Gọi
play.sh:324: Tuyến Cuối
play.sh:326: Tuyến Cuối
dev.sh:130: Rồng Giữ Ải
dev.sh:131: Lời Gọi
dev.sh:132: Tuyến Cuối
dev.sh:152: Rồng Giữ Ải
dev.sh:155: Lời Gọi
dev.sh:158: Tuyến Cuối
```

Đề xuất cho Claude: “Luyện gõ” → **Typing Practice**; “Game chiến đấu” →
**Combat Games**; “Khác” → **Other**; thương hiệu → **Typing Games**,
biểu tượng thật nhận từ bộ art riêng nếu cần. Phiếu này giữ nguyên tất
cả bốn nhãn, chỉ nêu đề xuất để Claude quyết.

## Danh sách file của phiếu

Các file mã/dữ liệu, test và tài liệu sửa hoặc tạo:

```text
portal/public/games.json
portal/src/main.ts
portal/src/styles.css
portal/src/game-card.ts
portal/tests/game-card.test.mjs
portal/tests/fixtures/legacy-games.json
scripts/game-dir.sh
scripts/bootstrap.sh
docs/changelog/2026-10-30-portal-english-names.md
docs/codex-queue/214-report.md
```

Danh sách chính xác từng file bằng chứng của cả hai lượt ở
[`214/files.txt`](214/files.txt); mọi file bổ sung nằm trong
`docs/codex-queue/214/`. Hai file mốc ban đầu được giữ nguyên.
Các log `.log` có trên đĩa nhưng thuộc luật ignore có sẵn của repo;
không sửa luật ignore trong phiếu này.

## Việc bỏ qua, rủi ro và bước Claude làm tiếp

- Không tạo/chép/chỉnh ảnh, âm thanh, không ghi games/** hay Tu Tiên,
  media config/scripts, admin, shared, package manifest, launcher hoặc
  chỉ mục changelog. Không dev server, trình duyệt, mạng, build/test game,
  commit, push hay lệnh Git ghi.
- Ba thẻ **chưa có ảnh** tới khi nhận ảnh 176, 177 và `media:push`.
  Trạng thái thiếu ảnh là thiết kế: khi giải mã lỗi, ảnh và khung bìa ẩn,
  thẻ dùng bố cục chữ. Không thay bằng emoji hoặc tranh dự phòng.
- Claude duyệt rồi kiểm trang chủ cổng **1280 và 1920**, mỗi cỡ ở cả
  trạng thái chưa ảnh và có ảnh 176/177; kiểm thêm menu gọn khi icon lỗi.
  Các test/helper và build không xác nhận nghiệm thu hình ảnh này.
- Nhánh cha **chưa push** theo bàn giao; phiếu này không thực hiện push
  và không kiểm trạng thái remote qua mạng. Claude duyệt, thêm chỉ mục
  changelog khi commit, rồi xử lý các nhãn ngoài phạm vi ở lượt riêng.
