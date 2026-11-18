# Phiếu 427 — vành tinh thể Hư Không 3D

Ngày 16/11/2026. Đã triển khai và kiểm mã trong `games/.wt-ic-lab-all`; **chờ Claude đo GPU và kiểm hình**. Áp dụng miễn hạn mức của owner ghi trong phiếu. Không chạy Blender, tạo media, build, bộ test game, commit hoặc đổi nhánh.

## Đã làm

Các đường dẫn mã dưới đây tính từ `games/.wt-ic-lab-all/`:

| Tệp | Thay đổi |
| --- | --- |
| `src/lab/void-ult-3d.ts` | Mới: GLTFLoader nạp GLB Tripo có sẵn; một InstancedMesh, tối đa 192 cụm; giữ texture màu gốc, kính tím giả lập và Fresnel tím trắng, RGB ≤ 0,9. Matrices/clock ghi một lần mỗi lần tung; mỗi khung chỉ đổi uniform thời gian. Có dọn tài nguyên và xử lý clear/dispose trong lúc nạp. |
| `src/lab/void-ult-sprites.ts` | Nối prepare/plan/update/clear; bỏ 384 thẻ rift và 84 thẻ kính ở vành. Giữ 60 cụm bên trong và các lớp phụ; forest được thu gọn từ 589 xuống 121 thẻ. Chỉ ready khi cả atlas và GLB đã nạp. |
| `src/lab/void-ult-layered.ts` | Thêm số instance/tam giác tinh thể vào báo cáo lab để kịch bản đo đọc được. |
| `src/lab/void-ult-check.mjs` | Mở rộng probe Hư Không: phân tích GLB thật, kiểm instance/mesh/clearance, xoá/tung lại, dọn tài nguyên và nạp muộn. |
| `src/lab/void-ult-review.mjs` | Chuẩn bị kịch bản Claude chụp hai góc và đo toàn khung trong lúc trói; xuất số tam giác cảnh, kiểm p95 ≤ 16,7 ms và bộ nhớ GPU qua 5 lần tung lại. |

Đã ghi thành phần vào `docs/games/tu-tien/skills/VFX_LIBRARY.md`. Không sửa media trong `art-src/`.

Nguồn: `art-src/lab/vfx/void-ult/models3d/tripo/ult-void-clean.tripo.v1.glb`, **9.088.664 byte**, SHA-256 `7e7f41b075097c8edf236fa32b9b0d2eabcd13b9557d8c2a2440196ab5e80375`.

Giữ tâm/vòng theo quái của mã hiện tại: bán kính danh nghĩa **7–12 m** (nằm trong dải 7–14 m của phiếu), ba vòng lệch nhau. Sinh theo sóng `0,6 + d/26`, mọc **0,28 s**, giữ tới tuổi **3,2 s**, tan/xói trong **2,5 s**; vẫn dùng mảnh và glint ảnh cũ. Không đổi sự kiện trói/sát thương/âm thanh. Bỏ cụm nếu chân mô hình lấn vùng 2 m quanh vị trí tung; cả mô hình và các thẻ còn lại cùng dùng mặt nạ màn hình bảo vệ người tung. Khi người chơi di chuyển, shader cũng khoét vùng 2 m theo vị trí hiện tại.

