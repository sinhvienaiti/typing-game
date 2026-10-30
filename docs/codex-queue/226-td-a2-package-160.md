# Phiếu 226 · Wordwoven · A3: chấm gói `a2-package-v2` trên 160 seed (dải chặt, B1–B8) và §12 trên 20 seed so với mã hiện tại, để có số cho lựa chọn (a) của chủ dự án

**Nguồn:**
- `docs/games/MAP1_PRODUCTION.md` §2.2 mục 21: "**A3** · P1 · G6. §12 trên 20 seed trượt 5a, 5b; thiếu B9; Đêm 1 trên trình duyệt mất 6–7/20 mạng. **Sửa:** đo 5a, 5b và mạng mất ở Đêm 1 trên 20 và 80 seed, cả bộ 81–160; gói `a2-package-v2.patch` là điểm bắt đầu".
- `games/typing-defense/docs/changelog/2026-10-27-open-items.md`, mục "Còn mở (về chủ dự án; chặn việc 1, 2, 4)": "Gói việc 1, 2, 4 (`a2-package-v2.patch`): đạt mọi cổng §12 trên 20 seed … nhưng dải chặt trượt ở Chậm chắc đúng một ván (88,75 %) … Chủ dự án chọn: (a) chấm dải chặt trên 160 seed (hai bộ hiện có cộng seed 81–160) …".
- `games/typing-defense/AGENTS.md` (dòng 112): "5a 8.48 s and 5b 29.5 % still fail on 20 seeds."
- Điều phối chạy thử 30/10: `git apply --check` của gói trên `a2-days` chỉ hỏng ở `src/content/slice-1a.ts:99`. Dòng ngữ cảnh của khối đó đã đổi từ "Thuồng Luồng" thành "River Serpent" (lượt tên tiếng Anh); các số trong khối không đổi. `patch -p1 -F2` của macOS áp được cả 11 khối ("Hunk #1 succeeded at 99 with fuzz 1"), và `diff -ru` sau đó ra đúng 60 dòng +/- của gói.
- `docs/HANDOFF_CURRENT.md` dòng 18 (30/10, 11:20): chủ dự án "bảo Claude dừng mọi việc, chỉ giao việc cho Codex (ba làn, nhiều việc)".
- Phản biện chạy lại 30/10, khoảng 13:15, trong bản chép ngoài repo: `patch -p1 -F2` mã 0, 11 khối, chỉ khối 1 của `slice-1a.ts` có fuzz 1; `diff -ru base pkg` đúng 5 file, 11 khối, +45/−15, `cmp` với dòng của gói mã 0. `night1.ts --seeds=40` trên `base` ra từng dòng bot giống hệt `base-night1.md`, trên `pkg` giống hệt `v1-night1.md`. Khói `balance.ts --stage-seeds=2 --stage-sets=1 --quick --threads=2` mã 0, 11 s.

**Vì sao:** lựa chọn (a) cần số thật trên 160 seed, đo trên mã hiện tại chứ không phải cây thử 27/10. `src/sim` và `src/content` của `a2-days` (`f9abfd0`) giống hệt `td-1c` (`2a1f61d`, nhánh map 1 đang làm); điều phối đã kiểm 30/10 (`diff --stat` rỗng). Vậy số đo trên `a2-days` đúng cho `td-1c`.

**Không trùng:** bước A1, A2 (`open-items.md`). A1 có dò seed 81–160 bằng `--quick` (dòng 125), nhưng trên mã A1, không phải gói; `runs/base-q240.md`, `m1-q240.md` là mã gốc và biến thể m1, cũng không phải gói. Gói chỉ được đo trên seed 1–80 và không giữ. Còn 209 (cân bằng Last Line), 199, 200, 202 (cảnh và ảnh Wordwoven, cùng làn s9 nhưng ở worktree khác). Phần còn lại của A3 (chủ dự án chơi B9, quyết định đưa gói vào luật, đổi mã) không thuộc phiếu này.

**Loại phiếu:** báo cáo đo. Không sửa file nào của game. Gói chỉ áp vào một bản chép trong `tmp/`.

**Báo cáo:** `docs/codex-queue/226-report.md` (tiếng Việt), thư mục `docs/codex-queue/226/`. Cả hai ở repo cha.

