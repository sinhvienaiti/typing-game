# Bản đồ: phiếu làm việc (28/10/2026)

**Đi kèm:** `MAP_PLAN.md` cùng thư mục (gọi tắt là "kế hoạch"; số mục § theo file đó). Kế hoạch mở rộng `docs/tools/MAP_FACTORY.md`.

**Tổng:**
- Bản thử (Rồng L2-cau): Codex 34 phiếu (6 ảnh, 28 mã), mỗi phiếu dưới một giờ; Claude 13 làn; chủ dự án 4 việc.
- Triển khai: Codex 25 phiếu (13 ảnh, 12 mã); Claude 8 làn; chủ dự án 6 việc.

**Số phiếu.** Mã MF-xx là mã kế hoạch. Khi xếp vào `docs/codex-queue/`, Claude gán số trống kế tiếp (hiện tới 064; kiểm `ls docs/codex-queue` lúc xếp). Tên file `<số>-mf-xx-<tên>.md`, báo cáo `docs/codex-queue/<số>-report.md`. Mỗi phiếu chép đủ phần luật chung (mục 1) vào đầu file, như phiếu 053.

**Thứ tự giao Codex:** ảnh trước, rồi mã (yêu cầu của chủ dự án và luật hạn mức 27/10).

## 0. Thứ tự

```text
Ngày 1 (Claude):  CL-01 chấm ảnh đợt 3 → OW-01 (chủ dự án dựng Tripo)
                  CL-02 gộp lõi, tạo worktree, xếp phiếu    CL-03 bộ giám khảo
Codex, ảnh:       MF-I1 → MF-I2 → MF-I5 → MF-I6 → MF-I3 → MF-I4
Codex, mã nền:    MF-C01 → MF-C02 → MF-C03 → MF-C04 → MF-C05          (repo cha)
                  MF-C20 → MF-C21 → MF-C22 → MF-C23 → MF-C24          (worktree Rồng)
Chặng A (Claude): CL-04 → CL-05 → CL-06  (cần MF-C03/C04 cho cổng A; MF-C24 cho ô đất)
Codex, lõi:       MF-C06 → MF-C07 → MF-C08 → MF-C09 → MF-C10 → MF-C11 → MF-C12
                  → MF-C13 → MF-C14 → MF-C15 → MF-C16 → MF-C17 → MF-C18 → MF-C19
Codex, đồ thị:    MF-C25 → MF-C26 → MF-C27 → MF-C28                    (worktree Rồng; cần CL-07)
Chặng B (Claude): CL-07 (đồ thị, brief) → CL-08 (nối lõi, thử tổng quát)
Chặng C:          OW-01, OW-02 → CL-09 → CL-10 → CL-11 → OW-03
Chặng D:          MF-C20..C23 → CL-12 (bot)
Tài liệu:         CL-13 (cuối mỗi chặng)
Triển khai:       sau GO (khoảng 17/11): mục 6
```

Hai làn Codex (repo cha, worktree Rồng) chạy xen kẽ, không cùng lúc nếu hạn mức chỉ đủ một. Không phiếu nào trong cùng một worktree chạy song song.

---

## 1. Luật chung

### 1.1 Mọi phiếu ảnh Codex

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh ghi vào `art-src` của game (media, không vào Git).
- **Luật điểm:** ảnh 2D đạt từ 8 điểm (`docs/games/ART_ACCEPTANCE.md` §2.2). Chưa đạt thì sửa prompt, tối đa 3 lượt mỗi ảnh. Ảnh nguồn Tripo không nướng ánh sáng hay vùng phát sáng.
- **Chỉ được ghi:** đúng các file phiếu liệt kê; mỗi lượt thử là `<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3); bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`; `art-src/_review/<mã phiếu>-*.jpg` và `art-src/_review/<mã phiếu>/`; file báo cáo.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`;
  - mọi lệnh git;
  - sửa mã hay tài liệu;
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - đụng game khác ngoài game của phiếu; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, logo, người, thần, nơi thờ trong ảnh.
- **Kiểm chung, bắt buộc:**
  - **KA1 md5:** `md5 -r` mọi file trong thư mục đích trước (`_review/<mã>/md5-before.txt`) và sau; `diff` chỉ có dòng của file mới.
  - **KA2 khổ và nền:** `magick identify` đúng khổ; với ảnh nguồn Tripo, 10 px mép bốn phía có độ lệch chuẩn ≤ 6/255 và màu trung bình gần `#E6E6E6` (mỗi kênh lệch ≤ 8); với sprite và decal, alpha sạch (không viền nền).
  - **KA3 lề:** ảnh nguồn Tripo cắt nền bằng `magick <ảnh> -fuzz 12% -trim -format '%X %Y %w %h' info:`; vật cách mép ≥ 24 px.
  - **KA4 màu giữ riêng:** tỉ lệ px có hue 0–50° hoặc 165–190°, saturation > 0,55, value > 0,5 phải ≤ 2 % (trừ khi phiếu cho phép rõ, như cây tán ấm có dải riêng).
  - **KA5 tự chấm:** 5 tiêu chí của §2.2, ở cỡ đầy đủ và ở 128 px; ghi điểm từng lượt.
- **Báo cáo:** tiếng Việt; file tạo ra; số đo từng kiểm; điểm từng lượt; lượt chọn và lý do.
- **Xong khi (chung):** KA1–KA5 đạt và bản chọn tự chấm ≥ 8. **Nhận** khi Claude chấm lại ≥ 8.

### 1.2 Mọi phiếu mã Codex ở repo cha

- **Thư mục làm việc:** worktree `/Users/toandx/htdocs/typing-game-wt/map-codex`, nhánh `map-factory` (MAP_FACTORY §9.4).
- **Chỉ được ghi:** đúng các đường dẫn phiếu liệt kê, cộng file báo cáo.
- **Cấm:**
  - lệnh git có ghi (`add`, `commit`, `checkout`, `stash`, `reset`, `clean`…); `git status`, `git diff`, `git archive` được phép;
  - mạng, trình duyệt, dev server, server bất kỳ;
  - ghi dưới `games/**` (chỉ đọc; bộ đọc lấy nội dung game bằng `git archive` ở commit ghim);
  - cài gói npm hay pip; chỉ Node 24 có sẵn và `node_modules` của `shared/game-kit` (TypeScript 6.0.3, vitest);
  - đọc hay ghi Tu Tiên;
  - `Math.sin/cos/tan/atan2/pow/hypot/exp/log/cbrt/random`, `Date`, `performance`, `**` trong `shared/game-kit/map/` (ngoài `*.test.ts`); số lẻ ở đầu ra lõi (đơn vị cm, ‰, độ nguyên).
- **Kiểm chung, bắt buộc:**
  - **KC1 cây Git:** lưu `git status --short --untracked-files=all` lúc đầu; lúc cuối chỉ được **thêm hoặc sửa** đường dẫn cho phép; không dòng ` M`, ` D` mới ngoài phạm vi.
  - **KC2 lint tất định:** test lint của 027 đạt trên mọi file mới trong `map/`.
  - **KC3 test:** `pnpm --dir shared/game-kit exec vitest run map` và `node --test tools/map-factory/test/*.test.mjs` đạt; `tsc -p shared/game-kit/map/tsconfig.json` đạt.
  - **KC4 tất định:** chạy hai lần (hai tiến trình Node) cho cùng từng byte; in băm.
- **Quá một giờ:** dừng ở phần đã xong, ghi phần còn lại vào báo cáo.
- **Báo cáo:** tiếng Việt; file tạo hay sửa; kết quả từng kiểm kèm số in ra; thời gian chạy.

### 1.3 Mọi phiếu mã Codex ở worktree Rồng

- **Thư mục làm việc:** `games/.wt-dh-mapcodex` (repo Rồng), nhánh `map-codex` tách từ `main` 02fe9c7, do Claude tạo ở CL-02. Phụ thuộc cài như các worktree `.wt-dh-*` khác.
- **Chỉ được ghi:** đúng các đường dẫn phiếu liệt kê **bên trong worktree này**, cộng file báo cáo ở repo cha `docs/codex-queue/<số>-report.md`.
- **Cấm:** như 1.2, cộng:
  - ghi vào checkout chính `games/dragon-hold` hay worktree khác (`.wt-dh-mappilot` là của Claude);
  - `pnpm media:push`, `pnpm media:pull`, `pnpm dev`, kịch bản trình duyệt (`scripts/visual/**`);
  - sửa `tests/golden/**` (golden chỉ Claude đổi, có chủ ý).
- **Kiểm chung, bắt buộc:**
  - **KR1 cây Git:** như KC1, trong worktree.
  - **KR2 golden:** `md5 -r tests/golden/*` trước và sau giống hệt; `pnpm test` đạt.
  - **KR3 check:** `pnpm check` (sha kit, test, tsc, vite build) đạt.
  - **KR4 tất định:** như KC4 với lệnh của phiếu.

### 1.4 Mọi làn Claude

- Duyệt từng phiếu Codex: đọc diff, chạy lại kiểm, phản biện, rồi mới commit. Commit kết thúc bằng dòng ghi công của phiên.
- Repo cha: commit trên `map-factory`; điều phối viên gộp về nhánh làm việc. Repo Rồng: Claude gộp `map-codex` vào `map-pilot`, rồi `map-pilot` vào `main` sau cổng C.
- Không media trong commit (`git diff --cached --stat` chỉ có `ts`, `mjs`, `json`, `md`, `svg` nhỏ). Media đẩy bằng `pnpm media:push` của game, chỉ Claude chạy.
- Ảnh chụp: nhìn trước khi kết luận; ghép tờ; dọn ảnh thô bằng `tools/capture-prune`.
- Mỗi lần đổi game: changelog `games/<id>/docs/changelog/<ngày>-<chủ đề>.md` ghi việc đã sửa.
- Giám khảo luôn là subagent mới; người dựng không chấm (kế hoạch §2.8).

### 1.5 Việc của chủ dự án

Chủ dự án làm trên web Tripo bằng tay (credit web), không qua CLI. Claude đưa danh sách: tên tiếng Anh, file ảnh, face limit, nơi thả GLB, credit ước. Sau mỗi model Claude xử lý (Blender `--kind props`, `prepare-models`), chấm ≥ 7 (hoặc ghi tạm), ghi metadata vào sổ, ghi số credit đã dùng.

