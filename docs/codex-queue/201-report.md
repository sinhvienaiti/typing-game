# Phiếu 201 · Wordwoven · Ba ô đất v3

Ngày làm: **30/10/2026**, Mac mini M4, tại repo cha.

**Kết quả: BỊ CHẶN Ở CÔNG CỤ SINH ẢNH; CHƯA HOÀN THÀNH, CHƯA ĐẠT.** `image_gen.imagegen` trả HTTP **429**, `usage_limit_reached`, “The usage limit has been reached” ngay ở yêu cầu đầu tiên cho `grass-jade`. **0 ảnh được trả về; 0 bản chọn `.v3.png`**. Không có cơ sở chấm M/Q mới hoặc xác nhận Kiểm 2–6 cho v3. Không lấy bộ 122 làm v3, không sinh bằng CLI/API khác.

Công cụ báo `resets_at = 1793364446`, tức **19:47:26 ngày 30/10/2026, giờ Việt Nam**; đây là mốc do dịch vụ trả về, không phải lời hẹn tự chạy. Nhật ký: [generation-error.json](201/generation-error.json). Một yêu cầu thất bại, không có lượt sinh thành công nào; cả ba ô còn nguyên ngân sách tối đa ba ảnh sinh. Không có lượt 2 hoặc 3, không có câu prompt nào được sửa.

## 1. Phạm vi và kiểm nguồn

Đã đọc phiếu 122 (STYLE, MAP, GROUND và Đo chung), báo cáo 122 §2, §3, §9, ART_DIRECTION §1.3–1.4 và §2.2–2.5, ART_ACCEPTANCE §1, §2.2, §5; xem ba tờ trước–sau 122, tờ lát 122, tờ cạnh mẫu 122, hai ô đường và ảnh mẫu chủ dự án. Đã đối chiếu HANDOFF làn L3/L4. Không mở mã hoặc chạy gì trong worktree.

Đã tìm trong **hai** `accept-*/verdict.md` đang có. Không có mục 122 nhận một trong ba ô; giữ đủ ba ô trong phạm vi. Một chuỗi “122” bắt gặp là giá trị RGB ở phần khác, không phải verdict cho phiếu 122. Dấu kiểm cùng MD5 các verdict ở [verdict-scan.json](201/verdict-scan.json).

## 2. KA1 và khung thật

Trước khi ghi tài sản, dùng `md5 -r` cho toàn bộ file đệ quy trong `ground-v2/`, `ground/` 095, `_review/122/` và `_review/122-*.jpg`, sắp theo đường dẫn từ repo cha. [Trước](201/md5-before.txt): **176 file**; [sau](201/md5-after.txt): **177 file**. [Diff](201/md5-diff.txt): **0 file cũ đổi, 0 file cũ mất, 1 file thêm** — chỉ `ground-v2/grass-jade.v3.try1.prompt.txt`, đúng mẫu `*.v3.*`. `_review/122/`, các tờ 122 và `ground/` 095 không đổi. [KA1 JSON](201/ka1.json).

Hai tờ gốc đều còn, chép một lần sang `games/typing-defense/tmp/201/frames/`. [MD5 gốc–chép](201/frames-md5.txt) trùng từng cặp:

| Tờ | MD5 của cả gốc và bản chép | Cỡ tờ | Hộp cắt khung (a) |
| --- | --- | --- | --- |
| 1280 | `e06d0f5faced88e82947aeb5ab0fe1a8` | 2005 × 572 | **960x540+0+32** |
| 1920 | `6a8582adeb21603f26c1848811fa3af4` | 2673 × 752 | **1280x720+0+32** |

Đo mép bằng số trên bản chép: dải nhãn kết thúc ở y = 31; dòng y = 32 bắt đầu nội dung. Khe tối ở x = **960–971** và **1280–1296** (hơn 95% px dưới luma 0,12 ở vùng quét). Cắt x = 0, y = 32, đến trước khe; không lấy nhãn/khe, không phóng to. Chi tiết phép dò ở `_review/201/real-frame-1280.json` và `real-frame-1920.json`.

