# Map 1 lên mức production: kế hoạch chung cho ba game (28/10/2026)

Mục tiêu của chủ dự án (28/10): "làm xong map 1 của mỗi game để tôi thử, phải ở mức một game sắp lên production". Tạm dừng tính năng mới. Map 1 phải qua bảy cổng G1–G7.

Nguồn: ba bản kiểm kê ngày 28/10. Rồng Giữ Ải ở `main` `02fe9c7`, Lời Gọi ở `a2-days` `a5cc147`, Tuyến Cuối ở `main` `bf0e6f9`. Tờ khung và số liệu nằm trong `games/<id>/tmp/map1-audit/`.

## 0. Tóm tắt

- Chưa game nào qua đủ bảy cổng. Rồng qua G1. Lời Gọi và Tuyến Cuối chưa qua cổng nào trọn vẹn.
- G7 chặn cả ba game theo cùng một cách: từ vựng đọc từ repo cha, và nginx đang cài chưa có host của game. Chủ dự án chạy một lệnh sudo là xong phần nginx.
- Tuyến Cuối gần nhất (khoảng 40 giờ Claude). Rồng ở giữa (khoảng 70 giờ, phần lớn là VFX và chống nhàn). Lời Gọi xa nhất (khoảng 235 giờ), vì map 1 phải lên 3D (bước 1C).
- Ngày dự kiến đủ bảy cổng: **Tuyến Cuối 03/11, Rồng Giữ Ải 06/11, Lời Gọi 12/11**.
- Chủ dự án làm khoảng 3 giờ: một tin trả lời quyết định, một lần sudo, duyệt VFX, nghe âm và chơi một ván B9 cho mỗi game.

## 0.1. Đối chiếu với hiện trạng (khi viết kế hoạch)

Ba bản kiểm kê viết song song. Tôi đối chiếu lại với repo và sửa mấy chỗ sau:

- **Phiếu Codex đã có:** 088 (TS-M1-07), 089 (TS-M1-09), 090 (TS-M1-02), 091 (phần từ vựng của A9), 092 (TS-M1-20), 093 (liền mép ô đất của map pilot Rồng). Lane M1 có 088, 089. Lane M2 có 093, 090, 092, 091. Lô mới bắt đầu từ 094 (`CODEX_BATCH.md`).
- **I5 của Lời Gọi gần xong:** phiếu 043 đã nhận ngày 28/10 (14 ảnh VFX alpha sạch, có `ink-smoke`, `brush-glyphs`, `paper-burn`, `scorch-mark` vẽ lại). Chỉ còn decal nứt rễ báo trước của Mộc Tinh và dải bọt thác (phiếu 099, khoảng 1 giờ).
- **Pin từ vựng** là `18338405` (27/10, sau đợt sửa nghĩa 024), không phải `56d3721d` như DEPLOY_INDEPENDENCE §8 còn ghi. Phiếu 090, 091 đã dùng `18338405`; phiếu 100 của Rồng dùng cùng pin.
- **Rồng chưa có worktree cho Codex.** Phải tạo `games/.wt-dh-codex` từ `main` `02fe9c7` trước khi lane M2 chạy tới phiếu 100.
- **`cdp-run.mjs` có ở hai nơi:** bản kit (`shared/game-kit/tools/`, chép vào `src/kit/tools/` của mỗi game) và bản riêng của Rồng (`scripts/visual/cdp-run.mjs`). Cả hai chọn cổng ngẫu nhiên 9300–9899 (A11).
- **Làn VFX 2D của Lời Gọi (`.wt-td-vfx`, V4a):** khi map 1 lên 3D, view 2D chỉ còn là bậc Low và đường lùi. Đề xuất gộp phần đã nhận (036 `FxPipe`) rồi dừng làn này, để lấy chỗ cho làn 1C. Thiết kế 5 pha của V4a dùng tiếp ở C11.

---

## 1. Rồng Giữ Ải (map 1: L2-cau)

### 1.1. Cổng

| Cổng | Kết quả | Bằng chứng |
|---|---|---|
| G1 lỗi, bot, phím thật | **Đạt** | Bot và phím CDP thật thắng 10/10 ở 1280 và 1920, mã băm phát lại khớp, 0 lỗi console (bản dev). |
| G2 hình | Trượt | Tự chấm cảnh map 7/10 (1080p) và 6,5/10 (720p). G01, Herb Hut, Spikes khó đọc. Bậc Low còn khối tạm. Chưa có giám khảo độc lập. |
| G3 cảm giác | Trượt | Đòn chữ chỉ là một chấm cam nhỏ. Hầu hết đòn thiếu pha. 52,4 % thời gian đợt không có chữ. Âm chưa ai nghe. Thẻ chữ đạt. |
| G4 hiệu năng | Một phần | High trung bình 5,21 ms, p95 9,8 ms; Medium đạt. Lần chơi đầu tải 12,4–12,7 MB (ngân sách 5 MB). |
| G5 trải nghiệm | Một phần | Thẻ tốc độ, tạm dừng, thua, chơi lại chạy tốt. Thiếu màn tựa, màn cài đặt, lối về cổng game. Tên ải còn "Bản thử". |
| G6 cân bằng | Một phần | G1 bot 86,7 %, hầu hết cổng đạt. B1 lệch 6 ô, B7 lệch 2 ô. Nhàn I trên dải D27. Chưa có B9. |
| G7 build tự đứng | Trượt | Bản build không có từ vựng: quái không có chữ, thua ở đợt 1, không báo gì. nginx chưa có host dragon. |

### 1.2. Việc P0 và P1 (theo thứ tự nên làm)

