# Phiếu 453b: Tuyệt kỹ Ánh Sáng, bảo kính to và rõ hơn (lab)

Phản biện: PASS (Sonnet, 18/11)

## Bối cảnh
Phiếu 453 (`docs/codex-queue/453-report.md`) đã thay ba lớp vẽ bằng code bằng hình đã duyệt. Trong ảnh chụp `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-18/tu-tien/light-ult-453.jpg`, bảo kính Nhật Luân ở tay nhân vật còn quá nhỏ, ở góc chơi Alt+1 gần như không thấy.

Nguồn hình: games/.wt-ic-lab-all/art-src/lab/vfx/light/models3d/tripo/light-relic-mirror.tripo.v1.glb

## Việc (chỉ trong `games/.wt-ic-lab-all/src/lab/light-ult-*`)
1. Bảo kính bay lên, lơ lửng phía trên đầu và hơi lệch trước nhân vật từ đầu chiêu cho tới hết chiêu. Phóng to đều, sao cho ở góc chơi Alt+1 (1280×720) đường kính bảo kính trên màn hình đạt ≥ 40 px. Mặt kính quay về hướng bắn quạt tia.
2. Gốc quạt tia và gốc vệt quạt trên đất dời theo tâm bảo kính; tia cuối vẫn nằm giữa như cũ.
3. Mặt kính sáng dần khi tích lực, chỉ bằng emissive hoặc nhuộm màu. Vẫn giữ ánh môi trường cho kim loại.
4. Không thêm lớp hiệu ứng tự vẽ nào. Chú thích `// 453b`.
5. **Kiểm:** `tsc --noEmit` không lỗi; diện tích trắng ≤ 6 %; lớp phụ ≤ 0,9 mỗi kênh; p95 ≤ 16,7 ms. Đo và ghi đường kính bảo kính trên màn hình (px) ở Alt+1.
6. **Chụp** như phiếu 453: `light-ult-453b.jpg` và `.mp4` vào `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-18/tu-tien/`, thêm một dòng vào ABOUT.md. Tắt Chrome và xoá profile tạm khi xong.

## Ràng buộc
Không commit, không đổi nhánh, không xoá ảnh hay model.

## Giao nộp
`docs/codex-queue/453b-report.md`.
