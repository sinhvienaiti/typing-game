# Phiếu 147 · Dragonhold · Chân dung rồng và huy hiệu tốc độ

**Ngày giao:** 29/10/2026. **Trạng thái:** đủ 7 ảnh và 21 bản thu; kiểm số đạt. Codex tự chấm trên bản hậu kỳ. **Chưa có điểm chấm nhận của Claude**, chưa chép vào `public/`.

## 1. Ảnh đã làm và nguồn tham chiếu

- Ba chân dung: `games/dragon-hold/art-src/ui/portraits/{hoa-long,hoa-long-hurt,bach-long}.png`.
- Bốn huy hiệu: `games/dragon-hold/art-src/ui/icons/{pace-hatchling,pace-young,pace-adult,pace-elder}.png`.
- Mỗi ảnh có bản 1024² RGBA sRGB, ba bản `.256.png`, `.128.png`, `.64.png`, prompt tương ứng cạnh từng PNG; mọi lượt `.tryN.png` và `.tryN.prompt.txt` được giữ nguyên. Danh sách 28 PNG: `_review/147/delivery-manifest.json`.
- Tạo bằng công cụ tích hợp **image_gen**, 10 lượt cho 7 ảnh; không dùng API bên ngoài, Blender, trình duyệt hay dev server. Không chạy build/test game, không có lệnh Git.
- Đã đọc STYLE-UI mới trong `ART_DIRECTION_2026-10-28.md` §3.2 và phiếu 119; dùng mức hoàn thiện của HUD ảnh chủ dự án, không chép nội dung. Đã xem `skill-fire-breath.png`, `gold.png`, `ui/title/title-emblem.png`, `ui/title-epic/emblem.png` và ảnh mẫu chủ dự án trong game Wordwoven (chỉ đọc).

**Thiếu nguồn nhân vật:** `_refs/dragons/` chưa tồn tại lúc bắt đầu. Tìm chỉ đọc trong `games/dragon-hold/art-src/` theo `draconis`, `dragon`, `long`, và kiểm thêm `guide`, `white`: không có ảnh 2D Bạch Long riêng. Hỏa Long dùng `ui/title/title-emblem.png` làm nguồn dáng/màu; `ui/title-epic/emblem.png` của 119 làm mức hoàn thiện. Bạch Long dùng mô tả ngọc trai trong phiếu, cổ chữ S và sừng ngà để phân biệt. **Claude cần đối chiếu lại Bạch Long với model hướng dẫn khi có render**; không tuyên bố đã khớp GLB. Không dựng hay sửa model.

## 2. Prompt và từng lượt

Mỗi prompt tiếng Anh gồm nguyên khối STYLE-UI mới, khối PORTRAIT hoặc ICON, nội dung riêng và dòng nền M. Khối KIND nhấn khối lớn, dáng riêng, không nền cảnh/đĩa/khung/chữ. Hỏa Long dùng bố cục nằm trong một đường tròn tưởng tượng, không vẽ vòng tròn, để giữ luật cấm khung/viền. Prompt đầy đủ ở cạnh ảnh; nguồn công cụ lưu trong `_review/147/generation-manifest.json`.

| Ảnh | Lượt 1 | Sửa ở lượt 2 | Chọn |
|---|---|---|---|
| hoa-long | Vảy đỏ cam, bụng kem, sừng nâu, mắt hổ phách, dáng ba phần tư | Không cần | try1 |
| hoa-long-hurt | Chỉnh từ hoa-long: mắt hẹp, vảy nứt, khói; dáng giữ nguyên nhưng khói lan ra ngoài và mỏng | Yêu cầu khói bạc xám đặc, ngắn, hướng xuống phần má; giữ tư thế và đường bao. Bản sinh vẫn có một lọn nhô nhẹ khỏi mũi, được giữ nguyên, IoU đạt | try2 |
| bach-long | Vảy trắng ngọc trai, sáng lạnh, cổ thanh chữ S, nhìn trái | Không cần; giới hạn thiếu nguồn nhận diện ghi ở trên | try1 |
| pace-hatchling | Trứng nứt đứng, rồng ló mắt; IoU với chân dung đứng tới 0,812 | Trứng nghiêng trái, vỏ có đỉnh dài/ngắn bất đối xứng, khe mở riêng; giữ rồng và vỏ thành một vật | try2 |
| pace-young | Đầu rồng thấp, mõm ngắn, sừng nhỏ, mắt lớn | Không cần | try1 |
| pace-adult | Đầu trưởng thành, sừng đầy đủ nhưng trung bình quá tối trên vỏ cây | Tăng sáng mặt/sừng bằng ánh sáng phía trước, mặt đồng cam, hàm kem rộng; lượt 2 tăng rõ độ sáng. Sau đó chỉnh sáng toàn ảnh 10% trong giới hạn | try2 |
| pace-elder | Mặt chính diện, sừng ngang, ba ngọn vương miện lửa liền với đầu | Không cần | try1 |

