# Phiếu 425: Ảnh tĩnh vương miện máu đẹp (làm khung đầu cho video Huyết)


Phản biện: PASS (Sonnet, 16/11; đã thêm bước 2 mẫu trước theo phản biện vòng 1)
## Bối cảnh
Owner 16/11 gửi khung đỉnh của Huyết bản v3 trong lab (`typing-game-review/owner-review/2026-11-16/tu-tien/burst-v2/owner-blood-crown-feedback.webp`): "ảnh này cần được làm đẹp hơn". Lỗi thấy được: các tia là đường thẳng mảnh đều nhau như kim, phẳng, không có chất lỏng; vòng đáy đều tăm tắp; vũng loang như mạng nứt chứ không như máu ướt. Luật owner 16/11 (nguyên văn): "các video phải được tạo đảm bảo chất lượng và phù hợp góc nhìn, đảm bảo để code có thể tích hợp thêm 1 số hiệu ứng khi gây ra ở mặt đất, nhìn chân thật không bị cảm giác ảo".

## Việc
`image_gen`: **làm 2 mẫu trước** (2 lần), ghép thành `blood-crown-samples-425.jpg` rồi dừng và ghi báo cáo để Claude gửi owner xem; chỉ khi phiếu được giao tiếp mới làm thêm. Tổng tối đa 6 lần, 1024×1024, lưu `games/immortality-cultivation/art-src/lab/vfx/blood/stills-55/blood-crown.v2-try<k>.png`, prompt thật trong `.prompt.txt`.
Ảnh tham chiếu bắt buộc mọi lần (ghi đường dẫn): ảnh lỗi của owner ở trên (để tránh), ảnh 55° đã đạt `games/immortality-cultivation/art-src/lab/vfx/water/stills-55/water-ring-burst.v1-try*.png` (vương miện nước được chấm A: dáng và phối cảnh), và khung đẹp nhất của `art-src/lab/vfx/blood/stills-55/blood-big-burst.v1-try*.png` (màu).
Vẽ: **một vương miện máu bắn tung** như giọt chất lỏng rơi xuống mặt phẳng, nhìn chéo xuống ~55°: vành chất lỏng dày, cong, gợn sóng không đều; các nhánh máu mọc lên dày mỏng khác nhau, cong theo quán tính, đầu nhánh tách thành giọt tròn bóng; chất máu đỏ thẫm, bóng ướt, có ánh phản chiếu và vùng trong mờ nhẹ ở mép mỏng; vài giọt văng xa bất đối xứng. Năng lượng tu tiên nhẹ: một quầng sáng đỏ mờ rất nhạt quanh đáy (mỗi kênh ≤ 0,9). Nền đen tuyệt đối, không mặt đất, không vũng, không chữ, lề ≥ 15 %, điểm chạm đất ở giữa-dưới. Chân thật, cao cấp, không hoạt hình, không tia thẳng như kim.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
Ảnh ghép `blood-crown-sheet-425.jpg` cạnh các ảnh và `docs/codex-queue/425-report.md` (gợi ý bản tốt).
