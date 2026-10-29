# Phiếu 116 · Wordwoven · Cây lớn và mép rừng sử thi

Ngày giao: 29/10/2026, repo cha trên macOS. Tiếp nối phần làm dở đã có, sau phiếu 115.

**Đủ tám bản chọn, đủ prompt và tờ kiểm; qua mục 2–7. Tự chấm M từng ảnh 8–8,3, Q 9–9,5; M chung của mock là 8. Chờ Claude chấm lại, chưa coi là đã được nhận.**

## 1. Nơi giao

- Ảnh và prompt: [scenery/meadow/](../../games/typing-defense/art-src/scenery/meadow/), bốn loại `almond-tree`, `mountain-pine`, `bamboo-clump`, `canopy-block`, mỗi loại `-v3.png`, `-v4.png` cùng `.prompt.txt`.
- [Tờ v1, v2, v3, v4](../../games/typing-defense/art-src/_review/116-sheet.jpg): mỗi loại một hàng, chiều cao phần vật 256 px, nền `#3f5a48`, có nhãn.
- [Tờ 128 px](../../games/typing-defense/art-src/_review/116-small.jpg).
- [Mép rừng 1536 × 1024](../../games/typing-defense/art-src/_review/116-mock.jpg), [so tham chiếu cùng cao 640 px](../../games/typing-defense/art-src/_review/116-vs-ref.jpg).
- [Script, alpha, số đo và bằng chứng](../../games/typing-defense/art-src/_review/116/). Alpha giao kèm để kiểm/ghép nằm trong `handoff-v2/<tên>.final/alpha.png`; bản chọn chính vẫn là PNG nền M.

Không ghi đè, đổi tên hoặc xóa file đã có, gồm mọi v1, v2, `.v1.png`, `.try*` và hồ sơ phần làm dở. Không chạy lệnh Git, build, test suite, game, dev server, trình duyệt hoặc mạng ngoài công cụ `image_gen`. Không đọc/ghi Tu Tiên, không ghi game khác. Không có ảnh chụp trình duyệt hay bộ khung thô cần dọn.

## 2. Lượt sinh và prompt

Dùng **`image_gen` tích hợp**, mỗi lượt một ảnh. Tổng cả phần kế thừa: **13 lượt**, không ảnh nào quá hai lượt; lần tiếp tục này sinh thêm năm ảnh. Mỗi bản thử có prompt cạnh ảnh; bản chọn sao đúng prompt của lượt chọn. [Kiểm SHA-256](../../games/typing-defense/art-src/_review/116/raw-source-audit.json) xác nhận **13/13 bản thử trùng nguyên byte nguồn công cụ**.

STYLE + MAP + SCENERY và câu nền §3.8 giữ nguyên văn. Phần bổ sung chỉ khóa khổ, lề, chất liệu, bố cục và khác biệt biến thể; cảnh đá vôi trong STYLE chỉ dẫn bảng màu, không được thành cảnh nền của asset. **Cả tám ảnh dùng M, `#FF00FF`**, vì có xanh lá, không có hồng/tím.

