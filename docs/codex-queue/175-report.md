# Phiếu 175 · Last Line · Texture plasma, kính đen và hư không hướng B

Ngày 29/10/2026 · Bộ giao chờ Claude chấm lại. **Đủ 12 bản chọn; chưa đạt điều kiện xong toàn bộ phiếu.** `void-smoke` còn hai cặp IoU ngoài dải và Q = 7,5. Mười một tấm còn lại qua các số đo đã kiểm và tự chấm M, Q từ 8. Các điểm này là tự chấm, chưa phải duyệt nhận.

## Phạm vi và nguồn

Khi bắt đầu lượt xử lý này, thư mục đã có 18 ảnh `.tryN.png`, đủ 18 prompt, cùng các bản hậu kỳ trung gian; chưa có báo cáo hoặc bộ bản chọn ở `vfx/b-pack`. Tiếp tục từ các tệp có sẵn, không sinh thêm và không ghi lượt sinh giả. Các prompt đã đối chiếu đủ khối STYLE §4.3 nguyên văn và câu `Stylized painterly game VFX texture, hand-painted, not photographic.` Nguồn gọi công cụ của các lượt cũ không có nhật ký độc lập trong thư mục; báo cáo ghi nguyên văn prompt cạnh tệp, không suy diễn thêm về lịch sử thực thi.

Chỉ tạo tệp trong `games/typing-survival/art-src/vfx/b-pack/`, `games/typing-survival/art-src/_review/175*` và báo cáo này. Không chạy lệnh Git, build, bộ test, dev server, trình duyệt hoặc mạng; không sửa mã, tài liệu khác, game khác hay Tu Tiên. Không có âm thanh trong phiếu. Không có lượt chụp trình duyệt mới hoặc khung chụp thô cần prune.

## Bộ giao và tờ duyệt

- [Thư mục 12 texture](../../games/typing-survival/art-src/vfx/b-pack): mỗi tên có `.png`, `.alpha.png`, `.prompt.txt`, `.json`; giữ nguyên toàn bộ `.tryN` và prompt cũ.
- [Tờ đầy đủ · 4096 × 29336 · khoảng 16,9 MB](../../games/typing-survival/art-src/_review/175-sheet-full.jpg): 12 tấm ở khổ giao, dải khung ở cỡ dự kiến trong game, so trước/sau và hai bản ghép lên ảnh trận; đầu tờ có ảnh mẫu thương mại và ý tưởng hướng B.
- [Tờ xem nhanh 12 bản chọn](../../games/typing-survival/art-src/_review/175/resume-selected-contact.jpg); [Tờ toàn bộ 18 lượt sinh](../../games/typing-survival/art-src/_review/175/resume-tries.jpg).
- Tờ đúng tên yêu cầu [175-sheet.jpg](../../games/typing-survival/art-src/_review/175-sheet.jpg) chỉ có mục đầu: script kế thừa bị thụt dòng ở bước ghép tờ, nên xuất sớm rồi dừng ở mục thứ hai. Giữ nguyên tệp đã tạo theo luật cấm ghi đè; bản đầy đủ chuyển sang `175-sheet-full.jpg`. Đây là sai lệch của lượt xử lý, không coi tờ một mục là tờ nghiệm thu.

Ảnh trận đọc từ [720-raytia-before.png](../../games/typing-survival/tmp/mac-2026-10-27/feel-n4n6/judge2/own/keep/720-raytia-before.png). Dùng đúng cùng ảnh 1280×720, đặt texture tại vùng sáng và tối, không tô lại nền. Luma trung bình sRGB của ô mẫu 80²: sáng `[610,130,80,80]` = **0,684432**, tối `[340,600,80,80]` = **0,202099**. Các dòng trên tờ làm tròn từ số đo trước đó; chênh dưới 0,00001. Đây là phép ghép tĩnh kiểm texture; ảnh trận vẫn thuộc bản game cũ, chưa có nhân vật hướng B và chưa chứng minh VFX khi shader chạy.

| Tên | Lượt chọn / số lượt | Khổ giao; lưới | fps; lặp | Blend | Cỡ kiểm trong game | Tờ riêng |
|---|---|---|---|---|---|---|
| [plasma-bolt](../../games/typing-survival/art-src/vfx/b-pack/plasma-bolt.png) | 1/1 | 2048×512; 8×2 | 24; có | additive | 64×64 px | [xem](../../games/typing-survival/art-src/_review/175/resume-sheets-v2/plasma-bolt/page.jpg) |
| [heat-beam](../../games/typing-survival/art-src/vfx/b-pack/heat-beam.png) | 1/1 | 2048×256; 1×1 | 0; không | additive | 512×64 px | [xem](../../games/typing-survival/art-src/_review/175/resume-sheets-v2/heat-beam/page.jpg) |
| [muzzle-star](../../games/typing-survival/art-src/vfx/b-pack/muzzle-star.png) | 2/2 | 1024×512; 4×2 | 60; không | additive | 96×96 px | [xem](../../games/typing-survival/art-src/_review/175/resume-sheets-v2/muzzle-star/page.jpg) |
| [glass-shards](../../games/typing-survival/art-src/vfx/b-pack/glass-shards.png) | 1/1 | 2048×512; 8×2 | 0; không | normal | 32×32 px | [xem](../../games/typing-survival/art-src/_review/175/resume-sheets-v2/glass-shards/page.jpg) |
| [crack-glow](../../games/typing-survival/art-src/vfx/b-pack/crack-glow.png) | 1/1 | 1024×1024; 1×1 | 0; không | additive | 128×128 px | [xem](../../games/typing-survival/art-src/_review/175/resume-sheets-v2/crack-glow/page.jpg) |
| [void-smoke](../../games/typing-survival/art-src/vfx/b-pack/void-smoke.png) | 3/3 | 2048×1024; 8×4 | 30; không | normal | 160×160 px | [xem](../../games/typing-survival/art-src/_review/175/resume-sheets-v2/void-smoke/page.jpg) |
| [shield-hex](../../games/typing-survival/art-src/vfx/b-pack/shield-hex.png) | 2/2 | 1024×1024; 1×1 | 0; không | additive | 128×128 px | [xem](../../games/typing-survival/art-src/_review/175/resume-sheets-v2/shield-hex/page.jpg) |
| [impact-burst](../../games/typing-survival/art-src/vfx/b-pack/impact-burst.png) | 3/3 | 4096×2048; 8×4 | 60; không | additive | 192×192 px | [xem](../../games/typing-survival/art-src/_review/175/resume-sheets-v2/impact-burst/page.jpg) |
| [scorch-deck](../../games/typing-survival/art-src/vfx/b-pack/scorch-deck.png) | 1/1 | 2048×1024; 2×1 | 0; không | normal | 160×160 px | [xem](../../games/typing-survival/art-src/_review/175/resume-sheets-v2/scorch-deck/page.jpg) |
| [rune-ring](../../games/typing-survival/art-src/vfx/b-pack/rune-ring.png) | 1/1 | 1024×1024; 1×1 | 0; không | additive | 160×160 px | [xem](../../games/typing-survival/art-src/_review/175/resume-sheets-v2/rune-ring/page.jpg) |
| [glyph-spark](../../games/typing-survival/art-src/vfx/b-pack/glyph-spark.png) | 1/1 | 1024×256; 4×1 | 0; không | additive | 32×32 px | [xem](../../games/typing-survival/art-src/_review/175/resume-sheets-v2/glyph-spark/page.jpg) |
| [cape-glow](../../games/typing-survival/art-src/vfx/b-pack/cape-glow.png) | 1/1 | 2048×1024; 4×2 | 24; có | additive | 128×128 px | [xem](../../games/typing-survival/art-src/_review/175/resume-sheets-v2/cape-glow/page.jpg) |

