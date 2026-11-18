# Phiếu 204 · Wordwoven · Icon và chân dung thật cho HUD, thanh đội, menu xây, tạm dừng, kết quả và thanh boss (chỉ ảnh Claude đã nhận)

**Nguồn:**
- Kiểm kê UI 29/10 (`docs/games/map1/UI_IMAGERY.md` §3.3–3.7):
  - WW-20, năm ô tài nguyên: "nhãn chữ + số, không icon";
  - WW-30, chân dung thanh đội: "**đĩa chữ cái**: đèn lồng CSS màu nhân vật, chữ "D", "C", "P", "G"";
  - WW-32, nơi được cử tới: "**emoji "🏹", "🧨"**";
  - WW-66, Tối Thượng: "đầu rồng vẽ canvas trên thẻ giấy".
- `AGENTS.md`: "Every UI detail carries real art, not text alone."
- `docs/HANDOFF_CURRENT.md` §3: "chân dung Draconis và Thư Đồng vào thanh đội Wordwoven; icon tài nguyên Wordwoven".
- `docs/games/MAP1_PRODUCTION.md` §2.2, C12: "skin HUD theo TK 23.5 với chân dung và icon thật; HUD ≤ 10 % ở 1280".
- Chủ dự án 29/10 tối: "tăng thêm việc cho codex cho tôi".

C12 là P1 có tên trong danh sách, nên được làm trong giai đoạn không thêm tính năng (chủ dự án 28/10). MAP1_PRODUCTION giao C12 cho làn L4 của Claude. Phần icon và chân dung nay chuyển sang Codex. Phần đồ bay về ô (đồng, Rice, Wood, Mảnh Chữ, Chest khi boss rút) vẫn thuộc làn Claude.

**Không trùng:**
- 133–136, 141–145, 160, 165–167: chỉ vẽ ảnh. Phiếu này chỉ gắn.
- 180, 193: nút Settings, nút loa, bảng âm. WW-14 … WW-17 và WW-19 không thuộc phiếu này.
- 200: script chuẩn bị `prepare-ui.mjs` và bảng ảnh `art.ts`. Phiếu này dùng lại, không viết lại.
- Thẻ chữ WW-44 … WW-50 (C10: phiếu 203 và làn L) và map 2D bậc Low WW-60 … WW-65 (làn L).

**Báo cáo:** `docs/codex-queue/204-report.md` (tiếng Việt), thư mục `docs/codex-queue/204/`.

## Chỉ chạy khi

Kiểm theo thứ tự. Thiếu một điều thì **dừng ngay**, ghi điều thiếu vào báo cáo, không sửa mã.

1. Có ít nhất một `docs/codex-queue/accept-*/verdict.md` ghi **Nhận** cho ít nhất một ảnh của lô UI Wordwoven (74 ảnh):
   - 134 HUD và hệ thống (12);
   - 135 tem hạng và sao (8);
   - 136 nút và icon thẻ nhà (10);
   - 141 menu, âm lượng, hồ sơ (12);
   - 160 năm khung `.v2`;
   - 165 nhà, đèn lồng `.v2` và hai icon khay (10);
   - 166 tài nguyên `.v2` và Seeds (8);
   - 167 chín chân dung `.v2`.

   Lúc viết phiếu (30/10) chưa có verdict nào cho lô này: `accept-29-10` và `accept-29-10b` chỉ chấm 113–120, 137–140, 158, 159.
2. Worktree `games/.wt-td-ui` có, nhánh `td-ui`.
3. Nhánh đã có phần của 193: file `src/app/quick.ts` và `src/ui/quick.css` đã commit trên `td-ui`. `td-ui` cắt từ `td-1c` `2a1f61d` (chưa có 193), nên Claude duyệt 193 rồi gộp `td-keys` vào `td-ui` sau 200 và 203.
4. Có `docs/codex-queue/200-report.md` và `docs/codex-queue/203-report.md`.

## Nơi làm

- Worktree `games/.wt-td-ui`, nhánh `td-ui`. Làn Codex duy nhất (chủ dự án 30/10: một làn), chạy sau 203. cwd của làn là repo cha (`.`).
- `git status --short -uall` phải sạch, hoặc chỉ còn file của 203 mà Claude chưa commit. Khi đó ghi danh sách vào báo cáo và không sửa phần của 203 ngoài chỗ việc này cần. Có file lạ khác thì dừng.
- **Ảnh vào:** chỉ đọc, ở checkout chính `games/typing-defense/art-src/` (`art-src` nằm ngoài Git; liên kết `art-src/*` của worktree, nếu có, trỏ về đó).
- **Ảnh ra:** WebP do `prepare-ui.mjs` ghi vào `public/assets/typing-defense/ui/` **của worktree**, đúng cách 200 đặt. Media không vào Git.

