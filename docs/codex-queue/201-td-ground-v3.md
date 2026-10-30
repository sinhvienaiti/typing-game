# Phiếu 201 · Wordwoven · Vẽ lại ba ô đất trượt của 122 thành bản `.v3` (grass-jade, grass-moss, stream-bank)

**Nguồn:**
- `docs/codex-queue/122-report.md`: "Kết quả: CHƯA ĐẠT … Hai ô cỏ trượt độ rối, cỏ chính trượt thêm đốm lặp, bờ suối trượt đốm lặp … M = 7,5/10".
- Lượt chấm nhận phiếu 116 (`docs/codex-queue/accept-29-10b/verdict.md`): "Cả cảnh trên khung đó chỉ khoảng 6, vì đất."
- `docs/HANDOFF_CURRENT.md`, làn L3 và L4: "đường chờ ảnh 122, 123c".
- Chủ dự án 30/10: "tăng thêm việc cho codex cho tôi".

**Vì sao:** ở camera 55° từ 58 m, đất chiếm gần hết màn hình. Năm ô của 122 qua số (trong đó `road-paved`, `trail-worn`). Ba ô còn lại trượt, nên sân vẫn một màu xanh. Phiếu này chỉ vẽ lại ba ô đó, khớp màu với hai ô đường đã qua.

**Không trùng:** 122 (đã giao, giữ nguyên), 095 (ô cũ), 123 (decal, ruộng), 186 (đất Dragonhold).

**Báo cáo:** `docs/codex-queue/201-report.md` (tiếng Việt). Thư mục `docs/codex-queue/201/` chỉ chứa số (JSON, md5), không chứa ảnh.

**Làn:** làn Codex duy nhất (chủ dự án 30/10: một làn). Thứ tự chỉ là hàng đợi, không phụ thuộc nội dung phiếu khác.

**Claude, trước khi giao:**
- Lúc viết phiếu (30/10), 122 chưa được chấm nhận (không có mục 122 trong `accept-29-10/verdict.md`, `accept-29-10b/verdict.md`). Nếu Claude đã chấm và nhận ô nào trong ba ô, xóa ô đó khỏi phiếu.
- Kiểm hai tờ khung game ở mục Đọc trước 6 còn tồn tại (làn L có thể dọn `tmp/`). Mất thì chụp lại tờ ở camera mặc định và sửa đường dẫn trong phiếu trước khi giao.

**Luật hậu kỳ (bắt buộc, 29/10):** `docs/games/ART_ACCEPTANCE.md` §5.
- Mỗi ô một tờ "bản sinh | bản hậu kỳ", cùng cỡ.
- Công cụ chỉ được: đổi cỡ, làm liền mép, chỉnh sáng toàn ảnh trong ±10 %.
- Cấm làm mờ, nén tương phản, lọc thông cao, phủ màu để đạt số.
- Ngưỡng số mâu thuẫn với tranh thì dừng, giữ tranh, ghi mâu thuẫn để Claude quyết.
- Tự chấm trên bản hậu kỳ.

## Luật chung

