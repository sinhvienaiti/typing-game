# Danh sách dựng 3D bằng Tripo

**Chủ dự án, 01/11/2026 khoảng 03:50:**
- Claude dùng Firefly làm ảnh 2D rồi Tripo dựng 3D, **ưu tiên API** (khoảng 1.000 credit).
- "Chắc chắn xác nhận đầy đủ r hãy tạo vì credit có giới hạn rất ít."
- Face: "đừng có chơi số face ở mức cao nhất, nó chỉ nên được nâng cao hơn để đẹp hơn so với trước" (các đợt trước chỉ 2–4k).

## Cấu hình (đã kiểm bằng `--dry-run`, không tốn credit)

```
tripo generate image-to-model <ảnh nguồn> -p texture_quality=detailed -p pbr=true -p face_limit=<theo bảng> -o <thư mục tạm> --name <tên>
```

- Model `v3.1-20260211`, texture HD, PBR. Không dùng smart low-poly, không quad.
- Geometry để `standard`. Mức `detailed` tốn thêm 20 credit; chỉ cân nhắc cho nhân vật chính nếu lần thử đầu cần.
- Giá theo tài liệu Tripo: **40 credit một model**.
- Ví API hiện có **970 credit** (`tripo balance`). Ví web là ví riêng, dùng sau khi hết ví API.

## Chốt trước khi bấm dựng (mỗi model)

1. Ảnh nguồn đã được hai giám khảo mù cùng cho từ 8,5, kể cả điểm "hợp làm nguồn Tripo":
   - một khối liền, chân phẳng, góc ba phần tư nhìn từ trên khoảng 30°;
   - không có nền đất, bóng hay viền màu khóa.
2. Chạy `--dry-run` lại và đối chiếu: model, texture, PBR, `face_limit` đúng bảng.
3. Dựng **một model trước**, kiểm số tam giác, các map và vòng quay trong Blender, rồi mới dựng tiếp.
4. Ghi credit trước và sau vào bảng dưới.

## Danh sách

| # | Game | Model | Ảnh nguồn | Trạng thái nguồn | face_limit | Credit | Kết quả |
|---|---|---|---|---|---|---|---|
| 1 | Dragonhold | Cổng ải `hold-gate` | `games/dragon-hold/art-src/landmarks/hold-gate.png` (phiếu 124) | **Trượt** (J 5,5 / K 6): vẽ lại | 50.000 | 40 | — |
| 2 | Dragonhold | Tường ải `hold-wall` | `landmarks/hold-wall.png` | **Trượt**: vẽ lại | 30.000 | 40 | — |
| 3 | Dragonhold | Tháp canh `watchtower` | `landmarks/watchtower.png` | **Trượt**: vẽ lại | 35.000 | 40 | — |
| 4 | Dragonhold | Tượng rồng `dragon-statue` | `landmarks/dragon-statue.png` | **Trượt**: vẽ lại | 50.000 | 40 | — |
| 5 | Dragonhold | Vòm đổ `ruined-arch` | `landmarks/ruined-arch.png` | **Trượt**: vẽ lại | 25.000 | 40 | — |
| 6 | Dragonhold | Chậu lửa `brazier` | `landmarks/brazier.png` | **Trượt**: vẽ lại | 12.000 | 40 | — |
| 7 | Last Line | Nữ xạ thủ (Lightbearer) | Firefly, 4 góc khớp `results-lose-bg.png` (`QUALITY_RESCUE` §4.4) | Chưa có, Claude làm | 50.000 | 40 (multiview) | — |
| 8 | Last Line | Drone hỗ trợ | Firefly, 4 góc | Chưa có | 25.000 | 40 | — |
| 9–13 | Last Line | 5 súng cầm tay: Pulse, Heat Beam, Scatter, Rail, Star Mortar | Firefly, ba phần tư | Chưa có | 15.000 mỗi súng | 5 × 40 | — |
| 14 | Tu Tiên | Kiếm tu nữ (nhân vật chính) | `art-src/heroine/r4-view-{front,back,left}.v1-try*.png` + phải lật gương (vòng 4, phiếu 350) | **Chưa đạt** (giám khảo mù 7,5 / 7,2, sức hút 7,9–8,2) | 50.000 | multiview v3.1, texture detailed, PBR (dry-run 12/11 10:2x: hợp lệ, 0 cảnh báo; ví API 850) | — |
| 14 | Tu Tiên | Kiếm Clear Wind `clear-wind` | `games/immortality-cultivation/art-src/weapons/clearwind-src3q.v4-try1-pad.png` | **Ngoại lệ của chủ dự án** (02/11 khuya, "Dựng thử bản 4"): nguồn chững ở 8,2–8,3 / 8–8,2 / 7,9–8,2 sau vòng 18–22 (`docs/games/tu-tien/art-requests/weapons/JUDGING.md`); model phải qua 8,5 trong lab | 15.000 | 40 | **Đã dựng** 02/11 23:12, task `0038a002-69f4-46e6-8ebc-3d1cd584a22c`, 40 credit (số dư 970 → 930). 14.728 tam giác, map màu, normal và ORM 4096. Gốc ở `games/immortality-cultivation/art-src/3d/weapons/clear-wind.glb`. Chờ đưa vào lab và chấm 8,5 |

