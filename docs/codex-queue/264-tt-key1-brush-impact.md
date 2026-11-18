# Phiếu 264 · Tu Tiên · Code: va chạm phím 1 bản 2, thẻ lửa nét cọ có mặt nạ thay hoa sen (gói CX-H)

**Loại việc:** code (`gpt-6.1-sol`, mức `xhigh`): kit Fire, sân khấu nguyên tố, đèn chớp của lab, hai API lab, kịch bản chụp, test. Lời giải đã chốt ở mục "Việc"; Codex không thiết kế lại hình, số, hướng hay cách đo. Chỗ nào không làm được đúng như viết thì dừng ở đó, ghi vào báo cáo, không tự chọn cách khác.

**Báo cáo:** `docs/codex-queue/264-report.md` (tiếng Việt).

**Đường duyệt:** Claude tự phân tích (đọc mã `main` `35f1b77`; phiếu và báo cáo 258, 273, 273b, 274; số nền A1; đo mặt nạ thật lúc 23:30 ngày 04/11). Duyệt theo đường phản biện Claude, bước 9 của skill `agent-orchestration`: agent phản biện độc lập. Từ luật làm gọn 05/11 (skill `agent-orchestration`, "Working lean" mục 6), phiếu dài hơn 1.500 chữ cần **một** PASS, ghi ở mục "Phản biện". Không giao Codex trước khi có PASS đó. Phiếu 274 đã gộp vào `main` (`0f4d72c`).

## Bối cảnh

**Nguồn**
- Kế hoạch `docs/games/tu-tien/skills/INTEGRATION_PLAN_2026-11-04.md` §2.5, §2.6, §2.8, §2.9, §3 hàng CX-G và CX-H.
  - Số phiếu: §7 ghi `263-tt-key1-brush-impact`; ghi chú đầu kế hoạch dời số lên một bậc, nên CX-H là **264**.
  - Cờ `?impact=brush|lotus` vốn thuộc CX-G (263, chưa viết). Phiếu này chỉ thêm đúng cờ đó; phần còn lại của CX-G để nguyên.
- Clip: phiếu và báo cáo 273, 273b; `art-src/lab/vfx/fire/impact-k1-r2/fire-impact-k1-r2-v1a.a4.masks.json`; tấm xem ở `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/impact-k1-r2/masks/`.
- Số nền A1 (Claude đo bản lab ở `bc94110`): `typing-game-review/captures/tu-tien/integration-r2/baseline/BASELINE.md`.
- Máy: `FlipbookPool` bản 2 (258, 258b, đã gộp ở `ceb51c2`) và `rampCool` của phiếu 274 (setter của pool, uniform `uRampCool`, mặc định 0). **Phiếu viết trên `main` sau khi 274 gộp.** Nếu lúc giao `FlipbookPool` chưa có setter `rampCool` thì Claude không giao.

**Anh đã duyệt** (04/11, khoảng 22:00) nhịp cháy của clip lửa nét cọ phím 1 (video 273b): ba nét lửa mở từ một gốc ở dưới bên trái, quét lên phải, hiện theo thứ tự nét, giữ, rồi xé từ mũi và tàn thành than. Trước đó anh đã duyệt khung cuối A3, trong đó gốc nét "nguội thành than đỏ son". Phiếu 274 thêm `rampCool` cho việc nguội đó; Claude đặt `rampCool = 1` cho clip này (274, mục "Claude làm sau").

**Clip** (MD5 kiểm lúc 23:30, khớp báo cáo 273b):

| Tệp trong `art-src/lab/vfx/fire/impact-k1-r2/` | Nội dung | MD5 |
|---|---|---|
| `fire-impact-k1-r2-v1a.a4.rgba.png` | 2304 × 1536, sRGB, alpha thẳng, lưới 6 × 4 ô 384 px, 24 khung, 24 fps (nguồn f053–f076 của lượt Firefly 2), viền 2 px bằng 0 | `9c2e2446eaffd655b7424fd2a5798240` |
| `fire-impact-k1-r2-v1a.a4.maskA.png` | dữ liệu tuyến tính: R bao, G ink, B vạch nóng, A thứ tự sống sót (theo hạng, 273b) | `01ca37174e6881c031bda65ecb6ab1b5` |
| `fire-impact-k1-r2-v1a.a4.maskB.png` | R thứ tự hiện: gốc 0,0024, ba mũi ≥ 0,996 | `a82cd18bca3033cf94490c562602fec8` |

- **Gốc chém** nằm ở (331, 797) trên khung nguồn 1080, tức (117,69; 283,38) px trong ô 384, tức `anchor` [0,306481; 0,737963]. Số này khớp `checks.reveal.endpoints` của `masks.json`.
- **Hướng quạt.** Claude đo trên A.R > 0,5 của cả 24 ô, lấy góc từ gốc, trục y hướng lên:
  - tâm vùng bao: 80,3° (ô 0) tới 82,5° (ô 23), trung bình **81,15°**;
  - tính theo alpha: 84,0–87,8°;
  - vùng bao trải từ 42–49° (phân vị 5 %) tới 137,5–139° (phân vị 95 %): nét đi lên phía trái rồi cong sang phải tới mũi;
  - hộp bao chung x 55–318, y 77–291 px (y xuống). Quạt cao 206 px (0,537 ô) trên gốc và rộng 263 px (0,685 ô).
  - Ghi vào manifest: `heading` **81**.
- **Xem trước CPU của 273b** (đá tối, `rampCool` 0):
  - đời 43/60 s theo lịch `impact-key1`: hiện 0–3, giữ 4–9, xé 10–20, tàn 20–42;
  - diện tích sáng so với tick 9: tick 12 là 0,68, tick 18 là 0,19, tick 40–42 bằng 0.
- **Với `rampCool = 1`** (274): ở tick 18, ngưỡng xói e ≈ 0,819, nên mọi điểm thân còn sống có r ≤ 0,181. Mức đó dưới bậc son 0,23–0,27 của `fbRamp`, nên thân đã thành than tối. Vạch nóng (`uHot`, HDR) không theo `rampCool`.
- **Bộ nhớ:** ba ảnh 2304 × 1536 RGBA8 có mipmap, khoảng 57 MB GPU.

**Mã hiện tại** (`games/immortality-cultivation`, `main` `35f1b77`, Claude đã đọc; số dòng dưới đây đã kiểm lại ở `0f4d72c`, HEAD của worktree):
- `src/view/skills/element-fire.ts`:
  - `impact()` (dòng 760–773) vẽ cho mọi ô kiếm:
    - `point()` (pool `fx-fire-points`);
    - `lotus()` (pool `flipbook-fire-burst`): gốc trên đất ở p + 0,15 × hướng đòn, cao 2,0·s m, `lift` 0,7;
    - `sparkRays()` (`flipbook-fire-sparks`);
    - `emberBurst()` (`fx-embers`);
    - vòng `ember()` (pool `motes`, không tên);
    - `stage.accent` ở đòn lớn.

    Trong đó `s = a.scale × (a.big ? 1,3 : 1)`.
  - `aftermath()` (807–810) gọi `burnGround()` (507–530), hàm này vẽ:
    - `scorch.spawn` (pool `ground-decals`): vết cháy code;
    - `groundFire()` (`flipbook-fire-ground`): lửa đất sống khoảng 3 s;
    - `risingEmbers`, hai `wisp`, và một bộ phát than bay lên.
  - `FIRE_LAB` (dòng 93) là chỗ duy nhất kit nhận cờ lab. `flip()` (166) dọn options dùng chung nhưng **không** xóa `timing`, `variant`.
