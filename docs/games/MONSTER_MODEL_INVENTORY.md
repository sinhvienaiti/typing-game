# Kiểm kê model quái 3D của bốn game (01/11/2026)

Chủ dự án, 01/11/2026: "chúng ta luôn có sẵn các hình ảnh quái của các game, bạn có thể tái sử dụng trước các hình quái 3d chứ k nên cứ game nào cũng tạo mới ra hàng đống ảnh quái".

Phạm vi: Space Typing, Dragonhold, Wordwoven, Last Line. Không tính Tu Tiên. Không tính worktree (`games/.wt-*`), `tmp/`, `dist/`.

## Tóm tắt

**Có sẵn nhiều hơn ta tưởng.** Bốn game đã có file cho 195 mục model sinh vật (quái, tướng, boss, nhân vật). Space còn thêm 14 bản gốc chưa build. Tổng cộng 31 bản gốc chưa game nào dùng. Trước khi đặt Tripo làm quái mới cho game nào, tra bảng ở mục 6.

| Game | Mục model sinh vật | Có xương và clip | Chỉ có clip node (không xương) | Chưa có clip | Chưa game nào dùng |
|---|---:|---:|---:|---:|---:|
| Space Typing | 153 mục manifest (112 quái, 10 LOD, 27 boss, 3 hero, 1 guide), 133 lưới khác nhau; thêm 14 bản gốc chưa build | 6 (4 Draconis, `tyrant-g01`, `auriel-hero`) | 147 (`Enemy_Idle` hoặc `Boss_*`) | 0 (14 bản gốc chưa build cũng chưa có clip) | 14 (11 `magma-*`, 3 drone: `drone`, `lock-on`, `bomb`) |
| Dragonhold | 11 (8 của game: 7 quái và tướng, 1 lính; 3 bản chép Draconis) | 3 (bản chép Draconis) | 0 | 8 (game dựng xương lúc chạy bằng code crowd-rig) | 0 |
| Wordwoven | 25 (8 đã ship: 6 quái, Lam, Linh Giáo; 17 thân gốc chưa ship) | 9 (8 đã ship, cú `helper-owlet` trong `art-src/models`) | 0 | 16 bản gốc Tripo chưa rig | 17 (trong đó 6 quái, 2 boss, Draconis riêng của WW) |
| Last Line | 6 (5 quái `rainbow-*`, `draconis-v3`), đều chép nguyên từ Space (md5 trùng) | 1 (`draconis-v3`) | 5 (`Enemy_Idle`) | 0 | 0 |
| **Cộng** | **195** (thêm 14 bản gốc) | **19** | **152** | **24** | **31** |

Mỗi bản sao được đếm riêng, nên Draconis tính cả ở Dragonhold và Last Line. "Có xương và clip" là rig thật. "Chỉ có clip node" là cả model cùng lắc hay nhún, không uốn được thân.

**Năm điều chính:**
1. **Last Line nên lấy họ `cosmic` của Space (14 model) làm quân chính của Black Hole Horde.** Họ này tím hư không viền vàng, có xúc tu, lính giáp, pháp sư và tàu, hợp chủ đề hố đen hơn họ `rainbow` pastel đang dùng. Chỉ cần chép vào manifest của Last Line như đã làm với `rainbow-*` (công S). 11 bản gốc `magma-*` của Space chưa game nào dùng. Chúng hợp vành lửa cam của hố đen (công M). Ba drone đấu tay đôi (`drone`, `lock-on`, `bomb`) cũng chưa dùng, và đúng chất máy công nghiệp của trạm.
2. **Dragonhold lấy được nhiều quái của Wordwoven đã rig sẵn.** `troll` dùng cho Chằn Rừng hoặc Chằn Đánh Trống. `thuong-luong` dùng cho Lươn Sông và boss Thủy Xà Sông Lam, trùng cả tên. `tanuki` dùng cho Lửng Đào Hang. `nuppeppo` (có clip chết tách đôi) dùng cho Nấm Phồng. `alicanto` dùng cho Quạ Trộm (cùng vai trộm). `moc-tinh` dùng cho Cổ Thụ Mục. Họ `nature` và `shadow` của Space cũng phủ được họ rêu, nấm và sương: chỉ cần chỉnh `wash` màu họ quái trong code Dragonhold, không cần ảnh mới.
3. **Hero Draconis của Wordwoven có thể dùng `draconis-v4` của Space.** v4 thân trắng, cánh đỏ, gần với mô tả WW. Bộ clip `Hero_*` của `draconis-v2` chạy thẳng trên v4 vì hai bản cùng một khung 25 xương (đã so tên khớp). Như vậy khỏi phải rig bản gốc WW 33.566 tam giác.
4. **Space không cần quái mượn.** Nó là kho nguồn. 9 mục chưa có bản gốc đúng ảnh 2D (`SOURCES.json` → `notMadeYet`: 7 quái và `tyrant-g03` đang dùng lưới tạm, `magma-tank` chưa build).
5. **Còn thiếu thật** (mục 7): dơi, bướm, cóc, nai, gấu, nhện, cua, rết, ngựa ma, kỳ nhông cho Dragonhold. Wordwoven thiếu Ghost Flame (nên làm bằng VFX). Last Line thiếu boss có bộ phận tách được và LOD bầy cho các họ mới.

**Luật khi tái dùng:**
- Mỗi game build và deploy một mình. Game đích build bản riêng từ **bản gốc** trong `art-src/3d` vào manifest của mình, như Last Line đã làm với `rainbow-*`. Không trỏ sang `public/` của game khác.
- Bản gốc chép sang `art-src/3d` của game đích, ghi vào `SOURCES.json` của game đó.
- Không sửa model của game nguồn ("model đang có thì giữ nguyên").
- Theo [MODEL_QUALITY](MODEL_QUALITY.md): quái và lính ở High ≥ 6.000 tam giác (giữ nguyên gốc nếu ≤ 20.000), boss và rồng ≥ 20.000, giữ normal map và roughness map, màu 2048 ở High.
- Không lấy file đã ship của Dragonhold làm nguồn. File High của Dragonhold chỉ còn 1.707–4.325 tam giác và một map màu 1024, dưới sàn. Build lại từ bản gốc Tripo.
- Clip và rig dùng lại giữa các game là hệ chung, phải qua [mốc 9 điểm](SHARED_SYSTEMS_BAR.md).
- Đổi VFX theo [VFX_STANDARD](VFX_STANDARD.md), đủ 5 pha.
- Đổi màu hay vẽ lại texture thì chấm lại theo [ART_ACCEPTANCE](ART_ACCEPTANCE.md).

## 1. Cách đo

- Số liệu đo ngày 01/11/2026. Một script Python nhỏ (để ngoài repo) đọc khối JSON của từng GLB. Nó đếm tam giác của mọi mesh trong scene, đếm xương theo `skins[].joints`, liệt kê tên `animations`. Nó đọc cỡ ảnh texture thật từ header PNG, JPEG hay WebP trong khối BIN. Khung (bbox) lấy từ `min/max` của `POSITION` qua các phép biến đổi node.
- Script đã quét 465 file: `public/` của bốn game, `art-src/3d`, `art-src/models` của Wordwoven, rig Mesh2Motion.
- **File tốt nhất đã ship** là bậc `.high.glb` trong `public/assets/<game>/models/<kind>/<id>/<id>.high.glb`. Bậc `.medium.glb` có cùng lưới, ít mặt hơn.
- **Map:** B là màu nền, N là normal map, MR là metal-roughness, E là emissive. Con số là cạnh ảnh tính bằng pixel.
- **Khung:** đơn vị là đơn vị scene (đv). Space chuẩn hoá cạnh dài nhất về 2 đv, game tự đặt cỡ lúc chạy, nên cột Khung của Space không phải mét. Bản gốc Tripo chuẩn hoá về 1 đv. Dragonhold và Wordwoven ghi cỡ thật bằng mét trong manifest. Last Line chép bản của Space nên khung vẫn tính theo 2 đv.
- **Phong cách:**
  - Space: *stylized bán thực, chi tiết dày*. Ảnh 2D vẽ kiểu sơn dầu; bản gốc Meshy khoảng 30.000 tam giác, riêng họ `shadow` làm trên Tripo. Quái nhìn như tàu từ trên xuống.
  - Dragonhold: *stylized* kiểu Warcraft, Tripo 3.700–8.400 tam giác. Bản ship đã cắt xuống *low-poly*.
  - Wordwoven: *stylized chibi, đồ chơi*, Tripo khoảng 5.700 tam giác. Boss và hero 23.000–35.000 tam giác.
- **Loại sinh vật:** humanoid, beast, flyer, insect, serpent, blob, plant, spirit, undead, mech, craft (tàu sinh học hay tàu máy), mine/core/totem (vật bất động).
- **Công:**
  - **S:** chép gốc, build bản của game đích, đổi màu bằng shader hay `wash`, đặt cỡ. Không ảnh mới. Khoảng nửa ngày.
  - **M:** vẽ lại texture, hoặc rig bằng crowd-rig marks hay Mesh2Motion, hoặc làm clip. 1–2 ngày.
  - **L:** sửa lưới, rig và đủ bộ clip, hoặc đổi phong cách. Từ 3 ngày, cần chủ dự án duyệt.
- **Tên game viết tắt:** ST là Space Typing, DH là Dragonhold, WW là Wordwoven, LL là Last Line. Mã quái DH như E12 hay B15 lấy từ [02-enemies-generals-bosses.md](dragon-lane/02-enemies-generals-bosses.md). Vai WW lấy từ `typing-defense/docs/td/TYPING_DEFENSE_DESIGN.md` §22.
- **Công cụ rig có sẵn:**
  - crowd-rig của Dragonhold: dựng xương bằng code theo dáng `biped`, `quadruped`, `flyer`, `hexapod` (`games/dragon-hold/src/view/model-specs.ts`).
  - Rig Mesh2Motion trong `games/typing-defense/art-src/anim/mesh2motion/`: người 66 xương (bộ clip base và addon), chim 55 xương (`Flap`, `Glide`, `Idle`, `Walk`), rắn 28 xương (`Bite`, `Coiled`, `Side winding`, `Hit`, `Death`).

## 2. Space Typing (`games/space-typing`)

Manifest: `public/assets/space-typing/models/manifest.json` (189 mục, 153 là sinh vật). Bản gốc: `art-src/3d/` (`SOURCES.json` ghi md5, ảnh 2D, nơi dùng). Preset build: `scripts/models/presets/campaign3d-models.json`.