Tổng dự kiến 13 × 40 = **520 credit**. Còn khoảng 450 credit cho làm lại, hoặc nâng geometry `detailed` cho nhân vật.

Model dựng xong lưu ở `art-src/3d/` của từng game. Claude dọn và rig trong Blender, chấm trong bản chơi ở mức 8,5. Runtime giữ đúng sàn của MODEL_QUALITY, không cắt thêm.

## Chấm nguồn 124 (01/11 khoảng 04:00, hai giám khảo mù J, K)

Không ảnh nào đạt 8,5 về mức thị trường, nên chưa tiêu credit. Kết quả ghi theo mức thị trường M (thang 10) và mức hợp làm nguồn Tripo.

| Ảnh | M (J / K) | Hợp Tripo (J) | Lỗi chính |
|---|---|---|---|
| hold-gate | 5,5 / 6 | 6 | Kiểu game mobile, tháp lùn, song lưới hở, vệt cam, góc gần chính diện |
| hold-wall | 5,5 / 6 | 8,5 | Tường vườn, đá bệt, không cũ |
| watchtower | 6 | 7,5 | Lùn như đồ chơi, chong chóng mảnh, góc chỉ 15–20° |
| dragon-statue | 7 | 8,5 | Đầu nhỏ, cánh phẳng, không có tỉ lệ khổng lồ |
| ruined-arch | 5 | 5,5 | Cây thông tí hon, dải sắt vô lý, mảnh như tấm phẳng |
| brazier | 7,5 | 8,5 | Vân sắt nhiễu, chậu rỗng, lệch kiểu vẽ |

Hướng vẽ lại: dùng Firefly Image 5 và ảnh mẫu `owner-epic`; kiểu painterly-realistic (O1); đá sa thạch ấm, phong hoá; góc ba phần tư 35°, nhìn từ trên 30°; nền phẳng màu khóa. Sửa từng ảnh theo góp ý của hai giám khảo.

## Vòng v2 và v2b (01/11, 04:00–07:45, Firefly Image 5, bốn giám khảo mù L, M, N, O)

Chưa ảnh nào được cả hai giám khảo cho từ 8,5, nên **chưa tốn credit**.

