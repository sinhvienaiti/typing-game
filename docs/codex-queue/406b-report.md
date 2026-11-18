# Phiếu 406b — Chữ phòng thủ, biên độ tấn công và nhãn PERFECT

Ngày: 16/11/2026. Phản biện đầu vào: **PASS (Sonnet)**. Đã sửa mã và bổ sung test; **chờ Claude chạy suite và nghiệm thu trình duyệt**. Đã đọc lại kết quả 409, giữ các chuỗi dịch của phiếu đó. Quota còn 41 % lúc nhận; làm một làn.

## Đã sửa

- Phòng thủ vẫn rơi **50–80 px** khi đủ chỗ. Canvas tính khoảng rơi tối đa theo đáy viewport, chừa **4 px** và bán kính bao toàn bộ chữ khi xoay. Khi sát đáy, rút ngắn quãng rơi và độ nảy theo khoảng trống; còn đúng một lần nảy. Tọa độ chữ và toàn bộ ảnh hạt được kẹp trong khung, cập nhật theo viewport mỗi lượt vẽ. Tổng lượt lóe/tan giữ **640 ms**, gồm lóe 40 ms.
- Tấn công bay theo đường cong, đạt **80–110 px ở 400 ms sau hoàn tất**, khi chữ còn rõ, rồi giữ độ cao trong đoạn tan. Không còn chỉ đạt biên độ cuối lúc opacity bằng 0.
- Dùng lại ảnh glint hiện có, tăng kích thước nền từ **12 lên 28 px**, cỡ vẽ theo nhịp khoảng **24–34 px**; opacity tối đa **0,9**, màu `rgb(229, 221, 183)` (mọi kênh dưới 0,9). Cả tám hạt dùng cùng đường tan của chữ, hết ở **640 ms**. Không tạo art hay âm thanh mới.
- Kit có hỗ trợ `numbers.label`. Ghi đè **`PERFECT`** trong `src/view/feedback-profile.ts`, thay nhãn cục bộ cũ `CHỚP`; cả profile thường và giảm chuyển động đều nhận nhãn này. Không sửa `src/kit/`.
- Không thêm timer, thời gian chờ hay thay đổi đường phím → Cast. Giữ giảm chuyển động: mờ tại chỗ, không bay/rơi/xoay/nảy/hạt. Mốc **≤50 ms** vẫn cần Claude đo trong trình duyệt; chưa tự nhận đạt bằng đo CPU.

## Tệp đã sửa

Đường dẫn dưới đây tính từ `games/immortality-cultivation/`:

| Tệp | Nội dung |
| --- | --- |
| `src/ui/word-fx.ts` | Quỹ đạo tấn công, giới hạn rơi, nảy theo khoảng trống và vòng đời hạt |
| `src/ui/word-flight.ts` | Biên chữ xoay, kẹp chữ/hạt theo viewport và áp dụng màu/cỡ hạt |
| `src/ui/styles/word-fx-css.ts` | Màu glint dùng chung và kích thước hạt DOM |
| `src/view/feedback-profile.ts` | Nhãn `PERFECT` phía game |
| `tests/ui/word-fx.test.ts` | Biên độ khi chữ còn rõ, rơi ngắn, một lần nảy, màu/cỡ và tan hạt |
| `tests/ui/word-flight.test.ts` | Biên vẽ thực sự được gửi tới canvas giả ở hai khung, chữ xoay, resize và hạt |
| `tests/view/fx.test.ts` | Nhãn tiếng Anh cho hai chế độ chuyển động, giữ profile kit riêng |
| `tests/ui/word-fx-capture.mjs` | Cho phép mã phiếu `406b` xuất dải khung như `406` |

Báo cáo: `docs/codex-queue/406b-report.md` ở repo cha. Không sửa các đường dẫn ngoài phạm vi phiếu, không commit hoặc đổi nhánh.

## Kiểm chứng đã chạy

