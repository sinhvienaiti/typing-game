# Phiếu 319 · Bộ biểu tượng kỹ năng đợt 2

Ngày 06/11/2026. Hoàn thành **30 chiêu × 2 hướng = 60 biểu tượng được chọn**, qua **62 lượt image_gen: 60 lượt chính + 2 lượt vẽ lại B1** (trần 60 + 6). Không bỏ chiêu nào trong manifest.

Toàn bộ file mới nằm trong [skill-icons](../../games/immortality-cultivation/art-src/lab/ui/skill-icons/): `<hướng>-<id manifest>.v1-try1.png`, bản `-32.png`, `-48.png` và `.prompt.txt`. **Riêng B1 chọn try2 ở cả hai hướng**; giữ nguyên try1. Mỗi prompt ghi câu hình chính, công cụ, hai ảnh tham chiếu và kích thước; A1 ink-gold có thêm `.metadata.txt` bổ sung số đo thực tế, giữ nguyên prompt đã ghi.

**Anh xem ở tỷ lệ 100%:** [ink-gold](../../games/immortality-cultivation/art-src/lab/ui/skill-icons/icons-batch2-ink-gold.png) · [jewel-crest](../../games/immortality-cultivation/art-src/lab/ui/skill-icons/icons-batch2-jewel-crest.png). Hai bảng 1200 × 784 px, lưới 5 × 6, mỗi biểu tượng đúng 48 px; đủ mã và tên English của bảng thiết kế, nền #15171c, phông Arial. Đã mở bằng `view_image`, ảnh và chữ đúng ô.

Đã mở hai mẫu đạt 314 và đủ 30 ảnh chiêu `S/<id>.v1-try1.png` bằng `view_image`; chỉ đưa ảnh repo được phiếu chỉ định vào image_gen. Giữ nguyên văn hai câu FRAME và mẫu prompt 314. Màu theo hệ đầu tiên: các mục “mọi hệ” B6/D3 lấy Kim, D7 lấy Phong; B5/D8 giữ đen viền đỏ thẫm.

Đã mở **31 tấm kiểm cỡ thật** `icons-batch2-sizecheck-*.png` (30 chiêu + B1 try2), mỗi tấm có cả hai hướng ở đúng 32/48 px. Điểm tự chấm 0–10 xét nhận ra hình chính, độ cuốn hút/sang trọng, tách hình–khung và độ sạch; ghi theo mặt yếu nhất. Đây là tự chấm theo phiếu, chưa phải duyệt độc lập trong thanh chiêu runtime.