| Ảnh | Lượt / chọn | Sửa gì và vì sao |
|---|---|---|
| `almond-tree-v3` | 1 / try1 | Kế thừa: bàng già cao, ba tầng, nghiêng phải; khóa lề và vỏ thân có múi. Giữ vì chất liệu và dáng đã tốt. |
| `almond-tree-v4` | 1 / try1 | Kế thừa: thấp/rộng, hai thân tách gốc, hai tầng; cùng bảng màu với v3. |
| `mountain-pine-v3` | 2 / try2 | Kế thừa lượt sửa: nhấn toàn bộ chân là gỗ, thân trần dài, bốn đệm kim, dáng cao nghiêng trái; tránh model biến chân thành đá theo STYLE. |
| `mountain-pine-v4` | 2 / try2 | Kế thừa lượt sửa: thông thật thấp/rộng, hai thân chung chân gỗ, ba đệm, nhánh chết bạc; chừa khoảng trống phía trên trong canvas dọc. |
| `bamboo-clump-v3` | 1 / try1 | Kế thừa: khóm rất cao cong trái, thân ngọc–vàng có đốt, chung một chân. |
| `bamboo-clump-v4` | 2 / try2 | Try1 kế thừa còn có đỉnh bên trái, gần dáng v3. Try2 nhấn thân giữa đứng, tán rộng, đỉnh phải ở khoảng 75% ngang ảnh và thân khô nhạt: khác dáng rõ. |
| `canopy-block-v3` | 2 / try2 | Try1 sinh thêm chân đá vôi. Không cắt bỏ phần vẽ; try2 nhấn chỉ bốn cây, toàn chân bằng gỗ, khối dài hạ từ trái sang phải. |
| `canopy-block-v4` | 2 / try2 | Try1 có sáu tán lớn và cây thấp phụ quanh chân. Try2 nhấn đúng năm tán: ba sau cao/tối, hai trước thấp/rộng; đáy chỉ là thân và lá thuộc năm cây ấy. |

Mọi lượt bị loại vẫn giữ tại `scenery/meadow/`; không cần lượt ba vì ứng viên chọn đã đạt. Hồ sơ trước lần tiếp tục giữ nguyên, gồm `prompts.json`, `pine-prompts-v2.json`, `bamboo-prompt-v2.json` và các thư mục thử cũ.

## 3. Hậu kỳ và đối chiếu §5

Quy trình giao cuối: `handoff-v2.mjs`, **không dùng các thư mục `.final` cũ ở cấp gốc**. Tách nền màu, cắt phần nền rỗng, đổi cỡ đồng tỷ lệ, thêm lề; ngưỡng alpha 50% chỉ làm gọn mép sau đổi cỡ. Không bỏ thành phần theo diện tích, không san phẳng tán, không phủ phần vẽ, không chỉnh màu hay sáng vật. Không gặp ngưỡng số buộc phá tranh.

Mặt nạ tương đương tách nền được tính từ RGB 8 bit: nền khi hue 250–345° và S > 0,15, hoặc khoảng cách kênh tối đa tới `#FF00FF` ≤ 60. Đây là nhận diện nền magenta và mép lẫn màu khóa; giữ mọi pixel còn lại, kể cả vùng lá nhỏ. Sau đổi cỡ dùng `-channel A -threshold 50% +channel`. Script lưu cả `keyed.png`, `alpha.png`, `candidate.png` để kiểm lại.

Nguồn bàng 1254 × 1254, xuất 1536 × 1536 bằng đổi cỡ đồng tỷ lệ; không coi đó là chi tiết sinh gốc 1536. Các ảnh dọc và ngang có khổ gốc đúng cột phiếu. Kiểm `magick identify` trên **bản chọn đã giao** nằm trong [final-identify.txt](../../games/typing-defense/art-src/_review/116/final-identify.txt).

Tám tờ **bản sinh | bản hậu kỳ**, cùng canvas hiển thị, đã xem trước khi chấm:

- [almond-tree-v3](../../games/typing-defense/art-src/_review/116-before-after-almond-tree-v3.jpg).
- [almond-tree-v4](../../games/typing-defense/art-src/_review/116-before-after-almond-tree-v4.jpg).
- [mountain-pine-v3](../../games/typing-defense/art-src/_review/116-before-after-mountain-pine-v3.jpg).
- [mountain-pine-v4](../../games/typing-defense/art-src/_review/116-before-after-mountain-pine-v4.jpg).
- [bamboo-clump-v3](../../games/typing-defense/art-src/_review/116-before-after-bamboo-clump-v3.jpg).
- [bamboo-clump-v4](../../games/typing-defense/art-src/_review/116-before-after-bamboo-clump-v4.jpg).
- [canopy-block-v3](../../games/typing-defense/art-src/_review/116-before-after-canopy-block-v3.jpg).
- [canopy-block-v4](../../games/typing-defense/art-src/_review/116-before-after-canopy-block-v4.jpg).

