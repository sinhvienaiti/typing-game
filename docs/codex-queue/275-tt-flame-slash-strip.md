# Phiếu 275 · Tu Tiên · Code: bỏ lưỡi lửa gai nhọn vẽ bằng mã ở nhát chém kết phím 7 (Hỏa), thay bằng dải lửa Firefly anh đã chọn

**Loại việc:** code shader (`gpt-6.1-sol`, mức `xhigh`). Lời giải đã chốt. Không thiết kế lại.

**Báo cáo:** `docs/codex-queue/275-report.md` (tiếng Việt).

**Đường duyệt:**
- Anh chê lúc 23:50 ngày 04/11, kèm ảnh chụp từ video demo âm: "tại sao, vẫn sử dụng cái kiểu xấu như các cái gai nhọn như kiểu tự style này vậy, nó nhìn thực sự rất xấu".
- Ảnh là nhát chém kết của phím 7 ở hệ Hỏa (`src/view/skills/flame-slash.ts`). Hai mép của nó là hàng lưỡi lửa tam giác do mã tự vẽ: "one per cell, each its own length, pointed".
- Luật của anh (04/11, `game-vfx-production`): hình lửa lấy từ Firefly hoặc Blender, mã chỉ đặt và hoạt hình.
- Anh đã chọn dải lặp `strip-fire-sheath` cho hệ Hỏa (04/11, khoảng 19:40).
- Claude viết lời giải; phản biện Claude trước khi chạy.

## Bối cảnh
- `flame-slash.ts` giữ nguyên:
  - `QI_SLASH_VERTEX`: hình trăng khuyết trải dọc cung, `s` từ 0 tới 1 dọc cung, `v` ngang;
  - mặt nạ trăng khuyết vẽ tay `tMask` và bảng dải `tBand` (tâm, nửa bề rộng theo `s`);
  - thân nhiệt, xương sống trắng vàng, ramp `uSoot`/`uDeep`/`uAmber`/`uCore`, xói `uErode`, mờ `uFade`.
- Chỉ phần `tongue` trong `main()` (từ `float edgeW = …` tới hết phép tính `tongue`, cùng chỗ nó góp vào `heat`) là thứ phải bỏ.
- Dải mới: `games/immortality-cultivation/art-src/lab/vfx/aura/strips/strip-fire-sheath.rgba.png` (512×128, sRGB, alpha thẳng, lặp liền theo x) và `strip-fire-sheath.json`.
  - Trục giữa dải là trục lưỡi. Lửa liếm ra hai phía.
  - `naturalAspect`: chu kỳ 600×300 px nguồn (2:1), dải 4:1.
  - `scroll.periodsPerSecond` 0,5 là giá trị xem trước; hướng trái, tức lùi về phía chuôi.
- `art-src` không nằm trong Git. Lab nạp texture qua `ElementStage.texture(name)` (`element-stage.ts`, khoảng dòng 113). Đọc hàm đó để biết cách đặt tên một đường dưới `art-src/lab/vfx/`.

## Làm ở đâu
- Worktree `games/.wt-ic-flame-slash`, nhánh `codex/flame-slash-strip`, từ `main` của game (Claude tạo, symlink `node_modules`). cwd là gốc repo cha.

### Được ghi
- `games/.wt-ic-flame-slash/src/view/skills/flame-slash.ts`;
- `games/.wt-ic-flame-slash/src/view/skills/element-fire.ts`, chỉ chỗ dựng `FlameSlash`, nạp texture dải và cờ ở mục 3;
- `games/.wt-ic-flame-slash/src/lab/skills-main.ts`, chỉ đọc cờ `?slash=` và đặt vào `FIRE_LAB`;
- `games/.wt-ic-flame-slash/tests/view/flame-slash.test.ts` (tạo mới);
- `games/.wt-ic-flame-slash/docs/changelog/2026-11-05-flame-slash-strip.md` (tạo mới);
- `docs/codex-queue/275-report.md`.

### Cấm
- Sửa file khác; sửa hay tạo ảnh trong `art-src`; mọi lệnh git trừ `status`, `diff`, `log`, `show`.
- Chạy Vitest hay Vite thiếu cờ `--no-cache --configLoader runner` (và `IC_VITE_CACHE_DIR` khi build).
- Mở cổng mạng.

