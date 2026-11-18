# Phiếu 174 · Wordwoven · Bộ texture chữ dệt

Ngày làm: 29/10/2026, Mac mini M4. Công cụ sinh: `image_gen` tích hợp; không dùng API hay mạng ngoài. Có **12 bản chọn**, **14 lượt sinh**, mọi `.tryN.png` và prompt được giữ. Không ảnh nào dùng quá hai lượt.

**Trạng thái: đã giao media để Claude chấm lại; chưa tuyên bố hoàn tất cổng nhận.** Khổ, nền/alpha, nối mép và IoU đạt các phép đo dưới đây. Riêng mục lõi trắng có hai cách diễn giải cho kết quả khác nhau: lõi liền ở tâm đạt, nhưng gom mọi phản quang sáng ở mép vào bán kính trắng thì không đạt. Theo ART_ACCEPTANCE §5, giữ tranh và dừng việc ép sáng/tô xóa để Claude quyết. M và Q là tự chấm trên bản hậu kỳ, không phải phê duyệt của chủ dự án.

## Bộ giao và tờ xem

- Ảnh, alpha, prompt, JSON: [word-v2/](../../games/typing-defense/art-src/vfx/word-v2/). Mỗi bản chọn có `<tên>.png`, `<tên>.alpha.png`, `<tên>.prompt.txt`, `<tên>.json`.
- Tờ bắt buộc: [174-sheet.jpg](../../games/typing-defense/art-src/_review/174-sheet.jpg), **4352×15432 px**, atlas ở cỡ 1:1; dưới mỗi atlas là dải ô ở cỡ dùng đề xuất và hai ảnh ghép trận.
- Xem nhanh ở cỡ dùng: [overview-game-size.jpg](../../games/typing-defense/art-src/_review/174/overview-game-size.jpg). Mỗi tấm có tờ riêng `<tên>-review.jpg` và tờ `<tên>-before-after.jpg` đặt **bản sinh | bản hậu kỳ** cùng cỡ ô xem. Cột bản sinh chứa toàn ảnh gốc, có lề khi khác tỉ lệ; file sinh nguyên vẹn vẫn nằm cạnh prompt.
- Số thô: [metrics-final.json](../../games/typing-defense/art-src/_review/174/metrics-final.json), [backdrops.json](../../games/typing-defense/art-src/_review/174/backdrops.json); có GIF xem nhịp cho ba flipbook. GIF chỉ là xem trước, không chứng minh timing của game.
- `seal-stamp` có khổ mâu thuẫn trong phiếu: giao atlas **2048×512, 4 ô 512²**, đồng thời thêm bốn bản rời **1024²**. Dùng **`seal-stamp-variant-1-clean.png` đến `seal-stamp-variant-4-clean.png`** với alpha/prompt/JSON cùng tên. Bốn file `seal-stamp-variant-N.png` không có `-clean` là bản phóng trung gian **không chọn**: alpha loang sau phóng; giữ theo luật cấm ghi đè/xóa. Không lấy chúng để gắn game.
- Bốn dấu rời sạch: [tờ 1:1](../../games/typing-defense/art-src/_review/174/seal-variants-clean-native.jpg), [số kiểm](../../games/typing-defense/art-src/_review/174/seal-variants-clean-metrics.json). Cả bốn: 1024², pixel alpha trung gian ngoài mép 3 px = **0**, magenta nhìn thấy = **0%**. Có bốn tờ `seal-stamp-variant-N-clean-before-after.jpg`.

## Chuẩn, vai trò và cảnh kiểm

Theo `docs/games/VFX_STANDARD.md` §3, §5.6; mức M theo `ART_DIRECTION_2026-10-28.md` §1.3, Q theo `ART_ACCEPTANCE.md` §2.2 và hậu kỳ theo §5. Prompt bắt đầu đúng nguyên văn STYLE Wordwoven §2.2, thêm đúng câu `Stylized painterly game VFX texture, hand-painted, not photographic.` Khối sau chỉ định texture cô lập; không sinh cảnh núi vào atlas. Tham chiếu mức hoàn thiện: `games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp`. Đây là ảnh cảnh, nên dùng để so độ hoàn thiện vật liệu/ánh sáng, không bắt texture cô lập phải có núi và trời.

Đã đọc `games/.wt-td-1c/tmp/lane-l3/judge-c10-r3/verdict.md`: ưu tiên thân ngọc bão hòa, lõi nhỏ và hổ phách cho combo. Texture chỉ cung cấp vật liệu cho lớp VFX; bộ ảnh riêng này không thay thế đủ năm pha trong runtime.

| Texture | Lớp và hành động |
|---|---|
| `jade-flash` | Word Shot T1–T2 · R · lóe tại nguồn |
| `ink-trail` | Word Shot T1–T2 · T · ribbon và lớp tối |
| `thread-glow` | Combo · T/F · dây nối |
| `paper-scraps` | Gõ xong từ · R/F · mảnh giấy |
| `ink-splash` | Phím sai T0 · R · mực son |
| `jade-burst` | Word Shot T1–T2 · I · lóe, vòng, mảnh |
| `gold-dust` | Combo/Word Shot · F · bụi vàng |
| `seal-stamp` | Phím đúng T0 · R · ấn trên thẻ |
| `ring-ripple` | Word Shot/Combo · I · vòng trên đất |
| `scorch-jade` | Word Shot · F · decal tối |
| `glyph-spark` | Phím đúng T0 · R · tia tại chữ/nguồn |
| `tier-aura` | Combo · I/F · vầng bậc |