- **Nơi làm:** repo cha `/Users/toandx/htdocs/typing-game` (làn chạy ở `.`). Không dùng worktree.
- Ảnh là media, không vào Git (`games/typing-defense/.gitignore` bỏ qua `art-src/*`).
- **Mức nhận:** M ≥ 8 theo game thương mại (`docs/games/ART_DIRECTION_2026-10-28.md` §1.3; ảnh mẫu `games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp`) và Q ≥ 8 (năm tiêu chí của `docs/games/ART_ACCEPTANCE.md` §1, ngưỡng §2.2). Ô đất là một phần cảnh: M chấm trên ảnh ghép (ART_DIRECTION §1.4).
- **Mốc M cho mặt đất** (giữ như phiếu 122, KA5): 9 là ảnh mẫu của chủ dự án; 8 là phát hành được: chất liệu thật, nhiều sắc độ có chủ đích, đọc rõ làn đường ở xa, hợp cảnh sử thi; 7 là gọn nhưng thường; 5 là đúng chất liệu nhưng sai tầm (đồ chơi, phẳng); 4 là màu phẳng kiểu clip-art. Khung (c) không có đèn, trời, mốc lớn: không trừ điểm vì thiếu ba thứ đó, chỉ chấm đất.
- **Tối đa 3 lượt sinh mỗi ô.** Giữ mọi `.tryN`. Không lượt 4.
- **Chỉ được ghi:**
  - `games/typing-defense/art-src/scenery/meadow/ground-v2/<tên>.v3.tryN.png` và `<tên>.v3.tryN.prompt.txt` (N = 1, 2, 3);
  - bản chọn `<tên>.v3.png` và `<tên>.v3.prompt.txt` cùng thư mục;
  - `games/typing-defense/art-src/_review/201/` (kể cả hai script mới `measure.mjs`, `sheets.mjs`) và `games/typing-defense/art-src/_review/201-*.jpg`;
  - `games/typing-defense/tmp/201/` (tmp của game, Git bỏ qua): bản chép hai tờ khung game và file trung gian;
  - `docs/codex-queue/201-report.md`, `docs/codex-queue/201/`.
- `<tên>` chỉ là `grass-jade`, `grass-moss`, `stream-bank`.

## Đọc trước (chỉ đọc)

1. `docs/codex-queue/122-td-ground-cliffs.md`: khối STYLE, MAP, GROUND nguyên văn; mục "Đo chung".
2. `docs/codex-queue/122-report.md` §2 (prompt đã thử từng lượt), §3 (mâu thuẫn §5), §9 (hướng khác đề xuất).
3. `games/typing-defense/art-src/_review/122/grass-jade-before-after.jpg`, `grass-moss-before-after.jpg`, `stream-bank-before-after.jpg`; `_review/122-tiles.jpg`; `_review/122-vs-ref.jpg`.
4. Hai ô đã qua số, để khớp màu và thang: `ground-v2/road-paved.png`, `ground-v2/trail-worn.png`.
5. Ảnh mẫu của chủ dự án (đường dẫn ở trên).
6. Khung game thật: `games/.wt-td-1c/tmp/lane-l3/road-sheets/td-1c-road-1280x720-default.jpg` (2005 × 572) và `td-1c-road-1920x1080-default.jpg` (2673 × 752).
   - Mỗi file là một tờ: dải nhãn tối cao 32 px ở trên, nửa trái là khung game (camera mặc định 55°, 58 m), một khe tối, nửa phải là ảnh mẫu.
   - Khung game đo sơ bộ: `960x540+0+32` ở tờ 1280 (khung 1280 × 720 đã thu nhỏ), `1280x720+0+32` ở tờ 1920 (khung 1920 × 1080 đã thu nhỏ). Codex đo lại mép bằng số rồi mới cắt.
   - Chụp 29/10 10:14 trên `td-1c` `bc05e67` (làn L3), mặt đất còn dùng ô 095 qua shader `src/view/3d/ground.ts` của nhánh `td-1c` (ô 8 m, `TILE_M = 8`; shader còn nhân màu cỏ, trộn ô ba lá và nhiễu). Ghi điều này trong báo cáo; không cần mở mã.
   - Worktree `.wt-td-1c` đang có làn khác. Chỉ đọc hai file này (chép một lần ở bước 1); không ghi, không chạy gì trong đó.
7. `docs/games/ART_DIRECTION_2026-10-28.md` §1.3, §1.4, §2.2–§2.5; `docs/games/ART_ACCEPTANCE.md` §1 (năm tiêu chí Q), §2.2, §5.
8. Hàm đo của 122: `games/typing-defense/art-src/_review/122/process.mjs` (`decode`, `metrics`, `seam`).
9. Mọi `docs/codex-queue/accept-*/verdict.md`: nếu có mục 122 nhận một trong ba ô, bỏ ô đó và ghi vào báo cáo.

