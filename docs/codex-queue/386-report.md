# Phiếu 386 — Ảnh tham chiếu tuyệt kỹ băng

Ngày 16/11/2026. Đã tạo **8 ảnh PNG bằng đúng 8/8 lần `image_gen`**, bao phủ hai khoảnh khắc và bốn loại bảng thành phần; hai lượt bổ sung dành cho cụm tinh thể và mặt băng. Tất cả PNG có kích thước **1536×1024**, được giữ nguyên từ công cụ, có prompt thật bên cạnh. Đã tạo ảnh ghép mọi bản. **Đây là bộ phương án để owner xem; một số yêu cầu kỹ thuật chưa đạt, liệt kê bên dưới. Không phải kết quả nghiệm thu.**

## File giao nộp

Thư mục ảnh: `games/immortality-cultivation/art-src/concept/ult-ice/`. Các liên kết dưới đây tính từ báo cáo này.

| Lượt | Ảnh | Prompt thật đã dùng | Nội dung |
| --- | --- | --- | --- |
| 1 | [ult-ice-moment-a.v1-try1.png](../../games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-moment-a.v1-try1.png) | [Prompt A](../../games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-moment-a.v1-try1.prompt.txt) | Khoảnh khắc chiêu, sân đá xám phủ băng trong, các cụm cao thấp và tâm sáng. |
| 2 | [ult-ice-moment-b.v1-try1.png](../../games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-moment-b.v1-try1.png) | [Prompt B](../../games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-moment-b.v1-try1.prompt.txt) | Khoảnh khắc dày hơn, nhiều tinh thể, sương và mảnh băng lơ lửng. |
| 3 | [ult-ice-crystal-clusters.v1-try1.png](../../games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-crystal-clusters.v1-try1.png) | [Prompt cụm, lần 1](../../games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-crystal-clusters.v1-try1.prompt.txt) | Bốn biến thể cụm tinh thể, một cụm mỗi ô. Lề quá hẹp. |
| 4 | [ult-ice-shards-sparkle.v1-try1.png](../../games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-shards-sparkle.v1-try1.png) | [Prompt mảnh và bụi](../../games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-shards-sparkle.v1-try1.prompt.txt) | Sáu ô: ba mảnh băng, bụi băng, bụi lấp lánh và một hạt lóe. |
| 5 | [ult-ice-cracked-surface.v1-try1.png](../../games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-cracked-surface.v1-try1.png) | [Prompt mặt băng, lần 1](../../games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-cracked-surface.v1-try1.prompt.txt) | Mặt băng nứt nhìn từ trên xuống, còn giống nhiều mảnh nổi và thiếu lề trên. |
| 6 | [ult-ice-round-shell.v1-try1.png](../../games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-round-shell.v1-try1.png) | [Prompt vỏ băng](../../games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-round-shell.v1-try1.prompt.txt) | Vỏ băng ôm khối cầu xám trung tính, hai ô góc ngang và góc trên theo prompt. |
| 7 | [ult-ice-crystal-clusters.v1-try2.png](../../games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-crystal-clusters.v1-try2.png) | [Prompt cụm, lần 2](../../games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-crystal-clusters.v1-try2.prompt.txt) | Thu nhỏ và đặt lại bốn cụm, sửa lề. |
| 8 | [ult-ice-cracked-surface.v1-try2.png](../../games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-cracked-surface.v1-try2.png) | [Prompt mặt băng, lần 2](../../games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-cracked-surface.v1-try2.prompt.txt) | Mặt băng phẳng hơn, ô vuông và lề tốt hơn; chưa bảo đảm tile kín. |

- [ult-ice-sheet-386.jpg](../../games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-sheet-386.jpg): ảnh ghép **1600×2284**, khoảng **1,25 MB**, hai cột và bốn hàng, chứa đủ tám bản với tên file.
- [ult-ice-sheet-386.prompt.txt](../../games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-sheet-386.prompt.txt): ghi lệnh ImageMagick thực tế dùng để ghép, không giả làm prompt sinh ảnh. Chỉ ảnh ghép có nhãn tên file; tám PNG nguồn không có chữ.

## Tham chiếu và cách làm

Đã xem trực tiếp và truyền đủ ba ảnh sau vào **mọi lần gọi công cụ**; mỗi prompt cũng ghi nguyên đường dẫn tuyệt đối và vai trò:

1. `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/lab/vfx/ice/ice-ground-mark.atlas.png`: cấu trúc mặt băng nứt, viền lạnh và bảng màu xanh trắng.
2. `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/lab/vfx/ice/ice-big-burst.atlas.png`: mặt cắt kim cương, độ trong và cụm đầu nhọn.
3. `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/clip-content-audit/ult__ult-ice-cold-silence.jpg`: chỉ mật độ tinh thể, ánh sáng, chất băng và quy mô. Prompt loại bỏ sinh vật, tượng và hình người của nguồn bị loại.

Lượt 7 nhận thêm PNG cụm lần 1 làm ảnh cần sửa bố cục; lượt 8 nhận thêm PNG mặt băng lần 1 làm ảnh cần sửa. Không đưa ảnh bên thứ ba vào công cụ. Hai ảnh khoảnh khắc đầu được xem và hiển thị cho owner trước khi làm các bảng thành phần. Các bản tiếp theo cũng được hiển thị ngay khi công cụ trả về.