Cảnh ghép lấy từ hai tờ chụp trận **C10 r3 1920×1080 có sẵn** trong worktree, không chạy trình duyệt: `td-1c-words-key-light-1920x1080.jpg` và `td-1c-words-key-dark-1920x1080.jpg`. Cắt vùng `[4,336,480,620]`, đổi cỡ 640×360, không chỉnh sáng/màu ảnh trận. Nền sáng là đất; nền tối là bóng nhà/cỏ, **không giả làm cảnh đêm**. Luma trung bình vùng đặt tâm trước ghép: **0,7482** và **0,2965**. Chỉ số là luma sRGB có trọng số Rec.709, không tuyến tính hóa. MD5 ảnh nguồn có trong `backdrops.json`.

Cỡ trong tờ là đề xuất bàn giao media, chưa phải cỡ đã đo trong runtime. Hai dải dùng trọn texture; atlas dùng ô đầu cho ảnh ghép và toàn bộ ô cho dải khung. Ghép cộng sáng RGB gain 1, normal dùng alpha thẳng. Trên đất sáng, cộng sáng vẫn có thể cháy màu; làn VFX phải phối lớp tối và gain theo chuẩn, rồi chụp lại nhịp 1280/1920. Không coi ảnh ghép tĩnh là bằng chứng game đã đạt.

## Kiểm 1–2 · Khổ, alpha, nền và chuyển động

Đo trên **file bản chọn ở thư mục giao**, không lấy số từ bản sinh hay ảnh JPEG. Normal: alpha trung gian phải nằm trong dải 3 px quanh mặt nạ alpha ≥128; phép nở/co 7×7 dùng khoảng cách L∞. Pixel mang nền đếm khi R>200, B>180, G<100 và alpha>0; đã kiểm thêm viền tím bằng mắt ở cỡ lớn. RGB tại alpha=0 đều bằng 0. Additive: đo nền trống ở dải an toàn ngoài 3 px mỗi ô; dải nối ngang chỉ xét mép trên/dưới vì trái/phải có vật chạy xuyên. `.alpha.png` additive là mask hỗ trợ kiểm, **không nhân thêm nó khi cộng RGB**.

| Tên | Khổ giao | Ô | Blend | Alpha trung gian ngoài 3 px | Pixel nền còn (%) / đen mép lớn nhất |
|---|---:|---:|---|---:|---:|
| `jade-flash` | 1024×512 | 4×2 | additive | mask nhị phân | 0/255 |
| `ink-trail` | 2048×256 | 1×1 | normal | 0 | 0.000000% |
| `thread-glow` | 2048×128 | 1×1 | additive | mask nhị phân | 0/255 |
| `paper-scraps` | 2048×512 | 8×2 | normal | 0 | 0.000000% |
| `ink-splash` | 2048×512 | 4×1 | normal | 0 | 0.000000% |
| `jade-burst` | 4096×2048 | 8×4 | additive | mask nhị phân | 0/255 |
| `gold-dust` | 2048×512 | 8×2 | additive | mask nhị phân | 0/255 |
| `seal-stamp` | 2048×512 | 4×1 | normal | 0 | 0.000000% |
| `ring-ripple` | 1024×1024 | 1×1 | additive | mask nhị phân | 0/255 |
| `scorch-jade` | 1024×1024 | 1×1 | normal | 0 | 0.000000% |
| `glyph-spark` | 1024×256 | 4×1 | additive | mask nhị phân | 0/255 |
| `tier-aura` | 2048×1024 | 4×2 | additive | mask nhị phân | 0/255 |

Cả 12 khổ đúng. Cả năm tấm normal: **0 pixel** alpha trung gian ngoài dải; **0%** nền magenta theo phép đếm. Bảy tấm additive: mép nền trống đen thật **0/255**, dưới trần 2/255. Không làm sạch bằng cách cắt mất phần vẽ.

Mặt nạ flipbook = max(R,G,B)>20/255; thứ tự hàng trước, rồi cột kế. IoU đo từng cặp ngay trên ô giao, không dịch tâm để làm đẹp số.

| Flipbook | FPS | Loop | IoU nhỏ nhất | IoU lớn nhất | Cặp cuối→đầu | Khung đầu/đỉnh luma |
|---|---:|---|---:|---:|---:|---:|
| `jade-flash` | 60 | false | 0.7608 | 0.8157 | không áp dụng | 1.0000 |
| `jade-burst` | 60 | false | 0.6072 | 0.8108 | không áp dụng | 1.0000 |
| `tier-aura` | 8 | true | 0.8001 | 0.8760 | 0.8665 | 0.8392 |

Toàn bộ cặp trong **0,55–0,95**. Hai dải `ink-trail`, `thread-glow`: chênh lớn nhất và trung bình RGBA giữa cột đầu/cuối đều **0/255**. Chỉ số này chứng minh biên khớp pixel; chưa chứng minh cuộn UV trong shader. Dải khung có trong tờ tổng và tờ riêng.

## Kiểm 3 · Lõi trắng và ramp màu — chỗ cần Claude quyết

Luma = 0,2126R + 0,7152G + 0,0722B, R/G/B sRGB chuẩn hóa. Khung sáng nhất là tổng luma lớn nhất. Bán kính vật là r95 của mặt nạ RGB>20/255 tính từ tâm ô. Đo ba số, không giấu phản quang ở ngoài:

1. **Lõi liền:** thành phần luma>0,92 liên thông 8 hướng, có hạt giống sáng nhất trong 25% bán kính tâm; lấy r95 lõi / r95 vật. Vòng rỗng không có lõi thì bằng 0.
2. **Bán kính tương đương diện tích:** căn bậc hai (tổng pixel luma>0,92 / tổng pixel vật), gồm cả phản quang ngoài mép.
3. **Toàn phản quang:** r95 của mọi pixel luma>0,92 / r95 vật; chấm trắng trên mảnh/vành cũng bị tính vào số này.

