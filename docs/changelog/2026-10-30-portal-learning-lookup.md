# Cổng game trả lời tra cứu hồ sơ học

Ngày 30/10/2026 · Phiếu 215.

Portal nhận `typing-game:learning:v1:lookup` từ iframe đang mở, kiểm đúng
cửa sổ và origin đăng ký, ghi hết attempt đang chờ rồi trả `query-result`
cùng `requestId`. Áp dụng chung cho mọi game trong registry, không gắn
cứng Dragonhold. Trước đây tin bị từ chối nên Dragonhold không đọc được
bản ghi đã học ở game khác.

Lõi chung lưu `recentSamples` cho vocabulary, grammar và sentence, mỗi
mẫu gồm thời gian, game, hoạt động, kết quả và boolean `hintUsed`; giữ tám
mẫu mới nhất theo thời gian, không chứa câu trả lời. Tra cứu trực tiếp
1–200 id, chuẩn hóa và bỏ trùng theo hợp đồng kit, bỏ id chưa học và khóa
nguyên mẫu. Kết quả luôn có `recentSamples`, dùng `[]` cho bản ghi cũ.
Sao lưu v1 nhận trường tùy chọn này và kiểm giới hạn tám object.

Không đổi công thức điểm, bộ đếm, ngày ôn, danh sách lịch sử cũ hay phiên
bản hồ sơ. Snapshot 12 sự kiện trước/sau giống hệt từng byte khi bỏ
`recentSamples`. Lookup chỉ đọc; tin hỏng trả `invalid-request`, kho lỗi
khi đọc trả `query-failed`.

| Kiểm | Trước | Test đỏ trước mã | Sau |
|---|---:|---:|---:|
| Shared learning | 12 file, 55/55 đạt | 13 file, 56 đạt, 28 lỗi | 13 file, 84/84 đạt |
| Portal | 2 file, 51/51 đạt | 3 file, 68 đạt, 9 lỗi | 3 file, 77/77 đạt |
| Build portal (`tsc`, Vite) | Mã 0 | — | Mã 0 |

55 test mới: shared learning 29 test, portal 26 test. Toàn bộ test cũ
vẫn xanh; `pnpm learning:check` mã 0. Tra 200 id trong hồ sơ 5.000 từ:
trung vị 20 lần **0,1875 ms**, dưới mục tiêu 20 ms trên Mac mini arm64,
Node v24.22.0. Bằng chứng, SHA-256 và phần Claude kiểm tiếp nằm trong
[`215-report.md`](../codex-queue/215-report.md). Chưa kiểm trình duyệt;
Claude duyệt, cập nhật các ghi chú phụ thuộc rồi kiểm Dragonhold qua cổng.