## Khối prompt

Mỗi prompt = **STYLE** + **MAP** + **GROUND** (nguyên văn trong phiếu 122, không sửa chữ nào) + phần riêng + dòng đính kèm.

Dòng đính kèm (nguyên văn):
```text
Use the attached images only to match the style, colours, lighting and scale. Paint a different ground as described.
```

**Thang:** một ô phủ 8 × 8 m (7,8 mm mỗi px). Shader đất của game lát ô 8 m. Khối 40–90 cm là 51–115 px. Chi tiết dưới 15 cm thành nhiễu ở camera chơi.

**Thứ tự sinh:** `grass-jade` → `grass-moss` → `stream-bank` (hai ô sau đính kèm `grass-jade.v3` đã chọn).

| Ô | Đính kèm | Đích màu (hướng dẫn, không phải ngưỡng) |
|---|---|---|
| `grass-jade` | `road-paved.png`, `trail-worn.png` (122) | hue 100–130°, S 0,30–0,50, L trung vị 0,34–0,44 |
| `grass-moss` | `grass-jade.v3.png`, `trail-worn.png` | hue cao hơn `grass-jade.v3` 0–10° (mát hơn), L thấp hơn 0–0,06 |
| `stream-bank` | `grass-jade.v3.png`, `road-paved.png` | L trung vị 0,28–0,40, xám trung tính |

`grass-jade.v3` chưa đạt sau 3 lượt thì hai ô sau đính kèm lượt tốt nhất của nó. Ghi lại.

**Phần riêng, lượt 1 (nguyên văn):**

`grass-jade`
```text
Short, dense jade turf of a high karst plateau, like a grazed mountain lawn seen from directly above, painted with broad soft brush strokes like a hand-painted terrain texture in a premium strategy game. The turf gathers into rounded soft masses 40 to 90 centimetres across; each mass is a little lighter on top and a little darker in the gaps between masses. Jade, teal-green and muted sage, all close in value. A few masses are tinted dry gold; they are spread evenly over the whole tile, each under one metre, never in bands, rings or clusters. Every square metre looks about as bright as every other. No single blades, no leaf shapes, no clover, no flowers, no pebbles, no bare soil, no grain or speckle.
```

`grass-moss`
```text
The same plateau turf turning into thick, low velvet moss: smooth rounded cushions 40 to 90 centimetres across with soft painted edges, slightly darker and cooler than the attached jade turf, jade-teal and grey-green, all close in value and spread evenly so no area is much lighter or darker than another. No clover, no round leaves, no dark channels or cracks, no flowers, no grain or speckle.
```

`stream-bank`
```text
A riverbank of continuous grey silt and fine wet gravel with smooth river stones 30 to 70 centimetres across half sunk into it. Stones and silt stay close in value: charcoal grey, slate and silver-grey, scattered evenly so no area is much lighter or darker than another, and no stone is pale white. Wetness is painted as broad soft silver tones, never as bright spots or highlights. A few flat moss patches under 60 centimetres. No single big boulder, no puddles, no plants standing up, no grain or speckle.
```

**Lượt 2–3:** sửa đúng câu gây trượt, theo số của lượt trước.
- Rối cao: bớt nét nhỏ, khối to hơn, chuyển mềm hơn trong khối.
- Đốm cao: chia sáng tối đều hơn, bỏ mảng lớn sáng hay tối.
- Màu lệch: nêu rõ màu đích trong câu.
- Ghi trong báo cáo: lượt nào sửa câu nào, vì số nào.

## Việc

Mọi lệnh chạy từ gốc repo cha. `<td>` = `games/typing-defense/art-src`.

