# Phiếu 203 · Wordwoven · C10: năm sửa của giám khảo trên thẻ chữ, rồi icon gọi 133, huy hiệu thẻ 172 và icon khay 165 thay emoji và chấm CSS

**Nguồn:**
- `docs/HANDOFF_CURRENT.md` §3, hàng L4 (C10 đạt 8,0), việc cho vòng sau: "giữ màu đã gõ trên mọi thẻ khớp; mũi chỉ khay dùng chữ V ở mọi mép (vòng hở ở mép trái đọc thành chữ "C"); ×N và chữ đóng dấu không ra khỏi màn, không đè HUD (kiểm `overHud` mọi khung); nét viền cứng 1–2 khung khi gõ xong; chữ đóng dấu hiện ngay khung phím".
- Hai giám khảo C10 vòng 4, cùng 8,0 sát ngưỡng (khay mép 7,0 và 7,5):
  - `games/.wt-td-1c/tmp/lane-l4/judge-c10-r4c/verdict.md`, mục "Năm sửa có ích nhất";
  - `games/.wt-td-1c/tmp/lane-l4/judge-c10-r4d/verdict.md`, mục "Năm việc nên sửa".
- `docs/td/BUILD_NOTES.md` §8.15 (nhánh `td-1c`): "emoji `CALL_ICON` và hạt ●○ bằng CSS vẫn chờ phiếu 133 và 172"; mũi chỉ của khay "là hiệu ứng tạm cho tới khi ảnh mũi tên của khay (phiếu Codex) được nhận".
- `AGENTS.md` (chủ dự án 28/10): không emoji, không hình vẽ bằng mã; mọi chi tiết UI có hình thật.
- Chủ dự án 29/10: "tăng thêm việc cho codex cho tôi".

**Vì sao:** C10 qua mức 8 nhưng không còn chỗ dư. Một lỗi ở khay nặng thêm là trượt. Năm sửa chung của hai giám khảo nâng khay và combo, và cho phím đúng nhanh như Typing Break. Emoji và hạt ●○ trên thẻ trái luật 28/10; ảnh thay đã giao (133, 165, 172), đang chờ chấm nhận.

**Báo cáo:** `docs/codex-queue/203-report.md` (tiếng Việt), thư mục `docs/codex-queue/203/` (chỉ chữ và số, không ảnh).

**Làn:** làn Codex duy nhất (chủ dự án 30/10: một làn). Chạy sau phiếu 200, trên cùng nhánh `td-ui`.

**Không trùng:** 133, 165, 172 (chỉ vẽ ảnh); 103 (thẻ kết, dải nghĩa); 174 (texture "chữ dệt"); 193 (Settings, loa, tiếng phím ở `.wt-td-keys`); 200 (danh sách chọn ảnh UI và `art.ts`: phiếu này dùng lại, không làm lại).

**Claude, trước khi giao:**
- 200 đã xong (có `docs/codex-queue/200-report.md`), worktree `games/.wt-td-ui` đúng nhánh.
- Báo làn L: không sửa `src/view/words/` và `src/view/3d/words.ts` khi phiếu này chạy.
- Muốn Phần B chạy thì chấm nhận 133, 165, 172 trước (`docs/codex-queue/accept-*/verdict.md`). Chưa chấm thì Phần B tự bỏ.

## Nơi làm

- Worktree `games/.wt-td-ui`, nhánh `td-ui` (Claude cắt cho phiếu 200). Làn chạy ở gốc repo cha (`.`); mọi đường dẫn trong phiếu tính từ đó.
- Kiểm trước khi sửa, lưu vào `203/status-before.txt`:
  - `git -C games/.wt-td-ui branch --show-current` là `td-ui`;
  - `git -C games/.wt-td-ui merge-base --is-ancestor 2a1f61d HEAD` thoát 0 (nhánh có C10 vòng 4 của `td-1c`);
  - `git -C games/.wt-td-ui status --short -uall` sạch, hoặc chỉ có file của 200 khi Claude chưa commit 200. Khi đó ghi danh sách, không sửa file nào của 200, trừ danh sách chọn và `art.ts` ở Phần B (ghi rõ dòng thêm).
  - Thiếu một điều trên thì dừng, ghi lý do vào báo cáo.
