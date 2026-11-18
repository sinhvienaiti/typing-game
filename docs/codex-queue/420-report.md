# Phiếu 420 — mười flipbook bùng nổ 55° bản -v2

Ngày 16/11/2026. **Đã xuất đủ 10 bộ; kiểm đóng gói PASS.** Giữ nguyên bản cũ và nguồn. Không tạo ảnh/video AI mới.

## Tệp đã làm

Gốc: `games/immortality-cultivation/art-src/lab/vfx/`. Mỗi hàng dưới tương ứng bốn tệp mới `<hệ>/<tên>-v2.{atlas.png,json,uastc.ktx2,prompt.txt}`: tổng cộng **40 tệp**, 11.30 MiB. Hệ là phần đầu tên: dark, water, poison, blood, wood, thunder hoặc star. `.prompt.txt` ghi đường dẫn/SHA-256 nguồn, chỉ số khung, crop, điểm chạm/pivot, màu/alpha, tail fade, nén và nguyên văn prompt Firefly của đúng take.

| Bộ mới | Nguồn trong `<hệ>/firefly-raw/` | Khung nguồn / phát | Lề PNG trái / phải / trên / dưới | Lề KTX2 giải mã | Tối thiểu cả hai |
| --- | --- | --- | --- | --- | --- | --- |
| `dark-ring-burst-v2` | `dark-ring-burst.v3-try2.mp4` | 32 khung: 0–62, bước 2; 12 fps | 53 / 52 / 102 / 99 px | 53 / 52 / 102 / 99 px | **16.25%** |
| `water-ring-burst-v2` | `water-ring-burst.v3-try1.mp4` | 28 khung: 0–27, bước 1; 24 fps | 68 / 60 / 95 / 105 px | 68 / 60 / 95 / 105 px | **18.75%** |
| `poison-big-burst-v2` | `poison-big-burst.v3-try2.mp4` | 32 khung: 0–62, bước 2; 12 fps | 60 / 57 / 47 / 62 px | 60 / 57 / 47 / 62 px | **18.36%** |
| `poison-ring-burst-v2` | `poison-ring-burst.v3-try1.mp4` | 32 khung: 0–62, bước 2; 12 fps | 53 / 52 / 105 / 74 px | 53 / 52 / 105 / 74 px | **16.25%** |
| `blood-big-burst-v2` | `blood-big-burst.v3-try2.mp4` | 32 khung: 0–62, bước 2; 12 fps | 58 / 57 / 46 / 64 px | 58 / 57 / 46 / 64 px | **17.97%** |
| `wood-big-burst-v2` | `wood-big-burst.v3-try2.mp4` | 32 khung: 0–31, bước 1; 24 fps | 47 / 53 / 49 / 70 px | 47 / 53 / 49 / 70 px | **18.36%** |
| `dark-big-burst-white-v2` | `dark-big-burst-white.v3-try2.mp4` | 32 khung: 0–31, bước 1; 24 fps | 42 / 44 / 41 / 45 px | 42 / 44 / 41 / 44 px | **16.02%** |
| `dark-ground-impact-white-v2` | `dark-ground-impact-white.v3-try1.mp4` | 32 khung: 0–62, bước 2; 12 fps | 48 / 50 / 53 / 68 px | 48 / 49 / 54 / 69 px | **18.75%** |
| `thunder-impact-v2` | `thunder-impact.v3-try1.mp4` | 32 khung: 0–31, bước 1; 24 fps | 48 / 48 / 55 / 48 px | 48 / 48 / 55 / 48 px | **18.75%** |
| `star-ring-burst-v2` | `star-ring-burst.v3-try1.mp4` | 32 khung: 0–62, bước 2; 12 fps | 50 / 51 / 97 / 82 px | 50 / 49 / 97 / 82 px | **15.31%** |

Đã thêm mục **Mười clip bùng nổ 55° — phiếu 420** vào [`VFX_LIBRARY.md`](../games/tu-tien/skills/VFX_LIBRARY.md). Không sửa những mục sẵn có.

## Chọn đoạn và đóng gói

- Lưới **8×4**; ô **320×320** cho bốn ring-burst, **256×256** cho sáu bộ còn lại; giữ nguyên kích thước atlas cũ.
- **Thủy có 28 khung**, bốn ô cuối rỗng. Phiếu cho “tối đa 32 khung”; nguồn có hạt đầu tiên chạm mép ở khung 28, 1,167 s, RGB mép 24. Lấy 0–27 ở 24 fps (1,167 s), không lặp/nội suy khung để đủ 32 và không làm mờ phần bị cắt.
- Chín bộ còn lại có đúng **32 khung**. Mộc, khói trắng lớn và Sét lấy 0–31, 24 fps (1,333 s). Sáu bộ còn lại lấy 0–62, bước 2, 12 fps (2,667 s). Toàn bộ chọn trong ba giây đầu, trước phần hỏng.
- Script đo mép **video gốc 1080×1080 trước crop/fade**: tất cả khung được chọn có RGB mép ≤12. Số đo từng khung của cả video nằm trong `source-audit.json`. Đã xem 12 mốc/nguồn và ảnh so sánh cuối của cả 10 bộ.
- Giữ 55°, không xoay, không ép tròn: `rotate=0`, `flipX=false`, `squashY=1`, một crop vuông cố định và thu nhỏ đồng nhất suốt đoạn. Chỉ thêm nền đen ngoài khung; không vignette/che tia. Pivot neo vào tâm chân/vành của khung đầu, không vào tâm toàn bộ khói. Các tọa độ là lựa chọn từ ảnh nguồn, chưa kiểm trong host.
- Tám bộ giữ **RGB additive**. Hai bộ `dark-big-burst-white`, `dark-ground-impact-white` giữ **normal RGBA, premultiplied=false**, nhưng nguồn lần này là khói bạc trắng nền đen. Tách đen với `alpha=maxRGB` và `F=C/alpha` sau crush: khi đặt lại trên đen, `alpha×F=C`. Không dùng phép tách nền trắng cũ, không đảo khói trắng thành khói tối. Ảnh so sánh thể hiện rõ thay đổi này.
- Dùng các hàm có sẵn của `tools/vfx-flipbook`: `decode_crop`, `crush_black`, `neutral_fade`, `write_atlas`, bộ nén KTX2 WASM. Crush `t0=0.02`, `greyCut=0.15` cho additive / 0 cho khói trắng; giữ tông. Tail fade smoothstep **10 khung cuối**, kết thúc hoàn toàn đen/alpha 0.
- JSON giữ đúng toàn bộ khoá cấp gốc và các khoá `source`, `trim` của bản cũ tương ứng. `version=v2`; `id`, `image` có `-v2`; nguồn trỏ đúng take `.v3-try1/2.mp4`; fps, số khung, crop và pivot phản ánh bộ mới.
- KTX2: **UASTC mức 2, sRGB, Zstd, Y-flip, 12 mức mip**. Giải mã lại bằng `inspect.mjs`, trả Y về hướng PNG rồi đo.

