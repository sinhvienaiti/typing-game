# Phiếu 195 · Dragonhold · Báo khi bộ từ lỗi hay thiếu, chặn Low ở bản phát hành, tự tua ×1,75 khi không có chữ

> **Chạy lại (30/10, 10:55, điều phối):** lượt đầu (08:43) bị điều phối cắt giữa chừng khi đổi làn; lượt 09:20 dừng vì thấy chính phần dở đó. Các file sau là **việc dở của chính phiếu này**: `src/app/app.css`, `src/app/deck-boot.ts`, `src/app/idle-speed.ts`, `src/app/quality.ts`, `tests/app/deck-boot.test.ts`, `tests/app/idle-estimate.test.ts`, `tests/app/idle-speed.test.ts`, `tests/app/pinned-deck.test.ts`, `tests/app/quality.test.ts`, cùng các đoạn trong `src/app/app.ts` và `src/app/learning.ts` về khởi động lại bộ từ, chất lượng và tăng tốc lúc không có từ (`fast-forward`). Đọc `git diff`, giữ phần đúng, làm tiếp đến hết phiếu. File chưa commit của 187 và 194 (xem `194-report.md`) cũng là file đã biết; không sửa phần của chúng. File lạ ngoài tập 187, 194, 195 thì dừng.

**Nguồn:**
- `docs/games/MAP1_PRODUCTION.md` §1.2 mục 2 (DH-02 · P0 · G7): "Bộ từ rỗng mà người chơi không được báo … không vào đợt". Luật ngôn ngữ 28/10 trong `AGENTS.md` thay chữ "thông báo tiếng Việt" của MAP1: bảng báo viết tiếng Anh.
- Cùng mục, mục 10: DH-18 gộp vào DH-15, "không cho chọn Low, và `?q=low` ở bản production dùng Medium". Bảng Settings là việc của phiếu 192. Phiếu này chỉ làm luật chất lượng.
- Mục 12 và §5.3 "Bước 0 (DH-05), không đổi sim". Chủ dự án đồng ý ngày 28/10, khoảng 19:45 (`docs/HANDOFF_CURRENT.md` §5). Số đo G3: 52,4 % thời gian đợt không có chữ.
- Chủ dự án 29/10: "tăng thêm việc cho codex cho tôi". DH-02 và DH-05 vốn ở làn T, R của Claude. Chủ dự án giao theo đề xuất của Claude.

**Báo cáo:** `docs/codex-queue/195-report.md` (tiếng Việt), thư mục `docs/codex-queue/195/`.

**Ngoài phiếu (Claude làm):** bỏ alias `/vocabulary/`, `/typing-texts/` trong `infra/nginx` (nửa sau của DH-02); đo trên trình duyệt.

## Luật chung (phiếu mã)

- **Nơi làm:** worktree `games/.wt-dh-codex`, nhánh `dh-codex`, chạy sau phiếu 194 trên cùng nhánh (cần `docs/codex-queue/194-report.md`; thiếu thì dừng, ghi vào báo cáo). cwd của làn là repo cha (`.`), vì mục Việc 11 sửa tài liệu ở repo cha. Chạy `pnpm` trong thư mục worktree.
- Lúc bắt đầu lưu `git status --short -uall` của worktree vào `195/start-status.txt` và `git status --short` của repo cha vào `195/parent-status-before.txt`.
- Kiểm `git status` trước khi làm. Chỉ được có file của 187 hay 194 mà Claude chưa commit. Có thì làm tiếp trên đó và ghi danh sách file vào báo cáo. Có file lạ thì dừng.
- Được dùng git chỉ đọc.
- Test trước, mã sau. Chú thích tiếng Anh. Chữ người chơi thấy là tiếng Anh.
- Luật chơi không đổi. Ván vàng và bot đo theo tick, nên phải giữ nguyên.
- Làn V-dh2 (`.wt-dh-vfx`) đang sửa vùng khung, `timeScale`, hit-stop và `optionsFromUrl` của `app.ts`. Để bớt xung đột khi gộp: logic mới nằm trong file mới; `app.ts` chỉ thêm vài dòng nối. Báo cáo ghi rõ các dòng đã đổi trong `app.ts`.

## Đọc trước

- `src/app/learning.ts`: `buildDeck` (khoảng dòng 314–350). Lỗi tải hiện chỉ `console.warn` (khoảng 320–323).
- `src/app/app.ts` (số dòng ở `dh-codex` hôm nay, sẽ lệch chút):
  - `QUALITIES` (76), `WORD_ZONE_U` (88), `optionsFromUrl` (91), chọn quality trong `startApp` (khoảng 188);
  - `ffBadge` (243); `fastForwardAllowed`, `fastForwardRefusal`, `fallback` (698–728);
  - phần cuối hàm khung (khoảng 812–842), `timeScale` (864–869), boot (871–910), `__dh.state()` (khoảng 950).