| Texture additive | Khung sáng nhất (từ 0) | Lõi liền / R | Trắng theo diện tích / R | Mọi phản quang r95 / R |
|---|---:|---:|---:|---:|
| `jade-flash` | 0 | 0.2812 | 0.2378 | **0.8364** |
| `thread-glow` | 0 | 0.0919 | 0.1124 | **0.9549** |
| `jade-burst` | 0 | 0.1868 | 0.1955 | **0.7455** |
| `gold-dust` | 10 | 0.1111 | 0.2160 | **1.0773** |
| `ring-ripple` | 0 | 0.0000 | 0.1764 | **0.9995** |
| `glyph-spark` | 3 | 0.2755 | 0.1626 | **0.7815** |
| `tier-aura` | 4 | 0.0000 | 0.1300 | **1.0029** |

**Lõi liền và bán kính tương đương diện tích đều ≤0,30**, nhưng cột toàn phản quang đều vượt 0,30. Giá trị lớn hơn 1 ở hạt/vành có thể xảy ra vì r95 vật bỏ 5% điểm xa nhất, trong khi một chấm phản quang nằm trong phần đó. Không đổi mẫu đo để giấu hiện tượng này. C10 dùng cả r95 của vùng trắng nên **không thể tự kết luận mục 3 đã qua theo cách tính rộng đó**. Chỉ làm chỉnh sáng toàn ảnh −2% cho `jade-flash`, `glyph-spark`, trong hạn ±10%; không dập phản quang, xóa cánh hay tô màu phủ. Dừng ở đây để Claude chọn định nghĩa lõi hoặc hướng sinh khác nếu bắt mọi đốm ngoài rìa cũng nằm trong 30%.

Các tấm normal là giấy/mực/decal không phát sáng; không áp luật lõi plasma cho mặt giấy kem. Ramp sáng/tối vẫn đo cho đủ 12. Ba dải dưới đây đếm trên phần nhìn thấy: tối <0,18; thân 0,18–<0,60; sáng ≥0,60. Đây là số bổ trợ; không đồng nhất ba dải sáng/tối với ba sắc bắt buộc. Nhìn ở tờ gốc xác nhận ngọc sẫm → ngọc sáng → hổ phách ở lớp sáng; mực son sẫm → thân son → mép ấm ở dấu/vệt; giấy có cháy mép → thân kem → gấp sáng.

| Tên | Pixel dải tối | Pixel thân | Pixel sáng |
|---|---:|---:|---:|
| `jade-flash` | 36814 | 96250 | 51156 |
| `ink-trail` | 72702 | 187732 | 48028 |
| `thread-glow` | 28142 | 72135 | 20708 |
| `paper-scraps` | 17615 | 120607 | 183237 |
| `ink-splash` | 76283 | 59887 | 3371 |
| `jade-burst` | 1037008 | 1280955 | 511316 |
| `gold-dust` | 13089 | 29301 | 20167 |
| `seal-stamp` | 100891 | 94792 | 1873 |
| `ring-ripple` | 76723 | 135744 | 77811 |
| `scorch-jade` | 172135 | 151799 | 12383 |
| `glyph-spark` | 9992 | 11753 | 6274 |
| `tier-aura` | 128931 | 366433 | 123872 |

## KA5 · Tự chấm bản hậu kỳ

M so mức phát hành thương mại ở độ hoàn thiện chất liệu, chiều sâu trong nét và độ đọc ở cỡ dùng; Q theo năm tiêu chí 0–2 của ART_ACCEPTANCE, có trừ cho hạn chế khung/chuyển bước. Điểm dưới đây không xóa vấn đề định nghĩa lõi đã nêu; **chờ Claude chấm lại**.

