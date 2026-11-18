# Phiếu 173 · Dragonhold · Bộ texture lửa v2

**Trạng thái: đã bổ sung hồ sơ bàn giao cho đủ 12 bản chọn có sẵn; chưa đạt điều kiện xong phiếu.** Tám tấm qua các cổng texture đã đo. Bốn tấm còn điểm chặn: `smoke-puff`, `soot-ring`, `scorch-decal` trượt alpha; `fire-burst` trượt bán kính lõi trắng và tự chấm Q = 7,5. Claude chưa chấm nhận. Không có thay đổi shader hay runtime.

## 1. Phạm vi và cách tiếp nhận

Ngày 29/10/2026, lượt này bắt đầu ở repo cha trên Mac. Thư mục đích đã có 12 bản chọn, đủ bộ `.png`, `.prompt.txt`, `.alpha.png`, 21 lượt `.tryN.png` + prompt, bản hậu kỳ và số đo cũ. Không coi các tệp đó là ảnh mới tạo trong lượt này. Chưa có 12 metadata `.json`, tờ chính hay báo cáo. Đã giữ nguyên toàn bộ 115 tệp có trước; thêm các tệp còn thiếu bằng chế độ tạo độc quyền, không ghi đè.

Không gọi tạo ảnh mới: tên bản chọn đã tồn tại và phiếu cấm ghi đè; riêng `fire-burst` và `smoke-puff` đã đủ ba lượt. Các prompt và ảnh sinh cũ được giữ nguyên. Lượt này không có nhật ký lời gọi image_gen cũ để xác minh độc lập nhà cung cấp; không khẳng định đã sinh chúng trong phiên hiện tại. Mọi xử lý mới chỉ là đo, ghép tờ và ghép ảnh trận bằng ImageMagick 7 tại `/opt/homebrew/bin/magick`; `ART_MAGICK` trỏ đúng đường dẫn này, font Arial của macOS. Không cài gói, không mạng, Git, build, test game, dev server hay trình duyệt.

Áp dụng skill `imagegen` cho quy tắc media và lưu prompt; `game-vfx-layered` dùng làm tham chiếu cho lớp tối, pha và màu. Phạm vi phiếu hẹp hơn workflow gameplay: không sửa mã, changelog, tài liệu game, danh sách thay ảnh, hay game khác. Không chạm Tu Tiên.

## 2. Các tệp bàn giao

- Media giữ nguyên: `games/dragon-hold/art-src/vfx/fire-v2/`; mỗi tên có bản chọn, alpha, prompt và mọi lượt thử. Thêm đúng một `<tên>.json` cho mỗi tấm, ghi lưới, fps, loop, blend, pha sử dụng, cổng chặn và trạng thái chờ Claude.
- Tờ chính ở cỡ đầy đủ: [173-sheet.jpg](../../games/dragon-hold/art-src/_review/173-sheet.jpg). Mỗi atlas có 1 pixel ảnh = 1 pixel tờ, kèm dải toàn bộ khung 64 px và cặp ảnh trận sáng/tối. Tờ có kích thước rất lớn; khi duyệt nên mở từng tờ riêng ở bảng dưới.
- Kiểm blend tuyến tính: [173-linear-sheet.jpg](../../games/dragon-hold/art-src/_review/173-linear-sheet.jpg). Tờ chính dùng Plus trực tiếp trong sRGB như phép thử bất lợi; tờ bổ sung giải mã cả nền và texture sang RGB tuyến tính trước khi ghép rồi mã hóa lại sRGB. Không giả lập bloom, tone mapping, độ sáng hay shader game.
- Tờ “bản sinh | bản hậu kỳ” và 5 dải khung cỡ gốc trong `_review/173/`. Không sửa hậu kỳ của bản chọn. Bên sinh giữ tỉ lệ và thêm lề để cùng khổ với bên hậu kỳ; khác biệt khổ nguồn được ghi rõ ở metadata và bảng dưới.
- Số đo mới: [delivery-audit.json](../../games/dragon-hold/art-src/_review/173/delivery-audit.json), [core-background-audit.json](../../games/dragon-hold/art-src/_review/173/core-background-audit.json); tự chấm: [self-scores.json](../../games/dragon-hold/art-src/_review/173/self-scores.json). Các số đo cũ vẫn nguyên; khi khác nhau dùng số mới và định nghĩa dưới đây.

## 3. Bảng khổ, lượt chọn và tờ duyệt

