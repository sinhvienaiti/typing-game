# Báo cáo phiếu 278 · Làm nốt 277, sửa hai cổng lab của 264

Đã hoàn tất phần mã và kiểm tự động trong phạm vi phiếu. **Kiểm kiểu qua; 995/995 test qua; build qua wrapper đổi đường dẫn trong bộ nhớ, grep sạch và đã dọn.** Chưa xác nhận lại hai ngưỡng bằng GPU; Claude làm bước đó theo phiếu. Chưa commit hoặc gộp.

Worktree `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`, HEAD `ee3ee974ad749b20e78afc065fb0b44ff9e0fac4`. Đã đọc báo cáo 277 trước khi sửa, tiếp tục nguyên các thay đổi chưa commit của 277.

## Tệp đã ghi

Tính từ worktree, trừ báo cáo này ở repo cha:

| Tệp | Nội dung phiếu 278 |
| --- | --- |
| `src/view/skills/element-fire.ts` | Bật vẽ trước tăng tuổi riêng cho chớp brush; thêm `prewarmFire()`, đợi đủ media và biên dịch vật liệu Hỏa, gồm brush v2 và bốn pool của 277. |
| `src/view/skills/fxkit.ts` | Thêm `SpritePoolOptions.drawBeforeAge`, mặc định `false`; không đổi layout trạng thái, shader hoặc các số. |
| `src/lab/skills-main.ts` | Chỉ import/gọi prewarm cạnh aura cho hai render target, khôi phục target bằng `finally`, và thêm `+ 0` cho `ageTicks`. |
| `tests/view/element-layer.test.ts` | Đặt `fxcode` trong đúng năm ca cũ, giữ toàn bộ phép kiểm. |
| `tests/view/key1-brush-impact.test.ts` | Đặt `fxcode` trong đúng một ca đếm điểm mã, giữ toàn bộ phép kiểm. |
| `tests/view/fire-lot1-art.test.ts` | Giữ sáu ca của 277; tăng độ chặt ca nạp dải và thêm một ca prewarm. |
| `tests/view/key1-flash-age0.test.ts` | Ba ca mới dùng clip giả: đỉnh tuổi 0, chớp chồng nhau/hit-stop/reset và hành vi mặc định của pool khác. |
| `docs/changelog/2026-11-05-fire-lot1-art.md` | Cập nhật kết quả của cả 277 và 278. |
| `docs/codex-queue/278-report.md` ở repo cha | Báo cáo này. |

Không cần sửa `element-stage.ts`: các pool đã được đăng ký trong constructor của `FireLayers`.

## Sáu ca cũ: không nới hoặc bỏ phép kiểm

Mỗi ca dưới đây chỉ thêm `vi.stubGlobal("location", { search: "?fxcode=1" })` trước phần dựng; `afterEach` dọn global. Các ca khác vẫn kiểm đường mặc định. Không có ca nào trong sáu ca này cần đổi sang art vì chúng kiểm trực tiếp kiểu pool/spec của đường mã cũ.

| Tệp · tên ca | Vì sao dùng đường mã |
| --- | --- |
| `element-layer.test.ts` · `keeps every kit's seal and ring body at 0.9 a channel at most, cool and lit (only the thin line may bloom; 03/11 recheck)` | Kiểm hai `HeatRingPool` và các uniform `uBody/uLit` của chúng. |
| `element-layer.test.ts` · `draws the seal and its rings as matter in Fire (soot underlay, a thin hot line) and as light in Metal` | Kiểm seal cùng vòng áp lực bằng `HeatRingPool`, gồm số vòng nhìn thấy. |
| `element-layer.test.ts` · `lands, kills and plants as points of fire, never smooth white balls (round 3: the dot × 3–4.5 up to 1.3 m)` | Spy `FirePointPool.emit`, kiểm reach/core/tongues và thân shader cũ. |
| `element-layer.test.ts` · `gives its rings of fire structure: room for flame tongues outside the band, and embers shed as they open (round 3)` | Kiểm cấu trúc vòng mã và các delay ember so với tuổi thọ vòng. |
| `element-layer.test.ts` · `draws the flame slash round a smooth spine with regular tongues outside the crescent, its molten lines gold (round 3)` | Spy hai beam mã từ finisher/cutSeam, kiểm số lần phát và màu core. |
| `key1-brush-impact.test.ts` · `keeps the spark-ray and loose-ember counts, removing only six hit fire points` | So brush/lotus trên cùng đường mã, yêu cầu đúng chênh lệch sáu `FirePointPool` và giữ đếm spark/ember. |

## Ba sửa lab

