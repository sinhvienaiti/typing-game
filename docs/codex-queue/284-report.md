# Báo cáo phiếu 284 · Vòng ngọc: nắp mềm và giữ vệt bóng

Hoàn tất phần code ngày 05/11/2026 trong `games/.wt-immortality-cultivation-codex`, nhánh `codex/jade-ring-material`, nền `453fd43`. Không chạy lệnh Git ghi, không mở cổng mạng, không sửa checkout chính hay các liên kết `node_modules`/`art-src`.

## Tệp đã ghi

Các đường dẫn dưới đây tính từ worktree, trừ báo cáo ở repo cha:

- `src/view/skills/sword-material.ts`: nắp mềm CPU/shader, uniform knee và đường sheen.
- `src/lab/skills-main.ts`: cờ URL, API knee và thống kê mới của `ringCap()`.
- `tests/view/jade-ring.test.ts`: cập nhật phép cắt cũ, kiểm thứ tự sheen, uniform, API và bộ đếm.
- `tests/view/jade-soft-cap.test.ts`: sáu test mới cho nắp mềm.
- `docs/changelog/2026-11-04-lab-jade-ring.md`: bổ sung cách tính, tham số và cách đọc số đo.
- Repo cha: `docs/codex-queue/284-report.md`.

## Thay đổi

Độ sáng vòng vẫn dùng Rec. 709 `(0.2126, 0.7152, 0.0722)`. Dưới điểm gối giữ nguyên; phía trên dùng đúng vai nén hàm mũ của phiếu, rồi nhân RGB theo `softCap(luma, knee, 0.95) / max(luma, 1e-4)`, với trọng số vòng như trước. Ánh mép tan `swRingDe` vẫn được trừ trước nắp và cộng lại sau nắp.

CPU xuất `softCap(y, knee, cap)` trong cùng tệp vật liệu; test và phép đo tổng hợp dùng hàm này. Shader và CPU cùng có bảo vệ làm tròn `min(kết_quả, cap − 1e-7)` ở nhánh trên knee: nếu không có bảo vệ, số hữu hạn lớn có thể cho kết quả bằng đúng cap khi `exp` quá nhỏ. Sai khác với công thức lý tưởng tối đa `1e-7`; ở knee mặc định, bảo vệ chỉ tác động từ độ sáng khoảng 4,089 trở lên. Trần vẫn giữ 0,95.

Sheen GGX nhám 0,12 được cộng vào `outgoingLight` **sau** bước headroom cũ, **trước** nắp mềm, chỉ theo trọng số ngọc và `jadeSheen`. Vì không còn đưa vào `swJadeE`, nền đã sáng trên 0,95 không xóa vệt bóng. Các phép tính headroom của ánh ngọc cũ, mặt nạ, độ mềm mép và ánh dissolve giữ nguyên.

- `?jadeKnee=0.72` hoặc `__lab.jadeRing({ knee: 0.72 })`: mặc định 0,72, kẹp trong [0; 0,94] để luôn có `knee < cap`.
- `__lab.jadeRing()` trả thêm `knee`; cập nhật từng phần giữ các trường khác, bỏ qua NaN/Infinity.
- `__lab.ringCap()` trả thêm `jadePixels`, `jadeAbove094`, `jadeAbove094Ratio`. Tỉ lệ 0–1 tính số điểm ảnh ngọc thuần có độ sáng **> 0,94** trên toàn bộ điểm ảnh ngọc thuần hữu hạn, gồm điểm không đổi giữa hai lượt. Loại vàng, biên pha và NaN/Infinity; không có ngọc thì trả 0.
- Các trường chẩn đoán cũ giữ ý nghĩa. `MASK=1` và `ring-parity.mjs` vốn giữ nguyên đối tượng kết quả nên tự mang theo các trường mới; không cần sửa hai script.

## Kiểm bắt buộc

Chạy trong worktree; dùng bộ khóa CPU sẵn có của repo, lần lượt từng kiểm nặng:

