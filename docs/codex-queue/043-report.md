# Phiếu 043 · Lời Gọi · Chấm ảnh VFX và chuẩn hóa alpha

Ngày 28/10/2026 · Sinh ảnh bằng **image_gen tích hợp** · Hậu kỳ ImageMagick 7 và `tools/art-normalize`.

**14/14 bản chọn đạt tự chấm từ 8 điểm**, gồm 11 tên cũ và ba ảnh mới. Đã giao đủ `<tên>.alpha.png` trong `games/typing-defense/art-src/vfx/`. Ba ảnh mới còn có `<tên>.png` cùng byte với `.alpha.png`, kèm prompt chính xác. Điểm là Codex tự chấm, không phải nghiệm thu trong game.

## 1. Bản chọn và điểm

Chuẩn: [ART_ACCEPTANCE §2.2](../games/ART_ACCEPTANCE.md), [VFX_STANDARD §4.4](../games/VFX_STANDARD.md), mẫu mặt nạ [phiếu 038](038-report.md). Giữ màu sẵn của Lời Gọi; chỉ `paper-burn` bắt buộc đơn sắc.

Nguồn khác mô tả phiếu: bốn ảnh mảnh (`leaf-flakes`, `paper-scraps`, `stone-chips`, `wood-chips`) là atlas tĩnh đúng prompt; `scorch-mark` là **một vết cháy đơn**, không có 16 ô. Giữ bốn atlas và vẽ lại scorch thành chuỗi. Bản giao gồm **8 flipbook, 5 atlas tĩnh, 1 ảnh đơn**. Hai ảnh lặp có nền đen, không phải phông xanh/hồng/lam.

Đã xem nguồn 1254², bản chuẩn hóa 1024² (ô 256), và sheet thu về 256² (ô 64), đặt trên `backdrops/w1-silverfall/sky-a.png`. Ảnh đơn xem ở 512 và 256 px. Nền tối là cùng backdrop nhân RGB 0,25. Ghép alpha thường để lộ quầng/phông, không bloom; không mở trình duyệt. Bằng chứng cỡ nguyên ở `_review/043/proofs/`, tờ xem nhanh ở kiểm 5. Chấm theo thứ tự **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2.

Đây là kiểm texture tĩnh, không chứng minh toàn bộ A/R/T/I/F đã dựng đủ. Vai dự kiến: lửa/lóe cho R/I, khói–muội cho F, mảnh theo chất liệu cho I/F, brush marks cho lớp mực A/R/I. Làn tích hợp quyết vị trí, thời gian và phối lớp; phiếu này không sửa runtime.