- Số dòng trong phiếu theo `td-1c` `2a1f61d`. Phiếu 200 có thể dời vài dòng; tìm theo tên hàm.
- Ảnh nguồn chỉ đọc ở checkout chính `games/typing-defense/art-src/` (liên kết `art-src/*` của worktree, nếu có, cũng trỏ về đó).

## Luật chung (phiếu mã)

- Test trước, mã sau. Mỗi sửa của Phần A có một hàm thuần (không `document`, không DOM, không three) và test riêng.
- Vitest chạy ở môi trường `node`. Không thêm jsdom hay thư viện nào.
- Chú thích tiếng Anh. Chữ người chơi thấy là tiếng Anh.
- Luật chơi, sim, bộ định tuyến và ván vàng không đổi.
- Không dev server, trình duyệt, mạng. Claude chạy `td-1c-words` và gửi giám khảo.
- Không thêm emoji, hình CSS, SVG hay hình canvas để thay ảnh còn thiếu. Ảnh chưa nạp xong thì chỗ đó trống.

## Đọc trước (chỉ đọc)

- `src/view/words/cards.ts`:
  - dòng 28, 34: emoji `CALL_ICON` và emoji neo, khiên của `callLabel`;
  - dòng 48: `pips()` trả ●○;
  - `read()` (132), `render()` (196), `layout()` (294);
  - `SWAP_MS`, `RIM`, `squeeze`, `burst` (98–104).
- `src/view/words/feel.css` (chữ đóng dấu `.k::before`, `td-key-hold`); `src/ui/td.css` dòng 150–187 (`.td-card::before`, `.td-card-pips`, `.td-stamp`, `.td-card .k`).
- `src/view/3d/words.ts`: `anchor()` (147), `slide()` (173), `slip()` (370), `combo()` (467), `frame()` (478), `pointers()` (519).
- `src/view/debug-2d.ts`: `calls()` (566; mũi tam giác ở mép dòng 580, bong bóng dòng 588–610); dấu thợ `NPC_LETTER` (52) và `⛏️` (537).
- `src/ui/build-menu.ts` dòng 82 (`callLabel(w, c).join(" ")`); `src/ui/hud.ts` `PANELS` và `boxes()`.
- `src/typing/router.ts` (`KEY.group`, `router.group`); `src/main.ts` dòng 340 (`--ui`: 0,8 ở 1280 × 720, 1,2 ở 1920 × 1080).
- `tests/td-c10-r3.test.ts`, `tests/td-sheet-cards.test.ts`: cách test không cần DOM.
- `scripts/visual/scenarios/td-1c-words.mjs`: `overHud`, `keyFrames`, `oneFrame`.
- `docs/games/TYPING_BREAK_STUDY.md` §4 (T1, T3) và §5.3 mục 1.
- Hai phiếu chấm vòng 4 (ở Nguồn) và `docs/td/BUILD_NOTES.md` §8.13–§8.15.
- Phiếu 200 và `200-report.md`: danh sách chọn ảnh, `art.ts`, cách chép ảnh.
- `docs/codex-queue/133-report.md` (§5: ngoại lệ alpha của bản thu), `165-report.md`, `172-report.md` (§4: bộ giao cuối ở `_review/172/delivery-final/`).

## Phần A · Năm sửa của giám khảo (chạy ngay)

**A0. Đo trước** (lưu `203/before.txt`): `pnpm check` (số test, số file); gói "/" và `?title=0` từ dòng `bundle budget`; chunk 3D; số dòng `.ts` ngoài kit.

**A1. ×N, chữ đóng dấu và mọi thứ của thẻ ở trong màn, ngoài HUD, ở mọi khung.**
- Hiện nay:
  - ×N đứng trái hay phải thẻ (`tag.side` trong `frame()`), không kẹp. Ở khay trái, ×11 mất dấu ×.
  - Chữ đóng dấu (3× lên trên trái) đè số Gold, Wood 2 khung (`tray-type`).
  - Lúc camera lia, thẻ trượt vào khay (`slide()`) đè bảng HUD trên trái ở 1920 (−20 → +130 ms, `tray-in`).
  - `overHud` của kịch bản chỉ kiểm thẻ, ở khung cuối.