1. **DH-01** · P0 · G7. Bản build không có từ vựng. **Sửa:** chép bản ghim (pin `18338405`, 100 level, `ATTRIBUTION.md`, manifest sha256) vào `public/vocabulary/`, thêm test. **Ai:** Codex mã (phiếu 100), Claude duyệt. **2,5 h.**
2. **DH-02** · P0 · G7. Bộ từ rỗng mà người chơi không được báo. **Sửa:** khi deck rỗng thì hiện thông báo tiếng Việt và không vào đợt. Có DH-01 rồi thì bỏ alias `/vocabulary/`, `/typing-texts/` của host dragon trong `infra/nginx`. **Ai:** Claude (làn T). **1,5 h.**
3. **DH-03** · P0 · G7. nginx đang cài chưa có host dragon; `/etc/hosts` thiếu tên; `portal/dist` cũ. **Sửa:** Claude chạy `pnpm build:local`; chủ dự án chạy `sudo bash scripts/setup-nginx.sh play` (một lần cho cả ba game). **Ai:** chủ dự án. **0,5 h.**
4. **DH-04** · P0 · G7. Chưa chơi thử qua cổng game. **Sửa:** kịch bản CDP mở `https://typing-game.local`, vào Rồng, chơi đợt 1 ở 1280 và 1920; 0 request hỏng, 0 request sang nguồn khác, quái có chữ, cầu học nhận sự kiện. **Ai:** Claude (làn T). **1 h.**
5. **DH-12** · P1 · G7. Map pilot chỉ nạp ô đất và decal từ `/art-src` ở bản dev. **Sửa:** trước khi gộp pilot, bản build phải mang ô đất và decal đã xử lý dưới `/assets/dragon-hold/` (hoặc ảnh đất nướng sẵn); kiểm trên server tĩnh. **Ai:** Claude (làn R). **3 h.**
6. **DH-16** · P1 · G5. Tên ải ghi "Bản thử: Cầu và Suối"; câu thua dùng sai Fire Breath. **Sửa:** tên "Ải 1 · Cầu và Suối" (chờ chủ dự án chốt); câu "Gõ chữ trên đầu quái để Hỏa Long phun lửa vào chúng." **Ai:** Codex mã (phiếu 101). **0,5 h.**
7. **DH-10** · P1 · G2. Khó đọc ở camera mặc định: G01 thành khối rêu, Herb Hut như bụi cây, Spikes che Blight Wolf, Hỏa Long chỉ là nét đỏ mảnh. **Sửa:** cán cờ G01 ngả 30°, ẩn cờ trên tay khi đã cắm; Herb Hut có wash ấm và nền đá; Spikes thấp hơn sói; Rồng viền sáng hơn hoặc to 1,15 lần. Chụp trước và sau. **Ai:** Claude (làn R). **6 h.**
8. **DH-13** · P1 · G5. Không có màn tựa. **Sửa:** màn tựa trên nền cảnh map: tên game, Enter để bắt đầu, ba dòng cách chơi, về cổng game; đi được bằng phím và chuột. **Ai:** Claude (làn R). **3 h.**
9. **DH-14** · P1 · G5. Chưa có hình tựa. **Sửa:** huy hiệu màn tựa không chữ; thử chữ logo "Rồng Giữ Ải", chỉ nhận khi dấu tiếng Việt đúng hết, nếu không thì Claude đặt chữ bằng font. **Ai:** Codex ảnh (phiếu 095). **1,5 h.**
10. **DH-15** · P1 · G5. Không có màn cài đặt. **Sửa:** mục Cài đặt trong menu tạm dừng: âm lượng nhạc, hiệu ứng, giọng; chất lượng High hoặc Medium; cỡ thẻ chữ 80–150 %; về cổng game; lưu `localStorage`; đi hoàn toàn bằng phím. Gộp luôn DH-18: không cho chọn Low, và `?q=low` ở bản production dùng Medium. **Ai:** Claude (làn R). **5,5 h.**
11. **DH-17** · P1 · G4. Lần chơi đầu tải 12,4–12,7 MB. **Sửa:** nén texture GLB Rồng (KTX2 hoặc WebP) qua preset; lần đầu nạp Medium rồi mới tải High; bỏ `draconis-v3` khỏi bản build. Đo lại byte và thời gian tới khi chơi được. **Ai:** Claude (làn T). **4 h.**
12. **DH-05** · P1 · G3. Nhàn, bước 0: tự tua ×1,75 khi không có chữ (xem mục 5). **Cần chủ dự án đồng ý sửa 06 §10.** **Ai:** Claude (làn R). **5,5 h.**
13. **DH-08** · P1 · G3. Bot mất khoảng 150 máu mỗi đợt, người thật gần như không mất. **Sửa:** bot chọn từ gần nhất và có độ trễ khi chữ vừa hiện, cho giống dữ liệu chơi thật; đo lại G1 và B4. **Làm trước DH-06**, để số đo Chữ Bẫy dựa trên bot giống người. **Ai:** Claude (làn R). **5 h.**
14. **DH-06** · P1 · G3. Nhàn, bước 1: Chữ Bẫy, đổi sim, đo trên nhánh `s7-trap-words` (mục 5). **Ai:** Claude (làn R). **16 h.**
15. **DH-07** · P1 · G3. VFX ngoài làn VFX hiện tại: ba bẫy, Herb Hut, Grove Warden, Fire Breath, Dragon Roar, Inferno, G01 cắm cờ và chết, quái xuất hiện. **Sửa:** mỗi hành động đủ 5 pha theo VFX_STANDARD §3.3, phía người ra đòn trước; tờ khung ở 1280 và 1920; dh-perf ở High. Bắt đầu sau khi chủ dự án duyệt bước 1a và 2. **Ai:** Claude (làn V). **20 h.**
16. **DH-09** · P1 · G6. B1, B7 lệch; nhàn I trên dải; B9 chưa đo. **Sửa:** chủ dự án chọn hướng D27, D31, D33 và hướng chống nhàn; chơi một ván 10 đợt B9 trên bản build. **Ai:** chủ dự án. **1,5 h.**
17. **DH-11** · P1 · G2. Chưa có điểm độc lập. **Sửa:** sau khi gộp pilot và VFX, một agent không làm làn nào chấm cảnh map và các màn chính ở 1280 và 1920 theo visual-scorecard; điểm 7,5–8,5 thì thêm người chấm thứ hai. **Ai:** Claude (giám khảo). **2 h.**

Việc đang chạy, không đếm lại: map pilot A (đất, đồng cỏ, vách, ao, mép rừng, ánh sáng) trong `.wt-dh-mappilot`; làn VFX trong `.wt-dh-vfx` (bước 1a đòn chữ xong chưa gộp, bước 2 Sky Fire, bước 4 đòn quái).

### 1.3. P2 (để sau)

- DH-18 Low còn khối tạm: đã gộp vào DH-15 (ẩn Low).
- DH-19 trần tam giác bench 3,09 M: Medium giảm nửa tam giác (3 h).
- DH-20 thẻ chữ nhảy trong lúc giữ chỗ (2 h, chờ D32).
- DH-21 số sát thương Thorn Ant xếp cột: gộp thành một số ×N (1,5 h).
- DH-22 âm thanh làm lại qua AUDIO_PIPELINE, chỉ khi chủ dự án nghe thấy chưa đạt (6 h).
- DH-23 kiểm deploy tự động theo DEPLOY_INDEPENDENCE §11 (2 h); phần bỏ chunk `ui-preview` đã vào phiếu 105.
- DH-24 nút "Về cổng game" ở màn kết quả: phiếu 105 (1 h).