| Ảnh | v2: M (L / M) | v2b: M (N / O) | v2b: hợp Tripo (N / O) | Ghi chú |
|---|---|---|---|---|
| hold-gate | chưa có | 6,8 / 6,8 | 7,5 / 8,0 | Kiểu tranh vẽ tay, gạch nhỏ gấp 4–5 lần khối của tường |
| hold-wall | chưa có | 7,0 / 6,8 | 6,5 / 6,5 | Lỗ châu mai thành ký hiệu mũi tên, có bóng đổ |
| watchtower | chưa có | chưa có | — | Firefly vẽ tháp chạm mép trên ở khung vuông; vòng sau dùng khung dọc 3:4 |
| dragon-statue | 6,5 / 6,5 | **8,0 / 8,3** | **8,5 / 8,5** | Gần đạt nhất. Thân lai sư tử, cánh nhỏ, đầu rồng có râu lệch với cả bộ |
| ruined-arch | 6 / 6 | 6,7 / 6,3 | 7,0 / 6,0 | Kiểu đất nặn, vệt mưa trắng |
| brazier | 6,5 / 7 | 8,2 / 7,6 | 8,0 / 7,8 | Chất liệu tốt; tay rồng mảnh, có móng không thân |

Lỗi chung theo giám khảo: sáu ảnh không thành một bộ (năm kiểu dựng hình, năm màu đá, bốn kiểu đầu rồng, năm màu nền xanh).

**Vòng v3** (bắt đầu 07:55) dùng một chuẩn chung:
- chất liệu lấy theo tượng rồng v2b và chậu lửa v2b: sa thạch khối lớn kiểu ảnh quét 3D, sắt rèn đai đồng;
- một thiết kế đầu rồng có sừng vuốt ngược, không râu;
- cùng một hướng sáng, không bóng đổ, nền #00FF00, lề ≥ 6–8 %;
- tháp canh dùng khung 3:4.

Ảnh ở `games/dragon-hold/art-src/landmarks/<tên>.v3.png` (vòng làm lại: `.v3b.png`).

## Last Line, vòng v1 (bắt đầu 07:55)

- **Màu:** ngà sứ và graphite, đường sáng cyan mảnh, **không dùng vàng**. Vàng dành cho Pack Leader (theo ChatGPT duyệt map 1); áo choàng xanh đen, chỉ ngà rất mảnh.
- **Nhân vật và drone:** làm tờ xoay bốn góc trước, rồi cắt thành bốn ảnh cho multiview. Có thêm ô kiểm ở 68 px.
- Ảnh ở `games/typing-survival/art-src/models-src/hero-v2/`.

**Chủ dự án, 01/11 khoảng 9h:** "Chờ ảnh đạt 8,5". Không dựng thử model nào dưới mốc này, kể cả tượng rồng v2b.

## Hướng thứ hai: model miễn phí có sẵn (01/11, 11:30–12:30)

Đã tìm 82 ứng viên trên Sketchfab (CC0/CC-BY), Poly Haven, BlenderKit, OpenGameArt, Quaternius và Kenney. Sau khi đọc lại giấy phép trên trang từng mục, giữ 58 ứng viên (bảng chi tiết trong kết quả workflow `wf_6089c9ed-958`). Hai giám khảo mù chấm từng ứng viên; **không ứng viên nào đạt 8,5**.

| Công trình | Ứng viên tốt nhất | Điểm thị trường / độ hợp |
|---|---|---|
| Vòm đổ | A7: bản quét khải hoàn môn sa thạch | 7 / 7 |
| Tượng rồng | S10: bản sculpt rồng nằm cuộn, chưa có texture, có thể là fan-art | 6,5–7 / 7–7,5 |
| Cổng, tường, tháp canh | Bản quét các công trình có thật; Poly Haven Modular Fort 01 (CC0, cần dán lại texture) | khoảng 6–6,5 |
| Chậu lửa | B1, B7 | khoảng 6–6,5 |

Các ứng viên tốt nhất không thành một bộ: đá, thời kỳ và ánh sáng nướng sẵn khác nhau. Giám khảo ước nếu khử ánh sáng và dán lại texture cả bộ thì cũng chỉ được khoảng 7–7,5.

Bị loại vì giấy phép: BlenderKit "Royalty Free", ShareTextures "Custom CC0", RenderCrate (điều khoản cấm AI), các mục gắn NoAI, NC, ND, SA, GPL.

**Kết luận:** hướng này không qua được mốc. Hướng kế tiếp: thử nhờ ChatGPT (chế độ Chat) vẽ ảnh nguồn cho cả bộ theo một chuẩn chung, vì tranh ý tưởng nó vẽ có chất liệu tốt hơn Firefly.

