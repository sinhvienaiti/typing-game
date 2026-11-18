# Lửa phím 1 có mặt nạ vào lab (rồi vào bản chơi)

**Mục tiêu:** đòn lửa phím 1 dùng clip Firefly lượt 2 với mặt nạ A/B (hiện từ gốc, giữ đỉnh, cháy rụi dần, than đỏ), thay hoa sen cũ.
**Cách đã chốt:**
- 273/273b: atlas RGBA, maskA (thứ tự sống sót theo hạng), maskB.
- 274/274b: `rampCool` giữ than ở dải son.
- 264: nối vào `element-fire.ts impact()`, sau cờ `?impact=brush|lotus` (mặc định brush).

(DECISIONS: 04/11 ~14:50, 19:40, ~22:00)
**Nghiệm thu:** khung đầu ≥ 95 % đỉnh; trắng xóa ≤ 6 %; thân sáng ≤ 15 % ở tuổi 18; Hỏa hơn Kim ≤ 0,85 ms; video.
**Phiếu:**
- `docs/codex-queue/273*`, `274*`, `264-tt-key1-brush-impact.md`.
- Tấm xem: `typing-game-review/captures/tu-tien/impact-k1-r2/masks/`.

## Nhật ký
- 04/11 21:13 · Codex · 273 xong (dừng một lần vì đặc tả mâu thuẫn, Claude chốt, chạy lại).
- 04/11 21:24 · Codex · 273b xong; nhịp cháy theo lịch (0,68 / 0,19 / 0,05 / 0).
- 04/11 ~22:00 · anh · duyệt.
- 04/11 23:31 · Codex · 274 xong: mã đạt, nhưng than chìm xuống muội (công thức của Claude sai).
- 04/11 23:35 · Claude · phiếu 274b (trần r về 0,40); Codex hết hạn mức tới 00:52, chạy lúc 00:54.
- 05/11 00:20 · Claude · 264 viết xong (phiếu dài, trước luật làm gọn), chạy sau 275 khi có `264/READY` (sau khi gộp 274).
- 05/11 01:03: Claude gộp 274/274b vào main game (`0f4d72c`); tạo worktree `games/.wt-ic-impact-k1` (nhánh `codex/key1-brush-impact`, mốc 979 test / 88 tệp); tạo `264/READY`. Codex chạy 264 sau 275.
- 05/11 02:15 · Claude · Codex 264 xong (02:01, 985 test đạt), Claude đã commit `ee3ee97` trên nhánh `codex/key1-brush-impact` (worktree `games/.wt-ic-impact-k1`). Lô 1 (phiếu 277) xây tiếp trên commit này. **Việc kế (agent kiểm):**
  - làm đúng mục "Claude làm sau" của `docs/codex-queue/264-tt-key1-brush-impact.md`: ghi manifest `art-src/lab/vfx/fire/impact-k1-r2/manifest.json`, chạy các cổng lab, quay video trước/sau phím 1 Hỏa ở camera chơi;
  - dev server riêng: wrapper Vite như 275, link `art-src`, cổng 3078;
  - không sửa code; lỗi thì ghi nhật ký và báo Claude;
  - video vào `typing-game-review/owner-review/2026-11-05/tu-tien/key1-fire/` kèm `ABOUT.md`.