```sh
../../.local/bin/heavy.sh --cores=2 node node_modules/typescript/bin/tsc --noEmit -p .
VITEST_MAX_THREADS=4 ../../.local/bin/heavy.sh --cores=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4
```

- TypeScript: thoát 0, không lỗi.
- Vitest: **939/939 test, 88/88 tệp**, thoát 0; thời gian 8,61 giây. Trong đó 16 test vòng hiện có và 6 test nắp mềm đều qua.
- Test mới kiểm liên tục và đạo hàm đơn vị ở hai phía knee, tăng nghiêm ngặt qua vai nén và không giảm qua toàn dải số, đầu ra dưới cap với các mẫu hữu hạn từ số nhỏ nhất đến `Number.MAX_VALUE`, cả sai số float và underflow hàm mũ. Kiểm đối chiếu trực tiếp thân hàm GLSL đã vá với CPU.
- Đĩa sáng tổng hợp gồm **28.608 điểm**, nét chạm theo góc, độ sáng theo bán kính và vệt phản chiếu hẹp: **22.744 điểm ≥ 0,94 (79,5022%)** với nắp cứng; **0 điểm (0%)** với nắp mềm. Độ sáng sau nén trải từ **0,825371 đến 0,936255**, vẫn giữ tỉ lệ màu RGB.
- Trên nền sáng 1,05, sheen có đỉnh đầu vào `0,18 × 0,6` tạo chênh độ sáng **0,0205269** sau nén; headroom cũ cho 0. Tổng nền và sheen dưới 0,95; ánh mép tan cộng ngoài nắp giữ nguyên.
- Test bộ đếm kiểm cả ngọc không đổi, vàng, biên pha, NaN/Infinity, hai phía 0,94, mẫu rỗng và khôi phục trạng thái khi đọc GPU lỗi.

Build dùng nguyên bộ bọc `.local/codex-runs/274-out/build-no-cache.mjs`, chỉ thay chuỗi số phiếu `274` thành `284` **trong bộ nhớ**, không sửa hay tạo wrapper. Lệnh đã chạy:

```sh
IC_VITE_CACHE_DIR=/private/tmp/codex-284-dist/.vite-cache ../../.local/bin/heavy.sh --cores=2 node --input-type=module - --no-cache --configLoader runner --outDir /private/tmp/codex-284-dist <<'JS'
import { readFileSync } from 'node:fs';
const wrapper = readFileSync('../../.local/codex-runs/274-out/build-no-cache.mjs', 'utf8').replaceAll('274', '284');
await import(`data:text/javascript;base64,${Buffer.from(wrapper).toString('base64')}`);
JS
```

Vite 7.3.7 build đạt, 183 module, 884 ms. `grep -rlE 'jadeKnee|jadeRingGlow|ring-parity|jadeSheen' /private/tmp/codex-284-dist` thoát **1**, không có kết quả. Đã xóa toàn bộ `/private/tmp/codex-284-dist`, gồm cache riêng. Cảnh báo outDir nằm ngoài project là thông báo thông thường của Vite; wrapper đã kiểm thư mục chưa tồn tại trước khi build.

`git diff --check` đạt. `git status --short` trong worktree chỉ có năm tệp đã nêu và `?? node_modules` có sẵn từ đầu; không có `art-src` khi nhận phiếu. Báo cáo là tệp mới ở repo cha; các thay đổi của agent khác giữ nguyên.

## Phần Claude làm tiếp

Chưa chạy trình duyệt, chưa chụp ảnh/video và chưa kết luận Kiểm 9 vì phiếu giao phần này cho Claude, đồng thời cấm Codex mở cổng. Claude chỉnh `knee` và `sheen`, kiểm thực tế trong lab với Kim/Hỏa, kiểm lại tràn mép rồi gửi tấm so cho anh trước khi gộp. Các số tổng hợp ở trên xác nhận hành vi toán học, không thay nghiệm thu hình trong lab. Không có phần code bắt buộc nào bỏ dở.