## 4. Số đo bản chọn

[Số đo đầy đủ](../../games/typing-defense/art-src/_review/116/metrics-handoff-v2.json), đo bằng `measure.mjs`. Hộp bao và thành phần liền dùng mặt nạ `max(|R−255|, G, |B−255|) > 60`, lân cận tám hướng. Luma là `0,2126R + 0,7152G + 0,0722B` trên thang 0–1. Dải mép là ba pixel trong cùng phía vật, lấy qua co mặt nạ bán kính ba pixel. `Mé​p/vật` phải ≥ 0,6.

**Tất cả:** sai lệch kênh lớn nhất trong vành 10 px = **0** (ngưỡng ≤ 12); tỷ lệ pixel lẫn hue nền ±12°, S > 0,5 = **0%** (ngưỡng ≤ 0,5%); đúng **một** vùng liền > 1% diện tích ảnh. Các vùng cực nhỏ còn lại không bị xóa để ép số.

| Ảnh | Khổ | Hộp bao x,y,w,h | Lề trái / phải / trên / đáy (%) | Luma vật / mép | Mép/vật |
|---|---|---|---|---|---|
| `almond-tree-v3` | 1536 × 1536 | 77, 95, 1382, 1349 | 5.01 / 5.01 / 6.18 / 5.99 | 0.341 / 0.377 | 1.104 |
| `almond-tree-v4` | 1536 × 1536 | 77, 296, 1382, 1148 | 5.01 / 5.01 / 19.27 / 5.99 | 0.312 / 0.377 | 1.209 |
| `mountain-pine-v3` | 1024 × 1536 | 68, 93, 887, 1351 | 6.64 / 6.74 / 6.05 / 5.99 | 0.256 / 0.207 | 0.807 |
| `mountain-pine-v4` | 1024 × 1536 | 51, 752, 921, 692 | 4.98 / 5.08 / 48.96 / 5.99 | 0.306 / 0.252 | 0.824 |
| `bamboo-clump-v3` | 1024 × 1536 | 59, 93, 905, 1351 | 5.76 / 5.86 / 6.05 / 5.99 | 0.303 / 0.307 | 1.013 |
| `bamboo-clump-v4` | 1024 × 1536 | 51, 156, 921, 1288 | 4.98 / 5.08 / 10.16 / 5.99 | 0.346 / 0.384 | 1.110 |
| `canopy-block-v3` | 1536 × 1024 | 77, 178, 1382, 785 | 5.01 / 5.01 / 17.38 / 5.96 | 0.260 / 0.217 | 0.835 |
| `canopy-block-v4` | 1536 × 1024 | 77, 76, 1382, 887 | 5.01 / 5.01 / 7.42 / 5.96 | 0.252 / 0.245 | 0.973 |

Lề trái/phải/trên đều ≥ 3%, đáy ≤ 12%. Khoảng trống trên lớn của thông v4 là chủ ý dáng thấp trong khổ dọc, không kéo giãn cây để lấp canvas.

| Cặp | W:H v3 → v4 | Lệch tỷ lệ, lấy giá trị nhỏ làm mẫu số | Đỉnh cao nhất v3 → v4 (% ngang canvas) | Chênh đỉnh |
|---|---|---|---|---|
| `almond-tree` | 1.024 → 1.204 | 17.51% | 57.46 → 53.44 | 4.02 điểm % |
| `mountain-pine` | 0.657 → 1.331 | 102.71% | 31.36 → 51.12 | 19.75 điểm % |
| `bamboo-clump` | 0.670 → 0.715 | 6.75% | 23.83 → 75.07 | 51.23 điểm % |
| `canopy-block` | 1.761 → 1.558 | 12.99% | 20.44 → 47.40 | 26.95 điểm % |

