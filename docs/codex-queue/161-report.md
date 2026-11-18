# Phiếu 161 · Dragonhold · Vẽ lại bốn icon

Ngày 29/10/2026. Đã sinh lại bốn đề tài bằng **image_gen tích hợp**, giữ nguyên các bản cũ; đủ master, bản thu, prompt và tờ so. **Chưa đủ điều kiện nhận:** còn kiểm tương phản trượt và độ đọc cỡ nhỏ cần Claude quyết. Không tự ghi đạt toàn bộ; không gắn vào public.

## 1. Bộ chọn cuối

Thư mục: games/dragon-hold/art-src/ui/icons/. **Bốn master đề nghị chấm:**

- armour.v2.final.png — chọn lượt 2 của phiếu này.
- danger.v2.final.png — chọn lượt 1.
- flag-pull.v2.final.png — chọn lượt 1.
- swarm.v2.try2.final.png — chọn lượt 2; bản thu mang cùng tiền tố .v2.try2.final.

Mỗi master có bản thu .v2.final.256.png, .v2.final.128.png, .v2.final.64.png; tổng **16 PNG chọn và 16 prompt cạnh từng PNG**. Prompt bản thu khớp byte prompt lượt chọn, resize không phải lượt sinh mới. selection-delivery.json liệt kê bốn master.

**Tờ chấm bộ chọn:** [161-sheet-selected.jpg](../../games/dragon-hold/art-src/_review/161-sheet-selected.jpg). Có bốn icon mới, cỡ thật 720p/1080p trên vỏ cây và kem, toàn bộ 31 icon 137–139, bốn icon cũ, HUD thương mại của chủ dự án và keyart 119 hiện có. Ô ×2 chỉ để soi, không thay cỡ thật.

Tờ bản sinh | bản hậu kỳ:

- [armour-selected.jpg](../../games/dragon-hold/art-src/_review/161/raw-vs-final/armour-selected.jpg).
- [danger-selected.jpg](../../games/dragon-hold/art-src/_review/161/raw-vs-final/danger-selected.jpg).
- [flag-pull-selected.jpg](../../games/dragon-hold/art-src/_review/161/raw-vs-final/flag-pull-selected.jpg).
- [swarm-selected.jpg](../../games/dragon-hold/art-src/_review/161/raw-vs-final/swarm-selected.jpg).

**Tên khác phiếu:** 161-sheet.jpg là tờ đo đầu; 161-sheet-final.jpg là bước sửa mép đầu. 161-sheet-delivery.jpg là bộ trước khi dùng lượt kiến cuối. Giữ nguyên theo luật không ghi đè; chỉ 161-sheet-selected.jpg dùng để chấm bộ chọn. Tương tự, .v2.png, .v2.alpha.png và các tờ không mang hậu tố -selected là bước trước. Không chép các bước đó vào runtime.

## 2. Nguồn và lượt sinh

Đã đọc 137, 139, báo cáo 137 và 139, verdict 29/10, AD và ART_ACCEPTANCE. Đã xem tờ dh-icons-137-139.jpg, skill-fire-breath, gold, ảnh chủ dự án, keyart 119 và ảnh kiến gai. Mỗi prompt giữ nguyên STYLE-UI Dragonhold, KIND ICON, **nguyên văn đoạn sửa tiếng Anh của người chấm**, rồi dòng nền khóa. Cờ dùng G; ba ảnh còn lại dùng M. Swarm đính kèm đúng enemies/thorn-ant.tripo.png trong lời gọi image_gen.

| Ảnh | Lượt mới / chọn | Sửa prompt |
|---|---|---|
| armour | 2 / 2 | Lượt 1 áo giáp rộng, vai rõ nhưng trang trí dày. Lượt 2 giữ đoạn sửa nguyên văn, thêm cổ U rộng, nách mở, eo hẹp, bốn hàng vảy lớn, một đinh giữa và đáy ngắn. Bản sinh vẫn có đầu rồng phù điêu ở vai; giữ tranh, không tẩy bằng công cụ. |
| danger | 1 / 1 | Tam giác men cam đỏ, nứt than hồng, viền sắt; không còn tia sét. Bản sinh thêm phù điêu rồng ở góc; không xóa. |
| flag-pull | 1 / 1 | Lá cờ tím xám lớn, bàn tay dưới phải, cán gãy và cục đất; không phóng bàn tay lấn cờ như phiếu cũ. |
| swarm | 2 / 2 | Lượt 1 đúng màu nhưng ba thân còn gom lại. Lượt 2 giữ đoạn sửa nguyên văn, thêm ba thân bằng nhau ở ba góc tam giác, khoảng âm rõ, mai đá xám bắt sáng lạnh và chân ngắn sát thân. Giữ nâu/mai xám/mắt vàng lục của model; không giáp kem vàng. |

