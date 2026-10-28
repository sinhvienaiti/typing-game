# Phiếu 037 · Chung · Công cụ `tools/vfx-sheet`: số đo VFX trên chuỗi khung và tờ khung cạnh ảnh tham chiếu (chỉ mã, không trình duyệt)

**Bối cảnh:** chủ dự án duyệt chuẩn VFX nhiều lớp ngày 28/10/2026: [`docs/games/VFX_STANDARD.md`](../games/VFX_STANDARD.md). Ba game sẽ được chấm VFX trên **tờ khung** đặt cạnh ảnh tham chiếu của chủ dự án (§4.5, §5.3), bằng các số đo ở §5.6:
- khung đầu của lóe và đèn ≥ 95 % đỉnh;
- trắng xóa ≤ 6 % vùng sân (chiêu cuối ≤ 15 % trong tối đa 3 khung);
- tương phản thẻ chữ ≥ 7 : 1 ở p99;
- độ bão hòa ở thân hiệu ứng.

Hôm nay mỗi kịch bản tự ghép tờ khung bằng `magick montage` và tự đo theo cách riêng. Phiếu này viết một công cụ Node dùng chung ở repo cha, có test trên ảnh tổng hợp với đáp án biết trước.

**Ba quy ước đã có trong các game** (công cụ dùng đúng như vậy):
- **luma** là `0.2126·R + 0.7152·G + 0.0722·B` trên giá trị sRGB đã mã hóa (0–255), chia 255. Đây là trọng số của `magick -grayscale Rec709Luma` mà `survival-feel.mjs` dùng cho "vết trắng ≥ 0,95" và "sáng lên ≥ 0,25"; công cụ không làm tròn về 8 bit như nó.
- **Độ chói tương đối** theo WCAG: `lin(c) = c ≤ 0.04045 ? c/12.92 : ((c+0.055)/1.055)^2.4`, `L = 0.2126·lin(R) + 0.7152·lin(G) + 0.0722·lin(B)`. Tương phản là `(Lsáng + 0.05)/(Ltối + 0.05)`. Chữ HUD của Tuyến Cuối là `#f4f1eb` (`contrast.mjs` của study C).
- **`meta.json`** của kịch bản có `rows: [{ file, f, ms, … }]`, ví dụ `games/typing-survival/tmp/mac-2026-10-27/feel-n4n6/round2/suite3/1280x720/meta-f5-xung-1280x720.json`. Dòng `f = −1` là khung ngay trước phím.

**Vì sao đặt ở `tools/` của repo cha** (§4.5): thêm file vào module `tools` của kit thì `kit:check` của các game sẽ đỏ.

**Thư mục làm việc:** worktree của repo cha `/Users/toandx/htdocs/typing-game-wt/vfx` (nhánh `vfx`, tách từ `feat/space-typing-admin-uiux`), do điều phối viên tạo trước khi chạy. Codex chạy với cwd `.` là worktree đó; mọi đường dẫn tương đối tính từ đây.
- **Vì sao không tách từ `main`** như `VFX_STANDARD.md` §5.4 ghi cho làn V1: `main` của repo cha (`dfccf7b9`, 08/10) không là tổ tiên của nhánh đang làm, chậm 1.092 commit, và không có `tools/codex-run`, `docs/codex-queue`. Điều phối viên chọn `feat/space-typing-admin-uiux` (28/10).
- **Một mình trong worktree:** trong lúc phiếu chạy, không agent nào khác ghi vào worktree này. Làn V1 của Claude chỉ bắt đầu ở đây sau khi Claude commit kết quả phiếu.
- Bản checkout chính `/Users/toandx/htdocs/typing-game` chỉ được **đọc**, và chỉ đọc các file sau:
  - hai đầu vào của lượt chạy thử ở Kiểm 6 (`META`, `REF`) và 25 ảnh khung mà `META` trỏ tới;
  - ảnh đo tốc độ ở Kiểm 7: `/Users/toandx/htdocs/typing-game/games/typing-survival/tmp/mac-2026-10-27/feel-n4n6/round2/suite3/1920x1080/c1-s1-1920x1080-burst-00.png`.