Ghi chú dữ liệu:
- Nhà làm bản gốc: quái và boss làm trên Meshy (file ghi `pygltflib`), riêng họ `shadow` và `rainbow-tank` làm trên Tripo. Thông tin từ ghi chú nhập 21/10 và trường `generator` của GLB.
- `art-src/models/raw/enemies/` là 124 bản trùng của bản gốc. Các tên "chưa làm" ở đó chỉ là bản chép byte của lưới tạm. Riêng `raw/rainbow-scout.glb` là bản chép của `prism-destroyer` (md5 trùng), không phải scout thật.
- `rainbow-scout-3d` và `rainbow-tank-3d` dùng chung lưới `rainbow-tank` (chủ dự án, 26/10).
- Draconis v1–v3 và guide v4 không còn bản gốc trên máy này (`SOURCES.json` → `noOriginalOnThisMachine`). Bản ship là nguồn duy nhất.

### 2.1 Hero và guide

| id | File High | Tam giác | Xương · clip | Map High | Khung High (đv) | Phong cách · loại | 2D | Dùng cho game khác |
|---|---|---:|---|---|---|---|---|---|
| `draconis` | `heroes/draconis/draconis.high.glb` | 22.000 | 25 xương · Hero_Idle_Hover, Hit, Death, Intro, Fly, Boost, Attack_L, Attack_R, Cast, Victory | B/N/MR/E 2048 | 2,18×2×1,05 | stylized bán thực · rồng hình người có cánh | không có | — |
| `draconis-v2` (Hỏa Long) | `heroes/draconis-v2/draconis-v2.high.glb` | 22.000 | 25 xương · Hero_Fly, Idle_Hover, Boost, Attack_L, Attack_R, Attack_Both, Cast, Hit, Victory, Death, Intro | B/N/MR/E 2048 | 2,21×2×1,56 | như trên, đỏ đào | không có | đang ở DH (rồng lửa); bộ clip này chạy được trên v1 và v4 (cùng 25 xương, cùng tên) |
| `draconis-v3` (Viêm Đế) | `heroes/draconis-v3/draconis-v3.high.glb` | 60.000 | 32 xương (thêm 3 đốt cổ, hàm, tay, 6 đốt đuôi) · Hero_Fly, Idle_Hover, Boost, Spit, Spit_Big, Cast, Hit, Victory, Death, Intro | B/N/MR/E 2048 | 4,11×2×2,77 | rồng cánh lớn | không có | đang ở DH và LL; DH B19 `black-wyrm` đổi vật liệu đen (đã ghi trong thiết kế DH, M) |
| `draconis-v4` (Bạch Long, guide) | `guides/draconis-v4/draconis-v4.high.glb` | 31.226 | 25 xương · Guide_Idle, Wave, Flap, Hop, Bow, Talk | B/N/MR/E 2048 | 2,02×2×1,18 | rồng hình người trắng, cánh đỏ | không có | đang ở DH; **WW hero Draconis**: thêm clip Hero_* của v2, vẽ lại cánh lông vũ kem viền cam (S–M) |

Socket chung của Draconis: `FX_MOUTH`, `FX_CAST_L/R`, `FX_WING_L/L2/R/R2`, `FX_TAIL`, `FX_FOOT_L/R`, `FX_CORE`, `FX_HALO` (v3 thêm `FX_JAW`).

### 2.2 Boss (27 mục, 25 lưới gốc)

Chung cho mọi dòng:
- File High: `bosses/<id>/<id>.high.glb`, khoảng 30.000 tam giác, map B/N/MR/E 2048.
- Bản gốc Meshy, map B/N/MR 2048.
- Socket `FX_HALO`, `FX_CAST_L/R`, `FX_CORE`.
- Phong cách stylized bán thực, trang trí dày, đứng thẳng nhìn trước.
- 2D: `art-src/bosses/<id>.png`.
- Chỉ `tyrant-g01` và `auriel-hero` có xương (64). Các boss khác chỉ có clip node, cả thân cùng chuyển động.

| id (High) | Gốc `art-src/3d/bosses/` | Tam giác gốc → High | Khung High (đv) | Xương · clip | Loại: dáng | Dùng cho game khác |
|---|---|---|---|---|---|---|
| `lieutenant-angel` | `lieutenant-angel` | 31.533 → 30.000 | 1,81×2×0,97 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | humanoid: thiên thần áo vàng cầm chuông | — |
| `lieutenant-cosmic` | `lieutenant-cosmic` | 29.701 → 29.701 | 1,93×2×1,49 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | mech: người máy golem giáp tím, lõi vàng | LL boss Station Golem (S) |
| `lieutenant-devil` | `lieutenant-devil` | 31.766 → 30.000 | 2×1,77×1,58 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | humanoid brute: quỷ giáp đỏ, tay pháo | LL boss Furnace Brute (S) |
| `lieutenant-frost` | `lieutenant-frost` | 31.729 → 30.000 | 1,2×2×0,69 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | humanoid spirit: hình người áo băng | WW tinh tuyết, cần đổi phong cách (L) |
| `lieutenant-nature` | `lieutenant-nature` | 30.359 → 30.000 | 1,83×2×1,17 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | beast (bọ): bọ cánh cứng rêu | DH B13 `storm-beetle` (đã ghi trong thiết kế DH, M); DH E27 `acid-beetle` thu nhỏ (M) |
| `lieutenant-prism` | `lieutenant-prism` | 30.158 → 30.000 | 1,08×2×0,34 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | humanoid: hiệp sĩ pha lê | — |
| `lieutenant-rainbow` | `lieutenant-rainbow` | 31.286 → 30.000 | 1,89×2×1 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | humanoid: hiệp sĩ pha lê hồng cầm khiên | — |
| `lieutenant-shadow` | `lieutenant-shadow` | 31.733 → 30.000 | 1,99×2×0,93 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | spirit: bóng ma tua rua | DH E05 `mist-wraith` cỡ lớn hoặc B20 (M); LL boss phụ (S) |
| `tyrant-g01` | `tyrant-g01` | 30.150 → 30.150 | 1,75×1,7×0,67 | 64 xương · 01_Boss_Skill_Prismatic_Burst_V3, 00_Boss_Idle_Hover_V3, Boss_Hit, Boss_Death, Boss_Intro | humanoid (seraph): nữ thiên sứ hồng nhiều cánh | — (Auriel, nhân vật Space) |
| `tyrant-g02` | `tyrant-g02` | 31.670 → 29.999 | 1,58×2×0,83 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | humanoid demon: chúa quỷ đỏ cầm lưỡi | LL boss Furnace Lord (S) |
| `tyrant-g03` | `warden-frost` (tạm) | 30.932 → 30.000 | 1,75×2×0,53 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | humanoid spirit: (tạm: lưới warden-frost; 2D nữ hoàng băng) | xem warden-frost |
| `tyrant-g04` | `tyrant-g04` | 28.825 → 28.825 | 1,43×2×0,54 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | plant giant: người cây khổng lồ | DH B11 `rotwood-ancient` (phương án 2) hoặc E17 `stone-golem` (M) |
| `tyrant-g05` | `tyrant-g05` | 31.772 → 29.999 | 1,41×2×0,22 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | eldritch spirit: thực thể hư không có mắt | LL boss chương Black Hole Herald (S); DH B20 `mist-mother` (M) |
| `tyrant-g06` | `tyrant-g06` | 31.457 → 30.000 | 1,76×2×1 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | mech: hiệp sĩ máy giáp xanh đen, lõi cam | LL boss Iron Colossus (S) |
| `tyrant-g07` | `tyrant-g07` | 31.865 → 30.000 | 1,85×2×0,69 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | eldritch demon: quỷ đỏ xúc tu | LL boss (S) |
| `tyrant-g08` | `tyrant-g08` | 31.426 → 30.000 | 1,67×2×0,93 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | humanoid caster: phù thủy hư không áo choàng lam | DH G12 `mist-hierophant` (M); LL Void Priest boss (S) |
| `tyrant-g09` | `tyrant-g09` | 31.289 → 30.000 | 2×1,95×1,14 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | humanoid (death knight): hiệp sĩ đen cánh, ngai | DH B14 `mist-knight`, phần kỵ sĩ; thiếu ngựa (M) |
| `tyrant-g10` | `tyrant-g10` | 30.699 → 29.999 | 1,53×2×0,5 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | humanoid (lich): hoàng đế tím áo choàng | DH G05 `mist-elder` (M) |
| `warden-angel` | `warden-angel` | 30.749 → 30.000 | 2×1,94×0,55 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | humanoid: thiên thần vàng cánh | — |
| `warden-cosmic` | `warden-cosmic` | 31.429 → 29.999 | 1,47×2×0,84 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | humanoid: vua vũ trụ áo choàng lam | LL boss (S) |
| `warden-devil` | `warden-devil` | 31.833 → 30.000 | 1,87×2×0,88 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | humanoid brute: quỷ sừng có cánh | LL boss (S); WW Oni King cần đổi phong cách (L) |
| `warden-frost` | `warden-frost` | 30.932 → 30.000 | 1,75×2×0,53 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | humanoid spirit: thiếu nữ băng | WW Snow Woman (Yuki-onna) boss, cần đổi phong cách (L) |
| `warden-nature` | `warden-nature` | 28.705 → 28.705 | 1,65×2×0,61 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | humanoid plant: chiến binh gỗ giáp lá | DH B02 `moss-chieftain` hoặc G14 `stone-marshal` (M) |
| `warden-prism` | `warden-prism` | 30.616 → 30.000 | 1,5×2×0,47 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | humanoid: người pha lê | — |
| `warden-rainbow` | `warden-rainbow` | 31.551 → 30.000 | 1,69×2×0,42 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | humanoid (fairy): tiên hồng | — |
| `warden-shadow` | `warden-shadow` | 31.687 → 29.999 | 1,79×2×0,41 | không · Boss_Hit, Boss_Death, Boss_Intro, Boss_Idle_Hover (node) | eldritch spirit: chúa hư không đầu mắt | LL boss Black Hole Herald (S); DH B20 `mist-mother` (M); WW avatar Mute Ink (L) |
| `auriel-hero` | `tyrant-g01` | 30.150 → 30.150 | 1,75×1,7×0,67 | 64 xương · 01_Boss_Skill_Prismatic_Burst_V3, 00_Boss_Idle_Hover_V3, Boss_Hit, Boss_Death, Boss_Intro, Hero_Fly, Hero_Boost, Hero_Attack_L, Hero_Attack_R, Hero_Cast, Hero_Victory | humanoid (seraph): Auriel bản anh hùng, thêm clip Hero_* | — |

### 2.3 Quái (112 mục `-3d`, 10 mục LOD, 104 lưới gốc)

Chung cho mọi dòng:
- File High: `enemies/<id>/<id>.high.glb`, 6.000 tam giác (khoảng 5.800 với lưới Tripo `rainbow-tank`), map B/N/MR/E 1024.
- Bản gốc khoảng 26.000–31.700 tam giác, map B/N/MR 2048.
- Không xương. Một clip node `Enemy_Idle`.
- Mục `-lod`: 1.000–1.200 tam giác, dùng cho đám đông.
- Phong cách stylized bán thực, trang trí dày. Hầu hết vẽ như tàu nhìn từ trên xuống, nên đọc tốt khi camera cao.
- "(tạm)" là mục đang dùng lưới của mục khác (`SOURCES.json` → `notMadeYet`).