| Bản chọn | Lượt | M | Q | Ghi chú trên bản giao | Tờ đối chiếu |
|---|---:|---:|---:|---|---|
| [`jade-flash`](../../games/typing-defense/art-src/vfx/word-v2/jade-flash.png) | 2 | 8.5 | 8.5 | Cánh ngọc có vân sợi, tâm nhỏ; một vài đầu sợi lượt sinh sát biên. Chọn lượt 2 vì đuôi không co đột ngột. | [Sinh/hậu kỳ](../../games/typing-defense/art-src/_review/174/jade-flash-before-after.jpg) · [1:1/cỡ dùng](../../games/typing-defense/art-src/_review/174/jade-flash-review.jpg) |
| [`ink-trail`](../../games/typing-defense/art-src/vfx/word-v2/ink-trail.png) | 1 | 8 | 8.5 | Mực tối và chỉ ngọc đan rõ, có giấy kem; nhịp lặp nhìn ra ở khổ lớn, cần chạy UV khi gắn ribbon. | [Sinh/hậu kỳ](../../games/typing-defense/art-src/_review/174/ink-trail-before-after.jpg) · [1:1/cỡ dùng](../../games/typing-defense/art-src/_review/174/ink-trail-review.jpg) |
| [`thread-glow`](../../games/typing-defense/art-src/vfx/word-v2/thread-glow.png) | 1 | 8.5 | 8.5 | Nhiều sợi xoắn, độ sáng có nhịp, còn thân xanh; không dùng như ống trắng đặc. | [Sinh/hậu kỳ](../../games/typing-defense/art-src/_review/174/thread-glow-before-after.jpg) · [1:1/cỡ dùng](../../games/typing-defense/art-src/_review/174/thread-glow-review.jpg) |
| [`paper-scraps`](../../games/typing-defense/art-src/vfx/word-v2/paper-scraps.png) | 1 | 8.5 | 8.5 | Đủ 16 mảnh giấy có gấp, lỗ, xơ và cháy mép; nét mực trừu tượng, không có chữ đọc được. | [Sinh/hậu kỳ](../../games/typing-defense/art-src/_review/174/paper-scraps-before-after.jpg) · [1:1/cỡ dùng](../../games/typing-defense/art-src/_review/174/paper-scraps-review.jpg) |
| [`ink-splash`](../../games/typing-defense/art-src/vfx/word-v2/ink-splash.png) | 1 | 8 | 8.5 | Bốn hướng bắn mực son khác nhau, tâm có độ sâu; bản 64 px còn nhận ra dáng. | [Sinh/hậu kỳ](../../games/typing-defense/art-src/_review/174/ink-splash-before-after.jpg) · [1:1/cỡ dùng](../../games/typing-defense/art-src/_review/174/ink-splash-review.jpg) |
| [`jade-burst`](../../games/typing-defense/art-src/vfx/word-v2/jade-burst.png) | 2 | 8 | 8 | Đủ 32 khung, lóe → vòng → mảnh → sợi/bụi. Các khung cuối còn nhiều sợi ngọc, bụi vàng chưa hoàn toàn chiếm ưu thế. Bản giao là ảnh phóng từ lượt sinh, không phải 4K chi tiết nguyên sinh. | [Sinh/hậu kỳ](../../games/typing-defense/art-src/_review/174/jade-burst-before-after.jpg) · [1:1/cỡ dùng](../../games/typing-defense/art-src/_review/174/jade-burst-review.jpg) |
| [`gold-dust`](../../games/typing-defense/art-src/vfx/word-v2/gold-dust.png) | 1 | 8 | 8.5 | Đủ 16 hạt/vảy vàng có vân lá và hướng khác nhau; lúc gắn cần trộn cỡ nhỏ, không dùng cả atlas như một sprite. | [Sinh/hậu kỳ](../../games/typing-defense/art-src/_review/174/gold-dust-before-after.jpg) · [1:1/cỡ dùng](../../games/typing-defense/art-src/_review/174/gold-dust-review.jpg) |
| [`seal-stamp`](../../games/typing-defense/art-src/vfx/word-v2/seal-stamp.png) | 1 | 8.5 | 8.5 | Bốn hoa văn ấn son không chữ: vuông, tròn, nút dệt chéo, bát giác. Màu có vân mực, lòng lỗ alpha. | [Sinh/hậu kỳ](../../games/typing-defense/art-src/_review/174/seal-stamp-before-after.jpg) · [1:1/cỡ dùng](../../games/typing-defense/art-src/_review/174/seal-stamp-review.jpg) |
| [`ring-ripple`](../../games/typing-defense/art-src/vfx/word-v2/ring-ripple.png) | 1 | 8 | 8.5 | Vòng rỗng, mép lượn và lớp sợi có chiều sâu; tránh tăng gain làm thành vòng trắng trên đất sáng. | [Sinh/hậu kỳ](../../games/typing-defense/art-src/_review/174/ring-ripple-before-after.jpg) · [1:1/cỡ dùng](../../games/typing-defense/art-src/_review/174/ring-ripple-review.jpg) |
| [`scorch-jade`](../../games/typing-defense/art-src/vfx/word-v2/scorch-jade.png) | 1 | 8 | 8 | Mực tối, vết xém và mảnh ngọc đọc rõ; dư âm hơi giống vết va đập có mảnh, mạnh hơn một vết cháy nhẹ. | [Sinh/hậu kỳ](../../games/typing-defense/art-src/_review/174/scorch-jade-before-after.jpg) · [1:1/cỡ dùng](../../games/typing-defense/art-src/_review/174/scorch-jade-review.jpg) |
| [`glyph-spark`](../../games/typing-defense/art-src/vfx/word-v2/glyph-spark.png) | 1 | 8.5 | 8.5 | Bốn hướng cánh vàng/ngọc, không vẽ chữ; cỡ nhỏ vẫn đọc ra một nhịp lóe. | [Sinh/hậu kỳ](../../games/typing-defense/art-src/_review/174/glyph-spark-before-after.jpg) · [1:1/cỡ dùng](../../games/typing-defense/art-src/_review/174/glyph-spark-review.jpg) |
| [`tier-aura`](../../games/typing-defense/art-src/vfx/word-v2/tier-aura.png) | 1 | 8.5 | 8.5 | Vòng rỗng đổi ngọc sang hổ phách rồi về ngọc; khung cuối nối đầu có chuyển động. Cần nội suy khi gắn để tránh cảm giác lật hình ở 8 fps. | [Sinh/hậu kỳ](../../games/typing-defense/art-src/_review/174/tier-aura-before-after.jpg) · [1:1/cỡ dùng](../../games/typing-defense/art-src/_review/174/tier-aura-review.jpg) |

## Hậu kỳ có lưu vết

- Nguồn sinh được chép nguyên vẹn từ nơi lưu mặc định của công cụ sang `.tryN.png`, prompt đúng nguyên văn cạnh file. Không dựa vào ảnh còn nằm ngoài repo để bàn giao.
- Tách nền magenta; gỡ màu key ở mép bằng giải trộn nền và màu lân cận, rồi khử phần chroma magenta dư. Giữ alpha/hình dạng chi tiết; không vẽ đè thân ngọc hay mực. Pixel nền hoàn toàn có RGB=0.
- Atlas đổi cỡ theo từng ô, giữ tỉ lệ hình, thêm 3,5% lề. Riêng giấy chia biên ô ở khe trống gần lưới sinh để không cắt lạc mép mảnh vào ô kế; không bỏ phần ảnh nguồn. Flipbook giữ cùng tâm và cùng quy tắc tỉ lệ, không phóng riêng từng khung theo mask.
- Dải vệt cắt phần nền trên/dưới, lặp lại texture nguồn để đủ tỉ lệ dài rồi đổi cỡ đồng đều. Giữ nguyên trọn lần lặp đầu. Trộn nối ở dải 32 px nguồn/24 px bản giao, sửa alpha tại cột nối; không san phẳng chi tiết trong thân.
- Hai ảnh lóe giảm sáng toàn ảnh đúng 2%; những ảnh khác không áp gamma hay chỉnh sáng toàn ảnh. Không dùng threshold để xóa phần vẽ. Bốn dấu rời phóng lên 1024² rồi khóa lại dải alpha 3 px và khử key; bản phóng chưa sạch vẫn được giữ.
- Nhật ký: [postprocess-log.json](../../games/typing-defense/art-src/_review/174/postprocess-log.json), [refine-log.json](../../games/typing-defense/art-src/_review/174/refine-log.json), [refine-v3-log.json](../../games/typing-defense/art-src/_review/174/refine-v3-log.json), [refine-v4-log.json](../../games/typing-defense/art-src/_review/174/refine-v4-log.json). Các thư mục `draft-v1`…`draft-v4` chỉ là bản trung gian có lưu vết, **không chọn để tích hợp**. Script và số trung gian được giữ trong thư mục review; không phải mã game.

