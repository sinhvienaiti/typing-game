# Phiếu 325 · Công cụ: `vfxflip upgrade` (flipbook nâng cấp: ô to, 12–24 khung/giây, vector chuyển động, KTX2)

**Vì sao:** anh đồng ý thử "cách lai" ngày 06/11 và cần xem demo A/B trước khi chốt (`.agents/skills/game-vfx-production/references/runtime-packaging.md`). Theo cách này, thứ lặp lại dùng flipbook ô to hơn, 12–24 khung/giây, trộn khung bằng vector chuyển động và nén KTX2. Số đo nằm ở `docs/games/tu-tien/skills/SKILL_TECH_OVERVIEW_2026-11-06.md`: mục 3 (thử clip `azure-cloud-dragon`) và mục 6 (bước 2, 3). Phiếu này thêm một lệnh vào `tools/vfx-flipbook`. Phiếu 326 dùng đầu ra của nó trong lab.

**Model `gpt-6.1-sol`, mức `xhigh`.** Báo cáo: `docs/codex-queue/325-report.md` (tiếng Việt, ngắn). Mọi lệnh chạy từ gốc repo cha `/Volumes/SS990TPRO/htdocs/typing-game`.

## Máy này có gì (Claude kiểm ngày 06/11)
- **Có:** `ffmpeg`, `ffprobe` (có bộ lọc `ssim`), `node` 24, `npm`, `uv` 0.13.5; Python 3.12 ở `~/AudioLab/python/cpython-3.12-macos-aarch64-none/bin/python3.12`. Venv `~/AudioLab/.venv` có numpy 2.5.4, scipy 1.18.1, Pillow 13.0.0, pytest 9.1.1.
- **Claude đã cài sẵn hai bước dưới đây lúc 20:00 ngày 06/11** (sandbox của Codex không có mạng): `tools/vfx-flipbook/.venv` có đủ gói của `requirements.txt` (`cv2` 4.14.0, numpy 2.5.4), và `tools/vfx-flipbook/ktx2/node_modules` có `ktx2-encoder` 0.6.0 và `ktx-parse` 1.1.0, cùng `ktx2/package.json` đúng nội dung ở bước 2. **Không chạy lại hai lệnh cài, không dùng mạng.** Chỉ kiểm `tools/vfx-flipbook/.venv/bin/python -c "import cv2"` và có thư mục `ktx2/node_modules/ktx2-encoder`; thiếu thì dừng và ghi báo cáo.
- **Không có (ngoài hai chỗ trên):** `basisu`, `toktx`, và OpenCV (`cv2`) trong mọi Python khác. Cấm cài toàn máy (`brew`, `pip --user`, `npm -g`) và cấm AI nặng. Chỉ cài vào thư mục công cụ, và chỉ được dùng mạng cho đúng hai bước dưới đây:
  1. **Python:** chạy `uv venv --python ~/AudioLab/python/cpython-3.12-macos-aarch64-none/bin/python3.12 tools/vfx-flipbook/.venv`, rồi `uv pip install --python tools/vfx-flipbook/.venv/bin/python -r tools/vfx-flipbook/requirements.txt`. File `requirements.txt` (mới) ghim `numpy==2.5.4`, `scipy==1.18.1`, `pillow==13.0.0`, `pytest==9.1.1`, `opencv-python-headless==4.14.0.94` (wheel abi3 macOS arm64, 46 MB, ra ngày 29/07/2026).
  2. **KTX2:** tạo `tools/vfx-flipbook/ktx2/package.json` (mới) với nội dung `{"name":"vfxflip-ktx2","private":true,"type":"module","dependencies":{"ktx2-encoder":"0.6.0","ktx-parse":"1.1.0"}}`, rồi chạy `npm install --no-audit --no-fund --prefix tools/vfx-flipbook/ktx2`. Gói `ktx2-encoder` 0.6.0 (MIT, ra ngày 19/07/2026) có sẵn `basis_encoder.wasm` của Basis Universal; bảng đo ở mục 3 đã dùng gói này.
- **`run.sh`:** khi `$VFXFLIP_PY` trống và có `$HERE/.venv/bin/python` thì dùng Python đó; không có thì dùng `~/AudioLab/.venv/bin/python` như cũ. Ghi hai bước cài vào chú thích đầu file. Thêm `.venv/` vào `tools/vfx-flipbook/.gitignore` (gốc repo đã bỏ qua `**/node_modules/`).