## Tu Tiên, mẫu Tripo cho ult Kim (16/11/2026)

Chủ dự án đồng ý "Dùng Tripo từ ảnh thành phần". Một mẫu duy nhất, chưa làm loạt.

| Mẫu | Ảnh nguồn | Cấu hình | Credit (trước → sau) | Kết quả |
|---|---|---|---|---|
| `tt-metal-blade-v1` (task `9745f72b`) | `games/immortality-cultivation/art-src/concept/ult-metal/ult-metal-blade-src.v1.png` | v3.1, detailed, pbr, face_limit 6000 | 850 → 810 (40) | 5.377 tam giác, Color/ORM/Normal 4096; GLB ở `games/.wt-ic-lab-all/art-src/lab/vfx/metal-ult/models3d/tripo/ult-metal-blade.tripo.v1.glb` |

Nhận xét: ba kiếm và chuôi đọc đúng, nhưng thân kiếm hơi méo, chất liệu vàng mờ (không còn pha lê), dải sáng thành dây mảnh lủng củng. Chờ chủ dự án xem.

### Tu Tiên, hai mẫu từ ảnh sạch (16/11/2026)

Chủ dự án duyệt "chạy Tripo cả hai". v3.1, detailed, pbr, face_limit 6000.

| Mẫu | Ảnh nguồn | Credit (trước → sau) | Kết quả |
|---|---|---|---|
| `tt-metal-clean-v1` (task `3720afc3`) | `art-src/concept/ult-metal/tripo-src/ult-metal-clean.v1-try1.png` | 810 → 770 (40) | 5.824 tam giác; `games/.wt-ic-lab-all/art-src/lab/vfx/metal-ult/models3d/tripo/ult-metal-clean.tripo.v1.glb` |
| `tt-void-clean-v1` (task `f55e08c4`) | `art-src/concept/ult-void/tripo-src/ult-void-clean.v1-try1.png` | 770 → 730 (40) | 5.930 tam giác; `games/.wt-ic-lab-all/art-src/lab/vfx/void-ult/models3d/tripo/ult-void-clean.tripo.v1.glb` |
| tt-metal-sword-v1 (task 65935807) | art-src/concept/ult-metal/tripo-src/ult-metal-sword.v1-try1.png | v3.1, detailed, pbr, face_limit 6000 | 730 -> 690 (40) | 5.570 tam giac; GLB games/.wt-ic-lab-all/art-src/lab/vfx/metal-ult/models3d/tripo/ult-metal-sword.tripo.v1.glb |

### Tu Tiên, thân gốc nữ chính v5B và gương Nhật Luân Kính (18/11/2026)

Chủ dự án duyệt hai ảnh nguồn cho Tripo (18/11). multiview-to-model (front/left/back), v3.1, detailed, pbr, không rig.

| Mẫu | Ảnh nguồn | face_limit | Credit (trước → sau) | Kết quả |
|---|---|---|---|---|
| Task mồ côi `3fd23159` (thân gốc v4, agent trước bị dừng giữa chừng) | `art-src/heroine/models3d/src/base-body.v4.*.png` | 50.000 | 690 → 650 (40) | Không tải, không dùng |
| `tt-base-body-v5B` (task `ec7ed4aa`) | `art-src/heroine/fashion/base-body.v5B-turn.v2-try1.png` | 50.000 | 650 → 610 (40) | 47.784 tam giác, Color/NormalGL/ORM 4096; `games/immortality-cultivation/art-src/heroine/models3d/base-body.v5B.tripo-try1.glb` |
| `tt-light-relic-mirror-v1` (task `b747cbd4`) | `art-src/lab/vfx/light/stills/light-relic-mirror-a.v2-try2.png` | 12.000 | 610 → 570 (40) | 11.676 tam giác, Color/NormalGL/ORM 4096; `games/.wt-ic-lab-all/art-src/lab/vfx/light/models3d/tripo/light-relic-mirror.tripo.v1.glb` |

