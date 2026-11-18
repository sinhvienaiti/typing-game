# Phiếu 168 · Last Line · Theo kit tiếng Anh, lệnh `deploy:pack`

Hoàn tất phần mã được giao. `pnpm check` xanh **206/206 test**, kit **61/61 file**; chạy thật `pnpm deploy:pack` trả mã **1**, phát hiện **2 lỗi thật**. Chế độ kiểm demo nhà còn **1 lỗi thật**. Gói chưa đủ điều kiện triển khai độc lập/G7.

## 1. Phạm vi và thay đổi

- Worktree: `games/.wt-ts-codex`, nhánh `ts-codex`, HEAD `b904a548e22e926ba297950f63fa7a0649fa4901`.
- Kit cha ghi trong manifest: `1b1fe6cfacdc81a55d13af202da0f42023455313`, `parentDirty: true`. Lượt đồng bộ có sẵn gồm 14 file sửa và 2 file mới; giữ nguyên byte của cả 62 file trong `src/kit` (61 file do manifest kiểm và chính manifest).
- `src/app/english.ts`: kế thừa `ADVICE_EN` của kit, bỏ phần ghi đè `steady` trùng nguyên văn. **Giữ 6 phần ghi đè** còn lại vì câu kit khác bản Last Line; bỏ chúng sẽ trái yêu cầu giữ nguyên chữ người chơi thấy. Bảy câu trước/sau giống hệt; bảng so với kit ở [advice-compatibility.json](168/advice-compatibility.json).
- `src/view/gun-rules.ts`: bỏ ghi đè PERFECT, kế thừa trực tiếp `SHIP.numbers` với cùng giá trị.
- `package.json`: thêm đúng hai lệnh `deploy:pack` và `deploy:pack:local` theo phiếu. README game trước đó chưa có; tạo `README.md`, một đoạn hướng dẫn tiếng Việt.
- `tests/english-ui.test.ts`: thêm 2 test bảo toàn nguyên văn và kế thừa cấu hình số. `tests/deploy-pack.test.ts`: thêm 8 test chạy các lệnh package với build giả nhỏ và bộ kiểm thật; kiểm dừng khi build lỗi, thứ tự build trước kiểm, phân biệt production/demo, chặn Space ở cả hai chế độ. Thư mục fixture riêng trong `tmp/` tự xóa sau mỗi test.
- Changelog game: `docs/changelog/2026-10-29-pack-and-kit.md`.

Không sửa sim, luật, nội dung, golden, cầu nối portal hay mã tải model. Không chạy `kit:sync`, server, trình duyệt, mạng hoặc lệnh Git ghi; không đọc hay sửa game/worktree khác, không tạo media.

## 2. Kiểm tra và số đo

| Lượt | Kết quả | Bằng chứng |
| --- | --- | --- |
| Test trước sửa mã, hai file liên quan | 9 đỏ, 4 xanh; 8 lỗi thiếu lệnh package, 1 lỗi còn ghi đè cấu hình số; test nguyên văn xanh | [tests-before.json](168/tests-before.json), [log](168/tests-before.log) |
| `pnpm check` sau sửa | Mã 0; 14,858 giây; 22 file, 206 test xanh; `verify-kit` 61/61; TypeScript và Vite build xanh | [check.json](168/check.json), [log](168/check.log) |
| Golden S0 trong `pnpm check` | 18/18 xanh; SHA-256 file golden giữ nguyên | [verification.json](168/verification.json) |
| Thời gian sim S0 | Trung vị 0,896 ms; p95 1,430 ms; ngưỡng trung vị ≤ 1,5 ms | [check.log](168/check.log) |
| Thời gian sim chương | Trung vị 1,148 ms; p95 1,889 ms; ngưỡng trung vị ≤ 1,5 ms | [check.log](168/check.log) |
| `pnpm deploy:pack` chạy thật | Build xanh; kiểm gói mã 1; 6,514 giây | [deploy-pack-run.json](168/deploy-pack-run.json), [log](168/deploy-pack.log) |
| Bộ kiểm production với `--json` trên chính gói đó | Mã 1, 2 lỗi | [check-pack.json](168/check-pack.json), [lệnh/mã thoát](168/check-pack-run.json) |
| Bộ kiểm demo với `--allow-local-host --json` | Mã 1, còn 1 lỗi; không build lại | [check-pack-local.json](168/check-pack-local.json), [lệnh/mã thoát](168/check-pack-local-run.json) |
| `git diff --check`, kiểm phạm vi, hash kit và golden | Đạt | [verification.json](168/verification.json), [status-final.txt](168/status-final.txt) |

