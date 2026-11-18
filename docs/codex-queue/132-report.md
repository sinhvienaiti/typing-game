# Phiếu 132 · Wordwoven · Chuyển chữ người chơi đọc sang tiếng Anh

## Trạng thái

Đã dịch phần nguồn được phép, hoàn thiện test quét và đủ ba bảng. **Chưa đủ điều kiện đóng phiếu:** còn 16 literal UI tiếng Việt trong `src/main.ts`, ngoài “Chỉ được ghi”; house rules cấm chạy build/test suite trong khi mục kiểm yêu cầu `pnpm check` (có cả test và build). Đã hỏi chủ dự án mở phạm vi dịch riêng các literal này và cho phép các kiểm bắt buộc; chưa có trả lời. Không tự sửa `main.ts` hoặc miễn trừ nó khỏi test để lấy kết quả xanh.

Mã ở **`games/.wt-td-codex`**, nhánh `td-codex`, HEAD nền `999958a`. Worktree lúc tiếp nhận đã có 21 file tracked sửa và test quét mới từ lượt làm trước; trong thư mục báo cáo đã có ảnh chụp literal và các log. Lượt này đối chiếu, sửa tiếp câu chữ/viết tắt và hoàn thiện giấy tờ; giữ nguyên các thay đổi sẵn có. Các số từ log cũ được ghi riêng, không dùng làm kết quả kiểm bản hiện tại.

## Đã làm

- **306 chuỗi nguồn/trang**, gồm mảnh template, nhãn không dấu, viết tắt và bảy lời khuyên từng đọc từ kit. **52 chuỗi hoặc dòng kỳ vọng test** đổi theo chữ mới; dòng regex được ghi nguyên dòng để không bỏ sót.
- `index.html`: `lang="en"`, `<title>Wordwoven</title>`, nhãn canvas và thông báo tải tiếng Anh.
- `src/app/{prefs,sandbox}.ts`: tên chế độ, âm lượng và các nhãn/tooltip hộp cát; dịch cả `Kho` không dấu.
- `src/ui/{title,settings,profile,sheets,hud,build-menu,team-bar,tips}.ts`, `src/ui/td.css`: màn tựa, cài đặt, hồ sơ, tạm dừng, kết quả, thẻ nhà, hành động, banner, toast, gợi ý phím, lời Mộc Tinh và lời dạy của Bà Cú Mực; dấu thẻ ôn `Ôn` thành `R`.
- `src/view/{boss-2d,fx-pipe,words/cards}.ts`: nhãn combat, điểm, lời gọi, trạng thái và dấu ôn; `Phá Khiên` dùng `Shatter` cho gọn.
- `src/content/slice-1a.ts`: chỉ đổi viết tắt `view.short` sang chữ đầu tiếng Anh, gồm `ĐĐ → ZL`, `CT → HZ`, `MT → GF` của Ghost Flame, `TL → RS`, `MG → S`, `TN → RD`, `NP → SB`, `np → lb`, `L → B`, `M → G`. Tên riêng Mộc Tinh vẫn có `MT`.
- Hồ sơ dùng bảng lời khuyên tiếng Anh cục bộ, vẫn lấy đúng `AdviceId` từ `skillAdvice`. Không sửa `ADVICE_VI` trong bản chép kit.
- Năm file test cũ cập nhật kỳ vọng: `td-hud`, `td-input`, `td-r2`, `td-settings`, `td-test-pass`. Test mới `tests/english-ui.test.ts` quét literal và từng mảnh template bằng TypeScript AST, giải escape Unicode, chuẩn hóa NFC; quét thêm chuỗi CSS và HTML.
- Changelog tiếng Việt tại `games/.wt-td-codex/docs/changelog/2026-10-29-english-ui.md`.

Không đổi sim, luật, số, id, khóa lưu, event, tên file hay golden. Không sửa kit. Không mở server/trình duyệt, làm media, đụng cây chính của game, worktree khác hoặc Tu Tiên. Không chạy lệnh git ghi.

## Bảng duyệt

- [Chuỗi trước sửa](132/strings-before.md): **292 literal/mảnh template có chữ Việt** trong các thư mục được phép; thêm nhãn không dấu `Kho`, `Neo`, và bảng riêng 16 literal ngoài phạm vi ở `main.ts`. Tên riêng được liệt kê để đối chiếu, không tự đổi tên nhân vật.
- [Cũ → mới](132/strings.md): đủ **306 mục nguồn/trang + 52 mục kỳ vọng test**. Vị trí là dòng hiện tại; ảnh chụp trước sửa giữ trong `literals-before.json` và `index-before.html`.
- [Còn lại](132/remaining.md): **16 literal chưa dịch ở main.ts**, **22 literal/mảnh chứa tên riêng được giữ**, **83 literal kit**, danh sách chú thích và các kết quả thô không phải tiếng Việt. Trong phạm vi được phép sửa: **0 literal tiếng Việt thường**.
- [Quét thô](132/remaining-raw.txt), [dữ liệu AST](132/inventory.json), [số đếm](132/inventory-summary.json). Tái lập từ repo cha: `node docs/codex-queue/132/inventory.mjs`, rồi `python3 docs/codex-queue/132/make-tables.py`. Đây là kiểm kê tĩnh, không khởi chạy game hay suite.

