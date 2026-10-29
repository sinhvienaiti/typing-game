# Phiếu 119 · Dragonhold · Màn tựa, ảnh chủ đạo và logo

Ngày kiểm: 29/10/2026, macOS, repo cha.

**Chưa hoàn thành: 0/5 bản chọn, chưa gọi `image_gen`.** Phiếu yêu cầu **“Thứ tự: sau 118”**. [Báo cáo 118](118-report.md) hiện ghi chưa sinh ảnh, chưa có bản chọn và đang chờ 117. Đã gửi câu hỏi trong phiên để chủ dự án quyết định giữ thứ tự hay cho phép sinh 119 ngay; chưa có trả lời tại lúc ghi báo cáo. Chưa tự đổi thứ tự và chưa tiêu lượt sinh nào.

## Đã chuẩn bị

- Đọc chỉ đạo mỹ thuật 28/10, thang M và bible Dragonhold §3; đọc `ART_ACCEPTANCE.md`, gồm §5 về hậu kỳ không phá tranh, cùng README và mã liên quan của `tools/art-normalize`.
- Đã xem ảnh tham chiếu chủ dự án; huy hiệu 096 để lấy màu Hỏa Long; ba icon lửa/tim; lính rêu, sói héo, cung thủ rêu, cờ rêu; ảnh map A2 và phông `pine-river-far.png` cũ.
- [Tờ đọc đầu vào](../../games/dragon-hold/art-src/_review/119/inputs.jpg) ghi rõ vai trò các ảnh; **không phải tờ so nghiệm thu, không phải ảnh mới**. Màu nhận diện cần giữ: rồng đỏ cam, bụng kem, sừng/gai nâu sẫm; quái gỗ/rêu, giáp đá có gân vàng xanh, vải tím xám. Tầm vóc và ánh sáng của huy hiệu cũ không phải chuẩn mới.
- Đã chuẩn bị năm prompt, giữ nguyên khối STYLE, STYLE-UI và phần nội dung tương ứng. Riêng `logo` thay câu cấm chữ cuối STYLE-UI bằng đúng khối LOGO, như phiếu yêu cầu.
- [Manifest](../../games/dragon-hold/art-src/_review/119/manifest.json) giữ nguyên toàn bộ prompt, khổ dự kiến và danh sách ảnh sẽ đính kèm. **Các `.try1.prompt.txt` chỉ là prompt dự kiến, chưa gửi công cụ**, nên không được hiểu là đã có lượt sinh thứ nhất.

| Ảnh | Prompt đã lưu dưới `games/dragon-hold/art-src/ui/title-epic/` | Khổ dự kiến | Phần bổ sung sau khối nguyên văn |
|---|---|---|---|
| `title-backdrop` | `title-backdrop.try1.prompt.txt` | 1536 × 1024 | Bố cục cho bản cắt giữa 16:9; vùng trời và lan can yên theo tọa độ kiểm, giữ vân đá và ánh sáng tự nhiên. |
| `keyart` | `keyart.try1.prompt.txt` | 1536 × 1024 | Vai trò ảnh đính kèm: huy hiệu chỉ lấy màu rồng; lính rêu và sói chỉ lấy dáng/màu. Giữ nguyên câu REF và câu tham chiếu quái. |
| `poster` | `poster.try1.prompt.txt` | 1024 × 1536 | Cùng khoảnh khắc KEYART, dựng lại dọc, trời yên ở một phần tư trên; chỉ đính kèm `keyart.png` sau khi chọn và xem. |
| `logo` | `logo.try1.prompt.txt` | 3072 × 1024 | Tỷ lệ 3:1, lề trống ít nhất 64 px, đủ mười chữ và lòng chữ rõ. |
| `emblem` | `emblem.try1.prompt.txt` | 1024 × 1024 | Lề trống ít nhất 64 px, trang trí liền khối; cổng, hai đỉnh núi và rồng trưởng thành đọc riêng ở 64 px. |

Chưa có ảnh nên chưa có lượt sửa prompt theo lỗi sinh, chưa chọn ứng viên và chưa sao prompt thành bản chọn. Không tạo ảnh bằng font hoặc hình vẽ mã để thay công cụ sinh.

## KA1 sau phần chuẩn bị

Đã dùng **`md5 -r` trên mọi file trong `games/dragon-hold/art-src/ui/`, đệ quy**, gồm prompt. Mốc trước được ghi trước mọi lần ghi vào UI.

| Số đo | Kết quả |
|---|---:|
| File trước | 439 |
| File sau chuẩn bị | 444 |
| Thêm | 5 prompt mới, đúng năm tên của phiếu |
| Đổi nội dung file cũ | 0 |
| Mất file cũ | 0 |
| PNG lượt sinh | 0 |
| PNG bản chọn | 0 |