- **Chớp tuổi 0:** `SpritePool` hiện giữ đồng hồ và hàm ghi thuộc tính ở phần private; không thể giữ đúng tuổi riêng cho các chớp chồng nhau bằng cách bỏ một lần `update` cục bộ. Vì vậy dùng tùy chọn theo pool mà B1 cho phép, chỉ bật ở `fx-fire-flash`. Vẽ tuổi hiện tại trước rồi mới tăng tuổi, cùng thứ tự với `FlipbookPool`. Các pool không bật tùy chọn và thẻ một khung giữ cách xử lý cũ; không đổi `BRUSH.flash` hay màu/gain/kích thước.
- **Biên dịch lần đầu:** `prewarmFire()` đợi thư viện `fire`, thư viện brush và Promise nạp dải; sau đó biên dịch các mesh Hỏa với vật liệu cuối cùng. Có cả mask A/B v2, sao, vòng tay, vòng đất và dải của 277. Cờ visible được trả lại từng mesh; render target được chụp trước lúc đợi, đặt lại trước biên dịch và khôi phục sau đó. Lab gọi cho buffer hậu kỳ và màn hình trước khi báo sẵn sàng. Không phát hiệu ứng, thay thời gian hay tiêu thụ luồng ngẫu nhiên.
- **CDP:** `Math.round(...) + 0` giữ số 0 dương; nhánh chưa có đòn vẫn trả `-1`.

## Kiểm bắt buộc

1. **PASS**, thoát 0: `node node_modules/typescript/bin/tsc --noEmit -p .`.
2. **PASS**, thoát 0:
   `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`.
   Kết quả cuối: **995 test / 91 tệp đều qua**, 12,40 giây. Mốc 985 + 6 test của 277 + 4 test của 278. Sáu lỗi cũ đã hết. Ca lượt 1–7 vẫn có 158 lần phát sao, tối đa 17/256 thẻ, 0 rơi.
3. **Build PASS với khác biệt wrapper dưới đây.** Vite 7.3.7, 183 module, thoát 0; lần cuối 828 ms. `grep -rl 'fxcode' /private/tmp/codex-278-dist` không in gì, thoát 1 đúng nghĩa không có kết quả. Đã xóa đúng thư mục này và xác nhận không còn.
4. **PASS phạm vi:** `git diff --check` sạch; trạng thái chỉ có các đường được phép và link `?? node_modules`. Không có `art-src` lúc nhận hay lúc kiểm; không tạo hoặc đụng link này.

Test chớp lấy dữ liệu kích thước/màu/alpha sau lần cập nhật thật của host, với clip brush giả có mask. Tích phân sáng của sheet giả cố định cho tỉ lệ tuổi 0/đỉnh bằng **1,0**, qua cả đòn thường và lớn; tuổi 1 thấp hơn tuổi 0. Đây là kiểm CPU/thuộc tính, **không phải phép đo pixel GPU**. Test prewarm giả lập renderer, gồm trường hợp target bị lab đổi khi ảnh còn đang nạp, và biên dịch ném lỗi. Đã kiểm riêng biểu thức `+ 0` loại bỏ `-0`.

### Wrapper build 274 khóa cứng tên thư mục

Đã chạy lệnh nguyên văn A2: thoát 1 trước build vì wrapper yêu cầu đúng `/private/tmp/codex-274-dist`. Không sửa wrapper, không gọi CLI Vite với `--no-cache`. Chạy cùng nội dung wrapper qua module trong bộ nhớ, **chỉ đổi chuỗi đường dẫn 274 sang 278**; giữ mọi kiểm tra cờ, cache riêng và thư mục chưa tồn tại. Lệnh tái lập, chạy từ worktree:

```sh
IC_VITE_CACHE_DIR=/private/tmp/codex-278-dist/.vite-cache node --input-type=module - --no-cache --configLoader runner --outDir /private/tmp/codex-278-dist <<'JS'
import { readFileSync } from 'node:fs';
const source = readFileSync('/Volumes/SS990TPRO/htdocs/typing-game/.local/codex-runs/274-out/build-no-cache.mjs', 'utf8');
if (!source.includes('const outDir = "/private/tmp/codex-274-dist";')) throw new Error('Wrapper 274 đã đổi; cần kiểm tra lại.');
const adapted = source.replaceAll('/private/tmp/codex-274-dist', '/private/tmp/codex-278-dist');
await import('data:text/javascript;base64,' + Buffer.from(adapted).toString('base64'));
JS
```

## Không làm và bàn giao

Không chạy game chính, mở cổng mạng, tạo media, sửa kit/sim/content/art-src hoặc chạy lệnh Git ghi. Không sửa work files hay báo cáo 277. Không tạo capture vì phiếu giao Claude kiểm lab và video.

Claude chạy lại **bảy cổng lab của 264**, đặc biệt tỉ lệ chớp ≥ 0,95 và khung trúng đầu ≤ 11,5 ms; sau đó parity **ONLY lô 1**, perf, video trước/sau và hai giám khảo mù. Chủ cần xem video sau khi có các số này. Chưa tuyên bố hai cổng GPU đã qua hoặc nghiệm thu thị giác. Không gặp hạn mức hay thời điểm phải đợi.
