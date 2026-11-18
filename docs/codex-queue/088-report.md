# Phiếu 088 · Tuyến Cuối · Ảnh sân Vành Chân Trời

Ngày 28/10/2026. Đã tạo đủ năm ảnh bằng công cụ tích hợp `image_gen`, lưu prompt nguyên văn cạnh từng lượt và từng bản chọn. **Năm bản chọn tự chấm 9/10; kiểm 1–6 đạt. Chưa có điểm duyệt của Claude.**

## 1. Nguồn và cách làm

- Đọc chuẩn [ART_ACCEPTANCE.md](../games/ART_ACCEPTANCE.md), ảnh màn tựa và `title-horizon.prompt.txt`. Cả bộ giữ nguyên bốn cụm phong cách bắt buộc.
- Tờ tham chiếu thực tế là 2584×1470. Cắt ô thứ hai hàng đầu bằng `magick -crop 646x368+646+0 +repage`: chiều cao một ô là 367,5 px, làm tròn thành 368 px. Lưu [ref-fight.png](../../games/typing-survival/art-src/_review/088/ref-fight.png).
- Chụp danh mục MD5 trước khi cắt ảnh và tạo media. Tạo concept trước; cả bốn ảnh sau đều nhận concept làm tham chiếu. Hai lượt sửa decal còn nhận ảnh decal của lượt trước.
- Mọi lượt gốc và prompt đều được giữ nguyên. Không xóa `.try*`.
- Công cụ trả concept ở 1536×1024, hai hull ở 887×1774, lớp xa ở 1774×887 và các atlas ở 1254×1254. Bản chọn được xuất đúng khổ bằng ImageMagick, lọc Lanczos, giữ tỉ lệ. Đây là chuẩn hóa kích thước; ảnh alpha không phải bản tạo nguyên sinh ở khổ giao.
- Decal lượt 2 có bố cục tiết chế hơn lượt 3 nên được chọn. Sau khi đổi khổ, xuất PNG bằng bước chuẩn hóa **chỉ alpha 1 → 0**, giữ nguyên alpha 0 và 2–255. So sánh RGBA xác nhận **0 pixel đổi RGB**; 108.051 pixel alpha 1 được đưa về 0 trong toàn atlas, gồm 1.332 pixel trong rãnh giữa ô. Không vẽ thêm hay cắt mất phần decal nhìn thấy. Vẫn còn 1.389.800 pixel alpha 2–254 để giữ mép mờ. Xem [nhật ký xuất decal](../../games/typing-survival/art-src/_review/088/deck-export-normalization.json).

## 2. Tự chấm từng lượt

Thứ tự năm tiêu chí: **Đúng đề / Đọc được trong game / Hợp bộ / Hình khối / Dùng được cho bước sau**, mỗi tiêu chí 0–2. Điểm ghi nhận cả bản đầy đủ và bản thu nhỏ, lấy mức thận trọng hơn.

Đã xem concept trong khung 1280×720, hull ở 128×256, lớp xa ở 640×320 và atlas ở 256×256. Các ảnh alpha được xem trên nền `#05060A` và nền ô vuông xám. Việc xem ảnh tĩnh này không phải nghiệm thu cảnh game sau tích hợp.

