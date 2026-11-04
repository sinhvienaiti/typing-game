# Chi phí token

Đo bằng `python3 tools/agent-usage/usage.py <thư mục phiên> <mốc giờ UTC>`. Đơn vị là token hiệu dụng: đầu vào + 0,1 × đọc cache + 2 × ghi cache + 5 × đầu ra.

## Theo ngày
| Ngày | Tổng | Trợ lý qua trình duyệt | Phản biện | Làm thật | Viết lời giải | Quay, đo | Luồng chính | Ghi chú |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 04/11 | 331 M | 134 M (41 %) | 61 M (18 %) | 35 M (11 %) | 30 M (9 %) | 23 M (7 %) | ~48 M (14 %) | hết giới hạn phiên 2 lần; luồng chính đọc lại ~515 nghìn token mỗi lần gọi |

## Theo lần hỏi trợ lý (từ 05/11)
| Ngày giờ | Trợ lý | Chủ đề | Bước | Token | Claude tự làm (ước) | Báo anh? |
|---|---|---|---:|---:|---:|---|

Luật: tốn hơn mức Claude tự làm, hoặc hơn 1,5 M, thì báo anh ngay (`README.md` luật 5).