- `src/view/skills/sword-skills.ts`:
  - Hook `impact` được gọi từ `strike()` cho mọi ô (k1, auto, k2, guard, k4, k5). Bay của phím 1 chạy dưới `use("k1")`, nên `ImpactArgs.slot === "k1"` đúng là đòn phím 1.
  - Mỗi lần phóng có hai đòn: đòn chính (scale 1,05, kiếm thứ ba `big`) và đòn xuyên vào thú gần đích trong 3 m (scale 0,8, không `big`).
  - Sau đòn chính có `aftermath(f.tx, f.tz, 1.1, 1.2, 18)` (slot k1), rồi dừng hình 50 ms (3 khung, `world` = 0).
  - Đòn trúng ở tick 6, 36, 66 (`T_K1_HITS`). CX-J sẽ dời đòn đầu sang 18; mã của phiếu này không phụ thuộc vào mốc đó.
- `src/view/skills/flipbook.ts` (sau 258 và 274):
  - `FlipbookPlayer.library(folder)` nhận bất kỳ chuỗi thư mục nào (base = vfxBase + folder + "/").
  - `parseFlipbookManifest` chỉ nhận tên tệp không có "/" (`FILE`, cờ `i`).
  - `FlipbookLibrary.load` bỏ qua im lặng khi không có `manifest.json` hoặc kết quả không phải JSON. Nó bỏ cả mục, kèm cảnh báo, khi atlas hay một mặt nạ không nạp được. Khi đó pool không bao giờ `ready`, và `spawn` không làm gì vì `meta === null`.
  - Pool vẽ sprite ở tuổi 0 rồi mới tăng tuổi.
  - Pool có mặt nạ A lấy đời từ `timingProfile` ((42 + 1)/60 s), bỏ qua `cool` và mặc định `fadeOut` 0.
  - Lưới tên `"flipbook-" + id`.
- `src/view/skills/element-stage.ts`: có `pool`, `firePoints`, `accent`; chưa có đường cho đèn.
- Lab (`src/lab/skills-main.ts`, `src/lab/feel.ts`):
  - Đèn chớp là `FlashLights` (3 `PointLight` ở High).
  - `flash()` chạy trong `fx.update()`, rồi `lights.update(dt)` giảm `exp(−7·dt)` **trước** khi vẽ, nên khung vẽ đầu chỉ có 0,89 cường độ đặt.
  - Có sẵn `__lab.fxNamed()`, `fxShowNamed()`, `debugShow()`, `post({ screen })`, `events()`, `perf()`.
  - Kịch bản `scripts/visual/scenarios/lab-element-fire.mjs` (`PLAN=fixes|linger`, `WORLD=1`, `QS`) và `lab-element-perf.mjs`.
- `art-src` không nằm trong Git (`.gitignore` của nó là `*`). Worktree không có atlas, nên test không được đọc ảnh.
- `src/view/skills/*` chỉ tới được từ lab: bản dựng gồm `index.html`, `bench.html`, `tinh-tu.html` (`vite.config.ts`).

**Claude kiểm danh sách "lớp cũ phải tắt".** ChatGPT và Gemini ghi rằng đòn phím 1 hôm nay có hoa sen, tia nan bánh xe, chấm than, vòng nhiệt, ấn đất và vết cháy code. Kiểm ở mã:
- Hoa sen, tia lửa nan (`fire-sparks`), than: có, như trên.
- **Vòng nhiệt: không có ở đòn.** `rings` chỉ dùng trong `release()` (vòng áp lực ở tay, 0,3 s), `groundRings` chỉ trong `plant()` của phím 7.
- **Ấn đất: không có ở đòn.** Ấn dưới chân người chơi bừng lên lúc phát chiêu là của `sword-skills.ts` (`blazeGoal`), thuộc pha phát. Hai trợ lý ghi nhầm hai mục này; phiếu này không đụng hai lớp đó.
- Vết cháy code: có, là `scorch.spawn` trong `burnGround()` qua hook `aftermath`.
- **Hai trợ lý bỏ sót một lớp:** hook `aftermath` của đòn phím 1 còn đặt lửa đất `fire-ground`, sống khoảng 3 s. Claude chốt tắt nó ở bản nét cọ (mục 2.4). Lý do: đó là một thân lửa thứ hai, sống lâu hơn nhịp tàn anh đã duyệt khoảng 2,3 s, và trái §2.6 ("phần sáng lớn tan gần hết" trước tick 20).

**Số nền A1** (bản hoa sen, `BASELINE.md`):
- khung đầu của chớp điểm `fx-fire-points` là 0,16 (đỉnh ở tuổi 6, vì lưỡi lửa mọc dần trong khoảng 60 ms);
- khung đầu của đèn chớp là 0,89 cường độ đặt (tính từ mã);
- thân hoa sen ở tuổi 18 còn 93–97 % diện tích, 100 % năng lượng;
- trắng xóa cả khung 0,007 %;
- phím 1, Fire hơn Metal +0,3 ms (hào quang tắt) và +0,7 ms (hào quang A); nhiễu giữa các vòng tới 1,6 ms.

## Lời giải (tóm tắt)

1. **Chế độ `brush` (mặc định), đòn phím 1:**
   - một thẻ lửa nét cọ có mặt nạ (`FlipbookPool` bản 2, `rampCool` 1), gốc đặt đúng điểm trúng, xoay theo hướng đòn trên màn hình có giới hạn;
   - một chớp nhỏ tên `fx-fire-flash` và một đèn, cả hai đủ sáng ở tuổi 0;
   - giữ tia lửa và than như hôm nay cho tới khi có CX-F;
   - bỏ hoa sen, chớp điểm lửa, vết cháy code và lửa đất của chính đòn đó.
2. **`?impact=lotus`:** mọi thứ như `main` trước phiếu, cùng lệnh gọi và cùng thứ tự rút số ngẫu nhiên.
3. **Thiếu clip** (không có manifest hay ảnh): đòn tự quay về hoa sen, cảnh báo một lần, đếm `missing`. Lab vẫn chạy.
4. **Manifest của clip** nằm cạnh ảnh, trong thư mục riêng; **Claude ghi**, Codex không đụng `art-src`. Lab của làn khác (đang chạy trên `main`) không bao giờ đọc thư mục đó, nên không nạp thêm 57 MB.
5. **Lab:** đèn tuổi 0 (`FlashLights` có `fresh`), `__lab.fireImpact()`, `__lab.fxSolo()`, và `PLAN=brush` cho kịch bản chụp, để Claude đo các cổng.

## Làm ở đâu
- **Worktree:** `games/.wt-ic-impact-k1`, nhánh `codex/key1-brush-impact`.
  - Claude tạo từ `main` **sau khi gộp 274**: `git -C /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation worktree add ../.wt-ic-impact-k1 -b codex/key1-brush-impact main`.
  - Rồi symlink `node_modules` sang game như phiếu 274. Lúc giao, `git status --short` trong worktree chỉ in `?? node_modules`.
  - cwd là gốc repo cha.
- **`node_modules` là symlink sang game:** không sửa, không cài thêm gói. Mọi thứ ghi vào `node_modules/` là ghi vào game, nên Vitest và Vite chỉ chạy đúng lệnh ở Kiểm 2 và 3.
- **Không ghi gì** trong `games/immortality-cultivation/`, `games/.wt-ic-sound`, `games/.wt-immortality-cultivation-codex`, `games/.wt-ic-flipbook-cool`, và thư mục chụp của chúng (làn khác đang dùng).
- **Mốc test** (Claude điền khi tạo worktree, cùng lệnh ở Kiểm 2): `979` test, `88` tệp (ở `0f4d72c`, sau 269 và 274). Trước 274, ở `35f1b77`, là 960 test.

