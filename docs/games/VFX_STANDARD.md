# Chuẩn VFX nhiều lớp cho ba game

Ngày 28/10/2026 · Áp dụng cho Rồng Giữ Ải (`games/dragon-hold`), Tuyến Cuối (`games/typing-survival`), Lời Gọi (`games/typing-defense`) · Viết từ năm bản kiểm chỉ đọc ngày 28/10 (ba game, quy trình và skill, nghiên cứu web) · Bản 2: sửa theo phản biện độc lập cùng ngày (số phiếu, trạng thái các làn, ngân sách của Rồng Giữ Ải, kế hoạch gọn hơn) · Đã duyệt 28/10; bước 0 (skill `game-vfx-layered`, dòng trong `AGENTS.md`) đã làm.

**Ảnh anh gửi:** `tmp/vfx/owner-reference-layered-vfx.webp`. Ảnh là media, không vào Git; nguồn là một kênh hướng dẫn Niagara của Unreal. Ảnh tách một chiêu lớn thành 9 lớp đơn giản: Weapon Ribbon Trail, Hemispherical Shockwave, Floating Earth Debris, Corrupted Holy Glow, Crystalline Geode Shards, Ground Fissure Decal, Distortion Refraction Ring, Runed Spark Flares, Sub-surface Plasma Core. Chồng lại, chúng thành một hiệu ứng ("Malignant Wrath of Light"). Từng lớp rất đơn giản; cái đẹp đến từ chồng lớp và canh thời gian.

**Lời anh (27–28/10):** VFX không chỉ lúc đạn trúng quái, mà phải đủ cả khi nhân vật bắn hay ra chiêu.

**Ký hiệu dùng trong tài liệu**

| Viết tắt | Đường dẫn |
|---|---|
| `DH` | `games/.wt-dh-m0b/src/` (nhánh `m0b-models` @ `607c3c1`, mã hình mới nhất với 24 model Tripo; `view/fx.ts`, `telegraphs.ts`, `camera.ts` giống hệt bản ở `games/dragon-hold`) |
| `TS` | `games/typing-survival/src/` (nhánh `main` @ `ce9dea3`) |
| `TD` | `games/typing-defense/src/` (nhánh `a2-days` @ `e49189a`, trùng `main`) |
| `KIT` | `shared/game-kit/` (bản chép trong mỗi game nằm ở `src/kit/`) |
| `05` | `docs/games/dragon-lane/05-presentation-audio-tech-split.md` |
| `FEEL` | `games/typing-survival/docs/FEEL_PASS_S1.md` |
| `TK` | `games/typing-defense/docs/td/TYPING_DEFENSE_DESIGN.md` |
| `ST` | `games/space-typing/src/defense/view/vfx.ts` (chỉ để học kỹ thuật, không import) |
| `[S1]`… | nguồn web ở cuối tài liệu |

**Năm pha của một đòn:**
- **A gồng:** lấy đà.
- **R tung đòn:** ở người ra đòn (miệng Rồng, nòng súng, tháp).
- **T bay:** đạn, tia hay sóng đang đi.
- **I trúng:** ở mục tiêu.
- **F dư âm:** những gì còn lại sau đòn.

Tên trong game dùng tên tiếng Anh theo `docs/games/NAMES_EN.md`, kèm tên Việt hiện tại ở lần nhắc đầu, ví dụ Sky Fire (Thiên Hỏa).

---

## 1. Trả lời ngắn

**Nói gọn:**
- **Cách làm đúng:** hiệu ứng tự viết bằng three.js (hạt instanced, shader riêng) là cách chuẩn cho game chạy trên trình duyệt. Lời Gọi vẽ bằng Canvas 2D cũng hợp với bước hiện tại của nó.
- **Còn thiếu ba thứ:**
  - nhiều lớp: mới có khoảng 3 trên 9 loại lớp của ảnh;
  - hiệu ứng ở người ra đòn;
  - độ sáng đúng cách.
- **Skill và quy trình:** chưa áp dụng đúng.
- **Hướng sửa:**
  - Làm thẳng trong game trước, thư viện chung sau.
  - Bản đầu anh xem là **đòn chữ của Hỏa Long trước và sau**. Đòn này anh thấy hàng trăm lần mỗi trận.
  - Tiếp theo là **Sky Fire đủ 5 pha**, đặt cạnh ảnh tham chiếu.
  - Song song có ba việc nhỏ: Tuyến Cuối mất khung đầu, Lời Gọi bắn không có hình, cánh Rồng không có vệt.

### 1.1 Mỗi game đang làm VFX bằng cách nào

| Game | Cách làm hôm nay | Bằng chứng |
|---|---|---|
| **Rồng Giữ Ải** | three.js, mã tự viết, gom trong một file 1.369 dòng. Gồm:<br>• hạt điểm cộng sáng (additive point sprite) của kit;<br>• billboard instanced có shader riêng cho khói (trộn thường, màu xám);<br>• ô phẳng trên đất cho vòng sóng và vết cháy;<br>• dải vệt `LightTrail`, mảnh vụn `Debris`;<br>• dừng hình, rung camera.<br>**Không có** ảnh, flipbook, mesh hiệu ứng hay đèn động nào.<br>Bloom có dựng nhưng chỉ bật ở Ultra. Bậc High (mặc định) tắt bloom, và không chỗ nào gọi `setBloom`. Ngưỡng 1,6 là cố ý: chỉ phép và lửa được sáng lóa, đất nắng thì không (`05` §2.1). | `DH view/fx.ts`; `KIT three/particles.ts:23`; `DH view/fx.ts:104-141` (khói); `DH view/stage.ts:81-86`, `:242-243` (`UnrealBloomPass(…, 0.32, 0.5, 1.6)`) |
| **Tuyến Cuối** | Cùng họ cách làm, đầy đủ hơn:<br>• atlas 8 ô vẽ bằng Canvas2D (sao lóe, vòng, lõi, khói);<br>• dải vệt quay về camera;<br>• model đạn GLB instanced;<br>• kho đèn điểm (PointLight) dùng lại: 0/2/4/6 đèn theo bậc;<br>• UnrealBloom độ mạnh 0,85, ngưỡng 1,0, tone map ACES;<br>• tàu giật lùi, rung camera, dừng hình theo bậc. | `TS view/fx.ts:19-76`, `:231-243`; `view/bolts.ts`; `view/lights.ts`; `view/gun-rules.ts:28`; `view/scene.ts:303-330` |
| **Lời Gọi** | Canvas 2D, vẽ hình vector bằng mã (cung, đường, elip, chữ) theo màu mực, với một kho 300 hạt. Không ảnh, không shader. Khi đánh nhau không dùng cộng sáng. | `TD view/fx-2d.ts:16-19`; `view/debug-2d.ts` |

### 1.2 Cách đó có đúng không

**Đúng họ phương pháp, nhưng thiếu nội dung.**
- **Phần đúng:**
  - Với three.js trong trình duyệt, kho hạt instanced dùng lại cộng shader tự viết là cách chuẩn.
  - Niagara của Unreal cũng chỉ là nhiều emitter đơn giản chồng lên nhau theo thời gian [S8].
  - Số hạt của ta (vài nghìn) thì CPU dư sức [S15].
  - Không cần đổi engine, không cần mua công cụ.
- **Phần thiếu:** ảnh tham chiếu có 9 loại lớp, ta mới làm đủ khoảng 3: quầng sáng, tia lửa, vệt. Chưa có:
  - vỏ lưới: vòm sóng, lõi plasma, cột phép;
  - decal vết nứt;
  - mảnh tinh thể;
  - sợi khói tối;
  - vòng méo không khí;
  - texture nhiễu;
  - đèn ở Rồng Giữ Ải;
  - pha gồng và pha tung đòn làm theo chuẩn.

**Vì sao đạn và tia trông nhạt** (đọc mã, chưa đo riêng):
1. **Rồng Giữ Ải không có bloom ở High, và chưa bật được ngay.**
   - Hạt cộng sáng trên nền cỏ và đất sáng chỉ thành một vệt nhạt. Chỉ `blastHot` (×1,8) vượt ngưỡng 1,6.
   - Bật bloom tốn thêm 2,2 ms (đo trên sân trống, `DH view/stage.ts:79`).
   - Cổng M0b đo trung bình 5,93 ms trên trần 8 ms, và 8,16 ms khi máy bận (`games/.wt-dh-m0b/docs/changelog/2026-10-27-m0b-models.md:15`, `:89`). Thêm bloom là chạm trần trước khi có hiệu ứng mới nào (§3.7).
2. **Tuyến Cuối mất khung đầu.** Vòng khung đọc sự kiện ở `TS app/main.ts:601` rồi mới vẽ. `Glows.step` tính tuổi hiệu ứng mới trước lần vẽ đầu (`view/fx.ts:181-197`), nên một lóe dài 3 khung chỉ hiện 44 % rồi 11 %.
   - Đèn cũng vậy (`view/lights.ts:96-109`): ở khung đầu, đèn của Pulse Gun (Xung) chỉ sáng 44 %, Rail Gun (Ray) 69 %.
   - Thêm nữa, mọi dải vệt cộng một lõi trắng tinh (`fx.ts:241`), và ACES đẩy màu sáng về trắng. Màu súng chỉ còn ở rìa.
3. **Lớp tối ít, nhỏ và xám.** Ảnh tham chiếu có sợi khói đen "Corrupted" đặt sau lớp sáng.
   - Rồng Giữ Ải có khói xám trộn thường (`fx.ts:104-141`, màu `#5a5650`) và vết cháy tối.
   - Tuyến Cuối có khói tối của big kill (`fx.ts:140`).
   - Không game nào có sợi tối, và **đạn, tia, viên súng không có lớp tối nào**.
4. **Lời Gọi không vẽ gì lúc bắn và lúc trúng một mục tiêu.**
   - `FX.fire` chỉ phần âm thanh đọc (`TD view/audio-min.ts:227-230`).
   - `FX.hit` (`TD sim/systems/projectile.ts:64`) không ai đọc.
   - Cầu lửa của Draconis bị vẽ thành mũi tên (`TD view/debug-2d.ts:778-781`).

**Phía người ra đòn là chỗ yếu nhất ở cả ba game**, đúng điều anh nhắc:
- **Rồng Giữ Ải:**
  - Đạn rời miệng ngay khi gõ xong từ. Hỏa Long được dựng không có bảng `release` (`heroes.ts:214-222`), nên `releaseDelay` luôn trả 0 và clip đánh chạy sau khi đạn đã đi.
  - Lóe miệng chỉ là một quầng 2 m trong 0,14 s (`DH view/fx.ts:527-530`). Lúc bắn không có đèn, không giật đầu, không rung camera.
  - Model Rồng có sẵn socket `FX_WING_L/R/L2/R2`, `FX_TAIL`, `FX_MOUTH`, `FX_CAST_L/R`. Kit vẽ ribbon từ các socket cánh, nhưng `trail: 2` (`heroes.ts:216`) chỉ cho 2 điểm, nên cánh gần như không có vệt.
  - Sky Fire (Thiên Hỏa) không có gì nối Rồng với khối lửa: khối lửa sinh ở điểm đích + (4, 16, 5) m trên trời (`fx.ts:621`).
  - Dragon Roar (Long Hống) nổ từ tâm bệ chứ không từ miệng Rồng (`fx.ts:682-691`).
- **Tuyến Cuối:**
  - Có lớp người ra đòn tốt nhất: lóe nòng, lõi tàu, Rail Gun gồng, tàu giật lùi.
  - Nhưng lóe nòng chỉ hiện 44–64 % ở khung đầu.
  - Heat Beam (Tia), Scatter Gun (Tán) và Star Mortar (Pháo Sao) không có pha gồng ở súng.
  - Star Mortar phóng không có đèn. Không rung là cố ý (`FEEL` §4.6).
- **Lời Gọi:** không có gì ở tháp, ở Draconis. Khi dùng Tối Thượng, Draconis trên sân cũng không làm gì.

### 1.3 Có dùng đúng skill và quy trình không

**Chưa.** Bằng chứng:
- **Skill VFX không dùng được cho ba game:**
  - Skill VFX duy nhất của repo, `combat-vfx-audio`, chỉ trỏ vào mã Space (`.agents/skills/combat-vfx-audio/references/presentation-map.md`). `AGENTS.md` ghi skill Space chỉ để tham khảo ở các game tách.
  - Bộ `threejs-*` và OpenAI Game Studio được cài cho Codex (`docs/AGENT_SKILLS_SETUP.md`); `scripts/sync-agent-skills.sh` chỉ chép 13 skill Space sang `.claude/skills`.
  - Agent Claude, người dựng và chấm VFX, không thấy chúng trong danh sách skill. Vì vậy dòng "Use installed OpenAI Game Studio and `threejs-*`" của `AGENTS.md` không làm được.
  - Nội dung VFX của các skill đó cũng mỏng: khoảng 10 dòng ở `threejs-aaa-graphics-builder/references/technical-art.md`.
  - Không skill nào nói về chồng lớp, flipbook, ribbon, vòm sóng, méo không khí, decal hay 5 pha.
- **Brief không trỏ tới skill:** 18 brief workflow trước đó của phiên này không cái nào nêu tên skill hay phương pháp VFX, kể cả hai lượt cảm giác `ts-feel-n4n6` và `dh-owner-27-10`. Người dựng chỉ có ghi chú của anh và tờ khung Typing Break.
- **Không có chuẩn VFX chung** (tài liệu này là bản đầu). Ngữ pháp 5 bước chỉ là một đoạn ở `05` §6 và `TK` §23.8 (TK:2629), không ai bắt buộc theo.
- **Thiếu kịch bản chụp và thước đo:**
  - Rồng Giữ Ải đặc tả hai kịch bản chụp VFX là `dh-vfx-tiers` và `dh-boss` (`05` §10), nhưng chưa file nào tồn tại.
  - Chỉ Tuyến Cuối có thước đo số (`FEEL` §7.3).
- **Không có ảnh VFX:**
  - Hai game 3D không có ảnh VFX nào.
  - Lời Gọi có 11 ảnh VFX Codex vẽ (23 file kể cả `.prompt.txt`; `ma-troi-sheet` chỉ có prompt, chưa có ảnh) ở `games/typing-defense/art-src/vfx/`. Chưa ảnh nào được gắn vào mã.

### 1.4 Sẽ làm gì (chi tiết ở §4–5)

1. **Chuẩn này:**
   - mọi hành động đủ 5 pha, pha nào bỏ thì ghi lý do;
   - lớp bắt buộc theo loại hành động;
   - thời gian theo khung;
   - luật dễ đọc;
   - ngân sách tính từ khoảng trống đo được của từng game;
   - bản giảm chuyển động.
2. **Làm thẳng trong game trước:**
   - Đòn chữ và Sky Fire dựng ngay trong view của Rồng Giữ Ải, dùng lại kho hạt và shader có sẵn.
   - Khi anh duyệt hướng hình và Tuyến Cuối cần cùng mảnh, mới rút thành module `vfx/` của kit.
   - Mỗi game vẫn deploy riêng.
   - Không dùng thư viện ngoài (lý do ở §4.3).
3. **Bản đầu anh xem:**
   - Đòn chữ trước và sau, dự kiến sau khoảng 1 ngày làm việc.
   - Sky Fire đủ 5 pha cạnh ảnh tham chiếu, sau 2–4 ngày.
   - Tờ khung ở 1280×720 và 1920×1080, kèm clip ngắn.
4. **Chia việc:**
   - Claude dựng hiệu ứng, chụp và chấm.
   - Codex làm phiếu mã nhỏ có phép kiểm (khung đầu Tuyến Cuối, ống sự kiện Lời Gọi, công cụ ghép tờ khung).
   - Codex vẽ vài texture (decal, mặt nạ vết nứt, sợi khói) ở mức ≥ 8/10. Sky Fire không chờ ảnh.