## Hậu kỳ và bảo toàn tranh

Đọc bản trung gian `delivery/` đã có, đối chiếu bản giao cuối trùng byte với từng atlas ở đó. Việc hậu kỳ trước đó được kiểm qua script và tờ so: chia đúng lưới, đổi cỡ giữ tỉ lệ từng ô và thêm lề (hệ số đặt trong ô 0,86; không kéo méo hình), tách nền magenta ở ba tấm blend thường, sửa mép và khử nhiễm màu sát viền. `heat-beam` đổi sang 2048×256 và hòa hai đầu trong dải 24 px; `impact-burst` và `cape-glow` nhân RGB 0,96, nằm trong ±10%. Không vẽ đè, thay tranh, nội suy ra khung mới hoặc nhân bản khung để đạt IoU.

`plasma-bolt` được xếp lại khung từ lượt 1 theo thứ tự gốc đánh số từ 0: `0, 1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15, 8, 9, 10, 7`. Các tấm khác giữ thứ tự gốc. Thứ tự này đạt kiểm mặt nạ; độ tự nhiên của chuyển động vẫn cần Claude xem trong shader. `void-smoke` giữ nguyên 32 khung, không bóp dáng hoặc đổi thứ tự chỉ để kéo số vào dải.

Tấm additive: `.png` giữ nền đen; `.alpha.png` giữ nguyên RGB và chỉ cho alpha = 0 ở pixel có max(R,G,B) ≤ 2, còn lại 255. File alpha này là bản phụ để xem/tách nền; atlas RGB dùng cộng sáng ONE + ONE, độ mờ do shader quản lý. Tấm normal: `.png` và `.alpha.png` đều là RGBA thẳng, dùng source-over. Kiểm cả 12 bản phụ: **0 pixel đổi RGB** so với atlas tương ứng.

Khổ nguồn công cụ không trùng khổ giao; không đánh đồng việc phóng ảnh với chi tiết gốc. Bảng dưới và JSON giữ kích thước nguồn để làn VFX quyết định mức phóng chấp nhận được.

| Tên | Khổ nguồn | Tờ bản sinh / hậu kỳ cùng hộp hiển thị | Dải khung nguyên cỡ |
|---|---|---|---|
| plasma-bolt | 2172×724 | [so đầy đủ](../../games/typing-survival/art-src/_review/175/resume-full-evidence/plasma-bolt-before-after.jpg) | [dải khung](../../games/typing-survival/art-src/_review/175/resume-full-evidence/plasma-bolt-native-strip.png) |
| heat-beam | 2172×724 | [so đầy đủ](../../games/typing-survival/art-src/_review/175/resume-full-evidence/heat-beam-before-after.jpg) | tĩnh / biến thể |
| muzzle-star | 1774×887 | [so đầy đủ](../../games/typing-survival/art-src/_review/175/resume-full-evidence/muzzle-star-before-after.jpg) | [dải khung](../../games/typing-survival/art-src/_review/175/resume-full-evidence/muzzle-star-native-strip.png) |
| glass-shards | 2079×756 | [so đầy đủ](../../games/typing-survival/art-src/_review/175/resume-full-evidence/glass-shards-before-after.jpg) | tĩnh / biến thể |
| crack-glow | 1254×1254 | [so đầy đủ](../../games/typing-survival/art-src/_review/175/resume-full-evidence/crack-glow-before-after.jpg) | tĩnh / biến thể |
| void-smoke | 1774×887 | [so đầy đủ](../../games/typing-survival/art-src/_review/175/resume-full-evidence/void-smoke-before-after.jpg) | [dải khung](../../games/typing-survival/art-src/_review/175/resume-full-evidence/void-smoke-native-strip.png) |
| shield-hex | 1254×1254 | [so đầy đủ](../../games/typing-survival/art-src/_review/175/resume-full-evidence/shield-hex-before-after.jpg) | tĩnh / biến thể |
| impact-burst | 1774×887 | [so đầy đủ](../../games/typing-survival/art-src/_review/175/resume-full-evidence/impact-burst-before-after.jpg) | [dải khung](../../games/typing-survival/art-src/_review/175/resume-full-evidence/impact-burst-native-strip.png) |
| scorch-deck | 1774×887 | [so đầy đủ](../../games/typing-survival/art-src/_review/175/resume-full-evidence/scorch-deck-before-after.jpg) | tĩnh / biến thể |
| rune-ring | 1254×1254 | [so đầy đủ](../../games/typing-survival/art-src/_review/175/resume-full-evidence/rune-ring-before-after.jpg) | tĩnh / biến thể |
| glyph-spark | 2172×724 | [so đầy đủ](../../games/typing-survival/art-src/_review/175/resume-full-evidence/glyph-spark-before-after.jpg) | tĩnh / biến thể |
| cape-glow | 1774×887 | [so đầy đủ](../../games/typing-survival/art-src/_review/175/resume-full-evidence/cape-glow-before-after.jpg) | [dải khung](../../games/typing-survival/art-src/_review/175/resume-full-evidence/cape-glow-native-strip.png) |

## Kiểm số

Luma = `(0,2126R + 0,7152G + 0,0722B)/255`, tính trực tiếp trên kênh sRGB, không phải luma tuyến tính. Mặt nạ additive là max(R,G,B) > 8; normal là alpha ≥ 128. Khung sáng nhất là khung có tổng luma × alpha lớn nhất. Bán kính vật lấy nửa cạnh dài nhất của hộp mặt nạ; bán kính lõi trắng lấy nửa cạnh dài nhất của cụm liên thông lớn nhất có luma > 0,92. Riêng beam dùng nửa bề dày theo chiều dọc. Phương pháp này đo một lõi liên thông, không vòng tròn bao tất cả các tia trắng rời nhau.

Kiểm alpha bằng dải hình thái Chebyshev ±3 px quanh đường alpha 50%. Pixel mang màu khóa đếm khi alpha > 0, R > 160, B > 150, G < 65 và min(R,B) − G > 100; phần trăm chia trên toàn atlas. Đây là phép đo màu còn sót, không bảo đảm mép đẹp bằng mắt. Các tấm normal vẫn có số nhỏ, nhất là scorch; không xóa phần vẽ để làm đẹp số. Nền đen đo riêng dải trống 3 px quanh mỗi ô; với beam bỏ hai cạnh trái/phải vì tia phải chạy xuyên qua đó.

