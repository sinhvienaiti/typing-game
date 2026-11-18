# Phiếu 019 · Lời Gọi · kiểm lại độc lập lượt sửa 27/10/2026

**Kết quả:** đối chiếu đủ **33 dòng có chữ “Đã sửa”**: 31 dòng khớp mã, 2 dòng khớp một phần (#1, #10), không dòng nào không thấy mã. Cổng đạt trên bằng chứng Codex lượt trước, được phép dùng lại vì HEAD và bản chụp nguồn vẫn khớp. **Chưa thể nghiệm thu phần trình duyệt:** sandbox tiếp tục chặn cổng 4291 bằng `EPERM`. Không có ảnh mới, không có lượt chơi CDP, chưa đo được 20 lần choáng mỗi cỡ. Các ô chưa chạy không được tính là đạt hay trượt của game.

Mã được kiểm: repo con `games/typing-defense`, HEAD `aa87ecac05391162e933a756ee9c6b1c6960fdf6`; diff `cc0c2c1..aa87eca`. `git diff` rỗng. Đã kiểm lại SHA-256 của **281 file** trong `snapshot.json`: **0 file lệch** ở cả cây nguồn hiện tại và bản sao dùng chạy Node/cổng; `fixes.diff` lưu từ lượt trước bằng đúng diff vừa đọc lại. Bằng chứng: [resume-validation.json](../../games/typing-defense/tmp/codex-019/resume-validation.json), [snapshot.json](../../games/typing-defense/tmp/codex-019/snapshot.json), [fixes.diff](../../games/typing-defense/tmp/codex-019/fixes.diff). [report-validation.json](../../games/typing-defense/tmp/codex-019/report-validation.json) kiểm đủ 33 dòng, 20 ô lỗi nặng/cỡ màn, 14 lượt kịch bản yêu cầu và 6 lượt bổ sung; không có liên kết bằng chứng bị thiếu.

Toàn bộ đường dẫn `src/...` dưới đây tính từ repo con. Bằng chứng `E/` là [games/typing-defense/tmp/codex-019/](../../games/typing-defense/tmp/codex-019/). Chỉ ghi vào thư mục này và báo cáo này; không sửa mã, test, tài liệu game; không commit/push hoặc dùng lệnh Git ghi. Skill dùng: `threejs-qa-release`, trong phạm vi của phiếu. Không tạo media. Không chạy phần cân bằng đang để chủ dự án quyết định.

## 1. Đối chiếu changelog với diff

“Khớp” trong bảng này là **khớp phần thay đổi mã được mô tả**, không thay cho kết luận nhìn ảnh hoặc chơi lại. Các số khung và kết quả trình duyệt của người sửa chưa được Codex xác nhận độc lập. Đã đọc `git show --stat` của đủ sáu commit; không commit nào thêm/sửa kịch bản trong `scripts/visual/scenarios`. `dfd574f` chỉ gói lại chú thích: máy quét TypeScript cho cùng token mã ở 31/31 file, lấy lại 54 dòng ([source-metrics.json](../../games/typing-defense/tmp/codex-019/source-metrics.json)).

Bằng chứng mã có số dòng: [source-map-resume.txt](../../games/typing-defense/tmp/codex-019/source-map-resume.txt). Bảng lấy cả #14: dòng này để mở phần dạy Ngắt nhưng vẫn có câu “Đã sửa nút Tanuki”.

| # | Lỗi | Changelog nói | Mã thấy ở | Khớp? |
|---|---|---|---|---|
| 1 | Thẻ chữ che hành động | Tránh boss + 1,5 m, mưa 6 m, đích Phát Chữ và chỗ trúng 0,7 s | `f7d43fc`: `src/main.ts:371` truyền `view.keepOut`; `src/view/debug-2d.ts:784`, `:798` gom hộp; `src/view/words/lanes.ts:38` chọn phía theo vị trí trước; `src/view/words/cards.ts:238` bố cục ba bước | **Khớp một phần.** Có đủ vùng và thời gian; bước cuối `cards.ts:240` gọi `spread(boxes, width)` bỏ vùng hành động. Chỗ hở được changelog thừa nhận vẫn có trong mã; tần suất chưa đo. |
| 2 | Dải nghĩa chồng thẻ khác | Bước cuối đẩy xa hơn 240 px | `f7d43fc`: `src/view/words/lanes.ts:53`, `:67` nhận `push`; `src/view/words/cards.ts:240` truyền chiều rộng màn. `d6c98cf`: `tests/td-test-pass.test.ts` có trường hợp bốn cột | **Khớp.** Đầu dò hàm thuần: giới hạn cũ còn chạm, giới hạn mới hết chạm; chưa kiểm DOM hai cỡ. |
| 3 | Câu Đêm 3 sai thanh đầy; phí mưa | Đổi lời dạy, từ chối tự chọn nếu không quái trong 14 m | `d6c98cf`: `src/ui/tips.ts:21`; `src/app/selection.ts:83` tạo `ultNone` trước khi gửi lệnh; `src/ui/hud.ts:33` có thông báo | **Khớp.** Node: thanh 100, không gửi lệnh khi trống; có quái gần thì gửi. Không áp điều kiện này cho điểm người chơi chủ động chọn. |
| 5 | C/P trùng Thư Đồng | Tháp dùng 🏹 và 🧨 | `f7d43fc`: `src/content/slice-1a.ts:50`, `:64`; nhãn Thư Đồng C/P/G vẫn ở `:154`–`:156` | **Khớp.** Chưa nhìn phông/biểu tượng trên canvas. |
| 6 | Phát Chữ, trúng và hạ quái nhạt | Quầng 1,3 m, chữ 15 px đậm, lóe ngọc/chữ bung, mực, vàng 16 px | `f7d43fc`: `src/view/debug-2d.ts:789` vẽ đầu/chữ; `:784` gọi hiệu ứng trúng; `:813` bắn mực (tốc 4 m/s, 500 ms); `:828` vàng; `src/view/fx-2d.ts:143`, `:197` lóe ✦ và chữ | **Khớp.** Mực đi khoảng 2 m theo tham số; cảm giác đọc vẫn cần chuỗi ảnh thực. |
| 7 | Thẻ kết cao hơn 720 px | Giữa màn, cao tối đa màn −24 px, cuộn; số hai cột dưới 800 px | `d6c98cf`: `src/ui/td.css:191`, `:213` | **Khớp.** Chưa đo hộp DOM, đầu thẻ, sao và năm từ ôn. |
| 8 | Gợi ý thua đổ cho boss | Đếm đòn boss và so mạng do quái lọt từ lúc lặng | `d6c98cf`: `src/ui/hud.ts:125`, `:163` đếm `blows`; `src/main.ts:314` truyền vào thẻ; `src/ui/sheets.ts:43` chọn gợi ý | **Khớp phần gợi ý đã nhận sửa.** Repro Node thực ra đúng câu ở cả hai cách bơm lũ. Phần áp lực Thuồng Luồng vẫn mở đúng phạm vi. |
| 9 | Xem bản đồ một chiều | Esc, Enter, Ⅱ mở lại thẻ kết; HUD nhắc | `d6c98cf`: `src/main.ts:195`, `:250`, `:296`; `:282` suy ra thẻ từ `mapOnly` | **Khớp.** Chưa bấm thật ba đường quay lại. |
| 10 | Neo/Phá Khiên bật ngoài vòng giúp | Chỉ bật trong vòng, “sáng ngay”; Neo ≥80% theo repro | `fe5186a`: `src/sim/systems/direct.ts:106` thêm `inRing` cho hai động từ, giữ Ngắt. `src/sim/systems/attention.ts:68`, `:102`, `:107` vẫn chặn theo ngân sách và số thẻ | **Khớp một phần.** Không có lời gọi tạo ngoài vòng trong mẫu Node; “sáng ngay” không đúng mọi lần. Neo đạt 18/21 và 34/39 trên **chiêu có kết quả**, không phải mọi lời gọi tạo ra. Chi tiết ở mục 3. |
| 11 | Nút tạm dừng còn dưới Cài đặt | Sửa CSS của `[hidden]` | `d6c98cf`: `src/ui/td.css:192` thêm `.td-sheet button[hidden] { display: none; }` | **Khớp.** Chưa xác nhận hình/đếm nút thấy được. |
| 12 | Phản hồi từng chữ nhạt | Nảy 1,5× trong 0,18 s, quầng ngọc, tắt theo giảm chuyển động | `f7d43fc`: `src/view/words/cards.ts:147` lớp `k`; `src/ui/td.css:153`–`:155` animation và `prefers-reduced-motion` | **Khớp.** Chưa nhìn hoạt ảnh. |
| 13 | Phím sai khó thấy | Giữ nền hồng/gạch đỏ tới phím đúng, rung 6 px/0,22 s | `f7d43fc`: `src/view/words/cards.ts:104` đặt `pinkUntil=Infinity`, `MS.shake=220`, `:257` biên độ 6; `src/ui/td.css:156` nền và gạch | **Khớp.** Chưa nhìn trạng thái trước/sau gõ đúng. |
| 14 | Ngắt dạy yếu, thẻ xa Tanuki | Để mở phần truyện; đã sửa nút hộp cát | `d6c98cf`: `src/app/selection.ts:94`, `:129`; `ce2a8c2`: `src/app/sandbox.ts:22`; cùng mã của #40 | **Khớp phần nút.** Node tạo được trống. Dẫn chiếu “dòng 31” trong changelog nhầm: nút Tanuki nằm ở #40. Phần truyện/vị trí thẻ chưa nhận sửa. |
| 16 | Gợi ý Đêm 1–4 luôn nhắc Tháp Pháo | Xét chưa có tháp, chưa gõ; Pháo chỉ khi mở | `d6c98cf`: `src/ui/sheets.ts:41`, `:42` xét tháp, `STAT.callWords`, `locked(w,"cannon")` | **Khớp.** Node kiểm bốn nhánh: không tháp, không từ, Ngày 1, Ngày 3. |
| 22 | Tối Thượng mở từ Ngày 3 | Mở từ Đêm 3; hộp cát giữ nguyên | `fe5186a`: `src/sim/systems/ult.ts:55`, `:60`; `src/ui/hud.ts:98`, `:100` đổi nhãn | **Khớp.** Node từ chối Ngày 3, nhận Đêm 3; test hộp cát trong cổng đã đạt. |
| 23 | Ma Trơi giống Cương Thi | Bay cao/nhấp nhô, bóng mặt đất, quầng tím sáng | `f7d43fc`: `src/view/debug-2d.ts:661`, `:666`, `:667`; bỏ viền quái đất cho quái bay ở `:649` | **Khớp.** Độ nâng dao động 0,75–1,45 m quanh 1,1 m; chưa nhìn ảnh đêm. |
| 24 | Câu Rễ hút bị Rễ Trồi đè | Đòn sau chờ lời đòn trước | `d6c98cf`: `src/ui/hud.ts:157`–`:160` đưa vào hàng đợi `this.lines` | **Khớp.** Node: 1.400 ms còn câu hút, 2.600 ms có hướng dẫn 30 s, 5.600 ms tới câu Rễ Trồi. |
| 25 | Thắng Đêm 5 ghi đã giữ 4 | Thẻ thắng lấy đêm đã thắng, sim không đổi | `d6c98cf`: `src/ui/sheets.ts:96` dùng `won ? Math.max(w.day, wavesCleared) : wavesCleared` | **Khớp.** Hai golden không đổi; chưa nhìn thẻ thắng. |
| 27 | Mầm báo khó thấy | Tăng mầm, vòng sáng 1,1 m; giữ thân boss | `f7d43fc`: `src/view/boss-2d.ts:302`, `:303`; bán kính mầm 0,2–0,55 thành 0,3–0,8 m | **Khớp phần mầm.** Chưa xác nhận độ đọc ở zoom 1; thân boss vẫn ngoài phạm vi sửa. |
| 28 | Nút đè dải chữ ở màn 720 | Dưới 1500 px dải đứng phải bảng đội; bốn nút ẩn phím | `d6c98cf`: `src/ui/td.css:68` đặt `left`, bỏ `transform`, selector `:has([data-act="space"]) kbd` | **Khớp.** Chưa đo lại tọa độ 308–668/853–1268 px mà người sửa nêu. |
| 29 | Sát thương đè nhãn Cháy | Đưa nhãn xuống dưới boss | `f7d43fc`: `src/view/boss-2d.ts:390` đổi `z-r-1.6` sang `z+r+1.6` | **Khớp.** Chưa nhìn hai cỡ. |
| 30 | Dấu hoảng đè nhau, thiếu tiếng | Xếp dấu cạnh nhau; hai tiếng mõ cao; để mở tần suất | `f7d43fc`: `src/view/debug-2d.ts:744` dịch theo chỉ số Thư Đồng; `src/view/audio-min.ts:215` gọi `go` ở 0 và 0,1 s, 1250 Hz | **Khớp phần hình/âm trong mã.** Chưa nghe hoặc nhìn; không kết luận mức đọc hay âm thực. |
| 31 | Mẹo boss đọc như trạng thái | Thêm “Mẹo:” | `d6c98cf`: `src/ui/hud.ts:199` | **Khớp.** Chưa nhìn thanh ngủ. |
| 33 | Nhắc bộ gõ hiện mãi | Tắt 8 s sau dấu hiệu cuối | `d6c98cf`: `src/main.ts:172`, `:261`, `:296` dùng hạn `imeUntil` và so đồng hồ | **Khớp.** Chưa đo trên trình duyệt/bộ gõ macOS. |
| 34 | Bắt đầu từ hộp cát lại vào hộp cát | Chọn Bản đồ 1 bỏ `sandbox` | `d6c98cf`: `src/main.ts:131`, `:134`, `:178` truyền `story=true` khi chọn ván từ màn đầu | **Khớp.** Chưa xác nhận URL và cờ ván sau điều hướng. |
| 35 | Thẻ mờ Neo/Phá Khiên mang ✋ | Vẽ biểu tượng theo động từ | `f7d43fc`: `src/view/debug-2d.ts:602` dùng `callLabel(w,b.c)[0]` thay `CALL_ICON[kind]`; hàm `callLabel` đã có ⚓/🛡️ trong `src/view/words/cards.ts` | **Khớp.** Chưa nhìn thẻ mờ. |
| 36 | Chép số không báo | HUD báo lưu file và chép số 10 s | `d6c98cf`: `src/main.ts:221` gọi `tellLost`; hạn 10.000 ms ở `:80` | **Khớp phần báo đã nhận sửa.** Chặn bấm lặp vẫn chưa có, đúng phần để mở trong changelog; chưa tải file hay kiểm clipboard. |
| 37 | Chunk Hồ sơ hỏng không báo | Ghi chưa tải được/F5 dưới mục | `d6c98cf`: `src/ui/title.ts:240` khi `card===null` đổi chữ `small` | **Khớp.** Chưa chặn request để kiểm thông báo. |
| 38 | Chưa đo vẫn khen | Hiện lời mời chơi một ngày đêm khi `stages===0` | `d6c98cf`: `src/ui/profile.ts:37` | **Khớp.** Chưa mở hồ sơ trên trình duyệt. |
| 39 | Thẻ tạm dừng xưng “anh” | Đổi thành “bạn” | `d6c98cf`: `src/ui/sheets.ts:93` | **Khớp.** Chuỗi mới có nguyên văn. |
| 40 | Tanuki gọi một mình không trống | Kèm 8 Cương Thi sau 6 s; sửa tooltip sót | `d6c98cf`: `src/app/selection.ts:94`, `:129` hẹn +360 tick; `ce2a8c2`: `src/app/sandbox.ts:22` tooltip | **Khớp.** Node: Tanuki +0, tám Cương Thi +360, trống tick 1.860. |
| 41 | Thiếu nút Boss/Ngày, báo lỗi chung | Thêm 2–5/Boss và lý do boss đã thức | `fe5186a`: `src/sim/commands.ts:293`; `d6c98cf`: `src/app/sandbox.ts:21`, `src/app/selection.ts:28` nhận `boss`; `src/ui/hud.ts:32` đã có `bossBusy` | **Khớp.** Test đường lệnh và từ chối đã đạt; chưa bấm/đo nút. |
| 42 | Nút kho tràn, “Nạp =” khó hiểu | Hàng Kho hai cột, “Đầy Tối Thượng” | `d6c98cf`: `src/app/sandbox.ts:15`, `:20` thêm `td-wide` và đổi tên; CSS hai cột đã có ở `src/ui/td.css:54`–`:56` | **Khớp.** Chưa đo `scrollWidth/clientWidth`. |

## 2. Cổng

Dùng lại lượt Codex trước theo quyền trong phiếu; **không chạy lại `pnpm check`/golden** khi chưa có thay đổi nguồn hay quan ngại về hai cổng đó. Chúng đã chạy dưới `heavy.sh` trong bản chụp `E/work/games/typing-defense` để đầu ra build/cache nằm trong đường dẫn được phép ghi. Đã xác minh lại nguồn như đầu báo cáo. Lượt thử server mới chạy ở repo con thật.

Các lệnh cổng của lượt trước, với `pnpm_config_verify_deps_before_run=warn` để pnpm không tự cài lại workspace:

```text
heavy.sh pnpm check                         exit 0
src/kit OK: 31 files match kit-manifest.json
Test Files 32 passed (32)
Tests      346 passed (346)
tsc --noEmit && vite build && bundle-budget: đạt
/:         84,81 kB gzip / 85 kB; còn 0,19 kB
/?title=0: 83,36 kB gzip / 85 kB; còn 1,64 kB

heavy.sh pnpm td:golden:check                exit 0
td-1a:      same: true, changed: {}, firstMovedAtTick: null
            ticks: 19660, commands: 389, problems: 0, rejected: 0
td-1b-boss: same: true, changed: {}, firstMovedAtTick: null
            ticks: 5306, commands: 45, problems: 0, rejected: 0
content: cd59313e; deck: 9c9b91d8 (cả hai)

Đếm dòng mới: 10.500 / 10.500, còn 0 dòng
```

Kích thước chưa làm tròn, đo gzip từ manifest và các file build của chính lượt Codex: `/` **84.812 byte**, trần 85.000, còn **188 byte**; `/?title=0` **83.362 byte**, còn **1.638 byte**. Quy tắc dòng đúng `tests/boundary.test.ts`: đếm ký tự xuống dòng trong `src/**/*.ts`, bỏ `src/kit/**`.

Log đầy đủ: [check.log](../../games/typing-defense/tmp/codex-019/check.log), [golden.log](../../games/typing-defense/tmp/codex-019/golden.log); đầu ra rút gọn: [gate-summary.log](../../games/typing-defense/tmp/codex-019/gate-summary.log); số byte: `E/source-metrics.json`; số dòng từng file: `E/line-count.json`, số tổng kiểm lại: `E/resume-validation.json`.

Có cảnh báo môi trường `Your node_modules are out of sync with your lockfile. The workspace structure has changed since last install`. Các cổng trên vẫn exit 0. Không chạy `pnpm install`, không sửa lockfile/dependency. Đây là cảnh báo của máy/workspace, chưa phải lỗi mới của game.

## 3. Tái hiện các lỗi nặng đã sửa

Đã thử đúng cổng riêng dưới khóa máy dùng chung:

```text
cwd: games/typing-defense
env pnpm_config_verify_deps_before_run=warn ../../.local/bin/heavy.sh \
  pnpm exec vite --host 127.0.0.1 --port 4291 --strictPort
exit 1
Error: listen EPERM: operation not permitted 127.0.0.1:4291
```

Bằng chứng: [server-resume.log](../../games/typing-defense/tmp/codex-019/server-resume.log). Không tìm cổng/host khác, không xin nâng quyền, không dùng máy chủ khác để vượt sandbox. Không khởi chạy Chrome khi máy chủ riêng chưa mở được. Vite đã thoát; không có server do lượt này khởi chạy còn cần tắt.

**“Không tái hiện được” dưới đây nghĩa là không thực hiện được lượt kiểm do hạ tầng; không có nghĩa là đã thử mà lỗi không xuất hiện.** Không lấy ảnh của người sửa làm kết luận của Codex. Số khung DOM/ảnh tự chụp ở tất cả các ô là **0**; kết luận trực quan là **chưa chắc**.

| # | Lỗi | Cỡ | Kết quả | Bằng chứng |
|---|---|---|---|---|
| 1 | Thẻ che boss/Rễ Trồi/choáng, mưa, nơi trúng | 1280×720 | **Không tái hiện được** trong trình duyệt | `E/server-resume.log`; 0 khung; nhánh bỏ `keep` thấy tại `cards.ts:240`. |
| 1 | Như trên | 1920×1080 | **Không tái hiện được** trong trình duyệt | Cùng log; 0 khung, chưa đo chồng hình. |
| 2 | Dải nghĩa đè thẻ | 1280×720 | **Không tái hiện được** trong trình duyệt | Cùng log; Node ở `E/node-rules.json` chỉ kiểm tọa độ hàm thuần, không phải DOM ở cỡ này. |
| 2 | Dải nghĩa đè thẻ | 1920×1080 | **Không tái hiện được** trong trình duyệt | Node bốn cột: `oldTouch=true`, `newTouch=false`; chưa chạy `td-1b-learn`. |
| 3 | Câu Đêm 3, bấm = khi không quái | 1280×720 | **Không tái hiện được** trên màn; **đã hết ở nhánh lệnh Node đã đo** | `E/node-rules.json`: 0 lệnh gửi, `ultNone`, charge 100; có quái gần thì 1 lệnh. Câu mới ở `tips.ts:21`. Không ảnh. |
| 3 | Như trên | 1920×1080 | **Không tái hiện được** trên màn | Cùng đầu dò Node, không có phép đo trình duyệt riêng ở cỡ này. |
| 5 | C/P trùng trên sân | 1280×720 | **Không tái hiện được** trên màn | `E/source-map-resume.txt`, hai nhãn tháp mới; chưa chụp canvas. |
| 5 | Như trên | 1920×1080 | **Không tái hiện được** trên màn | Cùng bằng chứng mã, không ảnh. |
| 6 | Phát Chữ, lóe, chết, vàng | 1280×720 | **Không tái hiện được** | `E/source-map-resume.txt`; 0 khung chuỗi 50 ms. Chưa kết luận độ nổi. |
| 6 | Như trên | 1920×1080 | **Không tái hiện được** | Cùng lý do; không ảnh. |
| 7 | Thẻ kết bị cắt, cả khi có ≥5 từ ôn | 1280×720 | **Không tái hiện được** | Chưa có `getBoundingClientRect`, `scrollWidth/clientWidth`; 0 ảnh thẻ thắng. |
| 7 | Như trên | 1920×1080 | **Không tái hiện được** | Cùng lý do; không có số đo hộp DOM. |
| 8 | Gợi ý do quái lọt lúc boss tới | 1280×720 | **Không tái hiện được** trên thẻ; **đã hết ở hai repro Node đã đo** | `E/node-repro.json`: hai ván bơm 220 quái đều thua, gợi ý đúng; chi tiết dưới bảng. Không ảnh. |
| 8 | Như trên | 1920×1080 | **Không tái hiện được** trên thẻ | Node không phụ thuộc viewport; chưa kiểm thẻ ở cỡ này. |
| 9 | Xem bản đồ → Esc/Enter/Ⅱ | 1280×720 | **Không tái hiện được** | Chưa gửi phím/click CDP; các nhánh mã đã đối chiếu mục 1. Không ảnh. |
| 9 | Như trên | 1920×1080 | **Không tái hiện được** | Cùng lý do. |
| 10 | Neo/Phá Khiên ngoài vòng giúp, sáng/gõ được | 1280×720 | **Không tái hiện được** trên màn; vị trí **đã hết trong mẫu Node**, khẳng định “sáng ngay” **còn phản ví dụ** | `E/node-direct.json`, `E/node-direct-detail.json`; 0/318 lời gọi tạo ngoài vòng. Chưa đo/nhìn thẻ. |
| 10 | Như trên | 1920×1080 | **Không tái hiện được** trên màn | Cùng mẫu Node, không phải lượt chơi thứ hai theo cỡ màn. |
| 11 | Cài đặt còn ba nút tạm dừng | 1280×720 | **Không tái hiện được** | Chưa đếm nút thấy được/chụp ảnh; selector `[hidden]` đã sửa trong mã. |
| 11 | Như trên | 1920×1080 | **Không tái hiện được** | Cùng lý do. |

### Số đo bổ sung trên Node

Dùng lại `E/audit-node.mts`, `E/node-rules.json`, `E/node-direct.json` của lượt trước; nguồn đã khớp lại SHA-256. Chạy mới dưới `../../.local/bin/heavy.sh`:

```text
node --import tsx tmp/codex-019/audit-direct-detail.mts   exit 0
node --import tsx tmp/codex-019/audit-repro.mts           exit 0
```

Các phép kiểm này dùng mô phỏng và bot thật của game, không có DOM, không chứng minh phím CDP hay cảm nhận hình/âm.

- **#2:** bốn cột tại x=900/905/910/915, một nửa rộng 172 px và ba nửa rộng 94 px: đẩy giới hạn 240 px cho offset `[-240, -57,50, 91,25, 240]`, vẫn chạm; cho giới hạn 1920 px ra `[-347,99, -77, 116, 308,99]`, hết chạm (`E/node-rules.json`).
- **#3/#22:** nhánh từ chối chỗ trống giữ **100/100 charge**, không gửi lệnh, có `ultNone`; sau khi đặt quái gần gửi đúng một lệnh. Ngày 3 bị `locked`, Đêm 3 có sự kiện `ult`. Bảy kiểm logic trong `E/node-rules.json` đều `true`.
- **#8:** seed 1, Đặt sẵn → Boss → flood(220) ngay: bơm tick 2, boss stage 2; thua tick **2.323**, stage 4; `livesBoss=42`, `blows=0`, gợi ý **“Quái lọt vào Lũy lúc Mộc Tinh tới: gõ Bắn mạnh ở tháp gần Lũy.”** Chờ boss vào stage 4 rồi bơm: bơm tick **1.082**, thua **2.743**, `livesBoss=58`, `blows=0`, cùng câu đúng. Các số 42/58 là bộ đếm mạng do mô phỏng bơm lũ, không phải 42/58 mạng khởi đầu và không phải số cân bằng truyện. Log: [node-repro.log](../../games/typing-defense/tmp/codex-019/node-repro.log).
- **#8/#16, nhánh chưa xây:** đầu dò hàm `lossHint` cho đúng câu xây Tháp Cung; có tháp nhưng chưa gõ thì nhắc gõ; Ngày 1 không nhắc Pháo, Ngày 3 có nhắc. Lượt AFK tự nhiên không xây/không gõ dừng tại giới hạn **21.600 tick**, đã tới Đêm 3 và **chưa thua**; không gọi đây là repro “thua Đêm 1”. Đường thua đó còn chờ trình duyệt/cách dựng lại phù hợp.
- **#14/#40:** qua `Selection.act` thật: Tanuki tại +0 tick, tám Cương Thi tại **+360 tick = 6 s**, sự kiện trống tại tick **1.860**. Không chỉ kiểm tooltip.

**#10 — tách mẫu số để không kết luận nhầm.** Hộp cát, Cân bằng, troll-lead, 3 đêm/seed, seed 1–20 ở mỗi tốc độ, cùng header/k và chính sách của repro. Cả 40 ván thắng, không có vấn đề invariant hoặc lệnh bị từ chối; phím Node gửi/đếm 30 WPM **6.802/6.802**, 70 WPM **11.680/11.680**.

| Tốc độ | Chiêu | Lời gọi tạo | Ngoài vòng | Sáng ngay cuối tick tạo | Từng sáng | Gõ được / chiêu có kết quả | Gõ được / lời gọi tạo |
|---|---|---:|---:|---:|---:|---|---|
| 30 WPM / 97% | Neo | 59 | 0 | 53 | 58 | 18/21 = 85,7% | 18/59 = 30,5% |
| 30 WPM / 97% | Phá Khiên | 114 | 0 | 53 | 106 | 62/102 = 60,8% | 62/114 = 54,4% |
| 70 WPM / 90% | Neo | 55 | 0 | 49 | 54 | 34/39 = 87,2% | 34/55 = 61,8% |
| 70 WPM / 90% | Phá Khiên | 90 | 0 | 72 | 80 | 68/82 = 82,9% | 68/90 = 75,6% |

“Chiêu có kết quả” đếm sự kiện `direct` (`ok=true` hoặc `false`); không phải toàn bộ `call:made`. Không suy rằng tất cả lời gọi chưa gõ đều bị bỏ lỡ: quái có thể chết trước khi chiêu kết thúc; một chiêu cũng có thể không được cấp lời gọi do giới hạn số chiêu mở. Chưa dùng tỷ lệ gõ/tạo để chấm cổng ≥80% khi mẫu số trong repro chưa được làm rõ.

Đầu dò mới xác nhận hai loại phản ví dụ, [node-direct-detail.json](../../games/typing-defense/tmp/codex-019/node-direct-detail.json):

- **Neo 30 WPM, seed 4**, call 8196, sự kiện tạo tick **22.699**, ở trong vòng, không sáng lần nào; đóng tick **22.788** khi quái đã biến mất, không có kết quả `direct` trong khoảng đó. Tương tự Neo 70 WPM seed 16: call 11267, tick **17.230–17.320**, quái biến mất. Đây không tự chứng minh một chiêu người chơi cần gõ đã bị bỏ lỡ.
- **Phá Khiên 70 WPM, seed 5**, call 6147, quái 2049: tạo tick **11.479**, trong vòng, số thẻ sáng lúc đó **0**, `typedWindowTicks=352`. Không sáng suốt **206 tick = 3,433 s**; tick **11.685** có `direct(ok=false)`, quái còn sống. Vì vậy “ở trong vòng thì sáng ngay” có phản ví dụ cả khi chiêu thực sự hết hạn. Ngân sách chú ý trong `attention.ts` vẫn là điều kiện độc lập; chưa đo bằng trình duyệt để chấm mức ảnh hưởng khi chơi.

### Tần suất Dồn lửa che boss lúc choáng

| Cỡ | Yêu cầu | Số lần choáng thực đạt | Số lần che | Tần suất |
|---|---:|---:|---|---|
| 1280×720 | khoảng 20 | **0** | chưa đo | **chưa đo**, không phải 0% |
| 1920×1080 | khoảng 20 | **0** | chưa đo | **chưa đo**, không phải 0% |

Lý do: cùng lỗi mở cổng, lưu rõ trong `E/resume-validation.json`. Nhánh bố cục bỏ `keep` vẫn tồn tại; chưa có ảnh Codex để xác nhận lần xuất hiện nào. Claude cần chạy lại độc lập: cùng cảnh `td-1b-tour` ảnh 07, khoảng 20 cửa sổ choáng mỗi cỡ; lưu cả số lần vào được choáng, số lần có Dồn lửa, rect thẻ/boss và ảnh. Không thay 20 cửa sổ choáng bằng 20 khung của cùng một lần choáng. Hai lỗi cân bằng Đêm 4 và áp lực Thuồng Luồng không được cố tái hiện.

## 4. Chơi hồi quy

**Chưa chạy được lượt chơi bàn phím CDP tại 1280×720**, do máy chủ riêng bị chặn. Không có số console, số phím CDP mất hay số đo chữ tràn/thẻ che của lượt trình duyệt; để là **chưa đo**, không ghi “0 lỗi”. Không có ảnh hồi quy mới để xem. Không coi bot Node dưới đây là lượt chơi trình duyệt.

Để giữ phần kiểm còn làm được, đã dùng lại hai ván bot Node seed 7, Cân bằng, chiến thuật `tacticsPlan("good")` ở **30 WPM/97%** và **70 WPM/90%**, đi đủ Ngày/Đêm 1–5 tới thua/thắng. Ván 30 WPM thua Đêm 5 tick **49.274**, 0 mạng; ván 70 WPM thắng tick **36.300**, 10 mạng. Cả hai 0 lệnh từ chối, 0 vấn đề invariant, chạy lại log cùng mã băm (`9be91465`, `21cbc54c`). [node-story.json](../../games/typing-defense/tmp/codex-019/node-story.json), script `E/audit-node.mts story`.

| Màn | 30 WPM: phím Node gửi/đếm | 70 WPM: phím Node gửi/đếm | Chơi CDP 1280×720, console/hình |
|---|---|---|---|
| Ngày 1 | 75/75 | 114/114 | Chưa chạy/chưa đo |
| Đêm 1 | 16/16 | 56/56 | Chưa chạy/chưa đo |
| Ngày 2 | 73/73 | 111/111 | Chưa chạy/chưa đo |
| Đêm 2 | 14/14 | 65/65 | Chưa chạy/chưa đo |
| Ngày 3 | 76/76 | 116/116 | Chưa chạy/chưa đo |
| Đêm 3 | 42/42 | 58/58 | Chưa chạy/chưa đo |
| Ngày 4 | 74/74 | 116/116 | Chưa chạy/chưa đo |
| Đêm 4 | 41/41 | 94/94 | Chưa chạy/chưa đo |
| Ngày 5 | 72/72 | 121/121 | Chưa chạy/chưa đo |
| Đêm 5 và boss | 117/117 | 188/188 | Chưa chạy/chưa đo |
| Các lúc hửng sáng cộng lại | 8/8 | 7/7 | Chưa chạy/chưa đo |
| **Toàn ván truyện** | **608/608** | **1.046/1.046** | **Không suy ra CDP không mất phím** |
| Hộp cát, 20 seed × 3 đêm mỗi tốc độ | 6.802/6.802 | 11.680/11.680 | Chưa chơi CDP; số Node ở mục 3 |

Chưa xác nhận được chữ tràn/cắt, thẻ che hành động hoặc lỗi console ở bất kỳ màn nào. Không phát hiện lỗi mới có bằng chứng hình ảnh trong mục này vì chưa vào trình duyệt. Danh sách còn cần kiểm gồm toàn bộ các màn trên, đặc biệt Đêm 3 với `=`, Đêm 5 lúc choáng và thẻ thắng có năm từ cần ôn.

## 5. Kịch bản sẵn có

Đã đọc thư viện `scripts/visual/scenarios/td-1a6-common.mjs` (phím thật CDP, `typeFor`, `LOOK`, `cardsClean`, chạy lại log trên Node) và runner `src/kit/tools/cdp-run.mjs`. Chưa khởi chạy kịch bản nào vì thiếu dev server. Ma trận riêng của lượt này: [scenario-matrix.json](../../games/typing-defense/tmp/codex-019/scenario-matrix.json). Mọi file kịch bản trong ma trận đều tồn tại.

| Kịch bản | 1280×720 | 1920×1080 |
|---|---|---|
| `td-1b-learn` | Chưa chạy — EPERM | Chưa chạy — EPERM |
| `td-1b-story` | Chưa chạy — EPERM | Chưa chạy — EPERM |
| `td-1b-boss` | Chưa chạy — EPERM | Chưa chạy — EPERM |
| `td-1b-night5` | Chưa chạy — EPERM | Chưa chạy — EPERM |
| `td-1b-build` | Chưa chạy — EPERM | Chưa chạy — EPERM |
| `td-1b-chunks` | Chưa chạy — EPERM | Chưa chạy — EPERM |
| `td-theme` | Chưa chạy — EPERM | Chưa chạy — EPERM |
| `td-1b-tour` (bổ sung cho repro và ảnh 07) | Chưa chạy — EPERM | Chưa chạy — EPERM |
| `td-1b-direct` (bổ sung cho #10) | Chưa chạy — EPERM | Chưa chạy — EPERM |
| `td-1b-ult` (bổ sung cho #1/#3) | Chưa chạy — EPERM | Chưa chạy — EPERM |

**Không có kịch bản mới được commit trong lượt sửa:** đầu ra `git diff --name-only cc0c2c1..aa87eca -- scripts/visual/scenarios` rỗng; `git show --stat` cũng xác nhận. `zz-verify.mjs` là kịch bản tạm của người sửa, có ở `tmp/mac-2026-10-27/test/verify-fix/zz-verify.mjs`; đã đọc mã để hiểu repro, không chạy hoặc lấy kết quả đó làm kết quả của Codex.

Hai điểm của phép kiểm cũ cần lưu ý khi Claude chạy lại: `pauseSettingsOneButton` đếm nút `data-sheet` nên kỳ vọng phải là **0** khi Cài đặt mở, đồng thời đếm riêng nút Xong thấy được là **1**; `cardsOffBoss` cho phép tỷ lệ chồng ≤10% và `cardsOffRain` cho phép không có khung mưa. Những kiểm ấy đạt không tự chứng minh “0 khung chồng” hoặc đã kiểm được mưa. Lượt mới cần báo số khung thực và số lần chồng, không chỉ cờ pass.

Đã để runner tuần tự [run-scenarios.mjs](../../games/typing-defense/tmp/codex-019/run-scenarios.mjs), tái sử dụng nguyên các kịch bản/thư viện, từng trình duyệt qua `heavy.sh --gpu`. Chỉ chạy chế độ `--list` trong lượt này (exit 0; **không mở Chrome**). Claude có thể dùng trong môi trường trình duyệt bình thường sau khi mở server riêng 4291:

```text
cd games/typing-defense
node tmp/codex-019/run-scenarios.mjs --run
```

Runner này chưa được kiểm đường chạy trình duyệt, chỉ chuẩn bị ma trận và chỗ lưu log/ảnh vào `E/browser/`. Nó không bao gồm lượt chơi đủ Ngày/Đêm 1–4 hay 20 lần choáng mỗi cỡ; Claude vẫn cần làm hai phần ấy. Không có lỗi mới từ các kịch bản để liệt kê vì chưa chạy, không có ảnh kịch bản mới.

## 6. Những điểm Claude cần xử lý tiếp, theo mức

1. **Nặng, đã biết — #1:** nhánh cuối bố cục bỏ vùng boss vẫn còn (`src/view/words/cards.ts:240`). Cần đo khoảng 20 lần choáng/cỡ ở cảnh tour 07, ảnh + rect; chưa có tần suất độc lập. Việc chọn ưu tiên bố cục vẫn theo phạm vi người sửa để mở, không coi đây là bản sửa mới của Codex.
2. **Lỗi gốc nặng, đã sửa một phần — #10:** điều kiện vị trí đã có và 0/318 lời gọi của mẫu Node tạo ngoài vòng. Còn phản ví dụ thẻ không sáng tới lúc Phá Khiên hết hạn: 70 WPM/90%, seed 5, Cân bằng, cảnh troll-lead, call 6147, tick 11.479–11.685. Repro: `../../.local/bin/heavy.sh node --import tsx tmp/codex-019/audit-direct-detail.mts`; xem `E/node-direct-detail.json`. **Chưa chắc mức ảnh hưởng trên màn; chưa có ảnh do EPERM.** Cần kiểm trực quan hai cỡ trước khi quyết định có đổi luật ngân sách/chiêu. Không suy rằng mọi lời gọi quái chết sớm phải gõ được.
3. **Nhẹ, độ chính xác giấy tờ — C019-1:** “sáng ngay” và cách gọi mẫu số ≥80% ở #10 cần diễn đạt chính xác; số 18/21 và 34/39 khớp chiêu có kết quả, trong khi lời gọi tạo là 59 và 55. Bằng chứng/repro như mục 3; không có ảnh vì đây là đối chiếu số Node. Dòng 14 còn dẫn nhầm #31 thay vì #40. Codex không sửa changelog theo giới hạn chỉ đọc.
4. **Chưa nghiệm thu, không gắn mức lỗi game:** Claude cần hoàn tất mục 3 ở cả hai cỡ, mục 4 bằng phím CDP thật và ma trận mục 5; ghi console, phím gửi/đếm, DOM, ảnh đã xem. Cổng đạt và kiểm mã không thay cho các phép này. Chưa thể đóng phiếu với kết luận mọi lỗi đã hết.

Hai lỗi cân bằng nặng để mở (#4 Đêm 4 quá nhàn; phần áp lực của #8) vẫn dành cho chủ dự án, không cố tái hiện và không đề xuất thay số trong phiếu này. Năm việc nhỏ trong changelog cũng không triển khai vì phiếu 019 chỉ đọc. Không sửa game, không chạy game khác/Tu Tiên/tools/audio-lab, không commit hoặc push.