- `pnpm exec tsc --noEmit`: **PASS** sau các sửa mã và test.
- `node src/kit/verify-kit.mjs`: **PASS**, 73 tệp khớp manifest.
- `node --check tests/ui/word-fx-capture.mjs`: **PASS**.
- Kiểm khoảng trắng trong các tệp sửa: **PASS**.
- Đo trực tiếp mã trình bày bằng Node/tsx và canvas giả, không chạy suite:
  - Tấn công từ `stone` tại 400 ms: **80 / 87,5 / 95 / 102,5 / 110 px**, opacity **0,9657**.
  - Ở cả **1280×720** và **1920×1080**, mẫu chữ 16×32 px có đỉnh ban đầu cách đáy 180 px: rơi **50 / 60 / 70 / 80 px** ở 460 ms; nảy về **38 / 48 / 58 / 68 px** ở 550 ms.
  - Cũng ở hai khung trên, mẫu sát đáy (đỉnh ban đầu cách đáy 52 px): rơi **14,11 px**, nảy về **10,72 px**, trở xuống **13,99 px** ở 638 ms. Quét mỗi 2 ms, tính biên chữ sau xoay: khoảng cách đáy nhỏ nhất **4,82 px**.
  - Hạt đầu tại 240 ms: cỡ **30,33 px**, opacity **0,9**; tại 520 ms opacity **0,3753**; tại 640 ms bằng **0**. Hai profile đều trả nhãn `PERFECT`.

Các số trên là kiểm mã trình bày với hình học giả; chưa phải số đo DOM, GPU, ảnh hay video thật.

### Rà tiếng Việt sau 409

Đã dùng `grep -RnE` với bộ ký tự có dấu trên toàn bộ **22 tệp `src/ui/`**, rồi đối chiếu các literal bằng TypeScript AST. Có 100 dòng khớp grep, chủ yếu là comment mã/CSS. Literal có dấu còn hiển thị cho người chơi là **`Thiết Bối Lang Vương`** tại `src/ui/hud.ts:58`: tên riêng boss, giữ theo luật tên riêng và kết quả 409. Ba đoạn template có dấu còn lại chỉ chứa comment CSS. Không phát hiện nhãn giao diện tiếng Việt khác cần dịch; nghĩa từ học vẫn đi qua dữ liệu gloss.

## Chưa chạy và lý do

**Không chạy `pnpm test`, suite riêng, build game hoặc trình duyệt**, theo house rule của lượt này và phân công để Claude chụp. Test đã thêm và qua typecheck nhưng **chưa được thực thi**. Chưa có kết luận nghiệm thu hình ảnh, hạt có đủ rõ trên nền thật, phím → Cast ≤50 ms hoặc điểm chuẩn hệ thống dùng chung.

Không bỏ hạng mục sửa mã nào. Bỏ qua sinh ảnh/âm vì phiếu chỉ điều chỉnh trình bày từ tài sản đang có. Không ghi capture vào repo hay thư mục review trong lượt này.

## Lệnh cho Claude

Kiểm thử và typecheck, không cần build để chạy các lệnh này:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation
pnpm test --maxWorkers=2
pnpm exec tsc --noEmit
```

Terminal phục vụ game:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation
pnpm dev
```

Terminal chụp tấn công/phòng thủ ở 1280×720 và 1920×1080, có gõ sai/Backspace và số đo độ trễ:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game
WORD_FX_TOPIC=406b-word-fx WORD_FX_TICKET=406b KEY_INTERVAL_MS=67 .local/bin/heavy.sh --gpu node games/immortality-cultivation/tests/ui/word-fx-capture.mjs
```

Đầu ra: `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-16/tu-tien/406b-word-fx/`, gồm `ABOUT.md`, hai MP4, hai JSON và bốn dải khung `attack|defence-<khung>-strip.jpg`. Kịch bản kiểm số mẫu và trần 50 ms, từ chối GPU phần mềm, chỉ dọn khung do lượt chạy đó tạo và xây lại review index. Các lệnh chụp chưa chạy end-to-end trong lượt này.

Claude cần xem: chữ phòng thủ sát đáy ở cả hai khung và cỡ chữ 100/125/150%; nảy ngắn còn đọc được; tấn công đạt đủ cao trước khi tan; hạt rõ nhưng không lấn chữ; nhãn `PERFECT` trong chiến đấu; đổi giảm chuyển động giữa hiệu ứng. So video trước/sau với ảnh lỗi 406; nghiệm thu cuối trong built play host ở thiết lập người chơi theo chuẩn hệ thống dùng chung.