**Đọc trước (chỉ đọc):**
- `docs/games/map1/UI_IMAGERY.md` §3.3–3.7 (bảng WW), §5.2 (hình vẽ bằng mã phải gỡ), §8 (một bảng URL; ảnh lỗi thì `console.warn`).
- `200-report.md`: đường dẫn và định dạng của `art.ts`, `prepare-ui.mjs`, cờ nhận nếu có, cỡ xuất. `203-report.md` và báo cáo của mọi phiếu trước trên nhánh `td-ui`: chỗ nào đã gắn thì không làm lại. `193-report.md`: file của 193.
- Mọi `docs/codex-queue/accept-*/verdict.md`.
- Báo cáo 134, 135, 136, 141, 160, 165, 166, 167: tên file, bản `.v2`, cỡ đã xuất.
- Mã trong worktree:
  - `src/ui/hud.ts`: `statusHtml` (WW-18 … 25), `stripHtml` (WW-28), `actionsHtml` (WW-35), `BossBanner` (WW-51 … 54), lớp `Hud` (ghi panel chỉ khi HTML đổi);
  - `src/ui/team-bar.ts` (WW-29 … 34; `view.short` là chữ cái và emoji);
  - `src/ui/build-menu.ts` (WW-36 … 43);
  - `src/ui/sheets.ts` (WW-55 … 58; `recordLine`, sao "★");
  - `src/ui/title.ts` (WW-12, 13; `bestHtml` "★☆");
  - `src/ui/td.css` (đèn lồng chân dung và sọc ô khóa khoảng dòng 89–103; sao khoảng 203–209), `src/ui/theme.css`;
  - `src/content/slice-1a.ts`: `short` của Archer Tower là "🏹", Cannon Tower là "🧨";
  - `src/view/fx-pipe.ts` `portrait()` (khoảng dòng 149–189) và chỗ gọi nó ở `src/view/debug-2d.ts` (khoảng dòng 181);
  - `tests/td-hud.test.ts`, `tests/english-ui.test.ts`, `tests/td-settings.test.ts` (dòng 57, 59 so ký tự "★").

## Luật chọn ảnh

- Một ảnh chỉ được gắn khi một `accept-*/verdict.md` ghi **Nhận** cho đúng tên và đúng bản (`.v2` hay bản gốc).
- Ảnh "Làm lại", chưa chấm, hay của 142–145 (giao 30/10, chưa chấm; gắn ở phiếu sau) thì **không gắn**, dù file đã có trong `art-src`.
- Ảnh đã nhận từ trước cũng được gắn:
  - `logo` của 113: chỉ bản sạch (`accept-29-10/verdict.md` mục 113). md5 của file dùng phải khớp `games/typing-defense/art-src/_review/113/delivery-alpha/`; không khớp thì không gắn, ghi lại;
  - `portrait-ring`, `crest`, `banner` của 115 (`ui/frames-epic/*.alpha.png`).
- `seeds` có hai bản: 134 `ui/icons/seeds` và 166 `ui/resources/seeds`. Dùng bản đã nhận. Nhận cả hai thì dùng 166 (cùng bộ tài nguyên), ghi lại.
- Mức nhận ảnh là việc của Claude (M ≥ 8 theo game thương mại, `docs/games/ART_DIRECTION_2026-10-28.md` §1.3; Q ≥ 8, `docs/games/ART_ACCEPTANCE.md` §2.2). Codex không tự chấm, không tự nhận.

## Chỗ gắn

Cỡ là px CSS ở 1280 × 720 / 1920 × 1080, theo UI_IMAGERY. Thang `--ui` và `--hud` của game giữ nguyên.

