# Phiếu 012c · Sửa `tools/art-normalize` lần 2 theo phản biện 012b

**Bối cảnh:** phiếu 012b đã sửa phần lớn 33 lỗi của 012 (23 đã sửa, 9 sửa một phần, 1 chưa sửa), **nhưng chưa đạt phản biện lần 2**. Claude phản biện 4 góc (mã, an toàn, chất lượng ảnh, tài liệu và test) ngày 25/10/2026 trên Mac mini M4: **4 lỗi lớn, 19 lỗi nhỏ**. Đầy đủ, có bằng chứng và cách sửa đề xuất: `.local/codex-runs/012b-review.json` (khóa `merged.findings`, `merged.review012_status`; bản từng góc ở `reviews`). Script và ảnh của người phản biện: `tools/art-normalize/.tmp/review-claude/`. Đọc hết trước khi sửa. Ảnh gốc không bị hỏng.

**Thư mục làm việc:** gốc repo. Chỉ được ghi vào:
- `tools/art-normalize/`;
- `games/dragon-hold/art-src/`: chỉ file dẫn xuất của phiếu 012, 012b, 012c; không đụng ảnh gốc;
- `games/dragon-hold/art-src/2d/README-normalize.md`.

Không chạy git. Máy là Mac: ImageMagick ở `/opt/homebrew/bin/magick` (`export ART_MAGICK=/opt/homebrew/bin/magick`).

## Phải sửa: 4 lỗi lớn

1. **`key()`, khử màu loang (despill) chạy trên mọi điểm ảnh đục.** Màu thật của vật trùng sắc với màu khóa bị làm trong và xám. Decal D2 `flower-clusters` mất hoa chuông tím mà prompt yêu cầu.
   - Chỉ áp alpha theo hiệu màu và phép kẹp kênh khóa trong vùng nền và vùng loang (mặt nạ nền nở vài px), hoặc ở điểm ảnh khóa bão hòa mạnh. Màu trong lòng vật giữ alpha 255 và giữ sắc.
   - Sửa alpha ở mép để không ra viền ô liu hay viền tối (`forest-litter.v1`). Thêm chế độ "bảo vệ phần trong" thay cho `--despill off` khi cần (icon `herb-hut` 256 có viền hồng mới).
   - Bỏ chốt `key_dominance_gt_25` (luôn đạt, vì chính phép kẹp xóa hết). Thay bằng: điểm ảnh khóa đậm chỉ được phép sát mép mặt nạ, cộng phép kiểm giữ sắc và alpha của phần trong so với ảnh nguồn.
   - Ca hồi quy mới: tím nhạt trên khóa xanh dương, xanh rêu trên khóa xanh lá, nằm trong lòng vật, phải giữ đục và giữ sắc.
   - Dựng lại mọi đầu ra đã dùng despill tự động (8 decal, 20 icon × 2 cỡ).
2. **`seamless()` co giãn lại cả ảnh về khổ nguồn.** Phông `pine-river-far` mềm đi khoảng một phần ba (độ chi tiết −34 %), bị kéo dãn 13,7 % theo chiều ngang, và có dải mờ chồng hình ở giữa vùng trộn.
   - Mặc định xuất ô W−B (và H−B) không co giãn. Muốn giữ khổ nguồn thì phải bật rõ bằng `--keep-size`: khi đó dùng virtual pixel `tile` và bộ lọc sắc.
   - Cân nhắc cắt đường nối theo sai số nhỏ nhất, hoặc vùng trộn hẹp hơn.
   - Báo độ chi tiết của cả ảnh so với ảnh nguồn. Dựng lại B1 và ảnh xem mép.
3. **Chốt `seam-check` có điểm mù.** Nó không thấy chỗ tụt chi tiết giữa vùng trộn (cửa sổ cột 90–150 chỉ còn khoảng 0,78 so với phần trong), không có phép kiểm sọc theo hàng, và bản phông có sọc của 012 (đã bị loại, nay là `.rejected-012`) **lại qua chốt mới**.
   - Đo chi tiết bằng cửa sổ trượt trên cả bề rộng vùng trộn, so với `--reference`.
   - Thêm thước đo bậc hoặc lệch theo hàng trong dải mép, so với phần còn lại của ảnh.
   - Cặp đối chứng phải cách nhau đúng bằng cặp gương.
   - Chặn ảnh có cạnh dưới 4 px (hiện ảnh rộng hoặc cao 1 px làm `measure` lỗi `IndexError`).
   - Sửa luật `--reference` cho nguồn vốn không liền mép, và ghi vào README.
