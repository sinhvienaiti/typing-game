# Phiếu 196 · Dragonhold · Ổ icon và khung thanh HUD

**Ngày:** 30/10/2026. **Thực hiện:** Codex trên Mac mini, công cụ `image_gen` tích hợp.

**Chưa hoàn thành: công cụ sinh ảnh hết hạn mức ngay lần gọi đầu tiên. Không có ảnh trả về; chưa có bản chọn để chấm hay nghiệm thu.** Giữ hồ sơ chuẩn bị và KA1; không gán điểm M/Q khi chưa có bản hậu kỳ.

## 1. Chỗ dừng và tài liệu đã tạo

Lần gọi `image_gen.imagegen` cho `skill-slot`, lượt 1, trả `http 429 Too Many Requests`, loại lỗi `usage_limit_reached`. Công cụ báo `resets_in_seconds: 41752`, `resets_at: 1793364446`, tương ứng **19:47:26 ngày 30/10/2026, giờ Việt Nam**. Đây là thời điểm do dịch vụ báo, không phải cam kết lần gọi sau chắc chắn thành công. Không gọi tiếp bảy ảnh còn lại vì cùng hạn mức; không chuyển sang CLI/API hay dịch vụ ngoài.

- Tám prompt đã chuẩn bị: [`ui/sockets/`](../../games/dragon-hold/art-src/ui/sockets/), mỗi tên có `.try1.prompt.txt`. Chỉ prompt `skill-slot` đã được gửi. Không có `.try1.png`; không tạo file ảnh giả để lấp chỗ.
- Hồ sơ: [`_review/196/README.md`](../../games/dragon-hold/art-src/_review/196/README.md), [`prompts.json`](../../games/dragon-hold/art-src/_review/196/prompts.json), [`generation-status.json`](../../games/dragon-hold/art-src/_review/196/generation-status.json).
- Script đã chạy: [`audit.py`](../../games/dragon-hold/art-src/_review/196/audit.py). Script và hồ sơ nằm đúng làn cho phép, không sửa công cụ dùng chung.
- `docs/codex-queue/196/` đã tạo, hiện rỗng; chưa có hồ sơ ảnh để đặt vào đó.

Đã đọc phiếu 115, 162, báo cáo 162 và 146, luật `ART_ACCEPTANCE.md` §5, thang M, README/thuật toán tách nền và CSS các ô/thanh. Đã xem ảnh tham chiếu chủ dự án cùng tờ `162-selected.jpg`; đọc JSON `plate-long` và `panel-large`. Chưa dựng thử với icon, nên chưa công bố đã dùng phiên bản icon nào.

## 2. Prompt và số lượt gọi

Giữ nguyên khối STYLE-UI, phần riêng, SOCKET/BAR và nền M của phiếu. Chỉ bổ sung câu bố cục cuối: ảnh vuông 1024 × 1024, ổ giữa ảnh có lề nền hẹp; thanh dùng tỷ lệ 3:1, 1536 × 512. Không có lượt sửa prompt sau sinh vì chưa nhận được ảnh. Hai prompt dẫn xuất có dòng SAME, chỉ được gọi khi đã có bản gốc được chọn và đính kèm đúng ảnh đó.

| Tên | Lần gọi công cụ | Ảnh trả về | Trạng thái |
| --- | ---: | ---: | --- |
| skill-slot | 1 | 0 | Bị từ chối do hạn mức trước khi trả ảnh |
| skill-slot-ready | 0 | 0 | Chờ bản skill-slot được chọn để sửa ảnh |
| item-cell | 0 | 0 | Chưa gọi |
| item-cell-armed | 0 | 0 | Chờ bản item-cell được chọn để sửa ảnh |
| icon-socket | 0 | 0 | Chưa gọi |
| star-socket | 0 | 0 | Chưa gọi |
| hp-bar-frame | 0 | 0 | Chưa gọi |
| rage-bar-frame | 0 | 0 | Chưa gọi |

Tổng **1 lần gọi, 0 lượt sinh thành công**, chưa ảnh nào vượt ba lần gọi. Các prompt chưa gửi chỉ là bản chuẩn bị, không phải bằng chứng công cụ đã chạy.

## 3. Kiểm 1–10