## Kết quả kiểm độc lập

**632 lượt khung PASS = 316 PNG + 316 KTX2 mức 0.** Quét mọi pixel ở mọi khung: pixel có hình khi `maxRGB>12` (additive) hoặc `alpha>12` (normal). Bốn dải lề rộng `ceil(10% × kích thước ô)` có tín hiệu tối đa **0** cho cả 10 bộ, cả hai định dạng. Lề thấp nhất sau nén **15,31%**, cao hơn mức 10% yêu cầu. Bảng trên in số cho từng bộ; `final-validation.json` và `metrics.json` giữ số từng khung.

Kiểm thêm: đúng danh sách 10 tên, schema cùng khoá, mode/channels/ô như atlas cũ, tối đa 32 khung, chỉ số khung duy nhất, fps khớp bước nguồn, bốn ô dư Thủy rỗng, khung cuối tắt, crop không bóp tỉ lệ, pivot khớp phép biến đổi, UASTC/sRGB/Zstd/mipmap giải mã được. Đã xác nhận SHA-256 **40 tệp gốc (10× PNG/JSON/KTX2/video) không thay đổi**; checksum mọi tệp mới cũng khớp.

Chạy lại phép kiểm, không ghi vào asset:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game
tools/vfx-flipbook/.venv/bin/python -B /private/tmp/420-burst-v2b/verify.py
```

## Ảnh kiểm và giới hạn sandbox

Đích yêu cầu `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/burst-v2b/` nằm ngoài `writable_roots`. Đã dùng ngoại lệ của phiếu: **`/private/tmp/420-burst-v2b/`**, có `ABOUT.md`.

Có **10 ảnh `<clip>-before-after.jpg`**, mỗi ảnh tám cặp khung: trái bản cũ cùng tên, phải `-v2`; chọn cùng phần trăm thời lượng. Khung xanh đánh dấu lề 10%, dấu cam là pivot mới, nền caro dùng cho RGBA. Có 10 ảnh `*-source-qa.jpg` (12 mốc nguồn), `pivot-qa.jpg` và bốn ảnh tổng hợp `comparison-group-*.jpg`. Đã mở xem đủ 10 nguồn và đủ 10 bản so sánh; không lưu khung thô. Script `audit.py`, `pivots.py`, `package.py`, `verify.py` và số đo nằm cùng thư mục. `package.py` từ chối ghi đè file đích khác checksum.

Lệnh cho coordinator chuyển bằng chứng ra ngoài sandbox, giữ file đích đã có rồi cập nhật chỉ mục:

```sh
mkdir -p /Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/burst-v2b
cp -Rn /private/tmp/420-burst-v2b/. /Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/burst-v2b/
cd /Volumes/SS990TPRO/htdocs/typing-game
node scripts/review-index.mjs
```

Chưa ghi thư mục review hoặc chạy chỉ mục tại đó vì ngoài quyền ghi. Không bỏ clip nào. Chỉ bỏ phần cuối nguồn tràn mép, bốn khung Thủy để giữ nội dung còn nguyên, và các bước nối host/nghiệm thu hình tổng hợp vì ngoài phiếu. Không chấm nguồn đơn lẻ theo thang 8,5.

## Owner/coordinator cần xem

1. Đoạn Thủy 1,167 s và ba bộ 1,333 s: khi nối phải dùng đúng `frames`/`fps` trong JSON, không mặc định 32 khung/12 fps.
2. Hai clip `white` mới là khói trắng, thay cho khói tối của nguồn cũ; ảnh trên nền caro cho thấy khác biệt.
3. Góc bầu dục, kích thước và điểm chạm đất khi nối lab/host: pivot đặt theo nguồn đầu, chưa được kiểm trong cảnh thật. Phiếu này chỉ hoàn tất đóng gói, không tuyên bố đạt hiệu ứng tổng hợp 8,5.

Phạm vi ghi: 40 tệp asset mới trong các thư mục hệ được phép, bổ sung `VFX_LIBRARY.md`, báo cáo này và bằng chứng `/private/tmp`. Không sửa code, không chạy build/test game, không stage media, không đổi nhánh, không commit/push/reset/clean/stash; không gọi subagent hoặc dịch vụ AI.
