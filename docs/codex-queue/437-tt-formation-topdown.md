# Phiếu 437: Ảnh trận pháp Kim nhìn thẳng từ trên xuống (texture cho mặt phẳng 3D)


Phản biện: PASS (Sonnet, 17/11)
## Bối cảnh
Owner 17/11: "những trận pháp được triệu hồi ở trên trời, nó cần được nhìn 3d để không bị lệch". Trận pháp trên trời sẽ là mặt phẳng 3D nằm ngang, nên texture phải nhìn **thẳng từ trên xuống (90°)**, hình tròn đều, không vẽ sẵn phối cảnh. Ảnh `formation-sky` của phiếu 435 đã vẽ nghiêng nên không dùng được làm texture.

## Việc
Dùng công cụ `image_gen`: tối đa 4 lần, 1024×1024, lưu `games/immortality-cultivation/art-src/concept/ult-metal/rain-components/formation-topdown.v1-try<k>.png`, prompt thật trong `.prompt.txt`.
Ảnh tham chiếu bắt buộc (ghi đường dẫn): `games/immortality-cultivation/art-src/concept/ult-metal/rain-components/formation-sky.v1-try1.png` (hoa văn, màu vàng, phù văn — chỉ lấy thiết kế, đổi sang nhìn thẳng từ trên).
Vẽ: vòng trận pháp vàng **tròn đều, nhìn thẳng từ trên xuống**, tâm ở giữa ảnh, nhiều lớp vòng đồng tâm, phù văn cổ, hoa văn mây; nền đen tuyệt đối; lề ≥ 6 %; không tia sáng, không phối cảnh, không bóng, không chữ, không watermark. Theo luật owner 12/11: trận pháp phải huyền bí kiểu tu tiên (vòng chữ cổ, bát quái), không hình học đơn giản.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
`docs/codex-queue/437-report.md`.