## Được ghi và cấm
- **Được ghi:**
  - trong `tools/vfx-flipbook/`: `run.sh`, `.gitignore`, `requirements.txt` (mới), `vfxflip/{__main__,pipeline,timing,grade,video_export}.py`, các file mới `vfxflip/{motion,ktx2,upgrade}.py`, `ktx2/{package.json,package-lock.json,encode.mjs}` (mới), `ktx2/node_modules/`, `.venv/` và test mới `tests/test_upgrade.py`;
  - thư mục đầu ra mới `games/immortality-cultivation/art-src/lab/vfx/hybrid/`;
  - thư mục ảnh chụp `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/vfxflip-325/` (kèm `ABOUT.md`);
  - báo cáo.
- **Cấm:** mọi lệnh git ghi; sửa file nào khác, kể cả bảng `immortality-cultivation.json`, mọi manifest và media khác trong `art-src`, và video Firefly gốc; mở trình duyệt; cài gì ngoài hai bước trên.

## Lời giải đã chốt
1. **`pipeline.py`, `timing.py`, `grade.py`**
   - `DEFAULTS` thêm `"fps": None, "look": "cool"`. Các dòng bảng cũ không có hai khoá này nên chạy y như trước.
   - Trong `process()`, ngay sau `fps = info["fps"]` (dòng 323):
     - nếu có `params["fps"]`, tính `r = fps / float(params["fps"])`;
     - nếu `r < 1` hoặc `abs(r - round(r)) > 1e-6` thì `raise media.MediaError` (nói rõ fps phải chia hết fps nguồn: với nguồn 24 là 6, 8, 12 hoặc 24);
     - `fixed_step = int(round(r))`; không có `params["fps"]` thì `fixed_step = None`;
     - `look` ngoài `"cool"`/`"neutral"` thì `ValueError`.
   - **Nhánh lặp** (dòng 367): `step=fixed_step or int(params["step"])`.
   - **Nhánh một lần:** khi có `fixed_step`, gọi `plan = timing.fixed_rate(plan, fixed_step, int(params["frames"]))` ở hai chỗ, mỗi lần gán lại `idx = plan["indices"]`:
     - ngay sau `plan_oneshot`, trước `span` (dòng 387);
     - ngay sau `plan = timing.refine_start(...)` (dòng 476).
   - **`timing.fixed_rate(plan, step, n_max)` (mới):**
     - `idx = list(range(start, end, step))`;
     - nếu `len(idx) > n_max`: cắt còn `n_max` khung, `end = min(end, idx[-1] + step)`, `capped = True`, `faded = False`;
     - trả `dict(plan, indices=idx, step=float(step), frames=len(idx), end=end, capped=…, faded=…)`.
   - **Look:**
     - dòng 484 chỉ dùng `grade.cool_dim` khi look là `cool`; khi `neutral` thì `post = None`;
     - dòng 523 dùng `grade.cool_fade` khi `cool`, `grade.neutral_fade` (mới) khi `neutral`;
     - `neutral_fade` chép đúng hàm cùng tên ở `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/lab-flipbooks/lab_batch.py` dòng 270–277. Atlas của mọi hệ trừ Hỏa đã được làm theo hàm này.
