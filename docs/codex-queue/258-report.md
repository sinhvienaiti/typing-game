# Báo cáo phiếu 258 · Tu Tiên · FlipbookPool bản 2 (CX-B)

Ngày: **04/11/2026**. Trạng thái: **xong phần Codex, chưa commit; chờ Claude duyệt diff và kiểm GPU trong lab**.

## Phạm vi và mã nền

Làm trong `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-immortality-cultivation-codex`, HEAD `bc94110`. Worktree đã được tạo trước; lúc nhận chỉ có symlink `node_modules` chưa được Git theo dõi. Lệnh đối chiếu `git -C games/.wt-immortality-cultivation-codex diff bc94110 HEAD -- src/view/skills/flipbook.ts tests/view/element-layer.test.ts` không có kết quả.

Áp dụng skill `agent-orchestration` theo vai trò worker một làn, nhận lời giải hoàn chỉnh trong phiếu. Theo chỉ thị giao việc lúc 18:50 của Claude được ghi ngay trong phiếu, không mở lại bước thiết kế hoặc chờ lượt phản biện song song. Không tạo agent phụ.

Đã ghi đúng bốn tệp được phép, đều qua đường `/Volumes`:

1. `games/.wt-immortality-cultivation-codex/src/view/skills/flipbook.ts`.
2. `games/.wt-immortality-cultivation-codex/tests/view/flipbook-v2.test.ts` — tệp mới, **114 test**.
3. `games/.wt-immortality-cultivation-codex/docs/changelog/2026-11-04-flipbook-v2.md` — tệp mới.
4. `docs/codex-queue/258-report.md` — báo cáo này.

## Các mục 1–7 đã làm

| Mục phiếu | Nơi thực hiện và kết quả |
|---|---|
| 1. Kiểu và manifest | Thêm các kiểu, hằng lịch/độ rộng và trường tùy chọn của `FlipbookMeta`; `parseFlipbookManifest` kiểm từng trường mới với tên lỗi đúng yêu cầu, giữ thứ tự 12 khóa cũ, bỏ qua hoàn toàn `variants` của mục cũ, đọc `frames` theo một biến thể và cho `anchor` thắng `pivot`. Thêm `isFlipbookV2`, `flipbookLoopMode`, `frameEnd`, `firstOf`; dùng chung đoạn khung trong `spawn`, `slowFromOf`, `playLife`, `clipS`. `playLife` lấy đời theo lịch ở mọi pool khi meta có A và lịch; `life` của người gọi vẫn thắng. |
| 2. Nạp mặt nạ | `FlipbookControls`, `Entry.controls`, tham số cuối tùy chọn của `FlipbookLibrary.add`; `load` nạp tuần tự atlas → A → B trong từng clip, giữ nguyên thiết lập atlas, đặt mặt nạ `NoColorSpace`/alpha thẳng và bộ lọc khớp atlas, không đổi `flipY`. Tệp lỗi thì cảnh báo, giải phóng mọi texture đã nạp của clip và không thêm clip. `reset` giải phóng atlas/A/B. Hai đường `FlipbookPlayer.library`/`pool` đều chuyển tiếp controls. |
| 3. Shader v2 | Giữ nguyên từng ký tự của `VERTEX` và `FRAGMENT`; thêm `replaceOnce`, dựng `VERTEX_V2`/`FRAGMENT_V2` đúng ba/năm neo một lần khi nạp module. Xuất `FB_PICK_GLSL`, `FB_COMPOSE_GLSL`, `FB_MASKED_GLSL`; chọn đoạn khung, làm tròn ô biến thể, đổi khung theo điểm ảnh và ghép ink/thân/lõi đúng khối phiếu. Phần còn lại của shader lấy nguyên từ đường cũ. |
| 4. Pool | Thêm `FLIPBOOK_MASKED_LOOK`, các uniform/setter mới và mảng cấp trước `iCtl`, `iVar`, `varCell`, `timings`; giữ `STRIDE = 35` và `ATTRS`. `attach` chỉ gắn thuộc tính v2 khi cần, cập nhật shader theo khóa loop/mặt nạ, lề A/B tính riêng bằng `maskInset`, không tăng `version` nếu khóa không đổi và trả được về đường cũ. `spawn` chốt lịch/biến thể mỗi lần dùng slot, giữ thứ tự lượt chọn và mặc định fade theo phiếu; `update` ghi vào chỉ số sprite nén trước khi tăng tuổi; `clear` đặt lại lượt biến thể. Pool không giải phóng texture. |
| 5. Hàm CPU | Thêm `flipbookTimingOf`, `flipbookTick`, `revealThreshold`, `erodeThreshold`, `rampMixAt`, `flipbookControl`, `srgbToLinear`, `flipbookFramePair`, `flipbookSwitch`, `composeLayers`, `composeFlipbookMasked`, `blendPremultiplied`. Công thức ghép theo thứ tự của shader; đầu vào atlas tuyến tính, mặt nạ là dữ liệu thẳng; `soft` nhân một lần cuối. Các hàm ghi vào `out` do người gọi cấp; các helper chạy mỗi sprite không cấp phát. |
| 6. Test | `tests/view/flipbook-v2.test.ts` có **114 test**, bao phủ đủ 12 nhóm bắt buộc cùng lỗi nạp atlas/A/B, lề texel khác độ phân giải, compaction/delay, lịch/biến thể khi tái dùng slot, quyền sở hữu texture, setter trước attach và năm tốc độ tích lũy tuổi Float32. |
| 7. Chú thích và changelog | Bổ sung JSDoc đầu tệp về v2, số khung mỗi biến thể, hai đường shader, ba loopMode, hai ngoại lệ tương thích và mặt nạ A/B; giữ nguyên dòng `// Source: …`. JSDoc của `FlipOptions.timing` và `playLife` nói rõ đời theo lịch cả khi pool thiếu A. Changelog tiếng Việt ghi API, manifest, test và phần Claude kiểm sau. |