**Họ angel** (craft (thánh quang trắng vàng, halo, cánh)). 2D: `art-src/enemies/<gốc>.png`.

| id (High) | Gốc `art-src/3d/enemies/` | Tam giác gốc → High | Khung High (x×y×z, đv) | Loại: dáng | Dùng cho game khác |
|---|---|---|---|---|---|
| `angel-carrier-3d` | `angel-carrier` · Meshy | 28.922 → 6.000 | 1,86×2,01×0,8 | craft: tàu mẹ có halo | — |
| `angel-cloaker-3d` | `angel-cloaker` · Meshy | 30.910 → 6.000 | 2×1,86×0,39 | craft: phi tiêu cánh mảnh | — |
| `angel-commander-3d` | `angel-commander` · Meshy | 30.972 → 6.000 | 2×1,96×0,87 | craft: soái hạm cánh trang trí | — |
| `angel-destroyer-3d` | `angel-destroyer` · Meshy | 31.372 → 6.000 | 1,22×2×0,74 | craft: tàu cánh móc | — |
| `angel-healer-3d` | `angel-healer` · Meshy | 30.061 → 6.000 | 1,46×2×0,76 | flyer (sứa): sứa thánh, xúc tu sáng | — |
| `angel-jammer-3d` | `angel-jammer` · Meshy | 30.595 → 6.000 | 1,84×1,98×0,88 | craft: tàu chảo ăng-ten | — |
| `angel-leech-3d` | `angel-leech` · Meshy | 27.873 → 6.000 | 2,01×1,97×1,16 | beast: xúc tu, miệng xoáy | LL Leech: đổi màu thép tối và cam (M) |
| `angel-mine-3d` | `angel-mine` · Meshy | 26.151 → 6.000 | 2×1,98×1,52 | mine: cầu gai vàng có cánh | — |
| `angel-oppressor-3d` | `angel-oppressor` · Meshy | 30.486 → 6.000 | 1,38×2×0,85 | craft: tháp halo có vòng | — |
| `angel-scout-3d` | `angel-scout` · Meshy | 31.248 → 6.000; LOD `angel-scout-lod` 999 | 1,99×1,55×1,4 | craft: phi tiêu cánh | — |
| `angel-shield-3d` | `angel-shield` · Meshy | 29.926 → 6.000 | 1,66×2,02×1,16 | craft: khiên cánh bọc giáp | — |
| `angel-sniper-3d` | `angel-sniper` · Meshy | 30.725 → 6.000 | 1,95×2×0,59 | craft: giáo dài có cánh | — |
| `angel-splitter-3d` | `angel-splitter` · Meshy | 30.373 → 6.000 | 1,96×2,02×0,95 | craft: hai cầu sáng có cánh | — |
| `angel-tank-3d` | `angel-tank` · Meshy | 29.621 → 6.000; LOD `angel-tank-lod` 1.199 | 1,86×1,42×1,99 | mech: xe hai động cơ nặng | LL Heavy Walker: tắt halo, đổi màu thép (M) |

**Họ cosmic** (tím hư không viền vàng; hợp Black Hole Horde nhất). 2D: `art-src/enemies/<gốc>.png`.

| id (High) | Gốc `art-src/3d/enemies/` | Tam giác gốc → High | Khung High (x×y×z, đv) | Loại: dáng | Dùng cho game khác |
|---|---|---|---|---|---|
| `cosmic-carrier-3d` | `cosmic-carrier` · Meshy | 27.318 → 6.000 | 2×1,45×0,88 | craft: tàu mẹ hư không | LL Brood Carrier, đẻ bầy (S) |
| `cosmic-cloaker-3d` | `cosmic-cloaker` · Meshy | 29.247 → 6.000 | 2×1,65×0,34 | flyer: cá đuối sao | LL Void Ray, ẩn hình (S) |
| `cosmic-commander-3d` | `cosmic-elite` · Meshy | 31.637 → 6.000 | 1,91×2,02×1,06 | humanoid: chiến binh ngoài hành tinh giáp, lưỡi liềm | LL Elite Stalker: lướt (S) hoặc rig người Mesh2Motion để đi (M) |
| `cosmic-destroyer-3d` | `cosmic-dreadnought` · Meshy | 26.671 → 6.000 | 1,41×2×0,8 | craft: chiến hạm nặng | LL Gunship nặng (S) |
| `cosmic-healer-3d` | `cosmic-sorcerer` · Meshy | 31.291 → 6.000 | 1,65×1,59×2 | humanoid caster: pháp sư trùm áo, cầu sáng | LL Void Priest (S); DH E15 `mist-shaman`: wash xám tím (M) |
| `cosmic-jammer-3d` | `cosmic-jammer` · Meshy | 30.851 → 6.000 | 2×1,52×0,31 | craft: tàu nhỏ nhiễu sóng | LL Jammer drone (S) |
| `cosmic-leech-3d` | `cosmic-leecher` · Meshy | 31.622 → 6.000 | 2,01×1,98×0,99 | beast: tôm mực xúc tu | LL Horde Leech, lắc xúc tu bằng shader (S) |
| `cosmic-mine-3d` | `cosmic-core` · Meshy | 27.778 → 6.000 | 1,98×2×0,3 | core: lõi tinh thể xoáy | LL lõi tổ đẻ quái (S) |
| `cosmic-oppressor-3d` | `cosmic-grunt` · Meshy | 31.598 → 6.000 | 1,76×2×0,95 | craft: phi tiêu tím, động cơ hồng | LL Dart (S) |
| `cosmic-scout-3d` | `cosmic-fast` · Meshy | 30.849 → 6.000; LOD `cosmic-scout-lod` 999 | 1,43×1,97×0,5 | craft: phi tiêu nhanh | LL bầy nhanh, có LOD (S) |
| `cosmic-shield-3d` | `cosmic-shield` · Meshy | 28.574 → 6.000 | 1,89×2×1,3 | beast: thú tinh thể trong bong bóng khiên | LL Shield Bearer (S) |
| `cosmic-sniper-3d` | `cosmic-sniper` · Meshy | 30.827 → 6.000 | 1,71×1,58×2,01 | humanoid: lính giáp cầm pháo | LL Sniper (S lướt; M nếu rig đi bộ) |
| `cosmic-splitter-3d` | `cosmic-beast` · Meshy | 31.621 → 6.000 | 2×1,98×0,81 | beast: tôm mực xúc tu (cùng dáng leecher) | LL Splitter (S) |
| `cosmic-tank-3d` | `cosmic-tank` · Meshy | 29.846 → 6.000 | 1,79×2,01×1,48 | mech: mai rùa giáp đi bộ | LL Heavy Tank (S) |

**Họ devil** (craft quỷ đen đỏ, gai dung nham). 2D: `art-src/enemies/<gốc>.png`.

| id (High) | Gốc `art-src/3d/enemies/` | Tam giác gốc → High | Khung High (x×y×z, đv) | Loại: dáng | Dùng cho game khác |
|---|---|---|---|---|---|
| `devil-carrier-3d` | `devil-carrier` · Meshy | 29.419 → 6.000 | 1,67×2×0,61 | craft: tàu mẹ gai | LL Furnace Horde (S) |
| `devil-cloaker-3d` | `devil-cloaker` · Meshy | 29.258 → 5.999 | 2×1,81×0,48 | craft: cánh dơi gai | LL Furnace Horde (S) |
| `devil-commander-3d` | `devil-commander` · Meshy | 31.685 → 6.000 | 2×1,82×1,08 | craft: soái hạm gai | LL Furnace Horde (S) |
| `devil-destroyer-3d` | `devil-cloaker` (tạm) · Meshy | 29.258 → 5.999 | 2×1,81×0,48 | craft: (tạm: lưới của cloaker) | theo cloaker |
| `devil-healer-3d` | `devil-healer` · Meshy | 30.946 → 6.000 | 1,87×1,99×0,58 | craft: tàu vòng sáng | LL Furnace Horde (S) |
| `devil-jammer-3d` | `devil-jammer` · Meshy | 30.165 → 6.000 | 2×1,68×1,38 | craft: tàu ăng-ten gai | LL Furnace Horde (S) |
| `devil-leech-3d` | `devil-leech` · Meshy | 31.006 → 6.000 | 1,86×2,01×0,92 | beast: vòng xúc tu quanh miệng | LL Furnace Leech (S) |
| `devil-mine-3d` | `devil-mine` · Meshy | 29.399 → 6.000 | 2,01×1,95×1,56 | mine: cầu gai có mắt | LL Furnace Mine (S) |
| `devil-oppressor-3d` | `devil-oppressor` · Meshy | 28.170 → 6.000 | 1,76×2,01×1,74 | totem: tháp mắt có vòng | LL (S) |
| `devil-scout-3d` | `devil-scout` · Meshy | 31.003 → 6.000; LOD `devil-scout-lod` 999 | 2,01×1,32×1,6 | craft: phi tiêu gai | LL (S) |
| `devil-shield-3d` | `devil-shield` · Meshy | 29.312 → 6.000 | 1,95×2×2,24 | craft: khiên gai | LL (S) |
| `devil-sniper-3d` | `devil-sniper` · Meshy | 30.683 → 6.000 | 1,49×2×0,47 | craft: giáo gai dài | LL (S) |
| `devil-splitter-3d` | `devil-splitter` · Meshy | 30.056 → 6.000 | 1,93×2×0,75 | craft: hai mắt dung nham | LL (S) |
| `devil-tank-3d` | `devil-tank` · Meshy | 30.889 → 6.000 | 1,7×2,01×0,91 | mech: xe gai hai động cơ | LL (S) |

**Họ frost** (craft băng tinh thể). 2D: `art-src/enemies/<gốc>.png`.

