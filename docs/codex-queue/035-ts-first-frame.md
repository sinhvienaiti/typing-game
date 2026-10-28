# Phiếu 035 · Tuyến Cuối · Bùng sáng và đèn mới hiện trọn ở khung đầu (chỉ mã, không trình duyệt)

**Bối cảnh:** chủ dự án duyệt chuẩn VFX nhiều lớp ngày 28/10/2026: [`docs/games/VFX_STANDARD.md`](../games/VFX_STANDARD.md). Theo §3.1 luật 5 và §3.4, lóe và đèn mới phải đủ sáng ngay khung đầu (f0); theo §5.6, khung đầu phải ≥ 95 % đỉnh. Tuyến Cuối (`games/typing-survival`) đang mất khung đầu:
- **Thứ tự một khung** (`src/view/combat.ts:399-419`, `src/app/main.ts:601-659`):
  1. sự kiện: `combat.read` gọi `Glows.burst` và `GunLights.flash`;
  2. `Glows.step(dt)`;
  3. vẽ: `stamp`, đôi khi `burst`;
  4. `Glows.flush()`.
- **Bùng sáng:** `Glows.step` cộng `dt` vào tuổi trước lần ghi đầu (`src/view/fx.ts:181-197`). Vì vậy một lóe dài 3 khung (`3 * F`, F = 1/60 s) hiện 44 % rồi 11 % rồi tắt, thay vì 100 %, 44 %, 11 %.
- **Đèn:** cùng lỗi (`src/view/lights.ts:96-109`). Ở khung đầu, đèn của Xung chỉ sáng 44 %, Tán và phát đầu băng Xung 63 %, Ray 69 %, Pháo Sao 74 %, hạ quái to 79 %.
- **Bản vá tạm của N4/N6:** lượt này cho riêng các burst mới của nó tham số `early = F` (`docs/FEEL_PASS_S1.md` §12, đoạn "Bùng ở khung đầu"). Các burst cũ vẫn mất khung đầu.
- **Lỗi cùng chỗ:** một burst tạo trong pha vẽ, sau một `stamp`, làm lệch chỉ số. Ví dụ là vòng giậm của Trâu (`src/view/gunfx.ts:207`). `stamp` ghi ở ô `live + stamps`, nên một ô trong `[0, instanceCount)` không được ghi ở khung đó, và vẽ lại dữ liệu của khung trước.

Phiếu này sửa `Glows` và `GunLights`:
- hiệu ứng và đèn mới được vẽ ở tuổi 0 ngay trong khung tạo ra chúng;
- sau đó chúng già đi đúng như thiết kế, **không** sáng hơn thiết kế;
- chỉ đụng view; sim không đổi (`FEEL_PASS_S1.md` §1.1, §7.1).

**Sau phiếu, Claude làm (không thuộc phiếu):**
- Đo lại trên trình duyệt, cảnh `f5` và `f8`:
  - tương phản dòng từ ≥ 7 : 1 ở p99 (nay 7,40–7,49);
  - nền dưới dòng từ: p50 tăng ≤ 0,02 (`FEEL` §4.1);
  - trắng xóa ≤ 6 % vùng sân (`VFX_STANDARD` §3.6), vì khung đầu nay sáng hơn. Đo được bằng `tools/vfx-sheet` (phiếu 037), `measure --field`.
- `survival-s1-stage` ở cả hai cỡ: trận trình duyệt chạy lại trong Node ra cùng mã băm (`FEEL` §7.1 ý 4).
- Sửa đoạn §12 của `FEEL_PASS_S1.md` và dòng `early` trong `AGENTS.md` của game.
- Viết changelog, rồi mới commit.

**Thư mục làm việc:** cwd `.` là repo cha `/Users/toandx/htdocs/typing-game`, để ghi được báo cáo. Mã của phiếu nằm trong worktree `games/.wt-ts-vfx` (nhánh `ts-vfx`), do điều phối viên tạo trước khi chạy.
- **Nền giả định:** nhánh `ts-vfx` tách từ `main` của Tuyến Cuối **sau khi** lượt n4n6 commit nốt tài liệu.
  - Lúc viết phiếu (28/10, khoảng 03:30) và lúc kiểm lại (07:32), `main` ở `ce9dea3`. Bản checkout chính còn bốn file chưa commit: `AGENTS.md`, `docs/BUILD_S1.md`, `docs/FEEL_PASS_S1.md`, `docs/changelog/2026-10-27-feel-n4n6.md`. `src`, `tests`, `scripts` sạch.
  - Phiếu giả định HEAD của worktree là `ce9dea3` cộng các commit chỉ sửa tài liệu. Mọi số trong phiếu tính trên `src`, `tests`, `scripts` của `ce9dea3` (Kiểm 0).