- Các thư mục `games/*` trong worktree là submodule chưa khởi tạo: không dùng, không gọi git trong đó.
- Worktree có thể có file chưa commit từ trước: không sửa, không xóa.
- Trước khi ghi gì, chạy `git status --short --untracked-files=all` và giữ kết quả cho Kiểm 8.
- **`sharp` không có;** không cài gì. Đọc PNG bằng mã thuần (zlib của Node). Các dạng ảnh khác (JPEG, WebP, PNG 16 bit hay xen dòng) chuyển qua ImageMagick: `/opt/homebrew/bin/magick` (bản 7.1.2), gọi bằng `execFileSync` với mảng tham số, không qua shell. Biến `MAGICK` thay được đường dẫn này.
- Phông cho nhãn: `/System/Library/Fonts/Supplemental/Arial.ttf`. Biến `VFX_SHEET_FONT` thay được.

**Chỉ được ghi:**
- `tools/vfx-sheet/README.md`: tiếng Việt có dấu; cách dùng, định nghĩa từng số đo, dạng mặt nạ, dạng `meta.json`, mã thoát;
- `tools/vfx-sheet/cli.mjs`;
- `tools/vfx-sheet/lib/png.mjs`, `lib/image.mjs`, `lib/measure.mjs`, `lib/sheet.mjs`;
- `tools/vfx-sheet/test/png.test.mjs`, `measure.test.mjs`, `sheet.test.mjs`, `cli.test.mjs`;
- `tools/vfx-sheet/.gitignore`: đúng hai dòng, `# vfx-sheet: test and smoke outputs, never in Git` và `/.tmp/`;
- `tools/vfx-sheet/.tmp/**`: ảnh của test và của lượt chạy thử (bị bỏ qua);
- `docs/codex-queue/037-report.md` trong worktree: tiếng Việt có dấu.

**Cấm:**
- ghi ngoài danh sách trên, nhất là `shared/game-kit/**`, `games/**`, `package.json`, các công cụ khác trong `tools/`;
- ghi vào `/Users/toandx/htdocs/typing-game` hay bất cứ worktree nào khác;
- cài gói (`npm`, `pnpm`, `brew`…), mạng, mở cổng, dev server, trình duyệt;
- lệnh git có ghi. Được dùng: `status`, `diff`, `log`, `rev-parse`, `branch --show-current`, `check-ignore`;
- đụng Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`).

Mã là Node ESM thuần (`.mjs`), chỉ thư viện chuẩn của Node 24. Chú thích trong mã viết bằng tiếng Anh.

## Việc

### 1. `lib/png.mjs`

- `encodePng({ width, height, data })`: RGBA 8 bit, bộ lọc 0, `zlib.deflateSync`, CRC32 đúng chuẩn PNG. Trả `Buffer`.
- `decodePng(buffer)`, trả `{ width, height, data: Uint8Array RGBA }`:
  - nhận ảnh 8 bit, không xen dòng, kiểu màu 0, 2, 3 (kể cả `tRNS`), 4, 6;
  - giải đủ năm bộ lọc 0–4;
  - sai chữ ký thì ném lỗi. Độ sâu khác 8, ảnh xen dòng, kiểu màu khác: ném `Error` có chữ `not supported`.
- `crc32(bytes)`: `crc32(Buffer.from("IEND"))` = `0xae426082`.

### 2. `lib/image.mjs`

`readImage(path)`:
- `.png`: thử `decodePng`. Nếu lỗi có chữ `not supported`, chuyển sang magick.
- Mọi đuôi khác, và PNG vừa chuyển: chạy `magick <path> -depth 8 png32:-` rồi `decodePng` (`maxBuffer` đủ cho ảnh 4K).
- Kênh alpha của khung bị bỏ qua khi đo (ảnh chụp là ảnh đục).

### 3. `lib/measure.mjs`

| Hàm | Định nghĩa chính xác |
|---|---|
| `luma(r, g, b)` | `(0.2126·r + 0.7152·g + 0.0722·b) / 255` |
| `relLum(r, g, b)` | Độ chói WCAG như phần Bối cảnh |
| `saturation(r, g, b)` | Độ bão hòa HSV: `max = 0` thì 0, ngược lại `(max − min)/max` |
| `parseMask(spec)` | Ba dạng; sai dạng hay số không hữu hạn thì ném `Error` có chữ `bad mask`:<br>• `rect:x,y,w,h`;<br>• `ring:cx,cy,r0,r1`;<br>• `png:<đường dẫn>` |
| `maskOf(mask, w, h)` | `Uint8Array` 0/1, mỗi điểm ảnh một ô. Điểm (x, y) thuộc mặt nạ khi:<br>• rect: `x0 ≤ x < x0 + w` và `y0 ≤ y < y0 + h`;<br>• ring: `r0 ≤ hypot(x + 0.5 − cx, y + 0.5 − cy) ≤ r1` (đĩa khi `r0 = 0`);<br>• png: ảnh mặt nạ cùng cỡ với khung, alpha ≥ 128 và luma ≥ 0,5 (khác cỡ thì lỗi) |
| `lightEnergy(img, mask, ref?)` | `Σ max(0, luma(img) − luma(ref))` trên mặt nạ; không có `ref` thì trừ 0 |
| `firstToPeak(frames, mask, ref?)` | Trả `{ energy[], peakIndex, ratio }`:<br>• `peakIndex`: chỉ số **đầu tiên** có năng lượng lớn nhất;<br>• `ratio = energy[0] / energy[peakIndex]`, bằng 0 khi đỉnh bằng 0 |
| `whiteShare(img, mask, threshold = 0.95)` | Số điểm có `luma ≥ threshold` chia số điểm của mặt nạ; mặt nạ rỗng thì 0 |
| `meanSaturation(img, mask, minLuma = 0)` | Trả `{ mean, count }`: trung bình `saturation` trên các điểm của mặt nạ có `luma ≥ minLuma`, và số điểm đó |
| `contrast(img, mask, textHex, pct = 99)` | Trả `{ text, background, ratio, count }`:<br>• `background`: sắp `relLum` các điểm của mặt nạ tăng dần, lấy hạng gần nhất, chỉ số `ceil(pct/100 · n) − 1`;<br>• `text = relLum` của `#rrggbb`;<br>• `ratio = (max + 0.05)/(min + 0.05)` |