1. **KA1 trước, rồi chép khung:**
   - `md5 -r` mọi file (đệ quy) trong `<td>/scenery/meadow/ground-v2/`, `<td>/scenery/meadow/ground/` (095), `<td>/_review/122/` và các file `<td>/_review/122-*.jpg`; sắp theo đường dẫn tính từ gốc repo. Ghi `docs/codex-queue/201/md5-before.txt` (từ chối ghi đè).
   - Chép hai tờ ở mục Đọc trước 6 sang `games/typing-defense/tmp/201/frames/` (chỉ đọc bản gốc). Ghi md5 của bản gốc và bản chép vào `docs/codex-queue/201/frames-md5.txt`; hai cặp phải trùng. Từ đây chỉ dùng bản chép.
   - Thiếu một trong hai tờ gốc: không dựng khung (a), làm tiếp phần còn lại, ghi rõ trong báo cáo.
2. **Script đo** `<td>/_review/201/measure.mjs`:
   - import `decode`, `encode`, `metrics`, `seam` từ `../122/process.mjs` (khối chạy chính của file đó chỉ chạy khi gọi trực tiếp nên import không ghi gì); không sửa và không gọi trực tiếp script nào của 122;
   - tự tính thêm L p5, p95 trên ảnh đã `decode` (công thức L của 122);
   - `node <td>/_review/201/measure.mjs baseline`: đo `road-paved.png`, `trail-worn.png` và ba ô 122 cũ (`grass-jade.png`, `grass-moss.png`, `stream-bank.png`), ghi `docs/codex-queue/201/baseline.json`;
   - `node <td>/_review/201/measure.mjs try <tên> <N> [--light=<hệ số>] [--tag=<chữ>]`: đo bản sinh, làm liền khi cần, chỉnh sáng nếu có cờ, ghi `<td>/_review/201/<tên>-v3-tryN[-tag].png` và `.png.json` (số trước và sau, các bước, hệ số);
   - `node <td>/_review/201/measure.mjs final`: gom mốc, mọi lượt, ba bản chọn và mọi quan hệ của Kiểm 6 vào `docs/codex-queue/201/metrics.json`;
   - mọi lệnh ghi file mới và từ chối ghi đè (`encode` của 122 đã từ chối; JSON dùng cờ `wx`). Muốn xử lý lại một lượt thì đặt `--tag` mới.
3. **Sinh `grass-jade.v3`.** Mỗi lượt:
   - lưu nguyên ảnh công cụ trả về thành `grass-jade.v3.tryN.png` và prompt đã gửi thành `.v3.tryN.prompt.txt` (đây là "bản sinh");
   - chạy `measure.mjs try`: đưa về 1024 × 1024, sRGB, RGB, 8 bit, không alpha; đo; nếu E/I > 1,25 thì làm liền bằng `seam` (core 8, fade 48), như 122;
   - nếu cần cho luật màu, chạy lại với `--light` trong 0,90–1,10 và `--tag` mới; ghi hệ số;
   - bản xử lý của lượt là file `<td>/_review/201/grass-jade-v3-tryN[-tag].png`.
4. **Chọn** lượt tốt nhất (ưu tiên đạt nhiều mục Kiểm 3–6 nhất, rồi Q cao hơn). Chép đúng byte bản xử lý của lượt đó thành `grass-jade.v3.png`; chép `.v3.tryN.prompt.txt` thành `grass-jade.v3.prompt.txt`. Kiểm bằng `cmp`: cả hai cặp trùng byte, ghi vào báo cáo.
5. **Lặp bước 3–4** cho `grass-moss.v3`, rồi `stream-bank.v3`.
6. **Tờ kiểm** bằng script `<td>/_review/201/sheets.mjs` (ghi mới, từ chối ghi đè):
   - `_review/201/<tên>-before-after.jpg`: bản sinh (chỉ đổi cỡ về 1024) | bản hậu kỳ (`<tên>.v3.png`), mỗi bên 1024 px, nhãn ở dải riêng.
   - `_review/201-tiles.jpg`: mỗi ô hai cột (122 | v3); mỗi cột có ô ở 512 px và ô lát 3 × 3 thu về 512 px (Lanczos).
   - `_review/201-256.jpg`: ba ô v3 ở đúng 256 px.
   - `_review/201-frame-1280.jpg` (lấy từ tờ 1280, mỗi khung khoảng 960 × 540) và `_review/201-frame-1920.jpg` (từ tờ 1920, mỗi khung khoảng 1280 × 720): ba khung xếp dọc, cùng cỡ, nhãn ở dải riêng:
     - (a) khung game thật, cắt từ nửa trái tờ của làn L3, bỏ dải nhãn và khe tối; ghi hộp cắt `WxH+X+Y`; không phóng to khung thật;
     - (b) mặt đất phối cảnh lát bộ 122;
     - (c) cùng bố cục, lát ba ô v3 cùng `road-paved`, `trail-worn` của 122.
   - `_review/201-vs-ref.jpg`: khung (c) của tờ 1920 cạnh ảnh mẫu của chủ dự án, cùng cao 640 px. Một dòng: "đứng cạnh được" hay "chưa", và vì sao.