- 05/11 02:18 · agent kiểm 264 · ba MD5 khớp bảng; đã ghi `art-src/lab/vfx/fire/impact-k1-r2/manifest.json` (nguyên văn mục 1, git bỏ qua); link `art-src` vào worktree (không commit); dev server riêng 3078 (wrapper ở scratchpad: config của worktree, `hmr: false`, `fs.allow` gốc repo, `publicDir` của game chính).
- 05/11 02:30 · agent kiểm 264 · **lỗi nhỏ kịch bản chụp (không sửa mã, báo Claude):** ở mục thứ hai của `PLAN=brush` (`k1bp`) `__lab.fireImpact().ageTicks` ra `-0` ở khung trúng (`Math.round` của số âm rất nhỏ); CDP `returnByValue` trả `undefined` cho `-0`, nên `age` mất và cả 12 khung chụp cùng khung 7. Đo bằng bản chép ở scratchpad có `+ 0` sau `ageTicks` (4 chỗ). Sửa đề nghị: `skills-main.ts` trả `Math.round(...) + 0` (hoặc kịch bản cộng `+ 0`). Console lab: không lỗi shader, không dòng `not loaded`; có 2 cảnh báo WebGL "Feedback loop formed between Framebuffer and active Texture" lúc nạp trang, có cả ở `?impact=lotus` nên không do 264.
- 05/11 02:43 · agent kiểm 264 · **Cổng lab** (1920×1080, High, DPR 1, `fixed=1`, ba nền, `k1b` + `k1bp`; số ở `typing-game-review/captures/tu-tien/impact-k1-v2/gates.json`):
  - Khung đầu chớp: **TRƯỢT** 0,76–0,91 (< 0,95). E(1) > E(0) ở cả 6 ca (cận 0,85–0,91, chơi 0,76–0,83); chớp tắt ở tuổi 3. Gợi ý: `BRUSH.flash` (`life` 0,07, `size0/size1`, `gain`) hoặc đường bao của `SpritePool`; cần phiếu chỉnh.
  - Khung đầu đèn: đạt, 4/4 = 1,00 ở tuổi 0; về sau ≤ 3,56.
  - Trắng xóa: đạt, tối đa 0,08 % (brush), 0,64 % (linger, ở `k7f`); trong vết thẻ ≤ 0,05 %.
  - Thân sáng tuổi 18 (TRIAL): đạt, 1,3–4,6 % đỉnh; chẩn đoán: diện tích OKLab 4–14 %, "Y > 0,1" 1–8 %.
  - Hỏa hơn Kim: đạt. p95 phím 1: Kim 7,2 / 9,6, Hỏa 7,9 / 8,5 (thứ tự M, F, F, M) → Hỏa − Kim ≈ −0,2 ms; mọi cửa sổ ≤ 11,1 ms; lotus 9,3. Nửa sau có tải CPU khác (cpuP95 ~2 ms), nhiễu lớn.
  - Không lớp cũ vẽ ngầm: đạt. (a) audit sau 1 lần phím 1: lotus = point = scorch = groundFire = missing = 0, brush = flash = light = 6. (b) không có `ground-decals` hay `flipbook-fire-ground` ở mọi khung brush và linger `k1h,k1hp`; `flipbook-fire-burst` 1 so với 3 (lotus), `fx-fire-points` 0–2 so với 3–4, không khung nào lớn hơn.
  - Biên dịch lần đầu: **TRƯỢT** 96 ms ở khung trúng (CPU 92 ms; lotus 38,5 ms; cả hai trượt 11,5). Theo phiếu: mở phiếu nhỏ làm ấm chương trình v2 lúc nạp.
- 05/11 02:43 · agent kiểm 264 · **Video** `typing-game-review/owner-review/2026-11-05/tu-tien/key1-fire/key1-fire-before-after.mp4` (52 s, 28,3 MB, 1920×1080 60 fps, có `ABOUT.md`) + tấm tuổi `key1-ages-lotus-vs-brush.jpg`. Trước = `?impact=lotus`, sau = brush; đá sáng rồi tối; camera chơi thật, 0,25×, cận vào đòn thật, cận 0,25×. Zoom cận của người chơi (`zoom(1)`) bỏ khỏi video vì khung đó chỉ thấy người phát chiêu, không thấy đòn trúng. Chưa gửi anh, chưa chấm mù. Đã xóa khung thô (prune `--apply`); index đã dựng lại. Dev server 3078 đã tắt; link `art-src` để lại trong worktree (không commit).
- 05/11 08:32 · Claude · Codex 278 xong (02:52): làm nốt 277 (lô 1 Hỏa bằng art) và sửa 2 cổng trượt của 264 (chớp tuổi 0, làm ấm biên dịch, `ageTicks + 0`), 995/995 test. Code chưa commit trong `games/.wt-ic-fire-lot1` (nền `ee3ee97` có 264). **Việc kế (agent kiểm):**
  - chạy lại 7 cổng lab của 264, cách đo như `typing-game-review/captures/tu-tien/impact-k1-v2/gates.json`; phải đạt chớp tuổi 0 ≥ 0,95 và khung trúng đầu ≤ 11,5 ms;
  - chạy `lab-element-parity.mjs` (ONLY theo lô 1, ELEMENT `metal` và `fire`) và `lab-element-perf.mjs` theo "Kiểm chung" của `docs/games/tu-tien/skills/CODE_DRAWN_AUDIT_2026-11-05.md` §3;
  - quay một video trước/sau ở camera chơi (`ee3ee97^` = main `0f4d72c` so với worktree): phím 1 Hỏa và các lớp lô 1 (sao, vòng tay, vòng đất, dải vạch);
  - dev server riêng: wrapper Vite, link `art-src` (không commit), cổng 3088;
  - đạt hết thì commit trong worktree đúng các tệp của 277 và 278 (đọc hai báo cáo); không gộp vào main;
  - video vào `typing-game-review/owner-review/2026-11-05/tu-tien/fire-lot1/` kèm `ABOUT.md`.