- **Một mình trong worktree:** trong lúc phiếu chạy, không agent nào khác ghi vào `games/.wt-ts-vfx`. Làn V3 của Claude (`VFX_STANDARD.md` §5.4) chỉ bắt đầu ở đó sau khi Claude commit kết quả phiếu.
- **`node_modules`:** điều phối viên đã cài sẵn trong worktree. Thiếu thì dừng và ghi báo cáo; không cài.
- **Chạy lệnh của game** trong worktree: `cd games/.wt-ts-vfx && <lệnh>`. Khóa máy dùng chung là `../../.local/bin/heavy.sh` (đường dẫn tính từ worktree).
- **`pnpm`:** gọi qua `env pnpm_config_verify_deps_before_run=warn`. Phiếu 021 cần biến này trong sandbox.
- **`tsx`:** dùng `node --import tsx …`. Lệnh `pnpm exec tsx` bị sandbox chặn (`listen EPERM`, phiếu 023).
- **Ngoại lệ luật chung:** luật chung đầu phiếu cấm chạy build và test của game. Phiếu này cho phép **chỉ** các lệnh ở mục Kiểm, **chỉ** trong `games/.wt-ts-vfx`.

**Chỉ được ghi:**
- `games/.wt-ts-vfx/src/view/fx.ts`: chỉ lớp `Glows`, và một hàm phụ cấp module nếu cần. `Strips`, `Streaks`, `Column`, atlas và shader giữ nguyên;
- `games/.wt-ts-vfx/src/view/lights.ts`: chỉ lớp `GunLights`;
- `games/.wt-ts-vfx/src/view/shots.ts` và `games/.wt-ts-vfx/src/view/typing-feel.ts`: chỉ bỏ đối số `, F` cuối ở 8 lời gọi `burst(…, NaN, F)` (mục 1, ý 5), không sửa gì khác;
- `games/.wt-ts-vfx/tests/first-frame.test.ts` (mới);
- `games/.wt-ts-vfx/tmp/035/**`: bằng chứng (`.gitignore` của game đã bỏ qua `tmp/`);
- `docs/codex-queue/035-report.md` ở repo cha: tiếng Việt có dấu.

