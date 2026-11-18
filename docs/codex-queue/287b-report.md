# Báo cáo phiếu 287b · Giải xung đột gộp main vào lô 1 Hỏa

**Hoàn tất mã và toàn bộ kiểm tự động.** Hai tệp hết dấu xung đột; TypeScript qua; **1028/1028 test, 94/94 tệp** qua; build qua và đã xóa đầu ra. Không dùng lệnh Git ghi. Claude còn đánh dấu giải xung đột trong index, commit merge, đo cổng 7 và parity.

Worktree: `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`. HEAD giữ nguyên `07b73f626b964af05c63ee40944327d32b4b95f5`; MERGE_HEAD giữ nguyên `bbb46d8e20c6d340df214ad10dbb889271d19dd5`.

## Đã làm

| Tệp trong worktree | Kết quả |
| --- | --- |
| `src/view/skills/element-fire.ts` | Gộp `FIRE_LAB`, giữ toàn bộ brush/art lô 1/chớp tuổi 0/prewarm/đường mã cũ; nối texture chung của nhát chém mới. |
| `src/lab/skills-main.ts` | Giữ import và cờ brush/prewarm; thêm import `FlameSlash`, cờ `slash=tongues` và `stripK` của main. |
| `tests/view/fire-prewarm.test.ts` | Thêm 4 ca cho hai cờ độc lập, dải nạp muộn, dùng chung sampler, upload một lần trước compile và khôi phục trạng thái. Tổng tệp 9 ca. |
| `docs/changelog/2026-11-05-fire-lot1-art.md` | Ghi phần tích hợp và kết quả kiểm 287b. |

Báo cáo này ở repo cha: `docs/codex-queue/287b-report.md`.

Nhát chém và thẻ vạch cùng dùng **`strip-fire-sheath-v2.rgba.png`** qua thư viện `fire`, giữ lựa chọn ưu tiên của phiếu 277. Đã đối chiếu cả hai JSON: cùng `600 / (2 × 150) = 2`, nên công thức tỉ lệ nguồn 2:1 của main vẫn đúng. Bỏ lượt nạp bản thường qua `stage.texture()`. Khi ảnh về muộn, thư viện cấp cùng đối tượng texture cho cả hai vật liệu trước khi Promise prewarm hoàn tất; texture được upload một lần và mesh nhát chém được tạm hiện trong lượt compile scene thật đã có.

Hai cờ so sánh độc lập: `?fxcode=1` trả các lớp nhỏ về mã cũ nhưng nhát chém vẫn dùng dải; `?slash=tongues` chỉ trả nhát chém về lưỡi lửa cũ. Khi bật cả hai, không nạp dải không dùng.

Không sửa thêm `flame-slash.ts`, `element-stage.ts` hoặc `flame-slash.test.ts`: phần main tự gộp đã giữ nguyên công thức `uStripK`, mép đầu mềm và 10 ca của main; prewarm hiện có đã gồm mesh nhát chém và các biến thể màn hình/HDR. `git diff MERGE_HEAD -- src/view/skills/flame-slash.ts tests/view/flame-slash.test.ts` rỗng.

## Kiểm bắt buộc

Chỉ chạy trong worktree được giao, công việc nặng lần lượt qua `.local/bin/heavy.sh` của repo cha.

1. **PASS:** `grep -rn '^<<<<<<<\|^>>>>>>>' src tests` không có dòng nào, thoát 1 theo quy ước grep khi không khớp. Đã kiểm thêm dấu phân cách `=======` của merge.
2. **PASS**, thoát 0: `node node_modules/typescript/bin/tsc --noEmit -p .`.
3. **PASS**, thoát 0: `VITEST_MAX_THREADS=4 …/heavy.sh --cores=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`. **1028/1028 test, 94/94 tệp**, gồm `flame-slash.test.ts` 10 ca, `fire-prewarm.test.ts` 9 ca, `fire-lot1-art.test.ts` 7 ca, `skill-prewarm-shared.test.ts` 14 ca và `key1-flash-age0.test.ts` 3 ca. Thời gian suite 12,06 giây; bắt đầu 14:23:44 ngày 05/11/2026.
4. **PASS build**, thoát 0: wrapper `.local/codex-runs/274-out/build-no-cache.mjs`, chỉ thay `/private/tmp/codex-274-dist` thành `/private/tmp/codex-287b-dist` trong bộ nhớ; giữ cờ `--no-cache --configLoader runner --outDir`, cache riêng `IC_VITE_CACHE_DIR=/private/tmp/codex-287b-dist/.vite-cache` và điều kiện thư mục mới. Không sửa wrapper trên đĩa. `grep -rn -E 'fxcode|stripK|prewarmReport' /private/tmp/codex-287b-dist` không có kết quả; đã xóa thư mục và kiểm không còn tồn tại.
5. **PASS:** `git diff --check` sạch. HEAD/MERGE_HEAD giữ nguyên; hai link `?? art-src`, `?? node_modules` giữ nguyên.

## Bàn giao

- Index vẫn hiện `UU src/lab/skills-main.ts` và `UU src/view/skills/element-fire.ts` vì phiếu cấm `git add`. Nội dung làm việc đã giải xung đột; Claude cần add từng tệp rồi commit merge sau khi kiểm.
- Các tệp có sẵn từ merge (`flame-slash.ts`, `flame-slash.test.ts`, changelog nhát chém) được giữ nguyên. Không ghi ngoài bốn tệp trong bảng và báo cáo này; không sửa link, media, wrapper, game chính hoặc thay đổi của luồng khác.
- Không mở cổng, chạy trình duyệt, đo GPU hoặc tạo video: phiếu giao cổng 7 và parity cho Claude. Cần xem nhát chém dùng dải chung `-v2` trên nhánh đã gộp, đo cổng 7 và parity rồi mới đưa lên main. Chưa tuyên bố nghiệm thu hình ảnh/GPU.
- Không có phần dừng vì hạn mức hoặc giờ phải chờ.
