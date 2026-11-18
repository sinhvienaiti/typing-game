# Phiếu 453: Tuyệt kỹ Ánh Sáng, thay ba lớp đang vẽ bằng code bằng hình đã duyệt (lab)

Phản biện: PASS (Sonnet, 18/11)

## Bối cảnh
Luật owner 17/11 cấm tự vẽ hiệu ứng bằng code. Bản kiểm `docs/work/tasks/vfx-code-drawn-audit.md` chỉ ra ba lớp của chiêu Ánh Sáng đang vẽ bằng code:
- quạt tia `FanBeams` trong `games/.wt-ic-lab-all/src/lab/light-ult-fan-space.ts`, khoảng dòng 35;
- thấu kính `HeldLens`, cùng file, khoảng dòng 74: dựng bằng torus, sphere và cylinder;
- vệt quạt trên đất, nếu có, trong `light-ult-ground.ts`.

Owner 18/11 đã chọn hình thay:
- tia sáng mẫu B;
- vệt quạt trên đất mẫu C (tia mảnh);
- bảo kính Nhật Luân v2, đã dựng 3D bằng Tripo.

Nguồn hình: games/immortality-cultivation/art-src/lab/vfx/light/stills/light-ray-a2.v1-try2.png, games/immortality-cultivation/art-src/lab/vfx/light/stills/light-ground-wedge.v1-try3.png, games/.wt-ic-lab-all/art-src/lab/vfx/light/models3d/tripo/light-relic-mirror.tripo.v1.glb

## Việc (chỉ trong `games/.wt-ic-lab-all`)
1. **Quạt tia:** bỏ phần hình học tự vẽ của `FanBeams`. Mỗi tia là một thẻ phẳng dán ảnh tia B, cộng màu (additive) vì nền ảnh đen. Code chỉ đặt vị trí, xoay, co giãn đều, nhuộm màu, làm mờ dần và hẹn giờ. Không làm mờ nhoè (blur), không kéo giãn lệch tỷ lệ, không dùng mặt nạ tự vẽ. Giữ nguyên số tia, hướng tia, thời điểm và đích bắn như hiện tại; tia cuối vẫn nằm giữa như owner đã yêu cầu trước đó.
2. **Bảo kính:** bỏ `HeldLens` tự dựng, nạp GLB bảo kính và đặt đúng chỗ cầm, lớn bằng thấu kính cũ (hàm `bbox`/`grip` vẫn trả số đúng). Kim loại cần ánh môi trường để không bị tối: thêm environment map lấy từ ảnh có sẵn trong lab (ví dụ PMREM từ một ảnh bầu trời hoặc studio có sẵn; ghi đường dẫn ảnh vào báo cáo). Mặt kính phát sáng nhẹ khi tung chiêu, chỉ bằng emissive hoặc nhuộm màu.
3. **Vệt quạt trên đất:** thay bằng ảnh C, dán lên mặt phẳng nằm trên đất (ảnh nhìn từ trên xuống 90°), đỉnh quạt ở chân người tung, mở theo hướng quạt tia, cộng màu và mờ dần.
4. Giữ các lớp khác như cũ. Mỗi lớp mới có một dòng chú thích `// 453` kèm tên file ảnh.
5. **Kiểm:** `tsc --noEmit` không lỗi. Diện tích trắng ≤ 6 %. Lớp phụ ≤ 0,9 mỗi kênh màu. p95 ≤ 16,7 ms.
6. **Chụp:** dùng kịch bản có sẵn `src/lab/light-ult-review-g.mjs` làm mẫu, chạy `node src/kit/tools/cdp-run.mjs <kịch bản> --width=1280 --height=720 --dpr=1`, phím 8 chọn tuyệt kỹ (theo cách của lab; kiểm trong lab chiêu Ánh Sáng dùng phím nào). Chụp góc chơi Alt+1 và góc sau Alt+2, nền tối `?ground=%23353a40`. Lưu `light-ult-453.jpg` và `.mp4` vào `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-18/tu-tien/`, thêm một dòng vào ABOUT.md của thư mục đó. Tắt Chrome và xoá profile tạm khi xong, kể cả khi lỗi.

## Ràng buộc
- Chỉ sửa file trong `games/.wt-ic-lab-all/src/lab/light-ult-*`.
- Không commit, không đổi nhánh, không xoá ảnh hay model.
- Không thêm hiệu ứng tự vẽ mới.

## Giao nộp
`docs/codex-queue/453-report.md`: file đã sửa, số đo, đường dẫn ảnh chụp và việc chưa làm.
