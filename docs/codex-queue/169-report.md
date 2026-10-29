# Phiếu 169 · Dragonhold · Theo kit tiếng Anh, lệnh `deploy:pack`, từ vựng trong bản build

Hoàn tất phần mã trong phạm vi phiếu. `pnpm check` xanh **492/492 test**,
kit **75/75 file**. Từ vựng đã đủ trong build: **103 file, 100 level**.
Chạy thật `pnpm deploy:pack` trả mã **1** do **1 lỗi production** chứa
hai tham chiếu nguồn portal nhà. Kiểm cùng gói với cờ demo trả mã **0**.
**Chưa đạt production/G7.**

## 1. Phạm vi và thay đổi

- Worktree `games/.wt-dh-codex`, nhánh `dh-codex`, HEAD
  `4f61c6eefad2b284470b995ecd5df6c3fe184a6b`.
- Giữ nguyên lượt đồng bộ kit có sẵn: 12 file sửa, 2 file mới, từ kit cha
  `1b1fe6cfacdc81a55d13af202da0f42023455313`, `parentDirty: true`.
  Đối chiếu SHA-256 trước/sau của toàn bộ 76 file kit, gồm chính manifest.
- `tests/sim/bot-run.test.ts`: sửa đúng kỳ vọng `Vùng cuốn: Cân bằng`
  thành `Vùng cuốn: Balanced`; giữ nguyên các assertion cổng/dải.
  Phiếu nói hai test đỏ; lượt nền thực tế tái hiện **một** test đỏ do nhãn
  này, không thấy lỗi thứ hai ở các file liên quan. Toàn bộ 492 test sau
  sửa đều xanh.
- `src/view/fx.ts`: `NUMBER_FEEL = DRAGON`, bỏ bản sao ghi đè nhãn.
  Hai cấu hình trước sửa đã giống nhau về giá trị; test nhãn `PERFECT`
  giữ nguyên kỳ vọng, thêm một test kiểm dùng trực tiếp cấu hình kit.
- `package.json`: thêm đúng `deploy:pack` và `deploy:pack:local` như
  phiếu 168, đổi id thành `dragon-hold`. README mới ghi cách dùng.
- `tests/deploy-pack.test.ts`: 8 test chạy lệnh package trong fixture
  riêng ở `tmp/`, dùng build giả nhỏ và bộ kiểm kit thật. Kiểm build trước
  khi đọc gói, build lỗi thì dừng, chặn tài nguyên game khác ở cả hai chế
  độ, chặn nguồn nhà ở production và cho phép ở demo. Fixture tự xóa.
- Changelog game: `docs/changelog/2026-10-29-pack-and-kit.md`.

Không sửa kit, Vite config, mã bố trí tag, sim, luật chơi, golden, nguồn
portal hay media. Không chạy `kit:sync`, server, trình duyệt, mạng hoặc
lệnh Git ghi; không làm việc trong game/worktree khác.

## 2. Kiểm tra và số đo