Ảnh xoay: `typing-game-review/owner-review/2026-11-18/tu-tien/tripo-v5b-mirror/`. Chờ chủ dự án xem.

### Tu Tiên, nữ chính v6B: thân và đầu tách riêng (18/11/2026)

Chủ dự án chọn nguồn 2D v6B (`art-src/heroine/fashion/base-body.v6B-turn.v1-try2.png`); chỉ dùng công cụ miễn phí và credit Tripo sẵn có. Dry-run cả hai: hợp lệ, 0 cảnh báo.

| Việc | Nguồn | face_limit | Credit | Kết quả |
|---|---|---|---|---|
| `tt-base-body-v6B` (task `bc5311fa`) | `models3d/v6b/src/{front,left,back}.png` (cắt từ tờ v6B, mặt nghiêng lật gương cho ô trái) | 50.000 | 570 → 530 (40) | 49.074 tam giác, Color/NormalGL/ORM 4096 |
| `tt-head-v6B` (task `9075e48d`) | `models3d/v6b/src/head-{front,left}.png` (phóng to Lanczos từ ảnh mặt v6B) | 30.000 | 530 → 490 (40) | 29.295 tam giác, Color/NormalGL/ORM 4096 |

Ghép trong Blender (đầu thay đầu thân, cổ cắm vào cổ áo): `models3d/v6b/heroine-v6b.assembled.glb`, `heroine-v6b.assembled-proj.blend`. Ảnh: `typing-game-review/owner-review/2026-11-18/tu-tien/heroine-v6b-3d/`. Chờ chủ dự án xem.

### Tu Tiên, nữ chính v8: đầu từ ảnh mặt Firefly (18/11/2026)

Nguồn: ảnh mặt Firefly chủ dự án chọn (`art-src/heroine/face/head-front.v1-try2.png`, `head-side.v1-try1.png` lật gương làm ô trái), chép vào `models3d/v8/src/`. Dry-run hợp lệ, 0 cảnh báo. Thiết lập: multiview front+left, `v3.1-20260211`, `texture_version=v3.5-20260815`, `delight=true`, `texture_quality=detailed`, `pbr=true`, geometry standard, `face_limit=40000`.

| Việc | Nguồn | face_limit | Credit | Kết quả |
|---|---|---|---|---|
| `tt-head-v8` (task `a97ea184`) | `models3d/v8/src/head-{front,left}.png` | 40.000 | 490 → 450 (40) | `models3d/v8/out/tripo-out/tt-head-v8-a97ea184/model.glb`; ghép thân v6B (cùng thông số ghép v6B): `models3d/v8/heroine-v8.assembled.glb` |

Ảnh: `typing-game-review/owner-review/2026-11-18/tu-tien/heroine-head-firefly-tripo/`. Chờ chủ dự án xem.

### Tu Tiên, nữ chính v8: thử Smart Mesh trên đầu (18/11/2026)

Chủ dự án duyệt một lần thử (35 credit). Dry-run (`tripo make a97ea184… --then decimate --dry-run`) hợp lệ, 0 lỗi. Lệnh: `tripo mesh decimate a97ea184… --model v3.0 --face-limit 20000 --smart-uv` (bake mặc định bật).

| Việc | Nguồn | face_limit | Credit | Kết quả |
|---|---|---|---|---|
| `tt-head-v8-smartmesh` (task `352ede3a`) | task `a97ea184` (đầu v8, 39.386 tam giác) | 20.000 | 450 → 415 (35) | 19.288 tam giác; `models3d/v8/smartmesh/tripo-out/tt-head-v8-smartmesh-352ede3a/model.glb` |

Kết quả: lưới đều và sạch hơn, nhưng texture nướng lại làm mặt mất chi tiết (da loang vệt, đường nối, môi méo và mất bóng, một lọn tóc dính màu da). Không dùng cho đầu. Ảnh: `typing-game-review/owner-review/2026-11-18/tu-tien/heroine-v8-smartmesh/`.