| id (High) | Gốc `art-src/3d/enemies/` | Tam giác gốc → High | Khung High (x×y×z, đv) | Loại: dáng | Dùng cho game khác |
|---|---|---|---|---|---|
| `frost-carrier-3d` | `frost-carrier` · Meshy | 29.877 → 6.000 | 1,99×2×1,16 | craft: tàu mẹ băng | — |
| `frost-cloaker-3d` | `frost-cloaker` · Meshy | 30.358 → 6.000 | 2×1,96×0,45 | craft: cánh băng mảnh | — |
| `frost-commander-3d` | `frost-commander` · Meshy | 30.251 → 6.000 | 1,97×2×0,53 | craft: soái hạm băng | — |
| `frost-destroyer-3d` | `frost-commander` (tạm) · Meshy | 30.251 → 6.000 | 1,97×2×0,53 | craft: (tạm: lưới của commander) | — |
| `frost-healer-3d` | `frost-healer` · Meshy | 31.279 → 6.000 | 1,87×1,98×1,3 | craft: tàu xúc tu băng | — |
| `frost-jammer-3d` | `frost-jammer` · Meshy | 30.263 → 5.999 | 1,96×2×0,9 | craft: tàu ăng-ten băng | — |
| `frost-leech-3d` | `frost-healer` (tạm) · Meshy | 31.279 → 6.000 | 1,87×1,98×1,3 | beast: (tạm: lưới của healer; 2D là bọ cạp băng cuộn) | — |
| `frost-mine-3d` | `frost-mine` · Meshy | 23.404 → 6.000 | 1,99×1,99×0,77 | mine: sao băng | — |
| `frost-oppressor-3d` | `frost-oppressor` · Meshy | 31.027 → 6.000 | 1,67×2×1,7 | totem: tháp băng có vòng | — |
| `frost-scout-3d` | `frost-scout` · Meshy | 30.416 → 6.000; LOD `frost-scout-lod` 1.000 | 2×1,95×0,26 | craft: phi tiêu băng | — |
| `frost-shield-3d` | `frost-shield` · Meshy | 30.635 → 6.000 | 1,88×2,03×1,53 | craft: mai băng cuộn | — |
| `frost-sniper-3d` | `frost-sniper` · Meshy | 30.575 → 6.000 | 0,47×0,94×1,99 | craft: giáo băng | — |
| `frost-splitter-3d` | `frost-splitter` · Meshy | 30.422 → 6.000 | 1,97×2,02×0,68 | craft: hai lõi băng | — |
| `frost-tank-3d` | `frost-tank` · Meshy | 20.505 → 6.000 | 1,9×2×0,96 | mech: xe băng nặng | — |

**Họ nature** (thực vật: lá, rêu, rễ, hoa; hợp Dragonhold nhất). 2D: `art-src/enemies/<gốc>.png`.

| id (High) | Gốc `art-src/3d/enemies/` | Tam giác gốc → High | Khung High (x×y×z, đv) | Loại: dáng | Dùng cho game khác |
|---|---|---|---|---|---|
| `nature-carrier-3d` | `nature-carrier` · Meshy | 30.009 → 6.000 | 1,99×0,86×0,93 | craft: thuyền lá rêu bay | — |
| `nature-cloaker-3d` | `nature-cloaker` · Meshy | 29.139 → 6.000 | 2×1,28×0,36 | flyer: lá dáng cá đuối | DH E07 `veil-moth`: cánh lam tím, rig flyer (M) |
| `nature-commander-3d` | `nature-boss` · Meshy | 31.689 → 6.000 | 2×1,65×1,09 | humanoid plant: nữ thần cây có cánh lá (gốc `nature-boss`) | DH G10 `thorn-matron`: crowd-rig biped, wash gai (M) |
| `nature-destroyer-3d` | `nature-destroyer` · Meshy | 28.759 → 6.000 | 1,89×1,41×2,02 | craft: hai lưỡi gai | — |
| `nature-healer-3d` | `nature-healer` · Meshy | 30.713 → 6.000 | 1,67×2×1,03 | flyer (sứa): sứa dây leo, vương miện hoa | DH healer bay họ spore, ngoài roster (M) |
| `nature-jammer-3d` | `nature-jammer` · Meshy | 30.446 → 6.000 | 1,97×2,01×0,74 | beast: bụi cây có hoa | — |
| `nature-leech-3d` | `nature-leecher` · Meshy | 31.243 → 6.000 | 2×1,91×0,99 | beast: bạch tuộc rễ, miệng tròn (gốc `nature-leecher`) | DH boss nhỏ Hắc Hóa họ rễ (M) |
| `nature-mine-3d` | `nature-mine` · Meshy | 29.558 → 6.000 | 1,98×1,86×1,27 | mine: quả gai phát sáng | DH E32 `spore-bloater` hoặc Bom Hạt Thông của địch (S–M) |
| `nature-oppressor-3d` | `nature-oppressor` · Meshy | 31.156 → 6.000 | 1,33×2×1,31 | totem: mắt vàng trong vòng dây leo | DH B02 `moss-chieftain`: cột tô tem (S) |
| `nature-scout-3d` | `nature-scout` · Meshy | 30.489 → 6.000; LOD `nature-scout-lod` 1.000 | 1,77×2×0,4 | craft: phi tiêu lá | — |
| `nature-shield-3d` | `nature-shield` · Meshy | 29.827 → 6.000 | 2,01×1,8×1,3 | beast: khúc gỗ cuộn như mai | DH quái khiên vỏ cây, ngoài roster (M) |
| `nature-sniper-3d` | `nature-sniper` · Meshy | 30.216 → 6.000 | 1,64×2,03×0,65 | totem: hoa mắt trên cuống | DH cây mắt của boss B11 (S) |
| `nature-splitter-3d` | `nature-splitter` · Meshy | 30.533 → 6.000 | 2×1,83×0,51 | blob: khối rêu có hai hạt | DH E26 `puffball`: wash nâu nhạt, nhún bằng shader (S–M) |
| `nature-tank-3d` | `nature-tank` · Meshy | 31.342 → 6.000 | 1,8×2×0,5 | craft: phi tiêu lá (2D trùng scout) | — |

**Họ prism** (craft pha lê ánh tím lam). 2D: `art-src/enemies/<gốc>.png`.

| id (High) | Gốc `art-src/3d/enemies/` | Tam giác gốc → High | Khung High (x×y×z, đv) | Loại: dáng | Dùng cho game khác |
|---|---|---|---|---|---|
| `prism-carrier-3d` | `prism-carrier` · Meshy | 31.485 → 6.000 | 2×1,41×1,34 | craft: tàu mẹ pha lê | — |
| `prism-cloaker-3d` | `prism-cloaker` · Meshy | 31.576 → 6.000 | 2×1,87×1,1 | craft: cánh pha lê | — |
| `prism-commander-3d` | `prism-commander` · Meshy | 30.848 → 6.000 | 1,92×2×0,59 | craft: soái hạm pha lê | — |
| `prism-destroyer-3d` | `prism-destroyer` · Meshy | 31.324 → 6.000 | 1,83×2×1,34 | beast: pha lê dáng nhện chân móc | LL Crystal Crawler: đổi màu (M) |
| `prism-healer-3d` | `prism-healer` · Meshy | 29.119 → 6.000 | 2×1,99×0,95 | flyer (sứa): sứa pha lê | — |
| `prism-jammer-3d` | `prism-jammer` · Meshy | 29.402 → 5.999 | 1,8×2×1,34 | beast: cua pha lê ăng-ten | — |
| `prism-leech-3d` | `prism-leech` · Meshy | 28.795 → 5.999 | 1,27×0,77×2 | beast: bọ cạp pha lê cuộn | — |
| `prism-mine-3d` | `prism-mine` · Meshy | 29.520 → 6.000 | 2×1,99×2 | mine: sao pha lê | — |
| `prism-oppressor-3d` | `prism-oppressor` · Meshy | 28.024 → 6.000 | 1,21×2×0,77 | totem: tháp pha lê có vòng | — |
| `prism-scout-3d` | `prism-scout` · Meshy | 30.846 → 6.000; LOD `prism-scout-lod` 1.008 | 2×1,89×0,36 | craft: phi tiêu pha lê | — |
| `prism-shield-3d` | `prism-shield` · Meshy | 30.491 → 6.000 | 1,47×2,01×0,78 | craft: khiên pha lê | — |
| `prism-sniper-3d` | `prism-sniper` · Meshy | 29.266 → 6.000 | 1,62×2×0,32 | craft: giáo pha lê | — |
| `prism-splitter-3d` | `prism-healer` (tạm) · Meshy | 29.119 → 6.000 | 2×1,99×0,95 | craft: (tạm: lưới của healer) | — |
| `prism-tank-3d` | `prism-tank` · Meshy | 28.695 → 6.000 | 2×1,73×1,57 | mech: xe pha lê nặng | — |

**Họ rainbow** (pastel ánh xà cừ; 5 model đang ở Last Line). 2D: `art-src/enemies/<gốc>.png`.

| id (High) | Gốc `art-src/3d/enemies/` | Tam giác gốc → High | Khung High (x×y×z, đv) | Loại: dáng | Dùng cho game khác |
|---|---|---|---|---|---|
| `rainbow-carrier-3d` | `rainbow-carrier` · Meshy | 31.396 → 6.000 | 1,99×1,46×1,72 | craft: tàu mẹ xà cừ | — |
| `rainbow-cloaker-3d` | `rainbow-commander` (tạm) · Meshy | 31.131 → 5.999 | 2×1,68×1,03 | craft: (tạm: lưới của commander) | — |
| `rainbow-commander-3d` | `rainbow-commander` · Meshy | 31.131 → 5.999 | 2×1,68×1,03 | craft: soái hạm xà cừ | — |
| `rainbow-destroyer-3d` | `rainbow-shield` (tạm) · Meshy | 31.367 → 5.999 | 1,65×1,99×1,4 | craft: (tạm: lưới của shield) | — |
| `rainbow-healer-3d` | `rainbow-healer` · Meshy | 31.561 → 6.000 | 1,91×2,01×0,95 | flyer (sứa): sứa xà cừ | — |
| `rainbow-jammer-3d` | `rainbow-jammer` · Meshy | 30.847 → 6.000 | 2×1,67×1,49 | beast: cua xà cừ ăng-ten | — |
| `rainbow-leech-3d` | `rainbow-leech` · Meshy | 30.465 → 6.000 | 2,01×1,86×1,36 | beast: bạch tuộc miệng tròn | — |
| `rainbow-mine-3d` | `rainbow-mine` · Meshy | 29.608 → 6.000; LOD `rainbow-mine-lod` 1.000 | 1,99×2×1,31 | mine: cầu gai xà cừ | đang ở LL |
| `rainbow-oppressor-3d` | `rainbow-oppressor` · Meshy | 30.597 → 5.999 | 1,47×1,99×1,03 | totem: tháp có vòng | — |
| `rainbow-scout-3d` | `rainbow-tank` · Tripo | 5.782 → 5.782; LOD `rainbow-scout-lod` 1.000 | 2×1,87×1,32 | insect flyer: côn trùng bay tím lam (lưới của tank) | đang ở LL |
| `rainbow-shield-3d` | `rainbow-shield` · Meshy | 31.367 → 5.999 | 1,65×1,99×1,4 | craft: khiên xà cừ | đang ở LL |
| `rainbow-sniper-3d` | `rainbow-sniper` · Meshy | 30.750 → 5.999 | 1×1,14×2 | craft: trượng dài | — |
| `rainbow-splitter-3d` | `rainbow-splitter` · Meshy | 31.328 → 6.000 | 2×1,81×1,22 | blob: hai bong bóng | đang ở LL |
| `rainbow-tank-3d` | `rainbow-tank` · Tripo | 5.782 → 5.782 | 2×1,87×1,32 | insect flyer: côn trùng bay tím lam (Tripo 5,8k) | đang ở LL; DH biến thể Ong Sấm của E01 (M) |

**Họ shadow** (bóng lửa tím (Tripo); spirit, undead). 2D: `art-src/enemies/<gốc>.png`.

