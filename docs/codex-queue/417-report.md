# Phiếu 417 — Mười kiểu dáng dải cut-in trung tính

Ngày: 16/11/2026. Người làm: Codex. Phiếu có phản biện PASS (Sonnet, 16/11).

## Kết quả

Đã gọi **image_gen 16 lần, thành công 16 lần**: mười kiểu trung tính, hai lượt làm lại chém chéo và khói mực, bốn ảnh thử màu. Không gặp giới hạn chờ của công cụ.

Thư mục giao nộp: `games/immortality-cultivation/art-src/concept/cutin-bands/shapes/`.

- 16 PNG, mỗi ảnh **1920×640**, kèm 16 tệp `.prompt.txt` lưu nguyên prompt thực tế và đường dẫn ảnh tham chiếu thực sự đính kèm.
- [Ảnh ghép cutin-shapes-sheet-417.jpg](../../games/immortality-cultivation/art-src/concept/cutin-bands/shapes/cutin-shapes-sheet-417.jpg), **1968×2618**, hai cột, bảy hàng: mười lựa chọn trung tính rồi bốn thử màu, có nhãn tiếng Việt.
- `cutin-shapes-sheet-417.prompt.txt` ghi cách ghép cơ học và lệnh ImageMagick chính xác.

Tên tệp trong bảng dưới có tiền tố `cutin-shape-` và hậu tố `.png`, nằm trong thư mục `shapes/`.

| Ô | Tệp được chọn | Hình dáng | Ảnh 416 dùng làm tham chiếu |
| --- | --- | --- | --- |
| 01 | `vortex.v1-try1` | Xoáy cuộn lệch phải, mắt rỗng, đuôi thấp | `cutin-metal.v1-try1.png` |
| 02 | `slashes.v1-try2` | Bốn tia chém chéo thẳng, tách nhau bằng khoảng đen | `cutin-metal.v1-try1.png` |
| 03 | `waves.v1-try1` | Sóng dâng nhiều tầng, giọt và vân sáng bên trong | `cutin-water.v1-try1.png` |
| 04 | `burst.v1-try1` | Tâm bên phải, chùm tia bung sang trái | `cutin-light.v1-try1.png` |
| 05 | `crystals.v1-try1` | Dòng mảnh pha lê có mặt khúc xạ | `cutin-ice.v1-try1.png` |
| 06 | `ink.v1-try2` | Nét bút rộng, xước khô, thân mực và khói | `cutin-dark.v1-try1.png` |
| 07 | `seal.v1-try1` | Các vòng trận pháp elip nghiêng, lớp cung và điểm sáng | `cutin-metal.v1-try1.png` |
| 08 | `lightning.v1-try1` | Thân sét gãy, nhánh mảnh nhiều cấp | `cutin-thunder.v1-try1.png` |
| 09 | `feathers.v1-try1` | Quạt các phiến lông vũ năng lượng, sợi nhỏ tỏa ra | `cutin-light.v1-try1.png` |
| 10 | `stardust.v1-try1` | Dòng bụi sao hạt mịn và màn khí loãng | `cutin-star.v1-try1.png` |
| 11 | `vortex-fire.v1-try1` | Xoáy đỏ lửa | `cutin-fire.v1-try2.png` |
| 12 | `vortex-ice.v1-try1` | Xoáy xanh băng | `cutin-ice.v1-try2.png` |
| 13 | `crystals-fire.v1-try1` | Pha lê đỏ lửa | `cutin-fire.v1-try2.png` |
| 14 | `crystals-ice.v1-try1` | Pha lê xanh băng | `cutin-ice.v1-try2.png` |

Mọi đường dẫn ảnh 416 trong bảng tính từ `games/immortality-cultivation/art-src/concept/cutin-bands/`. Hai lượt làm lại còn đính kèm try1 tương ứng làm ảnh cần sửa. Bốn thử màu còn đính kèm bản trung tính của chính kiểu đó làm ảnh cần tô. Không dùng ảnh bên thứ ba.

Hai mẫu đầu xoáy và chém chéo đã được xem và hiển thị cho owner trước phần còn lại. Chém chéo try1 còn mềm như lụa; khói mực try1 còn giống sóng cuộn. Try2 làm rõ tia thẳng và thân bút xước. **Giữ nguyên cả hai try1**, không ghi đè hoặc xóa.

## Kiểm tra và điểm cần owner xem

Đã xem từng đầu ra và ảnh ghép: mười dáng phân biệt được, có tầng lõi sáng, thân xám, viền mềm và hạt; vùng giữa-trái nhìn chung tối để ghép nhân vật và tên chiêu. Không thấy người, sinh vật, chữ hay watermark trong ảnh nguồn. Trận pháp là vòng hình học trừu tượng, không có chữ bùa.

Đây là **mẫu nguồn chờ chọn**, chưa phải hiệu ứng hoàn chỉnh đã nghiệm thu trong play host. Không chấm điểm 8.5 cho một lớp riêng và không tuyên bố đã đạt nghiệm thu trong game.

Các sai lệch còn lại được giữ rõ thay vì sửa âm thầm:

