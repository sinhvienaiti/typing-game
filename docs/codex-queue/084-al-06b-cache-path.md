# Phiếu 084 · Thư viện tài sản · AL-06b: bộ nhớ đệm băm về đúng `library/.cache/hash.json`, mọi test quét đạt

**Bối cảnh:**
- AL-06 (phiếu 057) dời bộ nhớ đệm băm sang `library/out/hash.json`, vì danh sách được ghi của phiếu đó chỉ có `library/out`.
- Thiết kế (`docs/tools/ASSET_LIBRARY.md` §3.2) đặt bộ nhớ đệm ở `library/.cache/hash.json`.
- Hậu quả: 4 test của AL-05 (`tools/asset-library/test/scan-core.test.mjs`) và 1 test của AL-06 (`scan-joins.test.mjs`, ca `--locks-only`) đang trượt.

**Thư mục làm việc:** repo cha (`.`). **Báo cáo:** `docs/codex-queue/084-report.md`.

**Chỉ được ghi:**
- `tools/asset-library/scan.mjs`
- `tools/asset-library/lib/hash-cache.mjs`
- `tools/asset-library/test/scan-core.test.mjs`
- `tools/asset-library/test/scan-joins.test.mjs`
- `library/.cache/**`
- `library/out/**`
- `docs/codex-queue/084-report.md`

**Cấm:** lệnh git có ghi; mạng; ghi dưới `games/**`; đọc hay ghi Tu Tiên; sửa test để né lỗi thay vì sửa mã.

## Việc

1. Quét thường đọc và ghi bộ nhớ đệm ở `library/.cache/hash.json`. Bỏ `library/out/hash.json`; nếu file này còn thì đọc làm mồi một lần.
2. `--locks-only` không đọc, không stat media và **không ghi** bộ nhớ đệm.
3. Giữ nguyên mọi hành vi khác của AL-05 và AL-06.

## Kiểm (bắt buộc)

1. `node --test tools/asset-library/test/*.test.mjs`: mọi test đạt. In tổng số test đạt.
2. Chạy quét thật hai lần liên tiếp. Lần hai không băm lại file nào: in số file băm mới của lần hai, phải bằng 0.
3. Quét thật với `--locks-only`: md5 của `library/.cache/hash.json` trước và sau giống hệt.
4. `git status --short`: so với lúc bắt đầu, chỉ đổi file trong danh sách được ghi.

**Xong khi:** bốn kiểm đạt.
