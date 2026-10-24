# Rồng Giữ Ải — Bộ prompt ảnh M0: mục lục, thứ tự làm, thiết lập Tripo (23/10/2026)

> **Dành cho:** chủ dự án (dựng model bằng Tripo từ ảnh 2D); AI điều khiển Codex CLI tạo ảnh 2D trên máy (đăng nhập ChatGPT, không dùng API key); AI ghép file sau (Blender, manifest, engine).
> **Lấy từ:** `../../DESIGN.md` §7 (ai làm gì: chủ dự án làm 3D bằng Tripo, Codex làm ảnh 2D, AI không dựng model), §7.2 (danh sách lát M0), §9 M0; `../../02-enemies-generals-bosses.md` (Bầy Héo, E01, E09, E11, E18, E19, E25, G01, §7.2 rig và clip); `../../03-our-side-shop-traps-support.md` (bẫy, nhà, lính); `../../05-presentation-audio-tech-split.md` §2 (phong cách, màu, tỉ lệ); `../../research/art-pipeline.md` (luật ảnh gửi Tripo, ô đất, prop).
> **Mẫu cách viết:** bộ prompt TD của Space Typing (`games/space-typing/docs/art-requests/td/`). Khác TD: ảnh gửi Tripo dùng **nền xám nhạt phẳng** thay cho nền khóa màu; mỗi khối prompt đã ghép sẵn đủ dòng, dán nguyên văn.

```text
Instructions for the image tool (Codex image_gen or ChatGPT)
- This README is only an index. Never make an image from this page alone.
- Open the file named in section 1 and use one ```text block per image, verbatim:
  do not shorten, reorder, soften or add to it.
- One subject per image. Never put two views or two subjects in one image.
- Extra views (-back, -front, -side) and HT-B / E09-F attach the image named in the
  "đính kèm" column as the only reference image.
- No text, letters, numbers, logos or watermarks inside any image.
- If an item is unclear or two files disagree, ask the owner a short question in
  Vietnamese instead of guessing.
```

## 1. Các file

| File | Chứa gì | Số ảnh |
|---|---|---|
| [`01-creatures.md`](01-creatures.md) | 2 ảnh thử dấu Héo (HT-A, HT-B); 7 sinh vật địch: E09, E18, E01 (mẫu duyệt), E11, E19, E25, G01, mỗi con 2 góc; cách đổi sang dấu B | 16 |
| [`02-allies-traps.md`](02-allies-traps.md) | 3 bẫy (Gai Chông, Bom Hạt Thông, Lưới Phóng), lính chặn Vệ Binh Rêu (2 góc), Nhà Thuốc Lá | 6 |
| [`03-pine-river-props.md`](03-pine-river-props.md) | 12 prop kit rừng thông có sông (xuân): 4 cây, 2 bụi, 3 đá, gốc, khúc gỗ, cầu | 12 |
| [`04-2d-ground-decals-backdrop.md`](04-2d-ground-decals-backdrop.md) | 8 ô đất lặp, 4 tấm decal 2 × 2, 1 phông xa (không gửi Tripo) | 13 |
| [`05-icons.md`](05-icons.md) | 20 icon HUD và cửa hàng (không gửi Tripo) | 20 |
| **Cộng** | 24 model (2 + 7 sinh vật, 5 phe ta, 12 prop: đúng DESIGN §7.2 "~24 model") + ảnh 2D dùng thẳng | **67** |

DESIGN §7.2 ước "~60 ảnh". Thêm 7 ảnh vì sinh vật và lính có 2 góc (DESIGN §7.1 "ảnh 2D nguồn cho mọi model (2 góc)") và vì 2 ảnh thử Héo.

## 2. Thứ tự làm

| Đợt | Việc | Ai | Cổng qua |
|---|---|---|---|
| **0 · Mẫu duyệt** | HT-A, HT-B, E09-F, E18-S, E18-F, E01-F (6 ảnh) | Codex | Chủ dự án chọn dấu Héo A hoặc B; duyệt dáng 3 loài. **Đã tạo 23/10**, xem `~/Downloads/dragon-hold-tripo-2d/` |
| 1 | Sửa theo ý chủ dự án; nếu chọn B: tạo lại E09-F, E18-S, E18-F, E01-F theo 01 §11. Thêm E09-B, E01-S | Codex | Ảnh đạt bảng kiểm 01 §12 |
| 2 | Tripo 3 model mẫu: E09 (Biped), E18 (Quadruped), E01 (bay) + 4 clip mỗi con | Chủ dự án | Chủ dự án duyệt model, rig, clip (DESIGN §9 M0, cổng "Chủ dự án"). Chưa đạt thì không làm đợt 4 |
| 3 | 12 prop kit (file 03), 8 ô đất, 4 decal, phông xa (file 04) | Codex → Tripo | Chủ dự án duyệt ảnh bản đồ 3 góc × 4 hướng khi M0b có hình |
| 4 | E11, E19, E25, G01 (file 01), Vệ Binh Rêu, Nhà Thuốc Lá, 3 bẫy (file 02) | Codex → Tripo | Bảng kiểm từng file |
| 5 | 20 icon (file 05); I01–I05 đính kèm ảnh nguồn đã duyệt + dòng `BUILDREF` | Codex | Đọc được ở 32 px |

- Ảnh 2D không chặn việc viết mã: M0a chạy bằng hộp xám (DESIGN §9).
- Prop và ô đất (đợt 3) không phụ thuộc dấu Héo: làm song song với đợt 1–2 được.

## 3. Thiết lập Tripo

### 3.1 Chung (giống bộ TD)

| Mục | Chọn |
|---|---|
| Chế độ | Có 2 góc: **Multiview to 3D** theo cột "Ô ảnh" ở 3.2. Một ảnh: **Image to 3D** |
| Tách nền | Bật (nền xám nhạt `#E6E6E6`) |
| Texture | Bật, HD cao nhất của gói. **PBR** bật |
| Lưới | Tam giác (Quad tắt). Smart Low Poly tắt |
| Face limit | Theo bảng 3.2. Blender giảm số tam giác chạy trong game sau (quái đám đông 1.500–3.000, prop 800–3.000) |
| Rig | Theo bảng 3.2 |
| Clip Tripo | Quái thường: đúng **4 clip** Idle, Move, Attack, Death, chọn preset gần nghĩa nhất trong thư viện Tripo. Thiếu preset (cắn, vồ, húc, bay) thì bỏ trống: Blender làm (02 §7.2). Tướng G01: thêm Cast, Hit, Intro nếu có preset |
| Tải về | **GLB** (bản có xương nếu đã rig). Đổi tên đúng id |