| Tên | Khổ | Nền đen max /255 | Alpha lưng chừng ngoài mép 3 px | Màu khóa còn lại % | Khung đỉnh (từ 0) | Lõi trắng / bán kính % | IoU min–max |
|---|---|---|---|---|---|---|---|
| plasma-bolt | đạt | 0 | 0 | 0.00000 | 14 | 23.03 | 0.57025–0.83697 |
| heat-beam | đạt | 1 | 0 | 0.00000 | 0 | 12.07 | không áp dụng |
| muzzle-star | đạt | 0 | 0 | 0.00000 | 0 | 23.72 | 0.75927–0.87145 |
| glass-shards | đạt | không áp dụng | 0 | 0.02451 | 5 | 9.18 | không áp dụng |
| crack-glow | đạt | 0 | 0 | 0.00000 | 0 | 3.94 | không áp dụng |
| void-smoke | đạt | không áp dụng | 0 | 0.06213 | 6 | 0.49 | 0.51707–0.95028 |
| shield-hex | đạt | 0 | 0 | 0.00000 | 0 | 7.31 | không áp dụng |
| impact-burst | đạt | 0 | 0 | 0.00000 | 0 | 20.96 | 0.74399–0.92443 |
| scorch-deck | đạt | không áp dụng | 0 | 0.10610 | 0 | 3.17 | không áp dụng |
| rune-ring | đạt | 0 | 0 | 0.00000 | 0 | 18.66 | không áp dụng |
| glyph-spark | đạt | 0 | 0 | 0.00000 | 2 | 30.00 | không áp dụng |
| cape-glow | đạt | 0 | 0 | 0.00000 | 2 | 20.79 | 0.87552–0.91380 |

Heat beam: chênh RGB trái/phải **MAE = 0, max = 0/255**. Cả chín atlas additive có nền trống ≤ 2/255; heat beam đạt 1/255 ở mép trên/dưới, tám tấm còn lại 0. Cả 12 tấm đạt khổ và ngưỡng lõi trắng theo phương pháp trên. `glyph-spark` đúng 30%, cần giữ nguyên mức sáng khi duyệt.

Flipbook: plasma 16/16 cặp đạt kể cả cuối–đầu; muzzle 7/7; impact 31/31; cape 8/8 kể cả cuối–đầu. Void smoke **29/31** cặp đạt: khung **6→7 = 0,95028**, khung **23→24 = 0,51707** (đánh số từ 0). Không làm tròn 0,95028 thành 0,95 để ghi đạt. Giữ bản 3 vì đã hết ba lượt; theo `ART_ACCEPTANCE.md` §5, dừng khi muốn sửa số phải làm lệch phần vẽ và chuyển Claude quyết.

Ba dải luma ở khung đỉnh: sáng > 0,75; thân > 0,18 đến 0,75; mép ≤ 0,18, chỉ tính trong mặt nạ vật. Đây là số đếm kiểm khoảng sáng tối, tách biệt với phép đo lõi trắng > 0,92. Màu kiểm bằng mắt: lam điện / trắng vàng ở phe ta; vàng trắng → vàng mật → đồng ở rune; trắng mảnh → vàng/cam → cam đỏ ở heat; kính navy/đen và cạnh cam; tím tối ở khói. Normal smoke/scorch không cần một lõi phát sáng trắng.

| Tên | Sáng (px) | Thân (px) | Mép (px) |
|---|---:|---:|---:|
| plasma-bolt | 1093 | 3617 | 5036 |
| heat-beam | 31369 | 105573 | 69497 |
| muzzle-star | 3778 | 13344 | 10067 |
| glass-shards | 409 | 6413 | 9285 |
| crack-glow | 13653 | 79277 | 212840 |
| void-smoke | 6 | 9732 | 20892 |
| shield-hex | 19069 | 93712 | 236529 |
| impact-burst | 18391 | 73304 | 47503 |
| scorch-deck | 7922 | 163478 | 180206 |
| rune-ring | 39922 | 107276 | 127677 |
| glyph-spark | 1531 | 4849 | 5513 |
| cape-glow | 5155 | 24953 | 36995 |

Số đo đầy đủ: [resume-measurements.json](../../games/typing-survival/art-src/_review/175/resume-measurements.json), [resume-alpha-check.json](../../games/typing-survival/art-src/_review/175/resume-alpha-check.json), [resume-context-luma.json](../../games/typing-survival/art-src/_review/175/resume-context-luma.json). Lưới được chia đều; nội dung khung có dao động tự nhiên về hộp bao, chưa có phép duyệt chuyển động trực tiếp trong game.

## KA5 · Tự chấm bản hậu kỳ

M chấm mức hoàn thiện và khả năng đọc của texture trên bản ghép, so trực tiếp với độ hoàn thiện của ảnh mẫu chủ dự án và hướng B; không nâng điểm cho cả cảnh trận cũ. Kết luận **đứng cạnh được ở chất liệu và chi tiết VFX**, còn cảnh tổng chưa được đổi hướng trong phiếu này. Q gồm năm tiêu chí 0–2: đúng đề, đọc được, hợp bộ, hình khối, dùng tiếp. Các điểm 8–8,5 cần Claude chấm độc lập; chưa có người chấm thứ hai trong lượt này.

