# Phiếu 020b · Lời Gọi · Chân dung Mộc Tinh (C21)

Ngày 27/10/2026. Tạo bằng công cụ tích hợp `image_gen`, dùng ảnh gốc Mộc Tinh làm mẫu nhận diện và ba ảnh Draconis, Chăm vui, Đại Bàng Tinh làm mẫu phong cách. Đã đọc prompt gốc, C21 trong `ART_FIX_QUEUE.md` §2 và thang điểm trong `ART_ACCEPTANCE.md` §1, §2.2.

**Bản chọn:** [moc-tinh.try1.png](../../games/typing-defense/art-src/portraits/moc-tinh.try1.png), Codex tự chấm **8,5/10 — Đạt ngưỡng 2D**. Dừng sau một lượt theo phiếu. **Chờ Claude chấm lại trước khi thay ảnh**; chưa ghi đè hoặc tích hợp vào game.

## Từng lượt

Thứ tự năm điểm trong bảng: **Đúng đề / Đọc được trong game / Hợp bộ / Hình khối / Dùng được cho bước sau**. Chấm trên ảnh thu nhỏ thật ở 128 px và 64 px, xem cạnh Draconis trong tờ đối chiếu.

| Lượt | Prompt thêm | Điểm 5 tiêu chí | Tổng | Còn thiếu |
|---|---|---|---|---|
| 1 | Giữ nguyên prompt cũ rồi thêm chỉ dẫn ưu tiên: đầu–tán–ngực, mặt lớn, bỏ chân/tay khỏi khung, viền mực tối, một nét cọ tím `#6B3FA0` sau vai có đầu đậm và đuôi khô, nền xanh lá `#00FF00`, khổ 1254×1254. Đính kèm Mộc Tinh gốc và ba mẫu cùng bộ. | 128 px: **1,5 / 1,5 / 1,5 / 2 / 2**. 64 px: **1,5 / 1,5 / 1,5 / 2 / 2**. | **8,5/10**, đạt theo tự chấm ở cả hai cỡ. | Nét cọ đã có sợi và khoảng đứt tự nhiên nhưng sắc tím sáng hơn mẫu hex yêu cầu; mặt còn nhiều chi tiết ở 64 px, tán chiếm khá nhiều diện tích; màu và tương phản hơi rực hơn Chăm. Claude cần kiểm lại các điểm này. |

- **Đúng đề (1,5):** giữ mắt hổ phách, lông mày gỗ, râu rễ, thân gỗ sáng, tán xanh và quả cam; chỉ còn đầu, tán, vai và ngực. Có một nét cọ chéo, đoạn giữa bị thân che. Trừ sắc tím chưa sát `#6B3FA0`.
- **Đọc được trong game (1,5):** ở 128 px đọc rõ mắt, mũi, miệng, râu và chùm quả; ở 64 px vẫn nhận ra mặt cây già và hướng nhìn, nhưng các đường gỗ nhỏ và tán lá dày làm nét mặt hơi bận. Mặt lớn hơn rõ rệt so với bản gốc và bản 017.
- **Hợp bộ (1,5):** giữ màu ấm, mảng vẽ truyện tranh và đường mực tối; màu hơi rực, tương phản nhỉnh hơn Chăm. Nét cọ tím có rãnh sợi, mép xước và đuôi khô, cải thiện lỗi dải phẳng của 017.
- **Hình khối (2):** mặt và thân gỗ nhất quán, không thấy lỗi lớn ở hai cỡ kiểm; không có chân hay bàn tay trong khung.
- **Dùng được cho bước sau (2):** bản giao 1254×1254, PNG sRGB 8-bit, nền ngoài đã khóa xanh lá, bốn góc xanh đúng giá trị. Có prompt nguyên văn và bản thô để truy lại.

Prompt chính xác gửi công cụ: [moc-tinh.try1.prompt.txt](../../games/typing-defense/art-src/portraits/moc-tinh.try1.prompt.txt). Phần bổ sung ghi rõ thay thế chỉ dẫn nền xanh dương và khổ 1024 trong prompt cũ; không sửa prompt gốc.

## Kiểm bắt buộc

### 1. Md5 trước và sau

Dùng `md5 -r` cho mọi file trong `portraits/`, sắp theo đường dẫn, gồm cả PNG và prompt:

- [md5-before.txt](../../games/typing-defense/art-src/_review/020b/md5-before.txt): **43 file**.
- [md5-after.txt](../../games/typing-defense/art-src/_review/020b/md5-after.txt): **48 file** tại thời điểm kiểm.
- [md5-diff.txt](../../games/typing-defense/art-src/_review/020b/md5-diff.txt): diff đầy đủ, giữ nguyên cả thay đổi đồng thời.
- [md5-check.json](../../games/typing-defense/art-src/_review/020b/md5-check.json): kết quả đối chiếu tự động.