Không có test thời gian đỏ, nên không kích hoạt điều kiện chạy riêng ba lần. Không chạy lại bộ test sau khi đã xanh; sau đó chỉ thêm tài liệu và thu thập bằng chứng. Chưa chạy toàn bộ `pnpm deploy:pack:local`; hành vi lệnh được kiểm bằng 4 test fixture và kiểm trực tiếp gói thật với cùng cờ local.

## 3. Gói thật và phân loại phát hiện

`dist` có **51 file, 1.522.519 byte (~1,452 MiB)**, chưa có model hay media. [dist-inventory.json](168/dist-inventory.json) ghi mọi file, số byte, SHA-256 và ngữ cảnh chuỗi bị phát hiện. Lệnh package theo phiếu xuất chẩn đoán dạng chữ; sau khi chạy nó, gọi bộ kiểm với `--json` trên nguyên `dist` để lưu JSON thuần, không trộn log build vào JSON.

| Phát hiện | Thật hay báo nhầm | Căn cứ và xử lý |
| --- | --- | --- |
| `foreign-asset` · `assets/index-CLt-HYPd.js` | **Lỗi thật**, chặn cả production/demo | Chuỗi `/assets/space-typing/models/manifest.json` được `src/view/models.ts:9` dùng thật; model không nằm trong gói. Giữ nguyên theo hướng B của chủ dự án; danh sách thay ở mục 4. |
| `local-host` · cùng file JS | **Lỗi thật ở production** | `src/kit/learning/contract.ts:22` đặt `https://typing-game.local`; `src/app/learning.ts:18` tạo bridge không truyền nguồn khác, nên bridge dùng mặc định ở `src/kit/learning/bridge.ts:115`, kiểm nguồn nhận ở dòng 248 và gửi `postMessage` ở dòng 292. Đây là nguồn thông điệp portal, không phải yêu cầu tải media. Không sửa trong phiếu. Cờ demo chỉ miễn lỗi này đúng quy định. |
| `external: kit.invalid`, 1 lần | **Báo thông tin; báo nhầm nếu hiểu là tải ra ngoài** | `src/kit/three/model-loader.ts:24,34,35` dùng gốc giả để phân giải URL tương đối rồi trả lại pathname khi manifest không có scheme. Không dùng làm nguồn fetch. Không thuộc `problems`, không chặn gói. |
| `vocabularyNotShipped: 97` | **Thông tin đúng, không phải thiếu file bắt buộc** | Index chung mô tả 100 level; bản ghim của game chỉ dùng level 001–003. Sáu file từ vựng, gồm manifest và `ATTRIBUTION.md`, đều trong gói và qua kiểm hash. Không chép thêm 97 level. |
| Vite: chunk trên 500 kB | **Cảnh báo thật, không phải lỗi bộ kiểm gói** | `BufferGeometryUtils-Dnx6px1C.js` 547,18 kB; build vẫn mã 0, dưới ngưỡng file 25 MiB. Không mở rộng sang tối ưu bundle. |

Không có lỗi cỡ file, số file, đường cha, media riêng tư, giấy phép hay hash từ vựng. Không kết luận mọi URL model có file: manifest Space không có trong gói, bộ kiểm chỉ phát hiện tham chiếu chéo game ở JS. Không có kiểm mạng hoặc kiểu nội dung HTTP do phiếu cấm server/trình duyệt; **chưa chứng nhận G7**.

## 4. Bàn giao các chỗ còn trỏ sang Space

Đường runtime duy nhất ghi cứng: **`/assets/space-typing/models/manifest.json`**. Thư viện đó cấp URL GLB động cho cả tàu, quái và đạn. Bỏ tàu riêng lẻ chưa xóa hết phụ thuộc. [space-references.json](168/space-references.json) ghi **10 file liên quan, 46 vị trí**, **16 id model ứng viên** và lượt quét toàn bộ mã: 52 dòng nhắc Space trong 45 file (gồm chú thích xuất xứ của kit và fixture test, không coi chúng là phụ thuộc tải).