| Tên | M | Q | Năm điểm Q | Nhận xét trên bản giao |
|---|---:|---:|---|---|
| plasma-bolt | 8 | 8.5 | 2 / 1.5 / 2 / 1.5 / 1.5 | Đầu đạn và các sợi xoáy rõ, không thành hình nón trơn; cần Claude xem nhịp lặp sau khi đổi thứ tự khung. |
| heat-beam | 8.5 | 9 | 2 / 2 / 2 / 1.5 / 1.5 | Có dòng xoáy cam/vàng và khe tối bên trong; làm liền mép bằng dải 24 px, không thay phần giữa. |
| muzzle-star | 8 | 8.5 | 2 / 1.5 / 2 / 1.5 / 1.5 | Lượt 2 giữ cùng ngôi sao rồi co dần; ở nền sáng một phần cánh lam chìm vào ánh đòn cũ. |
| glass-shards | 8 | 8 | 2 / 1.5 / 2 / 1.5 / 1 | Đủ 16 mảnh kính cạnh cam; ở cỡ 32 px đọc dáng tốt hơn chi tiết mặt kính; còn một ít viền khóa màu. |
| crack-glow | 8.5 | 9 | 2 / 2 / 2 / 1.5 / 1.5 | Nhánh nứt có nhiều bề dày, khe sáng nằm trong khối kính tối; không có khung vuông. |
| void-smoke | 8 | 7.5 | 2 / 1.5 / 1.5 / 1.5 / 1 | KHÔNG ĐẠT Q: còn nhảy dáng ở chuyển hàng 3 sang 4; một cặp đầu gần đứng yên. Đã hết ba lượt, giữ tranh theo §5. |
| shield-hex | 8 | 8.5 | 2 / 1.5 / 2 / 1.5 / 1.5 | Lượt 2 giảm lõi trắng ở các góc; cạnh có sợi sáng và vết xước, lòng khiên tối; viền hơi dày. |
| impact-burst | 8.5 | 8.5 | 2 / 1.5 / 2 / 1.5 / 1.5 | Lượt 3 lóe ngay đầu, tia cam chuyển sang khói tím; khổ 4096×2048 có phần phóng lớn từ nguồn, không phải chi tiết gốc 4K. |
| scorch-deck | 8 | 8 | 2 / 1.5 / 1.5 / 1.5 / 1.5 | Đủ vết tròn và vệt dài, có muội và nứt nóng. Mép còn sắc tím/magenta thấy ở cỡ gốc; chỉ tự chấm sát ngưỡng, Claude cần xem kỹ. |
| rune-ring | 8.5 | 9 | 2 / 2 / 2 / 1.5 / 1.5 | Vòng trắng vàng có nét khắc và khoảng đen lớn ở giữa; ký hiệu hình học không có chữ đọc được. |
| glyph-spark | 8 | 8.5 | 2 / 1.5 / 2 / 1.5 / 1.5 | Bốn dáng khác nhau đọc ở 32 px; lõi khung sáng nhất chạm đúng giới hạn 30%, không tăng sáng thêm khi nhập shader. |
| cape-glow | 8 | 8.5 | 2 / 1.5 / 2 / 1.5 / 1.5 | Dòng sáng chạy trên đường cong chữ S; vòng lặp có IoU trong dải, cần xem cùng áo choàng thật khi nhập shader. |

## KA1 · Bảo toàn tệp

Chạy `md5 -r` trên **1020 tệp có sẵn** trong hai thư mục đích trước khi thêm sản phẩm của lượt này; lưu [resume-before.md5](../../games/typing-survival/art-src/_review/175/resume-before.md5). Đã đối chiếu lại toàn bộ 1020 tệp: **0 thay đổi, 0 mất**. `ka1-before.md5` cũ rỗng được giữ nguyên; không dùng nó để giả chứng minh lịch sử trước lượt tiếp tục. Sau khi ghi báo cáo, lập [resume-after.md5](../../games/typing-survival/art-src/_review/175/resume-after.md5) và [resume-ka1.diff](../../games/typing-survival/art-src/_review/175/resume-ka1.diff); diff dữ liệu chỉ được có dòng thêm. Các tệp tự ghi kết quả kiểm (`resume-after.md5`, `resume-ka1.diff`, `resume-ka1-result.json`) loại khỏi chính danh sách của chúng để tránh tự băm; báo cáo và mọi tệp sản phẩm còn lại đều có trong danh sách sau. Kết quả cuối nằm ở [resume-ka1-result.json](../../games/typing-survival/art-src/_review/175/resume-ka1-result.json).

## Chỗ khác phiếu và việc cần người nhận xem

1. Bộ có đủ 12 bản chọn, nhưng chưa thể ghi xong vì `void-smoke` không qua IoU và Q < 8 sau ba lượt. Claude quyết giữ bản 3 làm nguồn, chỉnh thời gian/mặt nạ ở shader hay mở cách làm khác; không cấp thêm lượt sinh trong báo cáo này.
2. Tờ đầy đủ dùng tên `175-sheet-full.jpg`; giữ tờ `175-sheet.jpg` chỉ có mục đầu để không ghi đè. Người nhận dùng tờ đầy đủ và 12 tờ riêng.
3. Có phóng ảnh nguồn, rõ nhất `impact-burst` từ 1774×887 lên 4096×2048; xem dải nguyên cỡ, không coi là nguồn 4K. Beam có đổi tỉ lệ canvas để đạt 2048×256. Không sinh thêm vì đã có bộ thử; không xác nhận thay lịch sử công cụ cũ bằng một lần gọi mới.
4. Xem kỹ viền khóa màu ở `scorch-deck`, `glass-shards`, `void-smoke`, lõi đúng 30% của `glyph-spark`, nhịp sau đổi thứ tự của plasma và độ đọc trên nền sáng. Không tăng điểm vì chỉ đạt số.
5. Chưa gắn shader hoặc thử trong game theo phạm vi phiếu. Thời lượng, độ sáng, che thẻ chữ và đủ năm pha theo VFX_STANDARD phải được làn VFX kiểm khi tích hợp. Các kích thước trong game ở đây là kích thước kiểm tĩnh dự kiến, không phải cấu hình runtime đã xác nhận.

## Prompt nguyên văn từng lượt

Giữ đầy đủ 18 tệp prompt cạnh ảnh thử. Dưới đây là nội dung nguyên văn để kiểm lại, không phải prompt mới. Bản chọn `.prompt.txt` trùng byte với prompt của lượt chọn.

### plasma-bolt

[plasma-bolt.try1.prompt.txt](../../games/typing-survival/art-src/vfx/b-pack/plasma-bolt.try1.prompt.txt)

```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted, not photographic.
Use case: stylized-concept. Asset type: production VFX texture for shader integration, not a scene illustration. The STYLE paragraph supplies world identity, palette and paint treatment only. Render ONLY the isolated effect described next, with no character, environment, UI, floor, labels or grid lines.
Canvas: 2048 by 512 pixels. Precisely aligned atlas, 8 equal columns by 2 equal rows, zero gutters; row-major reading order. Each frame/object has exactly the same cell centre; no visible dividers. Exactly sixteen chronological animation frames of ONE electric-cyan plasma projectile pointing RIGHT, compact molten head at the exact centre of every cell, tapered split lightning tail to the left. Small white-gold core under 15 percent of projectile radius, large richly painted turquoise/cyan body, deep cobalt curling perimeter. Consistent silhouette with 10–20 percent undulating edge change per frame, stable scale, head position and luminous intensity; frames form one smooth repeating cycle, including final to first. All frames wholly contained with 24px black clearance. Fluid sculpted internal filaments and eddies, sharp energized tips, painterly volumetric depth. Not a solid cone.
Background: uniform absolute pure #000000 black; additive blending. Paint the coloured glow into the effect only, leaving the empty margins mathematically black.
Premium commercial action-game texture detail, crisp at native size and readable at game size. No text, numerals, symbols resembling readable language, logos or watermark.
```

### heat-beam

[heat-beam.try1.prompt.txt](../../games/typing-survival/art-src/vfx/b-pack/heat-beam.try1.prompt.txt)

