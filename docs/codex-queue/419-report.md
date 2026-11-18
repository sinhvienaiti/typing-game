# Phiếu 419 — cắt bảy clip Firefly thành flipbook -v2

Ngày 16/11/2026. **Hoàn tất 7/7 bộ mới; đạt phép đo lề cho toàn bộ PNG và KTX2 giải mã.** Không ghi đè bản cũ, không sinh nội dung bằng AI.

## Tệp đã làm

Gốc `games/immortality-cultivation/art-src/lab/vfx/`; mỗi bộ dưới đây có `.atlas.png`, `.json`, `.uastc.ktx2`, `.prompt.txt` trong thư mục hệ tương ứng, tổng **28 tệp mới**, khoảng **9,71 MB**. Prompt ghi thao tác, chỉ số khung, crop, mã băm nguồn và prompt Firefly gốc nguyên văn.

| Bộ mới | Nguồn | Lấy khung / phát | Ô | Lề trái / phải / trên / dưới |
| --- | --- | --- | --- | --- |
| `fire-impact-v2` | `fire/firefly-raw/fire-impact.v1-try2.mp4` | 8–70, bước 2; 12 fps | 256 px | 60 / 59 / 48 / 47; **18.36%** |
| `fire-big-burst-v2` | `fire/firefly-raw/fire-big-burst.v2-try1.mp4` | 0–31, bước 1; 24 fps | 256 px | 52 / 41 / 49 / 43; **16.02%** |
| `earth-ring-burst-v2` | `earth/firefly-raw/earth-ring-burst.v2-try1.mp4` | 0–62, bước 2; 12 fps | 320 px | 64 / 65 / 56 / 52; **16.25%** |
| `metal-impact-v2` | `metal/firefly-raw/metal-impact.v2-try1.mp4` | 0–62, bước 2; 12 fps | 256 px | 37 / 46 / 53 / 53; **14.45%** |
| `metal-big-burst-v2` | `metal/firefly-raw/metal-big-burst.v2-try1.mp4` | 0–31, bước 1; 24 fps | 256 px | 39 / 39 / 39 / 39; **15.23%** |
| `void-big-burst-v2` | `void/firefly-raw/void-big-burst.v2-try1.mp4` | 0–31, bước 1; 24 fps | 256 px | 39 / 39 / 38 / 38; **14.84%** |
| `wind-ring-burst-v2` | `wind/firefly-raw/wind-ring-burst.v2-try2.mp4` | 0–31, bước 1; 24 fps | 320 px | 56 / 53 / 47 / 47; **14.69%** |

Đã bổ sung mục **Bảy clip bùng nổ Firefly mới — phiếu 419** vào [`VFX_LIBRARY.md`](../games/tu-tien/skills/VFX_LIBRARY.md).

## Cách cắt và kiểm

Đọc cấu hình `tools/vfx-flipbook/immortality-cultivation.json`, dùng trực tiếp hàm giải mã, xử lý màu, đóng atlas và mã hoá KTX2 của công cụ; script điều phối nằm trong thư mục tạm, không sửa công cụ. Nguồn đều 1080×1080, 24 fps, 121 khung. Đã xem bảng nguồn 12 khung mỗi clip và bảy ảnh đối chiếu cuối.

- 32 khung/bộ, lưới 8×4; ô impact/big-burst 256 px, ring-burst 320 px. RGB additive, không premultiply, không loop.
- Chỉ chọn đoạn trước mép nguồn: RGB mép thật tối đa **2–4/255** trong mọi khung đã chọn. Lần đầu nội dung >12 chạm mép nguồn: Hỏa impact 95, Hỏa lớn 47, Thổ vòng 74, Kim lớn 57, Hư Không lớn 42, Gió vòng 53; impact Kim không chạm trong toàn clip. Không thu nhỏ phần hình đã bị cắt.
- Hỏa impact lấy 0,333–2,917 s, trong khoảng ~3 s đầu. Thổ vòng và impact Kim lấy 0–2,583 s. Bốn bộ còn lại lấy 0–1,292 s. Thời lượng phát lần lượt 2,667 s ở 12 fps hoặc 1,333 s ở 24 fps; không giãn thời gian bằng lặp khung.
- Một crop vuông chung cho cả đoạn, thêm nền đen khi cần; neo tại tâm nguồn, pivot `[0.5,0.5]`. Không vignette, không che hoặc làm mờ mép để đạt số đo. Các crop chính xác có trong JSON, prompt và `metrics.json`.
- `crush_black t0=0.02`, `greyCut=0.15`, `whiteFix=off`; đường tan `neutral_fade` smoothstep trên 10 khung cuối. Khung cuối cả bảy PNG là RGB **0**.
- JSON có đúng tập khoá cấp gốc và khoá con `source`/`trim` của atlas cùng loại. Giữ đầy đủ metadata; cập nhật nguồn, chỉ số khung, fps, crop, pivot, version/id/image. Ba bộ chưa có atlas cũ đúng tên dùng schema impact cùng hệ: `fire-ground-impact` và `metal-ground-impact`.
- UASTC mức 2, sRGB, Zstd, Y-flip, **12 mức mipmap**; đã giải mã lại bằng `inspect.mjs` và trả Y về hướng PNG trước khi đo.