---

## 2. Phiếu ảnh Codex (bản thử)

Phong cách chung cho MF-I1, MF-I2: đọc `docs/games/dragon-lane/art-requests/m0/03-pine-river-props.md` (§1, §3, §4) và xem `games/dragon-hold/art-src/props/pine-river/*.png`, nhất là `bridge-old.png`, `rock-boulder.png`, `pine-tall.png` và 8 ảnh của phiếu 046. Mỗi prompt giữ **nguyên văn** các dòng chung của bộ (Image-to-3D source…, House style…, View…, Colour rules…, Light…, Build…, Never draw…, Background `#E6E6E6`); chỉ thay dòng "Kit prop (pine-river forest, spring): …".

### MF-I1 · [codex-image] Campfire Ring và Woodpile (pine-river)

**Cần trước:** không.

**Chỉ được ghi:** `games/dragon-hold/art-src/props/pine-river/{campfire-ring,woodpile}.*` (theo mẫu tên ở 1.1), `games/dragon-hold/art-src/_review/MF-I1*`.

| Tên file | Tên | Cỡ thật | Khổ | Mô tả |
|---|---|---|---|---|
| `campfire-ring` | Campfire Ring | rộng 2,6 m | 1536×1024 | Vòng đá xám ấm quanh vài khúc củi xếp chéo **chưa đốt** (không lửa, không khói, không than đỏ), hai khúc gỗ dài làm ghế ngồi hai bên. Đáy phẳng |
| `woodpile` | Woodpile | dài 2 m, cao 1,1 m | 1536×1024 | Đống củi chẻ xếp gọn giữa hai cọc, một gốc cây có rìu cắm, vài mẩu vụn gỗ. Gỗ nâu ấm cùng chất với `bridge-old.png` |

**Kiểm (bắt buộc):** KA1–KA5; KA4 không ngoại lệ (than đỏ hay lửa là trượt).

**Xong khi:** hai ảnh đạt chung 1.1.

### MF-I2 · [codex-image] Maple Tree dự phòng, hai sắc (pine-river)

**Cần trước:** không. Chỉ dùng nếu cây tán tròn có sẵn nhuộm sắc ấm dưới 8 điểm (CL-05).

**Chỉ được ghi:** `games/dragon-hold/art-src/props/pine-river/{maple-tree-rust,maple-tree-copper}.*`, `_review/MF-I2*`.

**Việc:** một cây lá rộng mùa thu, thân lộ rõ từ góc 55° và 75°, tán thành 3–5 khối lá tròn mềm như các cây của bộ, cao 6 m, khổ 1024×1536. Hai bản: tán **gỉ sắt** và tán **đồng**. Dáng tán khác cây tròn và thông của bộ.

**Kiểm (bắt buộc):** KA1–KA3, KA5; thay KA4 bằng:
1. Mặt nạ tán (hue 0–60°, s > 0,25, trong vùng vật): hue trung vị 10–30°, s trung vị ≤ 0,70, v trung vị ≤ 0,70.
2. ΔE2000 của màu tán trung vị so với #FF4A4A, #FFB020, #FFC83A và vàng Héo #C8D24A, mỗi số ≥ 20. In bốn số.
3. Px ngoài tán: KA4 như thường.

**Xong khi:** hai ảnh đạt chung 1.1 và ba kiểm trên.

### MF-I3 · [codex-image] Sprite sự sống A: chim và bướm

**Cần trước:** không.

**Chỉ được ghi:** `games/dragon-hold/art-src/fx/life/{bird-flap,butterfly}.*`, `{bird-flap,butterfly}.json`, `_review/MF-I3*`.

**Việc:**
- `bird-flap.png`: 3 dáng chim nhỏ nhìn từ trên cao khoảng 55°, mỗi dáng 8 khung đập cánh; lưới 8 × 3, ô 64 px; màu xám nâu sẫm, đọc được ở 8–14 px.
- `butterfly.png`: 3 màu nhạt (kem, xanh lơ nhạt, tím nhạt `#8E7CC3` nhạt hơn), mỗi màu 4 khung; lưới 4 × 3, ô 32 px.
- Mỗi tờ một JSON: `{cell, cols, rows, frames, loop: true}`.

**Kiểm (bắt buộc):** KA1, KA5; nền trong suốt, viền alpha sạch; đúng lưới; khung cuối về khung đầu: in sai khác điểm ảnh trung bình (phải ≤ sai khác giữa hai khung liền kề lớn nhất); mỗi tờ ≤ 256 KB; KA4 = 0 %.

**Xong khi:** các kiểm đạt, tự chấm ≥ 8.

### MF-I4 · [codex-image] Sprite sự sống B: lá rơi, khói, đom đóm, bóng mây

**Cần trước:** không.

**Chỉ được ghi:** `games/dragon-hold/art-src/fx/life/{leaf-fall,smoke-puff,firefly,cloud-shadow}.*` và `.json`, `_review/MF-I4*`.

