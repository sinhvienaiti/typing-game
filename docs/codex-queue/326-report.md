# Phiếu 326 · Lab flipbook lai và cảnh A/B

**Trạng thái:** đã triển khai mã và test; **chưa hoàn tất demo/đo GPU**, do sandbox chặn cổng mạng và thư mục review ngoài repo. Media 325 đã đủ: 14 file lai và hai video đối chiếu đều có; không phải chờ 325.

Worktree `games/.wt-ic-lab-hybrid`, nhánh `codex/lab-hybrid-flipbook`, HEAD giữ nguyên `1b9461e`. Mặc định vẫn dùng video; lab không tham số không tải `hybrid/` hay khởi động transcoder.

## Đã làm

Trong worktree, 8 file mã/test/kịch bản, **+900 / −62 dòng**, chưa tính báo cáo:

- Sửa `src/view/skills/flipbook.ts`: manifest mở rộng nhưng giữ 12 khóa cũ; KTX2 và PNG dự phòng; vector qua ImageBitmap; shader vector, cắt nửa màn hình, giải phóng texture.
- Sửa `src/lab/comet-head.ts`, `meteor-rain.ts`: ba chế độ, pha riêng từng quả, giữ video của hệ khi nâng cấp atlas, bù crop, chờ frame video ngay sau lần tua, giữ video trước lần vẽ đầu và trong A/B.
- Sửa `src/lab/skills-main.ts`: import cả JS/WASM transcoder, tham số URL, host A/B, probe và phép tính bộ nhớ texture nén.
- Thêm `src/lab/hybrid-ab.ts`: cảnh meteor/rồng, đồng hồ chung, hai nhãn/vạch chia, only, prewarm, tua cố định, khởi động lại pool một ô, trạng thái tải/GPU/GL.
- Thêm `tests/lab/hybrid-flipbook.test.ts`: **30 test**, gồm manifest thật 325, loader giả, shader v1/v2, pha, số byte GPU và vòng đời A/B.
- Thêm `scripts/visual/scenarios/lab-hybrid-ab.mjs`: capture 240 JPEG → MP4/tấm ghép, perf ba cách, hitch ba lượt, kiểm hai tài nguyên transcoder, ghi JSON và dọn JPEG sau khi có MP4.

`tests/view/flipbook-v2.test.ts` chỉ đổi hai giá trị được phép:

- `FRAGMENT_SHA`: `3b5524bd2c052ed97c6261586915f9b218deb5756d0477d634e3605d05b93abd` → `abdd83d38bc128cbb046107dc251697115be06a42b515b943e8a11d60f5c6df7`.
- Độ dài FRAGMENT: **7272 → 7902**, in bằng `unwrapTagMask(new FlipbookPool(...).mesh.material.fragmentShader)`. Giữ nguyên `VERTEX_SHA` và **1823**.

## Kiểm

- `npx tsc --noEmit`: sạch.
- `npx vitest run tests/lab tests/view --maxWorkers=4`: **45 file / 530 test PASS** (lab 15 file / 109 test; view 30 file / 421 test).
- `node --check scripts/visual/scenarios/lab-hybrid-ab.mjs`: qua; `git diff --check`: sạch.
- Cảnh báo duy nhất từ bộ test có sẵn, lặp trong ba test: `[element-fire] fire-impact-k1-r2 not loaded (art-src/lab/vfx/fire/impact-k1-r2/manifest.json): key 1 hits fall back to the lotus`. Các lỗi KTX2 trong test dự phòng được giả lập và kiểm bằng spy.

## Phần chưa đo

| Cảnh | Nguồn/format nén thực tế; MB GPU | Thời gian khung chia đôi/trái/phải | Hitch không/có prewarm; video lần đầu | glError; transcoder 2×200; MP4 |
| --- | --- | --- | --- | --- |
| meteor | Chưa chạy GPU | Chưa đo | Chưa đo | Chưa kiểm; chưa có MP4 |
| azure-cloud-dragon | Chưa chạy GPU | Chưa đo | Chưa đo | Chưa kiểm; chưa có MP4 |

Dung lượng **file đầu vào trên đĩa**, không phải số tải/GPU đo trong trình duyệt: meteor video **4,662622 MB**, UASTC màu + vector **7,490316 MB**; rồng video **8,941828 MB**, UASTC màu + vector **12,217131 MB**.

Lệnh Vite đúng phiếu thất bại ngay: `Error: listen EPERM: operation not permitted 127.0.0.1:3126`. Đây không phải cổng bận, nên không thử 3127. Tạo `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/hybrid-ab/` cũng bị `Operation not permitted`. Không có server còn chạy từ lệnh đã thất bại; chưa mở trình duyệt. Không tạo capture, ABOUT, JSON hoặc INDEX; chưa chạy `PART=all` vì thiếu server và không ghi được đầu ra. Chưa có console trình duyệt để kết luận KTX2 thành công hay dùng PNG.

Claude cần chạy mục 7 ngoài sandbox này, kiểm transcoder 200 và hai cảnh thực tế; sau đó gửi anh hai MP4 `meteor-ab.mp4`, `azure-cloud-dragon-ab.mp4` cùng tấm ghép trong thư mục review quy định. Không thay đường dẫn/cấu hình transcoder, không tạo media thay 325, không sửa file ngoài phạm vi, không chạy build hay test suite khác, không chạy lệnh Git ghi. Phiếu còn mở ở bước demo và đo, chưa có kết luận chọn video hay cách lai.