5. **Sửa quy trình gọn:**
   - một skill ngắn trỏ về tài liệu này;
   - brief nào cũng trỏ vào chuẩn;
   - danh sách kiểm 5 pha cộng số đo, thay cho đếm lớp.

---

## 2. Bảng hiện trạng theo game

Cách đọc ô:
- **Có:** đủ dùng.
- **Mỏng:** có nhưng nhỏ, nhạt hoặc chỉ một lớp.
- **Thiếu:** không có gì.
- "—": pha không áp dụng.

Hành động của người chơi ghi trước, của quái ghi sau.

### 2.1 Rồng Giữ Ải (`DH`, nhánh `m0b-models`)

| Hành động | A gồng | R tung đòn (ở người ra đòn) | T bay | I trúng | F dư âm |
|---|---|---|---|---|---|
| Phím đúng (T0) | Mỏng: quầng ở miệng lớn dần theo phần từ đã gõ (`fx.ts:800`); thân Rồng không sáng theo phím | Mỏng: 3 tia lửa nhỏ (`fx.ts:799`); thẻ DOM nảy 1,45× (`ui/styles/dh.css:539, 553`) | Mỏng: một đốm 0,16 s, không vệt (`fx.ts:803-807`) | — | — |
| Phím sai | — | Thẻ DOM rung ±5 px, viền hồng (`dh.css:536`); không có gì trong 3D | — | — | — |
| Đòn chữ (bolt; T1, T3 khi Chớp hay Hoàn hảo) | Thiếu: không tụ lửa, không vòng phép. `Hero` dựng không có `release` (`heroes.ts:214-222`), nên `releaseDelay` = 0 và đạn rời trước khung tung đòn của clip | Mỏng: clip Attack (`heroes.ts:406-410`); quầng 2 m trong 0,14 s, 1 khói 0,9 m, 8 tia (`fx.ts:527-530`); không đèn, không giật, không rung, không vòng đất | Có: `LightTrail` 14 điểm dài ~2,5 m, cung bezier, khói lõi (`fx.ts:989-1000`) | Có: 2 quầng, tia theo bậc, sao tia, vòng từ T3, dừng hình, rung (`fx.ts:558-578`, `1168-1171`); quái lóe, co giãn | Mỏng: 1 khói 0,7 s; không vết cháy, không than |
| Cánh Rồng khi bay, khi đánh | — | Thiếu: model có `FX_WING_L/R/L2/R2`, `FX_TAIL`, nhưng `trail: 2` (`heroes.ts:216`) cho ribbon 2 điểm, gần như không thấy | — | — | — |
| Word Fire (Lửa Chữ, đốt) | — | — | — | — | Có: lửa trên lưng quái (`fx.ts:930-944`) |
| Fire Breath (Phun Lửa, Alt+1) | Thiếu | Thiếu: clip Attack_Both (`heroes.ts:418`), ở miệng không có gì | Mỏng: nón 520 hạt/s trong 0,7 s, độ đục thấp (`fx.ts:909-928`); không lõi nóng, không méo nhiệt | Mỏng: va chạm chung, kẹp ở T2 (`fx.ts:1235`) | Mỏng: 4 vết cháy tròn (`fx.ts:605-610`) |
| Sky Fire (Thiên Hỏa, Alt+2; hồi 24 s) | Mỏng: báo trước phe ta trên đất (`telegraphs.ts`), bóng rơi (`fx.ts:1035`) | Mỏng: clip Cast, phát sáng ×1,9 (`heroes.ts:303, 419`); **không gì nối Rồng với khối lửa**: khối lửa sinh ở đích + (4, 16, 5) m (`fx.ts:621`) | Có: vệt 18 điểm, khói, quầng, than (`fx.ts:1017-1041`) | Có: quầng trắng, cầu lửa, vòng lửa, 70 tia, 2 vòng, 16 bụi, vết cháy, đá vụn (`fx.ts:643-679`) | Có: khói 1,4–1,9 s, vết cháy 7 s, sao choáng 1 s (`fx.ts:958-966`) |
| Dragon Roar (Long Hống) | Thiếu | Thiếu ở miệng: chỉ có bay lượn 0,9 s và Bạch Long vỗ cánh (`heroes.ts:420-423`) | — | Mỏng: 2 vòng phẳng và 24 bụi tỏa ra **từ tâm bệ (0,0)**, không phải từ miệng (`fx.ts:682-691`); không vòm sóng, không méo | Thiếu |
| Inferno (Viêm Đế, Alt+5) | Thiếu: "lửa che 0,3 s, đổi model v3" chưa làm (`HERO_MODELS.fireInferno` không dùng, `heroes.ts:45`) | Mỏng: clip Cast; quầng trắng 5 m trong 0,15 s; vương miện 60 quầng/s suốt 10 s (`fx.ts:694-697`, `967-972`) | Mỏng: mỗi từ là 23 điểm khói và quầng **bắt đầu ở đầu đường phía bệ, không ở miệng**; không có mesh tia (`fx.ts:816-826`) | Qua `landBolt` | Mỏng: vết cháy 4 s; đòn kết dùng lại hiệu ứng Pine Bomb 7 m (`fx.ts:1271`) |
| Bạch Long | Thiếu toàn bộ. Bạch Long mới là người hướng dẫn (`rules.ts:379`); mọi hiệu ứng ở `05` §6.1 (khiên lông vũ, Gió Cuốn, Lời Thề…) chưa có, vì luật chưa vào sim | | | | |
| Spikes | — | Mỏng: model nhún (`actors.ts:373-376`, `469-474`) | — | Mỏng: tia màu gỗ và 4 bụi (`fx.ts:721-728`) | Thiếu |
| Pine Bomb | Mỏng: chỉ thở (`actors.ts:367-369`). Sim nổ ngay khi đủ điều kiện, nên không có chỗ cho ngòi (§3.3) | — | — | Có: quầng trắng, lửa, 40+ tia, vòng, đá vụn (`fx.ts:731-744`) | Có: khói 1,8 s, vết cháy 7 s |
| Net Launcher | Mỏng: đầu quay theo quái bay (`actors.ts:377-391`) | Mỏng: nảy | Thiếu: 14 tia màu dây, **không có lưới bay** (`fx.ts:749-752`) | Mỏng: decal lưới co lại (`fx.ts:753`) | Mỏng: decal 2,5 s |
| Herb Hut (Lều Thuốc Nam) | Mỏng: thở (`actors.ts:650`) | — | Mỏng: giọt hồi máu bay tới (`fx.ts:776-783`) | Có: viền vùng, vòng, đốm bay lên (`fx.ts:759-764`) | — |
| Grove Warden (Vệ Binh Rêu) | — | Có clip Block, Attack, Down, Rise (`actors.ts:425-448`) | — | **Sai màu:** dùng lại va chạm lửa của Rồng (`fx.ts:1235`) | Thiếu: không lóe khiên, không vệt quét |
| Quái gồng đòn | Có: cảnh báo đỏ trên đất (`telegraphs.ts:68-140`, `380-460`), dấu "!", clip giữ khung. Thiếu ánh sáng tụ trên quái và bụi chân heo rừng | — | — | — | — |
| Quái đánh | — | Thiếu: không vệt quét; **cung thủ bắn không có mũi tên** (`fx.ts` không có nhánh `attack`) | Thiếu | Mỏng: Rồng bị đánh chỉ rung, giật, ám đỏ, không có hạt (`fx.ts:1239-1241`); đòn vào lính, nhà dùng màu lửa phe ta (`fx.ts:1242-1245`) | — |
| Héo lan rút máu | — | — | Có: 7 khói tím và một quầng chảy về Rồng (`fx.ts:834-846`) | Có (`fx.ts:849-853`) | — |
| Moss Bannerman (G01) Cắm Cờ | Mỏng: clip Cast | Có: cột sáng cộng màu, vòng hào quang (`banners.ts:56-77`, `302-330`) | — | Thiếu: chỗ cắm cờ không nổ, không nứt | Có: vòng thở |
| Quái chết thường | — | — | — | Có: clip chết, tan nhiễu viền vàng (`crowd.ts:394-399`), mảnh theo chất liệu, tia, bụi, đốm bay về rừng (`fx.ts:581-592`) | Có: mảnh nằm 6 s |
| G01 chết | — | — | — | Mỏng: rêu khó đọc (`fx.ts:860-877`) | Có: decal 6 s |
| Quái xuất hiện | Thiếu | | | | |
| Boss | Chưa có ở M0; pha boss vào M2 (`sim/boss.ts`) | | | | |

Tờ khung ở camera chơi (`games/dragon-hold/tmp/mac-2026-10-27/test/fix/run-1280-70/crop-letters.jpg`, `.../recheck/crop-inferno-1920.jpg`, `.../fix/run-1280-70/crop-g01-death.jpg`, `games/dragon-hold/tmp/test-browser-b/crops/skyfire-seq.jpg`) cho thấy:
- **Đạn:** chấm cam kèm vệt nhạt; lóe miệng chỉ vài điểm ảnh.
- **Trúng:** đốm vàng nhạt với một vòng xanh mảnh.
- **Tia Inferno:** dải cam phẳng, không có nguồn ở Rồng.
- **G01 chết:** khó thấy.

### 2.2 Tuyến Cuối (`TS`)

S1 chưa có chiêu của người chơi. "Ra chiêu" ở đây là nạp súng, Rail Gun gồng, Heat Beam bật, Star Mortar phóng, và tàu.

| Hành động | A gồng | R tung đòn (ở tàu) | T bay | I trúng | F dư âm |
|---|---|---|---|---|---|
| Phím đúng | Có: lõi lớn dần mỗi chữ (`view/typing-feel.ts:244-257`) | Có: tia lửa ở chữ (DOM); sao 4 tia và 3 tia lửa (`typing-feel.ts:179-180`) | Có: sét 4 đoạn từ tấm chữ về lõi (`typing-feel.ts:203-229`) | Có: sao 8 tia trong lõi, vòng sàn (`typing-feel.ts:184-188`) | Có: lõi giữ mức |
| Pulse Gun (Xung), bắn cả băng | Mỏng: chỉ có lõi chung của từ, và tia mồi ở nòng khi gõ được nửa từ (`typing-feel.ts:259-262`) | Mỏng: lóe nòng 3–4 khung **chỉ hiện 44–56 %** (`view/shots.ts:158-160`); đèn 44 % (`:161`); giật 0,05 m. Không rung theo viên là cố ý (`FEEL` §4.6) | Mỏng: model đạn, vệt thẳng 3,7 × 0,18 m (`shots.ts:349-363`) | Mỏng: sao 4/8/12 theo bậc, mất khung đầu; mảnh vỡ chỉ từ T2 (`view/combat.ts:192`) | Thiếu |
| Heat Beam (Tia) | Thiếu | Mỏng: lóe 44 %; sao 8 tia quay ở nòng; đèn giữ sáng (`view/beams.ts:87-92`, `203-207`) | Mỏng: dải haze, glow, lõi trắng; không texture, không cuộn UV (`beams.ts:174-201`); sàn có shader dòng chảy (`fx.ts:316-355`) | Mỏng: sao 4 tia (`shots.ts:298-302`); không mảnh vỡ | Có: sàn cháy 2,4 s (`combat.ts:271-276`) |
| Scatter Gun (Tán) | Thiếu | Có: 3 lưỡi lửa; lóe 64 %; đèn 63 %; giật 0,28 m; khói; vỏ đạn (`shots.ts:181-198`) | Mỏng: 7 viên, vệt 2 m (`shots.ts:344-347`) | Mỏng: sao 4 tia và 3 tia lửa; không mảnh vỡ, không rung | Thiếu |
| Rail Gun (Ray) | **Có, tốt nhất game:** đạn sẵn sàng quay trên nòng; gồng 150 ms; vạch ngắm 26 m; tàu rung (`beams.ts:124-154`; `view/ship.ts:245-246`) | Có: vệt 3,4 m, sao 8 tia, đèn 69 %, giật 0,4 m, rung (`beams.ts:68-86`) | Mỏng: đường bắn tức thời 0,35 s, vòng ion (`beams.ts:78-122`); giảm còn ×0,6 quanh tàu | Mỏng: sao 8 tia; 6 tia lửa mỗi quái bị xuyên; dừng 12 ms; không mảnh vỡ | Thiếu: không vết cháy |
| Star Mortar (Pháo Sao) | Thiếu ở tàu. Vòng điểm rơi co lại khi đạn bay, coi như báo trước (`shots.ts:399`) | Mỏng: vệt lên 2,5 m; lóe 44 %; cột khói 0,7 s; **không đèn**. Không rung là theo `FEEL` §4.6 (`shots.ts:209-212`) | Mỏng: model đạn bay parabol; vệt thẳng ngắn, chỉ bằng 8 % đường cung (`shots.ts:392-397`) | Có: lóe, lõi, sao 8 tia, vòng sàn, 32 tia lửa, đèn 74 % (`shots.ts:220-229`). Quái trong vòng nổ không lóe (`shots.ts:286`) | Mỏng: sàn than 1,2 s, khói 1,4 s; không vết cháy |
| Tàu bị đánh | — | — | — | Mỏng: sao 8 tia đỏ ở nòng; rung 0,2; viền đỏ DOM (`combat.ts:222-230`; `hud.ts:253`) | Thiếu: không khói hỏng, không tia lửa trên vỏ |
| Shield Guard (Khiên) | — | — | Có: tường lục giác bằng shader, gợn sóng, 3 mức nứt (`view/hazard-fx.ts:19-121`) | Có: vỡ thành sao 12 tia, vòng, 22 mảnh kính, dừng hình T3 (`view/gunfx.ts:124-129`) | Có: kính nằm trên sàn |
| Rift (Vết nứt) | Có: vết nứt nóng dần trong 2,5 s (`hazard-fx.ts:135-206`) | Có: 40 tia lửa, cột lóe 14 m, rung (`gunfx.ts:139-150`) | — | — | Có: vết nứt mờ dần 2,5 s |
| Quái khác ra đòn | Có: Pack Leader (Đầu Đàn) có đèn hiệu, sừng lóe; Brute (Trâu) có vòng giậm (`gunfx.ts:135-138`, `188-207`) | Mỏng: quái bắn có sao ở nòng (`combat.ts:231-234`) | Mỏng | Mỏng | — |
| Quái chết thường | — | — | — | Có nhưng mất khung đầu: lõi 64 %, sao, vòng sàn, 2 chùm tia lửa, quái trắng 45 ms (`shots.ts:235-243`) | Có: khối vỡ có viền nóng, nảy, nằm 8 s (`view/chunks.ts:132-227`) |
| Big kill (Brute, Pack Leader) | — | — | — | **Có, nhiều lớp nhất:** lóe hiện đủ ngay (`early`); 9 cầu lửa, 36 tia lửa, dừng hình T3 (`shots.ts:246-261`) | **Có:** 17 khói chia 3 lớp; vết cháy và vết nứt sáng 7–9 s; than; 14 tàn bay lên; 28–32 khối vỡ (`shots.ts:263-279`) |

Tờ khung cho thấy (`games/typing-survival/tmp/mac-2026-10-27/feel-n4n6/round2/final/sheets/` và `round1/after/1920x1080/`):
- **Mỗi phím:** vùng tàu thành một đĩa trắng xanh.
- **Heat Beam và Rail Gun:** gần như cột trắng, mất màu súng.
- **Pulse Gun:** lóe nòng bị lóe nạp từ che mất ở f0–f3.
- **Star Mortar:** đạn là vệt hồng mảnh; vụ nổ là đĩa trắng 1–2 khung; từ f24 chỉ còn vòng đỏ.
- **Big kill** (`kill-ray-brute-full-1280x720.jpg`) là hiệu ứng duy nhất đọc ra nhiều lớp.

### 2.3 Lời Gọi (`TD`, 2D Canvas)