- Cần:
  - Hàm thuần `keepIn(box, view, panels, pad)` (gợi ý file mới `src/view/words/safe.ts`): dời hộp ít nhất để nằm trong màn (lề 8 px) và không cắt hộp HUD nào. Không có chỗ hợp lệ thì trả chỗ gần nhất kèm cờ.
  - Dùng nó mỗi khung cho: thẻ (cả lúc trượt, kẹp sau khi nội suy), ×N, chữ đóng dấu của phím ở trạng thái lớn nhất, nhãn hạng (`td-stamp`) trên đường nâng, điểm cuối của chữ bay (`td-fly`).
  - ×N: hàm `comboSide(...)` chọn phía. Giữ phía hôm nay nếu đủ chỗ; không thì đổi phía, rồi lên trên thẻ, rồi kẹp.
  - `words.ts` cần hộp HUD: thêm tham số tùy chọn cho `CardFeel.frame` (cỡ màn, `panels`), truyền từ `cards.draw`.
  - Kiểm `PANELS` của `hud.ts`: bảng trên trái, thanh nhập, bảng Build có trong `boxes()`. Thiếu thì thêm vào hộp tránh của thẻ. Không đổi bố cục HUD.
- Test:
  - 1280 × 720 và 1920 × 1080; hộp HUD theo bố cục thật (đọc `td.css`), ghi số vào test.
  - Lưới hộp thử khắp màn: 0 hộp ra ngoài, 0 hộp cắt HUD. Hộp đã hợp lệ thì dời 0 px.
  - Thẻ ở khay trái, phải, trên, dưới: ×N trong màn, đủ dấu ×.
  - Chữ đóng dấu trên chữ đầu của một thẻ ngay dưới bảng trên trái: không cắt bảng.

**A2. Mũi chỉ của khay: cùng một chữ V ở mọi mép.**
- Hiện nay: `pointers()` vẽ hai chữ V theo hướng thật tới nhà. Ở mép trái, giám khảo thấy một vòng hở như chữ "C" ngay trước từ. Ở mép dưới, chữ V đọc tốt nhưng chỉ khoảng 10 px và sát thanh nhập.
- Cần hàm thuần `trayPointer(edge, dir, card, view, bars)` trả tâm, góc, cỡ:
  - cùng hình V như mép dưới, xoay theo hướng tới nhà; lệch pháp tuyến của mép ≤ 60°;
  - đỉnh V ngoài khung thẻ, cách ≥ 4 px, không đứng ngay trước chữ đầu của từ;
  - cỡ ≥ 16 px ở 720p, ≥ 24 px ở 1080p; cách thanh nhập ≥ 8 px; nằm trong màn;
  - hai cánh đối xứng qua hướng; góc giữa hai cánh 70–100°; đầu hai cánh nằm sau đỉnh.
- Bỏ vòng hở. Báo cáo ghi vì sao mép trái thành chữ "C" (đọc mã).
- Mũi chỉ vẫn là hiệu ứng của kho hiệu ứng (`pool`), như nay, tới khi `tray-arrow` của 165 được nhận (B5).
- Test: 4 mép × 3 hướng (thẳng ra, ±40°) × 2 cỡ màn, đủ mọi luật trên. Hình ở mép trái là hình ở mép dưới xoay đúng góc (lệch ≤ 0,5 px).

**A3. Giữ màu đã gõ trên mọi thẻ khớp.**
- Hiện nay: phím đầu của cặp bậc 2 (`KEY.group`, ví dụ "t" khi có "team" và "thanks") đóng dấu lên cả hai thẻ (`read()`, dòng 138–141). Nhưng `typed` của cả hai vẫn 0. Sau khoảng 190 ms, chữ "t" về màu mực, dù ô nhập vẫn có "t".
- Cần hàm thuần, gợi ý `typedShown(word, typed, group)`:
  - nhóm còn mở (`router.group ≥ 0`): mọi thẻ chưa gõ có chữ đầu là chữ của nhóm hiện 1 chữ màu đã gõ (`.t`);
  - phím sau đóng nhóm: thẻ bị loại trả màu ngay khung đó; thẻ được khóa theo `typed`;
  - `draw()` vẽ lại thẻ khi số này đổi.