- 05/11 08:36 · agent kiểm 278 · đọc diff 277/278: đúng phạm vi; `tsc` qua, **995/995 test / 91 tệp** (chạy lại). Link `art-src` vào `.wt-ic-fire-lot1` (không commit). Ba dev server riêng (wrapper ở scratchpad `lot1/dev.mjs`, `hmr: false`): 3088 worktree, 3078 `ee3ee97` (trước cho parity), 3089 main `0f4d72c` (trước cho video). Đang chạy cổng, parity, perf, video; số vào `typing-game-review/captures/tu-tien/code-drawn/lot1/`.
- 05/11 08:52 · agent kiểm 278 · **7 cổng của 264** chạy lại trên `.wt-ic-fire-lot1` (1920×1080, High, DPR 1, `fixed=1`, ba nền, `k1b` + `k1bp`; số ở `typing-game-review/captures/tu-tien/code-drawn/lot1/gates.json`). Sửa `ageTicks + 0` có hiệu lực: kịch bản gốc chụp đúng từng tuổi.
  1. Chớp khung đầu: **ĐẠT** 1,00 ở cả 6 ca (trước 0,76–0,91); tuổi 0 sáng nhất, tắt ở tuổi 3.
  2. Đèn khung đầu: **ĐẠT** 1,00 (4/4), về sau ≤ 3,56.
  3. Trắng xóa: **ĐẠT**, tối đa 0,08 % (brush), 0,62 % (linger `k7f`); trong vết thẻ ≤ 0,05 %.
  4. Thân sáng tuổi 18: **ĐẠT** 1,3–4,6 % đỉnh.
  5. Hỏa hơn Kim (M, F, F, M): **ĐẠT**. Phím 1 p95: Kim 9,4 / 7,1, Hỏa 9,0 / 8,7 → +0,6 ms; mọi cửa sổ p95 ≤ 10,7, max ≤ 11,5. Nhiễu lớn (cpuP95 tới 2,4 ms). `fxcode=1` để so: phím 1 7,2.
  6. Không lớp cũ vẽ ngầm: **ĐẠT**. Không `ground-decals`/`flipbook-fire-ground` ở mục brush; brush không hơn lotus; ở đường mặc định không còn `fx-fire-points` hay vòng mã, thay bằng `flipbook-fire-twinkle-set`, `-halo-ring`, `-halo-seal-loop`, `flipbook-strip-fire-sheath-v2`.
  7. Biên dịch lần đầu: **TRƯỢT** 108 và 85,8 ms ở khung trúng (ngưỡng 11,5; trước 96). Prewarm 278 không đủ. **Chẩn đoán** (`stall-probe.json`, bọc hàm WebGL sau khi lab sẵn sàng): khung trúng có 9 `texSubImage2D` = **79,5 ms** (nạp texture lần đầu: `texStorage2D` + `generateMipmap`), cùng 10 `compileShader`/5 `linkProgram` mới. Khung bấm phím (tuổi −1) còn tệ hơn: 7 texture = **183 ms**, tổng 226–238 ms (trước 142). `renderer.compile(mesh)` chỉ dịch chương trình, không tải texture, và còn sót chương trình. Đề nghị phiếu nhỏ: trong `prewarm()` gọi `renderer.initTexture()` cho mọi atlas Hỏa (brush v2 + mặt nạ, sao, vòng tay, vòng đất, dải, các clip lúc phát chiêu), và dịch theo cả cảnh (`compile(scene, camera)` hay `compileAsync`) để khớp biến thể.