### Được ghi
- `games/.wt-ic-impact-k1/src/view/skills/element-fire.ts` (mục 2);
- `games/.wt-ic-impact-k1/src/view/skills/element-stage.ts` (mục 3);
- `games/.wt-ic-impact-k1/src/lab/feel.ts`: chỉ lớp `FlashLights` (mục 4);
- `games/.wt-ic-impact-k1/src/lab/skills-main.ts`: chỉ các khối ở mục 5, kể cả các dòng khai trong interface `__lab` và tên thêm vào dòng import `element-fire`;
- `games/.wt-ic-impact-k1/scripts/visual/scenarios/lab-element-fire.mjs` và `lab-element-perf.mjs` (mục 6);
- `games/.wt-ic-impact-k1/tests/view/key1-brush-impact.test.ts` (mới, mục 7);
- `games/.wt-ic-impact-k1/docs/changelog/2026-11-05-key1-brush-impact.md` (mới, mục 8; nếu chạy trong ngày 04/11 thì đổi ngày trong tên);
- `/Volumes/SS990TPRO/htdocs/typing-game/docs/codex-queue/264-report.md`;
- `/Volumes/SS990TPRO/htdocs/typing-game/.local/codex-runs/264-out/` (log lệnh).

### Cấm
- Mọi lệnh git, trừ `status`, `diff`, `log`, `show`, `ls-files`.
- Sửa `flipbook.ts`, `fire-points.ts`, `fxkit.ts`, `embers.ts`, `heat-rings.ts`, `ground-decals.ts`, `sword-skills.ts`, `myriad-swords.ts`, `element-kit.ts`, `element-metal.ts`, `elements.ts`, `src/sim/**`, `src/content/**`, `src/kit/**`.
- Sửa test có sẵn: không đổi số, không đổi câu. Chỉ thêm tệp test mới. `tests/view/element-layer.test.ts` và `tests/view/flipbook-v2.test.ts` phải qua mà không sửa.
- Sửa `FIRE_AURA`, `FIRE_BLADE`, `FIRE_STREAM`, `SCORCH`, `FIRE.flipbooks`, và hành vi của đường `lotus`, của các ô khác (auto, k2, guard, k4, k5) hay của phím 7. Ở những đường đó chỉ được thêm bộ đếm audit của mục 2.
- Sửa bất cứ thứ gì trong `art-src/**` (kể cả mọi manifest) hay `public/**`.
- Cấp phát bộ nhớ mỗi khung hay mỗi đòn: không `new`, không mảng hay đối tượng mới, không closure trong `impact()`, `aftermath()`, `brushHit()`, `brushRotation()`.
- Chạy dev server, mở trình duyệt, mở cổng mạng, tải gói hay ảnh, sinh ảnh.
- Chạy Vitest thiếu `--no-cache --configLoader runner`, hay Vite thiếu `--configLoader runner` và `IC_VITE_CACHE_DIR` (lý do như phiếu 258, Kiểm 2 và 3).

## Việc (lời giải đã chốt)

### 1. Manifest của clip (Claude ghi lúc nhận, Codex không ghi)
- Tệp `games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/manifest.json`, nằm cạnh ba ảnh. Không chép hay liên kết ảnh: `FILE` không nhận "/", và thư mục riêng giữ manifest `fire/` của lab đang chạy y nguyên.
- Kit đọc thư mục này bằng `BRUSH.folder = "fire/impact-k1-r2"`.
- Nội dung chính xác (test ở mục 7.1 chép nguyên văn khối này):

```json
{
  "version": 1,
  "kind": "lab-element-fire-impact",
  "element": "fire",
  "note": "Key 1's Fire hit, version 2 (ticket 264, INTEGRATION_PLAN CX-H): the owner's brushfire clip (04/11/2026 ~22:00). Media, never in Git. Masks are linear data. anchor = the strike root (331, 797) on the 1080 source; heading 81 = the fan's mass (mean hull centroid of the 24 cells seen from the root, y up). Measures: fire-impact-k1-r2-v1a.a4.masks.json, docs/codex-queue/273-report.md, 273b-report.md.",
  "flipbooks": {
    "fire-impact-k1-r2": {
      "file": "fire-impact-k1-r2-v1a.a4.rgba.png",
      "controlA": "fire-impact-k1-r2-v1a.a4.maskA.png",
      "controlB": "fire-impact-k1-r2-v1a.a4.maskB.png",
      "json": "fire-impact-k1-r2-v1a.a4.masks.json",
      "cols": 6,
      "rows": 4,
      "frames": 24,
      "fps": 24,
      "sourceFps": 24,
      "cell": 384,
      "mode": "rgba",
      "alpha": "straight",
      "loop": false,
      "loopMode": "none",
      "timingProfile": "impact-key1",
      "anchor": [0.306481, 0.737963],
      "heading": 81,
      "start": 0,
      "md5": "9c2e2446eaffd655b7424fd2a5798240",
      "roles": ["impact"],
      "use": "Key 1's hit (FireLayers.impact, ?impact=brush): one pass rooted at the strike, turned toward the blow (brushRotation), rampCool 1.",
      "source": "Firefly Video run 2 (seed 947037) f053-f076; masks: tickets 273 and 273b"
    }
  }
}
```

- `md5` là MD5 của atlas màu. Nó thành đuôi `?v=` của cả ba URL. Nếu sau này chỉ một mặt nạ đổi, Claude đặt `md5` bằng MD5 của mặt nạ đó để cả ba URL đổi theo.
- **Lab khi thiếu tệp:** không có `manifest.json` thì dev server trả 404 hay HTML, thư viện bỏ qua im lặng. Thiếu ảnh hay mặt nạ thì thư viện bỏ mục và cảnh báo. Cả hai trường hợp: pool không `ready`, đòn quay về hoa sen (mục 2.3).

### 2. `src/view/skills/element-fire.ts`

#### 2.1 Hằng, cờ lab và audit
```ts
/** Linear gold-white of key 1's hit flash (the fire point's own core colour; a white HDR core read as a white ball). */
const FLASH = lin("#FFE2A0");

/**
 * Key 1's hit, version 2 (ticket 264; INTEGRATION_PLAN CX-H): the owner's brushfire clip (04/11/2026, ~22:00) as a masked
 * one-shot card rooted at the strike, a flash and a light at age 0. TRIAL numbers, tuned in the lab.
 */
export const BRUSH = {
  folder: "fire/impact-k1-r2",
  id: "fire-impact-k1-r2",
  /** Cell height (m) × the blow's s: the fan is about 0.54 × that tall and 0.69 × that wide above the root. */
  size: 3.0,
  /** Share of the turn toward the blow's screen direction the fan takes, and its cap (rad): flames never hang down. */
  follow: 0.6,
  maxTurn: (50 * Math.PI) / 180,
  lift: 0.7,
  softM: 0.2,
  rampCool: 1,
  capacity: 24,
  renderOrder: 12,
  /** The flash at the strike root: m (× s), s, gain on FLASH (HDR, so only its centre reaches the bloom). */
  flash: { size0: 0.6, size1: 0.5, life: 0.07, gain: 2 },
  /** The impact light's intensity; × bigLight on the third, big blow. */
  light: 4,
  bigLight: 1.5,
} as const;

export interface FireAudit {
  brush: number; flash: number; light: number;
  lotus: number; point: number; scorch: number; groundFire: number;
  missing: number;
  /** stage.time at the first and the latest key-1 hit since the last reset (−1: none). */
  firstAt: number; lastAt: number;
}
```
- `FIRE_LAB` thêm hai trường; `riverSheath` giữ nguyên:
  - `impact: "brush" | "lotus"`, mặc định `"brush"`. JSDoc: `?impact=brush|lotus` (ticket 264); `"lotus"` là đòn phím 1 cũ y như trước phiếu.
  - `audit: FireAudit`: mọi số đếm 0, `firstAt` và `lastAt` −1. JSDoc: những gì đòn phím 1 đã vẽ từ lần reset trước; lab đọc qua `__lab.fireImpact`, game không đọc.
- `export function resetFireAudit(): void` đưa `FIRE_LAB.audit` về trạng thái đầu.
- Cảnh báo thiếu clip dùng một cờ cấp module (`let warnedBrush = false`), in **một lần mỗi lần nạp module**:
  ```
  [element-fire] fire-impact-k1-r2 not loaded (art-src/lab/vfx/fire/impact-k1-r2/manifest.json): key 1 hits fall back to the lotus
  ```

