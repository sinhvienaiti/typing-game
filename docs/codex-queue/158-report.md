# Phiếu 158 · Wordwoven · Làm lại nền tựa và poster

Ngày làm: 29/10/2026. Nguồn luật: phiếu 113, báo cáo 113, chỉ dẫn nhận ảnh 29/10 và phiếu 158. Dùng công cụ tích hợp `image_gen`, không dùng API/CLI sinh ảnh ngoài.

**Trạng thái: đã giao hai ứng viên v2 và hồ sơ kiểm; chưa đủ điều kiện nghiệm thu toàn phiếu.** Nền tựa hết hộp tối, logo đọc rõ, nhưng dải kiểm hình học còn vướng mép đầu rùa và mái Fort; ngưỡng menu còn mâu thuẫn với việc giữ tranh. Poster giữ trọn cánh, ít chi tiết hơn, nhưng cây chưa cao hơn mọi vách và cánh còn lấn vùng trời dành cho logo. Không tự đánh dấu đạt dựa riêng vào mức hoàn thiện mỹ thuật.

## 1. Ảnh, lượt sinh và prompt

Gốc đường dẫn ảnh: `games/typing-defense/art-src/ui/title-epic/`.

| Bản giao để duyệt | Nguồn chọn | Khổ cuối | Bản thu |
| --- | --- | --- | --- |
| `title-backdrop.v2.png` | `title-backdrop.v2.try1.png` | 1536 × 1024 | `title-backdrop.v2.384.png`, 384 × 256 |
| `poster.v2.png` | `poster.v2.try2.png` | 1024 × 1536 | `poster.v2.384.png`, 256 × 384 |

Mỗi lượt có `.prompt.txt` cạnh ảnh, gồm nguyên văn toàn bộ prompt thực gửi. Prompt bản chọn trùng prompt lượt chọn. Bản thu và từng tờ kiểm cũng có `.prompt.txt`, ghi prompt nguồn và lệnh hậu kỳ, phân biệt rõ với prompt của lượt sinh mới.

**Nền tựa: một lượt sửa ảnh đúng giới hạn riêng của phiếu 158.** Đính kèm `title-backdrop.try1.png`, đã xem trước bằng `view_image`. Dán nguyên văn đoạn tiếng Anh trong mục sửa 113 `title-backdrop` của verdict, rồi bổ sung tọa độ vùng logo trên nguồn, yêu cầu dời tháp nhọn sang phải, giữ rồng hoàn toàn dưới dải logo, giữ các lớp cảnh và màu. Đề nghị ruộng xanh ngọc/vàng lúa chín trầm, vùng yên khoảng 40%. Kết quả: rồng chuyển xuống trái nhưng lớn hơn trước và thấp hơn mốc 35%; tháp nhọn chuyển sang phải; trời giữ sáng tự nhiên. Công cụ chưa giữ vị trí đầu rùa hoàn toàn ngoài dải logo. Không sửa lần hai vì phiếu chỉ cho một lượt sửa nền tựa.

**Poster: hai lượt mới, cộng lượt gốc là ba lượt.** Cả hai lần đều đính kèm `keyart.png`, giữ nguyên văn đoạn tiếng Anh trong mục sửa 113 `poster` của verdict ở đầu prompt.

| Lượt | Sửa prompt | Kết quả |
| --- | --- | --- |
| `poster.v2.try1` — lượt 2 tính cả phiếu gốc | Bổ sung nhận diện nhân vật, trọn cánh và lề, một trọng tâm, khoảng 40% trời/sương/nước, cây cao hơn mọi vách. | Khổ dọc đúng nhưng cánh trên vẫn chạm/cắt mép, nhiều vách cao hơn cây. Không chọn. |
| `poster.v2.try2` — lượt 3 tính cả phiếu gốc | Khóa hình rồng vào một hộp tọa độ nằm dưới vùng trời, đầu/crown cây cao hơn đỉnh vách, Fort nhỏ ở phải dưới; chỉ hai vệt tên và ba đèn. | Hai cánh đã nằm trọn khung, chỉ hai vệt tên và ba đèn. Cây lớn hơn nhưng một vách trái vẫn cao hơn; mô hình chưa tuân hộp tọa độ và trời 22%. Chọn làm ứng viên tốt nhất, không ghi đạt. |