- 05/11 08:52 · agent kiểm 278 · **Parity ONLY `k1,k1z,k7`** (trước = `ee3ee97` cổng 3078, sau = worktree): Kim **0 điểm ảnh khác** ở cả 15 khung; Hỏa khác trong hộp quanh hiệu ứng, tối đa 2,7 % khung (`k1z-008`). `parity/parity.json`.
- 05/11 08:52 · agent kiểm 278 · **Video** `typing-game-review/owner-review/2026-11-05/tu-tien/fire-lot1/fire-lot1-before-after.mp4` (35 s, 19,9 MB, 1920×1080 60 fps, `ABOUT.md`): trước = main `0f4d72c` (cổng 3089), sau = worktree; camera chơi, phím 1 thật rồi 0,25×, phím 7 thật rồi 0,5×. Tấm so `captures/.../lot1/before-after-play.jpg`. Chưa gửi anh, chưa chấm mù. Đã xóa khung thô (prune `--apply`), index đã dựng lại; ba dev server đã tắt; link `art-src` để lại trong worktree (không commit).
- 05/11 08:52 · agent kiểm 278 · **Không commit**: cổng 7 trượt, mà việc kế ghi "đạt hết thì commit". Thay đổi 277/278 vẫn chưa commit trong `.wt-ic-fire-lot1`, chờ Claude quyết.
- 05/11 10:26 · Claude · Codex 280 (làm ấm texture, `renderer.compile` theo cả cảnh, `__lab.fireImpact().prewarmed`) và 281 (sửa 2 test cũ) xong: 1000/1000 test. **Việc kế (agent):**
  - đo lại cổng 7 trong `games/.wt-ic-fire-lot1` (cổng 3088, cách đo như 08:48): khung bấm phím và khung trúng đầu ≤ 11,5 ms; kiểm `prewarmed` là `true`;
  - chạy nhanh lại cổng 1 (chớp tuổi 0) và cổng 6 (không lớp cũ) để chắc không lùi;
  - đạt thì commit trong worktree đúng các tệp của 277, 278, 280 và 281 (đọc bốn báo cáo; không commit link `art-src`), không gộp vào main;
  - trượt thì ghi số và nguyên nhân.
- 05/11 10:40 · agent kiểm 280/281 · dev server riêng 3088 trên `.wt-ic-fire-lot1` (wrapper `lot1/dev.mjs`, `hmr: false`); đo lại cổng 7 (3 trang mới, kịch bản 08:48 thêm `prewarmed`/`textureIds`), stall probe, rồi cổng 1 và 6 ở nền mặc định; số vào `typing-game-review/captures/tu-tien/code-drawn/lot1/recheck-280/`.
- 05/11 10:34 · agent kiểm 280/281 · **Cổng 7 (biên dịch lần đầu): TRƯỢT nhưng giảm mạnh.** 3 trang mới, 1920×1080, High, DPR 1, cách đo 08:48 (`recheck-280/first-compile-{1,2,3}.json`). `prewarmed` = `true` ngay khi lab sẵn sàng (chờ 0 ms), 18 `textureIds` trước và sau đòn. Khung bấm phím: **39,8 / 32,5 / 35,2 ms** (trước 235); khung trúng đầu: **39,5 / 49,7 / 44,2 ms** (trước 108); ngưỡng 11,5. Còn vượt ở tuổi 1 (14,8–17,7) và tuổi 3 (20,8–26,3).
- 05/11 10:34 · agent kiểm 280/281 · **Nguyên nhân còn lại** (`stall-probe.json`, `stall-names.json`, bọc hàm WebGL sau khi `prewarmed`): phần lớn **không thuộc thư viện Hỏa**.
  - Tuổi 0: hai mặt nạ của qi slash chung (`src/view/skills/qi-slash.ts`, nạp ở `skills-main.ts:275`) `impact-tex/burst-star-mask.png` và `slash-crescent-mask.png`, 1024², tải lần đầu 6,7 + 6,3 ms; thêm 1 chương trình ShaderMaterial (frag ~11 kB); CPU khung trúng 24–43 ms.
  - Tuổi 1: 2 chương trình `MeshDepthMaterial` (bóng đổ; `renderer.compile` không dịch biến thể độ sâu bóng).
  - Tuổi 3: 1 ShaderMaterial + texture canvas 1024×256 (có lẽ số sát thương hay chữ gọi chiêu), 4,6 ms.
  - Khung bấm phím: không còn tải texture hay dịch shader, nhưng 18 chương trình dùng lần đầu (88 `getActiveUniform`), tổng 19–40 ms với CPU 8–14 ms. Có lẽ ANGLE/Metal chỉ tạo pipeline ở lần vẽ thật đầu tiên.
  - Đề nghị phiếu nhỏ: làm ấm cả hai mặt nạ qi slash và canvas chữ (`initTexture`); một lần vẽ thật ngoài màn (target 1×1 hay scissor) mọi mesh Hỏa và qi slash, bật bóng đổ để có biến thể độ sâu. Chưa đo Kim ở cùng cách nên chưa rõ phần chung; trước đây lotus trên main cũng trượt (38,5 ms).