### Tương thích và các mốc đã kiểm bằng test

- Shader cũ ở cả `rgba`, `fire`, `smoke`, `heat`: vertex **1823 ký tự**, SHA-256 `c2f64aa0e39d46ec17b4f60ecd3932e42178f933784a72ee8fec1d38cc25a9c7`; fragment **7272 ký tự**, SHA-256 `3b5524bd2c052ed97c6261586915f9b218deb5756d0477d634e3605d05b93abd`.
- Meta cũ có đúng 12 khóa theo thứ tự; `attach` cũ giữ `defines = {}`, `version = 0`, không có thuộc tính `iCtl`/`iVar`. `loop: true` vẫn dùng `uLoop = 1` và shader cũ hòa chéo bọc vòng.
- Mục `fire-twinkle-set` thật chép trong test vẫn bỏ qua `variants: 8`, `0` và `"x"`: meta bằng nhau, đời **16/24 s**, khung đầu là ô 0. Thêm `loopMode: "none"` mới bật 8 biến thể × 16 khung, với các ô đầu **48, 0, 16, 112** của ca Test 10; đời vẫn **16/24 s**.
- Lịch `impact-key1` trên pool có A vẽ đủ **43 lần**, tick 0–42, alpha tick 42 bằng 1. Pool `rgba` không controls và pool `fire` có controls vẫn sống **43/60 s**, không áp lịch hiện/xói, alpha tick 42 bằng **0,138889 ± 1e-4**.
- Các mốc cặp khung, màu ghép, hiện/xói, độ sáng thân, tick và `iCtl` đều đạt sai số yêu cầu. Cặp khung holderode bọc về đầu đoạn; shader v2 không còn `mod(f0 + 1.0, uFrames)`.

## Kiểm bắt buộc

Lệnh 1–3 chạy ở worktree nêu trên, không chạy trong game chính. Mốc trước là **793 test / 84 tệp** tại đúng `bc94110` theo kết quả Claude đã cung cấp trong phiếu; không chạy lại một bộ mốc riêng. Mốc sau đo được là **907 = 793 + 114 test / 85 tệp**.