| Tấm | Khổ bản chọn / ô | Nguồn lượt chọn | Lượt / fps / loop / blend | Tờ gốc và cỡ game | Sinh → hậu kỳ |
|---|---|---|---|---|---|
| `flame-tongue` | 2048×1024 / 256×256 | 1774×887 | try1 / 24 / true / additive | [tờ riêng](../../games/dragon-hold/art-src/_review/173/flame-tongue.review.jpg) | [đối chiếu](../../games/dragon-hold/art-src/_review/173/flame-tongue.before-after.jpg) |
| `flame-ball` | 2048×1024 / 256×256 | 1774×887 | try2 / 24 / true / additive | [tờ riêng](../../games/dragon-hold/art-src/_review/173/flame-ball.review.jpg) | [đối chiếu](../../games/dragon-hold/art-src/_review/173/flame-ball.before-after.jpg) |
| `fire-burst` | 4096×2048 / 512×512 | 1774×887 | try3 / 30 / false / additive | [tờ riêng](../../games/dragon-hold/art-src/_review/173/fire-burst.review.jpg) | [đối chiếu](../../games/dragon-hold/art-src/_review/173/fire-burst.before-after.jpg) |
| `smoke-puff` | 2048×1024 / 256×256 | 1774×887 | try3 / 24 / false / normal | [tờ riêng](../../games/dragon-hold/art-src/_review/173/smoke-puff.review.jpg) | [đối chiếu](../../games/dragon-hold/art-src/_review/173/smoke-puff.before-after.jpg) |
| `soot-ring` | 1024×1024 / 1024×1024 | 1254×1254 | try2 / 0 / false / normal | [tờ riêng](../../games/dragon-hold/art-src/_review/173/soot-ring.review.jpg) | [đối chiếu](../../games/dragon-hold/art-src/_review/173/soot-ring.before-after.jpg) |
| `ember-sprites` | 2048×512 / 256×256 | 2172×724 | try1 / 0 / false / additive | [tờ riêng](../../games/dragon-hold/art-src/_review/173/ember-sprites.review.jpg) | [đối chiếu](../../games/dragon-hold/art-src/_review/173/ember-sprites.before-after.jpg) |
| `flame-trail` | 2048×256 / 2048×256 | 2079×756 | try1 / 0 / true / additive | [tờ riêng](../../games/dragon-hold/art-src/_review/173/flame-trail.review.jpg) | [đối chiếu](../../games/dragon-hold/art-src/_review/173/flame-trail.before-after.jpg) |
| `heat-ring` | 1024×1024 / 1024×1024 | 1254×1254 | try2 / 0 / false / additive | [tờ riêng](../../games/dragon-hold/art-src/_review/173/heat-ring.review.jpg) | [đối chiếu](../../games/dragon-hold/art-src/_review/173/heat-ring.before-after.jpg) |
| `scorch-decal` | 2048×1024 / 1024×1024 | 1774×887 | try2 / 0 / false / normal | [tờ riêng](../../games/dragon-hold/art-src/_review/173/scorch-decal.review.jpg) | [đối chiếu](../../games/dragon-hold/art-src/_review/173/scorch-decal.before-after.jpg) |
| `cracks-glow` | 1024×1024 / 1024×1024 | 1254×1254 | try1 / 0 / false / additive | [tờ riêng](../../games/dragon-hold/art-src/_review/173/cracks-glow.review.jpg) | [đối chiếu](../../games/dragon-hold/art-src/_review/173/cracks-glow.before-after.jpg) |
| `glyph-spark` | 1024×256 / 256×256 | 2172×724 | try1 / 0 / false / additive | [tờ riêng](../../games/dragon-hold/art-src/_review/173/glyph-spark.review.jpg) | [đối chiếu](../../games/dragon-hold/art-src/_review/173/glyph-spark.before-after.jpg) |
| `glyph-ember-burst` | 1024×512 / 256×256 | 1774×887 | try2 / 30 / false / additive | [tờ riêng](../../games/dragon-hold/art-src/_review/173/glyph-ember-burst.review.jpg) | [đối chiếu](../../games/dragon-hold/art-src/_review/173/glyph-ember-burst.before-after.jpg) |

`fps: 0` là tập sprite/biến thể hoặc ảnh đơn, không phải clip. `flame-trail` có `loop: true` theo UV trái–phải, không phải hoạt họa. Có 16 ember và 4 glyph spark, hai biến thể scorch; cả hai biến thể/đủ sprite được ghép lên mỗi nền, không chỉ xem một ô. Các cỡ trong game là cỡ đề xuất cho phép ghép tĩnh, không phải khổ đã đo trong runtime.

Dải khung không thu nhỏ: [flame-tongue](../../games/dragon-hold/art-src/_review/173/flame-tongue.native-strip.png), [flame-ball](../../games/dragon-hold/art-src/_review/173/flame-ball.native-strip.png), [fire-burst](../../games/dragon-hold/art-src/_review/173/fire-burst.native-strip.png), [smoke-puff](../../games/dragon-hold/art-src/_review/173/smoke-puff.native-strip.png), [glyph-ember-burst](../../games/dragon-hold/art-src/_review/173/glyph-ember-burst.native-strip.png). Mỗi dải đọc trái → phải theo thứ tự atlas, không nội suy hay đảo khung.

## 4. Phép đo và kết quả

Mặt nạ chuyển động: `max(R,G,B) > 8` cho cộng sáng; `alpha > 8` cho blend thường. IoU là giao/chập của đúng hai ô cùng tọa độ; đo toàn bộ cặp kề, cộng cặp cuối–đầu cho hai clip loop. Không dịch ô để làm đẹp số. Alpha bán phần là giá trị 1–254; dải mép là gradient hình thái học Square:3 quanh vùng `alpha > 0` của ảnh cuối. Cách này kiểm đúng nghĩa đen “ngoài dải mép 3 px”, không miễn trừ vùng khói trong lòng. Vì số đo cũ dùng dải khác, các phần trăm alpha mới khác; cả hai cách đều trượt ở ba tấm thường.

Nền cộng sáng đo cả lề 3 px từng ô và toàn bộ vùng companion alpha = 0; vùng nền ở mọi tấm cộng sáng có RGB tối đa **2/255**, không có pixel vượt 2. Lề ô có RGB tối đa **0**; vệt lửa chỉ kiểm lề trên/dưới vì hai cạnh ngang là mép lặp. Màu key còn hiện dùng tiêu chí gần magenta (`R,B ≥ 245`, `G ≤ 10`, alpha > 0), toàn bộ 12 tấm có **0 pixel, 0 %**, dưới trần 0,2 %. Đây là cổng màu key, không phải chứng minh mọi quầng mép đã hoàn hảo về cảm giác.

| Tấm | Đúng khổ | Alpha bán phần ngoài mép 3 px | IoU min–max | Cuối → đầu | Lõi trắng hình học ở đỉnh | Cổng texture |
|---|---|---:|---|---|---|---|
| `flame-tongue` | đạt | 0 px · 0.0000 % | 0.7588–0.9231 | 0.7588 | 12.66 % | qua số đo; chờ chấm |
| `flame-ball` | đạt | 0 px · 0.0000 % | 0.8262–0.8734 | 0.8306 | 9.52 % | qua số đo; chờ chấm |
| `fire-burst` | đạt | 0 px · 0.0000 % | 0.5648–0.9003 | — | 34.05 % | chưa đạt |
| `smoke-puff` | đạt | 1,520,509 px · 72.5035 % | 0.6096–0.7276 | — | không áp dụng | chưa đạt |
| `soot-ring` | đạt | 540,691 px · 51.5643 % | — | — | không áp dụng | chưa đạt |
| `ember-sprites` | đạt | 0 px · 0.0000 % | — | — | 4.97 % | qua số đo; chờ chấm |
| `flame-trail` | đạt | 0 px · 0.0000 % | — | — | 0.20 % | qua số đo; chờ chấm |
| `heat-ring` | đạt | 0 px · 0.0000 % | — | — | 5.91 % | qua số đo; chờ chấm |
| `scorch-decal` | đạt | 950,522 px · 45.3244 % | — | — | không áp dụng | chưa đạt |
| `cracks-glow` | đạt | 0 px · 0.0000 % | — | — | 6.21 % | qua số đo; chờ chấm |
| `glyph-spark` | đạt | 0 px · 0.0000 % | — | — | 29.28 % | qua số đo; chờ chấm |
| `glyph-ember-burst` | đạt | 0 px · 0.0000 % | 0.6109–0.8366 | — | 5.26 % | qua số đo; chờ chấm |

