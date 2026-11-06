# Critic 325 (06/11/2026): FAIL

Hầu hết đều đúng; chỉ ba lỗi dưới đây chặn một người làm theo đúng từng chữ.

**Đã kiểm trên máy:**
- **Số dòng được trích đều đúng:** `pipeline.py` 323/367/387/476/484/523, `lab_batch.py` 270–277 và 317–379 (timing 371–378), `atlas.grid` ở dòng 13. `_export_one`, `_probe_video`, `_write_manifest` và `calculate_cut` có thật.
- **Công cụ có sẵn:** ffmpeg (có `ssim`, libx264), uv 0.13.5, node 24.22, npm 11.19, Python 3.12.15 đúng đường dẫn. Máy chưa có cv2, basisu và toktx.
- **Phiên bản ghim có thật:** các bản ghim có trên PyPI và npm (OpenCV abi3 arm64, 46 MB, 29/07). `ktx2-encoder` 0.6.0 ghim `ktx-parse ^1.1.0`.
- **Tuỳ chọn KTX2:** tôi chạy đúng các tuỳ chọn của phiếu bằng bản cài ở `.wt-dh-models`, ảnh 64×32. Kết quả có magic AB 4B…, 7 mức mipmap, transfer 2 (sRGB) và 1 (linear), supercompression 1 với ETC1S và 2 với UASTC: khớp phần test. WASM là bản cũ nên không có trần 12 Mpx, và atlas 3072×3456 lọt.
- **Test cũ:** 54 test đều qua.
- **Bộ đọc thứ hai:** đọc được qua tsx của `.wt-ic-lab-elements`.
- **Khớp với 326:** tên file, `ktx2.yFlip`, `motion` (layout, zero, scale, strength) và `videoVariants` đều qua `videoOf`. `compareWith`, `sourceRect` và `head.cellUv` (cho `cometOf`) cũng khớp. Chiều Y nhất quán: KTX2 lật trước khi nén, `mv.png` đọc với flipY, v = −dy/ch.
- **Mô phỏng hai lần chạy thật:**
  - rồng: rise 0–121, không capped;
  - sao chổi: vòng lặp 32 khung, crossfade 8;
  - cả hai: lưới 4×8, atlas 3072×3456.

**Cần sửa:**
1. **Số khung của rồng sai.** `range(0, 121, 4)` cho 31 khung (0…120), không phải 30. Atlas cũ cũng có 31 khung. Thay dòng "rồng: 30 khung (5 s ở 6 khung/giây, bước 4 của nguồn 24 khung/giây, trộn bằng vector), lưới 4×8, atlas 3072×3456 (≤ 4096)." bằng:
   "rồng: 31 khung (nguồn 0–120, bước 4 của nguồn 24 khung/giây, khoảng 5,2 s ở 6 khung/giây, trộn bằng vector), lưới 4×8, atlas 3072×3456 (≤ 4096)."
2. **Mốc của bộ kiểm manifest đã cũ.** Hôm nay nó in `333 task entries, 0 problems`, nên mốc 329/331 không đạt được. Thay "Trước phiếu in `329 task entries, 0 problems`. Sau phiếu phải có dòng `hybrid … 2 entries parse OK` và `331 task entries, 0 problems`." bằng:
   "Chạy một lần trước khi ghi gì vào `hybrid/` và ghi lại N trong dòng `N task entries, 0 problems` (06/11 lúc viết phiếu là 333; số này tăng khi phiên khác thêm mục). Sau phiếu phải có dòng `hybrid … 2 entries parse OK, 2 from this task` và `N+2 task entries, 0 problems`. Báo cáo ghi cả hai số."
3. **Đường dẫn tương đối tới `encode.mjs` hỏng khi chạy test.** `run.sh test` đổi thư mục vào `tools/vfx-flipbook` (`launch.py`), nên `node tools/vfx-flipbook/ktx2/encode.mjs` không chạy được trong test. Ở mục 3, phía Python, thay "Gọi `node tools/vfx-flipbook/ktx2/encode.mjs --raw …`" bằng:
   "Gọi `node <encode.mjs> --raw …`, với `<encode.mjs>` là đường dẫn tuyệt đối `pipeline.TOOL_DIR / "ktx2" / "encode.mjs"` (không phụ thuộc thư mục hiện hành). `skipif` của test KTX2 kiểm `shutil.which("node")` và `TOOL_DIR / "ktx2/node_modules/ktx2-encoder"`."

**Ghi chú (không chặn):**
- **`fixed_rate`:** nên viết rõ "khi không cắt thì giữ nguyên `capped`, `faded` của plan".
- **Mặc định còn thiếu:** nên ghi "mặc định `--ktx2 uastc,etc1s`; không có `--videos` thì không xuất video".
- **Stdout của WASM:** bộ mã hoá vẫn in "Total slices…" ra stdout dù `enableDebug: false` (đã kiểm), nên việc đọc "dòng JSON cuối" là bắt buộc. Phiếu đã làm đúng.
- **Không gắn hàm lúc import:** mã mới phải tra `grade.cool_fade` và `grade.cool_dim` lúc gọi, vì `lab_batch.py` vá đè hai hàm này.
- **Bộ lọc `flags` như `collect()`:** lấy `folder` là thư mục like.
- **Gói phụ chưa ghim:** iniconfig, pluggy và packaging (kéo theo pytest). Chấp nhận được.