## Kiểm đã chạy

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
export ART_MAGICK=/opt/homebrew/bin/magick
node node_modules/typescript/bin/tsc --noEmit
node src/lab/void-ult-check.mjs
node --check src/lab/void-ult-review.mjs
```

| Hạng mục | Kết quả |
| --- | --- |
| Strict TypeScript toàn worktree | **0 lỗi**; không chạy build hoặc bộ test |
| GLTFLoader đọc GLB thật | **Đạt**: một mesh, 3.901 đỉnh, 17.790 index = **5.930 tam giác/instance** |
| Ảnh nhúng | ImageMagick nhận đúng Color JPEG, ORM JPEG, Normal PNG; cả ba **4096×4096**. Runtime giữ map màu, giải phóng vật liệu/geometry nguồn và texture không dùng. |
| Probe 100 mục tiêu | **100 trói, 100 nhuộm màu**, đủ 3 s; 99 đòn kết + 1 mục tiêu chết được huỷ theo bài kiểm cũ |
| Hình học khi trói trong probe | **192 instance**, một InstancedMesh; **1.138.560 tam giác tinh thể** |
| Tổng hình học hiệu ứng gửi ở đỉnh probe | **1.145.374 tam giác**, gồm tinh thể và các thẻ còn lại; **không phải tổng cảnh stress** |
| Mesh thừa | **Không có**: 4 batch thẻ + 1 batch GLB; không gắn scene GLTF nguồn, không thêm vỏ kép |
| Xoá/tung lại 5 lần | **Đạt ở CPU**: cùng object/material/geometry/mảng bộ đệm, GLB chỉ nạp một lần, clear về 0 instance, không dispose trong lúc tái dùng |
| Nạp muộn/dọn | **Đạt**: clear trước nạp không làm cụm hiện lại; dispose giải phóng mesh/geometry/material/map; dispose trong lúc nạp không gắn mesh muộn |
| Vùng trống | **Đạt toán học**: cả bán kính chân mô hình ngoài 2 m; kiểm trường hợp tâm ở 0 m, 2,1 m và 4 m; mặt nạ người tung kiểm 8 bố trí camera |
| Shader, ảnh lên GPU, hình nhìn thấy, p95 toàn khung | **Chưa đo** trong sandbox; không tuyên bố đạt 16,7 ms hoặc 8,5 |

Probe chỉ mô phỏng đối tượng texture khi GLTFLoader nạp ảnh; hình học/buffer GLB và metadata ảnh được đọc từ tệp thật. Không coi kết quả này là bằng chứng nạp HTTP, giải mã/upload ảnh trong trình duyệt hay biên dịch GLSL. Lệnh `pnpm exec tsc --noEmit` ban đầu bị pnpm tự gọi bước kiểm/cài phụ thuộc rồi lỗi SQLite ngoài sandbox; đã dùng trực tiếp compiler có sẵn như trên, đạt 0 lỗi.

## Lệnh cho Claude: chụp và đo GPU

Dùng host đang phục vụ **đúng worktree này**. Nếu chưa có host 3146, ở terminal riêng chạy `node node_modules/vite/bin/vite.js --host 127.0.0.1 --port 3146 --strictPort` từ worktree; tắt tiến trình do mình mở sau khi xong.

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
export ART_MAGICK=/opt/homebrew/bin/magick
BASE=http://127.0.0.1:3146/stress.html \
OUT=/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/ult-void-3d-427 \
../../.local/bin/heavy.sh --perf node src/kit/tools/cdp-run.mjs \
  src/lab/void-ult-review.mjs --width=1920 --height=1080 --dpr=1
```

Kịch bản tạo `ABOUT.md`, ảnh từng mốc và `427-top/behind-{phases,reference,impact-window}.jpg`, cùng `427-measure.json`. Có các mốc sóng/trúng **1,20/1,90 s**, lúc trói **max(2,2; firstBindAt+1,5) s**, trước kết thúc trói và lúc tan. JSON ghi `peakTotalSubmittedTriangles`, `peakCrystalTriangles`, `frameP95WithReadbackMs`, `holdSamples`, `passes16_7ms`, `recastMemory`, `stableGpuResources`; thoát lỗi nếu cổng khung/bộ nhớ/log lỗi không đạt.

Đây là phép đo khung CPU + GPU chờ `readPixels`, không phải FPS rAF. Host hiện có **87 mục tiêu TargetField + 13 walker = 100 quái trong cảnh**, không phải 100 quái cùng trói. Kịch bản kiểm đủ 100 quái lúc bắt đầu và ghi số thực sự trói; bài kiểm CPU mới có 100 mục tiêu cùng trói. Không sửa `stress.ts` hoặc herd ngoài phạm vi phiếu.

Sau khi xem ảnh, Claude cần xác nhận kính tím vẫn đọc được từ sau lưng, vùng trống quanh người tung, xoáy tâm là điểm HDR duy nhất và nhịp tan; chưa có chấm mù tổng hợp 8,5. Khi gửi owner, đặt bản cứng các tờ cần xem vào `typing-game-review/owner-review/<ngày>/tu-tien/ult-void-3d-427/` cùng `ABOUT.md`, rồi chạy `node scripts/review-index.mjs` từ repo gốc. Kịch bản đã cập nhật index cho capture. Chỉ dọn raw mình tạo sau khi giữ tờ tổng hợp cần dùng:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game
node tools/capture-prune/prune.mjs /Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/ult-void-3d-427
# Sau khi xem danh sách:
node tools/capture-prune/prune.mjs /Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/ult-void-3d-427 --apply
node scripts/review-index.mjs
```

## Bỏ qua theo phạm vi

Không chạy Blender hoặc sinh asset vì dùng GLB Tripo owner chỉ định. Không chạy trình duyệt/server, chụp hay đo GPU trong sandbox theo đường giao việc; đã để kịch bản/lệnh tái lập cho Claude. Không chạy build/bộ test game; không sửa game chính, file Mộc, stress/herd, âm thanh hoặc Git.
