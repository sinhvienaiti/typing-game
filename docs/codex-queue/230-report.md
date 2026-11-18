# Phiếu 230 · Last Line · Kiểm lại độc lập 206 và 220

Ngày 30/10/2026, 15:22–15:47. Claude (Opus) làm thay Codex theo lệnh chủ dự án 15:25 ("dừng Codex, giao Claude"); phiếu ghi model `gpt-6.1-sol` nhưng lượt này không dùng runner Codex. Chỉ đọc hai worktree. Mọi lệnh `pnpm`, `node` chạy trong bản chép `games/typing-survival/tmp/codex-230/`. Không commit, không sửa mã.

## Bảng tổng

| Phiếu | Kết luận | P0 | P1 | P2 | P3 |
|---|---|---:|---:|---:|---:|
| 206 · ảnh UI (`.wt-ts-art`, `ts-art`, HEAD `79db628`) | **Commit được** sau lượt trình duyệt 1280/1920 mà phiếu 206 vốn đòi. Nên sửa P2 trong cùng lượt. | 0 | 0 | 2 | 3 |
| 220 · luật bến đầy (`.wt-ts-codex`, `ts-codex`, HEAD `ba6d70e`) | **Commit được** (núm mặc định tắt, tắt thì không đổi byte nào). Chưa áp luật nào, đúng khuyến nghị của 220. | 0 | 0 | 2 | 1 |

Mọi số của hai báo cáo chạy lại đều khớp. Không thấy lỗi chặn. Các P2 chủ yếu là lỗ test: đột biến ở chỗ gắn ảnh và ở nhánh băng thứ ba không làm test nào đỏ.

## 1. Mốc và bản chép

- `preflight.txt`: đủ hai báo cáo; `ts-art` ở `79db62851e00…`, `ts-codex` ở `ba6d70e9d697…`. Status hai worktree trùng từng dòng với `206/status.log` (20 đường) và `220/evidence/worktree-status-after.txt` (8 đường). Không có đường lạ.
- Điều 4: lượt 14:44 bị cắt. Theo ghi chú chạy lại, đã xóa `tmp/codex-230/` và `230/` cũ rồi làm lại từ đầu. Không xóa gì khác.
- Mốc `marker` tạo trước khi chép. `snapshot-before.json`: 311 file (art), 288 file (codex), kèm SHA-256, mục `node_modules` cấp 1 và mtime `results.json` của Vitest.
- Bản chép dựng theo mục "Dựng bản chép" của 224. `copy.json`: art 311/311, codex 288/288 SHA-256 trùng; mỗi bản 11 symlink, `node_modules` là thư mục thật.
- Thêm ba bản chép phụ, cũng trong `tmp/codex-230/`: `art-head` (mã `HEAD` của `ts-art`, 251/251 blob trùng index, `art-head-copy.json`), `art-mut` và `codex-mut` (chỉ để làm đột biến).

## 2. Số chạy lại so với số báo cáo