Các đường dưới đây tính từ worktree `games/.wt-ts-codex`:

| File và dòng | Vai trò cần xử lý ở làn thay model |
| --- | --- |
| `src/kit/three/model-loader.ts:21` | Định nghĩa URL manifest Space; **giữ nguyên kit**, làn sau thay cấu hình ở mã game. |
| `src/kit/three/index.ts:19` | Xuất hằng URL trên, không tự tải tài nguyên. |
| `src/view/models.ts:7,9,35,37,38` | Nhập hằng Space, tạo `ModelLibrary`, nạp mesh theo kind/id và chọn tier; điểm chuyển sang thư viện riêng. |
| `src/view/ship.ts:23,27,29,31,32,107–114` | Mượn thư viện chung, chọn tàu/hero, tier High; socket và anchor liên quan cần đối chiếu model mới của chủ dự án. |
| `src/view/crowd.ts:22,36–42,180` | Bảy loại quái lấy mesh từ thư viện Space; hai loại dùng lại mesh khác. Hàm tải chưa truyền tier, dùng mặc định High. |
| `src/view/bolts.ts:14,19–24,47,48` | Năm id đạn/chiêu của Space; Medium lấy Medium, High/Ultra lấy High; Low bỏ nạp. |
| `vite.config.ts:15,23` | `SPACE_MODELS_DIR` hoặc đường mặc định sang repo Space, plugin phục vụ URL `/assets/space-typing/models/` chỉ ở dev. Chưa xóa hay đổi. |
| `src/app/main.ts:66,68,81,135` | Hai lựa chọn Vanguard/Draconis, query/lưu pilot, tạo Ship. Cần rà khi bỏ tàu cũ; bản thân không chứa URL media. |
| `src/view/combat.ts:107` | Khởi tạo Bolts theo pilot Draconis; phụ thuộc gián tiếp vào lựa chọn model đạn. |
| `src/view/shots.ts:86,89,409` | Nhánh hiệu ứng theo Draconis; không tải file, cần giữ nhất quán khi thay nhân vật. |

| Nhóm manifest | Id ứng viên hiện có trong mã | Số id |
| --- | --- | ---: |
| `ships` | `vanguard` | 1 |
| `heroes` | `draconis-v3`, `draconis-v2`, `draconis` (thử theo thứ tự) | 3 |
| `enemies` | `rainbow-mine-3d`, `rainbow-mine-lod`, `rainbow-scout-3d`, `rainbow-scout-lod`, `rainbow-tank-3d`, `rainbow-shield-3d`, `rainbow-splitter-3d` | 7 |
| `skills` | `vanguard-bolt`, `solar-lance-bolt`, `frost-seraph-bolt`, `crimson-talon-bolt`, `dragon-fireball` | 5 |

Không có manifest Space/GLB trong worktree nên không thể liệt kê tên file GLB vật lý hay byte của chúng từ gói này. Không đọc game khác để suy ra. Các id trên là ứng viên và nhánh dự phòng trong mã, không phải 16 file chắc chắn tải mỗi ván. Gói thật chỉ có 1 file JS chứa URL Space; danh sách đầy đủ file của gói nằm trong inventory.

## 5. Việc giữ lại và chủ dự án cần xem

1. Sáu câu lời khuyên còn giữ bản game để không đổi chữ; chỉ câu `steady` và cấu hình số đã kế thừa kit hoàn toàn. Bảng nguyên văn giúp duyệt quyết định này.
2. `deploy:pack` **chủ động đỏ** vì hai lỗi có thật, không nới bộ kiểm để làm xanh. Hướng B bỏ tàu/thay model riêng và nguồn portal production cần làn sau; phụ thuộc Space còn gồm quái và đạn.
3. G7 cần lượt kiểm riêng trên server tĩnh sau khi xử lý phụ thuộc; phiếu này chỉ build và kiểm gói trên ổ đĩa.

Trạng thái Git cuối chỉ gồm lượt đồng bộ kit ban đầu, 6 file sửa/tạo của mã–test–README và 1 changelog mới; chi tiết ở [status-final.txt](168/status-final.txt). Các báo cáo/bằng chứng chỉ nằm ở `docs/codex-queue/168-report.md` và `docs/codex-queue/168/` của repo cha; thay đổi sẵn có của tác nhân khác không được sửa.
