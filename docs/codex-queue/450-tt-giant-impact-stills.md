# Phiếu 450: Ảnh tĩnh cú chạm đất của kiếm lớn: sóng năng lượng vàng và đất nứt núi lửa

Phản biện: PASS (Sonnet, 18/11, vòng 2)

## Bối cảnh
Ngày 18/11 owner nói về cú chạm đất của kiếm lớn: "nên thêm hiệu ứng chồng lên, toả ra dạng năng lượng vàng kiểu do kiếm va chạm với mặt đất… chồng lên hiệu ứng nổ lẫn với bụi, đất phải nứt dạng núi lửa".

Cú chạm đất sẽ ghép từ các thành phần riêng. Phiếu này chỉ vẽ ảnh tĩnh để owner chọn. Bụi nổ đã có sẵn: flipbook CC0 Explosion01, nhuộm vàng. Sau khi owner chọn, các ảnh tĩnh sẽ được làm thành video bằng Firefly hoặc gắn thẳng vào lab.

## Việc
Dùng công cụ `image_gen`, đúng 4 lần: 2 biến thể cho mỗi thành phần, mỗi biến thể 1 lần.

Ảnh tham chiếu (chỉ ảnh của dự án, ghi đường dẫn vào prompt):
- `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`, nửa trái, ô dưới trái: cú kiếm lớn cắm giữa trận, có vết nứt và tia vàng.
- `games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/giant-sword-aura.v1-try3.png`: màu vàng của hào quang C owner đã chọn.

Mỗi ảnh 1024×1024, nền đen tuyền, chỉ một thành phần, lề ≥ 8 %, **nhìn thẳng từ trên xuống 90°** (texture phẳng, không vẽ sẵn phối cảnh; code sẽ đặt lên một mặt phẳng nằm trên đất — luật camera của owner 17/11). Không vẽ kiếm, quái, nhân vật hay chữ.

1. **`metal-impact-wave` A/B:** sóng năng lượng vàng toả ra sát mặt đất từ một tâm.
   - Gồm các luồng năng lượng vàng sáng, xé tơi, lan ra ngoài trên mặt đất (nhìn thẳng từ trên xuống).
   - Tâm sáng trắng ấm (≤ 30 % trắng). Có tia sáng mảnh và hạt lấp lánh.
   - Không vẽ thành vòng tròn đều hay mandala: luồng năng lượng phải không đều, có hướng toả.
   - A: toả đều mọi hướng. B: toả mạnh hơn về phía trước và hai bên.
2. **`metal-impact-crack` A/B:** đất nứt kiểu núi lửa, nhìn thẳng từ trên xuống 90°.
   - Các vết nứt sâu toả từ tâm, trong lòng vết nứt phát sáng vàng cam như dung nham nóng.
   - Mép vết nứt tối, có mảnh đá vỡ nhô lên nhẹ.
   - Nền giữa các vết nứt là đen tuyền, để code cộng sáng và đặt lên mặt đất.
   - A: 6–8 vết nứt dài. B: vết nứt dày, nhiều nhánh hơn.

Lưu ảnh ở `games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/<tên>.v1-try<k>.png`, kèm `.prompt.txt`. Ghép tờ `giant-impact-450.jpg` có nhãn. Nếu sandbox không cho ghi vào thư mục review, để tờ ghép ở `/private/tmp/typing-game-450/`.

## Ràng buộc
Không sửa code, không làm video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh. Không dùng ảnh của game khác.

## Giao nộp
`docs/codex-queue/450-report.md`.