---

## 2. Lời Gọi (map 1: w1-silverfall)

### 2.1. Cổng

| Cổng | Kết quả | Bằng chứng |
|---|---|---|
| G1 lỗi, bot, phím thật | Một phần | Phím CDP thật chơi trọn truyện ở 1280 (thắng) và 1920 (thua Đêm 5 đúng luật), 0 lỗi console, 350/350 test. Bản 3D chưa có để chạy. |
| G2 hình | Trượt | Cảnh map là khung gỡ lỗi 2D: đĩa tròn ghi chữ tắt, tháp là emoji. Tự chấm 3,5–4/10. |
| G3 cảm giác | Trượt | Tháp bắn thiếu pha R và I; mọi loài chết giống nhau. Âm chỉ là tiếng tổng hợp. Thẻ chữ đạt (0 chồng, ≥ 18 px). |
| G4 hiệu năng | Một phần | Bản 2D nhẹ (draw p95 dưới 1 ms, gói "/" 84,91 kB). Bản 3D chưa đo. |
| G5 trải nghiệm | Một phần | Màn đầu, Cài đặt, tạm dừng, thẻ kết tốt. Người mới không có chữ nào trong 106 s đầu. HUD chiếm 14–16 % ở 1280 (trần 10 %). |
| G6 cân bằng | Một phần | B1–B8 đạt trên seed 1–80. §12 trên 20 seed trượt 5a (8,48 s) và 5b (29,5 %). Chưa có B9. |
| G7 build tự đứng | Trượt | Từ vựng đọc từ repo cha qua nginx; origin cha ghi cứng; dist mang 19,8 MB GLB không dùng; nginx chưa có host td. |

### 2.2. Việc P0 và P1 (theo thứ tự nên làm)

Bước 1C (map 1 lên 3D) là phần lớn. Thứ tự: C0 → C1 → C2 → (C3, C4, C5 song song) → C6, C7, C8 → C9 → C10 → C11 → C12 → C13 → C14.