Bàng/thông qua bằng tỷ lệ hộp bao; tre/khối tán qua bằng chênh vị trí đỉnh, tính theo toàn chiều rộng canvas, không dùng phần trăm tương đối để nới ngưỡng. Đỉnh lấy trung bình x của pixel vật trong ba hàng cao nhất.

## 5. Tự chấm sau hậu kỳ

M của cảnh vật xét trong mock và kiểm dáng ở ảnh lẻ; Q theo năm tiêu chí của ART_ACCEPTANCE: đúng đề / đọc được / hợp bộ / hình khối / dùng bước sau. Đã xem bản hậu kỳ đầy đủ và bản 128 px cạnh dài, không chấm từ bản sinh. Điểm Q trong ngoặc là năm điểm thành phần ở cỡ đầy đủ.

| Bản chọn | M đầy đủ | Q đầy đủ | M ở 128 px | Q ở 128 px | Nhận diện và chỗ còn thiếu |
|---|---|---|---|---|---|
| `almond-tree-v3` | 8,3 | 9,5 (2/1,5/2/2/2) | 8,1 | 9,5 | Nhận ra bàng ba tầng, thân cổ thụ có bạnh; lá lớn còn hơi dày chi tiết. |
| `almond-tree-v4` | 8,3 | 9,5 (2/1,5/2/2/2) | 8,1 | 9,5 | Hai tầng rộng và hai thân rõ; sắc vàng ở tán hơi nhiều so với bóng ngọc. |
| `mountain-pine-v3` | 8,1 | 9,5 (2/1,5/2/2/2) | 8 | 9 | Nhận ra thông thân uốn, bốn đệm; vân vỏ mất khi thu nhỏ, dáng vẫn rõ. |
| `mountain-pine-v4` | 8,1 | 9,5 (2/1,5/2/2/2) | 8 | 9 | Ba đệm, thân chẻ và cành bạc rõ; canvas dọc để cây thấp nên vật nhỏ hơn các ảnh khác ở bản thu cả canvas. |
| `bamboo-clump-v3` | 8,1 | 9 (1,5/1,5/2/2/2) | 8 | 9 | Khóm tre và hướng cong đọc ngay; còn vài lá mảnh hơn yêu cầu gom khối. |
| `bamboo-clump-v4` | 8,1 | 9 (1,5/1,5/2/2/2) | 8 | 9 | Dáng đứng, ngọn phải và thân khô nhạt khác v3; chi tiết lá nhỏ vẫn khá nhiều. |
| `canopy-block-v3` | 8,2 | 9,5 (1,5/2/2/2/2) | 8,1 | 9,5 | Nhận ra mép rừng hạ bốn bậc; thân lộ nhiều hơn chữ “only a little trunk”. |
| `canopy-block-v4` | 8,2 | 9,5 (2/1,5/2/2/2) | 8,1 | 9,5 | Năm tán, hai hàng và bóng teal rõ; tán có nhiều nhánh phụ nhưng vẫn gom thành năm khối. |

**M chung `116-mock.jpg`: 8/10. “Đứng cạnh được” về chất liệu cảnh vật, dáng cổ thụ và quy mô trong thế giới sử thi; chưa đạt mức 9 của tham chiếu.** Phông 114 cung cấp trời, đá vôi, lớp xa và mốc rùa trời; không gán những thành phần sẵn có ấy thành công của riêng phiếu 116. Mock là bằng chứng ghép màu/cỡ: nền 114 còn phần ngọc phẳng, chân cây chưa có bóng tiếp xúc/địa hình gameplay, lính cũ vẫn mang nét cũ. Đây không phải ảnh nghiệm thu cảnh trong game ở camera 55°.

Mock có hai hàng, hàng sau tối hơn 8% và cao theo mét; [mock-layout.json](../../games/typing-defense/art-src/_review/116/visual-final/mock-layout.json) ghi vị trí và tỷ lệ: bàng 14/18 m, thông 10/14 m, tre 16 m, khối tán 10/14 m. Hàng sau 25 px/m, hàng trước 30 px/m; lính nguồn `units/linh-giao.png` cao 1,8 m, 54 px. Dùng ảnh có sẵn làm thước, không vẽ người bằng mã.

