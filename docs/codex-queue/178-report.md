# Phiếu 178 · Hai ảnh làm lại: `easier.v3` và `poster.v3`

**Ngày:** 29/10/2026. **Kết quả:** đã giao hai bản chọn mới, mọi lượt sinh, prompt nguyên văn, bản thu và tờ so hậu kỳ. `easier.v3` tự chấm đạt, chờ Claude chấm nhận. **`poster.v3` chưa qua đủ kiểm bố cục:** sau ba lượt sửa, còn một đỉnh karst xa bên trái cao hơn tán cây khoảng 9 px ở bản gốc. Giữ bản đẹp nhất, không sửa núi bằng công cụ và không gọi lượt thứ tư. Phiếu chưa đủ điều kiện nhận toàn bộ.

## 1. File giao

| Ảnh | Bản chọn | Bản thu | Lượt giữ lại |
|---|---|---|---|
| Dragonhold | [`easier.v3.png`](../../games/dragon-hold/art-src/ui/icons/easier.v3.png), 1024² sRGBA | `.v3.256.png`, `.v3.128.png`, `.v3.64.png`, Lanczos trực tiếp, không làm nét | `.v3.try1.png`, `.v3.try2.png`, nguồn nguyên trạng 1254² |
| Wordwoven | [`poster.v3.png`](../../games/typing-defense/art-src/ui/title-epic/poster.v3.png), 1024 × 1536 sRGB, nền đặc | [`.v3.384.png`](../../games/typing-defense/art-src/ui/title-epic/poster.v3.384.png), 256 × 384 | `.v3.try1.png`, `.v3.try2.png`, `.v3.try3.png`, đều 1024 × 1536 |

Mỗi PNG có `<tên>.prompt.txt` cạnh ảnh, chứa đúng prompt đã gửi. Prompt của bản chọn và các bản thu trùng nguyên văn lượt được chọn; lệnh hậu kỳ ghi riêng trong script và báo cáo. Tổng file mới của phiếu trong hai thư mục UI: **11 PNG + 11 prompt**. Không đổi tên chính cũ; Claude đổi sang khi nhận.

Hồ sơ nằm trong phạm vi review của hai phiếu gốc: [`_review/140/178/`](../../games/dragon-hold/art-src/_review/140/178/) và [`_review/158/178/`](../../games/typing-defense/art-src/_review/158/178/). Báo cáo này là tài liệu duy nhất được thêm ngoài các thư mục ảnh/review cho phép.

## 2. Prompt và các lượt

Dùng **`image_gen` tích hợp**, năm lời gọi: hai lượt sinh icon mới và ba lượt sửa poster. Không dùng API khác. Đã xem hai tờ của người chấm, ảnh thương mại chủ dự án, `gold`, `skill-fire-breath`, `poster.v2.try1` và `keyart` trước khi làm.

### `easier`

- **`.v3.try1`** là lượt thứ hai tính cả ảnh gốc của 140. Mở đầu bằng STYLE-UI Dragonhold nguyên văn ở phiếu 119; thêm KIND–ICON, phần riêng của người chấm **nguyên văn**, rồi nền M `#FF00FF`. Đúng ba bậc và mũi tên xuống nhưng quá nhiều vảy, kim loại và trang trí trên thân bậc.
- **`.v3.try2`** là lượt thứ ba, cuối cùng theo ngân sách người chấm. Giữ toàn bộ prompt trước, thêm yêu cầu hình chiếu ngang, ba mặt bậc ngang và cổ bậc đứng, thân granite kem sáng, trang trí tiết chế, mũi tên vàng dày và đơn giản. **Chọn lượt này.** Không lông vũ, không còn dáng giày.
- Prompt thực gửi: [lượt 1](../../games/dragon-hold/art-src/ui/icons/easier.v3.try1.prompt.txt), [lượt 2](../../games/dragon-hold/art-src/ui/icons/easier.v3.try2.prompt.txt). Đường dẫn nguồn công cụ: [sources.json](../../games/dragon-hold/art-src/_review/140/178/sources.json).

### `poster`

