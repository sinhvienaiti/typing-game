# Phiếu 355 · Bộ Lôi D65 vòng 2

Ngày thực hiện: 12/11/2026, sau khi phiếu 354 đã có báo cáo. Công cụ: **image_gen tích hợp**, **11/12 lượt**, gồm tám ảnh đầu và **3/3 lượt vẽ lại**. **view_image: 12/14 lượt**, gồm mười tham chiếu và hai lần xem tấm ghép.

**Đã tạo đủ tệp trong phạm vi; bộ ảnh chưa đạt toàn bộ yêu cầu kỹ thuật.** Lõi trắng nóng, nhánh và lực đòn tăng rõ so với v3, nhưng các bản đầu quá sát mép; bản sửa đòn kết và mây lại thu quá nhỏ. Nền còn nhiễu 1–3/255 ở góc. Không ghi PASS, không tích hợp vào game.

## Tệp bàn giao

S = `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.

- **11 PNG + 11 prompt nguyên văn**: tám tên chủ đề `v4-try1` trong bảng số; ba bản sửa `thunder-five-strike.v4-try2`, `thunder-single-bolt-d.v4-try2`, `thunder-five-cloud-ink.v4-try2`. Mỗi PNG có tệp cùng tên gốc đuôi `.prompt.txt`, ghi đường dẫn và vai trò từng tham chiếu.
- [Tấm ghép thunder-v4-355-sheet.jpg](../../games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/thunder-v4-355-sheet.jpg), **2560 × 1800**. Hàng trên: tám v4; hàng giữa: v3 cùng chủ đề; hàng cuối: ba bản khác của đòn kết, D và mây. Nhãn ghi đúng try.
- Hàng trên dùng đòn kết try1, A/B/C try1, D try2, vụ nổ/tia sót try1, mây try2. Đây là các bản **đưa ra so sánh**, không phải bản đã nghiệm thu. Đòn kết try1 giữ cỡ/lực tốt hơn try2; D try2 đạt cỡ dọc và màu nhưng hẹp ngang; mây try2 gần cỡ riêng hơn try1 nhưng còn nhỏ và thiếu điểm nóng.

**Bỏ qua vành sốc v4 đúng điều kiện của phiếu:** `thunder-five-shock-ring-top.v3-try1.png` đo ở V > 0,12 có hộp bao (172,151)–(1069,1032), phủ **71,611% ngang × 70,335% dọc**, đều ≥ 60%. Giữ nguyên vành v3 và ấn tay v3, không vẽ lại.

Các PNG là bản sao nguyên vẹn đầu ra công cụ: kiểm SHA-256 **11/11 cặp trùng** với ảnh gốc trong thư mục generated_images. Không hậu kỳ màu, nền, lề hay hình bằng mã. ImageMagick chỉ đọc số và làm tấm ghép, dùng Arial đúng đường dẫn máy Mac.

## Tham chiếu và phương pháp

Dùng bản chọn của phiếu 353: đòn kết/B/C v3-try2; A/D/vụ nổ/tia sót/mây/vành v3-try1. Đã xem đủ chín ảnh này và `thunder-five-strike.v2-try9.png`. V2 chỉ cấp cỡ và lực lõi cho đòn kết; không lấy màu xanh hay thân plasma. Ba lượt sửa dùng bản v4 đầu tương ứng cùng bản v3 cùng tên. Không dùng ảnh bên ngoài repo.

Thực hiện phiếu đã chốt, giữ hướng mỹ thuật D65; không mở nghiên cứu, trợ lý hay vòng duyệt thiết kế mới. Chọn tranh tĩnh bằng image_gen theo yêu cầu trực tiếp, phù hợp nhánh “painted bolt sheets” của skill VFX. Hai mẫu đầu đã xem và hiển thị cho chủ nhân trước phần còn lại. Không tạo chuyển động.

## Phép đo

Đọc RGB 8-bit bằng ImageMagick 7; HSV bằng `colorsys.rgb_to_hsv`; V = max(R,G,B)/255. Mọi phép đo trên PNG gốc, không trên JPEG.

- Hộp bao: **mọi điểm V > 0,12**; tọa độ tính từ 0, gồm hai biên. Lề theo **trái / trên / phải / dưới**, yêu cầu 6–12% mỗi cạnh. Phủ khung theo **ngang / dọc**.
- Điểm nóng: số điểm **V > 0,9 / diện tích hộp bao**, yêu cầu ≥ 4%.
- Màu đúng phép đo phiếu 353: mẫu số là số điểm **V > 0,35**; xanh/tím H = **190–300°**, **không lọc S**; vàng kim sáng H = **45–60°**, S > 0,8, V > 0,85. Giới hạn lần lượt ≤ 2% và ≤ 5%.
- Yêu cầu riêng của mây 70% ngang × 40% dọc mâu thuẫn với lề chung 6–12%: prompt ưu tiên kích thước riêng cho mây. Bảng vẫn ghi nguyên số đo, **không tự miễn điều kiện độ sáng hoặc coi mây đạt lề chung**.
- Số nóng chứng minh có vùng sáng thực, không chứng minh thân lõi dày đúng 1,5–2 lần: thay đổi cỡ toàn ảnh làm phép so bề rộng không còn trực tiếp. Hệ số dày được yêu cầu trong prompt, chưa được xác nhận bằng đo mặt cắt.

| Tệp trong S | Kích thước | Hộp bao x0/y0/x1/y1 | Lề T/Tr/P/D % | Phủ ngang/dọc % | Nóng % | Xanh/tím % | Vàng sáng % |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| `thunder-five-cloud-ink.v4-try1.png` | 1672 × 941 | 55 / 205 / 1630 / 724 | 3.289 / 21.785 / 2.452 / 22.954 | 94.258 / 55.26 | 3.2432 | 2.1477 | 0.0000 |
| `thunder-five-cloud-ink.v4-try2.png` | 1672 × 941 | 306 / 304 / 1348 / 626 | 18.301 / 32.306 / 19.318 / 33.369 | 62.38 / 34.325 | 0.8807 | 1.0135 | 0.0000 |
| `thunder-five-impact-burst.v4-try1.png` | 1254 × 1254 | 54 / 42 / 1195 / 1197 | 4.306 / 3.349 / 4.625 / 4.466 | 91.069 / 92.185 | 16.5774 | 3.5652 | 0.0000 |
| `thunder-five-lingering-arcs.v4-try1.png` | 1671 × 941 | 40 / 26 / 1624 / 887 | 2.394 / 2.763 / 2.753 / 5.632 | 94.853 / 91.605 | 8.9591 | 3.8634 | 0.0000 |
| `thunder-five-strike.v4-try1.png` | 941 × 1671 | 35 / 103 / 905 / 1567 | 3.719 / 6.164 / 3.719 / 6.164 | 92.561 / 87.672 | 21.0904 | 2.4253 | 0.0000 |
| `thunder-five-strike.v4-try2.png` | 941 × 1672 | 115 / 234 / 828 / 1422 | 12.221 / 13.995 / 11.902 / 14.892 | 75.877 / 71.112 | 18.1927 | 0.3298 | 0.0000 |
| `thunder-single-bolt-a.v4-try1.png` | 941 × 1672 | 64 / 73 / 880 / 1598 | 6.801 / 4.366 / 6.376 / 4.366 | 86.823 / 91.268 | 10.0031 | 1.4008 | 0.0000 |
| `thunder-single-bolt-b.v4-try1.png` | 941 × 1671 | 25 / 64 / 907 / 1623 | 2.657 / 3.83 / 3.507 / 2.813 | 93.836 / 93.357 | 9.2709 | 4.9676 | 0.0000 |
| `thunder-single-bolt-c.v4-try1.png` | 941 × 1672 | 30 / 64 / 908 / 1556 | 3.188 / 3.828 / 3.401 / 6.878 | 93.411 / 89.294 | 7.8435 | 7.1246 | 0.0000 |
| `thunder-single-bolt-d.v4-try1.png` | 941 × 1672 | 36 / 56 / 898 / 1647 | 3.826 / 3.349 / 4.463 / 1.435 | 91.711 / 95.215 | 9.0643 | 6.3789 | 0.0000 |
| `thunder-single-bolt-d.v4-try2.png` | 941 × 1672 | 164 / 163 / 764 / 1500 | 17.428 / 9.749 / 18.704 / 10.227 | 63.868 / 80.024 | 5.1639 | 0.7926 | 0.0000 |

**Kết quả:** 0/11 đạt đồng thời bốn lề 6–12%; 9/11 đạt điểm nóng ≥ 4% (hai bản mây chưa đạt); 4/11 đạt ngưỡng xanh/tím (A try1, đòn kết try2, D try2, mây try2); 11/11 đạt ngưỡng vàng sáng. Trong năm chủ đề đòn kết và tia đơn, chỉ đòn kết try1, C try1 và D try2 đạt chiều cao 80–90%; cả ba vẫn lỗi lề hoặc màu.

Các điểm bị tính xanh/tím chủ yếu gần trắng: 96–99% số điểm này có S ≤ 0,03, S cao nhất từng ảnh chỉ 0,040–0,071. Vì phép đo phiếu 353 **không có ngưỡng S**, vẫn ghi lỗi màu theo đúng số; không thay mẫu số hay loại các điểm này để lấy PASS.

### Nền

Bốn pixel góc theo TL / TR / BL / BR; cột cuối là max kênh trong bốn ô góc 10% khung.

| Tệp | RGB bốn góc | Max ô góc, /255 |
| --- | --- | ---: |
| `thunder-five-cloud-ink.v4-try1.png` | (0,0,0) / (0,0,0) / (0,1,0) / (0,1,0) | 1 |
| `thunder-five-cloud-ink.v4-try2.png` | (1,0,0) / (0,0,0) / (0,1,0) / (0,1,0) | 1 |
| `thunder-five-impact-burst.v4-try1.png` | (0,0,0) / (0,0,0) / (1,3,1) / (0,1,1) | 243 |
| `thunder-five-lingering-arcs.v4-try1.png` | (0,0,0) / (0,0,0) / (1,1,1) / (0,1,0) | 3 |
| `thunder-five-strike.v4-try1.png` | (1,0,0) / (0,0,0) / (1,2,1) / (0,1,0) | 255 |
| `thunder-five-strike.v4-try2.png` | (0,0,0) / (0,0,0) / (1,2,1) / (0,1,0) | 2 |
| `thunder-single-bolt-a.v4-try1.png` | (0,0,0) / (0,0,0) / (1,2,1) / (0,1,0) | 2 |
| `thunder-single-bolt-b.v4-try1.png` | (1,0,0) / (0,0,0) / (1,2,1) / (0,1,0) | 255 |
| `thunder-single-bolt-c.v4-try1.png` | (1,0,0) / (0,0,0) / (1,2,1) / (0,1,0) | 182 |
| `thunder-single-bolt-d.v4-try1.png` | (0,0,0) / (0,0,0) / (1,2,1) / (0,1,0) | 166 |
| `thunder-single-bolt-d.v4-try2.png` | (0,0,0) / (0,0,0) / (1,1,0) / (0,1,0) | 1 |

**0/11 đạt nền đen tuyệt đối ở đủ bốn pixel góc.** Max ô góc cao ở một số bản do nhánh/hạt nằm trong ô 10%, không chỉ nhiễu nền; không dùng cột này để gán mọi điểm sáng là nhiễu. Không xoá nhiễu hay làm đen PNG bằng mã.

## Tự chấm theo mặt yếu nhất

Điểm nguồn ảnh theo phiếu, không phải điểm hai giám khảo hay nghiệm thu hiệu ứng trong play host. Cột “lực và cỡ” xét cả lực lẫn bố cục; “kiểu và màu” giữ lỗi màu đo được. Điểm cuối là giá trị thấp nhất.

| Bản | Lực và cỡ | Kiểu và màu | Sang | Cùng bộ | Khung đầu | Thấp nhất |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Đòn kết try1 | 7,7 | 7,9 | 8,5 | 8,5 | 7,8 | **7,7** |
| Đòn kết try2 | 7,5 | 8,5 | 8,4 | 8,4 | 7,6 | **7,5** |
| A try1 | 7,8 | 8,4 | 8,3 | 8,5 | 7,8 | **7,8** |
| B try1 | 7,4 | 7,7 | 8,3 | 8,4 | 7,5 | **7,4** |
| C try1 | 7,5 | 7,6 | 8,2 | 8,4 | 7,6 | **7,5** |
| D try1 | 7,1 | 7,6 | 8,2 | 8,4 | 7,2 | **7,1** |
| D try2 | 7,7 | 8,5 | 8,2 | 8,4 | 7,8 | **7,7** |
| Vụ nổ try1 | 7,5 | 7,8 | 8,5 | 8,5 | 7,6 | **7,5** |
| Tia sót try1 | 7,3 | 7,8 | 8,2 | 8,4 | 7,4 | **7,3** |
| Mây try1 | 6,9 | 7,9 | 8,2 | 8,2 | 7,0 | **6,9** |
| Mây try2 | 7,5 | 8,4 | 8,1 | 8,3 | 7,4 | **7,4** |

Đòn kết giữ năm thân rõ, hội một điểm, mây trên dày có khối; try1 đạt lực nhưng vượt bề ngang, try2 giảm sắc lạnh tốt nhưng chỉ cao 71,112%. B giữ chẻ đôi nửa dưới, C giữ ba nhánh phụ dài; D có hai vệ tinh, try2 cao 80,024% nhưng chỉ rộng 63,868%. Vụ nổ có năm nhánh, đá văng và vành sốc rõ. Tia sót mạnh lên nhưng nhánh cao, cần chủ nhân xem vai trò aftermath. Mây có khối cuộn tốt hơn v3; try1 quá rộng, try2 chỉ 62,380% × 34,325%, dưới mục tiêu 70% × 40%.

Đã vẽ lại một lần cho **đòn kết, D và mây**, ưu tiên chủ thể chính, tia có lề dưới kém nhất và lớp mây sai cỡ nhiều nhất. Những bản còn lại dưới 8 **chưa được vẽ lại** vì đã hết ngân sách **ba lượt sửa**; không dùng lượt tổng còn dư để vượt cấu trúc “9 ảnh + 3 vẽ lại”. Đây là phần chưa đạt, không phải đã bỏ qua có chấp thuận.

## Chủ nhân cần xem và phần không làm

Xem tấm ghép để chọn giữa lực/cỡ try1 và độ thu gọn của try2 ở đòn kết, kiểm mây đã đủ khối và tia sót còn hợp pha kết thúc hay chưa. **Chưa có bản nào đủ mọi điều kiện để chuyển thẳng sang video.**

Không sửa mã, tệp có sẵn trước phiếu, game docs, manifest hoặc công cụ; không chạy build/test, không mở cổng, không ghi Git, không tạo âm thanh, video hay tích hợp runtime. Chỉ thêm PNG/prompt v4, tấm ghép được chỉ định và báo cáo này. Tấm ghép của chính phiếu được chỉnh lại bố cục trong quá trình kiểm.

Không có HTTP 429 hay giờ reset do image_gen cung cấp. Đã kết thúc ngân sách ba lượt vẽ lại của phiếu; không tự gọi thêm trong lần chạy tiếp mà không có phạm vi bổ sung. Các lỗi kỹ thuật ở trên vẫn là việc chưa hoàn thành về chất lượng.