| Hành động | A gồng | R tung đòn (ở tháp, Draconis) | T bay | I trúng | F dư âm |
|---|---|---|---|---|---|
| Archer Tower | Mỏng: 5 chấm lực (`debug-2d.ts:530`) | **Thiếu** (chỉ có tiếng) | Mỏng: nét mực 1,1 m × 2 px (`debug-2d.ts:778-781`). Word Shot (Phát Chữ) có đầu xanh ngọc và chữ bay theo (`:789-795`) | Thiếu với mũi tên thường. Word Shot có dấu ✦ xanh ngọc, chữ bung ra (`fx-2d.ts:143-145`) | Thiếu |
| Cannon Tower | Thiếu | **Thiếu** | Mỏng: đĩa mực bay phẳng (`debug-2d.ts:773-776`) | Mỏng: một vòng hổ phách 3 px (`debug-2d.ts:823`) | Thiếu: không khói, không vết cháy |
| Fort (Lũy Chữ) bắn | Thiếu | Thiếu | Mỏng: nét trắng 3 px (`debug-2d.ts:781`) | Thiếu | Thiếu |
| Draconis đánh thường | Mỏng: cất cánh, hạ cánh (`debug-2d.ts:721-748`) | **Thiếu** | **Sai:** cầu lửa vẽ thành mũi tên mực (`debug-2d.ts:778-781`) | Mỏng: vòng hổ phách chung 1,8 m | Thiếu với quái thường: `burnUntil` không được đọc ở `src/view` |
| Fire Feather Rain (Mưa lông lửa, Tối Thượng) | Có: vòng nạp ở đèn lồng; thẻ Chữ Chiêu sáng cam (`ui/team-bar.ts:25`; `view/words/cards.ts:138`) | Mỏng: chân dung mực tạm trượt vào (`fx-2d.ts:205-244`). **Draconis trên sân không làm gì** | Mỏng: lông lửa là một nét 1,6 m với một chấm; bóng lớn dần (`debug-2d.ts:766-771`) | Mỏng: vòng chung 1,5 m | Có: vũng than 3 s (`fx-2d.ts:138`, `150-157`) |
| Helper (Thư Đồng), thợ | Có: dấu "!", "…" và bong bóng gọi | Có: thẻ bay về người gọi trong 220 ms, dấu điểm (`cards.ts:105-120`) | — | Thiếu trên sân | Mỏng |
| Mộc Tinh (boss) | **Có, 4–6 lớp:** rễ, vết nứt bò, đất phồng, rung (`view/boss-2d.ts:141-187`, `262-306`) | Có: trồi lên vượt 6 %; cung quét trắng 200 ms | — | Có: đá, rễ, bụi, mảnh gỗ, lóe trắng (`boss-2d.ts:63-99`, `359-361`) | Có: "Tê N s", trời ngả hổ phách, sao choáng |
| Quái ra đòn | Có ở vài loài: Tanuki có trống đỏ, Troll có vòm đá (`debug-2d.ts:661-702`) | Thiếu | Thiếu | Thiếu: lính giáp lá cà chỉ có viền (`debug-2d.ts:636`) | — |
| Quái trúng đòn | — | — | — | **Thiếu:** quái thường không lóe, chỉ có thanh máu (`debug-2d.ts:686`) | — |
| Quái chết | — | — | — | Mỏng: mọi loài cùng một đĩa tím và 6 viên đá (`debug-2d.ts:813, 824`), trái với `TK:2277-2278` | Mỏng: chữ "+vàng" bay lên |

**Gốc của "không có hiệu ứng khi bắn":** mỗi phát bắn, `sim/systems/combat.ts:86` đẩy một sự kiện `FX.fire`, nhưng chỉ `view/audio-min.ts:227-230` đọc nó.

**Thiết kế 3D có, nhưng xếp lịch muộn:** `TK` §23.8 (TK:2629-2694) đã có ngữ pháp 5 bước cho từng thực thể. Nhưng lịch `TK` §26.1 để phần này ở bước 2 "Sống" (TK:3245), tức là sau bước 1C 3D (TK:3239).

### 2.4 Chín lớp của ảnh tham chiếu ở ba game

| Lớp trong ảnh | Rồng Giữ Ải | Tuyến Cuối | Lời Gọi |
|---|---|---|---|
| Weapon Ribbon Trail | Mỏng: `LightTrail` trơn trên đạn và khối lửa; ribbon cánh chỉ 2 điểm; `FlameTrail` của kit không dùng | Mỏng: dải thẳng, gradient cố định; `Ribbon` chỉ dùng ở động cơ (`ship.ts:267-271`) | Thiếu |
| Hemispherical Shockwave | Thiếu (chỉ có vòng phẳng) | Thiếu | Thiếu (thiết kế có vòm cho Fort, TK:2662) |
| Floating Earth Debris | Mỏng: `Debris` chỉ rơi | Mỏng: khối vỡ khi hạ quái; không bay lơ lửng | Mỏng: đá 2D |
| Corrupted Holy Glow (lớp tối trên nền sáng) | Mỏng: khói xám trộn thường (`fx.ts:104-141`), vết cháy tối; không có sợi tối | Mỏng: chỉ có khói của big kill (`fx.ts:140`) | Thiếu |
| Crystalline Geode Shards | Thiếu | Mỏng: khối thép xỉn, không phát sáng | Thiếu |
| Ground Fissure Decal | Mỏng: vết cháy tròn | Mỏng: vết cháy của big kill; shader của Rift | Mỏng: vết nứt 2D của boss |
| Distortion Refraction Ring | Thiếu | Thiếu: chuỗi hậu kỳ chỉ có Render, Bloom, Output (`scene.ts:325-330`) | Thiếu (thiết kế có một vòng 6 m, TK:2681) |
| Runed Spark Flares | Mỏng: tia lửa tròn | Mỏng: tia lửa tròn, không kéo dài theo hướng bay | Mỏng |
| Sub-surface Plasma Core | Thiếu | Mỏng: billboard `CELL.core` | Thiếu (cũng không có trong kế hoạch) |

---

## 3. Chuẩn VFX nhiều lớp

### 3.1 Năm pha, làm phía người ra đòn trước

| Pha | Nghĩa | Người chơi phải thấy |
|---|---|---|
| **A gồng** | Lấy đà trước đòn | Đòn sắp đến, đến từ đâu, mạnh cỡ nào |
| **R tung đòn** | Khoảnh khắc ở người ra đòn: miệng Rồng, nòng súng, tháp, tay phép | Ai ra đòn, và đòn bắt đầu ngay lúc này |
| **T bay** | Đạn, tia, vệt, sóng đang đi | Đường đi và tốc độ |
| **I trúng** | Ở mục tiêu | Trúng ai, mạnh cỡ nào, vùng rộng bao nhiêu |
| **F dư âm** | Sau đòn | Chỗ vừa bị đánh, để mắt nghỉ |

Luật:
1. **Làm R trước I.** Một hành động chưa có R thì chưa xong, dù I đẹp.
2. **A không được làm chậm đòn.**
   - Phím vào lõi gõ ngay; từ phím tới đòn ≤ 50 ms (≤ 70 ms khi đang dừng hình) (`05` §8, `FEEL` §6).
   - Với đòn chữ, A chính là lúc gõ: mỗi chữ một nhịp.
   - Với chiêu bấm phím, A nằm trong độ trễ sim đã có sẵn, ví dụ 0,8 s của Sky Fire (`DH content/rules.ts:418`, `delayMs: 800`).
   - Thứ sim kích ngay khi đủ điều kiện (bẫy nổ) thì không có A "trước nổ". A khi đó là trạng thái **sẵn sàng** lúc chờ (`05` §6.5: rune mờ, quả thông thở). Muốn có ngòi thật trước khi nổ thì phải thêm độ trễ vào sim: đó là việc của làn luật (đổi golden), không phải của VFX.
   - VFX không đổi tick của sim.
3. **Khớp clip với R, nhưng không giữ đạn quá 50 ms.**
   - Trước hết ghi khung tung đòn cho từng clip vào tùy chọn `release` của `Hero` (`KIT three/hero.ts:67-68`). Rồng Giữ Ải hiện chưa ghi (`DH view/heroes.ts:214-222`), nên `releaseDelay` (`KIT three/hero.ts:270`) luôn trả 0.
   - **Cách ưu tiên:** phần gồng của clip chạy theo tiến độ gõ, mỗi chữ đẩy clip tới một đoạn. Khung tung đòn rơi đúng lúc gõ xong từ; đạn rời ngay.
   - **Cách dự phòng:** khi gõ xong từ, bắt đầu clip Attack ở điểm cách khung tung đòn ≤ 3 khung (≤ 50 ms), tức là bỏ qua phần đầu của clip. Đạn rời ở khung tung đòn và bay nhanh hơn một chút để vẫn trúng đúng tick sim.
   - Không bao giờ giữ đạn nhìn thấy quá 50 ms sau phím cuối.
4. **VFX chỉ nằm ở view.**
   - Không sửa `src/sim` hay `src/content`; golden và mã băm trận giữ nguyên.
   - Phần ngẫu nhiên của VFX dùng một luồng riêng có seed, để chụp lại lần nào cũng giống nhau.
5. **Khung đầu sáng đủ.** Hiệu ứng và đèn mới sinh được vẽ ở tuổi 0, trước khi bị tính tuổi. Tuyến Cuối sửa lỗi 44–64 % bằng phiếu 035; Rồng Giữ Ải kiểm cùng lỗi này trong lượt đòn chữ.

### 3.2 Thực đơn lớp

Bảng dưới là **thực đơn để chọn**, không phải để đếm. Người chấm xem chiều sâu trên tờ khung; không phép kiểm nào đếm số lớp. Lý do: đếm lớp dễ bị lách (chồng lớp cho đủ số), và sai với súng bắn nhanh.

Mười tám loại lớp:
- **L1–L9:** ứng với chín lớp của ảnh tham chiếu, mỗi lớp một kỹ thuật đơn giản.
- **L10–L18:** phần cảm giác mà ảnh không vẽ.

| # | Lớp | Trong ảnh | Kỹ thuật (three.js 0.170, WebGL2, GLSL) | Đã có để dùng lại |
|---|---|---|---|---|
| L1 | Vệt ribbon | Weapon Ribbon Trail | Dải lưới bám theo các vị trí cũ: thon đuôi, cuộn UV, ăn mòn bằng nhiễu (noise erosion) [S22][S24] | `KIT three/particles.ts`: `Ribbon`, `FlameTrail`, `LightTrail` |
| L2 | Vòm sóng | Hemispherical Shockwave | Bán cầu 32×16, viền fresnel, ăn mòn, nở theo đỉnh, viền nóng [S23]. Một bán cầu ít vẽ chồng hơn nhiều sprite [S30] | Shader SHIELD, PILLAR (`KIT three/materials.ts`, chưa dùng); trụ fresnel `DH view/banners.ts:56-77` |
| L3 | Đá vụn bay | Floating Earth Debris | InstancedMesh đá (icosahedron méo theo nhiễu), bay theo cung; chế độ "nâng lơ lửng" 0,2–0,4 s rồi rơi; vật liệu đục hoặc cắt alpha, không trộn màu [S15][S23] | `KIT feedback/debris.ts` (chỉ rơi); `TS view/chunks.ts` |
| L4 | Khói tối, sợi tối | Corrupted Holy Glow | Sprite trộn thường (normal blend) màu tối, ăn mòn bằng nhiễu, đặt sau lớp sáng để tạo tương phản | `TS view/fx.ts` chế độ smoke (`:105-140`); khói xám của `DH` (`fx.ts:104-141`) |
| L5 | Mảnh tinh thể | Crystalline Geode Shards | InstancedMesh hình bipyramid, cạnh phát sáng (emissive), fresnel; màu theo game (đá than lửa, băng, ngọc) | Chưa có |
| L6 | Decal vết nứt, vết cháy | Ground Fissure Decal | Ô phẳng có polygonOffset trên đất phẳng; chỗ đất gồ thì ôm địa hình (dùng lưới của `DH telegraphs.ts:68-140`). Mặt nạ vết nứt có khe sáng nguội dần. `DecalGeometry` chỉ dùng khi đất rất gồ [S17] | QuadPool của `DH` (`fx.ts:143-173`) |
| L7 | Vòng méo không khí | Distortion Refraction Ring | Vẽ vòng vào một buffer lệch UV ở nửa độ phân giải, rồi một lượt toàn màn đọc cảnh với UV lệch đó [S26]. Chỉ bật ở bậc mà số đo cho phép (§3.7) | Chưa có |
| L8 | Tia lửa kéo dài, ký tự lóe | Runed Spark Flares | Sprite kéo dài theo vận tốc; ký tự lấy từ atlas rune; than bay lên theo nhiễu cuộn | `ParticlePool` (chỉ có hạt tròn) |
| L9 | Lõi plasma | Sub-surface Plasma Core | Cầu fresnel với nhiễu động, HDR > 1, `toneMapped: false` [S14] | `CELL.core` của `TS` (billboard) |
| L10 | Lóe | (nằm trong lõi) | Billboard cộng sáng 2–3 khung, đủ sáng ngay khung đầu [S2] | Glows của `TS`, glow của `DH` |
| L11 | Quầng | | Sprite mềm cộng sáng | Có ở cả hai game 3D |
| L12 | Vòng sóng phẳng | | Ô shader hình vòng trên đất | Có ở cả hai game 3D |
| L13 | Vòng phép, nón, cột phép | | Decal vòng rune quay dưới người ra chiêu; nón hoặc trụ fresnel ở người ra chiêu | Texture `runes` của kit (chưa dùng) |
| L14 | Đèn chớp | | Kho PointLight dựng sẵn lúc nạp, chỉ đổi cường độ và vị trí. Thêm hay bớt đèn lúc chạy làm shader biên dịch lại [S25] | `TS view/lights.ts`; `impactLight` ở `KIT three/stage.ts:71`, `179-186` |
| L15 | Camera | | Giật theo hướng đòn, đẩy FOV, rung theo trauma² [S6][S7] | `KIT feedback/trauma.ts` |
| L16 | Dừng hình | | Thế giới chậm còn 0,05, theo bậc, có trần. Đòn đạn dừng ngắn hơn đòn cận chiến; quái rung với biên độ giảm dần [S3][S4] | `KIT feedback/hitstop.ts` |
| L17 | Phản ứng thân | | Lóe trên từng instance, co giãn, giật lùi giả, tan theo nhiễu có viền | `KIT feedback/reaction.ts`; `DH crowd.ts:394-439` |
| L18 | Giật thân người ra đòn | | Đầu Rồng giật, tàu giật lùi, tháp nhún, thân phát sáng | `TS view/ship.ts:226-247`; tower kick của Space (`towers.ts:92-95`) |

### 3.3 Công thức theo loại hành động

**Cách đọc bảng:**
- Mỗi ô ghi **lớp bắt buộc** của pha đó. Thêm lớp từ thực đơn §3.2 là việc của người dựng; người chấm xét chiều sâu.
- Pha nào ghi "—" thì không áp dụng. Bỏ một pha có áp dụng thì phải ghi lý do trong changelog.
- Bậc theo bảng `kit/feedback` (`05` §5):
  - T0: phím;
  - T1: đòn thường;
  - T2: hạ quái;
  - T3: chiêu;
  - T4: đòn lớn;
  - T5: chiêu cuối và boss đổi pha.