### 4.1 Lõi trắng: không dùng diện tích thay bán kính

Luma dùng hệ số Rec.709 trên mẫu màu sRGB: `0,2126 R + 0,7152 G + 0,0722 B > 0,92`. Ở ô có tổng luma cao nhất, lấy cụm trắng liên thông 8 hướng lớn nhất; tâm là trọng tâm cụm; bán kính lõi là khoảng cách xa nhất từ tâm tới pixel cụm, bán kính vật đo cùng tâm tới pixel mặt nạ vật xa nhất. Đây là kiểm tra hình học bảo thủ, kèm tọa độ và bán kính pixel trong JSON để Claude đo lại. Với ảnh vòng/sợi dài, số chỉ mô tả hình của texture, không thay việc nhìn độ dày nét trắng. Không dùng các ảnh khói để chấm ramp lửa.

`fire-burst`, khung 5: bán kính lõi **81.06 px / bán kính vật **238.02 px = **34,05 %**, trượt 30 %. Bán kính tương đương theo diện tích (`sqrt(diện tích trắng / diện tích vật)`) chỉ là **15,49 %**; con số này có trong dữ liệu cũ nhưng không đủ chứng minh cổng bán kính. [Tờ bằng chứng lõi](../../games/dragon-hold/art-src/_review/173/fire-burst-core-evidence.jpg). Không xóa hoặc nhuộm vùng trắng để ép qua số.

### 4.2 Ramp ba dải và mép nối

Ba dải rời nhau, tính trên mặt nạ ở ô sáng nhất: vàng (`R ≥ 220, G ≥ 150, B < 200`); cam (`R ≥ 140, 45 ≤ G < 150, B < 90`); đỏ thẫm (`R ≥ 24, R > 1,6G, G < 60, B < 60`). Đây là phép kiểm sự có mặt của ba họ màu; không thay việc xem thứ tự lõi–thân–mép. Cả 9 tấm cộng sáng đều có đủ ba dải, có khe tối bên trong; ba tấm thường là khói/muội/than, không bắt chúng có lõi trắng.

| Tấm cộng sáng | Khung đỉnh | Vàng / cam / đỏ thẫm (px) | Bán kính tương đương theo diện tích, chỉ để đối chiếu |
|---|---:|---|---:|
| `flame-tongue` | 19 | 1,039 / 5,236 / 13,456 | 9.83 % |
| `flame-ball` | 22 | 3,827 / 9,454 / 12,085 | 9.67 % |
| `fire-burst` | 5 | 24,270 / 41,909 / 53,038 | 15.49 % |
| `ember-sprites` | 10 | 451 / 1,467 / 7,925 | 6.47 % |
| `flame-trail` | 0 | 24,750 / 76,956 / 106,310 | 1.88 % |
| `heat-ring` | 0 | 8,379 / 14,800 / 71,924 | 15.97 % |
| `cracks-glow` | 0 | 20,606 / 39,389 / 235,965 | 6.90 % |
| `glyph-spark` | 1 | 1,167 / 2,684 / 7,401 | 15.05 % |
| `glyph-ember-burst` | 4 | 1,405 / 2,616 / 15,093 | 7.39 % |

`flame-trail`: chênh cột trái–phải tối đa **0**, trung bình **0** trên mọi kênh RGB. Số này chứng minh hai cột biên khớp, không chứng minh đạo hàm/motion UV; tờ đối chiếu cho thấy bản hậu kỳ kéo dài vùng vẽ so với bản sinh. Claude cần xem nó chạy trong ribbon. Không đổi bản chọn để giấu thay đổi này.

### 4.3 Ngưỡng số mâu thuẫn với tranh: dừng theo §5

`smoke-puff`, `soot-ring`, `scorch-decal` giữ lớp bán trong suốt trong lòng khói/tro. Ép toàn bộ về 0/255 chỉ chừa 3 px sẽ san phẳng khói và làm mất lớp bụi. Theo `ART_ACCEPTANCE.md` §5, giữ nguyên tranh và ghi điểm chặn; không tự miễn cổng, không đánh dấu pass. `fire-burst` đã đủ ba lượt; giữ bản chọn thay vì làm bẩn lõi để ép đạt 30 %. Đây là bốn tấm phải được Claude quyết trước khi gọi phiếu xong.

## 5. KA5 · tự chấm trên bản hậu kỳ

M dùng thước chợ của chủ dự án, đánh giá chất liệu, khối, mép vỡ và độ đọc của **texture** trong tờ native/cặp ghép tuyến tính. Không quy điểm texture thành điểm toàn đòn hoặc hệ gõ chữ dùng chung. Ảnh tham chiếu của chủ dự án được đặt cạnh đầu tờ chính; đó là mốc mức hoàn thiện, không phải tham chiếu hình dạng lửa. Q gồm năm mục của `ART_ACCEPTANCE.md`, có điểm nửa. Điểm là tự chấm; các tấm sát 8 còn phải Claude chấm độc lập. Không có giám khảo thứ hai trong lượt này.