| Kiểm | Báo cáo nói | Đo lại | Khớp |
|---|---|---|---|
| 206 · `pnpm check` | 24 file / 225 test, kit 61/61 | 24 / 225, kit 61/61, mã 0, 12,4 s | có |
| 206 · `pnpm check` mã `HEAD` (trước 206) | 22 / 206 | 22 / 206, mã 0 | có |
| 220 · `pnpm check` | 27 / 317, kit 61/61 | 27 / 317, kit 61/61, mã 0, 12,35 s | có |
| Golden `s0-trace.json` | md5 `eeaf2767…`, SHA-256 `42e4e5a9…` | hai bản chép: đúng cả md5 và SHA-256; `HEAD` của hai nhánh: đúng SHA-256 | có |
| 152 hash chương | trước = sau | 152 dòng ở art và codex; trùng byte `206/chapter-hashes-*`, `220/chapter-*` | có |
| 206 · `ui-art:prepare` lần chạy lại | 0 file ghi, 0,639 s | 0 file ghi, 0,684 s và 0,653 s | có |
| 206 · `--check` | mã 0 | mã 0, "UI art check: OK" | có |
| 206 · thiếu `--art-src` | mã 2 | mã 2, lời nhắc đúng đường | có |
| 206 · dựng lại toàn bộ từ nguồn vào `tmp/rebuild` | 49 WebP, 2.769.208 B | 49/49 md5 trùng manifest, bảng chạy trùng byte, 25 s | có |
| 206 · byte theo cỡ, PSNR nhỏ nhất | 64: 30.474 … 1536: 1.718.924; icon 35,126, portrait 35,2698, stage 26,7384 dB; 6 lossless, 16 q92 | đúng từng số | có |
| 206 · `--pending` | 21 vai, 61 WebP, 8.625.740 B | 21 / 61 / 8.625.740 B; 61/61 file trùng byte `206/pending.json` | có |
| 206 · byte ảnh từng màn (DPR 1 / 2) | 8 màn trong `bytes-per-screen.json` | tính lại từ HTML thật của `screens206()` và `artAttrs`: 8/8 màn trùng; lớn nhất 408.154 B (trước trận, DPR 2) | có |
| 206 · `deploy:pack` | mã 1, 2 lỗi (`foreign-asset`, `local-host`), như trước | 206: mã 1, đúng 2 lỗi đó; `HEAD`: mã 1, cùng 2 lỗi. `dist` 101 file (HEAD 51): thêm 49 WebP + manifest | có |
| 206 · chữ không đổi | golden `ui-text-206.json` ghi từ mã cũ | chạy `screens206()` trên mã `HEAD`: 9/9 màn trùng golden | có |
| 220 · tái tạo V6 và bốn ứng viên, `c1-s1`, seed 1–100 | JSON trùng 209/220 | `v6`, `f1`, `f2`, `f3`, `f4`: 5/5 JSON trùng SHA-256 `220/runs/*-s1.json`; MD chỉ khác dòng thời gian "cả lệnh … s"; `.err` cùng dòng `--set` | có |
| 220 · F4 seed 101–200 | — | `f4-s101.json` trùng SHA-256 220 | có |
| 220 · V0 `c1-s1` seed 1–100 (sau mã) | `x-v0` phần `c1-s1` trùng 209 | `v0-s1.json` trùng SHA-256 `209/runs/v0-s1.json` (`d5fa479d…`); 36/36 ô trùng phần `c1-s1` của `x-v0-s1.json` | có |
| 220 · F4 bốn ải seed 1–100 | `x-f4-s1.json` | `x-f4-s1.json` (144 ô) trùng SHA-256 220; MD chỉ khác dòng thời gian (717 s so với 831 s) | có |
| 220 · `summary.json`, `summary.md` | sinh bằng `220/tools/summarize.mjs` | chạy lại trên bản chép: SHA-256 trùng cả hai | có |
| 220 · số trong bảng báo cáo (seed 1–100) | ví dụ F4: I Khá/Nhanh 1,2/0,7; B3 85/88; B6 +11/+34; TT +7 | tính thẳng từ JSON mới: đúng cho V0, V6, F1–F4 (`metrics-s1.json`) | có |

Thời gian đo: 6 báo cáo `c1-s1` chạy 4 cùng lúc (192–224 s mỗi báo cáo), rồi `f4-s101` và `x-f4-s1` chạy 2 cùng lúc (`timeline.jsonl`). Tải 1 phút lúc mở đợt đầu 8,14; có lúc lên 28,9 khi bộ đột biến chạy cùng `x-f4-s1`. `nice -n 15` chạy được (0 dòng `setpriority`); `.err` chỉ có dòng `--set`, giống 220 khi bỏ dòng `setpriority` của 220. Mọi lệnh đo mã 0.

## 3. Phiếu 206 · đọc diff