Không ảnh nào dùng lượt 3. Các lượt cũ không bị ghi đè hoặc xóa. Bản sinh của công cụ là 1254²; giữ nguyên `.tryN.png`, bản giao chuẩn hóa xuống 1024², không ghi giả rằng nguồn sinh là 1024².

## 3. Hậu kỳ không phá tranh · ART_ACCEPTANCE §5

`_review/147/process.py` dùng Python chuẩn và ImageMagick 7 tại `/opt/homebrew/bin/magick`. Không cài gói, không ghi vào công cụ dùng chung.

1. Nền M sinh ra hơi lệch mã, chẳng hạn góc Hỏa Long là RGB 232/15/241. Tách nền theo độ trội magenta, rồi gỡ màu nền trộn ở dải 2 px của nguồn. Giữ màu trong ruột vật.
2. Cắt phần lề rỗng, thu **đồng tỷ lệ** bằng Lanczos để cạnh dài của vật là 717 px, đặt giữa canvas trong suốt 1024². Không bóp dáng.
3. Nhân RGB toàn ảnh 1,08 cho cặp Hỏa Long, 1,10 cho `pace-adult`, 1,00 cho bốn ảnh còn lại. Không chỉnh gamma, không phủ mảng, không vẽ bù, không làm nét.
4. Gỡ màu viền nhiễm bằng màu đặc gần nhất trong **dải mép 3 px**, giữ độ phủ alpha. Ở ngoài dải mép, làm tròn các alpha lẻ do nội suy thành 0/255. Chi tiết vẽ và khói được giữ; không cắt mất khói để đạt IoU. Log từng pixel alpha chỉnh và số pixel sửa màu nằm trong `release/*.post.json`.
5. Thu từng bản 256/128/64 **trực tiếp từ bản 1024**, Lanczos, không qua cỡ trung gian; chỉ làm sạch alpha ngoài dải mép. RGB của bản thu giữ nguyên kết quả Lanczos. Không làm nét bản 64. Bản Lanczos trước làm sạch alpha được giữ ở `release/*.lanczos.png`.

Các bản thử hậu kỳ `candidates-v1` tới `selected-clean` được giữ để truy vết; **chỉ thư mục `release/` là nguồn chép bản giao**. Không dùng điểm của bản sinh hoặc bản thử để thay điểm bản giao. Không có bước phải xóa/san phẳng phần vẽ để đạt số; các thay đổi dáng trứng và ánh sáng trưởng thành được giải quyết bằng lượt sinh mới.

## 4. Kiểm số

Luma: BT.709 trên sRGB mã hóa, trọng số 0,2126/0,7152/0,0722, chuẩn hóa 0–1, trung bình có trọng số alpha. Chênh luma đo trên hai nền chính xác của phiếu, ở cả hai cỡ game. Không dùng tương phản trên nền kem thay cho điều kiện nền tối.

Mép: dải Chebyshev 3 px quanh mặt nạ **alpha >16**, cùng ngưỡng với hộp bao. Số ngoài mép là số pixel alpha khác 0/255. Nhiễm màu khóa: hue cách 300° không quá 15°, S >0,5, tính trên pixel alpha >0. IoU dùng Lanczos 32 px, alpha >16; loại riêng cặp khỏe/bị thương khỏi phép so nhận diện khác nhau.

