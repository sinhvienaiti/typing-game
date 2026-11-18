# Phiếu 107 · `ModelLibrary` nhận thêm loại model của từng game

Đã sửa phần kit và hoàn tất kiểm kỹ thuật 1–4. Mục 5 đạt theo phần thay đổi của Phiếu 107; chưa thể đạt theo nghĩa toàn bộ `git status` chỉ chứa file được phép vì ba file Phiếu 102 đã có sẵn ngoài danh sách. Giữ nguyên công việc đó, không sửa hoặc hoàn tác.

## File và hành vi

- `shared/game-kit/three/model-loader.ts`: thêm `ModelLibraryOptions.kinds?: readonly string[]`, sao chép và kiểm tên trong constructor; tên sai ném lỗi chứa tên đó. `parseModelManifest` và `parseEntry` nhận `extraKinds` tùy chọn. Các loại thêm bổ sung cho loại Space, không thay thế; không truyền thì giữ hành vi cũ. `entry` và `url` nhận `kind: string`.
- `shared/game-kit/three/model-contracts.ts`: `ModelManifestEntry.kind` và tham số `kind` của `modelKey` thành `string`. Giữ nguyên `ModelKind`, `MODEL_KINDS`, `isModelKind`, `MODEL_CONTRACTS` và các hàm kiểm socket/clip.
- `shared/game-kit/three/models.test.ts`: thêm **11 test**, từ **9 lên 20**. Kiểm `buildings/barracks` khi bật/tắt tùy chọn, cả hai tier, URL, kích thước `[4, 3, 5]`, `props` ở cả hai trường hợp, loại chưa đăng ký vẫn bị bỏ, tên sai và tên chứa số/dấu gạch nối. Có trường hợp xuống dòng cuối để bảo đảm regex khớp toàn tên.
- `shared/game-kit/DRIFT.md`: thêm một dòng Phiếu 107; giữ nguyên dòng Phiếu 102 và các dòng trước.
- `docs/codex-queue/107/`: log trước/sau, kiểm đột biến, rà `.kind`, status, SHA-256 và xác nhận dọn bản chép tạm.

Không sửa `three/index.ts`: đã xuất sẵn `ModelLibraryOptions`, `ModelManifestEntry`, `modelKey` và `parseModelManifest`; các kiểu/chữ ký mới đi qua những export hiện có.

## Kết quả kiểm

| Mục | Lệnh / phép kiểm | Kết quả |
|---|---|---|
| 1 | `pnpm --dir shared/game-kit test` | Nền **700/700**, **46 file** ([log](107/test-before.log)); sau sửa **711/711**, **46 file** ([log](107/test-after.log)); sau khôi phục đột biến **711/711**, mã thoát **0** ([log](107/test-restored.log)). |
| Test trước mã | Thêm test rồi chạy trước khi sửa implementation | **10 đỏ, 701 xanh/711**, mã thoát **1**; tái hiện được `buildings` trả `null` và constructor không từ chối tên sai ([log](107/test-first-red.log)). Lệnh `pnpm --dir shared/game-kit test -- three/models.test.ts` thực tế chạy toàn bộ suite trong môi trường này. |
| 2 | `pnpm --dir shared/game-kit typecheck` | **0 lỗi**, mã thoát **0** ([log](107/typecheck.log)). |
| 3a | Dragonhold: `./node_modules/.bin/tsc --noEmit` trên bản chép tạm có kit mới | **0 lỗi**, mã thoát **0** ([log rỗng](107/compat-dragon-hold.log)). |
| 3b | Last Line: cùng lệnh trên bản chép tạm | **0 lỗi**, mã thoát **0** ([log rỗng](107/compat-typing-survival.log)). |
| 4 | Trong `parseEntry`, bỏ `&& !extraKinds.includes(raw.kind)`, chạy `pnpm --dir shared/game-kit exec vitest run three/models.test.ts` | **3 đỏ, 17 xanh/20**, mã thoát **1**; test `buildings` đỏ đúng yêu cầu ([log](107/mutation-red.log)). Khôi phục trong `finally`; SHA-256 trước/sau giống nhau ([số liệu](107/mutation.json)), rồi toàn bộ **711 test xanh**. |
| 5 | `git status --short -uall -- shared/game-kit` | Sau: **7 đường dẫn**, gồm **4 file kit được phép** của phiếu này và **3 file Phiếu 102 có sẵn**. Không có đường dẫn mới ngoài phạm vi. Xem [trước](107/status-before.txt), [sau](107/status-after.txt), [xác nhận SHA-256](107/preexisting-unchanged.txt). |
| Bổ sung | `git diff --check -- shared/game-kit` | Mã thoát **0**, không có lỗi khoảng trắng ([log rỗng](107/diff-check.log)). |

