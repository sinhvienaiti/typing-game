# Phiếu 421: Nối 17 flipbook bùng nổ -v2 vào lab, bật/tắt so với bản cũ


Phản biện: PASS (Sonnet, 16/11)
## Bối cảnh
Owner 16/11 duyệt làm lại clip bùng nổ. Đã có 17 bộ `-v2` mới (phiếu 419: fire-impact, fire-big-burst, earth-ring-burst, metal-impact, metal-big-burst, void-big-burst, wind-ring-burst; phiếu 420: dark-ring-burst, water-ring-burst, poison-big-burst, poison-ring-burst, blood-big-burst, wood-big-burst, dark-big-burst-white, dark-ground-impact-white, thunder-impact, star-ring-burst) trong `games/immortality-cultivation/art-src/lab/vfx/<hệ>/<clip>-v2.*` (và `games/.wt-ic-lab-all/art-src/...` cùng nội dung). Báo cáo `419-report.md`, `420-report.md` có json/pivot. `fire-impact` và `metal-impact` trước đây chưa có, nay có lần đầu. Clip góc 55° (420) có pivot ở điểm chạm đất.

## Việc (worktree `games/.wt-ic-lab-all`)
1. Tìm chỗ lab nạp atlas bùng nổ theo tên (ví dụ `element-kit` trong `src/view/skills/`, `five-phase-clip.ts`, `pilot-overrides.ts`); thêm bảng ánh xạ cũ → `-v2` trong **file mới** `src/lab/burst-v2.ts`, bật mặc định, với một phím lab (ghi trong báo cáo) và tham số URL `?burst=old` để quay về bản cũ.
2. Clip góc 55°: đặt thẻ theo pivot chạm đất (đáy thẻ ở mặt đất, không nổi lơ lửng), quay về camera theo trục đứng; clip vòng/chạm đất không ép thành tròn.
3. Mọi clip -v2: tail fade theo json; giới hạn số thẻ sống như cũ.
4. Chỗ cần đổi trong file có sẵn chỉ là một dòng gọi sang `burst-v2.ts`; không đổi `src/view/` của game chính (chỉ lab).

## Nghiệm thu
- Kiểm kiểu strict 0 lỗi cho file sửa/thêm; probe CPU: mỗi trong 17 tên -v2 được nạp, không lỗi 404 (đường dẫn tồn tại), `?burst=old` trả về đúng bản cũ.
- Để lệnh chụp cho Claude: lưới 17 clip ở camera chơi (55°) trên mặt đất lab, cũ | mới.
- Chỉ sửa trong `games/.wt-ic-lab-all/src/lab/` (file mới + một dòng nối). Không đụng `*-ult-*`, `anim-*`. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/421-report.md`.