Hai khung là ảnh chụp **29/10, 10:14**, `td-1c` **bc05e67**, làn L3; đất vẫn dùng bộ **095**, ô **8 m**, shader còn nhân màu cỏ, trộn ô ba lá và nhiễu. Thông tin này theo phiếu, không suy ra rằng hình chụp đã dùng 122. Chỉ đọc hai file gốc để chép và tính MD5; mọi thao tác ảnh sau đó dùng bản chép. Đã lưu riêng hai hộp cắt đúng cỡ trong `_review/201/` để tiếp tục sau khi dọn `tmp`.

## 3. Số mốc đo lại — chỉ là bộ 122

Script [measure.mjs](../../games/typing-defense/art-src/_review/201/measure.mjs) import nguyên `decode`, `encode`, `metrics`, `seam` của 122; không sửa hoặc chạy trực tiếp script 122. Tính thêm L p5/p95 với `L = 0,2126R + 0,7152G + 0,0722B` trên sRGB 0–1. [Toàn bộ mốc](201/baseline.json).

| Ô 122 | Độ rối | Đốm lặp | Hue (°) | S trung vị | L trung vị | L p5 | L p95 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `road-paved` | 0.033529 | 0.118645 | 37.894737 | 0.121053 | 0.672224 | 0.426138 | 0.777210 |
| `trail-worn` | 0.044702 | 0.116545 | 41.632653 | 0.295455 | 0.486369 | 0.332974 | 0.660078 |
| `grass-jade` | 0.053719 | 0.122424 | 106.153846 | 0.523810 | 0.380279 | 0.221489 | 0.589335 |
| `grass-moss` | 0.053327 | 0.054215 | 99.473684 | 0.459016 | 0.349329 | 0.191969 | 0.552262 |
| `stream-bank` | 0.029027 | 0.133576 | 52.500000 | 0.093750 | 0.320405 | 0.194977 | 0.581965 |

| Ô 122 | E | I | C | E/I | C/I |
| --- | --- | --- | --- | --- | --- |
| `road-paved` | 0.034250 | 0.037840 | 0.034250 | 0.905145 | 0.905145 |
| `trail-worn` | 0.050542 | 0.051203 | 0.050542 | 0.987103 | 0.987103 |
| `grass-jade` | 0.061962 | 0.056147 | 0.061962 | 1.103568 | 1.103568 |
| `grass-moss` | 0.054029 | 0.054321 | 0.054029 | 0.994623 | 0.994623 |
| `stream-bank` | 0.033510 | 0.032009 | 0.033510 | 1.046893 | 1.046893 |

Cả năm ô mốc có E/I ≤ 1,25; các giá trị C/I cũng ≤ 1,25. Cả năm có **0 px tím cấm**. **Không thực hiện hậu kỳ mới trên các ô 122.** Các số trên khớp lỗi báo cáo 122: cỏ chính rối 0,053719 > 0,035 và đốm 0,122424 > 0,09; cỏ rêu rối 0,053327 > 0,035; bờ suối đốm 0,133576 > 0,12.

Quan hệ màu mốc 122: lệch hue hai cỏ **6.680162°**, lệch L **0.030949**; cỏ rêu tối hơn nhưng **ấm hơn**, hue thấp hơn cỏ chính. Đường − cỏ chính **0.291945**; đường − bờ suối **0.351820**. L cỏ chính < L vai đường < L đường. Không dùng các quan hệ của bộ cũ để kết luận v3.

### Bảng 122 → v3 và Kiểm 2–6

| Ô | 122: rối / đốm / hue / S / L | v3 |
| --- | --- | --- |
| `grass-jade` | 0,053719 / 0,122424 / 106,153846° / 0,523810 / 0,380279 | **Chưa có ảnh, chưa đo** |
| `grass-moss` | 0,053327 / 0,054215 / 99,473684° / 0,459016 / 0,349329 | **Chưa có ảnh, chưa đo** |
| `stream-bank` | 0,029027 / 0,133576 / 52,500000° / 0,093750 / 0,320405 | **Chưa có ảnh, chưa đo** |

