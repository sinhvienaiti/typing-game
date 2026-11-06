# Phiếu 326 · Critic · FAIL

Đã đọc mã thật trên `1b9461e` (flipbook.ts, comet-head, meteor-rain, showcase, skills-main + thanh chiêu, KTX2Loader r170, Vite 7.3.7). Baseline thật: `tsc` sạch; `tests/lab` 14 file / 79 test; `tests/view` 30 file / 421 test. Mốc chuỗi shader, dòng 601/619/627–628, `meteor-rain` 247/363 khớp; `replaceOnce`, `withTagMask`, `headDisc`, sweep card, fire strip vẫn chạy với chỗ chèn mới.

## Phải sửa
1. **Vỡ test cũ (hash shader).** `tests/view/flipbook-v2.test.ts` (`oldShader()`, gọi 6 lần) khoá `FRAGMENT_SHA` và độ dài `7272` của FRAGMENT. Mục 3 đổi FRAGMENT, mà file test này không có trong danh sách được ghi. Thêm vào **Được ghi**: "`W/tests/view/flipbook-v2.test.ts`: chỉ đổi `FRAGMENT_SHA` và số `7272` sang giá trị của FRAGMENT mới (in từ `unwrapTagMask(new FlipbookPool("c", "rgba", 1, 12, new THREE.Texture()).mesh.material.fragmentShader)`); `VERTEX_SHA` và `1823` giữ nguyên; báo cáo ghi giá trị cũ và mới."
2. **Vỡ test cũ (khoá `bytes`).** `GLINT` trong cùng file có `bytes: 725605`, và test đòi đúng 12 khoá `OLD_KEYS` (dòng 105, 181–182). Thay "`FlipbookMeta` thêm các trường tuỳ chọn `bytes`, …" bằng: "`bytes` (số nguyên ≥ 0) chỉ ghi vào meta khi mục có `ktx2` hoặc `motion` hợp lệ. Mục cũ có `bytes` (như GLINT) vẫn giữ đúng 12 khoá cũ."
3. **`loadClip` mơ hồ, mục hoãn mất KTX2 và vector.** Trong `load()`, biến `loader` là `TextureLoader`, nên "nếu có loader … thì loadAsync" có thể bị hiểu thành gọi `TextureLoader` với file `.ktx2`. `fetchAtlas(…, null)` thì không dùng KTX2, vẫn `add(meta, texture, null)` nên mất `mv`. Rồng là mục hoãn (role `beast`), nên bên phải của A/B sẽ luôn là PNG và không có vector. Thay bằng: "`loadClip(meta: FlipbookMeta, anisotropy: number, bitmap: boolean, png: THREE.TextureLoader | null)`. Loader KTX2 luôn lấy từ cấu hình `setFlipbookKtx2` (biến cấp module), không qua tham số. `png` chỉ dùng cho đường PNG khi `bitmap` false (`loadAtlas(png ?? new THREE.TextureLoader(), …)`). `fetchAtlas()` gọi `loadClip(meta, this.anisotropy, true, null)` rồi `this.add(meta, r.texture, r.mv ? { mv: r.mv } : null, r.source)`. Test thêm một ca: mục hoãn qua `fetchAtlas` gọi đúng URL `uastc` và có `controls.mv`."
4. **Sao chổi: thay rim lai và tiêu chí sẵn sàng.**
   - Hai mục cùng id `fire-comet`, nên `comet().id` bắt đầu bằng `fire-comet` ngay cả khi rim còn của hệ.
   - A/B có thể báo sẵn sàng rồi ngừng gọi `prepareComet()`. Lần bắn đầu sẽ `drop()`, tạo lại video, và nửa trái trống.
   - Luật `drop()` ở mục 4 cũng không nói chỉ áp dụng ngoài mode `"video"`.

   Thay bằng: "Luật `drop()` rồi lấy lại chỉ áp dụng khi `mode !== "video"`; ở `"video"` rim luôn của hệ. Video (trong `load()` và chỗ nạp lại `src` trong `update()`, hiện đọc `this.rim.meta.video`) lấy từ `video` của mục hệ, giữ trong một trường riêng. Thêm getter `upgraded` (rim lấy từ thư viện lai). Cảnh `meteor`: `load()` chờ `player.ready("hybrid")` và `player.ready("fire")`, rồi gọi `prepareComet()` ở mỗi `update` cho tới khi có `comet().upgraded` (trừ `only=left`). Điều kiện sẵn sàng thêm `comet().upgraded`; `ready` đã true thì giữ true."
5. **Lab mặc định đổi hành vi.** `hybridLib` tạo vô điều kiện, nên lab không tham số vẫn tải và giải nén atlas lai 3072×3456 cùng vector của `fire-comet` (role `comet` không bị hoãn), lại khởi động transcoder. Thay bằng: "`const hybridLib = AB_SCENE !== null || params.get("cometFlip") === "1" || params.get("video") === "0" ? stage.flipbooks.library("hybrid", (m) => m.role !== "comet") : undefined;`. Host `MeteorRain` nhận `upgrade: hybridLib`. Lab không tham số không tải thư mục `hybrid/`."
6. **Pool phải của cảnh clip chưa có thông số.** Mode, order và vignette chưa ghi. Vignette lệch thì hai nửa khác góc thẻ. Thêm: "pool phải: `new FlipbookPool(id + "#ab", "fire", 1, 15, blank)`, `vignette = 0.35`, như pool trái."
7. **Quay bị chồng hai trận mưa.** `castMeteor()` không xoá trận trước, nên trận làm nóng còn rơi trong khoảng 4,5 s đầu của MP4, và bầy quái đã bị đánh. Sửa mục 7 `capture`: "làm nóng: `abStart()`, `step(60, 1/30)`, `__lab.reset()`, rồi `abStart()`".
8. **"Dòng 1305" không trích nội dung.** Trên nhánh này dòng 1305 là `meteor.comet.driven = fixed;`. Viết: "Thay dòng `meteor.comet.videoOn = params.get("video") !== "0";` bằng …; giữ dòng `meteor.comet.driven = fixed;` ngay trên."
9. **Số test trước phiếu sai.** Sửa thành: "`tests/lab` 14 file / 79 test, `tests/view` 30 file / 421 test."

## Ghi chú (không chặn)
- Vite trong worktree: `.wasm?url` vào `safeModulePaths`. `basis_transcoder.js` (không có import) đi qua transform nên giữ nguyên. Nên thêm bước `curl -sI` cả hai URL (mong 200) trước khi chạy kịch bản.
- Tấm ghép ffmpeg nên có `-frames:v 1`.
- `uploadMs` chưa định nghĩa: nên ghi "ms của các lệnh `initTexture` lúc prewarm, 0 khi không prewarm".
- Crop của sao chổi ≈ 1094/1080: thẻ lai to hơn video khoảng 1,3 %. Có thể nhân `abCardScale(meta.sourceRect)` cho rim lai.