| Ảnh | Cạnh dài % | Lệch tâm X/Y % | Alpha lẻ ngoài mép (1024) | Nhiễm M % (1024) | ΔY vỏ cây 720p / 1080p | ΔY kem 720p / 1080p | IoU lớn nhất với ảnh khác | Cặp |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| hoa-long | 70.0195 | 0.0488/0.0488 | 0 | 0.021187 | 0.270302 / 0.270687 | 0.487589 / 0.487203 | 0.726471 | bach-long |
| hoa-long-hurt | 70.0195 | 0.0488/0.0488 | 0 | 0.021349 | 0.261769 / 0.262048 | 0.496122 / 0.495843 | 0.728070 | bach-long |
| bach-long | 70.0195 | 0.0000/0.0488 | 0 | 0.000000 | 0.563793 / 0.564131 | 0.194097 / 0.193759 | 0.728070 | hoa-long-hurt |
| pace-hatchling | 70.0195 | 0.0000/0.0488 | 0 | 0.000000 | 0.443443 / 0.442774 | 0.314447 / 0.315116 | 0.717647 | hoa-long |
| pace-young | 70.0195 | 0.0488/0.0488 | 0 | 0.000000 | 0.258086 / 0.257936 | 0.499804 / 0.499954 | 0.639640 | pace-hatchling |
| pace-adult | 70.0195 | 0.0000/0.0488 | 0 | 0.002207 | 0.255851 / 0.255446 | 0.502040 / 0.502444 | 0.706231 | pace-hatchling |
| pace-elder | 70.0195 | 0.0000/0.0488 | 0 | 0.006719 | 0.257731 / 0.257277 | 0.500159 / 0.500614 | 0.651466 | pace-hatchling |

**Alpha của đủ 28 file giao** (mỗi ô là `số alpha lẻ ngoài mép / % nhiễm M`):

| Ảnh | 1024 | 256 | 128 | 64 |
|---|---:|---:|---:|---:|
| hoa-long | 0 / 0.021187 | 0 / 0.026849 | 0 / 0.000000 | 0 / 0.075075 |
| hoa-long-hurt | 0 / 0.021349 | 0 / 0.021240 | 0 / 0.000000 | 0 / 0.000000 |
| bach-long | 0 / 0.000000 | 0 / 0.006321 | 0 / 0.023702 | 0 / 0.000000 |
| pace-hatchling | 0 / 0.000000 | 0 / 0.000000 | 0 / 0.000000 | 0 / 0.000000 |
| pace-young | 0 / 0.000000 | 0 / 0.006073 | 0 / 0.000000 | 0 / 0.000000 |
| pace-adult | 0 / 0.002207 | 0 / 0.016634 | 0 / 0.041649 | 0 / 0.000000 |
| pace-elder | 0 / 0.006719 | 0 / 0.007127 | 0 / 0.053093 | 0 / 0.000000 |

28/28 PNG đúng khổ và kênh `srgba` (IM7 in thêm `4.0`), alpha ngoài dải mép bằng 0, nhiễm M ≤0,2%. 21/21 bản thu khớp Lanczos trực tiếp từ bản gốc kèm đúng quy tắc làm sạch alpha; không sharpen. Chi tiết: `_review/147/alpha-all-delivered.json`, `_review/147/identify-delivered.txt`, `release/metrics.json` và toàn bộ 21 cặp IoU trong đó.

- Cặp Hỏa Long khỏe/bị thương: IoU 1024 = **0.989752**, IoU 32 = **0.987539**; đạt cả ≥0,90 riêng và ≥0,95 cho biến thể cùng vật. Phần khói nhô nhẹ giải thích chênh lệch còn lại, không bị xóa.
- Ở 46 px: **có** điểm mắt sáng và sừng tách dáng; vết nứt nhỏ giảm chi tiết, khói và mắt nheo làm trạng thái bị thương rõ hơn.
- Bạch Long ở 19 px: **có** khác biệt với Hỏa Long về trắng/lạnh, mặt nhìn trái, cổ thanh; mắt xanh không còn là chi tiết đọc ổn định ở cỡ này.
- Bốn huy hiệu ở 20 px: **có**, xếp được `hatchling → young → adult → elder` bằng vỏ trứng nghiêng → đầu thấp sừng nhỏ → sừng dài mở V → vương miện lửa. Không dựa chỉ vào đỏ/lục.