## Chỉ chạy khi

Kiểm điều 6 trước tiên, trước khi tạo bất cứ thứ gì. Rồi kiểm từng điều, ghi đầu ra vào `226/preflight.txt`. Thiếu một điều thì dừng, ghi lý do vào báo cáo:

1. `git -C games/typing-defense rev-parse a2-days td-1c` ra `f9abfd09987dadd519233c2f38692758d35cefca` và `2a1f61d7da2ee6e6ca4abdc23f8775f872d9c9e7`. Nhánh đã tiến thì ghi lại và làm tiếp, miễn điều 2 còn đúng.
2. `git -C games/typing-defense diff --stat a2-days td-1c -- src/sim src/content` rỗng (0 dòng). Có dòng nào thì **dừng**: số đo sẽ không đúng cho `td-1c`.
3. `shasum -a 256 games/typing-defense/tmp/mac-2026-10-27/open/a2-days/a2-package-v2.patch` ra `66b61fbd73cfefe7533d0c6348822556b4b9c90c54ec37c3ae015553908e11aa` (11.086 byte).
4. Có `games/typing-defense/node_modules/.bin/tsx` và `games/typing-defense/node_modules/tsx/`. Không `pnpm install`.
5. `df -g .` còn ít nhất 10 GB trống.
6. `games/typing-defense/tmp/codex-226/` và `docs/codex-queue/226/` chưa có.
   - Có, và `226/preflight.txt` cho thấy đó là lượt trước của chính phiếu này bị cắt: xóa `games/typing-defense/tmp/codex-226/`, làm lại từ đầu (giữ `226/` cũ trong `226/prev-<giờ>/`).
   - Có mà không rõ của ai: **dừng**.

## Nơi làm

- **Không worktree.** Hai bản chép chỉ đọc của nhánh `a2-days`, đặt trong `tmp/` của game (Git của game bỏ qua `tmp/`). Không đụng worktree nào (`.wt-td-1c`, `.wt-td-scenery`, `.wt-td-ui`, `.wt-td-keys`, `.wt-td-vfx`, `.wt-td-codex`), nên chạy song song được với phiếu khác.
- cwd của làn: gốc repo cha (`.`). Mọi lệnh dưới đây viết từ gốc đó.
- Mỗi lệnh shell của Codex là một phiên mới: đặt lại `TD`, `W`, `E` ở đầu mỗi lệnh dùng chúng.
- Luật chung của runner cấm chạy build hay test suite của game. Phiếu này **được** chạy đúng `scripts/td/balance.ts`, `probe/pernight.ts` và `probe/night1.ts` bằng `node --import tsx` **trong hai bản chép**. Không `pnpm`, không `vitest`, không lệnh nào trong checkout chính hay worktree.
- **Chỉ được ghi:** `games/typing-defense/tmp/codex-226/`, `docs/codex-queue/226/`, `docs/codex-queue/226-report.md`.
- Dựng hai bản chép:
  ```bash
  TD=games/typing-defense
  W=$TD/tmp/codex-226
  E=$TD/tmp/mac-2026-10-27/open/a2-days
  mkdir -p "$W/base" "$W/pkg" "$W/runs" "$W/tmpdir"
  git -C "$TD" rev-parse a2-days td-1c > "$W/refs.txt"
  git -C "$TD" archive a2-days | tar -x -C "$W/base"
  git -C "$TD" archive a2-days | tar -x -C "$W/pkg"
  ln -s ../../../node_modules "$W/base/node_modules"
  ln -s ../../../node_modules "$W/pkg/node_modules"
  cp "$E/a2-package-v2.patch" "$W/"
  ```