- `src/sim/words.ts`: `inWordZone` (848), `ZONE_U`. `src/sim/lanes.ts`: `pointAt`. `src/sim/movement.ts`: quái bay, sky lane. `src/sim/fixed.ts`: `TICK_HZ` (60).
- `src/typing/deck.ts` `buildWordDeck`. `LEARNING.deckSize` = [70, 100] trong `src/content/rules.ts` (01 §6.1).
- `src/app/portal.ts` `portalHome`; nút "Back to portal" ở `src/ui/results.ts` (phiếu 187).
- `docs/codex-queue/194-report.md`: cách nạp icon HUD. Ảnh `fast-forward` của phiếu 137, J2 nhận ngày 29/10 (M 8, Q 9).
- `docs/games/IN_GAME_SETTINGS.md` §3, hàng Graphics.
- Số đo thật, chỉ đọc, ở checkout chính:
  - `games/dragon-hold/tmp/map1-audit/feel-35-1280/idle.json` (tóm tắt);
  - `games/dragon-hold/tmp/map1-audit/feel-35-1280/samples.json`: mỗi 100 ms một dòng `[ms, phase (2 = wave), wave, words, visibleWords, liveFoes, hp]`;
  - cách tính cũ: `games/dragon-hold/tmp/map1-audit/scen/idle-samples.mjs`.

## Việc A · Bộ từ lỗi hay thiếu (DH-02), không Low ở bản phát hành (DH-18)

1. **`buildDeck` báo lý do.**
   - Bộ hỏng khi: tải lỗi; tải được mà không có mục nào; bộ dựng ra ít hơn `LEARNING.deckSize[0]` (70 từ).
   - App nhận được lý do (`"load-failed"`, `"empty"`, `"too-small"`) và số từ. Giữ `console.warn`.
   - Bộ đủ thì cách chọn từ không đổi.
2. **Bảng báo, không vào đợt.** Khi bộ hỏng:
   - dòng "loading words…" nhường chỗ cho một bảng. Tiêu đề "Words could not load". Dòng phụ theo lý do: "Check your connection and try again." hay "Not enough words arrived for this stage.";
   - nút "Retry". Nút "Back to portal" chỉ hiện khi `portalHome(import.meta.env.VITE_PORTAL_URL)` có giá trị, trỏ như nút ở màn kết quả;
   - không tạo `run`, không chạy vòng lặp, không mở thẻ tốc độ. Không đợt nào bắt đầu;
   - dùng khung bảng đang có của game (lớp `dh-panel` như menu dừng). Không thêm hình vẽ bằng CSS, SVG hay emoji;
   - đi được bằng phím: focus sẵn ở Retry, `Enter` bấm, `Tab` hay `←` `→` đổi nút. `role="alertdialog"` có `aria-labelledby`. Bảng tự nghe phím (router chưa có lúc này) và gỡ listener khi đóng.
3. **Retry** gọi lại `buildDeck(stage)`.
   - Đang tải: nút mờ, chữ "Loading words…".
   - Được: bảng đóng, boot chạy như thường đúng một lần (một router, một loop).
   - Lỗi nữa: bảng hiện lại, nút dùng lại được.
4. **Chất lượng theo bản build.** File mới `src/app/quality.ts`:
   - `allowedQualities(prod: boolean)`: bản phát hành `["medium", "high", "ultra"]`; bản dev thêm `"low"`;
   - một hàm đưa giá trị về mức cho phép: `low` ở bản phát hành thành `medium`;
   - `optionsFromUrl` dùng hàm đó: `?q=low` ở bản phát hành ra `medium`, ở dev giữ `low`. Giá trị lạ vẫn ra `undefined`;
   - phiếu 192 (nhánh `dh-keys`) có thể liệt kê Low ở Settings. Nhánh nào gộp sau thì dùng `allowedQualities`. Ghi điều này vào báo cáo. Không sửa nhánh `dh-keys`.

## Việc B · Tự tua ×1,75 khi không có chữ (DH-05 bước 0)

