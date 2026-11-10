# Vì sao VFX của ta tăng chậm: so với video tham khảo của anh (10/11/2026)

## Tóm tắt (≤ 300 từ)

Anh hỏi (10/11): chất lượng VFX có tăng nhưng còn thấp là do chưa làm đúng cách hay do gì; kèm video tham khảo `/Volumes/SS990TPRO/htdocs/refer/vfx.mp4` (chiêu lửa lan tỏa). Claude xem từng khung (tấm khung ở `typing-game-review/captures/tu-tien/ref-vfx-study/`) và đo.

**Kết luận: chủ yếu do chưa làm đúng cách, không phải do thiếu chỉnh.** Năm khác biệt, xếp theo mức ảnh hưởng:

1. **Cỡ trên màn hình.** Chiêu lửa trong video phủ 20–57 % khung hình; Cột Lôi của ta lúc mạnh nhất phủ 2,4 % (bản gốc 3,2 %). Nhân vật của họ cao khoảng 11 % chiều cao khung, của ta khoảng 3 %.
2. **Vật liệu dựng.** Họ dùng lưới 3D (đĩa xoáy trên đất, cột và dải xoắn) với texture vẽ tay chạy liên tục bằng shader, cộng hạt và vệt. Ta ghép thẻ phẳng phát video AI 12 khung/giây: cả năm lớp của Cột Lôi đều là flipbook.
3. **Màu và sáng tối.** Họ có đủ dải: lõi trắng vàng, cam, đỏ, đỏ sẫm gần đen, trên nền đất tối ấm; mặt đất được chiếu sáng cam quanh chiêu. Ta: tím nhạt cộng sáng trên gạch xám, một tông, đất không phản ứng.
4. **Chuyển động.** Mọi lớp của họ xoay, chảy, nở liên tục ở nhiều nhịp (chớp 2–3 khung, bùng 0,3 s, duy trì 1–2 s, tàn lửa); có đẩy camera và nhoè. Lớp của ta chủ yếu hiện rồi mờ.
5. **Quy trình.** Ta chỉnh từng bước nhỏ trên một cái nền chưa có khung đích; người viết mã (Codex) không nhìn thấy kết quả; mỗi vòng mất hàng giờ.

**Đề xuất:** làm thử một chiêu theo cách mới: khung đích anh duyệt → cỡ ≥ 20 % màn hình → lưới + texture vẽ + 3 shader chung → chỉnh trực tiếp trong lab → so với bản cũ. Luật "hình do công cụ vẽ, mã chỉ đặt và làm chuyển động" vẫn giữ: hình dáng đến từ texture vẽ và lưới, shader chỉ làm chúng chuyển động.

## Số đo
| | Video tham khảo | Cột Lôi (hết vòng 3) |
|---|---:|---:|
| Độ phủ khung hình lúc mạnh nhất | 20 % (đĩa lửa vừa hiện) → 57 % (lốc lửa) | 2,35 % (bản gốc 3,18 %) |
| Chiều cao nhân vật so với khung | khoảng 11 % | khoảng 3 % (quái khoảng 2 %) |
| Ngưỡng "có hiệu ứng" trong kịch bản quay của ta | — | ≥ 0,5 % |
| Số lớp là flipbook phẳng | ít (đa số là lưới + shader) | 5/5 |
| Điểm chấm mù cả chiêu | — | 6,5 (bản gốc 5,5–6,0) |

Cách đo: video cắt dải chơi 480×272, so khung có chiêu với khung ngay trước (ngưỡng 12 %); của ta lấy `coverage.peak.share` trong `r3-step3/tp-ab/_private/evidence.json`. Số của video gồm cả chút chuyển động của quái, nên là ước lượng trên.

## Chiêu lửa lan tỏa trong video dựng thế nào (6,3–7,5 s)
1. **Khung 0:** đĩa xoáy đỏ sẫm hiện ngay dưới chân người tung, viền lưỡi liềm vàng kem; ánh cam loang trên đất rộng gấp đôi đĩa.
2. **+0,07–0,13 s:** chớp gai vàng ở tâm; số sát thương nhỏ, nằm phía trên, không che quái.
3. **+0,2 s:** cột lửa dựng lên rồi thành lốc: nhiều dải lửa cong dài (lưới dải, texture chạy dọc), dải gió trắng xoắn quanh, tàn lửa bay, khói bụi ở chân.
4. **Duy trì 1–1,5 s:** đĩa đất vẫn xoáy, đất vẫn sáng cam; rồi tan dần.
5. **Phụ trợ:** nền bản đồ nứt dung nham cùng tông; camera đẩy vào và nhoè ở đòn lớn; các chiêu khác chồng lên (quả cầu mặt trời, tia sao) vẫn đọc được vì mỗi chiêu có hình khối riêng, lớn.

## Vì sao ba vòng Cột Lôi chỉ lên 1 điểm
- Chỉnh lớp trên nền sai: video nguồn có lớp trụ, một tia mỏng, vết tím (anh chỉ ra 07/11).
- Hiệu ứng quá nhỏ: phản ứng quái 20 px, vết đất vài chục px; giám khảo không thấy khác biệt.
- Thẻ phẳng không có khối: nhìn từ camera 55° chúng nằm bẹp hoặc dựng như tấm bìa.
- Vòng lặp chậm và mù: phiếu → Codex viết không nhìn → quay → chấm; mỗi vòng 30–90 phút, chấm bằng 12 khung tĩnh.

## Cách làm đề xuất (thử trên một chiêu trước)
1. **Khung đích:** một ảnh cả chiêu ở đúng camera chơi, vẽ đè lên ảnh chụp lab (công cụ vẽ của ta, ảnh tham chiếu của ta); anh duyệt trước khi dựng.
2. **Cỡ:** chiêu nặng phủ ≥ 20 % khung hình lúc mạnh nhất. Chọn một trong hai: camera chiến đấu gần hơn, hoặc phóng to hiệu ứng so với nhân vật. Việc này anh quyết.
3. **Bộ dựng:** vài lưới chung (đĩa, vành, nón, trụ, dải xoắn, bán cầu) + texture vẽ (vệt lửa/sét, xoáy, nhiễu, mặt nạ nứt) + 3 shader chung (chạy texture có ăn mòn và méo; đèn loang trên đất; vệt). Flipbook từ video chỉ còn là lớp phụ (tàn lửa, khói).
4. **Màu:** bảng 4–5 nấc có nấc tối bão hoà; đất được chiếu sáng; không chỉ cộng sáng.
5. **Nhịp:** báo trước ngắn → bùng → duy trì có chuyển động → tàn; kèm rung, đẩy camera và nhoè ở đòn lớn.
6. **Vòng lặp nhanh:** bảng chỉnh trong lab (thanh trượt cỡ, tốc độ, màu, thời gian) để người chỉnh nhìn ngay; quay clip 60 khung/giây cho anh.
7. **So sánh:** bản mới và bản cũ cạnh nhau, Codex chấm trên bộ ảnh nhãn mới; đạt thì mới áp dụng cho các chiêu khác.

## Giới hạn cần nói thẳng
- Cách này là cách các game thương mại làm, nhưng tay nghề chỉnh VFX của agent còn yếu; kỳ vọng thực tế cho lần thử đầu là 7–8, chưa chắc 8,5.
- Một bộ texture VFX phong cách hoá mua sẵn (giấy phép thương mại) sẽ rút ngắn nhiều; việc mua là của anh.
- Video tham khảo là của bên thứ ba: chỉ để học cách dựng, không đưa vào công cụ AI.