- 05/11 10:34 · agent kiểm 280/281 · **Cổng 1 chớp tuổi 0: ĐẠT**, E0/max = 1,00 (`k1b`, `k1bp`, nền mặc định), số y hệt 08:52. **Cổng 6 không lớp cũ: ĐẠT**: không `ground-decals`/`flipbook-fire-ground` ở brush và linger `k1h,k1hp`; brush không hơn lotus; audit sau 1 phím 1: lotus = point = scorch = groundFire = missing = 0 (brush = flash = light = 2). Phụ: trắng xóa tối đa 0,08 % (main), 0,62 % (linger `k7f`); thân sáng tuổi 18 1,5–2,4 % đỉnh. Số ở `recheck-280/gates.json`.
- 05/11 10:34 · agent kiểm 280/281 · **Không commit** vì cổng 7 trượt: thay đổi 277/278/280/281 vẫn chưa commit trong `.wt-ic-fire-lot1`, chờ Claude quyết (commit dù cổng 7 trượt vì phần còn lại ngoài Hỏa, hay mở phiếu làm ấm qi slash, bóng và vẽ thật). Đã xóa 325 khung thô (prune `--apply`, 904 MB); `ABOUT.md` và index đã dựng lại; dev server 3088 đã tắt; link `art-src` để lại (không commit).
- 05/11 10:55 · Claude · Cổng 7 còn 33–50 ms (phần lớn là đồ dùng chung). Claude quyết commit phần Hỏa: `fe47341` (264+277+278+280+281). Phiếu 283 làm ấm phần chung, chạy sau 282.
- 05/11 10:57 · Claude · Codex 283 xong (10:56): làm ấm phần chung (mặt nạ qi slash, bóng đổ, chữ số, một lần vẽ thật ngoài màn hình, cả Kim), 1006/1006 test. Chưa commit trong `games/.wt-ic-fire-lot1`. **Việc kế:** đo lại cổng 7 cho Hỏa và Kim (agent, sau khi workflow tìm hiểu rồng xong vì luật tối đa 2 agent).
- 05/11 11:05 · Claude · **Việc kế (agent):**
  - đo lại cổng 7 sau 283 cho cả Hỏa và Kim trong `games/.wt-ic-fire-lot1` (cổng 3088, cách đo như 10:40): khung bấm phím và khung trúng đầu ≤ 11,5 ms; đọc `__lab.prewarmReport()`;
  - chạy nhanh lại cổng 1 và cổng 6;
  - đạt thì commit các tệp của 283 (đọc `docs/codex-queue/283-report.md`), không gộp;
  - trượt thì ghi số và phần còn lại.
- 05/11 11:00 · agent kiểm 283 · bắt đầu: dev server riêng 3088 trên `.wt-ic-fire-lot1` (wrapper `lot1/dev.mjs`, `hmr: false`); đo lại cổng 7 cho Hỏa và Kim (3 trang mới mỗi nguyên tố, khung trúng = khung đầu `events().impact` tăng), đọc `__lab.prewarmReport()`, rồi cổng 1 và 6; số vào `typing-game-review/captures/tu-tien/code-drawn/lot1/recheck-283/`.
- 05/11 11:14 · agent kiểm 283 · **Cổng 7 (khung bấm phím, khung trúng đầu ≤ 11,5 ms): TRƯỢT sát ngưỡng, giảm mạnh** (trước 33–50 ms). 3 trang mới mỗi nguyên tố, 1920×1080, High, DPR 1; khung trúng = khung đầu `events().impact` tăng (Hỏa trùng tuổi 0). Số ở `recheck-283/gate7.json`, `first-compile-{fire,metal}-{1,2,3}.json`.
  - Hỏa: bấm phím **13,5 / 11,4 / 13,9**; trúng **13,0 / 9,3 / 9,4**; trúng+1 10,7 / 8,1 / 8,5; khung thường ≤ 9,7.
  - Kim: bấm phím **12,2 / 11,8 / 14,9**; trúng **10,2 / 10,6 / 14,0**; trúng+1 **13,4 / 13,5 / 16,2**; khung thường 8,3–10,8 (ít dư so với 11,5).
  - `__lab.prewarmReport()`: 2 hồ sơ (fire 64 texture, metal 66), 100 vật thể (11 đổ bóng), target 64×64 cùng định dạng bloom, `renders` = 1 mỗi hồ sơ; có đủ `burst-star-mask`, `slash-crescent-mask`, atlas số; `prewarmed` = `true`.
