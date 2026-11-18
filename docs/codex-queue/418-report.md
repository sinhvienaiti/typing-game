# Phiếu 418 — 10 ảnh tĩnh nguồn góc nhìn 55°

Ngày thực hiện: 16/11/2026. Phản biện của phiếu: PASS (Sonnet, vòng 2).
Trạng thái: đã giao đủ 10 ảnh nguồn để owner duyệt; chưa nghiệm thu hiệu ứng tổng hợp trong game.

## Đã làm

- Dùng công cụ tích hợp `image_gen`: **10/14 lượt**, mỗi clip một ảnh `v1-try1`.
- 10 PNG giao đều **1024×1024**, nền đen đặc, có prompt thực tế cạnh ảnh dưới tên `<clip>.v1-try1.prompt.txt`.
- Hai mẫu đầu `dark-ring-burst` và `water-ring-burst` đã được xem và hiển thị cho owner trước tám ảnh còn lại.
- Các vòng có hình bầu dục nằm ngang, mép trước có chiều dày; khói và tia lệch hướng, có điểm phát ở vùng giữa-dưới. Không vẽ mặt đất, vết cháy, sinh vật hay chữ vào ảnh nguồn.
- Đã xem bảng ghép đầy đủ. Góc khoảng 55° là mục tiêu tạo ảnh và đối chiếu phối cảnh bằng mắt với ảnh tham chiếu; không phải kết quả đo camera 3D.

Gốc đường dẫn của bảng sau: `games/immortality-cultivation/art-src/lab/vfx/`.

| Clip | Ảnh giao |
| --- | --- |
| `dark-ring-burst` | `dark/stills-55/dark-ring-burst.v1-try1.png` |
| `water-ring-burst` | `water/stills-55/water-ring-burst.v1-try1.png` |
| `poison-big-burst` | `poison/stills-55/poison-big-burst.v1-try1.png` |
| `poison-ring-burst` | `poison/stills-55/poison-ring-burst.v1-try1.png` |
| `blood-big-burst` | `blood/stills-55/blood-big-burst.v1-try1.png` |
| `wood-big-burst` | `wood/stills-55/wood-big-burst.v1-try1.png` |
| `dark-big-burst-white` | `dark/stills-55/dark-big-burst-white.v1-try1.png` |
| `dark-ground-impact-white` | `dark/stills-55/dark-ground-impact-white.v1-try1.png` |
| `thunder-impact` | `thunder/stills-55/thunder-impact.v1-try1.png` |
| `star-ring-burst` | `star/stills-55/star-ring-burst.v1-try1.png` |

## Tham chiếu và xử lý

Mọi lượt đều truyền hai ảnh của repo vào công cụ:

1. `games/immortality-cultivation/art-src/lab/vfx/earth/earth-big-burst.atlas.png`: chọn **khung 12**, hàng 2 cột 4 (đếm từ 1), ô 256×256 tại tọa độ x=768, y=256. Ảnh trích nguyên khung tạm ở `/private/tmp/418-earth-frame-12.png`; chỉ lấy độ khối và ánh sáng, không lấy đá hoặc màu cam.
2. `games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-moment-a.v1-try1.png`: chỉ lấy góc nhìn chéo xuống; không lấy băng hoặc cảnh nền.

Prompt ghi đầy đủ đường dẫn gốc, đường dẫn ảnh trích và vai trò từng ảnh. Không dùng ảnh bên thứ ba.

Công cụ trả ảnh gốc **1280×1280** dù prompt yêu cầu 1024×1024. Để giao đúng kích thước và lề, mỗi ảnh được thu đồng đều xuống 716×716 rồi đặt giữa nền đen 1024×1024 bằng ImageMagick; không cắt, kéo méo, vẽ thêm hoặc đổi màu. Phép biến đổi: `-resize 716x716 -background black -gravity center -extent 1024x1024`.

Kiểm tra tệp giao: cả 10 ảnh đúng 1024×1024; bốn dải viền rộng **154 px (15,04%)** đều có giá trị RGB bằng 0 ở mọi pixel; đủ 10 prompt và mỗi prompt có cả hai đường dẫn tham chiếu bắt buộc. Khoảng trống thực tế tới phần hiệu ứng còn lớn hơn viền này. Hai bản `-white` nhìn xám trắng trung tính; chênh kênh RGB lớn nhất lần lượt 5/255 (nổ lớn) và 8/255 (va chạm), nên không phải ảnh grayscale tuyệt đối; đã giữ nguyên màu công cụ sinh ra.

Ảnh gốc do công cụ lưu tự động được giữ nguyên tại:
`/Users/toandx/.codex/generated_images/01a1e338-36f9-7bd1-983b-20e523a5c01e/`.

| Clip | Tệp gốc của công cụ |
| --- | --- |
| `dark-ring-burst` | `exec-f9bf21ae-ee89-4470-8a80-97e3122c145b.png` |
| `water-ring-burst` | `exec-f4412999-82f3-4ca9-a902-d4d704fdde0f.png` |
| `poison-big-burst` | `exec-0cd07eb2-94cc-4bfc-93eb-6cfcd420690b.png` |
| `poison-ring-burst` | `exec-57db8939-8f3a-43ed-888b-917e674e2083.png` |
| `blood-big-burst` | `exec-b0d0e2b2-e1c8-443d-b4f9-c9d7e50e9f50.png` |
| `wood-big-burst` | `exec-a6a44303-1130-4802-92d1-ff53e8a2e736.png` |
| `dark-big-burst-white` | `exec-86220c82-ad6b-4eba-a3a9-025a3e5fd5af.png` |
| `dark-ground-impact-white` | `exec-cc194ede-c65e-4109-ad7e-7cba8766cd50.png` |
| `thunder-impact` | `exec-7061d6f4-063d-4e6e-8c3f-7113d47b6ec1.png` |
| `star-ring-burst` | `exec-8eab12c2-cc4f-49dd-a788-15ce66d92843.png` |

## Ảnh ghép và phần chưa làm

Ảnh ghép: [stills-55-sheet-418.jpg](../../games/immortality-cultivation/art-src/lab/vfx/stills-55-sheet-418.jpg).

Sandbox chỉ cho ghi trong repo và thư mục tạm, không cho ghi sang `/Volumes/SS990TPRO/htdocs/typing-game-review/`. Vì vậy dùng đường dẫn dự phòng mà phiếu cho phép:
`games/immortality-cultivation/art-src/lab/vfx/stills-55-sheet-418.jpg`.
Chưa chép sang thư mục owner-review và chưa cập nhật chỉ mục bên đó.

Không tạo video, không sửa code, không chạy build/test game, không ghi đè hay xóa ảnh đã có, không đổi nhánh và không commit. Không dùng thêm bốn lượt còn lại vì đã có đủ mười ảnh để owner chọn.

Owner cần xem bảng ghép và ảnh gốc 1024×1024, đặc biệt góc ellipse/độ cao của các vòng, lượng gỗ trong `wood-big-burst`, và độ tách biệt giữa hai bản khói trắng. Chỉ chuyển sang image-to-video sau khi owner chọn ảnh nguồn; việc chấm hiệu ứng tổng hợp trong play host thuộc bước sau.