- Áp gói **chỉ vào `pkg`**, bằng `patch`, không bằng git:
  ```bash
  (cd "$W/pkg" && patch -p1 -F2 --verbose --no-backup-if-mismatch < ../a2-package-v2.patch) > "$W/runs/patch.log" 2>&1
  ```
  - Đúng ra: mã thoát 0; 11 dòng "Hunk #… succeeded"; chỉ khối 1 của `slice-1a.ts` có "with fuzz 1"; không file `.orig`, `.rej`.
  - `patch` hỏng: chép tay khối đó của `slice-1a.ts`. Chỉ đổi đúng hai dòng mà khối đổi (bốn dòng −/+): dòng chú thích `// BUILD_1B §6.5 round 1 …` thêm `; lane A2: 4,550` ở cuối, và `hp: 4200` → `hp: 4550` ở dòng `id: "moc-tinh"`; chép nguyên văn dòng `+` từ gói. Dòng ngữ cảnh "River Serpent" giữ nguyên. Rồi Kiểm 2 phải đạt. Không chép tay được thì dừng.
- Mọi lệnh Node chạy trong bản chép, với `TMPDIR="$PWD/../tmpdir"` (bộ nhớ đệm của `tsx` nằm trong repo; sandbox không ghi được ra ngoài) và `nice -n 15`.
- **Không dùng `.local/bin/heavy.sh`**: nó ghi trạng thái vào `/tmp`. Thay bằng luật máy dùng chung ở Việc 4.

## Đọc trước

- `games/typing-defense/docs/changelog/2026-10-27-open-items.md`, mục "Bước A2" (khoảng dòng 170–295): việc 1, 2, 4, bảng biến thể boss, "Còn mở".
- `games/typing-defense/docs/td/BUILD_NOTES.md` §7.10 (dòng 1791), tiểu mục "bước A2" (dòng 1832).
- `docs/games/BALANCE.md` §3 (dải đích), §7 (B1–B9) ở repo cha; `games/typing-defense/docs/td/BUILD_1B.md` §6.4 (đích chặt).
- Trong bản chép: `scripts/td/balance.ts` (70 dòng: `--stage-seeds`, `--stage-sets`, `--seeds`, `--nights`, `--threads`, `--modes`, `--quick`); `tests/td/flow.ts`: `TIGHT_BANDS` (dòng 198, thắng 780–880 ‰), `TIGHT_S` (Chuẩn 400–600 ‰), `tightTable` (319), `bossGates` (448), `stageReport` (483, in "seed from+1–from+seeds").
- `src/kit/balance/gates.ts:66`: thắng tính bằng `Math.round(thắng × 1000 / số ván)`. Vậy trên 160 ván, dải chặt đạt khi thắng **125–140 ván** (781–875 ‰); 141 ván là 881 ‰, trượt. Trên 80 ván: 63–70 ván; 71 ván (888 ‰) là ván trượt của Chậm chắc.
- **Báo cáo không in số ván.** `tightTable` in `pct(win)` (`src/kit/balance/gates.ts:129`): từ 10 % trở lên làm tròn tới 1 %. Trên 80 ván mỗi ván là 1,25 %, nên mỗi số % ứng đúng một số ván (phản biện đã thử k = 0…80: không trùng). Trên 160 ván thì **không**: 54 cặp trùng, gồm "88 %" = 140 ván (875 ‰, đạt) hay 141 ván (881 ‰, trượt). Vậy:
  - số ván mỗi bộ: k duy nhất trong 0…80 có `pct(Math.round(k × 1000 / 80))` bằng ô in ra;
  - số ván gộp = bộ 1 + bộ 2 (hai bộ là seed rời nhau: `playCell` chơi seed `from + k + 1`, `poolCells` nối các ván);
  - kiểm lại: `pct(Math.round(gộp × 1000 / 160))` phải bằng ô "gộp" in ra, và đạt/trượt tính từ ‰ đó phải khớp cột "Đích chặt 1B". Lệch thì ghi, không đoán.
  - Cùng cách cho bảng cũ: `r22-balance.md`, `v2-balance.md` có hai bộ 40 ván (mỗi ván 2,5 %, cũng không trùng).
- Đầu dò và kịch bản cũ (chỉ đọc): `$E/measure.sh`, `$E/probes/pernight.ts`, `$E/probes/night1.ts`.

## Số đã biết (để đối chiếu)

Số cũ nằm trong `$E/runs/`. Cùng seed, sim tất định, nên bản chép phải ra **giống hệt**.