Công cụ sinh không trả đúng khổ yêu cầu. Nguồn `jade-burst` là **1774×887** (ô khoảng 222²), giao phóng lên 4096×2048/ô512²; `tier-aura` cùng nguồn 1774×887, giao 2048×1024. Bốn dấu rời 1024² cũng là phóng từ ô512². Không gọi đây là ảnh nguyên sinh 4K/1K chi tiết. Claude cần mở cỡ gốc để đánh giá độ chi tiết trước khi nhận.

## Lượt sinh, prompt và lựa chọn

Không có lượt 3. `jade-flash.try1` bỏ chọn vì IoU hai cặp cuối ở mặt nạ 20/255 khoảng 0,499 và 0,411. `jade-burst.try1` bỏ chọn vì khung đầu chỉ khoảng 0,493 đỉnh và nhiều mảnh sát biên. Lượt 2 thay đúng các yêu cầu này; không ghi đè lượt 1. Các tấm còn lại dùng lượt 1. Dưới đây là **toàn văn prompt đã gửi**, gồm cả STYLE nguyên văn; file cạnh ảnh là nguồn kiểm độc lập.

### jade-flash

**Lượt 1 · giữ, không chọn.** [Ảnh](../../games/typing-defense/art-src/vfx/word-v2/jade-flash.try1.png) · [Prompt gốc](../../games/typing-defense/art-src/vfx/word-v2/jade-flash.try1.prompt.txt)

```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.

Deliver ONLY a VFX texture atlas, not a landscape; the STYLE block defines the art lineage only. Stylized painterly game VFX texture, hand-painted, not photographic. Exact output canvas 1024x512 pixels. A perfectly regular 4 columns by 2 rows atlas of eight consecutive animation frames, each cell 256x256, row-major chronological order, no gutters, no visible grid. Word Shot release jade-flash: a centered compact hand-painted jade muzzle starburst, translucent saturated jade-green petal flames twisting like woven silk, amber gold-leaf rim and jade-white seed only 6 percent of effect radius. Deep emerald body, bright jade mids, gold rim, granular brush striations and internal cavities. Pure flat #000000 background, no ambient haze outside each sprite, entire sprite contained with 20px safety margins in every cell, same exact center in every cell. Frame one immediately fully bright; subsequent frames maintain overlapping silhouette with smoothly contracting torn petals and ember disintegration. Consecutive silhouette mask IoU 0.65-0.9, first two frames near equal brightness, final frame dim jade embers still centered; non-loop. Three readable value/color bands; tiny bright core, broad saturated jade body, thin amber edges. Each frame is a real detailed painted effect, never a flat shape or smooth tube. No letters, numbers or symbols.
```

**Lượt 2 · chọn.** [Ảnh](../../games/typing-defense/art-src/vfx/word-v2/jade-flash.try2.png) · [Prompt gốc](../../games/typing-defense/art-src/vfx/word-v2/jade-flash.try2.prompt.txt)

```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.

Stylized painterly game VFX texture, hand-painted, not photographic.
VFX texture only; STYLE establishes lineage, not scenery. jade-flash revision 2. Pure flat #000000 background. A regular 4 columns by 2 rows sprite animation atlas of eight chronological centered hand-painted jade muzzle flashes; final delivery 1024x512 pixels, each frame 256 square. Tiny jade-white point center, saturated emerald and bright jade woven silk flame petals, fine amber gold-leaf frayed tips, real brush detail, dark internal crevices. Whole effect contained in every square with minimum 12 percent empty margins; fixed center and camera. Frame 1 already at peak brightness, a broad fully developed jade flower flash; frames 2 to 8 contract only gently, each next radius 96 percent previous, broad colored petals and wispy filaments remain in all eight frames, brightness decays gently to 55 percent by frame 8. IMPORTANT: final frames remain visibly substantial, never collapse to a tiny pin or disappear. Adjacent silhouette IoU 0.65 to 0.9 at max RGB greater than 20 of 255, including frames 6-7 and 7-8. Eight distinctive successive paintings, not copies. White center radius at most 6 percent of the effect, dark emerald body, luminous jade inner folds, gold edge. Non-loop. No text, no labels, no numbers, no symbols, no grid.
```

### ink-trail

**Lượt 1 · chọn.** [Ảnh](../../games/typing-defense/art-src/vfx/word-v2/ink-trail.try1.png) · [Prompt gốc](../../games/typing-defense/art-src/vfx/word-v2/ink-trail.try1.prompt.txt)

```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.

Stylized painterly game VFX texture, hand-painted, not photographic.
Production VFX asset only. The STYLE paragraph establishes the art lineage; deliver only the texture described below, with no landscape.
Exact delivery canvas 2048x256 pixels.
A horizontally seamless repeating ribbon strip, pure uniform #FF00FF magenta chroma-key background. A narrow long flowing dark ink brushstroke interwoven with saturated jade silk threads, subtle warm gold edges and cream do-paper flecks trapped among fibers. Ink has dense textured pools, dry-brush apertures, curling filaments and readable broad shapes; jade fibers weave over and under ink. Seam at left and right exactly matches at the vertical middle; central ribbon runs fully across the width and tapers softly toward its upper and lower edges with 32px clear magenta margins above/below. Multiple braided strands with a shallow sinusoidal undulation, not a straight smooth pipe. No lettering.
```