### 4. `lib/sheet.mjs`

**`layout({ ref, frame, n, cols = min(n, 6), tile = 320, label = 22, gap = 8, margin = 8 })`** là hàm thuần. `ref` là `{ w, h }` hay `null`; `frame` là `{ w, h }`. Trả `{ width, height, ref, tiles: [{ image, label }] }`, mỗi ô chữ nhật là `[x, y, w, h]`.

Các đại lượng:
- `th = round(tile · frame.h / frame.w)`
- `rows = ceil(n / cols)`
- `gw = cols·tile + (cols − 1)·gap`
- `gh = rows·(th + label) + (rows − 1)·gap`
- `rw = round(ref.w · gh / ref.h)` (0 khi không có `ref`)
- `x0 = margin + (ref ? rw + 2·gap : 0)`

Kết quả:
- ô ảnh tham chiếu: `[margin, margin, rw, gh]`, hay `null`;
- ô thứ k:
  - ảnh: `[x0 + (k % cols)·(tile + gap), margin + floor(k / cols)·(th + label + gap), tile, th]`;
  - dải nhãn ngay dưới ảnh: `[x, y + th, tile, label]`;
- tờ: rộng `x0 + gw + margin`, cao `margin + gh + margin`.

**`composeSheet({ ref, refSize, frames, frameSize, labels, out, …layout })`** chạy một lệnh magick:
1. nền `xc:#1e1e1e` đúng cỡ tờ;
2. mỗi ảnh `-resize WxH!` rồi `-geometry +x+y -composite` vào ô của nó;
3. nhãn bằng phông ở trên, `-pointsize 14 -fill #f4f1eb -gravity NorthWest -annotate +(x+4)+(y+3)` trong dải nhãn;
4. `-depth 8` trước tên file ra. Không có cờ này, magick ghi PNG 16 bit.

Sau đó ghi file JSON có tên là tên file ra thêm đuôi `.json` (ví dụ `f5-xung.jpg` → `f5-xung.jpg.json`, `sheet.png` → `sheet.png.json`). JSON gồm bố cục, `refFile`, và mỗi ô `{ image, label, file, text }` (`text` là chữ của nhãn). Trả lại đúng object đó.

### 5. `cli.mjs`

```text
node tools/vfx-sheet/cli.mjs measure (--meta <meta.json> | --frames <a.png,b.png | thư mục>) [--ref-frame <ảnh> | auto]
    [--flash <mask>] [--field <mask> [--threshold 0.95]] [--ring <mask> [--min-luma 0]]
    [--text <mask> --text-color #rrggbb [--pct 99]] [--out <file.json>]
node tools/vfx-sheet/cli.mjs sheet (--meta <meta.json> | --frames …) [--ref <ảnh>] [--cols N] [--tile W] --out <tờ.png | .jpg>
```