| Ảnh | Lượt | Prompt sửa gì | Điểm 5 tiêu chí | Tổng | Lưới | Viền phông | Còn thiếu |
|---|---|---|---|---|---|---|---|
| `dust-puff` | Nguồn cũ, sửa miễn phí | Không đổi prompt; khóa xanh, giữ tỷ lệ chung cả chuỗi. | 2 / 2 / 1,5 / 2 / 2 | **9,5/10 · Đạt** | 16/16 ô; lề ≥ 28 px | 0 px | Bụi còn viền nâu rõ; đốm cuối gần mất ở 64 px. |
| `explosion` | Nguồn cũ, sửa miễn phí | Không đổi prompt; khóa xanh, giữ đỏ son–cam–vàng, khói nâu. | 2 / 2 / 1,5 / 2 / 2 | **9,5/10 · Đạt** | 16/16 ô; lề ≥ 28 px | 0 px | Lửa hơi bóng so với chất giấy. |
| `flame-loop` | Nguồn cũ, sửa miễn phí | Không đổi prompt; khóa đen rồi chuyển ảnh phát sáng RGB sang RGBA thẳng. | 2 / 2 / 1,5 / 1,5 / 2 | **9/10 · Đạt** | 16/16 ô; lề ≥ 34 px | 0 px | Dáng giữa còn lặp nhịp; quầng đen của lần key đầu đã bỏ. |
| `ink-splat` | Nguồn cũ, sửa miễn phí | Không đổi prompt; khóa xanh, giữ tím đen, thêm lề. | 2 / 1,5 / 1,5 / 2 / 2 | **9/10 · Đạt** | 16/16 ô; lề ≥ 28 px | 0 px | Mực khá bóng và chìm trên nền tối; hợp vai lớp tối trộn thường. |
| `leaf-flakes` | Nguồn cũ, sửa miễn phí | Không đổi prompt; khóa hồng, giữ lá xanh; fit riêng từng mảnh atlas. | 2 / 2 / 1,5 / 2 / 2 | **9,5/10 · Đạt** | 16/16 ô; lề ≥ 28 px | 0 px | Gân nhỏ mất bớt ở 64 px. |
| `ma-troi-wisp` | Nguồn cũ, sửa miễn phí | Không đổi prompt; khóa đen rồi chuyển RGBA thẳng như lửa. | 2 / 1,5 / 1,5 / 2 / 2 | **9/10 · Đạt** | 16/16 ô; lề ≥ 31 px | 0 px | Mắt nhỏ/hở alpha hơi chìm trên trời sáng; dáng wisp vẫn rõ. |
| `paper-scraps` | Nguồn cũ, sửa miễn phí | Không đổi prompt; khóa xanh, giữ giấy kem và mực tím; fit từng mảnh. | 2 / 2 / 1,5 / 2 / 2 | **9,5/10 · Đạt** | 16/16 ô; lề ≥ 28 px | 0 px | Hạt giấy chi tiết hơn phong cách phẳng; dáng xé còn rõ. |
| `scorch-mark` | Vẽ lại 1, sửa miễn phí | Giữ nguyên đoạn đầu prompt nguồn; thay mô tả vết tĩnh bằng 16 pha nở–vỡ–tan. Bỏ đường lưới sinh thừa; mật độ sáng thành alpha, RGB than tím #30272d. | 1,5 / 1,5 / 1,5 / 2 / 2 | **8,5/10 · Đạt** | 16/16 ô; lề ≥ 28 px | 0 px | Tro khá vụn, lõi không đặc ở pha vòng; chìm trên nền tối. Cần chấm lại độc lập. |
| `stone-chips` | Nguồn cũ, sửa miễn phí | Không đổi prompt; khóa xanh, giữ đá xám và ngói đỏ; fit từng mảnh. | 2 / 2 / 1,5 / 2 / 2 | **9,5/10 · Đạt** | 16/16 ô; lề ≥ 28 px | 0 px | Mặt đá hơi nhiều chi tiết ở 64 px; cạnh lớn vẫn rõ. |
| `water-splash` | Nguồn cũ, sửa miễn phí | Không đổi prompt; ô 13–16 nhân kích thước 0,8 / 0,6 / 0,35 / 0,12 để tan. Giữ bạc–lam. | 1,5 / 2 / 1,5 / 2 / 2 | **9/10 · Đạt** | 16/16 ô; lề ≥ 28 px | 0 px | Đoạn cuối là vòng nước co lại, chưa thật tự nhiên như giọt tan. |
| `wood-chips` | Nguồn cũ, sửa miễn phí | Không đổi prompt; khóa xanh, giữ vỏ nâu/gỗ sáng; fit từng mảnh. | 2 / 2 / 1,5 / 2 / 2 | **9,5/10 · Đạt** | 16/16 ô; lề ≥ 28 px | 0 px | Thớ nhỏ mất ở 64 px, dăm và cuộn còn phân biệt. |
| `ink-smoke` | Mới 1 | Hai đoạn phong cách nguyên văn; thêm chuỗi khói tím đen bốc–loang–tách sợi, không viền nét. | 2 / 1,5 / 2 / 1,5 / 2 | **9/10 · Đạt** | 16/16 ô; lề ≥ 28 px | 0 px | Sợi cuối hơi dày; chi tiết nhỏ mất ở 64 px, các khối giữa khá gần nhau. |
| `brush-glyphs` | Mới 2, chọn | Lượt 1 có nét giống S, 7,5 điểm, loại. Lượt 2 đổi nét lượn/S thành giọt mực/quệt tam giác, đổi xoắn thành dấu quạt lông cọ; giữ nguyên hai đoạn đầu. | 2 / 1,5 / 2 / 1,5 / 2 | **9/10 · Đạt** | 16/16 ô; lề ≥ 28 px | 0 px | Vài nét gần họ nhau; mực chìm trên nền tối. Chỉ có nét quệt trừu tượng, không có ký tự viết đọc được, chữ Hán, chữ cái hay số. |
| `paper-burn` | Mới 1, sửa miễn phí | Hai đoạn phong cách nguyên văn; thêm mặt nạ đơn sắc trên đen. Nguồn sinh hai mảng: crop nguyên mảng phải, bỏ mảng nổ trái; độ sáng thành alpha, RGB xám than. | 1,5 / 2 / 1,5 / 1,5 / 2 | **8,5/10 · Đạt** | Ảnh đơn 512² | 0 px | Rìa khá giống tro/đá hơn sợi giấy. Tàn là hạt tro xám; không giữ nâu/đỏ vì đầu ra bắt buộc xám. Cần chấm lại độc lập. |

