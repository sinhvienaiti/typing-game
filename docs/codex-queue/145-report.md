# Phiếu 145 · Wordwoven · Mảnh UI nhỏ

Ngày làm: 30/10/2026, macOS, repo cha.

**Trạng thái: dừng do `image_gen` hết hạn mức; 0/7 ảnh, 0/28 PNG giao. Chưa hoàn tất, chưa tự chấm, chưa gửi nhận Claude.** Yêu cầu đầu tiên cho `keycap` trả HTTP 429, `usage_limit_reached`, trước khi có ảnh hoặc đường dẫn đầu ra. Không có ảnh thử để hậu kỳ; không dùng ảnh cũ hay hình dựng bằng mã thay thế.

## 1. Điều kiện đầu vào và phạm vi

Đã đọc phiếu 145, báo cáo 115 và 160, verdict 29/10, `ART_ACCEPTANCE.md` §2.2/§5, khối Wordwoven của chỉ đạo mỹ thuật 28/10, định dạng ảnh §3 và README `art-normalize`. Áp dụng skill `imagegen`, dùng công cụ sinh tích hợp theo yêu cầu.

Bốn trang trí 115 đã nhận và năm khung `.v2` của 160 có trong `art-src/ui/frames-epic/`, khác đường dẫn dự kiến `ui/frames/` trong phần luật chung. Đã dùng đúng thư mục hiện có. Báo cáo 160 còn ghi ngoại lệ rail và chờ Claude chấm lại; không tự coi các ngoại lệ đó đã được duyệt. Không tìm thấy việc chuyển `card-plate` hoặc `stamp-seal` vào danh sách ảnh khung 115; giữ đủ bảy mục trong phần chuẩn bị.

Tờ tham chiếu ghép đủ `banner`, `portrait-ring`, `crest`, `divider`; `panel-large`, `plate-long`, `button`, `button-active`, `tooltip` bản `.v2`; `keyart` 113 và ảnh mức chợ của chủ dự án. Đã mở xem tờ này và ảnh chủ dự án, crest, panel riêng. Mười một file tham chiếu chỉ đọc và có MD5 đối chiếu.

## 2. Đã làm và prompt

Gốc đường dẫn trong bảng: `games/typing-defense/art-src/`.

| Nội dung | Đường dẫn |
| --- | --- |
| Bảy prompt dự kiến lượt 1 | `ui/parts/<tên>.try1.prompt.txt` |
| Tập prompt nguyên văn | `_review/145/prompts.json` |
| Tờ tham chiếu đã đính kèm yêu cầu sinh | [_review/145/references.jpg](../../games/typing-defense/art-src/_review/145/references.jpg) |
| Nguồn và cách ghép tờ tham chiếu | `_review/145/references.prompt.txt` |
| Lỗi công cụ và mốc đặt lại hạn mức | `_review/145/generation-error.json` |
| Hồ sơ kiểm đường dẫn, nguồn, số file | `_review/145/audit.json` |
| Script dựng lại phần chuẩn bị | `_review/145/rebuild-preparation.py` |
| Script kiểm chỉ đọc và chụp MD5 | `_review/145/audit145.py` |

Mỗi prompt bắt đầu bằng **STYLE-UI nguyên văn** từ chỉ đạo mỹ thuật mới, tiếp theo là khối PART biên soạn cho mảnh vật liệu, phần riêng của vật, hướng dẫn tham chiếu và dòng nền M nguyên văn. Chọn M vì có ngọc xanh. PART giữ góc nhìn thẳng của STYLE-UI; không dùng khối ICON cũ có viền mực và góc 3/4 vì lệch hướng mỹ thuật mới. Dùng ba mốc ngọc của báo cáo 160: `#3B5530`, `#27351B`, `#131C0A`, đồng thời yêu cầu giữ biến thiên chất liệu tự nhiên.

