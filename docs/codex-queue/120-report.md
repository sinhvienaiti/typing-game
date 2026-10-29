# Phiếu 120 · Dragonhold · Trời và phông xa của ải rồng

Ngày kiểm: 29/10/2026, macOS, repo cha.

**Chưa hoàn thành: 0/6 ảnh, chưa gọi `image_gen`.** Phiếu quy định **“Thứ tự: sau 119.”** [Báo cáo 119](119-report.md) hiện ghi 0/5 bản chọn, chưa sinh ảnh vì đang chờ 118. Hai ảnh `ui/title-epic/title-backdrop.png` và `keyart.png` chưa tồn tại tại lúc kiểm. Đã gửi câu hỏi trong phiên để chủ dự án chọn giữ thứ tự hay cho phép sinh 120 ngay; chưa có trả lời tại lúc ghi báo cáo. Chưa tự đổi thứ tự; chưa tiêu lượt sinh.

## Đã chuẩn bị

- Đọc chỉ đạo mỹ thuật 28/10, bible Dragonhold §3 và thang M; đọc `ART_ACCEPTANCE.md`, nhất là §5 về hậu kỳ không phá tranh; đọc README và mã điều phối của `tools/art-normalize`.
- Đã xem ảnh tham chiếu của chủ dự án, ảnh map A2 và `pine-river-far-015.png`; đọc prompt phông cũ để hiểu luật ghép mép. Không dùng mức chi tiết hoặc ánh sáng của phông cũ làm chuẩn nhận.
- [Tờ đầu vào](../../games/dragon-hold/art-src/_review/120/inputs.jpg) chỉ phục vụ đối chiếu nguồn, **không phải ảnh mới hoặc tờ nghiệm thu**. Đã xem tờ này sau khi dựng.
- Trích nguyên văn STYLE, SKY, RING, dòng nền M và sáu phần riêng từ phiếu. Hai ô thứ hai có nguyên văn MATCH và đường dẫn ảnh neo dự kiến trong manifest. Không đính kèm ảnh neo chưa tồn tại, chưa gửi bất kỳ prompt nào tới công cụ.

Sáu prompt dự kiến nằm trong `games/dragon-hold/art-src/backdrops/pass-epic/`:

| Ảnh | File đã tạo | Khổ yêu cầu, chưa đo | Phụ thuộc khi sinh |
|---|---|---|---|
| `sky-dawn-a` | `sky-dawn-a.try1.prompt.txt` | 1536 × 1024 | Không |
| `sky-dawn-b` | `sky-dawn-b.try1.prompt.txt` | 1536 × 1024 | Đính kèm bản chọn `sky-dawn-a.png` đã xem, kèm MATCH |
| `layer-far` | `layer-far.try1.prompt.txt` | 1536 × 1024 | Mép chân núi 58%; vòng 380 m |
| `layer-mid` | `layer-mid.try1.prompt.txt` | 1536 × 1024 | Mép chân núi 60%; vòng 260 m |
| `layer-near-a` | `layer-near-a.try1.prompt.txt` | 1536 × 1024 | Mép chân núi 62%; vòng 170 m |
| `layer-near-b` | `layer-near-b.try1.prompt.txt` | 1536 × 1024 | Đính kèm bản chọn `layer-near-a.png` đã xem, kèm MATCH; mép 62% |

[Manifest](../../games/dragon-hold/art-src/_review/120/manifest.json) lưu prompt đầy đủ, khổ yêu cầu, ảnh neo và trạng thái. **Hậu tố `.try1.prompt.txt` hiện chỉ là tên prompt dự kiến, không chứng minh đã có lượt sinh.** Chưa sửa prompt qua lượt nào; chưa có `.tryN.png`, bản chọn, prompt bản chọn hoặc alpha.

## KA1 sau chuẩn bị

Đã chạy `md5 -r` trên **mọi file trong `games/dragon-hold/art-src/backdrops/`, đệ quy**, trước khi ghi prompt và sau phần chuẩn bị.

| Số đo | Kết quả |
|---|---:|
| File trước | 17 |
| File sau chuẩn bị | 23 |
| File thêm | 6 prompt đúng tên phiếu |
| File cũ đổi nội dung | 0 |
| File cũ mất | 0 |
| Prompt khớp manifest | 6/6 |
| PNG lượt sinh | 0 |
| PNG bản chọn | 0 |

Chứng cứ: [MD5 trước](../../games/dragon-hold/art-src/_review/120/md5-before.txt), [MD5 sau chuẩn bị](../../games/dragon-hold/art-src/_review/120/md5-after-preparation.txt), [kết quả `diff -u`](../../games/dragon-hold/art-src/_review/120/md5-preparation-diff.txt), [JSON đối chiếu](../../games/dragon-hold/art-src/_review/120/ka1-preparation.json). Diff chỉ thêm sáu dòng nội dung; không xóa hoặc thay dòng file cũ. Đây **chưa phải mốc sau bàn giao sáu ảnh**; khi tiếp tục phải ghi mốc mới, không ghi đè mốc chuẩn bị.

## Xung đột cần giữ lại theo §5

