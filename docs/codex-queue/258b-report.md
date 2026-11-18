# Báo cáo phiếu 258b · Công cụ đo GPU cho FlipbookPool bản 2

> **Claude duyệt (04/11/2026, 19:25): đạt, đã gộp cùng 258.**
> - Codex nêu đúng một lỗi của phiếu: lõi nóng là HDR (> 1), nên đòi số CPU nằm trong [0, 1] là sai. Lỗi do Claude viết phiếu; bỏ yêu cầu đó, chỉ giữ hữu hạn và không âm.
> - Ba ca Test 4 bị bỏ (`soft once`, `sharpen coverage`, `grade`) là đúng giới hạn của phiếu.
> - Claude sửa một chỗ: lab của `main` để sẵn một lỗi GL 1282 trước khi công cụ chạy (có cả trên `main`), nên công cụ rút lỗi cũ ra `staleErrors` trước khi đo. Sau sửa: đạt, chạy hai lần đều đạt.
> - Việc nợ nhỏ: tìm lệnh nào trong lab gây INVALID_OPERATION lúc khởi động.

Ngày 04/11/2026. Làm trong `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-immortality-cultivation-codex`, nhánh `codex/flipbook-v2`, HEAD `bf18505`. Không commit. Không ghi vào `games/immortality-cultivation/`.

**Trạng thái: đã viết công cụ và kiểm Node; còn chỗ dừng do yêu cầu số CPU mâu thuẫn với HDR. Chưa xác nhận GPU.** Áp dụng lời giải Claude giao, không chạy lại vòng duyệt thiết kế và không sửa shader để ép kết quả đạt.

## Tệp đã làm

Trong worktree:

- `src/lab/flipbook-probe.ts`: xuất `FlipbookProbeReport`, `ProbeCase`, `runFlipbookProbe`, `probeCases`, `cpuExpected`, `encodePngRgba`, `crc32`.
- `src/lab/skills-main.ts`: đúng ba vị trí được phép: một dòng import, khai báo phương thức kèm JSDoc, thân phương thức gọi `runFlipbookProbe(view.stage.renderer)`.
- `scripts/visual/scenarios/lab-flipbook-v2-probe.mjs`: mở URL cố định của phiếu, chờ `__lab.ready`, chờ kết quả probe, ghi JSON đẹp và trả tóm tắt.
- `tests/view/flipbook-probe.test.ts`: 10 test Node, không tạo WebGL.
- `docs/changelog/2026-11-04-flipbook-v2.md`: chỉ thêm mục “Công cụ đo GPU (258b)” ở cuối.

Ở repo cha: `docs/codex-queue/258b-report.md` (báo cáo này).

## Cách đo đã hiện thực

`runFlipbookProbe` lưu render target (kèm mặt cube và mức mip đang dùng), clear color/alpha, hai mục debug shader, `info.autoReset`, `autoClear`. Tạo ba PNG, nén bằng `CompressionStream("deflate")`, nạp xong trước khi đổi cờ renderer. Sau đó toàn bộ phép vẽ/đọc chạy đồng bộ, không gọi `requestAnimationFrame`, không gọi `__lab.step` và không đợi một khung lab giữa các mục. `finally` trả trạng thái renderer, dispose tài nguyên và thu hồi URL, kể cả khi tác vụ ném lỗi.

1. **Chương trình:** DataTexture atlas RGBA8 sRGB 64×32, hai ô 32×32; mặt nạ NoColorSpace cùng lưới, alpha thẳng, mipmap và lọc như thư viện. Meta đi qua `parseFlipbookManifest`, tên tệp hợp regex. Giữ đủ 18 pool đến cuối phép đo để chương trình không bị dispose trước khi lấy `p1 − p0`. Ghi từng hiệu số draw call và từng `currentProgram`; tiêu chí đạt giữ nguyên 9 chương trình khác nhau, thêm 9, mỗi pool một call, không lỗi shader/GL. Cờ `forceSinglePass` không bị công cụ thay đổi; ShaderMaterial trong three r170 mặc định đã đặt cờ này là `true`.
2. **GPU/CPU:** target 64×64 RGBA HalfFloat, không MSAA, không depth/stencil; camera trực giao của phiếu. Mỗi ca có pool riêng, ghi instance công khai sau `update(0)`. CPU giải mã chính byte atlas/mặt nạ, dùng `composeFlipbookMasked` với `soft: 1`, `FLIPBOOK_MASKED_LOOK`. Lượt nguồn tắt blending, đọc RGBA tại (32,32); lượt trộn giữ cấu hình pool, đọc lại nền vừa xóa và lấy RGB đó làm `dst` CPU. Đọc half float bằng `Uint16Array`/`DataUtils.fromHalfFloat`, không tone mapping hay bloom.
3. **Giải mã mặt nạ:** PNG 4×4 RGB (200,100,50), A = 1,3,8; chữ ký, IHDR RGBA8/filter 0/không interlace, một IDAT zlib, IEND, CRC chuẩn. TextureLoader giữ `flipY` mặc định, NoColorSpace, `premultiplyAlpha = false`, mipmap/lọc/clamp đúng thư viện. Quad ShaderMaterial xuất trực tiếp mẫu texture, NoBlending, target HalfFloat 4×4; đọc cả ảnh rồi lấy (1,1).
4. **Lỗi:** callback ghi lỗi compile/link; sau từng lần vẽ và đọc/xóa target, vét `gl.getError()` tới `NO_ERROR`. Kết quả `pass` là phép hội các tiêu chí của phiếu. Không có kết quả GPU giả lập hay đánh dấu đạt thay cho chạy thật.