#### 2.2 Pool trong `constructor`
- Ngay sau các pool flipbook có sẵn:
  ```ts
  this.brush = P.pool(BRUSH.folder, BRUSH.id, { mode: "rgba", capacity: BRUSH.capacity, renderOrder: BRUSH.renderOrder });
  this.brush.softM = BRUSH.softM;
  this.brush.rampCool = BRUSH.rampCool;
  ```
- **Không** gọi `setSoot`, `setSharpen`, `setGrade`, `setInk`, `setHot`, `setRamp`, `bodyCap`, `hotLead` trên pool này. Bản anh duyệt (xem trước 273b) là `FLIPBOOK_MASKED_LOOK` mặc định. Không thêm pool này vào vòng `setSoot` của bốn pool cũ.
- Sau dòng `const T = stage.textures;`:
  ```ts
  this.flash = stage.pool(16, T.glow, "add", "camera", 14, { crop: 0.6 });
  this.flash.mesh.name = "fx-fire-flash";
  ```
- Khai báo hai trường `private readonly brush: FlipbookPool;` và `private readonly flash: SpritePool;`, kèm JSDoc ngắn.

#### 2.3 `impact()`
Thêm ở đầu hàm, sau `const p`, `const s`. **Phần thân cũ giữ nguyên từng dòng**, chỉ thêm bộ đếm:
```ts
const k1 = a.slot === "k1";
if (k1) {
  if (FIRE_LAB.audit.firstAt < 0) FIRE_LAB.audit.firstAt = this.stage.time;
  FIRE_LAB.audit.lastAt = this.stage.time;
  if (FIRE_LAB.impact === "brush") {
    if (this.brush.ready) {
      this.brushHit(a, s);
      return true;
    }
    FIRE_LAB.audit.missing += 1;
    if (!warnedBrush) { warnedBrush = true; console.warn(/* the line of 2.1 */); }
  }
  FIRE_LAB.audit.lotus += 1;
  FIRE_LAB.audit.point += 1;
}
// … the old body unchanged: point(), lotus(), sparkRays(), emberBurst(), the ember() loop, the accent.
```
Hàm mới:
```ts
/** Key 1's hit, version 2 (ticket 264): the brushfire card, the age-0 flash and light; sparks and embers as before until CX-F. */
private brushHit(a: ImpactArgs, s: number): void {
  const p = a.at;
  const o = flip();
  o.rot = brushRotation(a.dx, a.dz, this.stage.camera.matrixWorldInverse, this.brush.meta!.heading, BRUSH.follow, BRUSH.maxTurn);
  o.ground = 0;
  o.lift = BRUSH.lift;
  this.brush.spawn(v.set(p.x, p.y, p.z), BRUSH.size * s, o);
  const f = this.flash.spec.reset();
  f.x = p.x; f.y = p.y; f.z = p.z;
  f.life = BRUSH.flash.life;
  f.size0 = BRUSH.flash.size0 * s;
  f.size1 = BRUSH.flash.size1 * s;
  f.r = FLASH[0] * BRUSH.flash.gain; f.g = FLASH[1] * BRUSH.flash.gain; f.b = FLASH[2] * BRUSH.flash.gain;
  this.flash.emit();
  this.stage.light(p.x, p.y, p.z, a.pal.flash, BRUSH.light * (a.big ? BRUSH.bigLight : 1));
  // Until CX-F (ticket 262): the spark rays and the thrown embers, exactly as the old hit draws them.
  this.sparkRays(p.x, p.y, p.z, 1.5 * s, 1.35);
  this.emberBurst(p.x, p.y, p.z, 1.1 * s, 1.0);
  const n = this.stage.n(8 + Math.round(6 * a.power));
  for (let i = 0; i < n; i += 1) this.ember(p.x, p.y, p.z, a.dx, a.dz, 7, 1.0);
  if (a.big) this.stage.accent(p.x, p.y, p.z, 0.3);
  FIRE_LAB.audit.brush += 1;
  FIRE_LAB.audit.flash += 1;
  FIRE_LAB.audit.light += 1;
}
```
- **Không đặt** `rate`, `frame`, `until`, `life`, `cool`, `timing`, `variant`, `dir`, `span`, `tint`, `intensity`. Lý do:
  - đời và lịch hiện/xói lấy từ `timingProfile` của manifest;
  - `rate` 1 phát 24 khung ở 24 fps như bản xem trước anh duyệt (vFrame = tuổi × 24);
  - `flip()` không xóa `timing`, `variant`, nên đặt ở đây sẽ rò sang lần spawn khác.
- **Vì sao dùng `rot` tính ở CPU, không dùng `dir`:**
  - `dir` của shader xoay trọn theo hướng đòn, không có hệ số theo và không có trần;
  - pool không có cách soi gương từng sprite: `VERTEX` bị khóa bằng băm của test 258, và một atlas soi gương tốn thêm khoảng 57 MB;
  - giới hạn ±50° giữ cho lửa luôn bốc lên;
  - nếu giám khảo chê đòn bay sang trái thì làm một phiếu sau, thêm soi gương từng sprite trên đường vertex v2.

#### 2.4 `aftermath()` và `burnGround()`
- `burnGround(x, z, r, life, rate, big, fire = true)`: khi `fire` sai thì bỏ hẳn `scorch.spawn` (cả hai lần rút `R.range` của nó) và `groundFire`. `risingEmbers`, các `wisp` và bộ phát giữ nguyên.
- `aftermath()`:
  ```ts
  if (a.slot === "k1" && FIRE_LAB.impact === "brush" && this.brush.ready) {
    // The brushfire burns down to embers on its own (owner 04/11): no code scorch, no ground fire; the wisps and the rising embers stay.
    this.burnGround(a.x, a.z, a.r, a.life, a.rate, false, false);
    return true;
  }
  if (a.slot === "k1") {
    FIRE_LAB.audit.scorch += 1;
    FIRE_LAB.audit.groundFire += 1;
  }
  this.burnGround(a.x, a.z, a.r, a.life, a.rate, false);
  return true;
  ```
- `leadStrike()` gọi `burnGround(..., true)` như cũ.

#### 2.5 `brushRotation` (export, thuần, không cấp phát)
```ts
/**
 * Screen angle (rad) of key 1's brushfire card for a blow along ground direction (dx, dz) (ticket 264): the blow as the
 * camera sees it (`view` = the camera's matrixWorldInverse, its rotation part), the painted fan's `heading` turned
 * `follow` of the way toward it, at most `maxTurn` either way. A blow along the view axis (or none) keeps the painting (0).
 */
export function brushRotation(dx: number, dz: number, view: THREE.Matrix4, heading: number, follow: number, maxTurn: number): number {
  const e = view.elements;
  const x = e[0]! * dx + e[8]! * dz;
  const y = e[1]! * dx + e[9]! * dz;
  if (x * x + y * y < 1e-10) return 0;
  let d = Math.atan2(y, x) - heading;
  d -= Math.PI * 2 * Math.round(d / (Math.PI * 2));
  return Math.max(-maxTurn, Math.min(maxTurn, d * follow));
}
```
- Shader cũ: góc `iData.y` xoay góc ô ngược chiều kim đồng hồ trong hệ nhìn (x phải, y lên). Ô được vẽ với ảnh hướng lên trên, `uPivot.y = 1 − anchor[1]`. Nên hướng quạt trên màn là `heading + rot`.
- Đúng ý định: đòn bay lên màn hình (thường gặp nhất, thú ở phía trước) thì xoay khoảng 5°, gần như hình anh đã duyệt.
- Ba r170 cập nhật `camera.matrixWorldInverse` trong `render()` (`three.module.js` dòng 30015, 12610). Lúc gọi hook nó là ma trận của khung trước, đủ dùng.