| Yêu cầu của 230 | Kết quả | Bằng chứng |
|---|---|---|
| Đúng phạm vi phiếu | Đạt | 20 đường, đúng danh sách Kiểm 12 của 206, thêm `tests/ui-art-fixtures.ts` (test mới). `main.ts` +2/−2, `hud.ts` +13/−1. `git diff --check` mã 0; file mới không lỗi khoảng trắng. |
| Không vẽ bằng mã thay ảnh | Đạt | Dòng thêm: 0 `url(`, 0 `canvas`, 0 `getContext`, 0 `<svg` trong mã (1 lần trong test kiểm "không có `<svg`"). Hai `gradient` là màn che `--veil` cũ dời xuống `::before` khi có nền; không phải hình thay. `⚠`, `★☆` có sẵn, giữ nguyên. Không `filter`, `opacity`, `mix-blend-mode`, `border-radius` trên `.sv-art`. |
| Ảnh chưa nạp thì trống | Đạt | `<img>` có `width`, `height`, `alt=""`, không nền, không khung. Vai chờ trả chuỗi rỗng. Ảnh lỗi: `watchArt` đặt `hidden`, mọi luật `display` của ảnh nằm trong `:not([hidden])`. Nền đang nạp: `::before` vẫn vẽ màn che như cũ. |
| Không media trong Git | Đạt | `ls-files`: 0 file ảnh, âm, model; file chưa theo dõi: 0. `check-ignore`: WebP và `manifest.json` bị `.gitignore:11 public/assets/**`; `src/view/ui-art.json` không bị bỏ qua. |
| Chữ người chơi thấy là tiếng Anh | Đạt | Golden từ mã `HEAD` trùng 9/9 màn. `alt` đều tiếng Anh, không dấu Việt. Không thêm chữ mới. |
| Gói khởi động trong ngân sách | Đạt | Ngân sách của phiếu: mỗi màn ≤ 1 MB ở DPR 2. Lớn nhất 408.154 B. Màn chính 0 B (nền 121 còn chờ). JS chính 340.056 → 344.803 B (+4.747; gzip 121,33 → 123,12 kB), CSS 53.202 → 55.854 B (+2.652). |

12 chỗ gắn LL và 5 điểm gắn nền đều đúng vị trí phiếu ghi (đọc từng dòng diff). `BOX`, `pick()`, `artHtml`, `artAttrs`, `watchArt` đúng mục 4 của 206.

Đột biến 206 (bản chép `art-mut`, `mutations-206.json`):

| Mã | Sửa | Test đỏ khi sửa |
|---|---|---|
| A1 | `hud.ts`: bỏ dòng gắn icon bến (LL-39) | 0 / 225 |
| A2 | `hud.ts`: bỏ chân dung thẻ ra mắt (LL-35) | 0 / 225 |
| A3 | `hud.ts`: bỏ `watchArt(root)` | 0 / 225 |
| A4 | `main.ts`: bỏ `art` của nút "Stage n" (LL-53) | 0 / 225 |
| A5 | `main.ts`: trận thử truyền `stage: "s0"` | 0 / 225 |
| A6 | `ui-art.ts`: 1x lấy `box` thay `box × 1,5` | 2 / 33 |
| A7 | CSS: `.sv-art-briefing { display: block }` không còn `:not([hidden])` | 0 / 225 |
| A8 | `ui-art.ts`: ảnh lỗi không `hidden` | 1 / 33 |

Mỗi lần trả file, SHA-256 trùng worktree, test xanh lại. Phiếu 206 chỉ đòi test `artAttrs` cho HUD (test 9) và fixture truyền thẳng `art`, `stage`, `guns`, nên phần nối trong `hud.ts`, `main.ts` và luật `[hidden]` chỉ có kịch bản trình duyệt canh.

## 4. Phiếu 220 · đọc diff

| Yêu cầu của 230 | Kết quả | Bằng chứng |
|---|---|---|
| Ba ứng viên sau `FULL_BAY`, mặc định tắt | Đạt | `src/content/guns.ts:20` `{ extra: 0, spill: 0, boost: 0 }`, không `as const`, không `freeze`. Luật đọc núm lúc gọi (`weapons.ts:27,108,120,129,145`). |
| Tắt thì hash và golden giữ nguyên | Đạt | 152 hash chương trùng byte; golden trùng; V6, V0 và bốn ứng viên ở `c1-s1` cho JSON trùng SHA-256 với 209/220. |
| Chỉ ải chương | Đạt | `chapter > 0` ở `weapons.ts:27`, `:108`, `:120`. Đột biến M1, M2, M3 bỏ từng điều kiện: 3, 2, 2 test đỏ. |
| Dấu "đã tăng" ngoài hash | Đạt | `weapons.ts:61` `fullBay: { boosted }` lồng; `hash.ts:23` chỉ trộn typed array và số tầng đầu. Thử thẳng: đặt dấu thì `hashWorld` không đổi (975820000); đổi `damage` thì đổi. Thêm một typed array tầng đầu (M14) thì 152/152 hash chương đổi. |
| `world.ts:119` đúng một dòng | Đạt | numstat `1 1`: `createGuns(header.kit, stage.chapter)`. |
| Test bắt đột biến | Đạt phần lớn | 16 đột biến, 13 làm test đỏ (bảng dưới). |
| Phạm vi ghi | Đạt | `words.ts` chỉ trong `finish` (`:257–258`); `pace.ts` chỉ import, JSDoc, vòng `live`; `typist-bot.ts` chú thích 16–18, `options()`, một import và `bayValue`. Không sửa view, app, kit, golden, scripts. Không thêm loại `EV`. |

