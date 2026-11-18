# Mẫu học trả ra iframe phải đúng kiểu

Ngày 30/10/2026 · Phiếu 234 · Đóng 227-F2 (phát hiện P1-233-01 của 233).

Sửa 228 chỉ bỏ trường dư ở cấp đầu của `recentSamples`. Một object hay
array đặt vào một trong năm trường hợp lệ vẫn đi qua `lookup`/`query`,
nên câu trả lời lồng bên trong tới được khung game (233: 10/10 đỏ).

Nay mỗi mẫu được dựng lại từ năm trường, và chỉ giữ khi đúng kiểu của
`LearningSample` trong `core.d.mts`: `occurredAt`, `gameId`, `activityType`
là chuỗi, `result` là `"correct"` hoặc `"wrong"`, `hintUsed` là boolean.
Mẫu sai kiểu hay thiếu trường bị bỏ cả mẫu, không ép kiểu, không cắt chuỗi.
Luật này chạy ở hai chỗ:

- đường trả dữ liệu (`shared/learning/query.mjs`), nên hồ sơ đã lưu từ
  trước cũng được bảo vệ; `recentSamples` không phải mảng thì trả `[]`;
- nhập sao lưu (`shared/learning/profile-backup.mjs`), bỏ mẫu sai kiểu
  khỏi bản hồ sơ trả về. Hàm không có chỗ báo số mẫu bị bỏ, nên chỉ bỏ.

Không đổi `recentMistakes`, `recentAnswers`, công thức hay phiên bản hồ sơ.
Mẫu không phải object và danh sách quá 8 mẫu khi nhập vẫn bị từ chối như cũ.

| Kiểm | Trước | Sau |
|---|---:|---:|
| Shared learning | 89/89 | 112/112 |
| Portal | 109/109 | 129/129 |
| Probe của 233 | 43/53 | 53/53 |

43 test mới viết trước mã, cả 43 đỏ. Tắt riêng kiểm kiểu ở đường trả
dữ liệu: 21 test đỏ; tắt riêng ở nhập sao lưu: 21 test khác đỏ. Chi tiết
trong [`234-report.md`](../codex-queue/234-report.md). Chưa chạy trình
duyệt; không commit/push.
