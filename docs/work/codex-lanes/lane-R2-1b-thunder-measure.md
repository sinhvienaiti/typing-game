# Vòng 2 · Bước 1b · Kịch bản quay và đo hiệu năng cho Cột Lôi (`tp2` tắt và bật)

Sau bước 1a. Luật đo: `.agents/skills/game-vfx-production/references/path-to-8.md` §7. Codex chỉ viết và kiểm cú pháp. Claude chạy ngoài sandbox.

**Model `gpt-6.1-sol`, mức `high`.** Một lần chạy. Báo cáo: thêm ≤ 8 dòng vào `docs/codex-queue/laneR2-report.md`, có hai lệnh chạy chính xác.

## 1. Quay trước và sau
Thêm cảnh `TP` vào `scripts/visual/scenarios/lab-pilot-ab.mjs`, giữ nguyên P1–P4:
- hệ Lôi, tung `pillar-thunder-single` (phím 8, mục Cột Lôi), đúng cách lab đang làm;
- **A:** URL hiện tại (B8). **B:** thêm `tp2=1`;
- **hai góc:**
  - `play`: camera chơi, khung chứa cả người tung và điểm giáng;
  - `caster`: cận cảnh người tung, người chiếm khoảng 35–50 % chiều cao khung;
- **12 khung:** 8 khung trong 0–0,6 s (tụ lực, phóng), 4 khung sau đó;
- cùng seed, cùng camera, nhãn mù X/Y, khoá riêng;
- kiểm điểm ảnh hiệu ứng ≥ 0,5 % ở khung đỉnh như các cảnh khác. Dùng `EFFECTS=TP` để chỉ quay cảnh này.

## 2. Đo hiệu năng
Viết `scripts/visual/scenarios/lab-tp-perf.mjs` theo cách đo của `games/immortality-cultivation/scripts/visual/scenarios/lab-element-perf.mjs`: thời gian CPU mỗi khung, rồi đọc 1 điểm ảnh để chờ GPU qua `__lab.perf` hoặc hàm tương đương.
- Tung Cột Lôi lặp lại 10 lần trong bầy quái mặc định, 1920 × 1080, DPR 1, `q=high`.
- Đo hai bản: không có `tp2` và có `tp2=1`. Mỗi bản `RUNS=3`, lấy trung vị.
- Ghi JSON: p50, p95, p99, max cho mỗi bản, chênh p95, cùng số draw call nếu đọc được (`renderer.info.render.calls`).
- In một dòng kết luận theo ngân sách: ĐẠT nếu chênh p95 ≤ 1,0 ms và p95 ≤ 11,5 ms, ngược lại TRƯỢT.

## Ranh giới
- **Được ghi:** hai file kịch bản trong `games/.wt-ic-lab-all/scripts/visual/scenarios/`; báo cáo.
- **Không:** sửa mã lab; lệnh git ghi; mở cổng mạng; mở trình duyệt.

## Đạt khi
- `node --check` cả hai file qua.
- Báo cáo có lệnh chạy, với `URL`/`BASE` là `http://127.0.0.1:3146/skills-lab.html` và `OUT_DIR` mới dưới `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/r2-step1/`.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