## Các hệ số đã trung hòa

Đã đọc `VERTEX`, `FRAGMENT`, `FB_MASKED_GLSL` và đường v2 ở HEAD được giao. Danh sách này cũng nằm trong `gpuVsCpu.neutralised` của JSON:

| Hệ số/nhánh | Thiết lập và lý do ở điểm (32,32) |
| --- | --- |
| `vxSoftGround` | `iColor.a = ground = −100000`; đi thẳng nhánh `ground < −10000` trả 1, bỏ qua `uSoftM`. |
| `border` | size 2, aspect 1, pivot (0.5,0.5), góc 0, hướng 0; UV ở tâm điểm ảnh là (0.5078125,0.5078125), khoảng cách cạnh > 0.025 nên smoothstep = 1. |
| `uVignette` | Đặt 0, hệ số vignette = 1. |
| `vAlpha` | `iData.w = 1`, alpha/intensity = 1, fadeIn/fadeOut = 0. |
| `iLift`, nâng sâu, span | `iLift = (0,0)`, `iDir.xyz = (0,0,0)`; không nâng sâu hay đổi chiều rộng theo hướng, target không có depth. |
| Khung/biến thể | `iVar = 0`, `uStep = 0`, `uBlur = 0`, loop `none`; w giữ đúng số phần tư được chỉ định. |
| Sharpen/grade | Giữ mặc định look `(0,0)` và `(0,0,0,0)`; không đổi w bằng nhánh sharpen. |
| Burn/erode/occlude cũ | `iAge = (0,0,0,0)`, `iDir.w = 0`; nhánh masked gọi `fbComposeMasked` rồi return trước các nhánh cũ. |
| Sau phép ghép | Không có hệ số ngoài nào sau return masked; `soft = 1`, tint là đầu vào của phép ghép. |

Không phát hiện hệ số buộc phải đo bù; công cụ đặt `inconclusive = false`. Đây là phân tích mã để chuẩn bị phép đo, chưa phải xác nhận thực nghiệm GPU.

## Bảng ca và phần bỏ/dừng

`probeCases()` có **24 ca**: **16/19 ca có tên trong bảng Test 4** và **8 ca impact** theo thứ tự tick 0,1,3,9,12,18,20,42. Tất cả mẫu texture là byte nguyên; RGB atlas chuyển ngược tuyến tính → sRGB rồi làm tròn; mặt nạ/alpha làm tròn trực tiếp; CPU đọc lại byte. Các w thuộc {0,0.25,0.5,0.75}. Ca `premultiplied frame interpolation` vẫn làm được bằng hai ô của cùng một sprite nên không bỏ.

Ba ca có tên trong `gpuVsCpu.skipped`:

- `soft once`: cần `soft = 0.5`, trái yêu cầu trung hòa `soft = 1`.
- `sharpen coverage`: cần look `sharpen = (0.06,0.4)`, trái `cpuExpected` dùng look mặc định có sharpen = 0.
- `grade`: cần look `grade = (0.9,0.55,0.12,0.9)`, trái look mặc định có grade = 0.

Đây là giới hạn hợp đồng cố định của phiếu, không phải giới hạn kỹ thuật của sprite hay setter. Không tự thêm look riêng hoặc sửa các đầu vào để biến chúng thành ca khác. Test đếm tên trực tiếp từ bảng Test 4, in `16/19` và ba tên bỏ. Hai test `composeLayers` tổng quát (375 tổ hợp và các mốc nền đá), cùng kiểm chữ GLSL/sRGB trong Test 4, không phải các mẫu `composeFlipbookMasked` với look cố định; vẫn giữ nguyên test gốc, không tính chúng vào bảng 19 ca GPU.

