# Phiếu 125 · Last Line · Bộ sân trận v2

Ngày 29/10/2026, Codex, Mac mini M4. Đã tạo **tám bản chọn**, bằng **16 lượt `image_gen` tích hợp**, giữ đủ ảnh gốc và prompt của mọi lượt. Không ảnh nào quá ba lượt. Tự chấm **M = 8,0 trên ảnh ghép cuối**, Q từng ảnh **8,5–9,5** ở khổ giao và **8–9** ở cạnh dài 384 px. **Chờ Claude chấm lại**, chưa tích hợp vào game.

Điều kiện chọn hướng đã đủ: [ART_DIRECTION_2026-10-28.md §4.3](../games/ART_DIRECTION_2026-10-28.md#43-bible-last-line-hướng-b-chủ-dự-án-chọn-2910) ghi chủ dự án chọn **B · Lightbearer ngày 29/10/2026 sáng**, cho phép các phiếu 121, 125, 126, 127 chạy theo bible. Tiêu đề phiếu và báo cáo 112 vẫn giữ trạng thái cũ; không sửa chúng.

## 1. Bộ giao cuối: dùng đúng danh mục này

Gốc media: `games/typing-survival/art-src/`. **Sáu bản alpha cuối có hậu tố `-alpha-v3`**. Các bản cùng tên không hậu tố và `-alpha-v2` là bước hậu kỳ trước, còn lỗi tách nền, được giữ nguyên theo luật không ghi đè. Không dùng các bản ấy để tích hợp. Danh mục máy: [final-selection.json](../../games/typing-survival/art-src/_review/125/final-selection.json).

| Ảnh | Bản chọn cuối trong `arena-v2/` | Nguồn | Khổ gốc → khổ giao | Kênh |
| --- | --- | --- | --- | --- |
| Sàn | [deck-tile.png](../../games/typing-survival/art-src/arena-v2/deck-tile.png) | try1 | 1254² → 1024² | RGB |
| Gờ đường | [deck-edge-alpha-v3.png](../../games/typing-survival/art-src/arena-v2/deck-edge-alpha-v3.png) | try1 | 2172 × 724 → 1536 × 512 | RGBA |
| Tường trái | [wall-left-alpha-v3.png](../../games/typing-survival/art-src/arena-v2/wall-left-alpha-v3.png) | try1 | 887 × 1774 → 1024 × 2048 | RGBA |
| Tường phải | [wall-right-alpha-v3.png](../../games/typing-survival/art-src/arena-v2/wall-right-alpha-v3.png) | try2 | 887 × 1774 → 1024 × 2048 | RGBA |
| Vòng xa | [far-ring-alpha-v3.png](../../games/typing-survival/art-src/arena-v2/far-ring-alpha-v3.png) | try2 | 1774 × 887 → 2048 × 1024 | RGBA |
| Trời hố đen | [sky-disk.png](../../games/typing-survival/art-src/arena-v2/sky-disk.png) | try1 | 1536 × 1024, giữ khổ | RGB |
| Leviathan | [void-leviathan-alpha-v3.png](../../games/typing-survival/art-src/arena-v2/void-leviathan-alpha-v3.png) | try3 | 1536 × 1024, giữ khổ | RGBA |
| Bốn decal | [deck-decals-alpha-v3.png](../../games/typing-survival/art-src/arena-v2/deck-decals-alpha-v3.png) | cháy try2; ba ô khác try1 | từng ảnh 1254² → 1024²; ghép 2048² | RGBA |

Tất cả PNG giao là **8-bit sRGB**, đúng khổ. Mỗi bản chọn có `<tên>.prompt.txt` cạnh ảnh, trùng byte với prompt lượt chọn. Prompt atlas gom nguyên văn bốn prompt, đánh dấu thứ tự ô; atlas là kết quả ghép, không phải một lượt gọi tạo ảnh riêng. Thứ tự: **cháy / kính vỡ / vòng glyph / khe đá** theo trái sang phải, trên xuống dưới.

**Khác phiếu về tên:** đáng lẽ chỉ xuất tên chuẩn sau khi duyệt hậu kỳ; tôi đã xuất chúng sớm. Khi phát hiện viền còn lỗi, tôi giữ nguyên các file ấy và giao phiên bản mới thay vì ghi đè. Vì vậy sáu tên alpha và tên một số tờ kiểm có hậu tố phiên bản. Bảng trên và `final-selection.json` chỉ rõ bộ cần duyệt; không có file cũ nào bị thay.

## 2. Các lượt sinh và sửa prompt

Đã đọc ảnh chuẩn của chủ dự án, hai concept B, ảnh trận `map1-audit`, prompt bộ 088, báo cáo 088/095, bible Last Line, `ART_ACCEPTANCE.md` §5 và `PATH_QUALITY.md` §2. Giữ nguyên văn hai khối STYLE và ARENA trong mọi prompt; thêm phần kỹ thuật về khổ, độ tối, hướng vật liệu, khoảng trống và đối tượng của lớp. Nền magenta cho lớp alpha; leviathan dùng green. Không sao chép nội dung ảnh chuẩn.

| Ảnh | Lượt | Thiếu gì; sửa prompt đúng chỗ |
| --- | --- | --- |
| `deck-tile` | 1, chọn | Thêm chỉ dẫn phiến thép/đá dài theo hướng dọc, khe nối so le, đinh chìm, vết mòn giữa làn và vật liệu tối. Đạt ngay; không sinh tiếp. |
| `deck-edge` | 1, chọn | Khóa mặt cắt gồm nắp thép, thân đá, kết cấu thép dưới gờ; nhìn ngang hơi từ trên, hai đầu cùng cao độ. Đạt ngay. |
| `wall-left` | 1, chọn | Khối đá nghiêng, giàn thép nhiều tầng, vòng trạm vỡ mở vào phía làn; đủ lề quanh hình. Đạt ngay. |
| `wall-right` | 1 | Có tham chiếu tường trái và đúng câu chỉ dùng để hợp phong cách/màu/sáng; công cụ vẫn gần như lật gương dáng trái. Không chọn. |
| `wall-right` | 2, chọn | Nhấn mạnh cấu trúc mới hoàn toàn: hai khối đá lớn xếp lệch, tay cập bến thẳng gãy, không có vòng cung. Vẫn đính kèm tường trái đã chọn. |
| `far-ring` | 1 | Công cụ vẽ thêm đường ở phần dưới. Không xóa phần đường bằng công cụ vì sẽ thay phần vẽ. |
| `far-ring` | 2, chọn | Khóa lớp bóng kiến trúc treo ở xa, không mặt đất/phối cảnh đường, khoảng nền ở dưới và giữa các mảnh. |
| `sky-disk` | 1, chọn | Trời riêng, tâm hố đen cao, phần tư dưới navy chuyển tự nhiên. Đạt ngay. |
| `void-leviathan` | 1 | Dáng và chất liệu tốt nhưng mắt không đủ rõ, sương chạm đáy. |
| `void-leviathan` | 2 | Yêu cầu đầu nhìn chính diện, ba cặp mắt và lề quanh sừng/đuôi. Dáng tốt hơn nhưng vẫn chỉ có bốn mắt rõ. Ảnh soi: `leviathan-eyes-try2.jpg`. |
| `void-leviathan` | 3, chọn | Đính kèm try2 làm ảnh sửa: thêm đúng một cặp mắt dưới hai cặp có sẵn, giữ vật liệu/dáng/màu, thu hình nhẹ để chừa lề. Đủ sáu mắt rõ. Dừng ở giới hạn ba lượt. |
| `deck-decals-scorch` | 1 | Trông như đống đá vỡ lớn. Không chọn. |
| `deck-decals-scorch` | 2, chọn | Đổi trọng tâm thành vết muội phẳng, khe cam mảnh, mép cháy mềm; không ụ đá lớn. |
| `deck-decals-shards` | 1, chọn | Mảnh kính đen vỡ, ánh phẳng từ trên, cụm lớn rõ. |
| `deck-decals-glyph` | 1, chọn | Vòng cyan bằng hình thoi, chấm, cung và đoạn ngắn; không bảng chữ. Có vành vật liệu đá/thép dày hơn một vòng ánh sáng thuần. |
| `deck-decals-crack` | 1, chọn | Khe sâu cắt chéo dải đá cổ, trang trí hình học và viền thép. |

[Danh mục 16 đầu ra gốc](../../games/typing-survival/art-src/_review/125/generation-sources-final.json) ghi đường dẫn công cụ, prompt, đích chép và ảnh đính kèm. Phép kiểm cuối xác nhận mọi `.tryN.png` còn trùng byte với đầu ra công cụ. Không có lượt sinh thứ tư.

ARENA chung nói không có sinh vật; phần riêng của leviathan được giải thích rõ là ngoại lệ duy nhất. Cảnh nền không vẽ người, súng, tàu, bầy quái hoặc HUD.

## 3. Hậu kỳ và kiểm không phá tranh

Tách lần đầu bằng bản sao **không sửa** của `tools/art-normalize/key-alpha.sh` cùng ba file phụ trong `_review/125/art-normalize/`. File tạm của công cụ vì thế nằm trong thư mục được phép ghi. Dùng `ART_MAGICK=/opt/homebrew/bin/magick`; không cài thêm gói.

Bản đầu đạt phép đếm hue nhưng còn viền hồng ở muội và xanh ở sương. Không dùng điểm số ấy để nhận ảnh. Bước sửa cuối giải pha màu nền trên RGB nguồn, giao alpha với mask công cụ chuẩn, thu Lanczos rồi dọn thành phần mask rời dưới 20 px. Leviathan khử thêm kênh xanh lẫn trong RGB của sương alpha một phần. Giữ nguyên alpha và dáng ở bước khử xanh ấy. Không thay mảng vẽ, không phủ màu lên trời/sàn, không làm tối hộp chữ, không san phẳng chi tiết. **Hệ số chỉnh phơi sáng toàn ảnh của cả bộ bằng 1**; không cần giảm sáng để ép số.

Sàn và gờ chỉ sửa dải biên 16 px để khớp giá trị ở hai đầu; phần nội thất được giữ. Có nét hơi mềm tại các dải sửa mép; đã trừ vào Q. Chi tiết dọc đường, khe nối và bề mặt mòn vẫn rõ. Mô típ lát còn nhận ra khi nhìn bảng 3 × 3, không khẳng định hết lặp.

Tám tờ **bản sinh | bản hậu kỳ** cùng cỡ, mỗi ô 640 × 640 có giữ tỷ lệ và đệm ngoài, ở `_review/125/`:

| Ảnh | Tờ đối chiếu cuối |
| --- | --- |
| Sàn | [deck-tile.before-after-v6.jpg](../../games/typing-survival/art-src/_review/125/deck-tile.before-after-v6.jpg) |
| Gờ | [deck-edge.before-after-v6.jpg](../../games/typing-survival/art-src/_review/125/deck-edge.before-after-v6.jpg) |
| Tường trái | [wall-left.before-after-v6.jpg](../../games/typing-survival/art-src/_review/125/wall-left.before-after-v6.jpg) |
| Tường phải | [wall-right.before-after-v6.jpg](../../games/typing-survival/art-src/_review/125/wall-right.before-after-v6.jpg) |
| Vòng xa | [far-ring.before-after-v6.jpg](../../games/typing-survival/art-src/_review/125/far-ring.before-after-v6.jpg) |
| Trời | [sky-disk.before-after-v6.jpg](../../games/typing-survival/art-src/_review/125/sky-disk.before-after-v6.jpg) |
| Leviathan | [void-leviathan.before-after-v6.jpg](../../games/typing-survival/art-src/_review/125/void-leviathan.before-after-v6.jpg) |
| Atlas | [deck-decals.before-after-v6.jpg](../../games/typing-survival/art-src/_review/125/deck-decals.before-after-v6.jpg) |

## 4. Số đo bắt buộc

[measurements-final.json](../../games/typing-survival/art-src/_review/125/measurements-final.json) đo lại từ PNG **giao cuối**. Luma dùng `0,2126R + 0,7152G + 0,0722B` trên sRGB 0–1, không tuyến tính hóa. “Đục” là alpha 255, theo phép đo bộ 088.

| Ảnh dưới chữ | Luma TB px đục ≤ 0,16 | Px luma > 0,8 ≤ 2 % |
| --- | ---: | ---: |
| `deck-tile` | **0,159663** | **0,018787 %** |
| `deck-edge` | **0,123925** | **0,095883 %** |
| `wall-left` | **0,143757** | **0,450815 %** |
| `wall-right` | **0,143009** | **0,122976 %** |

| Ảnh alpha | Min / max | Px alpha > 0 mang hue nền ±12°, S > 0,5 | Thành phần rời < 20 px |
| --- | --- | ---: | ---: |
| Gờ | **0 / 255** | **0 / 0 %** | **0** |
| Tường trái | **0 / 255** | **0 / 0 %** | **0** |
| Tường phải | **0 / 255** | **0 / 0 %** | **0** |
| Vòng xa | **0 / 255** | **0 / 0 %** | **0** |
| Leviathan | **0 / 255** | **0 / 0 %** | **0** |
| Atlas | **0 / 255** | **0 / 0 %** | **0** |

[Tờ mép 4×](../../games/typing-survival/art-src/_review/125-edge.jpg) lấy chín ô thật có mép: hai tường, gờ, vòng xa, vương miện và sương leviathan, muội, kính, glyph. Mỗi ô nguồn 128² được phóng đúng 512² bằng point, không thu lại trong tờ. Tọa độ lưu ở `edge-exact4x-coordinates.json`. Không thấy dải nền magenta/green sáng liên tục. Một số viền giàn mảnh còn sắc ấm hoặc lam và sương có rìa hơi hạt; Claude cần xem trực tiếp trên hai nền navy/xám ở cỡ đầy đủ, các file `<tên>.navy-v6.jpg` và `<tên>.grey-v6.jpg`.

Mép đo như phiếu 095: E là sai khác luma trung bình hai biên đối diện; I là sai khác pixel liền kề trong ảnh. Sàn lấy trung bình X/Y; gờ chỉ X. Đã đạt ngay trước sửa biên, sau sửa hai đầu bằng nhau:

| Ảnh | E/I trước | E sau | I sau | E/I sau ≤ 1,25 |
| --- | ---: | ---: | ---: | ---: |
| `deck-tile`, X/Y | 0,777902 | **0** | **0,034616** | **0** |
| `deck-edge`, X | 1,193913 | **0** | **0,008075** | **0** |

[Tờ lát 3 × 3](../../games/typing-survival/art-src/_review/125-tile-check-v6.jpg): không thấy đường nối sáng cứng, vẫn thấy nhịp hai dải đá và glyph khi cố nhìn lặp. Làn có phiến dọc, rãnh, đinh, vết mòn, gờ có mặt cắt và decal phá lặp; **không trông như dải màu đều có mép mờ**. Chưa đo UV hay nghiệm thu đường trong runtime vì phiếu cấm sửa mã/chạy game.

Đã xem toàn bộ bản giao ở khổ đầy đủ và [cạnh dài 384 px](../../games/typing-survival/art-src/_review/125-384-v6.jpg). Không thấy chữ, số, logo, HUD, chữ ký. Ký hiệu là hình thoi, chấm, vòng và nét trừu tượng, không ghép thành từ đọc được.

## 5. Ảnh ghép, tham chiếu và M

- [Ảnh ghép cuối 1536 × 1024](../../games/typing-survival/art-src/_review/125-composite-v6.jpg): có đủ tám lớp, hai gờ, decal vòng ở giữa đáy; từ sau và trên nhìn dọc làn. Sàn chỉ lấy mẫu texture đã sinh qua mipmap Lanczos và phép chiếu, không vẽ thêm hoa văn/cảnh bằng mã.
- [Ảnh ghép cạnh FIGHT B của 112](../../games/typing-survival/art-src/_review/125/composite-vs-fight-v6.jpg): giữ ảnh ghép riêng đúng khổ; tờ so rộng hơn để đặt hai ảnh cạnh nhau.
- [Ảnh ghép cạnh chuẩn, hàng dưới bộ 088](../../games/typing-survival/art-src/_review/125-vs-ref-v6.jpg): các ảnh nội dung cao 640 px, nhãn nằm ngoài.
- [Số đo vùng chữ](../../games/typing-survival/art-src/_review/125/composite-v6-metrics.json): hộp x = 537…998, y = 563…696, 61.908 px; luma TB **0,161502 ≤ 0,30**, max **0,589852**. Đo trên JPG cuối đã giải mã. Không hạ sáng vùng này bằng hậu kỳ.

**Đứng cạnh được ở mức 8:** mốc leviathan, vòng trạm vỡ và tường lớn tạo quy mô; lớp gần–giữa–xa và trời tách rõ; ánh cam có hướng, vật liệu đá/thép/kính có chi tiết. Chưa ngang mốc 9 của chủ dự án: cảnh ghép còn cứng, mặt leviathan nhìn thẳng, nhịp sàn đều và các lớp chưa hòa không khí tự nhiên như ảnh game thương mại.

**M = 8,0**, chấm trên **ảnh ghép hậu kỳ v6**, không trên bản sinh, dùng chung cho cả tám thành phần sân. Ở cỡ 384 px, mốc lớn và bảng màu vẫn đọc được; tự chấm M = 8,0. Đây là tờ ghép tĩnh để chọn media; không suy ra mức tăng sáng runtime ≤ 0,02 hoặc chất lượng hiển thị khi có chữ/quái/VFX.

Các tờ `125-composite.jpg`, `125-vs-ref.jpg`, v3 và v5 là bản kiểm trước, **không phải bản nhận cuối**. Bản đầu có vùng xám do vùng phép chiếu vô hiệu của ImageMagick; sửa bằng đệm trong suốt, không phủ tranh. V4 bị dừng vì phép lấy mẫu phối cảnh quá chậm; v5 còn răng cưa; v6 dùng mipmap cho sàn và bộ lọc phù hợp cho các lớp còn lại. Tất cả giữ nguyên để không ghi đè/xóa.

## 6. Q từng ảnh trên bản giao

Thứ tự năm tiêu chí: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi mục tối đa 2. M của mọi hàng là **8,0 trên cảnh ghép** ở trên.

| Ảnh | Khổ đầy đủ: năm điểm → Q | Cạnh dài 384 px: năm điểm → Q | Thiếu gì |
| --- | --- | --- | --- |
| Sàn | 2 / 2 / 2 / 1,5 / 1,5 → **9** | 2 / 2 / 2 / 1,5 / 1,5 → **9** | Nhịp hai dải đá dễ nhận khi lặp; vùng sửa biên hơi mềm |
| Gờ | 2 / 1,5 / 2 / 2 / 1,5 → **9** | 2 / 1,5 / 2 / 1,5 / 1,5 → **8,5** | Giàn dưới rất nhỏ ở 384 px; cần xem viền khi tích hợp |
| Tường trái | 2 / 1,5 / 2 / 2 / 1,5 → **9** | 2 / 1,5 / 2 / 1,5 / 1,5 → **8,5** | Thanh giàn mảnh giảm rõ ở cỡ nhỏ, viền nhiều chi tiết |
| Tường phải | 1,5 / 2 / 2 / 2 / 1,5 → **9** | 1,5 / 1,5 / 2 / 2 / 1,5 → **8,5** | Hai khối xếp lệch theo tầng, không thành hai phiến ngang lớn như chỉ dẫn sửa |
| Vòng xa | 2 / 1,5 / 2 / 2 / 1,5 → **9** | 2 / 1,5 / 2 / 1,5 / 1,5 → **8,5** | Chi tiết viền dày hơn bóng xa lý tưởng; nhịp hai vòng vẫn khá cân |
| Trời | 2 / 2 / 2 / 2 / 1,5 → **9,5** | 2 / 2 / 2 / 1,5 / 1,5 → **9** | Filament dày; cần tiết chế bloom trong game, chưa kiểm runtime |
| Leviathan | 2 / 2 / 1,5 / 2 / 1,5 → **9** | 2 / 1,5 / 1,5 / 2 / 1,5 → **8,5** | Sáu mắt rõ ở ảnh lớn; mắt nhỏ và nhấn tím/sương khá nhiều ở cỡ thu |
| Atlas | 2 / 1,5 / 2 / 1,5 / 1,5 → **8,5** | 2 / 1,5 / 2 / 1,5 / 1 → **8** | Vòng glyph có vành đá/thép; vài mảnh kính nhỏ hòa vào nhau ở cỡ atlas 384 px |

Tự chấm đạt ngưỡng; Claude cần chấm lại M/Q và xem PNG nguyên khổ, nhất là mép giàn, sương và vành glyph. Không dùng điểm tự chấm thay cho nghiệm thu độc lập.

## 7. KA1, script và phạm vi

Chạy `/sbin/md5 -r` đệ quy toàn `games/typing-survival/art-src/`, trước khi ghi bất kỳ file nào của phiếu và sau khi xong media/script/tờ kiểm:

| Chỉ số | Kết quả |
| --- | ---: |
| File mốc trước | **330** |
| File trong snapshot sau | **743** |
| File thêm | **413** |
| File cũ đổi MD5 | **0** |
| File cũ mất | **0** |
| Dòng dữ liệu bị bỏ trong diff | **0** |

[Mốc trước](../../games/typing-survival/art-src/_review/125/md5-before.txt), [mốc sau](../../games/typing-survival/art-src/_review/125/md5-after.txt), [diff](../../games/typing-survival/art-src/_review/125/md5-diff.txt), [tóm tắt](../../games/typing-survival/art-src/_review/125/md5-summary.json). **Diff chỉ thêm dòng dữ liệu.** Ba nhật ký sau được ghi sau snapshot, không thể tự băm chính mình; tổng thư mục sau thêm ba file ấy là 746 file. Báo cáo nằm ngoài `art-src/`.

Script, bản sao công cụ và tham số đều trong [_review/125/](../../games/typing-survival/art-src/_review/125/); xem [RUNBOOK.md](../../games/typing-survival/art-src/_review/125/RUNBOOK.md). Các bước cuối: `matte-v3.mjs`, `matte-v4-leviathan.mjs`, `publish.py`, `floor-project.mjs`, `review-v6.mjs`, `edges-v3.mjs`, `verify.mjs`, `md5-audit.py`. Các bản script trước giữ làm nhật ký. Không chạy lại lệnh ghi trên đầu ra đã có.

**Bỏ qua:** không sinh tiếp ảnh đã đạt; không âm thanh vì phiếu chỉ có ảnh; không tích hợp, sửa mã, đổi luật chơi, chạy Git, build/test, dev server, trình duyệt hoặc mạng ngoài `image_gen`, theo giới hạn phiếu. Không đọc/ghi Tu Tiên hay ghi sang game khác. Không có capture trình duyệt/raw frame cần prune; các `.try` phải giữ.

**Chủ dự án/Claude cần xem:** ảnh ghép v6, tờ so chuẩn và tờ mép 4×; duyệt tám file trong bảng đầu. Chú ý hậu tố `-alpha-v3` khi chọn file, không lấy các bản hậu kỳ trước cùng thư mục.
