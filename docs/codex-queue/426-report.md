# Phiếu 426 — Vành kiếm Kim 3D Tripo

Hoàn tất phần mã và kiểm tra không cần trình duyệt ngày **17/11/2026**. **Chờ Claude kiểm hình và GPU**, chưa nghiệm thu tổng hợp 8,5 hoặc kết luận p95 ≤ 16,7 ms.

## Đã làm

Chỉ sửa năm tệp trong `games/.wt-ic-lab-all/src/lab/`:

| Tệp | Thay đổi |
| --- | --- |
| `metal-ult-3d.ts` | Thay bộ nạp sáu mẫu Blender cũ bằng GLB Tripo được chỉ định; một `InstancedMesh`, tối đa 432 kiếm, cụm 1–3, seed cố định, nghiêng 5–25°, cỡ 0,7–1,3. Dùng `MeshStandardMaterial` PBR thật, texture màu/ORM/normal gốc, thép bạc và chuôi vàng; RGB vành ≤ 0,9. Mọc theo sóng, giữ rồi xói/tách nhẹ; quản lý nạp, clear và dispose. |
| `metal-ult-sprites.ts` | Giữ một dòng lập vành 3D hiện có, truyền upload và vị trí người tung cho lớp 3D; thẻ bên trong còn 60 cụm + một điểm nhấn tâm; tổng 5 kho vẽ. |
| `metal-ult-layered.ts` | Thêm số kiếm/tam giác/lỗi nạp vào chẩn đoán `__lab.metalUlt().last`; xoá số đếm khi phép kết thúc. |
| `metal-ult-check.mjs` | Kiểm kiểu, phân tích GLB thật, PBR hook, số instance/mesh, seed, footprint, lịch 100 mục tiêu và vòng đời tài nguyên. |
| `metal-ult-review.mjs` | Kịch bản Claude chụp đủ pha ở góc trên/sau lưng, đo p95 toàn khung lúc trói, tam giác cảnh, tài nguyên GPU qua năm lần tung. |

Ngoài worktree chỉ thêm mục thành phần 426 vào **`docs/games/tu-tien/skills/VFX_LIBRARY.md`** và viết báo cáo này. Không đổi nhánh, commit, đưa media vào Git hoặc chạy build/bộ test game.

Nguồn dùng nguyên vẹn qua symlink `art-src` có sẵn:
`art-src/lab/vfx/metal-ult/models3d/tripo/ult-metal-sword.tripo.v1.glb` — 10.857.200 byte, 3.880 vertex, 5.570 tam giác; ba texture 4096². Không tạo/sửa tệp media hoặc dựng Blender. Kiếm và đá là một mesh liền nên giữ đá; việc ẩn đá phụ là tùy chọn trong phiếu.

## Kết quả đã chạy

Chạy từ `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all`:

```sh
node node_modules/typescript/bin/tsc --noEmit
ART_MAGICK=/opt/homebrew/bin/magick node src/lab/metal-ult-check.mjs
node --check src/lab/metal-ult-check.mjs
node --check src/lab/metal-ult-review.mjs
```

