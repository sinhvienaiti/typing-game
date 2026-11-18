# Phiếu 209 · Last Line · Một vòng chỉnh cân bằng ải 1 (`c1-s1`) bằng `--set`: seed 1–100 và 101–200, đủ chỉ số BALANCE §3 và B1–B9

**Nguồn:**
- `docs/games/MAP1_PRODUCTION.md` §3.2 mục 9: "**TS-M1-12** · P1 · G6. Ải 1 quá dễ; B1, B6, B7 trượt; Thử thách đảo thứ bậc."
- Kiểm kê 28/10 (`docs/games/map1/audit-2026-10-28.json`, Last Line, cổng G6). Báo cáo gốc: `games/typing-survival/tmp/map1-audit/balance-c1s1-seeds1-100.md` và `-seeds101-200.md` (main `bf0e6f9`):
  - Cân bằng: Chậm chắc, Chuẩn, Khá, Nhanh thắng 92–96 %, S 68–76 % trên seed 1–100; thắng 82–92 % trên seed 101–200. Dải đích: thắng 75–90 %, S 35–65 %.
  - B6 ở Cân bằng chỉ +6 và +9 điểm (cần ≥ +10).
  - B7: ô Chuẩn tắt nhịp có S 73–78 %.
  - Thử thách đảo thứ bậc: Nhanh thắng 36 / 44 %, Mới thắng 59 / 51 %.
- N13 trong `games/typing-survival/docs/changelog/2026-10-27-test-pass.md`: chưa sửa, chờ "người điều phối chốt số biến thể mỗi vòng".
- Luật chủ dự án (`docs/games/BALANCE.md` đầu file, 23/10; nhắc lại 27/10): cân bằng theo nhiều yếu tố. Mỗi thay đổi báo đủ chỉ số §3 cho cả bộ bot ở mọi chế độ, không chỉ một tỉ lệ thắng. Không đạt cổng bằng một số chung duy nhất.
- Chủ dự án 30/10: "tăng thêm việc cho codex cho tôi".

**Người điều phối chốt cho vòng này:** một mốc và **tối đa 6 biến thể**. Mỗi biến thể chạy đủ hai bộ 100 seed. Đây là câu trả lời cho `games/typing-survival/AGENTS.md` ("the coordinator sets how many variants a tuning round may hold") và mục "Còn lại" 1 của `2026-10-26-s1-r1-review-fix.md`.

Không trùng 104, 104b (chỉ nhãn chữ). Chưa phiếu nào làm TS-M1-12 hay N13.

**Loại phiếu:** báo cáo. Chỉ đo trên bản chép; không sửa file nào của game. Đưa số đã chọn vào `src/content` là phiếu sau, hoặc việc của Claude (làn T).

**Báo cáo:** `docs/codex-queue/209-report.md` (tiếng Việt), thư mục `docs/codex-queue/209/`. Cả hai ở repo cha.

## Nơi làm

- **Không worktree.** Dùng bản chép chỉ đọc của nhánh `main` Last Line, đặt trong `tmp/` của game (Git bỏ qua `tmp/`). Không đụng worktree nào, nên chạy được song song với phiếu khác.
- cwd của làn: gốc repo cha (`.`).
- **Chỉ được ghi:** `games/typing-survival/tmp/codex-209/`, `docs/codex-queue/209/`, `docs/codex-queue/209-report.md`.
- Dựng bản chép:
  ```bash
  SRC=games/typing-survival
  W=$SRC/tmp/codex-209
  mkdir -p "$W/main" "$W/runs" "$W/tmpdir"
  git -C "$SRC" rev-parse main > "$W/main.commit"
  git -C "$SRC" archive main | tar -x -C "$W/main"
  ln -s ../../../node_modules "$W/main/node_modules"
  ```
- `node_modules` là liên kết tới bản checkout chính. Thiếu `$SRC/node_modules/tsx` thì dừng, ghi vào báo cáo. Không `pnpm install`.
- Mọi lệnh chạy trong `$W/main`, với `TMPDIR="$PWD/../tmpdir"`. Như vậy bộ nhớ đệm của `tsx` nằm trong repo. Sandbox Codex không ghi được ra ngoài repo (bài học phiếu 189).
- Không dùng `.local/bin/heavy.sh`: nó ghi trạng thái vào `/tmp`. Thay bằng `nice -n 15` và luật số tiến trình ở Việc 5.