**Dừng riêng yêu cầu “mọi số CPU hữu hạn trong [0,1]”.** `FLIPBOOK_MASKED_LOOK.hot = (1,0.982,0.871,2.2)` chủ ý cho lõi HDR. Với đúng mẫu impact được giao, RGB premultiplied và RGB sau trộn ở tick 0,12 đều lớn hơn 1 (bảng bên dưới). Không thể vừa giữ hàm/đầu vào đúng phiếu vừa đạt assertion đó. Test đã kiểm phần hữu hạn, alpha trong [0,1], `e = 1` và toàn bộ nguồn tick 42 bằng 0 ±1e−6; chưa viết assertion RGB ≤ 1. Không kẹp màu, không đổi look, không đánh dấu phiếu hoàn tất toàn bộ. Cần Claude chốt lại phạm vi assertion HDR và ba ca khác soft/look trước khi gộp.

## Các số CPU yêu cầu (4 chữ số thập phân)

`light`/`dark` ở đây dùng nền tuyến tính lý thuyết do `cpuExpected` trả. Khi chạy GPU, công cụ tính lại từ nền đã đọc được, đúng lượt 2 của phiếu.

| Tick | premul RGBA | light RGB | dark RGB |
| --- | --- | --- | --- |
| 0 | (1.8352, 1.6676, 1.4364, 0.9754) | (1.8517, 1.6831, 1.4496) | (1.8357, 1.6682, 1.4371) |
| 12 | (1.7604, 1.6297, 1.4315, 0.9754) | (1.7770, 1.6452, 1.4448) | (1.7610, 1.6303, 1.4322) |
| 42 | (0.0000, 0.0000, 0.0000, 0.0000) | (0.6724, 0.6308, 0.5395) | (0.0232, 0.0252, 0.0296) |

## Kiểm bắt buộc

Chạy tại worktree; công việc nặng chạy lần lượt qua `.local/bin/heavy.sh` ở repo cha (4 đơn vị CPU cho test, 2 cho build). Không chạy dev server hay trình duyệt.

| Kiểm | Lệnh/kết quả |
| --- | --- |
| 1 | `node node_modules/typescript/bin/tsc --noEmit -p .`: thoát 0, không lỗi sau khi sửa kiểu truy cập `renderer.properties`. |
| 2 | `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`: thoát 0; **917/917 test, 86/86 tệp**. Mốc trước theo phiếu **907 test / 85 tệp**, thêm **10 test / 1 tệp**. Không có test skip/todo; assertion HDR chưa triển khai được nêu riêng phía trên. |
| 3 | `IC_VITE_CACHE_DIR=/private/tmp/codex-258b-dist/.vite-cache node node_modules/vite/bin/vite.js build --outDir /private/tmp/codex-258b-dist --configLoader runner`: thoát 0, dựng 183 module. Thư mục chưa tồn tại trước khi chạy. `grep -rl "flipbookProbe\|fbComposeMasked\|encodePngRgba" /private/tmp/codex-258b-dist`: không in gì, thoát 1 đúng yêu cầu. Đã xóa thư mục build sau kiểm. |
| 4 | `node --check scripts/visual/scenarios/lab-flipbook-v2-probe.mjs`: thoát 0. |
| 5 | `git -C games/.wt-immortality-cultivation-codex diff --stat` và `status --short`: chỉ hai tệp theo dõi được phép sửa (changelog +8 dòng, skills-main +4 dòng) và ba tệp mới được phép. `node_modules` là mục chưa theo dõi đã có trước, không sửa. Báo cáo là một tệp mới riêng ở repo cha. `git diff --check`: thoát 0; diff `src/view/skills/flipbook.ts` rỗng. |

## Claude kiểm tiếp

`src/kit/tools/cdp-run.mjs` dòng 86–89 đặt `awaitPromise = true` mặc định cho `Runtime.evaluate`, nên kịch bản dùng trực tiếp `await page.eval("window.__lab.flipbookProbe()")`; kiểm `evalError` và timeout `ready` rõ ràng. Không dùng biến tạm trên `window` hay polling kết quả Promise.

Claude mở dev server của worktree rồi chạy lệnh trong phiếu, với `OUT_DIR` trỏ vào `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/flipbook-v2`. Tôi chưa tạo tệp capture, ảnh hay JSON GPU. Cần đọc JSON để xác nhận 18 pool/9 chương trình/mỗi pool 1 call, sai số tối đa ≤1/255, PNG alpha thấp và danh sách lỗi rỗng. Atlas cũ/fire/aura thuộc mục 2 phiếu 258, vẫn để Claude chạy bằng `lab-element-parity.mjs`.