```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted, not photographic.
Use case: stylized-concept. Asset type: production VFX texture for shader integration, not a scene illustration. The STYLE paragraph supplies world identity, palette and paint treatment only. Render ONLY the isolated effect described next, with no character, environment, UI, floor, labels or grid lines.
Canvas: 2048 by 256 pixels. One long horizontal continuous orange-gold HEAT BEAM STRIP, 2048 by 256 pixels. It stretches completely from left edge to right edge and tiles seamlessly horizontally: both boundary cross-sections match in colour and height. A very thin warm-white molten axial line less than 10 percent beam half-height, gold and amber turbulent body, orange-red rolling eddies on edges, intricate painted flowing striations and dark internal troughs. Middle-centred with broad pure black margins above and below. Consistent width throughout, no projectile head, no endpoints.
Background: uniform absolute pure #000000 black; additive blending. Paint the coloured glow into the effect only, leaving the empty margins mathematically black.
Premium commercial action-game texture detail, crisp at native size and readable at game size. No text, numerals, symbols resembling readable language, logos or watermark.
```

### muzzle-star

[muzzle-star.try1.prompt.txt](../../games/typing-survival/art-src/vfx/b-pack/muzzle-star.try1.prompt.txt)

```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted, not photographic.
Use case: stylized-concept. Asset type: production VFX texture for shader integration, not a scene illustration. The STYLE paragraph supplies world identity, palette and paint treatment only. Render ONLY the isolated effect described next, with no character, environment, UI, floor, labels or grid lines.
Canvas: 1024 by 512 pixels. Precisely aligned atlas, 4 equal columns by 2 equal rows, zero gutters; row-major reading order. Each frame/object has exactly the same cell centre; no visible dividers. Exactly EIGHT chronological animation frames of a sentinel-gun muzzle flash viewed front-on: an irregular six-point cyan star with a tiny warm-white-gold core, azure petal-shaped tongues, cobalt edge wisps, scattered short sharp sparks. Frame 1 already at full brightness, frame 2 similarly bright, then star contracts and breaks into thinner blue filaments, ending in a faint small remnant. Same exact centre each frame. Sculpted painted light, intricate interior energy, strong dimensional overlaps. Every star isolated with 24px black cell clearance.
Background: uniform absolute pure #000000 black; additive blending. Paint the coloured glow into the effect only, leaving the empty margins mathematically black.
Premium commercial action-game texture detail, crisp at native size and readable at game size. No text, numerals, symbols resembling readable language, logos or watermark.
```

[muzzle-star.try2.prompt.txt](../../games/typing-survival/art-src/vfx/b-pack/muzzle-star.try2.prompt.txt)

```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted, not photographic.
Use case: stylized-concept. Asset type: production VFX texture for shader integration, not a scene illustration. The STYLE paragraph supplies world identity, palette and paint treatment only. Render ONLY the isolated effect described next, with no character, environment, UI, floor, labels or grid lines.
Canvas: 1024 by 512 pixels. Precisely aligned atlas, 4 equal columns by 2 equal rows, zero gutters; row-major reading order. Each frame/object has exactly the same cell centre; no visible dividers. Exactly EIGHT chronological animation frames of a sentinel-gun muzzle flash viewed front-on: an irregular six-point cyan star with a tiny warm-white-gold core, azure petal-shaped tongues, cobalt edge wisps, scattered short sharp sparks. Frame 1 already at full brightness, frame 2 similarly bright, then star contracts and breaks into thinner blue filaments, ending in a faint small remnant. Same exact centre each frame. Sculpted painted light, intricate interior energy, strong dimensional overlaps. Every star isolated with 24px black cell clearance.
Background: uniform absolute pure #000000 black; additive blending. Paint the coloured glow into the effect only, leaving the empty margins mathematically black.
Premium commercial action-game texture detail, crisp at native size and readable at game size. No text, numerals, symbols resembling readable language, logos or watermark.
Revision 2. Make the central white nucleus much smaller: a single tiny white dot at 6 percent star radius, every extended ray remains saturated electric cyan or warm amber instead of near-white. Keep absolute pure-black generous margins occupying at least 20 percent of every cell width on all sides. First star has its maximum size and brightness, then each frame gently contracts by roughly 8 percent in radius; the last frame is still at least 50 percent the initial radius with coloured internal tongues, letting the shader fade it out afterward. All seven adjacent silhouette overlaps must remain 0.60–0.90. Smooth morphology, no abrupt final shrink.
```

### glass-shards

[glass-shards.try1.prompt.txt](../../games/typing-survival/art-src/vfx/b-pack/glass-shards.try1.prompt.txt)

```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted, not photographic.
Use case: stylized-concept. Asset type: production VFX texture for shader integration, not a scene illustration. The STYLE paragraph supplies world identity, palette and paint treatment only. Render ONLY the isolated effect described next, with no character, environment, UI, floor, labels or grid lines.
Canvas: 2048 by 512 pixels. Precisely aligned atlas, 8 equal columns by 2 equal rows, zero gutters; row-major reading order. Each frame/object has exactly the same cell centre; no visible dividers. Exactly SIXTEEN DISTINCT individual black-glass fragments in EIGHT columns and TWO rows, square equal cells. One whole shard in each cell, all different angular silhouettes and rotations, centrally placed and fully isolated with 24px clearance. Obsidian glass with layered translucent navy facets, razor thin orange-hot luminous fracture edges and small warm gold pin highlights, bold readable shapes, finely painted bevels and internal fracture planes. These are fragments of shattered Hollow Swarm armour, no ground, no shadows outside shard. Flat solid pure magenta #FF00FF background for chroma extraction.
Normal blending; background is flat #FF00FF magenta, completely separate from the object. Preserve every painted interior detail and silhouette.
Premium commercial action-game texture detail, crisp at native size and readable at game size. No text, numerals, symbols resembling readable language, logos or watermark.
```

### crack-glow

[crack-glow.try1.prompt.txt](../../games/typing-survival/art-src/vfx/b-pack/crack-glow.try1.prompt.txt)

```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted, not photographic.
Use case: stylized-concept. Asset type: production VFX texture for shader integration, not a scene illustration. The STYLE paragraph supplies world identity, palette and paint treatment only. Render ONLY the isolated effect described next, with no character, environment, UI, floor, labels or grid lines.
Canvas: 1024 by 1024 pixels. One centred irregular NETWORK OF INCANDESCENT ORANGE FRACTURES on black glass, face-on square texture. Fine branching jagged branching fissures open into a few wider molten seams. Thin pale-gold internal highlights under 10 percent total network radius, amber-orange major veins, ember red fading edge glow, subtle graphite glass bevels immediately alongside fissures. Rich varied branch weights and chipped crystalline intersections, asymmetrical organic connected network, generous black empty outer border 64px. The black glass merges into pure black background; no square panel border.
Background: uniform absolute pure #000000 black; additive blending. Paint the coloured glow into the effect only, leaving the empty margins mathematically black.
Premium commercial action-game texture detail, crisp at native size and readable at game size. No text, numerals, symbols resembling readable language, logos or watermark.
```

### void-smoke

[void-smoke.try1.prompt.txt](../../games/typing-survival/art-src/vfx/b-pack/void-smoke.try1.prompt.txt)

