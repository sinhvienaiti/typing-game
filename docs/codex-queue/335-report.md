# Phiếu 335 · Ngũ Lôi Oanh Đỉnh

Đã tạo đủ 5 ảnh pha và prompt nguyên văn bằng `image_gen`; dùng 6/10 lượt sinh ảnh, 10/10 lượt `view_image`. Một lần vẽ lại vành sốc. Không sửa mã, file có sẵn, chạy build/test hay lệnh Git ghi.

`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.

Tấm duyệt: [thunder-five-335-sheet.jpg](../../games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/thunder-five-335-sheet.jpg), 1920×1336, gồm ảnh gốc và 5 bản chọn, có tên pha.

## Tự chấm bản chọn

Tên dưới đây đều nằm trong `S`. Điểm cuối lấy **tiêu chí thấp nhất**, không lấy trung bình. “Góc/nền/chữ” gồm góc nhìn, nền đen và không chữ. Đây là tự chấm ảnh nguồn theo phiếu, chưa phải nghiệm thu hiệu ứng ghép trong game hay chấm mù độc lập.

| Ảnh được chọn | Đọc ngay | Cuốn hút, sang | Cùng bộ | Góc/nền/chữ | Khung đầu video | Điểm cuối | Lề trái/phải/trên/dưới (%) | Vẽ lại | Nhận xét |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| `thunder-five-cloud-vortex-top.v1-try1.png` | 9,0 | 8,8 | 9,0 | 8,8 | 9,0 | **8,8** | 10,05 / 10,21 / 9,65 / 12,28 | Không | Mây nhiều lớp, năm mầm sét rõ và tâm rỗng; sáng mạnh ở vành trong. |
| `thunder-five-caster-seal.v1-try1-pad.png` | 9,2 | 8,6 | 9,0 | 9,2 | 8,8 | **8,6** | 13,47 / 11,87 / 13,40 / 15,47 | Không | Năm ký hiệu sét đọc rõ; bố cục khá đều, cần video làm sống phần tia ngắn. |
| `thunder-five-impact-burst.v1-try1-pad.png` | 9,0 | 8,7 | 9,1 | 9,0 | 8,7 | **8,7** | 9,67 / 10,07 / 17,40 / 20,47 | Không | Năm nhánh lớn, đá văng và vành sốc rõ; lõi chạm hơi sáng đặc. |
| `thunder-five-shock-ring-top.v1-try2.png` | 8,9 | 8,6 | 8,9 | 8,7 | 9,0 | **8,6** | 10,61 / 11,32 / 8,53 / 13,80 | Có | Vòng mảnh tròn hơn bản đầu, tâm đen rộng để ghép dấu nứt; năm nút điện còn khá đều. |
| `thunder-five-lingering-arcs.v1-try1-pad.png` | 8,9 | 8,4 | 8,7 | 9,2 | 8,8 | **8,4** | 9,29 / 10,83 / 19,15 / 29,31 | Không | Cung điện thấp và khói mỏng đúng dư âm; độ rực giảm có chủ đích. |

Vành sốc `thunder-five-shock-ring-top.v1-try1.png` giữ lại: điểm lần lượt **8,9 / 8,5 / 9,0 / 7,7 / 8,2**, cuối **7,7** vì vòng hơi bẹt; lề **7,81 / 7,89 / 6,70 / 12,20%**. Chọn `try2` cao hơn, không vẽ lần ba.

## Kiểm tra và file phụ

- Đo bằng ImageMagick 7: vùng hiệu ứng là pixel có kênh RGB lớn nhất > 3/255; bỏ nhiễu nền ≤ 3/255. Đo nền bằng cực đại RGB trong ô 32×32 ở mỗi góc. Các bản chọn đều có lề ≥ 6%; bốn góc tối đa 0–2/255, gần đen thuần.
- Ảnh sinh vuông: 1254×1254. Ấn thi triển gốc có lề phải 4,39%; vụ nổ gốc có lề trái/phải 1,75/2,23%. Giữ nguyên hai file gốc, thêm bản `-pad.png` 1500×1500 bằng `magick -extent`, không đổi pixel tranh.
- Dư âm gốc 1672×941; thêm `-pad.png` 1680×945 để đúng 16:9, chỉ đệm 8 px ngang và 4 px dọc. Bản gốc vẫn giữ nguyên.
- Tổng cộng thêm 6 ảnh sinh, 3 ảnh đệm và 9 file `.prompt.txt` tương ứng; mỗi prompt ghi công cụ, đường dẫn tham chiếu, nguyên văn và khổ thật. Bản đệm ghi thêm thao tác hậu xử lý. Mọi lần sinh đều dùng `thunder-five-strike.v1-try1.png`; hai lần vẽ vành sốc dùng thêm `thunder-scorch-crack-top.v1-try1.png`.
- Không bỏ pha nào. Video Firefly và tích hợp game nằm ngoài phiếu. Anh xem tấm ghép, nhất là vòng `try2` và độ dịu của dư âm; dùng các bản chọn trong bảng cho bước video.
