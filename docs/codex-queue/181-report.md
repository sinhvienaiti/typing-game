# Phiếu 181 · Tờ tư thế khóa cho animation

Ngày 29/10/2026, Mac mini M4. Công cụ sinh: **image_gen tích hợp**. **Đã giao 3/4 tờ; phiếu chưa hoàn tất vì thiếu ảnh nguồn Hỏa Long.** Không chạy Git, mạng ngoài công cụ sinh ảnh, game, build hay test. Không sửa mã, tài liệu thiết kế, nguồn ảnh hoặc Tu Tiên. Tài liệu mới duy nhất là báo cáo này.

## Bản chọn

| Tờ | Tệp | Lượt sinh / bản chọn | Khổ cuối | KA5 tự chấm |
|---|---|---|---|---|
| Lightbearer | [keyposes-lightbearer.png](../../games/typing-survival/art-src/anim-ref/keyposes-lightbearer.png) | 1 / lượt 1 | 3072 × 1024 | **8,8/10 · đạt ảnh 2D** |
| Mộc Tinh | [keyposes-moc-tinh.png](../../games/typing-defense/art-src/anim-ref/keyposes-moc-tinh.png) | 3 / lượt 3 | 3072 × 1024 | **8,8/10 · đạt ảnh 2D** |
| Sáu họ quái Dragonhold | [silhouettes-dh-foes.png](../../games/dragon-hold/art-src/anim-ref/silhouettes-dh-foes.png) | 2 / lượt 2 | 3072 × 1024 | **9,0/10 · đạt ảnh 2D** |
| Hỏa Long | Chưa sinh | 0 | — | Chưa chấm |

Mỗi bản chọn có `.prompt.txt` nguyên văn cạnh ảnh. Giữ mọi `.tryN.png` và prompt của lượt sinh. Tổng **6 ảnh sinh thành công**, không tờ nào quá 3 lượt. Một yêu cầu quái bị công cụ từ chối ngay trước khi sinh vì nhận tối đa 5 ảnh nguồn; đã ghép sáu nguồn thành một bảng để gửi lại. Văn bản yêu cầu bị từ chối được giữ ở `silhouettes-dh-foes.try1.prompt.txt`; **prompt thực tế của ảnh `.try1.png` là `.try1b.prompt.txt`**, được ghi rõ trong `_review/silhouettes-dh-foes-generation.json`. Prompt bản chọn `.prompt.txt` khớp lượt 2.

## Nguồn và bố trí

- **Lightbearer:** `games/typing-survival/art-src/models-src/lightbearer-front.png` khóa nhận diện, cùng `concepts/b-lightbearer-fight.png` làm ngữ cảnh trang phục. Đã xem cả mặt nạ phiếu 156. Giữ mũ kín hai sừng vàng, giáp trắng viền vàng, lõi ngực lam và áo choàng xanh. Thứ tự: thủ ×2; lướt trái/phải; bắn trái/phải; bị đánh ×2; quỳ; đứng dậy; thắng ×2.
- **Mộc Tinh:** `games/typing-defense/art-src/portraits/moc-tinh.png`. Giữ mặt già, lông mày và râu gỗ sáng, tán lá xanh và chùm quả cam; thân đầy đủ được diễn giải từ chân dung, cần người dựng clip kiểm lại với rig. Thứ tự: nghỉ ×2; gồng ×2; tung chiêu ×2; bị đánh ×2; giận; choáng; ngã ×2. Lượt 2 bổ sung hai mũi tên thiếu; lượt 3 sửa bàn tay cành thừa ở ô bị đánh đầu tiên. Bản chọn chỉ còn hai tay ở ô đó.
- **Quái:** `games/dragon-hold/art-src/enemies/{moss-grunt,blight-wolf,tusk-boar,thorn-wasp,thorn-ant}.png`; Moss Bannerman lấy từ `generals/moss-banner.png` vì không có tệp tương ứng trong `enemies/`. Mỗi cặp ô là đỉnh tấn công rồi chết. Hàng trên: Grunt, Wolf, Boar; hàng dưới: Wasp, Ant, Bannerman. Lượt 2 bỏ nét sáng bên trong bóng bằng image_gen.

