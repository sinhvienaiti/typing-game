# Luồng Codex 1 · GIỮ-CHỈNH: mỗi lần chạy làm đúng MỘT dòng, rồi dừng

Anh (07/11 10:00): "Giảm và chia nhỏ"; (10:05) làm thử vài video trước khi áp cho cả kho (`docs/work/tasks/vfx-pilot-0711.md`, hiệu ứng P3).

Làm **dòng `todo` đầu tiên** của `docs/work/tasks/vfx-streams/stream-1-keep.md`, đúng theo "Mỗi việc", "Khoá" và "Ranh giới" của `docs/work/codex-lanes/lane-S1-keep-tune.md`. **Chỉ một dòng**, xong thì dừng.
- Lần chạy trước bị dừng giữa chừng và đã trích khung vào `.local/s1/<job>/`. Dùng lại nếu khớp SHA-256 nguồn.
- Soi từng khung **chỉ trong đoạn dùng**, xem bằng tấm ghép 6–12 khung, **tối đa 12 ảnh** trong lần chạy.
- Ghi thêm vào `recipe.md`:
  - đường bao engine bằng số (thời lượng; đường cong scale và alpha theo khung; ăn mòn bắt đầu và kết thúc);
  - lớp phụ cần có, kèm id. Lớp Blender do luồng 3 làm.
- Thêm một đoạn ≤ 6 dòng vào `docs/codex-queue/laneS1-report.md`.

**Model `gpt-6.1-sol`, mức `high`.** Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