## Đọc trước

- `docs/games/BALANCE.md`: §3 (chỉ số, dải đích), §4.2 (bộ điều nhịp, trần), §7 (B1–B9), §9.3.
- `games/typing-survival/AGENTS.md`: mục "Balance", "R1 gate state", "Next".
- `games/typing-survival/docs/changelog/2026-10-26-s1-r1-review-fix.md`: "Còn lại"; mục 4 (hai bộ seed lệch tới 16 điểm thắng); mục 21 (ngân sách biến thể).
- `games/typing-survival/docs/changelog/2026-10-27-test-pass.md`: hàng N13, n10, n24.
- Trong bản chép:
  - `scripts/balance.ts`, `balance-lib.ts`, `overrides.ts`, `rollup.ts`;
  - `src/content/chapter-1.ts` (ải `c1-s1`), `stage-rules.ts`;
  - `src/content/balance.ts` (`MODE_SPECS`, `PACE_GAIN`), `rules.ts` (`DRAIN`, `SCOUT`), `guns.ts` (`TIA_DUTY`).
- Mốc 28/10: `games/typing-survival/tmp/map1-audit/balance-c1s1-seeds1-100.md`, `.json`, `balance-c1s1-seeds101-200.md`.
- Tên bot trong báo cáo: `novice` Mới, `steady` Chậm chắc, `standard` Chuẩn, `skilled` Khá, `sloppy` Ẩu, `fast` Nhanh, `child` Trẻ em, `no-type` Không gõ, `type-only` Chỉ gõ, `standard@good` / `standard@poor` Chuẩn chiến thuật Tốt / Kém (11 bot), cộng hàng `standard (tắt nhịp)`.

## Núm được dùng (chỉ qua `--set`, số đã có)

| Đường `--set` | Giá trị ở `main` | Tác dụng | Phạm vi |
|---|---|---|---|
| `c1-s1.drainRate` | 2 | rỉ giáp ở vòng gần, × `DRAIN.perFoe` | chỉ ải 1 |
| `c1-s1.drainFrom` | 14 | rỉ bắt đầu từ bao nhiêu mét | chỉ ải 1 |
| `c1-s1.calm.0.rate` | 4,4 | nhịp sinh nền cả ải | chỉ ải 1 |
| `c1-s1.scouts.share` | 0,12 | phần lính trong toán thường (lính bắn đạn trừ giáp) | chỉ ải 1 |
| `c1-s1.packs.brute.share`, `.from` | 0,06; 80 | toán Trâu | chỉ ải 1 |
| `c1-s1.surges.0.*`, `c1-s1.surges.1.*`: `at`, `seconds`, `rate`, `lull`, `lullRate` | 50 / 115; 8; 8,5; 4; 1,5 | hai đỉnh tràn: giờ, độ dài, độ dày, quãng lặng sau đỉnh | chỉ ải 1 |
| `c1-s1.storm.chance` | 0,15 | xác suất đỉnh dữ dội | chỉ ải 1 |
| `MODE_SPECS.challenge.rate`, `.surge`, `.speed`, `.drain` | 1,12; 1,1; 1,06; 1,15 | hệ số của Thử thách | **mọi ải** ở Thử thách |
| `PACE_GAIN.surge`, `.speed` | 1; 0,2 | nhịp k phóng đỉnh tràn và tốc quái bao nhiêu | **mọi ải, mọi chế độ** |
| `TIA_DUTY.*` | `zone` 10, `near` 4, `scout` 3, `sweep` 1,5, `retarget` 15 | Tia trực | **mọi ải**; chỉ dùng khi ứng viên trượt G3c |

- Đường bắt đầu bằng tên ải chép đối tượng trước khi ghi, nên chỉ ải 1 đổi (`overrides.ts`). Đường bắt đầu bằng tên hằng đổi mọi nơi.
- `=` đặt số, `*=` nhân. Trong zsh để cả chuỗi trong nháy đơn.
- Dòng `--set: … old→new` đầu stderr phải khớp từng đường. Sai thì sửa chuỗi rồi chạy lại. Lần chạy hỏng không tính là biến thể.