**base** (`a2-days`). Cây `r22` của A2 là mã cuối `e49189a` (`src/sim`, `src/content`, `tests/td`, `scripts/td` giống từng file; điều phối so 30/10). Từ `e49189a` tới `a2-days`, `src/sim` không đổi; `src/content/slice-1a.ts` chỉ đổi tên hiển thị (`view.name`); `tests/td/typing.ts` đọc bộ từ ở `public/vocabulary` (bản ghim) thay cho `shared/vocabulary`, và level 1–5 của hai nơi giống từng byte.

| Đo | File cũ | Số |
|---|---|---|
| Cân bằng seed 1–80, thắng / Biên S | `r22-balance.md`, bảng "Gộp 2 bộ seed", cột gộp | Mới 86 / 60 %, Chậm chắc 86 / 65, Chuẩn 80 / 55, Khá 84 / 45, Ẩu 83 / 55, Nhanh 83 / 60; dải chặt 6/6 đạt; B1–B8 đạt, B9 THIẾU SỐ |
| §12 trên 20 seed | `r22-g12x20.md` (dòng 128–140) | 4 đạt (thấp nhất 3 mạng); 5a **8,48 s Hỏng**; 5b **29,5 % Hỏng**; 5c 23,0 %; 6 = 0; 7 +38,0 %; 5a Thư giãn 5,67, Thử thách 10,00, Học 5,67 s |
| §12 trên 5 seed (trong M1) | `r22-balance.md`, mục "Cổng BUILD_1A6 §12" | 4 (6 / 9 / 9 / 7 / 7 mạng); 5a 7,90 s; 5b 30,2 %; 5c 22,2 %; 7 +38,2 % |
| Từng pha, seed 25–48 | `r22-pn-balanced.md`, `-relax.md`, `-challenge.md` | Cân bằng, Đêm 1, mạng mất: Mới 0,63, Chậm chắc 2,08, Chuẩn 1,83, Khá 4,08, Ẩu 1,67, Nhanh 2,63, Không gõ 3,75. Đêm 3, Nhàn I: Chuẩn 20,1 %, Ẩu 20,1 %, Chậm chắc 14,2 % |
| Đêm 1, seed 1–40 | `base-night1.md` | mạng mất: 0,47 / 1,82 / 1,77 / 4,22 / 1,55 / 2,60 / 3,85 (Mới … Không gõ) |

**pkg** (`a2-days` + gói). Gói là biến thể 2 của A2 (máu boss 4.550, `kHp` 0,32, `kHp2` 12, trần 1,40, Rễ hút 20 s). Biến thể 1 và 2 chỉ khác ở trận boss, nên Ngày 1–5 và Đêm 1–4 của `v1-*` cũng là của gói.

| Đo | File cũ | Số |
|---|---|---|
| Cân bằng seed 1–80 | `v2-balance.md`, bảng "Gộp 2 bộ seed", cột gộp | Mới 80 / 50 %, Chậm chắc **89** / 65 (71/80, trượt), Chuẩn 81 / 55, Khá 85 / 60, Ẩu 79 / 55, Nhanh 85 / 55 |
| §12 trên 20 seed | `v1-g12x20.md` (dòng 128–140) | 4 đạt (thấp nhất **1 mạng**, seed 1 và 12); 5a 7,95 s; 5b 30,1 %; 5c 15,5 %; 6 = 0; 7 +39,2 %; 5a Thư giãn 5,67, Thử thách 9,98, Học 5,67 s |
| §12 trên 5 seed | `v2-balance.md`, mục §12 | 4 (1 / 7 / 4 / 8 / 7 mạng); 5a 7,93 s; 5b 30,5 %; 5c 15,4 % |
| Từng pha, seed 25–48 (chỉ Ngày 1–5, Đêm 1–4) | `v1-pn-balanced.md`, `-relax.md`, `-challenge.md` | Cân bằng, Đêm 1, mạng mất: 0,42 / 0,96 / 1,38 / 2,38 / 1,58 / 2,29 / 3,75. Đêm 3, Nhàn I: Chuẩn 31,1 %, Ẩu 34,6 %, Chậm chắc 24,5 % |
| Đêm 1, seed 1–40 | `v1-night1.md` | 0,55 / 0,72 / 1,27 / 2,00 / 1,48 / 2,17 / 3,85 |