Chứng cứ: [MD5 trước](../../games/dragon-hold/art-src/_review/119/md5-before.txt), [MD5 sau chuẩn bị](../../games/dragon-hold/art-src/_review/119/md5-after-preparation.txt), [diff từ lệnh `diff -u`](../../games/dragon-hold/art-src/_review/119/md5-preparation-diff-command.txt), [JSON kiểm](../../games/dragon-hold/art-src/_review/119/ka1-preparation.json). Diff không có dòng nội dung bị xóa hoặc thay; chỉ thêm năm prompt. Đây là mốc **sau chuẩn bị**, chưa phải mốc sau bàn giao năm ảnh. Khi tiếp tục phải ghi mốc sau bằng tên mới, không ghi đè mốc này.

## Script đã chạy

Tất cả nằm trong [thư mục `_review/119/`](../../games/dragon-hold/art-src/_review/119/), chỉ tạo tên mới và từ chối ghi đè.

- `prepare.py`: chụp MD5 trước; trích khối prompt nguyên văn từ phiếu; ghi năm prompt và manifest.
- `inputs.py`: dựng tờ đầu vào bằng ImageMagick 7, không sửa nguồn. Font `/System/Library/Fonts/Supplemental/Arial.ttf`.
- `audit.py`: chụp MD5 sau chuẩn bị bằng `md5 -r`, chạy `diff -u`, đối chiếu từng hash, kiểm cả năm prompt khớp manifest và ghi khổ các ảnh đầu vào. Chạy với `python3 -B` để không sinh `__pycache__`.

Lệnh đã chạy từ repo cha:

```sh
python3 games/dragon-hold/art-src/_review/119/prepare.py
python3 games/dragon-hold/art-src/_review/119/inputs.py
python3 -B games/dragon-hold/art-src/_review/119/audit.py
```

Các script trên tái tạo được từ đầu khi đích chưa tồn tại; không chạy lại vào tên đã có. Chưa chạy tách nền; khi làm bước đó phải đặt `ART_MAGICK=/opt/homebrew/bin/magick` và kiểm nơi ghi tạm của công cụ, vì WORK mặc định `tools/art-normalize/.tmp/` nằm ngoài phạm vi ghi của phiếu. Không được âm thầm ghi ra đó.

## Chưa làm và điều kiện tiếp tục

| Kiểm bắt buộc | Trạng thái |
|---|---|
| 2 · Khổ ảnh giao | Chưa có ảnh; các khổ trong bảng là yêu cầu, không phải kết quả đo. |
| 3 · Mười chữ Dragonhold, tờ từng chữ 4× | Chưa có logo; chưa kiểm chính tả. |
| 4 · Không chữ lạc | Chưa có ảnh mới để xem. |
| 5 · Alpha, sắc khóa, đốm rời, lề và tờ mép 4× | Chưa tách nền; chưa đo, không gán số 0. |
| 6 · Luma vùng logo/menu, `119-title-mock.jpg` | Chưa đo, chưa dựng mock. |
| 7 · Đúng màu/dáng, `119-models.jpg` | Đã đọc nguồn; chưa có bản mới để kết luận khớp. |
| 8 · Đọc nhỏ 384 px và huy hiệu 64 px | Chưa có ảnh để kiểm. |
| 9 · `119-vs-ref.jpg` | Chưa dựng; chưa kết luận “đứng cạnh được”. |
| 10 · M/Q của từng bản chọn, đầy đủ và cỡ nhỏ | **Chưa chấm** cả năm ảnh; không có cơ sở công bố đạt. |
| §5 · Tờ “bản sinh | bản hậu kỳ” mỗi ảnh | Chưa có nguồn sinh hoặc bản hậu kỳ. |

Tiếp tục khi 118 đã bàn giao hoặc chủ dự án cho phép làm 119 trước. Dùng `image_gen` tích hợp, tối đa ba lượt mỗi ảnh; giữ nguyên byte mọi nguồn `.tryN.png` cùng prompt chính xác. Poster phụ thuộc keyart đã chọn. Hậu kỳ chỉ cắt/thu, tách nền và sửa mép trong giới hạn §5; nếu ngưỡng luma hoặc alpha buộc phá phần vẽ thì giữ tranh và ghi mâu thuẫn cho Claude. Sau đó xem đủ bản lớn, bản nhỏ, tờ trước/sau, mock, tờ so tham chiếu rồi chấm M/Q trên bản giao.

Không có ngoại lệ về nội dung ảnh hoặc hậu kỳ vì chưa sinh. Phần chưa làm là do thứ tự phụ thuộc, không phải ảnh đã trượt ba lượt. Chưa tạo âm thanh, chưa tích hợp runtime; không chạy Git, dev server, trình duyệt, mạng, build hay test suite của game. Không sửa ảnh cũ, mã game, tài liệu khác; không đọc/ghi Tu Tiên. Tờ đầu vào là ảnh kiểm tĩnh trong phạm vi cho phép, không có khung chụp trình duyệt cần dọn.

**Chủ dự án cần xem:** quyết định giữ thứ tự 118 → 119 hay cho phép sinh 119 ngay. Chưa có bộ ảnh để Claude chấm nhận.
