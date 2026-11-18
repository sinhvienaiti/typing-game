# Phiếu 416: Ảnh tĩnh dải nền cut-in tuyệt kỹ cho 14 hệ (nguồn để làm video)


Phản biện: PASS (Sonnet, 16/11)
## Bối cảnh
Danh sách video owner duyệt 16/11 (`docs/work/tasks/video-production-list.md` mục 7): cut-in tuyệt kỹ là hạng SHOULD dùng video (skill `game-video-vfx-usage`). Nhân vật trong cut-in chờ nữ chính được duyệt, nên trước mắt làm **dải nền** (không người, không sinh vật) cho từng hệ. Video có hình phải làm image-to-video từ ảnh tĩnh, nên cần ảnh tĩnh trước.

## Việc
`image_gen`, tối đa 16 lần, mỗi ảnh 1920×640 (dải ngang 3:1), lưu `games/immortality-cultivation/art-src/concept/cutin-bands/cutin-<hệ>.v1-try<k>.png`, prompt thật trong `.prompt.txt`.
Ảnh tham chiếu bắt buộc mọi lần, ghi đường dẫn trong prompt:
- một atlas dải cut-in có sẵn trong `games/immortality-cultivation/art-src/lab/vfx/cutin/` (bố cục dải, ánh sáng);
- ảnh tham chiếu tuyệt kỹ của đúng hệ đó trong `games/immortality-cultivation/art-src/concept/ult-<hệ>/` (màu, chất liệu) nếu có.
14 hệ: metal, wood, water, fire, earth, ice, thunder, wind, light, dark, void, blood, poison, star.
Mỗi dải: năng lượng của hệ chảy ngang theo chiều dải, nhiều lớp (lõi sáng, làn khói/hạt, ánh lấp lánh), tông màu hệ, hai đầu dải mờ dần về đen, chừa vùng giữa-trái để sau này đặt nhân vật và tên chiêu; không người, không sinh vật, không chữ, không watermark. Phong cách game tu tiên thương mại, sang trọng, điện ảnh, chân thật (không hoạt hình phẳng, không viền nét).
Ưu tiên một ảnh mỗi hệ (14 lần), 2 lần dư để làm lại hệ kém nhất.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
Ảnh ghép `cutin-bands-sheet-416.jpg` trong `art-src/concept/cutin-bands/` và `docs/codex-queue/416-report.md`.