- Không đổi bộ định tuyến hay sim.
- Test theo khung:
  - phím "t": "team" 1, "thanks" 1;
  - 50 khung sau (khoảng 830 ms): vẫn 1 và 1;
  - phím "e": "team" 2, "thanks" 0, cùng khung;
  - Backspace đóng nhóm: cả hai 0;
  - thẻ không khớp ("eye") luôn 0.

**A4. Gõ xong từ: viền cứng 1–2 khung.**
- Hiện nay: `RIM` (dòng 100) là quầng mềm ngay từ khung đầu. Giám khảo đọc ra "sáng lên", chưa ra "đóng sập" (T3). Hộp gõ xong đo khung đầu / đỉnh 0,91 (cần ≥ 0,95).
- Cần hàm thuần `rimAt(t, cardH, ui)`:
  - khung 0 và 1 (t < 34 ms): một nét trắng ấm `#FFF0D8`, không nhòe (blur 0), dày ≥ 4 px ở 720p; mép ngoài vượt thẻ 10–12 % chiều cao thẻ mỗi phía;
  - từ khung 2: thành quầng mềm, tắt theo hàm mũ như nay; hết ở `SWAP_MS`;
  - độ sáng khung 0 ≥ khung 1 ≥ khung 2.
- Giữ nhịp bóp ngang 100 ms, trống 60 ms (`squeeze`).
- Test: các mốc 0, 17, 34, 100, 194 ms, ở 720p và 1080p.

**A5. Chữ đóng dấu hiện ngay khung phím, không khoét lỗ.**
- Hiện nay: chữ đóng dấu là `::before` của `.k`, chạy animation CSS 67 ms. Chữ gốc trong suốt 50 ms (`td-key-hold`). Giám khảo D thấy chữ đóng dấu hiện đầu tiên ở +53–61 ms (chậm khoảng 1 khung), và ô chữ bị khoét ("s _ e", "_ eam") khi chữ đóng dấu đang bay.
- Cần:
  - bậc theo TYPING_BREAK_STUDY §5.3 mục 1: 2,4× → 1,8× → 1,3× → 1,0× trong 50 ms, nghiêng −8° về 0°; `--tier` cộng thêm như nay;
  - trạng thái đầu đặt bằng JS ngay trong lần `draw()` đọc phím; không chờ animation CSS bắt đầu, không `animation-delay`;
  - chữ gốc luôn hiện, sang màu đã gõ ngay khung phím; bỏ mọi luật làm chữ `.k` trong suốt;
  - chữ cuối lúc gõ xong từ theo cùng luật, để từ còn đọc được khi thẻ nổ;
  - chữ đóng dấu đo được trong kịch bản: phần tử thật, hoặc hộp ghi ở `__td.view()` (A1 và A6 cần);
  - giảm chuyển động: không rơi, như nay.
- Hàm thuần `stampStep(t, tier)` trả `{ scale, tilt, opacity }`.
- Test:
  - t = 0: 2,4 (cộng bậc), −8°, hiện;
  - t = 17: 1,8; t = 33: 1,3; t ≥ 50: 1,0 và 0°; tắt trước 67 ms;
  - đọc `feel.css` và `td.css`: không còn luật nào làm `.k` trong suốt.
- Báo cáo ghi giả thuyết vì sao hôm nay chậm một khung (đọc mã). Claude đo `keyFrames` và tờ `key-dark` trên trình duyệt.

**A6. Kịch bản chụp: sửa, không chạy** (`scripts/visual/scenarios/td-1c-words.mjs`).
- `overHud` và số mới `offScreen` kiểm **mọi khung** trong cửa sổ chụp, không chỉ khung cuối.
- Gồm: thẻ, chữ đóng dấu, nhãn hạng, chữ bay, ×N, mũi chỉ khay (khi là phần tử DOM).
- Ghi số khung vi phạm và tên phần tử. Không đổi các cổng khác.
- Kiểm cú pháp bằng `node --check`.