Script độc lập kiểm **448 lượt khung = 7 × 32 × 2 định dạng**. Pixel có hình khi `max(R,G,B)>12`; từng cạnh phải có lề ít nhất `ceil(10% × ô)` (26 px hoặc 32 px). Bảng trên ghi lề nhỏ nhất qua mọi khung có hình; kết quả PNG và KTX2 giống nhau. Toàn dải lề 10% ở cả hai định dạng của cả bảy bộ có RGB tối đa **0**. Sai số nén RGB trung bình nằm trong **0,158–0,555/255**. Xác nhận SHA-256 của **28 tệp nguồn/bản cũ giữ nguyên**.

Lệnh chạy lại phép kiểm, không sửa asset:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game
tools/vfx-flipbook/.venv/bin/python -B /private/tmp/419-burst-v2/verify.py
```

## Ảnh và bằng chứng

Đích yêu cầu `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/burst-v2/` nằm ngoài quyền ghi của phiên. Theo ngoại lệ trong phiếu, tất cả bằng chứng ở **`/private/tmp/419-burst-v2/`**, có `ABOUT.md`.

- **7 ảnh** `<clip>-before-after.jpg`: mỗi ảnh tám cặp khung **cũ | v2**, mốc v2 0, 4, 8, 13, 18, 23, 27, 31; bộ cũ lấy cùng phần trăm thời lượng. Khung xanh chỉ vùng trong lề 10%; font Arial theo yêu cầu.
- `fire-impact` và `fire-big-burst` chưa có atlas cũ cùng tên, nên ảnh ghi rõ đối chiếu với **`fire-burst`**, không gọi đó là tiền nhiệm đúng tên. `metal-impact` đối chiếu **`metal-ground-impact`**. Bốn bộ khác đối chiếu đúng tên cũ.
- **7 ảnh nguồn** `<clip>-source-qa.jpg`, 12 mốc/clip; script `audit.py`, `package.py`, `verify.py`; số đo `source-audit.json`, `metrics.json`, `final-validation.json`; mã băm cũ `original-sha256.json`. Ảnh ghép có `.prompt.txt` mô tả phép ghép; không tạo ảnh AI.
- Không lưu khung thô. Công cụ prune chạy thử từ chối thư mục tạm vì `outside-roots`; không có ảnh thô nào cần xoá. Đã dọn bản atlas đóng gói trùng ở vùng staging, chỉ giữ asset chính và bằng chứng.

Lệnh chuyển bằng chứng khi chạy ngoài sandbox, giữ file đã có rồi cập nhật chỉ mục:

```sh
mkdir -p /Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/burst-v2
cp -Rn /private/tmp/419-burst-v2/. /Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/burst-v2/
cd /Volumes/SS990TPRO/htdocs/typing-game
node scripts/review-index.mjs
```

## Bỏ qua và việc owner cần xem

**Không bỏ clip nào.** Chưa ghi vào review SSD hoặc cập nhật chỉ mục ở đó do giới hạn quyền ghi; đã dùng đúng fallback được phép. Không sửa code/manifest, không nối runtime, không chạy build/test game; không đổi nhánh, không commit/push/reset/clean/stash, không đưa media vào Git. Quota đọc từ phiên mới nhất còn 25%; không dùng subagent hay gọi công cụ tạo nội dung.

Owner/coordinator cần xem **bảy ảnh so sánh**, đặc biệt Gió bắt đầu đã lớn và bốn đoạn phát 24 fps ngắn hơn bộ cũ. Ba tên thiếu tiền nhiệm được ghi rõ trên ảnh. Khi nối vào host, đọc fps/pivot mới và kiểm cỡ, điểm chạm/góc nhìn. Phép đo này chỉ nghiệm thu đóng gói nguồn; chưa chấm hiệu ứng tổng hợp 8,5 trong game.
