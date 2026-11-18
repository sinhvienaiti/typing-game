# Phiếu 162 · Dragonhold · Khung UI và bảng sử thi

**Ngày:** 29/10/2026. **Thực hiện:** Codex, công cụ `image_gen` tích hợp.

**Có đủ chín bản chọn, prompt, alpha nguyên độ phân giải, năm JSON 9-slice và bộ ảnh kiểm. Chưa đánh dấu nghiệm thu toàn bộ:** còn ba nhóm ngưỡng số cần người duyệt quyết định theo `ART_ACCEPTANCE.md` §5. `checks.json` giữ `strict_acceptance_pass: false`; không ép số bằng cách bỏ phần vẽ.

## 1. Giao ở đâu

- Chín món: [`games/dragon-hold/art-src/ui/frames/`](../../games/dragon-hold/art-src/ui/frames/): `panel-large`, `plate-long`, `button`, `button-active`, `banner`, `tooltip`, `portrait-ring`, `crest`, `divider`.
- Mỗi món có `.png`, `.prompt.txt`, `.alpha.png`, `.alpha.prompt.txt`; giữ mọi `.tryN.png` và prompt nguyên văn. Có 11 lượt sinh thực sự: tám lượt đầu, hai lượt hai và một lượt ba. Active là ảnh dẫn xuất, không sinh mới.
- [Tờ chín bản chọn](../../games/dragon-hold/art-src/_review/162-selected.jpg), [toàn bộ ba cỡ 9-slice](../../games/dragon-hold/art-src/_review/162-sheet.jpg), [cỡ nhỏ](../../games/dragon-hold/art-src/_review/162-small.jpg), [mép 4×](../../games/dragon-hold/art-src/_review/162-edge.jpg), [chữ thử](../../games/dragon-hold/art-src/_review/162-text.jpg).
- [HUD trận 1280 × 720 cạnh tham chiếu](../../games/dragon-hold/art-src/_review/162-mock.jpg), [mock 1280 × 720 riêng](../../games/dragon-hold/art-src/_review/162/mock-1280x720.png), [bảng tạm dừng với ba nút](../../games/dragon-hold/art-src/_review/162-pause-mock.jpg), [so tham chiếu và HUD hiện tại](../../games/dragon-hold/art-src/_review/162-vs-ref.jpg).
- Script, nguồn tham chiếu, số đo, KA1: [`_review/162/README.md`](../../games/dragon-hold/art-src/_review/162/README.md).

Đã đọc phiếu 115, mục chấm nhận 115, `ART_ACCEPTANCE` §5 và STYLE-UI Dragonhold §3.2. Đã xem ảnh tham chiếu chủ dự án, các tờ icon 137–139 và mock tựa 119. Prompt giữ nguyên văn khối STYLE-UI Dragonhold; dùng hoa cương kem, sắt rèn, vàng búa, men than hồng, vảy rồng và cành thông.

## 2. Chọn lượt và hậu kỳ

| Món | Chọn | Điều chỉnh theo từng lượt |
| --- | --- | --- |
| `panel-large` | try1 | Viền hoa cương có góc vảy rồng và thông, lòng sắt có vân; giữ nguyên toàn bộ phần vẽ. |
| `plate-long` | try2 | Try1 có đầu rồng lớn chiếm cả chiều cao. Try2 chuyển thành bốn chốt góc nhỏ, cạnh giữa liên tục. Giảm sáng RGB toàn tranh 10% để chữ đạt 7:1. |
| `button` | try3 | Try1 có đầu rồng lớn và khớp riêng ở giữa cạnh. Try2 bỏ hai lỗi đó nhưng lòng còn nhiều hạt sáng; thử giảm sáng 10% vẫn chưa đủ sau khi sửa cách dựng lòng. Try3 yêu cầu sắt than sẫm, vân ít tương phản, ánh sáng tập trung ở viền. Chọn try3, không áp bước giảm sáng của try2 lên bản giao. |
| `button-active` | dẫn xuất từ button try3 | Cùng hình, kích thước, alpha và đường cắt; tăng sáng vàng tối đa 10%, cộng ánh than hồng RGB tối đa +(25,10,2) giảm theo khoảng cách tới viền. Không sinh mới, không thay lòng. |
| `banner` | try1 | Giữ dải đuôi én, hai huy chương vảy rồng, hoa cương và vàng búa. |
| `tooltip` | try1 | Khung mảnh, chốt hoa cương và thông ở góc, lòng sắt có vân. |
| `portrait-ring` | try1 | Giữ vòng vảy rồng, bốn điểm men cam; lòng đã tách trong suốt. |
| `crest` | try1 | Giữ đầu rồng và hai cành thông. Sửa ba pixel phản nền sáng sát mép; không đổi hình. |
| `divider` | try1 | Giữ đường vàng búa và men than hồng giữa, hai đầu thông. Sửa sáu pixel phản nền sáng sát mép; không đổi hình. |