### thread-glow

**Lượt 1 · chọn.** [Ảnh](../../games/typing-defense/art-src/vfx/word-v2/thread-glow.try1.png) · [Prompt gốc](../../games/typing-defense/art-src/vfx/word-v2/thread-glow.try1.prompt.txt)

```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.

Stylized painterly game VFX texture, hand-painted, not photographic.
Production VFX asset only. STYLE defines art lineage, deliver only the texture below, no landscape.
Exact delivery canvas 2048x128 pixels.
A very slender horizontally seamless repeating luminous jade thread cord for combo links on pure flat #000000. Long fine silk strands twist lightly into a braided energy thread, saturated emerald body with luminous bright jade ridges and sparse gold-leaf flecks, tiny pale jade-white glints. Soft restrained glow. Left and right seams match perfectly at mid-height, strands continue across border. Clear black margins above and below. Rich hand-painted striations along woven fiber, a few subtle little loops, coherent cord. No white central tube. Not text.
```

### paper-scraps

**Lượt 1 · chọn.** [Ảnh](../../games/typing-defense/art-src/vfx/word-v2/paper-scraps.try1.png) · [Prompt gốc](../../games/typing-defense/art-src/vfx/word-v2/paper-scraps.try1.prompt.txt)

```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.

Stylized painterly game VFX texture, hand-painted, not photographic.
Production VFX asset only. STYLE defines art lineage, deliver only the texture below, no landscape.
Exact delivery canvas 2048x512 pixels.
Exactly sixteen isolated individual do-paper scraps, a perfectly regular 8 columns by 2 rows sprite atlas. Each cell 256x256 and same visual center with generous 35px margins. Flat pure #FF00FF chroma-key magenta background. Each scrap a different torn folded or curling cream mulberry paper fragment, lightly burnt umber edges and textured visible long paper fibers. Gentle jade reflected light and sparse cinnabar abstract ink smears. Ink markings are disconnected abstract gestural strokes only, absolutely no recognizable letters, no symbols and no writing. Each cell one different complete scrap, a few holes and irregular torn contours, crisp clean cutout edges, no shadows outside the object, no grid.
```

### ink-splash

**Lượt 1 · chọn.** [Ảnh](../../games/typing-defense/art-src/vfx/word-v2/ink-splash.try1.png) · [Prompt gốc](../../games/typing-defense/art-src/vfx/word-v2/ink-splash.try1.prompt.txt)

```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.

Stylized painterly game VFX texture, hand-painted, not photographic.
Production VFX asset only. STYLE defines art lineage, deliver only the texture below, no landscape.
Exact delivery canvas 2048x512 pixels.
Four different cinnabar-red ink splashes for wrong-key feedback, exactly four columns in a single row, 512x512 each cell. Flat pure #FF00FF magenta chroma-key background. Front-on isolated energetic splats with pooled dark red lacquer centers, burnt sienna and saturated cinnabar body, thin warm vermilion ragged rims. Dry brush feathering and dark textured lobes, a few chunky satellite droplets contained in each cell with 45px empty margin. Different shapes: diagonal flick, compressed star, sideways sweep, downward fan. Each shape centered, ink has depth and pigment grain rather than smooth vector blobs. No text.
```

### jade-burst

**Lượt 1 · giữ, không chọn.** [Ảnh](../../games/typing-defense/art-src/vfx/word-v2/jade-burst.try1.png) · [Prompt gốc](../../games/typing-defense/art-src/vfx/word-v2/jade-burst.try1.prompt.txt)

```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.

Stylized painterly game VFX texture, hand-painted, not photographic.
Production VFX asset only. STYLE defines art lineage, deliver only the texture below, no landscape.
Exact delivery canvas 4096x2048 pixels.
A perfectly regular 8 columns by 4 rows flipbook atlas, 32 consecutive chronological frames, same fixed center in every cell and generous blank safety margin in each, no visible cell boundaries. Original requested delivery 4096x2048, each cell 512 square; maximize painted detail. Pure flat #000000 background. Word Shot impact jade-burst: frame one is a full bright compact jade flash with tiny jade-white seed under 8 percent radius, saturated jade petal blades, thin amber rim; opening jade shockwave, jagged jade crystal chips, evolving ring with layered woven-silk brush filaments, chips drifting radially and progressively settling into gold-leaf dust in the final row. Maintain broad overlapping central jade mist and changing ring so adjacent silhouette overlap stays 0.65-0.9. Upper row flash/ring opening; second row ring grows and chips turn; third row jade fibers fray gold specks; last row dims to fine gold dust but preserves overlapping central remnants. Non-loop, no empty frames. Small white seed only during flash, green body remains colored, warm amber edges. No symbols.
```

**Lượt 2 · chọn.** [Ảnh](../../games/typing-defense/art-src/vfx/word-v2/jade-burst.try2.png) · [Prompt gốc](../../games/typing-defense/art-src/vfx/word-v2/jade-burst.try2.prompt.txt)

```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.

Stylized painterly game VFX texture, hand-painted, not photographic.
VFX texture only, no scenery. jade-burst revision 2. Perfectly regular 8 columns by 4 rows atlas, 32 chronological hand-painted frames on pure flat #000000. Delivery 4096x2048, square frames 512x512. Fixed center. CRITICAL: effect occupies at most the central 72 percent of each square in ALL frames; generous pure black safety gutters implied by empty margins, no frames touch any neighbor or outside border, no visible grid lines. Word Shot impact: the very first frame is ALREADY a FULL-SIZE FULL-BRIGHT saturated jade flash, tiny white seed under 6 percent radius, broad jade woven flame blades and thin amber rim; frame 2 is not larger or brighter. Frames 1-4 bloom opens into a hollow jagged jade ring, frames 5-12 fine jade crystals orbit along the ring, frames 13-24 ring unravels into flowing jade silk filaments and gold-leaf powder, frames 25-32 dark jade wisps with gold motes, substantial centered overlapping remnants still present in last frame. Adjacent mask IoU 0.65-0.9 with threshold maxRGB>20/255. Rich internal paint striations, emerald recesses, luminous jade folds, gold edges, never broad white patches. No detached debris outside central 72 percent. Smooth progression; non-loop. Every sprite complete, isolated, top-down circular effect. No text, letters, numbers, symbols, borders or labels.
```