**Cấm:**
- ghi ngoài danh sách trên. Trong worktree, không đụng `src/sim`, `src/content`, `src/kit`, `src/app`, `scripts`, các test khác, `docs`, `AGENTS.md`;
- ghi vào bản checkout chính `games/typing-survival`, hay vào worktree khác (các `games/.wt-*` khác, `typing-game-wt/*`);
- lệnh git có ghi (`commit`, `add`, `stash`, `checkout`, `reset`, `worktree`…). Được dùng: `status`, `diff`, `log`, `show`, `branch --show-current`, `rev-parse`, `merge-base --is-ancestor`. Khi trỏ vào bản checkout chính, luôn kèm `--no-optional-locks`;
- cài gói, mạng, mở cổng, dev server, trình duyệt;
- đổi số thiết kế (cường độ, đời, cỡ, ưu tiên đèn, công thức mờ dần) để bù khung đầu;
- đụng Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`).

Chú thích trong mã viết bằng tiếng Anh, ngắn, theo giọng của file.

## Việc

Trong phiếu, "tuổi" là thời gian từ lúc tạo, tính bằng giây.

### 1. `Glows` (`src/view/fx.ts:120-212`)

Hành vi bắt buộc:
1. **Khung đầu ở tuổi 0.** Một burst mới được `flush()` của **chính khung tạo ra nó** ghi ở tuổi 0, dù nó được tạo trước `step()` (pha sự kiện) hay sau `step()` (pha vẽ). Ở khung đó:
   - vị trí là chỗ tạo; cỡ là `from`; góc là `angle`;
   - alpha là công thức mờ dần hiện có tính ở tuổi 0:

   | Loại burst | Alpha ở tuổi 0 |
   |---|---|
   | Lóe thường (đời < 3 s) | 1 |
   | Than (đời ≥ 3 s) | 1 |
   | Khói, vết cháy (`smoke`, không phải `CELL.puff`) | `intensity` |
   | Khói cụm (`smoke`, `CELL.puff`) | 0, vì cụm khói "bốc lên" từ 0 theo thiết kế |

2. **Già đi như cũ.** Từ `step()` kế tiếp, tuổi tăng `dt` mỗi bước, vị trí và góc cũng tiến `dt` như cũ. Burst bị bỏ khi tuổi ≥ đời, như cũ. Không burst nào được ghi hai lần ở tuổi 0. Không đổi cường độ, công thức mờ dần, cỡ hay chuyển động.
3. **`stamp` giữ nguyên:** chỉ hiện ở khung được gọi, và đứng sau các burst trong mảng instance.
4. **Không bỏ trống ô nào.** Ở mỗi khung, mọi ô trong `[0, instanceCount)` đều được ghi ở chính khung đó.
5. **Bỏ tham số `early`** khỏi `burst`; 14 tham số còn lại giữ nguyên thứ tự và giá trị mặc định. Bỏ đối số `, F` cuối ở đúng 8 lời gọi:
   - `src/view/shots.ts:254`, `:255`, `:256`, `:261`;
   - `src/view/typing-feel.ts:179`, `:184`, `:186`, `:187`.

   Lý do: sau bản sửa, `early = F` cho burst hai khung đầy (tuổi −F rồi 0), tức là sáng hơn thiết kế.
6. **Không cấp phát bộ nhớ trong một khung.** Mảng mới chỉ được tạo trong constructor.

Cách làm gợi ý (Claude đã cài thử; cách này đạt mọi kiểm dưới đây):
- **Burst:** stride 17 → 18. Ô 17 là cờ "mới", bằng 1 lúc tạo. Tuổi lúc tạo là 0.
- **`step(dt)`:**
  - chỉ già hóa và di chuyển burst không có cờ mới;
  - bỏ burst hết đời (chỉ xét burst không có cờ mới), rồi nén mảng;
  - đặt `stamps = 0`;
  - **không** ghi instance.
- **`stamp`:** ghi vào ba mảng tạm `Float32Array` (vị trí, màu, cỡ; mỗi mảng `capacity` phần tử).
- **`flush()`:**
  - tính alpha và cỡ từ tuổi đã lưu;
  - ghi các burst vào ô `0 … live − 1`, rồi xóa cờ mới;
  - chép các stamp vào ô `live … live + stamps − 1`;
  - gọi `uploadQuads`.
- **`write`:** thành một hàm cấp module, nhận mảng đích.
- Chú thích của `Glows`, `burst`, `step`, `flush` sửa cho đúng.

### 2. `GunLights` (`src/view/lights.ts:39-127`)

- `flash()` đánh dấu đèn là mới. `update()` đầu tiên sau đó (cùng khung) ghi đèn ở `power × scale`, tức tuổi 0: không cộng `dt`, rồi xóa cờ. Các lần `update()` sau già hóa như cũ.
- Cường độ và vũng sáng trên sàn ở khung đầu:
  - `light.intensity` = `power × scale × 26` (`CANDELA`);
  - `uLightColor` = màu × `power × scale` × 1,4 (`POOL`).
- `hold()` xóa cờ mới: đèn giữ không đổi. `pickLight`, ưu tiên và `lit` không đổi.
- Hôm nay mọi `flash` đều gọi ở pha sự kiện, trước `lights.update` ở `shots.ts:369`. Bản sửa không được dựa vào thứ tự đó: một flash tạo sau `update()` phải được ghi ở tuổi 0 ở `update()` kế tiếp.

### 3. `tests/first-frame.test.ts` (mới, vitest, môi trường `node`)

**Chuẩn bị:**
- `atlas()` cần `document`. Trước khi tạo `Glows`, gọi `vi.stubGlobal("document", { createElement: () => ({ width: 0, height: 0, getContext: () => null }) })`. Nhánh `getContext() === null` đã có sẵn. Trả lại bằng `vi.unstubAllGlobals()` sau cùng.
- Đọc dữ liệu instance qua `g.mesh.geometry.getAttribute("iColor" | "iPos" | "iSize").array` và `g.mesh.geometry.instanceCount`. Alpha của ô i là `iColor[i * 4 + 3]`.
- Một khung trong test theo đúng thứ tự của game: sự kiện → `step(dt)` → vẽ → `flush()`, với `dt = 1/60`.
- **Khung "hiện":** ô còn trong `instanceCount` và alpha > 1e-6. Tuổi lưu bằng float32 có thể để lại thêm một khung có alpha < 1e-6. Lỗi đó có từ trước; không sửa.

**Chín ca bắt buộc:**
1. Lóe `CELL.star4`, đời `3 * F`, `intensity` 3: alpha theo khung là `1`, `0.444444`, `0.111111`, rồi tắt ở khung thứ tư. Mã cũ cho `0.444444`, `0.111111`.
2. Đời 2–6 khung (`CELL.soft`): đúng số khung hiện bằng số khung đời. Alpha ở khung n là `(1 − n·dt/đời)²` (sai số 1e-5), và chỉ đúng một khung có alpha bằng 1:

   | Đời | Alpha theo khung |
   |---|---|
   | 2F | `1, 0.25` |
   | 3F | `1, 0.444444, 0.111111` |
   | 4F | `1, 0.5625, 0.25, 0.0625` |
   | 5F | `1, 0.64, 0.36, 0.16, 0.04` |
   | 6F | `1, 0.694444, 0.444444, 0.25, 0.111111, 0.027778` |

3. **Vị trí, cỡ, góc.** Burst `CELL.ring + FLAT` tại (2; 0,5; −4), cỡ 1 → 3, đời 0,5 s, vận tốc (6; 0; −12), quay 3 rad/s, góc 0,25.
   - Khung đầu: `iPos` = `[2, 0.5, -4, CELL.ring + FLAT]`, `iSize` = `[1, 0.25]`.
   - Khung sau, với k = dt/0,5: x = 2 + 6·dt, z = −4 − 12·dt, cỡ = 1 + 2·(1 − (1 − k)²), góc = 0,25 + 3·dt (sai số 1e-5).
4. **Than và khói.** Ba burst, mỗi burst một cách mờ dần. Than nằm trong một `Glows` thường (`new Glows(8)`). Vết cháy và cụm khói nằm chung một `Glows` ở chế độ khói (`new Glows(8, true)`): công thức khói chỉ chạy khi `smoke` là `true`.

   | Burst | `Glows` | Khung đầu | Khung sau |
   |---|---|---|---|
   | Than (`CELL.soft + FLAT`, đời 3,5 s) | thường | 1 | |
   | Vết cháy của khói (`CELL.soft + FLAT`, đời 9 s, `intensity` 0,8) | khói | 0,8 | |
   | Cụm khói (`CELL.puff`, đời 3,5 s, `intensity` 0,75) | khói | 0 | `min(1, 20k)·(1 − k²)·0,75`, k = dt/3,5 |

5. **Burst tạo trong pha vẽ.**
   - Trước khung, lấp ba mảng instance bằng `NaN`.
   - Khung gồm: một burst ở pha sự kiện; `step`; hai `stamp`; một burst; một `stamp`; `flush`.
   - Kết quả:
     - `instanceCount` = 5;
     - không còn `NaN` trong `[0, 5)` của cả ba mảng;
     - hai burst có alpha 1;
     - ba stamp đứng ở ô 2, 3, 4, theo đúng thứ tự gọi.
   - Khung sau: `instanceCount` = 2, burst thứ hai có alpha `(1 − dt/0,45)²`.
6. **Dừng** (`dt` = 0, ba khung liền): burst mới giữ alpha 1. Ca giữ hành vi, đạt cả trên mã cũ.
7. **Đèn chớp.** Với mỗi đèn chớp của `LIGHT` (bỏ `tia`, `tiaSlide` vì đời 0), so cường độ khung đầu với một đèn giữ cùng công suất (`hold(…, LIGHT.tiaSlide, …, scale = power)`):
   - khung đầu bằng đèn giữ đó, tỉ lệ 1;
   - khung n bằng `lightLevel(n·dt, life)` (sai số 1e-5);
   - chỉ một khung có tỉ lệ 1.

   Bảng tỉ lệ cường độ / công suất (4 chữ số):

   | Đèn | Tỉ lệ theo khung | Mã cũ ở khung đầu |
   |---|---|---|
   | `xung` | `1, 0.4444, 0.1111` | 44 % |
   | `xungFirst` | `1, 0.6267, 0.3403, 0.1406, 0.0278` | 63 % |
   | `tan` | `1, 0.6267, 0.3403, 0.1406, 0.0278` | 63 % |
   | `ray` | `1, 0.6944, 0.4444, 0.25, 0.1111, 0.0278` | 69 % |
   | `phao` | `1, 0.7415, 0.5216, 0.3403, 0.1975, 0.0934, 0.0278, 0.0008` | 74 % |
   | `big` | `1, 0.7901, 0.6049, 0.4444, 0.3086, 0.1975, 0.1111, 0.0494, 0.0123` | 79 % |

8. **Vũng sáng trên sàn.**
   - Tạo `const deck = deckLightUniforms()` và `new GunLights(new THREE.Scene(), deck, 4)`.
   - `flash(LIGHT.ray, …, màu (0,5; 0,25; 1))`, rồi `update(dt)`.
   - Kết quả: `deck.uLightColor.value[0]` = `[2.1, 1.05, 4.2]` (5 chữ số).
9. **Đèn giữ** (`hold(1, LIGHT.tia, …)`, ba khung): cường độ 23,4 (0,9 × 26) mỗi khung. Khung không giữ nữa: 0. Ca giữ hành vi, đạt cả trên mã cũ.

In bảng 1, 2, 7 bằng `console.log`, có tiền tố `035 `, để báo cáo chép lại.

## Kiểm (bắt buộc)

Chạy từ cwd `.` (repo cha), trừ khi ghi khác. Dán lệnh và dòng kết quả vào báo cáo.

0. **Điều kiện đầu**, trước khi ghi gì vào `src`. Một điều không đạt thì dừng, ghi báo cáo, không sửa mã.
   - `git -C games/.wt-ts-vfx branch --show-current` in `ts-vfx`.
   - `git -C games/.wt-ts-vfx merge-base --is-ancestor ce9dea3 HEAD` thoát 0.
   - `git -C games/.wt-ts-vfx diff --quiet ce9dea3 HEAD -- src tests scripts package.json pnpm-lock.yaml tsconfig.json vite.config.ts vitest.config.ts kit.config.json` thoát 0: từ `ce9dea3` chỉ tài liệu đổi.
   - `test -e games/.wt-ts-vfx/node_modules/.bin/vitest` thoát 0.
   - Giữ kết quả để so ở Kiểm 7:
     - `git -C games/.wt-ts-vfx status --short --untracked-files=all`;
     - `git --no-optional-locks -C games/typing-survival status --short`;
     - `git status --short --untracked-files=all -- docs/codex-queue/`.
   - Mã băm trước khi sửa:
     - lệnh: `cd games/.wt-ts-vfx && mkdir -p tmp/035 && ../../.local/bin/heavy.sh node --import tsx scripts/chapter-hashes.ts > tmp/035/before.txt` (khoảng 8 s);
     - `wc -l` in 152;
     - `shasum -a 256` in `ae7e9859269b2aece6a7bacbd946dfa93b9a131aeb68a5f5dbed97830dfe626e`. Claude tính số này hai lần trên `ce9dea3` (bản checkout chính và một bản `git archive`), và một lần trên bản cài thử của phiếu: cả ba giống hệt.
   - **Test trước, mã sau:**
     - viết `tests/first-frame.test.ts` trước khi sửa `src`;
     - chạy riêng nó: `cd games/.wt-ts-vfx && env pnpm_config_verify_deps_before_run=warn ../../.local/bin/heavy.sh pnpm exec vitest run tests/first-frame.test.ts`;
     - phải ra: ca 1–5, 7, 8 hỏng; ca 6 và 9 đạt. Trên bản cài thử của Claude: 7 hỏng, 2 đạt;
     - ghi tên các ca hỏng vào báo cáo.
1. **`pnpm check`.** Lệnh: `cd games/.wt-ts-vfx && env pnpm_config_verify_deps_before_run=warn ../../.local/bin/heavy.sh pnpm check`, thoát 0. Phải thấy:
   - `src/kit OK: 59 files match kit-manifest.json`;
   - `Test Files  15 passed (15)`;
   - `Tests` ≥ 151 passed: trước phiếu 142 trong 14 file, bản cài thử thêm 9;
   - `tsc --noEmit` và `vite build` không lỗi.

   Test hiệu năng bước sim trong `tests/survival-sim.test.ts` có thể hỏng khi máy tải nặng (`AGENTS.md` của game). Nếu chỉ nó hỏng, chạy lại một lần và ghi cả hai kết quả.
2. **File test mới chạy riêng** đạt cả 9 ca. Các dòng `035 …` in ra khớp bảng ở mục 3 tới 4 chữ số.
3. **Mã băm sau khi sửa:**
   - `cd games/.wt-ts-vfx && ../../.local/bin/heavy.sh node --import tsx scripts/chapter-hashes.ts > tmp/035/after.txt`;
   - `cmp tmp/035/before.txt tmp/035/after.txt` không in gì;
   - sha256 vẫn là `ae7e9859…626e`; 152 dòng.
4. **Sim không đổi:** `git -C games/.wt-ts-vfx status --porcelain -- src/sim src/content src/kit src/app scripts tests/golden` không in gì.
5. **`early` đã bỏ hết:**
   - `grep -rnw early games/.wt-ts-vfx/src/view games/.wt-ts-vfx/src/app` không in gì (trước phiếu: 3 dòng, đều ở `fx.ts`);
   - `grep -c "NaN, F)"` trên `shots.ts` và `typing-feel.ts` in `0` và `0` (trước: 4 và 4);
   - `grep -c "NaN);"` trên hai file đó in `4` và `4` (trước: 0 và 0).
6. **Đột biến, để chứng minh test bắt được lỗi.** Chép bản đã sửa của `fx.ts` và `lights.ts` sang `tmp/035/`. Làm lần lượt hai đột biến; sau mỗi đột biến, chạy lại file test mới và ghi tên các ca hỏng:
   - (a) trong `Glows.step`, già hóa cả burst có cờ mới, như mã cũ. **Đạt khi ca 1–5 đều hỏng.** Bản cài thử: đúng 5 ca hỏng, là ca 1–5;
   - (b) trong `GunLights.update`, bỏ nhánh cờ mới. **Đạt khi ca 7 và 8 đều hỏng.** Bản cài thử: đúng 2 ca hỏng, là ca 7 và 8.

   Số ca hỏng của bản cài thử chỉ để so. Nếu thêm ca khác hỏng, ghi tên và lý do vào báo cáo; đột biến vẫn đạt.

   Sau đó trả lại hai file, rồi `cmp` với bản đã chép: không in gì.
7. **`git status` so với lúc bắt đầu:**
   - Worktree: chỉ **thêm** ` M src/view/fx.ts`, ` M src/view/lights.ts`, ` M src/view/shots.ts`, ` M src/view/typing-feel.ts`, `?? tests/first-frame.test.ts`. `tmp/` và `dist/` bị bỏ qua nên không hiện.
   - `games/typing-survival`: như lúc đầu. Nếu khác, chép các dòng khác vào báo cáo; đó là việc của làn khác, phiếu này không ghi ở đó.
   - `docs/codex-queue/` ở repo cha: chỉ thêm `?? docs/codex-queue/035-report.md`. Báo cáo của phiếu khác đang chạy cùng lúc (ví dụ `036-report.md`) thì ghi tên, không tính.
8. **`git -C games/.wt-ts-vfx diff --numstat`** ghi vào báo cáo. Để so: bản cài thử của Claude là `fx.ts` +46 −27, `lights.ts` +8 −2, `shots.ts` +4 −4, `typing-feel.ts` +4 −4. Mục này chỉ để tham khảo, không phải cổng.

## Báo cáo `docs/codex-queue/035-report.md`

- Nền thật của worktree (`git log --oneline -3`) và kết quả Kiểm 0.
- Các file đã sửa, mỗi file một dòng nói đã đổi gì.
- Kết quả 9 mục kiểm (Kiểm 0–8), kèm số: test (file, ca), hai sha256 của mã băm, tên các ca hỏng ở bước test trước, mã sau và ở hai đột biến.
- Hai bảng trước và sau (bùng sáng theo đời, đèn theo loại), lấy từ dòng `035 …`.
- Số dòng `src` trước và sau (`find src -name '*.ts' -not -path 'src/kit/*' | xargs cat | wc -l`).
- Những chỗ phiếu chưa rõ và cách đã chọn. Ghi riêng những chỗ Claude phải xem trên trình duyệt: cảnh `f5`, `f8`, tương phản dòng từ, nền dưới dòng từ, Ray và Tia quanh tàu.

**Xong khi:** Kiểm 0–7 đạt, báo cáo đã viết. Codex không commit; Claude đo lại trên trình duyệt rồi mới commit.