| Mục | Số đo / kết quả |
| --- | --- |
| 1 · KA1 | Trước **1.395** file, sau **1.403** file; **8 dòng thêm**, **0 dòng đổi**, **0 dòng mất**. Mọi dòng thêm đều là prompt dưới `ui/sockets/`. |
| 2 · Khổ/kênh | **0 ảnh giao**; không có dữ liệu `identify`, chưa kiểm được khổ hay srgba. |
| 3 · Alpha | **0 alpha**; min/max, dải mép 3 px, hue khóa, thành phần rời và mép 4× đều chưa đo. |
| 4 · Cặp dẫn xuất | **0/2 cặp** có ảnh; chưa đo IoU, lệch hộp bao hay chênh luma lòng ổ. |
| 5 · JSON tọa độ | **0/8 file**; chưa có nguồn alpha nên không suy đoán `well`, `trough`, `content` hoặc đường cắt. |
| 6 · Đoạn giữa | **0/2 thanh** có ảnh; chưa đo σ luma, chưa dựng 12 kích thước thanh. |
| 7 · Tương phản icon | **0 cặp đã đo**; chưa có well để đo. `star-unlit` vẫn chưa kiểm ngưỡng 0,25. |
| 8 · Cỡ 720p | **0/8 ảnh** được xem ở cỡ dùng; icon-socket 22/28 px đều chưa kết luận. |
| 9 · Tờ xem | **0 tờ mới**; chưa có raw-vs-final, edge, sheet, hai mock hoặc vs-ref. |
| 10 · KA5 | M/Q của tám ảnh và M của hai mock: **chưa chấm**. `strict_acceptance_pass: false`. |

Hồ sơ KA1: [trước](../../games/dragon-hold/art-src/_review/196/md5-before.txt), [sau](../../games/dragon-hold/art-src/_review/196/md5-after.txt), [diff](../../games/dragon-hold/art-src/_review/196/md5-diff.txt), [JSON](../../games/dragon-hold/art-src/_review/196/ka1.json). Snapshot trước được chụp khi `sockets/` vừa tạo và còn rỗng; bao phủ mọi file UI tồn tại lúc bắt đầu.

## 4. Bộ 162 tham chiếu

Đã xem tờ bộ 162; các hash bản `.png` được chụp từ KA1 trước như sau. Không ghép chúng vào mock nào trong lượt này. Hash alpha và JSON kèm theo nằm trong [references-md5.txt](../../games/dragon-hold/art-src/_review/196/references-md5.txt).

| Tệp trong `ui/frames/` | MD5 |
| --- | --- |
| panel-large.png | `8c6253f95c498be7a3e1f6a17a16270f` |
| plate-long.png | `5505862916496f601f7b119319a629bd` |
| button.png | `beac3e2deffec398f183d739533917fc` |
| button-active.png | `34d4a4f2a3e944d713fca806fbd805c1` |
| banner.png | `28f41e2f9e502cc782e2aac6c95bcf52` |
| tooltip.png | `8d167c913568403ba9d6f20860cc0731` |
| portrait-ring.png | `6658c4bd87ad9cd8ae43b34028619039` |
| crest.png | `f06c757051a9290edd243cd1ab726613` |
| divider.png | `0b0d4bc6fbaab04c3fb9a9d7f6d5eed7` |

## 5. Phần còn lại và khác phiếu

Toàn bộ bước sinh ảnh, chọn bản, tách nền nguyên độ phân giải, Lanczos, JSON tọa độ, đo kiểm hình và dựng tờ/mock còn nguyên do lỗi hạn mức. Không có xử lý phá tranh hay ngoại lệ ngưỡng số trong lượt này vì chưa có tranh. Chưa đạt điều kiện “xong khi”; Claude chưa thể chấm nhận.

Chỉ ghi vào `ui/sockets/`, `_review/196/` và báo cáo này; thư mục báo cáo `196/` còn rỗng. Không chạy lệnh Git, build, test suite, dev server, trình duyệt hay mạng ngoài công cụ sinh ảnh. Không ghi đè hoặc xóa file cũ; không động mã game, icon, khung 162 hay Tu Tiên. Không sinh âm thanh.

**Người tiếp nhận cần xem:** lỗi và thời điểm đặt lại trong `generation-status.json`; khi công cụ hoạt động lại, tiếp tục sáu ảnh gốc rồi hai lượt sửa ảnh dẫn xuất. Chưa có hình cần chủ dự án duyệt ở thời điểm này.
