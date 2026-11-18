# Vòng 4 · Bước 3b · Lắp vết sét cháy anh đã duyệt (sau `tp2=1`)

Chỉ làm sau khi anh duyệt một bản ở bước 3a (cổng A trong `LANE-1.md` ghi bản nào). Thay vết tím phẳng của R3-3 (`src/lab/thunder-aftermath-r2.ts`) bằng hai lớp đã duyệt. Luật: `path-to-8.md` §7.

## Việc
- Nạp `thunder-scorch-base` và `thunder-scorch-cracks` của bản được duyệt thành texture tĩnh (KTX2 như các atlas khác nếu có công cụ trong repo; không thì PNG), nằm phẳng trên đất đúng điểm giáng, cỡ như vết hiện tại.
- Nhịp (engine điều khiển, không vẽ thêm bằng mã):
  - hiện lúc cột rút (giữ mốc `THUNDER_MARK_START_S` hiện có);
  - lớp khe sáng ngay khi hiện rồi **nguội dần** (giảm sáng, ngả tím sẫm) trong khoảng 1,0 s;
  - lớp nền ở lại lâu hơn rồi **xói từ mép vào** (ngưỡng alpha theo khoảng cách tới tâm cộng nhiễu từ chính texture), hết trong 1,2–2,0 s;
  - điện dư giữ như R3-3, tắt trước vết.
- Bỏ vết tím cũ khi bật bản mới; `tp2` tắt thì không đổi gì.

## Ngân sách (§7)
- Thêm ≤ 1,0 ms p95; ≤ 2 draw call thêm; ≤ 16 MB texture; không cấp phát mỗi khung; mã khoảng ≤ 150 dòng không tính test. Nếu cần ngưỡng xói thì dùng lại cách ăn mòn đã có trong lab (không shader mới khi chưa đo A/B).

## Nơi làm và ranh giới
- Worktree `games/.wt-ic-lab-all`. **Được ghi:** `src/lab/thunder-aftermath-r2.ts`, chỗ nối, test, báo cáo `docs/codex-queue/laneL1-report.md`; chép hai ảnh đã duyệt vào `art-src/lab/vfx/thunder/` của worktree (media không vào git).
- **Không:** lệnh git ghi; mở cổng mạng; mở trình duyệt.

## Đạt khi
- Test node: hiện đúng lúc, nằm phẳng, khe nguội trước, nền xói từ mép, tan hết đúng hạn, `tp2` tắt thì không đổi.
- `tsc` sạch; chạy riêng các test liên quan. Claude chạy toàn bộ vitest.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