Không sinh lượt thứ tư cho poster. [Tờ các lượt poster](../../games/typing-defense/art-src/_review/158/poster-attempts.jpg) giữ cả lượt gốc và hai lượt làm lại.

## 2. Hậu kỳ và kiểm không phá tranh

**Hai bản `.v2.png` là bản sao nguyên byte của nguồn được chọn.** Không cắt tranh cuối, không chỉnh gamma, màu, sáng hay tương phản; không phủ màu, hộp tối, vignette hoặc vẽ lại bằng công cụ. Không phóng to nguồn. Hai nguồn sinh đã đúng khổ yêu cầu nên không cần chuẩn hóa khổ.

| Bản chọn | MD5 nguồn sinh và bản cuối | Nguồn = cuối |
| --- | --- | --- |
| Nền tựa | `4a526c42919b5cc8a391f2efc637e115` | Trùng byte |
| Poster | `dc4eab069ff22215a3c03921c4673da7` | Trùng byte |

Các tờ bắt buộc cùng cao 640 px ở mỗi bên:

- [Nền tựa: bản sinh \| bản hậu kỳ](../../games/typing-defense/art-src/_review/158/raw-vs-final/title-backdrop.jpg).
- [Poster: bản sinh \| bản hậu kỳ](../../games/typing-defense/art-src/_review/158/raw-vs-final/poster.jpg).
- [Try1 cũ \| sau lượt sửa nền tựa](../../games/typing-defense/art-src/_review/158/title-before-edit.jpg): phân biệt thay đổi do lượt sửa ảnh với hậu kỳ xác định.

Các bản 384 px dùng `/opt/homebrew/bin/magick INPUT -filter Lanczos -resize '384x384>' -strip OUTPUT`. Mock cắt giữa nền tựa thành `1536x864+0+80`, thu về 1280 × 720; logo alpha sạch của phiếu 113 thu về 576 × 192, đặt tại +352+6. Không thêm lớp tối sau logo. Khối menu xám chỉ nằm trên tờ kiểm vị trí menu, không nằm trong tranh cuối.

Script và lệnh được lưu ở [_review/158/deliver.py](../../games/typing-defense/art-src/_review/158/deliver.py), `commands.json`, `detail-commands.json`, `detail-corrected-commands.json`. Font nhãn: `/System/Library/Fonts/Supplemental/Arial.ttf`. Script gọi ImageMagick bằng mảng đối số, chặn ghi đè đầu ra. Dựng lại vào thư mục/tờ mới, ví dụ:

```sh
python3 games/typing-defense/art-src/_review/158/deliver.py \
  --out games/typing-defense/art-src/_review/158/recheck-1 \
  --comparison games/typing-defense/art-src/_review/158/recheck-1/vs-ref.jpg
```

Tờ `poster-models.jpg` đầu tiên cắt lệch do gravity kế thừa; không dùng tờ đó để duyệt. Đã khóa gravity về `northwest` và lưu thành `poster-models-corrected.jpg`, giữ tờ nháp để không ghi đè file đã có.

## 3. Kiểm theo phiếu 113 và 158