1. **A10** · P0 · G7. typing-game.local không mở được Lời Gọi. **Sửa:** cùng lần sudo của DH-03; Claude kiểm `https://td.typing-game.local/` trả 200 và portal có thẻ Lời Gọi. **Ai:** chủ dự án. **0,5 h.**
2. **A9** · P1 · G7. Build chưa tự đủ. **Sửa:** phần từ vựng là phiếu 091 (Codex). Phần còn lại Claude làm: bỏ plugin shared trong `vite.config.ts`, `deploy.config` bỏ `models` và `.vite` tới khi 1C nạp model, `VITE_PORTAL_ORIGINS`. Kiểm `deploy:standalone`, golden giữ nguyên. **Ai:** Codex mã + Claude (làn T). **4 h.**
3. **C0** · P0 · G2. Bước 1C chưa có kế hoạch và ngân sách. **Sửa:** viết `docs/td/BUILD_1C_MAP1.md`: chỉ map 1; 2D làm bậc Low và đường lùi; chunk 3D nạp lười để gói "/" ≤ 85 kB; trần dòng mới (+~6.000); ngân sách media (High ~12 MB, Medium ~6 MB) và lần chơi đầu nạp Medium. **Ai:** Claude (làn L); chủ dự án duyệt. **4 h.**
4. **C1** · P0 · G2. Chưa có module `three` trong kit; view buộc vào `DebugView`. **Sửa:** thêm `three` vào `kit.config.json`; tách giao diện `View`; chunk view3d nạp lười, WebGL lỗi thì lùi về 2D. **Ai:** Claude (làn L). **8 h.**
5. **C2** · P0 · G2. Chưa có sân khấu 3D và camera RTS. **Sửa:** chép từ `stage.ts`, `camera.ts` của Rồng (ghi nguồn); camera theo TK 23.6; ánh sáng theo StylePack Sách tranh; ba bậc. **Ai:** Claude (làn L). **12 h.**
6. **I1** · P0 · G2. Thiếu ô đất meadow. **Sửa:** sáu ô 1024² liền mép. **Ai:** Codex ảnh (phiếu 094). **3 h.**
7. **C4** · P0 · G2. Model map 1 chưa qua preset hay chưa vào manifest. **Sửa:** theo ghi chú của 3D_IMPORT_2026-10-28; dựng lại barracks và kiểm cao 4,5–5 m; `models:blender`, `models:index`, `media:push`. **Ai:** Claude (làn L). **10 h.**
8. **C3** · P0 · G2. Chưa có đất, đường, suối, cầu, sân Fort. **Sửa:** làm trong game theo MAP_FACTORY §8.1 và luật decor §6.4, không chờ lõi Map Factory; shader đất dùng ô đất và decal của 094, 096. **Ai:** Claude (làn L). **14 h.**
9. **C5** · P0 · G2. Thiếu rig và clip: Mộc Tinh, Draconis, dân làng. **Sửa:** Mộc Tinh đủ clip (đường găng); Draconis tạm nhập bản `draconis-v2` đã rig; `worker-base` rig bằng cách của `crowd-rig.ts`. **Ai:** Claude (làn L2). **18 h.**
10. **C6** · P0 · G2. Nhà chưa có hình 3D và trạng thái. **Sửa:** model theo loại và cấp, socket; xây, nâng cấp, bán, tê vì rễ; bóng ma đặt nhà; ô Rice Field theo trạng thái (097). **Ai:** Claude (làn L). **14 h.**
11. **C7** · P0 · G2. Quái, lính, dân, Helper, cây luật vẫn là đĩa tròn. **Sửa:** chép `crowd.ts`, `crowd-rig.ts` của Rồng; quái instanced, lóe khi trúng, chết theo loài; Ghost Flame là sprite (098); 36 cây luật. **Ai:** Claude (làn L3). **20 h.**
12. **C8** · P0 · G2. Draconis và Mộc Tinh chưa có cảnh 3D. **Sửa:** Draconis bay, đậu, Fire Feather Rain; Mộc Tinh trồi, decal báo Rễ Trồi ≥ 1,2 s (099), pha 2, rút lui; khung cận cảnh lúc ra mắt. **Ai:** Claude (làn L2). **16 h.**
13. **C9** · P0 · G2. Chưa có cây, bụi, đá, mép rừng, phông xa. **Sửa:** `scripts/td/prepare-scenery.mjs` (atlas WebP); shader billboard; mép rừng; phông 140/220/320 m; rải decor theo §6.4; ≤ 6 draw call. **Ai:** Claude (làn L3). **22 h.**
14. **C10** · P0 · G3. Thẻ chữ neo theo phép chiếu 2D. **Sửa:** neo ở `FX_top` + 0,6 m; giữ `lanes.ts`; khay mép ≤ 6; chữ bay vào nhà; mỗi phím đúng có một nhịp nhìn thấy. Cổng td-words, td-scale, td-hud-budget. **Ai:** Claude (làn L). **12 h.**
15. **C11** · P0 · G3. Đòn chính chưa đủ 5 pha. **Sửa:** Archer Tower, Cannon Tower, nỏ Fort, cầu lửa Draconis, Fire Feather Rain, lính, trống Tanuki, vòng nước River Serpent, trúng theo chất liệu, chết theo loài, bộ đòn Mộc Tinh; có cài đặt giảm chuyển động; tờ khung cho mỗi đòn. **Ai:** Claude (làn L4). **24 h.**
16. **C12** · P1 · G5. Không có đồ bay về HUD; HUD dùng chữ và emoji, vượt ngân sách ở 1280. **Sửa:** đồng, Rice, Wood, Mảnh Chữ bay về ô; Chest khi boss rút; skin HUD theo TK 23.5 với chân dung và icon thật; HUD ≤ 10 % ở 1280. **Ai:** Claude (làn L4). **14 h.**
17. **C13** · P1 · G4. Hiệu năng và tốc độ nạp của bản 3D chưa đo. **Sửa:** td-1b-perf trên 3D ở High và Medium; giữ trần draw call, tam giác, hạt; không khung nào quá 50 ms; gói deploy chỉ chứa model map 1. **Ai:** Claude (làn L). **10 h.**
18. **C14** · P1 · G1. Chạy lại mọi cổng trên bản 3D. **Sửa:** mọi td-* ở hai cỡ, map1-play, map1-newplayer; giám khảo độc lập ≥ 8/10 ở 3 góc nghiêng × 4 hướng; golden không đổi. **Ai:** Claude (làn L). **12 h.**
19. **A1** · P1 · G5. Người mới không có chữ trong 106 s đầu. **Sửa:** câu Ngày 1 thành một việc đầu có hướng dẫn ("Bấm Xây (Insert), đặt Rice Field cạnh Fort", mũi tên trên nút Xây), hoặc vòng Draconis lúc đầu chạm cụm cây gần Fort. Kiểm: từ đầu tiên ≤ 10 s. **Ai:** Claude (làn L3). **5 h.**
20. **A2** · P1 · G3. 62–84 % số mẫu 1 s không có từ trên màn. **Sửa:** chủ dự án chọn hướng (mục 4.4, câu 6). **Ai:** chủ dự án. **1 h.**
21. **A3** · P1 · G6. §12 trên 20 seed trượt 5a, 5b; thiếu B9; Đêm 1 trên trình duyệt mất 6–7/20 mạng. **Sửa:** đo 5a, 5b và mạng mất ở Đêm 1 trên 20 và 80 seed, cả bộ 81–160; gói `a2-package-v2.patch` là điểm bắt đầu; chủ dự án chơi B9. **Ai:** Claude (làn L2). **8 h.**
22. **A11** · P1 · G1. `cdp-run.mjs` chọn cổng ngẫu nhiên, ba làn chạy song song có thể trùng cổng (đã làm hỏng một lượt đo). **Sửa:** `--remote-debugging-port=0` rồi đọc `DevToolsActivePort`; cho phép `CDP_PORT`. **Ai:** Codex mã (phiếu 102); Claude sync vào các game và chạy 3 × 20 lượt song song. **1,5 h.**
23. **A13** · P1 · G3. Chưa có file âm thật. **Sửa:** một lượt Audio Lab (Stable Audio 3) theo THEME_SOUND_LIST: bắn, trúng, gọi, boss, UI, nhạc map 1, âm nền ngày và đêm; OGG ở `public/assets/typing-defense/audio`; chủ dự án nghe duyệt. **Ai:** Claude (làn L2). **12 h.**
24. **I2** · P1 · G2. Thiếu hai tờ decal mặt đất. **Ai:** Codex ảnh (phiếu 096). **2 h.**
25. **I3** · P1 · G2. Ô Rice Field chưa có ảnh theo trạng thái. **Ai:** Codex ảnh (phiếu 097). **1,5 h.**
26. **I4** · P1 · G3. Tờ khung Ghost Flame chỉ có prompt. **Ai:** Codex ảnh (phiếu 098). **1 h.**
27. **I5** · P1 · G3. Phiếu 043 đã xong; còn decal nứt rễ của Mộc Tinh và dải bọt thác. **Ai:** Codex ảnh (phiếu 099). **1 h.**

Không cần dựng thêm model Tripo cho map 1: ba mốc và các bộ cấp đã có GLB từ đợt 2.

### 2.3. P2 (để sau)

- A4 Esc phải bấm hai lần khi đang khóa từ: thêm gợi ý "Esc lần nữa: tạm dừng" (1 h).
- A6 thẻ kết ghi "Knowledge 0" ngoài chế độ Học: phiếu 103 (0,5 h).
- A7 nhãn kho cây "998/1000" chồng nhau: không sửa ở 2D; C10 thay bằng tooltip 3D.
- A8 dải nghĩa đè thẻ kế: phiếu 103 (1 h).
- I6 khung HUD 9-slice: chỉ làm khi giám khảo chấm HUD dưới 8 sau C12 (1,5 h).
- C15 phần 1C sau map 1: Credit Crystal sang kit, impostor, cảnh v3–v4, StylePack Neon, rig Draconis P18 (16 h).

---

## 3. Tuyến Cuối (map 1: c1-s1 "Ca trực đầu")

### 3.1. Cổng

| Cổng | Kết quả | Bằng chứng |
|---|---|---|
| G1 lỗi, bot, phím thật | Một phần | Người mới thắng ải 1 ở 1280 và 1920 bằng phím CDP thật, 0 lỗi console, 142/142 test. Còn khung 3D đen 267 ms sau khi nạp Rail Gun. |
| G2 hình | Trượt | Tự chấm 6,5–7,5. Sân "Vành Chân Trời" trống. Vệt động cơ chữ V ở màn chính. Thẻ súng chỉ có chữ. |
| G3 cảm giác | Trượt | Pulse Gun và Heat Beam thiếu pha; lóe mất khung đầu (035 chưa gộp). Âm chưa ai nghe. Thẻ chữ đạt (42 px, tương phản 7,8:1). |
| G4 hiệu năng | Một phần | High p95 1,9 ms, 0 khung trên 50 ms. Lần đầu tải 9,06 MB (ngân sách 4 MB). Medium chưa đo nhịp khung. |
| G5 trải nghiệm | Một phần | Mọi màn đi bằng phím; tạm dừng và cài đặt đúng. Lần đầu không có hướng dẫn; vài nhãn lệch. |
| G6 cân bằng | Trượt | B1 trượt (thắng 92–96 % ở Cân bằng), B6, B7 trượt; Thử thách đảo thứ bậc; chưa có B9. |
| G7 build tự đứng | Trượt | Lúc chạy đọc model của Space (manifest + 10 GLB) và từ vựng của repo cha. nginx chưa có host survival. |