## Việc

1. **Chạy khói.** V0 (không `--set`), `--seeds=2`, một bộ. Chỉ để thấy bản chép chạy được. Không tính biến thể, không vào bảng.
2. **Mốc V0** trên hai bộ seed. Lệnh mẫu cho bộ 1–100:
   ```bash
   cd games/typing-survival/tmp/codex-209/main
   TMPDIR="$PWD/../tmpdir" nice -n 15 node --import tsx scripts/balance.ts \
     --stages=c1-s1 --seeds=100 --first=1 --g3c \
     --json=../runs/v0-s1.json --out=../runs/v0-s1.md > /dev/null 2> ../runs/v0-s1.err
   ```
   - Bộ thứ hai: `--first=101`, tên file `v0-s101.*`.
   - Mặc định của lệnh đã là ba chế độ, 11 bot, Chuẩn tắt nhịp. Không truyền `--bots`, `--modes`, `--off`.
   - Biến thể: thêm `--set='…'`, đổi `v0` thành `v1` … `v6`.
3. **So mốc với 28/10.** Mỗi ô Cân bằng và Thử thách: thắng, S, P, I của V0 so với báo cáo 28/10.
   - Cùng seed và sim không đổi thì phải ra giống hệt. Mỗi ô lệch ≤ 4 điểm thắng thì coi là khớp.
   - Lệch hơn: tìm nguyên nhân bằng git chỉ đọc, ví dụ `git -C games/typing-survival log --oneline bf0e6f9..main -- src/sim src/content tests/survival public/vocabulary scripts`. Ghi vào báo cáo. Vẫn làm tiếp, lấy V0 mới làm mốc.
4. **Biến thể: tối đa 6, mỗi biến thể một ý, mỗi biến thể đủ hai bộ seed.** Lần chạy nào đổi số đều là một biến thể, kể cả lượt thử ngắn. Không có lượt 40 seed ngoài ngân sách.
   - **Đợt A, sức ép đều và nhịp đỉnh tràn ở ải 1** (số cố định):
     - V1, rỉ mạnh hơn: `c1-s1.drainRate=2.4`.
     - V2, dòng nền dày hơn: `c1-s1.calm.0.rate=4.8`.
     - V3, đỉnh tràn dài hơn, quãng lặng ngắn hơn: `c1-s1.surges.0.seconds=10,c1-s1.surges.1.seconds=10,c1-s1.surges.0.lull=2,c1-s1.surges.1.lull=2`.
   - **Chọn nền B** trong V0–V3: ít ô B1 lệch nhất (cộng hai bộ seed). Hòa thì lấy B6 Cân bằng lớn hơn, rồi biên B3 lớn hơn. Ghi bảng chọn vào báo cáo.
   - **Đợt B, Thử thách** (nền B cộng một ý):
     - V4: chuỗi của nền B, thêm `MODE_SPECS.challenge.surge=1.0,MODE_SPECS.challenge.rate=1.06`.
     - V5: chuỗi của nền B, thêm `PACE_GAIN.surge=0.7`.
   - **Đợt C, một biến thể cuối (V6)** do Codex chọn từ số của V1–V5. Ví dụ: ghép ý tốt nhất của A với ý tốt nhất của B; đổi cỡ bước của ý tốt nhất (nửa bước hay rưỡi bước); thêm một số `TIA_DUTY` nếu ứng viên trượt G3c. Ghi lý do bằng số **trước** khi chạy.
   - Chỉ dùng núm trong bảng trên. Không thêm đỉnh tràn thứ ba (review-fix mục 4: thêm một đỉnh là thêm một vực).
5. **Máy dùng chung.**
   - Mỗi báo cáo là một tiến trình Node một luồng. Tối đa **6 tiến trình cùng lúc**.
   - Trước mỗi đợt ghi `uptime`. Tải 1 phút > 10 thì chạy tối đa 3 cùng lúc.
   - Mốc 28/10: 204 s một báo cáo. Cả vòng là 14 báo cáo, khoảng 50 phút máy.
   - Ghi giờ bắt đầu và kết thúc mỗi đợt. Test thời gian ở làn khác có thể đỏ trong lúc này; Claude đối chiếu theo giờ.