Đột biến 220 (bản chép `codex-mut`, `mutations-220.json`; cột cuối là số test đỏ trên số test chạy):

| Mã | Sửa | Đỏ |
|---|---|---|
| M1 | R1 bỏ điều kiện ải chương | 3 / 21 |
| M2 | R2 bỏ điều kiện ải chương | 2 / 21 |
| M3 | R3 bỏ điều kiện ải chương | 2 / 21 |
| M4 | mặc định `boost: 0.3` | 7 / 317 |
| M5 | mặc định `spill: 1` | 5 / 317 |
| M6 | `nextMagazine` không dời dấu | 1 / 21 |
| M7 | `loadMagazine` không xóa dấu | **0 / 21** |
| M8 | R3 trước R2 | 1 / 21 |
| M9 | hòa thì chọn bến số lớn | 1 / 21 |
| M10 | `flowSnapshot` bỏ R3 | 1 / 21 |
| M11 | giá trị bot bỏ R3 | 1 / 21 |
| M12 | R2 không phát `EV.load` | 2 / 21 |
| M13 | trả `world.ts:119` về cũ | 5 / 21 |
| M14 | thêm typed array tầng đầu vào `guns` | **0 / 317** (152/152 hash chương đổi) |
| M15 | R2 bỏ kiểm `gun < 0` | 0 / 21 (đột biến tương đương: bến trống luôn có `cap` 0) |
| M16 | R3 nhân `1 + 2 × boost` | 3 / 21 |

## 5. Phát hiện