| Tấm | M | Q | Điểm cần xem |
|---|---:|---:|---|
| `flame-tongue` | 8.1 | 9.0 | Lưỡi phân nhánh rõ, xoáy trong tốt; trên đá be cần lớp muội dưới để giữ màu đỏ. |
| `flame-ball` | 8.1 | 9.0 | Khối cuộn có vỏ đỏ và khe tối; bản cộng sáng riêng lẻ còn nhạt trên nền sáng. |
| `fire-burst` | 8.0 | 7.5 | Khối nổ tốt nhưng lõi trắng hình học 34,05 % vượt trần; khổ 4096 là phóng từ nguồn 1774, không phải chi tiết gốc 4K. |
| `smoke-puff` | 8.1 | 8.5 | Khói cuộn có khối; sắc hơi lam. Alpha mềm trong lòng khói không qua luật nhị phân. |
| `soot-ring` | 8.0 | 8.5 | Vòng muội có lỗ và mép vỡ; chi tiết hơi hiện thực, alpha mềm không qua luật nhị phân. |
| `ember-sprites` | 8.1 | 9.0 | 16 biến thể cong, cỡ khác nhau; đốm nhỏ cần cỡ đầu sáng đủ lớn khi lane gắn. |
| `flame-trail` | 8.0 | 8.5 | Vệt có sợi xoáy, khe đỏ; chuẩn hóa kéo dài phần vẽ, cần Claude xem độ dày trong ribbon thật. |
| `heat-ring` | 8.1 | 9.0 | Nét vòng đứt đoạn, lóe nhọn đọc được; cần lớp tối để nổi trên đài be. |
| `scorch-decal` | 8.1 | 8.5 | Bản chọn try2 đã là than nguội, hai dáng khác nhau; alpha tro mềm không qua luật nhị phân. |
| `cracks-glow` | 8.0 | 8.5 | Khe nứt phân nhánh tốt, nền cộng sáng không thể làm tối đá; cần lớp decal thường bên dưới. |
| `glyph-spark` | 8.2 | 9.0 | Bốn sao có chi tiết lửa, lõi hình học 29,28 % sát trần; chưa phải nghiệm thu hệ gõ chữ dùng chung. |
| `glyph-ember-burst` | 8.1 | 9.0 | Chùm than bung theo cung, tiêu dần; lõi nhỏ, trên nền sáng nên đi cùng lớp tối rất gọn. |

Không có kết luận “12/12 đạt”: ba tấm alpha dù Q từ 8 vẫn trượt cổng bắt buộc; `fire-burst` có Q 7,5 và lõi vượt trần. Các phép ghép cho thấy cộng sáng đơn lẻ trên đá be làm màu nhạt đi, kể cả khi ghép tuyến tính. Làn VFX phải phối lớp tối blend thường bên dưới, giữ lõi nhỏ và đo lại ở camera chơi; không dùng điểm tự chấm này để bỏ qua duyệt trận thật. Các glyph cũng chưa qua quy trình hai giám khảo ≥ 9 của hệ phản hồi gõ chữ dùng chung.

## 6. Ảnh trận và giới hạn bằng chứng

Đọc nguyên hai crop ảnh trận của worktree VFX (chỉ đọc), mỗi crop 507×285:

- `games/.wt-dh-vfx/tmp/vfx/final6/strong/_crops/1280x720-play-light-strike/BEFORE-a-02.png`.
- `games/.wt-dh-vfx/tmp/vfx/final6/strong/_crops/1280x720-play-dark-strike/BEFORE-a-02.png`.

Không làm tối ảnh sáng để giả nền tối; cả hai là ảnh có sẵn từ kịch bản cũ, không phải capture build hiện tại. Phép ghép dùng Over cho texture thường, Plus cho texture cộng sáng; atlas không bị chỉnh. Cỡ gợi ý: lưỡi/quả cầu 96 px, nổ 192 px, khói 160 px, muội 192 px, ember 28 px, trail 360×45 px, vòng nhiệt/khe nứt 160 px, scorch 144 px/biến thể, sao 40 px, chùm than chữ 72 px. Không đo đáp ứng gõ, timing sát thương, contrast thẻ chữ, bloom, FPS, draw call hay IME.

Lóe ở khung đầu là việc lớp flash riêng: tổng luma khung đầu của `fire-burst` bằng **10,74 %** đỉnh, `glyph-ember-burst` bằng **41,72 %** đỉnh. Chúng không phải lớp flash tức thì ≥ 95 % của VFX_STANDARD; khi tích hợp phải ghép lớp flash đúng chuẩn, không kéo giãn timing sim để chờ atlas. Không có audio trong phiếu này. Không tạo raw frame capture hoặc video; chỉ giữ tờ/ảnh ghép được báo cáo liên kết, không chạy prune lên ảnh của làn khác.

## 7. KA1 · bất biến và tái lập

Ảnh chụp ban đầu của lượt tiếp nhận: [ka1-resume-before.md5](../../games/dragon-hold/art-src/_review/173/ka1-resume-before.md5) (115 tệp, `md5 -r` từng tệp). Bản `ka1-before.md5` cũ rỗng được giữ nguyên như bằng chứng lượt trước đã bắt đầu từ thư mục mới; không lấy nó làm bằng chứng cho lượt hiện tại. Kết quả sau và diff: `ka1-resume-after.md5`, `ka1-resume.diff`; báo cáo xác minh: `ka1-verification.json`. Hai tệp manifest/diff tự sinh và báo cáo xác minh không tự băm chính mình. Diff phải chỉ có bản ghi thêm, 0 bản ghi mất/đổi. Nội dung 115 tệp đầu được kiểm lại độc lập bằng `md5 -r`.

Script trong thư mục review chỉ phục vụ tái lập đo/tờ, không phải mã game: `audit-delivery-v2.py measure`, `check-core-background.py`, `render-delivery.py`, `render-linear-check.py`, `package-metadata.py`. Chúng tạo đầu ra độc quyền, nên cố chạy lại trên cùng thư mục sẽ từ chối ghi đè; muốn tái lập cần đích mới trong phạm vi owner cho phép. `audit-delivery.py` là bản công cụ đầu có lỗi vị trí subcommand ImageMagick, dừng trước khi sinh số đo; giữ lại, không dùng làm bằng chứng. Không có file nguồn nào bị sửa để sửa lỗi đó.

## 8. Chỗ khác phiếu và việc cần chủ dự án/Claude xem

1. Lượt này bổ sung hồ sơ cho bộ media đã có, không sinh lại 12 ảnh. Không thay tên, xóa, ghi đè bản cũ hay vượt ba lượt. Prompt từng lượt được sao nguyên văn ở phần 9 và giữ file gốc cạnh ảnh.
2. Ảnh sinh không đúng khổ giao: các nguồn từ 1254², 1774×887, 2172×724 hoặc 2079×756 đã được lượt trước chuẩn hóa về khổ bảng. Đặc biệt nổ 4096×2048 là phóng 2,309× mỗi chiều từ 1774×887. Không gọi đó là nguồn chi tiết 4K; xem tờ 1:1 trước khi duyệt.
3. Ba cổng alpha và một cổng lõi trắng chưa đạt. Giữ tranh theo §5, không lén đổi cách đo hoặc hạ ngưỡng. Cần Claude quyết cách giữ alpha khói/tro mềm trong chuẩn nghiệm thu và xử lý lõi `fire-burst`; phiếu chưa xong trước các quyết định đó.
4. Tờ ghép là bằng chứng texture offline từ crop trận cũ. Chưa tích hợp, chưa có clip trong shader. Claude/làn VFX gắn và chấm lại; owner xem bản chơi cuối. Không đề nghị sửa game hay chuẩn trong lượt này.