| Lượt | Ảnh đính kèm | Chỉ dẫn và kết quả |
|---|---|---|
| `.v3.try1` | `poster.v2.try1.png`, `keyart.png`, đúng thứ tự | Prompt bước 1 của verdict nguyên văn: lùi khung, mở trời phía trên, giữ hai cánh lông gắn ở vai. Cánh đã trọn khung, nhưng đầu cánh phải còn ở khoảng 15% chiều cao; vách trái vẫn cao hơn cây. |
| `.v3.try2` | `.v3.try1.png` | Prompt bước 2 của verdict nguyên văn: hạ các tháp karst phía trái sau cây. Vách cao đã hạ; dải 20% trên vẫn có đầu cánh. |
| `.v3.try3` | `.v3.try2.png`, `keyart.png`, đúng thứ tự | Lặp nguyên văn prompt bước 1, thêm khổ 1024 × 1536, dải trời 25%, hạ bố cục, giữ đường núi đã thấp và cây là điểm cao nhất bên trái. **Chọn lượt này:** cánh và khoảng trời đạt; một đỉnh xa trái lại nhỉnh hơn tán cây. |

Prompt thực gửi: [lượt 1](../../games/typing-defense/art-src/ui/title-epic/poster.v3.try1.prompt.txt), [lượt 2](../../games/typing-defense/art-src/ui/title-epic/poster.v3.try2.prompt.txt), [lượt 3](../../games/typing-defense/art-src/ui/title-epic/poster.v3.try3.prompt.txt). Nguồn công cụ: [sources.json](../../games/typing-defense/art-src/_review/158/178/sources.json). Không sinh lại poster từ chữ; cả ba lượt đều sửa ảnh nối tiếp.

## 3. Hậu kỳ không phá tranh · ART_ACCEPTANCE §5

**Icon:** `tools/art-normalize`, `ART_MAGICK=/opt/homebrew/bin/magick`, WORK đặt trong hồ sơ 178. Tách M toàn cục, bảo vệ màu trong vật, cắt theo alpha, giữ tỉ lệ, căn giữa bằng Triangle về vật dài khoảng 716 px trong ô 1024. Các bản thu Lanczos trực tiếp từ bản chọn, không làm nét.

Lần tách đầu có **596/291.170 pixel hiện mang sắc M = 0,20469%**, hơi trên ngưỡng 0,2%. Đã lưu đủ bản đầu trong `first-pass/`, rồi bật `no_key_hue` của công cụ tách nền để khử sắc khóa. So hai bản 1024: **3.326 pixel đổi RGB, 0 pixel đổi alpha**, không tăng/giảm sáng. Bản cuối còn **396/291.170 = 0,13600%**, đạt. Đây là sửa sắc nền ở mép; không xóa vật, vẽ đè hay sửa hình. Bằng chứng: [edge-repair.json](../../games/dragon-hold/art-src/_review/140/178/edge-repair.json).

**Poster:** nguồn lượt 3 đúng khổ, nên bản chọn **chép nguyên byte**, không cắt, đổi màu, tăng sáng, nung hộp tối hay sửa núi. MD5 bản chọn và `.try3` cùng là `f50ee312fa2adc999b6cd219cb44156f`. Chỉ bản thu và ảnh kiểm được đổi cỡ/cắt. Logo chỉ ghép trên tờ kiểm, không nằm trong ảnh giao.

Hai tờ bắt buộc, mỗi cặp có cùng cỡ hiển thị:

- [Icon: bản sinh | bản hậu kỳ cuối](../../games/dragon-hold/art-src/_review/140/178/easier-raw-vs-final-final.jpg), mỗi ô 512².
- [Poster: bản sinh | bản hậu kỳ](../../games/typing-defense/art-src/_review/158/178/poster-raw-vs-final-final.jpg), mỗi ô cao 640 px.

Các tờ không có hậu tố `-final` của icon phản ánh bước trước sửa sắc mép; giữ làm lịch sử. Dùng tờ `-final` và `metrics-delivery.json` để chấm nhận. Hai bộ tờ poster giống nhau vì poster không có lần sửa hậu kỳ.

## 4. Kiểm kỹ thuật và cỡ dùng

### Icon

[Kết quả đầy đủ](../../games/dragon-hold/art-src/_review/140/178/metrics-delivery.json), [identify](../../games/dragon-hold/art-src/_review/140/178/identify-delivery.txt). Đúng bốn khổ, 8-bit sRGBA; mọi khổ có alpha min 0, max 255.