## 6. KA1 và chạy lại

- Mốc đầu phiếu `md5-before.txt`: **192 file**; mốc tiếp tục `md5-resume-before.txt`: **211 file**; sau giao `md5-after.txt`: **234 file**.
- Cả hai diff chỉ có dòng thêm: **42** dòng từ mốc đầu, **23** từ mốc tiếp tục; **0 sửa, 0 mất**. Có băm mọi file trong `scenery/` đệ quy, gồm cả prompt. Xem [published-audit.json](../../games/typing-defense/art-src/_review/116/published-audit.json), `md5-before-diff.txt` và `md5-resume-before-diff.txt`.
- `final-audit.py` xác nhận 13 nguồn công cụ trùng SHA-256, tám bản chọn trùng ứng viên đã đo, tám prompt chọn trùng prompt lượt chọn và bốn cặp qua ngưỡng khác dáng.

Các script dùng trực tiếp ImageMagick 7 `/opt/homebrew/bin/magick`, Node và Python chuẩn, không cài thư viện. Font nhãn: `/System/Library/Fonts/Supplemental/Arial.ttf`. Chạy từ repo cha; dùng tên thư mục/tệp kết quả mới vì script cố ý từ chối ghi đè:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
node games/typing-defense/art-src/_review/116/handoff-v2.mjs replay-116
node games/typing-defense/art-src/_review/116/measure.mjs metrics-replay-116.json   replay-116/almond-tree-v3.final replay-116/almond-tree-v4.final   replay-116/mountain-pine-v3.final replay-116/mountain-pine-v4.final   replay-116/bamboo-clump-v3.final replay-116/bamboo-clump-v4.final   replay-116/canopy-block-v3.final replay-116/canopy-block-v4.final
node games/typing-defense/art-src/_review/116/review-final.mjs visual-replay-116
```

`review-final.mjs` đọc cố định alpha giao trong `handoff-v2/` để tái tạo đúng tờ đã chấm. `compare-handoff.mjs` tái tạo tờ trước/sau; `publish-handoff.py` và `final-audit.py` lưu quy trình giao/kiểm, chạy tại đích mới hoặc sau khi điều chỉnh tên đích trong một bản sao mới, không chạy đè bộ đã giao. Script cũ của phần làm dở giữ nguyên chỉ để truy vết, không phải đường giao cuối.

## 7. Khác phiếu, việc để lại

- Tiếp tục hồ sơ đã có thay vì sinh lại năm ứng viên tốt; không tính lại số lượt từ đầu. Giữ mốc KA1 cũ và thêm mốc tiếp tục, không ghi đè `md5-before.txt`.
- Giữ thêm alpha và ứng viên trong vùng review, không xuất alpha ra ngoài danh sách đường dẫn cho phép.
- Không làm các loại cây thấp/cỏ/hoa/đá/gỗ của 117–118. **Mẫu màu đề nghị cho hai phiếu sau: `almond-tree-v3.png` và `canopy-block-v4.png`**, lấy ngọc–teal ở bóng, vàng ấm tiết chế trên ngọn, vỏ xám và nâu đỏ tự nhiên; không lấy phong cách v1/v2.
- Không đổi mã `prepare-scenery`, không tích hợp runtime, không sửa danh sách ảnh cần nâng vì ngoài đường dẫn được phép. Claude tắt viền mực khi tích hợp, giữ v1/v2 trên đĩa.
- Chủ dự án/Claude cần xem **tám ảnh giao đầy đủ, tờ 128 px, tờ trước/sau và mock**; chấm lại M/Q trước khi nhận. Chú ý thông v4 có khoảng trống lớn và khối tán v3 còn lộ thân tương đối nhiều. Không cần chọn giữa các lượt nếu đồng ý bộ đề nghị ở trên.