2. **`vfxflip/motion.py` (mới).** `import cv2` đặt trong hàm; thiếu gói thì báo lệnh cài.
   - `cells_from_atlas(png, cols, rows, cw, ch, n)` trả `uint8 (n, ch, cw, C)`.
   - `luma8`: lấy `max(R,G,B)` (ảnh RGBA thì nhân thêm `A/255`), rồi đổi thành `round(255·(x/255)^0.5)` kiểu `uint8`.
   - **`flow(cells, loop)`:**
     - Tính từng cặp khung n → n+1. Clip lặp thêm cặp cuối → đầu; clip một lần cho khung cuối vector 0.
     - Dùng `cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_MEDIUM).calc(g0, g1, None)`, ra `(dx, dy)` tính bằng pixel: điểm `p` của khung n nằm ở `p + (dx, dy)` trong khung n+1.
     - Mặt nạ: lấy `(g0 > 8) | (g1 > 8)`, nở bằng `cv2.dilate` với nhân 9×9, làm mờ bằng `ndimage.gaussian_filter(σ=2)`, rồi nhân vào vector.
     - Đổi sang UV của ô: `u = dx/cw`, `v = -dy/ch` (trục y hướng lên, như shader).
   - **`strength`:** phân vị 99,5 của `|u|` và `|v|` trong vùng mặt nạ, tối thiểu `1e-4`, làm tròn lên 5 chữ số thập phân.
   - **Mã hoá:** `byte = clip(round(128 + 127·c/strength), 1, 255)`. **Giải mã:** `c = (byte − 128)/127·strength`.
   - **Bố cục `x-rgb-y-a`:** R = G = B = byte của u, A = byte của v. Basis nén RGB và A riêng nên hợp với dữ liệu hai kênh. Atlas vector cùng lưới với atlas màu; ô thừa điền 128.
   - **`warp_blend(f0, f1, d_px, w)`:** mẫu chuẩn, giống shader của phiếu 326:
     - `t0` = f0 lấy mẫu tại `q − w·d`; `t1` = f1 lấy mẫu tại `q + (1−w)·d` (song tuyến bằng `cv2.remap`, ngoài viền là 0);
     - kết quả `(1−w)·t0 + w·t1`.
   - **`warpRatio`:** với mỗi cặp có `mean|f1−f0| > 0.5/255`, tính `mean|warp(f0, w=1) − f1| / mean|f1−f0|`, dùng vector đã mã hoá rồi giải lại. Ghi trung vị và p90.
3. **`vfxflip/ktx2.py` và `ktx2/encode.mjs` (mới).**
   - **Phía Python:**
     - Ghi RGBA thô ra file tạm cạnh file đầu ra (hàng 0 là hàng trên cùng).
     - Gọi `node <encode.mjs> --raw <tạm> --width W --height H --out <file>.tmp --codec uastc|etc1s --transfer srgb|linear --uastc-level 2 --etc1s-quality 150`, với `<encode.mjs>` là đường dẫn tuyệt đối `pipeline.TOOL_DIR / "ktx2" / "encode.mjs"` (không phụ thuộc thư mục hiện hành; `run.sh test` đổi thư mục vào `tools/vfx-flipbook`). `skipif` của test KTX2 kiểm `shutil.which("node")` và `TOOL_DIR / "ktx2/node_modules/ktx2-encoder"`.
     - Đọc dòng JSON cuối của stdout, `os.replace` sang tên thật, xoá file tạm. Lỗi thì ném `Ktx2Error`.
   - **`encode.mjs`:**
     - Gọi `encodeToKTX2(raw, {isUASTC, isYFlip: true, generateMipmap: true, isKTX2File: true, enableDebug: false, imageDecoder: async () => ({width, height, data: raw}), …})`.
     - Codec UASTC: `uastcLDRQualityLevel: level, needSupercompression: true`. Codec ETC1S: `qualityLevel: q, compressionLevel: 2`.
     - Transfer `srgb`: `isSetKTX2SRGBTransferFunc: true, isPerceptual: true`. Transfer `linear` (cho vector): `isSetKTX2SRGBTransferFunc: false, isPerceptual: false, isNormalMap: true`.
     - Đọc lại file bằng `read` của `ktx-parse`, in `{width, height, levels, supercompression, transfer, colorModel, bytes, encodeMs}`.
   - **Bắt buộc `isYFlip: true`:** shader lab đọc ô theo quy ước của PNG đã lật (`vxCell`, `flipY`), mà texture nén thì không lật được lúc nạp.