| Khổ | Bbox alpha >16, x0/y0/x1/y1 | Cạnh dài / ô | Alpha mềm ngoài mép 3 px | Sắc M / pixel hiện | Sắc M (%) |
|---|---|---:|---:|---:|---:|
| 1024² | 154 / 192 / 870 / 831 | 69,92188% | 0 | 396 / 291170 | 0,13600 |
| 256² | 38 / 48 / 218 / 208 | 70,31250% | 0 | 11 / 19359 | 0,05682 |
| 128² | 19 / 24 / 109 / 104 | 70,31250% | 0 | 0 / 5134 | 0 |
| 64² | 9 / 12 / 55 / 52 | 71,87500% | 0 | 0 / 1448 | 0 |

Lệch tâm bản gốc lớn nhất **0,04883%**, dưới 2%; cạnh dài trong 68–72%. Dải mép lấy hiệu giãn/co vuông bán kính 3 px quanh alpha ≥128. Sắc M: hue cách 300° không quá 15°, S >0,5, đếm trên mọi pixel alpha >0.

| Cỡ icon | ΔY nền vỏ cây `#2b2118` | ΔY nền kem `#f1e3c4` | Đọc trên bản hậu kỳ |
|---|---:|---:|---|
| 16 px | 0,48557 | 0,27232 | Đọc được hướng bậc hạ và nét mũi tên xuống; các mặt bậc nhỏ, vết nứt mất. |
| 24 px | 0,48099 | 0,27690 | Ba tầng và mũi tên rõ hơn, không ra giày. |

ΔY là chênh luma Rec.709 trung bình có trọng số alpha sau khi thu đúng cỡ. Cả hai nền và hai cỡ đều ≥0,25. Xem [tờ cỡ thật và phóng nearest ×4](../../games/dragon-hold/art-src/_review/140/178/easier-sheet-final.jpg), kèm `easier` cũ, `upgrade`, bốn icon cùng bộ và HUD mẫu. Hướng bậc và tên mới xuống phải, ngược với `upgrade` lên phải.

**IoU:** alpha >16 sau thu Lanczos về 32²; so toàn bộ **40 icon tên chính** của 137–140, trừ `easier` cũ chưa nhận, cộng **9 bản v2/final** hiện có để không bỏ sót các bản làm lại. Tổng 49 phép so. Lớn nhất **0,65761** với `danger.v2.final`, dưới 0,80; riêng 40 tên chính lớn nhất **0,64896** với `slot-house`; với `upgrade` **0,55037**. Bản `swarm.v2.try2.final` xuất hiện trong lúc làm cũng đã so: **0,55801**.

### Poster

[Khổ và kênh](../../games/typing-defense/art-src/_review/158/178/identify-final.txt), [kết quả và tọa độ](../../games/typing-defense/art-src/_review/158/178/metrics.json).

| Kiểm trên bản giao | Kết quả |
|---|---|
| 1024 × 1536, nền đặc sRGB; không chữ lạc | Đạt. Không ép từ ảnh ngang. |
| Cạnh dài 384 px: nhận ra rồng, cây khổng lồ, Fort, sông | Đạt. Rồng và tia lửa là trọng tâm; cây và Fort vẫn tách được. |
| Hai cánh trọn khung, cánh lông rộng gắn ở vai | Đạt. Không còn hai thân rắn của `poster.v2.try2`. |
| 20% trên không có rồng | Đạt. Dải kết thúc ở y=307,2; đầu cánh cao nhất khoảng y=365, tức 23,8% chiều cao. |
| Logo 113 rộng 70% trên trời | Đọc được, không chạm rồng. Chỉ đặt thử trên tờ kiểm. |
| Cây cao nhất ở nửa trái | **Chưa đạt.** Đỉnh karst xa khoảng x=45, y=724; tán cao nhất khoảng x=310, y=733. Vách nhỉnh hơn khoảng 9 px gốc, tương đương 2,25 px khi thu cạnh dài 384. |

Tọa độ là **đọc bằng mắt trên crop**, xấp xỉ ±4 px, không phải phép phân đoạn tự động. [Tờ nhỏ và logo](../../games/typing-defense/art-src/_review/158/178/poster-small-logo-final.jpg); [crop đỉnh cây/vách](../../games/typing-defense/art-src/_review/158/178/left-crown-detail.jpg); [so nguồn sửa, bản mới, keyart và tham chiếu chủ dự án cùng cao 640 px](../../games/typing-defense/art-src/_review/158/178/poster-vs-ref-final.jpg).

Sau ba lượt, giữ bản này vì cánh đúng, khoảng trời đạt và cảnh còn đẹp. **Không coi sai số nhỏ là đã đạt luật cây cao nhất.** Không xóa hay san phẳng đỉnh núi để ép kiểm; Claude cần quyết nhận ngoại lệ này hay cấp lượt sửa riêng. Không tự nới giới hạn ba lượt.