## Phần B · Ảnh thật thay emoji và chấm CSS (chỉ ảnh đã "Nhận")

**B0. Cổng nhận.**
- Đọc mọi `docs/codex-queue/accept-*/verdict.md` (repo cha). Tìm mục của 133, 165, 172.
- Chỉ dùng ảnh có **Nhận** ở cột kết luận, kể cả "Nhận (sát ngưỡng)" và "Nhận (ngoại lệ …)". "Làm lại", hay chưa có mục chấm: không dùng.
- Không ảnh nào được nhận: bỏ Phần B, ghi vào báo cáo. Phần A vẫn giao.

**B1. Qua danh sách chọn và `art.ts` của phiếu 200.**
- Mọi ảnh vào game qua danh sách chọn và `art.ts` của 200. Không dựng bộ nạp thứ hai. Không ghi đường dẫn ảnh cứng trong `cards.ts`, `debug-2d.ts`, `build-menu.ts`.
- Thêm mục cho ảnh đã nhận theo đúng định dạng của 200. Chép media đúng cách 200 làm (vào `public/assets/typing-defense/ui/…`, hay để Claude chép). Media không vào Git.
- Nguồn (chỉ đọc) trong `games/typing-defense/art-src/`:
  - 133: `ui/calls/call-*.png` và bản thu;
  - 172: `_review/172/delivery-final/`. Không lấy bản thu cũ trong `ui/badges/` (báo cáo 172 §4);
  - 165: `ui/buildings/<id>.v2*.png`, `ui/tray/tray-arrow*.png`, `ui/tray/tray-call*.png`.
- Chọn bản thu theo luật của 200. Không dùng bản thu có ngoại lệ alpha hay sắc khóa ở báo cáo 133 §5 (ví dụ `call-power.64.png` 1,57 %), trừ khi phiếu chấm cho phép.
- Không sửa ảnh, không tạo bản thu mới. Cần cỡ khác thì dùng bản thu lớn hơn gần nhất.

**B2. Icon lời gọi (133) thay emoji.** `callLabel` trả mã ảnh và tên tiếng Anh, không emoji.

| Lời gọi | Hôm nay | Ảnh |
|---|---|---|
| power | 🏹 | `call-power` |
| build | 🔨 | `call-build` |
| harvest | 🌾 | `call-harvest` |
| chop | 🪓 | `call-chop` |
| mine | ⛏️ | `call-mine` |
| quiz | 📖 | `call-quiz` |
| ult ("Spell") | 🔥 | `call-spell` |
| direct ("Stop") | ✋ | `call-interrupt` |
| direct, "Pin" | ⚓ | `call-anchor` |
| direct, "Shatter" | 🛡️ | `call-shield-break` |

- Chỗ hiện:
  - đầu thẻ chữ (thay `.td-card::before { content: attr(data-icon) }`);
  - đầu dòng lời gọi ở `build-menu.ts:82`;
  - bong bóng 2D Low (`debug-2d.ts:608`);
  - dấu thợ 2D Low (`NPC_LETTER` dòng 52 và `⛏️` dòng 537): `call-harvest`, `call-chop`, `call-build`, `call-mine`.
- Cỡ trên thẻ theo phiếu 133: 18 px ở 720p, 24 px ở 1080p.

**B3. Hạt tiến độ (172) thay ●○.**
- Giữ đúng nghĩa hôm nay: một `pip-full` cho mỗi từ lời gọi còn hỏi (gồm từ đang hiện), rồi một `pip-empty` cho mỗi từ đã gõ. Lời gọi một từ: không hạt.
- `pips()` trả danh sách mã ảnh (hay hai số), không trả chuỗi ký tự.
- Cỡ 8 px ở 720p, 12 px ở 1080p (phiếu 172).
- Cả thẻ và bong bóng 2D Low (dòng 588 tính bề rộng theo số hạt, dòng 610 vẽ).
- `pip-gold` chưa có trạng thái trong mã: không thêm luật mới; ghi vào báo cáo.

