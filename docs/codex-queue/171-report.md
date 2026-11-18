# Phiếu 171 · JSON runtime trong kho media

Đã sửa bộ chọn và lưu bằng chứng offline. **Chưa đủ điều kiện đóng phiếu:** chưa chạy nguyên bộ `pnpm media:test`, do bộ test hiện có chạy `git init/add/commit/checkout` trong repo fixture tạm, còn phiếu cấm mọi lệnh Git ghi. Đã hỏi chủ dự án về ngoại lệ chỉ dành cho fixture; chưa nhận câu trả lời. Không chạy các lệnh đó trong lúc chờ.

## 1. Mã và tài liệu

| Đường dẫn | Thay đổi |
| --- | --- |
| `scripts/media/lib/sets.mjs` | Nhận JSON, kể cả đuôi `.JSON`, dưới `public/assets/<id>/` của đúng game; trừ danh sách tracked của repo cha và repo game, file rác, cache và file tạm. Dùng cùng quy tắc để kiểm đường dẫn trong `media.md5`, kể cả khi file chưa có trên máy. |
| `media/media.config.json` | Thêm riêng `sets.runtime.jsonExclude`; không thêm `json` vào danh sách đuôi media toàn cục, không sửa cấu hình `originals` hoặc `private`. |
| `scripts/media/lib/plan.mjs` | JSON thiếu trong thư mục model vẫn giữ trong danh sách md5 để tải về; không bị tự bỏ vì không phải URL model mà manifest liệt kê. |
| `scripts/media/test/runtime-json.test.mjs` | Thêm 3 ca: bộ chọn trên hai game và bảo toàn nhóm khác; biên đường dẫn/cache/tạm cho mọi cấu hình game; status, dry-run, md5 dự kiến và JSON chưa tải. Hai ca tạo fixture chưa chạy vì lệnh cấm Git ghi. |
| `docs/MEDIA_STORAGE.md` | Một đoạn ngắn về JSON runtime, cache/tạm và chuỗi push/pull/md5. |

Không sửa game, worktree, Tu Tiên, `media.md5` hoặc `media/private.md5`. Các lệnh status chỉ đọc dữ liệu game theo cấu hình có sẵn. Không dùng mạng, không push/pull thật, không build hay chạy bộ test game.

## 2. Test trước và sau

| Kiểm | Kết quả | Bằng chứng |
| --- | --- | --- |
| Trước sửa mã: ca biên JSON trong danh sách md5 | **0 xanh, 1 đỏ**, đúng tại `public/assets/space-typing/ground/manifest.json`, bị từ chối là `không phải file media` | [Log đỏ](171/test-json-red.txt) |
| Sau sửa: chạy lại đúng ca đó | **1/1 xanh** | [Log xanh](171/test-json-lock-green.txt) |
| Sau sửa: các ca chỉ dùng Git đọc hoặc hàm thuần | **16/16 xanh**, mã thoát 0 | [Log và tên từng ca](171/tests-read-only.txt) |
| Nguyên bộ `pnpm media:test` trước/sau | **Chưa chạy; không có số ca nguyên bộ được xác minh.** Fixture hiện có tự tạo repo và lịch sử bằng Git ghi. Cũng chưa có lần chạy đỏ của ca fixture JSON bị `.gitignore` bỏ qua. | [Fixture hiện có](../../scripts/media/test/fixture.mjs) |
| `git diff --check` | Mã thoát **0** | Đã chạy trên mã, cấu hình và hướng dẫn trong phạm vi phiếu. |

Không tính bộ test lọc 16 ca là nguyên bộ `pnpm media:test`. Mục kiểm bắt buộc số 1 **chưa đạt**. Cần cho phép Git ghi trong fixture tạm rồi chạy đủ bộ cũ, ca hồi quy đỏ trên mã cũ và bộ cuối; repo thật vẫn chỉ dùng Git đọc.

## 3. Status và dry-run

Cả `pnpm media:status --only runtime` và `pnpm media:push --dry-run --only runtime` trả mã **0**. Đầu ra: [status trước](171/status-runtime-before.txt), [status sau](171/status-runtime-after.txt), [dry-run](171/push-runtime-dry-run.txt), [danh sách từng file của dry-run](171/media-push-dry-run.txt).