### 3.2. Việc P0 và P1 (theo thứ tự nên làm)

1. **TS-M1-01** · P0 · G7. Lúc chạy đọc model của Space. **Sửa:** không chờ AL-19; `pnpm models:prepare --import` 12 id bậc High và Medium vào `public/assets/typing-survival/models` với manifest riêng; sửa `src/view/models.ts:9`; bỏ `modelsDir` và alias; `media:push`; sửa AL-23 từ 7 thành 12 id. Kiểm: 0 request `/assets/space-typing/`, golden `s0-trace` giữ. **Ai:** Claude (làn T). **3 h.**
2. **TS-M1-02** · P0 · G7. Từ vựng chỉ có qua alias. **Sửa:** phiếu 090 (bản ghim, hash bộ bài `7f073fa2`). **Ai:** Codex mã, Claude duyệt. **2 h.**
3. **TS-M1-03** · P0 · G7. typing-game.local chưa chạy Tuyến Cuối. **Sửa:** Claude build portal và game; chủ dự án chạy cùng lần sudo; Claude mở `https://survival.typing-game.local` kiểm 0 lỗi, 0 request chéo. **Ai:** chủ dự án. **0,5 h.**
4. **TS-M1-04** · P1 · G3. Lóe cũ và đèn súng mất khung đầu. **Sửa:** duyệt và gộp 035 vào `main`, giữ đời quả cầu lửa và hai dòng `gl_FragDepth` của bản sửa khói; chạy lại f5, f6b, f8 ở hai cỡ. **Ai:** Claude (làn V). **2 h.**
5. **TS-M1-06** · P1 · G2. Vệt động cơ chữ V ở màn chính. **Sửa:** hướng vệt theo trục tàu trong camera màn chính, hoặc chỉ giữ quầng sáng ở màn chính. **Ai:** Claude (làn T). **0,5 h.**
6. **TS-M1-13** · P1 · G1. Khung 3D đen 267 ms sau khi nạp Rail Gun (4/4 lần). **Sửa:** tái hiện bằng `survival-feel-ship kick-ray`; đo GL error, uniform, NaN; sửa ở view; 0 khung đen trên 10 lần ở hai cỡ. **Ai:** Claude (làn T). **3 h.**
7. **TS-M1-14** · P1 · G4. Lần đầu tải 9,06 MB; Medium vẫn nạp GLB High. **Sửa:** truyền bậc vào `loadMesh` (`crowd.ts:180`, `ship.ts:111`); manifest riêng nhỏ; nạp sau 4 đạn chưa dùng ở ải 1. **Ai:** Claude (làn T). **2 h.**
8. **TS-M1-11** · P1 · G5. Lần đầu không có hướng dẫn. **Sửa:** chọn sẵn Pulse Gun + Heat Beam kèm nhãn "Khuyên dùng"; nút "BẮT ĐẦU" kèm chú thích; gợi ý "Gõ từ trên bến để nạp súng" trong trận đầu, tắt sau 2 lần nạp. **Ai:** Claude (làn T). **3 h.**
9. **TS-M1-12** · P1 · G6. Ải 1 quá dễ; B1, B6, B7 trượt; Thử thách đảo thứ bậc. **Sửa:** chỉnh theo N13; luật §5.1 cho bến đầy; thêm áp lực đều ở ải 1; hạ k của Thử thách; 100 seed trên cả hai bộ. **Ai:** Claude (làn T). **6 h.**
10. **TS-M1-05** · P1 · G3. Cặp súng đầu thiếu pha. **Sửa:** Pulse Gun gồng theo tiến độ gõ, dư âm vết cháy; Heat Beam lóe mồi 50 ms, giữ màu cam ở lõi; tàu bị đánh có khói và tia lửa. Tờ khung §5.6, giám khảo ≥ 8. **Ai:** Claude (làn V). **8 h.**
11. **TS-M1-07** · P1 · G2. Sân chưa được thiết kế. **Sửa:** phiếu 088 (ảnh hai bên, nền xa, decal sàn). **Ai:** Codex ảnh. **4 h.**
12. **TS-M1-09** · P1 · G2. Thẻ súng chỉ có chữ; bảng tin không có hình quái. **Sửa:** 5 icon súng đã có trong `art-src/ui/icons`; chân dung quái là phiếu 089. **Ai:** Codex ảnh. **3 h.**
13. **TS-M1-08** · P1 · G2. Dựng ảnh 088 thành nền nhiều lớp, decal, ánh sáng trong `scene.ts`; giữ độ sáng dưới dòng từ trong +0,02; draw call ≤ 60. **Ai:** Claude (làn T). **6 h.**
14. **TS-M1-10** · P1 · G2. Gắn icon súng và chân dung quái vào thẻ súng, đầu bến, bảng tin; chữ ≥ 26 px, không tràn. **Ai:** Claude (làn T). **2 h.**
15. **TS-M1-15** · P1 · G2. Chưa có điểm độc lập. **Sửa:** sau mục 5–14, một agent không làm làn nào chấm màn chính, Hành trình, bảng tin, nạp súng, thẻ ải, trận, kết thúc ở hai cỡ; đạt khi mọi màn ≥ 8. **Ai:** Claude (giám khảo). **1,5 h.**

Kéo lên từ P2 vì cổng cần: **TS-M1-17** (nhịp khung ở Medium, 0,5 h, chạy trong lượt kiểm cổng cuối, G4 đòi cả Medium) và **TS-M1-22** (chủ dự án nghe 2 phút, G3).

### 3.3. P2 (để sau)