## Việc (lời giải đã chốt)
1. **Shader `FRAGMENT` trong `flame-slash.ts`:**
   - Thêm `uniform sampler2D tStrip; uniform float uHasStrip; uniform float uStripK; uniform float uStripScroll;`.
   - Khi `uHasStrip > 0.5`, **không tính `tongue`**. Thay bằng mẫu dải:
     ```glsl
     float reach = edgeW * 2.6;                       // lửa liếm ra tới 2,6 lần mép thân
     float vs = 0.5 + (v - centre) / (2.0 * reach);   // 0,5 là trục; 0 và 1 là mép dải
     float us = s * uStripK - uTime * uStripScroll;   // cuộn lùi về chuôi
     vec4 st = (vs > 0.0 && vs < 1.0) ? texture2D(tStrip, vec2(us, vs)) : vec4(0.0);
     float flame = st.a * env * behind;
     ```
     Trong đó `edgeW` tính như cũ; `env`, `behind` giữ như cũ.
   - **Ghép:**
     - `heat = max(heatThân, flame * mix(0.62, 0.3, abs(vs - 0.5) * 2.0))`. Lửa của dải đi qua cùng ramp của thân: gốc lửa cam, ngọn nguội về son và muội.
     - Màu dải chỉ dùng để điều biến: nhân `col` với `mix(vec3(1.0), st.rgb * 1.15, 0.5 * flame)`, để vân lửa vẽ tay hiện lên mà không thoát khỏi ramp của hệ.
     - Xói và mờ giữ như cũ (`heat * uFade − uErode * 0.55`, ngưỡng `edge`). Phần mảnh và mờ của dải (alpha thấp) tự xói trước.
   - Khi `uHasStrip < 0.5`, đường cũ (`tongue`) chạy **y nguyên từng phép tính**. Đây là cờ để so A/B.
2. **`FlameSlash`:**
   - uniform `tStrip` (null), `uHasStrip` 0, `uStripK` 1, `uStripScroll` 0,5;
   - phương thức `setStrip(texture: THREE.Texture | null, k: number, scroll: number)`.
   - `uStripK` đặt sao cho một chu kỳ dải phủ chiều dài nhát chém đúng tỉ lệ tự nhiên 2:1. Tính trong `set(...)` từ chiều dài cung trên màn và bề rộng dải; nếu không đo được thì dùng `k = 3` (ba chu kỳ dọc nhát chém). Ghi rõ trong báo cáo cách đã chọn.
3. **`element-fire.ts`:**
   - nạp `aura/strips/strip-fire-sheath.rgba.png` qua `stage.texture(...)`, theo đúng quy ước tên của hàm;
   - đặt texture: `SRGBColorSpace`, `wrapS = RepeatWrapping`, `wrapT = ClampToEdgeWrapping`, mipmap, `premultiplyAlpha = false`;
   - gọi `flameSlash.setStrip(tex, k, 0.5)`, trừ khi `FIRE_LAB.slashTongues` là true;
   - `FIRE_LAB` thêm `slashTongues: false`;
   - texture chưa nạp xong hoặc lỗi thì dùng đường cũ (không bao giờ rỗng).
4. **`skills-main.ts`:** `?slash=tongues` đặt `FIRE_LAB.slashTongues = true` (đường cũ, để so). Mặc định là dải. Ghi dòng này trong chú thích đầu file, chỗ liệt kê cờ.
5. **Test** `tests/view/flame-slash.test.ts` (Node, không WebGL):
   - (a) chuỗi `FRAGMENT` có nhánh `uHasStrip` và vẫn còn nguyên đoạn `tongue` cũ cho nhánh cờ;
   - (b) `setStrip(null, …)` đặt `uHasStrip` 0, có texture thì 1;
   - (c) `FIRE_LAB.slashTongues` mặc định false.

## Kiểm bắt buộc (trong worktree)
1. tsc không lỗi.
2. Vitest đủ, mọi test qua (mốc 975 test ở `main` `5de0d22`).
3. Build tạm `/private/tmp/codex-275-dist` với các cờ; `grep -rl "slashTongues\|uHasStrip" /private/tmp/codex-275-dist` không in gì (lab và kỹ năng chưa vào bản dựng); xóa thư mục.
4. `git status --short`: chỉ các file được ghi.

## Claude làm sau (trình duyệt)
- Quay nhát chém kết phím 7 ở hệ Hỏa, camera chơi, 1280×720 và 1920×1080: dải mới và `?slash=tongues` cạnh nhau, nền sáng và tối.
- Parity: hệ Kim trùng 100 %; các khung không có nhát chém của hệ Hỏa trùng 100 %.
- Gửi anh video.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
