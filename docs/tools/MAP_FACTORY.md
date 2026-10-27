# Map Factory: đánh giá đề xuất và kế hoạch làm (27/10/2026)

**Đọc cho ai:** chủ dự án, và các agent làm bản đồ về sau.

**Nguồn:**
- Đề xuất của ChatGPT: `~/Downloads/application/AI_DRIVEN_3D_MAP_FACTORY_CLAUDE_REVIEW.md` (gọi tắt là "đề xuất"; số mục § theo file đó).
- Năm hướng nghiên cứu ngày 27/10/2026: TopoTopo, Blender, sinh thủ tục, asset và hiệu năng, nhu cầu của từng game. Đường dẫn nguồn ở cuối tài liệu.
- Ba ảnh trong `tmp/map-studio/`: ảnh mẫu `owner-reference-haven-grove.webp`, Lời Gọi hôm nay `now-loi-goi-2d.png`, Rồng Giữ Ải M0b `now-rong-giu-ai-m0b.png`.

**Trạng thái:** đã duyệt ngày 27/10/2026 (bản nháp lần 2, đã sửa theo một vòng phản biện độc lập). Giai đoạn 1 bắt đầu cùng ngày: spike bố cục và phiếu Codex 027–029.

## Tóm tắt

- **Kết luận: GO, có sửa.** Ý chính của đề xuất đúng: bản đồ là dữ liệu nguồn (spec + seed + sổ model), sinh tất định, có luật chơi, CLI trước. Phần sai là phần giữa: Blender dựng cả bản đồ, `map.glb`, `collision.glb`, `navmesh.json`, Blender MCP, WFC và các gói asset miễn phí.
- **Bản đồ xấu vì bố cục, không vì thiếu máy làm địa hình.** Ảnh mẫu đẹp nhờ đất mòn dưới gốc cây, lối mòn rẽ nhiều ngả, cây mọc thành lùm, ao, vách đá đóng khung, đèn và rào dọc đường. M0b của Rồng thiếu gần hết. Lời Gọi chưa có 3D.
- **Kiến trúc:** một lõi TypeScript thuần, số nguyên, nằm trong kit chung. Game gọi lõi lúc nạp (hoặc lúc build) để sinh bố cục từ spec, rồi tự dựng hình. Blender chỉ chuẩn bị từng model. Sim không bao giờ đọc mesh.
- **Làm gì trước:** 1–2 ngày Claude **thử bố cục** (spike) trên Rồng L2-cau, trong một worktree mới tách từ `m0b-models`, dùng sân khấu 3D và bộ pine-river sẵn có. Chấm cạnh ảnh mẫu ở 12 góc nhìn, ghi rõ cái gì giới hạn điểm. Kết quả spike thành phiếu cho Codex.
- **Lời Gọi bản đồ 1** (`w1-silverfall`) là mẫu CLI thứ hai, và là game thứ hai đưa vào khi bước 1C bắt đầu. Cảnh của nó theo thiết kế §23.10: billboard 2D từ bộ tranh `meadow` đã có, chỉ 3 mốc dựng Tripo.
- **Codex** nhận 7 phiếu nhỏ, kiểm được (027–033, mục 9.2). Ba phiếu đầu chạy song song với spike vì cần cho mọi kết quả. Bốn phiếu sau chờ spike.
- **Thời gian của chủ dự án:** khoảng 30 phút tới khi Rồng có bản đồ mới (xem ảnh, chơi thử). Thêm khoảng 1,5 giờ ở bước Lời Gọi 1C (3 mốc Tripo, chơi thử).

---

## 1. Đánh giá kỹ thuật

### 1.1 Vì sao bản đồ của ta xấu

Đặt ảnh mẫu Haven Grove cạnh M0b của Rồng và Lời Gọi 2D. Bảng dưới tách cái làm ảnh mẫu đẹp ra từng phần, rồi ghi lớp nào trong kiến trúc (mục 3) sinh ra phần đó.

| Cái làm ảnh mẫu đẹp | Lớp sinh | Rồng M0b hôm nay | Lời Gọi hôm nay |
|---|---|---|---|
| Đất mòn dưới gốc cây, quanh ngã ba; mép đường mềm | L7 sơn đất, theo trường khoảng cách | Một màu cỏ; mép đường gắt | Bản vẽ 2D gỡ lỗi: dải màu phẳng |
| Lối mòn rẽ nhiều ngả | L4 lối mòn trang trí | Chỉ 2 đường quái | Chỉ đường quái |
| Cây mọc thành lùm, nhiều sắc (đỏ, cam) | L6 thực vật theo cụm, đổi sắc từng cây | Rừng dồn ra mép; giữa đồng lốm đốm bụi đều | Chưa vẽ cảnh |
| Ao có lá súng, cầu nhỏ | L3 nước | Sông và cầu (đạt) | Suối thẳng một dải |
| Vách đá đóng khung một cạnh | L2 dấu vách; đá dọc chân vách | Không có | Không có |
| Đèn, rào, cọc dọc đường | L5 đồ dọc đường | Không có | Không có |
| Bãi trống rộng, có hoa cỏ nhỏ | Vùng trống có chủ ý; L7 decal hoa cỏ | Trống nhưng phẳng lì | Trống |

Nửa trên ảnh mẫu ("BEFORE") không có nhà. Vẻ đẹp của nó đến từ lùm cây, lối mòn, ao, vách và đèn. Những thứ đó áp được vào cả Rồng (sân không có nhà) lẫn Lời Gọi (nhà do người chơi xây).

**Kết luận:** thiếu luật bố cục, không thiếu máy làm địa hình. Bào mòn (erosion), TopoTopo hay Houdini không sửa được các điểm trên. Sơn đất, lùm cây, lối mòn và đồ dọc đường thì sửa được, và ta tự làm được.

### 1.2 Đề xuất đúng ở đâu

- **GLB không phải nguồn** (§4). Nguồn là spec + seed + sổ model + luật sinh.
- **AI sửa spec, không sửa từng vật** (§5).
- **Sinh có luật chơi** (§16) và **kiểm tự động** (§19); không nhận bản đồ chỉ vì đẹp.
- **Seed tất định, ghi phiên bản bộ sinh** (§17, §18).
- **CLI trước, MCP sau** (§22).
- **Tripo chỉ làm từng vật**, không làm cả bản đồ (§15).
- **Không dùng Houdini ở bản đầu** (§10).

### 1.3 Đề xuất sai hoặc không hợp với ta ở đâu

| Đề xuất | Vấn đề với ta | Sửa thành |
|---|---|---|
| MapSpec → bộ sinh → **Blender** → `map.glb` (§2, §3) | Cả ba game dựng đất, nước, đường, shader lúc chạy. Prop instanced theo từng tier. Vật che được làm mờ (dither). Rồng và Lời Gọi cho xoay camera tự do. Rồng định 520 ải: mỗi ải một GLB thì vỡ cỡ deploy | Game gọi lõi sinh bố cục từ spec lúc nạp, rồi tự dựng. Blender chỉ chuẩn bị từng model |
| `collision.glb`, `navmesh.json` (§4) | Sim là TypeScript tất định trên mặt phẳng (x, z). Rồng tính bằng số nguyên u (1 m = 60.000 u); Lời Gọi đi trên lưới 1 m với A*. Sim không đọc mesh | Va chạm và đường đi nằm trong nội dung game. Bộ sinh chỉ đọc chúng và kiểm decor không nói dối luật |
| Blender MCP "có thể là phần quan trọng nhất" (§7.2) | Cả hai server MCP chạy Python tùy ý qua socket không xác thực, và làm cho phiên GUI đang mở | Blender headless qua CLI, ghim 5.2 LTS (mục 4.3) |
| WFC giải "40 phòng, 1 boss, đường chính ≥ 12" (§6.3) | Đó là ràng buộc toàn cục; WFC thuần chỉ biết luật kề nhau | Đồ thị phòng trước, WFC làm chi tiết; chỉ khi có game dungeon (mục 5) |
| Thư mục bộ sinh theo chủ đề: island, desert, village… (§13) | Phần dùng lại thật giữa các game là vài **phép toán**: trường, spline, rải, sơn đất, đồ dọc đường | Lõi là các phép toán theo lớp. Phần riêng mỗi game là lớp chơi và phép kiểm |
| Bộ sinh làng tự dựng nhà (§6.2) | Luật dự án cấm dựng nhà, prop, sinh vật bằng mã. Nhà của Lời Gọi do người chơi xây | Không sinh nhà. Chỉ sinh nền, lối mòn, chỗ đặt rào và đèn (model Tripo) |
| Poly Haven, Quaternius, Kenney (§11) | Lệch phong cách tranh vẽ của model Tripo; trái luật "model từ ảnh 2D của ta qua Tripo" | Mỗi vùng một bộ kit riêng: Tripo cho Rồng; billboard 2D cộng ≤ 6 mốc Tripo cho Lời Gọi (mục 4.5) |
| Bản đồ 1.200 × 1.200 m, 2 km (§5, §23) | Bản đồ thật nhỏ hơn nhiều: Rồng bán kính 32 m, Lời Gọi 96 × 96 m, Tuyến Cuối 24 × 40 m, Tu Tiên 40 × 26 m | Không chia chunk, không streaming ở bản đầu |
| Unity MCP, Unreal MCP (§8, §9) | Cả ba game là web three.js. Hai MCP đó còn beta hoặc thử nghiệm (mục 5.2) | Không dùng bây giờ. Lõi xuất dữ liệu trung lập, nên engine khác chỉ cần một bộ đọc |

### 1.4 Trả lời nhanh câu hỏi A–H