| Loại | Bậc | A | R (ở người ra đòn) | T | I | F |
|---|---|---|---|---|---|---|
| Phím gõ | T0 | — | Chữ nảy ở thẻ, và đốm hoặc tia ở nguồn (miệng, lõi tàu, tháp) trong cùng khung | Đốm bay từ thẻ về nguồn, nếu game có | — | Mức nạp ở nguồn lớn dần |
| Bắn thường (đòn chữ, mũi tên, phát Tán, phát Ray) | T1–T2 | Quầng tụ ở nguồn theo từng chữ | Lóe tuổi 0; đèn (hoặc quầng lớn ở bậc không có đèn); giật thân | Đầu đạn HDR; vệt ribbon | Lóe; phản ứng thân; tia lửa | Khói nhỏ hoặc vết xém |
| **Bắn liên thanh** (viên trong băng Pulse Gun) | T1 | Thuộc lúc gõ từ nạp băng (lõi chung), không theo từng viên | Mỗi viên: lóe tuổi 0 và giật nhỏ. Viên đầu băng thêm đèn, tia và cú đẩy 1,5 px. Không rung theo viên (`FEEL` §4.6) | Vệt mảnh | Sao nhỏ; phản ứng thân | — |
| Chiêu | T3 | Vòng phép; than bị hút về nguồn; đèn sáng dần | Lóe; vỏ dạng nón hoặc cột; vòng trên đất; camera | Lõi; ribbon; lớp tối | Lóe; vòm hoặc vòng đúng bán kính luật; đá vụn; tia; đèn; dừng hình | Decal; khói tối; than |
| Chiêu cuối | T5 | Như chiêu, thêm viền màn ám màu ≤ 20 % và biến hình | Như chiêu, lớn hơn | Như chiêu | Các loại lớp của ảnh tham chiếu hợp với chiêu, kể cả vòm; méo ở bậc mà số đo cho phép | Như chiêu, kéo dài hơn |
| Nổ bẫy | T2–T4 | Trạng thái **sẵn sàng** lúc chờ (`05` §6.5). Làn `s6-traps` đang thêm trạng thái "sẵn sàng" và "vừa kích" cho mọi ô bẫy, ô nhà | Trạng thái "vừa kích"; lóe ở bẫy; bẫy nhún | Vật bay (lưới, mảnh) nếu có | Lóe; vòng đúng bán kính; mảnh theo chất liệu; tia; khói | Decal; khói; dấu nạp lại (vòng đồng hồ, `05` §6.5) |
| Quái ra đòn | — | Báo trước đỏ trên đất; ánh tụ trên vũ khí quái | Vệt quét hoặc lóe nòng, màu phe địch | Đạn và vệt màu phe địch, nếu đánh xa | Ở nạn nhân: lóe màu phe địch; tia theo chất liệu; rung nhỏ | — |
| Quái chết | T2 (thường), T3–T4 (tinh anh, tướng) | — | — | — | Thân lóe; tan có viền; mảnh theo chất liệu; bụi | Mảnh nằm lại; đốm hoặc tiền bay về HUD |
| Boss | T4–T5 | Báo trước ≥ 1,2 s (TK:2653); ánh tụ; đất rung | Như chiêu | Theo từng đòn | Như chiêu, lớn hơn | Boss đổi pha dùng công thức chiêu cuối |

Luật thêm:
- **Không phải đòn nào cũng cần đủ chín lớp.** Đòn thường lặp nhiều lần mỗi giây nên phải gọn; lớp tăng dần theo bậc.
- **Súng bắn nhanh giữ trần theo phím:** gõ 10 phím/s thì ≤ 12 billboard và vệt sống do phím (`FEEL` §6).
- **Đòn vùng trúng N quái** chỉ tạo một vụ nổ cỡ √N, mỗi con 2 hạt, tối đa 20 hạt (TK:2696, `05` §5).
- **Đòn mạnh nhờ chữ** (Chớp, Hoàn hảo, Word Shot) có đầu đạn xanh ngọc, và vệt là chính các chữ cái của từ (`05` §6, TK:2638).

### 3.4 Thời gian (tính bằng khung ở 60 Hz)

| Lớp | Bắt đầu | Kéo dài | Nguồn |
|---|---|---|---|
| Lóe (L10) | f0, đủ sáng ngay khung đầu | 2–3 khung | [S2] |
| Thân lóe nòng, nón, sao | f0–f1 | 4–8 khung | |
| Vỏ nón, cột phép (pha R) | f0 | 8–12 khung | |
| Giật thân, camera kick | f0 | lò xo 6–10 khung (≈ 120 ms, `05` §5) | [S6] |
| Đèn chớp | f0, đủ sáng ngay khung đầu | đòn thường 4–6 khung, chiêu 10–15, chiêu cuối 15–24 | |
| Đầu đạn, ribbon | suốt đường bay | đuôi tắt dần trong 6–12 khung sau khi trúng | |
| Các lớp lúc trúng | lớp sau trễ 2–3 khung so với lớp trước | | [S2] |
| Vòng sóng, vòm | f1–f2 | 8–15 khung (vòm của chiêu cuối tới 20) | |
| Tia lửa | f0–f2 | 10–20 khung, tắt ngay sau vòng | [S2] |
| Đá vụn, mảnh | f2 | bay 20–40 khung, nằm lại 6–8 s | |
| Méo không khí | f1 | 10–15 khung | |
| Lóe thân quái | f0 | 2–5 khung (≈ 80 ms) | [S4] |
| Dừng hình | f0 | T1: 0; T2: 12 ms; T3: 35 ms; T4: 45 ms; T5: 70 ms (`05` §5). Ngắn hơn dải 50–150 ms của [S4][S5] là có chủ ý, vì nhịp gõ nhanh. Đòn đạn dừng ngắn hơn đòn cận chiến [S3] | |
| Khói, than | f4–f8 | 30–120 khung, tắt dần (ease-out), không bị cắt ngang | |
| Decal | lúc trúng | đòn thường 2–3 s, chiêu 4–7 s, tắt dần | |
| Pha A của chiêu | trong cửa sổ trễ của sim | 12–48 khung | |
| Báo trước của quái | | ≥ 30 khung (0,5 s); boss ≥ 72 khung (1,2 s) (TK:2280, 2653) | |

Về nhịp tổng thể: hiệu ứng nhanh hơn khoảng một nhịp tim (~60 BPM) sẽ đọc ra dữ dội [S1]. Chiêu cuối được dài hơn, nhưng đỉnh sáng vẫn ≤ 3 khung.

### 3.5 Độ sáng và màu: chống "nhạt"

1. **Bloom theo từng game, không một ngưỡng chung.**
   - **Rồng Giữ Ải:**
     - Giữ ngưỡng 1,6. Đây là lựa chọn có chủ ý: chỉ phép và lửa được sáng lóa, đất nắng thì không (`05` §2.1; chú thích ở `DH view/stage.ts:242`).
     - Lõi VFX đẩy lên HDR 2–6 với `toneMapped: false` [S14] để qua ngưỡng.
     - Chỉ bật bloom ở High khi đo trên cảnh M0b (DPR 1,25, 220 quái) mà vẫn vừa cổng 8 ms. Nếu không vừa, High dùng quầng sprite vẽ sẵn, không qua hậu kỳ; bloom ở lại Ultra, và đưa anh quyết (§6.2).
   - **Tuyến Cuối:** giữ bloom như `FEEL` §4.1 (ngưỡng 1,0; bán kính 0,3 sau lần Ray làm trắng sân). Chỉ sửa màu lõi, không sửa bloom.
   - **Lời Gọi (2D):** không bloom; lớp cộng sáng vẽ bằng `globalCompositeOperation = "lighter"`.
2. **Không dựa hết vào bloom.** Bậc không có bloom vẫn phải đạt, nhờ quầng và viền màu vẽ sẵn trong sprite, nhờ đèn và nhờ lớp tối. Với Rồng Giữ Ải, đây chính là bậc High mặc định.
3. **Lõi trắng nhỏ, thân màu lớn.**
   - Lõi trắng ≤ 30 % bán kính hiệu ứng; phần còn lại giữ màu bão hòa của súng, của phe.
   - Bỏ lõi trắng mặc định ở mọi dải vệt (`TS fx.ts:241`).
   - Dùng dải màu (ramp) theo từng hàng: lửa, vàng thánh, băng, độc, mục, mực.
4. **Có lớp tối.** Mọi hiệu ứng từ T2 trở lên trên nền sáng có ít nhất một lớp trộn thường màu tối: khói, muội, vết cháy.
5. **Khung đầu đủ sáng** (§3.1, luật 5), cả lóe lẫn đèn.
6. **Đủ to ở camera chơi**, không chỉ ở cận cảnh.
   - Đầu đạn ≥ 20 × 6 px ở 720p (`FEEL` §7.3).
   - Lóe nòng, lóe miệng lớn hơn đầu đạn ≥ 1,5 lần.
7. **Màu mang nghĩa.**
   - Phe ta theo bảng màu của game:
     - Rồng Giữ Ải: lửa cam vàng; xanh ngọc cho Chớp và Hoàn hảo.
     - Tuyến Cuối: màu riêng của từng súng.
     - Lời Gọi: mực, xanh ngọc, hổ phách.
   - Hồi máu màu xanh lá.
   - Phe địch màu rêu, tím, đỏ thẫm, **không bao giờ dùng màu lửa của phe ta** (sửa `DH fx.ts:1235`, `1242-1245`).

### 3.6 Luật dễ đọc

1. **Thẻ chữ và khung học luôn đọc được.**
   - Tương phản ≥ 7 : 1 (`05` §4.3; `FEEL` §7.3 đo ở p99).
   - Hạt cộng sáng quanh thẻ giảm 60 % (mặt nạ vùng yên, `05` §4.3 và `TK` §23.4).
   - Không hạt hay số nào đè khung học (`dh-learning-frame`).
   - Số sát thương không đè dòng từ (`FEEL` §2.5).
2. **Không để sân trắng xóa.**
   - Điểm ảnh có độ sáng ≥ 0,95 chiếm ≤ 6 % vùng sân ở mọi khung; riêng chiêu cuối được ≤ 15 % trong tối đa 3 khung.
   - Chớp toàn màn ≤ 2 lần mỗi giây (TK:2696). Mức này chặt hơn ngưỡng "ba lần chớp" của WCAG 2.3.1.
3. **Màu đỏ dành cho quái.**
   - Báo trước màu đỏ chỉ dùng cho đòn của quái; báo trước của phe ta màu cam nhạt viền trắng (`05` §6).
   - Thứ tự nổi giữ theo `05` §2, từ trên xuống:
     1. thẻ chữ, khung học;
     2. báo trước đỏ;
     3. quái, Rồng, lính;
     4. bẫy, nhà;
     5. cảnh.
   - VFX phe ta không được che báo trước đỏ.
4. **Đòn nào cũng biết là của ai.** R nằm ở người ra đòn; I nằm ở mục tiêu, mang màu của nguồn.
5. **Dư âm không thành rác.** Decal và khói có trần số lượng và tự tắt; khói không trôi qua thẻ chữ.
6. **Kiểm ở camera chơi, ở cả hai độ phân giải, trên nền sáng và nền tối.**

### 3.7 Ngân sách: tính từ khoảng trống đo được

**Thời gian khung là cổng thật.** Ngân sách VFX của mỗi game bằng khoảng trống đo được dưới cổng khung của game đó, đã trừ bloom. Không có con số chung "4 ms cho VFX".

| Game | Cổng khung | Đo gần nhất | Khoảng trống cho VFX (gồm cả bloom) |
|---|---|---|---|
| **Rồng Giữ Ải**, High 1080p | Trung bình ≤ 8 ms, p95 ≤ 12 ms (`05` §8, `dh-perf`) | Máy rảnh: 5,93 ms trung bình, p95 7,8 ms. Máy bận: bench có xương 8,16 ms trung bình (`.wt-dh-m0b/docs/changelog/2026-10-27-m0b-models.md:15`, `:89`) | **≈ 2 ms** khi máy rảnh, **≈ 0** khi máy bận. Riêng bloom (+2,2 ms, đo trên sân trống, `stage.ts:79`) đã vượt. Phải đo bloom ở High (DPR 1,25) trên cảnh M0b trước khi hứa |
| **Tuyến Cuối** | `FEEL` §6: khoảng cách khung trước và sau trên cùng cảnh cố định; kho hiệu ứng; ≤ 12 billboard và vệt theo phím ở 10 phím/s | `FEEL` §6, cột "Hôm nay" | Đo trước và sau mỗi lô; không vượt cổng `FEEL` §6 |
| **Lời Gọi**, 2D | `td-1b-perf` | — | Đo trước và sau V4a. Bước 1C (3D): TK:2696 |

**Trần số lượng (mặc định, chỉ áp khi chưa vượt cổng khung):**

| Mục | Low | Medium | High | Ultra |
|---|---|---|---|---|
| Draw call thêm do VFX (mỗi vật liệu, mỗi texture một call) | ≤ 12 | ≤ 20 | ≤ 32 | ≤ 40 |
| Hạt sống | ≤ 600 | ≤ 1.500 | ≤ 3.000 | ≤ 4.500 |
| Hạt sinh mới mỗi khung | ≤ 80 | ≤ 160 | ≤ 260 | ≤ 320 |
| Mảnh instanced (đá, tinh thể) | ≤ 150 | ≤ 400 | ≤ 600 | ≤ 900 |
| Ribbon sống | ≤ 8 | ≤ 16 | ≤ 32 | ≤ 48 |
| Vỏ lưới cùng lúc (vòm, lõi, nón) | ≤ 2 | ≤ 4 | ≤ 8 | ≤ 12 |
| Decal sống / sinh mới mỗi khung | 12 / 2 | 24 / 4 | 48 / 4 | 64 / 6 |
| Đèn điểm, Rồng Giữ Ải (dựng sẵn, số cố định) | 0 | 0 | 1, đo rồi mới tăng | 2 |
| Đèn điểm, Tuyến Cuối (đã đo, `TS view/gun-rules.ts:28`) | 0 | 2 | 4 | 6 |
| Lớp trong suốt chồng lên nhau ở mỗi điểm ảnh, vùng sân | TB ≤ 2, đỉnh ≤ 4 | TB ≤ 3, đỉnh ≤ 6 | TB ≤ 3, đỉnh ≤ 8 trong tối đa 10 khung | như High |
| Méo không khí | tắt | tắt | chỉ khi số đo cho phép | nửa độ phân giải |
| Bloom | tắt | theo từng game | Rồng: chỉ khi đo vừa cổng; Tuyến Cuối: bật | bật |
| Texture VFX trong bộ nhớ GPU | ≤ 8 MB (bản 512²) | ≤ 16 MB | ≤ 32 MB | ≤ 48 MB |

**Vì sao đèn ở Rồng Giữ Ải chặt hơn:**
- Mỗi PointLight làm mọi vật liệu có chiếu sáng tốn thêm ở từng điểm ảnh: đất `MeshLambertMaterial` (`DH view/terrain.ts:1066`, `:1115`) và đám đông 220 quái có xương dùng `MeshStandardMaterial` (`DH view/crowd.ts:717`).
- Số đèn còn nằm trong khóa biên dịch shader, nên kho đèn phải dựng một lần lúc nạp, đèn rảnh thì để cường độ 0.
- Tuyến Cuối chiếu sàn bằng shader riêng có sẵn chỗ cho 6 đèn (`DECK_LIGHTS`, `gun-rules.ts:29`), nên đèn ở đó rẻ hơn.

**Gốc của các con số:**
- Bản nghiên cứu web đề xuất ≤ 40 draw call, ≤ 3.000 sprite, ≤ 300 mảnh; trung bình chồng ≤ 3 lớp, đỉnh ≤ 8 trong tối đa 10 khung [S15][S19][S20].
- Số hạt khớp với `05` §8; trần mỗi khung khớp với TK:2696.

**Về chi phí vẽ chồng (overdraw):**
- Chi phí = số lớp × số điểm ảnh mỗi lớp × số lệnh shader [S19].
- Vì vậy vài sprite lớn có thể đắt hơn nhiều hạt nhỏ.

**Khi chạm trần:**
- Hiệu ứng ưu tiên cao thay chỗ hiệu ứng ưu tiên thấp.
- Không bao giờ mất hiệu ứng từ T3 trở lên vì kho đầy (`05` §8, `FEEL` §6).

Đây là số đề xuất đầu, sẽ chỉnh lại sau lần đo đầu.

### 3.8 Bản giảm chuyển động

Mỗi game dùng công tắc nó đã có:
- **Tuyến Cuối:** `TS app/motion.ts`, hàm `motionReduced()`, ba mức: đầy đủ, theo hệ thống, giảm.
- **Rồng Giữ Ải:** tùy chọn `reducedMotion` ở `DH view/camera.ts:57`, `:273`; chuyển giá trị này cho cả `fx`.
- **Lời Gọi:** hiện đọc thẳng media query ở `TD view/boss-2d.ts:55`; đổi thành cài đặt của game khi lên 1C.

