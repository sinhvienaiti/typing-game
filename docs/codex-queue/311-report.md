# Phiếu 311 · Vòng ấn và hiệu ứng bám · 06/11/2026

Đã gọi đúng **28 lần image_gen**, mỗi đầu ra một lần; thành công 28/28, không gọi sửa hay tạo thêm. Đã thêm đủ **28 PNG + 28 prompt.txt** bằng tên phiếu, ảnh chép bằng cp -n và giữ nguyên byte gốc.

Thư mục D: `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Mỗi tên trong bảng có hai tệp `.png` và `.prompt.txt`; prompt ghi công cụ, đường dẫn ảnh tham chiếu của hệ, nguyên văn prompt và kích thước thật.

Đã mở ảnh tham chiếu bằng view_image trước từng lần gọi; chỉ gửi ảnh của repo. Hai mẫu Kim đã hiển thị cho chủ trước phần còn lại. Kiểm tra 28 prompt khớp nguyên văn câu loại + chất liệu + đuôi chung; SHA-256 của 28 bản chép khớp ảnh công cụ trả về.

**Cần chủ xem:** bốn vòng bám Kim, Hỏa, Thủy, Băng sai hướng (ngang); vòng bám Hư Không đúng dáng nhưng ảnh dọc 1199 × 1312. Nhiều vòng ấn có phù văn giống chữ; Lôi, Ám, Quang, Độc rõ nét giống chữ Hán. Đủ tệp không đồng nghĩa tất cả đạt tiêu chí hình ảnh.

**Nền:** cả 28 ảnh nhìn đen, nhưng chưa thuần #000000 tuyệt đối: đo bốn góc có kênh 0–2/255. Trong bảng, “đen*” chỉ kết quả này. Không bật nền trong suốt, không thấy watermark.

**Sai nhãn siêu dữ liệu:** prompt.txt của void-hit-affliction ghi đúng số 1199 × 1312 nhưng còn nhãn “ngang” mặc định; phải đọc là **dọc**. Giữ tệp nguyên trạng theo lệnh chỉ thêm mới, không sửa tệp đã có.

| Tên trong D | Khổ thật (px) | Kiểm tra từng ảnh |
| --- | --- | --- |
| metal-caster-seal.v1-try1 | 1671 × 941 | Vòng ấn tròn chiếu xiên, tâm trống; nền đen*; có phù văn giống chữ, cần chủ xem. |
| metal-hit-affliction.v1-try1 | 1671 × 941 | Sai hướng: vòng bầu dục ngang, tâm trống; nền đen*; không thấy chữ. |
| fire-caster-seal.v1-try1 | 1671 × 941 | Vòng ấn tròn chiếu xiên, tâm trống; nền đen*; có phù văn giống chữ, cần chủ xem. |
| fire-hit-affliction.v1-try1 | 1672 × 941 | Sai hướng: vòng bầu dục ngang, tâm trống; nền đen*; không thấy chữ. |
| water-caster-seal.v1-try1 | 1678 × 937 | Vòng ấn tròn chiếu xiên, tâm trống; nền đen*; có phù văn giống chữ, cần chủ xem. |
| water-hit-affliction.v1-try1 | 1677 × 938 | Sai hướng: vòng bầu dục ngang, tâm trống; nền đen*; không thấy chữ. |
| thunder-caster-seal.v1-try1 | 1671 × 941 | Vòng ấn tròn chiếu xiên, tâm trống; nền đen*; có ký tự giống chữ Hán trong phù văn. |
| thunder-hit-affliction.v1-try1 | 1671 × 941 | Vòng bám bầu dục đứng, tâm trống; nền đen*; không thấy chữ. |
| wind-caster-seal.v1-try1 | 1671 × 941 | Vòng ấn tròn chiếu xiên, tâm trống; nền đen*; có phù văn giống chữ, cần chủ xem. |
| wind-hit-affliction.v1-try1 | 1671 × 941 | Vòng bám bầu dục đứng, tâm trống; nền đen*; không thấy chữ. |
| ice-caster-seal.v1-try1 | 1671 × 941 | Vòng ấn tròn chiếu xiên, tâm trống; nền đen*; có phù văn giống chữ, cần chủ xem. |
| ice-hit-affliction.v1-try1 | 1671 × 941 | Sai hướng: vòng bầu dục ngang, tâm trống; nền đen*; không thấy chữ. |
| earth-caster-seal.v1-try1 | 1671 × 941 | Vòng ấn tròn chiếu xiên, tâm trống; nền đen*; có phù văn giống chữ, cần chủ xem. |
| earth-hit-affliction.v1-try1 | 1671 × 941 | Vòng bám bầu dục đứng, tâm trống; nền đen*; không thấy chữ. |
| wood-caster-seal.v1-try1 | 1671 × 941 | Vòng ấn tròn chiếu xiên, tâm trống; nền đen*; không thấy chữ, có quẻ và hoa văn. |
| wood-hit-affliction.v1-try1 | 1671 × 941 | Vòng bám bầu dục đứng, tâm trống; nền đen*; không thấy chữ. |
| dark-caster-seal.v1-try1 | 1671 × 941 | Vòng ấn tròn chiếu xiên, tâm trống; nền đen*; có ký tự giống chữ Hán trong phù văn. |
| dark-hit-affliction.v1-try1 | 1671 × 941 | Vòng bám bầu dục đứng, tâm trống; nền đen*; không thấy chữ. |
| light-caster-seal.v1-try1 | 1678 × 937 | Vòng ấn tròn chiếu xiên, tâm trống; nền đen*; có ký tự giống chữ Hán trong phù văn. |
| light-hit-affliction.v1-try1 | 1678 × 937 | Vòng bám bầu dục đứng, tâm trống; nền đen*; không thấy chữ. |
| poison-caster-seal.v1-try1 | 1671 × 941 | Vòng ấn tròn chiếu xiên, tâm trống; nền đen*; có ký tự giống chữ Hán trong phù văn. |
| poison-hit-affliction.v1-try1 | 1671 × 941 | Vòng bám bầu dục đứng, tâm trống; nền đen*; không thấy chữ. |
| blood-caster-seal.v1-try1 | 1672 × 941 | Vòng ấn tròn chiếu xiên, tâm trống; nền đen*; có phù văn giống chữ, cần chủ xem. |
| blood-hit-affliction.v1-try1 | 1672 × 941 | Vòng bám bầu dục đứng, tâm trống; nền đen*; không thấy chữ. |
| void-caster-seal.v1-try1 | 1672 × 941 | Vòng ấn tròn chiếu xiên, tâm trống; nền đen*; có phù văn giống chữ, cần chủ xem. |
| void-hit-affliction.v1-try1 | 1199 × 1312 | Vòng bám bầu dục đứng, tâm trống; khung ảnh dọc, sai khổ yêu cầu; nền đen*; không thấy chữ. |
| star-caster-seal.v1-try1 | 1671 × 941 | Vòng ấn tròn chiếu xiên, tâm trống; nền đen*; có phù văn giống chữ, cần chủ xem. |
| star-hit-affliction.v1-try1 | 1671 × 941 | Vòng bám bầu dục đứng, tâm trống; nền đen*; không thấy chữ. |

Không bỏ sót đầu ra nào; không chỉnh ảnh, đổi prompt hay gọi lại vì phiếu cấm. Không tích hợp vào game, không chạy build/test, không thao tác Git ghi. Chỉ thêm 56 tệp trong D và báo cáo này; chưa chấm chất lượng hay nghiệm thu trong play host.