- 05/11 11:14 · agent kiểm 283 · **Phần còn lại** (`stall-probe-*`, `stall-names-*`, `stall-ids-*.json`, bọc WebGL sau ready):
  - Khung bấm phím: không còn dịch shader hay tải texture (chỉ 1 `texSubImage2D` ~0 ms), CPU 3,5–7,6 ms, tổng cao hơn khung thường 3–5 ms; có lẽ lần vẽ thật đầu của pipeline (ANGLE/Metal) hay việc CPU lúc bắt đầu chiêu, chưa rõ.
  - Khung trúng (cả Hỏa và Kim): còn **1 chương trình ShaderMaterial** (vert 1,6 kB chỉ `vUv`, frag ~11 kB), chính là chương trình 10:34 đã thấy; 283 chưa làm ấm nó (có lẽ shader mặt nạ impact/qi slash ở `screen-fx`, cần xác nhận).
  - Kim trúng+1: **2 chương trình bóng đổ `MeshDepthMaterial`** chưa có: `USE_SKINNING + USE_MAP` và `USE_INSTANCING + USE_MAP` (biến thể bóng có map/alphaTest; lượt vẽ 64×64 của 283 chưa chạm).
  - Đề nghị phiếu nhỏ: làm ấm chương trình ShaderMaterial đó và hai biến thể độ sâu có map (skinned, instanced) cho Kim; sau đó đo lại. Khung bấm phím cần đo thêm (nhiều lượt hơn, so với main) trước khi kết luận là lỗi.
- 05/11 11:14 · agent kiểm 283 · **Cổng 1 chớp tuổi 0: ĐẠT** E0/max = 1,00 (`k1b`, `k1bp`, nền mặc định), đèn 4/4 = 1,00. **Cổng 6 không lớp cũ: ĐẠT**: không `ground-decals`/`flipbook-fire-ground` ở brush và linger `k1h,k1hp`; brush không hơn lotus; audit sau 1 phím 1: lotus = point = scorch = groundFire = missing = 0. Phụ: trắng xóa tối đa 0,08 % (main), 0,62 % (linger `k7f`); thân sáng tuổi 18 1,5–2,4 % đỉnh. Số ở `recheck-283/gates.json`.
- 05/11 11:14 · agent kiểm 283 · **Không commit** vì cổng 7 trượt (việc kế ghi "đạt thì commit"): tệp 283 vẫn chưa commit trong `.wt-ic-fire-lot1`, chờ Claude quyết (commit vì đã giảm từ 33–50 xuống 9–16 ms, hay phiếu nhỏ cho 3 chương trình còn lại). Đã xóa 325 khung thô (prune `--apply`, 904 MB); `ABOUT.md` và index đã dựng lại; dev server 3088 đã tắt; link `art-src` để lại (không commit).
- 05/11 11:22 · Claude · Cổng 7 sau 283: 11–15 ms và 9–14 ms (trước 235 và 108). Đã commit 283 (`9434ac2`). Phiếu 286 làm ấm 3 chương trình còn lại, chạy sau 285.
- 05/11 11:50 · Claude · Codex 286 xong (1014 test). Phiếu 287: commit 286, gộp main (275/279) vào nhánh lô 1, giải xung đột `element-fire.ts`. Sau đó đo cổng 7 và parity trên nhánh đã gộp rồi fast-forward main.