**6 lượt sinh mới**, nguồn 1254² giữ đúng byte trong .v2.tryN.png, prompt chính xác cạnh mỗi lượt. Tính cùng phiếu gốc: armour 3 lượt, danger 3, flag-pull 3, swarm 3. Không vượt ba lượt mỗi đề tài. Không sinh tiếp danger/cờ để ép số. generation-manifest.json giữ bốn nguồn đầu; nguồn giáp lượt 2 ghi trong select-final.py và generation-armour-try2.json. Kiến lượt 2: generation-swarm-try2.json; so trực tiếp hai lượt ở swarm-two-tries.jpg, chọn lượt 2 vì ba thân còn tách ở 18 px.

## 3. Hậu kỳ giữ tranh

Đặt ART_MAGICK=/opt/homebrew/bin/magick; tools/art-normalize dùng WORK riêng trong _review/161/work, chế độ global, despill protect-interior. Giữ tím bên trong vật, không khử sắc khóa toàn lòng tranh.

Cắt theo alpha >16, Lanczos giữ tỉ lệ về cạnh dài 717 px, đặt giữa canvas 1024². Chỉ sửa alpha ngoài dải mép Chebyshev 3 px về 0/255. Sắc khóa còn sót được đưa về trung tính cùng luma **chỉ trong dải mép 3 px**; không xóa chi tiết hoặc phủ mảng tranh. **Gamma 1,0; nhân sáng 1,0 cho cả bốn ảnh.** Không nâng gamma mạnh để qua tương phản.

Mỗi tờ raw-vs-final có nguồn và thành phẩm cùng canvas 512²; bên dưới thêm nguồn căn cùng hình học với thành phẩm, cùng nền khóa, để so nét và màu. Đã xem trực tiếp cả bốn tờ bộ chọn, không chấm chỉ trên bản sinh.

| Ảnh | Pixel RGB sửa ở bước mép cuối | Pixel sửa ngoài mép 3 px | Alpha giữ nguyên ở bước mép cuối |
|---|---:|---:|---|
| armour | 673 | 0 | Có |
| danger | 1885 | 0 | Có |
| flag-pull | 3121 | 0 | Có |
| swarm | 823 | 0 | Có |

Bảng so bản trước khử sắc khóa mép cuối với master chọn, không phải so raw với toàn bộ quá trình tách nền/căn cỡ. Bằng chứng: preservation-selected.json; prompt master chọn cũng đã kiểm khớp byte lượt chọn.

## 4. Khổ, alpha, lề và IoU

Đủ 16 PNG chọn: master 1024², bản thu 256²/128²/64², **sRGBA 8 bit, sRGB**. selected-evidence/identify-selected.txt có số của đúng bộ chọn. reductions.json: cả 12 bản thu khớp từng pixel Lanczos trực tiếp từ master, không sharpen.

Định nghĩa: bbox alpha >16; sắc khóa có hue cách màu nền ≤15°, S >0,5 trên pixel alpha >0; IoU alpha ≥128 sau Lanczos 32². So mỗi ảnh mới với **30 icon còn lại của 137–139**, gồm ba bản v2 khác, không so với chính bản cũ bị thay.

| Ảnh | Bbox x,y,w,h | Cạnh dài | Lệch tâm tối đa | Bán alpha ngoài mép | Sắc khóa px / % | IoU lớn nhất / với |
|---|---|---:|---:|---:|---:|---|
| armour | 153,214,717,596 | 70,020% | 0,049% | 0 | 44 / 0,0152% | 0,777 / slot-house |
| danger | 171,153,682,717 | 70,020% | 0,049% | 0 | 63 / 0,0238% | 0,692 / seal-unlit |
| flag-pull | 182,153,659,717 | 70,020% | 0,049% | 0 | 54 / 0,0205% | 0,593 / armour |
| swarm | 153,220,717,584 | 70,020% | 0,049% | 0 | 404 / 0,2043% | 0,517 / danger |