| WW | Chỗ | Ảnh (phiếu) | Cỡ |
|---|---|---|---|
| WW-12 | 5 mục menu màn tựa | `menu-start`, `menu-continue`, `menu-settings`, `menu-learn`, `menu-profile` (141) | 24 / 36 |
| WW-13 | sao tốt nhất ở màn tựa | `star-lit`, `star-unlit` (135) | 16 / 20 |
| WW-18 | dòng tên HUD | `logo` (113), thay chữ "Wordwoven" | rộng 90 / 110 |
| WW-20 | 5 ô tài nguyên | `gold`, `wood`, `food` (Rice), `seeds`, `lives` (166) | 20 / 24 |
| WW-21 | mất mạng | `lives` nháy cạnh "−n" | 20 / 24 |
| WW-22 | dòng pha | `day`, `night` (134); `wave` (166) cạnh số quái | 20 / 24 |
| WW-23 | dòng học | `knowledge` (166), `review-book` (134) | 16 / 20 |
| WW-24 | gọi đêm sớm | `night-call` (134), `gold` (166) | 24 / 29 |
| WW-25 | dòng báo, thua | `warning` (134); icon tài nguyên bị thiếu | 16 / 20 |
| WW-28 | chuỗi | `chain` (134). Bốn chấm giữ như cũ (chấm vẽ là 145) | 16 / 20 |
| WW-29 | đầu thanh đội | `night-call` (134) | 16 / 20 |
| WW-30 | chân dung | `draconis`, `helper-cham-happy`, `helper-phay-happy`, `helper-gach-happy` (167); bản `-scared` khi `A.panic[a] !== 0`; đặt trong `portrait-ring` (115) | 54 / 65 |
| WW-32 | nơi được cử tới | `keep`, `archer`, `cannon`, `barracks`, `gold-mine`, `farm` (165) | 20 / 24 |
| WW-33 | vòng nạp Tối Thượng | `portrait-ring` (115) đè lên vòng đo `--ult`; phần đo giữ | 54 / 65 |
| WW-34 | ô khóa | chân dung của ô đó, tối bằng CSS `filter`; `lock` (136) | 16 / 20 |
| WW-35 | nút Build, Hire Villager, Ultimate, Pause | `build`, `hire-villager`, `ultimate` (136); `pause` (134) | 24 / 29 |
| WW-36 | đóng menu xây | `close` (134), thay "×" | 16 / 20 |
| WW-37 | 5 hàng nhà | icon nhà (165); `gold`, `wood` (166) trong giá | 28 / 34; giá 16 / 20 |
| WW-38 | dòng "làm gì" | icon tài nguyên trong dòng (166) | 16 / 20 |
| WW-39 | đầu thẻ nhà | icon nhà (165); `level-pip-lit`, `level-pip-unlit` (136) | 28 / 34; chấm 8 / 10 |
| WW-40 | ruộng | `seeds` (166). Ba trạng thái ruộng là 143: chưa gắn | 16 / 20 |
| WW-41 | thẻ Fort | `keep` (165); chân dung Chấm (167); `sell`, `upgrade` (136). `villager`, `builder` là 143: chưa gắn | 16 / 20; chân dung 24 / 29 |
| WW-42 | lượt mạnh | 5 đèn: `lantern-unlit`, `lantern-lit` (165), `lantern-blazing` (166) | 16 / 20 |
| WW-43 | nút gửi, hoàn tác, bán, nâng | `send`, `undo`, `sell`, `upgrade` (136); chân dung người được gửi (167) | 16 / 20 |
| WW-51 | thanh boss | `moc-tinh` (167) | 48 / 58 |
| WW-52 | máu boss | giữ thanh hiện có. Khung thanh vẽ chưa có phiếu: ghi "chờ AD" | — |
| WW-53 | lời Mộc Tinh | `moc-tinh` nhỏ | 24 / 29 |
| WW-54 | lời Bà Cú Mực | `narrator` (167) | 40 / 48 |
| WW-55 | thẻ tạm dừng | `play` (134), `menu-settings` (141), `close` (134) trên ba nút | 20 / 24 |
| WW-56 | đầu thẻ kết | `crest`, `banner`, `divider` (115) đã gắn ở 200 (crest giữa trên): giữ nguyên, không dời | — |
| WW-57 | sao kết quả | `star-lit`, `star-unlit` (135). `record-ribbon` là 142: chưa gắn | 28 / 34 |
| WW-58 | số kết quả | `lives`, `gold`, `knowledge` (166); `grade-perfect` (135). `stat-nights`, `stat-foes`, `stat-words` là 142: chưa gắn | 20 / 24 |
| WW-66 | chân dung Tối Thượng | xem Việc 6 | 420 × 280 / 630 × 420 |