- **`--meta`:** đọc `rows` (hoặc `frames`). Mỗi dòng có `file`, tính từ thư mục của meta; `f`, `ms`, `phase` không bắt buộc.
  - **Thứ tự:** sắp ổn định theo `f` tăng dần; dòng không có `f` đứng sau mọi dòng có `f`, giữ thứ tự trong file.
  - `measure` dùng các dòng có `f ≥ 0` (hoặc không có `f`), theo thứ tự trên.
  - `sheet` dùng **mọi** dòng, kể cả `f < 0`, theo thứ tự trên. Vì vậy ô 0 của lượt chạy thử là `f-1`.
  - `--ref-frame auto` lấy dòng có `f` âm lớn nhất. Không có dòng nào như vậy là lỗi dùng sai.
- **`--frames`:** danh sách cách nhau bằng dấu phẩy. Một thư mục thì lấy mọi `*.png` trong đó, sắp theo tên.
- **Nhãn của tờ khung:** có `f` thì là `f<f> · <ms> ms`, thêm ` · <phase>` nếu có `phase`. Không có meta thì là tên file bỏ đuôi.
- **`measure`** in JSON (thụt 1) ra stdout; có `--out` thì ghi thêm file. Mọi số thực trong JSON làm tròn 6 chữ số **thập phân**: `Math.round(x * 1e6) / 1e6` (ví dụ `0.020833`, `3808.051959`). Các khóa:
  - `frames` (tên file) và `size: [w, h]`;
  - `flash: { mask, ref, energy[], peakIndex, firstToPeak }`;
  - `white: { mask, threshold, share[], max, over6, over15 }`, trong đó `over6`, `over15` là số khung có tỉ lệ > 0,06 và > 0,15;
  - `saturation: { mask, minLuma, mean[], count[] }`;
  - `contrast: { mask, text, pct, ratio[], min }`.

  Chỉ có khối của các tùy chọn được đưa vào. Khung khác cỡ nhau, hay ảnh `ref` khác cỡ khung, là lỗi chạy.
- **`sheet`** gọi `composeSheet` (đo cỡ ảnh tham chiếu và khung đầu bằng `readImage`), rồi in JSON của bố cục.
- **Mã thoát:**
  - 0: đạt;
  - 2: dùng sai, ví dụ lệnh lạ, thiếu tùy chọn, `bad mask`, `--text` thiếu `--text-color`, `auto` không có dòng `f < 0`;
  - 1: lỗi chạy, ví dụ thiếu file, ảnh hỏng, khác cỡ, magick lỗi.

  Lỗi in ra stderr, bắt đầu bằng `vfx-sheet: `.

### 6. Test (`node --test`)

Đáp án dưới đây do Claude tính bằng một bản cài thử đúng các định nghĩa trên, chạy hai lần, cùng kết quả. Ảnh tổng hợp của test ghi vào `tools/vfx-sheet/.tmp/<tên test>/`; mỗi test xóa thư mục con của mình lúc bắt đầu. Sai số so sánh số thực: 1e-9, trừ khi ghi khác.

**`png.test.mjs`**
1. **Mã hóa rồi giải lại** ảnh 37×23 RGBA, byte sinh bằng `s = (s·1103515245 + 12345) >>> 0` (bắt đầu `s = 7`), mỗi byte `s >>> 24`: ra đúng từng byte.
2. **Năm biến thể do magick tạo** (`-seed 3`), mỗi ảnh 37×23. `decodePng` ra đúng từng byte như `magick <file> -depth 8 rgba:-`:

   | Biến thể | Lệnh magick | Kiểu màu |
   |---|---|---|
   | RGB | `-size 37x23 gradient:red-blue PNG24:` | 2 |
   | RGBA | `-size 37x23 gradient:#ff000080-#0000ffff PNG32:` | 6 |
   | Bảng màu | `-size 37x23 plasma:fractal -colors 16 PNG8:` | 3 |
   | Xám | `-size 37x23 gradient:black-white -colorspace Gray -depth 8 PNG:` | 0 |
   | Xám có alpha | `-size 37x23 gradient:#00000040-#ffffffff -colorspace Gray -depth 8 PNG:` | 4 |