- **Nền chưa đen tuyệt đối theo pixel.** Mười lựa chọn trung tính có giá trị kênh lớn nhất ở cột ngoài cùng trái là 1/255; bên phải là 1/255, riêng trận pháp 3/255. Nhìn nền đen nhưng còn sàn sáng rất thấp.
- **Không đạt vùng lề đen hoàn toàn 8% đã yêu cầu trong prompt.** Nhiều chi tiết sáng vẫn nằm trong dải 8% sát mép phải, dù cột biên đã tối. Khi ghép có thể cần thu nhỏ vị trí lớp và một mặt nạ mờ mép; chưa xác nhận đủ lề để đem làm video.
- **Hai bản pha lê thử màu cần xem mép phải:** đỏ lửa còn tối đa 13/255, xanh băng 9/255 ở cột biên. Hai bản xoáy thử màu chỉ 1/255 ở hai cột biên. Bốn thử màu chứng minh hướng màu nhìn được, chưa phải phép tô giữ nguyên từng pixel: image_gen có thay đổi một số hạt và độ sáng.
- **Trung tính theo cảm nhận, chưa xám tuyệt đối về số.** Độ lệch lớn nhất giữa ba kênh tại một pixel của các bản trung tính là 8–20/255. Nên lấy độ sáng làm dữ liệu nguồn khi tô màu, thay vì giữ sắc lệch nhỏ này.

Đã dùng hết 16 lượt được phép, không tạo thêm để xử lý các điểm trên. Owner nên xem toàn bộ ảnh ghép, đặc biệt chém chéo/khói mực try2, dáng trận pháp và mép phải hai thử màu pha lê trước khi chọn nguồn cho bước tiếp theo.

## Cách code nên tô màu

Đề xuất **gradient map hai màu viền/lõi** làm mặc định; nhân màu dùng cho biến thể đồng sắc đơn giản. Đây là hướng dẫn, chưa sửa hoặc thử shader trong phiếu này.

1. Đọc texture theo sRGB, đổi sang linear rồi lấy luminance `L = dot(rgb, (0.2126, 0.7152, 0.0722))`. Cách này loại sắc lệch nhỏ của nguồn trung tính. Trừ sàn đen nhỏ có chuyển tiếp mềm trước khi tô; tránh cộng một màu nền cố định vào mọi pixel.
2. Nhân màu: `C = L × màu_hệ × cường_độ`. Giữ tương phản và chi tiết, đổi được đủ 14 hệ bằng tham số, nhưng lõi sẽ cùng sắc với thân.
3. Gradient hai màu: cho viền/thân mang màu bão hòa, dùng độ sáng để chuyển mềm sang màu lõi nhạt gần trắng. Nhân kết quả gradient với độ sáng nguồn để nền đen vẫn bằng không; không dùng trực tiếp màu viền cho pixel đen. Điều chỉnh ngưỡng chuyển trên vùng lõi sáng, giữ thân có chi tiết.
4. Ví dụ màu sRGB để thử: lửa viền `#C51B30`, lõi `#FFF1CE`; băng viền `#2163D8`, lõi `#E7FCFF`. Chuyển các màu này sang linear trước khi tính. Nếu cần sát thử màu hơn, thêm một điểm trung gian cam hoặc cyan trong bảng gradient; không cần tạo thêm ảnh theo từng hệ.
5. Ghép lớp bằng additive hoặc screen có kiểm soát cường độ, kèm mờ hai đầu theo UV và thu nhỏ lớp nếu cần lề. Chồng 2–3 dáng với tỷ lệ, hướng và thời điểm khác nhau; theo dõi việc mất chi tiết do cộng sáng. Một texture độ sáng mỗi dáng cùng bảng màu hệ là đủ, không cần 140 ảnh.

## Kỹ thuật và phạm vi

Image_gen trả ảnh 2172×724, đúng tỷ lệ 3:1. ImageMagick 7 chỉ giảm đồng tỷ lệ về 1920×640; không cắt, tô màu lại hoặc vẽ sửa PNG. Ảnh gốc của công cụ vẫn ở thư mục mặc định của công cụ. Ảnh ghép chỉ thu nhỏ, sắp ô và thêm nhãn bằng Arial theo phiếu. Đã kiểm tra đủ 16 PNG đúng kích thước và đủ prompt đi kèm, rồi xem ảnh ghép sau khi xuất.

Chỉ ghi thư mục `shapes/` được giao và báo cáo này. Không sửa code, src, scripts, tests hoặc docs của Tu Tiên; không chạy build/test game; không video, âm thanh, tích hợp, đổi nhánh hay thao tác Git thay đổi trạng thái. Không ghi đè ảnh có sẵn. Không mở rộng nghiên cứu hoặc gọi trợ lý vì đây là phiếu sản xuất ảnh từ giải pháp đã có phản biện PASS.

Phần không làm theo phạm vi: không xuất 140 ảnh màu, không viết shader, không tạo video, không ghép nhân vật hoặc đo/chấm hiệu ứng trong game. Các phần đó thuộc bước dùng nguồn sau khi owner chọn; các vấn đề nền/lề nêu trên vẫn cần xử lý trước khi nghiệm thu.