Họ này làm trên Tripo, mặt quay +X (Meshy quay mặt trước). Lúc nhập 21/10, việc ghép 3D với 2D ở họ này kém chắc nhất. Theo ghi chú nhập, `cloaker` là dáng rồng, `tank` là quỷ, `splitter` là xoáy năng lượng, `shield` là chiến binh giáp. Cột Loại ở đây tả theo ảnh 2D, nên xem render 3D trước khi chọn.

| id (High) | Gốc `art-src/3d/enemies/` | Tam giác gốc → High | Khung High (x×y×z, đv) | Loại: dáng | Dùng cho game khác |
|---|---|---|---|---|---|
| `shadow-carrier-3d` | `shadow-carrier` · Tripo | 28.586 → 6.000 | 2×1,66×2 | craft: tàu gai bóng | LL Void variant (S) |
| `shadow-cloaker-3d` | `shadow-cloaker` · Tripo | 29.486 → 6.000 | 2,01×1,65×1,08 | spirit: bóng lưỡi liềm | DH E05 `mist-wraith`: wash xám tím (S) |
| `shadow-commander-3d` | `shadow-commander` · Tripo | 29.008 → 5.999 | 2×1,91×1,16 | humanoid spirit: chúa bóng đội vương miện, áo choàng | DH G12 `mist-hierophant` (S–M) |
| `shadow-destroyer-3d` | `shadow-cloaker` (tạm) · Tripo | 29.486 → 6.000 | 2,01×1,65×1,08 | spirit: (tạm: lưới của cloaker) | theo cloaker |
| `shadow-healer-3d` | `shadow-healer` · Tripo | 29.844 → 5.999 | 1,99×1,94×1,2 | humanoid spirit: pháp sư bóng có hào quang, cầu sáng | DH E15 `mist-shaman` hoặc G05 `mist-elder` (S–M) |
| `shadow-jammer-3d` | `shadow-jammer` · Tripo | 28.192 → 6.000 | 1,92×2,01×0,98 | spirit: bóng mang cầu và vòng | DH E16 `hex-witch` (M) |
| `shadow-leech-3d` | `shadow-leech` · Tripo | 28.608 → 6.000 | 2,01×2×1,81 | beast spirit: thú bóng có vuốt | DH E23 `shadow-lynx` (M) |
| `shadow-mine-3d` | `shadow-mine` · Tripo | 28.692 → 6.000 | 1,99×2×1,12 | spirit orb: cầu lửa tím | WW `ma-troi` Ghost Flame: lõi + VFX lửa lạnh (M); LL Void Mine (S) |
| `shadow-oppressor-3d` | `shadow-oppressor` · Tripo | 29.462 → 6.000 | 1,76×2×1,42 | totem: tháp bóng có vòng | LL (S) |
| `shadow-scout-3d` | `shadow-scout` · Tripo | 28.369 → 6.000; LOD `shadow-scout-lod` 1.000 | 1,96×1,93×1,99 | beast spirit: thú bóng vuốt dài | DH biến thể Linh Miêu Đêm (M) |
| `shadow-shield-3d` | `shadow-shield` · Tripo | 28.600 → 6.000 | 1,99×1,93×1,17 | humanoid spirit: bóng trùm đầu cầm khiên | LL Void Shield (S) |
| `shadow-sniper-3d` | `shadow-sniper` · Tripo | 28.900 → 6.000 | 1,92×2×0,89 | humanoid spirit: bóng cầm giáo dài | LL (S) |
| `shadow-splitter-3d` | `shadow-splitter` · Tripo | 29.656 → 6.000 | 2×1,93×0,48 | spirit: hai bóng xoắn | LL (S) |
| `shadow-tank-3d` | `shadow-tank` · Tripo | 28.328 → 6.000 | 2,01×1,95×0,87 | beast spirit: thú bóng nặng | LL (S) |

**Họ magma: 11 bản gốc chưa build, chưa có trong manifest** (đá dung nham nứt cam). 2D: `art-src/enemies/magma-<vai>.png`; `magma-tank` có ảnh 2D nhưng chưa có bản gốc 3D (`SOURCES.json` ghi lưới tạm `magma-shield`).

| Gốc `art-src/3d/enemies/` | Tam giác gốc | Map gốc | Khung gốc (đv) | Loại: dáng | Dùng cho game khác |
|---|---|---|---|---|---|
| `magma-carrier` · Meshy | 30.708 | B/N/MR 2048 | 0,96×0,86×0,55 | craft (đá dung nham): tàu mẹ đá dung nham | LL họ Accretion (lửa vành đĩa bồi tụ): build bản High 6.000 tam giác cho LL (M) |
| `magma-cloaker` · Meshy | 31.201 | B/N/MR 2048 | 0,96×0,69×0,62 | craft (đá dung nham): cánh xoáy dung nham | LL họ Accretion (lửa vành đĩa bồi tụ): build bản High 6.000 tam giác cho LL (M) |
| `magma-destroyer` · Meshy | 28.568 | B/N/MR 2048 | 0,78×0,51×0,95 | craft (đá dung nham): càng đá dung nham | LL họ Accretion (lửa vành đĩa bồi tụ): build bản High 6.000 tam giác cho LL (M) |
| `magma-healer` · Meshy | 30.283 | B/N/MR 2048 | 0,68×0,95×0,34 | craft (đá dung nham): sứa đá dung nham | LL họ Accretion (lửa vành đĩa bồi tụ): build bản High 6.000 tam giác cho LL (M) |
| `magma-jammer` · Meshy | 30.397 | B/N/MR 2048 | 0,91×0,95×0,48 | craft (đá dung nham): tàu ăng-ten dung nham | LL họ Accretion (lửa vành đĩa bồi tụ): build bản High 6.000 tam giác cho LL (M) |
| `magma-mine` · Meshy | 30.324 | B/N/MR 2048 | 0,95×0,92×0,83 | craft (đá dung nham): khối đá dung nham tròn | LL họ Accretion (lửa vành đĩa bồi tụ): build bản High 6.000 tam giác cho LL (M) |
| `magma-oppressor` · Meshy | 29.998 | B/N/MR 2048 | 0,74×0,95×0,74 | craft (đá dung nham): tháp đá có vòng | LL họ Accretion (lửa vành đĩa bồi tụ): build bản High 6.000 tam giác cho LL (M) |
| `magma-scout` · Meshy | 31.703 | B/N/MR 2048 | 0,93×0,41×0,95 | craft (đá dung nham): mảnh đá bay | LL họ Accretion (lửa vành đĩa bồi tụ): build bản High 6.000 tam giác cho LL (M) |
| `magma-shield` · Meshy | 31.196 | B/N/MR 2048 | 0,9×0,95×0,52 | craft (đá dung nham): khiên đá dung nham | LL họ Accretion (lửa vành đĩa bồi tụ): build bản High 6.000 tam giác cho LL (M) |
| `magma-sniper` · Meshy | 30.629 | B/N/MR 2048 | 0,95×0,95×0,19 | craft (đá dung nham): giáo đá dài | LL họ Accretion (lửa vành đĩa bồi tụ): build bản High 6.000 tam giác cho LL (M) |
| `magma-splitter` · Meshy | 30.850 | B/N/MR 2048 | 0,92×0,95×0,28 | craft (đá dung nham): khối đá nứt đôi | LL họ Accretion (lửa vành đĩa bồi tụ): build bản High 6.000 tam giác cho LL (M) |

### 2.4 Máy và drone chưa dùng (đáng giá cho Last Line)

Đây là bản gốc Tripo của mục tiêu đấu tay đôi (Duel). Chưa build cho Campaign 3D. Mỗi bản khoảng 28.000 tam giác, map B/N/MR 2048, khung 1 đv. 2D: `art-src/duel-targets/<id>.png`. Phong cách sci-fi công nghiệp, khối chắc, rất gần Last Line.

| Gốc `art-src/3d/duel-targets/` | Tam giác | Dáng | Dùng cho game khác |
|---|---:|---|---|
| `drone` | 28.326 | drone bốn chân đẩy, thép trắng xám, đèn lam | LL Drone thường (M: build 6.000 tam giác, xoay, cánh quạt bằng shader) |
| `lock-on` | 28.416 | mắt đỏ có vây | LL Sentry bắn tỉa, mắt đỏ báo ngắm (M) |
| `bomb` | 28.811 | cầu thép nứt cam | LL Bomb Drone tự nổ, hợp palette cam (M) |
| `black-hole` | 28.862 | hố đen có vành | LL cổng đẻ quái hay vật cảnh nhiệm vụ (M, VFX xoáy) |
| `gravity` | 29.255 | con quay tím | LL lõi tổ hay bẫy hút (M) |

Các mục tiêu Duel còn lại (`amplify`, `barrier`, `disrupt`, `energy`, `fate-crystal`, `laser`, `missile`, `railgun`, `reflect`, `repair`, `scan`, `shield`, `siege-lance`) là vật hay vũ khí, không phải quái. Chúng làm được bộ phận gắn từ của boss LL (nòng, khiên, lõi).

### 2.5 Tàu (không phải sinh vật, chỉ để tham khảo)

12 tàu người chơi (`ships/<id>.high.glb`): 12.000 tam giác, map B/N/MR/E 2048, clip node `Ship_Idle`. Last Line đã dùng `vanguard` cho người lái. Các tàu khác làm được phi đội Raider của địch bay cao ở LL: đổi màu sang đỏ cam (S). Phải giữ khác hẳn màu tàu người chơi.

## 3. Dragonhold (`games/dragon-hold`)

Manifest: `public/assets/dragon-hold/models/m0b/manifest.json`. Bản gốc Tripo: `art-src/3d/{enemies,generals,units}/`. Cách vẽ: `src/view/model-specs.ts`.

Không model nào có xương hay clip trong file. Game dựng xương lúc chạy bằng crowd-rig, theo dáng ghi ở cột Xương. Bản High đã cắt mạnh: chỉ còn map màu 1024, không normal map, roughness phẳng ([MODEL_QUALITY](MODEL_QUALITY.md) §1). Vì thế **tái dùng thì build lại từ bản gốc**, map B/N/MR 2048. Phong cách stylized kiểu Warcraft.

