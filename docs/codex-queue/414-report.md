# Phiếu 414 — đóng gói lại lề atlas bùng nổ

Ngày 16/11/2026. Kết quả: **2 clip đóng gói lại đạt lề; 3 clip cần làm lại nguồn** theo ngoại lệ đã ghi trong phiếu. Đã kiểm đủ đúng năm clip. Không tạo lại hình bằng AI.

## Tệp đã làm

Trong `games/immortality-cultivation/art-src/lab/vfx/`:

| Thư mục | Tên gốc của bộ mới | Tệp mới |
| --- | --- | --- |
| `thunder/` | `thunder-ground-impact-m` | `.atlas.png`, `.json`, `.uastc.ktx2`, `.prompt.txt` |
| `wood/` | `wood-ring-burst-m` | `.atlas.png`, `.json`, `.uastc.ktx2`, `.prompt.txt` |

`.prompt.txt` ghi rõ đây là xử lý cơ học, đường dẫn video repo, chỉ số khung, vùng lấy ảnh và thông số đóng gói. Đã bổ sung mục **Đóng gói lại lề atlas bùng nổ — phiếu 414** trong [`VFX_LIBRARY.md`](../games/tu-tien/skills/VFX_LIBRARY.md), gồm cả hai bộ mới và ba bộ cần làm lại. Tất cả bản cũ vẫn ở nguyên vị trí.

Video nguồn của cả năm bộ còn tại `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/video/<tên clip>/take1.mp4` (1080 × 1080, 24 fps, 121 khung). Hai bộ cứu được lấy lại từ video này, dùng chính các hàm của `tools/vfx-flipbook/`; không phóng lại atlas độ phân giải thấp.

## Cách đóng gói và kiểm

Giữ đúng chỉ số 32 khung trong JSON cũ, 12 fps, lưới 8 × 4, kích thước ô/atlas, chế độ additive RGB, tail fade 10 khung và các khoá JSON. Chỉ đổi `id`, `image`, `source.crop`, `pivot`. Vùng lấy ảnh mở rộng khoảng 25%, hình thu nhỏ khoảng 20%, nền thêm vào là đen; cùng một phép biến đổi dùng cho mọi khung, không cắt hay làm mờ nội dung để đạt số đo.

- `thunder-ground-impact`: vùng lấy ảnh `[20,22,1038,1038]` → `[-110,-108,1298,1298]`; atlas **2048 × 1024**, ô **256 × 256**.
- `wood-ring-burst`: `[-22,-6,1116,1116]` → `[-162,-146,1396,1396]`; atlas **2560 × 1280**, ô **320 × 320**.

Đã tái dựng hai atlas cũ từ nguồn để xác nhận cách xử lý màu/tan: **MAE = 0, sai số tối đa = 0 trên từng pixel của cả 32 khung mỗi bộ** với crop cũ. Vì bản cũ dùng `neutral_fade`, bản mới giữ đúng đường tan đó. Thông số: `crush_black t0=0.02`, `greyCut=0.15`, `whiteFix=off`. Bản mới không cần che mép nguồn vì nguồn còn nguyên và các mép đủ tối.

Nén bằng bộ mã hoá WASM sẵn có của `tools/vfx-flipbook/ktx2/encode.mjs`: **UASTC mức 2, sRGB, Zstd, 12 mức mipmap, Y-flip** như hai KTX2 cũ. Đã giải mã lại bằng `inspect.mjs`, trả Y về hướng PNG trước khi đo.

Script độc lập quét **mọi pixel của mọi khung**: pixel sáng khi `max(R,G,B) > 12`; bề rộng lề là `ceil(10% × kích thước ô)` mỗi cạnh. Từng khung phải có RGB tối đa trong cả bốn dải lề ≤12. Khung hoàn toàn đen được đánh dấu rỗng, không dùng để làm giảm lề nhỏ nhất của khung có hình.

| Clip | Lề cũ nhỏ nhất trái / phải / trên / dưới (px) | Lề mới PNG (px) | Lề KTX2 giải mã (px) | Kết quả |
| --- | --- | --- | --- | --- |
| `thunder-ground-impact` | 6 / 9 / 11 / 10 | **33 / 33 / 36 / 34** | **33 / 33 / 36 / 34** | PASS 32/32; tối thiểu **12,89%** |
| `wood-ring-burst` | 17 / 11 / 11 / 15 | **46 / 41 / 41 / 43** | **46 / 41 / 41 / 43** | PASS 32/32; tối thiểu **12,81%** |
| `thunder-impact` | 10 / 10 / 10 / 10 | Không xuất | Không xuất | Nguồn bị cắt |
| `star-ring-burst` | 13 / 14 / 13 / 15 | Không xuất | Không xuất | Nguồn bị cắt |
| `metal-ring-burst` | 14 / 14 / 15 / 15 | Không xuất | Không xuất | Nguồn bị cắt |