Tách nền bằng thuật toán của `tools/art-normalize/key-alpha.sh`, chế độ global, protect-interior, no-key-hue. Wrapper chỉ chuyển WORK vào phạm vi `_review/162/`; không sửa hay ghi vào công cụ dùng chung. Dùng ImageMagick 7 ở `/opt/homebrew/bin/magick` và Arial hệ thống.

Lượt dựng kiểm đầu lát lặp cả lòng nên xuất hiện các dải vân. Đã bỏ cách đó: chỉ cạnh dùng `round`; lòng giữ nguyên mảng vân sinh và co giãn theo 9-slice. Không trải màu `fill`, không vẽ lại rail, không xóa hay thu nhỏ góc trong ảnh nguồn.

## 3. Khổ, đường cắt và chữ

**Khổ bản `.png`:** bốn món vuông 1024 × 1024; năm món ngang 1536 × 512, đúng phiếu 115. Công cụ sinh trả ảnh vuông 1254 × 1254 và ảnh ngang 2172 × 724. Đã giữ nguyên các bản `.tryN` và `.alpha.png` ở khổ gốc; bản `.png` xuất bằng `-filter Lanczos -resize 1024x1024!` hoặc `1536x512!`. Không cắt tranh. Bản alpha dùng cho bước tích hợp giữ toàn bộ pixel nguồn.

`size`, `slice` và `source` trong JSON trỏ vào **alpha gốc**. `content=[x0,y0,x1,y1]` bỏ lề trong suốt khi dựng. Bốn số slice là khoảng cách tính từ mép canvas gốc, thứ tự L/R/T/B; góc giữ cùng một tỷ lệ hiển thị ở cả ba cỡ kiểm.

| Khung | Size alpha | Slice L/R/T/B | Tỷ lệ hiển thị | `repeat` |
| --- | --- | --- | ---: | --- |
| panel-large | 1254 × 1254 | 312 / 312 / 312 / 312 | 0,16 | round |
| plate-long | 2172 × 724 | 243 / 244 / 304 / 305 | 0,14 | round |
| button | 2172 × 724 | 245 / 245 / 336 / 338 | 0,13 | round |
| button-active | 2172 × 724 | 245 / 245 / 336 / 338 | 0,13 | round |
| tooltip | 1254 × 1254 | 256 / 256 / 256 / 256 | 0,22 | round |

Đường ngang của nút ở y=336 và y=386 nằm sau toàn bộ cành thông. Alpha và slice của hai trạng thái trùng tuyệt đối. Bản dựng thử có đủ 480 × 160, 320 × 320, 720 × 120; kiểm thêm 320 × 96. Vòng chân dung và crest ở 64 px còn nhận ra dáng vòng, đầu rồng và hai cành thông; chi tiết vảy nhỏ không còn đọc riêng ở cỡ đó.

Chữ thử đúng ba chuỗi tiếng Anh của phiếu 115, màu `#f3ead2`, 24 px, trên bản dựng 480 × 160. Đo nền dưới những pixel thuộc nét chữ, lấy điểm xấu nhất, không thay bằng trung vị:

| Khung | WCAG nhỏ nhất dưới chữ | Trung vị | Ngưỡng ≥ 7 |
| --- | ---: | ---: | --- |
| panel-large | 9,335:1 | 12,980:1 | Qua |
| plate-long | 7,176:1 | 12,881:1 | Qua |
| button | 7,144:1 | 12,507:1 | Qua |
| button-active | 7,144:1 | 12,507:1 | Qua |
| tooltip | 9,537:1 | 13,175:1 | Qua |

