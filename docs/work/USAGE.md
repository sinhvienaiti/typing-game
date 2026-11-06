# Chi phí token

Đo bằng `python3 tools/agent-usage/usage.py <thư mục phiên> <mốc giờ UTC>`. Đơn vị là token hiệu dụng: đầu vào + 0,1 × đọc cache + 2 × ghi cache + 5 × đầu ra.

## Theo ngày
| Ngày | Tổng | Trợ lý qua trình duyệt | Phản biện | Làm thật | Viết lời giải | Quay, đo | Luồng chính | Ghi chú |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 04/11 | 331 M | 134 M (41 %) | 61 M (18 %) | 35 M (11 %) | 30 M (9 %) | 23 M (7 %) | ~48 M (14 %) | hết giới hạn phiên 2 lần; luồng chính đọc lại ~515 nghìn token mỗi lần gọi |
| 05/11 | 185 M | 34 M (18 %) | 5 M (3 %) | 55 M (30 %) | — | 8 M (4 %) | ~83 M (45 %) | điều phối 151 M + phiên lab 29 M + 5 M; không hết giới hạn phiên; Bash luồng chính 42 M (1.758 lượt × ~63 nghìn) |
| 06/11 | 191 M | 6,5 M (3 %) | 13,7 M (7 %) | 117 M (61 %) | 7,1 M (4 %) | 1,4 M (1 %) | ~52 M (27 %) | điều phối 97 M + 4 phiên lab 94 M; không hết giới hạn phiên; 12 agent phản biện, phiếu 326 qua 3 vòng; từ 22:00 Codex 3 làn |

## Theo lần hỏi trợ lý (từ 05/11)
| Ngày giờ | Trợ lý | Chủ đề | Bước | Token | Claude tự làm (ước) | Báo anh? |
|---|---|---|---:|---:|---:|---|
| 05/11 20:10 | Gemini 4 Argon Cao | 30 kỹ năng mở rộng (diện rộng, pháp tướng, thần thú, pháp bảo) | 3 vòng (FAIL, PASS, PASS) | chưa đo (trước khi nén ngữ cảnh) | — | — |
| 05/11 22:22 | Gemini 4 Argon Cao | D60 bộ đếm chuỗi từ + D61 chiêu duy trì | 3 vòng (FAIL, PASS, PASS), khoảng 17 lượt gọi | ~1,1 M (ước) | ~0,5 M | có, trong rà soát 23:00 (tốn hơn ~0,6 M) |

Luật: tốn hơn mức Claude tự làm, hoặc hơn 1,5 M, thì báo anh ngay (`README.md` luật 5).