3. **Dạng không hỗ trợ:** `-size 37x23 gradient:red-blue -interlace PNG PNG24:` (xen dòng) và `-size 37x23 gradient:red-blue -depth 16 PNG48:` (16 bit). `decodePng` ném lỗi có chữ `not supported`; `readImage` vẫn đọc được qua magick, đúng từng byte như `magick <file> -depth 8 rgba:-`.
4. `crc32(Buffer.from("IEND"))` = `0xae426082`.

**`measure.test.mjs`**

Ký hiệu: "khung 40×30 đen" nghĩa là mọi điểm `(0,0,0,255)`.

1. **`firstToPeak`.**
   - Ba khung 40×30 đen. Mỗi khung có `n` điểm trắng ở `(10 + k % 20, 5 + floor(k/20))`, với k = 0…n−1, và `n` lần lượt 10, 20, 5.
   - Mỗi khung thêm 4 điểm trắng ở `(12…15, 20)` và một điểm trắng ở `(0, 0)`.
   - Khung tham chiếu: đen, chỉ có 4 điểm ở `(12…15, 20)`.
   - Mặt nạ `rect:10,5,20,20`.

   | Trường hợp | `energy` | `peakIndex` | `ratio` |
   |---|---|---|---|
   | Không tham chiếu | `[14, 24, 9]` | 1 | `0.5833333333333334` |
   | Có tham chiếu | `[10, 20, 5]` | 1 | `0.5` |

2. **`lightEnergy`:** 6 điểm xám `(128,128,128)` trong mặt nạ, nền đen: `3.011764705882353`, tức `6·128/255`.
3. **`whiteShare`.**
   - Ảnh 100×100 đen, mặt nạ `rect:0,0,100,50` (5.000 điểm).
   - Trong mặt nạ, xếp lần lượt theo hàng từ ô (0, 0): 300 điểm `(255,255,255)`, 200 điểm `(242,242,242)`, 100 điểm `(243,243,243)`, 50 điểm `(255,255,200)`.
   - Ngoài mặt nạ: 500 điểm trắng từ hàng 60.
   - Kết quả: `0.09`.
   - Kèm theo: `luma(242,242,242)` = `0.9490196078431372` (< 0,95); `luma(243,243,243)` = `0.9529411764705882`; `luma(255,255,200)` = `0.9844274509803921`.
4. **`meanSaturation`.**
   - Ảnh 100×100 nền `(90,90,90)`, vòng `ring:50,50,10,20`: có **948** điểm.
   - Điểm có `x < 50` (474 điểm) tô `(255,0,0)`; điểm còn lại tô `(255,128,128)`.
   - Kết quả: `{ mean: 0.7490196078431373, count: 948 }`, tức `0.5 + 127/510`; sai số 1e-12.
   - Đổi 40 điểm đầu tiên của vòng có `x ≥ 50`, theo thứ tự hàng rồi cột, thành `(20,0,0)`:
     - `minLuma` 0: `{ mean: 0.7701993877719873, count: 948 }`;
     - `minLuma` 0,05: `{ mean: 0.7600760127839691, count: 908 }`.
5. **`contrast`.**
   - Ảnh 60×30 trắng, mặt nạ `rect:5,5,50,20` (1.000 điểm). Trong mặt nạ, theo thứ tự hàng: 20 điểm đầu `(128,128,128)`, còn lại đen.
     - Chữ `#f4f1eb`: `text` = `0.8814184890328656`, `background` = `0.21586050011389923`, `ratio` = `3.503410580488`.
     - Chỉ 5 điểm xám: `background` = 0, `ratio` = `18.628369780657312`.
   - Ảnh 10×10 trắng, chữ `#000000`: `ratio` = `21`.
6. **`parseMask`:** `rect:1,2,3` và `circle:1,2,3,4` ném lỗi có chữ `bad mask`.

**`sheet.test.mjs`**
1. **`layout` có ảnh tham chiếu:** `ref {w:100, h:50}`, `frame {w:64, h:36}`, `n` 4, `cols` 2, `tile` 128 cho:

   | Phần | Kết quả |
   |---|---|
   | Tờ | `width` 688, `height` 212 |
   | `ref` | `[8, 8, 392, 196]` |
   | Ảnh của các ô | `[416, 8, 128, 72]`, `[552, 8, 128, 72]`, `[416, 110, 128, 72]`, `[552, 110, 128, 72]` |
   | Nhãn của các ô | `[416, 80, 128, 22]`, `[552, 80, 128, 22]`, `[416, 182, 128, 22]`, `[552, 182, 128, 22]` |