### gold-dust

**Lượt 1 · chọn.** [Ảnh](../../games/typing-defense/art-src/vfx/word-v2/gold-dust.try1.png) · [Prompt gốc](../../games/typing-defense/art-src/vfx/word-v2/gold-dust.try1.prompt.txt)

```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.

Stylized painterly game VFX texture, hand-painted, not photographic.
Production VFX asset only. STYLE defines art lineage, deliver only the texture below, no landscape.
Exact delivery canvas 2048x512 pixels.
Exactly sixteen individual hand-painted gold-leaf dust sparkle sprites in a perfectly regular 8 by 2 atlas, square cells 256x256, one isolated grain centered in each cell, black safety margins 45px minimum. Pure flat #000000 background. Each sprite different size and rotation: tiny folded gold foil flake, irregular floating leaf-gold chip, compact faceted gleam, torn foil shard. Vary from 18 to 110px apparent extent, one dominant mass each. Rich amber lowlights, warm gold body and pinprick pale cream highlights, white under 8 percent sprite radius. Finely hammered foliated metallic detail and painterly glints. This is a particle texture atlas, no scenery, no grid or border.
```

### seal-stamp

**Lượt 1 · chọn.** [Ảnh](../../games/typing-defense/art-src/vfx/word-v2/seal-stamp.try1.png) · [Prompt gốc](../../games/typing-defense/art-src/vfx/word-v2/seal-stamp.try1.prompt.txt)

```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.

Stylized painterly game VFX texture, hand-painted, not photographic.
Production VFX asset only. STYLE defines art lineage, deliver only the texture below, no landscape.
Exact delivery canvas 2048x512 pixels.
Exactly four distinct front-facing cinnabar-red seal stamp impressions, a perfectly regular four columns one row atlas, square cells 512x512. Flat pure #FF00FF magenta chroma-key background. Each centered with at least 45px clear margin, whole impression contained. Four variants: broken square cloud-scroll seal, round Dong Son sun-star seal, diamond woven-thread knot seal, octagonal jade-cloud rosette seal. Authentic uneven cinnabar pigment on rough fibrous paper but only the ink impression is painted, background magenta shows through open shapes and dry pigment holes. Rich dark red pools, red body, warm vermilion edges. Broad ornamental nonlinguistic patterns, no characters, no letters, no pictograms, no writing; no paper rectangle behind the ink. Hand-painted stamped grain and chipped edges, visually strong at small size.
```

### ring-ripple

**Lượt 1 · chọn.** [Ảnh](../../games/typing-defense/art-src/vfx/word-v2/ring-ripple.try1.png) · [Prompt gốc](../../games/typing-defense/art-src/vfx/word-v2/ring-ripple.try1.prompt.txt)

```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.

Stylized painterly game VFX texture, hand-painted, not photographic.
Production VFX asset only. STYLE defines art lineage, deliver only the texture below, no landscape.
Exact delivery canvas 1024x1024 pixels.
One isolated thin circular jade magical ground ripple, orthographic directly top down, centered at 512,512, on pure flat #000000 background. Outer diameter approximately 820px, entirely contained. Large hollow black middle, fine broken concentric wave fronts, softly feathered edges but detailed irregular hand-painted wave crests, translucent saturated jade-green ring body with emerald troughs and tiny amber gold accents. Inner texture like woven jade silk and ink flow, changing thickness organically, three readable color bands with pinprick pale jade highlights under 8 percent local band thickness. No solid glowing disc, no text, no surrounding scenery. Restrained elegant ground wave, dramatic material detail.
```

### scorch-jade

**Lượt 1 · chọn.** [Ảnh](../../games/typing-defense/art-src/vfx/word-v2/scorch-jade.try1.png) · [Prompt gốc](../../games/typing-defense/art-src/vfx/word-v2/scorch-jade.try1.prompt.txt)

```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.

Stylized painterly game VFX texture, hand-painted, not photographic.
Production VFX asset only. STYLE defines art lineage, deliver only the texture below, no landscape.
Exact delivery canvas 1024x1024 pixels.
One isolated top-down impact decal of dark jade-black ink pooling into a lightly scorched irregular mark, centered and complete with 90px magenta margin on all sides. Pure flat #FF00FF magenta chroma-key background. Painterly layered dark ink lobes with burnt umber singed perimeter, embedded tiny dull jade crystal splinters and warm gold ash specks. Dry-brush ragged porous outside, charcoal cracking within the pigment, a subtle center depression suggested by pigment value, no solid ground square. Readable broad organic mass, natural asymmetry, earth-bound aftermath rather than a crater illustration. No text, no symbols, no cast shadow outside decal.
```

### glyph-spark

**Lượt 1 · chọn.** [Ảnh](../../games/typing-defense/art-src/vfx/word-v2/glyph-spark.try1.png) · [Prompt gốc](../../games/typing-defense/art-src/vfx/word-v2/glyph-spark.try1.prompt.txt)

```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.

Stylized painterly game VFX texture, hand-painted, not photographic.
Production VFX asset only. STYLE defines art lineage, deliver only the texture below, no landscape.
Exact delivery canvas 1024x256 pixels.
Four isolated tiny letter-confirmation spark flashes, exactly 4 columns by 1 row, square 256x256 cells. Pure flat #000000 background. Same center and at least 30px clear safety margin each cell. Each a different compact bright painterly star flick: jade-white pinprick core under 8 percent radius, saturated jade inner blades and gold-leaf outer wings, emerald creases and warm amber frayed tips. Four different directional gestures: upright four-wing flare, diagonal crossed wings, horizontal fan, tight six-wing burst. Chunky readable silhouettes and real internal silk/foil brush detail at small game size, crisp luminous energy, not photographic. Absolutely no glyph, text, letters or symbols: the name is only the purpose; the image contains sparks.
```