**Cả 43 file có từ trước giữ nguyên md5; không file nào bị xóa. Điều kiện diff chỉ có `moc-tinh.try*` CHƯA ĐẠT trên thư mục dùng chung**, vì trong lúc thực hiện xuất hiện thêm ba file ngoài phiếu, phù hợp với phiếu 020 đang chạy song song. Không xóa file mới, sửa baseline hay lọc chúng khỏi log để làm kiểm đạt.

| File mới trong diff | Md5 | Ghi nhận |
|---|---|---|
| `moc-tinh.try1.png` | `8409ec34ed6ec9d89efbe16a4ef896ef` | Đầu ra 020b |
| `moc-tinh.try1.prompt.txt` | `e8c5d0a3248afddf19e601006af0d9fa` | Prompt 020b |
| `lam.try2.png` | `ad5ef3beef3ef5e9196665f121892a7c` | Xuất hiện đồng thời; 020b không ghi |
| `lam.try2.prompt.txt` | `4570f0026d94c901f181df9cbcb72973` | Xuất hiện đồng thời; 020b không ghi |
| `tre-ult.try2.prompt.txt` | `824438e20ffebc051b6f2b62b2d73e10` | Xuất hiện đồng thời; 020b không ghi |

Mộc Tinh gốc vẫn có md5 `d21762eca5d8089a4a3d05d158d72a8e` ở cả hai lần. Chủ dự án/Claude cần đối chiếu ba file đồng thời với phiếu 020 khi duyệt mục này.

### 2. Khổ và nền

Đầu ra `magick identify` và màu góc được lưu đầy đủ tại [identify-corners.txt](../../games/typing-defense/art-src/_review/020b/identify-corners.txt):

```text
games/typing-defense/art-src/portraits/moc-tinh.try1.png PNG 1254x1254 1254x1254+0+0 8-bit sRGB 2.16292MiB
TL=srgb(0,255,0)
TR=srgb(0,255,0)
BL=srgb(0,255,0)
BR=srgb(0,255,0)
```

**Đạt:** khổ đúng 1254×1254; cả bốn góc `#00FF00`, sai số mỗi kênh bằng 0 (giới hạn cho phép ±8).

Bản thô do `image_gen` tạo cũng là 1254×1254, nhưng hai góc trên lần lượt `(21,244,16)`, `(16,245,11)`, hai góc dưới là thân cây, nên chưa đạt nền. Đã chuẩn hóa bằng ImageMagick: co đều thành 1214×1214, thêm lề xanh 20 px mỗi cạnh, khóa vùng nền liên thông về `#00FF00` bằng floodfill với fuzz 12%. Không vẽ lại nhân vật hay nét cọ. Bản giao có mép cắt ngực nằm trong lề xanh mỏng; Claude xem khả năng dùng với khung HUD khi duyệt.

Bản thô và prompt nằm trong `_review/020b/moc-tinh.try1.raw.png`, `moc-tinh.try1.raw.prompt.txt`; lệnh chuẩn hóa đầy đủ ở [normalization.txt](../../games/typing-defense/art-src/_review/020b/normalization.txt). Không ghi đè bản thô hay file có sẵn.

### 3. Tờ xem nhanh

[Tờ xem nhanh 020b-moc-tinh.jpg](../../games/typing-defense/art-src/_review/020b-moc-tinh.jpg), 1140×680, nhãn tiếng Việt bằng `/System/Library/Fonts/Supplemental/Arial.ttf`:

- Hàng trên: `moc-tinh.png` → `017/moc-tinh.crop.retry.png` → toàn bộ lượt mới (lượt 1).
- Hàng dưới: Mộc Tinh và Draconis ở 128 px, rồi Mộc Tinh và Draconis ở 64 px. Giữ đúng kích thước ảnh cỡ game, không phóng lớn.
- Ảnh thu nhỏ riêng và bản sao prompt: `_review/020b/moc-tinh.try1.128.png`, `moc-tinh.try1.64.png` cùng các file `.prompt.txt` cạnh chúng.
- Lệnh ghép tờ xem nhanh được lưu tại `_review/020b/contact-sheet-command.txt`. Đây là tờ đối chiếu ghép từ ảnh có sẵn, không phải một lượt sinh ảnh.

## Phạm vi và việc còn lại

Chỉ tạo hai file `portraits/moc-tinh.try1.*`, tờ JPG cho 020b, bằng chứng dưới `_review/020b/` và báo cáo này. Không chạy Git, build hay test game; không sửa mã, tài liệu `ART_*`, ảnh gốc, bản 017, các file phiếu 020 hoặc Tu Tiên. Không tạo âm thanh.

Không tạo lượt 2–3 vì lượt 1 tự chấm từ 8. **Claude chưa chấm trong phiên này**; cần chấm độc lập vì mức 8,5 sát ngưỡng, xem sắc tím, độ rõ nét mặt ở 64 px, lề xanh và ngoại lệ md5 do làm song song trước khi quyết định thay ảnh. Chưa thay ảnh chính thức.