**128 lượt kiểm khung PASS: 64 PNG + 64 KTX2 mức 0.** RGB tối đa trong vùng lề 10% là **0** ở cả hai định dạng của cả hai clip. Sai số nén RGB trung bình lần lượt 0,496 và 0,421 mức trên thang 0–255. Số đo từng khung: `metrics.json`, kiểm độc lập: `final-validation.json` trong thư mục ảnh tạm dưới đây.

## Bỏ qua ba bản -m: chuyển sang làm lại

Đã xem tám khung nguồn mỗi clip và đo ở độ phân giải gốc toàn bộ 32 khung mà JSON cũ lấy. Không dùng việc atlas cũ đã làm mờ mép để coi nguồn còn nguyên.

| Clip | Bằng chứng trên video gốc | Việc cần giao tiếp |
| --- | --- | --- |
| `thunder-impact` | Tia chạy ra ngoài cả bốn cạnh; **32/32** khung được lấy chạm mép. Chỉ số nguồn 21, 23, …, 83; RGB mép tối đa **255** | Làm lại nguồn có đủ đầu tia và lề |
| `star-ring-burst` | Các nhánh tia lớn dần rồi bị cắt; **17/32** khung được lấy chạm mép, chỉ số nguồn 49, 51, …, 81; RGB mép tối đa **255** | Làm lại nguồn, giữ đủ nhánh ở cuối đợt |
| `metal-ring-burst` | Gai/tia và đốm sáng bị cắt ở biên; **19/32** khung được lấy chạm mép, chỉ số nguồn 45, 47, …, 81; RGB mép tối đa **255** | Làm lại nguồn, giữ đủ gai và hạt |

Đây là số đo trên khung nguồn thô trước tail fade. Với hai nguồn cứu được, RGB mép thật tối đa chỉ **3** (`thunder-ground-impact`) và **4** (`wood-ring-burst`) trong 32 khung được lấy. Không đổi khoảng lấy khung để né phần hỏng, vì phiếu yêu cầu giữ số khung và chỉ thu nhỏ hình. Không phát sinh bản -m cho ba bộ mất nội dung, không tự giao việc Firefly ngoài phạm vi.

## Ảnh kiểm và script

Đích được yêu cầu: `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/burst-repack/`.

Thư mục này nằm ngoài `writable_roots` của phiên, nên dùng ngoại lệ đường dẫn tạm của phiếu: **`/private/tmp/414-burst-repack/`**. Chưa ghi vào thư mục review và chưa chạy cập nhật chỉ mục ở đó.

Có **5 ảnh ghép** `<tên clip>-before-after.jpg`, mỗi ảnh **6 cột: ô 0, 6, 12, 18, 24, 31**:

- Hai bộ cứu được: hàng trên bản cũ, hàng dưới bản -m; khung xanh đánh dấu vùng 80% giữa ô.
- Ba bộ không cứu được: hàng trên bản cũ, hàng dưới **video nguồn**, ghi rõ không có bản sau và đánh dấu mép đỏ để thấy phần bị cắt.

Có thêm 5 ảnh `*-source-qa.jpg` đối chiếu tám khung nguồn/atlas. Đã mở xem tất cả ảnh ghép cuối. Mỗi ảnh có mô tả thao tác `.prompt.txt`. `ABOUT.md` ghi mục đích và điều kiện xoá. Không lưu khung thô.

Script và bằng chứng nằm cùng thư mục: `audit.py`, `source-audit.json`, `repack.py`, `check-reconstruction.py`, `reconstruction-check.txt`, `verify-margins.py`, `metrics.json`, `final-validation.json`, `original-sha256.json`. Script repack từ chối ghi đè tệp đã có; script đo chạy lại an toàn, không ghi vào asset:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game
tools/vfx-flipbook/.venv/bin/python -B /private/tmp/414-burst-repack/verify-margins.py
```

Lệnh copy ngoài sandbox, giữ tệp đã có ở đích, rồi cập nhật chỉ mục:

```sh
mkdir -p /Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/burst-repack
cp -Rn /private/tmp/414-burst-repack/. /Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/burst-repack/
cd /Volumes/SS990TPRO/htdocs/typing-game
node scripts/review-index.mjs
```

## Phạm vi và việc owner cần xem

Đã xác nhận **15 tệp gốc (5 × PNG/JSON/KTX2) giữ nguyên SHA-256**. Chỉ ghi 8 tệp mới trong hai thư mục hệ được phép, bổ sung `VFX_LIBRARY.md`, báo cáo này và thư mục tạm. Không sửa code, không chạy build/test game, không ghi media vào Git, không đổi nhánh, không commit/push/reset/clean/stash. Không dùng subagent hoặc gọi dịch vụ tạo ảnh; đây là đóng gói cơ học trên phiếu đã PASS.

Owner/coordinator cần xem hai ảnh trước/sau, chuyển ba clip nguồn bị cắt sang danh sách làm lại, và copy bằng chứng vào thư mục review trước khi dọn `/private/tmp`. Hai bản -m đã đạt phép đo lề; chưa nối vào host hay tuyên bố nghiệm thu hình tổng hợp 8,5. Khi nối lại cần kiểm cỡ hiển thị và pivot do nội dung trong ô đã nhỏ hơn.