- TS-M1-16 Scatter Gun, Rail Gun, Star Mortar thiếu pha: lô VFX thứ hai (6 h).
- TS-M1-18 nhãn nhỏ: phiếu 104 làm phần không cần quyết (bến 3 chỉ hiện khóa, Esc ở thẻ ải, câu Luật học ngắn); tên ải 2 và kiểu chữ hoa của biển chờ chủ dự án.
- TS-M1-19 khoảnh khắc thắng: bầy tan, súng im, nhạc `end.win` (2 h).
- TS-M1-20 `window.__survival` ở production: phiếu 092.
- TS-M1-21 khoảng mắt 223–226 px (đích 210): đo lại sau TS-M1-04, 05 (2 h).
- TS-M1-23 mã vượt trần dòng 12.787/12.500; chunk BufferGeometryUtils 547 kB (3 h).

---

## 4. Thứ tự làm chung cho ba game

### 4.1. Nguyên tắc

- **Đường găng là Lời Gọi.** Làn 1C bắt đầu ngay ngày 29/10, không chờ hai game kia.
- **G7 làm một lần cho cả ba game**, trong một làn riêng (làn T). Chủ dự án chỉ chạy sudo một lần.
- **Tối đa 4 workflow Claude cùng lúc.** Làn xong game này thì chuyển sang Lời Gọi.
- **Mỗi làn một lượt test, tối đa 3 người kiểm cùng lúc;** chỉ một lượt đo hiệu năng (`--perf`) chạy tại một thời điểm. Người chấm thứ hai chỉ khi điểm 7,5–8,5.
- **Codex: ảnh trước, mã sau,** không chạy phiếu ảnh và phiếu mã cùng lúc (luật hạn mức 27/10). Claude duyệt mọi đầu ra trước khi commit.
- **Mỗi làn dùng cổng cố định** cho dev server và DevTools tới khi phiếu 102 vào kit (Rồng 4140–4149, Lời Gọi 4150–4159, Tuyến Cuối 4180–4189).
- **Không media trong Git.** Ảnh, âm, GLB đi qua `media:push`. Mỗi lần cập nhật có changelog trong `docs/changelog/` của game.
- **Thứ tự gộp vào `main` của Rồng:** map pilot → VFX → `dh-codex`. Tránh ba nhánh cùng sửa view một lúc.

### 4.2. Bốn làn Claude

| Làn | Bắt đầu | Làm gì | Rồi chuyển sang |
|---|---|---|---|
| **T** (mới) | 29/10 | G7 của cả ba game, Tuyến Cuối, DH-17 | 03/11 → **L2** (Lời Gọi C5, C8, A13, A3) |
| **V** (gộp `.wt-dh-vfx` và `.wt-ts-vfx` thành một) | 29/10 | VFX Tuyến Cuối (TS-M1-04, 05), VFX Rồng (bước 2, 4, DH-07) | 05/11 → **L4** (Lời Gọi C12, C11) |
| **R** (tiếp làn map pilot) | 29/10 | Map pilot A, rồi mọi việc P1 còn lại của Rồng | 06/11 → **L3** (Lời Gọi C7, C9, A1) |
| **L** (thay làn `.wt-td-vfx`) | 29/10 | Lời Gọi 1C: C0 → C1 → C2 → C4 → C3 → C6 → C10 → C13 → C14 | — |

### 4.3. Lịch theo ngày

| Ngày | Làn T | Làn V | Làn R | Làn L |
|---|---|---|---|---|
| **29/10** (Năm) | TS-M1-01; DH-02; duyệt 090, 092; `pnpm build:local` rồi báo chủ dự án chạy sudo | TS-M1-04 (gộp 035); xong Sky Fire bước 2 | Xong map pilot A; DH-12 | Gộp 036, dừng V4a; C0 gửi duyệt; C1 |
| **30/10** (Sáu) | Duyệt 091, 100; bỏ alias nginx; kiểm qua typing-game.local (DH-04, A10, TS-M1-03); phần còn lại của A9; TS-M1-06 | TS-M1-05 | Gộp pilot vào `main`; DH-10 | C1, C2 |
| **31/10** (Bảy) | TS-M1-13; TS-M1-14; DH-17 | Rồng bước 4 (đòn quái) | DH-13 (dùng 095); DH-15 | C2 |
| **01/11** (CN) | TS-M1-11; TS-M1-12 (cân bằng) | Gộp `dh-vfx` vào `main`; DH-07 | DH-05 (bước 0, nếu được đồng ý) | C4 |
| **02/11** (Hai) | TS-M1-08, 10 (ảnh 088, 089); TS-M1-15 giám khảo; **kiểm cổng cuối Tuyến Cuối** | DH-07 | DH-08 (bot giống người) | C3 |
| **03/11** (Ba) | Sửa theo giám khảo; chủ dự án chơi B9 → **L2**: C5 Mộc Tinh | DH-07 | DH-06 Chữ Bẫy (nhánh) | C3 |
| **04/11** (Tư) | C5 | DH-07: tờ khung, dh-perf High | DH-06: đo cân bằng 2 × 60 + 300 seed | C6 |
| **05/11** (Năm) | C8 | → **L4**: C12 | DH-11 giám khảo; **kiểm cổng cuối Rồng**; chủ dự án chơi B9 | C6 |
| **06/11** (Sáu) | C8 | C12 | Sửa theo giám khảo → **L3**: C7 | C10 |
| **07–08/11** | A13 âm | C11 | C7, C9 | C10 |
| **09–10/11** | A3 cân bằng | C11 | C9, A1 | C13 |
| **11/11** (Tư) | Sửa | Sửa theo tờ khung | Sửa | **C14 kiểm cổng cuối Lời Gọi** |
| **12/11** (Năm) | Chủ dự án nghe, chơi B9 Lời Gọi; sửa nhỏ | | | |

Mốc kiểm giữa chừng của Lời Gọi: **06/11** một giám khảo độc lập chấm sân khấu, đất và nhà (sau C3, C6). Nếu hướng hình chưa ổn thì sửa sớm, không đợi tới C14.

### 4.4. Việc của chủ dự án

1. **29/10 sáng, trả lời một tin (khoảng 15 phút).** Mỗi câu có đề xuất sẵn. Quá 24 giờ chưa trả lời thì Claude làm theo đề xuất trên nhánh riêng và chưa gộp.
   1. Rồng: cho tự tua ×1,75 khi không có chữ (sửa 06 §10)? **Đề xuất: có.**
   2. Rồng: đo Chữ Bẫy trên nhánh riêng, chỉ gộp khi qua đủ cổng? **Đề xuất: có.**
   3. Rồng: hướng D27, D31, D33 (owner-decisions §8.7)? **Đề xuất: chưa đổi núm nào** (mọi núm đã đo đều đẩy G1 quá 90 %); đánh giá lại B1, B7 sau Chữ Bẫy.
   4. Rồng: tên ải 1 là "Ải 1 · Cầu và Suối"? **Đề xuất: có.**
   5. Lời Gọi: duyệt C0 (trần dòng +~6.000, chunk 3D nạp lười, media High ~12 MB và Medium ~6 MB, lần đầu nạp Medium)? **Đề xuất: có.**
   6. Lời Gọi, nhàn (A2): **đề xuất** chấp nhận khoảng chờ ban ngày và lấp bằng hành động đáng xem của 1C (VFX, đồ bay, dân làm việc). Đo lại sau 1C; nếu vẫn quá 50 % mẫu không có chữ thì áp cách tự tua của Rồng.
   7. Tuyến Cuối: tên ải 2 và kiểu chữ biển (HANDOFF §5). **Đề xuất:** "ẢI 2 · SĂN PACK LEADER" và viết hoa cả biển: "SWARM RÚT LUI!".