2. **`layout` không có ảnh tham chiếu:** `frame {w:1280, h:720}`, `n` 24, `cols` 6, `tile` 320 cho tờ 1976 × 848. Ô 6 ở `[8, 218, 320, 180]`; ô 23 ở `[1648, 638, 320, 180]`, nhãn `[1648, 818, 320, 22]`.
3. **`composeSheet` với ảnh tổng hợp:**
   - Ảnh tham chiếu 100×50 màu `(220,30,30)`.
   - Bốn khung 64×36 màu `(30,200,30)`, `(30,30,220)`, `(230,200,30)`, `(200,30,200)`.
   - Nhãn `f0 · 0 ms · R`, `f1 · 17 ms · R`, `f2 · 33 ms · I`, `f3 · 50 ms · F`; `cols` 2, `tile` 128.
   - Đọc file ra bằng `magick out png32:-` rồi `decodePng`:
     - cỡ 688 × 212;
     - điểm (204, 106) màu `(220,30,30)`;
     - tâm mỗi ô ảnh `(x + 64, y + 36)` đúng màu khung của ô đó;
     - mỗi dải nhãn có ≥ 20 điểm luma ≥ 0,5 (chữ);
     - file JSON đi kèm (`<out>.json`, ở đây `sheet.png.json`) có `tiles[].text` đúng bốn nhãn theo thứ tự.
   - File ra là 8 bit: `magick identify -format %z out` in `8`.

**`cli.test.mjs`** (gọi `node tools/vfx-sheet/cli.mjs` bằng tiến trình con)

1. **Dữ liệu:**
   - Ghi `pre.png` (khung tham chiếu ở `measure.test` 1), và `f0.png`, `f1.png`, `f2.png` (ba khung ở `measure.test` 1). Mỗi khung `f` thêm 6 điểm `(255,0,0)` ở `(30…35, 2)`.
   - Ghi `meta.json` với `rows`:
     - `{file:"pre.png", f:-1, ms:-17}`;
     - `{file:"f0.png", f:0, ms:0, phase:"R"}`;
     - `{file:"f1.png", f:1, ms:17, phase:"I"}`;
     - `{file:"f2.png", f:2, ms:33, phase:"I"}`.
2. **`measure`:** `--meta <meta> --ref-frame auto --flash rect:10,5,20,20 --field rect:0,0,40,30 --ring ring:33,2.5,0,3 --text rect:0,0,40,30 --text-color #f4f1eb`. Thoát 0, JSON có:

   | Khóa | Giá trị |
   |---|---|
   | `frames` | `["f0.png","f1.png","f2.png"]` |
   | `size` | `[40,30]` |
   | `flash` | `ref "pre.png"`, `energy [10,20,5]`, `peakIndex 1`, `firstToPeak 0.5` |
   | `white` | `share [0.0125,0.020833,0.008333]`, `max 0.020833`, `over6 0`, `over15 0` |
   | `saturation` | `mean [0.230769,0.230769,0.230769]`, `count [26,26,26]` |
   | `contrast` | `ratio [1.127313,1.127313,3.54691]`, `min 1.127313` |

3. **`sheet`:** `--meta <meta> --cols 2 --tile 80 --out <dir>/sheet.png`. Thoát 0; file ra 184 × 188, bằng `width`, `height` trong JSON in ra.
4. **Mã thoát:**
   - `measure --meta <meta> --flash rect:1,2,3`: 2;
   - `measure --frames <dir>/khong-co.png --field rect:0,0,1,1`: 1;
   - lệnh `bogus`: 2;
   - `measure --meta <meta> --text rect:0,0,4,4` (thiếu `--text-color`): 2.

   Mỗi lần, stderr bắt đầu bằng `vfx-sheet: `.

## Kiểm (bắt buộc)

Chạy từ cwd `.` của worktree. Dán lệnh và dòng kết quả vào báo cáo.

0. **Điều kiện đầu:**
   - `git branch --show-current` in `vfx`;
   - `test ! -e tools/vfx-sheet` thoát 0;
   - `/opt/homebrew/bin/magick -version` in `ImageMagick 7.`;
   - `test -f /System/Library/Fonts/Supplemental/Arial.ttf` thoát 0;
   - `node --version` ≥ v24.

   Giữ kết quả `git status --short --untracked-files=all`.