- **Strict toàn worktree: 0 lỗi.** Hai script kiểm cú pháp đạt. `pnpm exec tsc --noEmit` không chạy được do pnpm cố mở cơ sở dữ liệu store ngoài sandbox; dùng trực tiếp TypeScript đã cài như lệnh trên và đạt, không cài thêm gói.
- **Probe PASS:** 100 mục tiêu trói/tint trong 3 s; một mục tiêu chết sớm được gỡ, 99 mục tiêu còn lại nhận đúng một cú. Giữ lịch âm thanh và trần 128 trói cũ.
- **144 vị trí vành → 292 kiếm**: 41 cụm một, 58 cụm hai, 45 cụm ba. Seed, ma trận và số lượng lặp lại chính xác. Sức chứa 432.
- Một `InstancedMesh` mới, bốn kho thẻ còn lại; không gắn scene GLTF hoặc mesh dư. Các kho thẻ nộp lần lượt 61 / 194 / 1.408 / 1.444 slot khi có 100 mục tiêu.
- **1.626.440 tam giác kiếm**, **1.632.654 tam giác hiệu ứng được nộp** gồm các thẻ; không phải số tam giác toàn cảnh hoặc tất cả hình cùng sáng.
- Đỉnh kiếm gần vị trí người tung nhất trong kiểm độc lập qua mọc/vượt đỉnh/giữ/tan: **2,398812 m**, lớn hơn vùng cấm 2 m. Có kiểm điểm đặt sát người; vị trí ngoài vùng cấm được đẩy nhẹ khi cần đủ footprint. Shader giữ thêm vùng cấm theo vị trí hiện tại và mặt nạ màn hình khi người tung di chuyển.
- **Xoá/tung lại 5 lần:** giữ nguyên mesh, material, geometry, mảng ma trận và thuộc tính instance; count về 0 sau clear; không nạp GLB lần nữa. Clear/thay phép/dispose trước khi nạp xong không hồi sinh phép cũ; texture và tài nguyên được giải phóng khi dispose.
- GLTFLoader phân tích hình học GLB thật, ImageMagick đọc đúng ba ảnh nhúng; probe thay phần giải mã ảnh của trình duyệt bằng Texture rỗng. Kiểm hook shader trên `ShaderLib.standard` r170 đạt, **chưa biên dịch GLSL hoặc upload GPU**.
- p95 cập nhật riêng recipe CPU ở lượt cuối khoảng **0,027 ms**, lập phép khoảng **4,37 ms**; không dùng các số này để kết luận p95 toàn khung/GPU.

## Lệnh cho Claude: hình ảnh và hiệu năng

Phiếu giao phần trình duyệt cho Claude vì sandbox chặn. Không mở dev server hoặc trình duyệt trong phiên này, không sinh capture hoặc video. Claude dùng host đang phục vụ worktree này; nếu cổng khác thì đổi `BASE`:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
BASE=http://127.0.0.1:3146/stress.html \
OUT=/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/ult-metal-3d \
ART_MAGICK=/opt/homebrew/bin/magick \
node src/kit/tools/cdp-run.mjs src/lab/metal-ult-review.mjs \
  --width=1920 --height=1080 --dpr=1
```

Kịch bản chờ cả atlas và GLB, chạy làm ấm toàn bộ pha, rồi chụp `426-{top,behind}-*.png` tại tụ 0,3 s, tung 0,6 s, sóng 1,2/1,9 s, đang trói, sát hết trói, vỡ và dư âm. Ba bảng JPG mỗi góc so với ảnh repo `ult-metal-moment-b.v1-try1.png`; `426-measure.json` ghi p95 CPU và p95 toàn khung có readPixels, renderer/tam giác/số kiếm, dân số cảnh và bộ nhớ GPU qua 5 lần tung. Chỉ lấy mẫu đang giữ sau 1,9 s và trước cú vỡ đầu tiên; cờ `passes16_7ms` kiểm p95 ≤ 16,7 ms. Đây là chi phí khung render đồng bộ, không phải khoảng cách giữa các rAF.

**Dân số host hiện tại:** 87 mục tiêu `TargetField` có thể trói + 13 walker = 100 quái trong cảnh; script kiểm đủ tổng 100 và ghi số trói thực. Không coi đây là 100 quái cùng trói. Nếu cần đo 100 mục tiêu cùng trói thì Claude chuẩn bị host ngoài phạm vi phiếu, rồi điều chỉnh bước kiểm dân số tương ứng; probe CPU đã kiểm đúng 100.

**Owner cần xem:** độ rõ kiếm từ sau lưng lúc va chạm/trói, màu bạc/vàng và normal gốc, đá đế khi cụm ba chồng nhau, độ cao của vành gần người tung, viền sáng nhẹ và vùng người tung luôn sạch. Giữ điểm nhấn tâm là HDR duy nhất. Cần kiểm GLSL/404/console, p95 ở cả hai góc và bộ nhớ GPU ổn định trước khi chấm mù hai người ≥ 8,5.

Kịch bản tạo `ABOUT.md` và chạy lại chỉ mục review. Sau khi xem, Claude giữ bảng, số đo và các khung được dùng trong báo cáo; xem trước rồi dọn đúng khung do lần chạy này tạo bằng công cụ chuẩn:

```sh
node tools/capture-prune/prune.mjs /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/ult-metal-3d
# Sau khi đối chiếu danh sách chỉ gồm khung của lượt này:
node tools/capture-prune/prune.mjs /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/ult-metal-3d --apply
node scripts/review-index.mjs
```