2. **29/10 tối, chạy sudo một lần (0,5 h)** khi Claude báo `pnpm build:local` xong: `sudo bash scripts/setup-nginx.sh play`, thêm dòng hosts cho `dragon.`, `td.`, `survival.typing-game.local`. Xong việc này là DH-03, A10, TS-M1-03.
3. **29–30/10, duyệt VFX Rồng bước 1a và 2 (15 phút)** trên tờ khung.
4. **02–03/11, Tuyến Cuối (30 phút):** nghe 2 phút ải 1 (súng, phím, nhạc, UI); chơi một ván qua `https://typing-game.local`, bấm "Chép số chơi thử" (B9).
5. **05–06/11, Rồng (45 phút):** nghe 2 phút; chơi một ván 10 đợt (B9).
6. **11–12/11, Lời Gọi (30 phút):** nghe âm mới (A13); chơi trọn truyện map 1 (B9).

Tổng khoảng 3 giờ. Không cần dựng thêm model Tripo cho map 1 của game nào.

### 4.5. Codex

- **Đang có trong hàng:** M1 = 088, 089 (ảnh Tuyến Cuối). M2 = 093 (sửa ảnh bằng công cụ), 090, 092, 091 (mã nhỏ).
- **Lô 1 mới (`CODEX_BATCH.md`):**
  - ảnh, nối vào cuối M1: 094 ô đất Lời Gọi (P0), 095 huy hiệu màn tựa Rồng, 096 decal đất, 097 ô Rice Field, 098 tờ khung Ghost Flame, 099 decal nứt rễ và dải bọt thác;
  - mã nhỏ, nối vào cuối M2: 100 từ vựng ghim Rồng (P0), 101 hai câu chữ Rồng, 102 cổng DevTools trong kit, 103 thẻ kết và dải nghĩa Lời Gọi, 104 ba nhãn nhỏ Tuyến Cuối, 105 nút "Về cổng game" và bỏ `ui-preview` ở Rồng.
- **Dự phòng:** nếu tới trưa 30/10 lane M2 chưa tới phiếu 100 (hạn mức Codex hay "model at capacity"), làn T tự làm DH-01 theo mẫu 090.
- **Lô 2 (khi cần):** I6 khung HUD Lời Gọi nếu HUD dưới 8; script kiểm deploy chung (DH-23, DEPLOY_INDEPENDENCE §11); `VITE_PORTAL_ORIGINS` cho cả ba game (bước A của §9).

### 4.6. Lượt kiểm cổng cuối (mỗi game một lần)

Một agent kiểm mới, không làm làn của game đó, chạy trên bản build qua `https://typing-game.local`:

- **G1:** bot và phím CDP thật chơi trọn map 1 ở 1280×720 và 1920×1080; 0 lỗi console, 0 exception, 0 request hỏng.
- **G2:** giám khảo độc lập chấm cảnh map và các màn chính ≥ 8; quét không còn hình tạm (kể cả `?q=low`).
- **G3:** tờ khung 5 pha cho các đòn chính; thẻ chữ (dh-words, td-words, f8); đếm nguồn âm; chủ dự án nghe.
- **G4:** perf ở High và Medium trong khe `--perf`; byte lần chơi đầu so với ngân sách HOSTING_PLAN §7.
- **G5:** đi hết lối người mới, menu, tạm dừng, cài đặt, kết quả bằng phím; quét câu chữ theo NAMES_EN.
- **G6:** cổng bot của game trên cả hai bộ seed; B9 của chủ dự án.
- **G7:** bản build trên server tĩnh không alias, không fallback SPA; 0 request sang nguồn khác; từ vựng nạp từ bản ghim.

---

## 5. Rồng: đề xuất chống nhàn và cách đo

### 5.1. Số đo hôm nay (35 WPM, 1280, phím thật, tốc độ 1)

- 52,4 % thời gian đợt không có chữ nào trên màn. 43,6 % có đúng 1 chữ, 3,9 % có 2 chữ, 0,1 % có 3 chữ.
- Quãng không chữ: trung vị 1,5 s, p90 4,2 s, dài nhất 5,9 s. Theo đợt 39–70 %; đợt 1 nhàn nhất (69,6 %).
- Lúc đông nhất có 9–10 quái sống mà chỉ 0–1 chữ (sheet-08). Tua nhanh bị từ chối ở cả 10 đợt.
- Người chơi không thấy nguy: máu không tụt quá 33 dưới mức đầu đợt, kết thúc 100 %.

### 5.2. Vì sao

- Vùng Chữ là vòng 26 m cộng T_a. Bẫy và Grove Warden hạ quái ở 26–35 m, ngoài Vùng Chữ, nên quái chết trước khi có chữ.
- Mọi núm cho chữ hiện sớm hơn (D27 (i), D30, D31) đều làm Chuẩn thắng quá 90 %, vì chữ chính là sát thương.
- Vậy phải thêm việc gõ mà không cộng thêm sát thương, hoặc lấy sát thương từ chỗ khác bù lại.

### 5.3. Ba bước, bước sau chỉ làm khi bước trước chưa đủ

**Bước 0 (DH-05), không đổi sim.**
- Khi không còn chữ sống và theo sim chưa quái nào vào Vùng Chữ trong 1,5 s tới (cùng phép tính với `inWordZone`), thời gian tự chạy ×1,75 và hiện dấu ». Chữ đầu tiên hiện thì về ×1 ngay.
- Golden và mọi cổng bot giữ nguyên, vì bot đo theo tick.
- Ước tính thời gian thật không có chữ còn khoảng 39 % ở 35 WPM và khoảng 50 % ở 70 WPM. Chưa đủ, nhưng rẻ và an toàn.
- Cần chủ dự án đồng ý sửa luật tua 06 §10.