Định dạng ba bản chọn, E/I/C trước–sau, độ rối, đốm, hue/S/L, L p95 và mọi quan hệ màu v3: **chưa kiểm được vì chưa có ảnh**. Chưa có thao tác chọn/copy/cmp ảnh hoặc prompt chọn. Không tạo `metrics.json` trống giả hoàn tất; lệnh `final` dành cho khi đủ ba bản chọn, hiện sẽ từ chối vì thiếu PNG.

## 4. Prompt và yêu cầu sinh bị chặn

Đích yêu cầu: `grass-jade.v3.try1.png`. Hai ảnh đính kèm là `road-paved.png`, `trail-worn.png` của 122, đã xem trước khi gọi công cụ. Prompt giữ nguyên STYLE + MAP + GROUND của phiếu 122, nguyên phần riêng lượt 1 và dòng đính kèm của phiếu 201. Đã lưu đúng chuỗi gửi (không thêm câu chỉ dẫn khác) ở [grass-jade.v3.try1.prompt.txt](../../games/typing-defense/art-src/scenery/meadow/ground-v2/grass-jade.v3.try1.prompt.txt):

```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.

Asset for a 3D strategy game seen from a high camera looking 55 degrees down from 58 metres: every shape must read at that distance, so group detail into big masses with strong light-dark contrast, keep edges clean, and avoid fine noise, tiny scattered bits and thin strands.

Seamless tileable ground texture, edges wrap on all four sides, seen straight from above with no perspective. One tile covers 8 by 8 metres of ground. Flat, even, shadowless light: no cast shadows and no sun direction, the game lights it. Rich natural material with several close tones in big soft patches, painted detail no smaller than about 15 centimetres. No standing objects, no plants taller than the ground cover, no people or animals.

Short, dense jade turf of a high karst plateau, like a grazed mountain lawn seen from directly above, painted with broad soft brush strokes like a hand-painted terrain texture in a premium strategy game. The turf gathers into rounded soft masses 40 to 90 centimetres across; each mass is a little lighter on top and a little darker in the gaps between masses. Jade, teal-green and muted sage, all close in value. A few masses are tinted dry gold; they are spread evenly over the whole tile, each under one metre, never in bands, rings or clusters. Every square metre looks about as bright as every other. No single blades, no leaf shapes, no clover, no flowers, no pebbles, no bare soil, no grain or speckle.

Use the attached images only to match the style, colours, lighting and scale. Paint a different ground as described.
```

`transparent_background = false`. Không có file ảnh trả về để chép. Dừng trước hai ô còn lại vì chúng phải tham chiếu cỏ chính đã chọn/lượt tốt nhất; hiện chưa có lượt nào để chọn. Không chấm ba ô là “trượt sau ba lượt”. Chưa xảy ra mâu thuẫn §5 trên tranh v3, vì chưa có tranh để hậu kỳ.

## 5. Script tờ kiểm và khung phối cảnh

[sheets.mjs](../../games/typing-defense/art-src/_review/201/sheets.mjs) dùng Node và ImageMagick tại máy, không trình duyệt/WebGL. [mock-spec.json](201/mock-spec.json) ghi camera và bố cục:

- FOV dọc **38°**, 16:9, nhìn xuống **55°**, cách điểm nhìn **58 m**, điểm nhìn **(0,0,0)**. Tia từ pixel cắt mặt phẳng y = 0; khung đúng cỡ hai hộp cắt.
- Ô 8 m. Chuỗi mip **1024 → 512 → 256 → 128**, Lanczos; LOD từ đạo hàm tọa độ đất theo pixel, nội suy hai mức kề; lấy mẫu song tuyến tính tuần hoàn từng mip, **4 × 4 = 16 mẫu/pixel**.
- Cỏ chính phủ nền. Hai mảng rêu **18 × 12 m**, **16 × 12 m**, tâm XZ **(−14,4)** và **(12,−9)**. Đường chéo theo trục XZ **(0,6; 0,8)**, rộng **4 m**, vai **1,5 m mỗi bên**, vân đá chạy theo trục đường.
- Suối rộng **5 m**, bờ **2 m mỗi bên**, tuyến cong công thức trong JSON. Nước phẳng **`#386b68`**. Mép mặt nạ mềm khoảng **0,4 m**. Không thêm đèn, bóng, sương hoặc tia nắng.
- Cùng hàm dựng, UV và mặt nạ cho bộ 122 và v3. Đây là khung thử vật liệu, không mô phỏng shader của làn L và không gắn ảnh vào game.