| Lượt | Kết quả | Bằng chứng |
| --- | --- | --- |
| Test nền trước sửa | 4 file, 1 đỏ/33 xanh; lỗi nhãn Balanced | [JSON kết quả](169/tests-baseline-results.json), [lệnh và mã thoát](169/tests-baseline.json), [log](169/tests-baseline.log) |
| Test mới trước sửa mã | 9 đỏ/8 xanh: 8 test thiếu lệnh package, 1 test còn ghi đè số; nhãn PERFECT xanh | [JSON kết quả](169/tests-before-results.json), [log](169/tests-before.log) |
| `pnpm build` trước sửa | Mã 0; 4,335 giây; từ vựng đã đủ | [lệnh](169/build-baseline.json), [log](169/build-baseline.log), [hash từ vựng](169/vocabulary-baseline.json) |
| Tag chạy riêng lần 1 | 21/21 xanh; **0,351879 ms** < 1 ms | [log](169/tags-1.log) |
| Tag chạy riêng lần 2 | 21/21 xanh; **0,316416 ms** < 1 ms | [log](169/tags-2.log) |
| Tag chạy riêng lần 3 | 21/21 xanh; **0,300925 ms** < 1 ms | [log](169/tags-3.log), [tổng hợp](169/timing.json) |
| `pnpm check` sau sửa | Mã 0; **12,308 giây**; 56 file, 492/492 test; kit 75/75; TypeScript và Vite xanh | [lệnh](169/check.json), [log](169/check.log) |
| Golden M0 trong `pnpm check` | 10/10 xanh; file dữ liệu và test giữ nguyên SHA-256 | [xác minh](169/verification.json) |
| `pnpm deploy:pack` chạy thật | Build xanh, kiểm gói mã **1**; 4,346 giây | [lệnh/mã thoát](169/deploy-pack.json), [log](169/deploy-pack.log) |
| Bộ kiểm production với `--json` trên nguyên gói | Mã **1**, 1 lỗi | [JSON thuần](169/check-pack.json), [lệnh](169/check-pack-run.json) |
| Bộ kiểm demo với `--allow-local-host --json` | Mã **0**, 0 lỗi; không build lại | [JSON thuần](169/check-pack-local.json), [lệnh](169/check-pack-local-run.json) |
| Hash kit/golden, phạm vi và `git diff --check` | Đạt; không có đường thay đổi ngoài danh sách | [xác minh](169/verification.json), [trạng thái](169/status-final.txt), [mốc đầu](169/before.json) |

Để lấy đúng số đo của test tag, config tạm trong `tmp/169/` dùng plugin
Vite thêm `console.info` ngay trước `expect(ms).toBeLessThan(1)`. Vòng đo,
assertion, ngưỡng và file test trên đĩa giữ nguyên. Ba lần chạy tuần tự,
mỗi lần chỉ file tag; `pnpm check` sau đó chạy lại file gốc cùng bộ test
và cũng xanh. Không chạy lại bộ test sau khi đã xanh; sau đó chỉ chạy lệnh
đóng gói được yêu cầu và thu thập bằng chứng.

Lệnh package theo phiếu xuất chẩn đoán dạng chữ. Sau khi chạy thật lệnh,
gọi bộ kiểm thêm `--json` trên chính `dist` đó để lưu JSON thuần, không trộn
log build vào JSON. Không chạy toàn bộ `deploy:pack:local`; các test fixture
kiểm lệnh này và bộ kiểm demo chạy trên gói thật với cùng cờ.

## 3. Từ vựng và DH-01

Kết luận “bản build hiện tại không có từ vựng” **không còn đúng trên HEAD
của worktree này**. Vite dùng `publicDir` mặc định là `public`, chép bản ghim
vào `dist/vocabulary/` cả trước và sau sửa. Không thêm đường chép trùng hoặc
đổi cấu hình khi build đã đúng.

| Nội dung | Số lượng/kết quả |
| --- | --- |
| `index.json` | Có; hash khớp |
| `vocab-manifest.json` | Có; giống từng byte bản trong `public/` |
| Các level manifest liệt kê | **100/100**, `levels/001.json`–`100.json`; mọi SHA-256 khớp |
| `ATTRIBUTION.md` | Có; hash khớp |
| Tổng | **103 file, 2.675.955 byte**; 102 file được manifest ghim hash |
| Index mô tả level chưa gói | **0** |

[Bằng chứng sau đóng gói](169/vocabulary-final.json) ghi từng file, byte và
SHA-256; [bằng chứng trước sửa](169/vocabulary-baseline.json) cho cùng kết
quả. Bảy test hiện có trong `tests/vocab-pin.test.ts` xanh, kiểm đủ bản
ghim, hash, 100 level, bộ bài không rỗng và mọi mức đã lưu đều tải đúng file.
Bộ kiểm gói thật tiếp tục kiểm các hash và attribution trong **dist**.
Không có lỗi chép build nên không cần thêm mã sửa hay test cho đường chép mới.

## 4. Gói thật và phân loại phát hiện

Gói `dist` có **229 file, 29.949.229 byte (~28,562 MiB)**, gồm **70 GLB**,
**12 WebP** đã có sẵn và toàn bộ từ vựng. Không tạo, tải hay đưa media vào
Git. [Inventory](169/dist-inventory.json) ghi từng đường, byte, SHA-256 và
ngữ cảnh mọi chuỗi mà bộ kiểm báo.