Tên bot: `novice` Mới, `steady` Chậm chắc, `standard` Chuẩn, `skilled` Khá, `sloppy` Ẩu, `fast` Nhanh, `no-type` Không gõ, `child` Trẻ em.

## Việc

1. **Mốc.** Chạy sáu điều ở "Chỉ chạy khi". Ghi `git -C games/typing-defense status --short` và `git -C games/typing-defense branch --show-current` vào `226/git-before.txt` (lúc soạn phiếu: sạch, `a2-days`).
2. **Dựng và áp gói** như mục "Nơi làm", rồi làm Kiểm 2 ngay, trước khi chép đầu dò vào bản chép.
3. **Chạy khói**, không tính vào bảng. Mỗi bản chép một lần:
   ```bash
   (cd "$W/base" && TMPDIR="$PWD/../tmpdir" nice -n 15 node --import tsx scripts/td/balance.ts \
     --stage-seeds=2 --stage-sets=1 --quick --threads=2 > ../runs/base-smoke.md 2> ../runs/base-smoke.err)
   ```
   `pkg` như vậy, tên `pkg-smoke.*`. Mã thoát phải là 0; đầu file có "seed 1–2"; dòng cuối có "2 luồng". Không bỏ `--threads`: mặc định là 6 luồng (`Math.min(6, availableParallelism() - 1)`), quá luật 4 luồng. Hỏng thì dừng, ghi lỗi.
4. **Máy dùng chung** (làn khác có thể đo cùng lúc, ví dụ 220 của Last Line trong `.wt-ts-codex`, 224 của Wordwoven trong `tmp/codex-224/`):
   - Trước mỗi lệnh: ghi `date '+%F %T'`, `uptime` và `sysctl -n vm.loadavg` vào `$W/runs/timeline.txt`. Sau mỗi lệnh: giờ xong, mã thoát.
   - `--threads=4`. Tải 1 phút > 10 thì `--threads=2`; ghi số luồng đã dùng.
   - Mỗi lúc chỉ một lệnh `balance.ts`. Ba lệnh `pernight.ts` chạy cùng lúc được (ba tiến trình một luồng), nhưng chỉ khi không có `balance.ts` nào chạy và tải ≤ 10; tải > 10 thì chạy lần lượt.
   - Ước lượng: 40 × 2 seed với 6 luồng mất 245–260 s (27/10, `r22-balance.md`, `v2-balance.md`), nên 80 × 2 với 4 luồng khoảng 12–20 phút mỗi bản chép; §12 20 seed 44–54 s; mỗi `pernight` 95–200 s. Cả phiếu khoảng một giờ máy.