**KA1:** đã dùng `/sbin/md5 -r` với mọi file có sẵn trong hai thư mục đích trước khi ghi; thêm toàn bộ vùng kiểm 147 vào lần sau. `md5-before.txt`: **791 file**; `md5-after.txt`: **1824 file**; diff **1033 dòng thêm, 0 dòng mất/đổi**. Không có file cũ đổi MD5. Snapshot không tự băm chính nó; diff/tóm tắt được sinh sau snapshot. Không dùng Git để kiểm. Thư mục icon dùng chung có thể nhận thêm file từ tác vụ khác trong thời gian chạy; bảng này băm toàn thư mục, không nhận công những file ngoài `delivery-manifest.json`.

## 5. KA5 tự chấm trên bản hậu kỳ

Thứ tự năm tiêu chí: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. M chấm theo mức hoàn thiện HUD thương mại của ảnh chủ dự án và 119; không yêu cầu icon có ba lớp phong cảnh. Tất cả kiểm số đã đạt trước khi cho Dùng tiếp =2.

| Ảnh | Năm điểm ở 1024 | Q 1024 | Năm điểm ở cỡ 720p | Q 720p | M 1024 / 720p |
|---|---|---:|---|---:|---:|
| hoa-long | 2 / 2 / 1,5 / 2 / 2 | 9,5 | 2 / 1,5 / 1,5 / 2 / 2 | 9 | 8,5 / 8 |
| hoa-long-hurt | 2 / 2 / 1,5 / 2 / 2 | 9,5 | 2 / 1,5 / 1,5 / 2 / 2 | 9 | 8,5 / 8 |
| bach-long | 1,5 / 2 / 1,5 / 2 / 2 | 9 | 1,5 / 1,5 / 1,5 / 2 / 2 | 8,5 | 8 / 8 |
| pace-hatchling | 2 / 2 / 1,5 / 2 / 2 | 9,5 | 2 / 1,5 / 1,5 / 2 / 2 | 9 | 8,5 / 8 |
| pace-young | 2 / 2 / 1,5 / 2 / 2 | 9,5 | 2 / 1,5 / 1,5 / 2 / 2 | 9 | 8,5 / 8 |
| pace-adult | 2 / 2 / 1,5 / 2 / 2 | 9,5 | 2 / 1,5 / 1,5 / 2 / 2 | 9 | 8,5 / 8 |
| pace-elder | 2 / 2 / 1,5 / 2 / 2 | 9,5 | 2 / 1,5 / 1,5 / 2 / 2 | 9 | 8,5 / 8 |

Giới hạn điểm: vảy/mắt hoàn thiện hơn bộ icon cũ nhưng hơi bóng, cần Claude kiểm mức hòa bộ với HUD mới; giảm Hợp bộ còn 1,5. Tại 19–20 px, đọc bằng khối lớn, không còn đủ chi tiết mặt/vảy như cỡ 1024 nên giảm Đọc được. Bạch Long giảm Đúng đề vì chưa có nguồn model/2D gốc để xác thực nhận diện. M 720p giữ ở 8: đạt mức phát hành được theo tự chấm, chưa coi là HUD hàng đầu. Không tự nhận đã được Claude chấp thuận.

## 6. Tờ xem và cách chạy lại

Các đường dẫn dưới đây tương đối từ repo cha:

- [Tờ bốn hàng đúng phiếu](../../games/dragon-hold/art-src/_review/147-sheet.jpg).
- [Chi tiết pixel cỡ 720p, phóng Point ×6 để xem](../../games/dragon-hold/art-src/_review/147-small-detail.jpg); tờ chính vẫn giữ đúng pixel thật.