| Xử lý | Lớp |
|---|---|
| **Tắt** | Rung camera, camera kick, đẩy FOV, méo không khí, ám màu toàn màn, tách màu, đá "lơ lửng" (đá vẫn rơi) |
| **Làm dịu** | Đỉnh lóe ×0,6; bán kính lóe ×0,8; số hạt ×0,6; độ đục của vòm và khói ×0,6; chữ nảy 1,15× thay vì 1,25–1,45×; dừng hình vẫn giữ nhưng ≤ 45 ms |
| **Giữ nguyên** | Mọi lớp mang thông tin: mức nạp; báo trước; vòng cho biết vùng trúng; decal đánh dấu vùng đã đánh; lóe thân khi trúng (ngắn hơn); số sát thương; nghĩa của từ |

Mỗi lớp mới phải ghi rõ nó thuộc dòng nào ở bảng trên. Khi có preset dữ liệu (§4.2), mỗi emitter khai báo `reduced: keep | soften | drop`, và phép lint (phiếu 044) chặn preset thiếu khai báo.

---

## 4. Cách làm kỹ thuật

### 4.1 Chọn cách: tự xây, làm trong game trước

- **Giữ three.js 0.170 với WebGL2 và GLSL `ShaderMaterial`.** Kit viết toàn bằng GLSL, nên ở lại WebGL2. Lý do chưa chuyển:
  - Từ r164, TSL và node material chỉ chạy trên `WebGPURenderer` [S16].
  - Ở r170, các ví dụ WebGPU vẫn nằm trong nhóm "wip" [S17]; tới r171 `three/webgpu` mới dùng được ngay không cần cấu hình [S18].
  - Ngược lại, `ShaderMaterial` và `onBeforeCompile` không chạy trên `WebGPURenderer` [S16].
- **Làm thẳng trong view của game trước.**
  - Đòn chữ và Sky Fire dựng trong `DH view/fx.ts` và vài file mới cạnh nó.
  - Dùng lại kho có sẵn: pool của `FxCore`; shader fresnel PILLAR, SHIELD của kit (chưa dùng); `Debris` của kit; decal QuadPool; vòng phép `textures().runes` sinh bằng mã.
  - Chỉ rút thành module chung khi anh duyệt hướng hình **và** Tuyến Cuối cần cùng mảnh.
- **Mô hình dữ liệu kiểu Niagara: để sau** [S8].
  - Dữ liệu hóa (Effect gồm các pha, mỗi pha một danh sách emitter) chỉ làm khi đã có ít nhất ba hiệu ứng thật: đòn chữ, Sky Fire và một đòn của Tuyến Cuối.
  - Làm sớm hơn thì dễ đoán sai hình dạng dữ liệu.
- **Hạt vẫn mô phỏng trên CPU** như hiện nay. CPU đủ sức tới hàng chục nghìn hạt, trong khi ta chỉ dùng vài nghìn [S15].

### 4.2 Thư viện chung `shared/game-kit/vfx` (sau khi anh duyệt hướng hình)

**Nơi đặt và cách vào game:**
- Mọi phần mới nằm trong **module mới `vfx/`**. Module này được import `../three` và `../feedback`.
- **Không sửa `three/` và `feedback/`** khi còn làn đang chạy.
  - `pnpm kit:check` so mọi game có `kit.config.json` với kit hiện tại. Sáng 28/10 kết quả là: Rồng Giữ Ải OK, Lời Gọi OK; Tuyến Cuối và Tu Tiên lệch ở `feedback/index.ts`, `feedback/numbers.ts`.
  - Sửa `three/` hay `feedback/` sẽ làm Rồng Giữ Ải đỏ theo, trong khi không được `kit:sync` vào làn đang chạy.
  - Nếu buộc phải sửa, ghim kit cho game đang bận bằng khóa `pinned` trong `kit.config.json` (`scripts/sync-game-kit.mjs:98-105`), rồi bỏ ghim khi làn đó rảnh.
- Thêm module mới `vfx/` không làm đỏ game nào, vì `kit:check` chỉ xét các module game đó khai báo.
- Mỗi game muốn dùng thì ghi `vfx` vào `kit.config.json`. `kit:sync` chép module vào `src/kit/vfx/` và kiểm sha256 (`shared/game-kit/README.md`).
- Việc ở repo cha làm trong worktree riêng `typing-game-wt/vfx`, không trong bản checkout chính (đang ở nhánh Space `feat/space-typing-admin-uiux`). Map Factory cũng làm như vậy ở `typing-game-wt/map-codex`.

**Mỗi game giữ hai phần riêng:**
- Một **adapter** (`view/fx.ts` hiện có) đổi sự kiện sim thành hiệu ứng.
- Bộ **preset** của game ở `src/view/vfx-presets/*.ts`: màu, cỡ, texture theo chủ đề.

Phác thảo kiểu dữ liệu (định hướng; chỉ chốt khi đã có ba hiệu ứng thật):

```ts
// shared/game-kit/vfx/effect.ts
export type Phase = "charge" | "release" | "travel" | "impact" | "after"; // A R T I F
export type ActionClass = "key" | "shot" | "rapid" | "skill" | "ult" | "trap" | "foeStrike" | "death" | "boss";
export interface EmitterDef {
  layer: LayerKind;               // "ribbon" | "dome" | "debris" | "smokeDark" | "shards" | "decal" | "distort"
                                  // | "sparks" | "core" | "flash" | "glow" | "ring" | "rune" | "light" | "camera" | "hitstop" | ...
  at: "source" | "head" | "target" | "ground";
  socket?: string;                // "mouth", "castL", "muzzle", "core"...
  spawn: { burst?: number; rate?: number; perLetter?: number };
  delayF: number;                 // độ trễ trong pha, tính bằng khung 60 Hz
  lifeF: readonly [number, number];
  size: Curve; alpha: Curve; ramp: RampRow; hdr?: number;
  minQuality?: "low" | "medium" | "high" | "ultra";
  reduced: "keep" | "soften" | "drop";
}
export interface EffectDef {
  id: string; cls: ActionClass; tier: 0 | 1 | 2 | 3 | 4 | 5;
  phases: Partial<Record<Phase, readonly EmitterDef[]>>;
  skip?: Partial<Record<Phase, string>>;   // pha không áp dụng phải ghi lý do
}
```

| Phần | Việc | Lớp | Dựng trước ở đâu |
|---|---|---|---|
| `vfx/sprites.ts` | Sprite có chế độ kéo dài theo vận tốc; ăn mòn bằng nhiễu với hai ngưỡng để có viền nóng [S22]; ba kiểu trộn (cộng, thường, tối). Flipbook chỉ thêm khi có ảnh đạt | L4, L8, L10, L11 | `KIT ParticlePool`; Glows của `TS`; `ST:87-195` |
| `vfx/ribbon.ts` | Ribbon bám vị trí cũ: thon đuôi, cuộn UV, nhiễu; có thể dùng chữ của từ làm vệt | L1 | `KIT`: `Ribbon`, `FlameTrail`, `LightTrail` |
| `vfx/shell.ts` | Vỏ lưới: bán cầu, cầu, nón, trụ, tia; fresnel, ăn mòn, nở ra, viền nóng | L2, L9, L13 | Shader SHIELD, PILLAR của `KIT`; `DH banners.ts:56-77` |
| `vfx/shards.ts` | InstancedMesh đá và tinh thể: bay theo cung, nâng lơ lửng, nảy, nằm lại, viền nguội dần | L3, L5 | `KIT feedback/debris.ts`; `TS chunks.ts` |
| `vfx/decals.ts` | Decal phẳng hoặc ôm địa hình: vòng, vết cháy, vết nứt có khe sáng nguội dần, vòng rune | L6, L12, L13 | QuadPool của `DH`; `DH telegraphs.ts`; `ST:333-450` |
| `vfx/lights.ts` | Kho đèn với số lượng cố định theo bậc; mỗi lần chớp sáng đủ ngay khung đầu | L14 | `TS view/lights.ts`; `impactLight` ở `KIT stage.ts` |
| `vfx/distort.ts` | Buffer lệch UV ở nửa độ phân giải và một lượt toàn màn; chỉ ở bậc số đo cho phép | L7 | Mới [S26] |
| `vfx/camera.ts` | Camera kick, FOV, trauma, dừng hình theo bậc; có bản giảm chuyển động | L15, L16 | `KIT feedback/trauma.ts`, `hitstop.ts` (import, không sửa) |
| `vfx/palette.ts`, `vfx/textures.ts` | Ramp màu theo hàng; nhiễu và ramp sinh bằng mã (phiếu 039) | — | `KIT three/textures.ts` |
| `vfx/budget.ts` | Trần theo bậc (§3.7), thứ tự ưu tiên, bộ đếm cho `info()` của game | — | `05` §8, `FEEL` §6 |
| `vfx/effect.ts`, `vfx/runner.ts` | Chạy preset theo pha, độ trễ theo khung; neo vào socket hoặc đầu đạn; tôn trọng dừng hình; luồng ngẫu nhiên riêng có seed; không cấp phát bộ nhớ trong trận; vẽ ở tuổi 0 ngay khung đầu. **Làm sau cùng**, khi đã có ba hiệu ứng | tất cả | `FxCore` của `DH` (pool, hệ số cỡ `k` theo khoảng cách camera, `fx.ts:1335`) |

**Lời Gọi trước bước 1C:**
- Game vẫn vẽ bằng Canvas 2D, nên không chép module three vào.
- Bước tạm 2D chỉ sửa những chỗ thiếu nặng nhất (§5.4, làn V4a). Lớp cộng sáng vẽ bằng `globalCompositeOperation = "lighter"`.
- Khi lên 1C, Lời Gọi dùng thư viện này với bộ preset màu mực giấy.

**Học kỹ thuật từ Space Defense (`ST`), không import:**
- Ví dụ `explosion()` có 7 lớp (`ST:542-555`): chỉ chép **cách làm**.
- Lý do không import:
  - `tests/boundary.test.ts` của Lời Gọi cấm nhập từ Space;
  - sprite sheet của Space nằm ở `/assets/space-typing/combat-vfx/` (`ST:17`), trong khi mỗi game phải tự mang media của mình.
- Vì vậy kế hoạch chép "qua ngoại lệ" ở TK:2939-2940 phải viết lại.

**Mỗi game vẫn deploy độc lập:**
- Mã được chép vào từng game.
- Texture của game nào nằm ở `public/assets/<game-id>/vfx/` của game đó. Đây là media: không vào Git, sao lưu bằng `pnpm media:push`.
- `media:push` ghi `media.md5` vào bản checkout chính `games/<id>` (`scripts/media/commands/push.mjs:573-584`) và không tự commit. Đây là file Git của game. Vì vậy:
  - Chỉ Claude chạy `media:push`, và chỉ khi bản checkout chính của game đó không có làn nào đang chạy.
  - Claude commit `media.md5` cùng lúc gộp nhánh VFX.
  - Codex không chạy `media:push`.
  - Trong lúc chờ, ảnh vẫn dùng được ở worktree VFX, vì `public/assets` của worktree là liên kết tới media của bản checkout chính (`.wt-dh-m0b/public/assets`).
- Lúc chạy, không game nào đọc file của game khác hay của `shared/` (`docs/games/DEPLOY_INDEPENDENCE.md`).
- Mỗi lần đổi kit thì ghi một dòng vào `shared/game-kit/DRIFT.md`.

### 4.3 Có dùng thư viện ngoài không

| Lựa chọn | Tình trạng | Quyết định |
|---|---|---|
| three.quarks [S9][S10][S11] | MIT. Có sprite kéo dài, mesh, trail, soft particle, sub-emitter.<br>Bản mới 0.17.1 cần three ≥ 0.182; bản cuối cho 0.170 là 0.16.0 (189 KB, cộng gói quarks.core).<br>Trình sửa quarks.art chỉ xuất JSON khi trả phí, từ 12 USD mỗi người mỗi tháng. | **Không dùng bây giờ**, vì:<br>• khóa phiên bản three;<br>• công cụ GUI trả phí mà agent không điều khiển được;<br>• mô phỏng CPU không hơn của ta.<br>Lấy mô hình JSON và behaviour làm tham khảo. Xem lại nếu lên three ≥ 0.182. |
| three-nebula [S12] | MIT, hồi sinh năm 2026 (bản 13.3.0), 103 KB. Mô phỏng CPU; GPU chỉ trên WebGPU; không có trình sửa. | Không: không hơn kho hạt của ta. |
| pmndrs postprocessing [S13] | Zlib, bản 6.39.5, hợp three 0.170. Gộp nhiều hiệu ứng vào ít lượt vẽ [S15]. | Tùy chọn, thay cho EffectComposer + UnrealBloom. Đáng đo ở Rồng Giữ Ải nếu bloom ở High không vừa cổng. Chỉ đổi khi đo thấy lợi. |
| EmberGen [S27] | Công cụ GUI, 300 USD năm đầu; cần giấy phép mới xuất được PNG. | Không: anh sẽ phải chạy tay, trái với luật "AI làm toàn bộ VFX". |
| Babylon 9 [S28], @pixi/particle-emitter [S29] | Engine khác; gói Pixi chỉ cho Pixi < v8. | Chỉ để so sánh. |
| TSL / WebGPU [S16][S17][S18] | | Chưa dùng. Gom shader vào kit để sau này chuyển chỉ ở một chỗ. |

### 4.4 Texture

**Sinh bằng mã** (không phải media, không cần Codex vẽ). Sky Fire chỉ cần loại này:
- Nhiễu 256², liền mép, gói ba kênh: R là FBM, G là Voronoi, B là gradient.
- Ramp màu 256 × 16, mỗi hàng một bảng màu: lửa, vàng thánh, băng, độc, mục, mực.
- Mặt nạ vết nứt sinh từ nhiễu Voronoi (khe là đường biên ô), dùng tạm tới khi có ảnh đạt.
- Vòng phép: `textures().runes` có sẵn trong kit.
- Normal map cho vòng méo không khí.
- Atlas lóe, sao, vòng, lõi hiện có (`TS fx.ts:19-76`), chuyển vào kit khi rút thư viện.

Ở bước đầu, các texture này sinh ngay trong view của Rồng Giữ Ải. Phiếu 039 chuyển chúng vào kit sau.

**Ảnh Codex vẽ (ảnh 2D):**
- **Mức đạt:** ≥ 8/10. Ảnh chưa đạt thì sửa trước rồi mới vẽ lại, tối đa 3 lần (`docs/games/ART_ACCEPTANCE.md` §2.2).
- **Dạng ảnh:** ảnh xám có alpha; màu lấy từ ramp lúc chạy.
- **Chủ đề theo game:**
  - Rồng Giữ Ải: lửa rừng.
  - Tuyến Cuối: khoa học viễn tưởng.
  - Lời Gọi: mực giấy. Dùng lại 11 ảnh ở `art-src/vfx/` sau khi chấm lại (phiếu 043).

**Lô 1 (phiếu 038): không có flipbook.** Quota Codex thấp, và flipbook là loại khó đạt nhất.

| Ảnh | Cỡ | Ghi chú |
|---|---|---|
| Vết nứt đất | 2–3 ảnh 512², kèm mặt nạ khe nứt | Shader làm khe sáng nguội dần; thay mặt nạ sinh bằng mã nếu đẹp hơn |
| Vết cháy | 512² | |
| Dải quét, sợi khói tối | 512 × 128, liền mép theo chiều ngang | Cho vệt quét của quái và sợi tối |

**Để sau, chỉ làm khi cần thật:**