### 3.2 Từng model

Ảnh ở `games/dragon-hold/art-src/<thư mục>/`. GLB lưu ở **`games/dragon-hold/art-src/3d/<thư mục>/<id>.glb`** (cùng thư mục con với ảnh, thêm `3d/`).

| Mã | id | Ô ảnh Tripo | Face limit | Rig | Clip Tripo | GLB |
|---|---|---|---|---|---|---|
| E09 | `moss-grunt` | Multiview: Front = `moss-grunt.png`, Back = `moss-grunt-back.png` | 6000 | Biped | Idle, Walk, Attack (chém), Death | `3d/enemies/moss-grunt.glb` |
| E18 | `blight-wolf` | Multiview: Left = `blight-wolf.png` (nhìn ngang), Front = `blight-wolf-front.png` | 6000 | Quadruped | Idle, Run; Attack, Death nếu có preset | `3d/enemies/blight-wolf.glb` |
| E01 | `thorn-wasp` | Multiview: Front = `thorn-wasp.png`, Left = `thorn-wasp-side.png` | 5000 | Avian nếu gói có; lỗi thì không rig (Blender `build_winged_rig`) | Fly, Attack, Death (Blender `make_flight_clips` nếu thiếu) | `3d/enemies/thorn-wasp.glb` |
| E11 | `moss-archer` | Multiview: Front, Back | 6000 | Biped | Idle, Walk, Attack (bắn cung), Death | `3d/enemies/moss-archer.glb` |
| E19 | `tusk-boar` | Multiview: Left = ảnh chính, Front = `-front` | 8000 | Quadruped | Idle, Walk; Attack (húc), Death nếu có | `3d/enemies/tusk-boar.glb` |
| E25 | `thorn-ant` | Multiview: Left = ảnh chính, Front = `-front` | 4000 | Hexapod nếu gói có; lỗi thì không rig | Crawl, Attack, Death | `3d/enemies/thorn-ant.glb` |
| G01 | `moss-banner` | Multiview: Front, Back | 10000 | Biped | Idle, Walk, Attack, Death; thêm Cast, Hit, Intro nếu có | `3d/generals/moss-banner.glb` |
| U1 | `moss-warden` | Multiview: Front, Back | 6000 | Biped | Idle, Walk, Attack, Death | `3d/units/moss-warden.glb` |
| H1 | `herb-hut` | Image to 3D | 10000 | Không | — | `3d/houses/herb-hut.glb` |
| TR1 | `spikes` | Image to 3D | 4000 | Không | — | `3d/traps/spikes.glb` |
| TR2 | `pine-bomb` | Image to 3D | 4000 | Không | — | `3d/traps/pine-bomb.glb` |
| TR3 | `net-launcher` | Image to 3D | 6000 | Không | — | `3d/traps/net-launcher.glb` |
| K01 | `pine-tall` | Image to 3D | 10000 | Không | — | `3d/props/pine-river/pine-tall.glb` |
| K02 | `pine-round` | Image to 3D | 10000 | Không | — | `3d/props/pine-river/pine-round.glb` |
| K03 | `pine-young` | Image to 3D | 6000 | Không | — | `3d/props/pine-river/pine-young.glb` |
| K04 | `tree-violet` | Image to 3D | 10000 | Không | — | `3d/props/pine-river/tree-violet.glb` |
| K05 | `bush-moss` | Image to 3D | 5000 | Không | — | `3d/props/pine-river/bush-moss.glb` |
| K06 | `bush-blossom` | Image to 3D | 5000 | Không | — | `3d/props/pine-river/bush-blossom.glb` |
| K07 | `rock-boulder` | Image to 3D | 4000 | Không | — | `3d/props/pine-river/rock-boulder.glb` |
| K08 | `rock-slab` | Image to 3D | 4000 | Không | — | `3d/props/pine-river/rock-slab.glb` |
| K09 | `river-stones` | Image to 3D | 4000 | Không | — | `3d/props/pine-river/river-stones.glb` |
| K10 | `stump` | Image to 3D | 4000 | Không | — | `3d/props/pine-river/stump.glb` |
| K11 | `log` | Image to 3D | 4000 | Không | — | `3d/props/pine-river/log.glb` |
| K12 | `bridge-old` | Image to 3D | 10000 | Không | — | `3d/props/pine-river/bridge-old.glb` |