| Ảnh | Lượt | Prompt thêm hay sửa | Điểm 5 tiêu chí | Tổng | Còn thiếu |
| --- | --- | --- | --- | --- | --- |
| concept-fight | 1 | Paintover từ cảnh trận; giữ hành lang, sọc cảnh báo, cổng và hố đen; thêm thân trạm hai bên, giàn đỡ và lớp xa; hạ sáng vùng gõ | 1,5 / 2 / 2 / 1,5 / 2 | 9 | Vạch cảnh báo ngang nằm gần đáy hơn ảnh gốc; không dùng concept để suy ra tọa độ sàn |
| hull-left | 1 | Chiếu trực giao từ trên; mép phải đặc, giàn thò sang trái; một hatch lớn, ba ống dài, lò âm và LED thưa | 2 / 1,5 / 2 / 2 / 1,5 | 9 | Đinh tán nhỏ chìm khi cao 256 px; bản giao tăng kích thước từ ảnh gốc |
| hull-right | 1 | Bố cục độc lập: nắp bát giác thấp, hai hatch cao, ống chữ L và giàn chéo phía phải | 2 / 1,5 / 2 / 2 / 1,5 | 9 | Chi tiết nhỏ chìm ở cỡ thật; bản giao tăng kích thước từ ảnh gốc |
| far-structures | 1 | Nhìn ngang; mô-đun thấp và hai đầu vành gãy ở mép; chừa ô hố đen; viền cam mảnh | 2 / 2 / 2 / 1,5 / 1,5 | 9 | Hai đầu vành còn khá cân; bản giao tăng kích thước từ ảnh gốc |
| deck-decals | 1 | Bốn decal theo thứ tự yêu cầu, chevron hướng xuống; yêu cầu lề trong suốt | 1,5 / 2 / 1,5 / 2 / 0,5 | 7,5 | Rãnh 32 px ở khổ giao chỉ 97,468627% alpha 0; vết cháy hơi nhiều mảnh vụn |
| deck-decals | 2, gốc | Thu nhỏ từng decal, tăng khoảng trống thành chữ thập rộng, giữ thứ tự và chất liệu | 1,5 / 2 / 1,5 / 2 / 0,5 | 7,5 | Rãnh đạt 98,975763%; 1.332 pixel còn alpha 1 dù mắt không thấy |
| deck-decals | 3 | Khóa vùng trống và lề; yêu cầu alpha bằng 0 tuyệt đối, không bụi mờ | 1,5 / 2 / 1,5 / 1,5 / 0,5 | 7 | Rãnh đạt 99,376384% ở khổ giao; chất liệu gồ và sáng hơn lượt 2 |
| deck-decals | 2, xuất chuẩn hóa | Giữ nguyên prompt lượt 2; đổi khổ và đưa riêng alpha 1 về 0, không đổi RGB | 1,5 / 2 / 1,5 / 2 / 2 | 9 | Vết cháy vẫn có mảnh vụn dày hơn một vết xém phẳng; cần Claude xem lại cảm giác chất liệu |

Không có lượt tạo thứ tư. Bốn ảnh đầu dừng ở lượt 1 vì đạt từ 8. Decal dùng hết ba lượt rồi chọn hình tốt nhất và sửa lỗi kỹ thuật xuất alpha.

## 3. Bản chọn

Các đường dẫn dưới đây đều có `<tên>.prompt.txt` cùng thư mục, chép nguyên văn từ prompt của lượt được chọn.

| Bản chọn | Nguồn | Lý do |
| --- | --- | --- |
| [concept-fight.png](../../games/typing-survival/art-src/arena/concept-fight.png) | concept-fight.try1.png | Thân trạm đọc rõ, có chiều sâu dưới hành lang, cùng màu màn tựa; vùng gõ đủ tối |
| [hull-left.png](../../games/typing-survival/art-src/arena/hull-left.png) | hull-left.try1.png, đổi khổ | Mảng thép lớn, giàn bên trái và mép giáp hành lang thẳng; nhìn từ trên xuống |
| [hull-right.png](../../games/typing-survival/art-src/arena/hull-right.png) | hull-right.try1.png, đổi khổ | Khác bố cục trái, không lật gương; nắp bát giác và ống chữ L còn nhận ra ở cỡ nhỏ |
| [far-structures.png](../../games/typing-survival/art-src/arena/far-structures.png) | far-structures.try1.png, đổi khổ | Bóng công trình và vành gãy đọc được ở 640 px; ô hố đen trống hoàn toàn theo phép kiểm |
| [deck-decals.png](../../games/typing-survival/art-src/arena/deck-decals.png) | deck-decals.try2.png, đổi khổ và chuẩn hóa alpha | Bốn dấu tách rõ, chevron đúng hướng, chất liệu ít gắt hơn lượt 3; rãnh xuất đạt tuyệt đối |