## 9. Prompt nguyên văn của từng lượt đã lưu

Đủ 21 prompt lượt thử; kiểm cả 21 đều chứa nguyên văn khối STYLE Dragonhold §3.2 và câu bổ sung VFX của phiếu. Tiếng Anh dưới đây là nội dung gửi sinh ảnh được lưu sẵn, không phải đoạn hướng dẫn mới. Bản chọn có prompt trùng byte với prompt của lượt được chọn.

### flame-tongue

**Lượt 1 · bản chọn** — [flame-tongue.try1.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/flame-tongue.try1.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, flame-tongue.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: 32 consecutive animation frames of ONE upright licking dragon-fire tongue. It gently rises, forks into two or three sharp licking tips, curls inward and reconnects seamlessly into a loop. Chipped irregular edges, intricate turbulent internal orange swirls and dark crimson channels. Same base anchor at lower center, equal scale throughout. Small white-yellow hot core at the base, at most 20 percent of effect radius. Adjacent silhouettes overlap about 70 to 85 percent, with organic changing tips; final pose flows into first.
Technical composition: exact output 2048x1024 pixels. Perfect regular 8 columns by 4 rows atlas, 256x256 pixel cells; read row-major, evenly spaced cells, no visible grid or separators.
Backdrop: Flat uniform pure black #000000 throughout every empty area; intended for additive blending.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
```

### flame-ball

**Lượt 1** — [flame-ball.try1.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/flame-ball.try1.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, flame-ball.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: 32 consecutive looping frames of ONE rolling, billowing dragon fireball at the same center and roughly the same scale. Dense hand-painted turbulent orange whorls, little white-yellow core less than 20 percent of radius, broken deep-red licking outer shell, irregular spherical volume with interior shadow channels and tiny ember shedding. Rotation and changing tongues between adjacent frames; silhouette overlap 70 to 85 percent, including last into first.
Technical composition: exact output 2048x1024 pixels. Perfect regular 8 columns by 4 rows atlas, 256x256 pixel cells; read row-major, evenly spaced cells, no visible grid or separators.
Backdrop: Flat uniform pure black #000000 throughout every empty area; intended for additive blending.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
```

**Lượt 2 · bản chọn** — [flame-ball.try2.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/flame-ball.try2.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, flame-ball.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: 32 consecutive looping frames of ONE rolling, billowing dragon fireball at the same center and roughly the same scale. Dense hand-painted turbulent orange whorls, little white-yellow core less than 20 percent of radius, broken deep-red licking outer shell, irregular spherical volume with interior shadow channels and tiny ember shedding. Rotation and changing tongues between adjacent frames; silhouette overlap 70 to 85 percent, including last into first.
Technical composition: exact output 2048x1024 pixels. Perfect regular 8 columns by 4 rows atlas, 256x256 pixel cells; read row-major, evenly spaced cells, no visible grid or separators.
Backdrop: Flat uniform pure black #000000 throughout every empty area; intended for additive blending.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
Revision 2, animation correction only: each consecutive fireball silhouette must visibly roll and deform, with 15 to 25 percent of occupied shape exchanged per frame. The motion continues at the same strength through frames 16 to 24 and across frame 32 to frame 1. Keep the body compact inside the middle 75 percent of every cell with substantial pure black padding. Preserve the rich turbulent painted fire quality; small hot core. No held poses and no repeated outer contours.
```

### fire-burst

**Lượt 1** — [fire-burst.try1.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/fire-burst.try1.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, fire-burst.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: 32 consecutive frames of ONE fire impact explosion. First frame is a compact full-bright sharp flash, then connected orange fire lobes expand, shred into licking tongues, and decay into dark red embers. Progression is left to right then next row. Dense asymmetric turbulent internal detail. Keep the bright white-yellow central core less than 20 percent of radius at the brightest moment. Avoid a white cloud; retain orange-red saturated structured flames. Consistent centered origin. Gradual growth and decay, adjacent silhouette overlap about 60 to 85 percent. Last frame is a faint visible group of cooling embers.
Technical composition: exact output 4096x2048 pixels. Perfect regular 8 columns by 4 rows atlas, 512x512 pixel cells; read row-major, evenly spaced cells, no visible grid or separators.
Backdrop: Flat uniform pure black #000000 throughout every empty area; intended for additive blending.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
```

**Lượt 2** — [fire-burst.try2.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/fire-burst.try2.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, fire-burst.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: 32 consecutive frames of ONE fire impact explosion. First frame is a compact full-bright sharp flash, then connected orange fire lobes expand, shred into licking tongues, and decay into dark red embers. Progression is left to right then next row. Dense asymmetric turbulent internal detail. Keep the bright white-yellow central core less than 20 percent of radius at the brightest moment. Avoid a white cloud; retain orange-red saturated structured flames. Consistent centered origin. Gradual growth and decay, adjacent silhouette overlap about 60 to 85 percent. Last frame is a faint visible group of cooling embers.
Technical composition: exact output 4096x2048 pixels. Perfect regular 8 columns by 4 rows atlas, 512x512 pixel cells; read row-major, evenly spaced cells, no visible grid or separators.
Backdrop: Flat uniform pure black #000000 throughout every empty area; intended for additive blending.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
Revision 2, preserve the explosion art quality and repair temporal spacing: use a continuous moderate-size impact silhouette from the beginning, then expand gradually over the first 8 frames. During frames 8 through 32 each shape continues deforming by 15 to 25 percent. Frames 30, 31, 32 keep the same broadly overlapping ember-cloud footprint while brightness cools gradually; the last is dim but clearly visible red embers, not disappearance. Adjacent silhouette IoU target 0.60 to 0.88 at a fixed 8/255 visibility threshold. Do not hold a pose. Keep every frame contained within the central 76 percent of each cell with pure black margin.
```

**Lượt 3 · bản chọn** — [fire-burst.try3.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/fire-burst.try3.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, fire-burst.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: 32 consecutive frames of ONE fire impact explosion. First frame is a compact full-bright sharp flash, then connected orange fire lobes expand, shred into licking tongues, and decay into dark red embers. Progression is left to right then next row. Dense asymmetric turbulent internal detail. Keep the bright white-yellow central core less than 20 percent of radius at the brightest moment. Avoid a white cloud; retain orange-red saturated structured flames. Consistent centered origin. Gradual growth and decay, adjacent silhouette overlap about 60 to 85 percent. Last frame is a faint visible group of cooling embers.
Technical composition: exact output 4096x2048 pixels. Perfect regular 8 columns by 4 rows atlas, 512x512 pixel cells; read row-major, evenly spaced cells, no visible grid or separators.
Backdrop: Flat uniform pure black #000000 throughout every empty area; intended for additive blending.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
FINAL REVISION 3: make this a lively animated explosion, with genuinely changing silhouettes throughout all 32 frames. Never reuse a cloud silhouette during cooling. Frames 9 through 32 keep shredding, rotating lobes, peeling apart and drifting into differently shaped coherent ember clusters; 20 to 30 percent of occupied shape changes at every step. Small coherent cloudlets retain overlapping positions so IoU stays 0.60 to 0.88, including frames 30 to 31 to 32. The last frame is a distinct dim ember cluster, still visible, about 65 percent of the peak footprint. Small hot white-yellow core, orange body, crimson broken edges. All painted content sits inside the middle 70 percent of each equal cell, with wide pure-black padding on all four sides. Precisely 8 columns and 4 rows, 32 consecutive frames, no held poses.
```

### smoke-puff

**Lượt 1** — [smoke-puff.try1.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/smoke-puff.try1.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, smoke-puff.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: 32 consecutive frames of ONE charcoal-black smoke puff curling upward, swelling slowly and dissipating. Neutral cool charcoal, dark slate gray illuminated folds, rich rolling painterly volume, organic wispy soft broken edges, no orange fire. The smoke remains fully readable against the flat magenta key. Fixed centered anchor, gradual evolution, adjacent silhouettes overlap about 60 to 85 percent. Last frame is faint sparse visible wisps.
Technical composition: exact output 2048x1024 pixels. Perfect regular 8 columns by 4 rows atlas, 256x256 pixel cells; read row-major, evenly spaced cells, no visible grid or separators.
Backdrop: Flat uniform pure magenta #FF00FF in every empty area, including holes; intended for chroma-key alpha extraction and normal blending. Magenta is exclusively the removable backdrop.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
```

**Lượt 2** — [smoke-puff.try2.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/smoke-puff.try2.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, smoke-puff.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: 32 consecutive frames of ONE charcoal-black smoke puff curling upward, swelling slowly and dissipating. Neutral cool charcoal, dark slate gray illuminated folds, rich rolling painterly volume, organic wispy soft broken edges, no orange fire. The smoke remains fully readable against the flat magenta key. Fixed centered anchor, gradual evolution, adjacent silhouettes overlap about 60 to 85 percent. Last frame is faint sparse visible wisps.
Technical composition: exact output 2048x1024 pixels. Perfect regular 8 columns by 4 rows atlas, 256x256 pixel cells; read row-major, evenly spaced cells, no visible grid or separators.
Backdrop: Flat uniform pure magenta #FF00FF in every empty area, including holes; intended for chroma-key alpha extraction and normal blending. Magenta is exclusively the removable backdrop.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
Revision 2, repair temporal spacing while preserving charcoal smoke: first frame is an already formed medium-size smoke puff occupying about 60 percent of cell height, growing only 2 to 4 percent per next frame until the peak at frame 10. Maintain the same fixed centered anchor throughout. Later frames slowly curl and lose density with large coherent dark gray folds still visible in frames 30 to 32; the last frame is translucent smoke with the same broadly overlapping footprint. Adjacent silhouette IoU target 0.60 to 0.88. Neutral cool charcoal and slate-gray only; broad unpainted pure magenta padding around each cell.
```

**Lượt 3 · bản chọn** — [smoke-puff.try3.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/smoke-puff.try3.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, smoke-puff.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: 32 consecutive frames of ONE charcoal-black smoke puff curling upward, swelling slowly and dissipating. Neutral cool charcoal, dark slate gray illuminated folds, rich rolling painterly volume, organic wispy soft broken edges, no orange fire. The smoke remains fully readable against the flat magenta key. Fixed centered anchor, gradual evolution, adjacent silhouettes overlap about 60 to 85 percent. Last frame is faint sparse visible wisps.
Technical composition: exact output 2048x1024 pixels. Perfect regular 8 columns by 4 rows atlas, 256x256 pixel cells; read row-major, evenly spaced cells, no visible grid or separators.
Backdrop: Flat uniform pure magenta #FF00FF in every empty area, including holes; intended for chroma-key alpha extraction and normal blending. Magenta is exclusively the removable backdrop.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
FINAL REVISION 3: start with an already fully formed charcoal smoke puff in frame 1, the same 70-percent-of-cell-height size as frame 2. Absolutely no small starting puff. It is already a full mature plume at the start, then it swirls slowly upward and slowly dissipates through all 32 frames. Stable central registration, no shift of anchor between frames 1 and 2. Neighboring shapes overlap 65 to 85 percent. Keep large coherent gray folds and visible dim wisps even at frame 32, with gradual alpha fading; density and curls change while silhouette remains overlapping. Palette exclusively cool neutral charcoal-black and slate-gray with a pure magenta background. All artwork fully inside each equal cell with broad padding.
```

### soot-ring

**Lượt 1** — [soot-ring.try1.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/soot-ring.try1.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, soot-ring.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: ONE top-down toroidal soot ring, irregular torn porous charcoal-black broken perimeter, smoky slate-gray inward wisps, generous empty center. This is the dark backing layer placed under dragon fire. Rich painted soot grains and tangled curling ash, dimensional fold shading, full ring isolated and centered with 12 percent padding.
Technical composition: exact output 1024x1024 pixels. One isolated texture.
Backdrop: Flat uniform pure magenta #FF00FF in every empty area, including holes; intended for chroma-key alpha extraction and normal blending. Magenta is exclusively the removable backdrop.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
```

**Lượt 2 · bản chọn** — [soot-ring.try2.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/soot-ring.try2.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, soot-ring.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: ONE top-down toroidal soot ring, irregular torn porous charcoal-black broken perimeter, smoky slate-gray inward wisps, generous empty center. This is the dark backing layer placed under dragon fire. Rich painted soot grains and tangled curling ash, dimensional fold shading, full ring isolated and centered with 12 percent padding.
Technical composition: exact output 1024x1024 pixels. One isolated texture.
Backdrop: Flat uniform pure magenta #FF00FF in every empty area, including holes; intended for chroma-key alpha extraction and normal blending. Magenta is exclusively the removable backdrop.
Palette for this soot-only asset: neutral cool charcoal-black, deep slate gray, tiny dry ash-gray highlights. Entirely unlit, extinguished, matte soot and smoky ash, with all detail expressed by dark gray values. The removable magenta background is the only saturated color. No fire thermal ramp applies to this extinguished soot layer.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
Revision 2: this ring is exclusively the DARK soot backing layer underneath separate fire textures. All the ring artwork is cold black and charcoal gray, its brightest gray fold about RGB 70,75,80. Extinguished charcoal fragments and thin smoky gray curls make a torn toroidal silhouette. Preserve a very large empty center and broad clear magenta padding. Show no active glowing material.
```

### ember-sprites

**Lượt 1 · bản chọn** — [ember-sprites.try1.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/ember-sprites.try1.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, ember-sprites.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: SIXTEEN distinct isolated ember particle sprites, one per cell. Each ember has a short gently curved dark-red tail, a small white-yellow pinprick head, saturated orange body and dark crimson edges. Varied sizes and natural curved directions, varied chips and cracked charcoal texture. These are ember chunks, not straight laser lines. Keep each entirely within its cell with generous padding. Exactly 8 columns by 2 rows, no additional sprites.
Technical composition: exact output 2048x512 pixels. Perfect regular 8 columns by 2 rows atlas, 256x256 pixel cells; read row-major, evenly spaced cells, no visible grid or separators.
Backdrop: Flat uniform pure black #000000 throughout every empty area; intended for additive blending.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
```

### flame-trail

**Lượt 1 · bản chọn** — [flame-trail.try1.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/flame-trail.try1.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, flame-trail.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: ONE very wide horizontal flame ribbon UV strip filling a 2048 by 256 texture. Seamlessly tileable horizontally: left and right cut edges have matching narrow orange-red flame strands at the same heights, identical color and thickness. Tapered ragged top and bottom edges with black padding. Detailed streaming turbulent fire, orange interlocking curls, deep-crimson dark channels, yellow hot threads, falling embers and thin dark soot filaments. Uneven organic flowing silhouette, never a smooth tube or rigid cone. Horizontal periodic pattern, center thickness about 60 percent of texture height. Tiny white-yellow accents only.
Technical composition: exact output 2048x256 pixels. One isolated texture.
Backdrop: Flat uniform pure black #000000 throughout every empty area; intended for additive blending.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
```

### heat-ring

**Lượt 1** — [heat-ring.try1.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/heat-ring.try1.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, heat-ring.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: ONE top-down thin orange heat ring, broken into irregular burning rune-like abstract strokes without actual letters or symbols. Full circular arrangement with generous black empty center, thin lively ragged orange-red brush marks, gold slivers and a few white-yellow pinpoints. Chipped fiery edges and warm deep-red outer edge. Irregular variations in thickness and gaps. Whole centered ring with 12 percent padding.
Technical composition: exact output 1024x1024 pixels. One isolated texture.
Backdrop: Flat uniform pure black #000000 throughout every empty area; intended for additive blending.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
```

**Lượt 2 · bản chọn** — [heat-ring.try2.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/heat-ring.try2.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, heat-ring.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: ONE top-down thin orange heat ring, broken into irregular burning rune-like abstract strokes without actual letters or symbols. Full circular arrangement with generous black empty center, thin lively ragged orange-red brush marks, gold slivers and a few white-yellow pinpoints. Chipped fiery edges and warm deep-red outer edge. Irregular variations in thickness and gaps. Whole centered ring with 12 percent padding.
Technical composition: exact output 1024x1024 pixels. One isolated texture.
Backdrop: Flat uniform pure black #000000 throughout every empty area; intended for additive blending.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
Revision 2: a delicate segmented heat-rune ring, made of 18 to 24 separate short burning angular brushstroke segments around a circle, with clear black gaps between every segment. Ring band thickness about 4 percent of diameter. Each stroke has a dark crimson outside, orange body and very small gold inner edge. Mostly empty black center, no thick rolling flame wreath, no solid connected circle. Abstract shapes only, never writing.
```

### scorch-decal

**Lượt 1** — [scorch-decal.try1.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/scorch-decal.try1.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, scorch-decal.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: TWO different top-down scorched ground decal variants side by side, each in its own square cell. Irregular charcoal-black and dark brown centers, cooling dark red coal fissures, soft broken gray ash borders with particulate detail. Left is a roughly circular exploded scorch; right is a slightly asymmetric branching scorch. Both have fine hand-painted burnt-ground material detail and jagged natural silhouettes, neither contains an outside stone slab or a square ground tile. Isolated cutout marks on flat key, with 12 percent clear padding per cell.
Technical composition: exact output 2048x1024 pixels. Perfect regular 2 columns by 1 rows atlas, 1024x1024 pixel cells; read row-major, evenly spaced cells, no visible grid or separators.
Backdrop: Flat uniform pure magenta #FF00FF in every empty area, including holes; intended for chroma-key alpha extraction and normal blending. Magenta is exclusively the removable backdrop.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
```

**Lượt 2 · bản chọn** — [scorch-decal.try2.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/scorch-decal.try2.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, scorch-decal.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: TWO different top-down scorched ground decal variants side by side, each in its own square cell. Irregular charcoal-black and dark brown centers, cooling dark red coal fissures, soft broken gray ash borders with particulate detail. Left is a roughly circular exploded scorch; right is a slightly asymmetric branching scorch. Both have fine hand-painted burnt-ground material detail and jagged natural silhouettes, neither contains an outside stone slab or a square ground tile. Isolated cutout marks on flat key, with 12 percent clear padding per cell.
Technical composition: exact output 2048x1024 pixels. Perfect regular 2 columns by 1 rows atlas, 1024x1024 pixel cells; read row-major, evenly spaced cells, no visible grid or separators.
Backdrop: Flat uniform pure magenta #FF00FF in every empty area, including holes; intended for chroma-key alpha extraction and normal blending. Magenta is exclusively the removable backdrop.
Color palette for this extinguished decal: matte black-brown char, muted ash gray and a few thin dim deep-crimson coal cracks. The only vivid color is the removable magenta key background.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
Revision 2, extinguished scorch decal material: two flat soot-and-ash stains on the ground rather than raised rock chunks. Centers are matte black-brown, surrounding ash is muted dark gray. Only a few thin deep-crimson cooling coal fissures at RGB about 100,12,5; all yellow, white and orange flame emission has already cooled away. The removable background is flat pure magenta. Fine painted ash and char texture, torn soft natural borders, no cast shadow, top-down orthographic.
```

### cracks-glow

**Lượt 1 · bản chọn** — [cracks-glow.try1.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/cracks-glow.try1.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, cracks-glow.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: ONE top-down ground fissure glow decal for the aftermath of Sky Fire: an organic radial branching network of glowing red-orange cracks in dark stone, fissures only against pure black. Saturated red outer heat, deep-orange crack channels, tiny yellow-orange hottest slivers, dark stone borders fading naturally into the black background. Strong readable major branching paths plus fine subsidiary cracks. Irregular circular footprint, centered, 12 percent black padding, no rectangular stone tile.
Technical composition: exact output 1024x1024 pixels. One isolated texture.
Backdrop: Flat uniform pure black #000000 throughout every empty area; intended for additive blending.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
```

### glyph-spark

**Lượt 1 · bản chọn** — [glyph-spark.try1.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/glyph-spark.try1.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, glyph-spark.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: FOUR distinct compact starburst spark sprites for a freshly typed letter, exactly four equal square cells in one row. Tiny white-yellow core at most 15 percent of radius, saturated orange angular wings, crimson ragged tips, sharp asymmetric painterly rays with internal fiery brush texture. Varied four to six principal rays, readable at 24 pixels, each centered and fully contained with black padding. No glyphs or actual letters.
Technical composition: exact output 1024x256 pixels. Perfect regular 4 columns by 1 rows atlas, 256x256 pixel cells; read row-major, evenly spaced cells, no visible grid or separators.
Backdrop: Flat uniform pure black #000000 throughout every empty area; intended for additive blending.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
```

### glyph-ember-burst

**Lượt 1** — [glyph-ember-burst.try1.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/glyph-ember-burst.try1.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, glyph-ember-burst.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: EIGHT consecutive animation frames of a compact ember burst released from a completed typed word. Several short curved orange-red ember fragments expand outward from a fixed central origin, each has tiny hot yellow head and cooling dark red tail. First frame a compact sharp energetic orange spark, middle frames a lively radial burst, final frames sparse cooling red cinders. Dense painterly internal fire detail, organic staggered curved trajectories, not needles. Smooth stepwise expansion with adjacent silhouette overlap about 60 to 85 percent, all fragments entirely inside each equal square cell.
Technical composition: exact output 1024x512 pixels. Perfect regular 4 columns by 2 rows atlas, 256x256 pixel cells; read row-major, evenly spaced cells, no visible grid or separators.
Backdrop: Flat uniform pure black #000000 throughout every empty area; intended for additive blending.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
```

**Lượt 2 · bản chọn** — [glyph-ember-burst.try2.prompt.txt](../../games/dragon-hold/art-src/vfx/fire-v2/glyph-ember-burst.try2.prompt.txt)

```text
Use case: stylized-concept
Asset type: production Dragonhold game VFX texture, glyph-ember-burst.
STYLE (verbatim art direction; applies to painting quality, not scenery content):
Epic high-fantasy game art for Dragonhold, a mountain pass guarded by a fire dragon: a deep green valley with a fast river and an old stone bridge, walled in by colossal granite cliffs and snow-capped peaks, an ancient fortress gate and ramparts built across the pass, giant dragon statues carved into the cliff faces, dark pine forest climbing the slopes, morning mist pooling in the valley, and creeping violet blight coming out of the forest. Stylized painterly-realistic rendering at the level of a top commercial fantasy strategy game, not photographic: rich detail on stone, pine and water grouped into big readable shapes, crisp silhouettes, cinematic dawn light with long shadows, warm rim light on the cliffs and god rays through the mist, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: deep pine green and cool slate-blue shadows, warm ember-orange and gold light from the dragon and the dawn, cream granite, small muted-violet blight accents. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.
Primary request: EIGHT consecutive animation frames of a compact ember burst released from a completed typed word. Several short curved orange-red ember fragments expand outward from a fixed central origin, each has tiny hot yellow head and cooling dark red tail. First frame a compact sharp energetic orange spark, middle frames a lively radial burst, final frames sparse cooling red cinders. Dense painterly internal fire detail, organic staggered curved trajectories, not needles. Smooth stepwise expansion with adjacent silhouette overlap about 60 to 85 percent, all fragments entirely inside each equal square cell.
Technical composition: exact output 1024x512 pixels. Perfect regular 4 columns by 2 rows atlas, 256x256 pixel cells; read row-major, evenly spaced cells, no visible grid or separators.
Backdrop: Flat uniform pure black #000000 throughout every empty area; intended for additive blending.
Color palette for fire: small white-yellow core, saturated ember-orange body, deep crimson broken edges and dark charcoal soot. Preserve at least three distinct readable thermal bands. Large painterly forms hold intricate internal hand-painted detail.
Only the specified VFX texture artwork, no environment, no scenery, no objects, no people, no lettering, no numbers, no logo, no watermark, no border. Align every cell precisely, keep all effects away from cell boundaries except the explicitly seamless trail. Professional commercial fantasy VFX asset quality.
Revision 2, temporal spacing correction: exactly eight equally sized cells. Frame 1 already contains a medium-sized visible cluster occupying about 50 percent of the cell width; frames 2 to 5 expand gradually to about 70 percent width, only 8 to 12 percent scale increase per step. Frames 6 to 8 preserve overlapping curved ember trajectories while cooling slowly. Last frame still has dim visible crimson fragments, never disappearing abruptly. Adjacent frames overlap 60 to 85 percent by silhouette at an 8/255 visibility threshold. No held poses. Keep fixed central anchor, generous pure black padding, small white-yellow core.
```