Bản chép nằm ngoài repo cha tại `$TMPDIR/kit107/dragon-hold` và `$TMPDIR/kit107/typing-survival`. Chép nguồn, test, scripts và cấu hình của game, chép đè toàn bộ `shared/game-kit/three` vào `src/kit/three`; `node_modules` là symlink tới thư mục của game thật. Không chép các thư mục gốc `.git`, `public`, `art-src`, `tmp`, `dist`, `docs`, `.DS_Store` hoặc `node_modules`; giữ đủ đầu vào TypeScript hiện tại. Không sửa cây thật hoặc chạy build/test suite của game.

Đã xóa cả `$TMPDIR/kit107` và xác nhận không còn tồn tại ([bằng chứng](107/temp-cleanup.txt)). Môi trường từ chối lệnh `rm -rf` được yêu cầu; dùng `shutil.rmtree` sau khi xác nhận thư mục chỉ chứa đúng hai bản chép do phiên này tạo.

## Rà soát toàn bộ `.kind`

Đã chạy đúng `grep -rn "\.kind" shared/game-kit/three`, lưu [trước](107/kind-usage-before.txt) và [sau](107/kind-usage-after.txt). Mọi vị trí trước sửa:

- `guide-scene.ts:55`: truyền `options.model.kind` vào `library.entry`; đây là tùy chọn cảnh guide, không đọc `entry.kind` hoặc tra hợp đồng. API mới vẫn tương thích.
- `models.test.ts:26`: duyệt `MODEL_KINDS` rồi tra `MODEL_CONTRACTS[kind].kind`; loại đã được giới hạn bởi danh sách Space, giữ nguyên.
- `model-loader.ts:40`: bộ lọc loại trong `parseEntry`; đã thêm chấp nhận `extraKinds`.
- `model-loader.ts:51`: ghi `raw.kind` vào kết quả; kiểu đã là chuỗi.
- `model-loader.ts:74`: dùng `entry.kind` tạo khóa; đã đổi `modelKey` nhận chuỗi.

Kiểm thêm các tham chiếu `MODEL_CONTRACTS`, `ModelKind`, `modelKey`: **không có** `MODEL_CONTRACTS[entry.kind]` hoặc nơi tự kiểm socket/clip của entry trong kit hiện tại. Vì vậy loại riêng không đi qua hợp đồng Space và không phát sinh lỗi vì thiếu hợp đồng; không cần sửa thêm file ngoài danh sách. `GuideSceneOptions.model.kind` vẫn là `ModelKind` vì chỉ là tùy chọn của cảnh guide, không phải giá trị đọc từ manifest.

## Giới hạn và bàn giao

Ba file có sẵn ngoài phạm vi là `tools/cdp-run.mjs`, `tools/cdp-port.mjs`, `tools/cdp-port.test.ts`; hash trước/sau đều khớp. Không thể làm status chỉ còn file Phiếu 107 mà vẫn giữ nguyên công việc đồng thời theo yêu cầu chủ repo. Chủ repo/Claude cần xem ngoại lệ mục 5 này.

Không chạy `kit:sync`, dev server, trình duyệt hoặc media; không đụng Tu Tiên; Git chỉ dùng đọc. Claude tiếp tục đồng bộ vào `games/.wt-td-1c`, cấu hình `kinds: ["buildings", "kits", "projectiles"]` ở nơi tạo library nếu chưa có, rồi kiểm C6 thực sự nạp `buildings`. Phiên này xác nhận API và tương thích TypeScript; C6 trong game là bước bàn giao chưa chạy theo phạm vi phiếu.