| id (vai DH) | File High | Tam giác gốc → High | Xương | Map gốc / High | Cao (m) | Loại: dáng | 2D | Điểm | Dùng cho game khác |
|---|---|---|---|---|---:|---|---|---|---|
| `moss-grunt` (E09 Moss Grunt) | `m0b/enemies/moss-grunt/moss-grunt.high.glb` | 5.708 → 2.848 | crowd-rig `biped` | B/N/MR 2048 / B 1024 | 1,56 | humanoid: yêu tinh lùn áo rêu, dao đá | `art-src/enemies/moss-grunt.png` | 9 | — (không hợp WW hay LL) |
| `moss-archer` (E11 Moss Archer) | `m0b/enemies/moss-archer/…high.glb` | 5.903 → 3.471 | `biped` | như trên | 1,64 | humanoid: yêu tinh rêu cầm cung | `art-src/enemies/moss-archer.png` | 9 | — |
| `moss-banner` (G01 tướng) | `m0b/enemies/moss-banner/…high.glb` | 8.382 → 4.325 | `biped` (có cán cờ) | như trên | 2,40 | humanoid: yêu tinh rêu cầm cờ | `art-src/generals/moss-banner.png` | 9 | — |
| `blight-wolf` (E18 Blight Wolf) | `m0b/enemies/blight-wolf/…high.glb` | 5.637 → 2.560 | `quadruped` | như trên | 0,70 | beast: sói xám vân nứt lục | `art-src/enemies/blight-wolf.png` | 9,5 | WW Okuri-inu (sói đêm yêu quái Nhật): vẽ lại mực đen, mắt sáng (M) |
| `tusk-boar` (E19 Tusk Boar) | `m0b/enemies/tusk-boar/…high.glb` | 5.812 → 2.400 | `quadruped` | như trên | 0,90 | beast: lợn rừng nanh đá | `art-src/enemies/tusk-boar.png` | 9,5 | WW Boar Spirit (M); DH B01 `tuskfather` phóng to trong cùng game (S) |
| `thorn-wasp` (E01 Thorn Wasp) | `m0b/enemies/thorn-wasp/…high.glb` | 4.670 → 2.000 | `flyer` | như trên | 0,56 | insect: ong gai | `art-src/enemies/thorn-wasp.png` | 7,5 (tạm) | LL bio-drone bay: vẽ lại vỏ kim loại (M); DH B03 `thorn-queen` phóng to (S–M) |
| `thorn-ant` (E25 Thorn Ant) | `m0b/enemies/thorn-ant/…high.glb` | 3.744 → 1.707 | `hexapod` | như trên | 0,36 | insect: kiến gai | `art-src/enemies/thorn-ant.png` | 9,5 | LL Horde Crawler: vỏ đen, vân cam phát sáng (M); DH G04 `ant-matron` phóng to, bụng phồng (M) |
| `moss-warden` (lính phe ta) | `m0b/units/moss-warden/…high.glb` | 5.555 → 2.399 | `biped` | như trên | 1,60 | humanoid: người gỗ rêu cầm khiên | `art-src/units/moss-warden.png` | 8 (tạm) | — |
| `draconis-v2`, `draconis-v3`, `guides/draconis-v4` | `heroes/…`, `guides/…` | xem 2.1 | 25 / 32 / 25 xương | B/N/MR/E 2048 | — | bản chép byte của Space (md5 trùng) | — | — | — |

## 4. Wordwoven (`games/typing-defense`)

Manifest: `public/assets/typing-defense/models/manifest.json`. Bản gốc Tripo: `art-src/3d/`. Bản đã rig: `art-src/models/`. Rig Mesh2Motion: `art-src/anim/mesh2motion/`. Phong cách stylized chibi, kiểu đồ chơi, màu ấm. Boss và hero cỡ người thật hơn.

### 4.1 Đã ship (đều có xương và clip)

| id (tên EN) | File High | Tam giác gốc → High | Xương · clip | Map High | Cao (m) | Loại: dáng | 2D | Dùng cho game khác |
|---|---|---|---|---|---:|---|---|---|
| `cuong-thi` (Hopping Zombie) | `enemies/cuong-thi/cuong-thi.high.glb` | 5.813 → 5.813 | 28 · Enemy_Idle, Move, Attack, Hit, Death | B/N/MR 1024 | 1,70 | undead humanoid: cương thi mũ quan, bùa | `art-src/enemies/cuong-thi.png`; chân dung `portraits/enemies/hopping-zombie` | — |
| `mam-go` (Sapling) | `enemies/mam-go/…high.glb` | 5.840 → 5.840 | 28 · Enemy_Idle, Move, Attack, Hit, Death | B/N/MR 1024 | 1,60 | plant: mầm gỗ hai lá | `art-src/enemies/mam-go.png`; `portraits/enemies/sapling` | DH mầm của B11 `rotwood-ancient` hay bầy rêu: wash vân tím mục (S–M) |
| `nuppeppo` (Split Blob) | `enemies/nuppeppo/…high.glb` | 5.910 → 5.910 | 9 · Enemy_Idle, Move, Attack, Hit, Death, Death.split | B/N/MR 1024 | 2,00 | blob: khối thịt kem | `art-src/enemies/nuppeppo.png`; `portraits/enemies/split-blob` | DH E26 `puffball` hoặc B12 `spore-mother`: gắn mũ nấm, vẽ lại da nấm; clip chết tách đôi khớp luật (M) |
| `tanuki` (Raccoon Dog) | `enemies/tanuki/…high.glb` | 5.696 → 5.696 | 28 · Enemy_Idle, Move, Attack, Hit, Death, Skill | B/N/MR 1024 | 1,80 | beast hai chân: lửng chó, bụng trống | `art-src/enemies/tanuki.png`; `portraits/enemies/raccoon-dog` | DH E22 `tunnel-badger`: vẽ sọc lửng, bỏ lá trên đầu (M) |
| `thuong-luong` (River Serpent) | `enemies/thuong-luong/…high.glb` | 5.652 → 5.652 | 28 (đầu, râu, 20 đốt đuôi, túi, miệng) · Enemy_Idle, Move, Attack, Hit, Skill, Death | B/N/MR 1024 | 2,40 (dài 5,26) | serpent: thuồng luồng vảy lam | `art-src/enemies/thuong-luong.png`; `portraits/enemies/river-serpent` | DH E30 `river-eel` (thu 0,4×) và B15 `river-serpent` (phóng 1,5×): wash lục rêu nước (S–M) |
| `troll` (Troll) | `enemies/troll/…high.glb` | 11.720 → 9.000 | 25 (khung người, có váy) · Enemy_Idle, Move, Attack, Hit, Death, Skill | B/N/MR 1024 | 4,00 | humanoid brute: quỷ núi da đá phủ rêu | `art-src/enemies/troll.png`; `portraits/enemies/troll` | **DH E12 `forest-ogre`** hay G07 `drum-ogre` (thêm trống), E17 `stone-golem` (wash đá): cỡ 2,6–3,2 m (S–M) |
| `lam` (Lam, hero) | `heroes/lam/lam.high.glb` | 22.906 → 20.000 | 31 · Hero_Idle, Run, Attack, Skill1, Skill2, Ult, Assist, Hit, Death, Respawn, Victory, Idle_Fidget, Dash | B/N/MR 2048 | 2,70 | humanoid: mèo lửa Hỏa Miêu | `art-src/heroes/lam.png` | — (làm khung mẫu rig người cho model khác) |
| `linh-giao` (Spearman) | `units/linh-giao/…high.glb` | 4.772 (thân) + 2.852 (giáo) → 6.772 | 24 · Unit_Idle, Walk, Attack, Idle.guard, Hit, Death, Cheer, Charge | B/N/MR 1024 | 2,20 | humanoid: lính giáo nón lá | `art-src/units/linh-giao.png` | — |

### 4.2 Bản gốc chưa ship (Tripo, chưa rig trừ cú; map B/N/MR 2048; khung chuẩn hoá 1 đv)

| Gốc `art-src/3d/` | Tam giác | Vai WW (thiết kế) | Loại: dáng | 2D | Dùng cho game khác |
|---|---:|---|---|---|---|
| `enemies/alicanto` | 5.710 | Golden Alicanto, trộm vàng (1B) | flyer: chim vàng cánh lửa | `art-src/enemies/alicanto.png` | **DH E04 `crow-thief`** (cùng vai trộm): vẽ lại lông đen, rig chim Mesh2Motion (M) |
| `enemies/dokkaebi` (+ `dokkaebi-club` 2.944) | 5.730 | Dokkaebi, gọi Ma Trơi (VS) | humanoid: yêu tinh tóc rối | `art-src/enemies/dokkaebi.png` | DH E10 `moss-runner` hay E14 `moss-sapper`: phủ rêu, mặt nạ vỏ cây (M–L, lệch phong cách) |
| `enemies/kamaitachi` | 5.873 | Kamaitachi, bay thấp né đạn (VS) | beast: chồn đuôi dài | `art-src/enemies/kamaitachi.png` | DH E23 `shadow-lynx` (gượng): lông chàm, mắt vàng úa (M) |
| `enemies/ma-da` | 5.756 | Ma Da, tàng hình (VS) | spirit humanoid: thiếu nữ ma nước | `art-src/enemies/ma-da.png` | — (chibi, không hợp DH) |
| `enemies/oni` (+ `oni-club` 2.780) | 8.522 | Oni, phá nhà (VS) | humanoid brute: quỷ đỏ cầm chùy | `art-src/enemies/oni.png` | DH G07 `drum-ogre` hay E12: da lục rêu, thêm trống (M) |
| `enemies/tat-phuong` | 5.988 | Tất Phương (Bifang), tự nổ (VS) | flyer: hạc một chân | `art-src/enemies/tat-phuong.png` | — |
| `enemies/cuong-thi-lead-hat` | 2.827 | mũ của Zombie Leader | vật gắn | `art-src/enemies/cuong-thi-lead-hat.png` | — (đã ship ở `attachments/`) |
| `bosses/dai-bang-tinh` | 34.927 | Storm Eagle, boss bay (VS) | flyer: đại bàng | `art-src/bosses/dai-bang-tinh.png` | DH E06 `hawk-carrier` (thu 0,5×, lông khói) hay G08 `crow-captain`: rig chim (M) |
| `bosses/moc-tinh` | 29.177 | Mộc Tinh, the Nameless Banyan, boss (1B/VS) | plant giant: cây đa thành người | `art-src/bosses/moc-tinh.png` | **DH B11 `rotwood-ancient`**: build một lần cho cả hai game, hai bộ texture (đa xanh cho WW, gỗ mục cho DH); rig người (M–L) |
| `heroes/draconis` (của WW) | 33.566 | Draconis, hero WW | rồng hai chân, cánh lông vũ | `art-src/heroes/draconis.png` | — (đề xuất ngược: WW dùng `draconis-v4` của Space, mục 6) |
| `heroes/tre` (+ `tre-mallet`, `tre-slingshot`) | 23.546 | Tre, hero | humanoid: cậu bé | `art-src/heroes/tre.png` | — |
| `units/linh-khien` (+ `linh-khien-shield` 2.830) | 4.792 | lính khiên | humanoid | `art-src/units/linh-khien.png` | khiên `linh-khien-shield` làm khiên gỗ cho DH E13 `moss-shieldbearer` (S–M) |
| `units/linh-giao-dai` (+ giáo 1.906) | 4.720 | lính giáo dài | humanoid | `art-src/units/linh-giao-dai.png` | — |
| `workers/worker-base` (+ 24 món kit) | 4.682 | thợ làng | humanoid | `art-src/workers/worker-base.png` | — |
| `helpers/helper-owlet` | 9.654 (bản rig `art-src/models/helpers/helper-owlet.glb`: 8.000, 25 xương, 13 clip Helper_Idle, Walk, Walk.carry, Assist ×5, Cheer, Catch, Scared, Hit, Intro) | trợ thủ cú | flyer nhỏ: cú non đeo túi | `art-src/helpers/helper-owlet.png` | DH E08 `owl-seer`: gỡ túi và bảng (sửa lưới), mắt tím (L) |
| `animals/trau` | 5.982 | trâu ruộng | beast: trâu nước | `art-src/animals/trau.png` | — |
| `animals/piggy` | 5.888 | heo đất (vật) | vật: heo đất hoa | `art-src/animals/piggy.png` | — |
| `animals/chuon-chuon-tre` | 2.872 | chuồn chuồn tre (đồ chơi) | vật | `art-src/animals/chuon-chuon-tre.png` | — |