**Bước 1 (DH-06), đổi sim, nhánh `s7-trap-words`: Chữ Bẫy.**
- Khi quái vào vùng kích của Pine Bomb hay Net Launcher (bẫy đứng ngoài 26 m), bẫy hiện một từ 3–4 chữ cái lấy từ bộ ôn.
- Gõ đúng: bẫy nổ ngay, sức như hôm nay. Gõ Ẩu: 70 %. Không gõ: bẫy tự nổ theo luật cũ nhưng chỉ 70 % sức.
- Chữ Bẫy tính vào sổ chữ cái và N_max, và không hiện khi đã có từ 4 chữ quái sống.
- Vì sao giữ được cổng: bot Chuẩn rảnh tay khoảng 20 % nên sẽ gõ chữ bẫy, sát thương như cũ, G1 và G8 gần như giữ. Không gõ thì bẫy yếu đi, G6 càng chắc. Gõ Ẩu bị phạt, B4 có lợi. Đỉnh tải G9 không tăng nhờ luật N_max.
- Lợi thêm: người chơi ôn từ trong lúc chờ.

**Bước 2 (chỉ khi còn nhàn): Than Lửa.**
- Có 1,5 s không chữ thì hiện một từ ở bệ; gõ nó rút 3 s hồi chiêu Sky Fire.
- Đồng thời tăng hồi chiêu gốc từ 24 lên 30 s, để bot Chuẩn ra chiêu với nhịp như cũ.

**Không làm:** mini-game gõ giữa hai đợt. Nhàn I chỉ tính lúc đang có đợt, và Thẻ Ôn lúc nghỉ đã có.

**Thứ tự đã đổi so với bản kiểm kê:** làm DH-08 (bot giống người) trước DH-06. Hôm nay bot mất khoảng 150 máu mỗi đợt vì Héo lan, còn người thật gần như không mất. Đo Chữ Bẫy trên bot lệch như vậy sẽ cho kết luận sai.

### 5.4. Cách đo (chỉ giữ bước nào qua đủ cổng)

**Bot (`pnpm dh:balance`, ba chế độ, 2 × 60 seed; thêm 300 seed để chấm B4 và trần 90 % của Nhanh):**

| Chỉ số | Ngưỡng giữ |
|---|---|
| G1 | 75–90 % ở cả hai bộ seed |
| G3 | ≥ 70 % |
| G5 | ≤ 40 % |
| G6 | thua hết trước đợt 3 |
| G8 | 20–35 % |
| G9 | ≤ 1,40, chữ sống ≤ N_max |
| D23a | ≤ 15 % |
| B2–B8 | đạt ở từng bộ seed |
| **Đích:** nhàn I ở Cân bằng | ≤ 20 % cho b35, Khá, Nhanh, b60 (hôm nay 20,8 / 26,6 / 30,7 / 29,5 %) |

Chỉ số mới: số Chữ Bẫy hiện và số được gõ; phần lần bẫy nổ do người chơi gõ.

**Trình duyệt (phím CDP thật, tốc độ 1, `tmp/map1-audit/scen/feel.mjs`, mẫu mỗi 100 ms):**
- Chạy 35 WPM ở 1920 và 70 WPM ở 1280.
- Đích: không chữ ≤ 20 % ở 35 WPM và ≤ 30 % ở 70 WPM; quãng không chữ p90 ≤ 4 s.
- dh-words và dh-crowd vẫn đạt.
- Máu thấp nhất mỗi đợt cho thấy có nguy (ít nhất một đợt tụt dưới 70 %).

**Cuối cùng:** chủ dự án chơi B9 một ván 10 đợt trên bản build.

**Nếu Chữ Bẫy trượt cổng:** giữ bước 0, ghi nhàn còn lại vào giới hạn đã biết của map 1, và không lùi ngày quá 06/11.

---

## 6. Rủi ro

1. **Bước 1C của Lời Gọi lớn (khoảng 210 giờ).** Cảnh 3D có thể cần thêm một vòng chấm để đạt 8. Rig Mộc Tinh (C5) là đường găng của boss. Giảm rủi ro: C4, C5 làm sớm; giám khảo chấm giữa chừng ngày 06/11. Trễ nhất 16/11.
2. **Hạn mức Codex thấp** (cửa sổ 5 giờ, đã gặp "model at capacity" ở 065, 067). Ảnh có thể trễ một ngày. Dự phòng: C3 bắt đầu bằng màu phẳng; TS-M1-08 dời sau; làn T tự làm DH-01.
3. **Hàng GPU của Mac mini dùng chung.** Một lượt dh-perf từng giữ cả 3 suất hơn 28 phút. Luật: một lượt `--perf` tại một thời điểm, mỗi làn một lượt test, tối đa 3 người kiểm.
4. **Trùng cổng DevTools** làm hỏng bằng chứng mà không báo (A11). Tới khi 102 vào kit, mỗi làn dùng cổng cố định.
5. **Xung đột khi gộp.** Rồng có ba nhánh cùng sửa (pilot, VFX, `dh-codex`); Tuyến Cuối có 035 đụng bản sửa khói ở `shots.ts`, `fx.ts`; Lời Gọi có `td-vfx` đụng BUILD_NOTES. Gộp theo thứ tự đã định ở 4.1.
6. **Chờ quyết định.** 06 §10, Chữ Bẫy, C0 là việc đổi luật hay ngân sách, cần chủ dự án. Quá 24 giờ thì làm trên nhánh riêng, chưa gộp.
7. **Chữ Bẫy làm lệch cân bằng.** Chỉ gộp khi qua đủ bảng ở 5.4; nếu không, giữ bước 0.
8. **Nén texture có thể làm xấu hình** (DH-17, TS-M1-14). Chụp trước và sau ở camera chơi; giám khảo chấm lại.
9. **Âm chưa ai nghe.** Mọi game chạy headless. Nếu chủ dự án nghe thấy chưa đạt, mỗi game thêm 6–12 giờ Audio Lab.
10. **G7 phụ thuộc lần sudo của chủ dự án.** Các cổng khác vẫn làm song song được; chỉ phần kiểm qua typing-game.local phải chờ.
11. **Lời Gọi sát trần:** gói "/" còn 0,09 kB, mã 10.499/10.500 dòng. Mọi phiếu nhỏ trước C0 phải giữ trần; 1C cần trần mới (câu 5).
12. **Giám khảo độc lập:** phải là agent không làm làn nào của game đó. Cả ba bản kiểm kê hôm nay đều là điểm tự chấm, nên G2 có thể tụt thêm khi chấm thật.