5. **Hàm thuần** `idleSpeedUp(world)` trong file mới `src/app/idle-speed.ts`. Không đọc DOM, không đổi `world`. Đúng khi đủ ba điều:
   - `world.phase === "wave"`. Pha `prep`, `warning`, `break`, `victory`, `defeat` luôn sai: lúc nghỉ là lúc người chơi mua, đặt, ôn;
   - không còn chữ sống (`world.words.live` toàn `null`);
   - không quái sống nào đang ở hay sẽ vào Vùng Chữ trong 1,5 s tới (90 tick).
   Cách xét điều thứ ba:
   - đẩy `along` thêm `enemy.speed × 90`, không quá `stopAt`; lấy vị trí bằng `pointAt`; xét đúng phép của `inWordZone` (vòng 26 m và luật T_a theo `world.pace`);
   - quái đang đánh hay bị chặn trong vòng 26 m tính là đã vào;
   - dùng tốc độ gốc `enemy.speed` kể cả khi quái bị làm chậm hay đóng băng. Tắt sớm thì được, tắt muộn thì không;
   - quái bay đi trên sky lane: đọc `movement.ts`, xét đúng cách sim đặt nó;
   - quái chưa xuất hiện: đọc dữ liệu đợt của map 1. Có điểm xuất hiện chạm Vùng Chữ trong 1,5 s thì tính cả quái sắp ra. Không có thì ghi khoảng cách gần nhất vào báo cáo.
   Được tách một hàm thuần từ `inWordZone` (ví dụ `inWordZoneAt(world, enemy, along)`) để dùng chung, miễn `inWordZone` cho kết quả y hệt. Không sửa luật nào khác trong `src/sim/**`.
6. **Nối vào app.**
   - `timeScale` = hit-stop × (tay ? 2 : tự ? 1,75 : 1) × `speed`.
   - Tự tua bật khi hàm đúng liên tục 0,3 s (khỏi nháy dấu). Tắt ngay ở khung có chữ sống đầu tiên, hay khi hàm sai.
   - Luôn ×1 khi có bảng mở, đang đặt hay sửa (`run.placement.mode !== "idle"`), đang dừng hay đếm 3-2-1.
   - Chỉ đổi số bước sim mỗi khung, như đường ×2 đang có. Không đổi tốc độ hay cao độ nhạc. Không đổi đồng hồ VFX.
7. **Alt + → giữ nguyên.** Vẫn bật, tắt ×2 theo luật cũ (`fastForwardAllowed`, câu từ chối cũ). Khi ×2 bật thì ×2 thắng, không nhân dồn với ×1,75.
8. **Dấu ».**
   - Ô chữ "×2" (`ffBadge`) đổi thành ảnh `fast-forward`, nạp theo cách của phiếu 194, kèm số nhỏ "×1.75" hay "×2".
   - `aria-label` tiếng Anh: "Fast forward ×1.75: no words on screen" và "Fast forward ×2". Không đặt `aria-live` (khỏi đọc liên tục).
   - Bảng `src/ui/ui-art.json` của 194 đã có mục `fast-forward` (194 chỉ chuẩn bị, chưa gắn). Dùng `icon("fast-forward")` của 194. Nếu bảng thiếu mục này thì thêm đúng cách 194 làm. Không làm được thì dừng bước này và ghi lại. Không thay bằng ký tự, CSS, SVG hay emoji.
9. **Cho Claude đo:** `__dh.state()` thêm `idleSpeed` (bool) và `timeScale` (số của khung gần nhất).
10. **Script ước tính** `scripts/balance/idle-estimate.mjs <samples.json>`: Node, không mạng, đường dẫn qua tham số, không ghi gì cạnh file nguồn.
    - "Trước": tính lại như `idle-samples.mjs`. Phải ra 52,4 % như `idle.json`.
    - "Sau": mỗi quãng không chữ trong pha wave dài g giây giữ nguyên khi g ≤ 1,5; dài hơn thì thành `1,5 + (g − 1,5) / 1,75` (1,5 s cuối trước chữ chạy ×1).
    - Bảng nhạy: tầm nhìn 0; 0,5; 1,0; 1,5 s, nhân với tốc 1,75 và 2.
    - Ghi rõ giả định: mẫu không có vị trí quái, nên lấy "chữ hiện" thay cho "quái vào Vùng Chữ".
    - Claude tính nhanh ngày 29/10 theo mô hình này: khoảng 47,8 %. MAP1 §5.3 ghi khoảng 39 %; đó là số khi tua cả quãng (tầm nhìn 0 ra 38,6 %). Báo cả hai. Không sửa MAP1.
    - Đầu ra: `docs/codex-queue/195/idle-estimate.json` và một bảng trong báo cáo.
