# Phiếu 307 · Sao băng chéo · 12 hệ còn lại

Ngày: 06/11/2026. Đã gọi **đúng 12 lần `image_gen`**, thành công 12/12; không gọi thêm, không tạo lại hay hậu kỳ.

Đã thêm 12 ảnh `.png` bằng `cp -n` và 12 file `.prompt.txt` tại:
`games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.
Tên mỗi bộ là `<hệ>-comet.v1-try1`; prompt bên cạnh ghi công cụ, đường dẫn tham chiếu, prompt nguyên văn và khổ thật.

Mỗi lần đều mở đúng ảnh `<hệ>-crescent-sym.v1-try1.png` bằng `view_image`, gửi kèm ảnh đó, giữ nguyên prompt phiếu và chỉ thay chất liệu; nền đen, `transparent_background=false`.

| Hệ / tiền tố tên file | Khổ thật (px) | Quan sát ảnh đầu ra |
| --- | --- | --- |
| metal | 1672 × 941 | Đầu bạc–ngọc sáng rõ, đuôi thon dần thành mảnh sáng; không thấy dáng lưỡi liềm hay chữ. |
| thunder | 1671 × 941 | Đầu sét trắng–tím tròn rõ, đuôi thon dần thành tia phân nhánh; không thấy dáng lưỡi liềm hay chữ. |
| wind | 1671 × 941 | Đầu khí xoáy sáng rõ, đuôi thon dần kèm lá và hạt sáng; không thấy dáng lưỡi liềm hay chữ. |
| ice | 1671 × 941 | Đầu băng phân diện rõ, đuôi thon dần thành vụn băng; không thấy dáng lưỡi liềm hay chữ. |
| earth | 1671 × 941 | Đầu đá nứt hổ phách rõ, đuôi thon dần thành bụi và mảnh đá; không thấy dáng lưỡi liềm hay chữ. |
| wood | 1671 × 941 | Đầu linh mộc sáng rõ, đuôi thon dần kèm lá và hoa từ ảnh tham chiếu; không thấy dáng lưỡi liềm hay chữ. |
| dark | 1671 × 941 | Đầu khói đen viền đỏ rõ, đuôi thon dần thành tàn lửa; không thấy dáng lưỡi liềm hay chữ, không thấy tím. |
| light | 1678 × 937 | Đầu trắng–vàng rõ, đuôi thon dần kèm lông vũ và tia sáng; không thấy dáng lưỡi liềm hay chữ. |
| poison | 1671 × 941 | Đầu độc xanh–tím rõ, đuôi thon dần kèm giọt và bào tử; không thấy dáng lưỡi liềm hay chữ. |
| blood | 1671 × 941 | Đầu huyết năng đỏ rõ, đuôi thon dần kèm giọt và tinh thể đỏ; không thấy dáng lưỡi liềm hay chữ. |
| void | 1671 × 941 | Đầu xoáy hư không rõ, đuôi thon dần kèm vết nứt và mảnh không gian; không thấy dáng lưỡi liềm hay chữ. |
| star | 1671 × 941 | Đầu xoáy sao sáng rõ, đuôi thon dần thành bụi sao và đường chòm sao; không thấy dáng lưỡi liềm hay chữ. |

Đã kiểm tra đủ 24 file, khổ ngang, prompt khớp nguyên văn và SHA-256 của từng PNG trùng bản công cụ trả về.

**Anh cần xem:** trục rơi của cả bộ nhìn nghiêng ngang hơn yêu cầu khoảng 20° so với phương đứng; Wood có hoa đi theo chất liệu tham chiếu. Giữ nguyên mọi ảnh theo lệnh không tự sửa lại. Đây là kiểm tra ảnh tĩnh, chưa phải nghiệm thu trong game.

Không bỏ sót hệ nào. Không chạy build/test, không tích hợp runtime hay mở vòng chấm độc lập vì ngoài phạm vi phiếu; không sửa/xóa file có sẵn và không chạy lệnh Git ghi.