**Đã xuất và đã xem toàn cỡ:**

| Tờ / bằng chứng | Đường dẫn | Cỡ |
| --- | --- | --- |
| (a) và (b), mốc 1280 | [frame-1280-baseline.jpg](../../games/typing-defense/art-src/_review/201/frame-1280-baseline.jpg) | 960 × 1152 |
| (a) và (b), mốc 1920 | [frame-1920-baseline.jpg](../../games/typing-defense/art-src/_review/201/frame-1920-baseline.jpg) | 1280 × 1512 |
| Hộp cắt thật 1280 | [real-frame-1280.png](../../games/typing-defense/art-src/_review/201/real-frame-1280.png) | 960 × 540 |
| Hộp cắt thật 1920 | [real-frame-1920.png](../../games/typing-defense/art-src/_review/201/real-frame-1920.png) | 1280 × 720 |

Tên tờ có hậu tố **baseline** và nhãn “CHƯA CÓ v3”, chỉ có (a), (b). Không giả khung (c). Script đã có nhánh xuất đủ tờ trước–sau, lát 122 | v3, 256, ba khung và cạnh mẫu, nhưng **chưa thực thi nhánh này** vì thiếu ảnh. Các tên chính thức `201-frame-1280.jpg`, `201-frame-1920.jpg`, `201-tiles.jpg`, `201-256.jpg`, `201-vs-ref.jpg`, ba tờ trước–sau **chưa tồn tại**.

## 6. Xem bằng mắt, M/Q và rủi ro shader

Trên khung **(b) 1280**, tự chấm **M = 7,0/10 — chưa đạt** theo riêng phần đất: đường đá đọc rõ, có khoáng và nhiều sắc; cỏ vẫn có đốm vàng/xanh phân thành nhịp lặp dọc hai phía đường và ở nửa phải. Không trừ điểm vì thiếu đèn, trời hoặc mốc lớn. Không thấy khe pixel trắng/đen lộ rõ trong khung (b), nhưng **thấy lặp**; không ghi “không thấy lặp”. Điểm này chấm trên phối cảnh mới của bộ 122, không thay kết luận báo cáo 122 trên mock khác.

**M của (c), Q từng ô v3 ở 1024/256 (Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp): chưa chấm được.** Không có ảnh mới nên không tự cấp 8 điểm hoặc “Dùng tiếp = 2”. Chưa có tờ lát v3 để kiểm ở toàn cỡ; chưa có tờ cạnh mẫu để nói “đứng cạnh được”.

**Kiểm 9 mới làm được một phần:** khung (a) của làn L dùng 095, nhìn xanh khá đồng sắc và đường như dải quệt; khung (b) dùng 122 không qua shader đã có đá đường rõ, nhưng lại thấy đốm cỏ lặp. Điều đó cho thấy **bản thân ô 122 vẫn có nhịp lặp**, không thể quy toàn bộ lỗi cho shader. Chưa có (c) nên chưa tách được mức cải thiện của v3 hay định lượng phần một màu do shader. Theo thông tin phiếu, phép nhân màu cỏ, trộn ba lá/nhiễu và nhịp ô 8 m của làn L **có thể** góp phần làm đồng sắc. Đây là giả thuyết cần làn L kiểm sau, không phải kết luận đo từ cặp (a)/(c). Không sửa shader.