## 05/11 15:12 · Claude · 286 và merge main đã commit
- Codex 287 kẹt (sandbox không ghi được `.git`): Claude commit 286 (`07b73f6`), `git merge --no-ff main`; Codex 287b giải xung đột (không lệnh git); Claude kiểm (tsc qua, vitest 94/94 tệp, 1028/1028) và commit merge `672f2e7` trên `codex/fire-lot1-art`.
- **Bước kế:** đo lại cổng 7 (khung bấm phím đầu và khung trúng đầu ≤ 11,5 ms, Hỏa và Kim, 3 lần mỗi hệ), cổng 1 và 6, và parity ngoài hiệu ứng trên nhánh đã gộp. Không commit gì. Đạt thì Claude fast-forward `main` của game.
- 05/11 15:08 · agent kiểm nhánh gộp · bắt đầu: dev server riêng 3088 trên `.wt-ic-fire-lot1` (`672f2e7`) và 3089 trên main của game (`bbb46d8`, làm "trước" cho parity), wrapper `lot1/dev.mjs`, `hmr: false`; cổng 7 (3 trang mới mỗi hệ, cách đo 11:00), cổng 1 và 6 (nền mặc định), parity ONLY `k1,k1z,k7`; số vào `typing-game-review/captures/tu-tien/code-drawn/lot1/recheck-merge/`.
- 05/11 15:26 · agent kiểm nhánh gộp · **Cổng 7 (khung bấm phím, khung trúng đầu ≤ 11,5 ms) trên `672f2e7`: TRƯỢT nhẹ.** 3 trang mới mỗi hệ, 1920×1080, High, DPR 1, cách đo 11:00 (`first-compile-283.mjs`, một lượt làm ấm Vite bỏ đi trước); số ở `recheck-merge/gate7.json`. Máy bận lúc đo (load 3,2; `mediaanalysisd` 75 % CPU; khung thường trung vị 9,6–10,7, trước 8,3).
  - Hỏa: bấm phím **17,8 / 23,9 / 16,7**; trúng **14,9 / 12,1 / 14,4**; trúng+1 11,5 / 13,7 / 11,2.
  - Kim: bấm phím **16,4 / 14,2 / 15,9**; trúng **13,4 / 10,5 / 12,6**; trúng+1 17,3 / 13,4 / 14,3.
  - **Đối chứng xen kẽ main `bbb46d8` và nhánh gộp** (`recheck-merge/control/control-gate7.json`, 3 lượt mỗi bên): main Hỏa bấm phím 129–146, trúng 37–40; main Kim 53–61 / 31–35. Nhánh gộp Hỏa 11,6–15,8 / 11,2–13,7; Kim 10,1–18,8 / 8,2–10,9. Nhánh gộp nhanh hơn main 4–10 lần, không lùi.
  - **Phần còn lại** (`stall-probe-*`, `control/stall-ids-*.json`): Hỏa không còn dịch shader hay tải texture ở khung nào; khung bấm phím và khung trúng chỉ có CPU 3,5–9 ms và 28 `getActiveUniform` (dùng lần đầu chương trình đã dịch). Kim trúng+1 (khung 7) **vẫn dịch muộn 2 chương trình bóng `MeshDepthMaterial`**: `USE_MAP + USE_SKINNING` và `USE_MAP + USE_INSTANCING` (+ `DEPTH_PACKING 3201`), đúng hai chương trình 286 định làm ấm: lượt làm ấm của 286 chưa khớp khóa chương trình (báo cáo prewarm: `shadow=13`, trước 11). ShaderMaterial `ImpactPass` ở khung trúng: hết.
- 05/11 15:26 · agent kiểm nhánh gộp · **Cổng 1 chớp tuổi 0: ĐẠT** E0/max = 1,00 (`k1b`, `k1bp`, nền mặc định), đèn 4/4 = 1,00. **Cổng 6 không lớp cũ: ĐẠT**: không `ground-decals`/`flipbook-fire-ground` ở brush; brush không hơn lotus; linger lotus vẫn có hai lớp cũ (đối chứng, đúng). Phụ: trắng xóa tối đa 0,08 % (main), 0,21 % (linger); thân sáng tuổi 18 1,5–2,4 % đỉnh. Số ở `recheck-merge/gates.json`.
- 05/11 15:26 · agent kiểm nhánh gộp · **Parity ONLY `k1,k1z,k7` (trước = main `bbb46d8`, sau = `672f2e7`): ĐẠT.** Kim **0 điểm ảnh khác** ở cả 15 khung. Hỏa khác chỉ quanh hiệu ứng: > 8/255 tối đa 4,7 % khung (`k1z-008`, cận), 0,07–1,5 % ở camera chơi; **ngoài hộp hiệu ứng + 32 px** tối đa 0,16 % điểm > 2/255, chênh tối đa 8/255. `recheck-merge/parity/parity.json`.
- 05/11 15:26 · agent kiểm nhánh gộp · Không commit, không gộp. Đã xóa 385 khung thô (prune `--apply`, 1,06 GB); `ABOUT.md` và index đã dựng lại; hai dev server 3088, 3089 đã tắt. Đề nghị: cổng 7 chỉ còn trượt do máy bận và 2 biến thể bóng của Kim; Claude quyết fast-forward (nhánh gộp hơn main nhiều) hay phiếu nhỏ khớp khóa 2 chương trình bóng (so `program.cacheKey` lúc làm ấm và lúc trúng), rồi đo lại khi máy rảnh.
- 15:32 Claude: cổng 7 chưa đạt (máy bận) nhưng nhánh gộp nhanh hơn main 4–10 lần; chưa fast-forward theo kế hoạch. Phiếu 291 làm ấm đúng 2 chương trình bóng của Kim (xếp chạy sau 290), rồi đo lại khi máy rảnh.

