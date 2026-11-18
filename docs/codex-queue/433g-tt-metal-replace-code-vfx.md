# Phiếu 433g: Kim, thay các lớp vẽ bằng code bằng ảnh thật (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 17/11, vòng 3)

Nguồn hình: games/.wt-ic-lab-all/art-src/lab/vfx/aura/aura-metal-feather-mantle.atlas.png, games/.wt-ic-lab-all/art-src/lab/vfx/aura/aura-metal-windsilk.atlas.png, games/.wt-ic-lab-all/art-src/lab/vfx/aura/qi-streak-1.png, games/.wt-ic-lab-all/art-src/lab/vfx/metal-ult/rays.png, games/.wt-ic-lab-all/art-src/lab/vfx/metal/metal-ground-impact.atlas.png, games/.wt-ic-lab-all/art-src/lab/vfx/metal-ult/slash-ground.png

## Bối cảnh
Ngày 17/11 owner chốt hai điều:
- "cấm tự làm các hiệu ứng vfx bằng code";
- các lớp vùng xám (ảnh thật nhưng bị shader làm mờ, kéo giãn hoặc lọc kênh) **cũng tính là vẽ bằng code**, phải thay hết.

Danh sách lớp nằm ở `docs/work/tasks/vfx-code-drawn-audit.md`. Phiếu này thay K2, K3, K6 và K7. K5 (vệt kiếm rơi) **không làm ở phiếu này**: vệt kiếm còn chờ owner chọn ảnh ở phiếu 444.

Quyền, server 3148, ffmpeg, prune và cách đo giữ như `docs/codex-queue/433f-tt-metal-rain-bigger-longer.md`. Phạm vi sửa: `games/.wt-ic-lab-all/src/lab/metal-ult-*` và `metal-sword-look.ts`. Được ghi `docs/codex-queue/433g-report.md` và `ABOUT.md`. Khi xong, tắt Chrome và xoá profile tạm.

## Luật
- Mỗi lớp nhìn thấy là một file trong dòng "Nguồn hình", hiện **đúng hình gốc**.
- Code chỉ được làm các việc sau: đặt vị trí, xoay, thu phóng **đều cả hai chiều**, nhuộm màu, chỉnh độ mờ theo thời gian, chạy flipbook.
- Không làm mờ, không kéo giãn méo hình, không mask tròn, không dùng shader fresnel/sin/noise để tạo hình.

## Việc
1. **K2, hào quang kiếm lớn.** Bỏ vỏ fresnel. Thay bằng flipbook `aura-metal-feather-mantle` (hoặc `aura-metal-windsilk`, chọn bản đẹp hơn sau khi chụp), đặt quanh kiếm lớn, đứng thẳng theo kiếm, thu phóng đều theo **chiều cao**: chiều cao hào quang ≈ 1,3 lần chiều cao thân kiếm, chiều ngang theo tỉ lệ gốc của flipbook.
2. **K3, kiếm nhỏ dạng năng lượng.** Bỏ shader core/flow/rim. Giữ mô hình Tripo, phủ màu vàng sáng bằng emissive **một màu và một cường độ đều trên cả thân** (đặt bằng thuộc tính `emissive` + `emissiveIntensity` của vật liệu chuẩn three.js; gỡ `emissiveMap` và tắt vertex color; không shader tuỳ biến; không fresnel/rim, không gradient, không biến thiên theo điểm ảnh); gắn `qi-streak-1.png` dọc lưỡi kiếm làm dải khí **giữ nguyên tỉ lệ ảnh gốc** (thu phóng đều; nếu ngắn hơn lưỡi thì đặt 1–2 bản nối tiếp, không kéo giãn). Kiếm lớn vẫn là điểm nhấn: tỷ số độ sáng so với kiếm nhỏ ≥ 1,5.
3. **K6, tia sáng từ trận.** Thay lớp crop-blur bằng `rays.png`, để nguyên hình.
4. **K7, vệt sáng đất.** Thay mask tròn và blur bằng flipbook `metal-ground-impact` hoặc `slash-ground.png`, để nguyên hình.
5. **Giữ nguyên:** trận A, nhịp mưa và quãng rơi của 433f, vùng trắng ≤ 6 %. Không xoá code cũ của các lớp bị thay, chỉ ngừng dùng.

## Vòng lặp
- Tối đa 3 vòng: sửa → chụp → mở ảnh → so với `typing-game-review/owner-review/2026-11-17/tu-tien/metal-rain-f.jpg` → sửa.
- Chụp camera chơi (Alt+1) và góc sau lưng (Alt+2), nền `?ground=%23353a40`.
- Báo cáo ghi rõ: mỗi lớp đã thay dùng file nào, còn shader tạo hình hay không, vùng trắng, p95.

## Nghiệm thu
- Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms.
- Lưu `metal-rain-g.jpg` và `.mp4` mới, giữ file cũ, thêm dòng vào `ABOUT.md`.
- Xoá khung thô. Không commit.
