# Phiếu 394 — Bố cục UI chơi gõ chữ

Ngày: 16/11/2026. Áp dụng mục **Owner chốt** cuối `TYPING_GAMEPLAY_DECISION.md` và phiếu đã có PASS Sonnet. Một lane sửa mã; có review chỉ đọc độc lập.

**Đã triển khai và qua test/typecheck. Chưa nghiệm thu hình ảnh, mức che ≤17% hoặc điểm mỹ thuật:** sandbox chặn cổng Vite, nên chưa có ảnh trước/sau hay số DOM thật. Không dùng ước lượng 34,5% của phiếu 392 làm baseline.

## Đã làm

- Xóa `games/immortality-cultivation/src/ui/learn-ahead.ts`; bỏ khởi tạo, tự mở, quyền nhận phím, cờ `prelearn`, trạng thái pause và mục debug tương ứng trong `src/app/app.ts`. Không thêm phím mở. Giữ hồ sơ học, ledger, sự kiện học và các API dữ liệu cũ để tương thích.
- Bỏ presenter thẻ nghĩa nổi khỏi trận. `src/ui/ban-quyet.ts` nhận gloss và chỉ hiện một dòng nghĩa khi từ đang khóa có `hint=true`, giữ đúng hợp đồng `hintUsed`. Từ mới có dấu `NEW` trong ô kỹ năng.
- Dải kỹ năng sát đáy, vật phẩm thu gọn; chữ tối thiểu 28 px. Track phân bổ theo độ rộng chữ thực, có điều chỉnh khi đổi từ, viewport, text scale hoặc font tải xong; dành đủ chỗ cho `Ultimate ready · Space`. Text scale lớn có thể được giảm để vừa hàng, vẫn giữ sàn 28 px. Cần kiểm tra trực quan ở 100/125/150%.
- HUD máu/năng lượng/lõi/đợt nằm ở mép trên; posture và thông báo ở cạnh. `screen-zones.ts` dành 64 px đầu khung và dải đáy cho UI, qua API inset sẵn có. Không sửa renderer hay bản đồ.
- `shop-mode.ts`, `shop-strip.ts`, `styles/game-css.ts`: shop thành ngăn phải rộng 24vw, thu còn 190 px khi người dùng chuột chọn đặt trụ; tự ẩn/đóng từ warning trở đi. Model cũng chặn thao tác mua/đặt cũ nếu phase đã đổi. Wave card chỉ còn ở prep/break, có lựa chọn né cả hai mép; không hiện trong warning, wave, lull hoặc boss.
- Đường render quái không tạo nhãn từ trên đầu; các từ Seal/Cleanse vẫn nằm trên dải. Thêm `src/view/health-bars.ts`, nối từ `actors.ts`: mọi quái bị thương dùng chung **một InstancedMesh, một material, geometry không chia group**; nền và lượng máu trong cùng shader. Quái đầy máu, hồi đầy, chết hoặc đã freed không có instance. Cấu trúc này dùng một draw cho pass màu; chưa đo renderer/GPU thật.
- Tuyệt kỹ: hoàn tất từ ghi học một lần rồi lưu Cast riêng theo ghế, chưa tung. Space mới thử mục tiêu tại vị trí/điểm ngắm lúc bấm; không đệm Space sớm, không nhận key repeat. Không có đích: `No target`, giữ sẵn sàng và năng lượng, không tự thử lại. Hết đợt, gục hoặc trận kết thúc xóa ready. Không thêm vạch/vòng canh nhịp.
- Chuyển chữ chiến đấu, ô kỹ năng/vật phẩm, HUD, shop và wave card sang tiếng Anh. Các nghĩa tiếng Việt là nội dung học được giữ lại.

Các file nối thêm: `src/app/input-router.ts`, `src/content/{rules,types}.ts`, `src/sim/{cast,words,world,skills}.ts`. `src/ui/review-panel.ts` giữ các helper DOM của thẻ ôn sau khi xóa Learn Ahead; `review-card.ts` đổi import. `menu.ts` chỉ thêm tên tiếng Anh cho hành động Ultimate mới.

## Kiểm chứng

- `pnpm test --maxWorkers=2`: **96 file, 1008 test PASS**; lượt cuối mất 18,33 s. Chạy bộ test theo yêu cầu nghiệm thu cụ thể của phiếu; không chạy build.
- `pnpm exec tsc --noEmit`: PASS.
- `git diff --check` và `node --check scripts/visual/scenarios/ui-layout394.mjs`: PASS.
- Test mới: `tests/ui/no-learn-ahead.test.ts`, `tests/sim/ultimate-space.test.ts`, `tests/view/health-bars.test.ts`, `tests/ui/coverage.test.ts`. Bổ sung test Space/panel/repeat, nghĩa chỉ trên từ khóa và shop đóng/chặn intent cũ trong các test router, Bàn Quyết, shop.
- Cập nhật kỳ vọng tiếng Anh và vị trí HUD trong test UI. Script tích hợp `combat-real-lanes.test.ts` đã bấm Space khi có ready; các kiểm tra replay/hash, số nguyên và chống cast trùng vẫn PASS. Rebase hai bộ golden trong `twin-pearl.test.ts` vì trạng thái băm nay có mảng `casts.prepared`; số quái ở từng mốc giữ nguyên.
- Review mã chỉ đọc phát hiện và đã sửa: wave card còn xuất hiện trong lull, mất vị trí né mép phải, và nguy cơ ô Ultimate cắt mất chữ Space. Review không thay thế việc chạy browser.