Đạt cạnh dài 68–72%, tâm ≤2%, bán alpha ngoài mép bằng 0 và IoU chung ≤0,80. Ba ảnh đầu đạt sắc khóa ≤0,2%; **swarm là 0,2043%, vượt 0,0043 điểm phần trăm**. Một phần vùng tím này nằm trong ánh Héo do công cụ sinh vẽ dưới thân, đã thấy trên tờ raw-vs-final; không khử tím bên trong để ép số. Đây là thêm một mâu thuẫn cần Claude quyết theo luật giữ tranh. Alpha min/max cả bốn là 0/255.

**Giáp–khiên:** 12 px = **0,692**, đạt ngưỡng riêng ≤0,70 ở 12 px; 18 px = **0,733**, 32 px = **0,716**. Ở 18/32 px vẫn đạt ngưỡng chung 0,80, nhưng **không đạt nếu áp ngưỡng riêng 0,70 cho cả hai cỡ này**. Không bóp méo hoặc đục thêm áo giáp bằng công cụ để hạ IoU. Claude cần chốt cách áp ngưỡng trong đoạn sửa của verdict. Bản chọn đọc rõ cổ và hai vai hơn lượt 1, đáy không còn hình lá.

## 5. Tương phản — có kiểm trượt

Luma Rec.709 trên sRGB chuẩn hóa 0–1, đo sau ghép trên dấu chân alpha >16, như báo cáo gốc. Mỗi ô ghi vỏ cây #2b2118 / kem #f1e3c4.

| Ảnh | Cỡ 720p / 1080p | ΔY 720p tối / kem | ΔY 1080p tối / kem |
|---|---:|---:|---:|
| armour | 12 / 18 | 0,197 / 0,337 | 0,229 / 0,390 |
| danger | 24 / 36 | 0,139 / 0,522 | 0,141 / 0,526 |
| flag-pull | 18 / 22 | 0,085 / 0,404 | 0,092 / 0,432 |
| swarm | 18 / 22 | 0,111 / 0,365 | 0,122 / 0,401 |

**Cả bốn trượt ngưỡng ≥0,25 trên nền tối; đều vượt trên kem.** Giữ đúng cờ tím xám, kiến nâu/mai xám và men cam đỏ có viền sắt. Không đổi sang kem vàng để vượt số. Nâng sáng trong giới hạn +10% không giải quyết khoảng thiếu lớn của cờ, kiến và danger; gamma mạnh sẽ tái diễn lỗi người chấm vừa trả.

**Danger trên cỏ:** cắt ô đầu 640×360+4+54 từ đúng sheet đã giao, phục hồi 1280×720 / 1920×1080. Đây là ghép từ ảnh kiểm có sẵn, không phải capture runtime mới. Lấy nền đúng dưới dấu chân alpha, không thay phép đo luma bằng độ khác hue.

| Cỡ màn / icon | Vùng | Vị trí | Y cỏ | ΔY sau ghép | ≥0,25 |
|---|---|---|---:|---:|---|
| 720 / 24 px | Tối | 888,418 | 0,389 | 0,082 | Trượt |
| 720 / 24 px | Sáng | 950,320 | 0,547 | 0,220 | Trượt |
| 1080 / 36 px | Tối | 1332,627 | 0,389 | 0,082 | Trượt |
| 1080 / 36 px | Sáng | 1425,480 | 0,547 | 0,221 | Trượt |

Bằng chứng: [720p](../../games/dragon-hold/art-src/_review/161/danger-grass-delivery-720.png), [1080p](../../games/dragon-hold/art-src/_review/161/danger-grass-delivery-1080.png), grass-metrics-delivery.json. Cũng lưu trung bình trị tuyệt đối ΔY; cả bốn phép đo vẫn trượt. Màu đỏ và tam giác nhận diện được nhưng viền nhỏ không đủ kéo luma toàn dấu chân lên 0,25. **Theo luật mới: dừng ở tranh giữ màu tốt, chuyển mâu thuẫn cho Claude quyết; chưa nhận danger.** Tờ thử đầu có hai vùng gần cùng độ sáng, không dùng làm bằng chứng sáng/tối.

## 6. Tự chấm trên thành phẩm