## 5. KA5 · Tự chấm trên bản hậu kỳ

Thứ tự Q: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. M so mức thương mại của ảnh chủ dự án, không suy từ số đo. Đã xem bản giao đầy đủ và cỡ dùng, không chỉ xem bản sinh.

| Bản chọn | Q đầy đủ | Q cỡ dùng | M đầy đủ / cỡ dùng | Mức và hạn chế |
|---|---|---|---:|---|
| `easier.v3` | 2 / 2 / 1,5 / 2 / 2 = **9,5** | 16 px: 2 / 1,5 / 1,5 / 2 / 2 = **9** | **8 / 8** | **Tự chấm đạt**, chờ Claude. Khối đá và vàng hoàn thiện; ba bậc đơn giản, cùng bộ. Mặt vát bậc còn có độ dày nhẹ; cỡ 16 mất chi tiết mặt đá. |
| `poster.v3` | 1,5 / 2 / 2 / 2 / 1 = **8,5** | cạnh dài 384: 1,5 / 1,5 / 2 / 2 / 1 = **8** | **8 / 8** | Tranh đứng cạnh được về ánh sáng, lớp sâu và nhân vật; trời rộng hơn. **Chưa nhận vì kiểm cây cao nhất trượt**, dù điểm M/Q đạt ngưỡng. Chi tiết vẫn dày ở nửa dưới. |

Không tự ghi nhận thay Claude. `Dùng tiếp` của poster chỉ 1 vì còn kiểm bắt buộc chưa đạt; không tính điểm trung bình để bỏ qua kiểm đó.

## 6. KA1 · File cũ và công việc đồng thời

Đã chạy `md5 -q` cho từng file để dựng bảng tương đương `md5 -r`, trên toàn bộ `art-src/ui/` của mỗi game trước/sau. `diff` chỉ có dòng thêm; không file cũ đổi hoặc mất.

| Game | File trước / sau | Thêm | Đổi / mất |
|---|---:|---:|---:|
| Dragonhold | 579 / 609 | 30: **12 file của phiếu 178**, cộng 18 file `swarm.v2.try2*` xuất hiện do công việc đồng thời | 0 / 0 |
| Wordwoven | 195 / 205 | **10 file của phiếu 178** | 0 / 0 |

Không nhận 18 file `swarm` là sản phẩm của mình; không ghi hoặc sửa chúng. Bằng chứng: [Dragonhold](../../games/dragon-hold/art-src/_review/140/178/md5-audit.json), [Wordwoven](../../games/typing-defense/art-src/_review/158/178/md5-audit.json), cùng `md5-before.txt`, `md5-after.txt`, `md5.diff` trong hai hồ sơ.

## 7. Chạy lại và phần không làm

Script đã dùng: `process.py`, `refine.py`, `verify.py`, `sheets.py`, `audit.py` trong hồ sơ Dragonhold. `replay.py` dựng lại bản icon cuối từ nguồn giữ sẵn; `deliver.py` trong hồ sơ Wordwoven dựng lại poster. Dùng thư mục đích mới; không gọi AI, không ghi đè bản giao:

```bash
export ART_MAGICK=/opt/homebrew/bin/magick
python3 -B games/dragon-hold/art-src/_review/140/178/replay.py games/dragon-hold/art-src/_review/140/178/replay-moi
python3 -B games/typing-defense/art-src/_review/158/178/deliver.py games/typing-defense/art-src/_review/158/178/replay-moi
```

Không làm âm thanh, không tích hợp hoặc chép vào `public/`, vì phiếu chỉ giao hai ảnh cho Claude đổi sang sau nhận. Không sửa `ART_REPLACE_LATER.md` hay tài liệu khác ngoài báo cáo; phạm vi phiếu không cho phép. Không chạy Git, build, bộ test game, dev server hoặc trình duyệt. Không đọc/ghi Tu Tiên hay `.wt-*`. Không có capture trình duyệt hoặc frame thô cần prune; chỉ tạo tờ so và crop dùng trong báo cáo, mọi ảnh đều có prompt cạnh bên.

**Cần Claude/chủ dự án xem:** icon ở 16/24 px trên hai nền; poster ở 384 px, đặc biệt đỉnh karst xa trái còn cao hơn tán cây. Không còn lượt sửa poster trong ngân sách phiếu này.
