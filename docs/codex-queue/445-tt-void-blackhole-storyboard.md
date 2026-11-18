# Phiếu 445: Tuyệt kỹ Hư Không "hố đen vũ trụ", phân cảnh 2D để owner duyệt

Phản biện: PASS (Sonnet, 17/11)

## Bối cảnh
Owner (17/11) gửi ảnh mẫu một hố đen vũ trụ và yêu cầu: "dựa vào ảnh mẫu để tạo ra ảnh 2D và phát triển nó thành 1 kỹ năng". Owner chọn hệ Hư Không. Ảnh mẫu là tranh truyện của bên ngoài, nên theo luật **không đưa ảnh đó vào công cụ**. Claude đã phân tích ảnh mẫu thành lời như sau:
- **Lõi:** một quả cầu đen đặc rất to, mép có viền sáng mỏng.
- **Vành sáng:** quanh lõi có vành lửa vàng trắng rực, chỗ dày chỗ mỏng, trông như một vòng bồi tụ.
- **Dải sáng ngang:** một dải năng lượng trắng vàng rất dày cắt chéo ngang qua giữa quả cầu, có vệt tốc độ.
- **Lưỡi sáng:** nhiều lưỡi sáng trắng hình trăng khuyết, mảnh và nhọn, xoáy cong quanh quả cầu và hút vào tâm.
- **Nền và hạt:** nền vũ trụ cam đỏ chuyển sang xanh có sao, vài đốm lửa nhỏ trôi lơ lửng.
- **Màu:** đen là khối chính, vàng trắng là ánh sáng, cam đỏ ở rìa.

## Việc
Dùng công cụ `image_gen`, tối đa 4 lần: 1 phân cảnh 4 ô, nếu lệch thì sửa thêm 1 lần, và 2 ảnh thành phần.

Ảnh tham chiếu chỉ lấy ảnh của dự án, ghi đường dẫn vào prompt:
- `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`: lấy camera chơi chếch 55°, sân đá tối, người tung chiêu áo trắng nhỏ ở đáy giữa nhìn từ sau lưng, đàn quái phía trước, và chất liệu tranh.
- `games/immortality-cultivation/art-src/concept/ult-void/ult-void-components.v1-try2.png`: lấy màu và chất liệu Hư Không đã có.

1. **Phân cảnh `void-blackhole-storyboard`** (1536×1024, lưới 2×2, đúng camera chơi, không chữ):
   - **Ô 1, tụ lực:** một điểm đen nhỏ hiện lên giữa đàn quái, ở độ cao khoảng ngang ngực quái. Không gian quanh điểm bị bẻ cong, hạt sáng bị hút vào.
   - **Ô 2, hố đen mở:** quả cầu đen lớn lơ lửng thấp trên đàn quái, có vành bồi tụ vàng trắng xoáy nghiêng theo phối cảnh. Quái ở rìa bị kéo nghiêng về tâm. Bóng tối và ánh vàng hắt xuống đất.
   - **Ô 3, cao trào:** một dải năng lượng trắng vàng dày chém ngang qua hố đen, các lưỡi sáng hình trăng khuyết xoáy vào tâm, quái bị nuốt. Đây là điểm nhấn duy nhất.
   - **Ô 4, dư âm:** hố đen co lại thành một điểm rồi lóe tắt, còn hạt vàng và đốm lửa trôi, quái ngã rạp hướng về tâm.
   - Luật: không vòng phép hay vòng tròn vẽ dưới đất. Vành bồi tụ là vật thể nằm nghiêng ở trên không.
2. **Hai ảnh thành phần** (1024×1024, nền đen, mỗi ảnh một thứ, lề ≥ 10 %, nhìn chếch 55°):
   - **`void-accretion-ring`:** vành bồi tụ vàng trắng dày quanh một tâm đen, nằm nghiêng theo phối cảnh.
   - **`void-crescent-blade`:** một lưỡi sáng trăng khuyết trắng vàng, cong, mảnh và nhọn.

Lưu ảnh ở `games/immortality-cultivation/art-src/concept/ult-void/blackhole/<tên>.v1-try<k>.png`, kèm `.prompt.txt` cùng tên. Ghép tờ `void-blackhole-445.jpg`. Nếu sandbox không cho ghi thư mục review thì để tờ ghép ở `/private/tmp/typing-game-445/`.

Phong cách: game tu tiên thương mại cao cấp, hùng vĩ, đẹp và cuốn hút. Không chữ, không watermark.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh. Không dùng ảnh của game hoặc truyện bên ngoài.

## Giao nộp
`docs/codex-queue/445-report.md`.
