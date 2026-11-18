# Phiếu 447: Hư Không, dựng tuyệt kỹ hố đen trong lab (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 18/11, vòng 3)

Nguồn hình: games/immortality-cultivation/art-src/lab/vfx/void-ult/firefly-raw/void-accretion-ring.v1-try1.mp4, games/immortality-cultivation/art-src/lab/vfx/void-ult/firefly-raw/void-crescent-blade.v1-try1.mp4, games/immortality-cultivation/art-src/concept/ult-void/blackhole/void-blackhole-storyboard.v1-try1.png

## Bối cảnh
Ngày 18/11 owner duyệt phân cảnh hố đen của tuyệt kỹ Hư Không (`void-blackhole-storyboard.v1-try1.png`, 4 ô). Hai video Firefly dùng để dựng:
- vành bồi tụ có lõi đen, xoáy liên tục, chạy lặp được: `void-accretion-ring.v1-try1.mp4`, chấm A;
- lưỡi sáng trăng khuyết: `void-crescent-blade.v1-try1.mp4`, chấm B. Video này không có đoạn lóe vào và tắt chậm (gần 4,9 s mới đen), nên code phải tự cắt thời gian và làm mờ đuôi bằng độ mờ.

Tờ khung hình: `typing-game-review/owner-review/2026-11-18/tu-tien/void-blackhole-video/`.

Luật (owner, 17–18/11):
- Không vẽ hiệu ứng bằng code. Code chỉ được đặt, xoay, thu phóng đều, nhuộm, chỉnh độ mờ, chạy flipbook.
- Không vòng tròn hay vòng phép dưới đất. Vành bồi tụ là vật thể nghiêng trên không.
- Một điểm nhấn duy nhất.
- Vật thể trên trời phải là 3D thật, nhìn đúng ở camera chơi, từ trên xuống và từ sau lưng.

Quyền chạy:
- Full-access, Chrome headless chỉ vào localhost:3148, không dừng server.
- Được dùng ffmpeg và `tools/capture-prune/prune.mjs`.
- Cách đo p95 như `games/.wt-ic-lab-all/src/lab/metal-ult-rain-review.mjs`.
- Tắt Chrome và xoá profile tạm khi xong.

Phạm vi sửa:
- File mới `games/.wt-ic-lab-all/src/lab/void-blackhole-*.ts` và `.mjs`.
- Chỉ thêm import và hook trong `skills-main.ts` theo mẫu `ThunderUltChain`.
- Atlas mới vào `games/.wt-ic-lab-all/art-src/lab/vfx/void-ult/`.
- Ghi `docs/codex-queue/447-report.md` và `ABOUT.md`.
- Bật bằng tham số riêng `?blackhole=1` (không đụng tham số `ultVoid` cũ và giữ nguyên kiểm tra ở `void-ult-check.mjs:249`). Khi `blackhole=1`, hook trong `skills-main.ts` cho `ult-void` chạy hố đen **thay cho** cả hai nhánh cũ (layered và video) — chỉ thêm một nhánh `if` trước chỗ gọi cũ, không sửa logic cũ. Mặc định giữ chiêu Hư Không cũ cho tới khi owner duyệt.

## Việc
1. **Cắt flipbook** theo cách của `void-ult-cut.mjs` / `metal-ult-cut.mjs`:
   - vành bồi tụ: một đoạn lặp liền mạch 2–3 s;
   - lưỡi trăng khuyết: 0–2,2 s, làm mờ dần trong 25 % cuối.
   Trích khung bằng ffmpeg rồi đóng atlas. Nền đen chuyển thành alpha. Lõi đen của vành phải giữ đen đặc: làm một **mặt nạ alpha lấy từ chính các khung video vành** (vùng tối bên trong viền sáng), dùng làm lớp che phía sau (trộn thường, không cộng sáng). **Cấm** đĩa đen dựng bằng code, shader hình tròn hay bất kỳ hình tròn tự sinh nào.
2. **Dòng thời gian** theo 4 ô phân cảnh, tổng ≤ 7 s:
   - **Tụ lực (0–0,8 s):** một chấm đen nhỏ giữa cụm quái, cao ngang ngực quái, hạt sáng bị hút vào (dùng flipbook hạt có sẵn trong `art-src/lab/vfx/void*` hoặc `vfx/aura`).
   - **Mở (0,8–2,4 s):** vành bồi tụ (flipbook đặt trên một mặt phẳng trong không gian 3D, không quay theo camera) phóng to tới đường kính 9–12 m, nghiêng 20–30°, lơ lửng thấp trên đàn quái. Quái trong bán kính 8 m bị kéo trượt về tâm (gọi hook có sẵn). Bóng tối và ánh vàng hắt xuống đất dùng flipbook hoặc ảnh có sẵn, không dùng vòng tròn.
   - **Cao trào (2,4–4,4 s):** 6–10 lưỡi trăng khuyết lần lượt quét qua hố đen, mỗi lưỡi xoay một góc khác nhau. Quái bị nuốt (thu nhỏ rồi mờ đi). Đây là điểm nhấn.
   - **Dư âm (4,4–6,0 s):** vành co về một điểm, lóe một lần (vùng trắng ≤ 6 %), còn lại hạt vàng trôi.
3. **Âm thanh:** dùng `tt-sfx-ult-void` có sẵn, khớp lúc mở và lúc cao trào.

## Vòng lặp
- Tối đa 4 vòng: sửa → chụp → mở ảnh → so từng ô phân cảnh → sửa.
- Chụp ở 0,5 / 1,8 / 3,2 / 5,0 s, camera chơi (Alt+1) và sau lưng (Alt+2), nền `?ground=%23353a40`.
- Mỗi vòng in ra: đường kính vành trên màn hình, độ nghiêng, số lưỡi, vùng trắng, p95.

## Nghiệm thu
- Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms.
- Lưu `void-blackhole-lab.jpg` (phân cảnh bên cạnh khung chụp) và `.mp4` 7 s vào `typing-game-review/owner-review/2026-11-18/tu-tien/`, thêm dòng vào `ABOUT.md`.
- Xoá khung thô. Không commit.
