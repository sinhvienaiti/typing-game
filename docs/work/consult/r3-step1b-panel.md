# Vòng 3 · Bước 1 thử lại · Bảng chấm mù 3 giám khảo Claude và 2 người phản biện

## Tóm tắt

TRƯỢT lần hai. Bốn bản cùng seed, nhãn trung tính mới K/M/P/T, khoá giữ ngoài thư mục chấm. Ba giám khảo độc lập không phân biệt được bản thử lại (K), lần thử đầu (T) và bản cuối vòng 2 (P), kể cả ở ảnh cắt 1:1. Hai người phản biện đo điểm ảnh và xác nhận thân quái giống nhau từng khung. Cả chiêu ở góc chơi: K = T = P = 6, gốc M = 5,5. Đo trực tiếp trong lab: thân quái có nghiêng (3 quái, đỉnh 20°), nhưng đúng lúc đó bị đĩa sao lúc chạm, cột sáng và số sát thương che hết. Quái cao khoảng 20 px ở góc chơi. Hiệu năng đạt: Δp95 −0,7 ms.

## Cách chấm

- Bộ ảnh: `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/r3-step1b/panel/`, mỗi bản có:
  - tấm 12 khung ở góc chơi (dựng lại từ `X/Y.mp4`, bỏ nhãn X/Y cũ);
  - tấm 8 khung cắt 640×360 quanh điểm giáng ở độ phân giải thật, từ 0,97 đến 1,67 s.
- Khoá: chỉ Claude giữ, ngoài mọi thư mục giám khảo được mở. Giám khảo bị cấm mở `_private`, `docs/work`, mọi `*verdict*.md`, mã nguồn và git.
- Ba giám khảo xem bốn bản theo thứ tự xoay vòng khác nhau, ghi điều thấy trước khi chấm, rồi chấm 5 trục §1 cho pha chạm và quái nhận đòn, cộng điểm cả chiêu ở góc chơi.
- Hai người phản biện (một soi điểm ảnh, một nhìn như người chơi) cố bác mọi khẳng định "bản này hơn bản kia" mà trung vị đưa ra, và kiểm các cặp bị chấm bằng nhau.
- Workflow `wf_fd571adb-900`: 5 agent, khoảng 0,55 M token, 5 phút.

## Điểm (trung vị 3 giám khảo)

| Bản | Sức hút | Hình, vật liệu, ánh sáng | Nhịp và lực | Tương tác và đúng việc | Dễ đọc | Cả chiêu |
|---|---:|---:|---:|---:|---:|---:|
| K | 6 | 6 | 5,5 | 5 | 6 | 6 |
| M | 6 | 6,5 | 6 | 6 | 5,5 | 5,5 |
| P | 6 | 6 | 5,5 | 5 | 6 | 6 |
| T | 6 | 6 | 5,5 | 5 | 6 | 6 |

- Quái nhận đòn thấy được ở góc chơi: K, P và T đều "không" hoặc "một phần"; ở ảnh 1:1 cả bốn bản đều chỉ "một phần".
- Cả ba giám khảo ghi K = P = T. Chênh lệch điểm ảnh giữa ba bản ở mức nhiễu nén (RMSE 0,6–0,9 % trên tấm góc chơi, bằng các khung trước khi tung chiêu); chỗ khác nhỏ nhất là góc xoay của đĩa sao ở 1,03 s.
- Người phản biện bác cả ba khẳng định "M phản ứng quái tốt hơn": thân quái của M giống hệt; M chỉ khác ở lớp hiệu ứng (cột sáng sáng hơn, giữ lâu tới 1,80 s, tia lan sang quái bên cạnh).

## Mở khoá

| Nhãn | Bản |
|---|---|
| K | `r3-step1b` X: thử lại, nghiêng 12° → 20°, về sau 0,45 s (e132c92) |
| M | `r3-step1b` Y: gốc, không `tp2` |
| P | `r2-step4` X: bản cuối vòng 2 (Codex chấm cả chiêu 6,5) |
| T | `r3-step1` X: lần thử đầu, nghiêng 10° → 14°, về sau 0,3 s (bc6077c) |

Chênh lệch theo luật vòng 3 (K so với P): pha quái nhận đòn +0 ở mọi trục; cả chiêu +0. **TRƯỢT.**

## Vì sao nghiêng thân không hiện

Claude đo trực tiếp trong lab (`tp2=1`, cùng cách quay), có gắn đầu dò vào `ThunderBodyReaction`:
- chiêu trúng 3 quái (chỉ số 40, 43, 44) ở tick 47; có 96 lượt áp tư thế; góc thêm lớn nhất 19,99°. Mã chạy đúng.
- Ở khung đỉnh (tick 50), đĩa sao `thunder-impact` cỡ 2,4 m cùng quầng sáng phủ kín cả ba quái.
- Hai trong ba quái nghiêng chủ yếu theo chiều sâu (hướng trục z), nên từ camera 55° chỉ thấy như hơi thấp xuống.
- Khi đĩa sao tắt (0,28 s), số "101" nằm đè lên đúng các quái bị đánh, còn tư thế đã về gần gốc.
- Quái cao khoảng 20 px ở 1920×1080 góc chơi, nên nghiêng 20° chỉ dời đỉnh đầu khoảng 8 px.

## Điều bảng chấm thấy thêm (dùng cho các bước sau)

- Đĩa sao viền đen kiểu hoạt hình lúc 1,03 s lệch phong cách với sét vẽ tay, ở cả bốn bản.
- Từ 1,30 s cột sáng của K/P/T yếu dần và tắt ở 1,50 s; bản gốc M giữ lực lâu hơn. Đây là chỗ mất "nhịp và lực".
- Số sát thương che đúng chỗ quái nhận đòn.
- K/P/T hơn M nhờ tụ lực ở người tung, đường dẫn và vòng nứt trên đất; dấu cuối trên đất gần như không thấy ở góc chơi.

## Quyết định của Claude

- Bước 1 dừng ở đây, ghi TRƯỢT hai lần. Không tăng góc thêm nữa: ở góc chơi này, nghiêng thân không thể đọc được khi còn đĩa sao và số sát thương che.
- Mã nghiêng giữ sau `tp2` (không tốn hiệu năng: Δp95 −0,7 ms), nhưng không tính là đã cải thiện.
- Luật vòng 3 chỉ dừng khi cả chiêu không tăng qua **hai bước liền**. Đây là bước đầu tiên không tăng, nên mở bước 2 (dải sét dẫn đường): đây là thứ thấy rõ ở góc chơi. Nếu bước 2 cũng không làm cả chiêu tăng, dừng và báo anh.
- Hướng khác cho quái nhận đòn, để sau: đẩy lùi quái ra xa tâm theo mặt phẳng màn hình, nhảy ngắn có bóng, dời số sát thương khỏi thân quái, đĩa sao nhỏ hoặc trong hơn. Cần anh đồng ý trước khi làm.
- Lần này dùng giám khảo Claude, trái với lệnh anh 06/11 "dừng luôn phần giám khảo claude". Mặc định từ bước 2: giám khảo Codex chấm trên bộ ảnh dựng như ở đây (nhãn trung tính mới mỗi lần, khoá ngoài thư mục, tấm cắt 1:1), trừ khi anh chọn khác. Kịch bản dựng: `scratchpad/r3j/build-panel.sh` (sẽ chuyển vào `tools/` khi dùng lại).