6. **Bảng mỗi biến thể** trong `209/summary.md`, hai bộ seed cạnh nhau (`1–100 / 101–200`):
   - Bảng §3: mỗi bot × chế độ, cộng Chuẩn tắt nhịp. Cột: thắng, S, P, I, O, N, Q, bậc/đợt, khoảng sinh thấp–cao, mất giáp rỉ/chạm/đạn (đọc từ `.md`). Dấu ↓ / ↑ khi ra ngoài dải.
   - Cổng:
     - B1: ô lệch và chỉ số lệch;
     - B2; B3 (Mới ở Cân bằng, Trẻ em ở Thư giãn);
     - B4 (S Chậm chắc so với Ẩu; thời gian hạ quái Chuẩn so với Ẩu); B5;
     - B6: Tốt − Kém, tính bằng điểm, ở Cân bằng và Thử thách;
     - B7: bậc/đợt lớn nhất, khoảng sinh, ô Chuẩn tắt nhịp ở Cân bằng so với dải;
     - B8;
     - B9: ghi "THIẾU SỐ: cần người thật chơi". Không giả số.
   - Cổng S1 của báo cáo: G3c (kém nhất, tốt nhất, khoảng cách), G3m, G5, G8, §7.6.
   - Thứ bậc Thử thách: thắng của Mới, Chậm chắc, Chuẩn, Khá, Ẩu, Nhanh.
   - Thời gian chạy mỗi báo cáo (dòng "cả lệnh … s").
7. **Bảng tổng** ở đầu `summary.md`, mỗi biến thể × bộ seed một hàng:
   - chuỗi `--set`; số ô B1 lệch;
   - B6 Cân bằng; B6 Thử thách;
   - ô Chuẩn tắt nhịp ở Cân bằng (thắng, S);
   - B3: Mới ở Cân bằng, Trẻ em ở Thư giãn;
   - G3c kém nhất / tốt nhất;
   - Nhàn I của Khá và Nhanh ở Cân bằng;
   - Thử thách: Nhanh − Mới (điểm thắng);
   - thời gian chạy.
8. **JSON và Markdown** trong `docs/codex-queue/209/`:
   - `runs/v<n>-s1.json`, `.md`, `.err` và ba file `v<n>-s101.*`: đầu ra nguyên của `balance.ts`;
   - `summary.json`: mỗi biến thể × bộ seed có chuỗi `--set`, các dòng `old→new`, kết quả từng cổng, các số của bảng tổng;
   - `summary.md`;
   - `tools/summarize.mjs`: script Node không cần gói, đọc `runs/`, viết `summary.*`. Chạy lại ra đúng cùng kết quả.
9. **Khuyến nghị** (trong báo cáo). Một biến thể "đạt" khi trên **cả hai** bộ seed:
   - B1: mọi bot Mới tới Nhanh ở Cân bằng nằm trong dải (thắng, S, P, I, O). Ô lệch ≤ 3 điểm ở chỉ một bộ thì ghi "sát mép", không tính trượt (luật của `rollup.ts`);
   - B2, B3, B4, B5, B8 đạt;
   - B6 ≥ +10 điểm ở Cân bằng và ở Thử thách;
   - B7: ≤ 3 bậc/đợt, khoảng sinh trong ±15 %, ô Chuẩn tắt nhịp ở Cân bằng trong dải (cùng luật sát mép);
   - G3c (kém nhất ≥ 60 %, tốt nhất ≤ 97 %, cách nhau ≤ 30 điểm), G3m, G5, G8, §7.6 đạt;
   - Thử thách không đảo: Khá và Nhanh thắng không thấp hơn Mới quá 5 điểm. Ghi thêm số ô Mới–Nhanh dưới 50 %.

   Sau đó:
   - **Có biến thể đạt:** chọn một. Nhiều biến thể đạt thì chọn biến thể đổi ít số nhất.
     - Liệt kê việc Claude phải làm: file, hằng, số cũ → mới trong `src/content`.
     - Nói rõ thứ gì sẽ đổi: số `c1-s1.*` đổi băm chương của ải 1. `MODE_SPECS`, `PACE_GAIN` đổi cả ải 2–4: cần một báo cáo `--stages=c1-s1,c1-s2,c1-s3,c1-s4` trước khi commit (phiếu sau, không chạy ở đây). `TIA_DUTY` đổi cả ván vàng `s0-trace`.
   - **Không biến thể nào đạt:** nói rõ vì sao. Ghi biến thể gần nhất, cổng chặn, số chặn trên mỗi bộ seed.
   - **Luật §5.1 cho bến đầy** (`games/typing-survival/docs/BUILD_S1.md` §5.1; review-fix "Còn lại" mục 2; đổi luật, ngoài phạm vi): kết luận "cần" hay "chưa cần", kèm số. Ghi "cần" khi ở biến thể gần nhất Khá hay Nhanh vẫn có Nhàn I > 10 % ở Cân bằng trên một bộ seed, hoặc Thử thách vẫn đảo.
   - Núm nào làm khó một phía tốc gõ mà dễ phía kia (ví dụ Mới khó hơn, Nhanh dễ hơn) thì ghi rõ. Một núm không thay được đối trọng cho cả hai phía.