Prompt gốc viết bằng tiếng Anh để điều khiển công cụ; các file liên kết ở bảng trên lưu nguyên văn, gồm cả tham chiếu, góc máy, vật liệu, bố cục, ánh sáng và ràng buộc. Không cắt, vẽ lại, đổi màu hoặc ghi đè PNG. ImageMagick chỉ dùng để kiểm ảnh và tạo ảnh ghép.

## Ý kiến Codex, không phải điểm duyệt

**Chọn `ult-ice-moment-a.v1-try1.png` làm phương án tham chiếu tổng thể tốt nhất trong lượt này.** Tâm sáng dễ nhận, nền đá vẫn đọc được qua băng, các cụm cao thấp có khoảng thở, vết nứt và sương nối các cụm thành một vùng chiêu. Vật liệu có cạnh sắc, lõi xanh và ánh khúc xạ nhiều lớp; không thấy sinh vật, tượng hoặc hình người.

Mẫu B mạnh hơn về mật độ và cảm giác hoành tráng, gần phần owner thích ở video cũ hơn. Tuy vậy, hình bị chật ở mép trên, ánh sáng mặt sân hơi dày và phân cấp tâm kém rõ hơn A. Owner nên đối chiếu hai mẫu ở hàng đầu ảnh ghép để chọn mức mật độ mong muốn; chưa lấy mẫu nào làm nguồn dựng tiếp.

Trong bảng thành phần, **cụm tinh thể lần 2** phù hợp bố cục nhất: bốn dáng riêng, thấy trọn đầu nhọn và có lề rộng. Bản lần 1 giúp xem chi tiết lớn hơn nhưng không đạt lề. **Mặt băng lần 2** hợp vai lớp phủ hơn lần 1 vì bề mặt phẳng, ít cảm giác đá vụn xếp lên nhau. Vỏ băng đã cho thấy khối cầu xám qua lớp băng trong; góc trên và độ nhất quán giữa hai mặt vẫn cần owner xem trước khi dùng làm nguồn dựng.

## Kiểm tra và phần chưa đạt

Đã kiểm kích thước tám PNG và sự tồn tại của tám file prompt tương ứng; tất cả đều đúng 1536×1024 và đủ prompt. Đã mở xem ảnh ghép sau khi tạo. Không thấy chữ, watermark hoặc sinh vật trong tám bản.

Đo lề ngoài theo hộp bao pixel có kênh RGB lớn hơn 8/255 để bỏ nhiễu tối; đây là số đo lề toàn ảnh, không thay cho kiểm từng ô. Các góc ảnh bảng thành phần đều có RGB(0,0,0); phép đo này không xác nhận mọi pixel nền đều tuyệt đối bằng 0.

| Bảng | Trái / trên / phải / dưới | So với lề ngoài 8% |
| --- | --- | --- |
| Cụm tinh thể lần 1 | 8,85 / 1,66 / 3,97 / 4,49% | Chưa đạt. |
| Cụm tinh thể lần 2 | 20,77 / 14,65 / 17,19 / 19,82% | Đạt lề ngoài; khoảng trống từng ô cũng rộng khi xem ảnh. |
| Mảnh vỡ và bụi | 3,39 / 3,71 / 11,39 / 7,81% | Chưa đạt; mảnh dài và bụi gần biên. |
| Mặt băng lần 1 | 21,74 / 6,15 / 21,68 / 8,79% | Chưa đạt lề trên. |
| Mặt băng lần 2 | 25,00 / 11,91 / 24,93 / 12,99% | Đạt lề ngoài. |
| Vỏ băng | 2,67 / 11,13 / 3,26 / 16,99% | Chưa đạt lề ngang. |

**Yêu cầu texture tile được chưa hoàn tất.** Ô mặt băng lần 2 gần đúng kích thước yêu cầu: hộp bao đo được 769×769 pixel, gồm cả viền chuyển tiếp. Đối chiếu hai cạnh đối diện của hộp bao cho sai khác RGB trung bình khoảng 39,69/255 theo chiều ngang và 23,58/255 theo chiều dọc. Các vết nứt chưa được chứng minh nối kín; không coi đây là texture seamless sẵn dùng. Bản lần 1 cũng chưa đạt yêu cầu này.

Đã dành hai lượt cuối sửa cụm tinh thể và mặt băng. Dừng sinh ảnh ở **8/8** theo trần phiếu, không mở lượt thứ 9 để sửa lề bảng mảnh/vỏ hoặc tiếp tục sửa seam. Vì vậy bộ ảnh có đủ loại phương án nhưng **chưa đáp ứng trọn vẹn lề và tile**. Đây là các phần còn thiếu của phiếu, không đánh dấu đạt tạm và không tự chấm nghiệm thu.

## Phạm vi và việc owner cần xem

Chỉ tạo file trong thư mục concept được chỉ định và báo cáo này. Không sửa code, script, test hoặc docs của Tu Tiên; không tạo video/âm thanh, không chạy build/bộ test game, không đổi nhánh, stage media, commit, push hoặc xoá ảnh cũ. Không sửa thư mục review hay chỉ mục ngoài phạm vi phiếu. Không dựng lab hoặc tích hợp vào game trong lượt này.

Owner cần chọn hướng khoảnh khắc A hay B, xem bốn dáng cụm ở bản lần 2 và mức dày của vỏ băng. Các lỗi lề bảng mảnh/vỏ và seam mặt băng cần được sửa trước khi dùng làm bộ thành phần hoàn chỉnh. Chưa có hành động dựng tiếp dựa trên các ảnh này.