**Khung 160** (`panel-large.v2`, `plate-long.v2`, `button.v2`, `button-active.v2`, `tooltip.v2`):
- Chỉ gắn khi đã nhận **và** chưa phiếu trước nào trên `td-ui` gắn (xem báo cáo của chúng).
- Nếu gắn: chỉ `panel-large.v2` cho thẻ tạm dừng và thẻ kết (WW-55, WW-56), bằng `border-image` theo `slice` và `repeat` của `panel-large.v2.json`.
- Khung HUD trận không đổi. MAP1_PRODUCTION §2.3, I6: khung HUD 9-slice chỉ làm khi giám khảo chấm HUD dưới 8 sau C12.

## Việc

1. **Kiểm điều kiện chạy.** Lập danh sách ảnh đã nhận từ mọi verdict: tên, bản, phiếu, file verdict, dòng. Lưu `204/accepted.json`.
2. **Đưa ảnh đã nhận vào bảng của 200.**
   - Thêm mục vào `art.ts` và vào danh sách nguồn của `prepare-ui.mjs`, đúng định dạng 200 đặt, kể cả cờ nhận nếu 200 có.
   - Chạy `prepare-ui.mjs` để xuất WebP vào `public/assets/typing-defense/ui/` của worktree.
   - Script chỉ được cắt, tách nền (ảnh còn nền khóa), đổi cỡ. Không làm sáng, làm tối, phủ hay xóa phần vẽ (`ART_ACCEPTANCE.md` §5).
   - Cỡ xuất đủ cho 2× cỡ 1080p của bảng. Ô dưới 32 px không tải bản 256.
   - Mã chỉ đọc URL từ `art.ts`. Không `import` ảnh vào bundle, không base64.
3. **Một hàm vẽ icon cho mọi chỗ.**
   - Dùng hàm của 200 nếu có. Chưa có thì thêm `src/ui/art-html.ts`.
   - Ảnh đã nhận và có URL: trả `<img class="ww-ico" src="…" alt="" aria-hidden="true" data-art="<tên>" width height>`.
   - Ảnh thiếu, chưa nhận, hay đã hỏng: trả nhãn chữ tiếng Anh như hôm nay. Không emoji, không hình CSS. `console.warn` đúng một lần mỗi tên.
   - Ảnh lỗi khi tải: một bộ nghe `error` (pha capture) trên gốc HUD và gốc màn tựa ghi tên đó là hỏng trong `art.ts`. Lần vẽ sau trả nhãn chữ. Không gắn `onerror` trong chuỗi HTML.
   - Icon thay nhãn chữ thì ô chứa nó giữ `aria-label` và `title` tiếng Anh ("Gold", "Lives" …).
   - Chuỗi HTML của một ô chỉ đổi khi số hay trạng thái đổi. Lớp `Hud` chỉ ghi lại panel khi HTML đổi; đừng làm nó ghi lại mỗi khung.
4. **Gắn theo bảng "Chỗ gắn".**
   - `hud.ts`: WW-18, 20–25, 28, 35, 51–54. Lời trong `BossBanner` mang theo người nói (Mộc Tinh hay Bà Cú Mực) để chọn chân dung; không đoán theo tiền tố chuỗi.
   - `team-bar.ts`: WW-29, 30, 32–34. Chân dung thay chữ cái `view.short`. Số phím `<i>` giữ (mặt phím vẽ là 145). Huy hiệu nơi được cử tới lấy icon theo id nhà, không theo `short`.
   - `build-menu.ts`: WW-36–43. `sheets.ts`: WW-55–58. `title.ts`: WW-12, 13.
   - `td.css`, `theme.css`: thêm kiểu cho `.ww-ico` và ô chân dung. Bỏ hình CSS đã có ảnh thay: đèn lồng chân dung, sọc ô khóa, sao ký tự. Kiểu của phần chưa có ảnh đã nhận thì giữ nguyên.
   - Chỗ 200 hay 203 đã gắn thì giữ nguyên.
5. **Bỏ emoji và ký tự hình.**
   - `slice-1a.ts`: `short` của Archer Tower "🏹" thành "AT", của Cannon Tower "🧨" thành "CT". Sau việc 4 không UI nào trong phiếu này đọc `short`; chỉ map 2D bậc Low còn đọc (WW-60, làn L).
   - "★", "☆" ở `bestHtml` (`title.ts`), `recordLine` và sao kết quả (`sheets.ts`) thành ảnh sao. Thiếu ảnh thì chữ, ví dụ "Best 2/3".
   - `scripts/visual/scenarios/td-1b-story.mjs` (khoảng dòng 172, 185) đang đếm "★" ở màn tựa: đổi sang đếm `data-art="star-lit"`, giữ đường lui đếm chữ "Best n/3" khi thiếu ảnh. Không chạy kịch bản; liệt kê cho Claude.