| Tên | Nội dung prompt đã chuẩn bị | Thực tế gọi công cụ |
| --- | --- | --- |
| `keycap` | Đá vôi sáng, mặt phẳng trống, góc vuông mềm, vát rộng, một nét mây nhỏ ở phần vát dưới; đọc ở 16 px. | Một yêu cầu bị từ chối; không có ảnh. |
| `card-plate` | Ngọc sẫm, chỉ vàng mảnh, hai đầu đồng gọn, giữa yên theo chiều ngang; canvas 1536 × 512. | Chưa gọi. |
| `card-plate-review` | Cùng hình thẻ sẫm, lòng ngọc nhạt; sẽ đính kèm thẻ sẫm khi đã có ảnh. | Chưa gọi. |
| `stamp-seal` | Đĩa đồng tròn đầy, lòng trống rộng, nét khắc Đông Sơn chỉ ở vành vát. | Chưa gọi. |
| `pip-lit` | Hạt ngọc tròn, lõi ngọc vàng sáng; ánh mềm nằm trong đường bao đặc để tách nền sạch. | Chưa gọi. |
| `pip-unlit` | Cùng hình và vị trí hạt sáng, ngọc tối, phản sáng nhỏ; sẽ đính kèm hạt sáng khi đã có ảnh. | Chưa gọi. |
| `agent-badge` | Đĩa đồng tròn nhỏ, mặt hoàn toàn trống để game thêm số; vát hẹp. | Chưa gọi. |

Không có lượt 2/3 hoặc sửa prompt giữa các lượt. Bảy file `.try1.prompt.txt` là **prompt chuẩn bị**, không phải bằng chứng đã sinh đủ bảy lượt. Không tạo `.try1.png`, bản chọn hoặc bản thu giả khi công cụ chưa trả ảnh.

## 3. Lỗi chặn

Yêu cầu dùng `image_gen.imagegen`, nền magenta, `transparent_background=false`, đính kèm `references.jpg`. Công cụ trả:

```text
HTTP 429 Too Many Requests
error.type: usage_limit_reached
message: The usage limit has been reached
plan_type: plus
resets_at: 1793364445
resets_in_seconds: 66072
```

Mốc đặt lại do công cụ báo: **19:47:25 ngày 30/10/2026, Asia/Ho_Chi_Minh**. Đây là thông tin từ phản hồi lỗi, không bảo đảm yêu cầu sau mốc đó sẽ thành công. Không gọi lặp sáu ảnh còn lại khi cùng hạn mức đã hết; không chuyển sang CLI/API khác, không gọi mạng ngoài công cụ sinh ảnh.

## 4. Kiểm số và KA5

| Kiểm | Kết quả thực tế |
| --- | --- |
| KA1 trước ghi | Hai thư mục đích và báo cáo chưa tồn tại; tập file có trước rỗng, `md5-before.txt` có 0 dòng. |
| KA1 sau ghi | `md5-after.txt` băm bằng `md5 -r` toàn file chuẩn bị trong `ui/parts/`, `_review/145/` và báo cáo; `md5.diff.txt` chỉ có dòng thêm. Hai file snapshot sau/diff không tự băm chính chúng. Không có file cũ bị thay/xóa. |
| Tham chiếu | **11/11** nguồn trùng MD5 khi kiểm sau chuẩn bị. |
| Khổ/channels | **0/28 PNG**; chưa có ảnh để chạy `identify`. Không báo đạt. |
| Alpha ngoài dải mép 3 px | Chưa đo cho cả bảy ảnh. |
| Pixel nhiễm sắc khóa | Chưa đo cho cả bảy ảnh. |
| Hộp bao 68–72%, lệch tâm ≤ 2% | Chưa đo cho cả bảy ảnh. |
| Tương phản ở 720p/1080p | Chưa đo cho cả bảy ảnh. |
| IoU 32 px | Chưa đo cho cả bảy ảnh. |
| 9-slice hai thẻ, ba cỡ dựng, độ lệch chuẩn luma | Chưa thực hiện; chưa có đường cắt pixel để khai báo. |
| Tờ xem `_review/145-sheet.jpg` | Chưa có; `references.jpg` chỉ là tờ đầu vào, không thay tờ nghiệm thu. |
| Tờ “bản sinh · bản hậu kỳ” từng ảnh | Chưa có vì chưa có bản sinh. Không có bước hậu kỳ sửa tranh. |
| KA5 gốc và 720p, M mức chợ | **Chưa chấm** cả bảy ảnh; không có cơ sở cho điểm 0–2 hoặc công bố ≥ 8. |