Khi có ảnh v3, tiếp tục đo trước; chỉ resize/chuẩn hóa, vá mép `seam(8,48)` nếu E/I > 1,25, chỉnh sáng toàn ảnh **0,90–1,10** khi cần cho màu. Không lọc mờ, giảm tương phản, lọc thông cao hay phủ màu để ép số. Lượt này chưa áp dụng hệ số sáng nào, chưa hậu kỳ ảnh sinh nào; không có tờ trước–sau giả từ bộ cũ. Nếu phải hủy chất liệu mới đạt số, giữ tranh và ghi mâu thuẫn cho Claude quyết.

## 7. Kiểm script và cách tiếp tục

[script-checks.json](201/script-checks.json): hai script qua `node --check`; thử ghi lại `baseline.json` bị từ chối `EEXIST`; hệ số **0,89** bị từ chối; lệnh làm tờ v3 bị từ chối khi thiếu `grass-jade.v3.png`. ImageMagick 7 ở máy trả kênh `srgb  3.0`, script định dạng đã xét đúng chuỗi này và PNG Truecolor loại 2. **Chưa kiểm thực thi nhánh `try`/`final` và bộ tờ v3 trên ảnh thật**, do công cụ sinh không trả ảnh; không tuyên bố các nhánh này đã được xác minh hoàn chỉnh.

Lệnh đã chạy từ repo cha:

```sh
node games/typing-defense/art-src/_review/201/measure.mjs baseline
node games/typing-defense/art-src/_review/201/sheets.mjs --baseline
node --check games/typing-defense/art-src/_review/201/measure.mjs
node --check games/typing-defense/art-src/_review/201/sheets.mjs
```

Hai lệnh đầu ghi mới và **từ chối ghi đè** nếu chạy lại ngay. Sau khi dịch vụ sinh ảnh dùng được, tiếp tục ở yêu cầu **grass-jade lượt 1**, dùng prompt đã lưu và đúng hai ảnh đính kèm; không ghi đè prompt hiện có. Lưu nguyên byte ảnh trả về vào đích còn trống. Ví dụ lệnh xử lý (chỉ chạy khi ảnh tương ứng đã có):

```sh
node games/typing-defense/art-src/_review/201/measure.mjs try grass-jade 1
# Chỉ nếu cần chỉnh sáng cho luật màu; chọn tag mới, hệ số trong giới hạn:
node games/typing-defense/art-src/_review/201/measure.mjs try grass-jade 1 --light=0.95 --tag=light95
# Sau khi sinh/chọn/cmp đủ ba ô theo thứ tự của phiếu:
node games/typing-defense/art-src/_review/201/measure.mjs final
node games/typing-defense/art-src/_review/201/measure.mjs final --check
# Điền kết luận thật sau khi xem ảnh v3; không dùng câu kết luận mẫu để nhận tranh:
node games/typing-defense/art-src/_review/201/sheets.mjs --verdict='chưa, lý do theo ảnh thực tế'
```

`final --check` chỉ đọc, in kết quả. `final` giữ `metrics.json` chưa tồn tại để lượt tiếp tục ghi đúng một lần. `sheets` dùng hai crop PNG đã giữ ở `_review/201/`, không cần đọc lại worktree sau dọn tmp. Khi `metrics.json` hoặc tờ đã có thì không ghi đè. Nếu xử lý lại một lượt, dùng `--tag` mới. Hai ô sau chỉ sinh khi đã chọn cỏ chính hoặc có lượt cỏ chính tốt nhất sau đủ ba lượt.

## 8. Dọn ảnh thô

Đã chạy thử rồi áp dụng `capture-prune` cho riêng `games/typing-defense/tmp/201`. Thêm `--docs docs/codex-queue/201` để công cụ không quét cả cây tài liệu (có vùng Tu Tiên bị cấm đọc). Danh sách xem trước chỉ đúng **hai bản chép do phiên này tạo**, tổng **639.462 byte**; không có ảnh của làn khác. Các crop và tờ kiểm trong `_review/201/` giữ nguyên.

