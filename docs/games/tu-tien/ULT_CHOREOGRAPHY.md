# Thiết kế trình diễn 14 tuyệt kỹ (bản gộp để owner duyệt, 17/11/2026)

Nguồn: Gemini (`source/gemini-ult-choreography-2026-11-17.md`, chỉ 1 vòng PASS, không link) và nghiên cứu Naraka + Diablo IV (`source/ref-skill-staging-naraka-d4-2026-11-17.md`; 8 chiêu xem khung thật, phần còn lại theo hiểu biết, cần kiểm lại thời lượng). Luật: không hệ nào "mọc từ đất + vòng tròn"; mỗi kiểu nguồn tối đa 2 hệ. Owner 17/11: "rõ ràng nhiều kỹ năng áp dụng dạng rơi từ trên trời rơi xuống không phải đẹp sao, ví dụ chiêu hệ kim, tạo ra 1 vòng trận pháp, sau đó triệu hồi mưa kiếm rơi xuống".

| Hệ | Nguồn | Trình diễn | Điểm nhấn | Tham khảo |
|---|---|---|---|---|
| Kim | Trời | Vòng trận pháp hiện trên trời, mưa kiếm rơi thẳng theo 2–3 đợt, cắm đất rồi tan thành bụi vàng | Đợt kiếm cuối, một thanh lớn giữa trận | D4 Meteor/Blizzard; Naraka Yoto |
| Tinh Tú | Trời | Vẽ chòm sao trên trời, sao băng rơi **chéo** từng viên bắn tỉa quái | Viên sao cuối nổ ánh kim cương | D4 Meteor |
| Hỏa | Người tung | Rồng lửa phóng ra từ tay, uốn lượn bám quái, để vệt cháy | Mắt rồng rực + hơi nóng | D4 Hydra/Inferno |
| Quang | Người tung | Nâng thấu kính, tia sáng quét thành hình quạt từ người ra | Tia hội tụ trắng ở cuối | Naraka Yoto/Justina |
| Thủy | Một bên đường | Bức tường sóng quét ngang cả làn rồi rút, để bọt | Đỉnh sóng vỡ trắng | D4 Hurricane/Cataclysm |
| Mộc | Hai lề đường | Dây leo vọt từ hai lề quất chéo hình X, trói quái | Hoa nở tại giao điểm X | Gemini; D4 Call of the Ancients |
| Băng | Không trung trên sân | Bão mảnh băng rơi phủ vùng, quái đóng băng rồi vỡ | Tiếng vỡ đồng loạt + lóe tinh thể | D4 Blizzard |
| Lôi | Tầng mây | Sét nhảy dây chuyền quái này sang quái khác, đòn chót sét lớn từ mây | Sét chót | D4 Chain Lightning |
| Phong | Ngang qua đường | Lưỡi gió trăng khuyết chém ngang, kéo quái theo | Lưỡi lớn cuối | Naraka Ziping/Tianhai |
| Thổ | Đường thẳng từ người tung | Vết nứt chạy thẳng tới quái, gai đá phun nối tiếp theo đường (không vòng) | Tảng đá lớn cuối đường | Naraka Valda/Tianhai |
| Ám | Cầu trôi | Cầu bóng tối trôi chậm tới đám quái, sụp thành điểm hút | Lúc sụp đen kịt hút quái | D4 Ball Lightning |
| Hư Không | Khe nứt giữa không trung | Không gian rách ngang trước mặt, lưỡi không gian chém xé | Bên trong khe thấy vũ trụ | Naraka Temulch; Gemini |
| Huyết | Từ chính quái | Máu bị rút khỏi quái thành dòng, hội tụ thành lưỡi máu bán nguyệt rồi phóng lại | Lưỡi máu bóng ướt | D4 Blood Surge; Naraka Viper Ning |
| Độc | Hai mép sân, sát đất | Mây độc bò thấp từ mép vào, đọng 3–4 s, sủi bọt | Bong bóng độc vỡ | D4 Flame Shield/Hurricane |

Sau khi owner duyệt: mỗi hệ vẽ 3–4 khung phân cảnh đúng camera 55° → owner duyệt → liệt kê thành phần (mesh/shader/ảnh tĩnh/video nhỏ) → dựng lab. Bắt đầu với Kim.

## Đánh giá khả thi (Claude, 17/11) — với công cụ hiện có: three.js (mesh, shader, instancing, decal), Tripo, Firefly (thành phần nhỏ), Blender (mô hình đơn giản)

| Hệ | Khó | Vì sao | Đề xuất |
|---|---|---|---|
| Kim — mưa kiếm từ trận pháp | Vừa | Trận pháp = ảnh tĩnh xoay; kiếm = 1 mô hình Tripo đã có, nhân bản rơi + vệt sáng; va chạm = flipbook có sẵn | **Làm** (đầu tiên) |
| Tinh Tú — sao băng chéo | Dễ–vừa | Thiên thạch = mesh + đuôi ribbon; nổ = flipbook | **Làm** |
| Lôi — sét dây chuyền | Dễ–vừa | Tia sét bằng shader/ribbon nối quái; sét chót dùng cột sét đã duyệt | **Làm** |
| Quang — tia quét quạt | Dễ | Mesh tia + shader, cột sáng | **Làm** |
| Phong — lưỡi gió trăng khuyết | Dễ | Mesh cong + shader trượt + vệt | **Làm** |
| Thổ — vết nứt + gai đá theo đường | Vừa | Decal nứt + gai đá Tripo/Blender nhân bản theo đường | **Làm** |
| Băng — bão mảnh băng | Vừa | Mảnh băng instancing rơi + đóng băng quái (đã có) | **Làm** |
| Ám — cầu bóng tối sụp hút | Vừa | Cầu shader + biến dạng hút; khó làm đẹp phần "hút" | Làm sau |
| Hư Không — rách không gian | Vừa–khó | Khe rách shader + vũ trụ bên trong (parallax) | Làm sau |
| Huyết — rút máu thành lưỡi | Khó | Dòng chất lỏng bay nhiều quái hội tụ cần ribbon chất lỏng đẹp | Làm sau, có thể đơn giản hoá |
| Mộc — dây leo quất chữ X | Khó | Dây leo cong động cần rig/spline mesh; dễ xấu | Đơn giản hoá hoặc hoãn |
| Độc — mây độc bò thấp | Khó | Khói thể tích đẹp đã thất bại nhiều lần | Hoãn; tạm dùng flipbook độc mức B |
| Hỏa — rồng lửa uốn lượn | Rất khó | Sinh vật năng lượng chuyển động theo đường, cần rig/shader phức tạp | **Không làm** bản rồng; thay bằng mưa cầu lửa hoặc cột lửa quét |
| Thủy — tường sóng thần | Rất khó | Chất lỏng lớn chuyển động thật không làm được ở web với công cụ hiện có | **Không làm**; thay bằng mưa giọt nước/vòng nước từ trời |