**Việc:**
- `leaf-fall.png`: 4 biến thể lá (2 xanh, 2 gỉ sắt cùng dải MF-I2), mỗi cái 4 khung xoay; ô 32 px.
- `smoke-puff.png`: 6 khung làn khói xám mềm, ô 128 px, alpha mềm.
- `firefly.png`: một chấm sáng mềm vàng xanh nhạt, 32 px (không vàng kim #FFC83A).
- `cloud-shadow.png`: ô xám 512² liền mép, nhiễu mây thấp tần, chỉ kênh độ sáng.

**Kiểm (bắt buộc):** KA1, KA5; alpha sạch; đúng lưới theo JSON; `cloud-shadow` lệch mép khi lát nửa ô ≤ 2 % (in số); mỗi tờ ≤ 256 KB; KA4 = 0 % trừ lá gỉ (in tỉ lệ).

**Xong khi:** các kiểm đạt, tự chấm ≥ 8.

### MF-I5 · [codex-image] Ô đất đồng cỏ yên và đất mòn nhạt (pine-river)

**Cần trước:** không.

**Chỉ được ghi:** `games/dragon-hold/art-src/ground/pine-river/{meadow-calm-a,meadow-calm-b,soil-worn-pale}.*`, `_review/MF-I5*`.

**Việc:** cùng khổ và cách vẽ với 8 ô có sẵn trong thư mục đó (đọc khổ bằng `magick identify`), nhìn thẳng từ trên, liền mép.
- Hai ô cỏ yên: mảng thấp tần ±5 % độ sáng, hue 88–95°, không dải phân bậc, không chấm hoa.
- Một ô đất mòn nhạt: luma khoảng 0,67, mòn mềm, không chuỗi sỏi.

**Kiểm (bắt buộc):** KA1, KA5; lát nửa ô (`-roll`) không lộ đường nối (in sai khác dọc mép); độ rối (trung bình |L − mờ 5×5|, L = 0,2126R + 0,7152G + 0,0722B) ≤ 0,030 ở hai ô cỏ; hue trung vị cỏ 88–95°; luma trung vị đất 0,64–0,70.

**Xong khi:** các kiểm đạt, tự chấm ≥ 8.

### MF-I6 · [codex-image] Tờ decal mép và cổng (pine-river)

**Cần trước:** không.

**Chỉ được ghi:** `games/dragon-hold/art-src/decals/pine-river/edge-gate-sheet.*` và `.json`, `_review/MF-I6*`.

**Việc:** một tờ decal cùng khổ, cùng lưới với 4 tờ có sẵn, các ô: thảm rêu (cổng Yêu Rêu), cỏ giẫm và vết cào (cổng Thú Mục), cành gãy, cụm 2–4 viên sỏi xám vừa (thay chuỗi sỏi trắng), lá khô nâu (thay chấm lá đỏ). JSON ghi lưới và tên ô.

**Kiểm (bắt buộc):** KA1, KA5; alpha sạch; đúng lưới; KA4 = 0 %; luma trung vị mỗi ô trong ±0,08 của luma ô đất tương ứng (in số).

**Xong khi:** các kiểm đạt, tự chấm ≥ 8.

---

## 3. Phiếu mã Codex (bản thử)

### 3.1 Repo cha

#### MF-C01 · [codex-code] Kit sync không làm hỏng Vite với `map/tsconfig.json`

**Cần trước:** CL-02 (lõi đã gộp).

**Chỉ được ghi:** `scripts/sync-game-kit.mjs`, `shared/game-kit/map/tsconfig.json`, `scripts/test/sync-game-kit.test.mjs` (tạo mới nếu chưa có).

**Việc:** `map/tsconfig.json` hiện `extends: "../tsconfig.json"`; khi chép vào `games/<id>/src/kit/map/` thì Vite báo `failed to resolve "extends"`. Chọn một: kit sync bỏ qua `map/tsconfig.json`; hoặc tsconfig của map tự đứng (chép các tùy chọn cần, giữ `erasableSyntaxOnly`). Ghi lý do chọn.

**Kiểm (bắt buộc):** KC1–KC3, và:
1. Test tạo một game mẫu trong thư mục tạm (`os.tmpdir()`), chạy sync, rồi `vite build` (Vite của `shared/game-kit` hoặc của game mẫu nếu có sẵn, không cài): thành công.
2. `verify-kit` (sha256) đạt trên game mẫu.
3. Mọi module kit khác chép ra giống hệt từng byte trước và sau sửa.
4. Lint 027 vẫn bắt `enum` và `namespace` khi dịch trong RAM với tùy chọn của map.

**Xong khi:** bốn kiểm đạt; diff chỉ ở ba file trên.

#### MF-C02 · [codex-code] Bộ đọc `dragon-hold@2`: tách `simHash` và `viewHash`

**Cần trước:** không.

**Chỉ được ghi:** `tools/map-factory/adapters/dragon-hold*.mjs`, `tools/map-factory/test/adapters.test.mjs`, `tools/map-factory/test/fixtures/gameplay/dragon-hold*.json`.

**Việc:**
- `simHash` = băm JSON chuẩn của: bệ, làn đã biên dịch (`compileLanes`, u), bề rộng, đoạn cầu và lội, cung bay, ô.
- `viewHash` = băm của: `river` (điểm, bề rộng, nông), `terrain`, `camera`.
- Giữ `@1` đọc được (băm cũ đổi tên `hashLegacy`) cho spec cũ một phiên bản.

**Kiểm (bắt buộc):** KC1, KC3, KC4, và:
1. Sửa một bề rộng sông trong RAM: chỉ `viewHash` đổi.
2. Sửa `atM` của một ô trong RAM: chỉ `simHash` đổi.
3. `simHash` của L2-cau ở commit 83da970 và 02fe9c7: in cả hai; nếu khác, in trường khác nhau (dữ liệu làn và ô không đổi thì phải bằng).
4. `git status --porcelain` của checkout chính `games/dragon-hold` trước và sau giống hệt.
5. `canonicalJson` cho cùng đầu ra như trước với các trường không đổi.

**Xong khi:** năm kiểm đạt.

#### MF-C03 · [codex-code] Đọc PNG bằng `node:zlib` và thu nhỏ hộp

**Cần trước:** không.

**Chỉ được ghi:** `tools/map-factory/lib/png.mjs`, `tools/map-factory/test/png.test.mjs`, `tools/map-factory/test/fixtures/png/*` (PNG nhỏ do test tự sinh và ghi; ≤ 20 KB mỗi file).

**Việc:**
- `decodePng(buf)`: PNG 8 bit, RGB hoặc RGBA, không interlace, mọi bộ lọc dòng (0–4). Kiểu khác trả lỗi có mã (`png-unsupported-<kiểu>`).
- `boxDownscale(rgba, w, h, 384, 216)`: trung bình vùng (diện tích), ra RGB.
- `readRaw384(buf)`: đọc RGB thô 384×216 (định dạng file `.rgb` của script đo ảnh 28/10).

**Kiểm (bắt buộc):** KC1, KC3, KC4, và:
1. Bộ mã hóa PNG nhỏ trong test (zlib `deflateSync`) ghi ảnh đã biết với cả 5 bộ lọc; giải mã ra đúng từng byte.
2. Thu nhỏ ảnh 768×432 hai màu kẻ ô 2 px ra màu trung bình đúng ±1/255.
3. PNG 16 bit và interlace báo đúng mã lỗi.

**Xong khi:** ba kiểm đạt.

#### MF-C04 · [codex-code] Đo ảnh (`cli look`)

**Cần trước:** MF-C03.

**Chỉ được ghi:** `tools/map-factory/lint/look.mjs`, `tools/map-factory/cli.mjs` (thêm lệnh `look`), `tools/map-factory/test/look.test.mjs`, `tools/map-factory/test/fixtures/look/*.json`.

**Việc:** trên ảnh 384×216 (từ PNG qua MF-C03 hoặc từ `.rgb`), tính đúng như script của Claude (Claude chép nguyên văn `stats.mjs`, `stats2.mjs`, `stats3.mjs` vào phiếu khi xếp):
- L = 0,2126r + 0,7152g + 0,0722b; HSV theo hàm `hsv` của script;
- `meanLuma`;
- `litGrass`: hue 65–160°, s > 0,3, L > 0,45: tỉ lệ, trung vị L, trung vị hue;
- `brightMeadow`: hue 65–160°, s > 0,3, L > 0,5;
- `veryDark`: V < 0,22;
- `darkTeal`: hue 170–235°, s > 0,2, L < 0,3;
- `warmAccent`: (hue < 22° hoặc > 340°), s > 0,45, V > 0,3, theo thứ tự lớp của `stats.mjs`;
- `violet`: hue 240–300°, s > 0,25, theo thứ tự lớp của `stats.mjs`;
- `soil`: hue 18–55°, 0,18 < s < 0,65, V > 0,45;
- `fineTexture`: trung bình |L − mờ hộp bán kính 2|;
- `largeContrast`: độ lệch chuẩn của mờ hộp bán kính 12;
- lưới luma 4 × 3.
- Dải ngưỡng đọc từ một file JSON (`captureBands`); in bảng ĐẠT/TRƯỢT từng dòng và JSON; thoát 1 nếu có dòng trượt.

**Kiểm (bắt buộc):** KC1, KC3, KC4, và:
1. Ảnh tổng hợp biết trước đáp án (màu đơn, bàn cờ, dải chuyển): mọi số khớp ±1e-6.
2. Không DOM, không gói ngoài.
3. Dải mẫu cho pine-river (từ kế hoạch §2.9 Q5) nằm trong fixture; ảnh tổng hợp "đạt hết" và "trượt 3 dòng" cho đúng kết quả.

**Xong khi:** ba kiểm đạt. Claude chạy lại trên file thô ảnh mẫu, spike, M0b (đã chép vào `tools/map-factory/.cache/look-anchors/`, bị bỏ qua bởi Git): ảnh mẫu 0,522 và 41,7 %, spike 0,422 và 20,6 % (±0,005).

#### MF-C05 · [codex-code] Metadata kit, `captureBands` và `check-kit`

**Cần trước:** MF-C04.

**Chỉ được ghi:** `tools/map-factory/registry/kits/{pine-river,meadow}.json`, `tools/map-factory/lib/kit.mjs`, `tools/map-factory/cli.mjs` (lệnh `check-kit`), `tools/map-factory/test/kit.test.mjs`, `tools/map-factory/test/fixtures/kits/*.json`.

**Việc:**
- Mỗi proto: `role` (enum: `tree`, `bush`, `rock`, `log`, `landmark`, `path-prop`, `cliff`, `water-edge`, `set-piece`, `tuft`), `nominalHeightCm`, `footprintCm`, `clearanceCm`, `hueClass` (`green`, `violet`, `warm`, `neutral`; không có `signal-*`), `castsShadow`, `tintable`, `lodClass`, `maxTris`. Giá trị lấy từ bảng Claude ghi trong phiếu.
- Mỗi kit: `palette`, `captureBands` (pine-river theo kế hoạch §2.9 Q5), `lighting` mặc định, tham số bố cục.
- `check-kit <kit>`: kiểm đủ trường, enum, dải.

**Kiểm (bắt buộc):** KC1, KC3, và:
1. `check-kit` thoát 0 với hai kit.
2. Fixture thiếu trường, `role` lạ, `hueClass: "signal-red"` thoát 1 với đúng mã.
3. Mọi GLB trong sổ 025 của `public/assets/dragon-hold/models/m0b/props` có mục; chiều cao bao (đọc từ đầu ra sổ 025, không mở GLB) lệch `nominalHeightCm` ≤ 20 %, hoặc được in ra.

**Xong khi:** ba kiểm đạt.

#### MF-C06 · [codex-code] MapSpec v1: kiểu và chuyển từ v0

**Cần trước:** CL-02.

**Chỉ được ghi:** `shared/game-kit/map/spec.ts`, `shared/game-kit/map/spec.test.ts`, `shared/game-kit/map/spec-v1.ts` (nếu tách).

**Việc:** thêm các khối (kế hoạch §2.10): `gameplay {adapter, commit, simHash, viewHash}`; `brief` (enum và phương vị, không tọa độ); `lighting {preset, sunAzimuthDeg, sunElevDeg, hemiGround, exposurePermille, mistStartCm}`; `scene` (mỗi vật lớn là `"auto"` hoặc ghim: `cliff`, `pond`, `openSector`, `forestEdge`, `groves`, `accents`, `paths[]` với `tier` và `destination`, `landmarks`, `gates[]` với `source` và `telegraph`); `layers.life`; `critics` (ghi đè ngưỡng, bắt buộc có `reason`); `approved` (băm từng lớp). Viết `migrateV0toV1`.

**Kiểm (bắt buộc):** KC1–KC3, và:
1. Hai spec v0 mẫu chuyển sang v1 và hợp lệ.
2. Chuyển hai lần cho cùng byte.
3. Spec v1 tối thiểu (mọi vật lớn `auto`) hợp lệ.

**Xong khi:** ba kiểm đạt.

#### MF-C07 · [codex-code] MapSpec v1: mã lỗi và mẫu hỏng

**Cần trước:** MF-C06.

**Chỉ được ghi:** `shared/game-kit/map/spec.ts`, `spec.test.ts`, `tools/map-factory/test/fixtures/bad-spec/v1-*.json`, `tools/map-factory/cli.mjs` (`validate` đọc v1).

**Việc:** `validateSpec` cho v1 với mã lỗi.

**Kiểm (bắt buộc):** KC1–KC3, và 10 spec hỏng thoát 1 với đúng mã: preset ánh sáng lạ; `sunElevDeg` ngoài 30–70; số thùy quầng ngoài 3–5; `rimCm` ngoài 15–25; `accent.minLaneGapCm` < 900; `grove.gapCm` < 800; số sự sống quá ngân sách; thiếu `simHash`; tọa độ trong `brief`; lối mòn không có `destination`.

**Xong khi:** 10 mẫu hỏng đúng mã, 2 mẫu tốt thoát 0.

#### MF-C08 · [codex-code] Khung camera trên mặt đất (`frame.ts`)

**Cần trước:** CL-02.

**Chỉ được ghi:** `shared/game-kit/map/frame.ts`, `frame.test.ts`.

**Việc:** từ yaw, pitch, khoảng cách, `lookM`, fov dọc, tỉ lệ khung và danh sách chữ nhật HUD (px ở 1280×720 và 1920×1080), tính đa giác khung trên mặt đất (y = 0) và đa giác "khung trừ HUD". Hàm `insideShare(polygon, frame)` (tỉ lệ diện tích, ‰). Lượng giác bằng bảng tra số nguyên theo độ (‰); thử với `Math` chỉ trong test.

**Kiểm (bắt buộc):** KC1–KC4, và:
1. Camera mặc định L2-cau (yaw 0, pitch 55, khoảng cách 95, `lookM` [0, −4], fov dọc 30°, 16:9; Claude xác nhận với `stage.ts` khi xếp): đáy khung z ≈ +22,2 m, đỉnh z ≈ −42,2 m, nửa bề ngang ở z = 0 ≈ 44,2 m, mỗi số ±0,3 m. (Ảnh đo được: x ±43, đáy +23.)
2. So với cách tính số thực trong test: lệch ≤ 10 cm ở mọi đỉnh trên 50 camera ngẫu nhiên.
3. `insideShare` của một đĩa nằm trọn trong khung = 1000 ‰; nằm trên mép = 500 ‰ ±10.

**Xong khi:** ba kiểm đạt.

#### MF-C09 · [codex-code] Định vị A: bãi trống, vịnh rừng, khe cổng

**Cần trước:** MF-C06. Claude ghi thuật toán trong phiếu (CL-02).

**Chỉ được ghi:** `shared/game-kit/map/siting.ts`, `siting.test.ts` (phần A).

**Việc:**
- `openSector(gameplay)`: hành lang mỗi làn (nửa bề rộng + 220 cm) trong r 900–2800 cm chiếm một khoảng phương vị; trả cung trống lớn nhất (tâm, độ rộng, độ).
- `ringBays(seed, ringRCm, gates, openSector)`: vịnh mỗi 60–90° (seed), sâu 600–1000 cm, bỏ qua khe cổng.
- `gateGaps(gameplay)`: mỗi cổng một khe rộng ≥ bề rộng làn + 600 cm; vệt đường tiếp ≥ 1600 cm ra ngoài.

**Kiểm (bắt buộc):** KC1–KC4, và:
1. `openSector` bằng cách tính vét cạn (quét từng 1°) trên 50 bố cục ngẫu nhiên.
2. L2-cau: cung trống chứa khoảng 95–200° (in tâm và độ rộng).
3. Khoảng cách vịnh nằm trong 60–90°; không vịnh nào trùng khe cổng.
4. Bố cục lật gương (x → −x) cho kết quả lật gương.
5. Băm vàng.

**Xong khi:** năm kiểm đạt.

#### MF-C10 · [codex-code] Định vị B: vách hướng nắng

**Cần trước:** MF-C09.

**Chỉ được ghi:** `siting.ts`, `siting.test.ts` (phần B).

**Việc:** `cliffArc(gameplay, sun, openSector, seed)`:
- phía cao = phương vị mặt trời + 180° ± 30°; cung 60–100°; r 3800–4600 cm;
- giữ đoạn có pháp tuyến ngang (hướng về tâm) · mặt trời ≥ 300 ‰, tính bằng cos(độ cao) × cos(Δ phương vị) từ bảng tra;
- cách tâm bãi trống ≥ 60°;
- chỗ một làn hay nước đi qua cung thì mở khe vực rộng ≥ bề rộng + 600 cm;
- ra: các đoạn vách, khe vực, 2–3 tầng.

**Kiểm (bắt buộc):** KC1–KC4, và:
1. Mọi đoạn trả về có tích ≥ 300 ‰ (kiểm lại bằng `Math` trong test, lệch ≤ 5 ‰).
2. Không đoạn nào cắt tia từ (0, 0) tới điểm làn trong r ≤ 26 m.
3. L2-cau với mặt trời phương vị 95°, cao 50°: cung nằm trong 215–300°, có khe vực chứa phương vị 257° (cổng Suối) và 240° (sông).
4. Mặt trời phương vị 222° (hướng hôm nay, Tây Nam): không đoạn nào ở 300–340° (vách hôm nay) được giữ.
5. Lật gương cho kết quả lật gương; băm vàng.

**Xong khi:** năm kiểm đạt.

#### MF-C11 · [codex-code] Định vị C: ao trong khung, vật gây cong

**Cần trước:** MF-C08, MF-C09.

**Chỉ được ghi:** `siting.ts`, `siting.test.ts` (phần C).

**Việc:**
- `pondSite(gameplay, heightField, frame, openSector, seed)`: ứng viên trên lưới 50 cm trong vành 1400–2300 cm; cách hành lang làn ≥ 220 cm + R, cách ô ≥ 460 cm + R, cách hình chiếu cung bay ≥ 200 cm + R, không đè sông; điểm = trũng (cao độ thấp) + trong khung (`insideShare` ≥ 800 ‰ là bắt buộc) + gần mép xa bãi trống. R 460 cm.
- `bendAnchors(gameplay)`: mỗi đỉnh làn quay ≥ 15° cho một điểm neo phía trong, trên đường phân giác, cách mép làn 300–600 cm.

**Kiểm (bắt buộc):** KC1–KC4, và:
1. Ao trả về thỏa mọi khoảng cách (kiểm vét cạn) và `insideShare` ≥ 800 ‰.
2. L2-cau: in vị trí; so với ứng viên (19, 7) của kế hoạch (in khoảng cách, không phải cổng).
3. L2-cau: đúng một điểm neo, ở khúc 21,2° của Đường Suối, phía trong.
4. Lật gương; băm vàng.

**Xong khi:** bốn kiểm đạt.

#### MF-C12 · [codex-code] Định vị D: lùm, lùm neo, cây lẻ

**Cần trước:** MF-C09, MF-C10.

**Chỉ được ghi:** `siting.ts`, `siting.test.ts` (phần D).

**Việc:** `groveSites(gameplay, openSector, cliff, seed, params)`:
- ≤ 7 lùm có tâm trong r ≤ 3000 cm; R 380–750 cm; 1–2 lùm neo R 700–900 cm ở phía cao, nối vào rừng mép;
- khoảng cách mép–mép giữa hai lùm ≥ 800 cm;
- không lùm nào trong cung trống; ở các nêm giữa hai làn; cách hành lang làn ≥ 220 cm;
- mỗi lùm một loài chủ (≥ 700 ‰) và 1–2 điểm nhấn (chỉ id loài, chưa đặt cây);
- cây lẻ: chỉ trong dải chuyển tiếp (giữa mép lùm và bãi trống), cách nhau 600–1000 cm.

**Kiểm (bắt buộc):** KC1–KC4, và:
1. Mọi ràng buộc trên kiểm vét cạn trên 100 seed của L2-cau.
2. Phần vành r 900–3000 cm (trừ làn) không bị lùm và cây lẻ phủ ≥ 400 ‰ trên mọi seed (in nhỏ nhất).
3. Lật gương; băm vàng.

**Xong khi:** ba kiểm đạt.

#### MF-C13 · [codex-code] Lối mòn A: lưới chi phí và A* số nguyên

**Cần trước:** MF-C09.

**Chỉ được ghi:** `shared/game-kit/map/paths.ts`, `paths.test.ts` (phần A).

**Việc:**
- Lưới 50 cm từ `raster.ts` và `edt.ts` (029).
- Cấm: hành lang làn (nửa bề rộng + 220 cm) trừ sân bệ; đĩa ô 460 cm; nước trừ chỗ băng khai báo (cầu, lội, đá bước).
- Chi phí mềm (số nguyên): dưới tán lùm ×4; dốc theo ‰; trong 1400 cm quanh làn, bước đi lệch hướng làn tại chỗ < 25° bị cộng phạt (lưới 8 hướng, chi phí theo hướng bước).
- A* 8 hướng, heuristic octile số nguyên, hòa thì chọn chỉ số nhỏ.

**Kiểm (bắt buộc):** KC1–KC4, và:
1. A* bằng Dijkstra vét cạn về chi phí trên 100 lưới nhỏ ngẫu nhiên.
2. Không ô nào của đường đi nằm trong vùng cấm.
3. ≤ 20 ms mỗi đường trên lưới 208² (in thời gian).

**Xong khi:** ba kiểm đạt.

#### MF-C14 · [codex-code] Lối mòn B: làm mượt, bậc, sân ngã ba, đích; đèn và điểm nhấn

**Cần trước:** MF-C13, MF-C12.

**Chỉ được ghi:** `paths.ts`, `paths.test.ts` (phần B).

**Việc:**
- `routeFootpaths(spec.scene.paths, ...)`: mỗi lối từ một đầu (sân bệ hay lối khác) tới **đích khai báo** (`pond-jetty`, `bridge-head`, `cliff-foot`, `set-piece`, `gate-track`, `fishing-spot`); làm mượt Chaikin số nguyên 2 vòng; lấy mẫu lại theo độ dài cung.
- Bậc: `trail` 150 cm, `spur` 90 cm.
- Sân ngã ba chỉ khi ≥ 3 lối gặp nhau trong 200 cm.
- Đèn: qua `along.ts` (033) mỗi 900–1200 cm, đổi bên, lệch 90 cm ngoài mép; bỏ cửa sổ cách ô < 460 cm và cách làn < 220 cm.
- Điểm nhấn ấm: 6–10 trong khung mặc định (MF-C08), cách nhau ≥ 1200 cm, cách làn và ô ≥ 900 cm, ưu tiên ngã ba và mặt ngoài lùm.

**Kiểm (bắt buộc):** KC1–KC4, và:
1. Mỗi lối kết thúc ở đích khai báo, không ở ô.
2. Không mép lối nào cách ô < 460 cm hay cách mép làn < 220 cm, trừ sân bệ.
3. Trong 1400 cm quanh làn, hướng lối lệch hướng làn ≥ 25° ở mọi đoạn.
4. Khoảng cách đèn = `everyCm` ± 1 cm.
5. Điểm nhấn thỏa mọi khoảng cách (vét cạn).
6. Băm vàng.

**Xong khi:** sáu kiểm đạt.

#### MF-C15 · [codex-code] Phép kiểm hợp lý A: nước, vách, lối, cầu và lội

**Cần trước:** MF-C10, MF-C14.

**Chỉ được ghi:** `shared/game-kit/map/checks/logic.ts`, `checks/logic.test.ts`, `tools/map-factory/test/fixtures/bad-scene/*.json` (phần A).

**Việc:** mã lỗi:
- `river-narrows-downstream`: bề rộng giảm theo hướng chảy khai báo mà không đổ vào ao hay đầm;
- `bridge-angle`: cầu lệch vuông góc dòng > 20°;
- `cliff-faces-away`: đoạn vách có tích với mặt trời < 300 ‰;
- `cliff-in-play`: vách ở r < 3600 cm;
- `path-ends-at-slot`, `path-no-destination`, `path-near-slot`, `path-near-lane`, `path-angle-near-lane`;
- `bridge-art-off-span`, `ford-art-off-span`: mốc lệch đoạn sim (mặt cầu = đoạn cầu + 50 cm mỗi đầu).

**Kiểm (bắt buộc):** KC1–KC4, và:
1. Mỗi mã một mẫu hỏng thoát 1 với đúng mã; một mẫu tốt thoát 0.
2. Bố cục spike L2-cau (Claude chép vào fixture: sông theo thứ tự lưu, vách NW với mặt trời (−0,55, 1,05, 0,62)) báo đúng `river-narrows-downstream` và `cliff-faces-away`.
3. Cùng bố cục với hướng chảy đảo và mặt trời phương vị 95°: không còn hai lỗi đó.

**Xong khi:** ba kiểm đạt.

#### MF-C16 · [codex-code] Phép kiểm hợp lý B: cổng, khúc cong, tiêu điểm, đường bắn, màu

**Cần trước:** MF-C08, MF-C15.

**Chỉ được ghi:** `checks/logic.ts`, `checks/logic.test.ts`, fixtures `bad-scene/` (phần B).

**Việc:** mã lỗi:
- `gate-no-source`, `gate-track-short` (< 1600 cm);
- `bend-no-cause`: khúc ≥ 15° không có vật gây cong trong 600 cm phía trong;
- `focal-out-of-frame`: ao, vách, mốc < 800 ‰ trong khung ở 1920×1080 hoặc 1280×720;
- `line-of-fire`: vật rắn cao > 120 cm cắt tia từ (0; 250 cm; 0) tới điểm làn trong vùng chữ (mỗi 100 cm), hoặc từ ô nhà tới điểm làn trong tầm;
- `colour-near-lane`: proto `hueClass` `violet` hay `warm` cách làn hoặc ô < 900 cm;
- `slot-hole`: khoảng trống hình ô (đĩa không vật quanh tâm ô lớn hơn xung quanh 2 lần) trong vùng rải.

**Kiểm (bắt buộc):** KC1–KC4, và:
1. Mỗi mã một mẫu hỏng đúng mã; một mẫu tốt thoát 0.
2. Bố cục spike L2-cau báo `focal-out-of-frame` cho ao ở (0, 23) (khoảng nửa ngoài khung).

**Xong khi:** hai kiểm đạt.

#### MF-C17 · [codex-code] Phép kiểm bố cục nhìn từ trên

**Cần trước:** MF-C12, MF-C14.

**Chỉ được ghi:** `shared/game-kit/map/checks/composition.ts`, `checks/composition.test.ts`.

**Việc:** tính và so ngưỡng Q4 (kế hoạch §2.9): phần vành trống; độ rộng cung trống; phần điểm ảnh của cung trống chiếu lên khung mặc định (MF-C08); số lùm và khoảng cách; tỉ lệ loài chủ; tiêu điểm trong khung; mốc mỗi góc phần tư. Ra JSON số và ĐẠT/TRƯỢT.

**Kiểm (bắt buộc):** KC1–KC4; mẫu hỏng cho từng ngưỡng đúng mã; mẫu tốt đạt.

**Xong khi:** kiểm đạt.

#### MF-C18 · [codex-code] `cli skeleton` và băm từng lớp

**Cần trước:** MF-C07, MF-C11, MF-C14, MF-C16, MF-C17.

**Chỉ được ghi:** `tools/map-factory/cli.mjs`, `shared/game-kit/map/skeleton.ts`, `skeleton.test.ts`, `tools/map-factory/test/skeleton.test.mjs`.

**Việc:** `cli skeleton <spec> --gameplay <extract> [--out out/<id>.skeleton.json]`: giải mọi trường `auto` của `scene` bằng `siting` và `paths`, giữ ghim, chạy phép kiểm hợp lý và bố cục, ghi khung cảnh và băm từng lớp (L2 vách, L3 nước, L4 lối, L5 đồ dọc đường, L6 neo thực vật, L8 điểm sự sống). Chỉ ghi vào `out/`.

**Kiểm (bắt buộc):** KC1–KC4, và:
1. Hai lần chạy cùng byte.
2. Đổi một tham số thực vật: chỉ băm L6 và lớp sau đổi.
3. Ghim một trường thì giá trị ghim đi ra nguyên văn.
4. In thời gian cho L2-cau (đích ≤ 300 ms trong Node; không phải cổng lúc nạp vì chạy offline).

**Xong khi:** bốn kiểm đạt.

#### MF-C19 · [codex-code] `cli guide`: guide.svg

**Cần trước:** MF-C18.

**Chỉ được ghi:** `tools/map-factory/lib/guide.mjs`, `tools/map-factory/cli.mjs` (lệnh `guide`), `tools/map-factory/test/guide.test.mjs`, `tools/map-factory/test/fixtures/guide/*.svg`.

**Việc:** SVG nhìn từ trên: làn có vạch mét, đoạn cầu và lội, id ô và vai trò ô, vòng phủ 10 m của ô nhà, vòng 6/8/12/26 m, cung bay; khung cảnh (phía cao, vách, nước có mũi tên chảy, ao, cung trống, nguồn cổng, bậc lối, mốc, đích); đa giác khung mặc định và vùng HUD; bảng số và kết quả kiểm.

**Kiểm (bắt buộc):** KC1, KC3, KC4; ảnh chụp SVG (snapshot) cho L2-cau; mọi id làn và ô có mặt; ≤ 200 ms; chỉ ghi `out/`.

**Xong khi:** kiểm đạt.

### 3.2 Worktree Rồng

#### MF-C20 · [codex-code] Đợt quái theo bản đồ; test bản đồ chạy mọi bản đồ

**Cần trước:** CL-02.

**Chỉ được ghi:** `src/content/data/waves.ts`, `src/content/data/stages.ts` (chỉ nếu cần tra bản đồ theo ải), `tests/content/map.test.ts`, `tests/content/waves-map.test.ts` (mới).

**Việc:** `waves.ts` hôm nay import `MAP_L2_CAU` để tính `zoneDelayMs`. Đổi thành hàm nhận MapDef (ví dụ `wavePlanFor(map)`), bản đồ tra từ ải. `map.test.ts` lặp qua mọi mục của `MAPS`. Không đổi hành vi.

**Kiểm (bắt buộc):** KR1–KR4, và:
1. Bảng `zoneDelayMs` mọi làn × quái trên L2-cau bằng đúng giá trị cũ (test so bảng ghi trước khi sửa).
2. Một MapDef lật gương (x → −x) trong test cho cùng bảng.
3. `pnpm dh:balance --seeds=20 --json` cho cùng đầu ra trước và sau (in md5).

**Xong khi:** ba kiểm đạt.

#### MF-C21 · [codex-code] Báo cáo cân bằng: cột theo làn, theo ô, theo Herb Hut

**Cần trước:** MF-C20.

**Chỉ được ghi:** `scripts/balance/report.ts`, `scripts/balance/meter.ts` (chỉ thêm bộ đếm), `tests/balance/report-columns.test.ts` (mới).

**Việc:** chỉ báo cáo, không đụng sim:
- mỗi làn: tỉ phần sức ép đất, số giết, sát thương lên Rồng, số lọt;
- mỗi ô: tỉ lệ được đặt, tỉ phần giết;
- Herb Hut: số nhịp theo ô nhà;
- nền cho G14: tỉ phần món trong các bộ tốt nhất.

**Kiểm (bắt buộc):** KR1–KR4, và:
1. Trên 20 seed, tổng theo làn và theo ô bằng tổng hiện có.
2. Cùng seed, tỉ phần đợt 7 của Đường Cầu ra 58,2 % ±1 điểm (Phát hiện 40).

**Xong khi:** hai kiểm đạt.

#### MF-C22 · [codex-code] Lint chiến thuật A: hình học làn và thời gian

**Cần trước:** MF-C20.

**Chỉ được ghi:** `scripts/maps/lint-map.ts`, `scripts/maps/metrics-lane.ts`, `package.json` (thêm `dh:map-lint`), `tests/maps/lint-lane.test.ts`.

**Việc:** dùng `compileLanes`, `alongAtRadius`, `inWordZone`, hằng số `rules.ts`. Tính: độ dài, bán kính cổng, độ quanh co, các khúc và góc, đơn điệu hướng tâm trong 26 m, điểm vào vòng, thời gian mỗi lớp quái (trước vùng, trong vùng, tổng; bị chặn bởi T_a hay vòng) ở hồ sơ tham chiếu (k = 1, biên 1,219), sàn Q, khoảng cách làn và chỗ cắt, phương vị đầu làn, nón 60° và đĩa 4 m, tỉ lệ nghẽn, thời gian lội. Luật cứng H1–H4, H12 (kế hoạch §2.2). Ra JSON.

**Kiểm (bắt buộc):** KR1–KR4, và trên L2-cau (±0,05 m, ±0,5°, ±0,1 s):
1. Độ dài 24,59 / 25,29 m; cổng r 30,22 / 30,81 m; độ quanh co 1,015 / 1,019.
2. Khúc Suối 21,2°; vào vòng ở 4,35 / 4,95 m; khoảng cách làn nhỏ nhất 9,15 m; phương vị đầu làn 4° / 266° (= −94°).
3. Cung bay 24,3 m, kết thúc ở r 7,5.
4. Tỉ lệ cầu 1,13 (H12 trượt, mã `choke-not-real`); lội ×1,43 trên 7,1 m.
5. E09: trước vùng 2,5 / 2,9 s, tổng 12,3 / 12,6 s; vùng chữ E09 bắt đầu ở 5,09 m dọc Đường Cầu.
6. Thời gian trước vùng của lint **bằng đúng** `zoneDelayMs` của `waves.ts` cho mọi làn × quái.
7. Bản đồ hỏng tổng hợp trượt đúng luật: làn 22 m (H1), làn đi ra rồi vào lại (H2), hai làn cách 6 m (H3).
Số nào lệch fixture: dừng và báo; Claude kiểm lại fixture trước khi bên nào đổi.

**Xong khi:** bảy kiểm đạt.

#### MF-C23 · [codex-code] Lint chiến thuật B: ô, ô nhà, cung bay

**Cần trước:** MF-C22.

**Chỉ được ghi:** `scripts/maps/lint-map.ts`, `scripts/maps/metrics-slots.ts`, `tests/maps/lint-slots.test.ts`.

**Việc:** luật H5–H11 và số mềm S4–S9: ô bẫy (số, khoảng cách, ≥ 8 m, không trong lội, r ≤ 25,5 m trừ `hold`), phần bẫy trong vùng chữ E09 (hồ sơ tham chiếu), điểm chặn, vai trò ô nhà và độ phủ ở 6–16 m, ô chung, ô chết, độ lộ với chỗ đứng của E11 (12 m) và E01 (10 m), tầm với tới đầu cung bay (Net Launcher 10 m, Owl Hunter 12 m, Watchtower 16 m), số ô so với vàng (in để bot kiểm G13b). Vai trò đọc từ trường `role` nếu có; không có thì suy và báo `role-missing`.

**Kiểm (bắt buộc):** KR1–KR4, và trên L2-cau (±0,05 m):
1. `cau-t1` ở r 26,32: H5 trượt, mã `trap-outside-ring`; dời trong RAM sang 5 m: r 25,35, đạt.
2. Ở 10 m: `h-nw` 7,4 m Cầu và 6,1 m Suối (ô chung duy nhất); `h-se` 0 m (`pad-no-lane`); `h-e` 12,9 m Cầu; `h-w` 18,3 m Suối.
3. Net Launcher tới đầu cung bay chỉ từ `cau-t4` (9,4 m).
4. Đúng năm phát hiện của kế hoạch §3.4 cổng D, không thêm không bớt.
5. Bản đồ hỏng tổng hợp trượt đúng H5, H6, H7, H8.

**Xong khi:** năm kiểm đạt.

#### MF-C24 · [codex-code] `prepare-ground` và `prepare-decals`

**Cần trước:** không.

**Chỉ được ghi:** `scripts/assets/prepare-ground.mjs`, `scripts/assets/prepare-decals.mjs`, `package.json` (hai lệnh), `tests/assets/prepare-ground.test.mjs`, `src/view/ground-manifest.ts` (bộ đọc manifest, chưa nối vào phần vẽ).

**Việc:** từ `art-src/ground/<kit>/` và `art-src/decals/<kit>/` ra `public/assets/dragon-hold/{ground,decals}/<kit>/` theo mẫu `prepare-models` (cỡ, WebP), kèm manifest (tên, md5, byte). Test chạy trên ảnh tổng hợp trong thư mục tạm; **không chạy trên media thật** (Claude chạy).

**Kiểm (bắt buộc):** KR1–KR4, và:
1. Manifest tất định (hai lần cùng byte).
2. `git check-ignore` trả đường dẫn đầu ra (media không vào Git).
3. `grep -rn "/art-src/" src/` không in gì từ file mới.

**Xong khi:** ba kiểm đạt.

#### MF-C25 · [codex-code] Đồ thị mẫu: lược đồ và kiểm hợp lệ

**Cần trước:** CL-07 (Claude viết `TEMPLATE_GRAPH.md` và ba file đồ thị).

**Chỉ được ghi:** `scripts/maps/graph/spec.ts`, `tests/maps/graph-spec.test.ts`, `tests/maps/fixtures/graph-bad/*.json`.

**Việc:** kiểu và `validateGraph` theo `docs/tools/map-factory/TEMPLATE_GRAPH.md`: loại nút (kế hoạch §2.2), cạnh, dải, rung, ghim, khối đầu ra. Lỗi kèm đường dẫn JSON.

**Kiểm (bắt buộc):** KR1–KR4, và: ba đồ thị của CL-07 hợp lệ; ≥ 12 mẫu hỏng đúng mã (cổng ngoài 28–32 m; khúc thiếu `cause`; nước không có `from`/`to`; nghẽn không có `type`; cung bay cách cổng đất < 40°; ghim sai kiểu…).

**Xong khi:** kiểm đạt.

#### MF-C26 · [codex-code] Đồ thị mẫu: sinh làn, nghẽn, cung bay, `lookM`

**Cần trước:** MF-C25, MF-C22.

**Chỉ được ghi:** `scripts/maps/graph/instantiate.ts`, `tests/maps/graph-instantiate.test.ts`.

**Việc:** seed + đồ thị → khung chơi: hướng từ dải phương vị cổng và lật gương (không xoay tự do); cổng, nghẽn, tách, nhập trong dải; làn cong bán kính ≥ 400 cm, polyline dây cung ≤ 150 cm, làm tròn cm; đoạn cầu và lội; cung bay; `lookM` theo luật khung (H10, dùng `frame.ts` của kit sau sync). Node, số thực được phép; đầu ra cm nguyên. Nút ghim đi qua nguyên văn.

**Kiểm (bắt buộc):** KR1–KR4, và:
1. Bản ghim L2-cau cho khung chơi có `simHash` bằng bản trích của MF-C02.
2. 100 seed mỗi mẫu L2-l, L2-doi: cùng byte hai lần, hai tiến trình; không NaN.
3. Mọi giá trị rung nằm trong dải khai báo (kiểm thuộc tính).
4. ≤ 50 ms mỗi seed (in).

**Xong khi:** bốn kiểm đạt.

#### MF-C27 · [codex-code] Đồ thị mẫu: sinh ô và chế độ so với ô ghim

**Cần trước:** MF-C26, MF-C23.

**Chỉ được ghi:** `scripts/maps/graph/slots.ts`, `tests/maps/graph-slots.test.ts`.

**Việc:** sinh ô từ làn: luật 03 (bẫy 3–5 mỗi làn, cách 5–7 m, ≥ 8 m từ tâm, không trong lội; chặn 2–3, ưu tiên nghẽn, khúc cong, đoạn chậm; ô nhà trong 4–6 ở 7–10 m, ngoài 2–4 ở 14–20 m gần tách, nhập, nghẽn) và H5–H8 (bẫy r ≤ 25,5 m; vai trò ô nhà; ≥ 1 ô chung khi ≥ 2 làn; ô với tới đầu cung bay, đích 2). Chế độ `--check` so ô ghim với luật và in khác biệt.

**Kiểm (bắt buộc):** KR1–KR4, và:
1. 100 seed × 3 mẫu: mọi luật đạt (lint MF-C23 sạch).
2. `--check` trên L2-cau ghim báo `cau-t1` (r 26,32), `h-se` (0 m trong 10 m), tầm với cung bay 1.

**Xong khi:** hai kiểm đạt.

#### MF-C28 · [codex-code] Quét seed và dấu vân tay

**Cần trước:** MF-C27.

**Chỉ được ghi:** `scripts/maps/graph/sweep.ts`, `scripts/maps/graph/fingerprint.ts`, `package.json` (`dh:map-sweep`), `tests/maps/graph-sweep.test.ts`.

**Việc:** `dh:map-sweep <mẫu> --seeds 64`: sinh, lint, xếp theo khoảng cách tới vector đích của mẫu; in tỉ lệ đạt luật cứng, thời gian mỗi seed, top 3, và ghi seed tốt nhất ra `out/` (không vào Git). Dấu vân tay: phương vị cổng, phương vị bãi trống, phía mặt trời, loại nước, bộ mốc; hàm khoảng cách.

**Kiểm (bắt buộc):** KR1–KR4, và: L2-l và L2-doi mỗi mẫu 64 seed, ≤ 1 s mỗi seed, in tỉ lệ đạt (cổng ≥ 50 % là của CL-08, phiếu chỉ in); khoảng cách vân tay bằng 0 với chính nó, đối xứng.

**Xong khi:** kiểm đạt.

---

## 4. Làn Claude (bản thử)

| Mã | Việc | Được ghi | Xong khi |
|---|---|---|---|
| CL-01 | **Chấm 8 ảnh đợt 3 trước Tripo** (`lantern-post`, `rail-fence`, `cliff-rock-a`, `cliff-rock-b`, `grass-tuft`, `wildflower-clump`, `reed-clump`, `wooden-jetty`; Codex tự chấm 9–9,5). Kiểm Cliff Rock nhạt, cạnh gãy, không tròn rêu; màu so với màu tín hiệu và vàng Héo. Viết danh sách Tripo cho chủ dự án | `docs/codex-queue/046-report.md` (phần duyệt), danh sách trong tin nhắn | Mỗi ảnh ≥ 8 theo Claude, hoặc trả Codex (≤ 3 lượt); danh sách có tên file, thư mục tải lên, face limit, credit (khoảng 240) |
| CL-02 | **Nền.** Gộp `map-factory` (027–029, 031, 033) vào nhánh làm việc; tạo `games/.wt-dh-mapcodex` (nhánh `map-codex`) và `games/.wt-dh-mappilot` (nhánh `map-pilot`) từ Rồng `main` 02fe9c7; chép file thô đo ảnh vào `tools/map-factory/.cache/look-anchors/`; xếp phiếu MF-I1..I6, MF-C01..C28 với số trống kế tiếp và dòng `CODEX_QUEUE.md`; ghi thuật toán chính xác vào MF-C09..C14 (từ spike `layout.ts` §6, bỏ hằng số tay); bảng metadata cho MF-C05; xác nhận camera (fov 30°, `stage.ts` L201) cho MF-C08 | `docs/codex-queue/**`, `docs/CODEX_QUEUE.md`, `docs/tools/map-factory/**` | Lõi gộp, test lõi đạt trên nhánh làm việc; hai worktree tồn tại; phiếu đã xếp |
| CL-03 | **Bộ giám khảo:** lời nhắc (13 điểm con, điểm chung, đạt/trượt AFTER), mẫu hiệu chuẩn (ảnh mẫu 10, M0b ≈ 4,75, spike ≈ 6,75, dung sai 0,75), luật người thứ hai (±0,5 quanh cổng), từ điển góp ý (≥ 12 câu thường gặp → tham số spec) | `tools/map-factory/docs/judge.md` | Một giám khảo mới chạy trên ba mẫu, mỗi số trong ±0,75 |
| CL-04 | **A1 Đưa spike vào game.** Trong `.wt-dh-mappilot`: chép commit spike f491432..f7f1576; dời đường vách, 5 lối mòn, vị trí ao và lùm vào `src/view/maps/L2-cau.map.json` (cảnh ghim); chạy `prepare-ground`, `prepare-decals` (MF-C24) để bỏ `/art-src` | `games/.wt-dh-mappilot/**` | Golden `m0.json` và `map.test.ts` không đổi; `pnpm check` đạt; bản build không gọi `/art-src`; số đo ảnh ±0,01 so với spike `final2` (ngang bằng); nạp ≤ 300 ms |
| CL-05 | **A2 Sửa rẻ và bố cục.** V2 (bỏ stroke phân bậc trong bãi trống), ánh sáng (mặt trời khoảng 95°, cao 50°; màu đất bán cầu #6d7a5a; bóng lam; sương ngoài 50 m), V3 viền và thùy, V13 hue, V14 decal gom mép, sỏi xám, bỏ chấm đỏ, viền bệ; bố cục kế hoạch §3.2 (ghim tay); cây tán ấm bằng nhuộm cây tròn có sẵn, bật/tắt A/B; chấm thử cây nhuộm, < 8 thì gọi MF-I2 cho OW-02 | như trên | Số đo ảnh tiến về ngưỡng Q5; `dh-crowd` đạt; golden giữ; tờ trước/sau đã xem |
| CL-06 | **A3 Nướng và cổng A.** Nướng mặt nạ, ô đất, decal vào render target 2048² lúc nạp; đo `dh-map-bench` (đổi tên từ `dh-mapspike-bench`); chụp 12 ảnh; giám khảo mới; trang so sánh số 1 (Artifact riêng tư, có ô ghi chú) | như trên | Cổng A của kế hoạch §3.4 |
| CL-07 | **B1 Đồ thị và brief.** Viết `docs/tools/map-factory/TEMPLATE_GRAPH.md` (loại nút, cạnh, dải, rung, ghim, đầu ra); đồ thị L2-cau (mẫu + bản ghim tái hiện `MAP_L2_CAU`), L2-l, L2-doi trong `src/content/data/layouts/`; brief và spec v1 của L2-cau với trường `auto` | `docs/tools/map-factory/**`, `.wt-dh-mappilot/src/content/data/layouts/**`, `src/view/maps/**` | MF-C25 nhận cả ba; bản ghim không có tọa độ ngoài ghim khung chơi |
| CL-08 | **B2 Nối lõi và thử tổng quát.** Kit sync lõi vào `.wt-dh-mappilot`; phần vẽ đọc khung cảnh từ `cli skeleton`; so bản suy ra với bản ghim A; chạy thử tổng quát (lật gương, 3 seed, L2-l, L2-doi qua MF-C28 và hộp cát dev) | như trên | Cổng B của kế hoạch §3.4; ngoại lệ ghim (nếu có) ghi trong spec với lý do |
| CL-09 | **C1 Kit vào.** GLB của OW-01/02: Blender `--kind props`, `prepare-models`, chấm ≥ 7, metadata sổ; đặt theo luật: đèn, rào, tầng vách và bãi đá, cỏ và hoa ở mép, lau và cầu tàu, Campfire Ring | như trên, media qua `pnpm media:push` | Đèn không gần ô < 4,6 m hay làn < 2,2 m, khoảng cách ±1 m; prop ≤ 550 k tam giác lượt chính; Q3, Q5 đạt |
| CL-10 | **C2 Sự sống, bậc, Firefox, ảnh chụp.** Lớp L8 (kế hoạch §2.5) từ sprite MF-I3/I4; bậc Medium và Low (Low: không decal, ít vật, tắt sự sống trừ sông); `dh-map-shots`: 3 góc × 4 hướng 1080p, mặc định 720p, nheo mắt, AFTER (mọi ô đã xây, quái đợt 7 có thẻ), dải 10 s (20 khung), PNG; `dh-map-bench` ba bậc; một lượt Firefox | như trên | Sự sống ≤ 0,15 ms, ≤ 3 draw call; không gì động thấp hơn 8 m trên vùng chữ hay thẻ; Q7 ba bậc; Firefox có số hoặc ghi "chưa đo" |
| CL-11 | **C3 Cổng C và gộp.** Giám khảo mới (hiệu chuẩn trước); người thứ hai nếu sát cổng; trang so sánh số 2 (ảnh mẫu, M0b, spike, bản mới, 12 ảnh, AFTER, nheo mắt, 720p, dải sự sống, số đo, guide.svg); chủ dự án duyệt; ghi chú đổi thành tham số qua từ điển, sửa một vòng; gộp `map-pilot` vào `main` của Rồng; changelog `docs/changelog/<ngày>-map-pilot.md` | repo Rồng `main` | Cổng C; chủ dự án nói "đạt" |
| CL-12 | **D Thang chiến thuật.** Lint trên v1; v2a, v2b, v2c (kế hoạch §3.3) mỗi bước trên 2 × 300 seed cùng bản gốc; bảng G1–G16, B1–B9, D23 so cả dải BALANCE.md chung và dải game; cột MF-C21; bảng dự đoán | `.wt-dh-mappilot` (nhánh con cho mỗi ứng viên), changelog | Cổng D; ứng viên chỉ giữ khi mọi cổng đạt cả hai họ; golden đổi có chủ ý; không giữ thì ghi số và lý do |
| CL-13 | **Tài liệu và canon.** Mục "Map Factory v2" trong MAP_FACTORY (giai đoạn, §6.5 cũ, §11 dòng Survival); spike §8 (đã có giám khảo thứ hai 6,75); đề xuất canon (dải làn, vai trò ô, ba mẫu sửa, nghẽn thật, luật cây ấm, trần tam giác theo phần chênh); SURVIVAL_MODE_PLAN §4.1 (24 × 40 m), §4.0; Lời Gọi §22.9 | `docs/**`, changelog từng game | Mỗi ghi chú dẫn mục nguồn; tiếng Việt có dấu; không gì trình chủ dự án như "đã quyết" khi cần ông quyết (chỉ credit) |

---

## 5. Việc của chủ dự án (bản thử)

| Mã | Việc | Thời gian | Credit | Claude kiểm |
|---|---|---|---|---|
| OW-01 | Dựng 8 món đợt 3 trên web Tripo theo danh sách CL-01 (`typing-game-handoff-2026-10-25/tripo-upload-dot3`); thả GLB vào thư mục `art-src/3d` tương ứng | khoảng 60 phút | khoảng 240 | Mỗi GLB ≥ 7 (hoặc ghi tạm); trần tam giác: đèn và rào 600, Cliff Rock 800, cỏ 300, lau 400, cầu tàu 1.500; metadata |
| OW-02 | Dựng Campfire Ring (sau MF-I1); Maple Tree chỉ khi CL-05 báo cây nhuộm < 8 | 10–20 phút | 30–120 | ≥ 7; Campfire ≤ 2.500 tam giác, Maple ≤ 1.500; màu tán đo trong ảnh dựng vẫn trong dải MF-I2 |
| OW-04 | (Không bắt buộc) Xem trang so sánh số 1, ghi chú | 10 phút | 0 | Ghi chú đổi thành tham số |
| OW-03 | Xem trang so sánh số 2, chơi L2-cau 10 đợt, nói "đạt" hoặc ghi chú bằng lời của mình | 30 phút | 0 | Ghi nhận; thay đổi đi qua một vòng CL-11 |

---

## 6. Phiếu triển khai (sau GO, khoảng 17/11)

Luật chung như mục 1. Phiếu ảnh của Lời Gọi ghi vào `games/typing-defense/art-src/`, của Tuyến Cuối vào `games/typing-survival/art-src/`; phiếu mã của Lời Gọi chỉ ở repo cha (đọc bản trích 028); phiếu mã của Tuyến Cuối trong worktree riêng `games/.wt-ts-mapcodex` theo luật 1.3 (thay Rồng bằng Tuyến Cuối).

### 6.1 Ảnh Codex

| Mã | Việc | Chỉ được ghi | Kiểm (bắt buộc, cộng KA1–KA5) | Xong khi |
|---|---|---|---|---|
| MF-I7 | Lời Gọi: 3 ô đất đồng cỏ (cỏ sáng, cỏ vừa, đất mòn) | `games/typing-defense/art-src/scenery/meadow/ground/*` | Liền mép (lát nửa ô); 1024²; hue trung vị cỏ 86–96°; màu lấy từ bộ `meadow` có sẵn | Tự chấm ≥ 8 |
| MF-I8 | Lời Gọi: 3 ô đất (mép đất–cỏ, đất sỏi, bờ ẩm) | như trên | như trên | Tự chấm ≥ 8 |
| MF-I9 | Lời Gọi: 2 tờ decal (mảng đất mòn; hoa và sỏi) | `.../meadow/decals/*` | Lưới cố định, JSON, alpha sạch, KA4 = 0 % | Tự chấm ≥ 8 |
| MF-I10 | Tuyến Cuối: 2 ảnh ý tưởng sân (cho chủ dự án chọn làm ảnh mẫu) | `games/typing-survival/art-src/reference/*` | Nhìn từ góc camera của game; sân giữa trống; quái và thẻ không có | Tự chấm ≥ 8 |
| MF-I11 | Tuyến Cuối: phông tinh vân, 2–3 lớp | `.../art-src/backdrops/nebula/*` | 4096×1024, liền mép ngang; lớp xa luma trung bình ≤ 0,35; không màu tín hiệu của Tuyến Cuối | Tự chấm ≥ 8 |
| MF-I12 | Tuyến Cuối: phông vành đai thiên thạch | `.../backdrops/asteroid-belt/*` | như MF-I11 | như trên |
| MF-I13 | Tuyến Cuối: phông trạm vỡ | `.../backdrops/broken-station/*` | như MF-I11 | như trên |
| MF-I14 | Tuyến Cuối: tờ decal sàn (bẩn, cháy, đường nối tấm, sọc cảnh báo) | `.../art-src/decals/deck/*` | Lưới, JSON, alpha sạch; sọc cảnh báo dùng màu riêng đã có của game | như trên |
| MF-I15 | Tuyến Cuối: ảnh nguồn Tripo cho món còn thiếu sau CL-20 (≤ 4, ví dụ Antenna Mast, Cargo Stack, Coolant Tank, Broken Turret) | `.../art-src/props/arena/*` | Như ảnh nguồn Tripo (nền #E6E6E6, lề 24 px) | như trên |
| MF-I16 | Rồng violet-glade: ảnh mẫu kit (một khung cảnh nhìn 55°) | `games/dragon-hold/art-src/reference/violet-glade.*` | Bố cục theo luật V; dùng để đặt `captureBands` | như trên |
| MF-I17 | Rồng violet-glade: ảnh nguồn Glow Mushroom, Glade Arch, Crystal Rock | `.../art-src/props/violet-glade/*` | Như 046; màu ngoài dải tín hiệu khi gần làn | như trên |
| MF-I18 | Rồng violet-glade: 8 ô đất, 4 tờ decal (chia 2 phiếu khi xếp) | `.../art-src/{ground,decals}/violet-glade/*` | Như MF-I5, MF-I6 | như trên |
| MF-I19 | Rồng hill-meadow: ảnh mẫu kit + 2–3 ảnh nguồn (Windmill, Dry-stone Wall, Hill Oak), sau khi kiểm nhập mốc Lời Gọi | `.../art-src/{reference,props/hill-meadow}/*` | Như MF-I16, MF-I17 | như trên |

### 6.2 Mã Codex

| Mã | Việc | Chỉ được ghi | Kiểm (bắt buộc, cộng KC/KR) | Xong khi |
|---|---|---|---|---|
| MF-C29 | Rải lùm trong lõi (030 viết lại, phần A): cha–con, loài chủ ≥ 700 ‰, điểm nhấn, tầng dưới, theo khung cảnh | `shared/game-kit/map/scatter.ts`, test | Khoảng cách nhỏ nhất đúng mọi cặp (vét cạn); loài chủ ≥ 70 % mỗi lùm; ≤ 15 ms cho cỡ L2-cau; băm vàng; so đầu ra bản thử (số thực, làm tròn cm) bằng số đo ảnh, không bằng byte | Kiểm đạt |
| MF-C30 | Rải lấp trong mặt nạ (030 phần B): nhiễu xanh theo ô, xếp hạng, tăng mật độ chỉ thêm vật, ghim | `scatter.ts`, test | Trên 100 seed, tập 350 ‰ nằm trọn trong tập 550 ‰; không vật trong vùng cấm; decal bãi trống ≤ 300 ‰ lưới v0 | Kiểm đạt |
| MF-C31 | Mặt nạ sơn đất trong lõi: quầng hai tông, viền, thùy, bậc lối, đồng yên, cụm decal | `shared/game-kit/map/paint.ts`, test | Viền rộng đúng ±1 ô; không đĩa nào tròn ≥ 0,95; tâm đĩa lệch về phía khuất nắng trong 10°; ≤ 80 ms cho 416² | Kiểm đạt |
| MF-C32 | Kế hoạch sự sống trong lõi (L8): đường bay chim, vùng bướm, nguồn khói, cây rơi lá, tham số bóng mây | `shared/game-kit/map/life.ts`, test | Không điểm nào trong 300 cm quanh làn; đường chim ngoài hai phần ba trong của khung; số trong ngân sách; băm vàng | Kiểm đạt |
| MF-C33 | `cli diff`: bản đồ đã duyệt có băm lớp đổi | `tools/map-factory/{cli.mjs,lib/diff.mjs}`, test | Mẫu đổi thực vật chỉ liệt kê L6 trở đi; tất định | Kiểm đạt |
| MF-C34 | Rồng `stages:gen`: điền ải từ file chương (04 §11) theo tỉ lệ làn 04 §3.2, ≤ 3 ải liền cùng mẫu, khác biệt theo vân tay với 10 ải trước, ghi JSON ải có `simHash`, `viewHash` | worktree Rồng: `scripts/stages/gen.ts`, test | 20 ải C1 tất định (chạy lại cùng băm); ràng buộc khác biệt giữ; không sinh khung chơi lúc nạp | Kiểm đạt |
| MF-C35 | Rồng `stages:validate`: lint chiến thuật, hợp lý, luật ghép 04 §5.6, lịch dạy | `scripts/stages/validate.ts`, test | Mẫu hỏng cho từng nhóm đúng mã; 20 ải C1 đạt | Kiểm đạt |
| MF-C36 | Bảng bản đồ: phần lõi không DOM (ghim ghi chú, hoàn tác, chọn vật, lược đồ file duyệt) | `shared/game-kit/map/board/*.ts`, test | Hoàn tác và làm lại (kiểm thuộc tính); chuyển đổi tọa độ khứ hồi ≤ 1 mm; lược đồ duyệt có mẫu hỏng | Kiểm đạt |
| MF-C37 | Lời Gọi lint A: độ dài tuyến, trường phủ 9 m và 12 m, chỗ phủ cả hai nhánh | `tools/map-factory/lint/td.mjs`, test | Tây 116,0 m, Đông 112,6 m trên nút (±0,5); 77 chỗ ở 9 m, 277 ở 12 m; chỗ 12 m tốt nhất phủ 42 m; tâm Rainbow Hill (2, −21): 12 m phủ 28 m (Tây 18, Đông 10) ±1 m, 13,2 m phủ 36,5 m ±0,5 | Kiểm đạt |
| MF-C38 | Lời Gọi lint B: đoạn chết (giây boss đi không chỗ xây nào trong 12 m), người đi bộ chỉ qua cầu, độ lộ mỏ dưới đường bay, nhà quan trọng cách 15–35 m; bí danh `td-sandbox` ↔ `w1-silverfall` | `lint/td.mjs`, `adapters/typing-defense*.mjs`, test | Đoạn chết in ra và so với khoảng 50 s của BUILD_1B §4.2; mẫu hỏng đúng mã | Kiểm đạt |
| MF-C39 | Tuyến Cuối: lược đồ `FieldPreset` (hành lang, hai đầu, đoàn xe, trạm giữa) và số đo (thời gian tới tầm theo quái, độ sâu khe sinh so với tầm súng, dàn ngang so với nón Tán 9 m) | worktree Tuyến Cuối: `scripts/maps/field.ts`, test | Hành lang hôm nay: mìn 2,6 m/s từ 40 m tới 10 m mất 11,5 s (±0,1); khe RIFT z 13–17 đúng | Kiểm đạt |
| MF-C40 | Bộ sinh dải set-piece (`shared/game-kit/map/strip.ts`): chuỗi mô-đun dọc z từ `FieldPreset`, chỉ ở dải bên x 12–22 | `strip.ts`, test | Chạy lại cùng byte; không mô-đun nào trong \|x\| ≤ 12, z 2,4–40 hay dải khe sinh; đổi seed chỉ đổi lựa chọn biến thể; băm vàng | Kiểm đạt |

### 6.3 Làn Claude

| Mã | Việc | Xong khi |
|---|---|---|
| CL-14 | Chuyển phần rải và sơn đất của bản thử sang lõi (duyệt MF-C29..C32), kit sync vào Rồng, ngang bằng số đo ảnh | Q5 trong ±0,005 so với bản thử; golden giữ |
| CL-15 | Bảng bản đồ v1 của Rồng (`?view=mapboard`, chỉ dev): guide và hình thật, khung chơi khóa, tay cầm cảnh, đổi seed cảnh, biến thể, điểm số, ghim ghi chú, nút duyệt | `grep` bản build không có mã bảng; sửa trên bảng không bao giờ đổi `simHash` (test); dùng được ở 1280×720 |
| CL-16 | Rồng R1 (C1): đồ thị L1-thang, L1-s, L1-xoan (móc ≤ 36 m); hiệu chuẩn mẫu; phép thử độ nhạy (3 seed × 2 × 300, cổng lệch ≤ ±3 điểm); `stages:gen` cho 20 ải; bot mỗi ải; ải 1, 10, 20 dựng tay; trang trí cổng theo họ quái; tờ ghép 20 ải | Mỗi ải đạt lint và bot; bảng hệ số mẫu; chủ dự án duyệt tờ ghép |
| CL-17 | Rồng R2 (C2–C3): biến thể hè (preset); họ seed L2; gói kit violet-glade (`captureBands` từ ảnh mẫu kit, bảng luật, Glow Mushroom là vật mang chữ qua bot) | Kit `artApproved`; cơ chế chữ ký qua bot 2 × 300 |
| CL-18 | Lời Gọi ngay: đọc kết quả MF-C37/C38; đề xuất cho làn Lời Gọi (Rainbow Hill, Watchtower, đoạn chết ≤ 15 s); sửa §22.9 và MAP_FACTORY §6.5; lớp phủ trong `debug-2d` khi làn rảnh | Tài liệu dẫn mục; không đổi luật chơi Lời Gọi ngoài bot của nó |
| CL-19 | Lời Gọi 1C: brief w1-silverfall, cảnh billboard theo §23.10, mốc có sẵn, sơn lại cục bộ khi xây nhà (≤ 4 ms, chia khung), lối nhánh từ cửa nhà | Q1, Q3–Q8 với ngân sách §25.12; golden luật giữ; chủ dự án chơi |
| CL-20 | Tuyến Cuối: viết phiếu sửa đọc chéo model Space cho làn Tuyến Cuối (`vite.config.ts` L13–24, AGENTS.md L98) **trước** việc sân; kiểm sổ 025 tìm món sci-fi nhập được; danh sách Tripo ≤ 4; tài liệu sân (dải bên, phông, hiểm họa, mẫu mục tiêu); dựng lại Vành Chân Trời chỉ phần nhìn | Không đường chạy nào mới vào Space; số đo ảnh theo ảnh mẫu đã chọn; giám khảo ≥ 8; hiệu năng của game đạt; golden giữ; chủ dự án duyệt |
| CL-21 | Gói kit (mẫu cho mỗi kit mới): kit json (luật, bảng màu, `captureBands`, ánh sáng, tham số bố cục), nút chữ ký và hỗ trợ sim, ô và billboard từ Codex, bảng `artApproved` | Số đo ảnh theo kit; cơ chế chữ ký qua bot; chủ dự án duyệt; hiệu năng đạt |

### 6.4 Việc của chủ dự án

| Mã | Việc | Thời gian | Credit |
|---|---|---|---|
| OW-05 | Chọn một trong hai ảnh mẫu sci-fi (MF-I10) | 5 phút | 0 |
| OW-06 | Dựng món Tuyến Cuối còn thiếu (MF-I15) | 0–40 phút | 0–200 |
| OW-07 | Dựng 3 món violet-glade (MF-I17) khi lát C3 bắt đầu | khoảng 30 phút | 90–180 |
| OW-08 | Dựng 2–3 món hill-meadow (MF-I19) khi lát C4 bắt đầu | khoảng 25 phút | 60–180 |
| OW-09 | Duyệt: mỗi kit một lần (3 góc × 4 hướng), mỗi mẫu một lần (guide + một lượt chơi), mỗi chương một tờ ghép | 10 phút mỗi lần | 0 |
| OW-10 | **Quyết định trước lát M5:** nạp thêm khoảng 1.000–1.500 credit, hay 2 món chữ ký mỗi kit. Claude mang số dư chính xác và danh sách theo kit khi lát C4 bắt đầu | 5 phút | — |
