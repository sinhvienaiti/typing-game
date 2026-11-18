# Báo cáo phiếu 275 · Dải Firefly cho nhát chém kết phím 7 hệ Hỏa

**Trạng thái: hoàn tất phần mã và kiểm tự động. Chưa nghiệm thu hình ảnh; Claude kiểm trình duyệt và gửi video cho anh theo phiếu.**

## Đã làm

Worktree `games/.wt-ic-flame-slash`, nhánh `codex/flame-slash-strip`, mốc `5de0d22`.

- `src/view/skills/flame-slash.ts`: thêm sampler và ba uniform điều khiển dải, phương thức `setStrip(texture, k, scroll)`. Nhánh dải lấy alpha Firefly để ghép nhiệt, dùng RGB điều biến màu qua cùng ramp của thân. Không tính `tongue` trong nhánh này; nhánh dự phòng giữ nguyên từng biểu thức lửa cũ. Giữ vertex, mặt nạ trăng khuyết, bảng dải, xương sống, lịch xói và mờ.
- `src/view/skills/element-fire.ts`: nạp đúng tên `aura/strips/strip-fire-sheath.rgba.png` qua `stage.texture`, đặt sRGB, RepeatWrapping theo x, ClampToEdgeWrapping theo y, mipmap và alpha thẳng. Nối vào nhát chém, trừ khi `FIRE_LAB.slashTongues` bật; mặc định cờ là `false`.
- `src/lab/skills-main.ts`: đọc `?slash=tongues` và ghi cách dùng ở chú thích đầu file. Mặc định dùng dải khi ảnh sẵn sàng.
- `tests/view/flame-slash.test.ts`: 4 test Node, không WebGL: hai nhánh shader và biểu thức cũ; uniform/setStrip; dự phòng trong lúc chưa nạp hoặc nạp lỗi rồi chuyển sang ảnh đã nạp; cờ mặc định.
- `docs/changelog/2026-11-05-flame-slash-strip.md`: ghi thay đổi và phần kiểm hình ảnh còn chờ.

Các đường dẫn trên tính từ worktree; báo cáo này là tệp thứ sáu được ghi ở repo cha. Không tạo hay sửa ảnh, âm thanh hoặc tệp ngoài danh sách của phiếu.

## Cách đặt tỷ lệ và dự phòng

**Dùng `k = 3`, đúng phương án dự phòng trong phiếu**, tức ba chu kỳ dọc nhát chém, cuộn lùi về chuôi 0,5 chu kỳ/giây. `FlameSlash.set(...)` nhận hai đầu trong tọa độ thế giới và bề rộng quy về 1080p, không có camera để đo chiều dài cung trên màn hình. Vì vậy chưa khẳng định đã đo tỷ lệ tự nhiên 2:1; Claude cần xem độ kéo giãn khi quay A/B.

TextureLoader trả texture trước khi ảnh nạp xong. Mỗi lần `set(...)`, chỉ bật `uHasStrip` nếu ảnh có chiều rộng và chiều cao dương; ảnh thiếu hoặc lỗi giữ nguyên lửa cũ, không làm nhát chém rỗng. Không thêm bộ hẹn giờ, không đổi nhịp kỹ năng.

## Kiểm bắt buộc

Chỉ chạy trong worktree được giao, có bộ điều phối CPU `heavy.sh`, không mở cổng mạng.

| Kiểm | Kết quả |
| --- | --- |
| `node node_modules/typescript/bin/tsc --noEmit -p .` | **Đạt**, thoát 0. |
| `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4` | **Đạt 979/979 test, 89/89 tệp**, tăng 4 test từ mốc 975; 17,31 giây. |
| Build tạm `/private/tmp/codex-275-dist` | **Đạt**, Vite 7.3.7, 183 module, thoát 0. |
| `grep -rl "slashTongues\|uHasStrip" /private/tmp/codex-275-dist` | Không in gì, thoát 1 đúng nghĩa không tìm thấy. |
| Dọn build | **Đã xóa** thư mục build cùng cache tạm. |
| `git diff --check` | **Đạt**, không lỗi. |
| Phạm vi worktree | Chỉ thêm/sửa 5 tệp được phép; symlink `node_modules` chưa được theo dõi đã tồn tại trước khi làm. |

Lần gọi `pnpm exec tsc` đầu tiên bị pnpm cố kiểm/cài phụ thuộc và gặp lỗi SQLite của kho cache. Đã chuyển sang gọi trực tiếp TypeScript và Vitest đang có trong `node_modules`; không cài thêm phụ thuộc.

Vite đang cài không hỗ trợ CLI `--no-cache`. Dùng cùng cách API của phiếu 274, chạy trực tiếp từ stdin, giữ đủ cờ của phiếu và cache mới; không tạo thêm script:

```sh
IC_VITE_CACHE_DIR=/private/tmp/codex-275-dist/.vite-cache \
node --input-type=module - --no-cache --configLoader runner --outDir /private/tmp/codex-275-dist <<'JS'
import { existsSync } from 'node:fs';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
const outDir = '/private/tmp/codex-275-dist';
const args = process.argv.slice(2);
if (JSON.stringify(args) !== JSON.stringify(['--no-cache', '--configLoader', 'runner', '--outDir', outDir])) throw new Error('Sai cờ build của phiếu 275.');
if (existsSync(outDir)) throw new Error('Thư mục build phải chưa tồn tại để không dùng lại cache.');
const cacheDir = process.env.IC_VITE_CACHE_DIR;
if (cacheDir !== `${outDir}/.vite-cache`) throw new Error('Sai cacheDir riêng của phiếu 275.');
const { build } = await import(pathToFileURL(resolve('node_modules/vite/dist/node/index.js')).href);
await build({ configLoader: 'runner', cacheDir, build: { outDir } });
JS
```

Trạng thái worktree sau kiểm:

```text
 M src/lab/skills-main.ts
 M src/view/skills/element-fire.ts
 M src/view/skills/flame-slash.ts
?? docs/changelog/2026-11-05-flame-slash-strip.md
?? node_modules
?? tests/view/flame-slash.test.ts
```

Repo cha có nhiều thay đổi của các luồng khác từ trước; không sửa hoặc hoàn tác chúng. Không dùng lệnh Git ghi, không commit hay push.

## Claude cần làm tiếp

Theo phân công trong phiếu, chưa chạy trình duyệt hoặc tạo capture/video:

- Quay nhát chém kết phím 7 hệ Hỏa ở camera chơi, 1280×720 và 1920×1080, trên nền sáng và tối; so dải mặc định với `?slash=tongues`.
- Kiểm parity bằng ảnh: hệ Kim trùng 100%; khung hệ Hỏa không có nhát chém trùng 100%. Test Node chưa xác lập các kết quả hình ảnh này.
- Xem độ kéo giãn với `k = 3`, chất lửa, nhịp xói và gửi video cho anh. Chưa chấm hay tuyên bố đạt 8,5.

Không gặp hạn mức hoặc yêu cầu chờ.