11. **Sửa tài liệu** `docs/games/dragon-lane/06-other-systems.md` §10 (repo cha), tiếng Việt, câu ngắn:
    - thêm hàng "Tự tua × 1,75": điều kiện, dấu », về ×1 khi có chữ, Alt + → thắng, không đổi sim, chủ dự án đồng ý 28/10 (MAP1 §5.3 bước 0);
    - hàng "Tua nhanh × 2" giữ nguyên, thêm "thắng tự tua".

## Test (viết trước)

- Loader ném lỗi: bảng hiện, không có `run`, không có `wave-start`.
- Loader trả mảng rỗng; bộ giả 69 từ: bảng hiện với đúng lý do.
- Retry: lần hai được thì bảng đóng và boot đúng một lần; lần hai lỗi thì bảng còn.
- "Back to portal": ẩn khi biến trống; hiện và đúng `href` khi có biến.
- Bộ ghim thật (`public/vocabulary`): mọi cấp 1–100, `excludeMature` bật và tắt, khởi đầu lạnh, đều dựng ≥ 70 từ. Cấp nào dưới 70 thì không tự hạ ngưỡng: ghi cấp và số, dừng Việc A, để Claude chọn.
- `optionsFromUrl("?q=low", false)` ra `medium`; `optionsFromUrl("?q=low", true)` ra `low`; `allowedQualities(true)` không có `low`.
- Hàm tự tua:
  - quái ở biên 1,5 s (89, 90, 91 tick);
  - quái bay; quái đang đánh trong vòng; quái đóng băng; quái đã chết;
  - có một chữ sống;
  - từng pha `prep`, `warning`, `break`, `victory`, `defeat`.
- `timeScale`: tự ×1,75; tay ×2 thắng; nhân đúng với hit-stop và `speed`; bật sau 0,3 s; về ×1 ngay ở khung có chữ.
- Nếu tách `inWordZoneAt`: chép nguyên văn `inWordZone` cũ vào test, so với bản mới trên mọi quái ở mọi tick của một ván vàng. Phải giống hệt.

## Cấm

- Mọi lệnh git có ghi. Sửa `src/kit/**`; chạy đồng bộ kit.
- Dev server, trình duyệt, mạng. Ghi ra ngoài repo.
- Đổi luật sim; chạy `dh:golden:update`; sửa `tests/golden/**`.
- Đụng worktree khác (`.wt-dh-vfx`, `.wt-dh-keys`, `.wt-dh-models`, `.wt-dh-mappilot`, `.wt-td-*`, `.wt-ts-*`), game khác, Tu Tiên.
- Ghi vào `games/dragon-hold/tmp/**` (chỉ đọc).
- Sửa `infra/nginx`.
- Tạo ảnh mới; đưa ảnh hay âm vào Git.
- Chữ tiếng Việt người chơi thấy, trừ tên riêng Hỏa Long, Bạch Long.

## Kiểm (ghi số)

1. `pnpm check` xanh: số test trước và sau. Test thời gian đỏ khi máy bận thì chạy riêng ba lần.
2. Ván vàng: `tests/golden/m0.json` không đổi. Test bot trong `tests/sim/` xanh.
3. `pnpm dh:balance --seeds=20 --json=../../docs/codex-queue/195/balance.json` chạy một lần. Ghi G1, G3, G5, G6, G8 vào báo cáo để Claude so với `main`.
4. `pnpm deploy:pack`: 0 lỗi. Lưu đầu ra JSON vào `195/`.
5. `tests/english-ui.test.ts` qua (nằm trong check; ghi riêng số test).
6. Script ước tính: trước 52,4 %, sau, bảng nhạy.
7. `git status --short -uall`:
   - worktree: chỉ file của phiếu này, test, script và `docs/changelog/<ngày>-deck-notice-and-idle-speed.md` (ghi DH-02, DH-18, DH-05 đã sửa); cộng file 187, 194 chưa commit, liệt kê riêng;
   - repo cha: so với `195/parent-status-before.txt`, chỉ thêm `docs/games/dragon-lane/06-other-systems.md` và `docs/codex-queue/195*`.

## Rủi ro

- Xung đột khi gộp với `dh-vfx` ở `timeScale` và `optionsFromUrl`. Giữ phần nối trong `app.ts` ngắn, ghi dòng.
- Tốc độ đổi giữa trận không được làm lệch âm hay VFX. Nếu thấy chỗ nào hẹn giờ theo thời gian sim mà phát theo thời gian thật (hay ngược lại), ghi vào báo cáo, không tự sửa ngoài phạm vi.

**Xong khi:** mười một mục việc, các test và bảy mục kiểm đạt. Claude duyệt diff, đo trên trình duyệt ở 1280 và 1920 (phần thời gian không chữ thật, cảm giác tua, âm và VFX không lệch), rồi commit.