Khác: `tripo-spares/lam.tripo-skeleton.glb` (22.906 tam giác, 54 xương Tripo, không clip) là bản Lam rig tự động của Tripo, để dự phòng.

## 5. Last Line (`games/typing-survival`)

Manifest: `public/assets/typing-survival/models/manifest.json`. `art-src/3d/SOURCES.json` rỗng, vì game chưa có bản gốc riêng. Mọi model là bản chép byte từ Space (md5 trùng). Model nạp vào bầy instanced qua `src/view/models.ts`.

| id | Nguồn | Tam giác High | Xương · clip | Map High | Khung (đv) | Loại: dáng | Vai hiện tại | Nhận xét |
|---|---|---:|---|---|---|---|---|---|
| `rainbow-mine-3d` | ST `enemies/rainbow-mine` | 6.000 | không · Enemy_Idle | B/N/MR/E 1024 | 1,99×2×1,31 | mine: cầu gai xà cừ | bầy | Tông pastel lệch palette LL (thép than, cam nóng, lam điện) |
| `rainbow-scout-3d` | ST `rainbow-tank` (chung lưới) | 5.782 | như trên | như trên | 2×1,87×1,32 | insect flyer | bầy | Hợp chủ đề sinh vật |
| `rainbow-tank-3d` | ST `rainbow-tank` | 5.782 | như trên | như trên | 2×1,87×1,32 | insect flyer | bầy (bản to) | như trên |
| `rainbow-shield-3d` | ST `rainbow-shield` | 5.999 | như trên | như trên | 1,65×1,99×1,4 | craft: khiên xà cừ | bầy | lệch tông |
| `rainbow-splitter-3d` | ST `rainbow-splitter` | 6.000 | như trên | như trên | 2×1,81×1,22 | blob: hai bong bóng | bầy (×2 suất) | lệch tông |
| `draconis-v3` | ST `heroes/draconis-v3` | 60.000 | 32 · 10 clip Hero_* | B/N/MR/E 2048 | 4,11×2×2,77 | rồng cánh lớn | người lái (Draconis) | — |

Đề xuất cho Last Line: giữ `rainbow-tank` và `rainbow-scout` (côn trùng). Thêm họ `cosmic`, rồi `magma` và drone đấu tay đôi làm quân chính. Xem mục 6.

## 6. Bảng tái dùng chéo game

Sắp theo game đích. Cột "Công" theo thang S/M/L ở mục 1. "Nguồn build" là file mà game đích phải dùng để build bản của mình.

### 6.1 Cho Last Line (Black Hole Horde, sinh vật và drone trên trạm)

| # | Ứng viên (game nguồn) | Nguồn build | Vai ở LL | Thay đổi cần | Công |
|---|---|---|---|---|---|
| L1 | Họ `cosmic`, 14 model (ST) | `space-typing/art-src/3d/enemies/cosmic-*.glb` | Quân chính: `cosmic-leecher`/`cosmic-beast` là Crawler và Splitter; `cosmic-fast`/`cosmic-grunt` là bầy nhanh (đã có LOD 999 cho scout); `cosmic-elite` là Elite Stalker; `cosmic-sniper` là Sniper; `cosmic-sorcerer` là Void Priest hồi máu; `cosmic-shield` là Shield Bearer; `cosmic-tank`/`cosmic-dreadnought` là quân nặng; `cosmic-core` là lõi tổ | Chép gốc sang LL, build High 6.000 kèm LOD ~1.000 vào manifest LL như `rainbow-*`; nghiêng màu theo palette LL bằng shader; lướt và nghiêng bằng code (rigid) | S |
| L2 | Họ `magma`, 11 bản gốc chưa build (ST) | `space-typing/art-src/3d/enemies/magma-*.glb` | Họ Accretion, chương có vành lửa | Build lần đầu (preset, `rotate` theo 2D, 6.000 tam giác, giữ N/MR), emissive cam; thiếu `magma-tank` | M |
| L3 | `drone`, `lock-on`, `bomb` (ST, mục tiêu Duel) | `space-typing/art-src/3d/duel-targets/` | Drone thường, Sentry bắn tỉa, Bomb Drone tự nổ | Build, xoay, thêm socket `FX_MUZZLE`/`FX_CORE`, cánh quạt và đèn báo bằng shader | M |
| L4 | `tyrant-g05`, `warden-shadow` (ST boss) | `art-src/3d/bosses/` của ST | Boss chương Black Hole Herald | Chép, đổi tông tím về đen và cam vành đĩa; muốn phá theo bộ phận thì tách lưới mắt và vai | S (M nếu tách bộ phận) |
| L5 | `tyrant-g06`, `lieutenant-cosmic` (ST boss) | như trên | Boss Iron Colossus, Station Golem | Chép; lõi cam sẵn hợp palette; bộ phận gắn từ: thêm socket hoặc tách lưới | S–M |
| L6 | `tyrant-g02`, `lieutenant-devil`, `warden-devil`, `tyrant-g07` (ST boss) | như trên | Boss họ Furnace | Chép, hạ đỏ về cam | S |
| L7 | Họ `devil` và `shadow` (ST, 28 mục) | `art-src/3d/enemies/` của ST | Biến thể Furnace (cam) và Void (tím) ở chương sau | Chép, nghiêng màu | S |
| L8 | `black-hole`, `gravity` (ST, mục tiêu Duel) | `art-src/3d/duel-targets/` | Cổng đẻ quái, lõi tổ, mục tiêu "phá tổ" | Build; VFX xoáy theo VFX_STANDARD | M |
| L9 | `thorn-ant` (DH) | `dragon-hold/art-src/3d/enemies/thorn-ant.glb` (3.744 tam giác, không dùng bản ship 1.707) | Horde Crawler cỡ nhỏ | Vẽ lại vỏ đen, vân cam phát sáng; crowd-rig `hexapod` là code của DH, LL phải port hoặc chỉ lắc rigid | M |
| L10 | `thorn-wasp` (DH) | `dragon-hold/art-src/3d/enemies/thorn-wasp.glb` | Bio-drone bay | Vẽ lại vỏ kim loại; cánh bằng shader | M |
| L11 | `angel-tank`, `prism-destroyer` (ST) | `art-src/3d/enemies/` của ST | Heavy Walker, Crystal Crawler | Tắt halo, vẽ lại sang thép | M |
| L12 | 11 tàu người chơi trừ `vanguard` (ST) | `space-typing/public/…/ships/` hoặc bản gốc `art-src/3d/ships/` | Phi đội Raider của địch bay cao | Đổi màu sang đỏ cam của địch | S |

### 6.2 Cho Dragonhold (đàn rêu và mục rữa, đèo núi fantasy)

| # | Ứng viên (game nguồn) | Nguồn build | Vai ở DH | Thay đổi cần | Công |
|---|---|---|---|---|---|
| D1 | `troll` (WW, rig 25 xương, 6 clip) | `typing-defense/art-src/models/enemies/troll.glb` (bản rig) hoặc `art-src/3d/enemies/troll.glb` (gốc) | E12 `forest-ogre`; G07 `drum-ogre` (thêm trống); E17 `stone-golem` (wash đá) | Wash rêu 0,3; cỡ 2,6–3,2 m; DH vẽ quái bằng crowd-rig nên dùng gốc kèm marks `biped`, hoặc thêm đường vẽ model có xương sẵn | S–M |
| D2 | `thuong-luong` (WW, rig 28 xương) | `typing-defense/art-src/models/enemies/thuong-luong.glb` | E30 `river-eel` (0,4×) và B15 `river-serpent` (1,5×, trùng tên) | Wash lục nước; DH chưa có dáng rắn trong crowd-rig: dùng clip có sẵn hoặc thêm dáng `serpent` | S–M |
| D3 | `lieutenant-nature` (ST boss) | `space-typing/art-src/3d/bosses/lieutenant-nature.glb` | B13 `storm-beetle` (thiết kế DH đã chọn); E27 `acid-beetle` thu nhỏ | Build High ≥ 20.000 cho boss; rig `flyer`/`hexapod`; vân điện là VFX | M |
| D4 | `draconis-v3` (ST) | `dragon-hold/public/…/heroes/draconis-v3` (đã có trong DH) | B19 `black-wyrm` (thiết kế DH đã chọn) | Đổi vật liệu đen; rig 32 xương và clip `Hero_Spit` có sẵn | M |
| D5 | Họ `shadow` (ST, Tripo) | `space-typing/art-src/3d/enemies/shadow-*.glb` | `cloaker` → E05 `mist-wraith`; `commander` → G12 `mist-hierophant`; `healer` → E15 `mist-shaman` hay G05 `mist-elder`; `jammer` → E16 `hex-witch`; `leech`/`scout` → E23 `shadow-lynx` và biến thể Linh Miêu Đêm | Wash Hắc Vụ xám tím 0,4–0,6 trong `model-specs.ts`; crowd-rig `flyer` hoặc `biped`; khói là VFX | S–M |
| D6 | `nature-boss` (gốc của `nature-commander-3d`, ST) | `space-typing/art-src/3d/enemies/nature-boss.glb` | G10 `thorn-matron` | Wash gai; crowd-rig `biped`; cánh lá rung bằng shader | M |
| D7 | `nature-splitter` (ST) | `art-src/3d/enemies/nature-splitter.glb` của ST | E26 `puffball` (cùng vai splitter) | Wash nâu nhạt; nhún và tách bằng code | S |
| D8 | `nuppeppo` (WW, rig, có `Enemy_Death.split`) | `typing-defense/art-src/models/enemies/nuppeppo.glb` | E26 `puffball` (phương án đẹp hơn D7) hoặc B12 `spore-mother` | Gắn mũ nấm (lưới mới nhỏ), vẽ lại da nấm | M |
| D9 | `nature-mine`, `nature-oppressor`, `nature-sniper` (ST) | `art-src/3d/enemies/` của ST | E32 `spore-bloater`; cột tô tem của B02 `moss-chieftain`; cây mắt của B11 | Wash; vật bất động hoặc nhún | S–M |
| D10 | `moc-tinh` (WW, gốc 29.177) | `typing-defense/art-src/3d/bosses/moc-tinh.glb` | B11 `rotwood-ancient` | Build một lần cho cả WW và DH, hai bộ texture; rig người Mesh2Motion hoặc crowd-rig `biped` | M–L |
| D11 | `alicanto` (WW, gốc) | `typing-defense/art-src/3d/enemies/alicanto.glb` | E04 `crow-thief` (cùng vai trộm) | Vẽ lại lông đen, mắt vàng; rig chim Mesh2Motion (`Flap`, `Glide`) | M |
| D12 | `tanuki` (WW, rig) | `typing-defense/art-src/models/enemies/tanuki.glb` | E22 `tunnel-badger` | Vẽ sọc lửng, bỏ lá; giữ clip | M |
| D13 | `dai-bang-tinh` (WW, gốc 34.927) | `typing-defense/art-src/3d/bosses/dai-bang-tinh.glb` | E06 `hawk-carrier` (0,5×), G08 `crow-captain`, G13 `storm-harpy` (gượng) | Lông khói, rig chim; bản quái thường build 6.000–8.000 | M |
| D14 | `oni` + `oni-club` (WW, gốc) | `typing-defense/art-src/3d/enemies/oni.glb` | G07 `drum-ogre` (phương án 2 của D1) | Da lục rêu, thêm trống; rig người | M |
| D15 | `tyrant-g04`, `warden-nature` (ST boss) | `art-src/3d/bosses/` của ST | B11 (phương án 2 của D10); B02 `moss-chieftain`; G14 `stone-marshal`; G09 `thorn-warlord` (phần người cưỡi) | Wash rêu, bớt emissive; rig `biped` | M |
| D16 | `tyrant-g08`, `tyrant-g10`, `tyrant-g05`, `warden-shadow`, `lieutenant-shadow`, `tyrant-g09` (ST boss) | `art-src/3d/bosses/` của ST | G12 `mist-hierophant`; G05 `mist-elder`; B20 `mist-mother`; B14 `mist-knight` (thiếu ngựa) | Wash Hắc Vụ; giữ chi tiết cao vì là boss | M |
| D17 | `cosmic-sorcerer` (ST) | `art-src/3d/enemies/cosmic-sorcerer.glb` | E15 `mist-shaman` (phương án 2 của D5) | Wash xám lục | M |
| D18 | `mam-go` (WW, rig) | `typing-defense/art-src/models/enemies/mam-go.glb` | Mầm do B11 gọi; bầy rêu | Wash vân tím mục | S–M |
| D19 | `kamaitachi` (WW, gốc) | `typing-defense/art-src/3d/enemies/kamaitachi.glb` | E23 `shadow-lynx` (gượng) | Lông chàm; rig `quadruped` | M |
| D20 | `linh-khien-shield` (WW, gốc) | `typing-defense/art-src/3d/units/linh-khien-shield.glb` | Khiên của E13 `moss-shieldbearer` (gắn vào `moss-grunt`) | Vẽ lại gỗ rêu; gắn vào tay | S–M |
| D21 | `helper-owlet` (WW, rig) | `typing-defense/art-src/models/helpers/helper-owlet.glb` | E08 `owl-seer` | Gỡ túi và bảng (sửa lưới), mắt tím | L |