- Tự quyết: face limit theo bậc của bộ TD (quái nhỏ 6.000, lính 6.000 vì có khiên và chày, nhà 10.000) và art-pipeline §3 (prop 10.000 cho cây lớn, cầu). Bầy E25 và đồ nhỏ 4.000 vì sẽ giảm mạnh cho đám đông.
- Ảnh thử Héo (HT-A, HT-B) **không gửi Tripo**.

### 3.3 Khi Tripo ra lỗi

- Model Multiview ra ngược hoặc méo: đổi ảnh từ ô Left sang ô Right, tạo lại. Vẫn hỏng: dùng Image to 3D với ảnh chính.
- Ảnh phụ lệch nhiều so với ảnh chính (khác màu, khác mảng vỏ): báo AI tạo lại ảnh phụ, hoặc bỏ ảnh phụ.
- Rig báo lỗi: tải bản không rig, lưu cùng tên; Blender gắn xương (art-pipeline §12).
- Clip trượt về trước: vẫn dùng được, Blender khóa gốc.
- Có thể Regenerate 2–3 lần, giữ bản đẹp nhất.

## 4. Lưu file

- Thư mục game `games/dragon-hold/` chưa có (sẽ có khi tách game, DESIGN §9). Tới lúc đó ảnh nằm ở `~/Downloads/dragon-hold-tripo-2d/` theo **cùng cây thư mục con** (`refs/`, `enemies/`, `generals/`, `units/`, `houses/`, `traps/`, `props/pine-river/`, `ground/pine-river/`, `decals/pine-river/`, `backdrops/`, `ui/icons/`); mẫu duyệt nằm ở `samples/`.
- Khi có thư mục game: ảnh vào `games/dragon-hold/art-src/<thư mục>/<id>.png`, prompt cạnh ảnh `<id>.prompt.txt`, GLB vào `games/dragon-hold/art-src/3d/<thư mục>/<id>.glb`.
- **Không đưa ảnh, model, âm vào Git.** `games/dragon-hold/art-src/` phải nằm trong `.gitignore` từ commit đầu. Sao lưu bằng `pnpm media:push`; hiện script media chỉ quét `games/space-typing/art-src`, nên người tách game phải thêm `games/dragon-hold/art-src` vào cấu hình media trước lần push đầu.