| Ảnh | Cỡ | Điều kiện |
|---|---|---|
| Khói | 1 ảnh tĩnh 512² cộng ăn mòn bằng nhiễu [S22] | Nếu khói sinh bằng mã chưa đạt |
| Lửa lặp, bùng nổ (flipbook) | 4×4 hoặc 6×6 ở 1024² | Chỉ khi ảnh tĩnh cộng ăn mòn không đủ. Phải qua phép kiểm lệch tâm, độ phủ và vòng lặp |
| Atlas rune theo chủ đề | 4×4 ở 1024² | Nếu `runes` của kit không hợp chủ đề |
| Vòng phép riêng | 1024² | Như trên |

**Định dạng lúc chạy:**
- Dùng WebP, khớp với `fireImages()` của kit (`KIT three/textures.ts:103`).
- KTX2 chiếm VRAM ít hơn 4–8 lần [S15] nhưng cần thêm bộ giải mã. Chỉ chuyển sang KTX2 khi đo thấy vượt trần ở §3.7.

**Quota Codex:**
- Chốt toàn bộ danh sách ảnh của một lô trước.
- Chạy lô ảnh một mình trong một cửa sổ 5 giờ; xong lô ảnh mới giao việc khác.
- Chọn model theo bảng "Chọn model" của `tools/codex-run/README.md`.

### 4.5 Trang xem hiệu ứng và kịch bản chụp

**Trong game: mở rộng showcase có sẵn, không làm Lab mới.**
- Rồng Giữ Ải có `runFxShowcase` (`DH view/bench.ts:881`), chạy bằng `dh-bench.mjs` với `SHOWCASE=1`.
- Thêm vào đó:
  - đồng hồ giữ, bước ±1 khung, tốc độ 0,25× hoặc 1×, lặp lại;
  - nền sáng (cỏ nắng), nền tối (bóng râm, đêm), bản đồ thật;
  - camera chơi và cận cảnh;
  - bật tắt từng lớp;
  - bộ đếm: draw call (`renderer.info`), hạt sống, đèn.
- Trang dev của game **không đọc file của repo cha**, kể cả ảnh tham chiếu ở `tmp/vfx/`. Một bản clone riêng của game phải chạy được (`DEPLOY_INDEPENDENCE` §1, luật 8), và Vite không nên mở quyền đọc ra ngoài thư mục game.

**Ở repo cha: công cụ ghép tờ khung** `tools/vfx-sheet/` (phiếu 037).
- Đặt ở `tools/` của repo cha, **không** ở `shared/game-kit/tools/`, vì thêm file vào module `tools` của kit sẽ làm `kit:check` của các game đỏ.
- Công cụ đọc thư mục ảnh chụp của game và ảnh tham chiếu trong `tmp/vfx/`, rồi ghép: trái là ảnh tham chiếu, phải là tờ khung.
- Công cụ tính các số đo tự động:
  - độ sáng khung đầu so với đỉnh;
  - phần trăm vùng sân bị trắng xóa;
  - độ bão hòa màu ở thân hiệu ứng;
  - tương phản dưới thẻ chữ.

**Kịch bản chụp** `scripts/visual/scenarios/<id>-vfx-*.mjs`, chạy qua `KIT tools/cdp-run.mjs`:
- **Mỗi hiệu ứng chụp đủ các tổ hợp:**
  - hai độ phân giải: 1280×720, 1920×1080;
  - hai nền: sáng, tối;
  - hai camera: camera chơi, cận cảnh;
  - bậc High (mặc định); thêm Ultra nếu High không có bloom.
- **Nhịp chụp:**
  - pha R và I: 24 khung, cách nhau 16,7 ms;
  - pha T: cách 33 ms;
  - pha F: cách 250 ms, tới khi hết dư âm.
- **Tờ khung** ghép bằng `magick montage`, nhãn mỗi khung ghi số khung, ms và pha. Trên macOS cần thêm `-font /System/Library/Fonts/Supplemental/Arial.ttf` (`FEEL` §7.2).
- **`meta.json` cho mỗi khung:** pha, `renderer.info`, bộ đếm hạt và đèn.
- **Cảnh trong trận:**
  - Rồng Giữ Ải: `dh-vfx-tiers` (`05` §10, chưa có), rồi `dh-boss` ở M2.
  - Tuyến Cuối: cảnh F5, F6 của `FEEL` §7.2, thêm cột pha.
  - Lời Gọi: `td-1b-ult`, `td-1b-boss`, thêm phần chấm điểm.
- **Clip ngắn chạy thời gian thật** (CDP screencast, khoảng 3 s) để anh xem cảm giác.

### 4.6 Sửa skill và quy trình (gọn)

1. **Skill ngắn cho ba game:** `.agents/skills/game-vfx-layered/SKILL.md`.
   - Đây là bản gốc; chép sang `.claude/skills` bằng `bash scripts/sync-agent-skills.sh`.
   - Nội dung: các bước dò sự kiện → chọn loại hành động (§3.3) → dựng → chụp → đo → chấm; trỏ tới tài liệu này và lệnh chụp.
   - Skill cũng chỉ đường dẫn tới các tài liệu tham chiếu mà Codex có nhưng Claude không nạp được dưới dạng skill, để Claude đọc trực tiếp:
     - `~/.agents/skills/threejs-aaa-graphics-builder/references/{technical-art,shader-cookbook,visual-scorecard}.md`;
     - `~/.agents/skills/threejs-gameplay-systems/references/game-feel.md`.
2. **`AGENTS.md`:**
   - Bảng "Skills by game" của repo cha thêm skill này và tài liệu này cho ba game.
   - `AGENTS.md` của mỗi game thêm một dòng trỏ về đây, **khi làn của game đó rảnh**. Hôm nay `AGENTS.md` của Tuyến Cuối đang được lượt n4n6 sửa.
3. **Mẫu brief:** mọi brief về VFX hay cảm giác phải nêu:
   - tài liệu này và skill;
   - ảnh tham chiếu;
   - loại hành động và công thức áp dụng (§3.3);
   - kịch bản chụp;
   - số đo nghiệm thu (§5.6);
   - file được sửa và file không được đụng;
   - lệnh kiểm `git status` và nhánh của mọi cây sẽ đụng, chạy lại ngay trước khi làn bắt đầu.
4. **Changelog:** mỗi lần cập nhật ghi một file `docs/changelog/<ngày>-<chủ đề>.md` của game, liệt kê các mục đã sửa.
5. **Không đếm lớp.** Nghiệm thu dùng danh sách kiểm 5 pha, số đo và điểm chấm cạnh ảnh tham chiếu (§5.6).

---

## 5. Kế hoạch

### 5.1 Thứ tự theo game

1. **Rồng Giữ Ải trước.**
   - Lời phàn nàn về phía người ra đòn hiện rõ nhất ở đây: Rồng phun lửa mỗi từ, ba chiêu không có lớp ra chiêu.
   - Mã hình mới nhất có 24 model Tripo (nhánh `m0b-models`, đã commit sạch), nên chấm được cùng model thật. Model Rồng có sẵn socket miệng, tay, cánh.
   - `05` §6 có bảng VFX đầy đủ nhất trong ba game.
   - Đã có chỗ bám để chụp (`runFxShowcase`).
   - Điều phải dè chừng: khoảng trống hiệu năng chỉ còn khoảng 2 ms (§3.7).
2. **Tuyến Cuối: một việc nhỏ làm ngay, phần lớn làm sau.**
   - Lỗi lớn nhất nhìn thấy được là lóe và đèn chỉ hiện 44–79 % ở khung đầu. Đây là bản sửa nhỏ, tách riêng (phiếu 035).
   - Mã nguồn của lượt n4n6 đã commit (`ce9dea3`); chỉ còn tài liệu đang sửa. Phiếu 035 chạy ngay khi lượt n4n6 commit nốt tài liệu.
   - Lượt lớn (pha A, R riêng từng súng; ribbon; Star Mortar đủ lớp) làm sau Rồng Giữ Ải, khi các mảnh đã được anh duyệt.
3. **Lời Gọi: sửa 2D rẻ ngay, hệ nhiều lớp ở bước 1C.** Hình 3D chỉ đến ở bước 1C. Bây giờ chỉ sửa những chỗ tệ nhất:
   - bắn không có hình;
   - cầu lửa vẽ thành mũi tên;
   - trúng đòn không lóe;
   - Draconis trên sân không ra chiêu khi dùng Tối Thượng.

### 5.2 Các bước và lịch dự kiến

Lịch là ước lượng tính theo ngày làm việc của agent, không phải lời hứa. Lịch phụ thuộc vào quota Codex và việc các làn đang chạy commit xong.

| Bước | Khi nào | Việc | Ai | Anh thấy gì |
|---|---|---|---|---|
| 0 | Giờ đầu, song song với bước 1 | Mẫu brief; skill ngắn; dòng trong `AGENTS.md` của repo cha (§4.6) | Claude | — |
| 1a | Ngày 1 | **Đòn chữ của Hỏa Long, trước và sau** (§5.3, phần 1). Kèm số đo `dh-perf` ở High: có và không có bloom, có và không có đèn miệng | Claude V2 | Tờ khung trước/sau, clip 3 s |
| 1b | Ngày 1, khi n4n6 commit tài liệu | Tuyến Cuối: sửa khung đầu cho lóe và đèn (phiếu 035). Claude kiểm trên trình duyệt; sau đó thêm đèn lúc Star Mortar phóng (ghi vào `FEEL` §4.2) | Codex 035; Claude V3 | Tờ khung F5 trước/sau |
| 1c | Ngày 1–2 | Lời Gọi V4a (§5.4). Codex làm ống sự kiện (phiếu 036), Claude vẽ | Codex 036; Claude V4 | Tờ khung trước/sau |
| 1d | Ngày 1–2 | Công cụ ghép tờ khung (phiếu 037). Bước 1a không chờ công cụ này: Claude ghép tạm bằng `magick montage` | Codex 037 | — |
| 2 | Ngày 2–4 | **Sky Fire đủ 5 pha** trong view của Rồng Giữ Ải (§5.3, phần 2) | Claude V2 | Tờ khung cạnh ảnh tham chiếu, clip 3 s |
| — | Song song, một cửa sổ quota | Ảnh lô 1 cho Rồng Giữ Ải (phiếu 038). Sky Fire không chờ lô này | Codex 038 | — |
| 3 | Sau khi anh duyệt bước 1a và 2 | Rút các mảnh đã duyệt thành module `vfx/` của kit (§4.2), trong worktree `typing-game-wt/vfx`. Texture sinh bằng mã vào kit (phiếu 039); phản biện độc lập (phiếu 040) | Claude V1; Codex 039, 040 | — |
| 4 | Sau bước 3 | Rồng Giữ Ải, theo từng lô:<br>• **Fire Breath:** lõi nóng ở miệng, ribbon lửa.<br>• **Dragon Roar:** nón ở miệng, vòm, méo nếu số đo cho phép.<br>• **Inferno:** biến hình; tia có mesh, neo ở miệng.<br>• **Quái:** mũi tên của cung thủ, vệt quét, màu phe địch, hạt khi Rồng trúng đòn, hiệu ứng xuất hiện. **Kéo lên làm ngay sau Sky Fire trong làn V2** (chủ dự án hỏi 28/10: "khi quái chém có hiển thị vết chém chưa").<br>• **Quái chết; Grove Warden.**<br>• **Bẫy:** chỉ sau khi `s6-traps` gộp; A và R dựng trên trạng thái "sẵn sàng" và "vừa kích" của lượt đó | Claude V2 | Mỗi lô một tờ khung, điểm chấm và changelog |
| 5 | Sau bước 3 | Tuyến Cuối:<br>• `kit:sync` (phiếu 041), khi làn Tuyến Cuối rảnh.<br>• Mỗi súng có pha A, R riêng: Heat Beam bật lên; Scatter Gun nạp.<br>• Ribbon cho đạn.<br>• Mảnh tinh thể băng cho Rail Gun.<br>• Star Mortar nổ đủ lớp: vòm, đá, vết cháy, cột khói.<br>• Lớp muội tối; bớt lõi trắng.<br>• Ảnh lô Tuyến Cuối (phiếu 042)<br>• **Quái ra đòn (chủ dự án 28/10):** quái bắn có lóe nòng, đạn có vệt màu phe địch, trúng tàu có lóe và mảnh; quái cận chiến có vệt quét; Pack Leader và Brute thêm pha R, I | Claude V3; Codex 041, 042 | Cảnh F5, F6 thêm cột pha; các số của `FEEL` §7.3 vẫn đạt |
| 6 | Theo lịch 1C | Lời Gọi V4b: bước 1C dùng thư viện với preset màu mực. Sửa `TK` §26.1 để pha A–F của tháp, Draconis, Tối Thượng, **quái ra đòn** (lóe khi ra đòn, đạn có vệt, lóe ở nạn nhân, quái trúng đòn có lóe thân) và quái chết theo loài nằm trong 1C (chủ dự án 28/10). Viết lại TK:2939-2940. Chấm lại 11 ảnh (phiếu 043) | Claude V4; Codex 043 | |
| 7 | Khi đã có ba hiệu ứng thật | Dữ liệu hóa preset và phép lint (phiếu 044) | Claude V1; Codex 044 | — |
| 8 | Theo mốc boss | Boss: Rồng Giữ Ải ở M2, Tuyến Cuối ở R3, Mộc Tinh 3D | Claude | |

**Thời gian của anh:** khoảng 15–20 phút cho mỗi tờ khung ở bước 1a và 2, cộng một lần chơi thử sau bước 4.

### 5.3 Bản đầu tiên anh xem

#### Phần 1: đòn chữ của Hỏa Long (bước 1a)

**Vì sao trước Sky Fire:** đòn chữ bắn sau mỗi từ, nên anh thấy nó hàng trăm lần mỗi trận. Sky Fire hồi 24 s (`DH content/rules.ts:418`). Lời anh "khi nhân vật bắn" chỉ thẳng vào đòn này.

| Pha | Lớp |
|---|---|
| A | • Mỗi chữ đúng: quầng ở socket `FX_MOUTH` lớn thêm một nấc, 2–3 đốm than bị hút vào miệng (L8, L11).<br>• Phần gồng của clip Attack chạy theo tiến độ gõ (§3.1, luật 3). |
| R | • Lóe miệng 2–3 khung, đủ sáng ngay khung đầu (L10).<br>• Một đèn ở miệng, dựng sẵn lúc nạp, 4–6 khung (L14), nếu số đo cho phép (§3.7).<br>• Đầu Rồng giật về sau (L18).<br>• Camera kick 1–2 px chỉ với đòn T3 (Chớp, Hoàn hảo); đòn thường không rung. |
| T | • Ribbon lửa thon đuôi thay `LightTrail` trơn (L1), dùng `FlameTrail` hoặc `Ribbon` của kit.<br>• Đầu đạn HDR 2–4 (L9 dạng billboard).<br>• Vệt cánh: tăng `trail` (`heroes.ts:216`) để ribbon ở `FX_WING_*` thấy được khi Rồng đánh và bay. |
| I | Giữ như hôm nay; thêm vết xém nhỏ 2 s (L6). |
| F | Một khói xám nhỏ (có sẵn) cộng vết xém. |

Khớp clip: ghi bảng `release` cho các clip Attack của Hỏa Long. Khoảng từ phím cuối tới khi đạn nhìn thấy rời miệng phải ≤ 50 ms.

#### Phần 2: Sky Fire đủ 5 pha (bước 2)

**Vì sao chọn Sky Fire:**
- Đây là một chiêu (T3) xảy ra trọn trong một lần dùng, nên dễ chụp.
- Nó hợp tự nhiên với các lớp của ảnh: vệt, vòm, đá, vết nứt, khói, tia, lõi.
- Hôm nay nó thiếu đúng thứ anh nói: không có gì nối Rồng với khối lửa (`DH fx.ts:621`).

**Cửa sổ thời gian:** sim đã có sẵn độ trễ 0,8 s từ lúc dùng chiêu tới lúc trúng, tức 48 khung (`DH content/rules.ts:418`). VFX chia cửa sổ này cho các pha, không đổi sim.