| Mã | Phiếu | Mức | file:dòng | Tái tạo | Đề xuất sửa |
|---|---|---|---|---|---|
| 230-F1 | 206 | P2 | `src/view/hud.ts:176`, `:413`, `:134`; `src/app/main.ts:262`, `:306` | Bỏ từng dòng gắn ảnh (A1–A5): 225/225 test vẫn xanh. | Thêm test chuỗi đọc nguồn `hud.ts`, `main.ts` (như `tests/english-ui.test.ts`), hoặc tách `items("end")`, `view("intro")` ra hàm thuần rồi test. |
| 230-F2 | 206 | P2 | `src/view/survival.css:281–313` | A7: bỏ `:not([hidden])` ở luật `display` của băng thẻ ải, 225/225 vẫn xanh; ảnh lỗi khi đó vẫn chiếm chỗ. | Thêm test CSS: mọi luật `.sv-art-*` hay `.sv-bg` có `display` hay `position` phải nằm trong `:not([hidden])`. |
| 230-F3 | 206 | P3 | `public/assets/typing-survival/ui/manifest.json` (vào `dist/`) | `deploy:pack` chép manifest 18.029 B vào `dist`; trong đó có tên file `art-src` (`ui/icons/gun-xung.norm.64.png`…), `sourceMd5`, PSNR. Game không đọc file này. | Bỏ manifest khỏi gói (lọc khi pack) hoặc chuyển ra ngoài `public/`. |
| 230-F4 | 206 | P3 | `AGENTS.md:93` | Dòng mới viết tiếng Việt giữa phần Layout tiếng Anh. | Viết lại bằng tiếng Anh. |
| 230-F5 | 206 | P3 | `scripts/ui-art/prepare.mjs:176` | Ngưỡng 35 dB không với tới được cho ảnh ải bằng WebP có mất mát: thử `c1-s1` ở 768 px, q84 30,24 dB, q92 31,03 dB, q100 31,44 dB, q92 `-sharp_yuv` 32,22 dB; chỉ lossless qua. 16/16 file ải ở q92 vẫn dưới 35 dB (nhỏ nhất 26,74). | Chấm ảnh ải bằng mắt (đã có trong việc của Claude). Nếu muốn giữ ngưỡng số thì cần quyết định: `-sharp_yuv`, lossless cho cỡ nhỏ, hay ngưỡng riêng cho `stage`, `bg`. |
| 230-F6 | 220 | P2 | `src/sim/weapons.ts:135`, `src/sim/words.ts:257` | `loadMagazine.fullBayWord = fullBayWord` gắn hàm làm thuộc tính của hàm khác, chỉ để giữ nguyên dòng import của `words.ts` (phiếu chỉ cho sửa trong `finish`). Chạy đúng, tsc qua, nhưng là ghép ngầm. | Khi commit: `words.ts` import thẳng `fullBayWord`, bỏ dòng 134–135 của `weapons.ts`. Cần Claude cho phép sửa dòng import. |
| 230-F7 | 220 | P2 | `tests/full-bay.test.ts:103–122` (test R3) | M7: `loadMagazine` không xóa dấu, 21/21 vẫn xanh. Test chỉ dùng bến 2 băng; `nextMagazine` dời qua cả 3 ô nên ô cuối luôn nhận 0. Với bến 3 băng (Rèn cấp 3, hay R1 + R3), ô 2 giữ dấu cũ; bỏ dòng xóa thì băng mới nạp vào ô 2 bị coi là đã tăng. | Thêm ca `levels: [3, 1]` (hay `extra=1` cùng `boost=0.3`): tăng ô cuối, `nextMagazine`, nạp lại, kiểm `canBoost` là `true`. |
| 230-F8 | 220 | P3 | `tests/` (không có test ghim hash chương) | M14: 152/152 hash chương đổi mà 317/317 test xanh. `tests/s0-trace.test.ts:12` ghim hash sự kiện, không ghim `hashWorld`. Bất biến "tắt thì hash giữ nguyên" chỉ có `scripts/chapter-hashes.ts` chạy tay canh. | Nếu chọn R3 (đưa dấu vào hash), ghim 152 hash vào một test golden trong cùng phiếu. |

Ghi chú, không tính phát hiện: R3 hạ I Khá từ 14,9 % xuống 1,2 % phần lớn vì định nghĩa `live` mới (bến đầy chưa tăng được tính là có từ hữu ích); 220 đã nói rõ. Người chơi chưa thấy R3 (không sự kiện, view vẫn hiện `FULL`), nên số I của F4 chỉ có nghĩa sau khi có phần view mà 220 liệt kê.

## 6. Cần trình duyệt của Claude

Chạy `scripts/visual/scenarios/survival-ui-art.mjs` trên dev server của `ts-art`, ở 1280 × 720 và 1920 × 1080:

1. **Thẻ ải** `c1-s1` và `c1-s4` ở 720p: thẻ có cuộn dọc không (ước lượng `c1-s4` sát 94vh). Băng ảnh rộng cố định `760px × --ui` với lề âm 26 px: nếu thẻ hiện thanh cuộn dọc kiểu chiếm chỗ, băng sẽ tràn ngang đúng bề rộng thanh cuộn. Khi đó đổi bề rộng băng sang theo thẻ (`calc(100% + 52px * var(--ui) + 2px)`).
2. **Nạp súng** 720p: năm thẻ thêm khối icon 72 px; thẻ còn trọn trong 94vh, tên súng một dòng.
3. **Hành trình**: hàng ải cao thêm vì ảnh 96 × 54; hàng khóa mờ theo `.is-off`.
4. **Bến trong trận**: icon 40 px trên mép bến (1, 3 trái; 2, 4 phải), không chồng `.sv-strip`, không đè mũi súng. Bến `.is-dim` làm icon mờ 72 % theo luật cũ `.sv-slot.is-dim > *`.
5. **Thẻ ra mắt quái**: cao thêm vì chân dung 48 px, không che HUD trên.
6. **Trước trận** (ảnh ải 384 × 216 và icon súng) và **kết quả** (nút "Stage 2" có ảnh).
7. **Chớp ảnh**: `drawScreen()` thay `innerHTML` mỗi lần đổi chọn ở nạp súng; xem có chớp không.
8. **Console**: chỉ cảnh báo `no accepted image` của vai chờ (nền 121 ở các màn đi qua, `foe-shard`), 0 "missing image", 0 lỗi. Kịch bản không vào màn kết quả và không vào thẻ ải `c1-s4`: xem tay hai màn này.
9. **Chất lượng ảnh ải**: băng 1536 px ở 1080p, PSNR 26,7–33 dB (230-F5), nhìn vệt màu và khối.
10. Sau khi gộp 210: kịch bản đặt `survival.guide` sau khi trang đã nạp (`survival-ui-art.mjs:47`); kiểm lượt chọn súng phím 1, 2 vẫn đúng.