## 05/11 16:20 · agent kiểm 291 · cổng 7 vẫn trượt, không commit
- Đo trên `.wt-ic-fire-lot1` (`672f2e7` + 291 chưa commit), dev server riêng 3088, cách đo như 15:08 (`first-compile-283.mjs`, 3 trang mới mỗi hệ, 1920×1080, High, DPR 1, một lượt làm ấm bỏ đi). Máy bận: chờ 16:03–16:07 nhưng load không xuống dưới 2 (`mediaanalysisd` ~75 %, `mds_stores` 38–134 %); load 2,1–3,5 lúc đo cổng 7. Số ở `typing-game-review/captures/tu-tien/code-drawn/lot1/recheck-291/` (`gate7.json`, `late-programs.json`, `control/late-compare.json`, `gates.json`, `load.txt`).
- **Cổng 7 (≤ 11,5 ms): TRƯỢT.** Hỏa: bấm phím **11,5 / 21,4 / 15,3**; trúng **9,9 / 13,5 / 13,4**; trúng+1 7,9 / 10,3 / 11,2. Kim: bấm phím **16,8 / 12,0 / 13,5**; trúng **11,5 / 8,7 / 12,0**; trúng+1 **9,4 / 7,9 / 10,5** (trước 291: 13,4–17,3). Khung bấm phím không dịch shader, không tải texture (1 `texSubImage2D` ~0 ms, CPU 8,4–8,6 ms); khung trúng chỉ `getActiveUniform` 23–28 lần.
- **291 đạt đúng việc của nó:** so xen kẽ bản xuất `672f2e7` và worktree có 291, Kim khung 7 trước có 2 lượt link `MeshDepthMaterial` (`USE_MAP+USE_SKINNING`, `USE_MAP+USE_INSTANCING`), sau 291 không còn.
- **Còn 1 chương trình link muộn ở khung 13 (cả Hỏa và Kim, có từ trước 291):** `ShaderMaterial` vert 2228 / frag 5965 ký tự, uniform `uAtlas`, `uScreen`, `uRowY`, varying `vUv, vColor, vTint, vY` = vật liệu số sát thương `IcNumberSprites` (`src/view/hitfx.ts:754`). Khung đó 14,8–25,6 ms. Lượt `numbers.prewarm` hiện chưa làm ấm đúng khóa của nó (có lẽ cùng chuyện số đèn điểm trong khóa như 291 tìm ra). Các lần đo trước chỉ xem tới khung 10 nên chưa thấy.
- **Cổng 1: ĐẠT** E0/max = 1,00 (`k1b`, `k1bp`), đèn 4/4 = 1,00. **Cổng 6: ĐẠT** không lớp cũ ở brush, brush không hơn lotus, linger lotus còn hai lớp cũ (đối chứng). Trắng xóa tối đa 0,08 % (main), 0,21 % (linger); thân sáng tuổi 18 1,5–2,4 % đỉnh. Giống hệt 15:26.
- Không commit (cổng 7 trượt). Tệp 291 vẫn chưa commit trong worktree. Đã xóa 325 khung thô (905 MB), dựng lại index, tắt dev server 3088 và 3089 (bản xuất `672f2e7` trong scratchpad đã xóa). Đề nghị: phiếu nhỏ làm ấm vật liệu số `IcNumberSprites` đúng khóa lúc chơi; khung bấm phím (12–21 ms, không còn dịch shader) cần đo trên máy rảnh hoặc so với main trước khi coi là lỗi.
- 16:35 Claude: commit 291 (`c15af6f`, đã đo: hết 2 chương trình bóng muộn). Còn `IcNumberSprites` link muộn ở khung 13 → phiếu 297. Máy bận (mediaanalysisd 75 % CPU) làm số khung bấm phím nhiễu; đo lại khi máy rảnh.