5. **Đo**, cho từng bản chép `C` (`base` rồi `pkg`), trong `$W/C`:
   - **M1. 160 seed:**
     ```bash
     TMPDIR="$PWD/../tmpdir" nice -n 15 node --import tsx scripts/td/balance.ts \
       --stage-seeds=80 --stage-sets=2 --threads=4 > ../runs/C-balance160.md 2> ../runs/C-balance160.err
     ```
     - Lệnh này đo đủ ba chế độ, mọi bot, hồ sơ, và §12 trên 5 seed. Không thêm `--quick`, `--modes`, `--bots`, `--set`.
     - Đầu ra phải có hai tiêu đề "seed 1–80" và "seed 81–160" (`playSet(set * seeds)`), và mục "## Gộp 2 bộ seed (160 ván mỗi ô)". Bộ 2 không phải 81–160 thì dừng lệnh đó, đọc `balance.ts`, ghi cách lấy đúng bộ vào báo cáo rồi chạy lại.
     - Lấy ra: dải chặt từng bot trên 160 ván gộp (thắng, Biên S); B1–B8 từng bộ (BALANCE §3) và gộp (đích chặt), cùng dòng "Để so, B1 và B7 gộp theo dải BALANCE §3"; bảng boss gộp; dòng G3, G8 (từng bộ và gộp); dòng "R2 gộp" (G2, G5, G6); thắng Thử thách gộp từng bot.
   - **M2. §12 trên 20 seed:**
     ```bash
     TMPDIR="$PWD/../tmpdir" nice -n 15 node --import tsx scripts/td/balance.ts \
       --stage-seeds=12 --stage-sets=1 --seeds=20 --nights=4 --threads=4 --modes=balanced > ../runs/C-g12x20.md 2> ../runs/C-g12x20.err
     ```
     Lấy bảng "Cổng `BUILD_1A6.md` §12": cổng 4 (mạng từng seed, thấp nhất và seed nào), 5a, 5b, 5c, 6, 7, và 5a theo Thư giãn, Thử thách, Học.
   - **M3. Từng pha, seed 25–48, ba chế độ** (như `measure.sh`). Chép đầu dò vào bản chép (đầu dò import `../tests/td/flow`):
     ```bash
     mkdir -p probe && cp ../../mac-2026-10-27/open/a2-days/probes/pernight.ts probe/
     for m in balanced relax challenge; do
       TMPDIR="$PWD/../tmpdir" nice -n 15 node --import tsx probe/pernight.ts --from=24 --seeds=24 --modes=$m > ../runs/C-pn-$m.md 2>&1
     done
     ```
     Tiêu đề phải là "seeds 25–48". Lấy hàng "Đêm 1" (cột Mạng mất) mọi bot, ba chế độ; hàng "Đêm 3" (cột I) mọi bot, ba chế độ; bảng cuối (Qua 4 đêm, Thắng 5 đêm, S trung vị).
   - **M4. Đêm 1 trên 40 và 160 seed** (rẻ: chỉ Ngày 1 và Đêm 1):
     ```bash
     cp ../../mac-2026-10-27/open/a2-days/probes/night1.ts probe/
     TMPDIR="$PWD/../tmpdir" nice -n 15 node --import tsx probe/night1.ts --seeds=40 > ../runs/C-night1-40.md 2>&1
     TMPDIR="$PWD/../tmpdir" nice -n 15 node --import tsx probe/night1.ts --seeds=160 > ../runs/C-night1-160.md 2>&1
     ```
     Tiêu đề "seeds 1–40", "seeds 1–160". Lấy cột "Mạng mất Đêm 1" và "Ván mất ≥ 3" từng bot.
6. **Base phải ra số đã biết, trước khi so.** Đối chiếu từng ô ở bảng "Số đã biết":
   - base: seed 1–80 (cột "bộ 1" của bảng chặt ở M1) với cột gộp của `r22-balance.md`; §12 5 seed của M1 với `r22-balance.md`; M2 với `r22-g12x20.md`; M3 với `r22-pn-*.md` (mọi hàng, kể cả Đêm 5); M4 (40 seed) với `base-night1.md`.
   - pkg: seed 1–80 của M1 với cột gộp của `v2-balance.md`; §12 5 seed của M1 với `v2-balance.md`; M2 với `v1-g12x20.md`; M3 với `v1-pn-*.md` (chỉ Ngày 1–5, Đêm 1–4); M4 (40 seed) với `v1-night1.md`.
   - Ngưỡng: lệch > 0,05 s, > 0,5 điểm %, hay > 0,05 mạng là **lệch**. Thắng mỗi bot phải đúng từng ván (số ván tính như mục "Báo cáo không in số ván" ở "Đọc trước").
   - Có lệch: ghi ô nào, bao nhiêu, lên đầu báo cáo. Tìm nguyên nhân bằng git chỉ đọc, ví dụ `git -C games/typing-defense log --oneline e49189a..a2-days -- src tests/td scripts/td public/vocabulary` và `git -C games/typing-defense diff --stat e49189a a2-days -- src tests/td scripts/td public/vocabulary`. Vẫn đo tiếp. base → pkg vẫn so được (cùng cây), nhưng ghi rõ ô nào không khớp số cũ.