```sh
node tools/capture-prune/prune.mjs games/typing-defense/tmp/201 --min-age-min 0 --docs docs/codex-queue/201
node tools/capture-prune/prune.mjs games/typing-defense/tmp/201 --min-age-min 0 --docs docs/codex-queue/201 --apply
```

Đầu ra lần chạy thử ([toàn văn](201/prune-dry-run.txt)):

```text
Danh sách ảnh thô sẽ xóa (byte):
/Users/toandx/htdocs/typing-game/games/typing-defense/tmp/201/frames/td-1c-road-1280x720-default.jpg	252751
/Users/toandx/htdocs/typing-game/games/typing-defense/tmp/201/frames/td-1c-road-1920x1080-default.jpg	386711

Thư mục / nhóm cấp 1	Số file	MB (1 MB = 1.000.000 byte)
/Users/toandx/htdocs/typing-game/games/typing-defense/tmp/201/frames	2	0.639
/Users/toandx/htdocs/typing-game/games/typing-defense/tmp/201 [cộng]	2	0.639
Tổng: 2 file, 0.639 MB; giữ 0 ảnh, từ chối 0 mục.
```

Đầu ra áp dụng ([toàn văn](201/prune-apply.txt)):

```text
Danh sách ảnh thô sẽ xóa (byte):
/Users/toandx/htdocs/typing-game/games/typing-defense/tmp/201/frames/td-1c-road-1280x720-default.jpg	252751
/Users/toandx/htdocs/typing-game/games/typing-defense/tmp/201/frames/td-1c-road-1920x1080-default.jpg	386711

Thư mục / nhóm cấp 1	Số file	MB (1 MB = 1.000.000 byte)
/Users/toandx/htdocs/typing-game/games/typing-defense/tmp/201/frames	2	0.639
/Users/toandx/htdocs/typing-game/games/typing-defense/tmp/201 [cộng]	2	0.639
Tổng: 2 file, 0.639 MB; giữ 0 ảnh, từ chối 0 mục.
Đã xóa 2/2 file; nhật ký: /Users/toandx/htdocs/typing-game/games/typing-defense/tmp/201/.pruned-20261030-0818.txt.
```

## 9. Chỗ khác phiếu, phần còn thiếu và việc cần xem

**Khác phiếu do chặn dịch vụ:** chưa tạo ba PNG v3, chưa thử ba lượt mỗi ô, chưa chọn/cmp, chưa đo Kiểm 2–6 mới, chưa tạo bảng số cuối và các tờ có (c), chưa đủ M/Q. Chỉ làm phần độc lập với ảnh mới: khóa MD5, mốc đo, cắt khung, phối cảnh bộ 122, script và hồ sơ. Không gọi lại liên tiếp khi lỗi là hạn mức; không dùng cách sinh khác hoặc sửa ô 122 để thay thế.

**Khác nhỏ để giữ bằng chứng sau dọn:** thêm hai crop PNG và hai tờ baseline trong `_review/201/`; chúng là ảnh kiểm dẫn trong báo cáo, không phải tài sản v3. Không có ảnh trong `docs/codex-queue/201/`.

**Bỏ qua theo phạm vi:** không Git ghi, không commit/push/reset/clean/stash, không sửa game/shader, không build/test game, không dev server/trình duyệt, không mạng ngoài yêu cầu `image_gen` đã thất bại; không cài gói, không âm thanh, không `public/`, không ghi worktree, không đọc/ghi Tu Tiên.

**Claude/chủ dự án cần xem:** tờ [mốc 1280](../../games/typing-defense/art-src/_review/201/frame-1280-baseline.jpg) để thấy nhịp lặp cỏ; [lỗi hạn mức](201/generation-error.json) để tiếp tục phần sinh ảnh khi dịch vụ sẵn sàng. Phiếu vẫn **chưa hoàn thành**, chưa có ảnh được đề nghị nhận. Sau khi đủ ảnh và kiểm số, còn cần Claude chấm M ≥ 8, Q ≥ 8; quy tắc giám khảo thứ hai ở M 7,5–8,5 vẫn giữ nguyên.