**Đường nối Rồng với đích:** khối lửa rời miệng Rồng và bay **một cung cao duy nhất** tới đích.
- Đường bay là cung bezier bậc hai. Điểm đầu là `FX_MOUTH`; điểm cuối là đích; điểm điều khiển nằm trên trung điểm, lệch về phía camera.
- Đường này thay cho điểm sinh cố định đích + (4, 16, 5) m (`fx.ts:621`).
- Ribbon thấy được trên suốt đường bay.
- Đích có thể cách Rồng khoảng 20 m, và ở góc nghiêng 40–75° camera không thấy trời (`DH view/stage.ts`, chú thích `MIST`). Vì vậy độ cao điểm điều khiển chọn sao cho **≥ 90 % đường bay nằm trong khung hình ở camera chơi**, ở cả 1280×720 và 1920×1080. Tờ khung kiểm điều này.
- Không dùng "cột lửa lên trời" ở bản trước: đỉnh cột nằm trên Rồng chứ không trên đích, và trời nằm ngoài khung.

| Pha | Khung (f0 = lúc dùng chiêu) | Lớp |
|---|---|---|
| A | f0–f12 | • Vòng rune quay dưới chân Rồng trên bệ (L13; texture `runes` của kit).<br>• 12 đốm than bị hút về miệng (L8).<br>• Lõi ở miệng sáng dần, HDR 1 → 3 (L9).<br>• Thân Rồng phát sáng (clip Cast và `setLook` ×1,9 có sẵn).<br>• Đèn miệng tăng dần, nếu bậc có đèn (L14).<br>• Báo trước phe ta ở đích (có sẵn, màu cam viền trắng). |
| R | f12–f20 | • Lóe miệng 2–3 khung, đủ sáng ngay khung đầu (L10).<br>• Nón lửa ngắn ở miệng, hướng theo đường bay (L13; vỏ fresnel như `banners.ts`, nhiễu cuộn UV), 8–12 khung.<br>• Vòng sóng dưới bệ (L12).<br>• Camera kick 2–4 px theo hướng phóng, FOV +1° trong 8 khung (L15).<br>• Đầu Rồng giật lên (L18).<br>• Đèn nhấp 6 khung. |
| T | f12–f48 | • Khối lửa bay theo cung từ miệng tới đích.<br>• Lõi cầu HDR (L9).<br>• Ribbon lửa thon đuôi, có nhiễu và cuộn UV (L1).<br>• Ribbon khói tối mảnh đi sau (L4).<br>• Than rơi; tia kéo dài (L8).<br>• Bóng lớn dần (có sẵn); tiếng rít (có sẵn). |
| I | f48–f63 | • Lóe trắng 2–3 khung (L10); lõi nở trong 6 khung.<br>• **Vòm sóng** bán kính 0 → 4 m (đúng vùng của luật) trong 12 khung, có viền nóng và ăn mòn (L2; shader SHIELD của kit).<br>• Vòng bụi phẳng 16 khung (L12).<br>• 10–16 viên đá vụn; 3 viên nâng lơ lửng 0,3 s rồi rơi (L3; `Debris` của kit).<br>• 6–8 mảnh đá than có cạnh phát sáng (L5).<br>• 40–70 tia lửa kéo dài (L8).<br>• Vòng méo 12 khung, chỉ ở Ultra lúc đầu; ở High chỉ khi số đo cho phép (L7).<br>• Đèn 12 khung (L14).<br>• Dừng hình 35 ms và trauma 0,16 theo bậc T3 (`05` §5; L16, L15).<br>• Quái lóe và giật (L17). |
| F | f63 → 7 s | • **Vết nứt** có khe đỏ nguội trong 1,5 s, rồi thành vết cháy tối, tắt ở giây thứ 7 (L6; mặt nạ sinh từ nhiễu Voronoi).<br>• 3–5 khói tối, mỗi đám 1,4–1,9 s (L4).<br>• Than bay lên 1–2 s (L8).<br>• Sao choáng (có sẵn); đá nằm lại 6 s. |

**Nộp cho anh (cả hai phần):**
- Tờ khung ở 1280×720 và 1920×1080, ở camera chơi và cận cảnh, trên nền sáng và nền tối.
- Bậc High (mặc định). Nếu High chưa có bloom, thêm một tờ ở Ultra để anh so.
- Sky Fire ghép cạnh ảnh tham chiếu.
- Ảnh trước và sau. Sky Fire hôm nay: `games/dragon-hold/tmp/test-browser-b/crops/skyfire-seq.jpg`.
- Số đo theo §5.6, kể cả `dh-perf`.
- Clip 3 s chạy thời gian thật.

### 5.4 Làn Claude

| Làn | Nơi làm | Việc | Không đụng |
|---|---|---|---|
| V2 Rồng Giữ Ải | Worktree mới `games/.wt-dh-vfx`, nhánh `dh-vfx` tách từ `m0b-models` @ `607c3c1`; tạo liên kết `public/assets` như `.wt-dh-m0b` | Bước 1a, 2, 4 | • `src/sim`, `src/content`, `tests/sim`.<br>• File của làn map-spike: `view/layout.ts`, `paint.ts`, `scatter.ts`, `terrain.ts`, `water.ts`, `impostor.ts`.<br>• `view/stage.ts`: chỉ sửa khối `STAGE_QUALITY` và bloom (map-spike sửa phần import và preview).<br>• Mã bẫy trong `actors.ts` và các nhánh bẫy trong `fx.ts`, tới khi `s6-traps` gộp.<br>• Bản checkout chính `games/dragon-hold`: không chạy `media:push` khi `s6-traps` còn chạy. |
| V3 Tuyến Cuối | Worktree mới `games/.wt-ts-vfx`, tách từ `main` sau khi n4n6 commit tài liệu | Kiểm phiếu 035; đèn Star Mortar; bước 5 | `src/sim`, `src/content`, `tests`; `src/kit` chỉ đổi qua `kit:sync` |
| V4 Lời Gọi | Worktree mới `games/.wt-td-vfx`, tách từ `main` của Lời Gọi (`e49189a`) | **V4a:**<br>• đọc `FX.fire`, `FX.hit` (qua phiếu 036);<br>• lóe ở miệng tháp và tháp nhún;<br>• cầu lửa có lửa và vệt;<br>• Cannon Tower: đạn bay theo cung, đánh dấu chỗ rơi, bụi, vết cháy;<br>• quái lóe khi trúng đòn;<br>• lửa đốt hiện trên quái thường;<br>• **Draconis ra chiêu trên sân khi dùng Fire Feather Rain:** bay lên, miệng sáng, lông lửa bung lên trời từ Draconis rồi mới rơi xuống vùng.<br>**V4b:** bước 1C. | Không gì dưới `src/sim`, `src/content`, `tests` (làn `a2-days` đang sửa ở đó; danh sách file cụ thể đổi theo giờ) |
| V1 Kit VFX | Worktree mới `typing-game-wt/vfx`, nhánh `vfx` từ `main` của repo cha | Bước 3, 7 | `three/`, `feedback/` của kit (§4.2); file trong các game, trừ `kit:sync` vào worktree VFX |

Luật chạy làn:
- Mỗi làn một agent, commit từng phần.
- **Trước khi một làn bắt đầu,** chạy lại `git status` và `git branch --show-current` ở mọi cây làn đó sẽ đụng, và đối chiếu với §5.7. Bảng §5.7 cũ đi chỉ sau vài giờ.
- Tối đa 3 tester cùng lúc, đúng 3 khe trình duyệt của `.local/bin/heavy.sh`.
- Mỗi làn một lượt test.

### 5.5 Phiếu Codex (nhỏ, kiểm được, không cần trình duyệt)

Luật chung:
- **Số phiếu 035–044.** Map Factory đã giữ 030–033 (`docs/tools/MAP_FACTORY.md` §9.2), và một workflow đang viết phiếu 031. Phiếu 034 đã xong (`docs/codex-queue/034-3d-requests-status.md`).
- Codex không commit. Claude chạy lại phép kiểm, xem diff hoặc tờ ảnh, rồi mới commit.
- Phiếu nào chạm tới hình ảnh thì Claude phải kiểm trên trình duyệt trước khi commit.
- Codex và Claude không bao giờ cùng ghi vào một worktree cùng lúc.

| Phiếu | Khi nào | Loại | Phạm vi ghi | Phép kiểm bắt buộc |
|---|---|---|---|---|
| 035 Khung đầu Tuyến Cuối | Ngay khi n4n6 commit tài liệu | Mã game | `games/.wt-ts-vfx`: `src/view/fx.ts` (Glows), `src/view/lights.ts` và test | • Test: hiệu ứng dài 3 khung được vẽ 100 % ở khung đầu.<br>• Test: đèn ở khung đầu sáng bằng `power`.<br>• `pnpm check` đạt.<br>• 152 trận cho mã băm như cũ (`FEEL` §7.1).<br>• Claude đo lại tương phản dòng từ (hiện 7,40–7,49, sàn là 7). |
| 036 Ống sự kiện Lời Gọi | Ngày 1 | Mã game | `games/.wt-td-vfx`: bộ đọc `FX.fire`, `FX.hit` ở view; bộ đếm `fx.stats()`; test | • Mỗi `FX.fire` sinh đúng một lời gọi lóe nòng, đúng vị trí và loại.<br>• Mỗi `FX.hit` sinh đúng một lời gọi trúng.<br>• Không cấp phát bộ nhớ mỗi khung.<br>• `pnpm check` đạt; golden như cũ.<br>Phần vẽ do Claude làm ở V4a. |
| 037 Công cụ ghép tờ khung và số đo | Ngày 1–2 | Công cụ Node, repo cha | `typing-game-wt/vfx`: `tools/vfx-sheet/` và test | Test trên ảnh mẫu sinh tổng hợp, có đáp án biết trước:<br>• tỉ lệ khung đầu so với đỉnh;<br>• phần trăm trắng xóa trong mặt nạ;<br>• độ bão hòa trong vòng;<br>• tương phản.<br>• Ghép trái ảnh tham chiếu, phải tờ khung, đúng nhãn.<br>Chạy bằng `node --test`. Không ghi vào `shared/game-kit`. |
| 038 Ảnh VFX lô 1 cho Rồng Giữ Ải | Một cửa sổ quota riêng | Ảnh | `games/dragon-hold/art-src/vfx/`, `public/assets/dragon-hold/vfx/` (media, không vào Git); báo cáo. Không chạy `media:push` | Lô gồm: 2–3 vết nứt kèm mặt nạ, 1 vết cháy, 1 dải sợi khói. Không flipbook.<br>• Đúng cỡ (`magick identify`).<br>• Viền alpha 0 rộng ≥ 4 px.<br>• Dải liền mép theo chiều ngang.<br>• Không chữ, không logo.<br>• Tờ ghép trên nền sáng và nền tối.<br>• Tự chấm ≥ 8, kèm lý do.<br>• md5 trước và sau.<br>• Mỗi ảnh có `.prompt.txt`. |
| 039 Texture sinh bằng mã vào kit | Bước 3 | Mã kit | `typing-game-wt/vfx`: `shared/game-kit/vfx/textures.ts` và test | • Liền mép: sai khác giữa mép trái và mép phải < ε.<br>• Cùng seed cho cùng mã băm.<br>• Ramp có độ sáng đơn điệu.<br>• Chạy được trong Node, không cần DOM.<br>• Mỗi texture sinh trong ≤ 30 ms.<br>• `pnpm kit:test` đạt; `pnpm kit:check` không đỏ thêm game nào. |
| 040 Phản biện độc lập phần rút vào kit | Bước 3 | Chỉ đọc | Báo cáo | • Chạy lại kit test.<br>• Kiểm sha256 sau `kit:sync` vào worktree VFX.<br>• Golden của Rồng Giữ Ải không đổi.<br>• Đọc mã: không cấp phát trong vòng khung.<br>• Trần ngân sách được áp thật.<br>• Không file nào trong `three/`, `feedback/` bị sửa. |
| 041 `kit:sync` vào Tuyến Cuối | Bước 5, khi làn Tuyến Cuối rảnh | Mã | `games/.wt-ts-vfx/src/kit/` | • sha256 khớp.<br>• `pnpm check` đạt; golden như cũ. |
| 042 Ảnh VFX Tuyến Cuối | Sau khi lô 038 đạt và anh duyệt Sky Fire | Ảnh | `games/typing-survival/art-src/vfx/`… | Như phiếu 038, chủ đề khoa học viễn tưởng. |
| 043 Chấm lại 11 ảnh VFX Lời Gọi | Bước 6 | Ảnh, chấm | `games/typing-defense/art-src/vfx/` | • Chấm 11 ảnh theo mức 8/10; ghi riêng `ma-troi-sheet` chỉ có prompt.<br>• Đưa về chuẩn alpha của phiếu 038.<br>• Vẽ thêm: khói mực, atlas chữ, vết cháy giấy. |
| 044 Lint preset | Bước 7, khi đã có ba hiệu ứng dạng dữ liệu | Mã kit | `typing-game-wt/vfx`: `shared/game-kit/vfx/lint.ts` và test | • Mỗi preset đủ 5 pha, hoặc có `skip` kèm lý do.<br>• Lóe ≤ 3 khung và đủ sáng ở tuổi 0.<br>• Tổng theo bậc ≤ trần ở §3.7.<br>• Preset phe địch không dùng ramp lửa của phe ta.<br>• Mọi emitter có khai báo `reduced`.<br>• **Không** đếm số lớp. |

### 5.6 Nghiệm thu

Một hiệu ứng, hay một lô, đạt khi qua đủ sáu điều:
1. **Đủ 5 pha** theo §3.3, với các lớp bắt buộc của loại hành động. Pha bỏ phải có lý do trong changelog.
2. **Số đo** (bản đầu, sẽ chỉnh sau lần đo đầu):
   - khung đầu của lóe và đèn ≥ 95 % đỉnh;
   - trắng xóa ≤ 6 % vùng sân (chiêu cuối ≤ 15 % trong tối đa 3 khung);
   - tương phản thẻ chữ ≥ 7 : 1 ở p99 trong lúc hiệu ứng chạy;
   - bán kính vùng trúng trên màn khớp với luật, sai số ± 10 %;
   - đầu đạn ≥ 20 × 6 px ở 720p;
   - từ phím cuối tới khi đạn rời nguồn ≤ 50 ms.
3. **Trong cổng khung của từng game** (§3.7):
   - Rồng Giữ Ải ở High: trung bình ≤ 8 ms, p95 ≤ 12 ms (`05` §8, `dh-perf`), đo trên cảnh M0b, gồm cả bloom nếu bật;
   - Tuyến Cuối: theo `FEEL` §6;
   - Lời Gọi: `td-1b-perf`.
4. **Sim không đổi:** golden và mã băm trận như cũ.
5. **Chấm hình:**
   - Một agent chấm tờ khung đặt cạnh ảnh tham chiếu, thang 10, dựa trên hàng VFX của `visual-scorecard.md`.
   - Các tiêu chí:
     - đủ pha, nhất là phía người ra đòn;
     - chiều sâu nhiều lớp;
     - sáng và màu, không nhạt;
     - dễ đọc;
     - nhịp và độ "đã";
     - hợp chủ đề game.
   - Đạt từ 8 điểm. Điểm 7,5–8,5 thì thêm một người chấm độc lập.
   - **Lửa của Rồng ở Dragonhold** (đòn chữ, Sky Fire; chủ dự án 29/10 tối, sau clip Firefly thử): **nhắm 9, nhận từ 8,5**. Hai giám khảo độc lập đều phải từ 8,5; so cạnh game thương mại cùng loại, không so với vòng trước. Chất lửa (nổ, khói, cầu lửa, tàn lửa) lấy từ flipbook video Firefly của Adobe (`docs/games/vfx/FIREFLY_VFX_LIST.md`).
   - Chấm ở cả 1280×720 và 1920×1080.
6. **Anh xem:**
   - Anh xem bản đầu (đòn chữ và Sky Fire); mỗi lô sau có một clip ngắn.
   - Anh chơi thử trên một bản build hoặc worktree mà không agent nào đang sửa.