7. **Khung phối cảnh (b), (c)** (script Node thuần, không trình duyệt, không WebGL):
   - camera như game (số đã kiểm trên nhánh `td-1c`: `src/view/3d/stage.ts`, `camera.ts`; Codex không cần mở worktree đó): FOV dọc 38°, khung 16:9, nhìn xuống 55°, cách điểm nhìn 58 m, điểm nhìn trên mặt đất y = 0 ở giữa khung; cỡ bằng hộp cắt của (a);
   - ô lát 8 m; lấy mẫu như GPU: chuỗi mip 1024 → 512 → 256 → 128 (Lanczos), chọn mức theo cỡ px trên đất, trộn hai mức kề (trilinear), cộng ít nhất 4 × 4 mẫu mỗi px; không răng cưa, không moiré;
   - bố cục, mặt nạ mềm vẽ bằng script, giống hệt ở (b) và (c): cỏ `grass-jade` phủ nền; hai mảng `grass-moss` 10–20 m; một đường `road-paved` rộng 4 m, viền `trail-worn` 1,5 m mỗi bên, chạy chéo khung, vân đá theo trục đường; một suối rộng 5 m, viền `stream-bank` 2 m; nước là dải ngọc phẳng một màu (ghi mã màu);
   - không thêm đèn, bóng, sương hay tia nắng.
   - Ghi thông số (camera, cỡ, mip, số mẫu, bố cục, mã màu nước) vào `docs/codex-queue/201/mock-spec.json`.
8. **KA1 sau:** md5 lại cùng các thư mục và mẫu tên của bước 1, theo cùng cách (file mới của phiếu này hiện thành dòng thêm). Ghi `md5-after.txt` và `md5-diff.txt` (`diff md5-before.txt md5-after.txt`) vào `docs/codex-queue/201/`.
   - Rồi dọn file trung gian của mình (luật chụp 28/10 trong `AGENTS.md`): chạy thử `node tools/capture-prune/prune.mjs games/typing-defense/tmp/201 --min-age-min 0`, xem danh sách chỉ gồm file phiếu này ghi (hai bản chép khung và file trung gian), rồi chạy lại với `--apply`. Các tờ ở `_review/201` không nằm trong `tmp/` nên giữ nguyên. Ghi đầu ra vào báo cáo.
9. **Báo cáo:** prompt từng lượt và chỗ sửa; bảng số; điểm M, Q; đường dẫn mọi tờ; hộp cắt của (a); chỗ làm khác phiếu và vì sao; lệnh chạy lại hai script.

## Cấm