### tier-aura

**Lượt 1 · chọn.** [Ảnh](../../games/typing-defense/art-src/vfx/word-v2/tier-aura.try1.png) · [Prompt gốc](../../games/typing-defense/art-src/vfx/word-v2/tier-aura.try1.prompt.txt)

```text
Epic high-fantasy game art for Wordwoven, a majestic realm inspired by northern Vietnam: colossal limestone karst towers rising hundreds of metres from mist and jade-green rivers like Ha Long Bay and Trang An, silver waterfalls pouring from their cliffs, rice terraces climbing the slopes like giant green-and-gold stairs, ancient moss-covered stone temples, gates and stairways carved into the rock, floating lanterns, and colossal sky beasts gliding between the peaks. Stylized painterly-realistic rendering at the level of a top commercial fantasy game, not photographic: rich detail on rock, water and foliage grouped into big readable shapes, crisp silhouettes, cinematic light with god rays through drifting cloud, deep atmospheric perspective across foreground, midground, far layers and sky. Colour script: jade and teal shadows, warm gold light, silver water and mist, limestone white, small cinnabar-red and lantern-amber accents. No text, letters, numbers, signature, watermark, logo, frame or border.

Stylized painterly game VFX texture, hand-painted, not photographic.
Production VFX asset only. STYLE defines art lineage, deliver only the texture below, no landscape.
Exact delivery canvas 2048x1024 pixels.
A perfectly regular 4 columns by 2 rows looping flipbook, eight chronological centered frames with the exact same circular aura radius and generous 45px black margin each cell; each cell 512x512. Pure flat #000000 background. Thin ornate rotating combo tier halo: intertwined jade silk brush ribbons and gold-leaf amber wavelets, hollow dark middle, a few compact sparks hugging ring, big readable scalloped arcs and visible pigment filaments. Emerald jade shadows, saturated luminous jade body with amber outer crest; jade dominates frame one, then amber gradually strengthens toward frames four and five and returns to jade by frame eight. Eight phases of one slow rotation: 0, 8, 16, 24, 32, 24, 16, 8 degrees, gentle shape evolution and breathing, so frame eight to one also smooth. Adjacent silhouette mask IoU 0.65-0.9 including wrap; central hollow preserved, no opaque disc. Tiny pale highlights only, no broad white core. No text, symbols or runes.
```

## KA1 · Chỉ thêm file

Trước khi ghi, ba đích `word-v2/`, `_review/174/` và `174-report.md` đều chưa tồn tại; danh sách file ban đầu rỗng. Đã lưu mốc trước bằng `md5 -r`. Sau khi hoàn thành báo cáo, chạy lại `md5 -r` cho **mọi file** trong hai thư mục đích, cộng tờ `_review/174-sheet.jpg` và báo cáo. Manifest sau và diff đặt ở ngoài hai thư mục được băm, dưới tiền tố `_review/174-ka1-*`, để không tự băm chính nó.

- [Manifest trước](../../games/typing-defense/art-src/_review/174-ka1-before.md5).
- [Manifest sau](../../games/typing-defense/art-src/_review/174-ka1-after.md5).
- [Diff](../../games/typing-defense/art-src/_review/174-ka1-diff.txt): chỉ có nhánh thêm, không có dòng xóa hay sửa file có sẵn.
- [Kết quả đối chiếu](../../games/typing-defense/art-src/_review/174-ka1-audit.json).

## Chỗ khác phiếu, phần bỏ qua và việc cần nhìn

1. **Chưa xác nhận xong cổng 3 theo cách đếm mọi phản quang trắng.** Đã ghi đủ cả ba phép đo; dừng ép số để giữ tranh, đúng §5. Claude quyết lại định nghĩa/phương án; chủ dự án nhìn tờ lóe/nổ trên nền đất sáng.
2. `seal-stamp`: giải mâu thuẫn khổ bằng atlas 2048×512 và bốn dấu rời 1024² sạch. Bốn bản rời không hậu tố `-clean` không được chọn, vẫn giữ nguyên vì cấm ghi đè/xóa.
3. Ảnh gốc do công cụ trả khác khổ; có đổi cỡ và thêm lề, không giả nhận độ phân giải nguyên sinh. `jade-burst` cuối còn sợi ngọc nhiều hơn bụi; đây là hạn chế tự chấm M=8/Q=8 cần Claude xem.
4. Tờ ghép là media trên ảnh trận có sẵn và cỡ dùng đề xuất. Chưa gắn shader, chưa đo draw call/frame time, chưa kiểm timing/tương phản của trận chạy, chưa có chấm độc lập. Đây là phần của Claude/làn VFX; phiếu cấm sửa mã, dev server và trình duyệt nên không thực hiện.
5. Không tạo âm thanh vì phiếu chỉ giao texture. Không sửa tài liệu khác, ART_REPLACE_LATER hay mã game do giới hạn đường dẫn. Không chạy Git, build/test game, mạng ngoài công cụ ảnh. Không chạm game khác hoặc Tu Tiên. Không có capture trình duyệt mới hay khung thô để prune; giữ mọi lượt sinh, draft và tờ kiểm theo luật cấm xóa.

**Cần chủ dự án/Claude nhìn:** `174-sheet.jpg`, các tờ `jade-flash-before-after.jpg`, `jade-burst-before-after.jpg`, phần số đo lõi trắng, và bốn dấu `-clean`. Mỗi bản chọn tự chấm M≥8/Q≥8; nhận cuối vẫn chờ Claude và chủ dự án.