**B4. Huy hiệu nhãn hạng (172).**
- Nhãn "OK" có `badge-ok`, nhãn "Flash" có `badge-flash`, đặt trước chữ. Chữ tiếng Anh giữ nguyên.
- Cỡ 16 px ở 720p, 22 px ở 1080p.
- Hạng khác (Perfect, Good, Sloppy, Redeemed, hết giờ, hủy) chưa có ảnh: giữ như nay, liệt kê trong báo cáo.
- `badge-calling`, `badge-review`, `badge-chain` không gắn ở phiếu này; báo cáo ghi chỗ đề xuất.

**B5. Khay mép (165).**
- `tray-arrow` thay chữ V hiệu ứng của A2:
  - ảnh DOM, đặt và xoay bằng `trayPointer` của A2;
  - ảnh gốc chỉ sang phải, nên góc 0 là hướng phải;
  - có ảnh thì tắt chữ V của kho hiệu ứng.
- Icon nhà trên thẻ khay (`data-edge` ≥ 0):
  - nhà của lời gọi: `w.calls.b` → id công trình → `buildings/<id>.v2` (`keep`, `archer`, `cannon`, `barracks`, `gold-mine`, `farm`);
  - lời gọi không có nhà (người làng, sách ôn): `tray-call`;
  - đặt ở phía mép; 20 px ở 720p, 28 px ở 1080p;
  - thẻ ngoài khay không có icon nhà.
- 2D Low: mũi tam giác màu ở mép (`debug-2d.ts` dòng 580–585) thay bằng `tray-arrow`, xoay theo góc tới nhà.

**B6. Ảnh chưa nhận ở ngoài.**
- Chỗ nào ảnh chưa được nhận thì giữ như nay (emoji, ●○, chữ V hiệu ứng) và vào danh sách cho phép của test quét.
- Ảnh đã khai mà chưa tải xong: chỗ đó trống, không thay bằng emoji hay hình.

## Test (viết trước)

- `tests/td-c10-r5.test.ts`: A1–A5 như trên.
- `tests/td-card-art.test.ts`:
  - `callLabel` không trả emoji; đủ 10 mã đúng bảng B2;
  - `pips`: 3 từ, đã gõ 1 → full, full, empty; 1 từ → rỗng;
  - hạng → huy hiệu: "OK" và "Flash" có; hạng khác không;
  - thẻ khay → icon nhà theo id công trình; `tray-call` khi không có nhà;
  - mọi mã ảnh mã dùng có trong danh sách chọn của 200 (test đọc danh sách);
  - Phần B bỏ thì chỉ giữ phần test chạy được, ghi lý do.
- `tests/td-no-emoji.test.ts`:
  - quét mọi `.ts` và `.css` trong `src/view/words/`, `src/ui/`, cùng `src/view/debug-2d.ts`, kể cả chú thích;
  - mẫu: `/\p{Emoji_Presentation}|\p{Extended_Pictographic}️|[●○]/u`;
  - danh sách cho phép chỉ gồm mục Phần B còn chờ ảnh: file, ký tự, số phiếu (133, 165 hay 172);
  - mục cho phép mà không còn thấy trong mã thì test đỏ, để danh sách không cũ;
  - ký hiệu chữ khác (★, ▶, ⇧, mũi tên phím) không thuộc mẫu. Báo cáo liệt kê chỗ còn dùng, không sửa.

## Không làm ở phiếu này

- Nền mực hay viền sáng cho ×N ngọc trên cỏ (tương phản 4,5 : 1).
- Đặt chữ son lệch khỏi chữ cần gõ khi phím sai.
- Word Shot: T nhanh hơn, A to hơn, hạ tâm lóe ở 1280.
- Thẻ khay đậu trên một nhà khác.
- Dải tập trung giữa màn (kit TF2).

## Cấm

- Mọi lệnh git có ghi.
- Sửa `src/kit/**`; chạy `kit:sync`.
- Sửa `src/sim/**`, `src/typing/**`, `src/content/**`.
- Sửa `docs/td/BUILD_NOTES.md` (Claude thêm mục khi gộp) và `docs/changelog/README.md` (Claude thêm hàng khi commit).
- Dev server, trình duyệt, mạng; chạy kịch bản `td-1c-words`.
- Đụng worktree khác: `games/.wt-td-1c` (chỉ đọc phiếu chấm trong `tmp/`), `.wt-td-keys`, `.wt-td-codex`, `.wt-td-vfx`, mọi `.wt-dh-*`, `.wt-ts-*`. Đụng game khác hay Tu Tiên.
- Sửa, chuyển, xóa ảnh trong `art-src`; đưa media vào Git.
- Ghi ra ngoài repo. Thêm thư viện.
- Emoji, hình CSS, SVG hay hình canvas để thay ảnh còn thiếu.