6. **Chân dung Tối Thượng bằng DOM (WW-66).**
   - Bỏ `portrait()` ở `fx-pipe.ts` và dòng gọi nó ở `debug-2d.ts`. Không sửa gì khác trong `src/view/`.
   - Lớp mới `src/ui/ult-card.ts`. Nó đọc sự kiện `ult` ở cùng chỗ `BossBanner.read` đọc sự kiện.
   - Nhịp như cũ: trượt vào từ mép trái 0,6 s, giữ, trượt ra 0,4 s, tổng 1,9 s; đỉnh thẻ ở 30 % cao màn. Chỉ dùng CSS `transform` và `opacity`.
   - Ảnh, theo thứ tự:
     - `draconis-ult` (`portraits/draconis-ult.png`, 1536 × 1024) chỉ khi một verdict nhận nó;
     - không có thì `draconis` (167) trong `portrait-ring` (115), trên `banner` (115);
     - không chân dung nào đã nhận: chỉ `banner` với chữ, và `console.warn`.
   - Chữ "Ultimate!" bằng font tiêu đề đang nạp.
   - `pointer-events: none`. Không thêm vào `PANELS`.
   - Là DOM nên chạy cả trên map 3D lẫn 2D.
7. **Giữ HUD ≤ 10 % ở 1280** (C12).
   - Icon thay nhãn chữ, không đứng thêm cạnh nhãn, trừ chỗ bảng ghi cả hai.
   - Không thêm hàng. Không tăng `padding`, `font-size` hay bề rộng panel.
   - Liệt kê mọi chỗ có thể làm panel to ra (chân dung người kể, logo, chân dung boss) để Claude đo.
8. **Test trước, mã sau.**
   - `tests/td-hud-art.test.ts` (mới), mỗi WW đã gắn ít nhất một ca:
     - tên đã nhận: HTML có `data-art` đúng tên và đúng bản;
     - tên thiếu hay chưa nhận: có nhãn chữ tiếng Anh, không `<img>`, `console.warn` đúng một lần mỗi tên (`vi.spyOn`);
     - tên bị đánh dấu hỏng: lần vẽ sau ra nhãn chữ;
     - chân dung `-scared` khi `A.panic[a] !== 0`; ô khóa có `lock`; nơi được cử tới ra icon nhà đúng id;
     - thẻ Tối Thượng: trạng thái theo `now` (vào, giữ, ra, hết) và thứ tự chọn ảnh theo cờ nhận.
   - Bộ nghe `error` test bằng stub nhỏ viết tay. Không thêm gói (jsdom, happy-dom).
   - `tests/no-glyph-icons.test.ts` (mới), quét như `tests/english-ui.test.ts` (chuỗi trong mã qua TypeScript, chuỗi trong CSS):
     - phạm vi: `src/ui/**`, `src/content/slice-1a.ts`, `src/view/fx-pipe.ts`;
     - cấm `\p{Extended_Pictographic}` và `★`, `☆`, `●`, `○`;
     - ngoại lệ chỉ theo danh sách trong test, mỗi mục có file, ký tự, lý do. Ví dụ "▶" và "Ⅱ" của nút tạm dừng WW-19 (193) nếu còn; "✦" của số bay VFX (WW-67).
     - 203 đã có `tests/td-no-emoji.test.ts` thì gộp phạm vi, mẫu và ngoại lệ vào đó thay vì viết file quét thứ hai; ghi lựa chọn. Kiểm 4 khi đó đọc tên file của 203.
   - `tests/td-hud.test.ts` và mọi test khác vẫn xanh. Test so nhãn đã bỏ hay ký tự "★" (ví dụ `td-settings.test.ts` dòng 57, 59) thì đổi theo nghĩa: đếm sao sáng, kiểm `aria-label`. Ghi từng test đã đổi và lý do.
9. **Changelog** `docs/changelog/<ngày>-hud-art.md` của Wordwoven: WW đã gắn, ảnh và phiếu của nó, chỗ còn chờ.

## Cấm