## 5. Các dòng chung

Mọi prompt ghép từ các dòng dưới (giống từng chữ) + phần riêng của món. Bảng này để tra và để kiểm; **khi tạo ảnh, dán khối của từng món ở file 01–05, không ghép tay**.

| Dòng | Bắt đầu bằng | Dùng ở |
|---|---|---|
| Mục đích | `Image-to-3D source picture of ONE character or creature…` / `…ONE object…` / `Look-test picture…` | Mọi ảnh gửi Tripo / ảnh thử Héo |
| Phong cách 3D | `House style: stylized painterly 3D game art…` | Mọi ảnh gửi Tripo, ảnh thử |
| Khung, góc, dáng | `Framing:` + `View and pose for 3D rigging:` (hai chân tư thế A, bốn chân nhìn ngang, bay nhìn thẳng) hoặc `View: this is an extra view…` | Sinh vật, lính |
| Góc đồ vật | `View: three-quarter view, the object turned about 30 degrees…` | Bẫy, nhà, prop |
| Dấu Héo | `Héo mark (enemy faction signature)…` + `Shell coverage (look A, light)…` (hoặc look B) + câu `Shell placement` của loài | Chỉ quái và tướng địch |
| Phe ta | `Our side: this belongs to the Dragon's forest allies…` | Bẫy, nhà, lính |
| Màu | `Colour rules: no large areas of bright red, orange, gold or turquoise…` | Mọi ảnh gửi Tripo |
| Ánh sáng, khối | `Light: flat, even and frontal…` | Mọi ảnh gửi Tripo |
| Cấm | `Never draw: black outlines, fire, smoke, mist…` | Mọi ảnh gửi Tripo |
| Nền Tripo | `Background: plain flat very light neutral grey (#E6E6E6)…` | Mọi ảnh gửi Tripo, ảnh thử |
| Tham chiếu | `Reference: the attached image is…` | HT-B (đính kèm HT-A), E09-F (đính kèm ảnh thử đã chọn) |
| Phong cách 2D | `House style: hand-painted storybook fantasy art…` + khối `GROUND`, `DECAL`, `BACKDROP`, `ICON` + `Colour rules` bản 2D | File 04, 05 |
| Nền khóa màu | Ba dòng G, M, B của bộ TD, giống từng chữ | Decal, icon |

## 6. Cách AI tạo ảnh bằng Codex (trên máy chủ dự án)

1. Codex CLI đăng nhập bằng tài khoản ChatGPT của chủ dự án. **Không dùng API key:** chạy với `env -u OPENAI_API_KEY -u CODEX_API_KEY`. Không in, không chép token.
2. Mỗi lần **một ảnh**, khoảng 1 phút. Prompt là khối `text` của món, dán nguyên văn; khổ ảnh theo cột "Khổ" (1024×1024, 1024×1536 hoặc 1536×1024). Ảnh phụ, HT-B, E09-F: đính kèm ảnh ghi ở cột "Đính kèm".
3. AI **xem từng ảnh** và kiểm theo bảng kiểm của file. Hỏng rõ thì tạo lại, **tối đa 2 lần mỗi ảnh**. Lượt Codex tính vào hạn mức ChatGPT Plus của chủ dự án: chỉ tạo đúng đợt đang làm.
4. Chép ảnh đạt vào thư mục ở mục 4, đặt `<id>.prompt.txt` cạnh ảnh (đúng prompt đã dùng).
5. Báo chủ dự án: ảnh nào cần duyệt, ảnh nào đã tạo lại và vì sao.

## 7. Còn mở (hỏi chủ dự án; đều có mặc định)

1. Dấu Héo A hay B? **Mặc định:** A (đúng câu thiết kế "phủ một phần thân"). Chọn B thì làm theo 01 §11.
2. Cầu gỗ (K12) tính vào 12 prop M0 thay một hòn đá? **Mặc định:** có, vì bản đồ M0 `L2-cau` có cầu.
3. Bệ Rồng ở giữa bản đồ chưa có trong danh sách M0. **Mặc định:** M0 dùng khối tạm; thêm ảnh Tripo khi anh muốn.
4. Bài A/B cây 3D và 2D (art-pipeline §3)? **Mặc định:** làm bản 3D trước; ảnh billboard 2D chỉ làm khi anh muốn so.