| Câu | Trả lời ngắn | Chi tiết |
|---|---|---|
| A1 Kiến trúc có ổn không? | Nửa đầu ổn (spec → bộ sinh → kiểm). Nửa sau (Blender → GLB cả bản đồ) không hợp game web của ta | 1.3, 3 |
| A2 Sửa gì? | Lớp chơi đọc từ game, không sửa trong spec. Bố cục sinh lúc nạp, game tự dựng. Blender lùi về khâu từng model. Thử bố cục trước khi xây hạ tầng | 3, 6 |
| A3 Có cách đơn giản hơn không? | Có: một lõi TS thuần, không gói ngoài, chạy cả trong Node lẫn trình duyệt; dựng hình bằng mã sẵn có của game | 3, 4 |
| A4 CLI hay MCP? | CLI. MCP chỉ làm sau, dưới dạng một lớp mỏng gọi chính CLI, khi có agent thật sự cần | 4.1 |
| A5 Tự viết hay dùng ngoài? | Tự viết: spec, các lớp, rải, kiểm. Dùng ngoài: three.js, Blender (chuẩn bị model), meshopt, TypeScript, Tripo (model) | 4.1 |
| B TopoTopo | Có thật, Apache-2.0, chạy headless, xuất GLB có instancing. Mới 24 ngày tuổi, một người làm, chưa ai ngoài dùng: theo dõi, thử sau | 4.4 |
| C Blender | CLI headless + script bpy cho từng model; Geometry Nodes chỉ nhân bản theo điểm cho sẵn; MCP ngoài đường chính | 4.3 |
| D WFC | Không hợp TD, làn, làng, hang. Hợp phòng sci-fi khi có bộ ô khớp cỡ. Không tìm thấy thư viện JS/TS nào vừa còn bảo trì vừa có ràng buộc toàn cục (DeBroglie, bản C# mạnh nhất, phát hành lần cuối năm 2022); khi cần thì tự viết theo mẫu DeBroglie | 5.1 |
| E Asset | Sổ = bản quét 025 + file kit (vai trò, cách vẽ, cỡ danh nghĩa, bóng, LOD, giấy phép). Không ship gói ngoài | 4.5 |
| F Hiệu năng web | Có công thức draw call, phần khung hình, thời gian nạp, trần tam giác và texture | 4.2 |
| G MVP | Thử bố cục trên Rồng L2-cau; Lời Gọi bản đồ 1 là mẫu CLI đủ mọi phần G hỏi; bảng ai sinh phần nào ở 6.3 | 6 |
| H Dùng lâu dài | Lõi dùng chung được. Bộ đọc lớp chơi, luật decor, bộ kit và cách vẽ là riêng từng game | 11 |

---

## 2. Vấn đề và rủi ro

| Rủi ro | Vì sao | Cách giảm |
|---|---|---|
| **Xây hạ tầng trước khi biết có đẹp không** | Rủi ro lớn nhất là vẻ ngoài. Làm 7 phiếu hạ tầng rồi mới chấm ảnh là làm ngược | Spike bố cục 1–2 ngày trước (6.2). Chỉ 3 phiếu nền chạy song song, vì kết quả nào cũng cần chúng |
| Điểm thấp mà không biết vì sao | Có ba nguyên nhân: bố cục, bộ kit, hay luật chơi khóa sân | Spike ghi rõ nguyên nhân giới hạn cho từng góc nhìn (6.2) |
| Decor nói dối luật chơi (Lời Gọi) | Lời Gọi cho xây gần như khắp sân 96 m, sát cả mép đường và mép nước | Luật decor 6.4: trên đất xây được, mọi decor đều `clearOnBuild`; vật cố định chỉ ở vùng sim cấm xây. CLI kiểm, có mẫu hỏng |
| Cây decor trông như cây luật (Lời Gọi) | Thiết kế §23.10 cho cây cảnh trên đất xây và quật đổ khi đặt nhà. Người chơi có thể tưởng cây cảnh chặn đặt nhà hay chặt được | Luật nhìn ở 6.4: cây luật có dấu riêng; cây decor cách cây luật ≥ 4 m; bóng ma đặt nhà hiện cây nào sẽ đổ |
| Decor lộ ô ẩn (Rồng) | Thiết kế 05 §2: ô nhà và bẫy không bao giờ vẽ lên đất | Lối mòn không dẫn tới ô; không chừa khoảng trống hình ô; có phép kiểm |
| Đẹp tới đâu tùy bộ kit | Rồng có pine-river (13 GLB, 8 ô đất, 4 decal). Lời Gọi chưa có ô đất; 3 mốc mới có ảnh 2D còn lỗi nền | Spike đo xem kit có đủ không. Ảnh còn thiếu làm thành một lô riêng ở giai đoạn 4 |
| Trôi tất định | Số thực, trig, `Date` lọt vào lõi; V8 từng đổi cách tính sin, cos | Lint bằng bộ quét TypeScript; `erasableSyntaxOnly`; băm vàng từng lớp; quy tắc 8.5 |
| Bộ đọc lớp chơi đọc phải cây đang sửa | Làn A1/A2 của Lời Gọi sửa `slice-1a.ts` hằng ngày (đợt quái) | Đọc nội dung ở một commit ghim (`git archive`), băm phần bản đồ đã trích ra, không băm cả file |
| Codex và Claude cùng ghi một thư mục | Luật repo cấm hai người ghi một cây cùng lúc | Codex chạy trong worktree riêng của repo cha, nhánh `map-factory`; mỗi thư mục một người ghi tại một thời điểm (9.4) |
| Hạn mức Codex rất thấp | Cửa sổ 5 giờ; ảnh trước, mã sau | Giai đoạn 1–2 không thêm ảnh nào. Phiếu mã xếp sau các phiếu ảnh đang chờ |
| Thời gian nạp | Sinh bố cục lúc nạp tốn thời gian; Rồng có cổng "nạp ải cùng kit ≤ 1 s" (05 §8) | Cổng ≤ 300 ms trên M4 cho phần sinh; quá thì sinh lúc build (sản phẩm build, không vào Git) |
| Gói "/" của Lời Gọi chỉ còn 13 byte | `BUILD_NOTES.md` §7.10 | Lõi và cảnh 3D vào chunk nạp sau của bước 1C, không vào "/" |
| Chi phí kit sync | Thêm module `map` vào kit; mỗi lần sửa phải chép vào game và ghi `DRIFT.md` | Chỉ chép khi tới bước đưa vào game, do điều phối viên chạy |
| Lan phạm vi | "Nhà máy cho mọi game" trước khi có một bản đồ đẹp | Hoãn khóa lớp, `diff`, `guide.svg`, kiểm kit cho tới khi bản đồ đầu đạt; điều kiện dừng ở mục 12 |
| TopoTopo (nếu dùng sau) | Một người làm, ba bản phụ trong 5 ngày | Chỉ thử trong thư mục riêng, ghim đúng bản; luôn có đường lui |

**Điểm phản biện không theo nguyên văn:**
- "Sân Lời Gọi bị luật chơi khóa": đúng một phần. §23.10 vẫn cho cây cảnh trên đất xây (đổ khi đặt nhà), nên sân vẫn bố cục được bằng lùm cây và sơn đất; chỉ vật cố định là bị khóa.
- "13 ô dọc làn ở L2-cau": mã ở `m0b-models` có 11 ô (7 bẫy, 4 chặn) và 6 ô nhà. Kết luận không đổi.

---

## 3. Kiến trúc đề xuất

```text
 Người / Claude / Codex sửa CHỮ (spec), không sửa hình
        │
        ▼
 map.spec.json (Git)                   nội dung game (lớp chơi: làn, ô, nước, cầu, cây, nhà đặt sẵn)
        │                                      │
        │      giai đoạn 1–2: bộ đọc ở repo cha, git archive <commit ghim> → trích ra cm nguyên → băm
        │      sau khi đưa vào game: game tự đưa MapDef của mình vào lõi
        └──────────────────┬───────────────────┘
                           ▼
  lõi = shared/game-kit/map   (TS thuần, số nguyên; không three, không DOM, không trig)
  ┌───────────────────────────────────────────────────────────────────────┐
  │ L0 gameplay   đầu vào, chỉ đọc: làn đã lấy mẫu, ô, nước, cầu, cây luật │
  │ L1 fields     lưới 50 cm + biến đổi khoảng cách: đường, nước, đất xây  │
  │ L2 height     dấu đồi, vách, lòng chảo + nhiễu; san phẳng dưới đường   │
  │ L3 water      suối (khớp luật), ao trang trí, thác                      │
  │ L4 paths      dải đường quái (từ L0) + lối mòn trang trí               │
  │ L5 dressing   đèn, rào, cọc, cầu, mốc dọc đường cong                    │
  │ L6 vegetation lùm cây, rừng mép, cây luật; rải theo ô, theo hạng       │
  │ L7 paint      tham số sơn đất: dưới tán, mép mòn, ngã ba, decal        │
  │ checks        luật decor, ngân sách, sổ model, băm từng lớp            │
  └───────────────────────────────────────────────────────────────────────┘
        │                                   │
        │ CLI (repo cha): validate | build | check → out/ (không vào Git)
        │ golden: băm từng lớp (Git); layout.json chỉ cho bản đồ chỉnh tay
        ▼
  game: gọi lõi lúc nạp (hoặc lúc build) → bố cục trong bộ nhớ
    Rồng: terrain.ts, scatter.ts, water.ts sẵn có (InstancedMesh, LOD, impostor)
    Lời Gọi 1C: đất + billboard atlas 2D (§23.10) + ≤ 6 mốc Tripo
        ▲
  sổ model: registry/out/assets.<game>.json (phiếu 025) + registry/kits/<kit>.json
        ▲
  GLB Tripo của chủ dự án → Blender headless (static_model_tools.py, bake_impostor.py)
                          → prepare-models (meshopt, tier) → pnpm media:push
```

### 3.1 Sáu nguyên tắc

1. **Lớp chơi là sự thật, nằm trong nội dung game.** Bộ sinh chỉ đọc, không ghi. Sim không bao giờ đọc mesh hay bố cục.
2. **Bản đồ là spec + seed + phiên bản sổ model + phiên bản bộ sinh.** Game ship spec và lõi, sinh bố cục lúc nạp. Test của game giữ băm vàng từng lớp. `layout.json` chỉ vào Git làm golden hoặc để duyệt, với bản đồ chỉnh tay.
3. **Lõi chạy y hệt ở mọi nơi.** Node (CLI, test) và trình duyệt cho cùng từng byte, vì chỉ dùng số nguyên, `+ - * /`, `Math.sqrt`, `Math.floor`.
4. **Mỗi lớp một seed:** `hash32(mapSeed, tênLớp, phiênBảnLớp)`. Rải theo ô: `hash32(seedLớp, cx, cz)`. Mật độ theo hạng: tăng mật độ chỉ thêm vật, không dời vật cũ. Sửa lớp nào thì chỉ lớp đó và các lớp sau đổi băm.
5. **Ghim tách khỏi đầu ra.** Không bao giờ sửa tay bố cục.
6. **Không model dựng bằng mã.** Mã chỉ làm đất, nước, đường, decal, shader, instancing, billboard. Mọi cây, đá, nhà, đèn là model Tripo hoặc tranh 2D có trong sổ.

### 3.2 Khi nào nướng sẵn GLB thì tốt hơn

| Phần | Nướng GLB? | Lý do |
|---|---|---|
| LOD và impostor của **từng model** | Có, một lần mỗi model (`bake_impostor.py`, decimate giữ đường nối) | Loader r170 không có `MSFT_lod`; nướng sẵn rẻ và tái lập được |
| Vòng rừng xa của **một kit** | Chỉ khi đo thấy vòng xa dựng lúc chạy tốn quá nhiều draw call. Khi đó nướng một lần mỗi kit | Một kit dùng cho nhiều bản đồ |
| Xuất sang engine khác | Về sau: `cli export --glb` qua Blender headless, có `EXT_mesh_gpu_instancing` | Chỉ để trao đổi, game web không dùng |
| **Cả bản đồ chơi được** | Không | 520 ải × cỡ media; cần tier, dither, xoay camera; mỗi game deploy riêng |
| Lớp sơn đất | Không ship ảnh. Nướng lúc nạp vào render target (art-pipeline §2.2 của Rồng) | Cỡ deploy; vết cháy, hố bẫy vẽ thêm lên được |

---

## 4. Bộ công cụ

### 4.1 Chọn gì

| Phần | Chọn | Vì sao | Ghim |
|---|---|---|---|
| Lõi sinh | TS thuần trong `shared/game-kit/map` | Không cần cài gói. Cùng một mã cho CLI, vitest và trình duyệt | Node 24.x |
| Nạp TS trong Node | Node 24 tự bỏ kiểu, cộng một hook resolve khoảng 15 dòng để thêm đuôi `.ts` | Đã thử 27/10 trên Node v24.22.0, không cần gói nào: nạp được `lanes.ts`, `slice-1a.ts`, `rules.ts` của Lời Gọi, `maps.ts` của Rồng và module kit | — |
| Đọc lớp chơi | Bộ đọc cho từng game, đọc nội dung ở commit ghim, gọi chính hàm làn của game (`groundLanes` của Lời Gọi, `compileLanes` của Rồng) | Hàm làn của Lời Gọi là đường Hermite, tiếp tuyến lấy trung bình giữa các tuyến ở nút chung; một Catmull-Rom chung sẽ lệch chỗ quái đi thật | — |
| Số ngẫu nhiên | `hash32` số nguyên + `RngStream` (mulberry32) của `platform/rng.ts` | Có sẵn, cùng cách chia luồng theo tên | — |
| Nhiễu | `hash2`, `valueNoise` số nguyên, như `terrain.ts` của Rồng | Đủ dùng | — |
| Rải | Tự viết: theo ô, xếp hạng, có ghim | `@thi.ng/poisson` 3.2.99 không seed theo ô; `poisson-disk-sampling` 2.3.1 gọi `Math.cos`, `Math.sin` | — |
| Khoảng cách | Biến đổi khoảng cách chính xác bằng số nguyên (Meijster 2000) | Khoảng 100 dòng; một bộ trường dùng cho san đất, sơn đất, chỗ lùi cây | — |
| Lint tất định | `ts.createScanner` của TypeScript 6.0.3 (đã có trong `shared/game-kit`) + `erasableSyntaxOnly` trong `map/tsconfig.json` | Bỏ qua chú thích và chuỗi, nên không bắt nhầm `/**` hay chữ "enumerate" | 6.0.x |
| Dựng hình | three.js 0.170 của từng game | Rồng dùng lại `terrain.ts`, `scatter.ts`, `water.ts`; Lời Gọi làm billboard theo §23.10 ở bước 1C. Chưa làm module dựng hình dùng chung | 0.170.0 |
| Chuẩn bị model | Blender 5.2 LTS headless: `static_model_tools.py`, `bake_impostor.py` | Có sẵn. Đo 27/10: cùng đầu vào, cùng máy cho cùng byte | 5.2.x |
| Nén | meshopt (đã có trong `prepare-models.mjs`) | Bộ giải mã 6,5 KB gzip; Draco khoảng 100 KB | — |
| Texture | WebP như hiện nay; KTX2 (UASTC/ETC1S) khi một bản đồ có hơn 40 model có texture, hoặc ở tier Low | 1024² WebP chiếm khoảng 5,3 MiB GPU; UASTC khoảng 1,33 MiB; ETC1S khoảng 0,67 MiB | — |
| Kiểm GLB | `scan-assets.mjs` (phiếu 025); `gltf-transform inspect/validate` khi cần | 025 đọc được GLB nén mà không giải nén | 4.5.0 |
| Xem thật | Sân khấu sẵn có: `?view=terrain` của Rồng, kịch bản `dh-camera`, `dh-perf`, `dh-bench` | Claude chụp và đo; cần cổng nên không giao Codex | — |
| Instancing nâng cao | `@three.ez/instanced-mesh` 0.3.16 | Chỉ khi cần cull từng cây (hành lang dài của Tuyến Cuối) | — |

### 4.2 Hiệu năng web (câu F)

**Trần của từng game:**
- Rồng (`05-presentation-audio-tech-split.md` §8), High: tổng 2 M tam giác tính cả bóng, tam giác prop ≤ 0,9 M, ≤ 150 draw call, khung trung bình ≤ 8 ms và p95 ≤ 12 ms; nạp ải cùng kit ≤ 1 s, kit mới ≤ 5 s.
- Lời Gọi (`TYPING_DEFENSE_DESIGN.md` §25.12), High: khung trung bình ≤ 5,5 ms, p95 ≤ 8,5 ms, ≤ 150 draw call. Cảnh theo §23.10: High 1.500 vật lớn + 4.000 cỏ hoa chữ thập, ≤ 6 draw call cảnh 2D + 2–3 trụ phông; đo ở góc thấp 15°.

**Phần khung hình của bản đồ.** Trần 8/12 ms là cho cả trận ở mức tải cao nhất, không phải cho riêng bản đồ. Cổng của bản đồ là phần chênh so với đất trống, đo dưới tải `dh-bench` (220 quái có xương, High, 1080p):
- chênh trung bình ≤ 2 ms, chênh p95 ≤ 3 ms;
- tổng vẫn trong trần của game.

M0b đo ngày 27/10 dưới tải này: trung bình 5,93 ms, p95 7,8 ms, 70 draw call, tính cả bản đồ hiện tại. Phần còn trống là khoảng 2 ms và 80 draw call.

**Công thức draw call của bản đồ:**

```text
DC_bản đồ = G + P_gần + P_giữa + I + S
  G       đất 1, nước 1–2, thác 1, sương hoặc phông 1                ≤ 5
  P_gần   số proto ở dải gần (mỗi proto một InstancedMesh)           High ≤ 12, Medium ≤ 10
  P_giữa  proto có bậc 40 % tam giác ngoài 30 m (chỉ tán lớn, đá lớn) High ≤ 6,  Medium 0
  I       một atlas impostor dùng chung cho cả vòng xa của kit        1
  S       proto ở dải gần có đổ bóng                                 High ≤ 8,  Medium ≤ 4
High ≤ 5 + 12 + 6 + 1 + 8 = 32 (trần 40);  Medium ≤ 4 + 10 + 0 + 1 + 4 = 19 (trần 30)
```

Một kit có 12–20 món, nhưng mỗi bản đồ dùng tối đa 12 proto ở dải gần; các món còn lại dành cho bản đồ khác cùng kit. Dáng khác nhau đến từ cỡ, hướng và sắc của từng vật, không từ thêm proto. Lời Gọi theo §23.10: cảnh 2D ≤ 6, phông 2–3, mốc 3D ≤ 6 × 2 (vật và bóng), đất và nước ≤ 3, tổng ≤ 24.

**Tam giác, phần của bản đồ:**

| Mục | High | Medium |
|---|---|---|
| Prop của bản đồ, chưa tính bóng (trong trần prop 0,9 M của Rồng) | ≤ 0,55 M | ≤ 0,3 M |
| Lưới đất (chỉ nhận bóng, không đổ bóng) | Rồng hiện nay khoảng 200 k; Lời Gọi ước khoảng 108 k | ô 0,75 m: Rồng khoảng 97 k, Lời Gọi khoảng 56 k |
| Cây gần | ≤ 200 cây × ≤ 1.500 tam giác | tier medium, mật độ × 0,6 |
| Đá, bụi, đồ vụn 3D | ≤ 100 k tổng; đồ vụn ≤ 300 tam giác mỗi món | × 0,5 |
| Đồ dọc đường và mốc | ≤ 60 k | như High |
| Vòng ngoài | impostor nướng từ model, không đổ bóng | như High |

**Lưới đất.** Dùng lưới có trục đổi bước như `gridAxis` trong `terrain.ts` của Rồng: các đường lưới mịn trong sân chạy thẳng ra vòng ngoài, nên không có nối chữ T, không nứt. Số tam giác tính từ số điểm trên mỗi trục:
- Rồng hiện nay: ô 0,5 m trên cả hình vuông 144 m, cộng 14 bước ra tới 300 m: 317 điểm mỗi trục, khoảng 200 k tam giác. Cổng M0b đã đạt với lưới này.
- Lời Gọi: ô 0,5 m trong sân 96 m, bước 2 m ở vòng ngoài 40 m: 233 điểm mỗi trục, khoảng 108 k tam giác.

**Thời gian nạp.** Phần sinh bố cục (trường, rải, sơn) ≤ 300 ms trên M4, nằm trong cổng "nạp ải cùng kit ≤ 1 s" của Rồng. Quá thì sinh lúc build, ghi thành sản phẩm build (không vào Git).

**Các điểm khác:**
- **Cỏ, hoa, sỏi chủ yếu là decal trong lớp sơn đất, không phải 3D.** 2.500 viên đá cỡ 450 tam giác đã là 1,1 M tam giác. Hoa cỏ trong ảnh mẫu phần lớn cũng là texture.
- **Cỡ GLB:** prop của kit ≤ 250 KB; mốc lớn ≤ 600 KB. Một kit mới phải nạp ≤ 5 s, tức khoảng 6 MB ở 10 Mbps (số tự suy, không phải số đo).
- **Texture:** đồ vụn 512²; prop của kit 1024²; mốc lớn và ảnh trộn đất 2048².
- **Instancing:** mỗi proto, mỗi dải khoảng cách là một InstancedMesh. Không dùng `THREE.LOD` trên InstancedMesh, vì nó đổi cả nhóm cùng lúc. Không dùng BatchedMesh cho cây: mỗi model Tripo có texture riêng, và Firefox không có `WEBGL_multi_draw`.
- **Bóng:** cây xa, impostor và đồ vụn không đổ bóng.
- **Chia chunk:** chưa cần cho bản đồ một màn hình. Cần khi camera lia qua hơn khoảng hai màn hình, và cho hành lang Tuyến Cuối (đoạn khoảng 32 m).
- **Va chạm:** sim đọc dữ liệu nội dung (làn, ô, lưới đi). Phía hình chỉ cần chọn vật bằng mặt đất giải tích và hộp từng vật; `three-mesh-bvh` chỉ khi không đủ.
- **Draco hay Meshopt:** giữ Meshopt.

### 4.3 Blender (câu C)

| Cách | Đo và đọc được (27/10) | Dùng thế nào |
|---|---|---|
| Blender MCP | Bản chính thức của Blender Lab: GPL-3.0, v1.0.3 ngày 11/09/2026, cần Blender 5.1+; trang tài liệu nói nó chạy mã LLM "không có rào chắn" và khuyên dùng VM. Bản `ahujasid/mcp-for-blender`: MIT, khoảng 32,5 nghìn sao, socket localhost:9876 không xác thực, gửi telemetry mặc định, gọi API Tripo/Meshy. Cả hai làm cho phiên GUI | Ngoài đường chính. Chỉ dùng bản Blender Lab, trong VM, khi chủ dự án muốn ngồi chỉnh cùng AI |
| Script bpy trực tiếp | Cùng đầu vào, cùng máy cho cùng byte. Tạo vật bằng Python chậm: 20.000 bản sao mất 54 s | Chuẩn bị **từng model**: hướng, cỡ, gốc, giảm mặt, impostor. Không dựng cả cảnh |
| Geometry Nodes | Nhanh: khoảng 14.000 bản sao trong 15 s, cùng byte. Nhưng rải ngẫu nhiên phụ thuộc cả lưới: đổi một tham số là mọi điểm xáo lại. API đổi giữa các bản (`outputs[2]` hỏng ở 5.2) | Chỉ nhân bản theo điểm do lõi TS đưa vào, khi cần xuất GLB cho engine khác |
| CLI headless | `blender -b --factory-startup --python-exit-code 1 -P script.py -- <args>`; gói `bpy` 5.2.3 trên PyPI cho CI Linux (chưa kiểm cùng byte giữa hai nền) | Cách gọi chuẩn cho mọi việc Blender; ghim 5.2 LTS; chạy thử lại trên một mẫu mỗi khi nâng Blender |

**Kết hợp nên dùng:** CLI headless + script bpy cho từng model (`static_model_tools.py`, `bake_impostor.py`), ghim 5.2 LTS, mỗi lần chạy có file JSON đầu vào, báo cáo JSON và ảnh xem. Geometry Nodes chỉ làm bộ nhân bản khi xuất GLB. MCP không vào đường chính.

### 4.4 TopoTopo (câu B)

| Câu | Trả lời (kiểm 27/10/2026) |
|---|---|
| B1 Đủ chín chưa? | Chưa. Repo tạo ngày 03/10/2026; bản 0.4.0 ngày 27/10; 0 sao, 0 issue, 0 fork; khoảng 445 lượt tải npm từ 10/10 tới 27/10 |
| B2 Còn được bảo trì không? | Rất sôi nổi nhưng chỉ một người: khoảng 360 commit (27/10), phần lớn có đồng tác giả Claude Opus 5.5; ba bản phụ trong 5 ngày. README còn ghi "v0.3" khi v0.4 đã ra |
| B3 MCP có tin được không? | Thiết kế hợp agent: 14 công cụ qua stdio (build, edit, inspect, render, export, diff…), sửa graph từng phần có cache, `assert` trong graph, ảnh xem nhiều góc không cần GPU. Độ tin cậy **chưa được chứng minh**: chỉ có test đầu-cuối của chính tác giả, chưa ai ngoài báo lỗi; ta chưa chạy. Với ta, CLI là đủ; trình xem (cổng 7341) và gallery (cổng 7340) cần cổng nên Codex không dùng được |
| B4 Xuất GLB dùng được không? | Có: qua glTF Transform, có vật liệu, texture, màu đỉnh, meshopt và lượng tử hóa; bản sao xuất thành `EXT_mesh_gpu_instancing`, loader three r170 của ta đọc được. Tác giả báo nhập sạch vào Blender 5.2, Unreal 5.8, Houdini 22. Mỗi lần xuất có file nguồn gốc (băm graph, biến, seed, phiên bản) |
| B5 Chạy headless không? | Có: Node ≥ 22.18, không cần GPU, ảnh xem vẽ bằng phần mềm. Mọi phụ thuộc là JS hoặc WASM, nên đáng lẽ chạy được trên Mac arm64, nhưng CI không chạy macOS (chỉ Ubuntu, Windows) |
| B6 Hợp địa hình không? | Mạnh về heightfield: khoảng 25 node (nhiễu, mặt nạ, bậc thang, cắt); bào mòn kiểu giọt nước, ống ảo, stream-power, nhiệt; lấp trũng priority-flood có độ sâu hồ; dòng chảy D8 và D∞ cho mặt nạ sông; `heightfield_path` cắt và san đất dọc đường cong cho sẵn (có vai đường, nghiêng, mặt nạ đường; không tự tìm đường); `heightfield_scatter`. Rải: mặt nạ mật độ, blue noise, khoảng cách tối thiểu chính xác; `mask` theo dốc, cao độ, khoảng cách; `prune`, `orient`, `copy_to_points`; node `file` nạp GLB của ta. **Không có bộ sinh làng**: các ví dụ `house_city`, thành phố Voronoi, phố mẫu đều dựng nhà bằng mã, mà luật ta cấm. Số của tác giả (i7-10700K): bào mòn ống 1024² × 200 bước 3,0 s; thung lũng 1 km² có đường, mặt nạ sông, 26 nhà, 12,9 nghìn vật khoảng 6 s; 100 nghìn điểm blue noise 0,65 s. Bản đồ của ta nhỏ hơn nhiều |
| B7 Giới hạn | Một người làm, mã phần lớn do AI viết; biểu thức trong graph chạy trong `vm` mà tác giả nói "không phải ranh giới bảo mật"; không CI macOS; mặt nạ sông trông giả trên vùng đã lấp phẳng; không có trình sửa node; cùng byte giữa các nền chỉ thử trên một máy; bị khóa vào định dạng graph nếu graph thành nguồn |
| B8 Dùng ngay hay theo dõi? | **Theo dõi.** Giai đoạn 6 (tùy chọn): thử 1–2 ngày, chỉ địa hình (vách, lòng thác), ghim đúng `topotopo@0.4.0` trong thư mục riêng; MapSpec của ta vẫn là nguồn. Dùng thật khi có người dùng ngoài và định dạng graph đứng yên khoảng 3 tháng |

### 4.5 Asset (câu E)

**Quản lý:**

| Việc | Cách làm |
|---|---|
| Sổ model | Bản quét của phiếu 025 (`tools/map-factory/registry/out/assets.<game>.json`: cỡ, tam giác, xương, clip, nguồn, md5) cộng file kit `registry/kits/<kit>.json` cho phần quét không đo được |
| Siêu dữ liệu trong file kit | `role` (canopy, understory, rock, clutter, landmark, road-furniture); `render` (`mesh`, `billboard`, `decal`); `asset` dạng `<game>:<id>` cho từng tier hoặc ô atlas; `nominalHeightCm`, `scaleRangePermille`, `footprintRadiusCm`, `clearanceCm`; `pivot`; `castShadow`; `lod`, `impostor`; `variants`; `licence` |
| Cỡ | Mét, +Y lên, mặt trước theo glTF. `static_model_tools.py` đưa model về `nominalHeightCm`, gốc ở đáy (cầu: giữa mặt cầu; rào: một đầu). Kiểm: đáy ở y = 0 ± 1 cm |
| Va chạm | Trong sim, nền (footprint) là va chạm, nằm trong nội dung game bằng số nguyên. Phía hình: hộp để chọn vật. Không có GLB va chạm |
| LOD | Bậc 40 % tam giác ngoài 30 m (decimate giữ đường nối) và impostor, nướng một lần mỗi model; lúc chạy chia dải khoảng cách, mỗi dải một InstancedMesh |
| Biến thể vật liệu | Đổi sắc, tô màu từng vật qua `instanceColor` hoặc uniform. Không dùng `KHR_materials_variants`, vì loader r170 không có |
| Giấy phép | `origin`, `sourceArt`, mã SPDX, URL, ngày lấy, phiên bản gói. Kiểm báo hỏng khi model bên thứ ba thiếu trường. Quaternius QAL §7 nói phiên bản giấy phép "lúc bạn lấy asset" có hiệu lực, nên phải ghi ngày và bản |

**Các thư viện ngoài:**

| Thư viện | Giấy phép, nội dung | Hợp với ta? |
|---|---|---|
| Poly Haven | CC0; 521 model, nhiều cây, đá, đồ; ảnh quét thật (PBR). Điều khoản cấm cào dữ liệu không xin phép | Không cho model. Chỉ HDRI, tham chiếu ánh sáng |
| Quaternius | Trang giấy phép (cập nhật lần cuối 28/8/2026) ghi Quaternius Asset License v1.0: cấm phân phối lại asset rời. Trang gói Stylized Nature MegaKit vẫn ghi CC0 | Không ship. Giấy phép không nhất quán |
| Kenney | CC0; Nature Kit (2020), Fantasy Town Kit (2022); màu phẳng kiểu đồ chơi | Chỉ dựng thô |
| KayKit (tốt hơn danh sách của đề xuất) | CC0; Forest Nature Pack hơn 100 model, một atlas 1024² | Dựng thô tốt hơn hình nón trong `scatter.ts`; không ship |
| ambientCG | CC0, texture PBR thật | Chỉ làm chi tiết đất |
| Styloo Village | CC0; 7 nhà, rào, đèn, xe | Chỉ tham khảo |

Model Tripo của ta mỗi cái một vật liệu, texture WebP 1024², 450–4.400 tam giác. Đặt cạnh gói ngoài sẽ lộ hai mật độ texel và hai kiểu dáng. Nguồn thật là **bộ kit của từng vùng**: Rồng dùng 12–20 model Tripo (pine-river đã theo mẫu này); Lời Gọi dùng tranh 2D billboard cộng ≤ 6 mốc Tripo (§23.10). Ship model bên thứ ba là trái luật hiện hành; muốn đổi phải hỏi chủ dự án.

---

## 5. Công cụ nên tránh

| Công cụ | Tránh vì | Xem lại khi |
|---|---|---|
| `ahujasid/mcp-for-blender` (blender-mcp) | Socket "không xác thực, không mã hóa", chạy Python tùy ý; gửi telemetry mặc định; gọi API Tripo/Meshy, trái luật dựng Tripo bằng tay trên web | Không |
| Blender Lab MCP (chính thức) | Chạy mã LLM không rào chắn, khuyên chạy trong VM; không giúp gì cho build tái lập | Khi chủ dự án muốn chỉnh tay cùng AI, trong VM |
| `map.glb` cả bản đồ, `collision.glb`, `navmesh.json` | Mục 1.3 | Chỉ để xuất sang engine khác |
| TopoTopo trong đường chính | Mục 4.4 | Giai đoạn 6 |
| WFC cho TD, làn, làng, hang | Mục 5.1 | Khi có game dungeon với bộ ô khớp cỡ |
| Houdini | Giấy phép; Codex không chạy được; quá tầm | Không |
| Unity MCP, Unreal MCP | Mục 5.2 | Khi một game mới chọn engine đó |
| Poly Haven, Kenney, Quaternius trong game ship | Mục 4.5 | Khi chủ dự án đổi luật model |
| Draco | Bộ giải mã nặng hơn; đã có meshopt | — |
| `seedrandom`, `poisson-disk-sampling` | Bản cuối năm 2019 và 2022; cái sau dùng trig | — |
| `Math.sin/cos/pow/hypot/random`, `Date` trong lõi sinh | Trig "tính xấp xỉ tùy nơi chạy" theo spec ECMAScript; V8 đã đổi sin, cos từ fdlibm sang glibc | — |
| Geometry Nodes rải ngẫu nhiên | Đổi một tham số là mọi điểm xáo lại; API node đổi giữa các bản | Chỉ nhân bản theo điểm cho sẵn |

### 5.1 WFC (câu D)

| Loại bản đồ | Hợp không | Cách hợp hơn |
|---|---|---|
| Dungeon | Một phần | Đồ thị phòng hoặc nhiệm vụ trước (như bộ sinh vòng của Unexplored), WFC làm chi tiết |
| Khối làng | Kém | Nhà của ta là model Tripo riêng lẻ, không phải bộ ô khớp; đặt nhà theo lô dọc đường hợp hơn |
| Thành phố | Kém cho mạng phố (trường tensor tốt hơn); tốt cho mặt tiền, khối nhà (Townscaper, Bad North) | — |
| Phòng sci-fi | Tốt nhất, nếu có bộ ô mô-đun đúng cỡ khớp nối | Model Tripo phải qua Blender để về đúng mô-đun |
| Hang | Kém | Cellular automata + flood-fill bảo đảm liền |
| Bản đồ TD ngoài trời | Kém | Vẻ của ảnh mẫu là trường liên tục (đường cong, mép đất mềm, lùm cây), không phải lưới ô |

**Thư viện (kiểm 27/10):**
- DeBroglie (C#, MIT): mạnh nhất, có quay lui, ghim ô, ràng buộc đếm, cách nhau, đường liền, vòng. Bản phát hành cuối v2.0.0 ngày 28/08/2022, đẩy mã cuối 21/12/2025: không đạt mức "còn bảo trì".
- mxgmn/WaveFunctionCollapse (C#): bản gốc, còn hoạt động, không có ràng buộc toàn cục.
- kchapelier/wavefunctioncollapse (JS): 2.1.0 năm 2021, tác giả tạm nghỉ, không ràng buộc toàn cục.
- Gói npm mới (three-wfc, schrodinger-wfc 0.1.0): còn non.

**Kết luận:** không tìm thấy thư viện JS/TS nào vừa còn bảo trì vừa có ràng buộc toàn cục. Khi cần (giai đoạn 6), tự viết một WFC TS nhỏ theo mẫu DeBroglie: trạng thái số nguyên, quay lui, ghim, kiểm liền. Hợp một phiếu Codex có test vàng. Không thêm phụ thuộc .NET.

### 5.2 Unity MCP, Unreal MCP (đề xuất §8, §9)

- **Unity:** MCP server chính thức nằm trong gói `com.unity.ai.assistant`, cần Unity 6, dự án nối Unity Cloud và gói dùng thử hoặc thuê bao AI. Bài của Unity ngày 11/05/2026 ghi là "open beta", tính năng có thể đổi hoặc ngừng. Cầu nối chạy khi Editor mở. Có công cụ cho cảnh, script, console, GameObject, và cho tự thêm công cụ bằng C#. Bản cộng đồng: `Singtaa/UnityMCP` (MIT).
- **Unreal:** theo bản tin State of Unreal 2026 của Epic (trang trả 403 khi tải, nên chỉ đọc được qua kết quả tìm kiếm), UE 5.8 có plugin MCP **thử nghiệm**. Unreal PCG thì đã chín cho rải trong engine.
- **Kết luận:** chưa đủ chín để làm nền, và đều gắn vào một Editor đang mở. Nếu một game sau chọn Unity hay Unreal, Map Factory vẫn dùng được: lõi xuất dữ liệu trung lập (điểm, đường cong, mặt nạ), engine đó chỉ cần một bộ đọc (importer C# hoặc dữ liệu điểm cho PCG). MCP của engine khi đó chỉ để chỉnh tay.

---

## 6. MVP

### 6.1 Chọn đích

**Vẻ ngoài thử trước trên Rồng L2-cau.** Lý do:
- Rồng có sân khấu 3D chạy được (`?view=terrain`, `dh-camera`, `dh-perf`, `dh-bench`) và bộ pine-river thật (13 GLB, 8 ô đất, 4 decal). Điểm thấp thì biết ngay do bố cục hay do kit, không lẫn với đồ tạm.
- Sân Rồng ít bị luật khóa: 6 ô nhà, 11 ô dọc làn, 2 làn đất, 1 làn trời, 1 sông. Lùm cây, lối mòn, ao, vách đặt gần như mọi nơi khác.
- Rồng cần bộ sinh nhất: 520 ải, 16 mẫu bố cục, 8 kit (thiết kế 04 §3, §11).
- Thiết kế Rồng đã định sẵn bản đồ là dữ liệu: dấu cao độ, sơn đất, ô đất, `validate-map` (`research/art-pipeline.md` §2, §5).

**Lời Gọi bản đồ 1 là mẫu CLI thứ hai, từ ngày đầu.** Nó có đủ mọi phần câu G hỏi (đường quái, chỗ đặt nhà, Lũy, làng, ruộng, mỏ, cây, suối, cầu, đường đi), nên giữ cho lõi đúng với một game xây khắp sân. Nó vào game ở bước 1C, khi làn Lời Gọi bắt đầu 1C. Lời Gọi chưa đi trước được vì:
- game còn là Canvas 2D, đang ở 1B (làn A1/A2 trên nhánh `a2-days`), `kit.config.json` chưa có `three`, 1C chưa lên lịch;
- cảnh theo §23.10 là billboard 2D; bộ dựng billboard là việc mới của 1C, không có sẵn;
- 3 mốc Tripo (vách Thác Bạc, cầu gỗ, chòi canh) chưa dựng; ảnh 2D của chúng còn lỗi nền (V50–V52, `IMAGE_AUDIT_2026-10-25.md`).

Không đụng làn nào đang chạy: spike làm trong một worktree mới tách từ `m0b-models` (M0b chưa gộp vào `main`), nhánh `map-spike`, không bao giờ gộp. Thứ được giữ lại là luật và tham số, chuyển thành phiếu cho lõi ở repo cha.

### 6.2 Bước đầu: Claude thử bố cục (1–2 ngày)

**Ở đâu:** `games/.wt-dh-mapspike`, nhánh `map-spike` từ `m0b-models`; cài phụ thuộc như các worktree `.wt-dh-*` khác.

**Làm gì**, chỉ trong `src/view/` của worktree, dùng model và ô đất sẵn có:
- mặt nạ sơn đất: đất dưới tán, mép đường mòn, đất quanh ngã ba và quanh bệ Rồng;
- lùm cây: tâm cụm rồi rải trong cụm, thay cho rải đều;
- lối mòn trang trí: tới ao, tới mốc, ra mép rừng; không dẫn tới ô ẩn;
- hàng đá dọc sông và mép làn;
- một ao nhỏ trang trí, một dấu vách ở vòng ngoài đóng khung một cạnh.

**Luật riêng của Rồng phải giữ:** ô không bao giờ vẽ lên đất (05 §2), nên không chừa khoảng trống hình ô và lối mòn không dừng ở ô. Màu có nghĩa bị cấm gần đường; tán tím, xanh lam xa đường. Vật lớn không che làn.

**Chấm thế nào:**
- 12 ảnh: góc nghiêng 40°, 55°, 75° × hướng 0°, 90°, 180°, 270° (cổng nghệ thuật kit của Rồng), cộng phép nheo mắt (thu nhỏ, làm mờ). Đặt cạnh ảnh mẫu.
- Claude chấm từng ảnh trên thang 10. Điểm ở vùng giáp ranh (6,5–7,5) thì thêm một người chấm độc lập (subagent riêng).
- Mỗi ảnh ghi **nguyên nhân giới hạn điểm**: bố cục (sửa luật, rẻ), kit (thiếu món như đèn, rào, đá vách, hoa; hoặc món chưa đẹp), hay luật chơi (sân trống có chủ ý).
- Đo `dh-bench` với bản đồ mới và với đất trống: chênh trung bình, chênh p95, draw call, tam giác.

**Ra gì:** `docs/tools/map-factory/spike-l2-cau.md`: 12 ảnh và điểm, nguyên nhân, số đo, và **danh sách luật kèm tham số** (số cụm, bán kính, mật độ, khoảng sơn đất, cách đi lối mòn). Danh sách này thành thuật toán chính xác trong phiếu 030–033.

### 6.3 Mỗi phần do ai sinh (câu G)

| Phần | Lời Gọi `w1-silverfall` | Rồng `L2-cau` |
|---|---|---|
| Đường quái | Sự thật: `routes` (chữ S, tách đôi, nhập ở (0, 12)). Bộ đọc lấy mẫu `groundLanes` của game mỗi 25 cm. L2 san phẳng, L4 dải đường và mép mòn | Sự thật: `lanes` (polyline). Bộ đọc lấy `compileLanes`, đổi u → cm. L2 san phẳng, L4 dải đường |
| Chỗ đặt tháp | Đặt tự do theo `placement.ts`; không sinh. L1 làm mặt nạ "đất xây được" | Ô bẫy, ô chặn, ô nhà cố định nhưng ẩn; không sinh, decor tránh |
| Lũy / bệ | `keep` (0, 40), `keepClearM` 11; L2 san nền, L7 sân đất | `dais` bán kính 4 m; L7 sân đá |
| Làng, nhà | Người chơi xây; **không sinh** | Ô nhà ẩn; không sinh |
| Ruộng | Vùng phù sa trong thiết kế §22.9, mã chưa có: L7 chỉ sơn gợi ý (`designOnly`) | Không có |
| Tài nguyên | `nodes`: 3 quặng. L7 sân đá quanh mỏ, L5 đá vụn ngoài vòng làm việc | Không có |
| Cây | 36 cây luật (chặt lấy gỗ, chặn đặt nhà; chỉ số là id). Cây cảnh theo luật 6.4 | Toàn bộ là cảnh: L6 |
| Sông, suối | `water`: rect x −25,5…−22,5. L3 làm lòng suối uốn nhẹ **bên trong** rect, thêm bờ, lau sậy | `river` (chỉ hình, phải khớp cầu và chỗ lội của làn) |
| Cầu | 2 rect `bridges`; L5 đặt mốc Tripo "Wooden Bridge" khớp đúng rect | `bridge` trên làn Cầu; `paths.ts` sẵn có |
| Đường đi | Lưới 1 m và A* của sim; không sinh navmesh. Phép kiểm decor (6.4) | Sim đi theo polyline; không sinh |
| Hiệu năng | 4.2: CLI ước tĩnh; game đo khi đưa vào | 4.2: spike đo `dh-bench` |
| Cách vẽ | Đất + billboard atlas (§23.10) + ≤ 6 mốc Tripo | `terrain.ts`, `scatter.ts`, `water.ts` sẵn có |

### 6.4 Luật decor của Lời Gọi

Đây là điểm mấu chốt để sinh có luật chơi. Luật theo thiết kế §23.10.

- **Đất xây được** (trong `buildHalfM` 46; ngoài mặt đường, nước, vòng Lũy, vòng mỏ, nền nhà đặt sẵn, đĩa cây luật): mọi decor đều `clearOnBuild`. Kể cả cây cảnh: §23.10 cho cây đổ ra ngoài 0 → 85° khi đặt nhà, để lại decal gốc cây.
- **Cạnh đường không có dải cấm xây.** `roadClearM` 1,9 bằng đúng nửa bề rộng đường `roadHalfM` 1,9, nên nhà được sát mép đường. Đèn, cọc, rào dọc đường vì vậy đều `clearOnBuild`. Muốn đèn cố định như ảnh mẫu thì làn Lời Gọi phải nới `roadClearM`: đổi luật, có golden mới.
- **Vật cố định** (mốc, đá lớn, vách, rừng mép) chỉ ở vùng sim cấm xây: dải ngoài `buildHalfM` 46 tới mép sân 48, trong `keepClearM` (trừ vùng thẻ chữ của Lũy), trong rect nước, và vòng ngoài 40 m. Hai đầu cầu không phải vùng cấm: đường quái không qua suối, cầu dành cho người đi bộ, nên đất ở đó xây được.
- **Mốc có luật chơi phải có nền trong sim.** Thiết kế §22.9 đặt "chòi canh trên đồi" (Watchtower) trên Đồi Cầu Vồng. Đo bằng chính `groundLanes`: điểm (9, −24) cách tim tuyến đông 4,19 m, tâm đồi (2, −21) cách đường 7,77 m. Cả hai là đất xây được (nhà S chỉ cần 3,9 m). Vì vậy mẫu `w1-silverfall` đặt chòi canh ở vòng ngoài cho tới khi làn Lời Gọi cho nó một nền trong sim (có golden mới). Trường hợp (9, −24) không có nền nằm trong bộ mẫu hỏng của phép kiểm.
- **Cây luật phải đọc khác cây cảnh.** Đề xuất cho làn Lời Gọi chốt ở 1C:
  - cây luật có dấu riêng dưới gốc (decal vụn gỗ) và sáng viền khi rê chuột;
  - cây cảnh cách cây luật ≥ 4 m, nên năm cụm cây luật vẫn đọc thành năm khu lấy gỗ;
  - bóng ma đặt nhà tô đỏ cây luật (chặn) và làm mờ cây cảnh (sẽ đổ).
- **Ao trong sân** phải là nước của sim, nên do làn Lời Gọi quyết. Bản đồ 1 không có ao.
- **Lau sậy ven suối:** nằm trong rect nước hoặc `clearOnBuild` (nhà được sát mép nước).
- Phép kiểm decor đọc cả 5 nhà đặt sẵn với bán kính nền của chúng, `TREE.radiusM` 1,5 và `BUILD.gapM`.

### 6.5 Asset cho MVP

| Game | Có sẵn | Còn thiếu | Ai làm, khi nào |
|---|---|---|---|
| Rồng | 13 GLB pine-river (`public/assets/dragon-hold/models/m0b/props/`); 8 ô đất, 4 decal (phiếu 001, 006) | Spike sẽ nói (có thể: đèn, rào, đá vách, hoa) | Nếu thiếu: danh sách ảnh → một lô ảnh Codex → chủ dự án dựng Tripo |
| Lời Gọi | Bộ tranh `art-src/scenery/meadow/` (12 loại × v1, v2: mountain-pine, bamboo-clump, almond-tree, raspberry-bush, tall-grass, reed-clump, wildflowers, fern, rock-small, rock-medium, rotten-log, canopy-block), `scenery/shared/tree-stump`, chấm 8,5–9,5; phông `backdrops/w1-silverfall/`; ảnh nguồn 3 mốc `landmarks/{vach-thac-bac,cau-go,choi-canh-doi}.png` | 6 ô đất liền mép, 2 tờ decal (đất mòn; hoa, sỏi); nền 3 ảnh mốc chưa phẳng; 3 model Tripo | Giai đoạn 4: một lô ảnh Codex (ô đất, decal) theo quy ước `art-src/scenery/<vùng>/`; sửa nền mốc bằng `tools/art-normalize`; chủ dự án dựng 3 mốc trên Tripo |

Giai đoạn 1–2 không thêm ảnh nào. Không chép media giữa các game: khi cần model của game khác, mỗi game nhập vào media của chính nó (`prepare-models --import`).

### 6.6 MVP xong khi

1. **Spike** (6.2) có 12 ảnh, điểm, nguyên nhân, số đo, danh sách luật. Điểm trung vị ≥ 7/10, không ảnh nào dưới 6, phép nheo mắt vẫn đọc rõ làn.
2. **CLI:** `node tools/map-factory/cli.mjs build tools/map-factory/maps/dragon-hold/L2-cau` và `…/typing-defense/w1-silverfall` chạy hai lần cho cùng từng byte; băm vàng từng lớp đạt.
3. **Phép kiểm:** luật decor 6.4 với mẫu hỏng; luật ô ẩn của Rồng; đúng 36 cây luật, đúng id và vị trí; cầu phủ kín rect; ước ngân sách trong trần 4.2.
4. **Thử sửa:** đổi mật độ thực vật 350 ‰ → 550 ‰ thì chỉ băm L6 và các lớp sau đổi, tập cây cũ nằm trọn trong tập mới.
5. **Trong Rồng** (giai đoạn 3): bố cục do lõi sinh lúc nạp tái hiện được bản spike; 12 ảnh ≥ 8/10; chênh khung ≤ 2 ms trung bình, ≤ 3 ms p95 dưới `dh-bench`; draw call và tam giác trong 4.2; phần sinh ≤ 300 ms; golden của Rồng không đổi; chủ dự án chơi.

Ngưỡng 8 (không phải 7) khi vào game, vì bố cục sửa rẻ: chỉ sửa spec, không tốn credit.

---

## 7. Thư mục

```text
docs/tools/MAP_FACTORY.md                     tài liệu này
docs/tools/map-factory/spike-l2-cau.md        kết quả spike (Claude)

shared/game-kit/map/          lõi TS thuần: không three, không DOM, không trig
  tsconfig.json               extends ../tsconfig.json; "include": ["./**/*.ts"]; "erasableSyntaxOnly": true
  index.ts  hash.ts  seeds.ts  raster.ts  edt.ts  scatter.ts  along.ts
  spec.ts  layout.ts  budget.ts
  layers/   fields.ts  height.ts  water.ts  paths.ts  dressing.ts  vegetation.ts  paint.ts
  checks/   decor.ts
  *.test.ts                   vitest, theo nếp của kit; lint.test.ts

tools/map-factory/
  README.md
  cli.mjs                     validate | build | check   (guide, diff: sau)
  lib/ts-hook.mjs             hook nạp .ts (Node 24)
  adapters/                   extract.mjs  typing-defense.mjs  dragon-hold.mjs
  registry/                   phiếu 025: scan-assets.mjs, out/, test/; kits/ (sau)
  maps/
    dragon-hold/L2-cau/           map.spec.json   golden/layer-hashes.json
    typing-defense/w1-silverfall/ map.spec.json   golden/layer-hashes.json
  test/                       node --test; fixtures/ (lớp chơi đã trích, spec hỏng, decor hỏng)
  .cache/  out/               .gitignore: bản trích từ git archive, bố cục, báo cáo
```

**Sau khi đưa vào game,** mỗi game tự đủ, không gọi repo cha lúc build hay lúc chạy:

```text
games/dragon-hold/
  kit.config.json                     thêm "map"
  src/kit/map/                        chép bằng kit sync
  src/content/maps/L2-cau.spec.json   (Git)
  src/view/terrain.ts, scatter.ts     đọc bố cục do lõi sinh lúc nạp
  tests/content/map-layout.test.ts    băm vàng từng lớp

games/typing-defense/                 ở bước 1C
  kit.config.json                     thêm "three", "map"; mã 3D trong chunk nạp sau
  src/content/maps/w1-silverfall.spec.json
```

Spec trong game nằm ngoài phần `compile.ts` băm, nên băm nội dung và golden luật của Lời Gọi không đổi. `tools/map-factory/maps/` chỉ giữ mẫu và bản nháp; sau khi đưa vào game, bản trong game là sự thật.

---

## 8. MapSpec v0

### 8.1 Ví dụ đầy đủ: `w1-silverfall`

Chọn Lời Gọi làm ví dụ đầy đủ vì nó có nhiều luật nhất (xây khắp sân, cây luật, cầu, mỏ). Tọa độ là cm nguyên.

```json
{
  "format": "map-spec/0",
  "id": "w1-silverfall",
  "game": "typing-defense",
  "title": "Đồng Cỏ Thác Bạc (Silverfall Meadow)",
  "unit": "cm",
  "seed": 20261027,
  "generator": {
    "factory": "0.1.0",
    "layers": { "fields": 1, "height": 1, "water": 1, "paths": 1, "dressing": 1, "vegetation": 1, "paint": 1 }
  },
  "gameplay": { "adapter": "typing-defense@1", "commit": "86b7258", "hash": "<sha256 của bản trích chuẩn>" },
  "registry": { "scan": "2026-10-27", "kit": "meadow@1" },
  "extent": { "fieldHalfCm": 4800, "skirtCm": 4000, "cellCm": 50, "skirtCellCm": 200 },
  "review": { "pitchesDeg": [55, 85, 15], "yawsDeg": [0, 90, 180, 270] },
  "layers": {
    "height": {
      "reliefCm": 60,
      "stamps": [
        { "id": "rainbow-hill", "kind": "hill", "at": [200, -2100], "radiusCm": 800, "heightCm": 260, "rule": "td-hill-range" },
        { "id": "silverfall-cliff", "kind": "cliff", "line": [[-4800, -5200], [1600, -5200]], "heightCm": 900, "outsideField": true }
      ],
      "flatten": [{ "under": "routes", "marginCm": 120 }, { "under": "keep", "radiusCm": 900 }]
    },
    "water": {
      "streams": [{ "id": "silver-stream", "fromGameplay": "water/0", "wobbleCm": 40, "bankCm": 80 }],
      "falls": [{ "id": "silverfall", "at": [-1000, -5200], "widthCm": 700, "dropCm": 900 }],
      "ponds": []
    },
    "paths": {
      "fromGameplay": "routes",
      "footpaths": [
        { "id": "fp-keep-ore", "from": "keep", "to": "node/1", "widthCm": 110 },
        { "id": "fp-bridge-west", "from": "bridge/1", "to": [-3600, 3400], "widthCm": 100 }
      ],
      "wornEdgeCm": 90
    },
    "dressing": {
      "along": [
        { "proto": "lamp-post", "on": "routes", "everyCm": 1600, "sideCm": 280, "alternate": true, "clearOnBuild": true, "skipNearCm": { "bridge": 400, "gate": 800 } },
        { "proto": "fence-segment", "on": "footpaths", "everyCm": 240, "sideCm": 160, "maxRun": 6, "clearOnBuild": true }
      ],
      "landmarks": [
        { "proto": "wooden-bridge", "fit": "bridge/0" },
        { "proto": "wooden-bridge", "fit": "bridge/1" },
        { "proto": "silverfall-cliff", "at": [-1000, -5400], "yawDeg": 0 },
        { "proto": "watchtower", "at": [5600, -2400], "yawDeg": 200, "note": "vòng ngoài; lên đồi khi sim có nền (6.4)" }
      ]
    },
    "vegetation": {
      "gameplayTrees": { "fromGameplay": "trees", "mix": { "mountain-pine": 2, "almond-tree": 1 }, "mark": "chop-chips" },
      "decorTrees": { "where": "buildable", "clearOnBuild": true, "densityPermille": 120, "minGapToGameplayTreeCm": 400,
                      "mix": { "bamboo-clump": 2, "almond-tree": 1, "mountain-pine": 1 } },
      "groves": { "where": "noBuild", "count": [6, 9], "radiusCm": [500, 1000], "densityPermille": 600,
                  "mix": { "mountain-pine": 3, "bamboo-clump": 2, "almond-tree": 1 } },
      "edge": { "bandCm": 1400, "proto": "canopy-block", "densityPermille": 850 },
      "clutter": { "where": "buildable", "densityPermille": 300, "clearOnBuild": true,
                   "mix": { "raspberry-bush": 2, "tall-grass": 3, "fern": 1, "rock-small": 1, "rotten-log": 1 } },
      "minGapCm": 220,
      "cellCm": 800
    },
    "paint": {
      "canopyDirtCm": 260, "junctionDirtCm": 450, "routeWornCm": 90, "tintNoiseCm": 4000,
      "decals": { "wildflowers": 400, "pebbles": 150 },
      "hints": [{ "kind": "alluvial", "at": [1600, 2800], "radiusCm": 700, "designOnly": true }]
    }
  },
  "exclude": [
    { "id": "keep-word-cards", "poly": [[-800, 3200], [800, 3200], [800, 4800], [-800, 4800]], "reason": "thẻ chữ của Lũy" }
  ],
  "pins": [
    { "keep": "veg:groves:c-5_-4:2" },
    { "proto": "almond-tree", "at": [3800, -1200], "yawDeg": 40, "scalePermille": 1100, "variant": "red", "clearOnBuild": true }
  ],
  "budget": {
    "high": { "propTriangles": 550000, "drawCalls": 40, "loadMs": 300 },
    "medium": { "propTriangles": 300000, "drawCalls": 30, "loadMs": 300 }
  }
}
```

**Rồng `L2-cau`** dùng cùng vỏ, gọn hơn:

```json
{
  "format": "map-spec/0", "id": "L2-cau", "game": "dragon-hold", "unit": "cm", "seed": 20261028,
  "generator": { "factory": "0.1.0", "layers": { "fields": 1, "height": 1, "water": 1, "paths": 1, "vegetation": 1, "paint": 1 } },
  "gameplay": { "adapter": "dragon-hold@1", "commit": "3f3390d", "hash": "<sha256>" },
  "registry": { "scan": "2026-10-27", "kit": "pine-river@1" },
  "extent": { "playRadiusCm": 3200, "worldHalfCm": 7200, "cellCm": 50, "skirtCellCm": 200 },
  "review": { "pitchesDeg": [40, 55, 75], "yawsDeg": [0, 90, 180, 270] },
  "layers": {
    "height": { "stamps": [{ "id": "north-bluff", "kind": "cliff", "line": [[-3000, -5200], [2000, -5600]], "heightCm": 800, "outsidePlay": true }] },
    "water": { "river": "fromGameplay", "ponds": [{ "id": "west-pond", "at": [-1800, 2200], "radiusCm": 450 }] },
    "paths": { "footpaths": [{ "id": "fp-pond", "from": "dais", "to": "pond/west-pond", "widthCm": 90 }], "neverEndAt": "slots" },
    "vegetation": { "groves": { "count": [5, 8], "radiusCm": [400, 900], "densityPermille": 650 }, "keepClearOf": ["lanes", "sky", "slots", "dais"] },
    "paint": { "canopyDirtCm": 240, "routeWornCm": 80 }
  },
  "budget": { "high": { "propTriangles": 550000, "drawCalls": 40, "loadMs": 300 } }
}
```

### 8.2 Ghi chú từng trường

**Đơn vị và số**
- Mọi tọa độ, độ dài là số nguyên cm. Góc là số nguyên độ; tỉ lệ là phần nghìn (`Permille`).
- Lõi không tính sin, cos, atan2. Hướng dọc đường là vector chia `Math.sqrt`. Đổi vector ra góc bằng bảng tra tan số nguyên theo bát phân.
- Trục giống game: x đông, z nam, y lên.
- Rồng: 1 cm = 600 u, đổi chính xác. Lời Gọi dùng mét số thực, bằng cm / 100. Tọa độ nút hiện nay của cả hai game có tối đa 2 chữ số thập phân (ví dụ −25,5 và −25,48), nên đổi sang cm không mất gì. Đường cong lấy mẫu thì làm tròn tới cm gần nhất.

**Seed**
- `seed` là gốc. Seed mỗi lớp là `hash32(seed, tênLớp, generator.layers[tênLớp])`.
- Đổi `seed` thì mọi decor xáo lại. Đổi `layers.vegetation` thì chỉ L6, L7 đổi, vì đất dưới tán đọc vị trí cây.
- Rải theo ô `cellCm`, mỗi ô một seed. Sửa một góc bản đồ chủ yếu đổi các ô quanh đó. Đây là tính chất đo được, không phải bảo đảm (phiếu 030 báo bán kính thay đổi thật).

**Phiên bản**
- `generator.factory` là bản của lõi; `generator.layers` là bản thuật toán từng lớp. Đổi thuật toán thì tăng số của lớp đó; băm lớp đổi theo, có chủ ý.
- Bố cục ghi lại cả hai, cùng băm spec, băm lớp chơi và md5 từng GLB đã dùng.

**Lớp chơi** (`gameplay`)
- Ở repo cha: `adapter` là bộ đọc của game và phiên bản của nó; `commit` là commit của repo game; `hash` là sha256 của bản trích chuẩn (JSON khóa sắp xếp, số nguyên cm).
- Bộ đọc lấy nội dung bằng `git -C <repo game> archive <commit>` vào `.cache/`, không đọc cây làm việc đang sửa.
- Chỉ băm phần bản đồ đã trích và các hằng số nó dùng (Lời Gọi: `SLICE_1A.map`, `BUILD`, `TREE`, `RALLY`). Đổi đợt quái không làm lệch khóa.
- Muốn đổi lớp chơi thì làn của game sửa nội dung game; spec chỉ cập nhật `commit` và `hash`.
- Trong game (sau khi đưa vào): game đưa thẳng `MapDef` của mình vào lõi; không còn `commit`.

**Ghim** (`pins`, `exclude`)
- `keep` giữ một vật đã sinh, theo id ổn định `lớp:nguồn:ô:k`.
- Thêm vật cụ thể bằng `proto` và `at`.
- `exclude` và `include` là đa giác vẽ tay: áp trước khi rải (vùng cấm) và sau khi rải (ghi đè).

**Khóa lớp** (`locks`): định dạng dành sẵn, làm ở giai đoạn 5. Khi đó build hỏng nếu một lớp đã khóa đổi băm, trừ khi chạy `--unlock <lớp>`. Đây là cách làm "giữ đường, giữ Lũy, chỉ sinh lại cây" của đề xuất §14. Trước đó, băm vàng từng lớp trong test đã làm việc này.

**Tham chiếu model**
- `proto` (ví dụ `mountain-pine`) là tên trong file kit `registry/kits/<kit>.json`.
- Kit trỏ tới id trong sổ 025 (`<game>:<id runtime>`) cho model, hoặc ô atlas cho billboard. Spec không bao giờ trỏ thẳng vào đường dẫn file.
- `proto` viết tiếng Anh dạng kebab-case, theo luật "In-game names" (27/10). Tên hiện ra cho người chơi (Watchtower, Wooden Bridge) đi qua đợt đặt tên của từng game.

**Ngân sách** (`budget`): trần cho từng tier. `propTriangles` là tam giác prop của bản đồ (không tính lưới đất, chưa tính bóng); `drawCalls` ước bằng công thức 4.2; `loadMs` là trần phần sinh lúc nạp.

### 8.3 Lớp chơi đã trích (cm nguyên)

Lời Gọi (rút gọn):

```json
{
  "format": "map-gameplay/0", "adapter": "typing-defense@1", "commit": "86b7258",
  "unit": "cm",
  "field": { "halfCm": 4800, "buildHalfCm": 4600 },
  "rules": { "roadHalfCm": 190, "roadClearCm": 190, "keepClearCm": 1100, "gapCm": 100,
             "treeRadiusCm": 150, "footprintCm": { "S": 200, "M": 230, "L": 270, "XL": 350 } },
  "gate": [-1000, -4600], "keep": [0, 4000],
  "routeKnots": [
    [[-1000, -4600], [-400, -4000], [600, -3400], [-1200, -2000], [-1000, 0], [0, 1200], [-600, 2000], [600, 3000], [0, 4000]],
    [[-1000, -4600], [-400, -4000], [600, -3400], [1600, -2000], [1200, 200], [0, 1200], [-600, 2000], [600, 3000], [0, 4000]]
  ],
  "routes": [["mỗi 25 cm theo groundLanes của game: [x, z] cm …"], ["…"]],
  "fly": { "points": [[-1000, -4600], [2000, -2000], [0, 4000]], "heightCm": 300 },
  "water": [{ "x0": -2550, "x1": -2250, "z0": -4800, "z1": 4800 }],
  "bridges": [{ "x0": -2550, "x1": -2250, "z0": -1550, "z1": -1250 }, { "x0": -2550, "x1": -2250, "z0": 2450, "z1": 2750 }],
  "nodes": [{ "at": [2600, -3000], "richness": 3 }, { "at": [-1200, 3200], "richness": 1 }, { "at": [-3400, 800], "richness": 2 }],
  "trees": [[-2100, -4400], [-1750, -4450], "… đủ 36 cây; chỉ số là id"],
  "preset": [
    { "kind": "archer", "at": [-800, 1200], "footprintCm": 200 },
    { "kind": "cannon", "at": [700, 1200], "footprintCm": 230 },
    "… barracks (300, 1800), gold-mine (2600, -3000), farm (-1700, 4000), mỗi nhà một bán kính nền"
  ]
}
```

Bán kính nền thật của từng nhà lấy từ nội dung game (cỡ S/M/L/XL của nhà đó); hai số trên chỉ minh họa.

Rồng (rút gọn):

```json
{
  "format": "map-gameplay/0", "adapter": "dragon-hold@1", "commit": "3f3390d", "unit": "cm",
  "dais": { "at": [0, 0], "radiusCm": 400 },
  "lanes": [
    { "id": "cau", "halfWidthCm": 150, "points": [[850, -2900], [500, -2250], [220, -1540], [120, -1000], [40, -600]],
      "bridges": [{ "fromCm": 1050, "toCm": 1840, "halfWidthCm": 170 }] },
    { "id": "suoi", "halfWidthCm": 130, "points": [[-3000, 700], "…"], "fords": [{ "fromCm": 690, "toCm": 1400 }] }
  ],
  "sky": [{ "id": "troi", "points": [[3050, -850], [2000, -700], [730, -180]], "altitudeCm": 300 }],
  "slots": [{ "id": "cau-t1", "kind": "trap", "lane": "cau", "at": [660, -2548] }, "… 11 ô làn, 6 ô nhà"],
  "river": { "points": [[7000, -3300], "…"], "widthsCm": [800, "…"], "depthCm": 120, "bankCm": 40 }
}
```

### 8.4 Bố cục (đầu ra) và file kit

Bố cục là dữ liệu trong bộ nhớ của game. CLI ghi ra `out/layout.json` để xem và để test; chỉ vào Git làm golden khi bản đồ được chỉnh tay.

```json
{
  "format": "map-layout/0", "map": "w1-silverfall",
  "inputs": { "spec": "<sha256>", "gameplay": "<sha256>", "kit": "meadow@1", "assets": { "watchtower": "<md5 tier high>" } },
  "generator": { "factory": "0.1.0", "layers": { "…": 1 } },
  "layers": {
    "height": { "hash": "…", "stamps": [], "noise": { "seed": 0, "reliefCm": 60 } },
    "vegetation": { "hash": "…", "protos": ["mountain-pine", "bamboo-clump"],
                    "items": [[0, -3120, 2210, 135, 1040, 0, 1, "veg:groves:c-4_2:1"]] }
  },
  "stats": { "instances": 4180, "estPropTrianglesHigh": 412000, "estDrawCallsHigh": 31 },
  "checks": [{ "id": "decor-on-buildable", "status": "PASS" }]
}
```

Mỗi vật là `[chỉ số proto, x cm, z cm, góc độ, cỡ ‰, biến thể, clearOnBuild 0/1, id]`. Lưới (mặt nạ, trường) không ghi ra; game tính lại từ vector.

File kit `registry/kits/<kit>.json` chứa phần sổ quét không đo được (mục 4.5). Với Lời Gọi, `render: "billboard"` trỏ tới ô atlas do `scripts/td/prepare-scenery.mjs` (bước 1C, §23.10) làm ra; `nominalHeightCm` lấy từ bảng ảnh `03-2d-scenery-ui-vfx.md` (thông núi 10 m, bàng 8 m, tre 7 m…).

### 8.5 Quy tắc tất định cho lõi

1. Tọa độ lớp chơi và đầu ra là số nguyên cm. Băm dùng `Math.imul` và `>>> 0`.
2. Không `Math.random`, `Date`, `performance` trong mã lõi. Mọi lần rút ngẫu nhiên đi qua một luồng có tên. Test (`*.test.ts`) được dùng `performance` để in thời gian.
3. Không trig, `pow`, `hypot`, `**`. Chỉ `+ - * /`, `Math.sqrt` (spec bảo đảm làm tròn đúng), `Math.floor`, `Math.round`.
4. Thứ tự cố định: sắp xếp với hàm so sánh toàn phần, hòa thì so id; duyệt mảng, không duyệt object có khóa lẫn số và chữ; cộng theo thứ tự cố định.
5. Lượng tử hóa trước khi ghi JSON. Băm từng lớp; băm vàng nằm trong test.
6. Ghi phiên bản lõi và từng lớp vào đầu ra.
7. Mã dựng hình của game được dùng số thực, vì nó không vào băm.
8. Lint trong vitest dùng bộ quét TypeScript, bỏ qua chú thích và chuỗi. `enum`, `namespace`, tham số thuộc tính bị chặn bằng `erasableSyntaxOnly` trong `map/tsconfig.json`.

---

## 9. Các giai đoạn

### 9.1 Bảng giai đoạn

| Giai đoạn | Nội dung | Ai | Cổng |
|---|---|---|---|
| 0 (xong) | Sổ model 3 game: phiếu 025 (commit `90e4e3fe`, 800 GLB, 19/19 test). Tài liệu này | Codex, Claude | — |
| 1 Thử và nền (song song) | Claude: spike bố cục trên Rồng L2-cau (6.2). Codex: phiếu 027–029 (lõi tất định và lint, bộ đọc lớp chơi, trường) | Claude + Codex | Spike đạt 6.6 mục 1, hoặc ghi rõ nguyên nhân; 027–029 đạt kiểm và đã duyệt |
| 2 Lõi theo luật của spike | Claude viết luật spike thành thuật toán chính xác trong phiếu; Codex 030–033 (rải, spec, ghép bố cục và CLI, đặt dọc đường cong); Claude viết lớp lùm cây và lối mòn | Codex + Claude | 6.6 mục 2–4 cho cả hai bản đồ; bố cục từ CLI tái hiện bản spike |
| 3 Rồng vào game | Đồng bộ module `map` vào Rồng; sinh lúc nạp; `terrain.ts`, `scatter.ts` đọc bố cục; băm vàng từng lớp | Làn Rồng (khi rảnh) | 6.6 mục 5 |
| 4 Lời Gọi 1C | Bộ đọc + luật decor 6.4; đất, billboard atlas, phông; một lô ảnh (6 ô đất, 2 tờ decal); sửa nền 3 ảnh mốc; chủ dự án dựng 3 mốc Tripo; chunk nạp sau | Làn Lời Gọi, Codex, chủ dự án | Trong game ≥ 8/10 ở 3 góc × 4 hướng; §25.12 và §23.10 đạt; golden luật không đổi; chủ dự án chơi |
| 5 Mở rộng | Rồng: bộ đề xuất lớp chơi (16 mẫu L1–L4, `validate-map`, bot, khóa băm bố cục) cho 520 ải; kit thứ hai; khóa lớp, `diff`, `guide.svg`, file kit và `check-kit`; KTX2 | Làn Rồng + Map Factory | Cổng của từng game |
| 6 Tùy chọn | TopoTopo 0.4.0 thử 1–2 ngày (vách, lòng thác). Xuất GLB cho engine khác. WFC TS tự viết khi có game dungeon. Bộ sinh dải set-piece cho hành lang Tuyến Cuối. Lớp MCP mỏng gọi CLI | Khi cần | Mỗi việc một cổng riêng |

### 9.2 Phiếu Codex

Quy ước chung cho mọi phiếu:
- chạy trong worktree riêng của repo cha (9.4); không mạng; không cổng; không trình duyệt; không lệnh git có ghi (`git archive`, `git status` được phép);
- không ghi vào `games/**`;
- không cài gói, chỉ dùng thư viện chuẩn của Node và `node_modules` sẵn có của `shared/game-kit` (TypeScript 6.0.3, vitest);
- `git status --short` chỉ được có các đường dẫn cho phép;
- Claude đọc diff, chạy lại kiểm và phản biện trước khi commit.

| # | Việc | Phạm vi ghi | Kiểm (bắt buộc) | Sau |
|---|---|---|---|---|
| 027 | Lõi tất định: `hash32`, `layerSeed`, `cellSeed`, `rankOf`; lint tất định | `shared/game-kit/map/{tsconfig.json,index.ts,hash.ts,seeds.ts}`, `map/*.test.ts` | `pnpm --dir shared/game-kit exec vitest run map` đạt; `tsc -p map/tsconfig.json` đạt; bảng 12 băm vàng (Claude ghi sẵn trong phiếu) khớp. Lint dùng `ts.createScanner`: bắt từng token cấm trong mẫu mã (`Math.sin/cos/tan/atan2/pow/hypot/exp/log/cbrt/random`, `Date`, `performance`, toán tử `**`); **không** bắt `/** … */`, chuỗi `"enumerate"`, chú thích `// Math.sin`; cho phép `performance` trong `*.test.ts`. Một mẫu có `enum`, dịch trong RAM bằng API TypeScript với tùy chọn của `map/tsconfig.json`, phải báo lỗi (không để file mẫu trong `map/`) | — |
| 028 | Bộ đọc lớp chơi ở commit ghim, cho 2 bản đồ | `tools/map-factory/{lib/ts-hook.mjs,adapters/*.mjs,test/adapters.test.mjs,test/fixtures/gameplay/*.json}`; thêm `tools/map-factory/.cache/` và `out/` vào `.gitignore` | `node --test tools/map-factory/test/*.test.mjs` đạt; chạy 2 lần cùng byte; `git -C games/<id> status --porcelain` trước và sau giống hệt. Lời Gọi: 36 cây đúng thứ tự; 5 nhà đặt sẵn có bán kính nền; `TREE.radiusM`, `BUILD.roadClearM/keepClearM/gapM`; tuyến lấy mẫu mỗi 25 cm từ `groundLanes` của game, lệch ≤ 1 cm so với `Lane.xs/zs`. Rồng: làn từ `compileLanes`, u chia hết cho 600 ở mọi điểm (in số điểm không chia hết, phải bằng 0); 6 ô nhà, 11 ô làn. Băm bản trích ở `10ce627^` bằng băm ở `10ce627` (commit chỉ đổi đợt quái); băm đổi khi sửa một tọa độ cây trong RAM | — |
| 029 | Trường: tô lưới (đường có bề rộng, rect, đĩa, đa giác) và biến đổi khoảng cách số nguyên (Meijster) | `shared/game-kit/map/{raster,edt}.ts`, test | Bằng đúng cách tính vét cạn trên 200 lưới có seed (≤ 64²); băm vàng bộ trường của hai mẫu ở 50 cm (dùng fixture của 028); in thời gian, đích ≤ 60 ms cho 4 trường 288² trên M4; lint 027 đạt | 027, 028 |
| 030 | Rải theo ô, xếp hạng, mật độ theo vị trí, có ghim | `shared/game-kit/map/scatter.ts`, test | Khoảng cách tối thiểu đúng với mọi cặp (vét cạn); trên 100 seed, tập 350 ‰ nằm trọn trong tập 550 ‰; không vật nào trong vùng cấm; ghim `keep` sống khi giảm mật độ; ghim thêm thì xóa vật trong khoảng cách tối thiểu; băm vàng. **In** bán kính thay đổi khi sửa một đĩa cấm (trung vị, p95, lớn nhất trên 100 seed): số báo cáo, không phải cổng | 029, spike |
| 031 | MapSpec v0 tối thiểu: kiểu, `validateSpec`, lệnh `cli validate` | `shared/game-kit/map/spec.ts`, test, `tools/map-factory/cli.mjs`, `maps/*/*/map.spec.json` (chép từ 8.1), `test/fixtures/bad-spec/` | 2 spec mẫu thoát 0; 6 spec hỏng thoát 1 với đúng mã lỗi (số lẻ, ‰ > 1000, proto lạ, băm lớp chơi lệch, id ghim sai dạng, thiếu ngân sách); vitest, `node --test`, `tsc` đạt | 027, 028, spike |
| 032 | Ghép bố cục L0 + L1 + L6, băm từng lớp, `cli build` và `cli check`, ước ngân sách, kiểm decor | `shared/game-kit/map/{layout,budget}.ts`, `checks/decor.ts`, `layers/{fields,vegetation}.ts` (thuật toán Claude ghi sẵn từ spike), `cli.mjs`, test | Build hai bản đồ hai lần cùng byte; băm vàng từng lớp; đổi tham số thực vật chỉ đổi băm L6. Mẫu decor hỏng thoát 1 với đúng mã: Watchtower ở (9, −24) không có nền sim (`decor-on-buildable`), cây cảnh trên mặt đường, decor đè nhà đặt sẵn, cây cảnh cách cây luật < 4 m, lối mòn dừng ở ô của Rồng. In bảng ngân sách theo công thức 4.2. Bố cục chỉ ghi vào `out/` | 029, 030, 031 |
| 033 | `along.ts`: đặt vật dọc đường cong, theo thuật toán ghi trong phiếu | `shared/game-kit/map/along.ts`, test | Khoảng cách theo cung giữa hai vật liền nhau = `everyCm` ± 1 cm; lệch ngang = `sideCm` ± 1 cm; góc (bảng tan số nguyên) lệch ≤ 1° so với `Math.atan2` (chỉ trong test); bỏ đúng các cửa sổ cấm; băm vàng | 027, spike |

**Thứ tự:** 027 → 028 → 029, song song với spike. Sau spike: 031 → 033 → 030 → 032; phiếu nào spike cho thấy không cần (ví dụ 033 nếu đồ dọc đường không giúp) thì bỏ. Mỗi phiếu khoảng 10–60 phút chạy, vừa một cửa sổ hạn mức.

**Không giao Codex** (cần mắt hoặc quyết định thiết kế): chọn chỗ lùm cây, đường đi của lối mòn, tham số sơn đất, chấm ảnh. Claude làm, rồi ghi thành thuật toán chính xác trước khi giao phần còn lại.

**Để sau** (giai đoạn 4–5, chưa đánh số): file kit và `check-kit`; `guide.svg`; `diff`; khóa lớp; lô ảnh Lời Gọi (6 ô đất, 2 tờ decal); sửa nền ảnh mốc V50–V52.

### 9.3 Làn của Claude

| Làn | Phạm vi | Được ghi | Xong khi |
|---|---|---|---|
| S Spike bố cục (ngay) | 6.2 | `games/.wt-dh-mapspike/**` (nhánh `map-spike`, không gộp), `docs/tools/map-factory/spike-l2-cau.md` | 6.6 mục 1, hoặc nguyên nhân giới hạn đã ghi |
| 1 Lõi Map Factory | Viết phiếu 027–033 và dòng trong `CODEX_QUEUE.md`; duyệt, phản biện, sửa, commit từng phiếu; viết lớp lùm cây, lối mòn, sơn đất từ spike; README | `docs/tools/**`, `docs/codex-queue/027–033*`, `docs/CODEX_QUEUE.md`, `shared/game-kit/map/**`, `tools/map-factory/**` (theo lịch 9.4) | 6.6 mục 2–4 |
| 2 Rồng vào game | Làn Rồng làm khi rảnh: `kit.config.json`, bố cục lúc nạp, `terrain.ts`, `scatter.ts`, test băm vàng, đo | `games/dragon-hold/**` theo làn | 6.6 mục 5 |
| 3 Lời Gọi 1C | Làn Lời Gọi: bộ đọc trong game, luật decor 6.4, đất, billboard, mốc, chunk nạp sau, `DRIFT.md` | `games/typing-defense/**` theo làn | Cổng giai đoạn 4 |

### 9.4 Nhánh, worktree và ai ghi đâu

- **Nhánh `map-factory` ở repo cha**, tách từ nhánh làm việc hiện tại `feat/space-typing-admin-uiux` (đã có phiếu 025 `90e4e3fe`, bảng tên 026 và tài liệu này). Điều phối viên quyết ngày 27/10: không cherry-pick sang `main`. Mỗi phiếu duyệt xong được commit trên `map-factory`, rồi điều phối viên gộp về `feat/space-typing-admin-uiux`.
- **Codex chạy trong một worktree riêng** của nhánh đó (ví dụ `/Users/toandx/htdocs/typing-game-wt/map-codex`), gọi `tools/codex-run/run.sh` với thư mục làm việc ấy. Bộ đọc lấy nội dung game từ repo game của bản checkout chính bằng `git archive` (chỉ đọc).
- **Mỗi thư mục một người ghi tại một thời điểm.** Claude chỉ ghi `shared/game-kit/map/layers/` khi không có phiếu Codex nào đang mở trên `shared/game-kit/map/`. Ở giai đoạn 1, Claude chỉ ghi worktree spike và `docs/`.
- **Hàng Codex:** phiếu mã Map Factory xếp sau các phiếu ảnh đang chờ (luật hạn mức 27/10). Giai đoạn 1–2 không có phiếu ảnh.
- **Kit sync** vào game do điều phối viên chạy ở bước đưa vào game, có dòng `DRIFT.md`.

---

## 10. Độ phức tạp (ước thật)

| Giai đoạn | Claude | Codex | Chủ dự án |
|---|---|---|---|
| 1 Thử và nền | Spike 1,5–2 ngày; duyệt 3 phiếu 0,5 ngày | 027–029, khoảng 1–2 cửa sổ | 10 phút xem 12 ảnh |
| 2 Lõi | 2–3 ngày (luật từ spike thành thuật toán, lùm cây, lối mòn, duyệt) | 030–033, khoảng 2 cửa sổ | 0 |
| 3 Rồng vào game | 2–3 ngày của làn Rồng (sinh lúc nạp, nối `terrain.ts`, `scatter.ts`, golden, đo, 12 ảnh) | — | 20 phút chơi |
| 4 Lời Gọi 1C | Phần Map Factory khoảng 1,5 ngày; bộ dựng billboard của §23.10 là việc của 1C dù có Map Factory hay không (3–4 ngày) | 1 lô ảnh, 1 phiếu sửa nền ảnh | Khoảng 1 giờ dựng 3 mốc trên Tripo; 20 phút chơi |
| 5 Rồng 520 ải | 5–8 ngày (bộ đề xuất lớp chơi, `validate-map`, bot) | Vài phiếu kiểm hình học | Duyệt mẫu bố cục |

- **Tới bản đồ đầu tiên trong game (Rồng):** khoảng 6–8 ngày agent; 1,5–2 tuần lịch, tùy hạn mức Codex và lúc làn Rồng rảnh.
- **Thời gian chủ dự án tới lúc đó:** khoảng 30 phút.
- **Phần khó thật** không nằm ở thuật toán. Nó nằm ở luật bố cục cho ra cảm giác "có người sống" và ở sơn đất đẹp. Cả hai cần nhìn và chỉnh, nên spike đi trước và Claude giữ phần đó.

---

## 11. Dùng lâu dài (câu H)

**Phần chung**, viết một lần:
- vỏ spec: id, seed, đơn vị, phiên bản, ghim, khóa, ngân sách, tham chiếu sổ;
- băm và seed theo lớp, theo ô;
- tô lưới và biến đổi khoảng cách;
- dấu cao độ;
- rải theo hạng;
- đặt vật dọc đường cong;
- tham số sơn đất;
- định dạng bố cục;
- khung phép kiểm và ước ngân sách;
- sổ model và file kit;
- CLI và kỷ luật tất định.

**Phần riêng mỗi game:**
- bộ đọc lớp chơi (gọi đúng hàm làn, đúng luật của game);
- luật decor (vật trang trí được nằm đâu theo luật sim);
- phép kiểm luật chơi;
- bộ đề xuất lớp chơi (ví dụ mẫu bố cục của Rồng);
- bộ kit;
- **cách vẽ**: Rồng vẽ model instanced, Lời Gọi vẽ billboard 2D. Vì vậy chưa làm module dựng hình dùng chung; chỉ tách phần chung khi hai game thật sự vẽ giống nhau.

| Thể loại | Dùng được lõi? | Phần phải viết riêng |
|---|---|---|
| Tower Defense (Lời Gọi, Rồng) | Có, đủ | Bộ đọc, luật decor; Rồng thêm bộ đề xuất bố cục |
| Farming | Có | Thửa ruộng (đa giác lùi mép: tự làm hoặc Clipper2), luật mùa |
| Fantasy RPG vùng nhỏ | Có, thêm chia chunk | Điểm nhiệm vụ; navmesh cho đi tự do (navcat 0.4.1 hoặc recast-navigation 0.43.1) |
| Cultivation RPG (Tu Tiên, đang dừng) | Có: sân, cổng, ô cơ quan, sơn đất, rải | Flow field, phông Sơn Môn |
| Survival (Tuyến Cuối) | Một phần: sổ, seed, đặt dọc đường cong, ngân sách | Bộ sinh dải set-piece cho hành lang; kit sci-fi; không cần địa hình |
| Dungeon | Một phần: sổ, seed, phép kiểm | Đồ thị phòng, WFC TS tự viết, bộ ô khớp cỡ |
| Shooter | Một phần: sổ, rải, ngân sách | Bố cục chỗ nấp, tầm nhìn, navmesh |
| Căn cứ sci-fi | Một phần: đồ dọc tường, sổ | Bộ ô mô-đun, WFC |
| Thế giới mở | Chỉ các phép toán | Streaming, LOD theo chunk, có thể cần bào mòn (TopoTopo là ứng viên); ngoài 12 tháng tới |
| Game trên Unity hoặc Unreal | Lõi chạy ở bước build (Node), xuất dữ liệu | Một bộ đọc trong engine đó (mục 5.2) |

**Trả lời thẳng câu H:** một Map Factory dùng chung là thực tế, nếu "chung" nghĩa là chung **phép toán, định dạng, sổ model và kỷ luật tất định**. Một bộ sinh "bấm nút ra bản đồ cho mọi thể loại" thì không thực tế, và không nên nhắm tới. Mỗi thể loại mới tốn một bộ đọc lớp chơi, một bộ luật decor, một cách vẽ và một bộ kit: khoảng 3–6 ngày agent, chưa tính kit. Chi phí đó nhỏ hơn nhiều so với dựng tay từng bản đồ.

---

## 12. GO / NO-GO

**GO, có sửa:**
- Làm Map Factory dạng lõi TS tất định trong kit + CLI ở repo cha; game ship spec và sinh bố cục lúc nạp; game tự dựng hình bằng mã sẵn có.
- Bắt đầu bằng spike bố cục 1–2 ngày trên Rồng L2-cau. Lời Gọi bản đồ 1 là mẫu CLI thứ hai và vào game ở bước 1C, theo thiết kế §23.10.
- Giao Codex 027–029 ngay (song song với spike), 030–033 sau spike; Claude giữ các làn ở 9.3.

**NO-GO:**
- GLB cả bản đồ làm đầu ra chạy trong game;
- `collision.glb`, `navmesh.json`;
- Blender MCP trong đường chính;
- phụ thuộc TopoTopo;
- WFC cho các game hiện có;
- Poly Haven, Kenney, Quaternius trong game ship;
- hướng Unity, Unreal cho các game hiện có.

**Điều kiện dừng và xem lại:**
- Sau spike, nếu điểm trung vị < 7:
  - nguyên nhân là bố cục: thêm tối đa 1 ngày chỉnh luật;
  - nguyên nhân là kit: dừng phiếu 030–033, làm danh sách món còn thiếu (ảnh Codex, rồi Tripo của chủ dự án) trước;
  - nguyên nhân là luật chơi (sân trống có chủ ý): báo làn Rồng và chủ dự án; Map Factory không sửa được.
- Phần sinh lúc nạp > 300 ms trên M4: chuyển sang sinh lúc build.
- Giai đoạn 2 vượt 2 lần ước tính: cắt bớt lớp (L5, lối mòn), giữ L6, L7.

**Chủ dự án nên biết (không chặn việc trước bước Lời Gọi 1C):**
- **Cảnh Lời Gọi:** giữ billboard 2D theo §23.10 (mặc định; bộ tranh `meadow` đã có và đã chấm, không tốn thêm việc của chủ dự án). Chuyển sang cây đá 3D Tripo là đổi thiết kế Lời Gọi, tốn khoảng 3–4 giờ dựng Tripo và credit web cho mỗi vùng. Chỉ cần quyết nếu bản billboard ở 1C dưới 8/10.
- **Thứ tự:** Rồng đi trước Lời Gọi vì có sân khấu 3D và bộ kit thật; chủ dự án đổi được nếu muốn.

---

## Nguồn (truy cập 27/10/2026)

**TopoTopo**
- https://github.com/topotopo-dev/topotopo (README; API metadata, commit, release, Actions)
- https://github.com/topotopo-dev/topotopo/blob/main/docs/release/v0.2-release-notes.md
- https://github.com/topotopo-dev/topotopo/blob/main/docs/release/v0.4-release-notes.md
- https://github.com/topotopo-dev/topotopo/blob/main/docs/nodes.md
- https://registry.npmjs.org/topotopo
- https://api.npmjs.org/downloads/range/2026-10-10:2026-10-27/topotopo
- https://topotopo.dev

**Blender**
- https://projects.blender.org/lab/blender_mcp
- https://www.blender.org/lab/mcp-server
- https://github.com/ahujasid/mcp-for-blender
- https://pypi.org/pypi/blender-mcp/json
- https://pypi.org/pypi/bpy/json
- https://docs.blender.org/manual/en/dev/addons/scene_gltf2.html
- https://developer.blender.org/docs/release_notes/5.0/python_api/
- https://www.blender.org/download/lts/
- https://gltf-transform.dev/cli

**Unity, Unreal**
- https://unity.com/en/blog/unity-ai-mcp-how-to-get-started (11/05/2026)
- https://docs.unity3d.com/Packages/com.unity.ai.assistant@2.0/manual/unity-mcp-get-started.html
- https://glama.ai/mcp/servers/@Singtaa/UnityMCP
- https://www.unrealengine.com/news/state-of-unreal-2026-top-news-from-the-show (trả 403; đọc qua kết quả tìm kiếm)

**Sinh thủ tục, WFC, tất định**
- https://www.boristhebrave.com/2020/04/13/wave-function-collapse-explained/
- https://www.boristhebrave.com/2021/04/10/dungeon-generation-in-unexplored/
- https://boristhebrave.github.io/DeBroglie/articles/constraints.html
- https://github.com/mxgmn/WaveFunctionCollapse
- https://github.com/kchapelier/wavefunctioncollapse
- https://sci.utah.edu/~chengu/street_sig08/street_project.htm
- https://80.lv/articles/using-wave-function-collapse-algorithm-for-dioramas
- https://www.jeremykun.com/2012/07/29/the-cellular-automaton-method-for-cave-generation/
- https://dev.epicgames.com/documentation/en-us/unreal-engine/landscape-splines-in-unreal-engine
- https://dev.epicgames.com/documentation/en-us/unreal-engine/python-api/class/PCGGenerateSeedSettings
- https://www.guerrilla-games.com/read/gpu-based-procedural-placement-in-horizon-zero-dawn
- https://hal.archives-ouvertes.fr/hal-00694525 (Emilien và cộng sự 2012)
- https://cemyuksel.com/research/sampleelimination/
- https://www.angusj.com/clipper2/Docs/Overview.htm
- https://tc39.es/ecma262/multipage/numbers-and-dates.html
- https://bugzilla.mozilla.org/show_bug.cgi?id=1823880
- https://webassembly.github.io/spec/core/appendix/profiles.html
- https://gafferongames.com/post/floating_point_determinism

**Asset và hiệu năng**
- https://polyhaven.com/license
- https://quaternius.com/license.html
- https://quaternius.com/packs/stylizednaturemegakit.html
- https://www.kenney.nl/support
- https://kaylousberg.itch.io/kaykit-forest
- https://styloo.itch.io/vil
- https://docs.ambientcg.com/license/
- https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html
- https://github.com/BinomialLLC/basis_universal
- https://github.com/KhronosGroup/3D-Formats-Guidelines/blob/main/KTXArtistGuide.md
- https://github.com/zeux/meshoptimizer
- https://aframe.io/docs/1.7.0/components/gltf-model.html
- https://github.com/agargaro/instanced-mesh
- https://threejs.org/docs/pages/LOD.html
- https://caniuse.com/mdn-api_webgl_multi_draw

**Trong repo**
- `docs/games/dragon-lane/05-presentation-audio-tech-split.md` §2, §8 (ô ẩn, ngân sách, nạp ải)
- `docs/games/dragon-lane/research/art-pipeline.md` §2, §5, §9 (đất, bản đồ là dữ liệu, kit rẻ)
- `games/.wt-dh-m0b/docs/changelog/2026-10-27-m0b-models.md` (đo M0b: 5,93 ms, p95 7,8 ms, 70 draw call)
- `games/.wt-dh-m0b/src/content/data/maps.ts`, `src/sim/lanes.ts`, `src/view/{terrain,scatter,water,paths,stage}.ts`
- `games/typing-defense/docs/td/TYPING_DEFENSE_DESIGN.md` §22.9 (bản đồ 1, mốc 3D), §23.6 (camera), §23.10 (cảnh 2D), §23.12 (StylePack, BiomeRecipe, BiomeArt, CivKit), §25.12 (hiệu năng), §26.1 (1C)
- `games/typing-defense/docs/td/BUILD_NOTES.md` §7.10 (gói "/" còn 13 byte)
- `games/typing-defense/src/content/{slice-1a,rules}.ts`, `src/sim/{lanes,placement}.ts`
- `games/typing-defense/art-src/scenery/meadow/`, `art-src/landmarks/`, `art-src/backdrops/w1-silverfall/`; `docs/art-requests/td/03-2d-scenery-ui-vfx.md`
- `docs/games/IMAGE_AUDIT_2026-10-25.md` (điểm bộ tranh `meadow`, lỗi nền V50–V52)
- `tools/map-factory/registry/README.md`, `docs/codex-queue/025-report.md`, `docs/CODEX_QUEUE.md`
- `shared/game-kit/README.md`, `shared/game-kit/platform/rng.ts`, `shared/game-kit/package.json`