## Ảnh và phép đo còn thiếu

`pnpm dev` đã dừng với:

```text
Error: listen EPERM: operation not permitted 127.0.0.1:3008
```

Không có server do phiếu này để lại. Thư mục `typing-game-review` ở ngoài writable roots của sandbox này, nên chưa ghi ảnh hoặc `ABOUT.md` vào đó.

| Khung / trạng thái | Trước: DOM % | Sau: DOM % | Ảnh trước/sau |
| --- | --- | --- | --- |
| 1280×720, chuẩn bị | Chưa đo | Chưa đo | Chưa chụp |
| 1280×720, combat căng | Chưa đo | Chưa đo | Chưa chụp |
| 1920×1080, chuẩn bị | Chưa đo | Chưa đo | Chưa chụp |
| 1920×1080, combat căng | Chưa đo | Chưa đo | Chưa chụp |

Đã thêm `src/ui/coverage.ts` và debug handle `window.__ic.layout()`: đo hợp diện tích DOM rect, cắt theo viewport, không đếm lặp panel lồng/đè nhau; trả về % che và cỡ chữ nhỏ nhất. Kèm kiểm tra giao với lõi/cổng/ô trụ và AABB bảo thủ của cảnh báo đang hoạt động. Phép đo panel DOM không tính model/VFX/thanh máu WebGL; ảnh và kiểm tra cảnh báo thực tế vẫn bắt buộc.

Claude chạy ngoài sandbox, từ hai terminal:

```sh
# Terminal 1
cd /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation
pnpm dev
```

```sh
# Terminal 2; Chrome trên macOS, không dùng URL flag chất lượng
cd /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation
node src/kit/tools/cdp-run.mjs scripts/visual/scenarios/ui-layout394.mjs --width=1280 --height=720 --dpr=1
cd /Volumes/SS990TPRO/htdocs/typing-game
node scripts/review-index.mjs
```

Scenario tự chạy cả hai kích thước, chọn tốc độ 35 WPM bằng UI nếu cần, chụp prep rồi dựng fixture combat với 30 quái bị thương, hai Seal, Cleanse, Ultimate ready và một từ đang gõ. Kết quả mặc định vào:

`/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-16/tu-tien/ui-layout-build/`

Gồm `ABOUT.md`, bốn ảnh `after-<khung>-<trạng thái>.png` và `after-coverage.json`. Scenario mới chỉ qua kiểm tra cú pháp, chưa chạy trong browser. Cần đối chiếu trạng thái thực tế có đủ tám ô từ, kiểm tra các cảnh báo đang bật, text scale 125/150%, và bổ sung video trước/sau. Capture này là preflight ở dev host; chưa phải chấm mù ở built play host.

**Baseline trước 394 chưa có DOM/ảnh đúng hai kích thước.** Ảnh owner gửi vẫn ở topic `ui-layout-research`; không đổi nhãn bản hiện tại thành “before”. Muốn số trước/sau đúng cần một snapshot trước 394 đã lưu riêng; không hoàn nguyên source đang có nhiều worker để dựng baseline.

## Bỏ qua và owner cần xem

- **Icon tinh anh/boss:** không tìm thấy icon art phù hợp trong public assets của checkout này. Chưa thêm icon; không dùng SVG/CSS/emoji thay thế. Cần owner/Claude cấp đường dẫn art đã duyệt để nối tiếp.
- Chữ tiếng Việt còn ở các luồng ngoài combat vừa sửa: `src/app/pace-card.ts`, phần còn lại của `src/ui/menu.ts`, `review-card.ts`, `results.ts`, `word-book.ts`, `ime-banner.ts`, màn Tĩnh Tu và dữ liệu tên trong content. Đây chưa phải lượt chuyển ngôn ngữ toàn game.
- Owner cần xem bố cục thực, mức che và các điểm giao trên hai khung, khả năng đọc tám từ/cỡ chữ lớn, cảm giác gõ rồi Space, và mức nhận biết tinh anh/boss khi còn thiếu art.
- Không tạo image/audio/media; không sửa `src/lab/`, `view/ground.ts`, bản đồ, game khác hoặc docs Tu Tiên. Không đổi nhánh, commit, push, reset, clean hoặc stash. Giữ các thay đổi có sẵn của worker khác.

**Trạng thái bàn giao:** mã và kiểm chứng tự động xong; ảnh, số DOM trước/sau, icon art và nghiệm thu hình ảnh còn mở.
