# Phiếu 348 · Tu Tiên · Trận pháp lôi huyền bí theo D64

Đã tạo hai phương án, một lớp vành rời, prompt nguyên văn và tấm ghép có nhãn. Chạy sau phiếu 347: đã đọc `347-report.md` trước khi tạo ảnh. Dùng **6/6 lần gọi image_gen tích hợp**, **6/8 lần view_image**; không gọi công cụ ảnh khác.

**Bộ chọn:** A try2, B try2, vành try1. A được tự chấm cao hơn nên vành dùng màu đồng cổ/hổ phách của A. Đây là ảnh nguồn để anh chọn và làm khung đầu video; chưa có nghiệm thu hiệu ứng chuyển động trong game.

## Tệp bàn giao

`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.

| Tệp trong S | Vai trò | Kết quả |
| --- | --- | --- |
| `thunder-array-a.v1-try1.png` | A đầu: đồng cổ/hổ phách, bát quái | Giữ đối chiếu; lề nhỏ nhất 8,61%, không chọn |
| `thunder-array-a.v1-try2.png` | **A chọn** | Vẽ lại để tăng lề; giữ tám ô quẻ, cổ văn, lôi văn, sen/mây và năm nút điện |
| `thunder-array-b.v1-try1.png` | B đầu: tử lôi, sao chòm và long văn | Giữ đối chiếu; lề nhỏ nhất 7,89%, không chọn |
| `thunder-array-b.v1-try2.png` | **B chọn** | Vẽ lại để tăng lề; giữ hai rồng, sao chòm, cổ văn và năm nút điện |
| `thunder-array-ring.v1-try1.png` | **Vành chọn, theo A** | Chỉ dải cổ văn ngoài cùng; có alpha; tâm đen sạch khi ghép nền đen |
| `thunder-array-ring.v1-try2.png` | Thử làm sạch alpha | Không chọn: nhiễu alpha và chấm màu biên nhiều hơn try1 |
| `thunder-array-348-sheet.jpg` | Tấm ghép A try2 / B try2 / vành try1 | 1944×681 px, có nhãn |
| `thunder-array-348-sheet.prompt.txt` | Cách ghép | ImageMagick 7, Arial, nền đen; không tạo thêm tranh |

Cả sáu PNG đều 1254×1254 px. Mỗi PNG có tệp `.prompt.txt` cùng tên, ghi đúng prompt đã gửi và các đường dẫn tham chiếu. Các ảnh sinh được sao chép nguyên vẹn từ thư mục mặc định của image_gen vào S; không tô, sửa màu, đổi alpha hay thu phóng ảnh gốc bằng mã. Chỉ tấm ghép được resize và ghép trên đen.

## Tham chiếu và nội dung

Đã xem đủ ba ảnh chỉ định, chỉ dùng ảnh của repo:

- `thunder-formation-top.v1-try2-black.png`: chỉ góc thẳng từ trên; không dùng lại màu trắng xanh và bố cục bị chê.
- `foe-boss-summon-sigil-top.v1-try1.png`: mật độ dải ký hiệu và cách lồng vòng; không lấy đỏ và đầu thú.
- `light-ground-mark-top.v1-try3.png`: độ hoàn thiện, nét khắc sáng; không lấy nền đá và vàng sáng.

Try2 của A/B nhận thêm try1 tương ứng để giữ thiết kế. Vành nhận A try2 làm ảnh đích; vành try2 nhận thêm vành try1.

| Hạng mục | A chọn | B chọn |
| --- | --- | --- |
| Vành cổ văn ngoài cùng | Dải ký hiệu vuông gãy, màu đồng dịu | Dải ký hiệu tím bạc |
| Lôi văn | Vành hồi văn sét vuông cuộn | Vành hồi văn bên trong bản đồ sao |
| Sen/mây | Sen nhiều lớp và mây cuộn quanh ô quẻ | Sen phía trong, mây giữa thân hai rồng |
| Bố cục riêng | Tám ô quẻ cách điệu | Hai rồng uốn đuổi nhau; dải sao chòm |
| Vòng trong | Đúng năm nút điện, nối bằng cung tròn | Đúng năm nút điện, nối bằng cung tròn |
| Tâm | Lõi hổ phách và ấn điện nhỏ | Lõi bạc và ấn điện nhỏ |
| Khác màu tia sét trắng xanh | Đồng nâu/hổ phách dịu | Tím thẫm và bạc; không cyan |

Ký hiệu được yêu cầu là cổ văn hư cấu, không có câu chữ đọc được hay nhãn. Một số nét đơn vẫn gợi bộ thủ; không thể chứng minh bằng đo pixel rằng từng hình đều không trùng một chữ thật. Dải sao B có một số đoạn cung ngắn nhìn gần thẳng; không có đường nối năm nút xuyên tâm thành ngôi sao.

## Kiểm kỹ thuật

Đọc pixel bằng ImageMagick 7 và Python chuẩn, không chạy build/test của game. Hộp bao tính với `max(R,G,B) > 8/255`, sau khi ghép alpha trên đen; đây là ngưỡng loại nhiễu nền cực tối, không phải khẳng định nền A/B đen tuyệt đối từng pixel.

Độ tròn đo **vành sáng ngoài liên tục**, không tính hạt rời và đầu lóe: lấy tâm hộp bao, quét 360 tia cách nhau 1°, bước bán kính 0,5 px trong dải 94–101,5% bán kính ước lượng; chọn điểm ngoài cùng sáng >100/255, lọc trung vị 7° để loại hạt/lóe riêng lẻ. Sai lệch là `max(|r − median(r)|) / median(r)`. Đây là phép đo raster theo phương pháp nêu rõ, không phải chứng nhận hình học từ mô hình gốc.

| Ảnh chọn | Hộp bao sáng, px [trái, trên, phải, dưới) | Lề nhỏ nhất | Bán kính trung vị | Sai lệch bán kính |
| --- | --- | ---: | ---: | ---: |
| A try2 | [221, 195, 1031, 990) | **15,55%** | 384,5 px | **1,69%** |
| B try2 | [206, 182, 1045, 1009) | **14,51%** | 403,5 px | **0,99%** |
| Vành try1 | [160, 140, 1088, 1065) | **11,16%** | 452,0 px | **0,66%** |

- **Vàng kim sáng ở A try2:** 0 / 298.019 pixel vùng sáng = **0,00%**, đạt ≤5%. Vùng sáng là V >32/255; vàng kim đúng điều kiện H 45–60°, S >0,8, V >0,85 trong HSV. A try1 cũng đo được 0%.
- **Nền A/B:** đen về thị giác. Trong toàn dải viền ngoài 10%, giá trị kênh lớn nhất là **2/255**; pixel khác đen tuyệt đối chiếm 14,46% dải viền A và 33,87% dải viền B. Chưa phải nền RGB(0,0,0) tuyệt đối từng pixel; giữ nguyên ảnh sinh để không tự sửa tranh.
- **Độ thoáng tâm:** vùng tròn khảo sát bán kính 170 px ở tâm A có 68,27% pixel tối ≤8/255; vùng bán kính 157 px ở tâm B có 75,65%. Lõi sáng nhỏ nằm trong vùng này. Không có đa giác sao nối thẳng qua tâm.
- **Vành chọn:** sau khi ghép trên đen, toàn bộ đĩa tâm đường kính **55% khung** đúng RGB(0,0,0). Đĩa đen thuần lớn nhất quanh tâm khung có đường kính **57,42% khung**; quanh tâm vành đo được **60,17% khung**, tương đương khoảng 83,5% đường kính vành. Viền ngoài 10% cũng đen thuần.
- **Giới hạn alpha cần lưu ý:** trong đĩa tâm 55% khung của vành try1 còn **9.144 pixel alpha=1/255**, RGB vẫn ghép thành đen thuần; không có pixel alpha >1/255 trong vùng này. Vì vậy **đạt tâm đen thuần, chưa đạt alpha=0 tuyệt đối**. Vành try2 đã thử sửa một lần nhưng tệ hơn: 117.873 pixel alpha >0, trong đó 180 pixel alpha=2/255, và hai pixel ghép thành giá trị 1/255 ở tâm; không chọn.
- Vành là ảnh sinh riêng, chưa khớp pixel với A. Bán kính đo lớn hơn A; tỷ lệ bán kính tham khảo để căn về A là 384,5/452 ≈ **0,851**. Tâm đo A khoảng (625,5; 592), vành (623,5; 602). Chưa thực hiện căn lớp hoặc tích hợp.

## Tự chấm theo mặt yếu nhất

Điểm là tự chấm ảnh nguồn theo phiếu, không thay cho đánh giá hiệu ứng đã ghép trong play host.

| Tiêu chí | A try2 | B try2 | Vành try1 |
| --- | ---: | ---: | ---: |
| Huyền bí, chất tu tiên | 8,6 | 8,5 | 8,3 |
| Đọc ngay là trận lôi / vai trò lớp | 8,5 | 8,4 | 8,2 — lớp cổ văn, không phải trận lôi độc lập |
| Tâm thoáng | 8,5 | 8,6 | 8,8 — xét hình nhìn thấy |
| Khác trắng xanh nhưng hợp bộ | 8,8 | 8,5 | 8,8 |
| Sang, cuốn hút | 8,4 | 8,2 | 8,2 |
| Dùng làm khung đầu video / lớp quay | 8,3 | 8,0 | 8,1 — cần lưu ý alpha và căn lớp |
| **Điểm yếu nhất về hình ảnh** | **8,3** | **8,0** | **8,1** |

A/B try1 tự chấm tổng thể **7,6 / 7,5** do thiếu lề, đã vẽ lại mỗi ảnh một lần. Vành try1 bị đánh dấu lỗi kỹ thuật alpha; đã vẽ lại một lần thành try2 nhưng không cải thiện, giữ try1 làm bản tốt hơn. **Không đánh dấu alpha sạch tuyệt đối là PASS.** Đã dùng hết ba lượt vẽ lại trong ngân sách sáu lần gọi.

## Anh cần xem và phần không làm

Xem `S/thunder-array-348-sheet.jpg` để chọn A hay B; tôi nghiêng A vì chất nghi lễ và tương phản màu đồng cổ. Xem riêng vành try1 nếu bước tiếp theo đòi alpha sạch tuyệt đối; phần dư alpha=1/255 đã ghi ở trên. A/B cũng còn nhiễu nền tối tối đa 2/255.

Không sửa mã, runtime, tài liệu Tu Tiên, ảnh có sẵn; không mở cổng, chạy build/test, thao tác ghi Git hay dùng ảnh ngoài repo. Không tạo video, không kiểm chuyển động và không chấm trong game vì phiếu chỉ giao ảnh 2D. Không ghi sang thư mục review chung vì phạm vi ghi của phiếu chỉ cho S và báo cáo này. Không gặp HTTP 429 hoặc thông báo chờ của công cụ.