4. **Test của chốt mép nói quá.** Tiêu chí chi tiết và `--reference` chưa có test; bắt gập gương chỉ sát ngưỡng. Thêm các ca **phải trượt**:
   - phông có sọc `.rejected-012`, hoặc ảnh tương đương;
   - ảnh bù lệch (offset compensation);
   - trộn chéo 50 %;
   - ảnh gập gương không có `--reference`, khổ ≥ 256 px.

   Ảnh mẫu đo chi tiết phải bất đối xứng.

## Phải sửa: lỗi nhỏ (chi tiết trong JSON)
- Băm mọi `*.sh` vào hash công cụ, gồm `seamless.sh`. Script bọc phải có quyền chạy; ghi trong README rằng khi commit sẽ dùng `git add --chmod=+x`.
- `flat-bg` và `icon` nhận `--src-bg auto|#RRGGBB`; câu lỗi phải nêu đúng tùy chọn của lệnh đó.
- Sau khi tách nền: cảnh báo hoặc dừng nếu mảng góc nối với viền vẫn còn alpha > 8 (trừ khi có `--keep-alpha`). Chỉ coi alpha vào là có nghĩa khi vùng trong suốt đủ lớn, không phải chỉ 4 điểm góc.
- Các hàm ghi dùng được từ thư viện cũng phải qua chốt (không ghi đè, không mở rộng `%d`); kiểm cả `WORK`.
- Công bố nguyên tử: `os.link` từ file tạm, bắt SIGTERM và SIGHUP để dọn file tạm, không để lại file 0 byte ở tên cuối.
- Runner 012b, 012c: khóa để không chạy hai lần cùng lúc; công bố hai pha (kiểm hết rồi mới đổi).
- `.gitignore` theo kiểu danh sách cho phép: chặn mọi ảnh, 3D, âm, kể cả đuôi viết hoa.
- Giới hạn định dạng đầu vào (PNG, JPEG, WebP); chặn chuỗi MSL, SVG, MVG.
- Test đặt `cwd` rõ ràng; phủ các nhánh chưa test (ngưỡng túi nền, túi nền bão hòa, ngưỡng keep-alpha, đường dẫn phía đầu vào).
- Chốt túi nền của ảnh Tripo bỏ qua điểm ảnh ở viền mềm. 9 ảnh hiện ghi "chưa đạt" là báo nhầm: ghi lại nhãn đúng.
- Số trong báo cáo và manifest phải tính ra từ dữ liệu, không ghi cứng.
- README và README của job: bỏ câu bảo người dùng `source common.sh` trong shell; thêm bước report, verify, inspect.

## Quyết định đã chọn theo đề xuất
- **Ảnh Tripo có vật rộng** (ví dụ `pine-round` co còn 0,70×, vì khổ canvas theo bảng 012 không hợp vật): khổ canvas theo tỉ lệ của vật, chọn khổ chuẩn gần nhất trong bảng, giữ lề 8 %. Ghi "đã chọn theo đề xuất" vào README-normalize. Chủ dự án có thể đổi sau.

## Làm lại ảnh
- Dựng lại mọi dẫn xuất bị ảnh hưởng bằng công cụ đã sửa, ghi vào đúng tên phiếu 012 quy định.
- Bản 012b hiện có đổi hậu tố `.rejected-012b` (kèm kiểm hash). Giữ nguyên `.rejected-012` và mọi ảnh gốc.
- Cập nhật README-normalize: số đo trước và sau thật, ảnh nào còn chưa đạt.

**Xong khi:**
- `test.sh` đạt, gồm các ca mới phải trượt;
- 4 lỗi lớn đã sửa và có bằng chứng; lỗi nhỏ đã sửa hoặc ghi rõ lý do không sửa;
- README khớp mã.

Claude sẽ phản biện lại lần 3 trước khi commit.
