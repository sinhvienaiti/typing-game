# Báo cáo phiếu 279 · Sửa tỉ lệ dải và mép đầu nhát chém Hỏa

Thực hiện trong `games/.wt-ic-flame-slash`, từ HEAD `f3e7029`, một luồng theo lời giải đã chốt. Không tạo ảnh, âm thanh, server hoặc chạy lệnh Git ghi.

## Đã sửa

- `games/.wt-ic-flame-slash/src/view/skills/flame-slash.ts`: tính `uStripK` trong `set(...)` từ phép chiếu và bề rộng mẫu; đọc kích thước nguồn từ JSON bên cạnh ảnh; dự phòng 5; mép đầu mềm và rách theo nhiễu.
- `games/.wt-ic-flame-slash/src/view/skills/element-fire.ts`: chỉ sửa lời gọi `setStrip` và `set` cùng chú thích liên quan; bỏ số chu kỳ cố định, truyền camera của stage. `setStrip(texture, scroll)` giữ cấu hình ảnh và tốc độ cuộn; số chu kỳ được tính ở `set`.
- `games/.wt-ic-flame-slash/src/lab/skills-main.ts`: thêm duy nhất cờ `?stripK=<số dương hữu hạn>` và chú thích/import cần cho cờ. Không có bộ đọc URL này trong đường chơi.
- `games/.wt-ic-flame-slash/tests/view/flame-slash.test.ts`: 10 test, giữ phép kiểm nguyên đoạn tính lưỡi lửa cũ, cập nhật uniform và bổ sung các trường hợp bắt buộc.
- `games/.wt-ic-flame-slash/docs/changelog/2026-11-05-flame-slash-strip.md`: bổ sung thay đổi 279.
- `docs/codex-queue/279-report.md`: báo cáo này.

## Công thức

Metadata được đọc từ URL ảnh, đổi đuôi `.rgba.png` thành `.json`. Lấy **kích thước nguồn**, không dùng kích thước PNG đã đóng gói:

```text
A = mapping.periodPx / (2 × mapping.halfRows) = 600 / (2 × 150) = 2
L = hypot((ndcB.x − ndcA.x) × viewportWidth / 2,
          (ndcB.y − ndcA.y) × viewportHeight / 2)
W = 2 × (1,5 × h + 0,03) × 2,6 × halfPx × viewportHeight / 1080
uStripK = L / (A × W)
```

`h` là nửa bề rộng bình quân của bảng `tBand` đã đo và làm mềm, đúng các giá trị shader lấy mẫu. Khi chưa có bảng, `h = 0,34 × 2 / π`, bình quân của mặt nạ giải tích `0,34 × sin(πs)`. `W` là toàn bộ bề rộng tọa độ mẫu dải trong shader; không nhân thêm `WIDE` vì đó là phần mở rộng của lưới. Cung ở đây là cung đã trải thẳng bởi `QI_SLASH_VERTEX`, nên chiều dài trên màn là khoảng cách giữa hai đầu chiếu.

Thiếu camera, thiếu metadata, cung suy biến, bề rộng không hợp lệ, phép chiếu không hữu hạn hoặc đầu nằm sau camera: dùng `5`. Metadata lỗi không yêu cầu lặp mỗi khung; ảnh vẫn hiện bằng dải khi đã nạp. Ảnh còn chờ hoặc lỗi vẫn chạy nhánh lửa cũ như trước. Cờ lab hợp lệ ưu tiên hơn kết quả tự tính; bỏ cờ thì trở về tự tính.

Mép dải dùng `1 − smoothstep(tornFront − 0,07, tornFront, s)`, với `tornFront = uHead + 0,02 + (n − 0,5) × 0,02`. Xung đầu giữ nguyên hệ số, vị trí, giới hạn và hình mặt nạ; hệ số nhiệt dùng giá trị lớn hơn giữa mép mềm và xung đầu để đỉnh sáng tại `s = uHead` giữ nguyên. Nhánh lưỡi lửa cũ giữ ngưỡng bậc tương đương và toàn bộ phép tính cũ. Không sửa nhịp, ramp màu, xói hoặc mã hệ Kim.

## Kiểm

- `node node_modules/typescript/bin/tsc --noEmit -p .`: đạt, không lỗi.
- `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`: **985/985 test, 89/89 tệp đạt**; mốc 979, thêm 6 ca.
- Ba bộ số tổng hợp dùng viewport ngang/dọc 1920×1080, 1280×720, 1080×1920: tỉ lệ chu kỳ 2:1 đạt ±10% và phép kiểm chặt đến 5 chữ số thập phân; tăng đôi chiều dài thì `k` tăng đôi, tăng đôi bề rộng thì `k` giảm nửa. Có kiểm dự phòng 5 và shader không chứa `step(s, uHead`.
- Build Vite đạt, 183 module. `grep -rl stripK /private/tmp/codex-279-dist` không in gì, mã thoát 1 đúng nghĩa không tìm thấy. Đã xóa toàn bộ `/private/tmp/codex-279-dist`, kể cả cache riêng.
- `git diff --check`: đạt. `git status --short` trong worktree chỉ có 5 tệp được phép ở trên và `?? node_modules` đã có từ lúc giao; repo cha có thêm đúng tệp báo cáo của phiếu này trong phạm vi công việc. Không tạo link `art-src` hoặc `public`.

Lệnh build nguyên văn của phiếu bị bộ bọc 274 từ chối trước khi build, vì mã nguồn bộ bọc khóa cứng cả đối số `--outDir` và cache vào `codex-274-dist`. Đã chạy lại chính nội dung bộ bọc trong bộ nhớ, chỉ thay `codex-274-dist` thành `codex-279-dist`; giữ nguyên kiểm cache mới, `configLoader: "runner"` và các cờ được giao. Không sửa tệp bộ bọc. Lệnh thay thế đã đạt:

```sh
IC_VITE_CACHE_DIR=/private/tmp/codex-279-dist/.vite-cache node --input-type=module - --no-cache --configLoader runner --outDir /private/tmp/codex-279-dist <<'NODE'
import { readFileSync } from 'node:fs';
const wrapper = readFileSync('/Volumes/SS990TPRO/htdocs/typing-game/.local/codex-runs/274-out/build-no-cache.mjs', 'utf8');
await import('data:text/javascript,' + encodeURIComponent(wrapper.replaceAll('codex-274-dist', 'codex-279-dist')));
NODE
```

## Claude kiểm tiếp

Chưa quay video, chưa chấm hình ảnh hoặc tuyên bố đạt 8,5. Theo phiếu, Claude quay trước/sau ở camera chơi, kiểm hệ Kim trùng khít và gửi anh trước khi gộp. Tỉ lệ tự tính dùng bề rộng bình quân; phần đầu/cuối vẫn thuôn theo mặt nạ cũ. Cần xem độ liếm của dải và mép mềm trong chuyển động thực tế.
