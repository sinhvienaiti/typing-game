# Phiếu 300 · Ảnh 2D kỹ năng mở rộng

Đã tạo đủ **14/14 ảnh**, dùng đúng **14 lần gọi Codex `image_gen`**, mỗi thiết kế một lần, không gọi sửa hay tạo lại; không gặp hạn mức.

Đường dẫn chung: `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/`. Mỗi tên `.png` trong bảng có một file cùng tên gốc `.prompt.txt` bên cạnh, tổng cộng **28 file mới**. Ảnh chép bằng `cp -n`, giữ nguyên dữ liệu và khổ gốc **1672 × 941 px** (ngang, xấp xỉ 16:9; không crop/resize).

Đã mở đủ ảnh tham chiếu của từng mẫu bằng `view_image`, chỉ gửi các ảnh repo được phiếu chỉ định. Giữ nguyên văn đoạn “2D Still Prompt” Gemini, thêm câu mở đầu bắt buộc và dòng `Landscape 16:9.` để truyền khổ cho công cụ; B5 có câu màu Ám bắt buộc ở cuối. Từng file prompt ghi công cụ, đường dẫn tham chiếu, prompt gửi nguyên văn và khổ thật.

| Mã | File trong thư mục chung | Khổ thật (px) | Nhận xét kiểm tra trực quan |
| --- | --- | --- | --- |
| A1 | `myriad-lotus-domain.v1-try1.png` | 1672 × 941 | Đúng liên hoa cyan–vàng nhiều lớp và nhụy binh khí; không thấy chữ hay mặt người, nền đen có hào quang, góc nhìn hơi gần từ trên thẳng xuống. |
| A2 | `firmament-sundering-cleave.v1-try1.png` | 1672 × 941 | Đúng khe chém chéo tím–bạc, tâm tối và mảnh binh khí dựng lên; không thấy chữ hay mặt người, nền đen. |
| A3 | `nine-heavens-tribulation-net.v1-try1.png` | 1672 × 941 | Đúng lưới lôi điện cyan–tím nhưng có 19 cột và ô tam giác thay vì bảy cột/lưới lục giác theo gameplay; vòng phù có nét giống ký tự trang trí, không thấy chữ đọc được hay mặt người, nền đen. |
| A4 | `karmic-ember-tempest.v1-try1.png` | 1672 × 941 | Đúng xoáy lửa đỏ–vàng, liên hoa và vệt đao quanh tâm thoáng; không thấy chữ hay mặt người, nền đen. |
| A5 | `glacial-moon-tide.v1-try1.png` | 1672 × 941 | Đúng sóng băng lưỡi liềm ôm nguyệt kính, có tinh thể và quầng sáng; không thấy chữ hay mặt người, nền đen. |
| A6 | `samsara-blood-mandala.v1-try1.png` | 1672 × 941 | Đúng la bàn bát giác đỏ–vàng và kim giáo, có bát quái/âm dương theo thiết kế; không thấy chữ đọc được hay mặt người, nền đen. |
| A7 | `astral-meteor-constellation.v1-try1.png` | 1672 × 941 | Đủ bảy binh khí nối chòm sao, nhưng có rìu, cung và trượng ngoài kiếm/giáo; không thấy chữ hay mặt người, nền đen, tinh vân nằm trong hiệu ứng. |
| A8 | `miasma-briar-abyss.v1-try1.png` | 1672 × 941 | Đúng vòng gai năng lượng xanh–tím cuốn vào tâm rỗng và bào tử sáng; không thấy chữ hay mặt người, nền đen. |
| B1 | `asura-six-arms-avatar.v1-try1.png` | 1672 × 941 | Đủ ba đầu/sáu tay và ngực rỗng đỏ–vàng, nhưng chỉ hai vũ khí đang chạm tâm sóng; có nét mặt cách điệu, không phải người thật, không thấy chữ, nền đen, góc nhìn còn gần chính diện. |
| B2 | `myriad-palm-bodhi-avatar.v1-try1.png` | 1672 × 941 | Đúng quạt tay và chưởng ấn vàng–ngọc, nhưng thân/mặt khá đặc và không đủ 16 dấu tay theo gameplay; mặt cách điệu, không phải người thật, không thấy chữ, nền đen. |
| B3 | `heaven-earth-titan-avatar.v1-try1.png` | 1672 × 941 | Đúng cự thần xanh–hổ phách có mạch sét và cung chém lớn; mặt cách điệu, không phải người thật, không thấy chữ, nền đen, góc nhìn còn thấp hơn yêu cầu 55°. |
| B4 | `polar-star-emperor-avatar.v1-try1.png` | 1672 × 941 | Đúng tinh quân chỉ xuống tinh kiếm và vòng sóng sao, thân có chòm sao xuyên sáng; mặt trơn với mắt sáng cách điệu, không phải người thật, không thấy chữ, nền đen, góc nhìn còn thấp. |
| B5 | `nether-samsara-monarch-avatar.v1-try1.png` | 1672 × 941 | Đúng quân vương bóng đen và hai cung chém chữ X, không thấy tím/violet/cyan, nhưng lõi sáng trắng–đỏ vượt sắc ember đỏ thẫm; mặt nạ năng lượng, không có mặt người thật hay chữ, nền đen. |
| B6 | `immortal-sword-progenitor-avatar.v1-try1.png` | 1672 × 941 | Đúng kiếm quyết hai ngón, vòng kiếm sau lưng và mưa kiếm tỏa ra trận tròn; mặt cách điệu, không phải người thật, không thấy chữ, nền đen, góc nhìn gần chính diện và mật độ kiếm cao. |

Đã kiểm tra đủ 14 cặp file, nội dung prompt khớp nguồn và ảnh đích trùng byte với ảnh công cụ trả về. Nhận xét trên là kiểm tra still, chưa phải nghiệm thu trong game hay chấm mù 8,5.

Không bỏ qua thiết kế nào. Không sửa/xóa file có sẵn, không chạy lệnh git ghi, build hay test game; không tạo video hoặc tích hợp runtime vì ngoài phạm vi phiếu.

Anh cần xem kỹ A3 (số cột/kiểu lưới), A7 (loại binh khí), B1–B6 (góc nhìn và độ trong thân), B1/B2 (số đòn/dấu tay), B5 (lõi chém quá sáng so với quy tắc đỏ thẫm). Các ảnh được giữ nguyên đúng yêu cầu một lần gọi mỗi thiết kế.