| Kiểm | Kết quả |
| --- | --- |
| KA1, MD5 đệ quy toàn bộ `art-src/ui/` | Trước 156, sau 170 file; **thêm 14, sửa 0, xóa 0**. `md5-diff.txt` chỉ có dòng dữ liệu thêm. |
| Khổ hai bản cuối | Đạt, 1536 × 1024 và 1024 × 1536; không ép dọc keyart bằng công cụ. |
| Chữ lạc, số, chữ ký, watermark trong hai tranh | Không thấy qua quan sát ảnh nguồn đầy đủ và bản 384 px. Không dùng OCR để giả làm chứng nhận máy. |
| Chính tả, alpha logo/emblem | Không tạo hay sửa trong phiếu này. Mock dùng bản logo sạch đã được Claude nhận ở `_review/113/delivery-alpha/logo.alpha.png`; kiểm chữ và alpha kế thừa hồ sơ 113. |
| Logo std luma ≤ 0,12 | **Đã bỏ theo phiếu 158**. Chỉ đo để đối chiếu: 0,148465; không dùng làm điều kiện đạt. |
| Vùng menu x 3–35%, y 55–92% trên bản cắt giữa | Std luma **0,195069**, vượt ngưỡng **0,14** còn lại của phiếu 113. Không đạt số này; giữ tranh, không làm tối/giảm tương phản cục bộ. |
| Dải logo x 25–75%, y 6–30% trên bản cắt | Rồng và tháp nhọn đã ra ngoài. Mép đầu rùa còn lấn mép phải dải; vài mái Fort nằm ở đáy dải. Logo thực đặt thử không chồng rồng/rùa/tháp nhọn, nhưng chưa đạt cách hiểu nghiêm ngặt «cả dải không có rùa hay đỉnh tháp». |
| Logo đặt thử | Đọc rõ cả từ Wordwoven nhờ viền đồng sẫm, không cần nung hộp tối vào trời. Mái Fort gần mép dưới nét lượn. |
| Nhận diện nhân vật poster | Khớp các nét chính: Draconis trắng vàng, sừng/giáp đen viền vàng, cánh lông vàng đầu cam; cây vỏ nhạt xoắn, mặt râu gỗ, mắt hổ phách, quả và ngực rỗng. Cánh rồng uốn cong mạnh hơn dáng chuẩn. Fort giữ đá sáng và mái đỏ. |
| Đọc ở 384 px cạnh dài | Cả hai tranh nhận ra rồng/tháp; poster nhận rõ cây, nhưng vách trái vẫn cao hơn cây. Hai đầu cánh đều cách mép khung. |
| Poster: khoảng trời 22% phía trên | Không đạt hoàn toàn: cánh phải bắt đầu khoảng y 120–125/1536 (khoảng 8%), lấn vùng 22%. Trời có mây/tia nắng, không phẳng đen. |
| Poster: đầu cây khoảng 45%, cao hơn mọi vách | Không đạt: mặt cây khoảng y 830/1536 (54%); đỉnh vách trái khoảng y 560, cao hơn cả tán cây bắt đầu khoảng y 650. Các mốc này là ước lượng quan sát, không phải phân đoạn máy. |
| Ít chi tiết, vùng yên khoảng 40% | Đã giảm poster còn hai vệt tên và ba đèn, thêm trời và sương. Chưa xác nhận đạt 40% bằng mặt nạ; đáy 15% vẫn còn vài vật/đèn. Nền tựa còn nhiều đèn/kiến trúc theo yêu cầu giữ try1. |
| Ruộng xanh ngọc/vàng trầm | Đã yêu cầu trong prompt, nhưng nền tựa vẫn còn mảng ruộng vàng khá rực. Không tự ghi đạt màu; không dùng công cụ đổi riêng mảng ruộng vì luật hậu kỳ mới chỉ cho chỉnh sáng nhẹ toàn ảnh. |

Luma tính trên RGB sRGB mã hóa: `(0,2126R + 0,7152G + 0,0722B)/255`, độ lệch chuẩn tổng thể. Hộp đo nguồn: logo `[384,131,768,209]`, menu `[46,555,492,320]`. Số và dấu trùng byte ở [measurements.json](../../games/typing-defense/art-src/_review/158/measurements.json); hồ sơ băm ở `md5-before.txt`, `md5-after.txt`, `md5-summary.json` trong cùng thư mục.