`scorch-mark` và `paper-burn` ở 8,5 cần Claude/người duyệt chấm độc lập theo §4 của luật ảnh. Không sửa `ART_REPLACE_LATER.md` vì ngoài phạm vi ghi; thiếu sót được ghi ngay ở đây. Không gửi tin nhắn cho người khác.

### Nguồn cũ trước sửa

Điểm dùng tiếp có tính thiếu alpha/lề. Với lỗi miễn phí, sửa trước rồi chấm lại; không sinh lại chỉ vì bước key đầu chưa sạch.

| Nguồn | Điểm 5 tiêu chí trước sửa | Tổng | Xử lý |
|---|---|---|---|
| dust-puff | 2 / 2 / 1,5 / 2 / 1 | 8,5 | Sửa alpha/lề |
| explosion | 2 / 2 / 1,5 / 2 / 1 | 8,5 | Sửa alpha/lề |
| flame-loop | 2 / 1 / 1,5 / 1,5 / 0,5 | 6,5 | Key đơn còn quầng đen; sửa RGBA, lên 9 |
| ink-splat | 2 / 1,5 / 1,5 / 2 / 1 | 8 | Sửa alpha/lề |
| leaf-flakes | 2 / 2 / 1,5 / 2 / 1 | 8,5 | Giữ atlas, sửa alpha/lề |
| ma-troi-wisp | 2 / 1 / 1,5 / 1,5 / 0,5 | 6,5 | Sửa RGBA, lên 9 |
| paper-scraps | 2 / 2 / 1,5 / 2 / 1 | 8,5 | Giữ atlas, sửa alpha/lề |
| scorch-mark | 0,5 / 1,5 / 1,5 / 2 / 0 | 5,5 | Thiếu chuỗi 16 pha, vẽ lại 1 lượt |
| stone-chips | 2 / 2 / 1,5 / 2 / 1 | 8,5 | Giữ atlas, sửa alpha/lề |
| water-splash | 1,5 / 2 / 1,5 / 2 / 0 | 7 | Vòng cuối chưa tan; sửa bốn ô cuối, lên 9 |
| wood-chips | 2 / 2 / 1,5 / 2 / 1 | 8,5 | Giữ atlas, sửa alpha/lề |

`brush-glyphs` lượt 1: **1 / 2 / 1,5 / 2 / 1 = 7,5**, loại vì nét giống S. Lượt 2 đạt 9. Tổng **5 lần gọi image_gen**: ba tên mới, một lượt sửa brush, một lượt vẽ lại scorch. Không cần lượt 3. Các candidate-v1–v4 của scorch là hậu kỳ cùng một lần sinh, không phải bốn lượt sinh.

`ma-troi-sheet.prompt.txt` chỉ có prompt, không có ảnh. **Không sinh ảnh này**, đúng yêu cầu.

## 2. Lệnh tách alpha và ghép lưới

Chạy từ repo gốc. Nhật ký đầy đủ từng lệnh: `_review/043/commands.txt`, `commands-try2.txt`, `refine-commands-v4.txt`, `paper-burn.commands.txt`. Hồ sơ và script chỉ nằm trong media được phép, không phải mã game hay file đưa vào Git.

### Key phông