Prompt của tất cả **7 lượt tạo** nằm trong [arena/](../../games/typing-survival/art-src/arena/), tên `<tên>.tryN.prompt.txt`. Prompt bản chọn không được thêm câu hậu kỳ; bước chuẩn hóa được ghi riêng ở báo cáo và JSON để phân biệt với lệnh đã gửi công cụ.

## 4. Kiểm bắt buộc

### Kiểm 1 · KA1 MD5

Chạy `md5 -r` riêng từng file, đệ quy toàn bộ `art-src/`, rồi chạy `diff -u` hai danh mục.

| Chỉ số | Kết quả |
| --- | ---: |
| File có sẵn ở mốc trước | 26 |
| File trong ảnh chụp danh mục sau | 93 |
| File mới trong danh mục sau | 67 |
| File có sẵn đổi MD5 | 0 |
| File có sẵn bị thiếu | 0 |
| Dòng dữ liệu bị bỏ trong diff | 0 |
| Dòng dữ liệu thêm trong diff | 67 |

**Đạt:** diff chỉ thêm file mới. Hai file `md5-after.txt` và `md5-diff.txt` được ghi sau lúc liệt kê danh mục cuối; danh mục không tự băm chính nó. Báo cáo nằm ngoài `art-src/`.

Đầu ra: [trước](../../games/typing-survival/art-src/_review/088/md5-before.txt), [sau](../../games/typing-survival/art-src/_review/088/md5-after.txt), [diff](../../games/typing-survival/art-src/_review/088/md5-diff.txt).

### Kiểm 2 · Khổ ảnh

Đã chạy `/opt/homebrew/bin/magick identify` trên cả năm bản chọn; tất cả là PNG 8-bit sRGB.

| Ảnh | Kết quả identify | Đạt |
| --- | --- | --- |
| concept-fight | 1536×1024 | Có |
| hull-left | 1024×2048 | Có |
| hull-right | 1024×2048 | Có |
| far-structures | 2048×1024 | Có |
| deck-decals | 2048×2048 | Có |

Đầu ra đầy đủ: [checks-final.txt](../../games/typing-survival/art-src/_review/088/checks-final.txt).

### Kiểm 3 · Alpha

Đo trực tiếp RGBA 8-bit. Luma vùng mép là trung bình không trọng số trên các pixel alpha 1–254; ngưỡng tối đa 0,35.

| Ảnh alpha | Min | Max | Số pixel alpha 1–254 | Luma trung bình vùng mép | Đạt |
| --- | ---: | ---: | ---: | ---: | --- |
| hull-left | 0 | 255 | 1.460.506 | 0,111389 | Có |
| hull-right | 0 | 255 | 1.635.574 | 0,118994 | Có |
| far-structures | 0 | 255 | 792.432 | 0,074694 | Có |
| deck-decals | 0 | 255 | 1.389.800 | 0,253151 | Có |

- **Lớp xa:** vùng x 30–70%, y 0–60% có 503.685 pixel; **503.685/503.685 = 100% có alpha ≤8**, vượt yêu cầu ≥99%.
- **Atlas:** hợp hai dải x=1008–1039 và y=1008–1039 có 130.048 pixel; **130.048/130.048 = 100% có alpha 0**.
- Concept có alpha min=max=255, nền đặc.
- Xem trên nền tối và nền ô vuông không thấy viền trắng hoặc xám nhạt quanh các lớp.

### Kiểm 4 · Độ tối

Công thức: `Y = (0,2126R + 0,7152G + 0,0722B) / 255`, tính trên mẫu màu sRGB 8-bit. Với lớp alpha chỉ lấy pixel alpha >128; với concept lấy toàn ảnh và đo riêng hình chữ nhật quy định. Không nhân alpha vào luma.

| Ảnh | Số pixel alpha >128 | Luma trung bình | Pixel Y >0,8 | Ngưỡng | Đạt |
| --- | ---: | ---: | ---: | --- | --- |
| hull-left | 1.364.737 | 0,115933 | 0,114161% | Trung bình ≤0,14; sáng ≤2% | Có |
| hull-right | 1.566.394 | 0,121663 | 0,177350% | Trung bình ≤0,14; sáng ≤2% | Có |
| far-structures | 668.260 | 0,078847 | 0,230000% | Trung bình ≤0,14; sáng ≤2% | Có |
| concept-fight, toàn ảnh | 1.572.864 | 0,153870 | 0,730133% | Thông tin thêm | — |
| concept-fight, x25–75%, y50–70% | — | **0,146059** | — | Trung bình ≤0,20 | Có |