- Mọi lệnh git có ghi; sửa `src/kit/**`; chạy `kit:sync`.
- Gắn ảnh chưa có dòng **Nhận**; gắn ảnh của 142–145.
- Sửa `src/sim/**`, `src/content/rules.ts`, `src/view/**` (trừ hai chỗ ở Việc 6), `src/view/words/**` (thẻ chữ, C10), `src/view/3d/**`.
- Sửa nút Settings, nút loa, bảng âm của 193 (WW-14 … 17, WW-19).
- SVG, canvas, emoji, gradient hay hình CSS thay cho ảnh thiếu. Thêm trang trí CSS mới.
- Sửa, chép đè, xóa file trong `art-src`. Đưa ảnh vào Git. Xử lý ảnh làm đổi phần vẽ (§5).
- Dev server, trình duyệt, mạng. Thêm gói npm.
- Đụng game khác, worktree khác (nhất là `.wt-td-1c`, `.wt-td-keys`, `.wt-td-codex`, `.wt-td-vfx`), Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`).
- Ghi ra ngoài repo.
- Chữ người chơi thấy phải là tiếng Anh. Chỉ tên riêng Draconis, Mộc Tinh, Bà Cú Mực, Chấm, Phẩy, Gạch giữ dấu, như `tests/english-ui.test.ts`.

## Kiểm (ghi số)

1. `pnpm check` xanh (số test trước và sau). Test thời gian đỏ khi máy bận thì chạy riêng ba lần.
2. Dòng `bundle budget` của `/`: ≤ 85 kB gzip. Ghi số trước, sau và phần dư.
3. `pnpm td:golden:check` giữ nguyên; ván vàng không đổi.
4. `tests/english-ui.test.ts` và `tests/no-glyph-icons.test.ts` xanh. Liệt kê mọi chuỗi mới người chơi thấy và mọi ngoại lệ của test quét.
5. Bảng WW → ảnh (tên, bản, phiếu, file verdict và dòng) → trạng thái: "gắn", "chờ nhận", "chờ phiếu <số>", "ngoài phiếu". Đủ mọi WW: 12, 13, 18, 20–25, 28–43, 51–58, 66.
6. Danh sách media `204/media.txt`: mọi file `prepare-ui.mjs` ghi vào `public/assets/typing-defense/ui/` (đường dẫn, khổ, kB, md5). Ghi tổng kB tải thêm khi vào trận. `git -C games/typing-defense check-ignore -v` trên đường dẫn thật trong checkout chính cho thấy chúng nằm ngoài Git (trong worktree `ui/` là liên kết, git từ chối đường dẫn đi qua liên kết). Claude chạy `media:push`.
7. `git status --short -uall`: chỉ file của việc này, test, `docs/changelog/<ngày>-hud-art.md`. File 203 chưa commit (nếu có) thì nêu tên riêng.
8. `grep` trên các file đã sửa: không `<svg`, emoji, `gradient` mới. Ghi kết quả.
9. Chỗ còn emoji hay hình vẽ bằng mã ngoài phạm vi (`src/view/words/cards.ts`, `src/view/debug-2d.ts`, `src/view/boss-2d.ts`): đếm và ghi cho Claude, không sửa.
10. Hướng dẫn cho Claude kiểm trên trình duyệt:
    - `td-hud-budget` ≤ 10 % ở 1280 × 720;
    - xem ở 1280 × 720 và 1920 × 1080: HUD, thanh đội (có Thư Đồng hoảng, có ô khóa), menu xây, thẻ Fort, ruộng, thanh boss, lời Bà Cú Mực, tạm dừng, thắng, thua, màn tựa có sao, Tối Thượng trên map 3D;
    - đổi một ảnh sang chưa nhận để thấy nhãn chữ thay.

**Rủi ro:**
- Phiếu bị chặn tới khi Claude chấm lô 74 ảnh. Nhận một phần thì gắn phần đó; phần còn lại giữ nhãn chữ, ghi "chờ nhận". Chạy lại sau lượt chấm sau thì chỉ thêm mục vào `art.ts`, không làm lại phần đã gắn.
- `hud.ts` đụng 193 nếu 193 chưa gộp. Điều kiện 3 chặn việc này.
- Icon và chân dung có thể đẩy HUD quá 10 % ở 1280. Việc 7 giữ icon thay chữ; Claude đo, quá thì báo lại để giảm cỡ.

**Xong khi:** chín mục việc và mười mục kiểm đạt; hoặc phiếu dừng ở "Chỉ chạy khi" với lý do ghi trong báo cáo. Claude đo `td-hud-budget`, kiểm ở 1280 và 1920, chạy `media:push`, rồi commit.