Để WORK của công cụ chỉ nằm trong `.tmp/043/`, shim `.tmp/043/bin/python3` nạp nguyên `normalize.py`, đặt biến WORK về thư mục đó rồi gọi `main()`. Không sửa thuật toán key, ngưỡng, hay file công cụ gốc. Môi trường thực tế:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
export PYTHONDONTWRITEBYTECODE=1
export PATH="$PWD/tools/art-normalize/.tmp/043/bin:$PATH"
bash tools/art-normalize/key-alpha.sh games/typing-defense/art-src/vfx/dust-puff.png tools/art-normalize/.tmp/043/dust-puff/keyed.png --bg '#00FF00' --mode global --despill protect-interior --no-key-hue
```

Cùng công thức với nguồn tương ứng cho phông xanh; leaf dùng `--bg '#FF00FF'`. `--no-key-hue` chỉ dùng cho phông bão hòa khi vật không có sắc khóa; không mất xanh lá của leaf vì khóa là hồng. Hai loop và scorch dùng `--bg '#000000'`, bỏ `--no-key-hue`. Brush chọn nguồn `brush-glyphs.try2.png`. Nguồn sinh smoke/paper/scorch giữ nguyên tại `_review/043/<tên>.source.png`, có `.source.prompt.txt` chính xác cạnh ảnh.

### Crop từng ô và ghép 4×4

Không gọi `pad-margin.sh` cho lưới 4×4. Chia nguồn theo `round(c × W / 4)`, tương tự hàng: nguồn 1254² có ô 313 hoặc 314 px. Trim bbox alpha > 8/255. Flipbook dùng tỷ lệ chung `200 / max(kích thước bbox của 16 ô)` để giữ lớn–nhỏ theo pha; atlas fit từng vật vào 200×200. Căn bbox giữa ô 256²; lề mục tiêu 28 px dành chỗ lọc.

Ví dụ lệnh thực tế của dust (ô đầu, hàng đầu, toàn lưới):

```sh
/opt/homebrew/bin/magick tools/art-normalize/.tmp/043/dust-puff/keyed.png -crop 314x314+0+0 +repage tools/art-normalize/.tmp/043/dust-puff/crop-01.png
/opt/homebrew/bin/magick tools/art-normalize/.tmp/043/dust-puff/crop-01.png -crop 120x101+101+127 +repage -filter Triangle -resize '81x68!' -gravity center -background none -extent 256x256 -depth 8 PNG32:tools/art-normalize/.tmp/043/dust-puff/cell-01.png
/opt/homebrew/bin/magick tools/art-normalize/.tmp/043/dust-puff/cell-01.png tools/art-normalize/.tmp/043/dust-puff/cell-02.png tools/art-normalize/.tmp/043/dust-puff/cell-03.png tools/art-normalize/.tmp/043/dust-puff/cell-04.png +append tools/art-normalize/.tmp/043/dust-puff/row-0.png
/opt/homebrew/bin/magick tools/art-normalize/.tmp/043/dust-puff/row-0.png tools/art-normalize/.tmp/043/dust-puff/row-1.png tools/art-normalize/.tmp/043/dust-puff/row-2.png tools/art-normalize/.tmp/043/dust-puff/row-3.png -append -depth 8 PNG32:games/typing-defense/art-src/_review/043/dust-puff.candidate.png
```

Water ô 13–16 nhân thêm kích thước `0.8, 0.6, 0.35, 0.12`, không giảm alpha đồng loạt: giữ cách tan bằng co hình của phong cách bộ.

Hai loop: sau key và ghép, với kênh 0–1 đặt `E=max(R,G,B)`, `A_mới=A_key×E`, `RGB_mới=RGB/E`; E=0 thì RGBA=0. Đổi từ ảnh phát sáng trên đen sang RGBA thẳng, giữ tỷ lệ màu và bỏ quầng đen khi ghép alpha thường. Mã chính xác ở `refine-alpha.py`; kiểm vòng lặp dùng dữ liệu sau bước này.

Scorch: bỏ đường lưới sinh thừa bằng alpha 0 tại các dải hàng nguồn 302–316, 616–630, 925–940 và cột 306–320, 620–634, 935–949. Các dải quanh đường chia, không nằm trong hình giữa ô. Đặt `A_mới=A_key×L`, `RGB=(48,39,45)`, fit lại và ghép. Bản chọn **candidate-v4**; v1–v3 còn trong hồ sơ để thấy lỗi lưới, không dùng làm bản giao.

Paper: nguồn 1536×1024 sinh sai bố cục hai mảng. Crop nguyên mảng phải `768x1024+768+0`, về xám, trim theo độ sáng > 1%, fit 424×424, căn giữa 512². `L=level(1%,100%)`, alpha=L (viền 4 px ép 0), RGB=`0.32×(1−L)`. Lõi đậm có alpha cao, rìa tro tan về 0. Lệnh thực tế:

```sh
/opt/homebrew/bin/magick identify -format '%w %h' games/typing-defense/art-src/_review/043/paper-burn.source.png
/opt/homebrew/bin/magick games/typing-defense/art-src/_review/043/paper-burn.source.png -crop 768x1024+768+0 +repage -colorspace Gray tools/art-normalize/.tmp/043/paper-burn/right-panel.png
/opt/homebrew/bin/magick tools/art-normalize/.tmp/043/paper-burn/right-panel.png -threshold 1% -format %@ info:
/opt/homebrew/bin/magick tools/art-normalize/.tmp/043/paper-burn/right-panel.png -threshold 1% -format %@ info:
/opt/homebrew/bin/magick tools/art-normalize/.tmp/043/paper-burn/right-panel.png -crop 733x1024+4+0 +repage -resize 424x424 -gravity center -background black -extent 512x512 -level 1%,100% -depth 8 tools/art-normalize/.tmp/043/paper-burn/luminance.png
/opt/homebrew/bin/magick tools/art-normalize/.tmp/043/paper-burn/luminance.png -fx '(i<4 || i>=508 || j<4 || j>=508) ? 0 : u' -depth 8 tools/art-normalize/.tmp/043/paper-burn/alpha.png
/opt/homebrew/bin/magick tools/art-normalize/.tmp/043/paper-burn/luminance.png -negate -evaluate Multiply .32 tools/art-normalize/.tmp/043/paper-burn/charcoal.png
/opt/homebrew/bin/magick tools/art-normalize/.tmp/043/paper-burn/charcoal.png tools/art-normalize/.tmp/043/paper-burn/alpha.png -alpha off -compose CopyOpacity -composite -colorspace sRGB -depth 8 PNG32:games/typing-defense/art-src/_review/043/paper-burn.candidate.png
```

Bản giao sao chép nguyên byte từ `_review/043/selected-final/`; ánh xạ ứng viên ở `selection-final.json`. `brush-glyphs.try1.*` là lượt loại, `try2.*` là nguồn chọn; prompt chính được lưu đúng lượt chọn. `scorch-mark.try1.*` giữ nguồn sinh; dùng `scorch-mark.alpha.png`. Prompt chính của ba ảnh mới giữ nguyên lời gửi image_gen; hậu kỳ ghi trong báo cáo.

## 3. Đầu ra năm kiểm

### Kiểm 1 · MD5

Chạy `md5 -r` cho mọi file trong `art-src/vfx/` trước ghi và sau giao, sắp theo đường dẫn; đối chiếu `diff -u` và tập đường dẫn/hash. **23 trước → 49 sau: thêm 26, thay đổi 0, xóa 0.** Diff ngoài hai dòng tiêu đề chỉ có dòng thêm. Ba cặp ảnh mới `.png`/`.alpha.png` cùng byte; cả ba prompt chính mở đầu đúng nguyên văn hai đoạn của `ink-splat.prompt.txt`.

Hồ sơ: `_review/043/md5-before.txt`, `md5-after.txt`, `md5.diff`, `md5-comparison.json`, `prompt-checks.json`. Đầu ra sau:

```text
d7fd83c7b9febff4f703772175f506f9 games/typing-defense/art-src/vfx/brush-glyphs.alpha.png
d7fd83c7b9febff4f703772175f506f9 games/typing-defense/art-src/vfx/brush-glyphs.png
e960ab82709dba129869e6fc050f4c3d games/typing-defense/art-src/vfx/brush-glyphs.prompt.txt
f95952a2f1a1491b1603ffc42913dd60 games/typing-defense/art-src/vfx/brush-glyphs.try1.png
ca25525fb275f21bcc8668d15a9efd87 games/typing-defense/art-src/vfx/brush-glyphs.try1.prompt.txt
b6840fefeffa65ce9859553620775296 games/typing-defense/art-src/vfx/brush-glyphs.try2.png
e960ab82709dba129869e6fc050f4c3d games/typing-defense/art-src/vfx/brush-glyphs.try2.prompt.txt
c70b9400d2941a45468cd91513a62c38 games/typing-defense/art-src/vfx/dust-puff.alpha.png
cb16312e2dbae3638496c142c9fbdcd0 games/typing-defense/art-src/vfx/dust-puff.png
aa4ea55abe2c918d72664cc9e7899afe games/typing-defense/art-src/vfx/dust-puff.prompt.txt
148e612b378b098a7d14274d9dae3487 games/typing-defense/art-src/vfx/explosion.alpha.png
c5100580056482b69e215666fe7d7447 games/typing-defense/art-src/vfx/explosion.png
63a795cde1d005a098db88ed9253485a games/typing-defense/art-src/vfx/explosion.prompt.txt
cc0336982eab344f577e3712dee895a0 games/typing-defense/art-src/vfx/flame-loop.alpha.png
c55cb9dc034cd28d23c99e3a3158c980 games/typing-defense/art-src/vfx/flame-loop.png
e259e8794c9a1c0ebd8185c0fcdc314c games/typing-defense/art-src/vfx/flame-loop.prompt.txt
b76399505d12ab4ecd3ce4665ddd55c2 games/typing-defense/art-src/vfx/ink-smoke.alpha.png
b76399505d12ab4ecd3ce4665ddd55c2 games/typing-defense/art-src/vfx/ink-smoke.png
3ac79d052d96c14083f15f2748765e36 games/typing-defense/art-src/vfx/ink-smoke.prompt.txt
6479456651e24e9eaad0bdb1c21ecac8 games/typing-defense/art-src/vfx/ink-splat.alpha.png
c714a81dcef9bfab85f9d1af700960df games/typing-defense/art-src/vfx/ink-splat.png
e114dc4c0cb61b748f83f6cb6f2fefa0 games/typing-defense/art-src/vfx/ink-splat.prompt.txt
5919af684305e6fba159693d1c3a02d4 games/typing-defense/art-src/vfx/leaf-flakes.alpha.png
1b1ca0fcd3fb0a5baf8df09ccbef8d43 games/typing-defense/art-src/vfx/leaf-flakes.png
23a1b1a251365461b45d7217020b6910 games/typing-defense/art-src/vfx/leaf-flakes.prompt.txt
8639db820cc63e1569ff1c1b34d07900 games/typing-defense/art-src/vfx/ma-troi-sheet.prompt.txt
c03227607b818e891a1635e53cef1a5b games/typing-defense/art-src/vfx/ma-troi-wisp.alpha.png
2c989ea36b21b89351443b217a6a45b0 games/typing-defense/art-src/vfx/ma-troi-wisp.png
2ff8f302dd072905b73153e6f3698af5 games/typing-defense/art-src/vfx/ma-troi-wisp.prompt.txt
ebe2ca1435c0b57c488927f6a06f18c8 games/typing-defense/art-src/vfx/paper-burn.alpha.png
ebe2ca1435c0b57c488927f6a06f18c8 games/typing-defense/art-src/vfx/paper-burn.png
33cfd80796bdb5e5bbc7b537534e29f9 games/typing-defense/art-src/vfx/paper-burn.prompt.txt
e176a469c1f0f688bd0bb1a951a73a22 games/typing-defense/art-src/vfx/paper-scraps.alpha.png
e8e7930c1c5efa2e764c540956ac4410 games/typing-defense/art-src/vfx/paper-scraps.png
51e30216362201f668af607e673ee7dc games/typing-defense/art-src/vfx/paper-scraps.prompt.txt
f3d11618bb151f2e2dd4eff093f4770d games/typing-defense/art-src/vfx/scorch-mark.alpha.png
7e05df5589e4f7cf08b8dcab89b0b187 games/typing-defense/art-src/vfx/scorch-mark.png
983855e56998962e5dbf20f98909d838 games/typing-defense/art-src/vfx/scorch-mark.prompt.txt
77c2d6ec814b46cba1e2167a16d145e6 games/typing-defense/art-src/vfx/scorch-mark.try1.png
4f8b7c45ad3d87b3419acd99a0543f95 games/typing-defense/art-src/vfx/scorch-mark.try1.prompt.txt
59d5bb3f8f9f6ff452f3cf05f387323f games/typing-defense/art-src/vfx/stone-chips.alpha.png
2115ecf3c32fa349f6d9b2b4afd9a305 games/typing-defense/art-src/vfx/stone-chips.png
32b0c4498441efbce6a5931459dd67e1 games/typing-defense/art-src/vfx/stone-chips.prompt.txt
88dd9e185d66acd15e5c90fbcdd5b423 games/typing-defense/art-src/vfx/water-splash.alpha.png
428c96af0e4a99bfc49601d6067b86f4 games/typing-defense/art-src/vfx/water-splash.png
73b6fd330b13dcc17d8014f2298137ef games/typing-defense/art-src/vfx/water-splash.prompt.txt
1671d84b4e766e56b68c9c527ce2a628 games/typing-defense/art-src/vfx/wood-chips.alpha.png
5f95a1be391cc0a6d2c12c9984d37069 games/typing-defense/art-src/vfx/wood-chips.png
6e68163f069ef76949aad3995fcfacbf games/typing-defense/art-src/vfx/wood-chips.prompt.txt
```

### Kiểm 2 · Khổ, kênh

Lệnh từng file: `/opt/homebrew/bin/magick identify -format '%w %h %[channels]' <file>`. Đầu ra cho `.alpha.png` ở bảng dưới; ba PNG mới cùng byte nên cùng kết quả. Saturation HSV tính trên RGB toàn ảnh: `(max−min)/max`, đen tính 0. **paper-burn = 0,000000 ≤ 0,02**. Lõi alpha cao, không khoét alpha trống ở lõi.

### Kiểm 3–4 · Lề, alpha và viền phông

BBox lấy từ alpha > 0,1. **208/208 ô của 13 lưới đạt**, lề nhỏ nhất 28 px; mọi ô có viền 4 px alpha 0. Paper là ảnh đơn, không áp lưới, viền ảnh cũng 0.

Chroma chỉ đếm pixel `0.05 < alpha < 0.95`. Xanh: `G>R+40` và `G>B+40`; hồng: `R>G+40` và `B>G+40`. **Tổng 0 pixel vi phạm**. Phông đen không có sắc khóa; kiểm riêng bằng alpha và xem quầng trên nền sáng sau đổi RGBA thẳng.

| Ảnh | Identify | Số ô | Lề nhỏ nhất, px | Alpha lớn nhất viền 4 px /255 | Pixel bán trong suốt | Pixel phông vi phạm |
|---|---|---|---|---|---|---|
| `dust-puff` | `1024 1024 srgba 4.0` | 16 | 28 | 0 | 21888 | 0 |
| `explosion` | `1024 1024 srgba 4.0` | 16 | 28 | 0 | 25741 | 0 |
| `flame-loop` | `1024 1024 srgba 4.0` | 16 | 34 | 0 | 137127 | 0 |
| `ink-splat` | `1024 1024 srgba 4.0` | 16 | 28 | 0 | 23513 | 0 |
| `leaf-flakes` | `1024 1024 srgba 4.0` | 16 | 28 | 0 | 20429 | 0 |
| `ma-troi-wisp` | `1024 1024 srgba 4.0` | 16 | 31 | 0 | 155593 | 0 |
| `paper-scraps` | `1024 1024 srgba 4.0` | 16 | 28 | 0 | 15174 | 0 |
| `scorch-mark` | `1024 1024 srgba 4.0` | 16 | 28 | 0 | 139334 | 0 |
| `stone-chips` | `1024 1024 srgba 4.0` | 16 | 28 | 0 | 17292 | 0 |
| `water-splash` | `1024 1024 srgba 4.0` | 16 | 28 | 0 | 21715 | 0 |
| `wood-chips` | `1024 1024 srgba 4.0` | 16 | 28 | 0 | 17212 | 0 |
| `ink-smoke` | `1024 1024 srgba 4.0` | 16 | 28 | 0 | 25936 | 0 |
| `brush-glyphs` | `1024 1024 srgba 4.0` | 16 | 28 | 0 | 39236 | 0 |
| `paper-burn` | `512 512 srgba 4.0` | Ảnh đơn | 109 | 0 | 45783 | 0 |

Đầu ra từng ô: `_review/043/grid-inline-output.txt` (208 dòng bbox/lề và dòng tổng), `grid-output-delivered.txt` (thêm ảnh đơn), `verification-delivered.json` (kèm centroid, độ phủ, alpha mass). Lệnh inline đã chạy, không lưu script vào mã repo:

```sh
python3 - <<'PY' > games/typing-defense/art-src/_review/043/grid-inline-output.txt
from pathlib import Path
import subprocess
M='/opt/homebrew/bin/magick'
violations=[]; total=0
for f in sorted(Path('games/typing-defense/art-src/vfx').glob('*.alpha.png')):
    w,h=map(int,subprocess.check_output([M,'identify','-format','%w %h',str(f)]).split())
    if (w,h)!=(1024,1024): continue
    a=subprocess.check_output([M,str(f),'-alpha','extract','-depth','8','gray:-'])
    for n in range(16):
        ox=n%4*256; oy=n//4*256
        points=[(x,y) for y in range(256) for x in range(256) if a[(oy+y)*w+ox+x]>25.5]
        xs,ys=zip(*points)
        bbox=(min(xs),min(ys),max(xs),max(ys))
        m=(bbox[0],bbox[1],255-bbox[2],255-bbox[3]); total+=1
        print(f'{f.name} cell {n+1:02}: bbox={bbox}; margins L/T/R/B={m}')
        if min(m)<24: violations.append((f.name,n+1))
