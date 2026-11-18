# Phiếu 314 · Ba hướng biểu tượng kỹ năng

Ngày 06/11/2026. Đã gọi **image_gen 7 lần: đúng 6 lượt chính + 1 lượt vẽ lại**. Có đủ 6 mẫu được chọn, thêm 1 bản thử được giữ nguyên; mỗi bản có PNG gốc **1254 × 1254 px**, prompt nguyên văn và bản thu nhỏ **32/48 px**. Đã kiểm tra kênh alpha và góc ngoài trong suốt. Tổng cộng 23 PNG và 7 tệp prompt mới trong [thư mục skill-icons](../../games/immortality-cultivation/art-src/lab/ui/skill-icons).

Đã mở các tham chiếu của repo bằng `view_image`, chỉ lấy chất liệu, ánh sáng và độ hoàn thiện. Không dùng ảnh ngoài. Ảnh gốc được chép bằng `cp -n`; ImageMagick chỉ thu nhỏ và ghép tấm, không sửa tranh gốc.

Đã mở [tấm đầu](../../games/immortality-cultivation/art-src/lab/ui/skill-icons/icon-directions-sheet.v1-try1.png) và [tấm chọn cuối](../../games/immortality-cultivation/art-src/lab/ui/skill-icons/icon-directions-sheet.png) bằng `view_image` ở khổ gốc 1040 × 1080 px. Mỗi hàng một hướng; mỗi ô có ảnh 256, 48 và 32 px trên nền **#15171c**. Điểm tự chấm 0–10 ở đúng bản nhỏ, xét bốn mặt: nhận ra chiêu, cuốn hút/sang trọng, tách khung–hình, sạch; điểm chốt lấy mặt thấp nhất. Đây là duyệt mẫu theo phiếu, chưa kiểm tra trong thanh chiêu runtime hay ở 16–24 px.

| Ảnh | Điểm 32 px | Điểm 48 px | Nhận xét |
| --- | ---: | ---: | --- |
| [ink-gold · meteor · try1](../../games/immortality-cultivation/art-src/lab/ui/skill-icons/ink-gold-meteor-rain-fire.v1-try1.png) **chọn** | 8,4 | 8,7 | Đầu sáng và đuôi chéo rõ, viền mảnh nhường chỗ cho chiêu; vệt mực còn hơi nhiều. |
| [ink-gold · crescent · try1](../../games/immortality-cultivation/art-src/lab/ui/skill-icons/ink-gold-crescent-metal.v1-try1.png) **chọn** | 8,3 | 8,6 | Cung bạc đối xứng tách nền tốt, hoa văn nhỏ hòa lại nhưng dáng chính còn rõ. |
| [jewel-crest · meteor · try1](../../games/immortality-cultivation/art-src/lab/ui/skill-icons/jewel-crest-meteor-rain-fire.v1-try1.png) **chọn** | 8,1 | 8,5 | Ngọc đỏ sang, nhận ra thiên thạch; viền vàng và mặt cắt ngọc cạnh tranh với lửa. |
| [jewel-crest · crescent · try1](../../games/immortality-cultivation/art-src/lab/ui/skill-icons/jewel-crest-crescent-metal.v1-try1.png) | 7,7 | 8,0 | Tia dọc thêm vào chia hình chính ở 32 px; dưới 8 nên vẽ lại. |
| [jewel-crest · crescent · try2](../../games/immortality-cultivation/art-src/lab/ui/skill-icons/jewel-crest-crescent-metal.v1-try2.png) **chọn** | 8,3 | 8,6 | Bỏ tia dọc, cung bạc đậm và tâm tối mở nên đọc rõ hơn try1. |
| [bronze-seal · meteor · try1](../../games/immortality-cultivation/art-src/lab/ui/skill-icons/bronze-seal-meteor-rain-fire.v1-try1.png) **chọn** | 8,0 | 8,3 | Thiên thạch còn rõ, nhưng mép đồng/vân mây nặng và gần màu lửa. |
| [bronze-seal · crescent · try1](../../games/immortality-cultivation/art-src/lab/ui/skill-icons/bronze-seal-crescent-metal.v1-try1.png) **chọn** | 8,0 | 8,3 | Cung bạc nổi trên nền tối, khung cổ đẹp nhưng chi tiết mép nén thành dải ở 32 px. |

**Đề xuất ink-gold:** đọc ổn định nhất ở 32 px trên cả hai chiêu, viền nhẹ và cùng ngôn ngữ với bộ đếm chuỗi. Jewel-crest là lựa chọn nếu anh ưu tiên cảm giác ngọc/vàng; bronze-seal hợp nét cổ hơn nhưng khung nặng khi nhỏ. Tấm cuối dùng jewel-crest crescent **try2**, các ô còn lại **try1**.

Không dùng lượt vẽ lại thứ hai vì cả 6 bản chọn đều đạt ít nhất 8 ở hai cỡ. Không tích hợp game, không chạy build/test, không ghi Git, không mở cổng; không sửa hoặc xóa tệp có sẵn. Anh cần xem tấm chọn cuối ở tỷ lệ 100% và chọn hướng trước khi vẽ cả bộ.
