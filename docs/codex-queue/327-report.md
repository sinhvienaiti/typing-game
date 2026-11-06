# Phiếu 327 · Cổng trời và hai mẫu ấn Hỏa

Đã gọi **4 lần `image_gen`**, không vẽ lại; chỉ dùng ảnh repo được phiếu chỉ định. Bốn PNG gốc được chép bằng `cp -n`, đã đối chiếu SHA-256 với đầu ra công cụ; mỗi ảnh có `.prompt.txt` ghi đầy đủ prompt, ảnh tham chiếu và khổ thật.

`D = games/immortality-cultivation/art-src/lab/ui/skill-icons`.
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.

Tệp mới:
- `D/ink-gold-sky-gate-open-close.v1-try1.png`, `D/jewel-crest-sky-gate-open-close.v1-try1.png`: mỗi ảnh 1254 × 1254 px, nền ngoài trong suốt; kèm bản `-48.png`, `-32.png` và `.prompt.txt`.
- `D/sky-gate-icons-327-sheet.png`: 540 × 660 px, mỗi hàng gồm bản 256, 48 và 32 px; hai cỡ nhỏ đặt đúng 1:1 trên nền #15171c.
- `S/fire-sigil-hex.v1-try1.png`, `S/fire-sigil-line.v1-try1.png`: mỗi ảnh 1672 × 941 px, kèm `.prompt.txt`.
- `S/fire-sigils-samples-sheet.jpg`: 1680 × 1010 px; trái Kim, phải Hỏa; trên hex, dưới line.

Đã mở atlas `U/sky-gate-open-close.atlas.png` theo manifest, hai mốc biểu tượng, hai mốc dáng Kim và hai mốc chất liệu Hỏa. Giữ nguyên hai câu FRAME của phiếu 314. Các tấm ghép và bản nhỏ được tạo bằng ImageMagick; đã mở kiểm tra.

Điểm **tự chấm** 0–10, lấy mặt yếu nhất; chưa phải chấm mù hoặc nghiệm thu trong game. Bốn tiêu chí biểu tượng theo thứ tự: đọc ra chiêu / cuốn hút / tách khung–hình / sạch.

| Biểu tượng | Tiêu chí ở 32 px | Điểm 32 px | Tiêu chí ở 48 px | Điểm 48 px | Nhận xét |
| --- | --- | ---: | --- | ---: | --- |
| ink-gold · try1 | 8,5 / 8,5 / 8,5 / 8,5 | 8,5 | 9 / 8,5 / 9 / 8,5 | 8,5 | Vòng cổng và tia xuống rõ; phù văn chỉ đọc thành nét trang trí khi nhỏ. |
| jewel-crest · try1 | 8 / 8,5 / 8 / 8,5 | 8 | 8,5 / 9 / 8,5 / 8,5 | 8,5 | Giữ đúng khung ngọc; ở 32 px quầng sáng dày hơn, khoảng tối quanh cổng hẹp hơn ink-gold. |

| Ấn Hỏa | Đúng dáng | Đẹp, sang | Thẳng trên / nền / không chữ | Mặt nạ / lề | Cùng dáng Kim | Điểm chung |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hex · try1 | 9 | 8,5 | 8 | 8,5 | 9 | 8 |
| line · try1 | 8,5 | 8,5 | 8 | 8 | 9 | 8 |

Hex giữ sáu kiếm, hai lục giác, vòng ngoài và tâm trống. Line giữ hai biên, chuỗi phù văn, hoa văn đầu trái và mũi phải; lửa làm dải dày hơn mốc Kim một chút. Cả hai có lõi trắng vàng, mép cam đỏ và tàn lửa.

**Anh cần xem:** mức lửa và độ dày dải trên tấm Kim–Hỏa. Nền nhìn đen nhưng chưa đen tuyệt đối: góc hex có `(0,1,0)`, line có `(1,1,0)` trên thang 255. Giữ nguyên ảnh công cụ, chưa làm sạch nền. Hộp nét ở ngưỡng sáng 5%: hex `758×813+458+47`, line `1641×197+16+365`; không cắt nét chính, lề hai đầu line còn hẹp.

Không bỏ sót hạng mục ảnh của phiếu. Chưa làm đủ bộ Hỏa hoặc tích hợp runtime vì đang chờ anh duyệt hai mẫu. Không chạy build/test, mở cổng, dùng ảnh ngoài, sửa/xóa tệp cũ hay chạy lệnh Git ghi. Không gặp giới hạn công cụ.