## Kiểm (ghi số)

1. `pnpm check` xanh: số test và số file, trước và sau. Test thời gian đỏ khi máy bận thì chạy riêng ba lần.
2. `pnpm td:golden:check`: `"same": true` cả hai.
3. Gói "/" và `?title=0` ≤ 85 kB gzip (dòng `bundle budget`); chunk 3D ≤ 260 kB. Trước và sau.
4. Số dòng `.ts` ngoài kit, trước và sau (trần 16.500 của C0).
5. Bảng năm sửa: hàm, file và dòng, tên test.
6. Test quét: số chỗ tìm thấy; từng mục cho phép và phiếu đang chờ.
7. Bảng Phần B: ảnh, file chấm và dòng, kết luận, bản thu dùng, chỗ gắn. Ảnh không dùng và vì sao.
8. Media đã chép (nếu có): đường dẫn thật trong checkout chính, md5, `git -C games/typing-defense check-ignore -v public/assets/typing-defense/ui/<file>` từng file (trong worktree `ui/` là liên kết, git từ chối đường dẫn đi qua liên kết), và `git -C games/.wt-td-ui check-ignore -v public/assets/typing-defense/ui` cho chính liên kết.
9. `git -C games/.wt-td-ui status --short -uall` và `git diff --stat`, lưu `203/status-after.txt`:
   - chỉ file của phiếu này; file của 200 (nếu chưa commit) ghi riêng;
   - `git -C games/.wt-td-ui diff --quiet -- src/kit src/sim src/typing src/content` thoát 0.
10. Changelog `docs/changelog/<ngày>-c10-fixes-and-card-icons.md` trong worktree: yêu cầu, năm sửa, ảnh đã gắn, số đo, việc còn lại.

## Báo cáo

- Phần A: mỗi sửa một đoạn (hôm nay, đã đổi, test). Giả thuyết chậm một khung (A5). Vì sao mép trái thành chữ "C" (A2).
- Phần B: bảng mục kiểm 7; danh sách còn chờ ảnh.
- Chỗ còn vẽ bằng mã trên thẻ mà phiếu không đụng, để Claude mở phiếu ảnh. Ví dụ: chấm `td-card-dot`, vòng đồng hồ `conic-gradient` của lời gọi trực tiếp, nhãn "Review", hạng chưa có huy hiệu.
- Việc cho Claude:
  - chạy `td-1c-words` ở 1280 × 720 và 1920 × 1080 (High); xem `key-dark`, `key-multi`, `word-dark`, `combo`, `tray-in`, `tray-type`, `tray`;
  - gửi hai giám khảo C10 (mức 8);
  - `media:push` nếu có media mới.

**Rủi ro:**
- Codex không thấy trình duyệt. Sửa cảm giác có thể vẫn trượt giám khảo. Số trong phiếu là mục tiêu; Claude đo lại.
- Phần B chờ Claude chấm nhận 133, 165, 172. Chưa nhận thì Phần B tự bỏ.
- Gói `?title=0` chỉ còn khoảng 1,96 kB. Ảnh đi qua URL; không nhúng base64 vào JS hay CSS.

**Xong khi:**
- Phần A: năm sửa có hàm thuần và test xanh; kịch bản đã sửa và qua `node --check`; kiểm 1–6, 9, 10 có số.
- Phần B: mọi ảnh đã nhận gắn đúng chỗ của B2–B5; ảnh chưa nhận ở danh sách cho phép; kiểm 7, 8 có số. Hoặc báo cáo ghi rõ vì sao Phần B bỏ.
- Có báo cáo. Claude duyệt, chạy `td-1c-words` ở hai cỡ, gửi hai giám khảo (mức C10 8), rồi commit.
