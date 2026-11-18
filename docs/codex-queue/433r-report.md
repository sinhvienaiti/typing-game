# Phiếu 433r: báo cáo (Claude làm thay Codex)

18/11/2026. Owner chọn "Xám than lạnh" cho bụi. Owner cũng hỏi vì sao kiếm lớn lại quay cạnh mỏng về phía camera.

## Đã sửa (`src/lab/metal-ult-rain.ts`)
- **Bụi xám than lạnh:** đổi tint của bụi nổ kiếm lớn (Explosion01) và bụi chạm đất của kiếm con thành **(0,38; 0,41; 0,47)**: xám tối, hơi ánh xanh. Trước đó bụi kiếm lớn tint (3,0; 1,85; 0,42), bụi kiếm con (0,52; 0,44; 0,34). Chỉ đổi tint, ảnh gốc giữ nguyên. Vàng giờ chỉ còn ở kiếm, hào quang C, sóng A và nứt dung nham.
- **Viền ấm (tùy chọn):** không làm. Lý do: viền ấm sẽ đưa vàng quay lại lớp bụi, đúng chỗ đang cần tách màu.
- **Sấm sáng hơn** nhưng vẫn ≤ 0,9 mỗi kênh: tint (0,72; 0,84; 0,9) → **(0,8; 0,88; 0,9)**. Độ đậm của tia quanh kiếm lớn 0,85 → 1,0; tia ở kiếm con 0,7 → 0,9.
- **Kiếm lớn quay mặt:** mỗi lần tung chiêu, kiếm lớn xoay quanh trục dọc của nó để mặt rộng có hoa văn hướng về người chơi, tức hướng camera chơi. Góc xoay tính từ vị trí người chơi so với điểm cắm. Độ nghiêng khi cắm và độ ngập dưới đất giữ nguyên. Hào quang C vốn đã tự canh theo camera nên vẫn nằm sau lưỡi. Sóng A và nứt B xoay theo cùng góc này.
- **Kiếm con:** là các thẻ phẳng luôn quay mặt về camera, nên không bao giờ lộ cạnh mỏng. Không cần sửa.

## Số đo
- **Bề ngang lưỡi kiếm ở giữa thân, camera chơi:** 25 px khi quay cạnh, **67,7 px** khi quay mặt, gấp **2,7 lần** (yêu cầu ≥ 2,5). Đo ở các đoạn 25 %, 35 % và 45 % chiều dài: 59 / 68 / 65 px so với 25 / 25 / 27 px.
- **Tương phản sấm so với bụi**, đo ở Alt+1 tại 6 thời điểm từ 7,95 đến 8,7 s:
  - Cách đo: chụp mỗi khung hai lần, có và không có lớp sấm. Điểm ảnh sấm là những điểm sáng lên ít nhất 0,1. Vùng bụi là các điểm xám (ít màu) trong vòng 12 px quanh tia.
  - Tỉ lệ sáng giữa sấm và bụi: 3,13 / 2,42 / 2,36 / 1,86 / 2,57 / 2,96. **Trung vị 2,5**, thấp nhất 1,86 ở khung có ít tia nhất. Sấm trung bình 0,43–0,55, bụi quanh tia 0,18–0,23.
  - Nếu tính cả hào quang vàng và mặt kiếm nằm quanh tia thì tỉ lệ chỉ 1,3–1,8.
  - Sấm không thể sáng hơn nữa vì bị giới hạn 0,9 mỗi kênh, và tia mảnh nên giá trị trung bình bị kéo xuống.
- **Độ sáng tâm bụi:** khoảng 0,18–0,23 khi đo trên nền đất tối #353a40, hơi thấp hơn mức 0,25–0,35 owner đưa ra. Không nâng thêm, vì nâng bụi sáng lên thì tỉ lệ tương phản với sấm sẽ tụt dưới 2,5.
- p95 **7,0 ms**. Vùng trắng **0,0001 %**. Kiểm kiểu 0 lỗi.

## Tệp
- Gửi owner: `typing-game-review/owner-review/2026-11-18/tu-tien/metal-rain-r.jpg` và `.mp4` (đủ chiêu). Đã thêm dòng vào `ABOUT.md`.
- Driver: `games/.wt-ic-lab-all/src/lab/metal-ult-rain-r-review.mjs`.
- Đã xoá khung thô. Chrome headless đã đóng và đã xoá profile. Server 3148 vẫn chạy. Không commit.