Atlas không có ngưỡng tối toàn ảnh trong phiếu: đo thêm được trung bình 0,262115, pixel Y >0,8 là 0,362981%. Ngưỡng luma mép alpha của atlas vẫn đạt như kiểm 3.

Số đo đầy đủ: [metrics-final.json](../../games/typing-survival/art-src/_review/088/metrics-final.json). Có script đo và xác nhận trong cùng thư mục; các script chỉ đọc ảnh khi kiểm.

### Kiểm 5 · Không chữ, không số

Đã xem trực tiếp cả năm bản chọn ở bản đầy đủ và bản thu nhỏ. Đã xem thêm cả ba lượt decal ở cỡ đầy đủ và atlas rộng 256 px.

| Ảnh | Chữ, số | Người, sinh vật, tàu bay, logo, HUD |
| --- | --- | --- |
| concept-fight | Không thấy | Không thấy |
| hull-left | Không thấy | Không thấy |
| hull-right | Không thấy | Không thấy |
| far-structures | Không thấy | Không thấy |
| deck-decals | Không thấy | Không thấy |

Các điểm tròn trên hull và patch là đinh tán; các hình V của decal là ký hiệu chevron được yêu cầu. Ảnh tham chiếu cắt từ game vẫn có HUD và chữ gốc; ảnh này chỉ là đầu vào đối chiếu.

### Kiểm 6 · Tờ xem nhanh

Đã tạo [088-sheet.jpg](../../games/typing-survival/art-src/_review/088-sheet.jpg), **2560×1120**, có nhãn Arial:

- Hàng 1: ref-fight bên trái, concept bên phải, cùng ô 1280×780; nội dung được fit vào khung 1248×720, giữ tỉ lệ riêng nên phần lề khác nhau.
- Hàng 2: hull-left, hull-right, far-structures, deck-decals, mỗi ảnh hiện lần lượt trên nền `#05060A` và ô vuông xám; mỗi ô 320×340.
- Bản kiểm cỡ thật riêng: [hull cao 256 px](../../games/typing-survival/art-src/_review/088/hulls-runtime-256.jpg), [lớp xa rộng 640 px](../../games/typing-survival/art-src/_review/088/far-runtime-640.jpg), [concept fit 1280×720](../../games/typing-survival/art-src/_review/088/concept-runtime-1280x720.jpg), [ba lượt decal rộng 256 px](../../games/typing-survival/art-src/_review/088/deck-trials-runtime-256.jpg).

## 5. Bàn giao và phần chưa làm

Đã bàn giao đủ năm bản chọn, bảy lượt gốc, mọi prompt, ảnh tham chiếu, tờ xem nhanh, số đo và MD5. Không có ảnh yêu cầu nào bị bỏ.

Không tích hợp runtime, không sửa mã hoặc tài liệu khác: đó là TS-M1-08 và nằm ngoài các đường dẫn cho phép của phiếu. Không chạy lệnh Git, build, test suite, dev server, trình duyệt hoặc mạng ngoài công cụ tạo ảnh. Không đọc hoặc ghi Tu Tiên; không tạo âm thanh.

**Chủ dự án/Claude cần xem:** chấm lại năm ảnh, nhất là chất liệu vết cháy và patch trong atlas. Concept có vạch ngang gần đáy hơn tham chiếu; khi dựng TS-M1-08 phải giữ tọa độ hành lang và vạch hiện có từ cảnh gốc, dùng concept để dựng phần thân trạm mới. Bốn bản alpha đã được tăng khổ khi xuất; xem chất lượng nội suy ở cỡ sử dụng đã ghi. Chỉ chuyển trạng thái sang “Nhận” sau khi Claude chấm lại từ 8.