Kiểm 3 yêu cầu 10 px ở **cả bốn mép** là màu nền magenta; nhưng phần riêng của bốn ô núi yêu cầu đường chân núi chạm mép trái/phải ở 58%, 60% hoặc 62%, vật kéo xuống dưới và đáy là sương lam/xanh đặc. Hai yêu cầu không thể đồng thời đúng: magenta toàn bộ mép sẽ cắt vật hoặc đổi đáy thành nền khóa.

Chưa có tranh nên chưa xảy ra hậu kỳ phá tranh. Khi tiếp tục, **không tô viền magenta, không san phẳng núi hoặc phủ đáy sương để ép đạt số**. Giữ tranh theo `ART_ACCEPTANCE.md` §5, đo trung thực và để Claude quyết phạm vi kiểm nền: phần thật sự nằm ngoài silhouette thay vì toàn bộ bốn cạnh. Chưa tự thay tiêu chí nghiệm thu hoặc công bố ngoại lệ đã được duyệt.

## Các kiểm chưa thực hiện

| Kiểm | Trạng thái |
|---|---|
| 2 · Khổ sáu ảnh giao | Chưa có ảnh; 1536 × 1024 là yêu cầu, chưa phải số đo. |
| 3 · Nền, sắc khóa trong vật, alpha, viền 4× | Chưa tách nền hoặc đo; chưa có `120-edge.jpg`. |
| 4 · Chân núi, chênh màu mép trước/sau | Chưa đo; chưa pha mép cosin. |
| 5 · Thử vòng | Chưa có `120-ring.jpg`; chưa thể kết luận đường nối. |
| 6 · Cổng/tường, tượng rồng, đỉnh tuyết ở 384 px | Chưa có ảnh ghép để kiểm. |
| 7 · Ảnh ghép và so tham chiếu | Chưa có `120-composite.jpg` hoặc `120-vs-ref.jpg`; chưa kết luận “đứng cạnh được”. |
| 8 · Hue 285–330°, S > 0,5 | Chưa đo; không gán số 0. |
| 9 · M trên ảnh ghép; Q từng ô đầy đủ và 384 px | **Chưa chấm**; không công bố đạt. |
| §5 · “bản sinh \| bản hậu kỳ” mỗi ảnh | Chưa có nguồn sinh hoặc bản hậu kỳ để dựng. |

Không có ô nào đã trượt ba lượt. Sáu ảnh còn nguyên hạn mức tối đa ba lượt mỗi ảnh.

## Script và lệnh đã dùng

Script nằm trong [thư mục `_review/120/`](../../games/dragon-hold/art-src/_review/120/), ghi tên mới bằng chế độ độc quyền và từ chối ghi đè khi chạy lại. Chạy từ repo cha, với `-B` để không tạo `__pycache__`:

```sh
python3 -B games/dragon-hold/art-src/_review/120/prepare.py
python3 -B games/dragon-hold/art-src/_review/120/inputs.py
python3 -B games/dragon-hold/art-src/_review/120/audit.py
```

- `prepare.py`: chụp mốc trước bằng `md5 -r`, trích prompt nguyên văn và ghi manifest.
- `inputs.py`: đọc ba ảnh đầu vào, dựng tờ bằng ImageMagick 7; tự thêm hai bản chọn 119 nếu chúng tồn tại khi bắt đầu một lần chạy mới.
- `audit.py`: chụp mốc sau chuẩn bị, chạy `diff -u`, đối chiếu hash và kiểm prompt khớp manifest.

Dùng `/opt/homebrew/bin/magick`, font `/System/Library/Fonts/Supplemental/Arial.ttf`. Không cần Pillow. Chưa chạy `key-alpha.sh`; khi tiếp tục phải đặt `ART_MAGICK=/opt/homebrew/bin/magick` và chuyển WORK của thư viện vào `_review/120/` bằng wrapper cục bộ, không sửa công cụ chung hoặc ghi vào WORK mặc định `tools/art-normalize/.tmp/` ngoài phạm vi phiếu. Chưa tạo wrapper hoặc tuyên bố đã kiểm tách nền.

## Bàn giao và việc cần xem

Đã làm phần chuẩn bị có thể thực hiện trước phụ thuộc; **chưa giao sáu ảnh** vì lệnh thứ tự của chính phiếu, không phải do lỗi công cụ sinh. Tiếp tục khi 119 đã bàn giao hoặc chủ dự án cho phép đổi thứ tự. Lúc đó cần đọc hai ảnh 119 đã chọn để khớp nắng/màu, dùng `image_gen` tích hợp từng ảnh, lưu nguyên nguồn và prompt chính xác mọi lượt; xem ảnh lớn/nhỏ cùng các tờ kiểm trước khi chấm trên bản hậu kỳ.

Không chạy Git, dev server, trình duyệt, mạng, build hoặc test suite game. Không sửa phông cũ, mã game, công cụ chung hoặc tài liệu khác; không đọc/ghi Tu Tiên. Tờ đầu vào là ảnh kiểm tĩnh, không tạo khung chụp trình duyệt để dọn.

**Chủ dự án cần xem:** câu hỏi đổi thứ tự 119 → 120; **Claude cần quyết khi chấm:** xung đột nền bốn mép. Chưa có ảnh để Claude chấm nhận M/Q.