7. **Bảng** trong `226/summary.md` (và cùng số trong `226/summary.json`). Mỗi bảng base và pkg cạnh nhau:
   - **Dải chặt Cân bằng, 6 bot:** thắng bộ 1 / bộ 2 / gộp (ván/80, ván/80, ván/160 và ‰; số ván suy từ ô % như "Đọc trước" nói, kèm ô % in ra); Biên S cùng ba cột; đạt hay trượt. Thêm cột "cách mép": còn bao nhiêu ván nữa thì trượt (ví dụ 140/160 là cách trần 1 ván).
   - **B1–B8:** bộ 1, bộ 2 (dải BALANCE §3) và gộp (đích chặt). Cổng trượt thì ghi bot và chỉ số lệch, chép nguyên câu của báo cáo. B9: ghi "THIẾU SỐ" như báo cáo in; không giả số.
   - **Boss** (gộp, Cân bằng, 6 bot): boss rút, giao chiến p50, mạng mất ở đỉnh p50; G3, G8 từng bộ và gộp; G2, G5, G6 từ dòng "R2 gộp".
   - **§12 trên 20 seed:** 4 (thấp nhất, seed), 5a, 5b, 5c, 6, 7, 5a theo ba chế độ kia; cột "đạt" theo bảng. Thêm §12 trên 5 seed từ M1.
   - **Đêm 1, mạng mất:** từng bot × ba chế độ (seed 25–48); Cân bằng trên seed 1–40 và 1–160.
   - **Đêm 3, Nhàn I:** từng bot × ba chế độ (seed 25–48). Gói từng làm Nhàn I Đêm 3 tăng từ khoảng 20 % lên 31–35 % (Chuẩn, Ẩu).
   - **Thử thách:** thắng gộp từng bot, base và pkg.
   - Thời gian mỗi lệnh, số luồng, tải lúc bắt đầu.
   - Có thể viết `226/tools/summarize.mjs` (Node, không gói) đọc `226/runs/` và viết `summary.*`; chạy lại phải ra cùng kết quả.
8. **Kết luận cho lựa chọn (a)** ở đầu báo cáo, trả lời từng câu bằng số:
   - pkg có đạt dải chặt 78–88 % (cùng Biên S) cho cả sáu bot trên 160 ván gộp không? Bot nào sát mép, cách mấy ván.
   - B1–B8 của pkg: đạt ở từng bộ 80 seed và ở gộp không? Cổng nào trượt.
   - Mọi cổng §12 trên 20 seed của pkg có đạt không? Biên cổng 4 (mạng thấp nhất).
   - base: vẫn trượt 5a, 5b trên 20 seed? Dải chặt của base trên 160 ván?
   - Đọc số: sai số chuẩn của tỉ lệ thắng trên 160 ván ở 83 % là khoảng 3,0 điểm (trên 80 ván khoảng 4,2). Nói rõ ván nào của bot nào quyết định kết quả.
   - Ghi hai điều vẫn chờ chủ dự án, dù số đạt:
     - luật "gặt ban Đêm không lời gọi" (h0) mở rộng luật gỗ của chủ dự án, cần chủ dự án đồng ý trước khi vào luật;
     - gói làm Đêm 3 nhàn hơn (số ở bảng Đêm 3), và gói "/" còn 4 byte (84.996 byte, theo `open-items.md`; phiếu này không build).
   - Không đề xuất đổi số. Không sửa game.
9. **Chép và dọn.**
   - Chép nguyên mọi file trong `$W/runs/` (kể cả `.err`, `patch.log`, `timeline.txt`) và `$W/refs.txt` vào `226/runs/`. So SHA-256 từng cặp; ghi vào `226/runs.sha256`.
   - Lưu diff hai bản chép: `(cd "$W" && diff -ru -x node_modules -x probe base pkg) > docs/codex-queue/226/base-pkg.diff` (mã thoát 1 là bình thường: hai cây khác nhau).
   - Rồi in danh sách sẽ xóa (`find "$W" -maxdepth 2 | sort`) vào báo cáo, và xóa `$W` (`rm -rf games/typing-defense/tmp/codex-226`). Chỉ xóa thư mục này; nó do phiếu tạo ra.

## Cấm