10. **Dọn.** Chạy Kiểm 5 (cần `main/` và `verify/`) trước. Chép đầu ra vào `209/` xong thì xóa `tmp/codex-209/main/`, `tmpdir/`, `verify/`. Chỉ xóa file mình tạo. Giữ `runs/` và `main.commit`.

## Cấm

- Mọi lệnh git có ghi. Chỉ được `archive`, `rev-parse`, `log`, `diff`, `show`, `status`.
- Sửa bất kỳ file nào của game, kể cả trong bản chép (`scripts/`, `src/content`, `tests/golden`). Đổi số chỉ qua `--set`.
- Đổi luật (bến đầy §5.1, nhịp bắn nền, đỉnh tràn thứ ba), tham số bot, dải đích, số trong `src/kit`.
- Đổi bộ của người chơi: `c1-s1.kit.*` (giáp, số bến, cấp Rèn). Đó không phải sức ép.
- Quá 6 biến thể. Quá 6 tiến trình cùng lúc.
- Chạy ải khác ngoài `c1-s1`.
- `pnpm install`, mạng, dev server, trình duyệt, `heavy.sh`.
- Ghi ra ngoài repo.
- Đụng worktree khác (`games/.wt-*`), game khác, Tu Tiên.

## Kiểm (ghi số)

1. Mốc: commit `main` (từ `main.commit`); số ô V0 lệch so với 28/10; lệch lớn nhất (điểm thắng, điểm S) ở mỗi bộ seed.
2. Mỗi JSON có **36 ô** (11 bot × 3 chế độ, cộng Chuẩn tắt nhịp × 3). Mỗi `.md` có G3c đủ 10 cặp. Số biến thể đã chạy ≤ 6.
3. Mỗi `.err` có đúng các dòng `--set: … old→new` của biến thể đó. V0 không có dòng nào.
4. Thời gian từng báo cáo; tổng giờ máy; số tiến trình cùng lúc; `uptime` đầu mỗi đợt; giá trị `TMPDIR` đã dùng.
5. Bản chép không đổi: giải nén lại cùng commit vào `tmp/codex-209/verify/`; `diff -r -x node_modules main verify` rỗng.
6. `git -C games/typing-survival status --short -uall` trước và sau: không có file nào của phiếu này. Khác vì làn khác thì ghi rõ.
7. `git status --short -uall docs/codex-queue` ở repo cha: chỉ `209-report.md` và `209/`.

**Xong khi:** mốc và tối đa 6 biến thể có đủ bảng trên hai bộ seed; JSON và Markdown ở `209/`; báo cáo khuyến nghị một biến thể kèm số cần đưa vào `src/content`, hoặc nói rõ vì sao không biến thể nào đạt và kết luận về luật §5.1; bảy mục kiểm có số. Không có changelog trong game, vì game không đổi; changelog đi cùng lượt đưa số vào `src/content`. Claude duyệt rồi commit `docs/codex-queue/209*`.

## Lưu ý

- B9 cần người thật chơi. Phiếu này không đo được.
- Hai bộ seed lệch nhau tới 16 điểm thắng (review-fix mục 4). Không kết luận từ một bộ.
- Mọi số ở đây là của bot. Khuyến nghị nói "bot đạt", không nói "người chơi thấy vừa".