#### 2.6 `reset()` và chú thích
- `reset()` gọi `resetFireAudit()`. Chuỗi gọi: `__lab.reset()` → `fx.reset()` → hook `reset`.
- Khối JSDoc đầu tệp: gạch "impact" thêm một câu tiếng Anh:
  - key 1's hit, version 2: the brushfire card (masked flipbook, its own folder), a flash and a light at age 0, sparks and embers kept;
  - no lotus, fire point, code scorch or ground fire on that blow;
  - `FIRE_LAB.impact = "lotus"` puts the old hit back.
- **Không** thêm id vào `FIRE.flipbooks`. `ElementStage.prepare` chỉ đọc thư mục `fire`, nên nếu thêm sẽ cảnh báo sai.

### 3. `src/view/skills/element-stage.ts`
- `ElementStageOptions` thêm:
  ```ts
  /**
   * A kit's impact light (ticket 264): at (x, y, z), `colour` (CSS hex), `intensity`, at full strength on the frame it is
   * asked (the host's point-light pool; the lab: FlashLights, drawn before it ages). Absent: none.
   */
  readonly light?: (x: number, y: number, z: number, colour: string, intensity: number) => void;
  ```
- Trường riêng `onLight` (như `onAccent`) và phương thức:
  ```ts
  /** A kit's impact light at (x, y, z) (the host's, when it gave one). */
  light(x: number, y: number, z: number, colour: string, intensity: number): void {
    this.onLight?.(x, y, z, colour, intensity);
  }
  ```
- Không đổi gì khác. Không thêm đăng ký pool: `FlipbookPlayer.pool` đã đăng ký, cập nhật và dọn pool của kit.

### 4. `src/lab/feel.ts`: `FlashLights`
- `flash(at, camera, colour, intensity, fresh = false)`. Khi `fresh` đúng, đánh dấu đèn được chọn, cả khi dùng lại một đèn còn sáng ở gần.
- `update(dt)`: đèn đang đánh dấu thì bỏ một lần giảm (xóa dấu, giữ cường độ), các đèn khác giảm như cũ.
- `reset()` xóa mọi dấu.
- JSDoc: `fresh` là đèn được vẽ đủ sáng ở khung nó được gọi (`VFX_STANDARD.md` §3.1 luật 5). Lần `update` đầu không làm nó già đi. Người gọi cũ giữ `false`, nên không đổi gì.
- Thêm `levels(): number[]`, trả cường độ từng đèn theo thứ tự tạo. Chỉ lab gọi; được phép cấp phát.
- Mảng dấu dựng một lần trong `constructor`.

### 5. `src/lab/skills-main.ts`
1. **Cờ.** Ngay sau dòng `FIRE_LAB.riverSheath = …`:
   ```ts
   // INTEGRATION_PLAN CX-H (ticket 264): ?impact=lotus puts key 1's old Fire hit back (the lotus, the fire point, the code
   // scorch and the ground fire); the default is the brushfire card.
   const IMPACT = params.get("impact");
   FIRE_LAB.impact = IMPACT === "lotus" ? "lotus" : "brush";
   if (IMPACT !== null && IMPACT !== "lotus" && IMPACT !== "brush") console.warn(`[lab] ?impact=${IMPACT}: brush or lotus; brush is used`);
   ```
2. **Đèn.** Khai `const lightAt = new THREE.Vector3();` ngay trước `new ElementStage(…)`. Thêm vào options:
   ```ts
   light: (x, y, z, colour, intensity) => lights.flash(lightAt.set(x, y, z), view.camera.position, colour, intensity, true)
   ```
3. **Đồng hồ.** Biến cấp module `let lastWorldDt = 0;`, gán `lastWorldDt = world;` ngay sau dòng `const world = cutin.active ? 0 : screen.advance(dt);`.
4. **`__lab.fireImpact(mode?)`** (interface có JSDoc):
   - có `mode` thì đặt `FIRE_LAB.impact`;
   - trả `{ mode, ready, audit, ageTicks, lights }`, trong đó:
     - `ready = stage.flipbooks.loaded(BRUSH.folder).includes(BRUSH.id)`;
     - `audit` là bản sao `{ ...FIRE_LAB.audit }`;
     - `ageTicks = audit.firstAt < 0 ? -1 : Math.round((stage.time - audit.firstAt - lastWorldDt) * 60)`;
     - `lights = lights.levels()`.
   - Vì sao công thức `ageTicks` đúng: thẻ sinh trong khung N lúc `stage.time = firstAt`, được vẽ ở tuổi 0 rồi già thêm `world` của khung N. Ở khung N + k, tuổi lúc vẽ bằng tổng `world` của các khung N … N + k − 1, tức `stage.time − firstAt − world(N + k)`. Dừng hình (`world` = 0) không làm thẻ già đi.
5. **`__lab.fxSolo(prefix: string | null): number`** (interface có JSDoc):
   - Duyệt `view.layers.fx`. Với mọi đối tượng có `geometry` (lưới), lần đầu thì ghi `visible` gốc vào `const soloShown = new Map<THREE.Object3D, boolean>()`, rồi đặt `visible = name !== "" && name.startsWith(prefix) && <visible gốc>`.
   - Nhóm và đèn không đổi.
   - `null`: trả mọi `visible` gốc rồi xóa map.
   - Cuối cùng `view.render(0)` (không trôi thời gian), trả số lưới đang hiện.
   - Không dùng chung map `fxShown` của `debugShow`. Không đổi `fxShowNamed` hay `debugShow`.
6. Thêm `BRUSH` vào dòng import từ `../view/skills/element-fire`.

### 6. Kịch bản chụp
**`scripts/visual/scenarios/lab-element-fire.mjs`**
- **`PLAN=brush`:**
  ```js
  /** PLAN=brush (ticket 264): key 1's first hit at the brush's own ages (hit-stop frames do not age it; past ~26 the second blow lands). */
  const BRUSH_AGES = [0, 1, 2, 3, 4, 6, 9, 12, 15, 18, 21, 24];
  const BRUSH_PLAN = [
    ["k1b", "k1", "close:-0.3,-5.6,10", false, "age", BRUSH_AGES],
    ["k1bp", "k1", "play", false, "age", BRUSH_AGES],
  ];
  ```
- **`hitAt === "age"`:**
  - sau `type`, bước một khung một lần tới khi `__lab.fireImpact().ageTicks >= 0`. Tối đa 120 khung, quá thì ném `no key-1 hit`;
  - với mỗi tuổi a: bước một khung một lần tới khi `ageTicks >= a`, tối đa 60 khung;
  - tên tệp `<id>-a<aa>.png` (hai chữ số);
  - JSON của khung ghi `age` (tuổi thật đọc được).
- **Mọi khung, mọi PLAN:** JSON thêm `fire` (`__lab.fireImpact()` nếu có, không thì `null`) và `named` (`__lab.fxNamed()`).
- **`LAYERS=<danh sách>`:** các mục `brush`, `flash`, `lotus`, `point`, ứng với tiền tố `flipbook-fire-impact-k1-r2`, `fx-fire-flash`, `flipbook-fire-burst`, `fx-fire-points`. Sau ảnh chính (và ảnh `WORLD`):
  - với mỗi mục: `fxSolo(tiền tố)` rồi chụp `<tên>-<mục>.png`;
  - rồi `fxSolo("-none-")`, chụp `<tên>-base.png`;
  - cuối cùng `fxSolo(null)`.
- **`SCREEN=0`:** sau mỗi `__lab.reset()` gọi `__lab.post({ screen: false })`. JSON đầu ra ghi `screen: false`.
- **Chờ clip:** với `PLAN=brush`, `ELEMENT` là `fire` và `QS` không chứa `impact=lotus`: sau khi trang sẵn sàng, chờ `fireImpact().ready` tối đa 20 s. Không có thì ném `brushfire clip not loaded (art-src/lab/vfx/fire/impact-k1-r2/manifest.json)`.
- Chú thích đầu tệp: thêm dòng chạy `PLAN=brush` với `LAYERS`, `SCREEN`.
- Các PLAN cũ chụp như trước. Chỉ JSON có thêm hai trường `fire` và `named`.