Số này áp dụng cho bố cục và tỷ lệ đã dựng. Không công bố mọi hạt sáng của vân ở kích thước nguồn đều đạt 7:1: cực tiểu toàn vùng nguồn vẫn thấp hơn, được giữ nguyên trong `metrics.json`. Khi tích hợp ở tỷ lệ khác phải kiểm chữ trong cảnh.

## 4. Những mục chưa qua — giữ tranh theo §5

Mọi alpha đều min 0, max 255; tâm `portrait-ring` có alpha 0. Nhưng phép hue tuyệt đối của phiếu 115 vẫn đếm các bóng tím rất tối và một phần sắc phản nền nằm trong nét thông:

| Món | Pixel hue 285–330°, S > 0,5, alpha > 0 | % pixel thấy được | Điểm rời <20 px |
| --- | ---: | ---: | ---: |
| panel-large | 826 | 0,06355% | 0 |
| plate-long | 367 | 0,05849% | 1 |
| button | 312 | 0,03637% | 0 |
| button-active | 58 | 0,00676% | 0 |
| banner | 1042 | 0,21315% | 1 |
| tooltip | 1025 | 0,08921% | 0 |
| portrait-ring | 678 | 0,14265% | 0 |
| crest | 1542 | 0,44388% | 3 |
| divider | 376 | 0,39530% | 0 |

- **Hue chưa về 0.** Bảy món đầu không có pixel trong nhóm này sáng tới V=90/255. Ví dụ bóng nguồn có RGB (1,0,1), (13,2,9); xóa theo hue sẽ đục phần vẽ. Crest còn 11 pixel và divider còn 36 pixel với V≥90 ở các nét phía trong. Đã sửa chín pixel sáng thật sự sát mép trong bán kính 3 px; dừng trước khi phải đổi màu sơn phía trong. Mép thông còn chút tím nhìn thấy ở phóng 4×, cần người duyệt xem trực tiếp.
- **Điểm rời chưa về 0.** Plate-long, banner và crest còn lần lượt 1, 1, 3 thành phần; mỗi thành phần chỉ 1 pixel ở khổ nguồn. Không tự xóa nét nguồn để công bố 0. Tọa độ trong `*-components.txt`.
- **Rail panel-large vượt σ=0,05.** Theo thứ tự trên/dưới/trái/phải: 0,04382 / 0,04365 / **0,07259 / 0,07060**. Đây là vân và khe hoa cương dọc. San phẳng để đạt số sẽ mất chất liệu. Giữ nguyên tranh và `repeat: round`; bốn khung còn lại đều có σ lớn nhất ≤0,05 sau khi đặt đúng đường cắt.

Đây là ngoại lệ cần phân xử, **không phải các mục đã qua**. Không hạ ngưỡng, không thêm điều kiện độ sáng vào phép kiểm gốc để biến false thành true. Hồ sơ máy đọc: [checks.json](../../games/dragon-hold/art-src/_review/162/checks.json), [metrics.json](../../games/dragon-hold/art-src/_review/162/metrics.json), [preservation.json](../../games/dragon-hold/art-src/_review/162/preservation.json).

## 5. Tự chấm trên bản hậu kỳ

Q theo thứ tự Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp. Điểm mỹ thuật không thay thế các mục trượt số ở trên; chưa có lượt chấm nhận độc lập trong phiếu này.

