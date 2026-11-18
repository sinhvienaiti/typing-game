# Phiếu 447b: Hư Không, lõi cầu 3D thật và hố đen to hơn (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 18/11)

Nguồn hình: games/.wt-ic-lab-all/art-src/lab/vfx/void-ult/models3d/void-blackhole-core.v1.glb, games/immortality-cultivation/art-src/lab/vfx/void-ult/firefly-raw/void-accretion-ring.v1-try1.mp4, games/immortality-cultivation/art-src/lab/vfx/void-ult/firefly-raw/void-crescent-blade.v1-try1.mp4, games/immortality-cultivation/art-src/concept/ult-void/blackhole/void-blackhole-storyboard.v1-try1.png

## Bối cảnh
Bản 447 (`typing-game-review/owner-review/2026-11-18/tu-tien/void-blackhole-lab.jpg`) có hai lỗi:
- ở góc chơi, hố đen đúng dáng nhưng nhỏ hơn trong phân cảnh;
- nhìn từ sau lưng thì dẹt như cái đĩa, vì video vành và lõi chỉ là mặt phẳng.

Owner chọn ngày 18/11: "Lõi cầu 3D + to hơn".

Claude đã dựng sẵn quả cầu lõi bằng Blender: `void-blackhole-core.v1.glb`, bán kính 1, màu đen tuyền, không phản sáng.

Giữ nguyên như `docs/codex-queue/447-tt-void-blackhole-lab.md`:
- luật cấm vẽ hiệu ứng bằng code;
- quyền chạy, server 3148, ffmpeg, prune;
- phạm vi sửa (`void-blackhole-*`, hook `?blackhole=1` trong `skills-main.ts`, atlas trong `art-src/lab/vfx/void-ult/`);
- cách đo.

Được ghi `docs/codex-queue/447b-report.md` và `ABOUT.md`. Khi xong, tắt Chrome và xoá profile tạm.

## Việc
1. **Lõi cầu 3D.** Thay lớp lõi mặt nạ phẳng bằng mô hình cầu GLB. Đặt ở tâm hố đen, dùng nguyên vật liệu trong file. Nhìn từ camera chơi, từ sau lưng hay từ trên xuống đều phải tròn. Không giữ lớp mặt nạ lõi phẳng nữa (giữ code cũ, chỉ không gọi).
2. **Vành bồi tụ** (flipbook video vành đã có):
   - đặt quanh lõi trên một mặt phẳng 3D nghiêng 20–30°;
   - phần vành phía sau lõi phải bị quả cầu che, nhờ thứ tự vẽ và kiểm tra độ sâu, để tạo cảm giác vành ôm quanh khối cầu;
   - thu phóng đều, đường kính vành gấp khoảng 2,2 lần đường kính lõi.
3. **To hơn.** Phóng cả hố đen 1,5–2 lần. Ở camera chơi 1280×720, đường kính vành trên màn hình phải ≥ 32 % bề ngang khung và không ra ngoài khung (lề ≥ 4 %).
4. **Cao trào (ô 3 của phân cảnh).** Thêm dải sáng chém ngang bằng các lưỡi trăng khuyết có sẵn:
   - 2–3 lưỡi nối thành một đường quét dài cắt ngang qua lõi;
   - thu phóng đều, không kéo giãn;
   - giữ 6–10 lưỡi xoáy của 447;
   - không tạo hình mới bằng code.
5. **Giữ nguyên:** dòng thời gian, kéo quái, nuốt quái, vùng trắng ≤ 6 %.

## Vòng lặp
- Tối đa 3 vòng: sửa → chụp → mở ảnh → so từng ô phân cảnh → sửa.
- Chụp ở 0,5 / 1,8 / 3,2 / 5,0 s, camera chơi (Alt+1) và sau lưng (Alt+2), nền `?ground=%23353a40&blackhole=1`.
- Vòng cuối chụp thêm góc nhìn thẳng từ trên xuống 90° ở 3,2 s.
- In ra mỗi vòng:
  - đường kính vành trên màn hình (%);
  - tỷ lệ cao/rộng của lõi trên màn hình ở cả 3 góc (phải từ 0,9 đến 1,1);
  - vùng trắng;
  - p95.

## Nghiệm thu
- Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms.
- Lưu `void-blackhole-lab-b.jpg` và `.mp4` vào `typing-game-review/owner-review/2026-11-18/tu-tien/`, giữ file cũ, thêm dòng vào `ABOUT.md`.
- Xoá khung thô. Không commit.