1. `node --test tools/vfx-sheet/test/*.test.mjs` đạt, trên đủ 4 file test. In số test. Một thư mục đưa thẳng cho `node --test` bị hiểu là một module và hỏng, nên dùng glob như trên.
2. Chạy lại lệnh 1 lần nữa: cùng số test, cùng kết quả.
3. Mọi đáp án ở mục 6 khớp từng số (nằm trong lệnh 1). Báo cáo có bảng "giá trị test nhận được, cạnh giá trị trong phiếu" cho `measure.test` 1–5 và `cli.test` 2.
4. `node --check` đạt trên `cli.mjs` và từng file trong `lib/`.
5. **Bỏ qua của Git:**
   - `git check-ignore -q tools/vfx-sheet/.tmp/x` thoát 0;
   - `git check-ignore -q tools/vfx-sheet/cli.mjs` thoát 1;
   - `git check-ignore -q tools/vfx-sheet/lib/png.mjs` thoát 1.
6. **Chạy thử trên dữ liệu thật** (chỉ đọc, ra file trong `.tmp/smoke/`). Đặt:
   - `META=/Users/toandx/htdocs/typing-game/games/typing-survival/tmp/mac-2026-10-27/feel-n4n6/round2/suite3/1280x720/meta-f5-xung-1280x720.json` (25 dòng, khung 1280×720);
   - `REF=/Users/toandx/htdocs/typing-game/tmp/vfx/owner-reference-layered-vfx.webp` (1330×1202).

   Hai lệnh và kết quả phải có:
   - **`sheet`:** `node tools/vfx-sheet/cli.mjs sheet --ref $REF --meta $META --cols 6 --tile 320 --out tools/vfx-sheet/.tmp/smoke/f5-xung.jpg`. Thoát 0, trong ≤ 10 s (bản cài thử: 1 s), có thêm `tools/vfx-sheet/.tmp/smoke/f5-xung.jpg.json`.

     | Phần | Kết quả |
     |---|---|
     | Tờ | 3145 × 1058, khớp `magick identify` |
     | `ref` | `[8, 8, 1153, 1042]` |
     | Số ô | 25 |
     | Ô 0 | `[1177, 8, 320, 180]`, nhãn `f-1 · -17 ms` |
     | Ô 24 | `[1177, 848, 320, 180]`, nhãn `f23 · 766 ms` |

   - **`measure`:** `node tools/vfx-sheet/cli.mjs measure --meta $META --ref-frame auto --flash ring:643,536,0,60 --field rect:0,0,1280,400`. Thoát 0, trong ≤ 15 s (bản cài thử: 2 s).

     | Khóa | Kết quả |
     |---|---|
     | Số khung | 24, khung đầu `xung-00.png` |
     | `flash.ref` | `xung-pre.png` |
     | `flash.firstToPeak` | `1` |
     | `flash.peakIndex` | `0` |
     | `flash.energy[0]` | `3808.051959` |
     | `white.max` | `0.00934` |
     | `white.over6` | `0` |

   Nếu một trong hai file đầu vào không còn trên đĩa, ghi "bỏ qua, thiếu <file>". Đây không phải lỗi.
7. **Tốc độ** (chỉ ghi lại): thời gian `readImage` trên `/Users/toandx/htdocs/typing-game/games/typing-survival/tmp/mac-2026-10-27/feel-n4n6/round2/suite3/1920x1080/c1-s1-1920x1080-burst-00.png` (1920×1080, RGB 8 bit, không xen dòng, nên giải bằng mã thuần, không qua magick). Bản cài thử: 81–91 ms qua ba lần. File không còn thì ghi "bỏ qua, thiếu file".
8. **`git status --short --untracked-files=all`** so với lúc bắt đầu: chỉ **thêm** các file trong `tools/vfx-sheet/` (trừ `.tmp`) và `docs/codex-queue/037-report.md`.

## Báo cáo `docs/codex-queue/037-report.md`

- Các file đã viết, mỗi file một dòng nói nó làm gì.
- Kết quả 9 lệnh kiểm, kèm số; bảng đáp án nhận được cạnh đáp án của phiếu.
- Đường dẫn tờ khung chạy thử (`tools/vfx-sheet/.tmp/smoke/f5-xung.jpg`), để Claude mở xem.
- Những chỗ phiếu chưa rõ và cách đã chọn.

**Xong khi:** Kiểm 0–6 và 8 đạt, báo cáo đã viết. Codex không commit; Claude đọc diff, chạy lại test, xem tờ khung chạy thử rồi mới commit.