Số file và danh sách thiếu từng ảnh có trong `audit.json`; MD5 chi tiết nằm cạnh script. Không dùng việc chuẩn bị đủ prompt để đánh dấu các kiểm ảnh đạt.

## 5. Mâu thuẫn phải giữ khi tiếp tục

- Bảng riêng yêu cầu hai thẻ **1536 × 512** và cùng hình; quy định chung lại nói mọi bản gốc 1024². Khi tiếp tục, ưu tiên khổ của bảng riêng, ghi ngoại lệ; không ép thẻ thành vuông làm méo vật.
- `stamp-seal`, `agent-badge` và hai hạt đều được yêu cầu **tròn**. Hai thẻ cũng yêu cầu cùng hình. Ngưỡng IoU ≤ 0,80 cho mọi cặp, chỉ miễn cặp hạt sáng/tắt, có thể mâu thuẫn với đúng đề. Phải đo thật rồi ghi các cặp vượt; giữ tranh đúng vật thể theo §5, không cắt khuyết hoặc bóp dáng để đạt số. Phiên này chưa có số IoU, không tự miễn kiểm.
- Mặt giữa hai thẻ cần kiểm luma ≤ 0,05 trên tranh đã sinh. Nếu phải san vân hoặc phủ màu mới đạt, dừng và trình Claude quyết theo §5, không làm phẳng phần vẽ.
- Dòng cấm “khung hay viền” trong luật chung được hiểu là khung trình bày bao ngoài; chỉ vàng và vành vát là nội dung vật thể được chính bảng riêng yêu cầu.

## 6. Tái lập và việc còn lại

Kiểm lại hồ sơ hiện có, chỉ đọc, không gọi mạng và không chạy test game:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 games/typing-defense/art-src/_review/145/audit145.py
```

Dựng lại tờ tham chiếu cùng bảy prompt vào một thư mục **mới** bên trong `_review/145/`:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 games/typing-defense/art-src/_review/145/rebuild-preparation.py recheck-01
```

Script từ chối thư mục đã có. Không chạy lại `--snapshot` trên hồ sơ đã giao vì quy định cấm ghi đè. Khi tiếp tục sinh bằng công cụ tích hợp, dùng prompt đã lưu, đính kèm tờ tham chiếu; riêng hai biến thể cần bổ sung ảnh thẻ sẫm/hạt sáng thực tế. Lưu nguyên byte mọi ảnh thử, sau đó mới tách nền, chuẩn hóa khổ/lề, xuất ba bản thu trực tiếp bằng Lanczos và làm đủ bảng số, tờ trước–sau, tờ cỡ dùng, KA5. `ART_MAGICK=/opt/homebrew/bin/magick`; Arial tại `/System/Library/Fonts/Supplemental/Arial.ttf`.

Không chạy bất kỳ lệnh Git, dev server, trình duyệt, build hoặc test suite. Không sửa mã, tài liệu khác, `public/`, game khác, `.wt-*`; không đọc/ghi các đường dẫn Tu Tiên. Không làm âm thanh. Không có frame trình duyệt để dọn.

**Chủ dự án cần biết:** chưa có ảnh mới để duyệt. Cần tiếp tục bảy ảnh sau khi công cụ sinh có hạn mức; toàn bộ kiểm nghiệm thu và chấm Claude vẫn còn, phiếu 145 chưa xong.