4. **Lệnh `upgrade`** (`vfxflip/upgrade.py` mới; hàm `run(...)` nhận thêm `home` và `table_dir` để test truyền thư mục tạm):
   ```
   run.sh upgrade --like <manifest.json>:<id> --out <thư mục> --cell WxH --fps N [--frames 64] [--look cool|neutral] [--no-mv]
                  [--ktx2 uastc,etc1s|none] [--videos crf23,720p] [--uastc-level 2] [--etc1s-quality 150] [--max-atlas 4096] [--game immortality-cultivation] [--repo-root <dir>]
   ```
   - **Kiểm tham số:** `6 ≤ fps ≤ 24`, nhưng `fps < 12` chỉ được khi có vector (không có `--no-mv`), vì vector chuyển động là thứ làm nhịp thấp vẫn mượt; mỗi cạnh ô từ 16 đến 1024 và chia hết cho 4; `frames ≥ 2`.
   - **Trần atlas:** `--max-atlas N` (mặc định 4096). Sau bước b, nếu cạnh lớn nhất của atlas (lưới lũy thừa 2 của `atlas.grid`) vượt N thì dừng với lỗi rõ ràng, ghi số khung và lưới, không ghi file ra `<out>`. Lý do: một số máy người chơi chỉ nhận texture tới 4096, và bản demo A/B phải so cùng điều kiện có thể phát hành.
   - **`--look`:** mặc định `cool` khi thư mục chứa manifest `--like` là `fire`, còn lại `neutral` (như `lab_batch.py`).
   - **`--repo-root`:** mặc định `parents[3]` như `export-video`.

   Các bước:
   a. Đọc mục `<id>` trong manifest like, lấy `job` và `source` (tính từ repo-root).
   b. Lấy `params = pipeline.clip_params(load_table(game, table_dir), job)`, cộng thêm `cell`, `frames`, `fps`, `look`. Chạy `pipeline.process(source, <home>/out/<game>/upgrade/<id>/, game, job, "v1", params)`.
   c. Chép `<job>__v1.atlas.png` thành `<out>/<id>.atlas.png`, và `<job>__v1.json` thành `<out>/<id>.json` (thêm `id`, `element` = thư mục like, `role`, `job`, `take`, `image`, khối `upgrade`).
   d. Vector (bỏ qua khi có `--no-mv`): ghi `<id>.mv.png`.
   e. KTX2: ghi `<id>.<codec>.ktx2` (sRGB) và `<id>.mv.<codec>.ktx2` (linear).
   f. **Video** (chỉ clip một lần):
      - đoạn cắt lấy đúng `video_export.calculate_cut(mục like)`, lệnh ffmpeg giống `_export_one`, chỉ khác `-crf`;
      - `crf23`: giữ khung gốc, CRF 23, ra `<id>.crf23.mp4`;
      - `720p`: nối thêm `,scale=-2:720:flags=lanczos` vào cuối `-vf`, CRF 20, ra `<id>.720p.mp4`;
      - đọc lại thông số bằng `_probe_video`;
      - SSIM so với chính đoạn nguồn: `ffmpeg -i <bản nén> -i <nguồn> -lavfi "[1:v]select='between(n,S,E-1)',setpts=N/(24*TB)[r];[0:v]scale=<srcW>:<srcH>:flags=bicubic[d];[d][r]ssim" -f null -`, lấy số `All:`.
   g. **Ghi `<out>/manifest.json`:**
      - chưa có thì tạo `{"version": 1, "kind": "lab-hybrid", "note": "<một câu: phiếu 325/326, cách lai>", "flipbooks": {}}`;
      - chỉ thay mục `<id>`, giữ nguyên mục khác;
      - ghi nguyên tử bằng `video_export._write_manifest`.

   **Mục manifest.** Mọi file chỉ ghi tên, nằm cùng thư mục với manifest.
   - **Như `collect()` ở `lab_batch.py` dòng 317–379:** `file`, `json`, `cols`, `rows`, `frames`, `fps`, `loop`, `blend`, `cell`, `pivot`, `start: 0`, `heading: 0`, `tileX`, `width`, `height`, `md5`, `bytes`, `sourceFps`, `trim{start,end,step,startMode}`, `flags`, `notes`. Clip một lần thêm `timing`, đúng công thức ở dòng 371–378.
   - **Chép từ mục like (nếu có):** `role`, `roles`, `job`, `take`, `source`, `mode`, `alpha`, `code`, `design`, `name`, `elements`, `use`, `layer`, `modesAllowed`, `alphaKind`, `premultiplied`, `tint`, `dir`, `head`. Riêng `head.cellUv` tính lại theo crop mới: `[(uv.x·srcW − cropX)/cropW, (uv.y·srcH − cropY)/cropH]`, 4 chữ số.
   - **`sourceRect`:** `{"crop": source.crop, "frame": [source.width, source.height]}`, lấy từ `<id>.json` mới. Lab cần trường này để thẻ flipbook trùng khít thẻ video.
   - **`compareWith`:** `{"folder": <thư mục like>, "id": <id like>}`. Không ghi trường `video`; lab tìm video hiện tại qua trường này.
   - **`ktx2`:** `{"uastc": {file, bytes, md5, encodeS, level}, "etc1s": {file, bytes, md5, encodeS, quality}, "yFlip": true, "mipmaps": true, "transfer": "srgb"}`, chỉ có các codec đã xuất.
   - **`motion`:** `{"file": "<id>.mv.png", "bytes", "md5", "layout": "x-rgb-y-a", "zero": 128, "scale": 127, "strength", "units": "cell UV per frame step, x right, y up", "direction": "forward: frame n to n+1; one-shot last frame 0; loop last to first", "method": "opencv DIS medium on sqrt luma, masked", "checks": {"warpRatio", "warpRatioP90"}, "ktx2": {…như trên, "transfer": "linear"}}`.
   - **`videoVariants`** (khi có `--videos`): `{"crf23": {file, w, h, fps, frames, start: 0.0, peakTime, pivot, bytes, crf: 23, ssim}, "720p": {…, crf: 20}}`. `peakTime` và `pivot` chép từ `video` của mục like.
   - **`upgrade`:** `{"tool": "tools/vfx-flipbook upgrade", "cell": [w, h], "fps": n, "look", "date": "YYYY-MM-DD"}`.