| Phát hiện | Thật hay báo nhầm | Căn cứ và xử lý |
| --- | --- | --- |
| `local-host` · `assets/index-D6L5QOut.js` | **Lỗi thật ở production**, 2 tham chiếu trong 1 file | Cầu nối dùng `PARENT_ORIGIN = https://typing-game.local` (`src/kit/learning/contract.ts:22`); `src/app/app.ts:221` và mặc định `src/app/learning.ts:246` không truyền `parentOrigin`. `bridge.ts:248,292` dùng nguồn này để nhận/gửi thông điệp. Tham chiếu thứ hai là nút về portal: `src/app/portal.ts:4`, được `src/ui/results.ts:256` gọi với `VITE_PORTAL_ORIGINS`; chưa đặt biến nên build giữ nguồn nhà. Không phải báo nhầm. Cờ demo chỉ miễn lỗi này theo quy định. |
| `external: kit.invalid`, 1 lần | **Thông tin; báo nhầm nếu hiểu là request ra ngoài** | `src/kit/three/model-loader.ts:24,34,35` dùng gốc giả để phân giải URL tương đối rồi trả pathname. Không dùng gốc này để fetch. |
| `external: catlikecoding.com`, 1 lần | **Thông tin; báo nhầm nếu hiểu là request ra ngoài** | URL tài liệu trong chú thích GLSL của `three/examples/jsm/shaders/FXAAShader.js`, được `src/view/stage.ts:20,254` dùng. Ngữ cảnh bundle vẫn là chú thích shader. |
| `external: developer.download.nvidia.com`, 1 lần | **Thông tin; báo nhầm nếu hiểu là request ra ngoài** | URL white paper FXAA trong cùng chú thích GLSL, không phải mã fetch. |
| Vite cảnh báo chunk trên 600 kB | **Cảnh báo thật, không chặn build hay kiểm gói** | Bundle game **673,19 kB**, dưới 25 MiB mỗi file. Không mở rộng sang tối ưu bundle. |

Ba nguồn `external` chỉ nằm trong phần báo thông tin, không thuộc
`problems`. Không có lỗi tài nguyên game khác, đường cha, file quá cỡ,
số file, media riêng tư, hash từ vựng, attribution hoặc model theo phạm vi
bộ kiểm kit. Chế độ demo xanh **không chứng nhận mọi tài nguyên runtime đã
đủ**: bộ kiểm không thay thế lượt tải thật, đo byte lần chơi đầu hay kiểm
kiểu nội dung HTTP.

## 5. Bỏ qua và việc chủ dự án cần xem

1. **Không sửa đường chép từ vựng:** build hiện tại đã đúng; nhận xét DH-01
   cần cập nhật ở làn map theo bằng chứng của phiếu này. Không sửa tài liệu
   map ngoài phạm vi.
2. **Không sửa test thời gian hoặc thuật toán tag:** cả ba lượt riêng và
   lượt kiểm tổng đều xanh, giữ nguyên ngưỡng 1 ms.
3. **Nguồn portal production cần làn tiếp theo xử lý cả hai chỗ.** Chỉ đặt
   `VITE_PORTAL_ORIGINS` sẽ đổi nút về portal, chưa đổi mặc định của bridge.
   Phiếu giao theo kit/lệnh đóng gói/từ vựng, không giao đổi cấu hình cầu
   nối; chưa có nguồn production được chỉ định. Giữ nguyên kit và để bộ
   kiểm báo lỗi thật, không nới để làm xanh.
4. **Chưa chứng nhận G7 hoặc triển khai độc lập đầy đủ:** phiếu cấm server,
   trình duyệt và mạng; không kiểm HTTP hay đo lần chơi đầu. Cần lượt kiểm
   riêng sau khi nguồn portal production được cấu hình.

Trạng thái cuối của worktree chỉ có lượt đồng bộ kit ban đầu và **7 file**
mã/test/README/changelog của phiếu. Báo cáo và bằng chứng nằm riêng ở
`docs/codex-queue/169-report.md` và `docs/codex-queue/169/` của repo cha.