```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted, not photographic.
Use case: stylized-concept. Asset type: production VFX texture for shader integration, not a scene illustration. The STYLE paragraph supplies world identity, palette and paint treatment only. Render ONLY the isolated effect described next, with no character, environment, UI, floor, labels or grid lines.
Canvas: 2048 by 1024 pixels. Precisely aligned atlas, 8 equal columns by 4 equal rows, zero gutters; row-major reading order. Each frame/object has exactly the same cell centre; no visible dividers. Exactly THIRTY-TWO chronological frames of one central VOID SMOKE PLUME: starts as a small dense black-violet knot, swells into rotating layered charcoal billows with subtle violet rim highlights, folds inward and slowly disperses into wispy broken tendrils. Temporal change is gradual between every pair including row transitions, not thirty-two independent smoke concepts. Density carried in painted RGB shading with solid smoke silhouettes and narrow soft edges; dark graphite dominates, small violet accents. Same fixed centre and ample cell padding, no clipping. Flat pure magenta #FF00FF backdrop; avoid magenta in smoke; no surrounding cast shadow.
Normal blending; background is flat #FF00FF magenta, completely separate from the object. Preserve every painted interior detail and silhouette.
Premium commercial action-game texture detail, crisp at native size and readable at game size. No text, numerals, symbols resembling readable language, logos or watermark.
```

[void-smoke.try2.prompt.txt](../../games/typing-survival/art-src/vfx/b-pack/void-smoke.try2.prompt.txt)

```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted, not photographic.
Use case: stylized-concept. Asset type: production VFX texture for shader integration, not a scene illustration. The STYLE paragraph supplies world identity, palette and paint treatment only. Render ONLY the isolated effect described next, with no character, environment, UI, floor, labels or grid lines.
Canvas: 2048 by 1024 pixels. Precisely aligned atlas, 8 equal columns by 4 equal rows, zero gutters; row-major reading order. Each frame/object has exactly the same cell centre; no visible dividers. Exactly THIRTY-TWO chronological frames of one central VOID SMOKE PLUME: starts as a small dense black-violet knot, swells into rotating layered charcoal billows with subtle violet rim highlights, folds inward and slowly disperses into wispy broken tendrils. Temporal change is gradual between every pair including row transitions, not thirty-two independent smoke concepts. Density carried in painted RGB shading with solid smoke silhouettes and narrow soft edges; dark graphite dominates, small violet accents. Same fixed centre and ample cell padding, no clipping. Flat pure magenta #FF00FF backdrop; avoid magenta in smoke; no surrounding cast shadow.
Normal blending; background is flat #FF00FF magenta, completely separate from the object. Preserve every painted interior detail and silhouette.
Premium commercial action-game texture detail, crisp at native size and readable at game size. No text, numerals, symbols resembling readable language, logos or watermark.
Revision 2. A new production atlas with generous isolation. Every smoke cloud occupies at most the central 55 percent of its square cell; leave the outer 22 percent of each side perfectly flat magenta. Dense OPAQUE charcoal-painted cloud masses, sharply separated from the flat magenta backdrop by a clean narrow antialiased edge; the interior is deep neutral charcoal with restrained blue-violet ridges and retains solid dark painted RGB. The first frame is already a substantial full cloud about 65 percent of the maximum cloud diameter. Grow gently until frame 8, then curl and erode gently over the remaining frames into a smaller coherent smoky remnant, last frame about 45 percent maximum diameter. Each consecutive frame changes radius only 3–6 percent and contour gently rotates, silhouette IoU 0.65–0.90. The last cloud retains opaque painted tendrils, with final global disappearance to be handled by shader. Precisely eight columns and four rows.
```

[void-smoke.try3.prompt.txt](../../games/typing-survival/art-src/vfx/b-pack/void-smoke.try3.prompt.txt)

```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted, not photographic.
Stylized-concept production VFX atlas only. Render EXACTLY 32 individually isolated OPAQUE hand-painted charcoal smoke sprites in 8 columns and 4 rows, equal square cells. Canvas 2048x1024. Flat pure #FF00FF magenta backdrop. Every cell has a wide magenta margin. Every sprite is a solid dark graphite cloud with a crisp opaque silhouette and extremely narrow antialiased outer edge, like a painted cut-paper smoke illustration with sophisticated internal volumetric brushwork. The smoke interior is neutral BLACK and SLATE GREY, only very small electric-violet highlights on inner ridges. Its dark body completely covers and blocks the magenta background. Preserve deep blue-grey cloud folds and charcoal shadows. The magenta belongs exclusively to the blank backdrop, cleanly separate from the opaque charcoal paint.
Animate ONE centred cloud through 32 very gradual stages, row-major. Start with a developed cloud at 65% full diameter. Grow to full diameter over first eight cells. Then curl, break gently and slowly contract to 50% diameter over next 24 cells, with opaque dark tendrils and interior smoky brushwork in every frame. Equal centre and orientation anchors in all cells. Limit body to central 65% of each cell with generous margins. Every adjacent pair has enough visible contour motion to overlap 0.60–0.92, including row transitions. The cloud dissolves by small fragments peeling away and the remaining solid body contracting. Leave the final whole-sprite opacity fade to the shader.
Rich dimensional dark painterly smoke whorls, strongest detail in broad readable folds. Exactly 8 opaque clouds on each of 4 rows. No scenery, text, numerals, labels, grid, logos, shadows outside silhouette or watermark.
```

### shield-hex

[shield-hex.try1.prompt.txt](../../games/typing-survival/art-src/vfx/b-pack/shield-hex.try1.prompt.txt)

```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted, not photographic.
Use case: stylized-concept. Asset type: production VFX texture for shader integration, not a scene illustration. The STYLE paragraph supplies world identity, palette and paint treatment only. Render ONLY the isolated effect described next, with no character, environment, UI, floor, labels or grid lines.
Canvas: 1024 by 1024 pixels. One centred single HEXAGONAL SHIELD PLATE seen straight-on, six precise but subtly distressed sides. A thin electric-cyan perimeter with sharp blue rim highlights, a dim translucent navy glass interior carrying delicate concentric hexagonal fracture filaments, small white-gold glints at three corners, restrained energy crawling along edge. Broad dark negative centre reads clearly through additive blending. Rich hand-painted light striations and fine micro-abrasion grouped into readable bands, not a flat vector icon. Whole hexagon fits within 96px pure black margin.
Background: uniform absolute pure #000000 black; additive blending. Paint the coloured glow into the effect only, leaving the empty margins mathematically black.
Premium commercial action-game texture detail, crisp at native size and readable at game size. No text, numerals, symbols resembling readable language, logos or watermark.
```

[shield-hex.try2.prompt.txt](../../games/typing-survival/art-src/vfx/b-pack/shield-hex.try2.prompt.txt)