### 6.3 Cho Wordwoven (yêu quái và thú dân gian Đông Á, làng, đêm)

| # | Ứng viên (game nguồn) | Nguồn build | Vai ở WW | Thay đổi cần | Công |
|---|---|---|---|---|---|
| W1 | `draconis-v4` (+ clip của `draconis-v2`) (ST) | `space-typing/public/…/guides/draconis-v4` và `heroes/draconis-v2` | Hero Draconis | Dùng lưới v4 (trắng, cánh đỏ); clip Hero_* của v2 chạy thẳng vì cùng 25 xương cùng tên; vẽ lại cánh thành lông vũ kem viền cam; chủ dự án chọn giữa phương án này và rig bản gốc WW | S–M |
| W2 | `blight-wolf` (DH, gốc Tripo) | `dragon-hold/art-src/3d/enemies/blight-wolf.glb` | Okuri-inu, sói đêm theo người đi đường | Vẽ lại lông mực đen, mắt sáng; rig `quadruped` (port crowd-rig hoặc Mesh2Motion) | M |
| W3 | `tusk-boar` (DH, gốc Tripo) | `dragon-hold/art-src/3d/enemies/tusk-boar.glb` | Boar Spirit (heo rừng tinh) | Vẽ lại, thêm vân mực | M |
| W4 | `shadow-mine` (ST) | `space-typing/art-src/3d/enemies/shadow-mine.glb` | Lõi của `ma-troi` Ghost Flame | Đổi lửa tím sang lam lục lạnh; phần lớn hình là VFX | M |
| W5 | `warden-frost` (ST boss; `tyrant-g03` đang dùng chung) | `art-src/3d/bosses/warden-frost.glb` của ST | Snow Woman (Yuki-onna), boss Thế giới 2 | Đổi phong cách sang tông dân gian, bỏ gai pha lê; khó khớp chibi | L |
| W6 | `warden-devil` (ST boss) | `art-src/3d/bosses/warden-devil.glb` của ST | Oni King | Đổi phong cách, da đỏ, chùy | L |
| W7 | `warden-shadow` (ST boss) | như trên | Hình hiện của Mute Ink (boss cuối) | Vẽ lại thành mực đen; VFX mực | L |

### 6.4 Cho Space Typing

Không cần. Space là kho nguồn. 9 chỗ tạm (`rainbow-cloaker`, `rainbow-destroyer`, `devil-destroyer`, `frost-destroyer`, `frost-leech`, `prism-splitter`, `shadow-destroyer`, `magma-tank`, `tyrant-g03`) cần bản gốc đúng ảnh 2D. Model của game khác không khớp phong cách và ảnh 2D của các chỗ đó.

### 6.5 Mười lăm ứng viên nên làm trước

Xếp theo độ hợp chủ đề, công bỏ ra và chỗ trống được lấp.

| Hạng | Ứng viên → game đích, vai | Công | Vì sao |
|---:|---|---|---|
| 1 | Họ `cosmic` (14, ST) → LL, quân chính Black Hole Horde | S | 14 vai đủ loại, cùng một tông hư không; quy trình chép đã chạy với `rainbow-*` |
| 2 | `troll` (WW, đã rig) → DH E12 `forest-ogre` và G07 `drum-ogre` | S–M | Thân đá phủ rêu khớp họ rêu; đủ 6 clip |
| 3 | `thuong-luong` (WW, đã rig) → DH E30 `river-eel` và B15 `river-serpent` | S–M | Một model lấp một quái và một boss; khung xương rắn sẵn |
| 4 | `draconis-v4` + clip `draconis-v2` (ST) → WW hero Draconis | S–M | Khỏi rig bản 33.566 tam giác; clip đã qua duyệt ở Space và DH |
| 5 | `lieutenant-nature` (ST) → DH B13 `storm-beetle`, E27 `acid-beetle` | M | Thiết kế DH đã ghi model này; thêm một quái thường |
| 6 | Họ `shadow` (ST) → DH họ mist (E05, E15, E16, E23, G05, G12) | S–M | Năm vai sương chỉ cần chỉnh `wash` |
| 7 | `draconis-v3` (ST) → DH B19 `black-wyrm` | M | Đã có trong DH; chỉ đổi vật liệu |
| 8 | `drone`, `lock-on`, `bomb` (ST, chưa dùng) → LL drone | M | Đúng chất máy công nghiệp; 28.000 tam giác gốc, chưa game nào dùng |
| 9 | `tyrant-g05` hoặc `warden-shadow` (ST) → LL boss Black Hole Herald | S | Thực thể hư không có mắt, hợp hố đen |
| 10 | `tyrant-g06` hoặc `lieutenant-cosmic` (ST) → LL boss Iron Colossus | S–M | Lõi cam và giáp thép hợp palette LL |
| 11 | Họ `magma` (11 gốc chưa build, ST) → LL họ Accretion | M | Bản gốc 28.000–31.000 tam giác nằm không; tông cam vành đĩa |
| 12 | `nature-splitter` (ST) hoặc `nuppeppo` (WW) → DH E26 `puffball` | S / M | Cùng vai tách đôi; `nuppeppo` có sẵn clip chết tách |
| 13 | `moc-tinh` (WW) → DH B11 `rotwood-ancient` | M–L | WW cũng phải build: một lần rig, hai bộ texture |
| 14 | `alicanto` (WW) → DH E04 `crow-thief` | M | Cùng vai trộm; rig chim Mesh2Motion có sẵn |
| 15 | `nature-boss` (ST) → DH G10 `thorn-matron` | M | Nữ thần cây có cánh lá đúng dáng Mụ Gai |

Kế đó: `tanuki` → DH E22 (M), `dai-bang-tinh` → DH E06 (M), `blight-wolf` → WW Okuri-inu (M), `thorn-ant` → LL Crawler (M).

## 7. Chỗ trống: chưa model nào hợp

**Dragonhold** (vai trong thiết kế 02; "gượng" là có ứng viên nhưng yếu):
- Bay: E02 `bat-swarm` và B09 `night-bat-lord`; E03 `ember-moth`; E07 `veil-moth` (chỉ có `nature-cloaker` gượng).
- Bốn chân: E20 `toad-spitter` và B05 `bog-toad-king`; E21 `moss-stag`, G11 `elk-king` và B17 `frost-stag`; E24 `bramble-bear`; B10 `magma-salamander`.
- Bò: E28 `web-spider`, E31 `brood-spider`, G06 `web-weaver`, B06 `web-matriarch` (không có nhện nào); E29 `shell-crab` và B08 `tide-crab`; B18 `deep-centipede`.
- Hai chân: B07 `canyon-colossus` và người đá thật cho E17 (troll và `tyrant-g04` chỉ gượng); B16 `raven-sage`; G13 `storm-harpy` (`dai-bang-tinh` gượng); ngựa ma cho B14 `mist-knight`.

**Wordwoven:** Ghost Flame (`ma-troi`, `ma-troi-nho`) chưa có model nào. Nên làm chủ yếu bằng VFX theo [VFX_STANDARD](VFX_STANDARD.md), `shadow-mine` chỉ làm lõi. Các quái VS khác đã có bản gốc. Chúng chỉ chưa được rig (mục 4.2).

**Last Line:**
- Boss phá theo bộ phận (khiên, nòng, lõi gắn từ) cần lưới tách sẵn. Không model nào có. Phải tách trong Blender từ ứng viên L4 hoặc L5.
- Bầy 700–1.000 con cần LOD ≤ 1.000 tam giác cho mỗi họ mới. Hiện chỉ 10 mục có LOD.
- Chưa có quái bò kiểu nhện máy của trạm (`thorn-ant` và `prism-destroyer` chỉ gượng).

**Space Typing:** 9 chỗ tạm nêu ở 6.4.