### 5.7 Khớp với các làn đang chạy (kiểm lúc 28/10, khoảng 03:00)

| Nơi | Nhánh @ HEAD | Đang sửa (chưa commit) | VFX làm gì |
|---|---|---|---|
| `games/dragon-hold` (bản checkout chính) | `s6-traps` @ `abc2a75` | `src/sim/traps.ts`, `src/sim/houses.ts`, `src/content/data/our-side.ts`, `src/content/types.ts`, `scripts/balance/policy.ts`, `tests/sim/ourside-*.test.ts`. Brief bước 6 (`dh-owner-27-10-wf_41bb40a8-014.js`, dòng 54) còn thêm: Pine Bomb nổ khi ≥ 2 quái trong 3 m, Herb Hut phát sau 3 lần hạ, chữ của Net Launcher trong shop, trạng thái "sẵn sàng" và "vừa kích" cho mọi ô bẫy và ô nhà | Không đụng. Lô VFX bẫy chỉ làm sau khi `s6-traps` gộp, dựng trên hai trạng thái đó. Không chạy `media:push` trong lúc này (nó ghi `media.md5` ở cây này) |
| `games/.wt-dh-m0b` | `m0b-models` @ `607c3c1` | Sạch. Nhánh này chưa vào `s6-traps` | V2 tách nhánh từ HEAD này; không sửa gì trong worktree này |
| `games/.wt-dh-mapspike` | `map-spike` @ `f7f1576` | Sạch. Nhánh sửa `view/layout.ts`, `paint.ts`, `scatter.ts`, `terrain.ts`, `water.ts`, `impostor.ts`, và phần import, preview của `stage.ts` | Không đụng các file đó; ở `stage.ts` chỉ sửa khối `STAGE_QUALITY` và bloom; gộp sau |
| `games/.wt-dh-d27c`, `games/.wt-dh-codex` | `d27-counter`, `codex-023-easy-hint` | changelog D27 ở `.wt-dh-d27c` | Không đụng |
| `games/typing-survival` | `main` @ `ce9dea3` (mã n4n6 đã commit) | Chỉ tài liệu: `AGENTS.md`, `docs/BUILD_S1.md`, `docs/FEEL_PASS_S1.md`, `docs/changelog/2026-10-27-feel-n4n6.md` | Phiếu 035 chạy ngay khi các file này commit, ở `.wt-ts-vfx` |
| `games/typing-defense` | `a2-days` @ `e49189a`, trùng `main` | `src/content/rules.ts`, `src/content/slice-1a.ts`, `src/sim/systems/economy.ts`, `src/sim/systems/waves.ts`, `tests/td-sim-economy.test.ts` | V4 tách từ `main`, không đụng gì dưới `src/sim`, `src/content`, `tests` |
| `typing-game-wt/map-codex` | `map-factory` | Map Factory; phiếu 030–033 đã giữ, workflow đang viết phiếu 031 | Không đụng; số phiếu VFX bắt đầu từ 035 |
| Repo cha (bản checkout chính) | `feat/space-typing-admin-uiux` | Việc Space; tài liệu này chưa theo dõi | Việc VFX ở repo cha làm trong `typing-game-wt/vfx` |
| `shared/game-kit` | | `kit:check`: Rồng Giữ Ải OK, Lời Gọi OK; Tuyến Cuối, Tu Tiên lệch ở `feedback/` | Chỉ thêm module mới `vfx/` (§4.2). Game khác đồng bộ khi làn của nó rảnh (`DRIFT.md` đã nhắc Tuyến Cuối và Lời Gọi đồng bộ lại `feedback/`) |

---

## 6. Rủi ro và câu cần anh quyết

### 6.1 Rủi ro

| Rủi ro | Cách giảm |
|---|---|
| **Rồng Giữ Ải hết chỗ hiệu năng.** Cổng 8 ms, đo 5,93 ms khi máy rảnh và 8,16 ms khi máy bận; bloom tốn thêm 2,2 ms; mỗi đèn làm đất và 220 quái tốn thêm | • Ngân sách tính từ khoảng trống đo được (§3.7).<br>• Đo bloom và đèn miệng ở High ngay ở bước 1a, trước khi hứa.<br>• Không vừa thì High dùng quầng sprite, bloom ở lại Ultra; đưa anh quyết (§6.2).<br>• Thử `pmndrs postprocessing` nếu cần bloom rẻ hơn. |
| Sân trắng xóa, chữ bị che. Tuyến Cuối đang sát sàn tương phản (7,40–7,49, sàn là 7) | • Luật §3.6 và số đo tự động.<br>• Đo lại sau mỗi lần đổi ánh sáng gần tấm chữ. |
| Đụng các làn đang chạy. Rồng Giữ Ải có ba nhánh tách nhau: `m0b-models`, `map-spike`, `s6-traps` | • Mỗi làn VFX một worktree riêng, có danh sách không đụng (§5.4, §5.7).<br>• Kiểm lại `git status` và nhánh trước mỗi làn.<br>• Bẫy làm sau khi `s6-traps` gộp. |
| Kit lệch nhau giữa các game | • Chỉ thêm module `vfx/`; không sửa `three/`, `feedback/` khi còn làn chạy; ghim kit nếu buộc phải sửa.<br>• Ghi `DRIFT.md`. |
| `media.md5` va chạm với làn đang chạy | Chỉ Claude chạy `media:push`, chỉ khi bản checkout chính rảnh; commit `media.md5` lúc gộp nhánh VFX. |
| Ảnh do AI vẽ không đạt; quota Codex thấp | • Lô 1 không có flipbook.<br>• Sky Fire chỉ dùng texture sinh bằng mã.<br>• Mỗi cửa sổ quota chỉ một lô ảnh. |
| Thay đổi hình do Codex làm hỏng khi chạy trên trình duyệt (đã xảy ra ở phiếu 021, 023) | • Codex chỉ làm logic, công cụ, test.<br>• Claude kiểm trên trình duyệt trước khi commit. |
| VFX lấn vào sim, làm đổi golden | • VFX chỉ nằm ở view.<br>• Golden và mã băm là cổng chặn. |
| Quá nhiều lớp làm màn hình rối | Lớp tăng theo bậc (§3.3); súng bắn nhanh có trần theo phím. |
| Chớp sáng gây khó chịu | • Tối đa 2 lần chớp toàn màn mỗi giây.<br>• Có bản giảm chuyển động (§3.8). |
| Việc làm 2D của Lời Gọi bị bỏ khi lên 1C | Chỉ sửa 2D ở mức tối thiểu (V4a). |
| Cung bay của Sky Fire ra ngoài khung ở camera chơi | Chọn độ cao điểm điều khiển theo tờ khung: ≥ 90 % đường bay trong khung ở cả hai độ phân giải. |
| Sau này lên WebGPU, shader GLSL không chạy được [S16] | Gom shader vào kit để chỉ phải chuyển ở một chỗ. |
| Khung đen sau khi nạp Rail Gun ở Tuyến Cuối (chưa rõ nguyên nhân, ghi trong `AGENTS.md` của game) dễ bị nhầm là lỗi VFX | Ghi thành mục riêng, không gộp vào lượt VFX. |

**Chỗ em không theo phản biện:** phản biện đề xuất thêm rung khi Star Mortar phóng. Em chỉ thêm đèn, vì `FEEL` §4.6 đặt cú đẩy lúc phóng bằng 0 sau nghiên cứu Typing Break, và cổng rung p95 ≤ 3 px.

### 6.2 Câu cần anh quyết

Không có câu nào chặn việc bắt đầu. Theo lời anh giao ngày 27/10, em làm theo đề xuất. Có hai việc chỉ anh quyết được:

1. **Xem và chấm bản đầu** (đòn chữ trước/sau, rồi Sky Fire). Đây là chuyện gu; các game sau sẽ theo hướng anh chọn.
2. **Chỉ khi số đo ở bước 1a cho thấy bloom không vừa cổng 8 ms của Rồng Giữ Ải ở High:** chọn một trong ba cách.
   - **(a) Mặc định của em:** High không bloom, độ sáng nhờ quầng sprite, đèn và lớp tối; bloom ở lại Ultra.
   - **(b)** Nới cổng High của Rồng Giữ Ải, ví dụ trung bình 8 → 9 ms.
   - **(c)** Bật bloom ở High nhưng hạ độ phân giải High từ DPR 1,25 xuống 1,0.

   Em làm (a) trước. Em chỉ hỏi nếu tờ khung ở (a) vẫn nhạt khi đặt cạnh bản Ultra.

Những điểm dưới đây em làm theo mặc định; anh chỉ cần lên tiếng nếu muốn khác:
- Ảnh tham chiếu dùng làm mẫu cho **cách chồng lớp**, không chép phong cách vàng–đen. Mỗi game giữ màu và chủ đề của mình.
- Lời Gọi đưa VFX đủ 5 pha cho tháp, Draconis, Tối Thượng và quái chết vào phạm vi bước 1C (sửa `TK` §26.1).
- Không mua công cụ trả phí (EmberGen, quarks.art).

---

## Nguồn

### Trong repo

- **Ảnh tham chiếu:** `tmp/vfx/owner-reference-layered-vfx.webp`
- **Rồng Giữ Ải:**
  - mã: `games/.wt-dh-m0b/src/view/{fx,telegraphs,banners,heroes,actors,crowd,stage,camera,bench,terrain}.ts`, `src/content/rules.ts:418`;
  - model: `draconis-v2.high.glb` (socket `FX_MOUTH`, `FX_CAST_L/R`, `FX_WING_L/R/L2/R2`, `FX_TAIL`, `FX_CORE`, `FX_HALO`);
  - số đo: `games/.wt-dh-m0b/docs/changelog/2026-10-27-m0b-models.md:15`, `:89`;
  - kịch bản chụp: `scripts/visual/scenarios/dh-*.mjs`;
  - thiết kế: `docs/games/dragon-lane/05-presentation-audio-tech-split.md` §2.1, §4.3, §5, §6, §6.5, §8, §10;
  - brief làn bẫy: `~/.claude/projects/-Users-toandx-htdocs-typing-game/157c54d6-5a15-4acc-b09d-0aae10862f93/workflows/scripts/dh-owner-27-10-wf_41bb40a8-014.js`, dòng 54.
- **Tuyến Cuối:**
  - mã: `games/typing-survival/src/view/{fx,shots,beams,combat,gunfx,lights,ship,chunks,typing-feel,hazard-fx,scene,gun-rules}.ts`, `src/app/{main,motion}.ts`;
  - đặc tả và changelog: `docs/FEEL_PASS_S1.md` §4, §6, §7, §12, `docs/changelog/2026-10-27-feel-n4n6.md`.
- **Lời Gọi:**
  - mã: `games/typing-defense/src/view/{debug-2d,fx-2d,boss-2d,audio-min}.ts`, `src/sim/systems/{combat,projectile}.ts`, `src/view/words/cards.ts`;
  - thiết kế: `docs/td/TYPING_DEFENSE_DESIGN.md` §23.8, §25.2, §26.1;
  - ảnh: `art-src/vfx/` (11 ảnh, 12 prompt).
- **Kit:** `shared/game-kit/README.md`, `DRIFT.md`, `three/{particles,materials,textures,stage,hero}.ts`, `feedback/*`; `scripts/sync-game-kit.mjs`.
- **Media:** `scripts/media/commands/push.mjs`; `media.md5` của từng game.
- **Space:** `games/space-typing/src/defense/view/vfx.ts` (chỉ kỹ thuật); `games/space-typing/art-src/combat-vfx*`.
- **Quy trình:**
  - `AGENTS.md`, `docs/AGENT_SKILLS_SETUP.md`, `scripts/sync-agent-skills.sh`;
  - `.agents/skills/combat-vfx-audio/`;
  - `~/.agents/skills/threejs-*`;
  - `docs/games/{ART_ACCEPTANCE,NAMES_EN,DEPLOY_INDEPENDENCE}.md`;
  - `tools/codex-run/README.md`, `docs/CODEX_QUEUE.md`, `docs/tools/MAP_FACTORY.md` §9.2.

### Web (truy cập ngày 28/10/2026)

- S1 https://www.vfxapprentice.com/blog/the-soul-of-effects-what-is-timing-in-vfx
- S2 https://realtimevfx.com/t/stylized-frag-launcher-explosion-overwatch-inspiration-breakdown-posted/1894?page=2
- S3 https://sourcegaming.info/2015/11/11/thoughts-on-hitstop-sakurais-famitsu-column-vol-490-1/ (11/11/2015)
- S4 https://uhiyama-lab.com/en/notes/unity/unity-game-feel-hit-feedback/ (16/07/2026, sửa 10/10/2026)
- S5 https://www.wayline.io/learn/game-feel/1
- S6 https://www.youtube.com/watch?v=AJdEqssNZ-U (liên kết từ https://itch.io/post/3680470)
- S7 https://www.gamedeveloper.com/programming/video-sprucing-up-cameras-with-math (GDC 2016)
- S8 https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-niagara-effects-for-unreal-engine và https://docs.unrealengine.com/4.27/RenderingAndGraphics/Niagara/Overview
- S9 https://github.com/Alchemist0823/three.quarks và https://raw.githubusercontent.com/Alchemist0823/three.quarks/master/CHANGELOG.md
- S10 https://registry.npmjs.org/three.quarks và https://data.jsdelivr.com/v1/packages/npm/three.quarks@0.16.0
- S11 https://quarks.art/
- S12 https://github.com/creativelifeform/three-nebula và https://registry.npmjs.org/three-nebula
- S13 https://registry.npmjs.org/postprocessing
- S14 https://react-postprocessing.docs.pmnd.rs/effects/bloom và https://discourse.threejs.org/t/pmndrs-post-processing-selective-bloom-renders-differently-on-chrome-vs-firefox/59433
- S15 https://www.utsubo.com/blog/threejs-best-practices-100-tips (sửa 11/09/2026)
- S16 https://threejs.org/manual/en/webgpurenderer và https://discourse.threejs.org/t/r164-nodes-no-longer-working-with-webgl-webgl2/64909
- S17 https://raw.githubusercontent.com/mrdoob/three.js/r170/examples/files.json
- S18 https://buttondown.com/webgamedev/archive/issue-024/ (12/2024)
- S19 https://docs.unrealengine.com/udk/Three/VFXOptimizationResults.html và https://docs.imgtec.com/performance-guides/graphics-recommendations/html/topics/optimal-particle-rendering-on-powervr.html
- S20 https://developer.nvidia.com/gpugems/gpugems3/part-iv-image-effects/chapter-23-high-speed-screen-particles
- S21 https://discourse.threejs.org/t/soft-particles-rendering-performance/27610 và https://keaukraine.medium.com/implementing-soft-particles-in-webgl-and-opengl-es-b968d61133b0
- S22 https://vfxdoc.readthedocs.io/en/latest/shaders/alpha-erosion/, https://mirzabeig.substack.com/p/unity-tutorial-dissolve-shader-part-1 và https://realtimevfx.com/t/shannon-mcsheehan-lol-fx-knowledge-share/1133/171
- S23 https://pmnd.rs/blog/creating-flow-shield và https://quirkbit.itch.io/adrift-arena/devlog/122433/creating-stylised-explosions
- S24 https://drei.docs.pmnd.rs/abstractions/trail
- S25 https://discourse.threejs.org/t/adding-and-removing-three-js-lights-at-run-time/3303
- S26 https://drei.docs.pmnd.rs/shaders/mesh-transmission-material và https://tympanus.net/codrops/?p=44326
- S27 https://jangafx.com/software/pricing
- S28 https://blogs.windows.com/windowsdeveloper/2026/03/26/announcing-babylon-js-9-0 (26/03/2026)
- S29 https://registry.npmjs.org/@pixi/particle-emitter
- S30 https://realtimevfx.com/t/best-ways-to-optimize-vfx-in-unreal/828?page=2