## Kiểm 1–3 và số đo

Ba bản chọn đều có lưới **6 × 2, ô 512 × 512**, nền sáng, đủ 12 dáng; đã xem toàn tờ ở khổ đầy đủ và ảnh kiểm thu nhỏ. **0 chữ, 0 số** trong ba tờ giao, có mũi tên hình vẽ. Không dùng OCR để thay cho xem ảnh. Cả 36 ô đọc được ở 256 px; 12 ô quái cũng đã xem ở **64 px/ô**.

| Tờ | IoU cặp 1–2 | 3–4 | 5–6 | 7–8 | 9–10 | 11–12 | IoU lớn nhất sau đưa cùng tâm |
|---|---|---|---|---|---|---|---|
| Lightbearer | 0,5473 | 0,4809 | 0,3769 | 0,6159 | 0,5513 | 0,5673 | 0,6720 |
| Mộc Tinh, lượt 3 | 0,7269 | 0,6679 | 0,4638 | 0,5903 | 0,6120 | 0,4543 | 0,7351 |
| Quái | 0,2289 | 0,0608 | 0,3638 | 0,0881 | 0,2603 | 0,2109 | 0,5705 |

Tất cả cặp đo **≤ 0,85**, gồm cả các cặp khác hành động được đo thêm. Mặt nạ đo ở 256 px/ô: ngưỡng RGB tách khối chính, loại mũi tên đỏ và thành phần rời dưới 45 pixel, lấp vùng sáng khép kín; quái dùng ngưỡng đen. Đây là mặt nạ chẩn đoán gần đúng, có thể bỏ sót một số phần giáp trắng/ngón nhỏ; không phải phân đoạn được tô tay. IoU chính giữ nguyên tọa độ ô; phép kiểm thêm chỉ tịnh tiến theo tâm hộp bao, không xoay hay đổi cỡ. Không dùng số đo để tô sửa ảnh giao.

Tờ đối chiếu nguồn, mỗi tờ cạnh nguồn của chính nó:

- [Lightbearer · 181-vs-source.jpg](../../games/typing-survival/art-src/anim-ref/_review/181-vs-source.jpg)
- [Mộc Tinh · 181-vs-source.jpg](../../games/typing-defense/art-src/anim-ref/_review/181-vs-source.jpg)
- [Quái · 181-vs-source.jpg](../../games/dragon-hold/art-src/anim-ref/_review/181-vs-source.jpg)

Số đo và mặt nạ ở `_review/` trong từng thư mục đích: Lightbearer và quái dùng `<tên>-metrics.json`, `<tên>-masks-256.png`; **Mộc Tinh dùng `<tên>-metrics-final.json`, `<tên>-masks-final-256.png`**. Số đo Mộc Tinh không có `final` là hồ sơ lượt 2, đã bị thay thế về giá trị nghiệm thu. Quái có thêm `silhouettes-dh-foes-64.png`.

## Hậu kỳ §5 và KA1

Ảnh sinh thực tế **2172 × 724**, cùng tỉ lệ 3:1. Bản chọn chỉ đổi cỡ đều bằng ImageMagick Lanczos lên **3072 × 1024**, hệ số **256/181**. Không cắt, phủ màu, san phẳng, tách nền hoặc chỉnh gamma. Không tạo thêm chi tiết thực khi phóng ảnh. Việc sửa tay thừa và nét bóng đen thực hiện bằng lượt image_gen, giữ ảnh trước đó.

Đã xem ba tờ “bản sinh | bản hậu kỳ”, hai phía cùng cỡ 1536 × 512:

