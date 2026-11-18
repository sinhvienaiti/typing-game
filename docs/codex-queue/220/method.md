# Phương pháp · Phiếu 220

Kế thừa cách đếm và dải đích của [209](../209/method.md). Mỗi báo cáo một ải có 36 ô × 100 seed và 10 cặp G3c × 100 seed; báo cáo bốn ải có 144 ô và 40 cặp. Hai bộ seed 1–100 / 101–200 luôn đi cùng. Không có lượt thử ngắn đổi số.

- Mốc worktree: `ba6d70e9d6978eb4b430d119c409f3d47f9a364e`, nhánh `ts-codex`. V6 trước sửa so mọi trường `summary`, không làm tròn; bắt buộc 0 ô lệch với 209. Sau sửa đối chiếu lại phần c1-s1 của ba cấu hình bốn ải.
- `variants.json` giữ nguyên chuỗi V6, thêm một núm mỗi f1–f4. Không ghi các khóa `x-*`; runner bỏ tiền tố `x-` để tra cấu hình. `--stages=` nhận danh sách ải; đường JSON/MD là tuyệt đối.
- Chạy Node và pnpm trong gốc `games/.wt-ts-codex`. `TMPDIR=/Users/toandx/htdocs/typing-game/games/.wt-ts-codex/tmp/codex-220/tmpdir`. Đầu ra đo lưu ở `tmp/codex-220/runs/`, chép và đối chiếu SHA-256 ở `220/runs/`.
- Mỗi đợt đọc `uptime`, tối đa 4 báo cáo đồng thời, tải 1 phút > 10 thì tối đa 2. `nice -n 15` có thể bị sandbox từ chối đổi ưu tiên; ghi nguyên văn, không suy rằng ưu tiên thực là 15. Nhật ký UTC, lệnh, PID, exit và peak ở `evidence/wave-*.json`.
- B1 đếm sáu ô Mới–Nhanh ở Cân bằng, kèm số chỉ số thắng/S/P/I/O lệch. N và Q là mềm. Luật sát mép áp cả ô: mọi chỉ số lệch ≤ 3 điểm, chỉ lệch ở một bộ, bộ kia trong dải. B7 áp cùng luật với Chuẩn tắt nhịp, cộng trần bậc/đợt và khoảng sinh.
- B2 kiểm mọi ô có director ở Cân bằng (S ≥ 90 % kèm I ≥ 20 %); script 209 lọc `summary.mode`, trường này có trong JSON. B3–B8, G3c, G3m, G5, G8, §7.6 giữ ngưỡng 209. Thử thách không đảo: Khá và Nhanh không dưới Mới quá 5 điểm; vẫn in riêng Nhanh − Mới và đích ≥ 0.
- Chọn ứng viên theo phiếu 220: đạt đủ cả hai bộ trước; nhiều bản đạt thì ít núm trước, rồi I Khá lớn nhất nhỏ hơn. Không bản đạt: ít điều kiện bắt buộc trượt cộng hai bộ, hòa xét I Khá lớn nhất rồi số ô B1 lệch.
- Công cụ tổng hợp lọc thêm `stage` khi lấy ô; báo cáo bốn ải chấm từng ải riêng. G3m, G5, G8 và §7.6 là cổng chung mà script gốc in cuối báo cáo; G3c, B1–B8 có số từng ải; riêng B6 còn in số gộp bốn ải là cổng chung, số từng ải dùng để chỉ suy giảm cục bộ. G3m dùng cảnh một súng nạp thẳng `loadMagazine`: chỉ R1 đổi sức chứa; R2/R3 không chạy trong cảnh đó.
- I = lúc `live <= 0 && !busy`: R2 không đổi định nghĩa trạng thái mọi bến đầy; chỉ tác động gián tiếp qua chọn bến/trận đấu. R3 cho bến đầy chưa tăng được tính `live`, vì còn một từ hữu ích; giảm I vì lý do này là một phần có chủ đích của luật.
- B9: **THIẾU SỐ: cần người thật chơi**. Mọi khuyến nghị là số bot, không kết luận cảm nhận người chơi.

Tái tạo bảng từ gốc worktree, không mở thêm mô phỏng:

```sh
TMPDIR="$PWD/tmp/codex-220/tmpdir" node ../../docs/codex-queue/220/tools/summarize.mjs
```

Sau khi đã dọn tmpdir, chỉ cần tạo lại đúng thư mục tạm nếu muốn dùng cùng lệnh; script tổng hợp chỉ đọc file và không cần tsx.