| Món | M | Q | Nhận xét ở cỡ dùng |
| --- | ---: | --- | --- |
| panel-large | 8,5 | 9 (2/2/2/2/1) | Còn đủ góc chạm và hoa cương, lòng có vân; chờ phân xử độ biến thiên rail. |
| plate-long | 8 | 9 (2/2/2/2/1) | Viền nhẹ, hợp icon, chữ rõ; điểm rời 1 px và phép hue chưa qua. |
| button | 8,5 | 9 (2/2/2/2/1) | Vân sắt có khối, nguyên góc, đã cắt sau cành thông; còn bóng bị phép hue đếm. |
| button-active | 8 | 8,5 (2/1,5/2/2/1) | Cùng hình, viền than hồng rõ ở cỡ vừa; chênh trạng thái còn tiết chế ở cỡ rất nhỏ. |
| banner | 8,5 | 9 (2/2/2/2/1) | Hai huy chương lửa và đuôi én đọc rõ; chưa qua điểm rời/hue tuyệt đối. |
| tooltip | 8 | 9 (2/2/2/2/1) | Gọn, đúng chất liệu, chữ rõ; chốt góc hơi to khi kéo cực thấp. |
| portrait-ring | 8,5 | 9 (2/2/2/2/1) | Vòng và bốn điểm men rõ ở 64 px, lòng trong suốt. |
| crest | 8,5 | 8,5 (2/1,5/2/2/1) | Đầu rồng có khối, thông hợp bộ; dày chi tiết ở 64 px, còn tím ở vài nét. |
| divider | 8 | 9 (2/2/2/2/1) | Vàng búa và men cam đọc được, không thành đường CSS; vài nét thông còn tím. |

**Mock HUD: M 8. Mock tạm dừng: M 8.** Đứng cạnh được về chất liệu khung và sự thống nhất với icon; HUD giữ viền mảnh, icon gánh phần hình. Ảnh trận nguồn vẫn là cảnh cũ, không dùng điểm này để nhận chất lượng cảnh hay xác nhận runtime đã tích hợp. Nguồn chỉ đọc: `games/dragon-hold/tmp/gate-r2/shots/telegraphs/telegraph-blight-wolf-1280x720.png`. Gear Settings mượn đọc từ `ui/quick-settings/hud-settings.256.png` vừa xuất hiện ở làn song song, không tính là ảnh do 162 làm.

Chín tờ cùng cỡ “bản sinh | bản hậu kỳ”:

- [panel-large](../../games/dragon-hold/art-src/_review/162-panel-large-raw-vs-final.jpg), [plate-long](../../games/dragon-hold/art-src/_review/162-plate-long-raw-vs-final.jpg), [button](../../games/dragon-hold/art-src/_review/162-button-raw-vs-final.jpg), [button-active](../../games/dragon-hold/art-src/_review/162-button-active-raw-vs-final.jpg).
- [banner](../../games/dragon-hold/art-src/_review/162-banner-raw-vs-final.jpg), [tooltip](../../games/dragon-hold/art-src/_review/162-tooltip-raw-vs-final.jpg), [portrait-ring](../../games/dragon-hold/art-src/_review/162-portrait-ring-raw-vs-final.jpg), [crest](../../games/dragon-hold/art-src/_review/162-crest-raw-vs-final.jpg), [divider](../../games/dragon-hold/art-src/_review/162-divider-raw-vs-final.jpg).

Ở active, cột trái là bản dẫn xuất chưa tách nền, không phải một lượt sinh mới. Tờ bộ có hai trạng thái nút để so trực tiếp.

## 6. KA1, phạm vi và việc còn lại

KA1 toàn `games/dragon-hold/art-src/ui/`: **609 file trước, 764 file sau; 0 file cũ đổi md5, 0 file cũ bị mất**. Chênh lệch chỉ thêm: **65 file của phiếu này dưới `ui/frames/`**, cộng **90 file `ui/quick-settings/` do làn song song**. Danh sách tách riêng ở `ka1.json`; không nhận phần quick-settings là việc 162 đã làm.

Chỉ ghi vào `ui/frames/`, `_review/162*` và báo cáo này. Không chạy Git, dev server, game, build hay test suite; không ghi mã runtime, không động Tu Tiên. Không sinh âm thanh. Không có ảnh chụp trình duyệt mới hoặc chuỗi raw frame cần prune; giữ đủ nguồn sinh bắt buộc, xóa các mảnh ghép tạm do chính script tạo ngay sau khi ghép.

**Người duyệt cần xem:** ba ngoại lệ ở mục 4, đặc biệt mép thông của crest/divider và rail hoa cương panel-large; sau đó chấm nhận M/Q trên alpha nguyên cỡ và các mock. Chưa tích hợp vào game vì phiếu chỉ cho phép giao art. Không sửa các danh sách/chỉ đạo nghệ thuật ngoài báo cáo vì không nằm trong phạm vi được ghi.