Giữ các tên riêng Mộc Tinh, Bà Cú Mực, Chấm, Phẩy, Gạch theo AGENTS.md và `docs/games/NAMES_EN.md`; phần câu quanh tên đã dịch. Chỗ đọc/hiện nghĩa từ động ở `app/vocab.ts`, `app/learn.ts`, `typing/decks.ts`, `view/words/cards.ts`, `ui/hud.ts`, `ui/sheets.ts` không bị loại cả file khỏi test. Dữ liệu trường `vi` giữ nguyên. Không có nghĩa tiếng Việt hardcode ngoài kit cần miễn trừ trong bản nguồn hiện tại.

**Độ dài chưa đạt toàn bộ:** đã rút `Typing stats → Profile`, `Break Shield → Shatter`, các nhãn gọi/khởi tạo thành `Add`, cùng nhiều toast. Còn **34 mảnh nguồn** có cờ vượt 20% trong bảng (tính ký tự sau bỏ thẻ HTML hoàn chỉnh); gồm cả mảnh của câu dài, tên game bắt buộc và từ rất ngắn như Build, Learn, Good, Sound. Đây là danh sách bảo thủ theo mảnh literal, chưa phải số ô thực sự tràn. Không coi đã đạt cổng độ dài; Claude cần duyệt cách rút ở các ô nhỏ và kiểm đúng câu được ghép ở 1280/1920.

## Bốn kiểm bắt buộc

| Kiểm | Số và bằng chứng | Kết luận cho bản hiện tại |
|---|---|---|
| 1. `pnpm check`, số test trước/sau | Log kế thừa [check-before.log](132/check-before.log): **368/368 xanh, 35 file**. Log [tests-first-pass.log](132/tests-first-pass.log): **361 xanh + 8 đỏ = 369 test, 36 file**, là lượt sau dịch đầu tiên trước sửa kỳ vọng cũ. Log [ui-tests.log](132/ui-tests.log): **33/33 xanh, 4 file** sau lượt sửa đó. Test mới thêm **1** so với 368; bản hiện tại chưa chạy lại. | **Chưa đạt**. House rules cấm build/test suite; chưa được phép chạy lại. Test quét còn 16 literal ở main.ts nên chưa thể xanh. Log cũ không có lỗi thời gian; chưa phát sinh lượt thời gian cần chạy riêng 3 lần trong lượt này. |
| 2. Golden, gói, trần dòng | Log kế thừa [golden-check.log](132/golden-check.log): **2/2 `same:true`**, nội dung `f2a21037`, deck `9c9b91d8`; golden 1A **19.660 tick**, boss **5.695 tick**. Build trước dịch trong check-before: `/` **83,72/85 kB gzip**, `?title=0` **82,28/85 kB**. Đếm tĩnh hiện tại **10.564/10.900 dòng**, dư **336**; HEAD **10.554**, tăng **10** cho bảng lời khuyên EN. Trần hiện hành là **1B.V4, 10.900** theo BUILD_1B §16 và BUILD_NOTES §1.2; không nâng trần. | **Trần dòng đạt qua đếm tĩnh; golden/gói bản hiện tại chưa chạy lại**. Không cập nhật golden. Các file golden hiện tại không có diff. |
| 3. Đột biến “Bắt đầu” | Log kế thừa [mutation-red.log](132/mutation-red.log): scanner đỏ, chỉ rõ `src/ui/title.ts:285: Bắt đầu`, nhưng cùng lúc có **16 literal main.ts** khác; tổng **17 lỗi**. Bản hiện tại đã không còn literal đột biến ở title. | **Chưa đạt cặp đỏ → xanh**. Log đỏ trước đây bắt được đột biến nhưng không chứng minh được xanh sau xóa, vì 16 lỗi thật chưa được phép sửa. Không chạy lại test khi chưa có cho phép. |
| 4. Status đúng phạm vi | [status-final.txt](132/status-final.txt): **23 file**, gồm **21 tracked sửa + 2 file mới** (test quét và changelog); **0 file ngoài danh sách được ghi**. [scope-check.json](132/scope-check.json): **0 diff** trong kit/sim/typing/golden/package/scripts/vite config. `git diff --check` exit **0**. | **Đạt** kiểm phạm vi hiện tại. |

Không dùng số bundle trước dịch để khẳng định bản cuối dưới 85 kB. Không dùng log golden kế thừa để thay cho lần kiểm bản cuối. Cần chủ dự án cho phép chạy kiểm bắt buộc sau khi phạm vi nguồn đã đủ.

## Chủ dự án/Claude cần xem

1. Cho phép dịch riêng **16 literal `src/main.ts`**, hoặc giữ phiếu mở vì giới hạn đường dẫn. Đã chuẩn bị [bảng dịch đề xuất](132/proposed-main-translations.md); chưa áp dụng vào file ngoài phạm vi.
2. Xác nhận ngoại lệ cho phép `pnpm check`, `pnpm td:golden:check`, test quét và phép thử đột biến. `pnpm check` thực sự có build, không chỉ kiểm kiểu.
3. Duyệt từng dòng trong `strings.md`, đặc biệt 34 mảnh gắn cờ; sau đó kiểm các màn ở **1280 × 720** và **1920 × 1080**. Không có ảnh hay kết luận duyệt trực quan trong phiếu này vì trình duyệt bị cấm.

Chưa commit hoặc gộp.