Thứ tự Q: Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp, mỗi mục 0–2. Dùng tiếp chỉ **1** vì còn kiểm trượt. M so mức hoàn thiện HUD thương mại của ảnh chủ dự án, sau hậu kỳ, ở cỡ thật trên cả hai nền. Điểm không thay quyết định nhận.

| Ảnh | Năm điểm gốc | Q gốc | Năm điểm 720p | Q 720p | M gốc / 720p |
|---|---|---:|---|---:|---:|
| armour | 2 / 2 / 2 / 2 / 1 | 9 | 2 / 1,5 / 2 / 1,5 / 1 | 8 | 8,5 / 8 |
| danger | 2 / 2 / 2 / 2 / 1 | 9 | 2 / 1,5 / 2 / 1,5 / 1 | 8 | 8,5 / 8 |
| flag-pull | 2 / 1,5 / 2 / 2 / 1 | 8,5 | 2 / 1 / 2 / 1,5 / 1 | 7,5 | 8 / 7,5 |
| swarm | 2 / 2 / 1,5 / 2 / 1 | 8,5 | 2 / 1,5 / 1,5 / 2 / 1 | 8 | 8 / 8 |

Giáp và danger **đứng cạnh được về vật liệu/mức vẽ**, nhưng còn kiểm kỹ thuật. Cờ ở gốc đã đọc thành cờ thay vì nắm tay cầm giáo; ở 18 px nếp rách, cán và đất vẫn gom lại, đặc biệt trên vỏ cây. Kiến lượt 2 đúng màu và tách rõ ba thân ở 18 px trên cả hai nền; mai đá theo model ít ánh kim hơn bộ 137 và tím dưới chân hơi rõ. M ở cỡ nhỏ lên 8 nhờ dáng ba khối, nhưng kiểm tương phản và sắc khóa vẫn trượt. **Cờ chưa đứng cạnh được ổn định ở 720p**, giữ M 7,5, không tự chấm 8 để thông qua.

## 7. KA1, phạm vi và phần cần người nhận nhìn

KA1: trước **427 file**, sau **571 file** trong thư mục icon; diff **+144 / −0**. Toàn bộ **427 file có trước giữ nguyên MD5**. Phiếu này tạo **132 file icon: 66 PNG + 66 prompt**. 12 file thêm đồng thời mang tiền tố easier.v3 do luồng khác tạo; không đọc nội dung, sửa hoặc nhận là sản phẩm phiếu 161. Snapshot dùng /sbin/md5 -r, lưu md5-before.txt, md5-after-selected.txt, md5-diff-selected.txt và ka1-selected.json. _review/161* và báo cáo 161 chưa có trước khi bắt đầu.

Chỉ ghi bốn tiền tố icon của phiếu, _review/161* và báo cáo này. Không chạy Git, build/test game, server hoặc browser. Không tạo âm thanh vì phiếu chỉ yêu cầu ảnh. Không đọc/ghi Tu Tiên, .wt-*, public, mã game hoặc sửa công cụ dùng chung. Chỉ đọc ảnh tham chiếu game khác được phiếu gốc yêu cầu. Không có capture/raw frame browser mới cần prune; mọi .try* là nguồn sinh bắt buộc giữ.

Script đã dùng nằm trong _review/161/; bước tạo ảnh từ chối ghi đè. Đo lại với thư mục chưa có: `python3 games/dragon-hold/art-src/_review/161/verify-selected.py selected-evidence-rerun`. Nguồn và các bước ảnh nằm trong prepare.py, clean-edges.py, select-final.py, finalize.py; lượt kiến cuối có swarm-try2.py và finalize-swarm.py; tờ chọn dùng sheets-selected.py; kiểm cỏ dùng grass-delivery.py. Dùng Arial hệ thống và ImageMagick 7 Homebrew.

**Claude/chủ dự án cần nhìn:** tờ 161-sheet-selected.jpg, bốn tờ *-selected.jpg, cờ/kiến 18 px trên vỏ cây, giáp–khiên 12/18 px và danger trên cỏ sáng/tối. Cần quyết các ngưỡng tương phản/IoU còn mâu thuẫn, cùng cách xử lý cờ chưa đạt M ở 720p và sắc khóa của kiến. Người nhận đổi nguồn sau khi chấm; chưa tự gắn các ảnh này.