5. **`__main__.py`:** thêm lệnh con `upgrade` (dùng argparse như `_export_video`), thêm vào `USAGE`, và bắt `Ktx2Error` cùng các lỗi đang bắt.

## Test (`tests/test_upgrade.py`, clip tổng hợp, không cần mạng)
- **`fixed_rate`:** với start 0, end 121, step 2, n_max 64 → 61 khung, chỉ số cuối 120, không capped. Với n_max 30 → 30 khung, capped, end 60.
- **Mã hoá vector:** 0 → 128; +strength → 255, −strength → 1; sai số sau khi giải ≤ strength/127.
- **Đốm sáng đi chéo** (ô 128×72, mỗi khung +3 px ngang, +2 px xuống):
  - trung vị vector trong đốm ≈ (3/128, −2/72) UV, sai lệch tối đa ±25 %;
  - `warpRatio < 0.5`;
  - `warp_blend(w=0.5)` gần khung giữa thật hơn trộn chồng: MAE nhỏ hơn ít nhất 30 %.
- **KTX2** (ảnh 64×32), với cả hai codec:
  - file bắt đầu bằng 12 byte `AB 4B 54 58 20 32 30 BB 0D 0A 1A 0A`;
  - `levels ≥ 2`;
  - `transfer` 2 khi sRGB, 1 khi linear;
  - `supercompression` 1 với ETC1S, 2 với UASTC.
- **Look:** với clip xanh, `neutral` giữ sắc độ ở đuôi mờ (B/R lệch dưới 5 %); `cool` thì đổi sắc độ.
- **`upgrade` từ đầu tới cuối:** clip tổng hợp 48 khung (fixture `lab`), manifest like và repo-root tạm, chạy với `--cell 128x72 --fps 12 --ktx2 uastc,etc1s --videos crf23`.
  - Ra đủ file, md5 đúng.
  - `mv.png` cùng lưới và cùng cỡ với atlas.
  - Các trường đúng như mục 4.
  - Một mục có sẵn khác trong manifest giữ nguyên.
- **Không bỏ test:** test cần KTX2 hay OpenCV chỉ dùng `skipif` khi thiếu gói. Báo cáo phải cho thấy các test này đã **chạy**, không bị bỏ qua.

## Chạy thật (sau khi test qua)
```
export VFXLAB_HOME=/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/vfxflip-325
tools/vfx-flipbook/run.sh upgrade --like games/immortality-cultivation/art-src/lab/vfx/expansion/manifest.json:azure-cloud-dragon \
  --out games/immortality-cultivation/art-src/lab/vfx/hybrid --cell 768x432 --fps 6 --frames 32 --ktx2 uastc,etc1s --videos crf23,720p
tools/vfx-flipbook/run.sh upgrade --like games/immortality-cultivation/art-src/lab/vfx/fire/manifest.json:fire-comet \
  --out games/immortality-cultivation/art-src/lab/vfx/hybrid --cell 768x432 --fps 24 --frames 32 --ktx2 uastc,etc1s
```
- **Dự kiến:**
  - rồng: 31 khung (nguồn 0–120, bước 4 của nguồn 24 khung/giây, khoảng 5,2 s ở 6 khung/giây, trộn bằng vector), lưới 4×8, atlas 3072×3456 (≤ 4096). Cùng nhịp 6 khung/giây với atlas cũ anh chê mờ, nhưng ô to hơn (768×432 thay 640×360), trộn bằng vector và nén KTX2: đây chính là phép thử;
  - sao chổi: vòng lặp 32 khung, lưới 4×8, atlas 3072×3456.