- [Bản sinh | bản hậu kỳ · hoa-long](../../games/dragon-hold/art-src/_review/147-hoa-long-before-after.jpg).
- [Bản sinh | bản hậu kỳ · hoa-long-hurt](../../games/dragon-hold/art-src/_review/147-hoa-long-hurt-before-after.jpg).
- [Bản sinh | bản hậu kỳ · bach-long](../../games/dragon-hold/art-src/_review/147-bach-long-before-after.jpg).
- [Bản sinh | bản hậu kỳ · pace-hatchling](../../games/dragon-hold/art-src/_review/147-pace-hatchling-before-after.jpg).
- [Bản sinh | bản hậu kỳ · pace-young](../../games/dragon-hold/art-src/_review/147-pace-young-before-after.jpg).
- [Bản sinh | bản hậu kỳ · pace-adult](../../games/dragon-hold/art-src/_review/147-pace-adult-before-after.jpg).
- [Bản sinh | bản hậu kỳ · pace-elder](../../games/dragon-hold/art-src/_review/147-pace-elder-before-after.jpg).

Hàng 4 của tờ chính: `skill-fire-breath`, `gold`, `dragon-rage`, `hard-scale` có sẵn, mảnh HUD ảnh mẫu và emblem 119, cùng chiều cao 160 px. Lấy mức hoàn thiện từ HUD, không chép nội dung. **Tự đánh giá đứng cạnh được ở mức 8; cần Claude chấm lại**, nhất là Bạch Long và bốn huy hiệu 20 px. Đã xem trực tiếp các PNG 1024 và tờ cỡ game, không chỉ xem bản sinh.

Script trong `_review/147/`: `process.py`, `boards.py`, `validate.py`, `deliver.py`, `snapshot.py`, `write-report.py`. Python chỉ dùng thư viện chuẩn. Ví dụ chạy lại hậu kỳ vào thư mục mới (các script từ chối ghi đè):

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
python3 games/dragon-hold/art-src/_review/147/process.py --out games/dragon-hold/art-src/_review/147/replay-01
python3 games/dragon-hold/art-src/_review/147/validate.py --assets games/dragon-hold/art-src/_review/147/replay-01 --out games/dragon-hold/art-src/_review/147/replay-01-check.json
python3 games/dragon-hold/art-src/_review/147/boards.py --assets games/dragon-hold/art-src/_review/147/replay-01 --out games/dragon-hold/art-src/_review/147/replay-01-boards
```

Font tờ xem: `/System/Library/Fonts/Supplemental/Arial.ttf`. `deliver.py` chỉ chạy khi kiểm số đạt, chép với chế độ không ghi đè. `snapshot.py <đường-dẫn-mới>` cho lần kiểm tiếp theo. Không dùng `tools/art-normalize` để tránh phát sinh file tạm ngoài phạm vi; thuật toán hậu kỳ riêng được lưu đầy đủ tại đây.

## 7. Khác phiếu, phần để lại cho người nhận

- Không có render ba góc, không có ảnh 2D Bạch Long riêng: đã dùng nguồn 2D Hỏa Long được phép và mô tả Bạch Long; cần Claude đối chiếu model sau. Không đọc hay ghi Tu Tiên, không đụng `.wt-*`, không ghi game khác.
- Nguồn sinh 1254² do công cụ tích hợp quyết định; chỉ bản giao và ba bản thu mới đúng các khổ yêu cầu. Mọi nguồn và prompt giữ nguyên.
- “Trong vòng tròn” được hiểu là bố cục bust tròn, không vẽ khung/vòng, theo luật cấm viền của phiếu.
- Có thêm làm sạch alpha sau nội suy ở cả ba cỡ, vì Lanczos thuần tạo pixel lẻ ngoài dải mép. Không thay RGB, không sharpen, không xóa phần vẽ. Đã lưu cả bản Lanczos trước làm sạch để kiểm lại.
- Không cập nhật `ART_REPLACE_LATER.md` hay tài liệu khác vì phiếu chỉ cho phép báo cáo này. Ảnh ở mức M=8 cần người nhận theo dõi nâng chất lượng khi duyệt.
- Không gắn mã hay chép `public/`; Claude chấm nhận từ 8 rồi mới thực hiện bước gắn. Chủ dự án cần xem tờ chính, cặp Hỏa Long và nhận diện Bạch Long. Không có âm thanh trong phạm vi phiếu.