220 không đổi view nên không cần trình duyệt, trừ khi chọn một luật.

## 7. Dọn và phạm vi

- `find games/.wt-ts-art games/.wt-ts-codex -newer …/codex-230/marker -not -path '*/.git/*'`: **0 dòng** (chạy hai lần, lần cuối ngay trước khi dọn). `find games/typing-survival/art-src -newer marker`: 0 dòng.
- `snapshot-after.json` so với `snapshot-before.json`: art 311/311, codex 288/288 file trùng SHA-256; HEAD, nhánh, status không đổi; 0 file mới; mục `node_modules` cấp 1 và mtime `results.json` không đổi (`snapshot-compare.json`).
- Đã xóa `games/typing-survival/tmp/codex-230/` (bản chép, `dist`, WebP dựng lại trong `tmp/` của bản chép, bộ đệm). Thư mục do phiếu này tạo, không có ảnh chụp trình duyệt, nên xóa thẳng như 224. Trước khi xóa: 85 MB. `rm -rf` mã 0, thư mục đã mất; `ls games/typing-survival/tmp` trước và sau chỉ khác đúng `codex-230` (`cleanup.txt`, `tmp-*-cleanup.txt`).
- Repo cha: phiếu này chỉ thêm `docs/codex-queue/230-report.md` và `docs/codex-queue/230/`. Không đụng `tmp/codex-209`, `codex-220` hay thư mục khác.

## 8. Việc của Claude

1. 206: chạy mục 6, rồi commit trên `ts-art`. Nên thêm hai test của 230-F1, 230-F2 trước khi commit; sửa 230-F4 cùng lúc. 230-F3, 230-F5 để phiếu sau hay khi chấm ảnh.
2. 220: commit trên `ts-codex` với núm tắt. Nên làm 230-F6 (một dòng import) và 230-F7 (một test) trước. Chọn luật là việc riêng: 220 chưa khuyến nghị luật nào; nếu chọn R3 thì cần phiếu đưa dấu vào hash và ghim hash (230-F8).
3. Thứ tự gộp: theo rủi ro đã ghi ở 206 (`main.ts`, `hud.ts`, `screens-journey.ts`, `journey.ts`, `survival.css` cũng đổi ở `ts-codex` 210 và `ts-typefx`).

## Bằng chứng trong `230/`

`preflight.txt`, `snapshot-before.json`, `snapshot-after.json`, `snapshot-compare.json`, `newer.json`, `cleanup.txt`, `copy.json`, `art-head-copy.json`, `{art,codex}-{status,diff-stat,HEAD}-before.txt`, `prepare-rerun.json`, `bytes-per-screen-rerun.json`, `golden-from-head.json`, `hash-probe.json`, `metrics-s1.json`, `runs-compare.json`, `mutations-206.json`, `mutations-220.json`, `logs/` (check, chapter, prepare, deploy-pack; đuôi `.txt` vì repo cha bỏ qua `*.log`), `runs/` (`.err`, `timeline.jsonl`), `tools/` (`snap.py`, `run-balance.sh`, `mutate.py`, `mutate-206.py`, ba probe `.ts.txt`). JSON chạy bot không chép lại vì trùng SHA-256 với `220/runs/` và `209/runs/`.