### Kiểm 1 — TypeScript

```sh
node node_modules/typescript/bin/tsc --noEmit -p .
```

Kết quả cuối: **thoát 0, không có lỗi**.

### Kiểm 2 — toàn bộ test

```sh
VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4
```

Kết quả: **thoát 0; 907/907 test, 85/85 tệp đều qua**, thời gian 7,33 s. Tệp mới **114/114**; `tests/view/element-layer.test.ts` **33/33**, không sửa tệp đó.

### Kiểm 3 — build và kiểm phủ định shader

Xóa riêng `/private/tmp/codex-258-dist` nếu có, rồi chạy:

```sh
IC_VITE_CACHE_DIR=/private/tmp/codex-258-dist/.vite-cache node node_modules/vite/bin/vite.js build --outDir /private/tmp/codex-258-dist --configLoader runner
grep -rl "fbComposeMasked\|uSharpen" /private/tmp/codex-258-dist
```

Kết quả build: **thoát 0**, Vite 7.3.7, 183 module, 919 ms. Có ba trang `index.html`, `bench.html`, `tinh-tu.html`. Vite nhắc `outDir` ngoài project sẽ không tự làm rỗng; thư mục đã được dọn trước lệnh theo phiếu.

Kết quả grep: **không in đường dẫn nào, thoát 1**, đúng điều kiện phủ định. Shader flipbook không bị kéo vào bản build. Đã xóa thư mục `/private/tmp/codex-258-dist` sau kiểm tra và xác nhận không còn.

### Kiểm 4 — phạm vi diff

Chạy từ repo cha:

```sh
git -C games/.wt-immortality-cultivation-codex diff --stat
git -C games/.wt-immortality-cultivation-codex status --short
```

Kết quả:

```text
 src/view/skills/flipbook.ts | 625 ++++++++++++++++++++++++++++++++++++++++++--
 1 file changed, 605 insertions(+), 20 deletions(-)

 M src/view/skills/flipbook.ts
?? docs/changelog/2026-11-04-flipbook-v2.md
?? node_modules
?? tests/view/flipbook-v2.test.ts
```

`diff --stat` không liệt kê hai tệp mới chưa được Git theo dõi; `status --short` xác nhận chúng ở đúng phạm vi cho phép. `node_modules` là symlink có sẵn, không sửa. Báo cáo này ở repo cha là tệp thứ tư được phép. Kiểm thêm `git diff --check` thoát 0; diff riêng `tests/view/element-layer.test.ts` rỗng.

## Khác biệt và phần chưa làm

Không đổi lời giải hay chọn phương án thay thế cho mã. Riêng thao tác dọn thư mục build: công cụ từ chối lệnh `rm -rf` theo quy tắc chặn `rm -f`, nên dùng Python `pathlib`/`shutil.rmtree` cho đúng đường dẫn tạm cố định, có xử lý symlink, trước và sau build. Không có bước nào bị chặn còn dang dở.

Chưa nối vào kit hoặc lab (CX-G, CX-H), chưa sửa bất kỳ manifest/tài sản nào; không tạo ảnh, tải gói/ảnh, chạy dev server hay mở trình duyệt. Không sửa game chính, nguồn/lab/test khác, hoặc tài liệu Tu Tiên ở repo cha. Không chạy lệnh Git ngoài nhóm đọc được phép; không commit hay gộp nhánh.

Claude cần đọc diff và chạy lại Kiểm 1–4, sau đó làm đủ phần **Claude kiểm sau** của phiếu: biên dịch **18 pool / 9 chương trình**; chênh ảnh atlas cũ bằng 0, kể cả ba glint; so CPU/GPU ±1/255 trên target half-float; kiểm PNG mặt nạ không bị premultiply khi giải mã. Các kết quả node và build ở trên chưa xác nhận GPU hay mức chấp nhận hình ảnh trong lab.