- [Lightbearer](../../games/typing-survival/art-src/anim-ref/_review/keyposes-lightbearer-before-after.jpg)
- [Mộc Tinh, lượt 3](../../games/typing-defense/art-src/anim-ref/_review/keyposes-moc-tinh-before-after.jpg)
- [Quái](../../games/dragon-hold/art-src/anim-ref/_review/silhouettes-dh-foes-before-after.jpg)

**KA1:** trước tác vụ, cả ba thư mục `art-src/anim-ref/` chưa có tệp. Đã lập MD5 trước khi sinh, sau bước kiểm và bản chốt; xem `_review/181-ka1-before.json`, `181-ka1-after.json`, `181-ka1-final.json` trong từng thư mục. **0 tệp có trước bị đổi hoặc mất ở cả ba đích.** Các bản chọn và tờ kiểm do chính phiếu này tạo được cập nhật theo lượt chọn, các ảnh thử giữ nguyên. Bản kê tự loại chính nó để tránh vòng băm.

## KA5 trên bản hậu kỳ

Mỗi tiêu chí tối đa 2 điểm theo ART_ACCEPTANCE; điểm này đánh giá **tờ tham chiếu 2D**, không chứng nhận clip animation dùng chung.

| Tờ | Đúng đề | Đọc được | Hợp bộ | Hình khối | Dùng bước sau | Tổng |
|---|---|---|---|---|---|---|
| Lightbearer | 2,0 | 1,8 | 1,8 | 1,6 | 1,6 | **8,8 · đạt** |
| Mộc Tinh | 2,0 | 1,7 | 1,9 | 1,6 | 1,6 | **8,8 · đạt** |
| Quái | 1,9 | 1,9 | 1,8 | 1,7 | 1,7 | **9,0 · đạt** |

Điểm còn thiếu: áo choàng Lightbearer che một phần chân, bàn tay sau ở ô lướt phải sát đường chia ô; tán Mộc Tinh vẫn là khối lớn ở dáng nghỉ/gồng, thân và chân rễ là diễn giải từ ảnh chân dung; bóng quái bỏ toàn bộ thông tin vật liệu, cần so nguồn khi đặt xương, một số chân côn trùng chồng ở tư thế chết. Chưa có góc cận riêng hoặc mốc thời gian cho clip vì phiếu chỉ yêu cầu một tờ 12 ô/nhân vật.

Chưa có hai giám khảo độc lập hay chủ dự án duyệt animation. Khi dựng clip vẫn phải qua cổng **từ 9 điểm** của SHARED_SYSTEMS_BAR. Không sửa ART_REPLACE_LATER hoặc tài liệu khác vì ngoài đường dẫn được phép.

## Phần chưa làm và chủ dự án cần xem

**Chưa sinh `keyposes-hoa-long`.** Không tìm thấy ảnh 2D rồng lửa đỏ cam trong `games/dragon-hold/art-src/` sau khi tìm tên `draconis`, `dragon`, `long`, `hoa`, `fire` và kiểm tra các thư mục nguồn. Các ảnh tên `dragon` tìm được là icon, tượng hoặc tờ duyệt icon. Có model Draconis ở `public/` và ảnh Draconis của Wordwoven, nhưng chưa có căn cứ nhận chúng là ảnh nguồn Hỏa Long được phiếu chỉ định. Không tự dùng nhân vật khác để chấm đạt nhận diện. Đã gửi câu hỏi xin **đường dẫn nguồn Hỏa Long**; chưa nhận được câu trả lời khi chốt báo cáo.

Chủ dự án cần cung cấp đường dẫn đó để làm tờ thứ tư, và xem ba tờ đối chiếu nguồn trước khi giao người dựng clip. **Điều kiện xong 4/4 chưa đạt.** Không tạo âm thanh, không gọi Tripo, không chụp trình duyệt nên không có khung chụp thô cần dọn.
