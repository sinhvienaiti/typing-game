# Phiếu 126 · Last Line · Bốn ảnh ải v2

Ngày 29/10/2026, Codex, Mac mini M4. Đã giao **bốn bản chọn 1536 × 864**, bằng **năm lượt `image_gen` tích hợp**: ba ảnh dùng try1, Rift Wall dùng try2. Giữ đủ năm bản sinh gốc và prompt nguyên văn. Tự chấm trên **bản hậu kỳ**: **M 8,0–8,5; Q 8,5–9,5**, gồm cả cỡ đầy đủ và 384 × 216. **Chờ Claude chấm lại**, chưa tích hợp vào game.

Điều kiện chạy đã đủ: [ART_DIRECTION_2026-10-28.md §4.3](../games/ART_DIRECTION_2026-10-28.md#43-bible-last-line-hướng-b-chủ-dự-án-chọn-2910) ghi chủ dự án chọn **B · Lightbearer sáng 29/10**, cho phép chạy các phiếu 121, 125, 126, 127. Tiêu đề phiếu và báo cáo 112 vẫn còn trạng thái chờ cũ; không sửa các file đó.

## Bộ giao

Gốc media: `games/typing-survival/art-src/`. Mỗi bản chọn có prompt `.prompt.txt` cạnh ảnh, trùng byte với prompt của lượt được chọn.

| Ải, tên theo `chapter-1.ts` | Bản chọn | Lượt | Mốc và bố cục |
| --- | --- | --- | --- |
| c1-s1 · First Shift | [c1-s1.png](../../games/typing-survival/art-src/ui/stages-v2/c1-s1.png) | try1 | Nhân vật dưới phải; đường chéo về trái; vòng trạm vỡ lớn bên trái; Pulse Gun lam và Heat Beam cam |
| c1-s2 · Leader Hunt | [c1-s2.png](../../games/typing-survival/art-src/ui/stages-v2/c1-s2.png) | try1 | Nhân vật dưới trái; ba Pack Leader ở ba lớp sâu, ba vòng sàn; khối đá nghiêng bắt sáng bên phải |
| c1-s3 · Rift Wall | [c1-s3.png](../../games/typing-survival/art-src/ui/stages-v2/c1-s3.png) | try2 | Nhân vật dưới phải; cửa Rift cam tím chiếm nửa trái, phiến sàn nổi; vòng trạm và hố đen cao phải |
| c1-s4 · Shining Shields | [c1-s4.png](../../games/typing-survival/art-src/ui/stages-v2/c1-s4.png) | try1 | Nhân vật dưới trái; hàng khiên chéo bên phải, hai súng đánh vào khiên; bóng leviathan trong hố đen bên trái |

Tên thật khác gợi ý trong phiếu: **First Shift / Leader Hunt / Rift Wall / Shining Shields**. Mục tiêu mã hiện tại lần lượt là giữ **150 giây**, hạ **3 Pack Leader** với trần **240 giây**, giữ **165 giây** có Rift, giữ **165 giây** giới thiệu Shield Guard. Ba thủ lĩnh trong ảnh 2 là cách minh họa mục tiêu; mã cho chúng xuất hiện theo các mốc thời gian. Không đổi tên hoặc nội dung trong mã.

Đã đọc ảnh chuẩn của chủ dự án, hai concept B của 112, [bộ sân 125 ghép cuối](../../games/typing-survival/art-src/_review/125-composite-v6.jpg), phiếu 109, `chapter-1.ts` và sáu dáng quái gốc. [Tờ dáng quái đã đọc](../../games/typing-survival/art-src/_review/126/source-foes.jpg). Mọi lượt sinh đều đính kèm **`concepts/b-lightbearer-fight.png`**; không đính kèm ảnh chuẩn để chép nội dung.

## Prompt và từng lượt sinh

Giữ nguyên văn STYLE, STAGE, phần riêng và câu REF của phiếu. Thêm chỉ dẫn khổ ngang, khung an toàn, nhận diện áo choàng navy viền vàng, giáp trắng/than chì, hai sentinel, sàn đá/thép và tọa độ bố cục. Các đoạn thêm nằm đầy đủ trong từng `.tryN.prompt.txt`; không có prompt ẩn hoặc runner API thay thế.

| Ảnh | Lượt | Bổ sung, kết quả và quyết định |
| --- | --- | --- |
| First Shift | 1 | Đặt nhân vật x≈70%, đường về trái, vòng trạm trái và hai màu súng. Có Scout phía trước, Brute lớn phía sau. Chọn; ảnh còn thêm hai quái mang khiên ở xa và nhiều quái nhỏ. Trừ điểm đúng đề/đọc, ghi để Claude xem. |
| Leader Hunt | 1 | Đặt nhân vật dưới trái, đúng ba thủ lĩnh với vòng sàn riêng, khối đá nghiêng phải. Ba lớp thủ lĩnh tách được. Chọn. |
| Rift Wall | 1 | Đặt nhân vật dưới phải, cửa xé trái, phiến sàn nổi. Cảnh đúng đề nhưng còn khiên phụ; vùng sáng nhất x=69,92% quá gần ảnh 4 x=60,61%, chỉ cách **9,31%**. Không chọn. |
| Rift Wall | 2 | Bỏ câu mô tả toàn bộ các loại quái khỏi phần bổ sung của riêng ảnh này; thay bằng crawler kính đen và vài Scout. Nhấn cửa Rift là mốc chính, phiến sàn lớn thay mưa mảnh vụn, vòng trạm tối che một phần đĩa xa. Hàng khiên phụ đã hết; chọn. Công cụ vẫn vẽ khối tua lớn trong Rift và đĩa xa vẫn giữ cực đại sáng sau blur. |
| Shining Shields | 1 | Đặt hàng khiên chéo bên phải, điểm va chạm khoảng x=63%, Splitter phía sau và leviathan xa bên trái. Chọn. Số khiên nhiều hơn gợi ý năm chiếc trong đoạn bổ sung, nhưng phiếu không khóa số lượng. |

Tổng **5 lượt**, không ảnh nào quá ba lượt. Bốn bản chọn cùng danh tính nhân vật và súng; hướng đường, mốc lớn và trọng tâm sáng khác nhau. Không sinh thêm khi ảnh đã tự đạt.

## Hậu kỳ và khổ

Ảnh công cụ trả **1672 × 940** cho c1-s1, **1672 × 941** cho ba ảnh còn lại và Rift try2. Mỗi bản chọn cắt giữa **1664 × 936**, rồi thu Lanczos về **1536 × 864**. Chỉ bỏ tổng cộng 8 px chiều ngang và 4–5 px chiều dọc; nhân vật, súng và mốc không bị cắt mất.

```sh
/opt/homebrew/bin/magick <ban-sinh.png> -gravity center \
  -crop 1664x936+0+0 +repage -filter Lanczos -resize '1536x864!' \
  -colorspace sRGB -depth 8 PNG24:<ban-chon.png>
```

`magick identify` và [kiểm nguồn](../../games/typing-survival/art-src/_review/126/provenance-check.json) xác nhận bốn bản chọn là **PNG RGB, 8-bit sRGB, nền đặc, 1536 × 864**. Không chỉnh sáng, gamma hoặc hue; mức chỉnh sáng **0%**. Không tách nền, phủ màu, xóa vật, san phẳng hoặc vẽ bù. Năm `.tryN.png` trùng SHA-256 với đầu ra công cụ gốc. Ảnh nhỏ dùng Lanczos `384x216!`.

Tờ **“bản sinh | bản hậu kỳ”**, mỗi vế 768 × 432, đã xem:

- [First Shift](../../games/typing-survival/art-src/_review/126/c1-s1-before-after.jpg).
- [Leader Hunt](../../games/typing-survival/art-src/_review/126/c1-s2-before-after.jpg).
- [Rift Wall](../../games/typing-survival/art-src/_review/126/c1-s3-before-after.jpg).
- [Shining Shields](../../games/typing-survival/art-src/_review/126/c1-s4-before-after.jpg).

## Kiểm đọc và số đo

Đã xem riêng bốn bản hậu kỳ ở khổ đầy đủ và [tờ 384 × 216](../../games/typing-survival/art-src/_review/126/thumbnails.jpg). Không thấy chữ/số đọc được, logo, chữ ký, khung, viền hoặc HUD. Vòng quanh súng gồm nét hình học rời; đường vàng trên áo là hoa văn. HUD ở tờ tham chiếu thuộc ảnh chuẩn, không nằm trong ảnh giao.

| Bản chọn | Nhân vật ở 384 px | Bầy ở 384 px | Mốc riêng ở 384 px | Luma TB | Hue trung vị | Cực đại sau blur 64: x, y | x / chiều rộng |
| --- | --- | --- | --- | ---: | ---: | --- | ---: |
| First Shift | Được | Được | Được: vòng trái, Brute, hai luồng súng | 0,304571 | 28,723° | 360, 156 | 23,44% |
| Leader Hunt | Được | Được | Được: ba thủ lĩnh, khối nghiêng; vòng xa rất mảnh | 0,338749 | 24,567° | 1463, 201 | 95,25% |
| Rift Wall | Được | Được | Được: vết xé và phiến nổi | 0,304349 | 25,920° | 1249, 0 | 81,32% |
| Shining Shields | Được | Được | Được: hàng khiên; Splitter nhỏ hơn | 0,328390 | 30,909° | 931, 452 | 60,61% |

Luma tính trên RGB sRGB 0–1: `L = 0,2126R + 0,7152G + 0,0722B`. Hue là trung vị HSV trên mọi pixel có màu, chỉ bỏ pixel hoàn toàn vô sắc. Cực đại là pixel sáng nhất trên trường luma sau Gaussian **sigma 64 px**, ở khổ giao, mép dùng `edge`. [Số đo kiểm trực tiếp](../../games/typing-survival/art-src/_review/126/metrics-validated-pass1.json) và [danh mục chọn](../../games/typing-survival/art-src/_review/126/final-selection.json).

- Biên luma: **0,034399 ≤ 0,06**. Biên hue: **6,342° ≤ 15°**.
- Khoảng cách x từng cặp, tính theo chiều rộng: 1–2 **71,81%**; 1–3 **57,88%**; 1–4 **37,17%**; 2–3 **13,93%**; 2–4 **34,64%**; 3–4 **20,70%**. Nhỏ nhất **13,93% > 10%**.
- Cực đại sáng của Rift Wall vẫn thuộc đĩa xa ở mép trên, không phải cửa Rift. Phép đo phân biệt bố cục đã đạt; mốc kể chuyện là cửa Rift lớn phía trái. Không làm tối cục bộ đĩa để ép số hoặc đổi phần vẽ.

## Tờ so và tự chấm KA5

[126-sheet.jpg](../../games/typing-survival/art-src/_review/126-sheet.jpg): hàng trên bốn ảnh mới, hàng dưới bốn ảnh 109, mỗi ảnh **768 × 432**, thứ tự 1–4. [126-vs-ref.jpg](../../games/typing-survival/art-src/_review/126-vs-ref.jpg): bốn cặp mới–chuẩn, mỗi ảnh cao đúng **480 px**, giữ tỷ lệ.

| Ảnh cạnh tham chiếu | Nhận xét |
| --- | --- |
| First Shift | **Đứng cạnh được:** vòng trạm làm nhân vật nhỏ lại, ngược sáng và lớp gần–giữa–xa–trời rõ; bầy còn dày hơn ảnh chuẩn. |
| Leader Hunt | **Đứng cạnh được:** khối đá nghiêng có quy mô, ba thủ lĩnh có phân cấp, vật liệu hoàn thiện; sàn còn bóng. |
| Rift Wall | **Đứng cạnh được:** vết xé lớn, phiến sàn nổi có chiều sâu, sắc cam tím kể được biến cố; nhiều lửa hơn ảnh chuẩn. |
| Shining Shields | **Đứng cạnh được:** hàng khiên đọc nhanh, leviathan tạo quy mô, ánh sáng có hướng; hạt sáng quanh va chạm còn dày. |

M lấy ảnh chuẩn làm mốc **9**, không lấy bộ cũ làm chuẩn. Q theo năm tiêu chí ở bảng §1 của `ART_ACCEPTANCE.md`; §2.2 quy định ngưỡng ảnh 2D. Điểm dưới đây đều chấm trên bản hậu kỳ, không suy ra từ phép đo.

| Bản chọn | Cỡ | M | Đúng đề | Đọc được | Hợp bộ | Hình khối | Dùng tiếp | Q |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| First Shift | 1536 × 864 | **8,2** | 1,5 | 1,5 | 2 | 1,5 | 2 | **8,5** |
| First Shift | 384 × 216 | **8,0** | 1,5 | 1,5 | 2 | 1,5 | 2 | **8,5** |
| Leader Hunt | 1536 × 864 | **8,5** | 2 | 2 | 2 | 1,5 | 2 | **9,5** |
| Leader Hunt | 384 × 216 | **8,2** | 2 | 1,5 | 2 | 1,5 | 2 | **9,0** |
| Rift Wall | 1536 × 864 | **8,4** | 1,5 | 2 | 2 | 1,5 | 2 | **9,0** |
| Rift Wall | 384 × 216 | **8,1** | 1,5 | 1,5 | 2 | 1,5 | 2 | **8,5** |
| Shining Shields | 1536 × 864 | **8,4** | 2 | 2 | 2 | 1,5 | 2 | **9,5** |
| Shining Shields | 384 × 216 | **8,2** | 2 | 1,5 | 2 | 1,5 | 2 | **9,0** |

**Chỗ cần Claude/chủ dự án xem:** First Shift có hai quái mang khiên ở xa ngoài nhóm quái được mã ải giới thiệu; Rift có khối tua lớn tự sinh; các quái mang dáng người rõ hơn sprite gốc. Các nét này giảm độ sát đề, đã trừ Q. Bốn sàn còn phản sáng khá mạnh dù prompt yêu cầu khô; tư thế nhân vật và dáng sentinel vẫn gần concept B. Chưa đạt độ thoáng, tiết chế chi tiết của ảnh chuẩn; vì vậy M không lên 9. Không xóa các phần vẽ bằng công cụ để sửa những thiếu sót này.

## KA1 và phạm vi

Đã chạy `/sbin/md5 -r` đệ quy trên toàn bộ `games/typing-survival/art-src/` **trước lần ghi đầu tiên**: **1693 file**. Snapshot sau có **1762 file**, thêm **69**, **0 thay đổi, 0 mất**. Diff chỉ có dòng thêm. Mọi file của 109 và mọi media có trước phiên còn nguyên.

- [MD5 trước](../../games/typing-survival/art-src/_review/126/md5-before.txt), [MD5 sau](../../games/typing-survival/art-src/_review/126/md5-after.txt), [diff](../../games/typing-survival/art-src/_review/126/md5-diff.txt), [tóm tắt](../../games/typing-survival/art-src/_review/126/md5-summary.json).
- Ba đầu ra audit `md5-after.txt`, `md5-diff.txt`, `md5-summary.json` được ghi sau snapshot, nên không tự băm chính chúng. Baseline và các script/tờ kiểm đều đã nằm trong snapshot sau.
- Script nằm trong [_review/126/](../../games/typing-survival/art-src/_review/126/): `prepare.py`, `refine-rift.py`, `measure.py`, `validate-metrics.py`, `select-and-review-v2.py`, `provenance-check.py`, `md5-audit.py`. `baseline.py` lưu lại thao tác snapshot đã chạy nội tuyến trước khi thư mục tồn tại; lệnh dựng tờ quái lưu trong `source-foes-command.json`. `select-and-review.py` là bản nháp chưa chạy, giữ nguyên; dùng v2 có chú thích tiếng Việt đủ dấu.
- Script dùng chế độ tạo file mới và dừng nếu đích đã tồn tại; tái hiện trong thư mục phiếu mới, không chạy đè lên bộ giao. Đường dẫn đầu ra công cụ và ảnh đính kèm nằm trong năm `*.tryN-source.json`; sinh lại dùng công cụ tích hợp với prompt đã lưu. Không có script mạng thay thế.

Không chạy Git, build, test game, dev server hoặc trình duyệt. Không sửa mã, tích hợp runtime, âm thanh hay tài liệu khác. Không đọc/ghi Tu Tiên hoặc ghi game khác. Không có raw frame trình duyệt cần prune; các try và ảnh kiểm là hồ sơ giao phải giữ. Việc tích hợp và lượt chấm độc lập của Claude nằm sau phiếu này.