```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted, not photographic.
Use case: stylized-concept. Asset type: production VFX texture for shader integration, not a scene illustration. The STYLE paragraph supplies world identity, palette and paint treatment only. Render ONLY the isolated effect described next, with no character, environment, UI, floor, labels or grid lines.
Canvas: 1024 by 1024 pixels. One centred single HEXAGONAL SHIELD PLATE seen straight-on, six precise but subtly distressed sides. A thin electric-cyan perimeter with sharp blue rim highlights, a dim translucent navy glass interior carrying delicate concentric hexagonal fracture filaments, small white-gold glints at three corners, restrained energy crawling along edge. Broad dark negative centre reads clearly through additive blending. Rich hand-painted light striations and fine micro-abrasion grouped into readable bands, not a flat vector icon. Whole hexagon fits within 96px pure black margin.
Background: uniform absolute pure #000000 black; additive blending. Paint the coloured glow into the effect only, leaving the empty margins mathematically black.
Premium commercial action-game texture detail, crisp at native size and readable at game size. No text, numerals, symbols resembling readable language, logos or watermark.
Revision 2. Make the hex shield rim entirely saturated electric blue and cyan: luminous but coloured even at its brightest. White-gold exists only as three tiny separated pinpoints, each at most 2 percent overall diameter. Dark navy glazing, fine rich hand-painted refractive cracks in cobalt and azure, broad dark empty middle. A single perfectly flat face-on hexagon. Entire effect including wisps stays inside the central 70 percent of the square, leaving wide absolute black margins.
```

### impact-burst

[impact-burst.try1.prompt.txt](../../games/typing-survival/art-src/vfx/b-pack/impact-burst.try1.prompt.txt)

```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted, not photographic.
Use case: stylized-concept. Asset type: production VFX texture for shader integration, not a scene illustration. The STYLE paragraph supplies world identity, palette and paint treatment only. Render ONLY the isolated effect described next, with no character, environment, UI, floor, labels or grid lines.
Canvas: 4096 by 2048 pixels. Precisely aligned atlas, 8 equal columns by 4 equal rows, zero gutters; row-major reading order. Each frame/object has exactly the same cell centre; no visible dividers. Exactly THIRTY-TWO chronological frames of one plasma impact smashing orange-cracked black glass. First frame is a brilliant compact CYAN flash with a tiny white-gold core; next frames eject pointed black-glass silhouettes outlined orange, broad broken electric-blue shock petals, hot amber sparks; layered dark-violet smoke whorls grow after the flash and decay into thin embers at the end. First frame maximum luminous power, tiny white nucleus below 15 percent radius. Smooth gradual animation with stable centre and controlled growth/shrink, neighbouring silhouettes overlap 65–85 percent. Each frame fully inside equal square cell with 48px clearance. Additive asset: smoke reads as faint violet illuminated ridges separated by black troughs, glass reads through orange edge highlights.
Background: uniform absolute pure #000000 black; additive blending. Paint the coloured glow into the effect only, leaving the empty margins mathematically black.
Premium commercial action-game texture detail, crisp at native size and readable at game size. No text, numerals, symbols resembling readable language, logos or watermark.
```

[impact-burst.try2.prompt.txt](../../games/typing-survival/art-src/vfx/b-pack/impact-burst.try2.prompt.txt)

```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted, not photographic.
Use case: stylized-concept. Asset type: production VFX texture for shader integration, not a scene illustration. The STYLE paragraph supplies world identity, palette and paint treatment only. Render ONLY the isolated effect described next, with no character, environment, UI, floor, labels or grid lines.
Canvas: 4096 by 2048 pixels. Precisely aligned atlas, 8 equal columns by 4 equal rows, zero gutters; row-major reading order. Each frame/object has exactly the same cell centre; no visible dividers. Exactly THIRTY-TWO chronological frames of one plasma impact smashing orange-cracked black glass. First frame is a brilliant compact CYAN flash with a tiny white-gold core; next frames eject pointed black-glass silhouettes outlined orange, broad broken electric-blue shock petals, hot amber sparks; layered dark-violet smoke whorls grow after the flash and decay into thin embers at the end. First frame maximum luminous power, tiny white nucleus below 15 percent radius. Smooth gradual animation with stable centre and controlled growth/shrink, neighbouring silhouettes overlap 65–85 percent. Each frame fully inside equal square cell with 48px clearance. Additive asset: smoke reads as faint violet illuminated ridges separated by black troughs, glass reads through orange edge highlights.
Background: uniform absolute pure #000000 black; additive blending. Paint the coloured glow into the effect only, leaving the empty margins mathematically black.
Premium commercial action-game texture detail, crisp at native size and readable at game size. No text, numerals, symbols resembling readable language, logos or watermark.
Revision 2. Deliver a large detailed 4096 by 2048 texture atlas, exactly 8 columns by 4 rows. FIRST FRAME IS THE MAXIMUM LUMINOUS PLASMA IMPACT: a large luminous electric-cyan multi-lobed shattering burst, same overall radius as frames 2–8, already showing orange-glass edges and dim violet smoke. Subsequent frames smoothly replace cyan flash petals with orange-edged black-glass fracture lobes and dark violet smoke curls, then diminish gradually. Last frame still has a coherent dark blue-violet curling smoke remnant with a few orange sparks; shader will fade the rest. Consecutive masks overlap 0.60–0.90, including final pair. Every effect is fully isolated in the middle 60 percent of each cell, at least 20 percent absolute black padding every side. White only a tiny dot, 5 percent effect radius; all extended rays saturated cyan. Large detailed volumetric paint, clear glass edge highlights. Keep tiny smoke wisps inside the same protected zone.
```

[impact-burst.try3.prompt.txt](../../games/typing-survival/art-src/vfx/b-pack/impact-burst.try3.prompt.txt)

```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted, not photographic.
Use case: stylized-concept. Production VFX atlas, isolated effect only. Render a precise SPRITE SHEET with EXACTLY FOUR ROWS, EACH ROW CONTAINS EXACTLY EIGHT FRAMES: total 32 separate frames. Layout 8 columns by 4 rows, all cells square and aligned with zero gutter. Canvas 4096x2048. Row 1 holds frames 1–8. Row 2 holds 9–16. Row 3 holds 17–24. Row 4 holds 25–32. Full pure black background #000000. NO labels, numbers, grid lines, UI or scenery.
The same centre-anchored plasma impact shattering orange-cracked black glass animates chronologically left to right, top to bottom. Every effect contained within central 60% of its cell, with a wide clean black surround.
ROW 1: begins AT PEAK with large bright sculpted ELECTRIC CYAN petal-shaped plasma burst, tiny warm-white nucleus, sharp orange-edged obsidian shards, faint purple smoke; next seven frames gradually dim cyan and roll the same outline.
ROW 2: eight smooth continuation frames: cyan diminishes, orange-lit glass pieces separate slowly, violet smoke curls thicken.
ROW 3: eight smooth continuation frames: fewer orange sparks, violet-charcoal smoke curls dominate and slowly contract.
ROW 4: eight smooth continuation frames: dark curled smoke, few dim embers, gradual contraction to half peak diameter, last two silhouettes similar in size. Final disappearance belongs to the shader.
First frame has highest luminous energy of entire atlas. White exists only as one tiny nucleus at 5% effect radius. All extended light remains saturated cyan or orange, with rich internal dark folds. All 31 consecutive silhouette overlaps 0.60–0.90: gentle contour movement between every pair, including row boundaries. Premium hand-painted volumetric microstructure in broad readable masses. All FOUR rows equally tall and all EIGHT columns equally wide. Exactly THIRTY-TWO effects.
```