**`scripts/visual/scenarios/lab-element-perf.mjs`**
- `ELEMENT=fire` và `QS` không chứa `impact=lotus`: sau `sleep(1500)`, chờ `fireImpact().ready` tối đa 20 s, không ném lỗi.
- Đối tượng JSON ghi thêm `impact` (`fireImpact().mode`, hay `null`) và `brushReady`.

### 7. Test mới `tests/view/key1-brush-impact.test.ts`
Không đọc tệp ảnh. Sai số 1e-9 trừ khi ghi khác. Helper tự viết trong tệp, chép theo `element-layer.test.ts`:
- `camera()`: `PerspectiveCamera(28, 16/9, 0.1, 300)`, vị trí (0, 26, 14), `lookAt(0, 0, -6)`, `updateMatrixWorld(true)`;
- `sheets()`;
- `swordHost`: caster ở (0, 3) nhìn (0, −1);
- `field(3)`: thú x = −4 + 1,2i, z = −6, `midY` 0,5, **không giết**;
- stage: `new ElementStage({ …, vfxBase: "/v/", light: (x, y, z, c, k) => lights.push([c, k]) })`.

**Cách chạy một lượt** (dùng cho 3–5). Mỗi lượt dựng mới `camera()`, `sheets()`, `field(3)`, mảng `lights`, `ElementStage` và `SwordSkillFx` (không dùng lại giữa các lượt: clip đã `add` và hai luồng ngẫu nhiên phải bắt đầu lại):
1. `resetFireAudit()`, đặt `FIRE_LAB.impact`;
2. `fx.setElement(elementById("fire")!, stage)`;
3. nếu "có clip": `stage.flipbooks.library(BRUSH.folder).add(meta, new THREE.Texture(), { a: new THREE.Texture(), b: new THREE.Texture() })`, với `meta` lấy từ manifest của 7.1;
4. spy (`vi.spyOn`, trả lại ở `finally`):
   - `FlipbookPool.prototype.spawn`: thay bằng hàm ghi `{ id, at: at.clone(), size, o: { ...o } }` (chép `at`: kit dùng lại một `Vector3` cấp module `v` cho mọi spawn, ghi tham chiếu thì mọi bản ghi mang giá trị cuối);
   - `GroundDecalPool.prototype.spawn`: ghi đối số;
   - `FirePointPool.prototype.emit`, `EmberPool.prototype.emit`, `SpritePool.prototype.emit`: gọi tiếp hàm gốc, đếm theo `this.mesh.name` (tên rỗng thì theo `renderOrder`);
5. `fx.cast("k1", 0, -6)`, rồi 120 khung `stage.begin(); fx.update(1/60); stage.update(1/60);`.

Với lưới này đích là thú 2 (x −1,6), đòn xuyên vào thú 1: 3 đòn chính (scale 1,05, kiếm thứ ba `big`) và 3 đòn xuyên (scale 0,8).

1. **Manifest.** Chép nguyên văn JSON của mục 1 vào test, parse với base `/art-src/lab/vfx/fire/impact-k1-r2/`. Kiểm:
   - `isFlipbookV2` đúng;
   - `url` = base + `fire-impact-k1-r2-v1a.a4.rgba.png?v=9c2e2446eaffd655b7424fd2a5798240`; `controlA`, `controlB` cùng dạng;
   - cols 6, rows 4, frames 24, fps 24, `sourceFps` 24, `aspect` 1, mode `rgba`, `loop` sai, `loopMode` `none`, `timingProfile` `impact-key1`;
   - `pivot` và `anchor` = [0.306481, 0.737963];
   - `heading` = 81·π/180;
   - `playLife(meta, {})` = 43/60.
2. **`brushRotation`** với camera trên, `heading` 81°, `follow` 0,6, `maxTurn` 50° (đáp số theo độ, so bằng radian):

   | (dx, dz) | Đáp số |
   |---|---|
   | (0, −1) | +5,4° |
   | (1, 0) | −48,6° |
   | (−1, 0) | +50° (chạm trần) |
   | (0, 1) | −50° |
   | (0, 0) | 0 |
3. **Chế độ `brush`, có clip.**
   - 6 spawn `fire-impact-k1-r2`; `size` sắp xếp = [2.4, 2.4, 2.4, 3.15, 3.15, 4.095];
   - mỗi spawn: `at.y` 0,5; `o.ground` 0; `o.lift` 0,7; |`o.rot`| ≤ 50° + 1e-12;
   - `o.rate`, `frame`, `until`, `life`, `cool`, `timing`, `variant`, `dir`, `slowFrom` đều `undefined`;
   - không spawn `fire-burst` nào có `rate` 1,25; đúng một `fire-burst` `rate` 1,3 (phát) và hai `rate` 1,6 (phóng kiếm 2, 3);
   - 0 spawn `fire-ground`, 0 lần `GroundDecalPool.spawn`;
   - `emit` của `fx-fire-flash`: 6;
   - đèn: 6 lần, năm lần cường độ 4 và một lần 6, màu là chuỗi;
   - `FIRE_LAB.audit`: `brush` 6, `flash` 6, `light` 6, `lotus` 0, `point` 0, `scorch` 0, `groundFire` 0, `missing` 0, `firstAt` ≥ 0, `lastAt` ≥ `firstAt`;
   - uniform của pool `flipbook-fire-impact-k1-r2`: `uRampCool` 1, `uSoftM` 0,2; pool `flipbook-fire-burst`: `uRampCool` 0.
4. **`lotus` y như cũ.** Lượt A: `FIRE_LAB.impact = "lotus"`, có clip. Lượt B: `"brush"`, **không** có clip (quay về). Mọi bản ghi của A và B bằng nhau (`toEqual`): danh sách spawn flipbook, đối số decal, các bộ đếm `emit`, danh sách đèn (rỗng). Riêng A:
   - 0 spawn `fire-impact-k1-r2`, 0 `emit` `fx-fire-flash`, 0 đèn;
   - 6 spawn `fire-burst` `rate` 1,25, 3 `fire-ground`, 3 decal;
   - audit `lotus` 6, `point` 6, `scorch` 3, `groundFire` 3, `missing` 0.

   B giống A, trừ `missing` 6.
5. **Phần giữ lại không đổi.**
   - Số spawn `fire-sparks` và số `emit` của `EmberPool` ở lượt 3 bằng lượt A của 4;
   - số `FirePointPool.emit` ở lượt 3 bằng lượt A trừ 6.
6. **`FlashLights`.** `new FlashLights(new THREE.Group(), 2)`:
   - `flash((0, 1, 0), camPos (0, 5, 10), "#ffaa55", 4, true)`, `update(1/60)`: `levels()` có đúng 4; `update(1/60)` lần nữa: 4·e^(−7/60);
   - `flash((10, 1, 0), camPos, "#ffaa55", 4)` (không `fresh`, chọn đèn kia), `update(1/60)`: đèn đó 4·e^(−7/60);
   - `flash((0, 1, 0), camPos, "#ffaa55", 4, true)` (đánh dấu), rồi `reset()`, rồi `flash((0, 1, 0), camPos, "#ffaa55", 4)` không `fresh`, `update(1/60)`: đèn đó 4·e^(−7/60) (dấu cũ đã xóa).

### 8. Changelog
`docs/changelog/2026-11-05-key1-brush-impact.md` (tiếng Việt). Ghi:
- làm gì và vì sao (anh duyệt clip; bỏ hoa sen, chớp điểm, vết cháy code, lửa đất của đòn phím 1);
- các số TRIAL của `BRUSH`;
- cờ `?impact`, `__lab.fireImpact`, `__lab.fxSolo`, `PLAN=brush`, `LAYERS`, `SCREEN`;
- test mới;
- "manifest của clip do Claude ghi ở `art-src`; thiếu thì đòn quay về hoa sen".

