# Phiếu 433d: Kim mưa kiếm — trận pháp 3D thật trên trời và kiếm 3D rơi


Phản biện: PASS (Sonnet, 17/11; sửa sau phản biện vòng 2: bỏ chỗ mâu thuẫn ở Bối cảnh)
## Bối cảnh
Owner 17/11 chọn "Video Firefly ghép mảnh nhỏ" cho Kim vì bản dựng bằng code chỉ ~5/10 (`typing-game-review/owner-review/2026-11-17/tu-tien/metal-sword-rain-r3.jpg`). Phiếu 435 đã có 2 thành phần đẹp (`games/immortality-cultivation/art-src/concept/ult-metal/rain-components/metal-rain-comp-samples-435.jpg`): (a) kiếm rơi có vệt sáng vàng mềm, (b) vòng trận pháp nhìn phối cảnh có tia sáng rủ. Owner 17/11 sau đó yêu cầu mọi thứ trên trời hay nằm phẳng phải là hình 3D thật trong không gian, nên phiếu này **không** dùng hai ảnh 435 làm thẻ; chúng chỉ là tham chiếu màu và độ mềm. (Tên file giữ chữ `use-stills` vì lịch sử phiếu.) Phân cảnh đích: `.../ult-storyboards/ult-storyboard-samples-431.jpg` (nửa trái).

## Việc (worktree `games/.wt-ic-lab-all`, `src/lab/metal-ult-rain.ts`)
1. Kiểm góc nhìn: mọi thành phần trên trời hoặc nằm trên mặt đất phải là hình học 3D đặt đúng trong không gian thế giới, nhìn đúng ở cả camera chơi 55°, góc trên và góc sau lưng. Không dùng ảnh đã vẽ sẵn phối cảnh cho các mặt phẳng nằm.
2. **Trận pháp (3D thật, owner 17/11: "những trận pháp được triệu hồi ở trên trời, nó cần được nhìn 3d để không bị lệch"):** **không** dùng thẻ quay về camera và **không** dùng ảnh `formation-sky` (ảnh đã vẽ sẵn phối cảnh nghiêng, đặt vào 3D sẽ lệch). Trận là một mặt phẳng nằm ngang thật trong không gian (mặt XZ, pháp tuyến hướng xuống đất) ở độ cao 6–8 m, dùng texture nhìn thẳng từ trên xuống (tạm dùng `art-src/lab/vfx/metal/metal-caster-seal` — nhìn từ trên — cho tới khi có ảnh trận pháp nhìn thẳng mới), để camera 55° tự tạo phối cảnh bầu dục đúng. Tia sáng rủ xuống là các mặt phẳng dọc hoặc hình nón mở mờ nối từ viền trận xuống đất, cũng là hình 3D thật. Đặt sao cho cả vòng và các tia rủ nằm trong khung camera chơi 1280×720, cách mép trên ≥ 12 %, không giao thẻ tên chiêu; xoay chậm nhẹ (lắc ±3°) và nhịp sáng.
3. **Kiếm rơi:** dùng mô hình 3D Tripo hiện có `art-src/lab/vfx/metal-ult/models3d/tripo/ult-metal-sword.tripo.v1.glb` cho cả lúc rơi và lúc cắm (không dùng thẻ phẳng cho kiếm, vì ảnh `sword-fall-streak` cũng đã vẽ sẵn góc nhìn); cao 4–6 m, rơi từ dưới trận xuống; vệt sáng phía sau là ribbon 3D theo quỹ đạo (có thể lấy màu và độ mềm tham khảo từ ảnh `sword-fall-streak`); khi chạm đất cắm nghiêng nhẹ, cùng `metal-impact-v2` và `metal-ground-mark` phóng to.
4. Giữ nhịp camera đẩy vào của 433c nhưng giảm còn 70–80 % khoảng cách (nhẹ hơn) để trận pháp không tụt khỏi tầm nhìn trời.
5. Giữ dư âm bụi vàng, kiếm lớn cuối (mô hình kiếm ×3 rơi và cắm).

## Nghiệm thu
- Ảnh chụp lệnh để lại cho Claude gồm cả góc trên (phím 1), góc sau lưng (phím 2) và camera chơi, để kiểm trận pháp không lệch ở mọi góc.
- Kiểm kiểu 0 lỗi; probe in toạ độ màn hình của trận pháp (mép trên ≥ 12 %, không giao thẻ tên chiêu) ở 0,4/1,2/2,4 s; số kiếm 3D đang rơi ≥ 4 ở 0,8–2,0 s; trả pool sau 4 s; 0 lỗi nạp ảnh.
- p95 `stress.html` 100 quái ≤ 16,7 ms; để lệnh chụp + quay clip 4 s cho Claude.
- Chỉ sửa `src/lab/metal-ult-*`, `art-src/lab/vfx/metal-ult/rain/`. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/433d-report.md`.