| Mã | Chiêu | Hình chính | Ink 32 | Jewel 32 | Ink 48 | Jewel 48 |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| A1 | Myriad Spirit Lotus Bloom | Sen ngọc lục lớn, tâm vàng trắng | 8,3 | 8,1 | 8,6 | 8,5 |
| A2 | Firmament-Sundering Rift | Khe nứt tím chéo, lòng tối, viền sáng | 8,2 | 8,1 | 8,6 | 8,5 |
| A3 | Nine-Heavens Tribulation Grid | Lục giác sét tím với tia sét giữa | 8,3 | 8,2 | 8,7 | 8,6 |
| A4 | Karmic Ember Tempest | Xoáy lửa sen đỏ vàng | 8,4 | 8,3 | 8,8 | 8,7 |
| A5 | Glacial Moon Reflection Tide | Trăng lưỡi liềm và một ngọn sóng băng | 8,5 | 8,4 | 8,8 | 8,7 |
| A6 | Scarlet Samsara Compass | La bàn huyết tám hướng, mũi thương đỏ | 8,1 | 8,0 | 8,5 | 8,4 |
| A7 | Seven-Star Astral Fall | Sao rơi lớn mang đuôi chòm sao | 8,3 | 8,2 | 8,7 | 8,6 |
| A8 | Netherworld Briar Vortex | Vòng gai độc lục tím quanh lòng xoáy tối | 8,4 | 8,3 | 8,7 | 8,6 |
| B1 | Three-Faced Six-Armed War Sovereign | Bán thân ba đầu lớn, sáu tay tách thành ba cặp | 8,2 | 8,1 | 8,6 | 8,5 |
| B2 | Thousand-Hand Bodhi Illuminator | Bán thân quang vàng với quạt chưởng mở | 8,1 | 8,0 | 8,5 | 8,4 |
| B3 | Primordial Heaven-and-Earth Titan | Cự thần vai rộng, tay giơ vũ khí chém | 8,2 | 8,1 | 8,6 | 8,5 |
| B4 | Purple Micro Star Emperor | Tinh quân đội miện sao, tay chỉ xuống | 8,1 | 8,0 | 8,5 | 8,4 |
| B5 | Nine-Nether Soul Arbiter | Minh đế mặt đen viền đỏ, hai lưỡi chéo | 8,2 | 8,1 | 8,6 | 8,5 |
| B6 | Taixu Sword Immortal Phantom | Bán thân kiếm tiên, vòng kiếm bạc sau vai | 8,2 | 8,1 | 8,6 | 8,5 |
| C1 | Azure Tempest Dragon | Đầu rồng sét tím trắng lao tới | 8,2 | 8,1 | 8,6 | 8,5 |
| C2 | Astral Slaying White Tiger | Đầu bạch hổ và vuốt năng lượng bạc | 8,3 | 8,2 | 8,7 | 8,6 |
| C3 | Nirvana Sunfire Vermilion Bird | Chu tước lửa dang cánh chữ V | 8,5 | 8,4 | 8,8 | 8,7 |
| C4 | Black-Abyss Tortoise & Serpent | Mai rùa lục giác, cổ rắn nước cuộn phía trên | 8,1 | 8,0 | 8,5 | 8,4 |
| C5 | Violet-Gold Auspicious Qilin | Đầu kỳ lân có gạc và bờm sét tím vàng | 8,2 | 8,1 | 8,6 | 8,5 |
| C6 | North-Sea Astral Kunpeng | Côn bằng dạng chim, cánh rộng trên xoáy nước | 8,3 | 8,2 | 8,7 | 8,6 |
| C7 | Celestial Truth Spirit Baize | Đầu bạch trạch quang vàng, mắt thứ ba trên trán | 8,1 | 8,0 | 8,5 | 8,4 |
| C8 | Moonlight Illusion Nine-Tailed Fox | Đầu hồ ly giữa quạt đuôi băng lớn | 8,4 | 8,3 | 8,7 | 8,6 |
| D1 | Heaven-Overturning Mountain Seal | Ấn vuông hổ phách với núm rồng | 8,3 | 8,2 | 8,7 | 8,6 |
| D2 | Soul-Shaking Primordial Bell | Chuông cổ miệng loe, một cung sóng âm | 8,5 | 8,4 | 8,8 | 8,7 |
| D3 | Myriad-Blade Spirit Gourd | Hồ lô hai bầu phóng quạt kiếm bạc | 8,3 | 8,2 | 8,7 | 8,6 |
| D4 | Nine-Dragon Heaven-Refining Cauldron | Đỉnh ba chân, rồng lửa chữ S ở miệng | 8,4 | 8,3 | 8,8 | 8,7 |
| D5 | Seven-Aperture Demon-Suppressing Pagoda | Tháp vàng nhiều tầng và hai xích sáng | 8,5 | 8,4 | 8,8 | 8,7 |
| D6 | Taiji Void-Reflecting Mirror | Gương tròn cán ngắn, lõi thái cực lớn | 8,5 | 8,4 | 8,8 | 8,7 |
| D7 | Immortal Binding Aurora Ribbon | Dải lụa bạc hà cuộn số tám | 8,6 | 8,5 | 8,9 | 8,8 |
| D8 | Twelve-Metropolis Array Banners | Một cờ đen viền đỏ lớn và hai cờ lùi nhỏ | 8,3 | 8,2 | 8,7 | 8,6 |

**Vẽ lại:** B1 try1 có quá nhiều binh khí, vòng trận và vệt sáng nên ba đầu/sáu tay hòa lại khi nhỏ: ink-gold **7,8/8,2**, jewel-crest **7,7/8,1** (32/48 px). Try2 phóng lớn ba đầu và bán thân, tách ba cặp tay bằng khoảng tối, bỏ vòng trận dưới; đạt điểm trong bảng. Mỗi hướng chỉ vẽ lại một lần; giữ cả hai bộ thử và prompt.

**Đối chiếu file:** đủ 62 PNG gốc 1254 × 1254 px, 62 bản 32 × 32, 62 bản 48 × 48, 62 prompt; tất cả PNG biểu tượng có sRGBA. Hai câu FRAME và đường dẫn ảnh chiêu đều có trong prompt. ImageMagick chỉ thu nhỏ, ghép và đặt nhãn; PNG gốc chép bằng `cp -n`. Có bốn JSON tiến độ thêm mới `icons-batch2-progress-{A,B,C,final}.json` để đối chiếu ID, prompt và điểm.

**Anh cần xem:** hai bảng tổng hợp ở 100%, nhất là B1 try2 và các hình còn sát ngưỡng ở 32 px: A6, B2, B4, C4, C7. Chi tiết vòng khắc, tinh vân, vảy và mắt thứ ba hòa lại tại cỡ này; 48 px rõ hơn. Tên English giữ theo bảng thiết kế; ID tệp giữ nguyên manifest.

Không bỏ phần việc nào của phiếu; chưa tích hợp runtime vì ngoài phạm vi. Không chạy build/test game, mở cổng hay ghi Git. Chỉ thêm file mới trong D và báo cáo này; không sửa/xóa tệp có sẵn.

