# Chưa đủ bằng chứng (NEE) · cần truy vết

Quy trình: `.agents/skills/game-vfx-production/references/path-to-8.md`. Thiếu use, prompt, still hay hash; truy vết xong thì chuyển vào đúng luồng.

Do việc phân loại toàn kho (T0, luồng 2) điền.

| # | Key / việc | Vai trò · đoạn | Lý do · việc cần làm | Ưu tiên | Trạng thái |
|---|---|---|---|---|---|

<!-- T0:header -->
## T0 · Định tuyến toàn kho

Đơn vị là việc + vai trò + đoạn dùng; các key trong một dòng thuộc một owner. `chính` là take đề xuất theo toàn kho, không phải chứng nhận chất lượng. Mọi đoạn là đề xuất; kiểm A, matte, lề, seam và tốc độ thật thuộc bước sau. NEE giữ trạng thái công việc `todo`. Bằng chứng SHA-256, still và đường gọi: `.local/s2/jobs.json`.

| Mã việc · các key | Take chính | Vai trò · đoạn đề xuất | Lý do · việc cần làm | Ảnh | Ưu tiên | Trạng thái |
|---|---|---|---|---|---|---|
| T0:dragon-fire-body-ribbon <!-- job:dragon-fire-body-ribbon --> `dragon-fire-body-ribbon__take1`, `dragon-fire-body-ribbon__take2`, `dragon-fire-body-ribbon__take3` | `dragon-fire-body-ribbon__take1` | dải chất liệu travel; chưa khoá; nguồn mới kiểm 0–5 s | Thiếu use. Có cả đầu và đuôi rồng như hình dán uốn cong gần bất động; sai dải chất liệu thân lửa chảy ngang. Ít ember tách rời, không có nội khí sống đ → Truy vết use/prompt/still/hash thực trước khi chốt tuyến; không suy công dụng từ tên. | — | P4 | todo |
| T0:fire-ground-impact <!-- job:fire-ground-impact --> `fire-ground-impact__take1` | `fire-ground-impact__take1` | va chạm mặt đất; chưa chọn đoạn; đối chiếu best ngoại lai | Kết quả take1 yêu cầu chọn take2, nhưng take2 chỉ có trong results và không thuộc clips.json hiện tại. → Truy vết take2 và quan hệ nguồn trước khi thay/giữ; T0 chỉ sở hữu take1 thuộc kho. | — | P4 | todo |
| T0:fire-lotus-bloom-top <!-- job:fire-lotus-bloom-top --> `fire-lotus-bloom-top__take1`, `fire-lotus-bloom-top__take2`, `fire-lotus-bloom-top__take3` | `fire-lotus-bloom-top__take1` | chưa rõ vai trò; chưa khoá; nguồn mới kiểm 0–5 s | Thiếu use. Tám cánh như họa tiết phẳng, chỉ mép mới mọc lửa về sau. Hai cánh đối diện chưa dài nổi bật; chủ yếu phóng to chậm, 90% vẫn nguyên bông, thi → Truy vết use/prompt/still/hash thực trước khi chốt tuyến; không suy công dụng từ tên. | — | P4 | todo |