- **Kiểm hai bộ đọc cũ không vỡ:**
  1. `cd games/immortality-cultivation && node_modules/.bin/tsx /Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/lab-flipbooks/validate-manifests.ts`. Chạy một lần trước khi ghi gì vào `hybrid/` và ghi lại N trong dòng `N task entries, 0 problems` (06/11 lúc viết phiếu là 333; số này tăng khi phiên khác thêm mục). Sau phiếu phải có dòng `hybrid … 2 entries parse OK, 2 from this task` và `N+2 task entries, 0 problems`. Báo cáo ghi cả hai số.
  2. Bộ đọc của lab (`b8ebd51`):
     - viết file tạm `/private/tmp/codex-325-parse.mts`;
     - trong đó nhập `parseFlipbookManifest` bằng đường dẫn tuyệt đối từ `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-elements/src/view/skills/flipbook.ts`;
     - đọc `hybrid/manifest.json` với base `/art-src/lab/vfx/hybrid/` và in các id;
     - chạy bằng `games/.wt-ic-lab-elements/node_modules/.bin/tsx`.
- **Thư mục ảnh chụp:**
  - viết `ABOUT.md` cho `captures/tu-tien/vfxflip-325/`, gồm `purpose`, `made-by: codex 325`, `doc: docs/codex-queue/325-tt-vfxflip-mv-ktx2.md` và `delete-when`;
  - chạy `node scripts/review-index.mjs`;
  - chỉ giữ `sheet.jpg`, `preview.mp4`, `metrics.json`; không để khung thô.

## Kiểm
- `VFXLAB_HOME=/private/tmp/codex-325-vfxflip tools/vfx-flipbook/run.sh test -q -o cache_dir=/private/tmp/codex-325-vfxflip/pytest --basetemp=/private/tmp/codex-325-pytest` phải qua cả 54 test cũ (trước phiếu: `54 passed`) lẫn test mới.
- `git diff --check` sạch. Lệnh này chỉ đọc.

## Xong khi
Các lệnh kiểm đều qua, hai lần chạy thật xong, hai bộ đọc cũ không vỡ.

Báo cáo ghi:
- file đã sửa;
- lệnh cài và phiên bản đã cài;
- kết quả test: số test qua, không test nào bị bỏ;
- với từng clip: lưới, cỡ atlas, số khung, fps; dung lượng PNG, KTX2 UASTC và KTX2 ETC1S (cả màu lẫn vector); thời gian mã hoá; `strength`; `warpRatio`;
- với rồng: dung lượng và SSIM của `crf23` và `720p`;
- mọi cảnh báo của công cụ.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).

## Ghi chú từ phản biện (không chặn)
- `fixed_rate`: khi không cắt thì giữ nguyên `capped`, `faded` của plan.
- Mặc định `--ktx2 uastc,etc1s`; không có `--videos` thì không xuất video.
- Bộ mã hoá in log ra stdout dù đã tắt debug: luôn đọc dòng JSON cuối.
- Mã mới tra `grade.cool_fade` và `grade.cool_dim` lúc gọi (không gắn lúc import), vì `lab_batch.py` vá đè hai hàm này.
- Bộ lọc `flags` như `collect()`: lấy `folder` là thư mục của manifest like.

## Ghi chú từ phản biện vòng 2 (PASS)
- Thêm hai test cho luật mới: `--fps 6 --no-mv` phải báo lỗi; `--max-atlas 256` phải báo lỗi và không ghi file nào vào `<out>`.
- Lỗi `look`, `fps`, `--max-atlas` ném `media.MediaError` (để `__main__` in lỗi gọn), không ném `ValueError`.
- Thư mục ảnh chụp ghi tên file thật: `<job>__v1.sheet.jpg`, `<job>__v1.preview.mp4`, `<job>__v1.metrics.json`.
- Được ghi thêm `typing-game-review/INDEX.md` (do `node scripts/review-index.mjs` sinh ra).
- Mục like trong test đầu cuối phải có `video`, `trim` và `timing`, vì phần xuất video đọc ba trường này.