**Mâu thuẫn để Claude quyết:** ngưỡng menu ≤ 0,14 còn trong phiếu gốc, trong khi vị trí đó chứa lan can, sông và sương có tương phản tự nhiên. Cách ép số cũ chính là hậu kỳ làm hỏng tranh. Dừng ở bản nguyên vẹn, đề nghị người duyệt quyết dùng bảng UI 115 hoặc điều chỉnh tiêu chí menu; phiếu này không sửa UI và không tự bỏ ngưỡng.

## 4. Tờ kiểm để duyệt

- [158-vs-ref.jpg](../../games/typing-defense/art-src/_review/158-vs-ref.jpg): hai bản mới và tham chiếu chủ dự án cùng cao **640 px phần hình**; hàng dưới có mock logo đúng **1280 × 720**, không phóng.
- [Mock logo 1280 × 720](../../games/typing-defense/art-src/_review/158/title-mock.jpg): xem độ đọc logo trên trời tự nhiên.
- [Dải kiểm logo](../../games/typing-defense/art-src/_review/158/title-logo-band.jpg): khung đỏ chỉ phục vụ kiểm hình học.
- [Mock vị trí menu](../../games/typing-defense/art-src/_review/158/title-menu-layout.jpg): khối xám 30% × 35% chỉ là ô chiếm chỗ.
- [Hai tranh cạnh dài 384 px](../../games/typing-defense/art-src/_review/158/small-sizes.jpg).
- [Poster so model — tờ đúng](../../games/typing-defense/art-src/_review/158/poster-models-corrected.jpg).

Không mở game hay trình duyệt; đây là kiểm ảnh và mock tĩnh, không phải nghiệm thu UI runtime. Không có frame chụp trình duyệt cần prune. Các `.tryN.png` là nguồn sinh bắt buộc giữ.

## 5. Tự chấm trên bản cuối

M theo mức chợ, ảnh chủ dự án là mốc 9. Q theo thứ tự Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp. Điểm không thay thế các kiểm bắt buộc còn trượt.

| Bản cuối | M đầy đủ | Q đầy đủ | M ở cạnh dài 384 px | Q ở 384 px | So với tham chiếu |
| --- | ---: | --- | ---: | --- | --- |
| `title-backdrop.v2.png` | 8,5 | 8,5 (1,5/2/2/1,5/1,5) | 8 | 8,5 | **Đứng cạnh được về tranh:** Fort/rùa khổng lồ, bốn lớp sâu, nắng xiên và thác bạc; không hộp xám. Chưa qua hết điều kiện dải logo/menu và ruộng còn rực. |
| `poster.v2.png` | 8 | **7,5 (1/2/2/1,5/1)** | 8 | **7,5** | **Chưa đứng cạnh được như poster hoàn chỉnh theo brief:** chất liệu/ánh sáng có tầm, hai nhân vật đọc rõ và cánh không cắt, nhưng sai tương quan cây–vách, vùng trời logo và độ cong cánh. |

Không nâng Q lên 8 chỉ vì tranh đẹp. Không chấm poster đạt khi còn sai hai điểm bố cục chính mà người chấm đã trả ở phiếu 113.

## 6. Phạm vi và việc cần xem

Chỉ thêm ảnh/prompt v2 trong `ui/title-epic/`, hồ sơ ở `_review/158/`, `_review/158-vs-ref.jpg` cùng prompt, và báo cáo này. Giữ nguyên mọi bản cũ, keyart, logo, emblem và báo cáo 113. Không chạy lệnh Git, build, test suite, dev server hay mạng ngoài công cụ sinh ảnh; không sửa mã, âm thanh, tài liệu khác hoặc game khác; không đọc/ghi Tu Tiên.

**Claude/chủ dự án cần xem:** tờ so tham chiếu và mock logo để quyết nền tựa cùng mâu thuẫn ngưỡng menu; poster v2 là ứng viên tốt nhất sau tổng cộng ba lượt, vẫn cần đổi cách nếu giữ nguyên các điều kiện bố cục. Chưa đổi asset runtime hay chép đè bản cũ. Phiếu 158 **chưa nghiệm thu trọn vẹn**.