- Ghi đè, đổi tên, xóa file có sẵn: tám ô 122 và mọi `.try` của chúng, `scenery/meadow/ground/*` của 095, mọi file trong `_review/122/`.
- Xóa file `.try*` của phiếu này.
- Mọi lệnh git có ghi; sửa mã, shader hay tài liệu (trừ báo cáo và `docs/codex-queue/201/`).
- Dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex; cài gói.
- Ghi vào `public/`, game khác, bất kỳ worktree nào (`games/.wt-*`); ghi ra ngoài repo.
- Đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`).
- Chữ, số, logo, khung trong ảnh.
- Làm mờ, nén tương phản, lọc thông cao, phủ màu hay san mảng để đạt độ rối hay đốm lặp (§5).

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. **KA1:** `md5-diff.txt` trên `ground-v2/` chỉ có dòng thêm, mọi dòng thêm khớp `*.v3.*`; 0 file cũ đổi hay mất. `_review/122/` không đổi dòng nào.
2. **Định dạng:** `magick identify` ba bản chọn: 1024 × 1024, sRGB, 3 kênh, 8 bit, không alpha.
3. **Mép liền:** E ≤ 1,25 · I. Ô đã làm liền thì thêm chữ thập: C ≤ 1,25 · I. Ghi E, I, C, tỉ số trước và sau.
4. **Độ rối** (trung bình `|L − box5(L)|`, tuần hoàn): hai ô cỏ ≤ 0,035; `stream-bank` ≤ 0,045.
5. **Đốm lặp** (`p95 − p5` của box129(L), tuần hoàn): hai ô cỏ ≤ 0,09; `stream-bank` ≤ 0,12.
6. **Màu** (trung vị trên cả ô; L của `road-paved`, `trail-worn` đo lại ở bước 2, 122 ghi 0,672 và 0,486):
   - hue hai ô cỏ trong 80–150°; S trung vị ≤ 0,55;
   - hai ô cỏ lệch ≤ 10° hue và ≤ 0,06 L; ghi thêm `grass-moss` mát hơn (hue cao hơn) và tối hơn hay không;
   - L `road-paved` ≥ L `grass-jade.v3` + 0,15;
   - L `grass-jade.v3` < L `trail-worn` < L `road-paved`;
   - L `stream-bank.v3` ≤ L `road-paved` − 0,10;
   - L p95 của hai ô cỏ ≤ 0,60 (nền dưới thẻ chữ, ART_DIRECTION §2.5);
   - 0 px có hue 285–330° và S > 0,5.
7. **Bảng 122 → v3** cho từng ô: độ rối, đốm lặp, hue, S, L.
8. **Xem bằng mắt** ở cỡ đầy đủ: tờ lát 3 × 3 và khung (c). Ghi "không thấy đường nối, không thấy lặp" hay chỉ đúng chỗ thấy.
9. **Shader hay ô:** so (a) với (c). Ghi phần "một màu" nào của khung thật do ô, phần nào có thể do shader và lặp ô của làn L. Không sửa shader.
10. **KA5:** M trên khung (c) 1280; ghi M của (b) để so. Q từng ô ở 1024 và 256 (Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp, mỗi tiêu chí 0–2). "Dùng tiếp" chỉ được 2 khi mục 2–6 của ô đều đạt.
11. **§5:** mỗi ô có tờ before-after; liệt kê mọi bước công cụ và hệ số.

## Rủi ro (ghi vào báo cáo, không tự xử lý)

Một phần màu cỏ đơn điệu đến từ shader của làn L và nhịp lặp ô 8 m. Ô mới có thể chưa đủ nâng cả cảnh. Mục Kiểm 9 cho Claude số để quyết việc của làn L.

## Xong khi

- Ba ô có bản chọn `.v3`, với số và tờ trong báo cáo.
- Mỗi ô qua mục Kiểm 2–6; khung (c) tự chấm M ≥ 8; mỗi ô Q ≥ 8 ở 1024 và 256.
- Ô nào trượt sau 3 lượt: vẫn chọn lượt tốt nhất làm `.v3`; ghi chỗ trượt bằng số, mâu thuẫn §5 nếu có, và một cách khác đề xuất.
- Nhận khi Claude chấm lại M ≥ 8 và Q ≥ 8 (người chấm thứ hai khi M ở 7,5–8,5). Nhận rồi thì làn Wordwoven gắn ô vào đường và sân.