## Kiểm bắt buộc (trong `games/.wt-ic-impact-k1`; ghi lệnh và kết quả vào báo cáo)
1. `node node_modules/typescript/bin/tsc --noEmit -p .`: không lỗi.
2. `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`: mọi test qua.
   - Trước = mốc Claude ghi ở "Làm ở đâu". Sau = mốc + số test của `key1-brush-impact.test.ts`, thêm một tệp.
   - `element-layer.test.ts` và `flipbook-v2.test.ts` qua mà không sửa.
3. **Build tạm:**
   - xóa `/private/tmp/codex-264-dist` nếu còn;
   - `IC_VITE_CACHE_DIR=/private/tmp/codex-264-dist/.vite-cache node node_modules/vite/bin/vite.js build --outDir /private/tmp/codex-264-dist --configLoader runner`: thoát 0;
   - `grep -rl "fire-impact-k1-r2\|fx-fire-flash\|fxSolo" /private/tmp/codex-264-dist` **không in đường dẫn nào** (thoát 1 là đúng), vì kit Fire và lab không lọt vào bản dựng;
   - xóa `/private/tmp/codex-264-dist`.
4. `node --check scripts/visual/scenarios/lab-element-fire.mjs` và `node --check scripts/visual/scenarios/lab-element-perf.mjs`: thoát 0.
5. Trong worktree: `git diff --stat` và `git status --short`. Chỉ các tệp được ghi, cộng `?? node_modules` (symlink, như báo cáo 258). Báo cáo nằm ở repo cha nên không hiện ở đây.

## Claude làm sau (trình duyệt; không phải việc của Codex)

**Trước khi giao**
1. Gộp 274, kiểm `FlipbookPool` có setter `rampCool`.
2. Tạo worktree, điền mốc test.
3. Có một PASS phản biện (luật làm gọn 05/11).

**Khi nhận**
1. **Đọc diff, chạy lại Kiểm 1–5.**
   - Đường `lotus` trong `impact()` và `burnGround(…, true)` phải giữ nguyên từng dòng, chỉ thêm bộ đếm.
   - 269 (âm thanh) đã gộp trong `0f4d72c`, nền của worktree: không còn chồng chéo phải xem ở `skills-main.ts` và `feel.ts`; chỉ xem lại nếu `main` có commit mới trước khi gộp.
2. **Ghi manifest** của mục 1.
   - Kiểm lại ba MD5; khác bảng thì dừng và xem lại `anchor`, `heading`.
   - Symlink `art-src` vào worktree để chạy lab (không gộp symlink).
   - Chạy bản cố định không HMR qua `.local/bin/heavy.sh --gpu`, High, DPR 1, `fixed=1`.
   - Console không có lỗi shader, và không có dòng `[element-fire] … not loaded`.
3. **Đo cổng.** Ảnh và JSON vào `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/impact-k1-v2/` (có `ABOUT.md`, chạy `node scripts/review-index.mjs`). Y tuyến tính là Rec. 709 giải mã từ PNG sRGB. "Ba nền" là sân mặc định, đá sáng `#d6d0c2` (`GROUND=`), đá tối `#2a2c30`. "Hai camera" là `k1b` (cận) và `k1bp` (chơi).

   | Cổng (§2.8, §2.9) | Ngưỡng | Claude đo thế nào |
   |---|---|---|
   | Khung đầu: chớp | ≥ 0,95 (REQUIRED) | `PLAN=brush LAYERS=flash SCREEN=0 WORLD=0`, ba nền, hai camera. E(tuổi) = Σ max(0, Y(`-flash`) − Y(`-base`)) trên cả khung. Tỉ số E(0) / max E(0…12). Cách A1, chỉ lấy phần sáng thêm. |
   | Khung đầu: đèn | ≥ 0,95 | `fire.lights` trong JSON: ở tuổi 0, đèn sáng nhất ≥ 0,95 × cường độ đặt (4; đòn lớn 6), và không nhỏ hơn đèn đó ở mọi tuổi sau. |
   | Trắng xóa | ≤ 6 % cả khung, mọi khung | Khung chính (pass màn hình bật) của `PLAN=brush` và `PLAN=linger`, 1920 × 1080, ba nền. Tỉ lệ điểm ảnh có luma mã hóa 0,2126 R′ + 0,7152 G′ + 0,0722 B′ ≥ 0,95. Ghi riêng tỉ lệ trong vết của thẻ (điểm ảnh `-brush` khác `-base`) để chẩn đoán. |
   | Thân sáng ở tuổi 18 | ≤ 15 % đỉnh (TRIAL) | `LAYERS=brush SCREEN=0`: E_brush(18) / max E_brush(0…24), E như hàng 1, ba nền, hai camera. Ghi thêm để chẩn đoán: diện tích ΔE OKLab > 0,12 (cách A1) và diện tích "Y > 0,1 và sáng hơn base" (cách 273b). |
   | Fire hơn Metal | ≤ 0,85 ms p95 ở cửa sổ phím 1; mọi cửa sổ ≤ 11,5 ms | `lab-element-perf.mjs`, `RUNS=3`, thứ tự Metal, Fire, Fire, Metal, qua `.local/bin/heavy.sh --perf`, 1920 × 1080, cùng hào quang mặc định. JSON phải có `brushReady: true`. Ghi thêm Fire với `QS=&impact=lotus`. Chênh dưới khoảng 0,7 ms là trong nhiễu (A1). |
   | Không lớp cũ nào vẽ ngầm | 0 | (a) Sau một lần phím 1 ở `brush`, `fireImpact().audit` có `lotus = point = scorch = groundFire = missing = 0` và `brush = flash = light` = số đòn phím 1 (chính và xuyên). (b) `named` của mọi khung `PLAN=brush` và một lượt `PLAN=linger ONLY=k1h,k1hp` (mục `k7f` của linger vẽ vết cháy và lửa đất của phím 7, đúng thiết kế): không có `ground-decals` hay `flipbook-fire-ground`. Số instance `flipbook-fire-burst` và `fx-fire-points` bằng lượt `QS=&impact=lotus` trước đòn đầu, không lớn hơn ở mọi khung, và nhỏ hơn hẳn ở những khung mà hoa sen hay chớp điểm của đòn còn sống trong lượt lotus. |
   | Biên dịch lần đầu | ≤ 11,5 ms | Trang mới, không làm ấm: `perf()` quanh khung trúng đầu tiên của phím 1. Vượt thì mở phiếu nhỏ làm ấm chương trình v2 lúc nạp. |

4. **Chụp để xem và chấm.**
   - `PLAN=brush` và `PLAN=linger`, ở `--width=1280 --height=720` và `--width=1920 --height=1080`, DPR 1;
   - camera cận (`k1b`) và zoom cận của người chơi (`zoom(1)`, mục `k1z`);
   - ba nền; `brush` và `QS=&impact=lotus`;
   - tấm so tuổi 0, 1, 2, 3, 6, 9, 12, 18, 24.

   Chỉnh các số TRIAL của `BRUSH` (cỡ 2,4–3,6 m, `follow`, `maxTurn`, chớp, đèn) bằng mắt nếu cần, ghi lý do. Xong thì xóa khung thô của mình bằng `node tools/capture-prune/prune.mjs <thư mục> --apply` (chạy thử không `--apply` trước).
5. **Video cho anh** (MP4 < 30 MB, chữ trên video tiếng Anh):
   - camera chơi 1920 × 1080 ở tốc độ thật rồi 0,25×, rồi zoom cận, đá sáng rồi đá tối;
   - dựng từ khung bước cố định 60 Hz bằng ffmpeg như các video lab trước;
   - lưu ở `owner-review/<ngày>/tu-tien/impact-k1/` (có `ABOUT.md`, chạy `review-index`), gửi anh bằng `SendUserFile`.