print('TOTAL_CELLS',total,'VIOLATIONS',violations)
PY
```

Dòng cuối: `TOTAL_CELLS 208 VIOLATIONS []`.

Các ô nguồn thiếu lề trước sửa (quy đổi về 1024², không phải lỗi bản giao):

```text
dust-puff: ô thiếu lề 24 px trước sửa = [4, 5, 6, 7, 8, 9, 10, 11, 12]
explosion: ô thiếu lề 24 px trước sửa = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
flame-loop: ô thiếu lề 24 px trước sửa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ink-splat: ô thiếu lề 24 px trước sửa = [5, 6, 8, 9, 10]
leaf-flakes: ô thiếu lề 24 px trước sửa = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
ma-troi-wisp: ô thiếu lề 24 px trước sửa = [1, 2, 3, 4, 5, 6, 7, 8, 11, 13, 14, 15, 16]
paper-scraps: ô thiếu lề 24 px trước sửa = [1, 7, 10, 11, 13, 14, 15, 16]
stone-chips: ô thiếu lề 24 px trước sửa = [6, 9]
water-splash: ô thiếu lề 24 px trước sửa = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
wood-chips: ô thiếu lề 24 px trước sửa = [1, 3, 5, 8, 9, 10, 11, 12, 13, 15]
scorch-mark: 1 hình tĩnh, thiếu chuỗi 16 ô.
```

### Kiểm thêm · Pha tan và vòng lặp

Atlas không có thứ tự thời gian, không ép pha tan hay vòng. Sáu one-shot có pha cuối vỡ/co/tan; tỷ lệ tổng alpha ô 16 so với ô đỉnh xác nhận phần dư nhỏ, không thay phép chấm hình:

| One-shot | Tổng alpha ô 16 / ô đỉnh |
|---|---|
| `dust-puff` | 0.586% |
| `explosion` | 3.214% |
| `ink-splat` | 2.046% |
| `scorch-mark` | 1.372% |
| `water-splash` | 0.374% |
| `ink-smoke` | 2.715% |

Loop không tan cuối. Đã xem dáng 16→1 và đo MAE RGBA premultiplied (0–255), chốt tham khảo seam ≤ 2,5×trung vị các cặp kề. Phép đo này không thay kiểm chuyển động trong game.

| Loop | MAE 16→1 | Trung vị MAE cặp kề | Tỷ số | Kết quả |
|---|---|---|---|---|
| `flame-loop` | 0.611504 | 7.292279 | 0.083856 | Đạt đo + duyệt dáng |
| `ma-troi-wisp` | 2.740963 | 12.207840 | 0.224525 | Đạt đo + duyệt dáng |

### Kiểm 5 · Tờ xem nhanh

- [Tờ nền sáng](../../games/typing-defense/art-src/_review/043-sheet.jpg).
- [Tờ nền tối](../../games/typing-defense/art-src/_review/043-sheet-dark.jpg).

Mỗi ảnh một hàng: nguồn cũ/nguồn sinh lượt 1 → alpha trên bàn cờ → alpha trên backdrop, kèm tên và điểm bản chọn. Brush cột trái là lượt bị loại, hai cột phải là lượt 2. Paper cột trái cho thấy nguồn hai mảng để kiểm phần crop. Sheet 4×4 thu về 256² nên mỗi ô đúng 64 px; paper thu cả ảnh về 256². Có `sheet-part-1..3.jpg` để đọc từng nhóm, `proofs/*.native.jpg` để xem bản giao cỡ nguyên và `*.old-native.jpg` để xem nguồn key trước sửa trên backdrop.

## 4. Bàn giao và phần còn lại

Dùng **14 file `.alpha.png`**; ba ảnh mới có `.png` cùng byte. Không dùng `.tryN.png` làm alpha runtime. Giữ nguyên 23 file ban đầu; không ghi public, media sync, chạy Git, build, test suite, dev server hay trình duyệt; không động game khác hoặc Tu Tiên. Đây là kiểm art ngoại tuyến.

Cần người duyệt chấm lại `scorch-mark` và `paper-burn` ở mức 8,5, nhất là tro vụn và độ chìm ở nền tối. Chưa đăng ký hai ảnh vào danh sách nâng cấp chung vì ngoài đường dẫn cho phép; chưa tích hợp runtime theo phạm vi phiếu. `ma-troi-sheet` bỏ qua vì chỉ có prompt, đúng yêu cầu.