- Ghi trong `games/typing-defense` ngoài `tmp/codex-226/`. Sửa file của game, kể cả trong bản chép, ngoài việc áp gói vào `pkg`.
- `--set`, đổi số, đổi luật, đổi bot hay dải đích. Thêm biến thể. Đề xuất số mới thay chủ dự án.
- Mọi lệnh git có ghi. Được: `rev-parse`, `archive`, `diff`, `log`, `show`, `status`, `branch --show-current`. Không `git apply` vào repo nào (kể cả `--check` lên cây làm việc thật).
- Đụng worktree nào (`games/.wt-*`) hay checkout chính ngoài `tmp/codex-226/`. Đọc `games/typing-defense/tmp/codex-224/` (phiếu 224) hay bất kỳ thư mục `tmp/` nào khác ngoài `tmp/mac-2026-10-27/open/a2-days/` (chỉ đọc).
- `heavy.sh` (ghi `/tmp`), `pnpm install`, `vitest` (ghi bộ nhớ đệm vào `node_modules` của checkout chính), dev server, trình duyệt, mạng.
- Quá 4 luồng; hai lệnh `balance.ts` cùng lúc.
- Ghi ra ngoài repo. Đụng game khác, Tu Tiên.

## Kiểm (ghi số)

1. `src/sim` + `src/content`, `a2-days` so với `td-1c`: 0 file khác (`diff --stat` rỗng). Lưu lệnh và đầu ra.
2. `(cd "$W" && diff -ru -x node_modules base pkg)`:
   - đúng 5 file: `src/content/rules.ts`, `src/content/slice-1a.ts`, `src/sim/systems/economy.ts`, `src/sim/systems/waves.ts`, `tests/td-sim-economy.test.ts`;
   - 11 khối; 45 dòng `+`, 15 dòng `-` (theo file: `rules.ts` +2/−2, `slice-1a.ts` +6/−6, `economy.ts` +5/−5, `waves.ts` +2/−2, test +30/−0);
   - các dòng `+`/`-` (bỏ `+++`, `---`), sắp xếp, giống hệt các dòng `+`/`-` của gói: `cmp` hai danh sách, mã 0.
3. Base và pkg so với "Số đã biết": số ô khớp, số ô lệch, lệch lớn nhất (giây, điểm %, mạng). Ghi trước mọi so sánh base → pkg.
4. Lệnh chạy:
   - mọi lệnh mã thoát 0;
   - tiêu đề mỗi báo cáo có seed và bộ đúng như M1–M4;
   - giờ bắt đầu, giờ xong và `uptime` trước mỗi lệnh (`timeline.txt`);
   - ≤ 4 luồng (≤ 2 khi tải 1 phút > 10), ghi số luồng thật.
5. Bảng ở Việc 7 đủ: dải chặt từng bot (ván/160 và ‰); B1–B8 từng bộ và gộp; §12 4/5a/5b/5c/6/7; Đêm 1 mạng mất từng bot và chế độ; Đêm 3 Nhàn I. Với mỗi ô thắng gộp của sáu bot (base và pkg): số ván bộ 1 + bộ 2, `pct` tính lại khớp ô in ra, đạt/trượt tính lại khớp cột "Đích chặt 1B" (12 ô, ghi số ô khớp).
6. `git -C games/typing-defense status --short` và `branch --show-current` trước và sau giống nhau (lúc soạn phiếu: sạch, `a2-days`). Khác vì làn khác thì ghi rõ file nào.
7. `226/runs.sha256`: mọi file chép khớp bản gốc. Danh sách đã xóa có trong báo cáo; `games/typing-defense/tmp/codex-226` không còn.
8. `git status --short -uall -- docs/codex-queue` ở repo cha: phần của phiếu này chỉ là `226-report.md` và `226/`.

## Báo cáo phải có

- Kết luận cho lựa chọn (a) (Việc 8), đặt đầu tiên.
- `refs.txt`, SHA-256 của gói, log `patch` (dòng fuzz), kết quả Kiểm 1–2.
- Bảng đối chiếu với "Số đã biết" (Kiểm 3).
- Các bảng của Việc 7, base và pkg cạnh nhau.
- Thời gian, luồng, tải; danh sách file trong `226/`.
- Câu nói rõ: mọi số là của bot; B9 cần người thật chơi; phiếu không đổi game; h0 cần chủ dự án đồng ý.

**Xong khi:** mỗi bản chép đo đủ M1–M4 (bảy lệnh), base khớp số đã biết (hay lệch được ghi và tìm nguyên nhân), tám mục kiểm có số, báo cáo trả lời được lựa chọn (a) bằng số trên 160 ván. Claude đọc báo cáo, chuyển số cho chủ dự án, rồi commit `docs/codex-queue/226*`.
