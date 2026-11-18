# Phương pháp · Phiếu 209

- Chỉ ải `c1-s1`, ba chế độ mặc định, 11 bot và Chuẩn tắt nhịp ở cả ba chế độ. Mỗi báo cáo 36 ô × 100 seed, thêm 10 cặp G3c × 100 seed. Không truyền `--bots`, `--modes` hay `--off`.
- V0 chạy khói 2 seed trước, không đưa vào bảng cân bằng. V0 chính thức và mỗi biến thể đều chạy seed 1–100 và 101–200. Không có lượt thử ngắn đổi số.
- Bản chép từ `git archive main`; commit được ghim trong `evidence/main.commit`. Liên kết `main/node_modules -> ../../../node_modules` trỏ về thư viện có sẵn; không cài gói.
- Lệnh đo chạy trong `games/typing-survival/tmp/codex-209/main`, với `TMPDIR=/Users/toandx/htdocs/typing-game/games/typing-survival/tmp/codex-209/tmpdir`. Lệnh đầy đủ và thời gian UTC được lưu trong từng `evidence/wave-*.json`; giờ Việt Nam = UTC + 7.
- Mỗi đợt đọc `uptime` trước khi mở tiến trình. Tải 1 phút > 10 thì tối đa 3 báo cáo, còn lại tối đa 6. Các đợt không chồng nhau. Điều phối là một tiến trình Node chờ kết quả, không chạy mô phỏng. Dòng `peak` đếm tiến trình báo cáo đang chạy do làn này mở.
- Đã gọi `nice -n 15` đúng chỉ dẫn. Sandbox macOS từ chối đổi ưu tiên (`nice: setpriority: Operation not permitted`); `nice` vẫn chạy Node và lệnh đo kết thúc bình thường. Không có lần leo quyền hay công cụ thay thế. Không khẳng định tiến trình thực sự nhận mức ưu tiên 15.
- `summary.json` giữ số từng ô nguyên đơn vị ‰ từ JSON gốc, các số tổng hợp dùng phần trăm hoặc điểm phần trăm. Bảng tổng và cổng dùng độ chính xác JSON; bảng giáp dùng chuỗi đã làm tròn trong Markdown gốc. So mốc dùng các số được in trong Markdown ở cả hai bộ, bổ sung so chính xác JSON ở seed 1–100 (mốc cũ không có JSON cho seed 101–200).
- B1 đếm một ô cho mỗi bot trong sáu bot Mới–Nhanh ở Cân bằng; kèm riêng số chỉ số lệch để không lẫn hai cách đếm. Chọn nền B theo tổng ô lệch thô của hai bộ; hòa lấy trung bình B6 Cân bằng lớn hơn, rồi biên B3 nhỏ nhất lớn hơn (biên tới 70 % của Mới và 85 % của Trẻ em).
- Luật sát mép xét cả ô: mọi chỉ số lệch của ô không quá 3 điểm, và chỉ lệch ở một bộ seed; cùng ô ở bộ kia phải trong dải. Giữ cổng thô bên cạnh kết luận đã xét sát mép. Không nới dải, không miễn I ở cả hai bộ.
- B7 dùng trung bình bậc/đợt của từng ô, lấy ô lớn nhất và khoảng sinh nhỏ–lớn trên toàn ma trận. In thêm `maxWaveSteps` để phân biệt với trung bình. Chuẩn tắt nhịp chấm thắng/S/P/I/O ở Cân bằng theo luật sát mép.
- N, Q vẫn in đủ; không đưa hai chỉ số mềm này vào B1. B8/G5 là các bất biến học mà script bot đo, không chứng minh người chơi đã đọc nghĩa hay nghe âm. G8 là hai trận phát lại trong Node (seed 1, 2) do script gốc quy định, không phải toàn bộ 100 seed.
- G3m luôn dùng hai bộ cảnh khắc chế 1–16 và 17–32 của script gốc, độc lập với bộ 100 seed đang đo. Không chạy riêng test suite.
- B9: **THIẾU SỐ: cần người thật chơi**. Kết luận chỉ nói bot đạt hay chưa đạt; không kết luận người chơi thấy vừa.

## Tái tạo bảng

Từ repo cha:

```sh
node docs/codex-queue/209/tools/summarize.mjs
```

Script chỉ dùng Node chuẩn, đọc `variants.json`, `runs/`, mốc cũ trong `evidence/audit-2026-10-28/` và commit đã ghim. Không đọc checkout game, không cần `node_modules`, không ghi vào game. Chạy lại ghi `summary.json` và `summary.md` với cùng nội dung. Chạy lại mô phỏng là việc khác, cần dựng lại bản chép theo phiếu và dùng `tools/run-wave.mjs`; không dùng script tổng hợp để mở thêm biến thể.
