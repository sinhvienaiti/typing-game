# Phiếu 118 · Wordwoven · Đá và gỗ sử thi v3, v4

Ngày kiểm: 29/10/2026, macOS, repo cha.

**Chưa hoàn thành. Chưa sinh ảnh: 0/8 bản chọn, 0 lượt gọi `image_gen`.** Phiếu yêu cầu thứ tự **sau 117**. Tại lúc kiểm 10:20, phiếu 117 chỉ có hồ sơ xử lý và các `.try*`; chưa có `117-report.md`, `117-mock.jpg` hay bản chọn `fern-v3.png`. Đã hỏi chủ dự án bằng câu hỏi trong phiên về việc chờ 117 hay tiếp tục theo bộ 116; chưa có trả lời. Không tự coi sự im lặng là cho phép đổi thứ tự.

## Đã chuẩn bị

- Đọc `ART_ACCEPTANCE.md`, gồm §5; chỉ đạo mỹ thuật và bible Wordwoven; câu nền §3.8 của bộ yêu cầu cảnh vật.
- Đã xem ảnh tham chiếu chủ dự án, `114-composite-day.jpg`, tám bản chọn 116, v1/v2 của bốn loại trong phiếu. [Tờ đọc ảnh cũ](../../games/typing-defense/art-src/_review/118/old-inputs.jpg) chỉ là đầu vào kiểm; **không phải tờ giao v1–v4**.
- Đã ghi tám prompt nguyên văn STYLE + MAP + SCENERY, phần riêng và câu nền M. Nơi ghi: `scenery/meadow/{rock-medium,rock-small,rotten-log}-v{3,4}.try1.prompt.txt` và `scenery/shared/tree-stump-v{3,4}.try1.prompt.txt`, dưới `games/typing-defense/art-src/`.
- [Manifest tám prompt](../../games/typing-defense/art-src/_review/118/manifest.json) lưu khổ dự kiến, thư mục và toàn bộ nội dung. **Các prompt này chưa được gửi công cụ**, nên không tính là lượt sinh thứ nhất đã dùng.
- Tất cả dùng nền **M `#FF00FF`** vì có rêu/lá xanh và không có hồng/tím. Khổ dự kiến: đá vừa và gốc cây 1536 × 1536; đá nhỏ và khúc gỗ 1536 × 1024.

| Loại | Khác biệt v3 / v4 đã khóa trong prompt |
|---|---|
| `rock-medium` | Cao, đỉnh nghiêng trái / thấp rộng, hai khối chung chân, đỉnh phải. |
| `rock-small` | Tròn, vai trái cao / phiến dẹt, mép phải nhô lên. |
| `rotten-log` | Dài thẳng, miệng rỗng phải / ngắn cong, chạc gãy nhô ở một phần ba phải. |
| `tree-stump` | Cao, vành gãy lởm chởm, mặt vòng tuổi lõm / thấp rộng, mặt cắt phẳng rõ vòng tuổi. |

Chưa có lượt sửa prompt vì chưa có ảnh để đánh giá.

## Script đã lưu

Tất cả nằm trong [thư mục 118](../../games/typing-defense/art-src/_review/118/), dùng trực tiếp ImageMagick 7, Node và Python chuẩn; font Arial theo phiếu.

- `setup.py`: đã chạy để ghi tám prompt và manifest; từ chối ghi đè.
- `process.mjs`: đã chuẩn bị, **chưa chạy**; tách riêng màu khóa magenta, cắt nền rỗng, đổi cỡ đồng tỷ lệ, thêm lề; không bỏ vùng theo diện tích, không đổi màu phần vật. Phải xem tranh thực tế và tờ trước/sau trước khi chấp nhận mặt nạ.
- `measure.mjs`, `pairs.py`: đã chuẩn bị, **chưa chạy**; đo khổ, nền, hộp bao, vùng liền, luma mép ba pixel và độ khác biến thể. `measure.mjs` kế thừa phép đo 116, đổi điều kiện khổ cho phiếu này.
- `review.mjs`: đã chuẩn bị, **chưa chạy**; tờ trước/sau cùng canvas, tờ v1–v4 và tờ 128 px.
- `mock.mjs`: đã chuẩn bị, **chưa chạy**; phông 114, đất đá có sẵn, cây 116 và cây 117 nếu bản chọn đã xuất hiện; kích thước theo mét, lính nguồn cao 1,8 m làm thước. Không thay tranh cảnh vật bằng hình vẽ mã.
- `delivery-final.py`: dùng để nhập nguyên byte nguồn công cụ, giao bản chọn khi đạt và chụp MD5. Đã chạy riêng nhánh `snapshot` để ghi mốc sau phần chuẩn bị. `delivery.py` là bản nháp chưa dùng; dùng bản `delivery-final.py` vì đã sửa vị trí đọc tên file trong dòng MD5.
- Đã kiểm cú pháp các script JavaScript và Python; không chạy build hoặc test suite của game.

## KA1 sau phần chuẩn bị

| Số đo | Kết quả |
|---|---|
| File trước | 256 |
| File sau | 264 |
| Thêm | 8 prompt mới của đúng bốn loại được phép |
| Đổi nội dung | 0 |
| Mất | 0 |

[Mốc trước](../../games/typing-defense/art-src/_review/118/md5-before.txt), [mốc sau phần chuẩn bị](../../games/typing-defense/art-src/_review/118/md5-after.txt), [diff chỉ có dòng thêm](../../games/typing-defense/art-src/_review/118/md5-preparation-diff.txt), [JSON đối chiếu](../../games/typing-defense/art-src/_review/118/ka1-preparation.json). Đã dùng `md5 -r` trên mọi file trong `scenery/`, đệ quy, gồm prompt. Khi tiếp tục, giữ các mốc này và dùng tên mới cho mốc sau giao; không ghi đè.

## Chưa làm và điều kiện tiếp tục

Chưa sinh tám PNG; chưa có bản chọn, prompt chọn, tờ trước/sau, `118-sheet.jpg`, `118-small.jpg`, `118-mock.jpg`, `118-vs-ref.jpg`. Các kiểm 2–7 và điểm M/Q đều **chưa đo/chưa chấm**, không có cơ sở ghi đạt. Chưa có tờ so để kết luận “đứng cạnh được”. Không có ảnh sinh hay khung chụp nào cần dọn.

Tiếp tục khi 117 đã bàn giao hoặc chủ dự án cho phép làm 118 trước. Dùng `image_gen` tích hợp theo skill `imagegen`, mỗi ảnh tối đa ba lượt; giữ nguyên byte từng nguồn công cụ và prompt chính xác. Sau hậu kỳ xem đủ ảnh lớn, ảnh 128 px, tờ trước/sau và mock; nếu ngưỡng số buộc phá phần vẽ thì giữ tranh và ghi mâu thuẫn cho Claude. Chỉ giao khi đạt điều kiện phiếu hoặc đã hết ba lượt và ghi rõ thiếu gì.

Không chạy lệnh Git, dev server, trình duyệt hay mạng. Không sửa mã game, tài liệu khác, ảnh cũ hoặc nội dung game khác; không đọc/ghi Tu Tiên. Chưa tích hợp runtime và chưa sửa viền mực của `prepare-scenery`.

**Chủ dự án cần xem:** câu hỏi về thứ tự 117 → 118 trong phiên. Hiện chưa có bộ ảnh để Claude chấm nhận.