### scorch-deck

[scorch-deck.try1.prompt.txt](../../games/typing-survival/art-src/vfx/b-pack/scorch-deck.try1.prompt.txt)

```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted, not photographic.
Use case: stylized-concept. Asset type: production VFX texture for shader integration, not a scene illustration. The STYLE paragraph supplies world identity, palette and paint treatment only. Render ONLY the isolated effect described next, with no character, environment, UI, floor, labels or grid lines.
Canvas: 2048 by 1024 pixels. Precisely aligned atlas, 2 equal columns by 1 equal rows, zero gutters; row-major reading order. Each frame/object has exactly the same cell centre; no visible dividers. Exactly TWO different TOP-DOWN isolated SCORCH DECALS side by side, equal 1024 square cells. Irregular burnt damage marks for graphite steel causeway surface; left a compact plasma-scorched radial molten fracture, right an elongated gouged heat-beam burn with radiating cracked steel flakes. Carbon-black soot broken into richly painted irregular islands, blue-grey heat-discoloured steel exposed inside, a few dim ember-orange hairline cracks. Organic asymmetric jagged eroded edges with narrow soft soot fringe. No intact rectangular steel plate, no floor outside marks, no perspective, ample 96px margin per cell. Flat solid pure magenta #FF00FF background for chroma extraction.
Normal blending; background is flat #FF00FF magenta, completely separate from the object. Preserve every painted interior detail and silhouette.
Premium commercial action-game texture detail, crisp at native size and readable at game size. No text, numerals, symbols resembling readable language, logos or watermark.
```

### rune-ring

[rune-ring.try1.prompt.txt](../../games/typing-survival/art-src/vfx/b-pack/rune-ring.try1.prompt.txt)

```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted, not photographic.
Use case: stylized-concept. Asset type: production VFX texture for shader integration, not a scene illustration. The STYLE paragraph supplies world identity, palette and paint treatment only. Render ONLY the isolated effect described next, with no character, environment, UI, floor, labels or grid lines.
Canvas: 1024 by 1024 pixels. One centred WHITE-GOLD LUMINOUS RUNE RING viewed directly overhead, circular not elliptical. Two delicate concentric broken metallic-light arcs linked by angular abstract nonlinguistic geometric motifs and small diamond marks, gently uneven hand-painted energy strokes, warm ivory highlights under 10 percent ring radius, honey-gold body and dim bronze outer wisps, tiny cyan accents. Fine layered engraved-light detail grouped into a clean readable circle around a large completely empty black centre. Entire ring within 96px pure black outside margin. Symbols are abstract invented shapes, not letters, numbers, readable text or real scripts.
Background: uniform absolute pure #000000 black; additive blending. Paint the coloured glow into the effect only, leaving the empty margins mathematically black.
Premium commercial action-game texture detail, crisp at native size and readable at game size. No text, numerals, symbols resembling readable language, logos or watermark.
```

### glyph-spark

[glyph-spark.try1.prompt.txt](../../games/typing-survival/art-src/vfx/b-pack/glyph-spark.try1.prompt.txt)

```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted, not photographic.
Use case: stylized-concept. Asset type: production VFX texture for shader integration, not a scene illustration. The STYLE paragraph supplies world identity, palette and paint treatment only. Render ONLY the isolated effect described next, with no character, environment, UI, floor, labels or grid lines.
Canvas: 1024 by 256 pixels. Precisely aligned atlas, 4 equal columns by 1 equal rows, zero gutters; row-major reading order. Each frame/object has exactly the same cell centre; no visible dividers. Exactly FOUR DIFFERENT compact typing-confirmation SPARK FLARES, ONE per square cell in a single row. Small warm-white nuclei, each under 12 percent flare radius, two or four electric-cyan wings and sharp curling cobalt filaments with subtle white-gold pin flecks. Distinct cross, diagonal, winged and crescent energy gestures; rich painterly internal light texture and pointed energetic motion, readable at 24 pixels. Centre each flare in its cell with 32px pure black padding. Pure abstract energy, no glyph letters or readable writing.
Background: uniform absolute pure #000000 black; additive blending. Paint the coloured glow into the effect only, leaving the empty margins mathematically black.
Premium commercial action-game texture detail, crisp at native size and readable at game size. No text, numerals, symbols resembling readable language, logos or watermark.
```

### cape-glow

[cape-glow.try1.prompt.txt](../../games/typing-survival/art-src/vfx/b-pack/cape-glow.try1.prompt.txt)

```text
Epic mythic science-fiction game art for Last Line, set on the last causeway of a colossal space station at the edge of a black hole, where a lone armoured Lightbearer with a long cape, a glowing visor and two floating sentinel guns holds the line against the Hollow Swarm, void creatures of black glass with glowing orange cracks: a long deck of dark graphite steel and pale ancient stone runs toward a blazing orange-gold accretion disk that fills the sky, and titanic broken station rings, gantries and tilted monoliths drift at the event horizon. Stylized painterly-realistic rendering at the level of a top commercial sci-fi action game, not photographic: crisp hard-surface detail grouped into big readable shapes, cinematic backlight from the accretion disk, rim light on every silhouette, light shafts through drifting dust, huge depth across foreground, midground, far layers and sky. Colour script: deep space navy and graphite shadows, blazing orange-gold disk light, electric cyan and white-gold for the hero and her weapons, small violet accents in the void. No text, letters, numbers, signature, watermark, logo, frame or border.
Stylized painterly game VFX texture, hand-painted, not photographic.
Use case: stylized-concept. Asset type: production VFX texture for shader integration, not a scene illustration. The STYLE paragraph supplies world identity, palette and paint treatment only. Render ONLY the isolated effect described next, with no character, environment, UI, floor, labels or grid lines.
Canvas: 2048 by 1024 pixels. Precisely aligned atlas, 4 equal columns by 2 equal rows, zero gutters; row-major reading order. Each frame/object has exactly the same cell centre; no visible dividers. Exactly EIGHT chronological frames of a slender luminous CYAN STREAK following a flowing cape hem, isolated as a curved S-shaped ribbon, no character or cloth body. A travelling bright pulse runs steadily along the same elegant undulating vertical S path, faint blue trailing filaments and gold-white pin highlights inside cyan flowing strands. The pulse leaves one end and re-enters the other seamlessly across final-first frames. Consistent silhouette and position, edge flow changes gently 10–20 percent each frame. Tiny near-white highlights under 12 percent effect radius, saturated cyan body, cobalt fading perimeter. One whole ribbon centred in each square cell with 48px black padding.
Background: uniform absolute pure #000000 black; additive blending. Paint the coloured glow into the effect only, leaving the empty margins mathematically black.
Premium commercial action-game texture detail, crisp at native size and readable at game size. No text, numerals, symbols resembling readable language, logos or watermark.
```
