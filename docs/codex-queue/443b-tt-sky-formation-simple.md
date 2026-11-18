# Phiếu 443b: Trận pháp trên trời một lớp, đơn giản và đẹp, xem trong camera chơi (full-access)

Phản biện: PASS (Sonnet, 17/11, vòng 2)

## Bối cảnh
Ngày 17/11 owner bỏ cả 3 hướng trận pháp chồng tầng của phiếu 443. Lời owner: "bạn thiết kế làm sao bạn làm đẹp chứ đừng làm phức tạp, bạn bày vẽ các tầng trận lồng, chồng chất lên nhau xong cuối cùng có làm đẹp được đâu, chưa kể đến góc nhìn bạn có làm nổi không mà vẽ ra như vậy".

Vì vậy hướng mới là:
- **một** trận pháp phẳng, một lớp;
- dựng được thật: ảnh nhìn thẳng từ trên xuống, dán lên một mặt phẳng 3D nằm ngang trên trời;
- vẻ đẹp đến từ hoạ tiết và chuyển động (xoay, chữ hiện dần, sáng nhịp), không từ việc chồng tầng;
- owner xem từng mẫu **ngay trong camera chơi** của lab, không xem tranh vẽ.

Mặt phẳng ngang đã có sẵn trong `games/.wt-ic-lab-all/src/lab/metal-ult-rain.ts` (đang dùng `formation-topdown`).

Luật của owner cho trận pháp: phong cách tu tiên huyền bí (vòng chữ cổ, bát quái, sen), không hình học cơ bản. Vòng phải là dải năng lượng dày, không nét mảnh.

Quyền chạy giống `docs/codex-queue/433e-tt-metal-sword-mix.md`: full-access, Chrome headless chỉ vào localhost:3148, không dừng server, tắt Chrome và xoá profile tạm khi xong.

Phạm vi được sửa và ghi:
- `games/.wt-ic-lab-all/src/lab/metal-ult-*`;
- ảnh gốc mới trong `games/immortality-cultivation/art-src/concept/ult-metal/sky-formation/`, đặt tên `sky-formation-simple-<a|b|c>.v1-try<k>.png` (không ghi đè file `sky-formation-*` có sẵn);
- atlas lab mới trong `games/.wt-ic-lab-all/art-src/lab/vfx/metal-ult/` tên `formation-simple-<a|b|c>.atlas.png` + `.json` (cùng định dạng atlas `formation-topdown` hiện có);
- `docs/codex-queue/443b-report.md` và `ABOUT.md`.

## Việc
1. **Vẽ 3 ảnh trận pháp nhìn thẳng từ trên xuống.** Dùng công cụ `image_gen`, tối đa 6 lần (3 mẫu, mỗi mẫu tối đa 2 lần).
   - Khung vuông 1024×1024, nền đen, hình tròn nằm gọn trong khung với lề 6 %, đối xứng tâm.
   - Một lớp duy nhất gồm 1 vành dày chứa chữ cổ, một hoạ tiết giữa, và khoảng trống tối giữa các phần để nhìn xa vẫn đọc được.
   - Màu vàng ấm, nét dày.
   - Ảnh tham chiếu: hoạ tiết chữ cổ trong `games/immortality-cultivation/art-src/concept/ult-metal/rain-components/formation-topdown.v1-try1.png`.
   - Ba mẫu:
     - **A:** vành chữ cổ và kiếm hướng tâm;
     - **B:** vành chữ cổ và bát quái;
     - **C:** vành chữ cổ và sen.
2. **Thử từng mẫu trong lab.** Thêm tham số `?formation=a|b|c` để thay texture trên mặt phẳng ngang có sẵn.
   - Trận nằm cao, phía trên và phía sau đàn quái. Ở camera chơi, đường kính trận chiếm 35–50 % bề ngang khung, không chạm mép trên.
   - Thêm 3 dấu hiệu độ cao: tia sáng rủ từ trận xuống (giữ tia đã có), một vùng sáng mờ bên dưới in trên mặt đất (vệt mềm, không vòng), và mặt dưới trận phát sáng nhẹ.
   - Chuyển động: vành xoay chậm, chữ hiện dần trong 0,4 s đầu, sáng theo nhịp.
   - Kênh màu ≤ 0,9. Kiếm lớn vẫn là điểm nhấn duy nhất.
3. **Chụp ảnh so sánh.** Mỗi mẫu chụp ở 0,8 s và 1,4 s, camera chơi (Alt+1) và góc sau lưng (Alt+2), nền `?ground=%23353a40`. Ghép tờ `sky-formation-443b.jpg`: mỗi hàng là ảnh trận nhìn từ trên kèm 4 khung chụp trong lab.

## Nghiệm thu
- Kiểm kiểu 0 lỗi.
- p95 ≤ 16,7 ms.
- Lưu tờ ghép vào `typing-game-review/owner-review/2026-11-17/tu-tien/` kèm một dòng trong `ABOUT.md`.
- Mặc định vẫn dùng texture cũ cho tới khi owner chọn.
- Xoá khung thô. Không commit.