| Game | Runtime trước → sau | Mới trước → sau | JSON mới |
| --- | --- | --- | --- |
| Space Typing | 423 → 423 | 0 → 0 | Không có |
| Dragonhold | 92 → 97 | 10 → 15 | 5 file bên dưới |
| Wordwoven | 137 → 137 | 0 → 0 | Không có |
| Last Line | 0 → 0 | 0 → 0 | Không có |
| Tu Tiên, chỉ được lệnh đọc theo cấu hình | 3 → 3 | 0 → 0 | Không có |

Năm JSON mới đều thuộc Dragonhold, đường dẫn tính từ `games/dragon-hold/`:

| Đường dẫn | Byte | md5 tính trên máy |
| --- | ---: | --- |
| `public/assets/dragon-hold/decals/manifest.json` | 1.343 | `086098cb7586c2fe82af69855fdc511d` |
| `public/assets/dragon-hold/ground/manifest.json` | 2.470 | `067774882d722d4d2af8919711bb0dc8` |
| `public/assets/dragon-hold/models/kit3/manifest.json` | 5.159 | `4375f731f03dccf535c0d2054d141a57` |
| `public/assets/dragon-hold/models/m0b/manifest.json` | 14.674 | `8306fedb0ea15d311fbfa1c5cccf885a` |
| `public/assets/dragon-hold/vfx/firefly/manifest.json` | 4.942 | `0c179fd7dd3773f7f8e8f3b08146176b` |

[Danh sách TSV](171/new-json.tsv) ghi cả trạng thái **Mới**. Dry-run có **15 file**: 5 JSON này và 10 ảnh VFX vốn đã mới trước sửa. Status chỉ in tổng số file mới theo nhóm; danh sách đầy đủ nằm trong TSV/dry-run. Mã push sẵn có đưa md5 từ bộ chọn vào kế hoạch `newLock`, xác minh Drive rồi mới ghi `media.md5`; chưa thực hiện bước ghi thật.

## 4. Nhóm khác và tác vụ đồng thời

[Status toàn bộ trước](171/status-before.txt), [sau](171/status-after.txt), [ảnh chụp trạng thái trước](171/snapshot-before.json), [sau](171/snapshot-after.json).

Hai lần status cách nhau có thêm **14 file originals của Wordwoven** và **11 file originals của Last Line**. Không kết luận hai log giống hệt: repo đang có agent khác làm media; phép so đầu tiên [báo khác dữ liệu](171/compare.txt). Không có đường dẫn originals nào được tác vụ này ghi.

Đã đối chứng bộ chọn nguyên bản từ `git show HEAD:scripts/media/lib/sets.mjs` với bộ chọn mới, lần lượt trên cùng dữ liệu đang có, cùng cache trong bộ nhớ. **5 nhóm originals và 1 nhóm private giữ nguyên toàn bộ đường dẫn, kích thước và md5; mọi runtime cũ giữ nguyên; chỉ thêm 5 JSON Dragonhold.** [Số liệu](171/selection-control.json), [kết quả](171/selection-control.txt), [mã kiểm](171/selection-control.mjs). Không khôi phục hay sửa file nguồn khi đọc bản cũ.

## 5. Phạm vi ghi và bàn giao

`git status --short -uall -- scripts/media media docs/MEDIA_STORAGE.md`: trước sạch, sau chỉ có **4 file sửa và 1 file test mới**, đều trong phạm vi. [Trước](171/git-status-before.txt), [sau](171/git-status-after.txt). Báo cáo và bằng chứng nằm trong `docs/codex-queue/171-report.md`, `docs/codex-queue/171/`.

[Trình bọc kiểm tra](171/offline-cache.mjs) giữ cache md5 chỉ trong bộ nhớ và chuyển danh sách dry-run từ `.cache/` sang thư mục phiếu; không sửa cache ở gốc repo. Tái chạy CLI đã dùng `NODE_OPTIONS='--import ./docs/codex-queue/171/offline-cache.mjs'` trước lệnh pnpm. [Mã chụp trạng thái](171/snapshot.mjs) và [mã so hai ảnh chụp](171/compare.mjs) cũng chỉ ghi bằng chứng trong phiếu.

**Chủ dự án cần xem:** ngoại lệ Git ghi chỉ trong fixture test để hoàn tất mục 1; các thay đổi dữ liệu đồng thời ở mục 4. Claude chỉ chạy push thật sau khi duyệt và sau khi kiểm thử bắt buộc đạt. Chưa có file nào được đẩy lên Drive trong lượt này.