6. **Chấm và gộp.**
   - Hai giám khảo mù chấm trên bản cố định ở camera chơi, không cờ URL (§2.10). Món ≥ 7 thì gửi anh demo và làm tiếp; đạt khi cả hai ≥ 8,5 và mọi cổng số qua.
   - Gộp vào `main` khi Kiểm và các cổng số qua. Anh chê thì chỉnh hằng `BRUSH` ở phiếu sau. `?impact=lotus` ở lại để so.

## Hết hạn mức
Giữ mọi file, viết báo cáo phần đã xong. Dòng cuối của tin nhắn cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).

## Nhận
- Thay đổi nằm trong worktree, chưa commit. Claude đọc diff, chạy lại Kiểm 1–5, rồi làm phần "Claude làm sau".
- Báo cáo ghi:
  - từng mục 2–8 đã làm ở tệp và hàm nào;
  - chỗ phải làm khác và vì sao;
  - kết quả Kiểm 1–5, số test trước và sau.
- Báo cáo không tuyên bố nghiệm thu hình: phiếu không chạy trình duyệt.

## Ngoài phạm vi
- Đòn tự động (`auto`) và các ô khác vẫn dùng hoa sen. Chỉ đòn phím 1 đổi, đúng gói CX-H.
- Tia lửa, sao đòn, bụi vẽ tay (CX-F, phiếu 262); vòng ấn vẽ tay (CX-I, 265); nhịp +18 của đòn đầu (CX-J, 266).
- Soi gương từng sprite cho đòn bay sang trái; làm ấm chương trình v2 lúc nạp. Chỉ làm khi phép đo hay giám khảo cần.
- Vòng áp lực ở tay và ấn dưới chân lúc phát chiêu (pha phát, không phải đòn).
- Đưa kit Fire vào bản dựng của game (`art-src` → `public`).

## Phản biện
### Lượt 1 · 05/11 01:51 · agent phản biện Claude độc lập · **PASS** (sau 4 sửa nhỏ ghi dưới, đã sửa thẳng trong phiếu)

**Cách kiểm.** Đọc mã ở worktree `games/.wt-ic-impact-k1` (HEAD `0f4d72c`, `git status` chỉ `?? node_modules`). Không chạy game, build hay test.
- `element-fire.ts`: `impact()` 760–772, `aftermath()` 807–810, `burnGround()` 507–530, `FIRE_LAB` 93, `flip()` 166 đúng số dòng. `flip()` không xóa `timing`, `variant`; không chỗ nào trong kit đặt hai trường đó. Không trùng tên `BRUSH`, `FLASH`, `brush`, `flash`.
- `flipbook.ts`: setter `rampCool` (1168) và `softM` (1173) có. `meta` public, `ready` = `meta !== null`. `pool()` gọi `library()` rồi `load()`; trong Vitest (`environment: "node"`, không `location`) `load()` trả ngay, nên pool chỉ `ready` khi test `add` clip. `FILE` và `ID` nhận đúng tên tệp và id. Manifest mục 1 parse ra đúng: `md5` làm đuôi `?v=` cho cả ba URL, `anchor` thành `pivot`, `heading` 81·π/180, `playLife` = 43/60.
- Shader: góc `iData.y` xoay CCW trong hệ nhìn, `uHeading` chỉ dùng khi có `dir`. Vertex v2 không đổi phần này, nên hướng quạt trên màn = `heading + rot`.
- Bảng 7.2: tự tính với camera (0, 26, 14) nhìn (0, 0, −6): y = −0,7926·dz, x = dx. Ra +5,4°, −48,6°, +50°, −50°, 0, khớp.
- Lượt test: `castK1` chọn thú gần caster nhất (thú 2, x −1,6), xuyên vào thú 1. Phát: một `fire-burst` `rate` 1,3 (tier 2, không `big`, không vết cháy ở `release`). Hai lần `launch` (1,6). Ba đòn chính (1,05; kiếm thứ ba `big`) cộng ba đòn xuyên (0,8). Kích thước 2,4 / 3,15 / 4,095 đúng. Host của test có `hitStop` rỗng, nên 120 khung đủ. `palSlot` = `f.slot` = `"k1"` ở cả `impact` lẫn `aftermath`.
- A/B bằng nhau và mục 7.5: `point()` và `lotus()` không rút số ngẫu nhiên. Đường brush rút đúng cùng chuỗi `sparkRays`, `emberBurst`, `ember`. Số `EmberPool.emit` không phụ thuộc số ngẫu nhiên.
- Lab: `lights` dựng ở dòng 426, trước `stage` ở 819. `flash()` của kit chạy trong `fx.update`, `lights.update(dt)` ở 1311 trước `render`. `stage.update(world)` cộng `stage.time`, nên công thức `ageTicks` đúng. `fx.reset()` gọi hook `reset` (sword-skills 1013).
- Không có `params.get("impact")`, `fxSolo`, `fireImpact` sẵn. `feel.ts` chỉ import `three`, nên test node nạp được.
- Bản dựng: không tệp nào ngoài `src/lab` và `src/view/skills` import `view/skills/*`, nên grep của Kiểm 3 trống. Lệnh Vite của Kiểm 3 không có `--no-cache` (cờ làm 274 phải dùng bộ chuyển tiếp).
- Mốc: 88 tệp test, khớp. 979 = 964 (274) + 15 (269), khớp.

**Lỗi đã sửa thẳng trong phiếu**
1. **Mục 7, bước 4 của "Cách chạy một lượt" (lỗi làm test hỏng).** Spy ghi `at` theo tham chiếu. Kit dùng lại `const v` cấp module (`element-fire.ts:158`) cho mọi `spawn`, nên mọi bản ghi mang giá trị cuối: kiểm `at.y` 0,5 ở 7.3 sai, và phép so A/B ở 7.4 so một đối tượng với chính nó. Đã sửa thành `at: at.clone()`.
2. **Mục 7, "Cách chạy một lượt" (mơ hồ).** Phiếu không nói mỗi lượt dựng mới stage và fx. Nếu dùng lại, lượt B mang clip của A và hai luồng ngẫu nhiên lệch, nên 7.4 hỏng. Đã thêm câu: mỗi lượt dựng mới `camera`, `sheets`, `field`, `lights`, `ElementStage` và `SwordSkillFx`.
3. **Mục 7.6, gạch cuối.** Ca `reset()` không kiểm gì: trước `reset()` không còn dấu nào, vì `update` đầu đã xóa dấu. Đã đổi thành: `flash(…, true)`, `reset()`, rồi `flash` không `fresh` và `update`, ra 4·e^(−7/60).
4. **"Claude làm sau", cổng "Không lớp cũ nào vẽ ngầm" (b).** `PLAN=linger` có mục `k7f`, mà phím 7 vẽ vết cháy và lửa đất đúng thiết kế (`finisher`, `leadStrike`), nên cổng sẽ trượt sai. Đã giới hạn ở `ONLY=k1h,k1hp`.

Thêm: tiêu đề "Mã hiện tại" ghi rõ số dòng đã kiểm ở `0f4d72c`. Câu "xem chồng chéo với 269" đã sửa, vì 269 đã gộp trong nền.

**Ghi chú, không chặn**
- `SpritePool.update` tăng tuổi trước khi ghi (`fxkit.ts:451`). Vì vậy `fx-fire-flash` được vẽ lần đầu ở tuổi `world` của khung trúng (≈ 0,24 đời 0,07 s), không ở tuổi 0. Cổng chớp tính tỉ số E(0) / max E(0…12), nên vẫn qua: khung đầu là khung sáng nhất. Nếu giám khảo thấy chớp yếu, chỉnh `BRUSH.flash.life` hoặc `gain`, không cần sửa mã pool.
- Phiếu đi trước CX-G (kế hoạch §3 xếp CX-G trước CX-H, và `skills-main.ts` "chỉ CX-G") và chỉ lấy cờ `?impact`. Lệch này đã ghi ở mục Nguồn; Claude chốt.
